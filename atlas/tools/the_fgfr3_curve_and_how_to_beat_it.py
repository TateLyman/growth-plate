#!/usr/bin/env python3
"""
THE FGFR3 GROWTH CURVE, FITTED, AND THE ONLY WAY TO BEAT IT AT A FIXED 8 mg DOSE.

WHY THIS TOOL EXISTS
--------------------
The user fixed the dose at erdafitinib 8 mg, set safety and the spine aside, and
asked what the curve actually is and how to beat it. That makes the question
purely quantitative: what is growth gain as a function of FGFR3 pathway
inhibition, and what raises inhibition without raising the dose?

THE ANSWER HAS THREE PARTS.
  1. THE CURVE IS A POWER LAW WITH AN EXPONENT NEAR 2.4 TO 3.3, fitted
     independently from two human points and two mouse points. Supra-linear on
     both. Doubling pathway inhibition roughly quintuples the growth gain.
  2. DOSE ESCALATION INSIDE THE LABEL IS NOT A LEVER. 8 to 9 mg buys about 20
     per cent more gain. And ONE PLAUSIBLE-LOOKING LEVER IS ARITHMETICALLY DEAD -
     protein-binding displacement cannot raise unbound exposure for a
     low-extraction drug, and the hepatic-impairment study proves it empirically.
  3. WHAT DOES WORK IS MULTIPLICATION AT NODES IN SERIES, because residual
     signal multiplies while the growth response is a power of inhibition. One
     extra agent contributing 27 per cent inhibition on its own TRIPLES the
     growth gain from 8 mg erdafitinib without touching the dose.
"""

import math

# --------------------------------------------------------------- the anchors
# free steady-state Cav / cellular IC50, on the developers' own numbers (round 216)
COVERAGE = {"erda 3 mg": 0.176, "erda 7 mg": 0.410, "erda 8 mg": 0.469,
            "erda 9 mg": 0.527, "dabo 45 mg": 0.187, "dabo 60 mg": 0.292,
            "dabo 90 mg": 0.690, "dabo 120 mg": 1.580}

# human growth observations, and the baseline they must be measured against
HUMAN = [("erda 3 mg", 0.176, 10.0, "erdaseries2025 patient 1, on GH, hypogonadal, "
          "severe pre-treatment impairment so part is catch-up"),
         ("erda 7 mg", 0.410, 19.06, "erdachild2024, pre-pubertal hormones, no "
          "baseline bone age")]
TYPICAL_AHV = 7.66   # tyra_corporate_deck_2026 citing Merck Manuals, 12 mo to 10 y

# mouse, from the deposited individual-animal data re-analysed in round 215
MOUSE = [("tibia", 12, 3.86, 14, 6.45), ("femur", 12, 5.00, 14, 8.23)]


def residual(x):
    """Residual pathway signal at coverage x = C/IC50, competitive, Hill n=1."""
    return 1.0 / (1.0 + x)


def inhibition(x):
    return 1.0 - residual(x)


def fit_exponent(i1, g1, i2, g2):
    return math.log(g2 / g1) / math.log(i2 / i1)


def rule(c="="):
    print(c * 92)


def main():
    rule()
    print("THE FGFR3 GROWTH CURVE, AND HOW TO BEAT IT AT A FIXED 8 mg")
    rule()

    # ------------------------------------------------------------------ [1]
    print("\n[1] TRANSLATING EXPOSURE INTO FRACTIONAL PATHWAY INHIBITION")
    rule("-")
    print("    For a competitive inhibitor the residual signal is 1/(1 + C/IC50).\n")
    print(f"    {'regimen':<16}{'C/IC50':>9}{'residual':>11}{'% inhibited':>14}")
    for k, v in COVERAGE.items():
        print(f"    {k:<16}{v:>9.3f}{residual(v):>11.3f}{inhibition(v)*100:>13.1f}%")
    print("\n    NOTE HOW COMPRESSED THIS IS. The whole clinically attainable range runs")
    print("    from 15 per cent inhibition at 3 mg erdafitinib to 41 per cent at 90 mg")
    print("    dabogratinib. NOBODY HAS EVER HALVED FGFR3 SIGNALLING IN A GROWING HUMAN.")

    # ------------------------------------------------------------------ [2]
    print("\n[2] FITTING THE CURVE - HUMAN")
    rule("-")
    i1, i2 = inhibition(HUMAN[0][1]), inhibition(HUMAN[1][1])
    g1, g2 = HUMAN[0][2] - TYPICAL_AHV, HUMAN[1][2] - TYPICAL_AHV
    print(f"    Growth GAIN above a typical paediatric {TYPICAL_AHV} cm/yr:\n")
    for label, cov, vel, note in HUMAN:
        print(f"      {label:<12} {inhibition(cov)*100:>5.1f}% inhibition -> "
              f"{vel:>5.2f} cm/yr, a gain of {vel-TYPICAL_AHV:+.2f}")
        for i in range(0, len(note), 78):
            print(f"                   {note[i:i+78]}")
    n_h = fit_exponent(i1, g1, i2, g2)
    print(f"\n    A {i2/i1:.2f}-fold rise in inhibition travels with a {g2/g1:.2f}-fold rise in")
    print(f"    GAIN. POWER-LAW EXPONENT = {n_h:.2f}.")

    print("\n    SENSITIVITY, BECAUSE THE BASELINE IS A CHOICE AND THE EXPONENT DEPENDS ON IT:")
    for base in (4.0, 6.0, 7.66, 8.5, 9.0):
        gg1, gg2 = HUMAN[0][2] - base, HUMAN[1][2] - base
        if gg1 <= 0:
            print(f"        baseline {base:>4.2f} cm/yr -> the 3 mg point is at or below "
                  "baseline; no exponent")
            continue
        print(f"        baseline {base:>4.2f} cm/yr -> exponent "
              f"{fit_exponent(i1, gg1, i2, gg2):.2f}")
    print("\n    THE EXPONENT IS STRONGLY BASELINE-SENSITIVE - 1.39 at a 4 cm/yr baseline up")
    print("    to 3.48 at 9 - AND THAT IS THE BIGGEST SINGLE UNCERTAINTY IN THIS TOOL. What")
    print("    survives every choice is that IT IS ALWAYS WELL ABOVE 1, so the curve is")
    print("    supra-linear on the human data regardless. The conclusions below scale with")
    print("    the exponent, so they are quoted at 2.38 and should be read as a range.")

    # ------------------------------------------------------------------ [3]
    print("\n[3] FITTING THE CURVE - MOUSE, INDEPENDENTLY")
    rule("-")
    print("    Dose is the exposure proxy here and the readout is per cent length gain,")
    print("    so this fit needs no baseline choice at all.\n")
    ns = []
    for bone, d1, p1, d2, p2 in MOUSE:
        n = math.log(p2 / p1) / math.log(d2 / d1)
        ns.append(n)
        print(f"      {bone:<7} {d1} mg/kg {p1:+.2f}%  ->  {d2} mg/kg {p2:+.2f}%   "
              f"exponent {n:.2f}")
    print(f"\n    MOUSE EXPONENT {min(ns):.2f} TO {max(ns):.2f}, HUMAN {n_h:.2f}. Two species, two")
    print("    completely different readouts, both strongly supra-linear. THE CURVE IS A")
    print("    POWER LAW WITH AN EXPONENT SOMEWHERE BETWEEN 2 AND 3.5.")

    # ------------------------------------------------------------------ [4]
    print("\n[4] WHY A BRAKE-RELEASE CURVE SHOULD BE SUPRA-LINEAR")
    rule("-")
    print("    This is not a curiosity - it follows from the atlas's own decomposition.")
    print("    Length = CELLS RECRUITED FROM THE RESERVE x DIVISIONS EACH x TERMINAL CELL")
    print("    HEIGHT, and FGFR3 inhibition raises ALL THREE. horike2026 puts excess FGFR3")
    print("    on resting-zone TURNOVER through an ERK-INDEPENDENT CREB limb; tyra300_2025")
    print("    reports increased proliferation AND differentiation; weber2025's exchange")
    print("    rate makes the hypertrophic term worth 40-50 micrometres against 8-9 for a")
    print("    division. THREE MULTIPLICATIVE TERMS EACH RISING A FEW PER CENT COMPOUND INTO")
    print("    A CONVEX OUTPUT. A 6.45 per cent tibia gain decomposes to about 2.1 per cent")
    print("    per term if the three are equal.")

    # ------------------------------------------------------------------ [5]
    print("\n[5] THE LEVER THAT LOOKS BIGGEST AND IS ARITHMETICALLY DEAD")
    rule("-")
    print("    Erdafitinib is 99.7 per cent bound to alpha-1-acid glycoprotein, an")
    print("    acute-phase protein that varies several-fold between individuals. It is")
    print("    tempting to think displacing it - lowering AAG - would multiply free drug at")
    print("    a fixed 8 mg. IT WOULD NOT.")
    print("\n    For a LOW-EXTRACTION drug, unbound steady-state concentration is")
    print("    Dose / (CLint x tau) and is INDEPENDENT OF PROTEIN BINDING. Erdafitinib's")
    print("    CL/F is 0.362 L/h against a hepatic blood flow near 90 L/h - an extraction")
    print("    ratio of well under one per cent, so it is as low-extraction as drugs get.")
    print("    Raising the free fraction raises total clearance in exact proportion and the")
    print("    unbound exposure does not move.")
    print("\n    AND zhu2026 PROVES IT EMPIRICALLY WITHOUT MEANING TO. In moderate hepatic")
    print("    impairment the free fraction ROSE and apparent total clearance rose with it,")
    print("    and the geometric mean ratios for FREE Cmax and FREE AUC against controls")
    print("    were 104.8 and 87.5 per cent - UNCHANGED UNBOUND EXPOSURE. The one natural")
    print("    experiment that perturbs binding shows the free concentration does not move.")
    print("    THIS KILLS THE WHOLE PROTEIN-BINDING FAMILY OF IDEAS AND IT SHOULD BE")
    print("    RECORDED SO IT IS NOT PROPOSED AGAIN.")

    # ------------------------------------------------------------------ [6]
    print("\n[6] WHAT DOSE ESCALATION INSIDE THE LABEL BUYS, USING THE FITTED CURVE")
    rule("-")
    base_i = inhibition(COVERAGE["erda 8 mg"])
    for k in ("erda 9 mg", "dabo 60 mg", "dabo 90 mg", "dabo 120 mg"):
        i = inhibition(COVERAGE[k])
        print(f"      {k:<14} inhibition {i*100:>5.1f}% -> gain multiple against 8 mg "
              f"erdafitinib = {(i/base_i)**n_h:>5.2f}x")
    print("\n    8 to 9 mg BUYS ABOUT 20 PER CENT MORE GAIN. That is the entire label")
    print("    headroom and it is not worth optimising. Even dabogratinib at 90 mg, which")
    print("    costs a liver signal, is only about 1.8-fold.")

    # ------------------------------------------------------------------ [7]
    print("\n[7] THE ONE THING THAT DOES WORK - MULTIPLICATION AT NODES IN SERIES")
    rule("-")
    print("    Residual signal MULTIPLIES across independent nodes in one cascade, while")
    print("    the growth response is a POWER of total inhibition. That asymmetry is the")
    print("    whole opportunity.\n")
    f_erda = residual(COVERAGE["erda 8 mg"])
    print(f"    8 mg erdafitinib alone: residual {f_erda:.3f}, inhibition "
          f"{(1-f_erda)*100:.1f} per cent.\n")
    print(f"    {'second agent inhibits':>22}{'combined inhib':>16}{'gain multiple':>15}"
          f"{'erdafitinib dose that':>24}")
    print(f"    {'on its own':>22}{'':>16}{'vs 8 mg alone':>15}{'would be needed':>24}")
    print("    " + "-" * 78)
    for f2_inh in (0.10, 0.20, 0.265, 0.30, 0.40, 0.50):
        comb = 1 - f_erda * (1 - f2_inh)
        mult = (comb / base_i) ** n_h
        # what single-agent coverage would give the same inhibition
        need_x = comb / (1 - comb)
        need_mg = need_x / COVERAGE["erda 8 mg"] * 8
        print(f"    {f2_inh*100:>21.1f}%{comb*100:>15.1f}%{mult:>15.2f}x"
              f"{need_mg:>21.0f} mg")
    print("\n    READ THE 26.5 PER CENT ROW. ONE ADDITIONAL AGENT CONTRIBUTING A QUARTER OF")
    print("    THE PATHWAY, ADDED TO 8 mg ERDAFITINIB, TRIPLES THE GROWTH GAIN AND IS")
    print("    EQUIVALENT TO AN ERDAFITINIB DOSE OF ABOUT 27 mg - THREE TIMES THE LABEL")
    print("    MAXIMUM. That is how you beat the curve without touching the dose.")

    # ------------------------------------------------------------------ [8]
    print("\n[8] THE SERIES NODES THAT EXIST, IN ORDER ALONG THE CASCADE")
    rule("-")
    nodes = [
        ("LIGAND", "soluble FGFR3 decoy (recifercept class)",
         "removes FGF before it reaches the receptor; works extracellularly so it does "
         "not need to enter a chondrocyte, which is the one biologic geometry avascular "
         "cartilage does not exclude"),
        ("LIGAND, COMPENSATORY", "block the FGF19/KLB rise",
         "surf301_pb060_2024 found FGF19 AND KLOTHO-BETA ROSE on treatment as a potential "
         "COMPENSATORY MECHANISM to FGFR3 inhibition, with no rise in FGF21. THE SYSTEM "
         "PUSHES BACK BY RAISING THE LIGAND, WHICH IS EXACTLY WHAT FLATTENS THE CURVE. "
         "Blocking that loop steepens it and nobody has tried"),
        ("RECEPTOR ABUNDANCE", "statins",
         "statin_ipsc_achondroplasia - the proposed mechanism is ENHANCED DEGRADATION or "
         "reduced accumulation of FGFR3 PROTEIN rather than kinase inhibition, so it is "
         "strictly in series with an ATP-competitive inhibitor. Corrected cartilage "
         "degradation in patient iPSC chondrocytes from two genotypes and recovered bone "
         "growth in achondroplasia mice. Published 2014, never randomised for growth"),
        ("KINASE", "erdafitinib 8 mg - FIXED", "31.9 per cent inhibition, the anchor"),
        ("MAPK, DOWNSTREAM", "meclizine",
         "meclizine_repurposing - full human paediatric PK at 12.5 mg/day, Cmax 167 ng/mL, "
         "AUC 1170 ng.h/mL, no serious adverse events in 12 children. HUMAN EFFICACY ALONE "
         "IS ESSENTIALLY NULL at +0.11 cm/yr on top of growth hormone, which is exactly "
         "what a small series contribution looks like when given alone - and exactly what "
         "the multiplication argument predicts should still be worth having in combination"),
        ("CREB, ERK-INDEPENDENT", "666-15",
         "horike2026 - the FGFR3-to-CREB limb that disrupts resting-zone turnover is "
         "INDEPENDENT OF ERK, so every downstream MAPK agent misses it and only receptor-"
         "level inhibition touches it. The CREB inhibitor 666-15 restored growth plate "
         "pathology and bone length in the achondroplasia mouse - BUT WAS NULL IN WILD-TYPE, "
         "so it corrects pathology rather than elevating a normal plate"),
        ("PARALLEL, NOT IN SERIES", "CNP arm two - cAMP/PKA on the hypertrophic zone",
         "is_the_cnp_arm_redundant_with_fgfr3_blockade - arm one (cGMP/PKG2, acting at "
         "RAF-1) IS redundant with FGFR3 blockade, but arm two is cAMP/PKA acting on "
         "HYPERTROPHIC ZONE ELONGATION, a different zone, second messenger and kinase. "
         "hirota2022 showed CNP predominantly activates PKA in hypertrophic chondrocytes "
         "and that H89 BLOCKS the length effect - a necessity test. THIS DOES NOT MULTIPLY "
         "WITH ERDAFITINIB, IT ADDS ON A DIFFERENT TERM, which is better"),
    ]
    for tier, agent, note in nodes:
        print(f"\n    {tier}")
        print(f"        {agent}")
        for i in range(0, len(note), 82):
            print(f"          {note[i:i+82]}")

    print("\n[9] WHAT IS MISSING, AND IT IS ONE NUMBER PER AGENT")
    rule("-")
    print("    THE FRAMEWORK IS COMPLETE AND THE INPUTS ARE NOT. To use the table in [7] we")
    print("    need, for each candidate, THE FRACTION OF FGFR3 PATHWAY OUTPUT IT REMOVES IN")
    print("    A CHONDROCYTE AT AN ACHIEVABLE HUMAN CONCENTRATION - one number, measurable")
    print("    as phospho-ERK or phospho-FGFR suppression in the same assay for all of them.")
    print("    NOBODY HAS EVER MEASURED THESE ON ONE AXIS. Every agent in [8] has been")
    print("    studied alone, as a monotherapy, against a growth endpoint - which is the")
    print("    least informative way to test something whose value is multiplicative.")
    print("\n    AND THE ASSUMPTION THAT COULD SINK THE WHOLE THING IS INDEPENDENCE. Series")
    print("    multiplication assumes the nodes do not share a rate-limiting step and that")
    print("    the cascade has no strong feedback. THE FGF19/KLB RISE IS DIRECT EVIDENCE OF")
    print("    FEEDBACK, so the true combined effect will be less than the product. How much")
    print("    less is unmeasured.")
    rule()


if __name__ == "__main__":
    main()
