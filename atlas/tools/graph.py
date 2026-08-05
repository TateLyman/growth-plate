#!/usr/bin/env python3
"""
Graph analysis over the atlas — the Phase 3 integration tool.

A pile of 14 layers is not a system. This finds the structure that makes it one:

  --convergence   nodes with >=N inbound edges from DISTINCT pathways/layers.
                  These are where independent signals are integrated, and they are
                  the highest-value targets in the whole map.
  --loops         directed cycles (feedback loops), reported with the sign product
                  so negative-feedback and positive-feedback loops are separated.
                  PTHrP/IHH should appear here; if it does not, the edges are wrong.
  --orphans       non-stub nodes with no edges, which Phase 3 requires be justified.
  --crosslayer    edges whose endpoints sit in different layers - the seams.
  --hubs          highest total degree.
  --mermaid LAYER emit a Mermaid diagram for one layer (or `all` for cross-layer).
  --duplicates    candidate duplicate nodes (same concept under different names),
                  matched on normalised name/alias overlap.

Usage:
  python3 atlas/tools/graph.py --summary
  python3 atlas/tools/graph.py --convergence 3 --loops --crosslayer
  python3 atlas/tools/graph.py --mermaid L3 > atlas/figures/L3_signaling.mmd
"""
import os, sys, glob, argparse, re
from collections import defaultdict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_all():
    nodes = {}
    for p in glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"), recursive=True):
        # tolerant: one malformed file must not blind the whole graph analysis
        try:
            with open(p) as f:
                n = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"  ! UNPARSEABLE {os.path.relpath(p)}: {str(e)[:80]}",
                  file=sys.stderr)
            continue
        if isinstance(n, dict) and n.get("id"):
            nodes[n["id"]] = n
    ed = os.path.join(ROOT, "edges", "edges.yaml")
    edges = []
    if os.path.exists(ed):
        with open(ed) as f:
            edges = (yaml.safe_load(f) or {}).get("edges", []) or []
    return nodes, edges


SIGNED = {"+": 1, "-": -1}


def find_loops(edges, max_len=6, cap=200):
    adj = defaultdict(list)
    for e in edges:
        adj[e.get("source")].append(e)
    seen, loops = set(), []

    def walk(start, cur, path, edgepath):
        if len(path) > max_len or len(loops) >= cap:
            return
        for e in adj.get(cur, []):
            t = e.get("target")
            if t == start and len(path) >= 2:
                key = frozenset(path)
                sig = (key, len(path))
                if sig not in seen:
                    seen.add(sig)
                    loops.append(list(path) + [edgepath + [e]])
            elif t not in path:
                walk(start, t, path + [t], edgepath + [e])

    for s in list(adj.keys()):
        walk(s, s, [s], [])
    return loops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--convergence", type=int, metavar="N")
    ap.add_argument("--loops", action="store_true")
    ap.add_argument("--orphans", action="store_true")
    ap.add_argument("--crosslayer", action="store_true")
    ap.add_argument("--hubs", type=int, default=0)
    ap.add_argument("--duplicates", action="store_true")
    ap.add_argument("--mermaid", metavar="LAYER")
    a = ap.parse_args()

    nodes, edges = load_all()
    indeg, outdeg = defaultdict(list), defaultdict(list)
    for e in edges:
        if e.get("target"):
            indeg[e["target"]].append(e)
        if e.get("source"):
            outdeg[e["source"]].append(e)

    if a.mermaid:
        L = a.mermaid
        sel = [e for e in edges
               if (L == "all" and nodes.get(e.get("source"), {}).get("layer")
                   != nodes.get(e.get("target"), {}).get("layer"))
               or (L != "all" and (nodes.get(e.get("source"), {}).get("layer") == L
                                   or nodes.get(e.get("target"), {}).get("layer") == L))]
        arrow = {"inhibits": "--x", "activates": "-->", "binds": "---",
                 "hypothesized_link": "-.->"}
        print("graph LR")
        used = set()
        for e in sel:
            for nid in (e["source"], e["target"]):
                if nid in used or nid not in nodes:
                    continue
                used.add(nid)
                nm = str(nodes[nid].get("name", nid)).replace('"', "'")
                print(f'  {nid}["{nm}"]')
        for e in sel:
            ar = arrow.get(e.get("relation"), "-->")
            lbl = e.get("relation", "")
            c = e.get("confidence", "")
            print(f'  {e["source"]} {ar}|"{lbl} ({c})"| {e["target"]}')
        return 0

    if a.summary or not any([a.convergence, a.loops, a.orphans, a.crosslayer,
                             a.hubs, a.duplicates]):
        full = [n for n in nodes.values() if not n.get("stub")]
        print(f"nodes {len(nodes)} ({len(full)} researched)   edges {len(edges)}")
        rel = defaultdict(int)
        for e in edges:
            rel[e.get("relation")] += 1
        print("relations:", dict(sorted(rel.items(), key=lambda x: -x[1])))

    if a.convergence:
        print(f"\n=== CONVERGENCE NODES (>= {a.convergence} inbound) ===")
        rows = []
        for nid, ins in indeg.items():
            if len(ins) >= a.convergence:
                srcl = {nodes.get(e["source"], {}).get("layer") for e in ins}
                rows.append((len(ins), len(srcl), nid, sorted(x for x in srcl if x)))
        for cnt, nl, nid, ls in sorted(rows, reverse=True)[:40]:
            nm = nodes.get(nid, {}).get("name", nid)
            print(f"  {cnt:3d} inbound from {nl} layer(s) {ls}  {nid}  [{nm}]")
        if not rows:
            print("  none yet")

    if a.loops:
        print("\n=== FEEDBACK LOOPS ===")
        loops = find_loops(edges)
        if not loops:
            print("  none found")
        for L in loops[:30]:
            path, eps = L[:-1], L[-1]
            sign = 1
            unk = False
            for e in eps:
                s = SIGNED.get(str(e.get("sign")))
                if s is None:
                    unk = True
                else:
                    sign *= s
            kind = "UNKNOWN-sign" if unk else ("NEGATIVE (stabilising)" if sign < 0
                                               else "POSITIVE (amplifying)")
            print(f"  {kind}: " + " -> ".join(path) + " -> " + path[0])

    if a.crosslayer:
        print("\n=== CROSS-LAYER EDGES (the seams) ===")
        pairs = defaultdict(int)
        for e in edges:
            sl = nodes.get(e.get("source"), {}).get("layer")
            tl = nodes.get(e.get("target"), {}).get("layer")
            if sl and tl and sl != tl:
                pairs[(sl, tl)] += 1
        for (sl, tl), c in sorted(pairs.items(), key=lambda x: -x[1])[:30]:
            print(f"  {sl} -> {tl}: {c}")
        if not pairs:
            print("  none yet")

    if a.orphans:
        print("\n=== ORPHAN non-stub nodes ===")
        o = [nid for nid, n in nodes.items()
             if not n.get("stub") and not indeg.get(nid) and not outdeg.get(nid)]
        for nid in sorted(o):
            print(f"  {nid}  [{nodes[nid].get('layer')}]")
        print(f"  total {len(o)}")

    if a.hubs:
        print(f"\n=== TOP {a.hubs} HUBS (total degree) ===")
        deg = {nid: len(indeg.get(nid, [])) + len(outdeg.get(nid, []))
               for nid in nodes}
        for nid, d in sorted(deg.items(), key=lambda x: -x[1])[:a.hubs]:
            if d == 0:
                break
            print(f"  {d:3d}  {nid}  [{nodes[nid].get('layer')}]")

    if a.duplicates:
        print("\n=== CANDIDATE DUPLICATE NODES ===")
        def norm(s):
            s = re.sub(r"[^a-z0-9 ]", " ", str(s).lower())
            return frozenset(w for w in s.split()
                             if w not in {"the", "of", "in", "and", "a"} and len(w) > 2)
        keys = {}
        for nid, n in nodes.items():
            for nm in [n.get("name")] + list(n.get("aliases") or []):
                k = norm(nm)
                if k:
                    keys.setdefault(k, set()).add(nid)
        hits = {k: v for k, v in keys.items() if len(v) > 1}
        for k, v in list(hits.items())[:30]:
            print(f"  {sorted(v)}  <- {' '.join(sorted(k))}")
        print(f"  total candidate collisions {len(hits)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
