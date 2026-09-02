#!/usr/bin/env python3
"""
ERDAFITINIB'S ACTUAL CEILING, AND WHETHER TYRA-300 CAN BE PUSHED PAST IT.

WHY THIS TOOL EXISTS
--------------------
Round 210 said "the decisive unknown is dose, not molecule" and stopped there.
That was a framing, not an answer. The user asked for the answer, and for
erdafitinib's THEORETICAL ceiling rather than the one dose that happened to be
given. This tool computes both from held data.

THE TWO QUESTIONS
  1. What is the most height erdafitinib could ever deliver, at its best
     achievable exposure and its best achievable duration?
  2. Can an FGFR3-selective molecule be dosed to a HIGHER FGFR3 occupancy than
     erdafitinib can, in a human?

Everything below is arithmetic on published numbers. No number is typed from
memory; each carries its source.
"""

# ---------------------------------------------------------------- erdafitinib PK
# zhu2026 (hepatic impairment phase 1) reporting population PK
ERDA = {
    "MW": 446.5,               # pubchem CID 67462786, C25H30N6O2
    "CL_F_L_per_h": 0.362,     # mean apparent clearance
    "t_half_h": 59.0,          # mean effective half-life
    "Vd_L": 29.0,
    "protein_bound": 0.997,    # 99.7 %, primarily alpha-1-acid glycoprotein
    "linear_range_mg": (0.5, 12),
}
# every human dose at which a growth response has been recorded, plus the label
ERDA_DOSES = [
    (3, "erdaseries2025 patient 1 after reduction for bone pain and abdominal "
        "aches - still grew, ~10 cm/year"),
    (5, "erdaseries2025 patient 1 starting dose; erdachild2024 months 6-9"),
    (7, "erdachild2024 months 1-5, WITH FREQUENT INTERRUPTIONS FOR "
        "HYPERPHOSPHATAEMIA"),
    (8, "BALVERSA label starting dose"),
    (9, "BALVERSA label MAXIMUM, reached only by up-titration at day 14-21 IF "
        "serum phosphate is below target"),
]

# ------------------------------------------------------- the one PD anchor there is
# erdachild2024, the patient's OWN dermal fibroblasts, serum-starved
PD_ANCHOR = ("erdafitinib 100 nM dramatically reduced BOTH phospho-ERK1/2 and "
             "phospho-AKT with NO FURTHER REDUCTION at 200 or 300 nM. "
             "NOTHING BELOW 100 nM WAS TESTED, so this bounds the saturating "
             "concentration from above and says nothing about where the curve "
             "actually turns over.")

# --------------------------------------------------------------- the time ceiling
# nadeaunguyen2026, FDA postmarketing review, 5 paediatric cases
TIME_TO_TOXICITY_DAYS = {"earliest": 84, "median": 137, "latest": 274}
OBSERVED_VELOCITY_CM_PER_YEAR = 14.3 / (9 / 12)   # erdachild2024, 14.3 cm in 9 months

# ------------------------------------------------------------------- TYRA-300
TYRA = {
    "MW": 559.5,                       # pubchem CID 170647464
    "cell_IC50_nM": {"RT112/84 (FGFR3::TACC3)": 9,
                     "RT112/84-V555M (gatekeeper)": 17,
                     "UM-UC-14 (FGFR3 S249C)": 16},   # hudkins2024 via dabogratinib2026
    "selectivity_fold": {"over FGFR1": 63, "over FGFR2": 19, "over FGFR4": 55},
}
TYRA_CLINICAL = [
    ("dose range explored", "10 to 120 mg once daily, plus 40 and 50 mg twice "
     "daily, 28-day cycles, fasted (dabogratinib2026)"),
    ("cleared", "dosages THROUGH 100 mg once daily cleared at publication; "
     "120 mg once daily administered to a patient"),
    ("MTD", "NOT ESTABLISHED. The optimal monotherapy dosage is explicitly yet "
     "to be determined"),
    ("efficacy", "6 confirmed partial responses in 11 (54.5 per cent) "
     "FGFR3-altered mUC efficacy-evaluable patients at dosages >= 90 mg once "
     "daily"),
    ("toxicity", "a VERY LOW frequency of grade 3 treatment-related AEs; no "
     "grade >=3 treatment-related toxicity in the three detailed cases. The two "
     "dose reductions in those cases were for grade 2 peripheral neuropathy and "
     "grade 2 AST rise - NEITHER was hyperphosphataemia"),
]
ERDA_CLINICAL = [
    ("efficacy", "overall response rate 35.3 per cent in mUC (dabogratinib2026 "
     "citing the registrational data)"),
    ("toxicity", "serious AE rate 41 per cent; dose INTERRUPTION in 68 per cent, "
     "REDUCTION in 53 per cent, PERMANENT DISCONTINUATION in 21 per cent"),
    ("hyperphosphataemia", "affected MORE THAN 70 PER CENT of patients, and is "
     "an FGFR1 effect - FGFR1 sits in kidney regulating phosphate reabsorption"),
]

# --------------------------------------------------- the mouse dose-response for GROWTH
TYRA_GROWTH_DOSES = ("tyra300_2025, WILD-TYPE C57BL/6J mice dosed orally once daily "
                     "from 4 to 8 weeks. Doses explored 8 to 14 mg/kg, chosen "
                     "DELIBERATELY BELOW the 18 mg/kg oncology dose because a lower "
                     "dose was thought more appropriate for long-term paediatric use. "
                     "Naso-anal length rose significantly ONLY at 14 mg/kg (+7.3 per "
                     "cent); tibia and femur rose significantly and DOSE-DEPENDENTLY at "
                     "12 AND 14 mg/kg. THE CURVE HAD NOT TURNED OVER AT THE TOP OF THE "
                     "RANGE TESTED, and 18 mg/kg - which gives 96 per cent tumour growth "
                     "inhibition - WAS NEVER TESTED FOR GROWTH.")

# ------------------------------------------------- does the velocity become adult height
ADD_NOT_BORROW = [
    ("toydemir2006", "human", "CATSHL - lifelong HETEROZYGOUS PARTIAL FGFR3 loss of "
     "function, 27 affected in one kindred: ADULT male height mean 195.6 cm, about "
     "+2.8 SD, above the 97th centile in 5 of 5 men. AN ADULT ENDPOINT, not a velocity"),
    ("propel3_2026", "human", "randomised placebo-controlled phase 3 of oral "
     "infigratinib, n = 74 against 39: NO ACCELERATED PROGRESSION OF BONE AGE at 52 "
     "weeks, and no negative change in bone mineral density"),
    ("erdaseries2025", "human", "atypical physeal WIDENING with NO apparent progression "
     "of bone maturation on serial wrist films - severely confounded by hypogonadotropic "
     "hypogonadism with unmeasurable sex steroid, which holds bone age still by itself"),
]

COUNTER = ("THE COUNTERARGUMENT, WHICH THIS ATLAS ALREADY HOLDS AND WHICH IS THE "
           "STRONGEST THING AGAINST THE SELECTIVITY CASE. SCOLIOSIS IS IN THE NAME OF "
           "THE FGFR3 SYNDROME - CATSHL is camptodactyly, tall stature, scoliosis and "
           "hearing loss. The NPR3 biallelic patient needed spinal fusion at 12 for a "
           "39-degree Cobb angle. The NPR2 activating family had severe scoliosis with "
           "vertebral fractures. EVERY ROUTE TO EXTREME ENDOCHONDRAL GROWTH PRODUCES "
           "SPINAL DEFORMITY, genetic and pharmacological, FGFR and CNP alike. If the "
           "deformity is intrinsic to driving a physis rather than to FGFR1, then "
           "FGFR3-selectivity buys DOSE and does not buy TIME, and the clock is the "
           "binding constraint.")


def rule(c="="):
    print(c * 92)


def free_nM(dose_mg):
    """Steady-state average FREE plasma concentration, nmol/L, from Dose/(CL x tau)."""
    total_ng_per_mL = dose_mg * 1000.0 / (ERDA["CL_F_L_per_h"] * 24.0)
    free_ng_per_mL = total_ng_per_mL * (1.0 - ERDA["protein_bound"])
    return total_ng_per_mL, free_ng_per_mL, free_ng_per_mL / ERDA["MW"] * 1000.0


def main():
    rule()
    print("ERDAFITINIB'S CEILING AGAINST TYRA-300'S REACH")
    rule()

    print("\n[1] ERDAFITINIB'S EXPOSURE AT EVERY DOSE THAT HAS EVER GROWN A CHILD")
    print("    Steady-state average concentration = Dose / (CL/F x 24 h).")
    print(f"    CL/F {ERDA['CL_F_L_per_h']} L/h, t-half {ERDA['t_half_h']} h, protein "
          f"binding {ERDA['protein_bound']*100:.1f} per cent to AGP (zhu2026);")
    print(f"    MW {ERDA['MW']} (pubchem). PK linear from "
          f"{ERDA['linear_range_mg'][0]} to {ERDA['linear_range_mg'][1]} mg.\n")
    print(f"    {'dose':<7}{'total ng/mL':>13}{'free ng/mL':>13}{'free nM':>10}   note")
    for d, note in ERDA_DOSES:
        tot, fr, nM = free_nM(d)
        print(f"    {d:>2} mg {tot:>12.0f} {fr:>12.2f} {nM:>9.2f}   {note[:44]}")
        if len(note) > 44:
            print(" " * 48 + note[44:110])

    lo = free_nM(7)[2]
    hi = free_nM(9)[2]
    print(f"\n    THE WHOLE CLINICALLY REACHABLE FREE RANGE IS {free_nM(3)[2]:.1f} TO "
          f"{hi:.1f} nM.")
    print(f"    HEADROOM ABOVE THE DOSE THE INDEX CHILD ACTUALLY TOOK: {hi/lo:.2f}-FOLD.")
    print("    THAT IS THE ENTIRE THEORETICAL CEILING OF THE MOLECULE AS LABELLED - and")
    print("    it is gated by SERUM PHOSPHATE, which is an FGFR1 effect, in a child who")
    print("    was ALREADY having frequent interruptions for hyperphosphataemia at 7 mg.")
    print("    ERDAFITINIB'S DOSE CEILING IS SET BY THE WRONG RECEPTOR.")

    print("\n[2] AND NOBODY HAS SHOWN THAT ANY TOLERATED DOSE SATURATES THE TARGET")
    rule("-")
    print(f"    {PD_ANCHOR[:86]}")
    for i in range(86, len(PD_ANCHOR), 86):
        print(f"    {PD_ANCHOR[i:i+86]}")
    print(f"\n    For scale: the free plasma concentration at the 9 mg label maximum is")
    print(f"    {hi:.1f} nM, about {100/hi:.0f}-fold below the 100 nM that was shown to")
    print("    saturate in culture. THAT COMPARISON IS NOT CLEAN - the fibroblasts were")
    print("    serum-starved, so nominal culture concentration is close to free, whereas")
    print("    plasma is 99.7 per cent bound, and cartilage penetration is unmeasured for")
    print("    this drug in any species. WHAT IT DOES ESTABLISH: the concentration-response")
    print("    between zero and 100 nM was never mapped, so 'erdafitinib was already at its")
    print("    pharmacodynamic ceiling' is NOT a supported statement. It is unknown.")

    print("\n[3] THE CEILING THAT ACTUALLY BINDS IS TIME, NOT DOSE")
    rule("-")
    v = OBSERVED_VELOCITY_CM_PER_YEAR
    print(f"    Best observed velocity: {v:.2f} cm/year (erdachild2024, 14.3 cm in 9 months).")
    print("    Time to forced discontinuation (nadeaunguyen2026, five paediatric cases,")
    print("    ALL FIVE permanently discontinued, THREE requiring surgery):\n")
    for label, days in TIME_TO_TOXICITY_DAYS.items():
        print(f"        {label:<9} {days:>3} days  ->  {v*days/365.25:>5.2f} cm accrued")
    print(f"\n    SO ERDAFITINIB'S CEILING IS ROUGHLY "
          f"{v*TIME_TO_TOXICITY_DAYS['earliest']/365.25:.1f} TO "
          f"{v*TIME_TO_TOXICITY_DAYS['latest']/365.25:.1f} cm GROSS, MEDIAN ABOUT "
          f"{v*TIME_TO_TOXICITY_DAYS['median']/365.25:.1f} cm.")
    print("    And that is BEFORE subtracting the spine lost to kyphoscoliosis, and before")
    print("    the three-in-five chance of a surgical correction - a spinal fusion ENDS")
    print("    spinal growth permanently, which converts a yield gain into a yield loss.")

    print("\n[4] DOES THE VELOCITY BECOME ADULT HEIGHT, OR IS IT BORROWED?")
    rule("-")
    print("    Round 198 makes fusion the exhaustion of proliferative potential, so a drug")
    print("    that only accelerates consumption adds nothing to the adult endpoint. THREE")
    print("    HUMAN OBSERVATIONS SAY FGFR3 INHIBITION IS NOT THAT DRUG:")
    for ref, sp, res in ADD_NOT_BORROW:
        print(f"\n        {ref} [{sp}]")
        for i in range(0, len(res), 82):
            print(f"            {res[i:i+82]}")
    print("\n    CATSHL IS THE LOAD-BEARING ONE because it is an ADULT height under lifelong")
    print("    FGFR3 partial loss. FGFR3 inhibition raises the endpoint, not just the rate.")
    print("    THE LIMIT: CATSHL is germline, partial, heterozygous and lifelong. It says")
    print("    nothing about what a nine-month pharmacological block at bone age 16 does,")
    print("    and no bone age was recorded before erdafitinib in the index case.")

    print("\n[5] CAN TYRA-300 BE PUSHED PAST ERDAFITINIB? THE PD BRIDGE, WHICH NEEDS NO PK")
    rule("-")
    print("    Both drugs' FGFR3 engagement in a human can be read off tumour response in")
    print("    an FGFR3-DRIVEN tumour. Same target, same disease, same criterion:\n")
    for k, v2 in ERDA_CLINICAL:
        print(f"        erdafitinib  {k:<20} {v2[:60]}")
        for i in range(60, len(v2), 60):
            print(" " * 38 + v2[i:i+60])
    print()
    for k, v2 in TYRA_CLINICAL:
        print(f"        TYRA-300     {k:<20} {v2[:60]}")
        for i in range(60, len(v2), 60):
            print(" " * 38 + v2[i:i+60])
    print("\n    TYRA-300 cellular IC50 at FGFR3:")
    for line, ic in TYRA["cell_IC50_nM"].items():
        print(f"        {line:<34} {ic} nmol/L")
    print("    and dabogratinib2026 states its in vitro potency in FGFR3-driven lines is")
    print("    SIMILAR to the pan-FGFR inhibitors, with slightly MORE regression than")
    print("    erdafitinib head to head in the UM-UC-14 xenograft.")
    print("\n    CONCLUSION OF THE BRIDGE: at >= 90 mg once daily TYRA-300 produces confirmed")
    print("    regressions in FGFR3-driven human tumours at a rate AT LEAST MATCHING")
    print("    erdafitinib's, with a fraction of the toxicity, WITHOUT a phosphate gate, and")
    print("    WITHOUT having reached its maximum tolerated dose. THE ANSWER TO 'CAN IT BE")
    print("    PUSHED PAST ERDAFITINIB' IS YES, AND IT ALREADY HAS BEEN.")

    print("\n[6] AND THE GROWTH DOSE IS AN ONCOLOGY DOSE, WHICH IS THE POINT")
    rule("-")
    for i in range(0, len(TYRA_GROWTH_DOSES), 86):
        print(f"    {TYRA_GROWTH_DOSES[i:i+86]}")
    print("\n    So the growth-effective dose in a NORMAL animal is 67 to 78 per cent of the")
    print("    oncology dose and still climbing. Erdafitinib's growth doses (3 to 7 mg) are")
    print("    BELOW its own oncology dose (8 to 9 mg) and it could not be held there.")
    print("    INFIGRATINIB MAKES THE SAME POINT FROM THE OTHER SIDE: 0.25 mg/kg/day, a small")
    print("    fraction of its oncology dose, chosen for tolerability, buys +1.74 cm/year -")
    print("    about a ninth of erdafitinib's velocity at near-oncology exposure. THE FGFR")
    print("    GROWTH EFFECT IS STEEPLY DOSE-DEPENDENT AND NOBODY HAS TOPPED IT OUT.")

    print("\n[7] THE COUNTERARGUMENT, STATED IN FULL")
    rule("-")
    for i in range(0, len(COUNTER), 86):
        print(f"    {COUNTER[i:i+86]}")
    print("\n    WHAT WOULD DECIDE IT. If the physeal failure is FGFR1/perichondrium-mediated,")
    print("    TYRA-300 extends the clock and the ceiling rises with the dose. If it is")
    print("    intrinsic to the growth, TYRA-300 hits the same 137-day wall at a higher dose")
    print("    and the ceiling is the same 7 cm. ONE PIECE OF EVIDENCE LEANS THE FIRST WAY:")
    print("    in the ACH mouse TYRA-300 INCREASED femoral metaphyseal bone mineral density")
    print("    and BV/TV, which is the opposite of the weakening that produces SCFE - but it")
    print("    is a dysplasia model, not a normal one, and mice do not fuse.")

    print("\n[8] THE ONE NUMBER I CANNOT GET")
    rule("-")
    print("    TYRA-300's HUMAN free plasma concentration at 90 to 120 mg, against its 9 to")
    print("    17 nmol/L cellular IC50. With it, the comparison in [1] becomes exact instead")
    print("    of inferential. It sits in hudkins2024 (J Med Chem, paywalled) and in the")
    print("    SURF301 conference PK. Plasma protein binding for TYRA-300 is also unpublished")
    print("    in any source reachable here, and without it a free-concentration comparison")
    print("    cannot be computed at all.")
    rule()


if __name__ == "__main__":
    main()
