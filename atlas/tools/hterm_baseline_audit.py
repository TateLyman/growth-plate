#!/usr/bin/env python3
"""
THE h_term LEDGER, RE-READ BY BASELINE - and round 205 conflated two different
things.

WHY THIS TOOL EXISTS
--------------------
Round 205 concluded that "the whole observed range of h_term across every agent
this atlas holds is roughly 1.0 to 1.4x", and used that to argue the free axis is
worth only about forty per cent. THAT NUMBER MIXES TWO INCOMPATIBLE BASELINES and
the distinction decides whether the axis is worth anything to a GH-replete
subject.

  RESTORATION  a deficient animal returned toward normal. The ceiling is the
               normal animal, and the number tells you nothing about what
               happens ABOVE normal.
  ELEVATION    a normal, untreated animal pushed above its own baseline. This
               is the only kind of number that applies to a person who is not
               hormone-deficient.

The subject of this programme is not growth-hormone deficient. Every restoration
number is therefore inadmissible as a prediction for them, and round 205 quoted
the largest restoration number in the file as though it were a ceiling.
"""

# ref, agent, baseline type, control value, treated value, species, tissue, note
ROWS = [
    ("hunziker1994", "GH vs hypophysectomised", "RESTORATION", 19.5, 26.5,
     "rat", "proximal tibia",
     "the control is a HYPOPHYSECTOMISED animal - a deficiency state"),
    ("hunziker1994", "IGF-I vs hypophysectomised", "RESTORATION", 19.5, 27.3,
     "rat", "proximal tibia",
     "same deficient control"),
    ("hunziker1994", "intact normal vs hypophysectomised", "RESTORATION", 19.5, 29.8,
     "rat", "proximal tibia",
     "THE CEILING OF RESTORATION - what an intact animal has. Note GH at 26.5 does "
     "not reach it"),
    ("weber2025", "Npr3 loss vs wild-type sibling", "ELEVATION", 1.00, 1.20,
     "mouse", "tail vertebrae",
     "ratio only; control is a NORMAL littermate"),
    ("trompet2024", "SAG bead vs contralateral DMSO, femur, 1 month", "ELEVATION", 26.72, 31.46,
     "rat", "distal femur",
     "control is the contralateral limb of the SAME normal animal"),
    ("trompet2024", "SAG bead vs contralateral DMSO, tibia, 1 month", "ELEVATION", 25.99, 32.38,
     "rat", "proximal tibia",
     "same design; the largest elevation in the file"),
    ("trompet2024", "SAG bead, femur, 2 months", "ELEVATION", 21.87, 20.29,
     "rat", "distal femur",
     "THE SAME AGENT AT A LATER TIMEPOINT - the elevation does not persist"),
]


def rule(c="="):
    print(c * 90)


def main():
    rule()
    print("EVERY TERMINAL-CELL-HEIGHT NUMBER IN THE ATLAS, SORTED BY WHAT ITS CONTROL WAS")
    rule()
    print(f"\n    {'ref':<14} {'baseline':<12} {'ctrl':>7} {'treated':>8} {'ratio':>7}  agent")
    for ref, agent, kind, c, t, sp, tis, note in ROWS:
        print(f"    {ref:<14} {kind:<12} {c:>7.2f} {t:>8.2f} {t/c:>7.3f}  {agent}")

    rest = [r for r in ROWS if r[2] == "RESTORATION"]
    elev = [r for r in ROWS if r[2] == "ELEVATION"]

    print("\n[1] THE TWO POPULATIONS ARE NOT THE SAME MEASUREMENT")
    rmax = max(t / c for *_, c, t, _, _, _ in [(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]) for r in rest])
    print(f"    RESTORATION, largest ratio : {rmax:.2f}x  (hypophysectomised -> intact)")
    peak = [r for r in elev if r[4] / r[3] == max(x[4] / x[3] for x in elev)][0]
    print(f"    ELEVATION,  largest ratio  : {peak[4]/peak[3]:.2f}x  ({peak[0]}, {peak[1]})")
    print("\n    ROUND 205 QUOTED hunziker1994's 1.36x ALONGSIDE weber2025's 1.20x AS IF")
    print("    THEY WERE THE SAME KIND OF NUMBER. They are not. 1.36x is what growth")
    print("    hormone does to a HYPOPHYSECTOMISED rat, and it does not even reach the")
    print("    intact animal's 29.8 micrometres. It is a deficiency-correction number.")

    print("\n[2] WHAT THAT DOES TO THE STACK, AND IT CUTS BOTH WAYS")
    print("    AGAINST GH: the subject of this programme is NOT growth-hormone")
    print("    deficient. In a GH-replete animal h_term is ALREADY at the top of the")
    print("    restoration range - hunziker1994's intact controls sit at 29.8 against")
    print("    26.5 on GH-treated hypophysectomised. THERE IS NO EVIDENCE ANYWHERE THAT")
    print("    GH RAISES h_term ABOVE A NORMAL BASELINE, and the number the atlas has")
    print("    been carrying for it cannot support that claim.")
    print("\n    FOR THE OTHER AGENTS: the elevation numbers are measured against normal")
    print("    controls and they are real. Two independent agents - NPR3 loss and a")
    print("    hedgehog agonist - both give about 20 per cent ABOVE a normal baseline,")
    print("    in different species and different bones.")

    ratios = [r[4] / r[3] for r in elev if r[4] > r[3]]
    print(f"\n[3] SO THE HEADROOM ABOVE NORMAL IS ABOUT {100*(sum(ratios)/len(ratios)-1):.0f} PER CENT, NOT ZERO")
    print("    and it is NOT the same as the 40 per cent round 205 implied. Restated:")
    print("      - restoring a deficient plate to normal      up to 1.53x")
    print(f"      - pushing a NORMAL plate above its baseline   about "
          f"{sum(ratios)/len(ratios):.2f}x on present evidence")
    print("    The second number is the one that applies here, and it rests on two")
    print("    studies in two species with no combination arm between them.")

    print("\n[4] THE ADDITIVITY QUESTION, RESTATED CORRECTLY")
    print("    The question is NOT 'do GH and a CNP agent add on h_term'. On the")
    print("    evidence GH has no demonstrated h_term effect above normal at all, so")
    print("    there is nothing for it to add TO. The real question is whether the two")
    print("    agents that DO elevate above normal - the hedgehog arm and the")
    print("    natriuretic arm - share a ceiling. THEY HAVE NEVER BEEN GIVEN TOGETHER.")
    print("    And round 205 showed the hedgehog elevation does not survive to two")
    print("    months, so even the single-agent effect may not be bankable.")
    rule()


if __name__ == "__main__":
    main()
