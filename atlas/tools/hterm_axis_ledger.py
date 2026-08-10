#!/usr/bin/env python3
"""
THE h_term AXIS - can terminal cell height be raised, what does it cost, and
which agent in the stack is buying it efficiently?

WHY THIS TOOL EXISTS
--------------------
Round 198 fixed the objective function: adult height = RESERVE x TERMINAL CELL
HEIGHT, because fusion is triggered by exhaustion of proliferative potential.
That makes h_term the ONLY axis on which a gain is free - a taller terminal cell
adds length without consuming a division.

The atlas then never audited it. Gap g_l1_raise_terminal_cell_volume states the
problem plainly: "no evidence the parameter can be pushed upward at all rather
than only downward, and every manipulation on record LOWERS it (tamoxifen,
oestrogen, Igf1 deficiency)".

If that is true, the free axis does not exist and the whole programme reduces to
preserving reserve. This tool tests it against everything the atlas holds.

TWO SOURCES, BOTH ALREADY IN THE FILE, NEITHER READ THIS WAY.
"""
import math

# ============================================================================
# PART 1 - THE EXCHANGE RATE. What is a division worth against a hypertrophy?
# ============================================================================
# AUTHOR-STATED in the jerboa/mouse tail paper (weber2025), citing the
# comparative growth-plate literature. This is the number that decides whether
# h_term is worth chasing at all.
DIVISION_UM = (8.0, 9.0)      # micrometres added to the axis by ONE doubling
                              # of a flattened proliferative chondrocyte
HYPERTROPHY_UM = (40.0, 50.0)  # micrometres added by that same cell as it
                               # proceeds through hypertrophic enlargement

# ============================================================================
# PART 2 - CAN IT BE RAISED? The first affirmative in the atlas.
# ============================================================================
# weber2025, mouse Npr3-/- against wild-type siblings, tail vertebrae TV1 and
# TV6, P7. Welch's two-tailed t-test, n = 3 per group (n = 4 for Npr3-/- TV6).
# MEASURED AS "maximum height of hypertrophic chondrocytes IN THE DIRECTION OF
# BONE ELONGATION" - which is h_term proper, not a zone height and not a volume.
NPR3_CELL_HEIGHT_GAIN = 1.20        # author-stated "approximately 20% greater"
NPR3_HZ_HEIGHT_GAIN_TV6 = 2.00      # author-stated "nearly twice the height"
NPR3_PZ_SIGNIFICANT = False         # significant only in caudal TV1 of four cartilages

# ============================================================================
# PART 3 - hunziker1994, RE-READ AS A DOSE-RESPONSE RATHER THAN FOUR TREATMENTS
# ============================================================================
# Hypophysectomised rat proximal tibia, 8-day minipump, four groups of six.
# EVERY VALUE AUTHOR-STATED. This is the only experiment in the literature
# carrying growth rate, terminal cell height, cycle time and cells per column
# in the SAME animals.
#            group        GR um/d  h_term um  turnover cells/col/day
HUNZIKER = [("saline",       31.0,   19.5,    1.0),
            ("IGF-I",        92.0,   27.3,    3.0),
            ("GH",          163.0,   26.5,    6.0),
            ("normal",      284.0,   29.8,   10.0)]


def rule(c="="):
    print(c * 88)


def main():
    rule()
    print("PART 1  THE EXCHANGE RATE - WHY h_term IS THE HIGH-LEVERAGE AXIS")
    rule()
    lo = HYPERTROPHY_UM[0] / DIVISION_UM[1]
    hi = HYPERTROPHY_UM[1] / DIVISION_UM[0]
    print(f"\n    one doubling of a flat proliferative chondrocyte adds "
          f"{DIVISION_UM[0]:.0f}-{DIVISION_UM[1]:.0f} um to the axis")
    print(f"    that same cell then adds  {HYPERTROPHY_UM[0]:.0f}-{HYPERTROPHY_UM[1]:.0f} um "
          f"as it goes through hypertrophy")
    print(f"    RATIO                     {lo:.1f}x to {hi:.1f}x")
    print("\n    A DIVISION IS THE CHEAP PART OF THE TRANSACTION AND THE EXPENSIVE")
    print("    PART OF THE BUDGET. It costs one unit of an exhaustible reserve and")
    print("    returns about a fifth of the length that the hypertrophy of the same")
    print("    cell returns for free. Every per-cent added to h_term is worth roughly")
    print("    five per cent added to division count, AND IT IS NOT DEDUCTED FROM")
    print("    ANYTHING.")

    rule()
    print("PART 2  CAN h_term BE RAISED? YES - AND THIS IS THE FIRST ONE")
    rule()
    print("\n    weber2025, Npr3-/- mouse tail vertebrae against wild-type siblings:")
    print(f"        maximum hypertrophic cell height in the axis of elongation"
          f"   +{100*(NPR3_CELL_HEIGHT_GAIN-1):.0f}%")
    print(f"        hypertrophic ZONE height at TV6                            "
          f"   ~{NPR3_HZ_HEIGHT_GAIN_TV6:.1f}x")
    print(f"        proliferative zone height          significant in only 1 of 4 cartilages")
    print("\n    THE MEASUREMENT IS THE RIGHT ONE. CORR-189 forbids reading a zone")
    print("    height as a cell-height claim; this paper measures the cell directly,")
    print("    axially, and reports it SEPARATELY from the zone. It is the first")
    print("    intervention in this atlas to RAISE terminal cell height rather than")
    print("    lower it, which contradicts the standing text of")
    print("    g_l1_raise_terminal_cell_volume.")

    print("\n    BUT THE DECOMPOSITION SAYS h_term IS THE MINORITY OF THE EFFECT:")
    implied = NPR3_HZ_HEIGHT_GAIN_TV6 / NPR3_CELL_HEIGHT_GAIN
    print(f"        zone {NPR3_HZ_HEIGHT_GAIN_TV6:.2f}x  /  cell height "
          f"{NPR3_CELL_HEIGHT_GAIN:.2f}x  =  {implied:.2f}x MORE CELLS PER COLUMN")
    print("    So about two thirds of the hypertrophic zone expansion is extra CELLS")
    print("    and about one third is bigger cells. NPR3 loss is mostly a")
    print("    cells-per-column agent with a real but minority h_term component.")
    print("\n    AND WHERE THE EXTRA CELLS COME FROM IS UNRESOLVED, WHICH IS THE")
    print("    WHOLE QUESTION UNDER A FIXED RESERVE. The proliferative zone is not")
    print("    significantly taller in three of four cartilages, and THE Npr3 ARM OF")
    print("    THIS PAPER CARRIES NO CALCEIN AND NO EdU - the flux measurements exist")
    print("    only in the mouse-versus-jerboa comparison. Extra hypertrophic cells")
    print("    can come from extra divisions (which SPENDS reserve) or from delayed")
    print("    clearance at the chondro-osseous junction (which does NOT). Npr3 mice")
    print("    are independently reported to have DELAYED ENDOCHONDRAL OSSIFICATION,")
    print("    which points at the second, and nobody has measured it.")

    rule()
    print("PART 3  hunziker1994 AS A DOSE-RESPONSE - AND THE RESULT IS UNCOMFORTABLE")
    rule()
    base = HUNZIKER[0]
    print(f"\n    {'group':<9} {'GR um/d':>8} {'h_term':>7} {'D /col/d':>9}"
          f" {'A':>6} | {'h_term x':>9} {'D x':>6} {'A x':>6}")
    rows = []
    for name, gr, h, d in HUNZIKER:
        a = gr / (d * h)
        rows.append((name, gr, h, d, a))
        print(f"    {name:<9} {gr:>8.0f} {h:>7.1f} {d:>9.1f} {a:>6.3f} |"
              f" {h/base[2]:>9.2f} {d/base[3]:>6.2f} {a/(base[1]/(base[3]*base[2])):>6.2f}")
    print("\n    A = amplification, computed as GR / (D x h_term). The identity closes")
    print("    with no residual because all four quantities are from the same animals.")

    print("\n[3a] h_term SATURATES. POOL CONSUMPTION DOES NOT.")
    print(f"    {'step':<22} {'h_term gain':>12} {'D gain':>9} {'h_term per unit D':>19}")
    for i in range(len(rows) - 1):
        n0, _, h0, d0, _ = rows[i]
        n1, _, h1, d1, _ = rows[i + 1]
        dh = h1 / h0
        dd = d1 / d0
        print(f"    {n0+' -> '+n1:<22} {100*(dh-1):>11.1f}% {dd:>8.2f}x"
              f" {(dh-1)/(dd-1):>19.3f}")
    print("\n    THE FIRST STEP BUYS 40 PER CENT OF THE h_term FOR A TRIPLING OF POOL")
    print("    CONSUMPTION. EVERY STEP AFTER THAT BUYS ALMOST NOTHING AND KEEPS")
    print("    SPENDING. From IGF-I to fully normal, pool consumption rises another")
    print("    3.3-fold to buy a further 9 per cent of terminal cell height.")

    print("\n[3b] THE STACK CONSEQUENCE, STATED PLAINLY")
    igf = rows[1]; gh = rows[2]
    print(f"    IGF-I : h_term {igf[2]:.1f} um at pool consumption {igf[3]:.0f}/col/day")
    print(f"    GH    : h_term {gh[2]:.1f} um at pool consumption {gh[3]:.0f}/col/day")
    print(f"    GH SPENDS THE POOL {gh[3]/igf[3]:.0f}x FASTER AND DELIVERS "
          f"{100*(gh[2]/igf[2]-1):+.1f}% h_term.")
    print("    Under adult height = reserve x h_term, that is the wrong side of the")
    print("    curve. THE INFERENCE IS NOT 'USE IGF-I INSTEAD OF GH' - see the")
    print("    caveats below - IT IS 'THE SOMATOTROPIC DOSE THAT MAXIMISES ADULT")
    print("    HEIGHT IS THE LOWEST ONE THAT SATURATES h_term, NOT THE HIGHEST")
    print("    TOLERATED ONE', which is the opposite of how the axis is dosed.")

    print("\n[3c] WHAT WOULD KILL THIS READING, AND IT IS NOT EXCLUDED")
    print("    (i) THE DOSES WERE NOT MATCHED FOR EQUIPOTENCY. If GH and IGF-I lie on")
    print("        ONE dose-response curve, then 'IGF-I is more efficient' collapses")
    print("        into 'IGF-I was given at a lower dose', and the only surviving")
    print("        claim is the saturation shape - which is still the actionable one.")
    print("        The four points are non-monotonic in h_term against D (27.3 at")
    print("        D = 3 against 26.5 at D = 6), which is weak evidence GH sits BELOW")
    print("        the IGF-I curve, but 3 per cent at n = 6 is noise and is not")
    print("        claimed here.")
    print("    (ii) HYPOPHYSECTOMISED RAT. The background is GH-deficient, so GH is")
    print("        restoring an axis while IGF-I is bypassing it. Neither maps")
    print("        cleanly onto a GH-replete human adolescent.")
    print("    (iii) THE RAT DOES NOT FUSE, so no adult-height endpoint exists here.")
    print("    (iv) n = 6 per group, one study, 1994, never replicated with this")
    print("        readout set.")

    rule()
    print("PART 4  DOES THE STACK CONTAIN THREE AGENTS FIGHTING OVER ONE TERM?")
    rule()
    print("\n    cooper2013 assigns h_term to IGF-1 directly: Igf1-deficient mice have")
    print("    THE SAME NUMBER of hypertrophic chondrocytes, each 30 per cent shorter")
    print("    in the axis of elongation, and removing IGF1 ABOLISHES the between-bone")
    print("    difference in cell height. hunziker1994 gives GH 1.36x h_term.")
    print("    weber2025 gives the CNP/NPR3 axis 1.20x h_term.")
    print("\n    SO GH/IGF-1 AND THE CNP AXIS MAY BE ACTING ON THE SAME TERM, AND THE")
    print("    ATLAS HAS BEEN ASSUMING THEY STACK. If h_term saturates - and part 3a")
    print("    says it does - then two h_term agents are SUB-ADDITIVE by construction,")
    print("    and the second one is paid for at full reserve cost for a fraction of")
    print("    the benefit. NOBODY HAS MEASURED TERMINAL CELL HEIGHT UNDER A")
    print("    COMBINATION. That is now the most decision-relevant unmeasured quantity")
    print("    in the stack.")

    print("\n    AND THE COMPARATIVE DATA SAYS DIVIDING FASTER IS NOT HOW LENGTH IS")
    print("    MADE. weber2025 measured the proliferation index by 2-hour EdU in")
    print("    growth cartilages differing more than TWOFOLD in daily elongation rate,")
    print("    in two species, and 'the fraction of S-phase chondrocytes is not")
    print("    significantly different'. Faster bones are not built by faster")
    print("    division. That is a third independent line against rate agents.")
    rule()


if __name__ == "__main__":
    main()
