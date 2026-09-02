#!/usr/bin/env python3
"""
THE FREE-CONCENTRATION COMPARISON ROUND 212 SAID COULD NOT BE COMPUTED.

WHY THIS TOOL EXISTS
--------------------
Round 212 closed with one named missing number: TYRA-300's human free plasma
concentration at 90 to 120 mg, against its FGFR3 cellular IC50. Without
TYRA-300's plasma protein binding the comparison with erdafitinib could only be
made on a pharmacodynamic bridge - tumour response rate - which is a downstream
readout across two different trials.

surf301_ena2024 supplies every piece. The steady-state AUC table is printed. The
Ba/F3 isoform IC50 panel is plotted on a linear axis for all five FGFR
inhibitors under identical conditions. And the PK figure draws four horizontal
target-coverage lines - FGFR1, FGFR2 and FGFR4 IC50 and FGFR3 IC90 - against
TOTAL plasma concentration, which means the offset between the plotted line and
the measured cellular IC50 IS the protein-binding adjustment. Three independent
isoforms give the same factor, so the binding can be recovered.

A DISCIPLINE NOTE. On first pass I derived TYRA-300's FGFR3 IC50 as about 7.3 nM
from the two numbers the text layer exposed (459 and 142) divided by the printed
63-fold and 19-fold selectivities. Rendering the figure showed 459 and 142 are
INFIGRATINIB'S and PEMIGATINIB'S FGFR4 values sitting past an axis break, and
TYRA-300's FGFR3 IC50 is about 1.75 nM. The error was caught before it entered
the atlas. Text extraction of a figure is not reading the figure.
"""

MW = {"erdafitinib": 446.5, "tyra300": 559.5}    # PubChem CID 67462786 / 170647464

# ------------------------------------------- Ba/F3 cellular IC50, nmol/L
# surf301_ena2024 slide 6. Values read off a LINEAR 0-120 nmol/L axis; the
# printed fold-selectivities are used to cross-check every read.
BAF3 = {
    "TYRA-300":    {"FGFR1": 113, "FGFR2": 35,  "FGFR3": 1.75, "FGFR4": 98},
    "erdafitinib": {"FGFR1": 5.7, "FGFR2": 2.1, "FGFR3": 1.35, "FGFR4": 17.5},
}
# printed fold selectivity (FGFR3 over X), same slide
FOLD_PRINTED = {
    "TYRA-300":    {"FGFR1": 63,  "FGFR2": 19,  "FGFR4": 55},
    "erdafitinib": {"FGFR1": 4.2, "FGFR2": 1.4, "FGFR4": 14},
    "futibatinib": {"FGFR1": 4.9, "FGFR2": 1.3, "FGFR4": 7.6},
    "pemigatinib": {"FGFR1": 2.4, "FGFR2": 0.8, "FGFR4": 27},
    "infigratinib":{"FGFR1": 2.2, "FGFR2": 0.8, "FGFR4": 67},
}

# ------------------------------------------------------------- pharmacokinetics
# erdafitinib: zhu2026 population PK. TYRA-300: surf301_ena2024 slide 12 table.
ERDA_CL_L_PER_H = 0.362
ERDA_FU = 0.003                      # 99.7 % bound, primarily to AGP
TYRA_AUC24 = {40: 2270, 60: 4360, 90: 10300, 120: 23578}   # ng*h/mL, C1D15
TYRA_N     = {40: 10,   60: 8,     90: 13,    120: 3}
ERDA_DOSES = {3: "erdaseries2025 pt 1 after reduction, still grew ~10 cm/yr",
              5: "erdaseries2025 pt 1 start; erdachild2024 months 6-9",
              7: "erdachild2024 months 1-5 -> the 19.06 cm/yr case",
              8: "BALVERSA label starting dose",
              9: "BALVERSA label MAXIMUM"}

# ------------------- recovering TYRA-300 protein binding from the coverage lines
# surf301_ena2024 slide 12: horizontal lines on a log ng/mL axis, read by pixel
# against the decade ticks. These are the ONLY estimated inputs in this file.
LINES_NG_PER_ML = {"FGFR1": 6890, "FGFR4": 5105, "FGFR2": 1990, "FGFR3_IC90": 277}

# ------------------------------------------------- the murine translational anchor
MURINE_ANCHOR_AUC = 6500    # ng*h/mL, "Murine 18 mg/kg" line, slide 13, read off a log axis
MURINE_ONCOLOGY_MGKG = 18   # 96 % TGI in UM-UC-14; beat erdafitinib 12.5 mg/kg BID
MURINE_GROWTH_MGKG = (12, 14)   # tyra300_2025, WILD-TYPE mice, significant length gain

# --------------------------------------------- what actually caps erdafitinib's dose
# surf301_ena2024 slides 4 and 5, from the BALVERSA label, study BLC3001, n=135
ERDA_AE = [
    ("Hyperphosphatemia", "FGFR1", 75, 4, 7, 4.4),
    ("Nail disorders",    "FGFR2", 69, 12, 22, 27),
    ("Diarrhea",          "other", 62, 2, 10, 7),
    ("Stomatitis",        "FGFR2", 56, 10, 19, 19),
    ("ALT increase",      "other", 45, 3, 5, None),
    ("AST increase",      "other", 44, 4, 6, None),
    ("Dry mouth",         "FGFR2", 38, 0, None, 4.4),
    ("PPE",               "FGFR2", 30, 10, 15, 12),
    ("Dry skin",          "other", 26, 1, None, None),
    ("Dry eye",           "FGFR2", 25, 2, None, None),
    ("Central serous retinopathy", "FGFR2", 18, 3, None, None),
]
ERDA_TOTALS = {"interruption": 72, "reduction": 69, "discontinuation": 14}
# TYRA-300 at the working dose, slide 18, n=15
TYRA_90 = [("Nail disorders", "FGFR2", 7), ("Stomatitis", "FGFR2", 7),
           ("Dry mouth", "FGFR2", 40), ("PPE", "FGFR2", 13),
           ("Dry eye", "FGFR2", 0), ("Central serous retinopathy", "FGFR2", 7),
           ("Hyperphosphatemia", "FGFR1", 13), ("Diarrhea", "other", 20),
           ("ALT increase", "other", 47), ("AST increase", "other", 47),
           ("Dry skin", "other", 13)]
TYRA_TOTALS = {"reduction (90 mg)": 27, "discontinuation (90 mg)": 7,
               "any TRAE (all doses, n=41)": 78, ">=grade 3 TRAE (n=41)": 20}


def rule(c="="):
    print(c * 92)


def cav_ng_per_ml(auc24):
    return auc24 / 24.0


def to_nM(ng_per_ml, mw):
    return ng_per_ml / mw * 1000.0


def main():
    rule()
    print("FGFR3 FREE TARGET COVERAGE - ERDAFITINIB AGAINST TYRA-300, ON ONE AXIS")
    rule()

    # ---------------------------------------------------------------- step 1
    print("\n[1] CROSS-CHECKING THE IC50 READS AGAINST THE PRINTED FOLD SELECTIVITIES")
    print("    Every IC50 below is read off a linear axis, so each read is checked")
    print("    against the fold value printed on the same slide.\n")
    for drug in ("TYRA-300", "erdafitinib"):
        f3 = BAF3[drug]["FGFR3"]
        print(f"    {drug}   FGFR3 = {f3} nmol/L")
        for iso in ("FGFR1", "FGFR2", "FGFR4"):
            implied = BAF3[drug][iso] / f3
            print(f"        {iso}: read {BAF3[drug][iso]:>6.1f} nmol/L -> implies "
                  f"{implied:>5.1f}x   printed {FOLD_PRINTED[drug][iso]}x")
    print("\n    ERDAFITINIB IS SLIGHTLY MORE POTENT AT FGFR3 THAN TYRA-300 "
          f"({BAF3['erdafitinib']['FGFR3']} against {BAF3['TYRA-300']['FGFR3']} nmol/L).")
    print("    The selectivity is NOT bought with on-target potency, and it is not free")
    print("    either - the whole difference is what they do to the other three isoforms.")

    print("\n    AND THE PAN AGENTS ARE NOT UNIFORMLY UNSELECTIVE - the atlas has been")
    print("    saying 'no meaningful FGFR3 selectivity at all', which is only true at FGFR2:")
    print(f"\n        {'drug':<15}{'over FGFR1':>12}{'over FGFR2':>12}{'over FGFR4':>12}")
    for d, f in FOLD_PRINTED.items():
        print(f"        {d:<15}{f['FGFR1']:>11}x{f['FGFR2']:>11}x{f['FGFR4']:>11}x")
    print("\n    AT FGFR2 THE FOUR PAN AGENTS RUN 0.8 TO 1.4-FOLD - equipotent, and for")
    print("    pemigatinib and infigratinib INVERTED, i.e. more potent at FGFR2 than at")
    print("    FGFR3. TYRA-300's 19-fold is its THINNEST margin and it is still 14-fold")
    print("    better than erdafitinib's on that axis.")

    # ---------------------------------------------------------------- step 2
    print("\n[2] RECOVERING TYRA-300 PLASMA PROTEIN BINDING FROM THE COVERAGE LINES")
    rule("-")
    print("    Slide 12 plots TOTAL plasma concentration and draws the isoform target")
    print("    lines on the same axis. If those lines were raw cellular IC50s they would")
    print("    sit far lower, so the offset is a protein-binding adjustment. Three")
    print("    isoforms, three independent checks:\n")
    factors = []
    for iso in ("FGFR1", "FGFR2", "FGFR4"):
        line_nM = to_nM(LINES_NG_PER_ML[iso], MW["tyra300"])
        f = line_nM / BAF3["TYRA-300"][iso]
        factors.append(f)
        print(f"        {iso}: line {LINES_NG_PER_ML[iso]:>5} ng/mL = {line_nM:>8.0f} nmol/L "
              f"/ IC50 {BAF3['TYRA-300'][iso]:>5.1f} = {f:>5.0f}x")
    mean_f = sum(factors) / len(factors)
    fu_tyra = 1.0 / mean_f
    print(f"\n        mean factor {mean_f:.0f}x  ->  FRACTION UNBOUND ABOUT "
          f"{fu_tyra*100:.1f} PER CENT")
    ic90_nM = to_nM(LINES_NG_PER_ML["FGFR3_IC90"], MW["tyra300"])
    print(f"\n    CONSISTENCY CHECK ON THE FOURTH LINE. FGFR3 IC90 sits at "
          f"{LINES_NG_PER_ML['FGFR3_IC90']} ng/mL")
    print(f"    = {ic90_nM:.0f} nmol/L total; unadjusted that is {ic90_nM/mean_f:.2f} nmol/L, "
          f"which is")
    print(f"    {ic90_nM/mean_f/BAF3['TYRA-300']['FGFR3']:.1f}x the {BAF3['TYRA-300']['FGFR3']} "
          "nmol/L IC50 - a Hill slope near 2.2, entirely ordinary for a")
    print("    48-hour viability assay. FOUR LINES, ONE FACTOR, NO FREE PARAMETERS.")

    # ---------------------------------------------------------------- step 3
    print("\n[3] THE COMPARISON, IN FREE MULTIPLES OF EACH DRUG'S OWN FGFR3 IC50")
    rule("-")
    print(f"    erdafitinib: fu = {ERDA_FU*100:.1f} per cent (zhu2026), FGFR3 IC50 "
          f"{BAF3['erdafitinib']['FGFR3']} nmol/L")
    print(f"    TYRA-300   : fu = {fu_tyra*100:.1f} per cent (derived above), FGFR3 IC50 "
          f"{BAF3['TYRA-300']['FGFR3']} nmol/L\n")
    print(f"    {'drug / dose':<26}{'Cav total':>12}{'free nM':>10}{'x IC50':>9}   note")
    print("    " + "-" * 86)
    erda_ref = None
    for d, note in ERDA_DOSES.items():
        tot = d * 1000.0 / (ERDA_CL_L_PER_H * 24.0)
        free = to_nM(tot, MW["erdafitinib"]) * ERDA_FU
        x = free / BAF3["erdafitinib"]["FGFR3"]
        if d == 7:
            erda_ref = x
        print(f"    erdafitinib {d:>2} mg{'':<9}{tot:>11.0f}{free:>10.2f}{x:>9.2f}   {note[:34]}")
    print()
    for d in sorted(TYRA_AUC24):
        tot = cav_ng_per_ml(TYRA_AUC24[d])
        free = to_nM(tot, MW["tyra300"]) * fu_tyra
        x = free / BAF3["TYRA-300"]["FGFR3"]
        print(f"    TYRA-300 {d:>3} mg (n={TYRA_N[d]:>2}){'':<3}{tot:>11.0f}{free:>10.2f}"
              f"{x:>9.2f}   AUC {TYRA_AUC24[d]:,} ng*h/mL")

    x90 = to_nM(cav_ng_per_ml(TYRA_AUC24[90]), MW["tyra300"]) * fu_tyra / BAF3["TYRA-300"]["FGFR3"]
    x120 = to_nM(cav_ng_per_ml(TYRA_AUC24[120]), MW["tyra300"]) * fu_tyra / BAF3["TYRA-300"]["FGFR3"]
    x9 = (9 * 1000.0 / (ERDA_CL_L_PER_H * 24.0)) / MW["erdafitinib"] * 1000.0 * ERDA_FU \
        / BAF3["erdafitinib"]["FGFR3"]
    print("\n    THE ANSWER, AND IT IS CLEANER THAN ANYTHING I EXPECTED TO GET:")
    print(f"      - the child who grew 19.06 cm/year sat at {erda_ref:.2f}x his drug's FGFR3 IC50")
    print(f"      - TYRA-300 at 90 mg sits at {x90:.2f}x - THE SAME EXPOSURE, in free terms")
    print(f"      - TYRA-300 at 120 mg sits at {x120:.2f}x")
    print(f"      - erdafitinib's ABSOLUTE label maximum is {x9:.2f}x")
    print(f"    SO 120 mg IS {x120/x9:.2f}x ABOVE ANYTHING ERDAFITINIB CAN EVER REACH, and the")
    print("    MTD HAS NOT BEEN REACHED. The answer to 'is TYRA even possible at a dose we")
    print("    can benefit from beyond erda' is YES, WITH ROOM, AND IT IS ALREADY DOSED THERE.")

    # ---------------------------------------------------------------- step 4
    print("\n[4] THE HUMAN EXPOSURE-RESPONSE FOR GROWTH THAT NOW EXISTS, WITH TWO POINTS")
    rule("-")
    x3 = (3 * 1000.0 / (ERDA_CL_L_PER_H * 24.0)) / MW["erdafitinib"] * 1000.0 * ERDA_FU \
        / BAF3["erdafitinib"]["FGFR3"]
    print(f"      {x3:.2f}x FGFR3 IC50  ->  about 10 cm/year   (erdaseries2025 patient 1, 3 mg)")
    print(f"      {erda_ref:.2f}x FGFR3 IC50  ->  19.06 cm/year     (erdachild2024, 7 mg)")
    print(f"\n    A {erda_ref/x3:.1f}-fold rise in free target coverage travels with a roughly")
    print("    1.9-fold rise in height velocity. THIS IS THE ONLY HUMAN EXPOSURE-RESPONSE")
    print("    FOR FGFR3 BLOCKADE AND GROWTH THAT EXISTS AND IT IS TWO PATIENTS. They differ")
    print("    in age, in growth hormone status, in gonadal status and in how much catch-up")
    print("    was available, and neither paper reports velocity by dose period. IT IS NOT A")
    print("    DOSE-RESPONSE CURVE. It is two points that happen to lie in the right order,")
    print("    and it is recorded here so that a third point can be placed against it.")
    print(f"\n    FOR SCALE: TYRA-300 at 120 mg is {x120:.1f}x coverage, which is {x120/erda_ref:.1f}x")
    print("    beyond the 19 cm/year point. NOTHING JUSTIFIES EXTRAPOLATING THE VELOCITY")
    print("    THERE - two points define a line only if you already believe it is one.")

    # ---------------------------------------------------------------- step 5
    print("\n[5] THE MURINE BRIDGE - HUMAN 60 mg ALREADY MATCHES THE GROWTH DOSE")
    rule("-")
    print(f"    Slide 13 draws the murine {MURINE_ONCOLOGY_MGKG} mg/kg AUC as a horizontal line")
    print(f"    across the human dose groups, at about {MURINE_ANCHOR_AUC:,} ng*h/mL.")
    lo, hi = MURINE_GROWTH_MGKG
    for mgkg in (lo, hi, MURINE_ONCOLOGY_MGKG):
        auc = MURINE_ANCHOR_AUC * mgkg / MURINE_ONCOLOGY_MGKG
        tag = ("GROWS WILD-TYPE MICE" if mgkg in MURINE_GROWTH_MGKG
               else "96 per cent tumour growth inhibition")
        print(f"        murine {mgkg:>2} mg/kg  ->  about {auc:>6,.0f} ng*h/mL   {tag}")
    print("\n    Against the human table:")
    for d in sorted(TYRA_AUC24):
        r = TYRA_AUC24[d] / (MURINE_ANCHOR_AUC * lo / MURINE_ONCOLOGY_MGKG)
        print(f"        human {d:>3} mg QD -> {TYRA_AUC24[d]:>6,} ng*h/mL = {r:>4.1f}x the "
              f"murine {lo} mg/kg growth exposure")
    print("\n    HUMAN 60 mg QD IS ALREADY THE MOUSE GROWTH DOSE. 90 mg is about twice it and")
    print("    120 mg about five times it. THE ASSUMPTION IS LINEAR DOSE-TO-AUC SCALING IN THE")
    print("    MOUSE across 12, 14 and 18 mg/kg, which was not measured - tyra300_2025's only")
    print("    mouse PK is a single 1.2 mg/kg SUBCUTANEOUS dose while the growth study was")
    print("    ORAL. The 18 mg/kg anchor itself is printed, so only the interpolation is mine.")

    # ---------------------------------------------------------------- step 6
    print("\n[6] AND THE GATE IS FGFR2, NOT FGFR1 - ROUND 212 GOT THIS WRONG")
    rule("-")
    print(f"    erdafitinib, n = 135, study BLC3001. Interruption "
          f"{ERDA_TOTALS['interruption']} per cent, reduction "
          f"{ERDA_TOTALS['reduction']} per cent, discontinuation "
          f"{ERDA_TOTALS['discontinuation']} per cent.\n")
    print(f"    {'adverse reaction':<30}{'axis':>7}{'any':>6}{'>=G3':>6}{'->intr':>8}{'->red':>7}")
    print("    " + "-" * 76)
    for name, axis, any_g, g3, intr, red in ERDA_AE:
        i = f"{intr}" if intr is not None else "-"
        r = f"{red}" if red is not None else "-"
        print(f"    {name:<30}{axis:>7}{any_g:>6}{g3:>6}{i:>8}{r:>7}")
    print("\n    HYPERPHOSPHATAEMIA IS THE MOST FREQUENT TOXICITY AND THE LEAST DOSE-LIMITING.")
    print("    75 per cent incidence but only about 4 per cent grade 3, and it drives 7 per")
    print("    cent of interruptions and 4.4 per cent of reductions - it is managed with diet")
    print("    and binders, not with dose. THE DOSE COMES DOWN FOR FGFR2 EPITHELIAL TOXICITY:")
    print("    nail disorders 22 and 27 per cent, stomatitis 19 and 19, eye disorders 16 and")
    print("    17, palmar-plantar erythrodysesthesia 15 and 12.")
    print("\n    ROUND 212 SAID THE GATE WAS FGFR1 AND PHOSPHATE. HALF RIGHT AND THE WRONG HALF.")
    print("    The label TITRATES UP on phosphate - that part stands, phosphate is an FGFR1")
    print("    pharmacodynamic marker used to push the dose higher. But the dose COMES DOWN")
    print("    for FGFR2. And the index child WAS interrupted for hyperphosphataemia, so in")
    print("    the one paediatric case phosphate was the gate - n = 1, and a growing skeleton")
    print("    handles phosphate differently from an elderly urothelial cancer patient.")

    print("\n    TYRA-300 AT 90 mg QD, n = 15, ON THE SAME AXES:")
    print(f"\n    {'adverse reaction':<30}{'axis':>7}{'any %':>7}")
    print("    " + "-" * 46)
    for name, axis, pct in TYRA_90:
        print(f"    {name:<30}{axis:>7}{pct:>7}")
    print()
    for k, v in TYRA_TOTALS.items():
        print(f"        {k:<34}{v} per cent")
    print("\n    THE FOUR TOXICITIES THAT ACTUALLY CAP ERDAFITINIB ARE 7, 7, 0 AND 13 PER CENT")
    print("    HERE. Dose reduction at 90 mg is 27 per cent against erdafitinib's 69, and")
    print("    discontinuation 7 per cent against 14. And no phosphorus above 7.0 mg/dL at ANY")
    print("    dose, with one patient needing a binder.")

    print("\n[7] BUT THE CEILING MOVED RATHER THAN DISAPPEARING, AND IT IS NOW THE LIVER")
    rule("-")
    print("    At 90 mg QD, ALT rose in 47 per cent and AST in 47 per cent, both with a")
    print("    substantial grade 3 or worse component. The single dose-limiting toxicity in")
    print("    the whole study was grade 3 diarrhoea at 90 mg and the single drug-related")
    print("    discontinuation was grade 3 ALT at 90 mg. The sponsor classes transaminitis")
    print("    as an OTHER adverse event, not FGFR1, 2 or 4.")
    free90 = to_nM(cav_ng_per_ml(TYRA_AUC24[90]), MW["tyra300"]) * fu_tyra
    free120 = to_nM(cav_ng_per_ml(TYRA_AUC24[120]), MW["tyra300"]) * fu_tyra
    print(f"\n    AND THE ARITHMETIC SAYS THEY ARE RIGHT. Free Cav at 90 mg is {free90:.2f} nmol/L")
    print(f"    against an FGFR4 IC50 of {BAF3['TYRA-300']['FGFR4']} nmol/L - that is "
          f"{free90/BAF3['TYRA-300']['FGFR4']*100:.0f} per cent of IC50. At 120 mg it is")
    print(f"    {free120/BAF3['TYRA-300']['FGFR4']*100:.0f} per cent. FGFR4 IS BARELY ENGAGED, "
          "so the transaminitis is almost")
    print("    certainly NOT an FGFR effect - which means MORE SELECTIVITY WILL NOT FIX IT.")
    print("    IT IS A PROPERTY OF THIS MOLECULE, AND IT IS THE NEW CEILING.")
    print("\n    WHETHER THAT CEILING SITS ABOVE OR BELOW THE GROWTH-OPTIMAL DOSE IS THE")
    print("    QUESTION THIS DOCUMENT OPENS AND CANNOT ANSWER. What it does establish is that")
    print(f"    the ceiling is at least {x120:.0f}x FGFR3 coverage, because 120 mg was given.")
    rule()


if __name__ == "__main__":
    main()
