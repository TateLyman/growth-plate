#!/usr/bin/env python3
"""
AUDIT OF ROUND 217. TWO OF THE FOUR SERIES NODES ARE DEAD, THE HEADLINE EXPONENT
IS SUBSTANTIALLY AN ARTEFACT OF MY OWN HILL ASSUMPTION, AND THE PRACTICAL
CONCLUSION SURVIVES ANYWAY.

WHY THIS TOOL EXISTS
--------------------
The user asked me to be sure. Two supplied documents test round 217 directly and
both come back negative, and re-examining my own arithmetic finds a third
problem that nobody supplied - I made it.

  1. STATINS. fafilek2017 is a four-statin, four-system replication attempt of
     the receptor-abundance mechanism I put in the series list. It fails
     completely, with positive controls in both directions.
  2. THE LIGAND DECOY. The recifercept phase 2 results confirm a clean human
     futility termination at three dose levels with demonstrated exposure - AND
     THE ATLAS ALREADY HELD A NODE SAYING SO, which I did not read before
     promoting the decoy into a combination strategy. Second instance of the
     CORR-205 failure mode.
  3. THE HILL COEFFICIENT. Round 217 converted exposure into fractional pathway
     inhibition assuming a Hill slope of 1, then fitted a power law to the
     resulting axis. ROUND 214 HAD ALREADY DERIVED A HILL SLOPE NEAR 2.1 FROM
     THE SAME SPONSOR FIGURE. At n = 2.13 the fitted exponent collapses from
     2.38 to 0.94 - essentially linear. The headline was an artefact of a
     parameter my own atlas had already estimated differently.
"""

import math

# ------------------------------------------------------------------ [1] statins
FAFILEK = [
    ("compounds", "atorvastatin, fluvastatin, lovastatin and pravastatin - four statins, "
     "not one"),
    ("systems", "RCS rat chondrosarcoma chondrocytes, cultured mouse embryonic tibias, "
     "limb bud micromass cultures, and human control and thanatophoric-dysplasia "
     "chondrocytes from the International Skeletal Dysplasia Registry"),
    ("the mechanism I cited", "NO change in FGFR3 protein level - not for wild-type, not "
     "for G380R (achondroplasia), not for K650M (thanatophoric), transfected or "
     "CRISPR-flag-tagged endogenous, at 12, 24, 48 and 72 hours"),
    ("positive control one", "AZD4547, an FGFR inhibitor, RESCUED every readout in the "
     "same experiments - ERK activation, EGR1, caveolin-1, lamin A/C, collagen II and "
     "the alcian-blue extracellular matrix loss. The systems could show a rescue"),
    ("positive control two", "statin functionality was confirmed by the Ras prenylation "
     "band-shift. The statins were working; they were not touching FGFR3"),
    ("and it is worse than null", "in cultured mouse embryonic tibias, 1 micromolar "
     "statins ALONE INHIBITED TIBIA GROWTH to an extent comparable with FGF2, and "
     "worsened the phenotype when combined with FGF2"),
    ("the authors' own caveats", "statins might act indirectly in vivo through AKT, BMP "
     "or Hedgehog; and their models use robust FGF2 stimulation that could mask a subtle "
     "effect. They conclude the earlier rescue is LIKELY NOT INTRINSIC TO GROWTH PLATE "
     "CARTILAGE"),
]

# ------------------------------------------------------------ [2] the ligand decoy
RECIFERCEPT = [
    ("design", "phase 2, NCT04638153 / EudraCT 2020-001189-13, Pfizer C4181005, children "
     "aged 2-10 with achondroplasia, three arms - 1 mg/kg weekly (n=20), 2 mg/kg twice "
     "weekly (n=19), 1.5 mg/kg daily (n=18)"),
    ("primary efficacy", "ratio of observed to expected change in standing height. Month "
     "6 - 0.9, 1.1, 1.0. Month 9 - 1.0, 1.0, 1.0. Month 12 - 0.9, 1.1, 0.8. A RATIO OF 1.0 "
     "IS GROWTH EXACTLY AS EXPECTED WITHOUT TREATMENT"),
    ("was it an exposure failure", "NO. Trough serum concentrations at day 61 were 183.8, "
     "974.8 and about 3800 ng/mL across the three arms - dose-proportional, accumulating, "
     "and spanning roughly twentyfold. The drug was present"),
    ("why it stopped", "terminated 18 November 2022, and the register states the reason "
     "verbatim - DUE TO NOT MEETING THE PRE-SPECIFIED 6 MONTH EFFICACY CRITERIA AT THE "
     "TESTED DOSES AND NOT DUE TO ANY SAFETY CONCERNS"),
    ("what it does NOT settle", "achondroplasia is the wrong background for a ligand trap "
     "if the G380R receptor signals without ligand - and this atlas already grades that "
     "claim CONTESTED, with naski1996 and webster1996 reporting ligand-independent "
     "activation and monsonegoornan2000 disputing it. SO THE DECOY IS DEAD AS AN ASSET AND "
     "UNRESOLVED AS A MECHANISM IN A PATHWAY-INTACT PLATE - and nobody will run that "
     "experiment now, because the programme, its open-label extension, its natural-history "
     "study and a Chinese phase 1 were all terminated together"),
]

# ------------------------------------------------------------------- [3] the Hill
COV = {"erda 3 mg": 0.176, "erda 7 mg": 0.410, "erda 8 mg": 0.469, "erda 9 mg": 0.527}
TYPICAL = 7.66
OBS = {"erda 3 mg": 10.0, "erda 7 mg": 19.06}


def resid(x, n):
    return 1.0 / (1.0 + x ** n)


def inh(x, n):
    return 1.0 - resid(x, n)


def rule(c="="):
    print(c * 92)


def main():
    rule()
    print("ROUND 218 - AUDIT OF ROUND 217")
    rule()

    print("\n[1] THE RECEPTOR-ABUNDANCE NODE IS REFUTED. STATINS DO NOT TOUCH FGFR3.")
    rule("-")
    for k, v in FAFILEK:
        print(f"\n    {k.upper()}")
        for i in range(0, len(v), 84):
            print(f"        {v[i:i+84]}")
    print("\n    ROUND 217 PUT STATINS IN THE SERIES LIST ON THE MECHANISM 'ENHANCED")
    print("    DEGRADATION OF FGFR3 PROTEIN'. THAT IS THE EXACT CLAIM THIS PAPER TESTS AND")
    print("    FAILS TO REPRODUCE. And the atlas's own statin node already said it recorded")
    print("    'an unrepeated human-cell finding, not an intervention' - which should have")
    print("    prompted a search for a replication attempt BEFORE promoting it. One existed,")
    print("    published in 2017, nine years before I cited the original.")

    print("\n[2] THE LIGAND NODE WAS ALREADY DEAD IN THIS ATLAS'S OWN FILES")
    rule("-")
    for k, v in RECIFERCEPT:
        print(f"\n    {k.upper()}")
        for i in range(0, len(v), 84):
            print(f"        {v[i:i+84]}")
    print("\n    THE PROCESS FAILURE IS THE POINT. atlas node soluble_fgfr3_decoy already")
    print("    contained the termination, the three dose arms and the month-12 ratios, and")
    print("    described the trial as 'the cleanest available human test of the")
    print("    ligand-dependence of achondroplasia'. I listed the decoy as a series node")
    print("    without opening it. THIS IS THE SECOND INSTANCE OF CORR-205 IN TEN ROUNDS.")

    print("\n[3] THE EXPONENT WAS SUBSTANTIALLY AN ARTEFACT OF MY OWN HILL ASSUMPTION")
    rule("-")
    print("    Round 217 converted C/IC50 into fractional inhibition as 1 - 1/(1 + C/IC50),")
    print("    which is a Hill slope of 1, flagged it as an assumption, and then fitted a")
    print("    power law to the resulting axis. BUT ROUND 214 HAD ALREADY ESTIMATED THE HILL")
    print("    SLOPE FROM THE SAME SPONSOR FIGURE - the FGFR3 IC90 line sat at about 2.8")
    print("    times the IC50, and IC90/IC50 = 9^(1/n) gives n = ln9/ln2.8 = 2.13.")
    print("    I USED n = 1 ANYWAY, IN A ROUND THAT CITED ROUND 214 THROUGHOUT.\n")
    print(f"    {'Hill n':>7}{'3 mg inh':>11}{'7 mg inh':>11}{'8 mg inh':>11}"
          f"{'fitted exp':>13}{'26.5% partner':>16}")
    print("    " + "-" * 72)
    rows = []
    for n in (1.0, 1.5, 2.0, 2.13, 2.5, 3.0):
        i1, i2 = inh(COV["erda 3 mg"], n), inh(COV["erda 7 mg"], n)
        g1, g2 = OBS["erda 3 mg"] - TYPICAL, OBS["erda 7 mg"] - TYPICAL
        e = math.log(g2 / g1) / math.log(i2 / i1)
        r8 = resid(COV["erda 8 mg"], n)
        i8 = 1 - r8
        comb = 1 - r8 * (1 - 0.265)
        gain = (comb / i8) ** e
        rows.append((n, e, gain))
        print(f"    {n:>7.2f}{i1*100:>10.1f}%{i2*100:>10.1f}%{i8*100:>10.1f}%"
              f"{e:>13.2f}{gain:>15.2f}x")
    print("\n    AT THE HILL SLOPE MY OWN ATLAS IMPLIES, THE FITTED EXPONENT IS 0.94 -")
    print("    ESSENTIALLY LINEAR, NOT A POWER LAW. Round 217's headline claim, that the")
    print("    curve is supra-linear IN FRACTIONAL PATHWAY INHIBITION, does not survive.")

    print("\n[4] WHAT SURVIVES - AND IT IS THE VERSION THAT NEEDED NO ASSUMPTION")
    rule("-")
    e_c = math.log((OBS["erda 7 mg"] - TYPICAL) / (OBS["erda 3 mg"] - TYPICAL)) / \
        math.log(COV["erda 7 mg"] / COV["erda 3 mg"])
    print(f"    FIT THE GAIN AGAINST CONCENTRATION DIRECTLY AND NO HILL SLOPE IS NEEDED.")
    print(f"      human, in C/IC50 units    exponent {e_c:.2f}")
    print(f"      mouse, in dose units      exponent 3.23 and 3.33 (tibia, femur)")
    print("\n    BOTH SUPRA-LINEAR, BOTH ASSUMPTION-FREE. THE ROBUST CLAIM IS THEREFORE")
    print("    'GROWTH GAIN IS SUPRA-LINEAR IN EXPOSURE', NOT 'IN PATHWAY INHIBITION'. The")
    print("    two differ by exactly the Hill transformation, and only the first is measured.")
    print("    Round 217 should have led with this and did not.")

    print("\n[5] AND THE PRACTICAL CONCLUSION SURVIVES EVERY HILL SLOPE, WHICH IS LUCK")
    rule("-")
    lo = min(r[2] for r in rows)
    hi = max(r[2] for r in rows)
    print(f"    A partner removing 26.5 per cent of the pathway, added to 8 mg erdafitinib,")
    print(f"    is worth {lo:.2f} to {hi:.2f}-fold across Hill slopes from 1 to 3.")
    print("    THE TWO ERRORS CANCEL. A steeper Hill slope lowers the fitted exponent, which")
    print("    shrinks the payoff - but it ALSO lowers the fractional inhibition that 8 mg")
    print("    achieves, which means a fixed partner contribution moves the total")
    print("    proportionally further. The product is nearly flat in n.")
    print("\n    SO THE STRATEGY CONCLUSION HOLDS AND THE MECHANISTIC HEADLINE DOES NOT.")
    print("    A partner's INCREMENTAL gain is about six to ten times the 8-to-9 mg dose")
    print("    bump's across the same Hill range. I should have found this by running")
    print("    the sensitivity rather than by being asked to check.")

    print("\n[6] WHAT IS ACTUALLY LEFT IN THE INVENTORY, WHICH IS MUCH THINNER")
    rule("-")
    inv = [
        ("LIGAND", "DEAD IN HUMANS", "recifercept - three dose levels, twentyfold trough "
         "range, ratio 1.0, futility termination. Unresolved for a pathway-intact plate "
         "and no asset survives to test it"),
        ("RECEPTOR ABUNDANCE", "EMPTY", "the statin mechanism is refuted and there is no "
         "replacement - a literature sweep finds an erdafitinib-based FGFR2-selective "
         "degrader but NO FGFR3 degrader, and nothing in cartilage"),
        ("KINASE", "THE ANCHOR", "erdafitinib 8 mg, fixed by the user"),
        ("MAPK DOWNSTREAM", "WEAK BUT ALIVE", "meclizine - full human paediatric PK, and "
         "+0.11 cm/year alone on top of growth hormone. Consistent with a small series "
         "contribution and equally consistent with nothing"),
        ("CREB, ERK-INDEPENDENT", "WEAK FOR THIS CASE", "666-15 restored bone length in "
         "the achondroplasia mouse and WAS NULL IN WILD-TYPE - and wild-type is the "
         "relevant background here, so it corrects pathology rather than elevating a "
         "normal plate"),
        ("PARALLEL, NOT SERIES", "NOW THE STRONGEST SURVIVOR", "CNP arm two, the cAMP/PKA "
         "effect on hypertrophic zone elongation that hirota2022 showed is abolished by "
         "H89. It does not multiply with erdafitinib, it ADDS on a term FGFR3 blockade "
         "does not touch, and the atlas already specifies the 2x2 in wild-type that would "
         "test it"),
        ("THE COMPENSATORY LOOP", "UNTESTED AND UNCHANGED", "FGF19 and klotho-beta rise "
         "under FGFR3 inhibition. Still the one lever nobody has tried"),
    ]
    for tier, status, note in inv:
        print(f"\n    {tier:<24}{status}")
        for i in range(0, len(note), 82):
            print(f"        {note[i:i+82]}")

    print("\n[7] THE HONEST POSITION AFTER THIS BUNDLE")
    rule("-")
    print("    THE FRAMEWORK IS SOUND AND THE INVENTORY IS NOT. Multiplication at series")
    print("    nodes is arithmetically robust and worth roughly 2.2 to 2.9-fold for a")
    print("    modest partner on any Hill assumption. But of the four series nodes round")
    print("    217 named, ONE IS THE ANCHOR, TWO ARE NOW DEAD, and the fourth is a drug")
    print("    whose solo human effect is a tenth of a centimetre per year.")
    print("\n    THE STRONGEST REMAINING PARTNER IS NOT IN SERIES AT ALL - it is the CNP")
    print("    cAMP/PKA arm acting on terminal cell height, which adds rather than")
    print("    multiplies, and which the atlas has an unrun 2x2 design for.")
    print("\n    AND THE HONEST HEADLINE IS NARROWER THAN ROUND 217's. Growth gain is")
    print("    supra-linear IN EXPOSURE, assumption-free, in two species. Everything")
    print("    expressed per unit of pathway inhibition depends on a Hill slope that has")
    print("    never been measured in a chondrocyte for either drug.")
    rule()


if __name__ == "__main__":
    main()
