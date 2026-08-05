#!/usr/bin/env python3
"""
Adversarial self-audit. Assumes a hostile expert reviewer.

Implements the Phase 5 checks that can be mechanised. The ones that cannot
(re-reading a source to confirm it says what the node claims) are set up here as
a reproducible SAMPLE so the manual pass is honest and repeatable.

  --sample N       draw N random claims (seeded) with their sources, for manual
                   re-verification against the primary. Prints a checklist.
  --species        find claims where mouse/animal data may be stated as human fact:
                     * human_evidence: direct but species_basis excludes human
                     * summary asserts human anatomy/physiology while species_basis
                       is animal-only and translation_risk is low
                     * translation_risk: low on an animal-only node
  --hedging        find summaries that hedge instead of resolving ("may", "might",
                   "could", "suggests", "remains unclear", "further research")
                   - banned as a conclusion per the atlas standard
  --xgrade         list every X-grade node/edge (untraceable to primary data) and
                   check each is logged in audit/contradictions.md
  --gapcheck       verify no gap is manufactured: every search_established gap has
                   a search log with a real query string and a hit count
  --unsourced      quantitative rows with value_unverified, or a source that is
                   abstract-only, or no uncertainty stated
  --all            run every mechanised check

Usage:
  python3 atlas/tools/redteam.py --all
  python3 atlas/tools/redteam.py --sample 30 --seed 7 > atlas/audit/sample_30.md
"""
import os, sys, glob, re, argparse, random, json
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEDGE = re.compile(
    r"\b(may |might |could |possibly|perhaps|it is thought|it is believed|"
    r"suggests that|appears to|seems to|remains unclear|remains to be|"
    r"further (research|study|studies|work) (is|are) needed|not fully understood|"
    r"poorly understood|is complex)\b", re.I)

# phrases asserting a human fact
HUMAN_ASSERT = re.compile(
    r"\b(in humans?|human (growth plate|physis|chondrocyte|cartilage|children)|"
    r"in (children|adolescents|patients)|clinical)\b", re.I)

ANIMAL = {"mouse", "rat", "rabbit", "bovine", "porcine", "ovine", "chicken",
          "zebrafish", "xenopus", "in_vitro_animal_cell"}


def load_nodes():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"), recursive=True):
        with open(p) as f:
            n = yaml.safe_load(f) or {}
        if isinstance(n, dict) and n.get("id"):
            n["__path"] = os.path.relpath(p, ROOT)
            out[n["id"]] = n
    return out


def load(p, d=None):
    if not os.path.exists(p):
        return d
    with open(p) as f:
        return yaml.safe_load(f) or d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--species", action="store_true")
    ap.add_argument("--hedging", action="store_true")
    ap.add_argument("--xgrade", action="store_true")
    ap.add_argument("--gapcheck", action="store_true")
    ap.add_argument("--unsourced", action="store_true")
    ap.add_argument("--provenance", action="store_true")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    if a.all:
        a.species = a.hedging = a.xgrade = a.gapcheck = a.unsourced = True
        a.provenance = True

    nodes = load_nodes()
    full = {k: v for k, v in nodes.items() if not v.get("stub")}
    edges = (load(os.path.join(ROOT, "edges", "edges.yaml"), {}) or {}).get("edges", [])
    gaps = (load(os.path.join(ROOT, "gaps", "gaps.yaml"), {}) or {}).get("gaps", [])
    slogs = (load(os.path.join(ROOT, "gaps", "search_log.yaml"), {}) or {}).get("searches", [])
    refs = (load(os.path.join(ROOT, "sources", "bibliography.yaml"), {}) or {}).get("refs", {})
    findings = 0

    if a.sample:
        random.seed(a.seed)
        pool = []
        for nid, n in full.items():
            for q in (n.get("quantitative") or []):
                pool.append(("quant", nid, q.get("parameter"),
                             f"{q.get('value')} {q.get('unit')}", q.get("source_ref")))
            for kr in (n.get("key_refs") or []):
                pool.append(("finding", nid, kr.get("ref_id"),
                             kr.get("one_line_finding"), kr.get("ref_id")))
        for e in edges:
            pool.append(("edge", e.get("edge_id"),
                         f"{e.get('source')} -{e.get('relation')}-> {e.get('target')}",
                         e.get("context"), ",".join(e.get("refs") or [])))
        k = min(a.sample, len(pool))
        print(f"# Redteam claim sample (n={k}, seed={a.seed})\n")
        print("Re-verify each against the PRIMARY source. Mark PASS/FAIL/UNCHECKABLE.")
        print("Target: <5% error rate, else fix and re-sample.\n")
        print("| # | kind | node/edge | claim | source | verdict | note |")
        print("|---|------|-----------|-------|--------|---------|------|")
        for i, (kind, nid, what, val, src) in enumerate(random.sample(pool, k), 1):
            r = refs.get(src, {}) if isinstance(src, str) else {}
            cite = f"{r.get('first_author','?')} {r.get('year','?')}" if r else (src or "-")
            sw = str(what)[:44].replace("|", "/")
            sv = str(val)[:52].replace("|", "/")
            print(f"| {i} | {kind} | `{nid}` | {sw} = {sv} | {cite} | | |")
        print(f"\n_pool size {len(pool)}_")
        return 0

    if a.species:
        print("=== SPECIES LAUNDERING CHECK ===")
        for nid, n in sorted(full.items()):
            sb = set(n.get("species_basis") or [])
            he, tr = n.get("human_evidence"), n.get("translation_risk")
            animal_only = sb and sb.issubset(ANIMAL)
            if he == "direct" and "human" not in sb:
                print(f"  ✗ {nid}: human_evidence=direct but species_basis={sorted(sb)}")
                findings += 1
            if animal_only and tr == "low":
                print(f"  ✗ {nid}: animal-only basis {sorted(sb)} but translation_risk=low")
                findings += 1
            if animal_only and HUMAN_ASSERT.search(str(n.get("summary") or "")):
                m = HUMAN_ASSERT.search(str(n.get("summary")))
                print(f"  ! {nid}: animal-only basis but summary asserts human "
                      f"context ('{m.group(0)}') - confirm it is explicitly flagged")
                findings += 1
        print(f"  ({findings} flags)\n")

    if a.hedging:
        print("=== HEDGING CHECK (banned as a conclusion) ===")
        h = 0
        for nid, n in sorted(full.items()):
            for m in HEDGE.finditer(str(n.get("summary") or "")):
                print(f"  ! {nid}: '{m.group(0).strip()}'")
                h += 1
        print(f"  ({h} hedges - each must be resolved or converted to a gap entry)\n")
        findings += h

    if a.xgrade:
        print("=== X-GRADE CLAIMS (untraceable to primary data) ===")
        cpath = os.path.join(ROOT, "audit", "contradictions.md")
        ctxt = open(cpath).read() if os.path.exists(cpath) else ""
        xs = [nid for nid, n in full.items() if n.get("confidence") == "X"]
        xe = [e.get("edge_id") for e in edges if e.get("confidence") == "X"]
        for nid in xs:
            ok = nid in ctxt
            print(f"  {'✓' if ok else '✗'} node {nid}"
                  f"{'' if ok else '  <- NOT logged in audit/contradictions.md'}")
            findings += 0 if ok else 1
        for eid in xe:
            print(f"  · edge {eid}")
        if not xs and not xe:
            print("  none yet (expect these to appear as layers are researched)")
        print()

    if a.gapcheck:
        print("=== GAP ADMISSIBILITY (is any gap manufactured?) ===")
        logged = {s.get("gap_id"): s for s in slogs}
        bad = 0
        for g in gaps:
            gid, t = g.get("gap_id"), g.get("type")
            if t == "search_established":
                s = logged.get(gid)
                if not s:
                    print(f"  ✗ {gid}: search_established with NO search log")
                    bad += 1
                    continue
                if not s.get("exact_query_string") or len(str(s["exact_query_string"])) < 15:
                    print(f"  ✗ {gid}: query string too vague to reproduce")
                    bad += 1
                if s.get("hit_count") is None:
                    print(f"  ✗ {gid}: no hit_count")
                    bad += 1
                if s.get("hit_count", 0) > 0 and not s.get("reason_none_qualified"):
                    print(f"  ✗ {gid}: {s['hit_count']} hits but no reason none qualified")
                    bad += 1
            de = str(g.get("discriminating_experiment") or "")
            if len(de) < 120:
                print(f"  ! {gid}: discriminating_experiment is thin ({len(de)} chars) "
                      f"- must name model system, readout, and expected result per hypothesis")
                bad += 1
            if re.search(r"more research is needed|further study", de, re.I):
                print(f"  ✗ {gid}: discriminating_experiment contains banned filler")
                bad += 1
        print(f"  ({bad} problems across {len(gaps)} gaps)\n")
        findings += bad

    if a.unsourced:
        print("=== WEAK QUANTITATIVE ROWS ===")
        w = 0
        for nid, n in sorted(full.items()):
            for q in (n.get("quantitative") or []):
                if q.get("value_unverified"):
                    print(f"  ! {nid}: '{q.get('parameter')}' value_unverified")
                    w += 1
                u = str(q.get("uncertainty") or "")
                if not u or u.lower() in ("none", "-"):
                    print(f"  ! {nid}: '{q.get('parameter')}' no uncertainty stated")
                    w += 1
                src = refs.get(q.get("source_ref"), {})
                if src.get("type") == "primary_abstract_only":
                    print(f"  ! {nid}: '{q.get('parameter')}' sourced from an "
                          f"ABSTRACT ONLY ({q.get('source_ref')})")
                    w += 1
        print(f"  ({w} weak rows)\n")

    if a.provenance:
        print("=== REFERENCE PROVENANCE (anti-fabrication) ===")
        SIG = {"open_access", "has_full_text", "cited_by", "added", "is_preprint"}
        allrefs = dict(refs)
        for sp in glob.glob(os.path.join(ROOT, "sources", "shards", "*.yaml")):
            allrefs.update((load(sp, {}) or {}).get("refs", {}) or {})
        machine = manual = 0
        hand = []
        for k, v in allrefs.items():
            if not isinstance(v, dict):
                continue
            if v.get("verify_by_hand"):
                manual += 1
            elif SIG & set(v.keys()):
                machine += 1
            else:
                hand.append(k)
        print(f"  machine-populated by addref.py from a live record : {machine}")
        print(f"  manual / non-indexed, flagged verify_by_hand      : {manual}")
        print(f"  HAND-WRITTEN with no machine signature            : {len(hand)}")
        for k in hand[:20]:
            print(f"    x {k}  <- provenance unverifiable, re-add via addref.py")
        findings += len(hand)
        print()

    print(f"TOTAL MECHANISED FINDINGS: {findings}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
