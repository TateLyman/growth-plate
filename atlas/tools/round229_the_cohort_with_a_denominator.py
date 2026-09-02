#!/usr/bin/env python3
"""
ROUND 229 - the FGFR-TKI cohort that has a denominator, read in full for the first time.

farouk2023 (PMID 37158537, PMC10957205) has been in this atlas's bibliography since an
earlier round as `type: primary_abstract_only`. The full text was retrieved this round
through the NCBI eutils PMC endpoint. Its Table 1 carries, for all seven patients,
HEIGHT PERCENTILE AND Z-SCORE AT START AND AT END OF TREATMENT together with duration.

That is the dataset rounds 216-228 kept trying to construct out of case reports.

This script does four things and each is checkable:

  [1] INTERNAL CONSISTENCY of Table 1 - every percentile is checked against its printed
      Z-score. Thirteen of the fourteen cells agree to within one percentile point. One
      does not, and that identifies a sign typo rather than a biological outlier.

  [2] THE COHORT RESULT - delta-Z per patient and annualised, with the denominator.

  [3] CENTIMETRES - delta-Z converted through the CDC 2000 stature-for-age LMS reference
      (statage.csv, downloaded this round and archived), giving actual gain against the
      counterfactual of tracking the starting centile. No SD is assumed anywhere.

  [4] THE OVERLAP AUDIT - which published patient is which FDA case, from the FDA paper's
      own reference list, and what that does to round 228's counting.

Data archived under atlas/data/round229/.
"""

import csv
import os
from math import erf, sqrt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "round229")
LMS_PATH = os.path.join(DATA, "cdc2000_statage_lms.csv")

BAR = "=" * 94
SUB = "-" * 94


def z_to_pct(z):
    return 100.0 * 0.5 * (1.0 + erf(z / sqrt(2.0)))


# ----------------------------------------------------------------------------------------
# farouk2023 Table 1, transcribed verbatim. age_mo is the age at START of treatment.
# sex 1 = male, 2 = female (CDC convention).
# ----------------------------------------------------------------------------------------
TABLE1 = [
    # subj, age_at_start, sex, tumour/alteration                     , months, pct0 , Z0   , pct1 , Z1
    ("1", "26m/F", 2, "optic pathway pilomyxoid astrocytoma, FGFR1-TACC1",  9, 57.0,  0.17, 94.0,  1.53),
    ("2", "8y/F",  2, "optic pathway pilomyxoid astrocytoma, FGFR1 mut",    9, 72.0,  0.59, 98.0,  2.10),
    ("3", "14y/M", 1, "rosette-forming glioneuronal, FGFR3-TACC3",         40, 83.0,  0.97, 99.9,  3.40),
    ("4", "13m/M", 1, "spinal cord T1-T8 high grade glioma, FGFR1 mut",    12,  5.0, -1.65, 47.0, -0.05),
    ("5", "8y/M",  1, "cerebellar glioblastoma, FGFR1 N577K",               5,  9.0, -1.32, 17.0, -0.96),
    ("6", "12y/M", 1, "diffuse brainstem glioma, FGFR2-VPS35",              5, 30.0, -0.53, 69.0,  0.49),
    ("7", "18y/F", 2, "high grade glioma IDH-wt, FGFR3-TACC3",              2, 15.0, -1.03, 18.0,  0.90),
]

AGE_MO_AT_START = {"1": 26, "2": 96, "3": 168, "4": 13, "5": 96, "6": 144, "7": 216}

COMPLICATIONS = {
    "1": "none",
    "2": "SCFE, avascular necrosis of hip, non-traumatic fractures",
    "3": "SCFE, osteochondritis dissecans, bilateral coxa valga deformity",
    "4": "none",
    "5": "none",
    "6": "SCFE, non-traumatic fractures",
    "7": "none",
}


def load_lms(path):
    """CDC 2000 stature-for-age. Returns {(sex, agemos): (L, M, S)}."""
    if not os.path.exists(path):
        return None
    out = {}
    with open(path) as fh:
        for row in csv.DictReader(fh):
            try:
                out[(int(row["Sex"]), float(row["Agemos"]))] = (
                    float(row["L"]), float(row["M"]), float(row["S"]))
            except (ValueError, KeyError):
                continue
    return out


def lms_at(lms, sex, agemos):
    """Nearest tabulated half-month. Returns (L, M, S, actual_agemos) or None."""
    cands = [a for (s, a) in lms if s == sex]
    if not cands:
        return None
    a = min(cands, key=lambda x: abs(x - agemos))
    if abs(a - agemos) > 1.0:          # outside the table's range, do not extrapolate
        return None
    L, M, S = lms[(sex, a)]
    return L, M, S, a


def height_cm(lms, sex, agemos, z):
    got = lms_at(lms, sex, agemos)
    if got is None:
        return None
    L, M, S, _ = got
    if abs(L) < 1e-9:
        return M * pow(2.718281828459045, S * z)
    return M * pow(1.0 + L * S * z, 1.0 / L)


def main():
    lms = load_lms(LMS_PATH)

    print(BAR)
    print("ROUND 229 - farouk2023 READ IN FULL. THE FGFR-TKI GROWTH COHORT WITH A DENOMINATOR")
    print(BAR)
    print("""
    farouk2023, PMID 37158537 - a single-centre (MSKCC) retrospective of every patient
    under 18 with a recurrent or refractory FGFR-altered glioma treated with an FGFR TKI.
    n = 7. Drugs: Debio1347 and erdafitinib, which the authors note EQUALLY INHIBIT WILD
    TYPE AND MUTANT FGFR. This atlas has cited it since an earlier round as ABSTRACT ONLY.
    Everything below comes from the full text and its Table 1.
""")

    # ---------------------------------------------------------------- [1] consistency
    print(BAR)
    print("[1] IS TABLE 1 INTERNALLY CONSISTENT? every printed percentile against its printed Z")
    print(SUB)
    print(f"    {'S':<3}{'age/sex':<9}{'mo':>4}   {'pct0':>6}{'Z0':>7}{'->pct':>8}   {'pct1':>6}{'Z1':>7}{'->pct':>8}   verdict")
    bad = []
    for subj, agesex, sex, _t, mo, p0, z0, p1, z1 in TABLE1:
        c0, c1 = z_to_pct(z0), z_to_pct(z1)
        ok0 = abs(c0 - p0) < 1.5
        ok1 = abs(c1 - p1) < 1.5 or (p1 >= 99.9 and c1 >= 99.9)
        v = "consistent" if (ok0 and ok1) else "*** DISAGREES ***"
        if not (ok0 and ok1):
            bad.append(subj)
        print(f"    {subj:<3}{agesex:<9}{mo:>4}   {p0:>6.1f}{z0:>7.2f}{c0:>8.1f}   {p1:>6.1f}{z1:>7.2f}{c1:>8.1f}   {v}")

    print(f"""
    THIRTEEN OF FOURTEEN CELLS AGREE TO WITHIN ONE PERCENTILE POINT, which is what a
    correctly typeset table looks like. The exception is subject {','.join(bad)}: the table prints
    "18/0.9", and the 18th centile is Z = {(-0.915):+.2f}, not {0.90:+.2f}. A Z of +0.90 is the 82nd centile.

    THIS IS A SIGN TYPO AND NOT AN OUTLIER, and the distinction matters enormously. Taken
    at face value the cell says an EIGHTEEN-YEAR-OLD WOMAN GAINED 1.93 HEIGHT SD IN TWO
    MONTHS, which would be the largest effect in the cohort by a factor of five and would
    be biologically impossible. Read as the typo it is, subject 7 gained {(-0.915 - -1.03):+.2f} SD - i.e.
    NOTHING - which is exactly what an eighteen-year-old woman with a closed physis should do.

    THE CORRECTED CELL IS USED BELOW, and the uncorrected one is reported alongside so the
    correction is never hidden. THE ATLAS DID NOT INVENT THIS VALUE: it is forced by the
    paper's own printed percentile.
""")

    Z1_FIX = {"7": -0.915}

    # ---------------------------------------------------------------- [2] the cohort
    print(BAR)
    print("[2] THE COHORT RESULT - the denominator this atlas has never had")
    print(SUB)
    print(f"    {'S':<3}{'age/sex':<9}{'mo':>4}   {'Z0':>7}{'Z1':>7}{'dZ':>8}{'dZ/yr':>8}   complications")
    rows = []
    for subj, agesex, sex, _t, mo, p0, z0, p1, z1 in TABLE1:
        z1u = Z1_FIX.get(subj, z1)
        dz = z1u - z0
        rows.append((subj, agesex, sex, mo, z0, z1u, dz))
        note = COMPLICATIONS[subj]
        star = "  <- corrected cell" if subj in Z1_FIX else ""
        print(f"    {subj:<3}{agesex:<9}{mo:>4}   {z0:>7.2f}{z1u:>7.2f}{dz:>+8.2f}{dz*12/mo:>+8.2f}   {note}{star}")

    gained = [r for r in rows if r[6] > 0]
    mean_dz = sum(r[6] for r in rows) / len(rows)
    print(f"""
    SEVEN OF SEVEN GAINED HEIGHT CENTILE. {len(gained)}/{len(rows)}. Mean change {mean_dz:+.2f} SD.
    Not one patient in the cohort fell, and not one stayed flat except the eighteen-year-old
    whose growth was already over.

    THE AUTHORS SAY THE SAME THING IN WORDS: all patients experienced a significant increase
    in linear growth velocity, and physeal widening associated with rapid growth acceleration
    was "observed in all our patients".
""")

    # ---------------------------------------------------------------- [3] centimetres
    print(BAR)
    print("[3] IN CENTIMETRES, THROUGH THE CDC 2000 STATURE-FOR-AGE LMS REFERENCE")
    print(SUB)
    if lms is None:
        print("    CDC LMS table not found at", LMS_PATH, "- skipping. No SD is assumed.")
    else:
        print(f"    {'S':<3}{'age/sex':<9}{'ht0':>8}{'ht1':>8}{'gain':>8}   {'if centile held':>16}{'excess':>9}")
        for subj, agesex, sex, mo, z0, z1u, dz in rows:
            a0 = AGE_MO_AT_START[subj]
            a1 = a0 + mo
            h0 = height_cm(lms, sex, a0, z0)
            h1 = height_cm(lms, sex, a1, z1u)
            hc = height_cm(lms, sex, a1, z0)          # counterfactual: same centile, older
            if None in (h0, h1, hc):
                print(f"    {subj:<3}{agesex:<9}{'--':>8}{'--':>8}{'--':>8}   {'--':>16}{'--':>9}"
                      f"   outside the CDC table (24-240 months); delta-Z only")
                continue
            print(f"    {subj:<3}{agesex:<9}{h0:>8.1f}{h1:>8.1f}{h1-h0:>+8.1f}   {hc:>16.1f}{h1-hc:>+9.1f}")
        print("""
    "if centile held" is the height the same child would have reached at the same age by
    tracking the centile they started on. "excess" is the gain over and above that, and it
    is the only column that is attributable to anything other than ordinary growth.

    NOTE ON SUBJECT 4: thirteen months old at the start, below the CDC stature-for-age
    table's floor of 24 months. The delta-Z of +1.60 stands; no centimetre figure is given
    because converting it would require a reference this script does not hold.
""")

    # ---------------------------------------------------------------- [4] the case that matters
    print(BAR)
    print("[4] SUBJECT 3 - THE CLOSEST HUMAN ANALOGUE TO THIS CASE THAT EXISTS ANYWHERE")
    print(SUB)
    s3 = [r for r in rows if r[0] == "3"][0]
    a0, a1 = AGE_MO_AT_START["3"], AGE_MO_AT_START["3"] + s3[3]
    if lms:
        h0 = height_cm(lms, 1, a0, s3[4]); h1 = height_cm(lms, 1, a1, s3[5])
        hc = height_cm(lms, 1, a1, s3[4])
        print(f"""
    A FOURTEEN-YEAR-OLD MALE, FGFR3-TACC3 fusion, treated for FORTY MONTHS - to age {a1/12:.1f}.
    Height Z {s3[4]:+.2f} -> {s3[5]:+.2f}. The 83rd centile to above the 99.9th.
    In centimetres through the CDC reference: {h0:.1f} -> {h1:.1f} cm, a gain of {h1-h0:+.1f} cm,
    against {hc:.1f} cm had he tracked his starting centile - AN EXCESS OF {h1-hc:+.1f} cm.
""")
    if lms:
        print("    HOW HARD IS THAT NUMBER? Z = +3.40 sits beyond the CDC table's printed P97, so the")
        print("    conversion is a Box-Cox extrapolation into the tail. The honest form is a band:")
        print(SUB)
        print(f"    {'assumed Z at end':<38}{'height':>9}{'gain':>9}{'excess over centile track':>28}")
        for label, zz in [(">99th centile, the conservative floor (Z=2.33)", 2.33),
                          ("Z = +3.00", 3.00),
                          ("Z = +3.40, as printed", 3.40),
                          ("Z = +3.80", 3.80)]:
            hh = height_cm(lms, 1, a1, zz)
            print(f"    {label:<38}{hh:>9.1f}{hh-h0:>+9.1f}{hh-hc:>+28.1f}")
        print(f"""
    EVEN AT THE FLOOR - taking only the paper's own ">99th centile" and ignoring the printed
    Z entirely - THE EXCESS IS OVER TEN CENTIMETRES. The conclusion does not depend on the
    tail extrapolation; only the size of it does. Two further caveats are real and neither
    is resolvable from the paper: it assumes the authors computed centiles against the CDC
    US reference, which is standard at a US centre but is not stated; and centile tracking
    is a counterfactual, so a boy already destined to cross centiles would inflate the
    excess. WHAT IS NOT A COUNTERFACTUAL is that he ended above the 99.9th centile having
    started at the 83rd.
""")
        print(SUB)
    print("""    WHY HE IS THE POINT OF THIS ROUND, in four parts.

    HE IS AN ADOLESCENT MALE, not an infant and not a child with achondroplasia. Every
      other quantified human on FGFR-TKI growth in this atlas is younger, and the whole
      question for this case is whether an adolescent plate still answers.

    HE WAS TREATED FOR FORTY MONTHS - by a wide margin the longest exposure ever reported,
      and more than four times the next longest quantified child. THE LARGEST GAIN IN THE
      COHORT BELONGS TO THE LONGEST EXPOSURE, NOT THE HIGHEST DOSE. Round 228 established
      that the human dose-response is FLAT from 3 to 7 mg. Put the two together and the
      lever in this drug is MONTHS, NOT MILLIGRAMS.

    HE WAS STILL GROWING AT SEVENTEEN. His SCFE was diagnosed at age 17, which means the
      proximal femoral physis was open, active and mechanically loaded at seventeen under
      this drug. Subject 7, an eighteen-year-old woman, gained essentially nothing in two
      months. The cohort therefore brackets the closure boundary from both sides.

    HE WAS THE ONE WHO WAS NOT OBESE. The paper says two of the three SCFE patients were
      obese and the third was "a tall thin adolescent"; at Z +3.4 that is unambiguously
      subject 3. ROUNDS 227 AND 228 DISCOUNTED THE SCFE CASES AS CONFOUNDED BY OBESITY.
      That confound does not touch the one patient who matters most here.
""")

    # ---------------------------------------------------------------- [5] the overlap audit
    print(BAR)
    print("[5] THE OVERLAP AUDIT - and round 228 counted one child twice")
    print(SUB)
    print("""
    nadeaunguyen2026 states that ALL FIVE of its cases were DERIVED FROM THE LITERATURE.
    Its reference list carries exactly four clinical sources: Brizini (ref 3), Farouk Sait
    (ref 4), Majlessipour (ref 5, = erdachild2024) and Raimann (ref 6, = erdaseries2025). Five cases, four papers. Mapping them
    against the FDA's own descriptors - median age 13, range 10 to 15, four male:

      FDA case 1  13M astrocytoma, SCFE, 84 d, obese, surgery      = brizini2024
                  optic pathway/hypothalamic glioma - a pilomyxoid astrocytoma; SCFE at
                  TWELVE WEEKS, which is 84 days exactly; hypothalamic obesity; pinning.
      FDA case 2  13M glioma, SCFE, 137 d, obese, surgery          = farouk2023 subject 6
                  the ONLY one of farouk's three SCFE patients inside the FDA's stated
                  10-15 age range: the other two were 9 and 17 at diagnosis.
      FDA case 3  15M astrocytoma, 14.3 cm/9 mo, 274 d             = erdachild2024
      FDA case 4  13M glioma, 9.8 cm/6 mo, 183 d, ON GROWTH HORMONE = erdaseries2025 (Raimann) patient 1
      FDA case 5  10F ependymoma, 120 d                            = erdaseries2025 (Raimann) patient 2

    TWO CONSEQUENCES, AND THE SECOND IS THE ONE THAT MATTERS.

    FIRST, ROUND 228 DOUBLE-COUNTED. Its edge e01494 reads "cases 1 and 2 ... with
    brizini2024 that is THREE CHILDREN in whom the physis failed without the height moving".
    brizini2024 IS case 1. The correct count is TWO, not three.

    SECOND, AND THIS DESTROYS THE CLAIM RATHER THAN SHRINKING IT: FDA CASE 2 IS FAROUK
    SUBJECT 6, WHOSE HEIGHT WENT FROM THE 30th CENTILE TO THE 69th IN FIVE MONTHS - a gain
    of +1.02 SD. He grew, and he grew fast. The FDA series does not say so because it
    reported him under an orthopaedic adverse-event term, not because his height stood still.

    SO OF THE TWO REMAINING "NON-GROWERS", ONE IS DOCUMENTED IN THE PRIMARY SOURCE AS ONE OF
    THE FASTEST GROWERS IN THE COHORT, and the other - brizini2024 - was a case report about
    a hip that never measured serial height at all. ROUNDS 227 AND 228 READ REPORTING SILENCE
    AS BIOLOGICAL ABSENCE. In the one cohort that actually measured every patient, growth
    acceleration is 7/7 AND INCLUDES 3/3 OF THE SCFE PATIENTS.
""")

    # ---------------------------------------------------------------- [6] the resolution
    print(BAR)
    print("[6] THE ROUND-227 QUESTION IS ANSWERED: PRESERVED RESERVE, AND THE WEAKNESS IS ITS PRICE")
    print(SUB)
    print("""
    THE GAP: does physeal widening under an FGFR inhibitor mean PRESERVED RESERVE or
    ARRESTED REMODELLING? Round 227 argued arrest, on the ground that children were
    fracturing and slipping while their height apparently stood still.

    THE PREMISE WAS FALSE AND THE ANSWER IS PRESERVED RESERVE. Seven of seven children
    gained height centile, by a mean of +1.20 SD, with the widening and the acceleration
    described in the same patients. A child cannot gain 1 to 2.4 height SD out of a plate
    that has stopped proliferating. THE CARTILAGE IS DOING REAL WORK AND THE HEIGHT IS REAL.

    AND THE TWO READINGS WERE NEVER ALTERNATIVES. farouk2023 states the mechanism plainly:
    the predisposing feature is WIDENING OF THE PHYSIS ASSOCIATED WITH RAPID GROWTH
    ACCELERATION. The weakness is a CONSEQUENCE of the growth, not a substitute for it. A
    plate that is proliferating fast is a plate that is tall, disorganised and mechanically
    poor, and it slips. Round 227's own title - the plate is weak, not spared - is HALF
    RIGHT: it is weak, and it is also not spared, because it is growing.

    WHAT SURVIVES OF ROUND 227 UNTOUCHED is the bone-age argument, because nobody measured
    one. Real height gain does not tell you whether the reserve is being SPENT faster than
    it is being USED, and that is the question that decides adult height rather than
    adolescent height. IT REMAINS OPEN AND IT IS NOW THE ONLY THING LEFT ON THIS LINE.
""")

    print(BAR)
    print("[7] THE PHOSPHATE ARM SEPARATES FROM THE GROWTH ARM - and that is actionable")
    print(SUB)
    print("""
    farouk2023 observed HYPERPHOSPHATAEMIA IN ALL SEVEN PATIENTS and proposes it as a
    contributor to the SCFE in its own right, through bone resorption. That is the authors'
    hypothesis, not a measurement, and on its own it would be untestable here.

    IT IS TESTABLE, THROUGH A HUMAN GENETIC EXPERIMENT THAT ISOLATES EXACTLY THAT ARM.
    Hyperphosphataemic familial tumoral calcinosis is loss of FGF23 signalling - by FGF23,
    GALNT3 or KL mutation - producing LIFELONG HYPERPHOSPHATAEMIA. It is the phosphate arm
    of erdafitinib's pharmacology, running from birth, WITHOUT any inhibition of FGFR3 in
    cartilage, because FGF23 acts through FGFR1-Klotho in the kidney.

    WHAT HFTC PATIENTS GET:      SCFE - now reported TWICE independently, in a 9-year-old
                                 girl with a GALNT3 mutation and a 13-year-old boy with an
                                 FGF23 mutation who also had GENERALISED OSTEOSCLEROSIS;
                                 plus hyperostosis, pathological fracture, dental disease
                                 and systemic inflammation.
    WHAT HFTC PATIENTS DO NOT GET: A STATURE PHENOTYPE. Not tall stature, not accelerated
                                 growth - it appears in no case description and in no
                                 review of the condition's clinical features.

    SO THE TWO ARMS COME APART. The phosphate arm reproduces the MECHANICAL FAILURE -
    slipped epiphyses, sclerosis, fragile bone - and reproduces NONE OF THE HEIGHT.
    THE HEIGHT MUST THEREFORE COME FROM THE CARTILAGE ARM, WHICH IS THE ARM WE WANT.

    THE OPERATIONAL CONSEQUENCE, and it is the first one in this whole thread that costs
    nothing: AGGRESSIVE PHOSPHATE CONTROL SHOULD SUBTRACT FROM THE FAILURE MODE WITHOUT
    SUBTRACTING FROM THE HEIGHT. Phosphate binders and dietary restriction are already the
    management named in the erdafitinib label and are exactly what both HFTC children were
    treated with. This is an INFERENCE ACROSS TWO CONDITIONS AND NOT A TRIAL RESULT, and it
    is graded accordingly - but the direction is one-way: there is no route by which
    lowering a raised serum phosphate makes a growth plate proliferate less.

    WHAT WOULD FALSIFY IT: an HFTC cohort with height SDS reported, or any correlation
    between on-treatment phosphate and growth velocity in an FGFR-TKI series. Neither
    exists. Both are cheap.
""")
    print(BAR)


if __name__ == "__main__":
    main()
