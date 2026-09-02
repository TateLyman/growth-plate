#!/usr/bin/env python3
"""
THE VOSORITIDE TERM ASSIGNMENT, FROM A PRIMATE - and it is not the favourable one.

WHY THIS TOOL EXISTS
--------------------
Round 203 concluded, after obtaining and exhaustively searching the two candidate
full texts, that NO CELL-LEVEL MEASUREMENT EXISTED under any CNP-axis agent. That
was wrong, and the paper that disproves it was one this atlas held as a ref_id
with no finding and no note: wendt2015, the BMN 111 (vosoritide) preclinical
paper, supplied by the user.

Its Table 3 carries, in CYNOMOLGUS MONKEYS at 6 months, four of the five
quantities the Hunziker decomposition needs, in the same animals. Nothing else on
this pathway comes close.

EVERY VALUE BELOW IS AUTHOR-STATED, read from a 500 dpi render of Table 3.
"""
import math

# wendt2015 Table 3, cynomolgus monkey, 6 months, n = 4 per group.
# ANOVA with Tukey post hoc versus vehicle. Author-stated mean +/- S.D.
#                          vehicle   2.25 nmol/kg/d      8.25 nmol/kg/d
TABLE3 = {
    "longitudinal growth rate (um/day)": (26.0, 26.0, 40.0, "N.S.", "<0.05"),
    "growth plate thickness (um)":       (555.0, 594.0, 682.0, "N.S.", "<0.05"),
    "proliferating zone thickness (um)": (125.0, 139.0, 196.0, "N.S.", "<0.001"),
    "proliferating cells/column (n)":    (13.0, 11.0, 11.0, "N.S.", "N.S."),
    "hypertrophic zone thickness (um)":  (72.0, 89.0, 128.0, "N.S.", "<0.05"),
    "hypertrophic cell 'volume' (um2)":  (232.0, 258.0, 286.0, "N.S.", "N.S."),
}
SD = {   # author-stated standard deviations, same order
    "longitudinal growth rate (um/day)": (7, 5, 9),
    "growth plate thickness (um)":       (61, 64, 48),
    "proliferating zone thickness (um)": (10, 89, 14),
    "proliferating cells/column (n)":    (2, 2, 1.6),
    "hypertrophic zone thickness (um)":  (26, 23, 56),
    "hypertrophic cell 'volume' (um2)":  (30, 56, 34),
}


def rule(c="="):
    print(c * 90)


def main():
    rule()
    print("wendt2015 TABLE 3 - CYNOMOLGUS MONKEY, BMN 111 (VOSORITIDE), 6 MONTHS, n = 4/GROUP")
    rule()
    print(f"\n    {'parameter':<36} {'vehicle':>9} {'2.25':>9} {'8.25':>9}  {'high/veh':>9}  P(high)")
    for k, (v0, v1, v2, p1, p2) in TABLE3.items():
        print(f"    {k:<36} {v0:>9.1f} {v1:>9.1f} {v2:>9.1f}  {v2/v0:>8.2f}x  {p2}")

    print("\n[1] THE ONE ROW THAT DECIDES THE TERM, AND IT GOES THE WRONG WAY")
    c0 = TABLE3["proliferating cells/column (n)"][0]
    c2 = TABLE3["proliferating cells/column (n)"][2]
    print(f"    PROLIFERATING CELLS PER COLUMN: {c0:.0f} -> {c2:.0f}  ({c2/c0:.2f}x), N.S.")
    print("    At BOTH doses it is LOWER than vehicle. Vosoritide does not buy length")
    print("    by adding divisions to a column. Under the round-198 reserve model that")
    print("    is good news in isolation - divisions are the exhaustible term - but it")
    print("    forces the growth into one of the two remaining terms.")

    print("\n[2] AND THE CELL-SIZE ROW IS AN AREA, NOT A HEIGHT")
    print("    The column is printed as \"Hypertrophic cell volume\" and the UNIT IS")
    print("    um2. A volume is not measured in um2. This is a PROJECTED AREA, which")
    print("    CORR-190 forbids reading as a length, and which cooper2013 showed is")
    print("    the wrong quantity anyway - jerboa hypertrophic cells are 2.9x the")
    print("    VOLUME of mouse but only 1.58x the HEIGHT, because volume includes")
    print("    radial expansion that adds nothing to the axis of elongation.")
    a0 = TABLE3["hypertrophic cell 'volume' (um2)"][0]
    a2 = TABLE3["hypertrophic cell 'volume' (um2)"][2]
    print(f"    area {a0:.0f} -> {a2:.0f} um2 = {a2/a0:.2f}x, NOT SIGNIFICANT")
    print(f"    IF the cell scaled isotropically, height would go as the square root:")
    print(f"        implied height ratio = sqrt({a2/a0:.3f}) = {math.sqrt(a2/a0):.3f}x")
    print("    THAT IS AN ASSUMPTION, NOT A MEASUREMENT, and it is the weakest link in")
    print("    everything below. Hypertrophic cells do NOT enlarge isotropically.")

    print("\n[3] CLOSING THE IDENTITY, AND WHAT IS LEFT OVER")
    g0 = TABLE3["longitudinal growth rate (um/day)"][0]
    g2 = TABLE3["longitudinal growth rate (um/day)"][2]
    gr = g2 / g0
    cr = c2 / c0
    hr = math.sqrt(a2 / a0)
    print(f"    growth rate            {gr:.2f}x   (P < 0.05, the only significant term here)")
    print(f"    cells per column       {cr:.2f}x   (N.S.)")
    print(f"    implied cell height    {hr:.2f}x   (N.S., and derived from an area)")
    resid = gr / (cr * hr)
    print(f"    RESIDUAL, i.e. everything not explained by those two: {resid:.2f}x")
    print("\n    In the Hunziker identity growth rate = amplification x POOL CONSUMPTION")
    print("    x terminal cell height, that residual sits on POOL CONSUMPTION - the")
    print("    rate at which resting-zone cells are recruited and spent.")
    print(f"    SO THE PRIMATE DATA READS: vosoritide raises growth {gr:.0%} of baseline")
    print(f"    with FEWER cells per column and an unproven {hr:.2f}x on cell height,")
    print(f"    leaving roughly {resid:.1f}x to be carried by SPENDING THE RESERVE FASTER.")
    print("    THAT IS THE UNFAVOURABLE ASSIGNMENT. It puts vosoritide in the same")
    print("    category as growth hormone rather than in the free-axis category the")
    print("    stack has been assuming.")

    print("\n[4] WHY THIS IS A DIRECTION AND NOT A VERDICT")
    for i, x in enumerate([
        "n = 4 PER GROUP, and the authors themselves write that the study 'was not "
        "powered for significance'.",
        "BOTH decomposition terms - cells per column and cell area - are NON-SIGNIFICANT. "
        "Only the growth rate and the zone thicknesses clear P < 0.05.",
        "The cell measure is a PROJECTED AREA (um2) and the conversion to height is an "
        "isotropy assumption this atlas has already shown to be false (cooper2013).",
        "Cells per column was counted in the PROLIFERATING zone. That is not the "
        "amplification term of the identity, which is residence time in the "
        "proliferative compartment - it is a standing count, and a standing count can "
        "fall while flux rises.",
        "No resting-zone cycle time was measured, so pool consumption is INFERRED as a "
        "residual rather than measured. A residual absorbs every error in the other terms.",
        "6 months in a growing monkey, with a growth plate that does not fuse on the "
        "same schedule as a human at bone age 16.",
    ], 1):
        print(f"    ({i}) {x}")

    print("\n[5] WHAT WOULD SETTLE IT, AND IT IS CHEAP")
    print("    The sections exist. wendt2015 embedded left tibias in methyl")
    print("    methacrylate and cut five 7-um sections per animal, and ran calcein and")
    print("    oxytetracycline double labelling. RE-MEASURING TERMINAL HYPERTROPHIC")
    print("    CELL HEIGHT AXIALLY ON THOSE SAME SECTIONS converts a projected area")
    print("    into the term the decomposition needs, with no new animals. Adding a")
    print("    resting-zone cycle time would close the identity outright.")
    rule()


if __name__ == "__main__":
    main()
