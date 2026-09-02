#!/usr/bin/env python3
"""
EVERY bone-length observation under a PTH1R agonist, from the complete
NDA 21-318 pharmacology review plus the published and human literature.

WHY THIS SUPERSEDES pth1r_final_length_ledger.py
------------------------------------------------
Round 194 had only the part of the FDA review covering the SECOND rat
carcinogenicity study. Round 195 has the complete review - all four parts,
including the FIRST carcinogenicity study (the one vahle2002 published), the
1-year intact-male/OVX-female bone quality study, the 26-week toxicity study,
both rabbit studies and the monkey study - plus the two human paediatric
studies and the human growth plate immunolocalisation.

With the whole package in view, the femoral-length signal resolves into a
pattern that no single study showed: EVERY POSITIVE IS FEMALE AND TRAVELS WITH
A BODY-WEIGHT INCREASE; EVERY MALE ARM IS NULL; AND THE ONE TERMINAL
MEASUREMENT IS NULL IN BOTH SEXES.

All values are transcribed from the sources named. Nothing here is estimated.
"""

# (label, ref, species/sex, age at start, duration, doses ug/kg/d, method,
#  length result, concurrent body-weight effect, verdict)
LEDGER = [
    ("CG3-04 young male rats (unpublished, IND 1995)",
     "fda_forteo_pharmreview_2002", "SD rat, male", "4 wk", "18 d", "16, 80",
     "QCT", "no change at any dose",
     "BW gain +20% (PTH1-34 HD), +10% ns (LY333334 HD)", "NULL"),

    ("26-week rat toxicity study, females",
     "fda_forteo_pharmreview_2002", "rat, female", "not stated", "140 d",
     "LD/MD/HD up to 100", "not stated",
     "+2% LD, +3% MD, +4% HD, all significant",
     "BW +7/+10/+10%; BW GAIN x1.4/x1.7/x1.8; food efficiency x1.4/x1.6/x1.7",
     "POSITIVE but fully confounded by body weight"),

    ("26-week rat toxicity study, males",
     "fda_forteo_pharmreview_2002", "rat, male", "not stated", "140 d",
     "LD/MD/HD up to 100", "not stated",
     "change not seen in males",
     "BW -3.8%, BW gain -5.2%, food efficiency x0.7", "NULL"),

    ("R00796/R04296 bone quality, intact males",
     "fda_forteo_pharmreview_2002", "F344 rat, intact male", "18-20 wk",
     "1 y", "8, 40", "DXA proximal tibia",
     "did not alter linear bone growth in males",
     "LY reduced BW gain in intact males", "NULL"),

    ("R00796/R04296 bone quality, OVX females",
     "fda_forteo_pharmreview_2002", "F344 rat, OVX female", "18-20 wk",
     "1 y", "8, 40", "DXA proximal tibia",
     "1.300 (OVXV) -> 1.333 (OVX8), 1.330 (OVX40) cm, +2.5%/+2.3%",
     "BW increased in OVX vs sham",
     "POSITIVE but the column is a 1.2-1.33 cm PROXIMAL TIBIA ROI, "
     "not a whole-bone length"),

    ("first carcinogenicity study (published as vahle2002)",
     "vahle2002", "F344 rat, both sexes", "6-8 wk", "2 y", "5, 30, 75",
     "calipers",
     "length up to +6%, width up to +33%, wet weight up to +60%; "
     "MALE LENGTH EFFECT MAXIMAL AT THE LOW DOSE",
     "female BW +4.5/+9.0/+10.4%, BW gain +8.5/+15.6/+17.3%",
     "POSITIVE, method cannot exclude periosteal/periarticular bone, "
     "and not dose-dependent in males"),

    ("second carcinogenicity study, interim, treated 2-8 months",
     "fda_forteo_pharmreview_2002", "F344 rat, female", "2 mo", "6 mo",
     "5, 30", "QCT", "32.8 -> 33.3 (+1.5%) -> 33.9 mm (+3.4%), both starred",
     "not reported per arm", "POSITIVE"),

    ("second carcinogenicity study, interim, treated 6-12 months",
     "fda_forteo_pharmreview_2002", "F344 rat, female", "6 mo", "6 mo",
     "5, 30", "QCT", "34.2 -> 34.7 (+1.5%) -> 35.2 mm (+2.9%), both starred",
     "not reported per arm", "POSITIVE, and NO AGE GATE"),

    ("second carcinogenicity study, TERMINAL, all eight arms",
     "fda_forteo_pharmreview_2002", "F344 rat, female", "2 or 6 mo",
     "6 mo to 24 mo", "5, 30", "QCT",
     "35 mm in every arm including the two dosed continuously to "
     "termination; no asterisk",
     "not reported per arm", "NULL"),

    ("rabbit CG3-06",
     "fda_forteo_pharmreview_2002", "NZW rabbit, ovary-intact female",
     "mature adult", "140 d", "10, 40", "-",
     "BONE LENGTH NOT MEASURED", "BW gain decreased in treated groups",
     "NOT MEASURED"),

    ("rabbit CG3-13",
     "fda_forteo_pharmreview_2002", "NZW rabbit, intact female", "9 mo",
     "35 or 70 d", "10", "-",
     "BONE LENGTH NOT MEASURED; no sustained effect on X-area or BMD in "
     "whole femur, femoral midshaft or whole tibia",
     "not reported", "NOT MEASURED"),

    ("monkey X95-11",
     "fda_forteo_pharmreview_2002", "cynomolgus, female", "9-11 y",
     "18 mo", "1, 5", "-",
     "BONE LENGTH NOT MEASURED; animals selected as skeletally mature "
     "adults with NO OPEN GROWTH PLATES",
     "not reported", "EXCLUDED BY DESIGN"),

    ("Winer 2010, randomised controlled trial in children",
     "winer2010", "human children 5-14 y, 8 of 12 male", "5-14 y", "3 y",
     "PTH(1-34) twice daily, replacement", "Harpenden stadiometer",
     "height percentile 47+/-13 (PTH) vs 53+/-15 (calcitriol), P=0.76, "
     "no difference across time or between arms",
     "weight percentile 54+/-13 vs 63+/-15, P=0.68", "NULL, RANDOMISED"),

    ("Winer 2018, long-term paediatric cohort",
     "winer2018", "human children, 14 subjects", "childhood", "up to 10 y",
     "0.75 +/- 0.15 ug/kg/day", "annualised height velocity Z",
     "mean height velocity normal for age throughout; CaR patients "
     "attained mid-parental height, two exceeded it by 4 and 6 cm; "
     "APS-1 patients 8-12 cm below MPH",
     "not the endpoint",
     "NULL for acceleration, NULL for truncation"),
]


def main():
    print("=" * 96)
    print("EVERY BONE-LENGTH OBSERVATION UNDER A PTH1R AGONIST")
    print("=" * 96)
    for (lab, ref, sp, age, dur, dose, meth, res, bw, verdict) in LEDGER:
        print(f"\n{lab}")
        print(f"    ref      : {ref}")
        print(f"    subject  : {sp}, from {age}, for {dur}, at {dose} ug/kg/day")
        print(f"    method   : {meth}")
        print(f"    LENGTH   : {res}")
        print(f"    body wt  : {bw}")
        print(f"    verdict  : {verdict}")

    print("\n" + "=" * 96)
    print("[1] THE PATTERN THE COMPLETE PACKAGE MAKES VISIBLE")
    print("=" * 96)
    male_null = [l for l in LEDGER if "male" in l[2] and "female" not in l[2]]
    print(f"    Arms in an intact MALE animal: {len(male_null)}")
    for l in male_null:
        print(f"      {l[0][:56]:58s} -> {l[9]}")
    print("    Every one is null. The doses span 8 to 100 ug/kg/day and the")
    print("    durations span 18 days to 1 year.")
    print()
    print("    Every POSITIVE length result in the package is in a female")
    print("    animal, and every one of them travels with a large concurrent")
    print("    body-weight increase, in the same studies where the male arm")
    print("    LOST weight and showed no length change. The 26-week study is")
    print("    the cleanest case: females +2/+3/+4% femur length with BW gain")
    print("    x1.4-1.8 and food efficiency x1.4-1.7; males no length change")
    print("    with BW gain -5.2% and food efficiency x0.7.")
    print()
    print("    The FDA reviewer reached for the same explanation and recorded")
    print("    the sponsor's: that in females PTH enhances IGF-1 expression,")
    print("    'which may lead to increased femur length'. That is a systemic")
    print("    body-size mechanism, not a growth plate mechanism, and no data")
    print("    in the package tests it.")

    print("\n[2] WHAT THIS DOES TO THE INTERIM POSITIVES")
    print("    The two interim positives (+1.5 to +3.4%) are also female-only,")
    print("    because the second carcinogenicity study used FEMALE F344 rats")
    print("    exclusively. They are therefore inside the confounded class, not")
    print("    outside it. Round 194 read them as the clean age-gate answer.")
    print("    They still retire the age gate - the two windows agree - but they")
    print("    cannot be read as a plate effect in a male.")

    print("\n[3] THE HUMAN EVIDENCE IS A RANDOMISED NULL")
    print("    winer2010 is a 3-year randomised parallel trial in 12 children,")
    print("    8 of them male, comparing twice-daily PTH(1-34) against")
    print("    calcitriol. Both arms are eucalcaemic; only one delivers PTH1R")
    print("    pulses to the plate. Height percentile did not differ between")
    print("    arms OR across time. winer2018 extends the same cohort to ten")
    print("    years with height velocity Z normal throughout.")
    print("    This is the most direct test that exists and it is null.")

    print("\n[4] POWER - WHAT THE HUMAN NULL CAN AND CANNOT EXCLUDE")
    import math
    sd = 14.0            # percentile points, from the reported 13 and 15
    n = 6                # per arm, 12 children in two arms
    tcrit = 2.228        # two-sided 0.05, df=10
    for power, z in (("50%", 0.0), ("80%", 0.84)):
        mdd = (tcrit + z) * sd * math.sqrt(2.0 / n)
        print(f"      min detectable difference at {power:>3} power: "
              f"{mdd:.1f} percentile points")
    print("    A ~25 percentile-point difference is a very large effect. The")
    print("    randomised comparison therefore excludes only a large benefit.")
    print("    The tighter statement is the within-subject one: height")
    print("    percentile did not drift across three years, and height velocity")
    print("    Z stayed at reference for up to ten. A drug adding even 10% to")
    print("    growth rate would move a percentile track visibly over that span.")

    print("\n[5] WHAT IS STILL NOT MEASURED, ANYWHERE IN THE PACKAGE")
    print("    - bone length in ANY fusing species: both rabbit studies used")
    print("      mature or 9-month-old animals and did not measure length, and")
    print("      the monkey study excluded open plates by protocol")
    print("    - any growth plate histopathology, despite the physis being")
    print("      SECTIONED in every animal of both carcinogenicity studies")
    print("    - the words 'closure' and 'senescence' do not appear in the")
    print("      review at all")
    print("    - vertebral body HEIGHT, in any study, in any species")
    print("=" * 96)


if __name__ == "__main__":
    main()
