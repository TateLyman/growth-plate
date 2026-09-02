#!/usr/bin/env python3
"""
FUSION IS TRIGGERED BY EXHAUSTION OF PROLIFERATIVE POTENTIAL, NOT BY A CLOCK.
What that single fact does to every agent in the stack.

WHY THIS TOOL EXISTS
--------------------
Gap g_l12_is_the_pth1r_acceleration_banked_or_does_it_advance_fusion has been
the decisive open question since round 194: the rat gains femoral length at
interim and gives it back by terminal, and no rat can settle whether the gain
would be BANKED in a species whose plate fuses, because the rat never fuses.

weise2001 settles it in a species that does fuse, and it settles it against
the optimistic reading. Juvenile ovariectomised rabbits, growth plates from
proximal tibia, distal tibia and distal femur at 2, 4, 6 and 8 weeks:

  "epiphyseal fusion is triggered when the proliferative potential of growth
   plate chondrocytes is exhausted"
  "Fusion occurred when the rate of chondrocyte proliferation approached zero"
  oestrogen "does not induce growth plate ossification directly; instead,
   estrogen accelerates the programmed senescence of the growth plate, thus
   causing earlier proliferative exhaustion and consequently earlier fusion"

That is a FIXED-RESERVE model. The plate carries a finite number of remaining
divisions. Fusion happens when they run out. Time is not the trigger; spending
is.

THE ARITHMETIC BELOW IS A MODEL, NOT A MEASUREMENT. It is written to expose
which agents change the reserve and which merely change the rate of spending
it, because under a fixed reserve those two have opposite consequences for
adult height and the literature routinely conflates them.
"""

# What each agent does, per the atlas, on the two terms that matter under a
# fixed-reserve model:
#   reserve  - does it change the number of divisions remaining?
#   rate     - does it change how fast they are spent?
AGENTS = {
    "anastrozole (aromatase inhibition)": {
        "reserve": "PRESERVES - removes the oestrogen drive that accelerates "
                   "senescence, so the reserve is spent more slowly per unit "
                   "time (weise2001: oestrogen accelerates programmed "
                   "senescence and brings fusion forward)",
        "rate": "may LOWER - chou2025 shows oestrogen acting through GPER-1 "
                "sustains the PTHrP/Ihh ratio and the proliferative zone, so "
                "removing oestrogen may also lower proliferation",
        "verdict": "the only agent in the stack whose primary action is on the "
                   "RESERVE. This is why it works.",
    },
    "growth hormone": {
        "reserve": "SPENDS - round 183, hunziker1994 flux decomposition: GH "
                   "raises resting-zone pool consumption 5.00x while "
                   "amplification falls to 0.77",
        "rate": "RAISES - growth rate 31 to 163 micrometres per day in the "
                "hypophysectomised rat series",
        "verdict": "buys rate by spending reserve. Under a fixed reserve that "
                   "is a loan, not income, unless fusion is time-triggered - "
                   "and weise2001 says it is not.",
    },
    "vosoritide / CNP": {
        "reserve": "UNKNOWN - assigned to terminal cell height from a "
                   "hypertrophic zone thickness, which CORR-189 forbids "
                   "reading as a cell-height claim",
        "rate": "RAISES in achondroplasia",
        "verdict": "term assignment unverified; the h_term axis does not "
                   "consume divisions, which would make it the safe axis if "
                   "the assignment were secure.",
    },
    "erdafitinib (FGFR3 inhibition)": {
        "reserve": "UNKNOWN - gap "
                   "g_l2_does_fgfr3_inhibition_raise_cells_per_column_or_only_"
                   "zone_height",
        "rate": "RAISES in FGFR3 gain-of-function states",
        "verdict": "unresolved, and it matters: if FGFR3 inhibition works by "
                   "raising throughput it is a second GH.",
    },
    "teriparatide (PTH1R agonism)": {
        "reserve": "NEITHER - endogenous PTH1R tone PRESERVES the pool "
                   "(correa2010: losing the effector collapses the resting "
                   "zone from 5-plus layers to 1-2; hirai2011: postnatal "
                   "receptor deletion destroys the plate), but the system is "
                   "SATURATED, so adding agonist adds nothing",
        "rate": "NO CHANGE in any wild-type animal or randomised human trial",
        "verdict": "not harmful to the reserve, and not useful either. The "
                   "saturation is the whole finding.",
    },
}


def main():
    print("=" * 84)
    print("FIXED-RESERVE MODEL OF FUSION, AND WHAT IT DOES TO THE STACK")
    print("=" * 84)
    print("\nweise2001, rabbit, a species that FUSES:")
    print("  fusion is triggered by exhaustion of proliferative potential;")
    print("  it occurs when the proliferation rate approaches zero;")
    print("  oestrogen accelerates senescence rather than ossifying directly.")
    print("\nTHE CONSEQUENCE, STATED PLAINLY:")
    print("  adult height = reserve x terminal cell height, NOT rate x time.")
    print("  An agent that only raises rate brings fusion forward by exactly")
    print("  as much as it raises growth, and banks nothing. An agent that")
    print("  raises the RESERVE, or the height of each terminal cell, adds")
    print("  adult height.")

    print("\n" + "=" * 84)
    print("EVERY AGENT IN THE STACK, SORTED BY WHICH TERM IT TOUCHES")
    print("=" * 84)
    for name, d in AGENTS.items():
        print(f"\n{name}")
        print(f"    reserve : {d['reserve']}")
        print(f"    rate    : {d['rate']}")
        print(f"    VERDICT : {d['verdict']}")

    print("\n" + "=" * 84)
    print("[1] THIS RETROSPECTIVELY EXPLAINS THE RAT TERMINAL TABLE")
    print("=" * 84)
    print("    Round 194: femur length 32.8 -> 33.9 mm at 8 months under")
    print("    teriparatide, 34.2 -> 35.2 mm at 12 months, and 35 mm in EVERY")
    print("    arm at 26 months. A fixed reserve predicts exactly that shape:")
    print("    treated animals arrive at the ceiling earlier and stop. The rat")
    print("    never fuses, so the ceiling is asymptotic rather than abrupt,")
    print("    but the accounting is the same.")

    print("\n[2] AND IT CLOSES THE GAP THAT HAS BEEN OPEN SINCE ROUND 194")
    print("    The question was whether an accelerated six months is BANKED in")
    print("    a fusing species or merely brings fusion forward. weise2001")
    print("    answers it in a fusing species: the trigger is exhaustion, so")
    print("    acceleration is not banked. THE ANSWER IS NEGATIVE, and it is")
    print("    negative for GH as much as for teriparatide.")

    print("\n[3] THE NEW QUESTION THIS OPENS, WHICH IS STACK-SPECIFIC")
    print("    chou2025: oestrogen acting through GPER-1 SUSTAINS the growth")
    print("    plate PTHrP/Ihh ratio; blocking or deleting GPER-1 lowers it and")
    print("    expands the hypertrophic zone. Anastrozole removes oestrogen.")
    print("    If aromatase inhibition lowers growth-plate PTHrP tone, it moves")
    print("    the plate DOWN the inverted U established in round 197 - and a")
    print("    plate below the optimum is the one state in which a PTH1R")
    print("    agonist has ever added length.")
    print("    THE STACK MAY MANUFACTURE ITS OWN INDICATION. That is a specific,")
    print("    testable prediction and nobody has tested it.")

    print("\n[4] THE COUNTERWEIGHT, WHICH IS EQUALLY SPECIFIC")
    print("    Oestrogen has two opposing arms at the plate. Through GPER-1 it")
    print("    is pro-proliferative and pro-PTHrP (chou2025). Through the")
    print("    senescence programme it spends the reserve (weise2001). An")
    print("    aromatase inhibitor removes both. The reason it nets positive")
    print("    for adult height in humans is that the reserve arm dominates.")
    print("    Adding a PTH1R agonist to replace the lost GPER-1 arm would")
    print("    restore proliferation - which under a fixed reserve is the arm")
    print("    you did not want back.")
    print("    So the stack-specific hypothesis is self-limiting: the deficit")
    print("    anastrozole creates is a RATE deficit, and rate is not what sets")
    print("    adult height.")
    print("=" * 84)


if __name__ == "__main__":
    main()
