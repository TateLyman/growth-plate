#!/usr/bin/env python3
"""
ERDAFITINIB FULLY MAPPED AGAINST THE ACCELERATING DOSE-RESPONSE CURVE, AND
AGAINST DABOGRATINIB AT THE DOSES EACH CAN ACTUALLY BE GIVEN.

WHY THIS TOOL EXISTS
--------------------
The user asked whether erdafitinib can be made to work maximally against the
non-diminishing curve round 215 established, and whether its problems are
fixable with anything niche. Cost is the reason - dabogratinib is investigational
and expensive, erdafitinib is a marketed tablet.

THE ANSWER TURNS ON A NUMBER THIS ATLAS HAD WRONG TWICE. Rounds 213 and 215
expressed target coverage as multiples of FGFR3 cellular IC50 using the panel on
a TYRA conference slide. Both developers' own primary papers are now in hand and
they agree with EACH OTHER and disagree with that slide by roughly eightfold.
Recomputing on the developers' numbers does not change which drug is ahead - it
changes BY HOW MUCH, and it changes the absolute framing completely.
"""

# ---------------------------------------------------------- three IC50 datasets
BAF3_FGFR3 = {
    "perera2017 (Janssen, erdafitinib developers)": {
        "erdafitinib": 13.2, "note": "Ba/F3 proliferation, 4 days. Enzyme IC50 FGFR1-4 "
        "= 1.2, 2.5, 3.0, 5.7 nM; KINOMEscan Kd FGFR1 0.24, FGFR3 1.1, FGFR4 1.4, "
        "FGFR2 2.2 nM; VEGFR2 cellular 1160 nM and IL-3 rescue >7000 nM"},
    "hudkins2024 SI (TYRA, dabogratinib developers)": {
        "dabogratinib": 11.0, "note": "compound 22 in the primary SAR table; FGFR1 278, "
        "FGFR2 157, FGFR4 405 nM, so folds of 25, 14 and 37"},
    "surf301_ena2024 slide (TYRA marketing panel)": {
        "erdafitinib": 1.35, "dabogratinib": 1.75,
        "note": "read off a linear axis, cross-checked against the printed folds "
        "63/19/55 for dabogratinib and 4.2/1.4/14 for erdafitinib"},
}

# ------------------------------------------------------------------------ PK
ERDA = {"CL_F": 0.362, "fu": 0.003, "MW": 446.5}          # zhu2026
TYRA_AUC24 = {40: 2270, 60: 4360, 90: 10300, 120: 23578}  # surf301_ena2024
TYRA_FU = 0.0099                                          # derived round 214
TYRA_MW = 559.5

# what dose each drug can ACTUALLY be given at, and what stops it going higher
ATTAINABLE = [
    ("erdafitinib 3 mg", 3, "erda", "erdaseries2025 patient 1 after reduction - still grew ~10 cm/yr"),
    ("erdafitinib 7 mg", 7, "erda", "erdachild2024 - the 19.06 cm/yr case, with interruptions"),
    ("erdafitinib 8 mg", 8, "erda", "BALVERSA label starting dose"),
    ("erdafitinib 9 mg", 9, "erda", "BALVERSA LABEL MAXIMUM - hard ceiling as marketed"),
    ("dabogratinib 45 mg", 45, "tyra", "BEACH301 TOP PAEDIATRIC DOSE, 0.625 mg/kg = half oncology"),
    ("dabogratinib 60 mg", 60, "tyra", "HEPATICALLY CLEAN - ALT 1/22 G1-2, AST 0/22"),
    ("dabogratinib 90 mg", 90, "tyra", "liver signal appears - ALT 7/15 with 2 G3, AST 7/15 with 1 G3"),
    ("dabogratinib 120 mg", 120, "tyra", "AST grade 3 in 2 of 4; MTD still not declared"),
]

# ------------------------------------------- what actually gates erdafitinib
# surf301_ena2024 slides 4-5, from the BALVERSA label, BLC3001, n=135
ERDA_GATE = [
    ("Nail disorders", "FGFR2", 69, 12, 22, 27,
     "months-long nail turnover; the slowest to recover and the biggest single "
     "driver of both interruption and reduction"),
    ("Stomatitis", "FGFR2", 56, 10, 19, 19,
     "oral mucosa turns over in 1-2 weeks, so it recovers fast on a break"),
    ("Eye disorders", "FGFR2", 25, 2, 16, 17,
     "ohagan2026 across 5 studies plus RAGNAR: retinopathy 21.5 and 13.7 per cent, "
     "GRADE 3 ONLY 2.3 AND 1.0 PER CENT, NO GRADE 4, discontinuation 2.9 and 1.0 "
     "per cent, and 63-65 per cent RESOLVED by data cutoff. 78.6 per cent occurred "
     "within 90 days"),
    ("PPE (hand-foot)", "FGFR2", 30, 10, 15, 12, "skin, recovers over weeks"),
    ("Hyperphosphataemia", "FGFR1", 75, 4, 7, 4.4,
     "HIGHEST incidence, LOWEST dose cost. Managed by diet 600-800 mg/day, sevelamer "
     "800-1600 mg three times daily, and acetazolamide 250 mg 2-3 times daily above "
     "9 mg/dL - all codified in surf301_protocol_v4"),
    ("Diarrhoea", "other", 62, 2, 10, 7, "loperamide, standard"),
]

# ----------------------------------------------- the niche levers, ranked
LEVERS = [
    ("A. INTERMITTENT DOSING, AND THE CLASS ALREADY HAS AN APPROVED PRECEDENT",
     "STRONGEST, AND IT IS NOT A HYPOTHESIS. patel2023 - pemigatinib's FDA-approved "
     "dosage is 13.5 mg once daily for 14 CONSECUTIVE DAYS FOLLOWED BY 7 DAYS OFF, "
     "and it delivers ORR 36 per cent against erdafitinib's 35.3 on CONTINUOUS "
     "dosing. Same class, same target family, equivalent efficacy, and the schedule "
     "exists precisely because of these toxicities. ERDAFITINIB IS THE MEMBER BEST "
     "SUITED TO IT AND IS THE ONE DOSED CONTINUOUSLY - 59-hour plasma half-life PLUS "
     "the lysosomal depot that perera2017 showed holds complete pFGFR suppression "
     "for 4 hours and only returns to basal at 24 hours after a ONE-HOUR exposure, "
     "against 2 hours for a non-lysosomotropic analogue at ten times the "
     "concentration. THE EPITHELIUM GETS A HOLIDAY THE GROWTH PLATE LARGELY DOES "
     "NOT. What this cannot fix is nail toxicity, whose turnover is months.",
     "free - it is a schedule"),
    ("B. TREAT THE FGFR2 GATE INSTEAD OF DOSE-REDUCING FOR IT",
     "The gate is four epithelial toxicities and the largest, nail disorders, drives "
     "27 per cent of reductions. IN AN ONCOLOGY TRIAL YOU REDUCE FOR GRADE 2 NAIL "
     "TOXICITY BECAUSE THE PATIENT HAS ALTERNATIVES. In a growth indication the "
     "benefit-risk is not the same object, and the eye data says the scariest of the "
     "four is largely reversible - grade 3 in 2.3 per cent, discontinuation in 2.9, "
     "and roughly two thirds resolved. THE HONEST LIMIT - this is a reframing of "
     "acceptable toxicity, not a pharmacological fix, and it is the user's call not "
     "this atlas's.",
     "free, but it is a judgement not a intervention"),
    ("C. PHOSPHATE IS ALREADY SOLVED AND WAS NEVER THE MAIN GATE",
     "75 per cent incidence, 4 per cent grade 3, 7 per cent of interruptions. "
     "surf301_protocol_v4 codifies the management - dietary restriction to 600-800 "
     "mg/day, sevelamer 800-1600 mg three times daily with food, and acetazolamide "
     "250 mg two or three times daily above 9 mg/dL. THE INDEX CHILD'S INTERRUPTIONS "
     "WERE FOR HYPERPHOSPHATAEMIA, so in that one case this lever alone might have "
     "kept him on drug.",
     "cheap and codified"),
    ("D. THE SPINE IS THE REAL YIELD KILLER AND THE FIX IS MECHANICAL, NOT CHEMICAL",
     "nadeaunguyen2026 - five of five discontinued, THREE required surgery. A "
     "kyphoscoliotic spine is shorter and a spinal fusion ENDS spinal growth, which "
     "converts a yield gain into a permanent yield loss. NOTHING PHARMACOLOGICAL "
     "ADDRESSES THIS. What exists is orthopaedic - serial spine imaging with Cobb "
     "angle, bracing at the threshold rather than after deformity, and the question "
     "of prophylactic in-situ pinning for the slipped capital femoral epiphysis that "
     "forced surgery. THIS ATLAS HAS NO EVIDENCE THAT ANY OF IT WORKS UNDER AN FGFR "
     "INHIBITOR - it is standard paediatric orthopaedics applied to a situation "
     "nobody has studied.",
     "unstudied in this setting"),
    ("E. PHARMACOKINETIC BOOSTING - REAL, BUT IT DOES NOT BEAT THE GATE",
     "Erdafitinib is cleared 39 per cent by CYP2C9 and 20 per cent by CYP3A4 "
     "(zhu2026), so an inhibitor of either raises exposure at the same milligram "
     "dose, and CYP2C9 poor metabolisers run higher exposure natively. THAT LOWERS "
     "COST PER UNIT EXPOSURE, WHICH IS THE USER'S CONSTRAINT. IT DOES NOT RAISE THE "
     "CEILING, because it scales FGFR3 and FGFR2 exposure together - it is "
     "arithmetically identical to raising the dose, which the label already permits "
     "up to 9 mg.",
     "cheap, and solves cost rather than ceiling"),
    ("F. THE LYSOSOME ALKALINISER, AND WHY IT IS WORSE UNDER A PULSED SCHEDULE",
     "englinger2018 gave 5.1-fold better phospho-ERK suppression with chloroquine at "
     "the same drug concentration, and qiu2026 shows hydroxychloroquine is "
     "hepatoprotective against a lysosomotropic TKI. BUT ROUND 214's STEADY-STATE "
     "ARGUMENT SAYS THE POTENTIATION SHOULD SHRINK ON CONTINUOUS DOSING, AND IT IS "
     "ACTIVELY COUNTERPRODUCTIVE UNDER LEVER A - the whole point of pulsing "
     "erdafitinib is that the depot carries target suppression through the off "
     "period, and an alkaliniser empties the depot. THE TWO BEST IDEAS IN THIS FILE "
     "ARE MUTUALLY EXCLUSIVE, and the schedule one is far better evidenced.",
     "drop it if pulsing"),
]


def rule(c="="):
    print(c * 92)


def erda_free_nM(mg):
    tot = mg * 1000.0 / (ERDA["CL_F"] * 24.0)
    return tot / ERDA["MW"] * 1000.0 * ERDA["fu"]


def tyra_free_nM(mg):
    auc = TYRA_AUC24.get(mg)
    if auc is None:                       # interpolate on the observed superlinearity
        lo, hi = 40, 60
        auc = TYRA_AUC24[lo] + (TYRA_AUC24[hi] - TYRA_AUC24[lo]) * (mg - lo) / (hi - lo) \
            if mg < 60 else TYRA_AUC24[60]
    return (auc / 24.0) / TYRA_MW * 1000.0 * TYRA_FU


def main():
    rule()
    print("ERDAFITINIB AGAINST DABOGRATINIB AGAINST THE CURVE, AT ATTAINABLE DOSES")
    rule()

    print("\n[1] THE NUMBER THIS ATLAS HAD WRONG TWICE")
    rule("-")
    for src, d in BAF3_FGFR3.items():
        print(f"\n    {src}")
        for k, v in d.items():
            if k == "note":
                for i in range(0, len(v), 82):
                    print(f"        {v[i:i+82]}")
            else:
                print(f"        {k:<14} Ba/F3 FGFR3 IC50 = {v} nmol/L")
    print("\n    THE TWO DEVELOPERS' OWN PRIMARY PAPERS AGREE WITH EACH OTHER - 13.2 nmol/L")
    print("    for erdafitinib and 11 for dabogratinib, within 1.2-fold - AND BOTH DISAGREE")
    print("    WITH THE MARKETING PANEL BY ROUGHLY EIGHTFOLD. Rounds 213 and 215 expressed")
    print("    everything as multiples of the marketing panel's IC50, which inflated every")
    print("    absolute coverage figure by about eight. THE RATIO SURVIVED because both")
    print("    drugs were taken from the same slide. THE ABSOLUTE FRAMING DID NOT. CORR-211.")
    print("\n    AND THE CORRECTED READING IS MORE USEFUL, BECAUSE ON THE DEVELOPERS' OWN")
    print("    NUMBERS THE TWO MOLECULES ARE ESSENTIALLY EQUIPOTENT AT FGFR3. Everything")
    print("    then reduces to FREE CONCENTRATION, which is a pure PK question.")

    print("\n[2] COVERAGE AT THE DOSES EACH DRUG CAN ACTUALLY BE GIVEN")
    rule("-")
    print(f"    erdafitinib fu {ERDA['fu']*100:.1f} per cent against IC50 13.2 nmol/L;")
    print(f"    dabogratinib fu {TYRA_FU*100:.1f} per cent (derived) against IC50 11 nmol/L\n")
    print(f"    {'regimen':<24}{'free nM':>10}{'x IC50':>9}   what stops it going higher")
    print("    " + "-" * 88)
    rows = {}
    for label, mg, which, note in ATTAINABLE:
        if which == "erda":
            f = erda_free_nM(mg); x = f / 13.2
        else:
            f = tyra_free_nM(mg); x = f / 11.0
        rows[label] = x
        print(f"    {label:<24}{f:>10.2f}{x:>9.3f}   {note[:44]}")
        if len(note) > 44:
            print(" " * 47 + note[44:110])

    e9 = rows["erdafitinib 9 mg"]; e7 = rows["erdafitinib 7 mg"]
    t45 = rows["dabogratinib 45 mg"]; t60 = rows["dabogratinib 60 mg"]
    t90 = rows["dabogratinib 90 mg"]; t120 = rows["dabogratinib 120 mg"]
    print("\n    THE COMPARISON THE USER ASKED FOR, AND IT FAVOURS ERDAFITINIB:")
    print(f"      erdafitinib at its LABEL MAXIMUM          {e9:.3f}x IC50")
    print(f"      dabogratinib at the TOP PAEDIATRIC DOSE   {t45:.3f}x  -> "
          f"{e9/t45:.2f}x LESS than erdafitinib")
    print(f"      dabogratinib at the HEPATICALLY CLEAN 60  {t60:.3f}x  -> "
          f"{e9/t60:.2f}x LESS than erdafitinib")
    print(f"      dabogratinib at 90 mg, liver signal on    {t90:.3f}x  -> only "
          f"{t90/e9:.2f}x MORE than erdafitinib")
    print(f"      dabogratinib at 120 mg, AST G3 2 of 4     {t120:.3f}x  -> "
          f"{t120/e9:.2f}x more")
    print("\n    ERDAFITINIB AT 9 mg BEATS DABOGRATINIB AT EVERY DOSE THE PAEDIATRIC")
    print("    PROGRAMME WILL USE, AND BEATS ITS HEPATICALLY CLEAN DOSE BY ABOUT TWOFOLD.")
    print("    Dabogratinib only overtakes it by accepting the liver signal, and even at")
    print("    90 mg the margin is about a third. THAT IS THE OPPOSITE OF WHAT THE")
    print("    SELECTIVITY STORY IMPLIES, AND IT IS CONSISTENT WITH THE CLINICAL RECORD -")
    print("    erdafitinib is the only FGFR inhibitor that has ever produced 19 cm/year in")
    print("    a child, and no selective agent has produced anything like it.")

    print("\n[3] BUT NOTICE WHERE EVERYONE SITS ON THE CURVE")
    rule("-")
    print("    ON THE DEVELOPERS' OWN CELLULAR IC50, NOBODY REACHES 1x FREE COVERAGE except")
    print("    dabogratinib at 120 mg. Erdafitinib produced 19.06 cm/year at 0.41x and about")
    print("    10 cm/year at 0.18x. SO THE WHOLE HUMAN GROWTH RECORD SITS ON THE BOTTOM")
    print("    SHOULDER OF THE CONCENTRATION-RESPONSE, WHICH IS EXACTLY WHERE ROUND 215's")
    print("    MOUSE RE-ANALYSIS SAID THE CURVE IS STEEPEST. Two independent lines agreeing")
    print("    that the top has never been approached.")
    print("\n    THE CAVEAT THAT MATTERS. A 4-day Ba/F3 PROLIFERATION IC50 is a harsher")
    print("    endpoint than pathway inhibition. perera2017's own washout work suppressed")
    print("    phospho-FGFR completely at 30 nmol/L NOMINAL for one hour, and erdachild2024's")
    print("    fibroblasts saturated phospho-ERK and phospho-AKT at 100 nmol/L nominal with")
    print("    nothing tested below. So the concentration needed to INHIBIT THE PATHWAY may")
    print("    be well under the concentration needed to STOP A CELL DIVIDING, and 0.41x of")
    print("    a proliferation IC50 is not the same as 0.41x of a pathway EC50.")

    print("\n[4] WHAT ACTUALLY GATES ERDAFITINIB, AND WHETHER EACH PIECE IS FIXABLE")
    rule("-")
    print(f"    {'toxicity':<22}{'axis':>7}{'any%':>6}{'G3%':>5}{'intr%':>7}{'red%':>6}")
    print("    " + "-" * 60)
    for name, axis, any_g, g3, intr, red in [(a, b, c, d, e, f) for a, b, c, d, e, f, _ in ERDA_GATE]:
        print(f"    {name:<22}{axis:>7}{any_g:>6}{g3:>5}{intr:>7}{red:>6}")
    print()
    for name, axis, _, _, _, _, comment in ERDA_GATE:
        if comment:
            print(f"\n    {name}")
            for i in range(0, len(comment), 84):
                print(f"        {comment[i:i+84]}")

    print("\n[5] THE NICHE LEVERS, RANKED BY EVIDENCE")
    rule("-")
    for title, body, cost in LEVERS:
        print(f"\n    {title}")
        for i in range(0, len(body), 84):
            print(f"        {body[i:i+84]}")
        print(f"        [{cost}]")

    print("\n[6] THE VERDICT")
    rule("-")
    print("    ERDAFITINIB IS CURRENTLY AHEAD ON ATTAINABLE TARGET COVERAGE AND IT IS THE")
    print("    CHEAPER MOLECULE. It is not ahead because it is better - the two are")
    print("    equipotent at FGFR3 - but because its 9 mg label maximum happens to deliver")
    print("    more free drug than dabogratinib's tolerated dose does, and because")
    print("    dabogratinib's paediatric programme has chosen a dose band a quarter of that.")
    print("\n    THE ONE THING THAT IS GENUINELY FIXABLE AND HAS NOT BEEN TRIED IS THE")
    print("    SCHEDULE. Pemigatinib is approved 14 days on, 7 days off, at equivalent")
    print("    response rate to continuous erdafitinib. Erdafitinib has a 59-hour half-life")
    print("    and a lysosomal depot that holds target suppression twelve times longer than")
    print("    a matched non-lysosomotropic analogue. It is the class member best suited to")
    print("    intermittent dosing and the only one given continuously.")
    print("\n    THE ONE THING THAT IS NOT FIXABLE PHARMACOLOGICALLY IS THE SPINE, AND IT IS")
    print("    THE TERM THAT DECIDES ADULT HEIGHT. Five of five discontinued at a median of")
    print("    137 days and three needed surgery. Until someone shows that bracing and")
    print("    surveillance hold the curve under an FGFR inhibitor, erdafitinib's ceiling is")
    print("    still a clock, and the clock is what caps the integral no matter how good the")
    print("    coverage arithmetic looks.")
    rule()


if __name__ == "__main__":
    main()
