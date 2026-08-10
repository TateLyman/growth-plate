#!/usr/bin/env python3
"""ROUND 221 - the three supplied documents, and what they do to rounds 219 and 220.

WHY THIS EXISTS
---------------
Round 220 concluded that the two approved CNP ligand drugs are "pharmacologically
interchangeable" and that "I looked for a pharmacological reason to prefer one and
did not find one." THAT REASONING WAS STRUCTURAL - I compared the two peptides'
N-terminal extensions and inferred equivalence. THE HEAD-TO-HEAD EXISTS, IT IS IN
THE RIGHT SPECIES, AND IT SEPARATES THEM. Logged as CORR-221.

Round 219 quantified the FGF19 compensatory rise as "1.5- to 3-fold" because the
poster figure was not available. IT NOW IS, RENDERED, AND THE MEDIANS ARE READ OFF
THE AXIS RATHER THAN ASSUMED.

THE READING DISCIPLINE FOR THE BOX PLOTS
----------------------------------------
Medians below are read from a 200-dpi render of the poster figure against its own
printed axis. They are good to about +/- 0.15 log2 units and are NOT sponsor-stated
numbers. Every derived fold change carries that. This is stated because round 213
nearly put a misread figure value into the atlas, and the rule from that near-miss
is that reading a figure means rendering it AND saying how precisely you read it.
"""
import math

W = 92
def rule(c="="): print(c * W)
def head(n, t):
    print(); rule(); print(f"[{n}] {t}"); rule("-")
def wrap(s, ind=4):
    out, line = [], ""
    for w in s.split():
        if len(line) + len(w) + 1 > W - ind:
            out.append(" " * ind + line); line = w
        else:
            line = (line + " " + w).strip()
    if line: out.append(" " * ind + line)
    return "\n".join(out)

# ----------------------------------------------------------------------------- 1
head(1, "THE PRIMATE HEAD-TO-HEAD THAT ROUND 220 SAID DID NOT EXIST")
print(wrap(
    "breinholt2019, 26-week juvenile cynomolgus monkey, n = 4 per group. TransCon CNP at 100 ug "
    "CNP/kg/WEEK against a daily CNP-39 molecule - stated by the authors to have the SAME AMINO "
    "ACID SEQUENCE AS VOSORITIDE - at 20 ug CNP/kg/DAY, against vehicle."))
print()
print("      endpoint                        TransCon CNP    daily CNP-39     separation")
rows = [("body length", "+5%", "+3%", "1.7x"),
        ("TAIL length", "+9%", "+3%", "3.0x"),
        ("tibia length", "+6%", "+3%", "2.0x"),
        ("ulna length", "+3%", "no change", "-"),
        ("proliferative zone width", "+37% *", "+16% *", "2.3x"),
        ("hypertrophic zone width", "+38% *", "+39% *", "NONE"),
        ("epiphyseal plate thickness", "+16% *", "+7% (n.s.)", "significant vs not")]
for a, b, c, d in rows:
    print(f"      {a:<30s}  {b:<14s}  {c:<14s}  {d}")
print("      * significantly different from control, P <= 0.05")
print()
weekly_transcon, daily_cnp39 = 100.0, 20.0 * 7
print(wrap(
    f"AND THE DOSING MAKES IT WORSE FOR THE DAILY ARM, NOT BETTER. TransCon delivered "
    f"{weekly_transcon:.0f} ug CNP/kg/week; the daily arm delivered {daily_cnp39:.0f}. "
    f"THE WEEKLY PRODRUG WON ON {100*weekly_transcon/daily_cnp39:.0f} PER CENT OF THE WEEKLY "
    f"PEPTIDE DOSE."))
print()
print(wrap(
    "THE TAIL ROW IS THE ONE THIS CASE SHOULD READ FIRST. Tail is pure caudal vertebrae - a clean "
    "axial growth plate readout - and the separation there is THREEFOLD, the largest of any "
    "endpoint. CORR-195 forbids scoring an agent against one site, and this is the site profile "
    "difference between the two ligand drugs that nobody had put in front of the decision."))

# ----------------------------------------------------------------------------- 2
head(2, "AND THE MOUSE ARM IS THE CLEANEST SCHEDULE EXPERIMENT THAT CAN BE DONE")
print(wrap(
    "Same paper. Three-week-old male FVB mice, n = 9, CNP-38 at 203 ug/kg/day for five weeks, "
    "delivered either as a DAILY SUBCUTANEOUS BOLUS or as CONTINUOUS SUBCUTANEOUS INFUSION by "
    "osmotic Alzet pump. SAME MOLECULE. SAME DAILY DOSE. ONLY THE SCHEDULE DIFFERS. Daily bolus "
    "produced significant appendicular and axial growth; CONTINUOUS INFUSION PRODUCED "
    "SIGNIFICANTLY MORE, on several growth parameters, against the bolus arm directly."))
print()
print(wrap(
    "THAT IS THE EXPERIMENT ROUND 220's CEILING ARGUMENT PREDICTED WOULD COME OUT NULL. It did "
    "not. The atlas claim - graded D - was that vosoritide and navepegritide reach a comparable "
    "ceiling despite roughly 300-fold different exposure duration, so the ceiling must sit "
    "DOWNSTREAM of NPR2 and continuity buys nothing. A same-molecule same-dose bolus-versus-"
    "infusion comparison is the direct test of exactly that, and continuity wins."))

# ----------------------------------------------------------------------------- 3
head(3, "WHY THE CLINICAL DATA LOOKED LIKE A WASH - IT CANNOT SEE A DIFFERENCE THIS SIZE")
nav, lo, hi = 1.49, 1.05, 1.93
vos = 1.57
print(wrap(
    f"APPROACH gives navepegritide {nav} cm/year against placebo with a 95 per cent interval of "
    f"{lo} to {hi}. Vosoritide's randomised effect is about {vos}. Round 220 called that a wash "
    f"and concluded the drugs are interchangeable. THAT IS A NULL-IS-NOT-EQUIVALENCE ERROR."))
print()
print(f"      the APPROACH interval spans {hi/lo:.2f}-FOLD end to end")
print(f"      a true effect anywhere from {lo} to {hi} is compatible with the data")
print(f"      vosoritide's {vos} sits comfortably inside it, AND SO WOULD {hi:.2f}")
print()
print(wrap(
    "A cross-trial comparison of two point estimates, in different cohorts with different "
    "baselines, neither reporting adult height, cannot exclude the 1.7- to 3-fold separations "
    "the primate study measured. THE CORRECT STATEMENT IS THAT THE TRIALS DO NOT DISTINGUISH "
    "THEM, WHICH IS NOT THE SAME AS THE DRUGS BEING EQUIVALENT - and where the trials are silent "
    "the controlled preclinical comparison is the better evidence, not the worse."))

# ----------------------------------------------------------------------------- 4
head(4, "THE FGF19 AND KLB FOLD CHANGES, NOW READ OFF THE FIGURE RATHER THAN ASSUMED")
print(wrap(
    "surf301 poster (Loriot et al.), Olink on 60-120 mg QD participants, paired t-test, cut-off "
    "P < 0.01 and absolute fold change 1.5. Box plots of C1D15 log2 fold change by dose. MEDIANS "
    "BELOW ARE READ FROM A 200-dpi RENDER AGAINST THE PRINTED AXIS, good to about +/- 0.15 log2, "
    "and are not sponsor-stated values."))
print()
FGF19 = {"40 mg": 0.15, "60 mg": 0.95, "90 mg": 1.80, "120 mg": 1.40}
KLB = {"40 mg": -0.30, "60 mg": 0.45, "90 mg": 0.85, "120 mg": 0.85}
print("      dose      FGF19 log2FC   fold      KLB log2FC   fold     crosses 1.5x?")
for d in FGF19:
    f, k = FGF19[d], KLB[d]
    ff, kf = 2 ** f, 2 ** k
    flag = []
    if abs(f) > 0.585: flag.append("FGF19")
    if abs(k) > 0.585: flag.append("KLB")
    print(f"      {d:<9s} {f:+8.2f}     {ff:6.2f}x   {k:+8.2f}     {kf:5.2f}x    "
          f"{', '.join(flag) if flag else 'neither'}")
print()
print(wrap(
    "TWO THINGS THE 1.5-FOLD THRESHOLD LINE HID. FGF19 IS STRONGLY DOSE-DEPENDENT and peaks near "
    "3.5-fold at 90 mg, well above the 1.5- to 3-fold band round 219 assumed. AND KLB FALLS AT 40 "
    "mg - a median near 0.8-fold - before rising, so the co-receptor response is NOT monotonic "
    "from the lowest dose and the sponsor's single phrase 'FGF19 and KLB increased' flattens a "
    "biphasic curve."))

# ----------------------------------------------------------------------------- 5
head(5, "DOES THE MEASURED RISE CHANGE ROUND 219's CONCLUSION - NO, AND NOW IT IS MEASURED")
phys = 0.221   # ng/mL, upper median fasting serum FGF19 in healthy humans
paper = 200.0  # ng/mL, fgf19cart2025
peak = 2 ** max(FGF19.values())
print(f"      human median fasting FGF19          {phys*1000:8.0f} pg/mL")
print(f"      x the largest measured rise ({peak:.2f}x)  {phys*peak*1000:8.0f} pg/mL")
print(f"      concentration that shortened a bone {paper*1000:8.0f} pg/mL   (fgf19cart2025,")
print(f"                                                       WITH 200 ng/mL added beta-klotho)")
print(f"      REMAINING GAP                       {paper/(phys*peak):8.0f}-FOLD")
print()
print(wrap(
    "ROUND 219's ARITHMETIC SURVIVES WITH A SMALLER MARGIN AND A REAL NUMBER. The gap falls from "
    "the 300- to 600-fold estimated under the assumed rise to about 260-fold under the measured "
    "one. Still not close. The conclusion that the FGF19 loop is not worth adding an agent for "
    "stands, and it now stands on a measurement rather than on a range I picked."))

# ----------------------------------------------------------------------------- 6
head(6, "AND ONE HUMAN OBSERVATION THAT ARGUES AGAINST MY OWN SELF-LIMITING HYPOTHESIS")
COL9A1 = [0.25, 0.15, 0.90, 1.05]
print(wrap(
    "Round 219 floated, and graded E, that FGFR3 inhibition might be SELF-LIMITING - because "
    "cinque2015 found Fgfr3 RNAi blocks FGF18-induced autophagy in chondrocytes, and that "
    "autophagy is what type II collagen secretion needs. IF THAT WERE OPERATING, A CARTILAGE "
    "COLLAGEN SHOULD NOT RISE UNDER THE DRUG."))
print()
print("      COL9A1, C2D1 log2 fold change by ascending dose (read from the render):")
print("      " + "   ".join(f"{v:+.2f} ({2**v:.2f}x)" for v in COL9A1))
print()
print(wrap(
    "IT RISES, DOSE-DEPENDENTLY, CROSSING THE 1.5-FOLD LINE AT THE TOP TWO DOSES. That is the "
    "sponsor's own cartilage-relevant marker moving in the direction opposite to a collagen "
    "secretion deficit. THE DIRECTION IS NOT UNAMBIGUOUS - a plasma collagen fragment can rise "
    "from increased synthesis OR increased turnover and degradation - so this does not prove the "
    "arm is intact. It does mean the self-limiting hypothesis has a human observation against it "
    "and none for it, and it stays at E while moving down the list of things to worry about."))
print()
print(wrap(
    "AND THE AUTHORS' OWN COMMENTARY SHIFTS THE SAME QUESTION. cinque2016_editorial states that "
    "FGF18 acts 'mainly through FGFR4, and to a lesser extent through FGFR3' - so the FGFR3 "
    "contribution is real in their reading rather than an in-vitro artefact, which cuts the other "
    "way. It also points to wang2015_ach_autophagy, which reports DEFECTIVE autophagy in the "
    "growth plates of an ACHONDROPLASIA mouse - FGFR3 OVERACTIVITY SUPPRESSING AUTOPHAGY. If "
    "activation suppresses it, inhibition plausibly relieves it, which is the opposite sign to "
    "the self-limiting worry and is consistent with the COL9A1 rise. THREE OBSERVATIONS, TWO "
    "DIRECTIONS, NOT RESOLVED - recorded as a gap rather than decided."))

# ----------------------------------------------------------------------------- 7
head(7, "WHAT THE EDITORIAL DOES AND DOES NOT ANSWER ABOUT THE AUTOPHAGY CANDIDATE")
print(wrap(
    "ASK ONE WAS WHETHER Tat-beclin-1 LENGTHENS A WILD-TYPE FEMUR. The editorial does not report "
    "the extended data, but it describes the rescue three times and every description is "
    "RESTORATION language - 'restored ECM matrix defects in Fgf18+/- and Fgfr4-/- mice', "
    "'rescued autophagy in the growth plates of Fgf18+/- mice'. NO WILD-TYPE ELEVATION IS CLAIMED "
    "ANYWHERE by the authors in either the paper or their own summary of it."))
print()
print(wrap(
    "THAT IS NOT PROOF OF ABSENCE and it is not the extended-data panel. But authors summarising "
    "their own work generally state the strongest true version, and the strongest version they "
    "state is restoration. THE CANDIDATE STAYS UNRANKED and the prior moves against elevation."))
print()
print(wrap(
    "ASK FIVE - the sponsor's FGFR4 PD analysis - IS STILL OPEN. The poster says in terms: "
    "'Confirmation of FGFR3 dependence ongoing with FGFR4 PD analysis.' It has not reported."))

# ----------------------------------------------------------------------------- 8
head(8, "ONE NUMBER FROM THE POSTER THAT BEARS ON THE ERDAFITINIB COMPARISON")
print(wrap(
    "The poster states that in SURF301 'TYRA-300 had demonstrated exposures above the IC90 for "
    "FGFR3 inhibition that are below the IC50 for FGFR1/2/4.' Round 214 derived the Hill slope "
    "from this sponsor's own IC90/IC50 spacing of about 2.8, so an exposure above the FGFR3 IC90 "
    "is C/IC50 above about 2.8."))
x_erda, x_dabo = 0.469, 2.8
for n in (1.0, 2.13):
    ie = 100 * (1 - 1 / (1 + x_erda ** n))
    idb = 100 * (1 - 1 / (1 + x_dabo ** n))
    print(f"      at Hill n = {n:<5.2f}  erdafitinib 8 mg removes {ie:5.1f}% of FGFR3; "
          f"a dose at the FGFR3 IC90 removes {idb:5.1f}%")
print()
print(wrap(
    "RECORDED AS A SPONSOR CLAIM ON A CONFERENCE POSTER, NOT AS A MEASUREMENT, and it uses the "
    "protein-binding-adjusted Ba/F3 target lines round 213 reconstructed rather than an "
    "independent scale. IT IS NOT A LICENCE TO REOPEN THE RECEPTOR LEDGER (CORR-046, CORR-217). "
    "It bears only on FGFR3 coverage, where the exchange rate to height is the one thing this "
    "atlas does know something about."))

rule()
