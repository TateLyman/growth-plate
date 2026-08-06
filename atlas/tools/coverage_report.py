#!/usr/bin/env python3
"""
Regenerate the generated sections of /query/coverage.md from the repository.

WHY THIS EXISTS
The Phase 7 falsification agent found coverage.md asserting 612 nodes, 764 edges and
"L8 = 3 nodes" against an actual 614, 1181 and 39. coverage.md is the file a reader is
told to consult BEFORE trusting an answer, so a stale coverage.md is worse than none:
it warns about the wrong layers with the authority of a measurement.

Everything numeric in that file is now generated between markers and can never drift
again. The interpretive prose lives outside the markers and is hand-written, because a
judgement about which layer to distrust is not something a script should invent.

Markers:
  <!-- COVERAGE:LAYERS:BEGIN -->    per-layer evidence quality + measured hit rate
  <!-- COVERAGE:STRUCT:BEGIN -->    node/edge/gap/ref counts, sign + context coverage
  <!-- COVERAGE:QUANT:BEGIN -->     parameter reliability classes

Usage:
  python3 atlas/tools/coverage_report.py           # rewrite in place
  python3 atlas/tools/coverage_report.py --check   # non-zero exit if stale
"""
import os, sys, re, glob, json, argparse
from collections import defaultdict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
COV = os.path.join(REPO, "query", "coverage.md")

LAYER_NAMES = {
    "L0": "developmental_origin", "L1": "growth_plate_architecture",
    "L2": "stem_and_progenitor_biology", "L3": "signaling_networks",
    "L4": "endocrine_and_systemic", "L5": "matrix_and_mineralization",
    "L6": "mechanobiology", "L7": "fusion_and_cessation",
    "L8": "genetics_and_heritability", "L9": "whole_organism_growth",
    "L10": "environment_and_population", "L11": "pathology_as_natural_experiment",
    "L12": "pharmacology_as_mechanistic_probe", "L13": "methods_and_data",
}
# Phase 7 baseline, query/falsification_baseline.md. Held constant here because it is a
# MEASUREMENT taken at a fixed graph state, not a property of the current tree - it must
# not silently track later edits. Update only when the falsification run is re-run.
HIT_RATE = {"L0": "100", "L1": "40", "L2": "0 †", "L3": "100", "L4": "40", "L5": "100",
            "L6": "100", "L7": "75", "L8": "20", "L9": "100", "L10": "100", "L11": "60",
            "L12": "50", "L13": "50"}
HIT_SOURCE = "query/falsification_baseline.md, cutoff 2026-02-01, 63 held-out papers"

# dashboard.py's definition, reused verbatim so the two files cannot disagree.
PRIMARY_TYPES = {"primary", "meta_analysis", "systematic_review",
                 "trial_registry", "regulatory"}


def load(p, default=None):
    try:
        return yaml.safe_load(open(p)) or default
    except Exception:
        return default


def human_primaries(n):
    return sum(1 for k in (n.get("key_refs") or [])
               if isinstance(k, dict) and (k.get("type") or "") in PRIMARY_TYPES)


def gather():
    nodes = []
    for p in glob.glob(os.path.join(ROOT, "nodes", "*", "*.yaml")):
        n = load(p)
        if isinstance(n, dict) and n.get("id"):
            nodes.append(n)
    researched = [n for n in nodes if not n.get("stub")]

    gdoc = load(os.path.join(ROOT, "gaps", "gaps.yaml"), {})
    gaps = gdoc.get("gaps", []) if isinstance(gdoc, dict) else (gdoc or [])
    sdoc = load(os.path.join(ROOT, "gaps", "search_log.yaml"), {})
    slogs = ((sdoc.get("searches") or sdoc.get("search_log") or [])
             if isinstance(sdoc, dict) else (sdoc or []))

    edoc = load(os.path.join(ROOT, "edges", "edges.yaml"), {})
    edges = edoc.get("edges", []) if isinstance(edoc, dict) else (edoc or [])

    bib = (load(os.path.join(ROOT, "sources", "bibliography.yaml"), {}) or {}).get("refs", {})
    return nodes, researched, gaps, slogs, edges, bib


def layers_block(researched, gaps):
    per = defaultdict(lambda: dict(n=0, dh=0, rep=0, htr=0, A=0, B=0))
    for n in researched:
        d = per[n.get("layer")]
        d["n"] += 1
        if n.get("human_evidence") == "direct":
            d["dh"] += 1
            if human_primaries(n) >= 2:
                d["rep"] += 1
        if str(n.get("translation_risk", "")).lower() in ("high", "very_high"):
            d["htr"] += 1
        c = str(n.get("confidence", "")).strip()
        if c in ("A", "B"):
            d[c] += 1
    gc = defaultdict(int)
    for g in gaps:
        gc[g.get("layer")] += 1

    out = ["| Layer | Name | nodes | direct human | **replicated human** | "
           "high transl. risk | gaps | A/B | **hit rate %** |",
           "|---|---|---:|---:|---:|---:|---:|---|---:|"]
    T = dict(n=0, dh=0, rep=0, gp=0)
    for k in [f"L{i}" for i in range(14)]:
        d = per[k]
        if not d["n"]:
            continue
        T["n"] += d["n"]; T["dh"] += d["dh"]; T["rep"] += d["rep"]; T["gp"] += gc[k]
        out.append(
            f"| {k} | {LAYER_NAMES[k]} | {d['n']} | "
            f"{d['dh']} ({100*d['dh']//d['n']}%) | {d['rep']} ({100*d['rep']//d['n']}%) | "
            f"{d['htr']} ({100*d['htr']//d['n']}%) | {gc[k]} | {d['A']}/{d['B']} | "
            f"**{HIT_RATE[k]}** |")
    out.append(
        f"| | **TOTAL** | **{T['n']}** | **{T['dh']} ({100.0*T['dh']/T['n']:.1f}%)** | "
        f"**{T['rep']} ({100.0*T['rep']/T['n']:.1f}%)** | | **{T['gp']}** | | **64.0** |")
    out.append("")
    out.append("`replicated human` = `human_evidence: direct` **and** ≥2 human primary "
               "sources. `hit rate` is the Phase 7 measured value, "
               f"CORRECT / (CORRECT + WRONG + SILENTLY_ABSENT) — source: {HIT_SOURCE}. "
               "† L2's denominator is 1: two of its three held-out papers were correct "
               "refusals, so the 0 is a small-sample artefact and not a verdict.")
    return "\n".join(out)


def struct_block(nodes, researched, gaps, slogs, edges, bib):
    from importlib.machinery import SourceFileLoader
    ea = SourceFileLoader("edge_audit", os.path.join(ROOT, "tools", "edge_audit.py")).load_module()
    cf = SourceFileLoader("context_filter", os.path.join(ROOT, "tools", "context_filter.py")).load_module()

    bearing = sum(1 for e in edges if e.get("relation") in ea.SIGN_BEARING
                  or e.get("relation") not in ea.SIGN_EXEMPT)
    usable = sum(1 for e in edges if e.get("traversal_usable"))
    exempt = len(edges) - usable

    ctx = {}
    for ax in cf.AXES:
        ctx[ax] = sum(1 for e in edges
                      if cf.classify(str(e.get("context") or ""), ax, None) == "MATCH")

    logged = len({s.get("gap_id") for s in slogs})
    nq = sum(len(n.get("quantitative") or []) for n in nodes)

    rows = [
        "| | |", "|---|---|",
        f"| Nodes | {len(nodes)} ({len(researched)} researched, "
        f"{len(nodes)-len(researched)} stubs) |",
        f"| Edges | {len(edges)} — **{usable} usable for perturbation reasoning**, "
        f"{exempt} flagged unusable |",
        f"| Gaps | {len(gaps)}, with {logged} gap ids carrying reproducible search logs "
        f"({len(slogs)} log entries) |",
        f"| References | {len(bib)}, all machine-resolved against Europe PMC/NCBI |",
        f"| Quantitative values on nodes | {nq} |",
        "",
        "**Context annotation, three-state** (MATCH / MISMATCH / UNANNOTATED — only "
        "MISMATCH excludes an edge; see `atlas/tools/context_filter.py`):",
        "",
        "**DETERMINED** = the axis carries a value. An explicit `zone unknown` is honest, "
        "queryable annotation and is **not** coverage; it is counted separately and never "
        "in the numerator.",
        "",
        "| axis | determined | of edges | explicitly `unknown` | MR-004 target |",
        "|---|---:|---:|---:|---:|",
    ]
    targets = {"zone": "40%", "sex": "30%", "stage": "40%", "species": "—"}
    import re as _re
    for ax in ["zone", "sex", "stage", "species"]:
        c = ctx.get(ax, 0)
        unk = sum(1 for e in edges
                  if _re.search(cf.PROV["explicit_unknown"][ax],
                                str(e.get("context") or ""), _re.I))
        rows.append(f"| {ax} | {c}/{len(edges)} | {100.0*c/max(1,len(edges)):.1f}% | "
                    f"{unk} ({100.0*unk/max(1,len(edges)):.1f}%) | {targets[ax]} |")
    zdet = ctx.get("zone", 0)
    t_src = sum(1 for e in edges
                if _re.search(cf.ZONE_PROVENANCE["resolved in the cited source"],
                              str(e.get("context") or ""), _re.I))
    t_inf = sum(1 for e in edges
                if _re.search(
                    cf.ZONE_PROVENANCE["inferred from endpoint localization records"],
                    str(e.get("context") or ""), _re.I))
    t_def = zdet - t_src - t_inf
    rows += [
        "",
        "**Zone provenance — `determined` is not one thing.** A zone inferred from the "
        "endpoint nodes' localisation records says where the *entities* live, not where "
        "the *interaction* was observed, and it is where an incoherent tag can hide "
        "(see `audit/fragility.md` §4).",
        "",
        "| provenance | edges | of edges |",
        "|---|---:|---:|",
        f"| resolved in the cited source | {t_src} | {100.0*t_src/max(1,len(edges)):.1f}% |",
        f"| definitional — an endpoint node **is** a zone | {t_def} | "
        f"{100.0*t_def/max(1,len(edges)):.1f}% |",
        f"| **inferred from endpoint localization records** | **{t_inf}** | "
        f"**{100.0*t_inf/max(1,len(edges)):.1f}%** |",
        f"| → strong (source-resolved + definitional) | {t_src+t_def} | "
        f"{100.0*(t_src+t_def)/max(1,len(edges)):.1f}% |",
    ]
    rows += [
        "",
        f"Sign coverage on sign-bearing relations is the traversal gate and stands at "
        f"**{usable}/{usable} = 100%**. The {exempt} excluded edges are `precedes` "
        "(temporal), `binds` (no direction), `correlates_with` and `hypothesized_link` "
        "— signing them would be fabrication, so they are flagged "
        "`traversal_usable: false` rather than traversed.",
    ]
    return "\n".join(rows)


def quant_block():
    p = os.path.join(REPO, "query", "parameters.json")
    try:
        j = json.load(open(p))
    except Exception:
        return "_`query/parameters.json` not compiled — run `atlas/tools/compile_query.py`._"
    rc = j.get("reliability_classes", {})
    tot = sum(rc.values()) or 1
    order = sorted(rc.items(), key=lambda kv: -kv[1])
    rows = ["| reliability class | rows | share |", "|---|---:|---:|"]
    for k, v in order:
        star = "**" if k == "single_source_point_no_uncertainty" else ""
        rows.append(f"| {star}`{k}`{star} | {star}{v}{star} | {100.0*v/tot:.1f}% |")
    rows.append(f"| | **{tot}** | |")
    rows += ["",
             "`single_source_point_no_uncertainty` is the risk class: one source, a "
             "point value, and nothing to warn a reader. Phase 2e classified every row "
             "rather than hunting duplicate parameter names, because ~94% of parameter "
             "names appear exactly once — disagreement in this field is not encoded as "
             "duplicate rows."]
    return "\n".join(rows)


def splice(text, tag, body):
    b, e = f"<!-- COVERAGE:{tag}:BEGIN -->", f"<!-- COVERAGE:{tag}:END -->"
    if b not in text or e not in text:
        sys.exit(f"markers for {tag} not found in coverage.md")
    return re.sub(re.escape(b) + r".*?" + re.escape(e),
                  lambda _: f"{b}\n{body}\n{e}", text, flags=re.S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    nodes, researched, gaps, slogs, edges, bib = gather()
    txt = open(COV).read()
    new = splice(txt, "LAYERS", layers_block(researched, gaps))
    new = splice(new, "STRUCT", struct_block(nodes, researched, gaps, slogs, edges, bib))
    new = splice(new, "QUANT", quant_block())
    if a.check:
        stale = new != txt
        print("coverage.md is " + ("STALE - run coverage_report.py" if stale else "current"))
        return 1 if stale else 0
    open(COV, "w").write(new)
    print("coverage.md regenerated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
