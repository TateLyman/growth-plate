#!/usr/bin/env python3
"""
Structural validator for the Human Growth System Atlas.

Enforces, without touching the network:
  - node files parse, have required fields, use only controlled-vocabulary values
  - node id matches filename stem and is globally unique
  - node layer matches the directory it lives in
  - every edge endpoint resolves to a real node
  - hypothesized_link / speculative edges carry a gap_id that exists
  - every ref_id cited by a node or edge exists in sources/bibliography.yaml
  - every gap_id referenced exists; search_established gaps have a search log entry
  - gap quota per layer (>=8 gaps, >=3 of type search_established|quantitative_gap)

Network verification of PMIDs/DOIs is a separate tool: verify_refs.py

Usage:
  python3 atlas/tools/validate.py            # full check, human-readable
  python3 atlas/tools/validate.py --json     # machine-readable
  python3 atlas/tools/validate.py --quota    # include per-layer gap quota check
"""
import sys, os, json, glob, argparse
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # -> atlas/

REQUIRED_ALWAYS = ["id", "name", "type", "layer", "human_evidence", "last_verified"]
REQUIRED_FULL = ["summary", "human_evidence_note", "species_basis",
                 "translation_risk", "translation_risk_reason", "confidence", "key_refs"]
EDGE_REQUIRED = ["edge_id", "source", "target", "relation", "context",
                 "evidence_tier", "refs", "confidence"]
GAP_REQUIRED = ["gap_id", "question", "type", "layer", "why_it_matters",
                "what_is_known", "what_is_missing", "discriminating_experiment"]

GAP_QUOTA_MIN = 8
GAP_QUOTA_HARD_TYPES = {"search_established", "quantitative_gap"}
GAP_QUOTA_HARD_MIN = 3


class _DupKeyLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys.

    PyYAML silently keeps the LAST of a repeated key, so a second entry for an
    existing ref_id or gap_id parses cleanly and overwrites the first with no
    error anywhere. That is how a bibliography entry was silently rebound
    (CORR-025) and how two refs were duplicated with the originals' citation
    counts discarded (CORR-033). Duplicate keys are now a hard error.
    """


def _no_duplicate_keys(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"duplicate key {key!r} - PyYAML would silently keep the last one",
                key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_DupKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicate_keys)


def load(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path) as f:
        return yaml.load(f, Loader=_DupKeyLoader) or default


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []
        self.stats = {}

    def err(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def validate(quota=False):
    r = Report()
    vocab = load(os.path.join(ROOT, "schema", "vocab.yaml"))
    if not vocab:
        r.err("schema/vocab.yaml", "missing or unparseable - cannot validate")
        return r, {}, {}

    node_types = set(vocab["node_types"])
    layers = set(vocab["layers"].keys())
    relations = set(vocab["relations"])
    signs = set(str(s) for s in vocab["signs"])
    conf_ok = set(vocab["confidence"].keys())
    tiers = set(vocab["evidence_tier"].keys())
    ref_types = set(vocab["ref_types"])
    gap_types = set(vocab["gap_types"])
    he_ok = set(vocab["human_evidence"])
    tr_ok = set(vocab["translation_risk"])

    # ---- bibliography ----
    bib = load(os.path.join(ROOT, "sources", "bibliography.yaml"), {}) or {}
    refs = bib.get("refs", {}) if isinstance(bib, dict) else {}
    if isinstance(refs, list):  # tolerate list form
        refs = {x["ref_id"]: x for x in refs}
    known_refs = set(refs.keys())
    for rid, rv in refs.items():
        if not isinstance(rv, dict):
            r.err(f"bibliography/{rid}", "entry is not a mapping")
            continue
        if not (rv.get("pmid") or rv.get("doi") or rv.get("url") or rv.get("accession")):
            r.err(f"bibliography/{rid}", "no pmid, doi, url, or accession - unresolvable")
        if rv.get("type") and rv["type"] not in ref_types:
            r.err(f"bibliography/{rid}", f"bad ref type '{rv['type']}'")

    # ---- gaps ----
    gapdoc = load(os.path.join(ROOT, "gaps", "gaps.yaml"), {}) or {}
    gaps = gapdoc.get("gaps", []) if isinstance(gapdoc, dict) else (gapdoc or [])
    known_gaps, gaps_by_layer = set(), {}
    for g in gaps:
        gid = g.get("gap_id", "<no id>")
        if gid in known_gaps:
            r.err(f"gaps/{gid}", "duplicate gap_id")
        known_gaps.add(gid)
        for f in GAP_REQUIRED:
            if not g.get(f):
                r.err(f"gaps/{gid}", f"missing required field '{f}'")
        if g.get("type") not in gap_types:
            r.err(f"gaps/{gid}", f"bad gap type '{g.get('type')}'")
        if g.get("layer") not in layers:
            r.err(f"gaps/{gid}", f"bad layer '{g.get('layer')}'")
        for rid in (g.get("nearest_evidence") or []):
            if rid not in known_refs:
                r.err(f"gaps/{gid}", f"nearest_evidence cites unknown ref '{rid}'")
        gaps_by_layer.setdefault(g.get("layer"), []).append(g)

    slogdoc = load(os.path.join(ROOT, "gaps", "search_log.yaml"), {}) or {}
    slogs = slogdoc.get("searches", []) if isinstance(slogdoc, dict) else (slogdoc or [])
    logged = {s.get("gap_id") for s in slogs}
    for s in slogs:
        for f in ["gap_id", "database", "exact_query_string", "date_run", "hit_count"]:
            if s.get(f) is None:
                r.err(f"search_log/{s.get('gap_id')}", f"missing '{f}'")
    for g in gaps:
        if g.get("type") == "search_established" and g.get("gap_id") not in logged:
            r.err(f"gaps/{g.get('gap_id')}",
                  "type=search_established but no entry in gaps/search_log.yaml - INADMISSIBLE")

    # ---- nodes ----
    nodes, seen_ids = {}, {}
    for path in sorted(glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"), recursive=True)):
        rel = os.path.relpath(path, ROOT)
        try:
            n = load(path)
        except Exception as e:
            r.err(rel, f"YAML parse error: {e}")
            continue
        if not isinstance(n, dict):
            r.err(rel, "file is not a YAML mapping")
            continue
        stem = os.path.splitext(os.path.basename(path))[0]
        nid = n.get("id")
        if nid != stem:
            r.err(rel, f"id '{nid}' does not match filename stem '{stem}'")
        if nid in seen_ids:
            r.err(rel, f"duplicate node id '{nid}' (also {seen_ids[nid]})")
        seen_ids[nid] = rel
        nodes[nid] = n

        for f in REQUIRED_ALWAYS:
            if not n.get(f):
                r.err(rel, f"missing required field '{f}'")
        if n.get("type") not in node_types:
            r.err(rel, f"bad node type '{n.get('type')}'")
        if n.get("layer") not in layers:
            r.err(rel, f"bad layer '{n.get('layer')}'")
        else:
            dirlayer = os.path.basename(os.path.dirname(path)).split("_")[0]
            if dirlayer != n.get("layer"):
                r.err(rel, f"layer '{n.get('layer')}' but lives in directory for '{dirlayer}'")
        if n.get("human_evidence") not in he_ok:
            r.err(rel, f"bad human_evidence '{n.get('human_evidence')}'")

        if not n.get("stub"):
            for f in REQUIRED_FULL:
                if not n.get(f):
                    r.err(rel, f"missing required field '{f}' (non-stub node)")
            if n.get("confidence") not in conf_ok:
                r.err(rel, f"bad confidence '{n.get('confidence')}'")
            if n.get("translation_risk") not in tr_ok:
                r.err(rel, f"bad translation_risk '{n.get('translation_risk')}'")
            for kr in (n.get("key_refs") or []):
                if not isinstance(kr, dict):
                    r.err(rel, "key_refs entry is not a mapping")
                    continue
                rid = kr.get("ref_id")
                if not rid:
                    r.err(rel, "key_refs entry missing ref_id")
                elif rid not in known_refs:
                    r.err(rel, f"key_ref '{rid}' not in bibliography.yaml")
                if kr.get("type") and kr["type"] not in ref_types:
                    r.err(rel, f"key_ref '{rid}' bad type '{kr.get('type')}'")
                # CITATION INTEGRITY: the node states a pmid alongside the ref_id.
                # If it disagrees with the bibliography entry that ref_id points at,
                # the citation is pointing at the wrong paper. This catches the
                # merge-rewrite corruption class, which is otherwise silent because
                # every id still resolves.
                # A withdrawn or retracted source is the one defect that gets WORSE with
                # time: the paper stays resolvable, the PMID stays valid, addref.py stays
                # happy, and the claim quietly keeps circulating. Caught 2026-08-05 when a
                # full verify_refs run flagged wu2013, withdrawn by J Biol Chem in 2020 and
                # cited on a node, three edges and three gaps. An ERROR, not a warning: a
                # node may keep the reference (flagged) but must declare it.
                if rid in refs and refs[rid].get("retracted") and not kr.get("retracted"):
                    r.err(rel, f"key_ref '{rid}' is RETRACTED/WITHDRAWN in bibliography.yaml "
                               f"but this node does not declare it - add 'retracted: true' "
                               f"to the key_ref and record the disposition in "
                               f"audit/corrections.md")
                npm = str(kr.get("pmid") or "").strip()
                if rid in refs and npm:
                    bpm = str(refs[rid].get("pmid") or "").strip()
                    if bpm and npm != bpm:
                        r.err(rel, f"CITATION MISMATCH: key_ref '{rid}' declares pmid "
                                   f"{npm} but bibliography[{rid}] has pmid {bpm} "
                                   f"- citation points at the wrong paper")
                if not kr.get("one_line_finding"):
                    r.warn(rel, f"key_ref '{rid}' has no one_line_finding")

        for q in (n.get("quantitative") or []):
            if not isinstance(q, dict):
                r.err(rel, "quantitative entry is not a mapping")
                continue
            for f in ["parameter", "value", "unit", "species", "source_ref"]:
                if q.get(f) in (None, ""):
                    r.err(rel, f"quantitative '{q.get('parameter')}' missing '{f}'")
            if q.get("source_ref") and q["source_ref"] not in known_refs:
                r.err(rel, f"quantitative '{q.get('parameter')}' cites unknown ref "
                           f"'{q['source_ref']}'")
            if q.get("species") and q["species"] not in set(vocab["species"]):
                r.err(rel, f"quantitative '{q.get('parameter')}' bad species '{q['species']}'")

        for gid in (n.get("open_questions") or []):
            if gid not in known_gaps:
                r.err(rel, f"open_questions references unknown gap '{gid}'")

    # ---- edges ----
    edoc = load(os.path.join(ROOT, "edges", "edges.yaml"), {}) or {}
    edges = edoc.get("edges", []) if isinstance(edoc, dict) else (edoc or [])
    seen_edge = set()
    for e in edges:
        eid = e.get("edge_id", "<no id>")
        where = f"edges/{eid}"
        if eid in seen_edge:
            r.err(where, "duplicate edge_id")
        seen_edge.add(eid)
        for f in EDGE_REQUIRED:
            if e.get(f) in (None, "", []):
                r.err(where, f"missing required field '{f}'")
        if e.get("source") not in nodes:
            r.err(where, f"source node '{e.get('source')}' does not exist")
        if e.get("target") not in nodes:
            r.err(where, f"target node '{e.get('target')}' does not exist")
        if e.get("relation") not in relations:
            r.err(where, f"bad relation '{e.get('relation')}'")
        if e.get("sign") is not None and str(e.get("sign")) not in signs:
            r.err(where, f"bad sign '{e.get('sign')}'")
        if e.get("confidence") not in conf_ok:
            r.err(where, f"bad confidence '{e.get('confidence')}'")
        if e.get("evidence_tier") not in tiers:
            r.err(where, f"bad evidence_tier '{e.get('evidence_tier')}'")
        for rid in (e.get("refs") or []):
            if rid not in known_refs:
                r.err(where, f"cites unknown ref '{rid}'")
        needs_gap = (e.get("relation") == "hypothesized_link"
                     or e.get("confidence") == "speculative")
        if needs_gap:
            if not e.get("gap_id"):
                r.err(where, "hypothesized_link/speculative edge requires a gap_id")
            elif e["gap_id"] not in known_gaps:
                r.err(where, f"gap_id '{e['gap_id']}' does not exist")
        if e.get("relation") == "hypothesized_link" and e.get("confidence") != "speculative":
            r.err(where, "hypothesized_link must carry confidence: speculative")

    # ---- orphans ----
    linked = set()
    for e in edges:
        linked.add(e.get("source")); linked.add(e.get("target"))
    orphans = [n for n in nodes if n not in linked and not nodes[n].get("stub")]

    # ---- held-but-unread (CORR-035) ----
    # `in_epmc` (formerly misnamed has_full_text) is Europe PMC metadata and says
    # nothing about what this atlas possesses. `local_pdf` says the file is on disk.
    # A reference whose PDF is HELD, whose type is still primary_abstract_only, and
    # which a node cites, is a claim resting on an abstract that could be resolved by
    # opening a file already in hand. That is exactly the schrier2006 failure: its
    # oestrogen arm - a null against one of this atlas's load-bearing claims - sat
    # unread on disk for two days while five nodes cited the paper.
    cited_refs = set()
    for nid, n in nodes.items():
        for kr in (n.get("key_refs") or []):
            if isinstance(kr, dict) and kr.get("ref_id"):
                cited_refs.add(kr["ref_id"])
        for q in (n.get("quantitative") or []):
            if isinstance(q, dict) and q.get("source_ref"):
                cited_refs.add(q["source_ref"])
    # A record that says its full text was read while still typed abstract-only is
    # SELF-CONTRADICTORY, and that is an error rather than a warning. glasson2005 sat in
    # exactly that state - full_text_read 2026-08-06, type primary_abstract_only - while a
    # node cited it from an abstract that states the OPPOSITE of its growth-plate result.
    # Nothing detected it, because no check compared the two fields (CORR-037).
    for rid, rv in sorted(refs.items()):
        if not isinstance(rv, dict):
            continue
        if (rv.get("full_text_read") or rv.get("access_route")) and \
                rv.get("type") == "primary_abstract_only":
            r.err(f"bibliography/{rid}",
                  "full_text_read/access_route is set but type is still "
                  "primary_abstract_only - the record contradicts itself")

    # ---- the same paper held twice under two ref_ids (CORR-047) ----
    # The duplicate-key loader catches the same KEY twice. It cannot catch the same
    # PAPER under two different keys, and nine of them had accumulated: one entry
    # minted by addref.py in author-year form (hartmann2025, nadeau2026, starrett2025)
    # and one hand-authored in descriptive form (erdaseries2025, nadeaunguyen2026,
    # tyra300_2025). The harm is not untidiness. A duplicate is a SECOND VOTE FOR THE
    # SAME EVIDENCE: two nodes citing the two aliases look like independent corroboration
    # and are one paper. It also splits the record - cnpmeta2026 was tier T2 and read,
    # kamrulhasan2026 was tier T4 and unread, for the identical meta-analysis, so the
    # atlas held two incompatible gradings of one source and could not see the conflict.
    for field in ("pmid", "doi"):
        seen = {}
        for rid, rv in sorted(refs.items()):
            if not isinstance(rv, dict):
                continue
            val = rv.get(field)
            if not val:
                continue
            key = str(val).strip().lower()
            if key in seen:
                r.err("bibliography/duplicate",
                      f"'{rid}' and '{seen[key]}' are the same paper "
                      f"({field} {key}) held under two ref_ids - merge them; a "
                      f"duplicate double-counts one source as two")
            else:
                seen[key] = rid

    for rid in sorted(cited_refs):
        rv = refs.get(rid) or {}
        if rv.get("local_pdf") and rv.get("type") == "primary_abstract_only":
            r.warn(f"held_but_unread/{rid}",
                   "PDF is on disk (local_pdf) but type is still primary_abstract_only "
                   "and nodes cite it - read the full text or drop the citation")

    # ---- quota ----
    if quota:
        for L in sorted(layers, key=lambda x: int(x[1:])):
            gl = gaps_by_layer.get(L, [])
            hard = [g for g in gl if g.get("type") in GAP_QUOTA_HARD_TYPES]
            if len(gl) < GAP_QUOTA_MIN:
                r.err(f"quota/{L}", f"{len(gl)}/{GAP_QUOTA_MIN} gaps")
            if len(hard) < GAP_QUOTA_HARD_MIN:
                r.err(f"quota/{L}",
                      f"{len(hard)}/{GAP_QUOTA_HARD_MIN} search_established|quantitative_gap")

    # ---- stats ----
    by_layer, by_conf, stubs = {}, {}, 0
    for nid, n in nodes.items():
        by_layer[n.get("layer")] = by_layer.get(n.get("layer"), 0) + 1
        if n.get("stub"):
            stubs += 1
        else:
            by_conf[n.get("confidence")] = by_conf.get(n.get("confidence"), 0) + 1
    r.stats = {
        "nodes": len(nodes), "stubs": stubs, "full_nodes": len(nodes) - stubs,
        "edges": len(edges), "gaps": len(gaps), "search_logs": len(slogs),
        "refs": len(known_refs), "orphan_nonstub_nodes": len(orphans),
        "nodes_by_layer": dict(sorted(by_layer.items(), key=lambda x: int(x[0][1:]))),
        "confidence_distribution": dict(sorted(by_conf.items())),
        "gaps_by_layer": {k: len(v) for k, v in sorted(
            gaps_by_layer.items(), key=lambda x: int(x[0][1:]) if x[0] else 99)},
    }
    return r, nodes, orphans


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quota", action="store_true")
    a = ap.parse_args()
    r, nodes, orphans = validate(quota=a.quota)
    if a.json:
        print(json.dumps({"errors": r.errors, "warnings": r.warnings,
                          "stats": r.stats, "orphans": orphans}, indent=2))
    else:
        print("=" * 70)
        print("HUMAN GROWTH SYSTEM ATLAS - structural validation")
        print("=" * 70)
        for k, v in r.stats.items():
            print(f"  {k:28s} {v}")
        print("-" * 70)
        if r.errors:
            print(f"ERRORS ({len(r.errors)}):")
            for e in r.errors[:80]:
                print("  ✗ " + e)
            if len(r.errors) > 80:
                print(f"  ... and {len(r.errors) - 80} more")
        else:
            print("ERRORS: none")
        if r.warnings:
            print(f"WARNINGS ({len(r.warnings)}): showing first 20")
            for w in r.warnings[:20]:
                print("  ! " + w)
        if orphans:
            print(f"ORPHAN non-stub nodes ({len(orphans)}): {orphans[:15]}")
    return 1 if r.errors else 0


if __name__ == "__main__":
    sys.exit(main())
