#!/usr/bin/env python3
"""ROUND 225 - the bone-age rates, measured, and what they do to round 224.

BOTH THINGS THE USER ASKED FOR WERE FOUND, AND BOTH KILL THE HYPOTHESIS THEY WERE
MEANT TO TEST.

(1) A BASELINE BONE AGE FOR THE WONG CASE: there is none, and the paper says so in
    terms. But reading it directly returned something better and worse - the child
    was NOT pre-pubescent. He was 15 y 4 m, TANNER 2-3, with testosterone consistent
    with early puberty and GH, IGF-I and IGFBP-3 WITHIN NORMAL RANGES for that stage.

(2) A BONE AGE IN CHILDREN WITH INTACT GONADAL FUNCTION: found, randomised,
    placebo-controlled, Greulich-Pyle, with numbers - in a file this atlas has held
    since round 207.

Round 224 proposed that the FGFR arm grows children without advancing bone age
BECAUSE they were sex-steroid deficient, and that anastrozole might therefore be a
prerequisite rather than a parallel lever. BOTH LEGS OF THAT ARGUMENT ARE NOW GONE.
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

head(1, "THE MEASURED BONE-AGE RATE, IN CHILDREN WITH INTACT GONADAL AXES")
print(wrap(
    "Voxzogo CHMP assessment report, study 111-301 - randomised, placebo-controlled, bone age by the "
    "GREULICH AND PYLE atlas method on left hand and wrist X-rays, baseline bone age about 8 years in "
    "both arms, 52 weeks. THIS IS THE ONLY RANDOMISED BONE-AGE RATE ON THIS AXIS IN THIS ATLAS."))
print()
vos, vos_sd, pbo, pbo_sd = 1.02, 0.83, 1.14, 0.82
print(f"      vosoritide   change from baseline  {vos:.2f} years (SD {vos_sd})")
print(f"      placebo      change from baseline  {pbo:.2f} years (SD {pbo_sd})")
print(f"      difference   {vos-pbo:+.2f} years - THE TREATED ARM MATURED SLIGHTLY LESS THAN PLACEBO")
print("      similar in both males and females; no acceleration to Month 48 in 111-202/205")
print()
print(wrap(
    "CHILDREN WITH ACHONDROPLASIA HAVE NORMAL GONADAL FUNCTION. So the question round 224 could not "
    "answer from three case reports is answered here by a randomised trial: an agent that suppresses "
    "the FGFR3-MAPK axis grew these children WITHOUT advancing bone age, in a population with intact "
    "sex steroids. THE SEX-STEROID-POOR BACKGROUND IS NOT REQUIRED FOR THE EFFECT."))

head(2, "AND THE OTHER LEG BREAKS TOO - THE WONG CHILD WAS NOT PRE-PUBESCENT")
print(wrap(
    "erdachild2024, read directly rather than through this atlas's own one-line summary. AGE AT START "
    "15 YEARS 4 MONTHS. TANNER STAGE 2-3, described as delayed. TOTAL TESTOSTERONE CONSISTENT WITH THE "
    "EARLY PUBERTAL STAGE with free testosterone low. GH, IGF-I AND IGFBP-3 WITHIN NORMAL RANGES for a "
    "male at pubertal stage II-III. NO pituitary or gonadal deficiency reported."))
print()
print(wrap(
    "THE BIBLIOGRAPHY ENTRY SAID 'PRE-PUBESCENT BOY' WITH 'PRE-pubertal GH, IGF-I, IGFBP-3 and "
    "testosterone', AND ROUND 224 BUILT ON THAT. He was mid-pubertal with normal growth-axis hormones. "
    "The strongest case in the series - the 19.06 cm/year child - is therefore NOT an example of growth "
    "in a sex-steroid-deficient background, and round 224's 'all three children' is false."))

head(3, "THE BASELINE BONE AGE THE USER ASKED FOR - IT DOES NOT EXIST, STATED BY THE AUTHORS")
print(wrap(
    "The paper says it in terms: BONE AGE ASSESSMENTS HAD NOT BEEN PERFORMED PRIOR TO OR DURING "
    "ERDAFITINIB THERAPY. What exists is two readings, both AFTER the drug:"))
print()
print("      chronological age 16.2 y   (at cessation)     bone age 14.0 y   delay 2.2 y")
print("      chronological age 17.42 y  (follow-up)        bone age 'remained 2 years delayed'")
ca0, ba0, ca1 = 16.2, 14.0, 17 + 5/12
for delay in (2.0, 2.2):
    ba1 = ca1 - delay
    print(f"        if the follow-up delay is exactly {delay:.1f} y -> bone age {ba1:.2f}, "
          f"dBA/dCA = {(ba1-ba0)/(ca1-ca0):.2f}")
print()
print(wrap(
    "AND THE INTERVAL IS LARGELY OFF DRUG, because therapy ceased at 16.2. So even this does not give "
    "an ON-TREATMENT maturation rate. THE ON-TREATMENT BONE-AGE RATE FOR ERDAFITINIB DOES NOT EXIST "
    "AND CANNOT BE RECOVERED FROM THIS CASE - the films were never taken."))

head(4, "SO WHAT DOES THE COACH CONTRAST ACTUALLY SURVIVE AS")
print("      agent / regimen                         dBA per calendar year    source quality")
rows = [("vosoritide 111-301", f"{vos:.2f}", "randomised, placebo-controlled, GP method"),
        ("PLACEBO in the same trial", f"{pbo:.2f}", "the natural-history anchor"),
        ("navepegritide + GH, naive", "1.33", "derived from cohort mean ratios, n=12"),
        ("navepegritide + GH, experienced", "1.57", "derived from cohort mean ratios, n=9"),
        ("infigratinib PROPEL3", "no number", "'no accelerated progression' - conference PDF"),
        ("erdafitinib", "no number", "no bone age ever taken on treatment")]
for a, b, c in rows:
    print(f"      {a:<38s} {b:>8s}                {c}")
print()
print(wrap(
    "THE RIGHT COMPARATOR IS 1.14, NOT 1.0. Round 223 read COACH's 1.33 and 1.57 against an implicit "
    "normal rate of 1.0. The only measured contemporaneous control on this axis matured at 1.14, so "
    "the excess attributable to adding growth hormone is about +0.19 and +0.43 bone-age years per year, "
    "not +0.33 and +0.57."))
print()
print(wrap(
    "AND THE NOISE SWALLOWS PART OF IT. The EPAR gives the only dispersion anywhere in this comparison - "
    "SD about 0.82 years on a 52-week bone-age change, which is Greulich-Pyle reader variability as much "
    "as biology."))
print()
for n in (60, 30, 12, 9):
    se = pbo_sd / math.sqrt(n)
    print(f"      at n={n:3d}  SE of a mean dBA = {se:.3f} y   95% interval +/-{1.96*se:.2f} y")
print()
print(wrap(
    "COACH REPORTS NO DISPERSION FOR ITS RATIOS AND HAS n = 12 AND 9. At n = 9 a 95 per cent interval "
    "spans about +/-0.54 years, which comfortably contains the gap between 1.57 and 1.14. THE CONTRAST "
    "IS DIRECTIONAL AND NOT STATISTICALLY ESTABLISHED, and nobody - not the paper, not this atlas until "
    "now - has run the test. Round 223 stated it as though it were established."))

head(5, "WHAT SURVIVES, AND WHAT ROUND 224 HAS TO GIVE BACK")
for line in [
    "SURVIVES - suppressing the FGFR3-MAPK axis grows children without measurably advancing bone age,",
    "  and this is now a RANDOMISED result with numbers rather than three case reports.",
    "SURVIVES - growth hormone added on top is the arm that carries the bone-age cost, directionally,",
    "  and it is the only agent in this file that moves the ratio at all.",
    "",
    "GIVEN BACK - round 224's claim that all three erdafitinib children were sex-steroid deficient.",
    "  The 19.06 cm/year child was Tanner 2-3 with normal GH, IGF-I and IGFBP-3.",
    "GIVEN BACK - round 224's hypothesis that a sex-steroid-poor background is the CONDITION for",
    "  growth without maturation, and that anastrozole is therefore a prerequisite. Children with",
    "  intact gonadal axes show the same absence of bone-age advance in a randomised trial.",
    "  Anastrozole returns to being an independent lever, which is what it was before round 224.",
    "GIVEN BACK - round 223's presentation of the COACH bone-age excess as established rather than",
    "  directional.",
]:
    print("    " + line if line else "")

head(6, "AND ONE PROVENANCE PROBLEM WORTH MORE THAN IT LOOKS")
print(wrap(
    "The atlas's claim that infigratinib shows NO ACCELERATED PROGRESSION OF BONE AGE comes from "
    "propel3_2026, recorded as a T3 CONFERENCE PRESENTATION PDF. Querying the trial registry directly, "
    "NCT06164951 HAS NO BONE-AGE OUTCOME MEASURE AT ALL - not primary, not secondary, not exploratory - "
    "and the NEJM abstract contains no bone-age statement. SO THE ONE FGFR-INHIBITOR BONE-AGE CLAIM IN "
    "THIS ATLAS HAS NO PRESPECIFIED ENDPOINT BEHIND IT and rests on a sentence in a slide deck."))
print()
print(wrap(
    "THAT MATTERS BECAUSE IT IS THE ONLY BONE-AGE EVIDENCE FOR THE DRUG CLASS THIS STACK ACTUALLY USES. "
    "The vosoritide numbers are excellent and they are a DIFFERENT MOLECULE acting on the same axis from "
    "the other end. Transferring them to an FGFR inhibitor is the same disease-to-normal style of "
    "assumption round 223 flagged, one axis over."))
rule()
