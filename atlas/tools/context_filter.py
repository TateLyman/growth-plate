#!/usr/bin/env python3
"""
Context-filtered traversal with THREE-STATE semantics (MR-004 item 1).

THE BUG THIS FIXES
Identical class to the reachability defect fixed in Phase 5, in a different field.
Edge context is free text; zone appears in ~5% of edges and sex in ~10%. A naive
context filter drops an edge when the requested value is absent from the string —
so the overwhelming majority of edges are excluded for MISSING ANNOTATION, not for
context mismatch. The surviving set then looks like a small propagation result and
is indistinguishable from one.

Three states, never collapsed:
    MATCH        the context string affirms the requested value
    MISMATCH     the context string affirms a DIFFERENT value on that axis
    UNANNOTATED  the axis is not mentioned at all

Only MISMATCH is a reason to exclude an edge. UNANNOTATED edges are carried, and
counted, and the answer reports what fraction of the path rested on them.

If annotation coverage on the traversed subgraph falls below the threshold, the
result is returned as UNRELIABLE with the coverage figure attached — not as a
small answer.

Usage:
  python3 atlas/tools/context_filter.py --node glucocorticoid_receptor --sex female --age 11
  python3 atlas/tools/context_filter.py --node fgfr3_receptor --zone hypertrophic
  python3 atlas/tools/context_filter.py --coverage-report
"""
import os, sys, json, re, argparse
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.path.join(os.path.dirname(ROOT), "query")
SIGN = {"+": 1, "-": -1}
UNRELIABLE_THRESHOLD = 0.40   # annotation coverage below this => UNRELIABLE

# Explicit-unknown markers written by the MR-004 context-fill campaign. An explicit
# unknown is honest annotation and is queryable, but it is NOT coverage - the axis
# still carries no value. classify() already returns UNANNOTATED for these because no
# value pattern matches; these patterns exist so the two can be COUNTED separately.
PROV = {"explicit_unknown": {
    "zone": r"zone unknown", "sex": r"sex unknown",
    "stage": r"age/stage unknown", "species": r"species unknown"}}

# Where a zone annotation came from. Written inline on the edge by the fill campaign.
ZONE_PROVENANCE = {
    "resolved in the cited source": r"zones? resolved in source",
    "inferred from endpoint localization records":
        r"zonal localization of the interacting nodes",
}

AXES = {
    "zone": {
        "resting": r"\b(RZ|resting|reserve)\b",
        "proliferative": r"\b(PZ|proliferat\w*)\b",
        "prehypertrophic": r"\b(PHZ|prehypertroph\w*)\b",
        "hypertrophic": r"\b(HZ|hypertroph\w*)\b",
        "perichondrium": r"\b(perichondr\w*|groove of Ranvier|LaCroix)\b",
    },
    "sex": {
        "female": r"\b(female|girls?|women)\b",
        "male": r"\b(male|boys?|men)\b",
        "both": r"\b(both sexes|either sex|sex-independent)\b",
    },
    "stage": {
        "fetal": r"\b(fetal|foetal|embryon\w*|prenatal|E\d+)\b",
        "infant": r"\b(infant\w*|neonat\w*|P\d+\b)\b",
        "child": r"\b(child\w*|prepubert\w*|juvenile)\b",
        "pubertal": r"\b(pubert\w*|adolescen\w*|peri-?pubert\w*)\b",
        "adult": r"\b(adult|mature|skeletally mature)\b",
    },
    "species": {
        "human": r"\bhuman\b", "mouse": r"\b(mouse|mice|murine)\b",
        "rat": r"\brat\b", "rabbit": r"\brabbit\b",
    },
}


def classify(ctx, axis, want):
    """Return MATCH / MISMATCH / UNANNOTATED for one axis."""
    pats = AXES[axis]
    present = [v for v, p in pats.items() if re.search(p, ctx, re.I)]
    if not present:
        return "UNANNOTATED"
    if want is None:
        return "MATCH"
    return "MATCH" if want in present else "MISMATCH"


def load():
    g = json.load(open(os.path.join(Q, "graph.json")))
    return g["nodes"], g["edges"]


def filtered_reach(nodes, edges, start, want, max_depth=4):
    adj = defaultdict(list)
    for e in edges:
        if e.get("traversal_usable"):
            adj[e.get("source")].append(e)

    stats = {"considered": 0, "excluded_mismatch": 0, "carried_unannotated": 0,
             "carried_match": 0}
    per_axis = {ax: {"MATCH": 0, "MISMATCH": 0, "UNANNOTATED": 0} for ax in want}

    out, frontier = {}, [(start, 1, 0, [], 0, 0)]
    while frontier:
        node, sgn, d, path, n_unann, n_tot = frontier.pop()
        if d >= max_depth:
            continue
        for e in adj.get(node, []):
            ctx = str(e.get("context") or "")
            stats["considered"] += 1
            verdicts = {ax: classify(ctx, ax, v) for ax, v in want.items()}
            for ax, vd in verdicts.items():
                per_axis[ax][vd] += 1
            if "MISMATCH" in verdicts.values():
                stats["excluded_mismatch"] += 1
                continue
            unann = sum(1 for v in verdicts.values() if v == "UNANNOTATED")
            if unann:
                stats["carried_unannotated"] += 1
            else:
                stats["carried_match"] += 1
            s = SIGN.get(str(e.get("sign")))
            if s is None:
                continue
            t, ns = e["target"], sgn * s
            nu, nt = n_unann + (1 if unann else 0), n_tot + 1
            if t not in out or len(path) + 1 < out[t]["depth"]:
                out[t] = {"sign": ns, "depth": len(path) + 1,
                          "path": path + [e["edge_id"]],
                          "unannotated_edges_on_path": nu,
                          "path_len": nt,
                          "annotation_coverage_on_path":
                              round(1 - nu / max(1, nt), 3)}
                frontier.append((t, ns, d + 1, path + [e["edge_id"]], nu, nt))

    carried = stats["carried_match"] + stats["carried_unannotated"]
    cov = stats["carried_match"] / max(1, carried)
    return out, stats, per_axis, cov


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--node")
    ap.add_argument("--zone"); ap.add_argument("--sex")
    ap.add_argument("--stage"); ap.add_argument("--species")
    ap.add_argument("--age", type=float)
    ap.add_argument("--coverage-report", action="store_true")
    a = ap.parse_args()
    nodes, edges = load()

    if a.coverage_report:
        n = len(edges)
        print("EDGE CONTEXT ANNOTATION COVERAGE (three-state)\n")
        print("DETERMINED = the axis carries a value. An explicit 'zone unknown' is honest")
        print("annotation and is NOT coverage - it classifies as UNANNOTATED here, which is")
        print("why these numbers are already determined-only.\n")
        for ax in AXES:
            det = sum(1 for e in edges
                      if classify(str(e.get("context") or ""), ax, None) == "MATCH")
            unk = sum(1 for e in edges
                      if re.search(PROV["explicit_unknown"][ax], str(e.get("context") or ""), re.I))
            print(f"  {ax:9s} determined {det:5d}/{n} = {100*det/n:5.1f}%   "
                  f"explicitly unknown {unk:5d} = {100*unk/n:5.1f}%")
        print("\nZONE PROVENANCE - determined is not one thing, and the three tiers are")
        print("not equally strong:")
        tiers = {k: sum(1 for e in edges
                        if re.search(v, str(e.get("context") or ""), re.I))
                 for k, v in ZONE_PROVENANCE.items()}
        zdet = sum(1 for e in edges
                   if classify(str(e.get("context") or ""), "zone", None) == "MATCH")
        tiers["definitional (an endpoint node IS a zone)"] = (
            zdet - tiers["resolved in the cited source"]
            - tiers["inferred from endpoint localization records"])
        for k in ["resolved in the cited source",
                  "definitional (an endpoint node IS a zone)",
                  "inferred from endpoint localization records"]:
            print(f"  {k:46s} {tiers[k]:5d} = {100*tiers[k]/n:5.1f}%")
        strong = (tiers["resolved in the cited source"]
                  + tiers["definitional (an endpoint node IS a zone)"])
        print(f"  {'-> STRONG (source-resolved + definitional)':46s} {strong:5d} "
              f"= {100*strong/n:5.1f}%")
        print("\nA zone-filtered answer resting on the inferred tier is a statement about")
        print("where the ENTITIES live, not where the INTERACTION was observed.")
        print(f"\nUNRELIABLE threshold: annotation coverage < "
              f"{UNRELIABLE_THRESHOLD:.0%} on the traversed subgraph")
        return 0

    want = {}
    if a.zone: want["zone"] = a.zone
    if a.sex: want["sex"] = a.sex
    if a.species: want["species"] = a.species
    if a.stage: want["stage"] = a.stage
    elif a.age is not None:
        want["stage"] = ("infant" if a.age < 2 else "child" if a.age < 10
                         else "pubertal" if a.age < 18 else "adult")
    if not want:
        print("no context axes requested; use unfiltered reachability instead")
        return 2

    out, stats, per_axis, cov = filtered_reach(nodes, edges, a.node, want)
    reliable = cov >= UNRELIABLE_THRESHOLD
    res = {
        "node": a.node, "filter": want,
        "reachable_count": len(out),
        "edges_considered": stats["considered"],
        "excluded_MISMATCH": stats["excluded_mismatch"],
        "carried_MATCH": stats["carried_match"],
        "carried_UNANNOTATED": stats["carried_unannotated"],
        "annotation_coverage": round(cov, 3),
        "per_axis": per_axis,
        "verdict": "RELIABLE" if reliable else "UNRELIABLE",
        "interpretation": (
            "Result is constrained by real context annotation."
            if reliable else
            f"UNRELIABLE: only {cov:.1%} of carried edges were actually annotated on "
            f"the requested axes. The remainder were carried as UNANNOTATED, not "
            f"excluded - so this set is NOT a context-specific answer. It is the "
            f"unfiltered set minus the few edges that positively contradict the "
            f"filter. Do not present it as sex- or zone-specific."),
        "top_targets": sorted(
            ({"node": k, **v} for k, v in out.items()),
            key=lambda x: (x["depth"], -x["annotation_coverage_on_path"]))[:15],
    }
    print(json.dumps(res, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
