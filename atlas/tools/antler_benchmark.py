#!/usr/bin/env python3
"""
THE ANTLER BENCHMARK - a mammal runs endochondral elongation 365 times faster
than a human growth plate, and the atlas had one passing mention of it.

WHY THIS MATTERS NOW
--------------------
Round 198 established the objective function: adult height is RESERVE times
terminal cell height, fusion is triggered by exhaustion of proliferative
potential, and every intervention that raises rate spends reserve faster. The
atlas's own coverage audit had already reached the uncomfortable version of
this - two men with zero lifetime oestrogen signal reached 197 and 204 cm, one
of them stopping at 24 with plates still ANATOMICALLY OPEN. Growth stopped
while the door was still open. The budget, not the closure, is binding.

So the only question left worth asking is whether the budget is a mammalian
constant. IT IS NOT, AND THE COUNTEREXAMPLE IS ENORMOUS.

ba2025 states the comparison in its own abstract: deer antler, regenerating by
endochondral ossification, elongates UP TO 2 CM PER DAY, "far surpassing the
~2 cm annual growth of human growth plates".

AUTHOR-STATED INPUTS ONLY. Everything below is arithmetic on those two numbers
plus figures already held in this atlas.
"""

ANTLER_CM_PER_DAY = 2.0        # ba2025, author-stated upper figure
HUMAN_CM_PER_YEAR = 2.0        # ba2025, author-stated, per growth plate
ANTLER_SEASON_DAYS = 120       # nominal growth season; NOT from ba2025

# atlas-held human figures, for scale
HUMAN_PUBERTAL_PEAK_CM_PER_YEAR = 9.5   # nominal peak height velocity, whole body
HUMAN_FEMUR_CM = 48.0                   # nominal adolescent male femur


def main():
    print("=" * 78)
    print("ANTLER VERSUS HUMAN GROWTH PLATE - THE RATE GAP")
    print("=" * 78)
    per_year = ANTLER_CM_PER_DAY * 365.0
    print(f"    antler                 : {ANTLER_CM_PER_DAY:.1f} cm/day"
          f"  = {per_year:,.0f} cm/year if sustained")
    print(f"    human growth plate     : {HUMAN_CM_PER_YEAR:.1f} cm/YEAR")
    print(f"    ratio                  : {per_year / HUMAN_CM_PER_YEAR:,.0f}x")
    print(f"    per season ({ANTLER_SEASON_DAYS} d)     : "
          f"{ANTLER_CM_PER_DAY * ANTLER_SEASON_DAYS:.0f} cm of new bone")
    print(f"    same, as human femurs  : "
          f"{ANTLER_CM_PER_DAY * ANTLER_SEASON_DAYS / HUMAN_FEMUR_CM:.1f} femurs "
          "grown from nothing, annually")

    print("\n[1] WHAT ba2025 ATTRIBUTES IT TO, IN ITS OWN TERMS")
    for i, x in enumerate([
        "a VAST stem-progenitor pool in the antler growth centre",
        "vigorous proliferation supported by paracrine signalling",
        "a transcriptional programme with intrinsically LOW TUMORIGENIC "
        "potential, associated with apoptotic regulation",
        "a RICHLY VASCULARISED niche supporting angiogenesis and efficient "
        "recruitment of osteogenic cells",
        "HYBRID ossification - endochondral plus direct hypertrophic "
        "chondrocyte-to-osteoblast transdifferentiation via PHEX+ intermediates",
    ], 1):
        print(f"    ({i}) {x}")

    print("\n[2] READ AGAINST THE ATLAS DECOMPOSITION, ONLY ONE OF THOSE IS")
    print("    AN AMPLIFICATION CLAIM, AND IT IS NOT THE MAIN ONE")
    print("    growth rate = POOL x AMPLIFICATION x h_term.")
    print("    Items (1) and (4) are POOL terms. Item (2) is rate within the")
    print("    pool. Item (5) changes what happens AFTER the cell has already")
    print("    delivered its length, so it cannot be a length term. Nothing in")
    print("    the list is an amplification claim.")
    print("    THE ANTLER'S ADVANTAGE IS A POOL ADVANTAGE, and the atlas has")
    print("    spent most of its effort on amplification.")

    print("\n[3] THE POINT THE ABSTRACT DOES NOT MAKE, AND IT IS THE USEFUL ONE")
    print("    An antler is CAST AND REGROWN every year from the pedicle")
    print("    periosteum. Its budget is not larger than a human's - it is")
    print("    RENEWABLE. The reserve is refilled annually from a stem")
    print("    reservoir OUTSIDE the growth centre. ba2025's companion work")
    print("    identifies RXFP2+ mesenchymal stem cells in the antlerogenic")
    print("    periosteum as that source.")
    print("    THAT IS ROUTE 8 OF THIS ATLAS'S OWN ENUMERATION - external")
    print("    recruitment - the route round 179 listed as never costed.")
    print("    The largest natural experiment in endochondral growth runs on")
    print("    the one route the atlas never worked.")

    print("\n[4] THE VASCULAR INVERSION, WHICH CUTS BOTH WAYS")
    print("    The antler growth centre is RICHLY VASCULAR. The human growth")
    print("    plate is avascular and alymphatic - ye2026 names exactly that")
    print("    as the reason drugs cannot reach it. The resting zone is the")
    print("    most hypoxic compartment in the plate.")
    print("    ONE READING: the human reserve is starved, and vascularity is")
    print("    part of what the antler buys. Against it: hypoxia is what keeps")
    print("    resting-zone cells quiescent and stem-like, and vascular")
    print("    invasion of a growth plate is what FUSION IS. Type H vessel")
    print("    ingrowth into the plate ends it.")
    print("    So vascularising a human plate is either the lever or the")
    print("    fusion trigger, and nothing in the atlas distinguishes them.")

    print("\n[5] THE CONSERVED GENE THAT LINKS THE TWO TISSUES")
    print("    hu2025: PRRX1 drives miR-143-3p in antler RESERVE mesenchymal")
    print("    cells, and PRRX1 overexpression DECREASES their proliferation")
    print("    while maintaining the undifferentiated state.")
    print("    chu2026: PRRX1 marks the 'root' stem cell of the human and mouse")
    print("    growth plate resting zone, the population upstream of the")
    print("    PTHrP-positive cells.")
    print("    THE SAME TRANSCRIPTION FACTOR GUARDS THE RESERVE IN BOTH")
    print("    TISSUES, and in the antler it does so by holding cells back.")
    print("    That is a quiescence switch with a known direction, in the one")
    print("    system where the reserve is demonstrably not limiting.")
    print("=" * 78)


if __name__ == "__main__":
    main()
