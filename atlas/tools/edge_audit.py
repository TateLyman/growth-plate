#!/usr/bin/env python3
"""
Edge context audit + principled sign repair (Phase 5b).

WHY SIGN COVERAGE IS NOT A SINGLE NUMBER
Not every relation carries a sign. `precedes` is a TEMPORAL ordering: "primary
ossification centre precedes growth plate" has no + or -, and forcing one on it
would be fabrication dressed as completeness. So raw sign coverage over all edges
is the wrong metric. What matters is coverage over SIGN-BEARING relations - the
ones a perturbation traversal actually multiplies through.

Three classes:
  SIGN_BEARING   sign is meaningful and required for perturbation reasoning
  SIGN_ENTAILED  sign follows from the relation's definition, so it can be set
                 without consulting a source (documented, not silent):
                   required_for      -> '+'  (remove X and Y falls)
                   sufficient_for    -> '+'
                   differentiates_into -> '+' (lineage flow)
                   transcribes       -> '+'
                   degrades          -> '-'
  SIGN_EXEMPT    sign is not meaningful; edge is excluded from the metric and
                 marked traversal_usable: false for perturbation queries
                   precedes          temporal ordering
                   binds             association without direction
                   hypothesized_link speculative by construction
                   correlates_with   sign IS meaningful but is the DIRECTION of a
                                     measured correlation - it cannot be inferred
                                     from the relation type. Left unsigned edges
                                     are marked unusable rather than guessed.

Usage:
  python3 atlas/tools/edge_audit.py            # report only
  python3 atlas/tools/edge_audit.py --fix      # apply entailed signs + usability flags
"""
import os, sys, re, argparse
from collections import Counter
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDGES = os.path.join(ROOT, "edges", "edges.yaml")

SIGN_ENTAILED = {"required_for": "+", "sufficient_for": "+",
                 "differentiates_into": "+", "transcribes": "+", "degrades": "-"}
SIGN_BEARING = {"activates", "inhibits", "phosphorylates", "secretes"} | set(SIGN_ENTAILED)
SIGN_EXEMPT = {"precedes", "binds", "hypothesized_link", "correlates_with"}

# BUG FIXED 2026-08-05, found by the context-fill campaign. Every stem alternative here
# (proliferat, hypertroph, embryon, ...) was written with a TRAILING \b, which cannot
# match inside a word - so "proliferative" and "hypertrophic", the two commonest zone
# words in the corpus, never matched and zone fill was under-reported as 18.3% against a
# real 53.9%. The trailing boundary is removed; the leading one is kept so that
# "metaphyseal" still requires a word start. Any zone/stage figure quoted from this tool
# before this date is wrong and low.
PROBES = {
    "zone": r"\b(RZ|PZ|PHZ|HZ)\b|\b(resting|proliferat|prehypertroph|hypertroph|perichondr|ZPC|epiphys|metaphys)",
    "species": r"\b(human|mouse|murine|rat|rabbit|bovine|porcine|ovine|chick|zebrafish|in vitro|iPSC)\b",
    "stage_age": r"\b(E\d|P\d)\b|\b(postnatal|prenatal|fetal|embryon|adult|pubert|neonat|week|month|year|age|infan)",
    "sex": r"\b(male|female|both sexes|sex-|sex differ)",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    a = ap.parse_args()

    doc = yaml.safe_load(open(EDGES))
    edges = doc["edges"]
    n = len(edges)

    print(f"EDGES: {n}\n--- context field fill rates ---")
    for f in ["sign", "context", "magnitude", "evidence_tier", "refs", "confidence",
              "timescale", "notes"]:
        c = sum(1 for x in edges if x.get(f) not in (None, "", [], "unknown"))
        print(f"  {f:16s} {c:4d}/{n}  {100*c/n:5.1f}%")

    print("\n--- context STRING coverage (fields are packed into free text) ---")
    for k, pat in PROBES.items():
        c = sum(1 for x in edges if re.search(pat, str(x.get("context") or ""), re.I))
        print(f"  {k:16s} {c:4d}/{n}  {100*c/n:5.1f}%")

    fixed_sign = fixed_flag = 0
    if a.fix:
        for x in edges:
            rel = x.get("relation")
            s = str(x.get("sign") or "")
            if rel in SIGN_ENTAILED and s in ("", "None", "unknown"):
                x["sign"] = SIGN_ENTAILED[rel]
                x["sign_basis"] = "entailed_by_relation"
                fixed_sign += 1
            usable = not (rel in SIGN_EXEMPT
                          or str(x.get("sign") or "") in ("", "None", "unknown"))
            if x.get("traversal_usable") != usable:
                x["traversal_usable"] = usable
                fixed_flag += 1
        yaml.safe_dump(doc, open(EDGES, "w"), sort_keys=False,
                       default_flow_style=False, width=120, allow_unicode=True)

    # metric computed over SIGN-BEARING relations only
    bearing = [x for x in edges if x.get("relation") in SIGN_BEARING]
    signed = [x for x in bearing if str(x.get("sign") or "") in ("+", "-", "biphasic")]
    exempt = [x for x in edges if x.get("relation") in SIGN_EXEMPT]
    usable = [x for x in edges if x.get("traversal_usable")]

    print(f"\n--- SIGN COVERAGE (the gate) ---")
    print(f"  sign-bearing relations      : {len(bearing)}")
    print(f"  of those, signed            : {len(signed)}  "
          f"= {100*len(signed)/max(1,len(bearing)):.1f}%   <- GATE (>=90%)")
    print(f"  sign-exempt relations       : {len(exempt)} "
          f"({dict(Counter(x.get('relation') for x in exempt))})")
    print(f"  traversal_usable edges      : {len(usable)}/{n} "
          f"= {100*len(usable)/n:.1f}%")
    print(f"  UNUSABLE for perturbation   : {n-len(usable)} "
          f"(flagged, not silently traversed)")
    if a.fix:
        print(f"\n  entailed signs applied: {fixed_sign}; usability flags set: {fixed_flag}")

    unsigned_bearing = [x for x in bearing if str(x.get("sign") or "") not in ("+", "-", "biphasic")]
    if unsigned_bearing:
        print(f"\n  sign-bearing but UNSIGNED ({len(unsigned_bearing)}) - genuine defects:")
        for x in unsigned_bearing[:15]:
            print(f"    {x['edge_id']}: {x['source']} -{x['relation']}-> {x['target']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
