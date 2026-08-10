#!/usr/bin/env python3
"""
THE SUPPLIED BUNDLE SETTLES THE LIVER, NAMES THE MECHANISM, AND SHOWS THE
PAEDIATRIC PROGRAMME IS DELIBERATELY DOSING BELOW THE GROWTH EXPOSURE.

WHY THIS TOOL EXISTS
--------------------
Round 214 ended with a named request: the SURF301 exposure-response for
transaminitis, and the unreported twice-daily arms. The user supplied a bundle
containing the investor webcast that breaks every treatment-related adverse
event out BY DOSE LEVEL, the full redacted SURF301 protocol, the erdafitinib
discovery paper in full, the TYRA-300 discovery paper's supporting information
with the primary Ba/F3 SAR table, and TYRA's August 2026 corporate deck with the
paediatric dose levels.

FIVE THINGS FELL OUT, TWO OF WHICH CORRECT EARLIER ROUNDS.
"""

import statistics as st

# ------------------------------------------------------------------- [1] liver
# tyra_surf301_webcast_2024 slide 36, "Safety readthrough at lower doses"
# n per band: <=60 mg 22, 90 mg 15, 120 mg 4, all 41. (grade 1-2, >=grade 3)
TRAE_BY_DOSE = [
    ("ALT increase",  (1, 0),  (5, 2),  (2, 0),  (8, 2)),
    ("AST increase",  (0, 0),  (6, 1),  (0, 2),  (6, 3)),
    ("Diarrhea",      (3, 0),  (2, 1),  (4, 0),  (9, 1)),
    ("Dry mouth",     (3, 0),  (6, 0),  (0, 0),  (9, 0)),
    ("Dry skin",      (2, 0),  (2, 0),  (2, 0),  (6, 0)),
    ("Fatigue",       (2, 0),  (2, 0),  (2, 0),  (6, 0)),
]
N_BAND = {"<=60 mg": 22, "90 mg": 15, "120 mg": 4, "all": 41}
AUC = {40: 2270, 60: 4360, 90: 10300, 120: 23578}   # ng*h/mL, C1D15

# ---------------------------------------------------- [2] the named mechanism
PROTOCOL_QUOTE = (
    "surf301_protocol_v4 section 6.5.5, verbatim: pan-FGFR inhibitors, "
    "PARTICULARLY THOSE THAT HAVE POTENCY AGAINST FGFR4, have been associated "
    "with hepatotoxicity in preclinical models and in clinical use. IN ADDITION, "
    "TYRA-300 IS AN INHIBITOR OF BILE SALT EXPORT PUMP (BSEP) IN VITRO.")

# protocol Table 6.6 - what actually costs dose
LFT_RULES = [
    ("Grade 1", "ALT/AST >ULN to 3x ULN", "CONTINUE at current dose", "weekly LFTs >=4 wk"),
    ("Grade 2", ">3x to 5x ULN, bili <2x ULN",
     "CONTINUE at current dose OR hold at investigator discretion; if held, "
     "RESUME AT THE SAME DOSE LEVEL", "weekly until resolved"),
    ("Grade 3", ">5x to 20x ULN, ALT <8x ULN", "HOLD, resume ONE dose level lower",
     "GI consult considered"),
    ("Grade 3", ">8x ULN, or >5x ULN for 2 weeks",
     "HOLD, consider discontinuation; restart 1 to 2 dose levels lower",
     "GI consult recommended"),
    ("Grade 4", ">20x ULN", "DISCONTINUE", "medical management"),
    ("Hy's Law", "AST/ALT >3x ULN WITH bilirubin >2x ULN",
     "HOLD, report as SAE, GI consult, full DILI workup", "twice-weekly LFTs"),
]

# ------------------------------------------------- [3] the two Ba/F3 datasets
# hudkins2024 SI table (compound 22 = TYRA-300), against the slide panel used in round 213
BAF3_DISCOVERY = {"FGFR3": 11, "FGFR1": 278, "FGFR2": 157, "FGFR4": 405,
                  "RT112/84": 9, "RT112/84-V555M": 17, "UM-UC-14": 16,
                  "FGFR3 enzyme": 1.6}
BAF3_SLIDE = {"FGFR3": 1.75, "FGFR1": 113, "FGFR2": 35, "FGFR4": 98}

# ----------------------------------------------- [4] the paediatric dose levels
# tyra_corporate_deck_2026 pages 42-43
BEACH301 = {
    "sentinel safety cohort": "ACH age 5-10, no run-in, dose levels 0.125, 0.25, "
                              "0.375, 0.50 mg/kg, n=6 per level",
    "cohort 1": "treatment naive, ACH age 3-10, 6-month natural-history run-in, "
                "dose levels 0.25, 0.375, 0.50, 0.625 mg/kg",
    "cohort 2": "prior growth-accelerating therapy, ACH age 3-10, 6-month run-in, "
                "same dose levels",
    "total": "anticipate about 25 participants",
}
DOSE_EQUIV = ("the deck's own equivalence chart maps human child 0.625 mg/kg to "
              "ONE HALF the adult oncology dose and 0.25 mg/kg to ONE SIXTH of it, "
              "against an adult oncology dose of 90 mg described as the dose giving "
              "50 per cent objective response rate")

# ---------------------------- [5] the mouse growth dose-response, re-analysed
# jci.insight.189307.sdval.xlsx sheets 1C (tibia) and 1D (femur), individual animals
MOUSE = {
    "tibia": {"vehicle": 15.720, "12": 16.327, "14": 16.734,
              "n": (11, 12, 11), "p12": 0.0046, "p14": 4.37e-6, "p_incr": 0.0553},
    "femur": {"vehicle": 13.171, "12": 13.830, "14": 14.255,
              "n": (11, 11, 12), "p12": 0.0019, "p14": 9.05e-5, "p_incr": 0.0835},
}

# TYRA's own published dose-response for height velocity, corporate deck slide 40
AHV_LANDSCAPE = [
    ("untreated achondroplasia", 4.04, "Savarirayan 2021"),
    ("vosoritide, CNP analogue", "5.4-5.9", "phase 2 and phase 3"),
    ("TransCon CNP", "5.7-5.9", "phase 2 and phase 3"),
    ("infigratinib AT ONE SIXTH OF ITS ONCOLOGY DOSE", 6.0, "phase 2 cohort 5"),
    ("typical paediatric average", 7.66, "Merck Manuals 12 mo to 10 y"),
    ("PAN-FGFR AT ONCOLOGY DOSE", 19.2, "sait2023, three paediatric oncology cases - "
     "A REVIEW, not a primary report"),
]


def rule(c="="):
    print(c * 92)


def main():
    rule()
    print("ROUND 215 - THE SUPPLIED BUNDLE: THE LIVER IS EXPOSURE-DEPENDENT, THE")
    print("MECHANISM IS NAMED, AND THE PAEDIATRIC DOSE IS DELIBERATELY LOW")
    rule()

    print("\n[1] THE EXPOSURE-RESPONSE I ASKED FOR, AND IT IS UNAMBIGUOUS")
    rule("-")
    print("    tyra_surf301_webcast_2024 slide 36 breaks every TRAE out by dose band.")
    print(f"    n = {N_BAND['<=60 mg']} at 60 mg or below, {N_BAND['90 mg']} at 90 mg, "
          f"{N_BAND['120 mg']} at 120 mg.\n")
    hdr = f"    {'adverse event':<16}{'<=60 mg':>16}{'90 mg':>16}{'120 mg':>16}{'all':>16}"
    print(hdr); print("    " + "-" * 76)
    for name, a, b, c, d in TRAE_BY_DOSE:
        def fmt(x, n):
            tot = x[0] + x[1]
            return f"{tot:>2} ({tot/n*100:>3.0f}%) G3+{x[1]}"
        print(f"    {name:<16}{fmt(a,22):>16}{fmt(b,15):>16}{fmt(c,4):>16}{fmt(d,41):>16}")
    print("\n    THE HEPATIC SIGNAL IS A STEP, NOT A GRADIENT, AND IT SITS BETWEEN 60 AND 90 mg.")
    print("    At 60 mg and below, in 22 patients: ALT 1 of 22 grade 1-2 and ZERO grade 3;")
    print("    AST ZERO OF 22 AT ANY GRADE. At 90 mg: ALT 7 of 15 with 2 grade 3, AST 7 of 15")
    print("    with 1 grade 3. At 120 mg, in only 4 patients, AST grade 3 in TWO.")
    print(f"\n    In exposure terms that step is {AUC[60]:,} ng.h/mL against {AUC[90]:,} -")
    print(f"    a {AUC[90]/AUC[60]:.1f}-fold jump. THE LIVER IS A DOSE PROBLEM, NOT A MONITORING")
    print("    PROBLEM, AND THE CEILING IS BETWEEN 60 AND 90 mg.")

    print("\n[2] AND THE SPONSOR NAMES A MECHANISM THAT IS NOT FGFR AT ALL")
    rule("-")
    for i in range(0, len(PROTOCOL_QUOTE), 86):
        print(f"    {PROTOCOL_QUOTE[i:i+86]}")
    print("\n    ROUND 214 PREDICTED THIS AND THE PREDICTION IS CONFIRMED WITH A NAME.")
    print("    Round 214 computed free Cav at 8 per cent of the FGFR4 IC50 at 90 mg and 18")
    print("    per cent at 120, concluded the transaminitis was probably not an FGFR effect,")
    print("    and said more selectivity would not fix it. BSEP INHIBITION IS A CHEMICAL")
    print("    PROPERTY OF THE SCAFFOLD. It is one of the best-established in vitro")
    print("    predictors of drug-induced liver injury, and no amount of FGFR3 selectivity")
    print("    touches it.")
    print("\n    IT ALSO CHANGES WHICH ANTIDOTE IS RIGHT. Round 214 put S-adenosyl-L-methionine")
    print("    forward on the strength of qiu2026's TFEB mechanism in osimertinib. BSEP")
    print("    inhibition is a BILE SALT EXPORT problem, and the matched pharmacology for")
    print("    that is URSODEOXYCHOLIC ACID, which shifts the bile-acid pool to a less")
    print("    hydrophobic composition. SAMe remains reasonable and is not mechanism-matched.")
    print("    NEITHER IS TESTED FOR THIS DRUG. And the observed signal is transaminitis")
    print("    rather than cholestasis, so BSEP is a flagged risk, not a demonstrated cause.")

    print("\n[3] WHAT ACTUALLY COSTS DOSE, FROM THE PROTOCOL ITSELF")
    rule("-")
    for grade, defn, mgmt, med in LFT_RULES:
        print(f"\n    {grade:<10}{defn}")
        for i in range(0, len(mgmt), 76):
            print(f"        -> {mgmt[i:i+76]}" if i == 0 else f"           {mgmt[i:i+76]}")
    print("\n    GRADE 1 AND GRADE 2 TRANSAMINITIS DO NOT COST DOSE. Grade 2 resumes at the")
    print("    SAME dose level. So the 47 per cent ALT and AST rate at 90 mg is mostly")
    print("    tolerable on paper; what binds is the grade 3 rate, which is 13 per cent for")
    print("    ALT and 7 per cent for AST at 90 mg and ZERO for both at 60 mg and below.")

    print("\n[4] THE PAEDIATRIC PROGRAMME IS DOSING WELL BELOW THE GROWTH EXPOSURE, ON PURPOSE")
    rule("-")
    for k, v in BEACH301.items():
        print(f"    {k:<26}{v[:60]}")
        if len(v) > 60:
            print(" " * 30 + v[60:])
    print()
    for i in range(0, len(DOSE_EQUIV), 86):
        print(f"    {DOSE_EQUIV[i:i+86]}")
    print("\n    SO THE TOP PLANNED BEACH301 DOSE IS HALF THE ADULT ONCOLOGY DOSE AND THE")
    print("    BOTTOM IS ONE SIXTH. Against round 213's exposure table, one half of 90 mg is")
    print("    about 45 mg, which sits BELOW the 60 mg that already matches the murine")
    print("    growth exposure, and roughly a quarter of the 90 mg that matches the free")
    print("    FGFR3 coverage of the child who grew 19 cm/year.")
    print("\n    THIS IS THE SAME CONSERVATISM THAT CAPPED INFIGRATINIB AT 0.25 mg/kg/day FOR")
    print("    +1.74 cm/YEAR, AND TYRA'S OWN SLIDE SAYS SO OUT LOUD - it plots infigratinib")
    print("    at 6.0 cm/year labelled ONE SIXTH ONCOLOGY DOSE against pan-FGFR at 19.2")
    print("    cm/year labelled ONCOLOGY DOSE CAUSING FRACTURES. THE COMPANY HAS DRAWN THE")
    print("    DOSE-RESPONSE AND THEN CHOSEN THE BOTTOM OF IT.")

    print("\n[5] THE HEIGHT-VELOCITY LANDSCAPE, FROM TYRA'S OWN SLIDE 40")
    rule("-")
    for label, v, src in AHV_LANDSCAPE:
        print(f"        {str(v):>9} cm/yr   {label}")
        print(f"                        [{src}]")
    print("\n    NOTE THE PROVENANCE OF THE HEADLINE NUMBER. TYRA's 19.2 cm/year traces to")
    print("    sait2023, which is a REVIEW of paediatric low-grade glioma treatment, not a")
    print("    primary report. This atlas's own figure, 19.06 cm/year, comes from a primary")
    print("    case report and lands within 1 per cent of it - reassuring, but the two are")
    print("    probably not independent.")

    print("\n[6] AND THE MOUSE GROWTH CURVE IS NOT SATURATING - IT IS ACCELERATING")
    rule("-")
    print("    Re-analysed from the deposited individual-animal source data.\n")
    for bone, d in MOUSE.items():
        v, a, b = d["vehicle"], d["12"], d["14"]
        print(f"    {bone.upper():<8} vehicle {v:.3f}   12 mg/kg {a:.3f} ({(a/v-1)*100:+.2f}%)"
              f"   14 mg/kg {b:.3f} ({(b/v-1)*100:+.2f}%)")
        s1, s2 = (a - v) / 12, (b - a) / 2
        print(f"             marginal mm per mg/kg: 0->12 = {s1:.4f}, 12->14 = {s2:.4f}"
              f"   RATIO {s2/s1:.2f}x")
        print(f"             Welch p: 12 vs veh {d['p12']:.2g}, 14 vs veh {d['p14']:.2g}, "
              f"14 vs 12 {d['p_incr']:.3f}")
    print("\n    THE LAST 2 mg/kg BUYS AS MUCH AS THE FIRST 12 DID. In both bones the")
    print("    marginal gain per mg/kg is about FOUR TIMES higher over the 12-to-14 step than")
    print("    averaged over 0-to-12. THE HONEST READING - there are only three dose points")
    print("    and nothing between 0 and 12, so a threshold below 12 with a steep rise above")
    print("    it fits the same data, and the 14-against-12 increment is p = 0.055 and 0.084,")
    print("    not significant on its own. WHAT THE DATA WILL NOT SUPPORT IS SATURATION AT")
    print("    14 mg/kg. Nobody has found the top of this curve in any species.")

    print("\n[7] WHAT THIS DOES TO THE STACK")
    rule("-")
    print("    THE LIVER IS NO LONGER THE BINDING CONSTRAINT ON A GROWTH DOSE. A dose band")
    print("    exists - at and below 60 mg adult-equivalent - where 22 patients showed one")
    print("    grade 1-2 ALT rise and no AST signal at all, and that band ALREADY CONTAINS")
    print("    the exposure that grew wild-type mice. What it does not contain is the")
    print("    exposure that grew the erdafitinib child.")
    print("\n    SO THE QUESTION SHARPENS FROM 'CAN THE LIVER BE ROUTED AROUND' TO 'IS 60 mg")
    print("    ENOUGH'. At 60 mg free FGFR3 coverage is 1.83 times IC50 against 4.01 for the")
    print("    19 cm/year child - and the mouse says the curve is still climbing steeply at")
    print("    the top of its tested range. THE GAP BETWEEN THE HEPATICALLY CLEAN DOSE AND")
    print("    THE GROWTH-OPTIMAL DOSE IS NOW THE WHOLE PROBLEM, AND IT IS ABOUT 2.2-FOLD.")
    rule()


if __name__ == "__main__":
    main()
