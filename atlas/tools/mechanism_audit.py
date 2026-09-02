#!/usr/bin/env python3
"""
Phase 2d — canonical-mechanism audit target selection.

RATIONALE
The two highest-value corrections in this build (ANKH exporting ATP rather than PPi;
the zonal stiffness gradient disagreeing in DIRECTION across species and method) came
from REFUSING THE CONSENSUS FRAMING, not from searching harder. That is a repeatable
procedure, and it was never run deliberately — both corrections were opportunistic.

This tool selects the audit targets. It cannot do the audit itself, which requires
reading primary sources, but it can identify precisely which nodes are most exposed
to the failure mode: a mechanism everyone repeats, load-bearing for several edges,
whose primary evidence nobody in this build actually read.

SELECTION CRITERIA (a node scores on each)
  load_bearing     >= N edges depend on it
  review_sourced   its refs are weighted toward reviews / abstract-only reads
  unread_primary   carries `primary_abstract_only` refs, or pending_source
  no_contradiction has no `contradicts` entry - suspiciously clean for a
                   mechanism this heavily used
  high_confidence  graded A or B, so a correction would propagate widely

The last criterion is the important one and is counter-intuitive: audit the nodes you
are MOST confident about. A D-grade node that turns out wrong costs little; an A-grade
node load-bearing for 12 edges is where a silent error does real damage.

Usage:
  python3 atlas/tools/mechanism_audit.py            # rank targets
  python3 atlas/tools/mechanism_audit.py --top 25
"""
import os, sys, json, argparse
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.path.join(os.path.dirname(ROOT), "query")

WEAK = {"review", "systematic_review", "meta_analysis", "textbook",
        "conference_abstract", "thesis", "primary_abstract_only"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--min-edges", type=int, default=3)
    a = ap.parse_args()

    g = json.load(open(os.path.join(Q, "graph.json")))
    nodes, edges = g["nodes"], g["edges"]

    deg = defaultdict(int)
    for e in edges:
        deg[e.get("source")] += 1
        deg[e.get("target")] += 1

    rows = []
    for nid, n in nodes.items():
        if n.get("stub"):
            continue
        krs = [k for k in (n.get("key_refs") or []) if isinstance(k, dict)]
        if not krs:
            continue
        weak = sum(1 for k in krs if (k.get("type") or "") in WEAK)
        abstract_only = sum(1 for k in krs
                            if (k.get("type") or "") == "primary_abstract_only")
        weak_frac = weak / len(krs)
        conf = n.get("confidence")
        d = deg.get(nid, 0)
        if d < a.min_edges:
            continue

        score = 0.0
        score += min(1.0, d / 12.0) * 3.0                  # load-bearing
        score += weak_frac * 2.5                            # review-sourced
        score += (1.0 if abstract_only else 0.0) * 2.0      # primary unread
        score += (1.0 if not n.get("contradicts") else 0.0) * 1.5  # suspiciously clean
        score += (1.5 if conf in ("A", "B") else 0.0)       # correction would propagate
        score += (1.0 if n.get("pending_source") else 0.0)

        rows.append({
            "node": nid, "layer": n.get("layer"), "confidence": conf,
            "edges": d, "refs": len(krs),
            "weak_ref_frac": round(weak_frac, 2),
            "abstract_only_refs": abstract_only,
            "has_contradiction": bool(n.get("contradicts")),
            "pending_source": n.get("pending_source"),
            "score": round(score, 2),
        })

    rows.sort(key=lambda x: -x["score"])
    print(f"PHASE 2D AUDIT TARGETS (top {a.top} of {len(rows)} eligible)\n")
    print(f"{'score':>5} {'edges':>5} {'conf':>4} {'weak':>5} {'abs':>3}  node")
    print("-" * 78)
    for r in rows[:a.top]:
        print(f"{r['score']:5.2f} {r['edges']:5d} {str(r['confidence']):>4} "
              f"{r['weak_ref_frac']:5.2f} {r['abstract_only_refs']:3d}  "
              f"{r['node']} [{r['layer']}]")
    print(f"\nAudit question set, applied to each target's PRIMARY source:")
    print("  1. Does the primary data actually show the mechanism the field attributes to it?")
    print("  2. Is the mechanism direct, or is there an unnamed intermediate?")
    print("  3. Was it established in a system where the relevant alternative was present?")
    print("  4. Has a later paper revised it without the revision reaching reviews?")
    print("\nLog EVERY audit performed, including confirmations. A null result here is")
    print("evidence the node is solid and is worth recording.")
    json.dump(rows, open(os.path.join(Q, "audit_targets.json"), "w"), indent=1)
    print(f"\nwrote query/audit_targets.json ({len(rows)} ranked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
