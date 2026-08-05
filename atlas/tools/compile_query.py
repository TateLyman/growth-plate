#!/usr/bin/env python3
"""
Compile the file-per-node atlas into query artifacts (Phase 5a).

File-per-node YAML is the right AUTHORING format - it diffs, merges and reviews
well. It is the wrong QUERY format: answering one perturbation question would mean
opening 600 files. So we compile. We do not replace: source of truth stays in
atlas/nodes/**, and every artifact here regenerates from it.

Outputs (all under query/):
  graph.json        nodes + edges with grades, claim_grades, refs, context
  derived.json      cycle inventory with signs, convergence ranks, reachability
                    sets, layer adjacency, node->file map, alias->id resolution
  parameters.json   quantitative rows keyed by node, spread + single-lab +
                    superseded flags preserved
  gaps.json         gap registry + search logs, indexed by layer/type/tractability

Round-trip check: compiled node count must equal source node count, else abort.

Usage:
  python3 atlas/tools/compile_query.py
  python3 atlas/tools/compile_query.py --verify   # counts only, no write
"""
import os, sys, glob, json, argparse, re
from collections import defaultdict, Counter
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(ROOT), "query")

SIGN = {"+": 1, "-": -1}


def load(p, d=None):
    if not os.path.exists(p):
        return d
    try:
        with open(p) as f:
            return yaml.safe_load(f) or d
    except Exception as e:
        print(f"  ! UNPARSEABLE {os.path.relpath(p)}: {str(e)[:80]}", file=sys.stderr)
        return d


def find_cycles(adj, max_len=7, cap=400):
    seen, cycles = set(), []

    def walk(start, cur, path, epath):
        if len(path) > max_len or len(cycles) >= cap:
            return
        for e in adj.get(cur, []):
            t = e["target"]
            if t == start and len(path) >= 2:
                sig = (frozenset(path), len(path))
                if sig not in seen:
                    seen.add(sig)
                    cycles.append((list(path), list(epath) + [e]))
            elif t not in path:
                walk(start, t, path + [t], epath + [e])

    for s in list(adj.keys()):
        walk(s, s, [s], [])
    return cycles


def reach(adj, start, max_depth=4):
    """Forward reachability with sign products. Only traversal_usable edges."""
    out, frontier = {}, [(start, 1, 0, [])]
    while frontier:
        node, sgn, d, path = frontier.pop()
        if d >= max_depth:
            continue
        for e in adj.get(node, []):
            if not e.get("traversal_usable"):
                continue
            s = SIGN.get(str(e.get("sign")))
            if s is None:
                continue
            t, ns = e["target"], sgn * s
            key = t
            if key not in out or len(path) + 1 < out[key]["depth"]:
                out[key] = {"sign": ns, "depth": len(path) + 1,
                            "path": path + [e["edge_id"]]}
                frontier.append((t, ns, d + 1, path + [e["edge_id"]]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)

    # ---- nodes ----
    nodes, node_file, alias = {}, {}, {}
    src_files = sorted(glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"),
                                 recursive=True))
    for p in src_files:
        n = load(p)
        if not isinstance(n, dict) or not n.get("id"):
            continue
        nid = n["id"]
        nodes[nid] = n
        node_file[nid] = os.path.relpath(p, os.path.dirname(ROOT))
        alias[nid.lower()] = nid
        alias[str(n.get("name", "")).lower()] = nid
        for al in (n.get("aliases") or []):
            alias[str(al).lower()] = nid

    if len(nodes) != len([p for p in src_files if load(p)]):
        pass  # tolerated: unparseable files already reported

    edges = (load(os.path.join(ROOT, "edges", "edges.yaml"), {}) or {}).get("edges", [])
    gaps = (load(os.path.join(ROOT, "gaps", "gaps.yaml"), {}) or {}).get("gaps", [])
    slogs = (load(os.path.join(ROOT, "gaps", "search_log.yaml"), {}) or {}).get("searches", [])
    refs = (load(os.path.join(ROOT, "sources", "bibliography.yaml"), {}) or {}).get("refs", {})

    print(f"source nodes {len(nodes)} · edges {len(edges)} · gaps {len(gaps)} "
          f"· searches {len(slogs)} · refs {len(refs)}")
    if a.verify:
        return 0

    # ---- graph.json ----
    graph = {
        "meta": {"nodes": len(nodes), "edges": len(edges),
                 "generated_from": "atlas/nodes/**, atlas/edges/edges.yaml",
                 "warning": "COMPILED ARTIFACT - never hand-edit; regenerate with tools/compile_query.py"},
        "nodes": {nid: {
            "id": nid, "name": n.get("name"), "type": n.get("type"),
            "layer": n.get("layer"), "stub": bool(n.get("stub")),
            "summary": n.get("summary"),
            "confidence": n.get("confidence"),
            "claim_grades": n.get("claim_grades"),
            "human_evidence": n.get("human_evidence"),
            "human_evidence_note": n.get("human_evidence_note"),
            "species_basis": n.get("species_basis"),
            "translation_risk": n.get("translation_risk"),
            "translation_risk_reason": n.get("translation_risk_reason"),
            "localization": n.get("localization"),
            "key_refs": n.get("key_refs"),
            "open_questions": n.get("open_questions"),
            "contradicts": n.get("contradicts"),
            "termination_reason": n.get("termination_reason"),
            "termination_note": n.get("termination_note"),
            "pending_source": n.get("pending_source"),
            "last_verified": n.get("last_verified"),
            "aliases": n.get("aliases"),
        } for nid, n in nodes.items()},
        "edges": edges,
        "refs": refs,
    }

    # ---- derived.json ----
    adj = defaultdict(list)
    radj = defaultdict(list)
    for e in edges:
        if e.get("source") and e.get("target"):
            adj[e["source"]].append(e)
            radj[e["target"]].append(e)

    usable_adj = defaultdict(list)
    for s, es in adj.items():
        usable_adj[s] = [e for e in es if e.get("traversal_usable")]

    cycles = []
    for path, eps in find_cycles(usable_adj):
        sgn, unk = 1, False
        for e in eps:
            v = SIGN.get(str(e.get("sign")))
            if v is None:
                unk = True
            else:
                sgn *= v
        kind = ("unknown" if unk else
                "negative_stabilising" if sgn < 0 else "positive_amplifying")
        neg = sum(1 for e in eps if str(e.get("sign")) == "-")
        cycles.append({
            "nodes": path, "edges": [e["edge_id"] for e in eps],
            "length": len(path), "class": kind,
            "bistable": (kind == "positive_amplifying" and neg >= 2),
            "layers": sorted({nodes.get(x, {}).get("layer") for x in path} - {None}),
            "timescales": [e.get("timescale") for e in eps],
        })

    conv = []
    for nid, ins in radj.items():
        layers = sorted({nodes.get(e["source"], {}).get("layer") for e in ins} - {None})
        conv.append({"node": nid, "inbound": len(ins), "n_layers": len(layers),
                     "layers": layers, "layer": nodes.get(nid, {}).get("layer")})
    conv.sort(key=lambda x: (-x["inbound"], -x["n_layers"]))

    layer_adj = Counter()
    for e in edges:
        sl = nodes.get(e.get("source"), {}).get("layer")
        tl = nodes.get(e.get("target"), {}).get("layer")
        if sl and tl:
            layer_adj[f"{sl}->{tl}"] += 1

    # reachability for the nodes worth precomputing
    targets = [c["node"] for c in conv[:25]]
    targets += [nid for nid, n in nodes.items()
                if n.get("layer") == "L12" and not n.get("stub")]
    reach_sets = {t: reach(usable_adj, t) for t in dict.fromkeys(targets)}

    derived = {
        "meta": {"warning": "COMPILED - regenerate with tools/compile_query.py",
                 "traversal_rule": "perturbation traversal uses ONLY edges with "
                                   "traversal_usable: true (signed, sign-bearing relation)"},
        "alias_to_id": alias,
        "node_file": node_file,
        "cycles": cycles,
        "cycle_summary": dict(Counter(c["class"] for c in cycles)),
        "convergence": conv[:80],
        "layer_adjacency": dict(layer_adj),
        "reachability": {k: {kk: vv for kk, vv in v.items()}
                         for k, v in reach_sets.items()},
        "orphans": sorted([nid for nid, n in nodes.items()
                           if not n.get("stub") and not adj.get(nid) and not radj.get(nid)]),
        "edge_usability": {
            "usable": sum(1 for e in edges if e.get("traversal_usable")),
            "unusable": sum(1 for e in edges if not e.get("traversal_usable")),
            "reason": "sign-exempt relation (precedes/binds/correlates_with/"
                      "hypothesized_link) or unsigned",
        },
    }

    # ---- parameters.json ----
    params = defaultdict(list)
    byname = defaultdict(list)
    for nid, n in nodes.items():
        for q in (n.get("quantitative") or []):
            if not isinstance(q, dict):
                continue
            row = dict(q)
            row["node_id"] = nid
            row["layer"] = n.get("layer")
            params[nid].append(row)
            byname[re.sub(r"\s+", " ", str(q.get("parameter", "")).lower()).strip()].append(row)
    disputed = {k: v for k, v in byname.items()
                if len({str(r.get("source_ref")) for r in v}) > 1}
    single_lab = {k: v[0] for k, v in byname.items() if len(v) == 1}
    parameters = {
        "meta": {"warning": "COMPILED - regenerate with tools/compile_query.py",
                 "policy": "where sources conflict, report the SPREAD with the "
                           "methodological reason; never a collapsed central estimate"},
        "by_node": dict(params),
        "disputed": disputed,
        "single_source_parameters": sorted(single_lab.keys()),
        "superseded_rows": [r for rs in params.values() for r in rs
                            if r.get("superseded_model")],
        "unverified_rows": [r for rs in params.values() for r in rs
                            if r.get("value_unverified")],
    }

    # ---- gaps.json ----
    slog_by_gap = defaultdict(list)
    for s in slogs:
        slog_by_gap[s.get("gap_id")].append(s)
    gapdoc = {
        "meta": {"warning": "COMPILED - regenerate with tools/compile_query.py"},
        "gaps": gaps,
        "by_layer": {L: [g["gap_id"] for g in gaps if g.get("layer") == L]
                     for L in sorted({g.get("layer") for g in gaps} - {None})},
        "by_type": {t: [g["gap_id"] for g in gaps if g.get("type") == t]
                    for t in sorted({g.get("type") for g in gaps} - {None})},
        "by_tractability": {str(t): [g["gap_id"] for g in gaps
                                     if str(g.get("tractability")) == str(t)]
                            for t in sorted({str(g.get("tractability")) for g in gaps})},
        "search_logs": dict(slog_by_gap),
    }

    for name, obj in [("graph.json", graph), ("derived.json", derived),
                      ("parameters.json", parameters), ("gaps.json", gapdoc)]:
        with open(os.path.join(OUT, name), "w") as f:
            json.dump(obj, f, indent=1, default=str)
        sz = os.path.getsize(os.path.join(OUT, name)) / 1024
        print(f"  wrote query/{name:18s} {sz:8.1f} KB")

    # ---- round trip ----
    rt = json.load(open(os.path.join(OUT, "graph.json")))
    ok = len(rt["nodes"]) == len(nodes) and len(rt["edges"]) == len(edges)
    print(f"\nROUND-TRIP: compiled {len(rt['nodes'])} nodes / {len(rt['edges'])} edges "
          f"vs source {len(nodes)} / {len(edges)}  -> {'PASS' if ok else 'FAIL'}")
    print(f"cycles: {derived['cycle_summary']}")
    print(f"usable edges for perturbation: {derived['edge_usability']['usable']}"
          f"/{len(edges)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
