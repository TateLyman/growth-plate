#!/usr/bin/env python3
"""
Fragility analysis — where would this map BREAK?

WHY THIS EXISTS
CORR-004 found a withdrawn reference carrying what the atlas called "the only
DEMONSTRATED molecular entry point from the environment layer into a local signalling
node". It was found by accident during a retraction check rather than by analysis.

Convergence (query/derived.json) answers "where does causal information concentrate".
This answers "where would this map break", which is a different question and the one
that decides where verification effort belongs. A node with 40 inbound edges is
important; a node with 2 inbound edges that is the sole route between two subsystems is
FRAGILE. Importance and fragility are not the same property.

TWO GRAPHS, AND THE DIFFERENCE BETWEEN THEM IS THE POINT

  structural   all 1,181 edges, whatever their grade or relation type
  answerable   the traversal_usable subset only — the graph that can actually carry a
               derived answer, excluding `precedes`, `binds`, `correlates_with` and
               every `hypothesized_link`

An edge can be irrelevant in the first and load-bearing in the second. That is exactly
what CORR-004 hit, and it is why fragility computed on the full edge set alone would
have missed it. See --control.

METRICS, computed by traversal and not estimated

  bridge edge          removal increases the number of weakly-connected components, OR
                       it is the only edge connecting a layer pair
  articulation node    removal increases the number of components
  pairs_destroyed      ordered reachable (s,t) pairs lost when the edge is removed.
                       For a true bridge this is exact: |ancestors(u)+u| x
                       |descendants(v)+v| across the split. For a non-splitting edge it
                       is summed directly over the affected origins.
  claims_lost /        claim_grades and quant/parameters.csv rows carried by the nodes
  quant_rows_lost      that become unreachable. THIS is "how many downstream claims
                       depend on it".
  single-source seam   a layer-pair connection where every connecting edge cites the
                       same single reference — the CORR-004 class by construction.

Usage:
  python3 atlas/tools/fragility.py --json query/fragility.json
  python3 atlas/tools/fragility.py --control        # run the CORR-004 positive control
"""
import os, sys, json, argparse, subprocess
from collections import defaultdict, deque

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
Q = os.path.join(REPO, "query")

CONTROL_EDGE = "e01055"
CONTROL_COMMIT = "9c80db7"     # last commit before CORR-004 reclassified e01055


def load_graph():
    g = json.load(open(os.path.join(Q, "graph.json")))
    nodes = g["nodes"] if isinstance(g["nodes"], dict) else {n["id"]: n for n in g["nodes"]}
    try:
        params = json.load(open(os.path.join(Q, "parameters.json"))).get("by_node", {})
    except Exception:
        params = {}
    return nodes, g["edges"], params


def adj(edges):
    fwd, rev, und = defaultdict(list), defaultdict(list), defaultdict(set)
    for e in edges:
        s, t = e["source"], e["target"]
        fwd[s].append((t, e["edge_id"]))
        rev[t].append((s, e["edge_id"]))
        und[s].add(t); und[t].add(s)
    return fwd, rev, und


def bfs(g, start, ban_edge=None, ban_node=None):
    seen, dq = {start}, deque([start])
    while dq:
        u = dq.popleft()
        for v, eid in g.get(u, ()):
            if eid == ban_edge or v == ban_node or v in seen:
                continue
            seen.add(v); dq.append(v)
    return seen


def n_components(und, ids, ban_node=None, ban_edge_pair=None):
    seen, c = set(), 0
    for n in ids:
        if n == ban_node or n in seen:
            continue
        c += 1
        dq = deque([n]); seen.add(n)
        while dq:
            u = dq.popleft()
            for v in und.get(u, ()):
                if v == ban_node or v in seen:
                    continue
                if ban_edge_pair and {u, v} == ban_edge_pair:
                    continue
                seen.add(v); dq.append(v)
    return c


def analyse(nodes, edges, params, label):
    ids = list(nodes)
    layer = {n: nodes[n].get("layer") for n in nodes}
    fwd, rev, und = adj(edges)
    base = n_components(und, ids)

    def payload(ns):
        c = sum(len(nodes.get(n, {}).get("claim_grades") or []) for n in ns)
        q = sum(len(params.get(n, []) or []) for n in ns)
        return c, q

    # --- layer seams ----------------------------------------------------------
    seam = defaultdict(list)
    for e in edges:
        a, b = layer.get(e["source"]), layer.get(e["target"])
        if a and b and a != b:
            seam[tuple(sorted((a, b)))].append(e)
    seams = []
    for pair, es in sorted(seam.items()):
        rs = set()
        for e in es:
            rs |= {str(r) for r in (e.get("refs") or [])}
        seams.append({"pair": f"{pair[0]}-{pair[1]}", "n_edges": len(es),
                      "n_distinct_refs": len(rs), "refs": sorted(rs)[:8],
                      "edge_ids": [e["edge_id"] for e in es][:10],
                      "sole_edge": len(es) == 1, "single_source": len(rs) == 1})
    sole_seam_ids = {es[0]["edge_id"] for p, es in seam.items() if len(es) == 1}
    single_source_ids = set()
    for p, es in seam.items():
        rs = set()
        for e in es:
            rs |= {str(r) for r in (e.get("refs") or [])}
        if len(rs) == 1:
            single_source_ids |= {e["edge_id"] for e in es}

    # --- bridge edges ----------------------------------------------------------
    rows = []
    for e in edges:
        eid, u, v = e["edge_id"], e["source"], e["target"]
        splits = n_components(und, ids, ban_edge_pair={u, v}) > base
        if not (splits or eid in sole_seam_ids or eid in single_source_ids):
            continue
        if splits:
            up = bfs(rev, u, ban_edge=eid)          # ancestors of u, + u
            down = bfs(fwd, v, ban_edge=eid)        # descendants of v, + v
            pairs = len(up) * len(down)
            lost = down
        else:
            lost, pairs = set(), 0
            for s in bfs(rev, u, ban_edge=eid):
                d = bfs(fwd, s) - bfs(fwd, s, ban_edge=eid)
                pairs += len(d); lost |= d
            up = bfs(rev, u, ban_edge=eid)
        cl, qr = payload(lost)
        rows.append({
            "edge_id": eid, "source": u, "target": v,
            "layers": f'{layer.get(u)}->{layer.get(v)}',
            "cross_layer": layer.get(u) != layer.get(v),
            "relation": e.get("relation"), "confidence": e.get("confidence"),
            "traversal_usable": bool(e.get("traversal_usable")),
            "refs": e.get("refs") or [], "n_refs": len(e.get("refs") or []),
            "splits_components": splits,
            "sole_layer_seam": eid in sole_seam_ids,
            "single_source_seam": eid in single_source_ids,
            "nodes_isolated": len(lost),
            "claims_lost": cl, "quant_rows_lost": qr,
            "upstream_dependents": len(up),
            "pairs_destroyed": pairs,
        })
    rows.sort(key=lambda r: (-r["pairs_destroyed"], -r["claims_lost"], r["edge_id"]))

    # --- articulation nodes -----------------------------------------------------
    art = []
    for n in ids:
        if n_components(und, ids, ban_node=n) <= base:
            continue
        lost = set()
        for p, _ in rev.get(n, ()):
            lost |= bfs(fwd, p) - bfs(fwd, p, ban_node=n)
        lost.discard(n)
        cl, qr = payload(lost)
        art.append({"node": n, "layer": layer.get(n),
                    "name": nodes[n].get("name"),
                    "confidence": nodes[n].get("confidence"),
                    "human_evidence": nodes[n].get("human_evidence"),
                    "n_key_refs": len(nodes[n].get("key_refs") or []),
                    "nodes_isolated": len(lost),
                    "claims_lost": cl, "quant_rows_lost": qr,
                    "load_bearing": cl + qr + len(lost)})
    art.sort(key=lambda r: (-r["load_bearing"], r["node"]))

    return {"graph": label, "n_nodes": len(ids), "n_edges": len(edges),
            "components": base, "bridge_edges": rows, "articulation_nodes": art,
            "layer_seams": seams,
            "single_source_seams": [s for s in seams if s["single_source"]],
            "sole_edge_seams": [s for s in seams if s["sole_edge"]]}


def control(nodes, params):
    """CORR-004 positive control, run against the PRE-correction graph."""
    try:
        blob = subprocess.check_output(
            ["git", "-C", REPO, "show", f"{CONTROL_COMMIT}:atlas/edges/edges.yaml"],
            text=True)
    except Exception as ex:
        return {"error": f"cannot read pre-correction edges: {ex}"}
    import yaml
    d = yaml.safe_load(blob)
    pre = d["edges"] if isinstance(d, dict) else d
    out = {}
    for label, es in (("structural", pre),
                      ("answerable", [e for e in pre if e.get("traversal_usable")])):
        r = analyse(nodes, es, params, label)
        hit = next((x for x in r["bridge_edges"] if x["edge_id"] == CONTROL_EDGE), None)
        out[label] = {"n_edges": len(es), "is_bridge": bool(hit), "row": hit}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--control", action="store_true")
    ap.add_argument("--stamp", action="store_true",
                    help="write is_bridge / single_source_seam flags back onto "
                         "query/graph.json so a traversal can see a chokepoint")
    a = ap.parse_args()
    nodes, edges, params = load_graph()

    if a.control:
        c = control(nodes, params)
        print(json.dumps(c, indent=1)[:3000])
        return 0

    res = {}
    for label, es in (("structural", edges),
                      ("answerable", [e for e in edges if e.get("traversal_usable")])):
        r = analyse(nodes, es, params, label)
        res[label] = r
        print(f"\n===== {label.upper()}  ({r['n_edges']} edges, "
              f"{r['components']} weakly-connected components) =====")
        print(f"bridge/seam edges {len(r['bridge_edges'])} · "
              f"articulation nodes {len(r['articulation_nodes'])} · "
              f"layer pairs {len(r['layer_seams'])} "
              f"(sole-edge {len(r['sole_edge_seams'])}, "
              f"single-source {len(r['single_source_seams'])})")
        print(f"--- top {a.top} by reachable pairs destroyed ---")
        for x in r["bridge_edges"][:a.top]:
            tags = "".join([" SOLE_SEAM" if x["sole_layer_seam"] else "",
                            " 1SRC" if x["single_source_seam"] else "",
                            " SPLITS" if x["splits_components"] else ""])
            print(f"  {x['edge_id']} {x['layers']:9s} pairs={x['pairs_destroyed']:6d} "
                  f"iso={x['nodes_isolated']:3d} claims={x['claims_lost']:3d} "
                  f"quant={x['quant_rows_lost']:4d} up={x['upstream_dependents']:3d} "
                  f"refs={x['n_refs']} {str(x['confidence']):11s}"
                  f"{x['source']}->{x['target']}{tags}")

    res["control"] = control(nodes, params)
    cs, ca = res["control"].get("structural", {}), res["control"].get("answerable", {})
    print("\n===== CORR-004 POSITIVE CONTROL (pre-correction graph) =====")
    print(f"  e01055 bridge in STRUCTURAL graph : {cs.get('is_bridge')}")
    print(f"  e01055 bridge in ANSWERABLE graph : {ca.get('is_bridge')}")

    if a.stamp:
        gp = os.path.join(Q, "graph.json")
        g = json.load(open(gp))
        flags = {}
        for label in ("structural", "answerable"):
            for x in res[label]["bridge_edges"]:
                f = flags.setdefault(x["edge_id"], {})
                f[f"bridge_{label}"] = True
                if x["single_source_seam"]:
                    f["single_source_seam"] = True
                if x["sole_layer_seam"]:
                    f["sole_layer_seam"] = True
                f["pairs_destroyed"] = max(f.get("pairs_destroyed", 0),
                                           x["pairs_destroyed"])
        n = 0
        for e in g["edges"]:
            f = flags.get(e["edge_id"])
            # Always write the field, so absence of a flag is a stated NO rather than
            # a missing key a traversal could read as unknown - the same null-semantics
            # defect that cost this project two shipped-wrong answers.
            e["chokepoint"] = f if f else False
            n += 1 if f else 0
        g.setdefault("meta", {})["fragility_stamped"] = True
        json.dump(g, open(gp, "w"))
        print(f"stamped {n} chokepoint edges onto query/graph.json "
              f"(all {len(g['edges'])} edges carry the field explicitly)")

    if a.json:
        json.dump(res, open(a.json, "w"), indent=1)
        print(f"\nwrote {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
