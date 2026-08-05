#!/usr/bin/env python3
"""
Compact digest of one layer — enough to write the /docs/<layer>.md synthesis
without loading every node file.

Prints: node inventory by type with confidence and species basis, every
quantitative value, the gap register with types, and the reference list ranked
by how many nodes cite it (which surfaces the load-bearing sources).

Usage:
  python3 atlas/tools/digest.py L2
  python3 atlas/tools/digest.py L2 --quant-only
  python3 atlas/tools/digest.py L2 --max-summary 0     # suppress summaries
"""
import os, sys, glob, argparse
from collections import Counter, defaultdict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(p, d=None):
    if not os.path.exists(p):
        return d
    with open(p) as f:
        return yaml.safe_load(f) or d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("layer")
    ap.add_argument("--quant-only", action="store_true")
    ap.add_argument("--max-summary", type=int, default=240)
    a = ap.parse_args()
    L = a.layer

    nodes = {}
    for p in glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"), recursive=True):
        n = load(p)
        if isinstance(n, dict) and n.get("layer") == L:
            nodes[n["id"]] = n
    full = {k: v for k, v in nodes.items() if not v.get("stub")}

    refs = (load(os.path.join(ROOT, "sources", "bibliography.yaml"), {}) or {}).get("refs", {})
    for sp in glob.glob(os.path.join(ROOT, "sources", "shards", "*.yaml")):
        refs.update((load(sp, {}) or {}).get("refs", {}) or {})

    gaps = (load(os.path.join(ROOT, "gaps", "gaps.yaml"), {}) or {}).get("gaps", [])
    for sp in glob.glob(os.path.join(ROOT, "gaps", "shards", "*.gaps.yaml")):
        gaps += (load(sp, {}) or {}).get("gaps", []) or []
    gaps = [g for g in gaps if g.get("layer") == L]

    edges = (load(os.path.join(ROOT, "edges", "edges.yaml"), {}) or {}).get("edges", [])
    for sp in glob.glob(os.path.join(ROOT, "edges", "shards", "*.yaml")):
        edges += (load(sp, {}) or {}).get("edges", []) or []
    ledges = [e for e in edges
              if nodes.get(e.get("source")) or nodes.get(e.get("target"))]

    print(f"# DIGEST {L}   nodes {len(nodes)} ({len(full)} researched)  "
          f"gaps {len(gaps)}  edges touching layer {len(ledges)}")
    print(f"confidence: {dict(Counter(v.get('confidence') for v in full.values()))}")
    print(f"types:      {dict(Counter(v.get('type') for v in full.values()))}")
    hr = Counter(v.get("human_evidence") for v in full.values())
    tr = Counter(v.get("translation_risk") for v in full.values())
    print(f"human_evidence: {dict(hr)}   translation_risk: {dict(tr)}")

    if not a.quant_only:
        print("\n## NODES")
        for nid, n in sorted(full.items()):
            sb = ",".join(n.get("species_basis") or [])
            print(f"\n### {nid}  [{n.get('type')}] conf={n.get('confidence')} "
                  f"he={n.get('human_evidence')} tr={n.get('translation_risk')} sp={sb}")
            if a.max_summary:
                s = " ".join(str(n.get("summary") or "").split())
                print(f"  {s[:a.max_summary]}{'...' if len(s) > a.max_summary else ''}")
            if n.get("contradicts"):
                print(f"  CONTRADICTS: {n['contradicts']}")

    print("\n## QUANTITATIVE")
    nq = 0
    for nid, n in sorted(full.items()):
        for q in (n.get("quantitative") or []):
            nq += 1
            uv = " [UNVERIFIED]" if q.get("value_unverified") else ""
            print(f"  {nid}: {q.get('parameter')} = {q.get('value')} {q.get('unit')} "
                  f"({q.get('species')}; {str(q.get('conditions'))[:60]}) "
                  f"±{q.get('uncertainty')} <{q.get('source_ref')}>{uv}")
    print(f"  -- {nq} values")

    print("\n## GAPS")
    for g in sorted(gaps, key=lambda x: str(x.get("gap_id"))):
        print(f"  [{g.get('type')}] {g.get('gap_id')} (tract={g.get('tractability')}): "
              f"{' '.join(str(g.get('question') or '').split())[:170]}")
    print(f"  -- {len(gaps)} gaps, types {dict(Counter(g.get('type') for g in gaps))}")

    print("\n## REFERENCES (by citing-node count)")
    cite = defaultdict(set)
    for nid, n in full.items():
        for kr in (n.get("key_refs") or []):
            if kr.get("ref_id"):
                cite[kr["ref_id"]].add(nid)
        for q in (n.get("quantitative") or []):
            if q.get("source_ref"):
                cite[q["source_ref"]].add(nid)
    for rid, ns in sorted(cite.items(), key=lambda x: -len(x[1])):
        r = refs.get(rid, {})
        print(f"  {len(ns):2d}x {rid:24s} {r.get('first_author','?')} "
              f"{r.get('year','?')} [{r.get('tier','?')}] "
              f"{str(r.get('title',''))[:70]}")
    print(f"  -- {len(cite)} distinct refs cited in this layer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
