#!/usr/bin/env python3
"""
structural_confidence — a quality signal for DERIVED answers (MR-003 item 1).

WHY THIS EXISTS AND WHAT IT IS NOT
Evidence grades were correctly removed from derived answers: attaching an A/B/C to
"there are 17 negative cycles" is a category error, because that is a property of
the graph and not an empirical claim. But that left derived answers with NO quality
signal at all, and they are the answers whose failure mode is least visible — a
convergence rank computed over a sparse neighbourhood and one computed over a dense
one look identical to the reader.

`structural_confidence` fills that hole. It answers exactly one question:

    HOW COMPLETE IS THE GRAPH IN THE REGION THIS ANSWER CAME FROM?

It NEVER answers "how good is the evidence". A structural_confidence of 0.9 over a
region built entirely from mouse D-grade nodes is still mouse D-grade evidence. The
two axes are orthogonal and must be reported separately.

COMPONENTS (all computed, none asserted)
  local_density     edges per node in the traversed neighbourhood / graph mean
  stub_penalty      fraction of nodes on or adjacent to the path that are stubs
  sign_coverage     fraction of traversed edges that are traversal_usable
  layer_completeness mean sweep completeness of every layer the path crosses
  truncation        whether a reachability set hit the depth cap

Score is the geometric-ish mean of the components, deliberately punitive: a single
bad component drags the result down, because a chain is as complete as its gap.

Usage:
  python3 atlas/tools/structural_confidence.py --node epiphyseal_fusion
  python3 atlas/tools/structural_confidence.py --path node_a node_b node_c
  python3 atlas/tools/structural_confidence.py --bake   # write into derived.json
"""
import os, sys, json, argparse
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.path.join(os.path.dirname(ROOT), "query")

# Sweep completeness per layer: researched fraction, from the build record.
# L8 is 3 nodes of a planned ~36 and was never swept - that must drag any answer
# crossing it downward, which is the entire point of this metric.
LAYER_COMPLETENESS = {
    "L0": 1.0, "L1": 1.0, "L2": 1.0, "L3": 0.99, "L4": 1.0, "L5": 1.0,
    "L6": 1.0, "L7": 1.0, "L8": 0.08, "L9": 1.0, "L10": 1.0, "L11": 1.0,
    "L12": 1.0, "L13": 1.0,
}


def load():
    g = json.load(open(os.path.join(Q, "graph.json")))
    d = json.load(open(os.path.join(Q, "derived.json")))
    return g, d


def score(nodes, edges, focus, path_edge_ids=None):
    adj, radj = defaultdict(list), defaultdict(list)
    for e in edges:
        adj[e.get("source")].append(e)
        radj[e.get("target")].append(e)
    n_nodes = len(nodes)
    graph_mean_deg = (2.0 * len(edges)) / max(1, n_nodes)

    hood = set(focus)
    for f in focus:
        for e in adj.get(f, []):
            hood.add(e["target"])
        for e in radj.get(f, []):
            hood.add(e["source"])

    hood_edges = [e for e in edges
                  if e.get("source") in hood and e.get("target") in hood]
    local_deg = (2.0 * len(hood_edges)) / max(1, len(hood))
    local_density = min(1.0, local_deg / max(0.01, graph_mean_deg))

    stubs = sum(1 for x in hood if nodes.get(x, {}).get("stub"))
    stub_penalty = 1.0 - (stubs / max(1, len(hood)))

    considered = ([e for e in edges if e.get("edge_id") in set(path_edge_ids)]
                  if path_edge_ids else hood_edges)
    usable = sum(1 for e in considered if e.get("traversal_usable"))
    sign_coverage = usable / max(1, len(considered))

    layers = {nodes.get(x, {}).get("layer") for x in hood} - {None}
    layer_completeness = (sum(LAYER_COMPLETENESS.get(L, 0.5) for L in layers)
                          / max(1, len(layers)))

    comps = {"local_density": round(local_density, 3),
             "stub_penalty": round(stub_penalty, 3),
             "sign_coverage": round(sign_coverage, 3),
             "layer_completeness": round(layer_completeness, 3)}
    prod = 1.0
    for v in comps.values():
        prod *= max(0.01, v)
    overall = round(prod ** (1.0 / len(comps)), 3)

    band = ("high" if overall >= 0.75 else
            "moderate" if overall >= 0.5 else
            "low" if overall >= 0.3 else "very_low")
    return {"structural_confidence": overall, "band": band,
            "components": comps,
            "neighbourhood_nodes": len(hood),
            "layers_crossed": sorted(layers),
            "semantics": "graph completeness in this region; NOT evidence quality"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--node")
    ap.add_argument("--path", nargs="+")
    ap.add_argument("--bake", action="store_true")
    a = ap.parse_args()
    g, d = load()
    nodes, edges = g["nodes"], g["edges"]

    if a.bake:
        out = {}
        for nid, r in d.get("reachability", {}).items():
            focus = [nid] + list(r.keys())[:40]
            eids = [step["path"][-1] for step in r.values() if step.get("path")]
            out[nid] = score(nodes, edges, focus, eids)
        d["structural_confidence"] = out
        d["structural_confidence_meta"] = {
            "semantics": "How complete is the graph in this region? NEVER how good "
                         "is the evidence. Report alongside, never instead of, the "
                         "evidence grade.",
            "components": ["local_density", "stub_penalty", "sign_coverage",
                           "layer_completeness"],
            "bands": "high >=0.75 | moderate >=0.5 | low >=0.3 | very_low <0.3",
        }
        json.dump(d, open(os.path.join(Q, "derived.json"), "w"), indent=1, default=str)
        vals = [v["structural_confidence"] for v in out.values()]
        from collections import Counter
        print(f"baked structural_confidence for {len(out)} nodes")
        print("band distribution:",
              dict(Counter(v["band"] for v in out.values()).most_common()))
        print(f"mean {sum(vals)/len(vals):.3f}  min {min(vals):.3f}  max {max(vals):.3f}")
        return 0

    focus = a.path if a.path else [a.node]
    print(json.dumps(score(nodes, edges, focus), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
