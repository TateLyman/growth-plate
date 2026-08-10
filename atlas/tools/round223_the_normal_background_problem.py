#!/usr/bin/env python3
"""ROUND 223 - all five open questions worked, and the answer to a sixth nobody asked.

THE SIXTH QUESTION IS THE ONE THAT MATTERS. Chasing question 3 (what does FGFR
inhibition do to autophagy in a NORMAL chondrocyte) turned up an experiment nobody
in this atlas had seen: an FGFR inhibitor given to WILD-TYPE littermates through
the pubertal window. And re-reading the Voxzogo EPAR - a file this atlas has held
since round 207 - turned up the regulator saying the same thing about the CNP arm.

BOTH AGENTS PUSH THE SAME AXIS THE SAME DIRECTION. BOTH WERE TESTED IN A NORMAL
BACKGROUND. BOTH CAME OUT WORSE THERE THAN IN THE DISEASE MODEL. This atlas has
been assuming that agents developed for achondroplasia transfer to an FGFR3-normal
patient, and has never tested the assumption.

That does NOT overturn the human erdafitinib measurement, and CORR-046 forbids
letting a rodent ledger overrule it. It does mean the premise now has direct
evidence against it in two species and two drug classes.
"""
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
head(1, "THE FGFR ARM, TESTED IN A NORMAL BACKGROUND, DID NOT LENGTHEN BONE")
print(wrap(
    "kot2026 - JBMR Plus 2026;10(3):ziag005. Infigratinib, an FGFR1-3 inhibitor, 2 mg/kg/day "
    "subcutaneously from postnatal day 21 to day 49 - the pubertal growth window - in Aga2/+ "
    "osteogenesis imperfecta mice AND IN WILD-TYPE LITTERMATES, n = 8 to 15 per group per sex."))
print()
print("      group                        femur length      growth plate zones     strength / trabecular")
print("      WILD-TYPE + infigratinib     NO SIGNIFICANT    no significant         REDUCED trabecular BMD")
print("                                   EFFECT, either    difference in          and microarchitecture;")
print("                                   sex               proliferative or       reduced stiffness, yield")
print("                                                     hypertrophic zone      point and ultimate force")
print("                                                                            in MALES")
print("      Aga2/+ + infigratinib        increased in      increased in BOTH      not the comparison here")
print("                                   FEMALES           sexes, specifically")
print("                                                     the proliferative zone")
print()
print(wrap(
    "THIS IS THE CLOSEST PUBLISHED EXPERIMENT TO THIS CASE AND IT IS THE FIRST TIME THE ATLAS HAS "
    "SEEN IT. An FGFR inhibitor, through the growth window, in an animal with NORMAL FGFR3: no "
    "length gain, no zone change, and a measurable cost to bone quality in one sex. And note "
    "CORR-191 applies to the positive arm too - the Aga2/+ femur gain is FEMALE ONLY, which by "
    "this atlas's own rule is not a length result."))

# ----------------------------------------------------------------------------- 2
head(2, "AND THE REGULATOR SAYS THE SAME THING ABOUT THE CNP ARM, IN A FILE HELD SINCE ROUND 207")
print(wrap(
    "The Voxzogo CHMP assessment report, EMA/397108/2021, has been on disk since round 207 and this "
    "passage was never extracted:"))
print()
for line in [
    "\"Particularly in HEALTHY ANIMALS as tested in the repeated-dose toxicity studies, vosoritide",
    "at least in high doses caused undesired bone effects. These included ALTERED SHAPE,",
    "DISLOCATION OF PHYSIS, DECREASED BMD, REDUCED MECHANICAL STABILITY, ALTERED HISTOLOGY OF THE",
    "GROWTH PLATE and consecutive IMPAIRMENT OF GAIT AND HIND LIMB USE.\"",
    "",
    "\"In animals of disease, functional impairment of hind limbs was HARDLY OBSERVED.\"",
    "",
    "\"vosoritide affected the normal chondrocyte ordering in the growth plates of NORMAL ANIMALS,",
    "leading to functional impairment of the adjacent joints, probably due to IRREGULAR OR",
    "ASYMMETRIC BONE GROWTH.\"",
]:
    print("      " + line)
print()
print(wrap(
    "AND THE SPONSOR'S OWN EXPLANATION IS THE MECHANISM, NOT AN EXCUSE. They argued that irregular "
    "bone growth is a consequence of STRONG FGFR3 INHIBITION, which vosoritide can achieve in "
    "healthy animals but not in achondroplasia patients BECAUSE THERE THE BASAL FGFR3 ACTIVITY IS "
    "MUCH HIGHER - and that it is not intended to suppress FGFR3 below normal. The CHMP recorded "
    "that it understood the argument. THE ARGUMENT IS THAT A NORMAL BACKGROUND IS THE ONE THAT "
    "GETS PUSHED BELOW NORMAL. That is our background."))
print()
print(wrap(
    "The juvenile rat findings at 30 micrograms/kg and above - twice the 15 microgram/kg clinical "
    "dose - were enlargement and persistence of physes, DEGENERATION AND NECROSIS IN THE FEMORAL "
    "HEAD AND NECK AND ACETABULUM, disorganised cartilage and bone growth in the tibia, and "
    "tibiotarsal arthritis, described as degenerative joint disease and attributed to EXAGGERATED "
    "GROWTH CAUSING MECHANICAL DYSFUNCTION. At 300 micrograms/kg, five animals had limited use of "
    "hips from day 88 that persisted through recovery, with bilateral abnormal femoral heads at "
    "necropsy in two."))
print()
print(wrap(
    "THIS IS A YIELD TERM AS WELL AS A SAFETY TERM, WHICH IS WHY IT BELONGS HERE AND NOT ONLY IN A "
    "RISK SECTION. Round 203 established that a scoliotic curve converts axial length into "
    "deviation. A dislocated physis, asymmetric growth and a necrotic femoral head do the same "
    "thing to the appendicular skeleton - and the CHMP notes it CANNOT BE EXCLUDED that vosoritide "
    "leads to irregular bone growth INDEPENDENT OF GROWTH VELOCITY."))

# ----------------------------------------------------------------------------- 3
head(3, "WHAT THE CONVERGENCE DOES AND DOES NOT ESTABLISH")
print(wrap(
    "TWO INDEPENDENT SOURCES, TWO SPECIES, TWO DRUG CLASSES ACTING ON THE SAME AXIS FROM OPPOSITE "
    "ENDS - one raising CNP to suppress FGFR3-MAPK, one inhibiting the receptor directly - AND "
    "BOTH COME OUT WORSE IN A NORMAL BACKGROUND THAN IN THE DISEASE MODEL. The atlas has been "
    "assuming that achondroplasia-developed agents transfer to an FGFR3-normal patient, and has "
    "never tested the assumption."))
print()
print(wrap(
    "WHAT IT DOES NOT DO IS OVERTURN THE HUMAN MEASUREMENT, AND CORR-046 IS EXPLICIT ABOUT THIS. "
    "The erdafitinib child grew 19.06 cm/year and 'accelerated growth' went into the US label from "
    "a five-case series. Those are humans, in the right background, with the outcome measured. A "
    "ledger assembled from rodents does not overrule a measurement - that is precisely the error "
    "CORR-046 retracted and CORR-217 caught on its fourth approach. THE HONEST STATEMENT IS THAT "
    "THE TRANSFER PREMISE NOW HAS DIRECT EVIDENCE AGAINST IT AND ONE LARGE HUMAN OBSERVATION FOR "
    "IT, and that the two have never been reconciled because nobody has measured a growth plate in "
    "a human with normal FGFR3 under either drug."))
print()
print(wrap(
    "THE DOSE CAVEAT CUTS BOTH WAYS AND MUST BE STATED. kot2026 used 2 mg/kg/day of infigratinib "
    "for 28 days; this atlas has separately established that the selective agents have NEVER been "
    "dosed near the exposure that produced 19 cm/year. A null at one exposure is not a null at "
    "all exposures. Equally, the vosoritide findings were dose-dependent and appeared at twice the "
    "clinical dose, so the margin in a normal background is narrower than the achondroplasia "
    "programme's numbers imply."))

# ----------------------------------------------------------------------------- 4
head(4, "COACH - GROWTH HORMONE ON TOP OF A MAXIMAL CNP ARM, AND WHAT IT COSTS")
print(wrap(
    "mcdonnell2026, Eur J Endocrinol 2026;194(6):745-755. COACH, phase 2, open-label, externally "
    "controlled, 21 children with achondroplasia aged 2-11 at three sites. Navepegritide 100 "
    "micrograms/kg/week PLUS lonapegsomatropin at a mean 0.24 to 0.27 mg/kg/week, 52 weeks."))
print()
print("      cohort                          AGV week 52     comparator          difference")
print("      treatment-naive (n=12)          8.69 cm/yr      5.95 (matched       +2.74 cm/yr")
print("                                                      navepegritide       (95% CI 2.11-3.38,")
print("                                                      monotherapy)        P<0.0001)")
print("      navepegritide-experienced (n=9) 8.42 cm/yr      5.14 (own treated   +3.28 cm/yr")
print("                                                      baseline, >1 yr)    (P<0.0001)")
print()
print(wrap(
    "THE SECOND ROW IS THE ONE THAT MATTERS. Those children were ALREADY AT STEADY STATE ON "
    "NAVEPEGRITIDE FOR OVER A YEAR, and adding growth hormone bought +3.28 cm/year WITHIN SUBJECT. "
    "That is the cleanest human demonstration in this atlas that the somatotropic arm is ADDITIVE "
    "ON TOP OF A SATURATED CNP ARM. And the size reorders the stack: navepegritide's own effect "
    "over placebo is 1.49 cm/year, so GH's increment on top of it is roughly TWICE the CNP "
    "increment over nothing."))
print()
# bone age arithmetic
for label, ca0, r0, r1 in [("treatment-naive", 5.26, 0.77, 0.86), ("navepegritide-experienced", 8.32, 0.92, 0.99)]:
    ba0 = ca0 * r0
    ca1 = ca0 + 1.0
    ba1 = ca1 * r1
    print(f"      {label:<28s} CA {ca0:.2f} -> {ca1:.2f}   BA {ba0:.2f} -> {ba1:.2f}   "
          f"dBA/dCA = {(ba1-ba0):.2f}")
print()
print(wrap(
    "AND THAT IS THE COST, COMPUTED FROM THEIR OWN RATIOS. The paper reports the bone-age to "
    "chronological-age ratio rising from 0.77 to 0.86 and from 0.92 to 0.99, and reads it as 'no "
    "acceleration of skeletal maturation beyond normal' BECAUSE THE RATIO STAYED BELOW 1.0. THAT "
    "IS THE WRONG INFERENCE. A ratio that RISES means bone age advanced FASTER THAN TIME. On their "
    "own numbers the combination spent 1.3 to 1.6 BONE-AGE YEARS PER CHRONOLOGICAL YEAR."))
print()
print(wrap(
    "IT IS CATCH-UP FROM A DELAYED BASELINE TOWARD NORMAL, WHICH IS BENIGN IN A FIVE-YEAR-OLD WITH "
    "A DECADE OF RESERVE. IT IS NOT BENIGN AT BONE AGE 16. Round 198 made reserve the exhaustible "
    "currency; a regimen that converts 1.5 years of reserve per calendar year is spending the "
    "thing this case has least of. The atlas's round-29 test - height gained per bone-age year - "
    "was retired at CORR-040 because vosoritide and infigratinib both passed it. THE COMBINATION "
    "DOES NOT PASS IT, and it is the first agent in this file that measurably fails."))
print()
print(wrap(
    "AND THE SECOND COST IS DIRECTIONAL. The upper-to-lower segment ratio FELL by 0.07 and 0.06, "
    "and arm span rose 9.4 and 7.9 cm - the gain is LEG-FAVOURING, with the trunk lagging. The "
    "atlas already found vosoritide alone drifting the same way at -0.10 in a real-world cohort. "
    "FOR A CASE WHOSE RESERVE IS SUBSTANTIALLY AXIAL, THE COMBINATION BUYS THE WRONG SEGMENT."))

# ----------------------------------------------------------------------------- 5
head(5, "THE OTHER FOUR QUESTIONS, ANSWERED OR PRICED")
items = [
    ("Q1  Does Tat-beclin-1 lengthen a WILD-TYPE bone?",
     "ANSWERED - NO SUCH EXPERIMENT EXISTS ANYWHERE. Round 222 established the arm is absent from "
     "the inventors' patent. A literature sweep now confirms it is absent from the published "
     "literature too - Tat-beclin-1 bone work is confined to the deficient genotypes. The nearest "
     "genetic reciprocal, Beclin-1 heterozygous mice, was studied at SEVEN MONTHS in females and "
     "reports NO BONE LENGTH AT ALL, only thicker cortex and lower body weight. The question is "
     "open because nobody has asked it, not because the answer is hidden."),
    ("Q2  Do BH3 mimetics do anything to bone?",
     "ANSWERED - THE VOID IS REAL, AND IT CONVERGES WITH SOMETHING THIS ATLAS ALREADY FOUND. No "
     "bone length, no growth plate histology, no chondrocyte autophagy measurement for any BH3 "
     "mimetic in any species. AND ROUND 199 INDEPENDENTLY GRADED AT A THAT NO STUDY HAS EXAMINED "
     "p16-POSITIVE SENESCENCE OR SENOLYTIC CLEARANCE IN THE GROWTH PLATE. Navitoclax and ABT-737 "
     "are the canonical senolytics AND the patent's claimed BH3 mimetics. ONE MOLECULE CLASS, TWO "
     "INDEPENDENT RATIONALES REACHING IT FROM DIFFERENT DIRECTIONS, AND ZERO EXPERIMENTS."),
    ("Q3  What does FGFR3 inhibition do to autophagy in a normal chondrocyte?",
     "THE OVERACTIVITY END IS NOW THREE-DEEP AND THE NORMAL END IS STILL EMPTY. wang2015's title "
     "states the mechanism outright - FGFR3 INHIBITS AUTOPHAGY through decreasing the ATG12-ATG5 "
     "conjugate, delaying cartilage development in achondroplasia - agreeing with the patent's "
     "Example 2 and with the human COL9A1 rise. All three describe REMOVING A PATHOLOGICAL BLOCK. "
     "None describes reducing a normal signal, which is what this case does."),
    ("Q4  Is there a cell-level decomposition for navepegritide?",
     "NOT YET PUBLIC, AND THE DOCUMENT IS NOW IDENTIFIED AND DATED. The FDA review package for NDA "
     "219164 is NOT posted - the approval letter and label are up, every review-document filename "
     "pattern returns 404. The EU route is live but pending: Ascendis submitted the MAA to the EMA "
     "in OCTOBER 2025 and CHMP review is ongoing, so THE EPAR DOES NOT EXIST YET. That EPAR is the "
     "document that will answer this - the Voxzogo EPAR is exactly where the vosoritide zone "
     "measurements came from. ICCBH 2026 carried no preclinical abstract. THIS IS PENDING, NOT "
     "UNOBTAINABLE."),
    ("Q5  Does sustained CNP beat daily on the SPINE in a primate?",
     "ANSWERED INFERENTIALLY IN BOTH SPECIES, DIRECTLY IN NEITHER. Every axial readout that has "
     "been taken favours sustained exposure - mouse SPINE +11.3 against +25.0 per cent at the same "
     "daily dose, a 2.21-fold separation; monkey TAIL +3 against +9 per cent, a 3.0-fold "
     "separation and the largest of any endpoint in that study. NO PRIMATE SPINE MEASUREMENT "
     "EXISTS. Two axial readouts in two species agreeing in direction and magnitude is a strong "
     "inference and not a measurement."),
]
for q, a in items:
    print(f"    {q}")
    print(wrap(a, 8))
    print()

# ----------------------------------------------------------------------------- 6
head(6, "WHAT THIS OPENS")
for i, q in enumerate([
    "Has ANY growth plate been measured in a human with NORMAL FGFR3 under either an FGFR inhibitor",
    "  or a CNP agent? The transfer premise the whole stack rests on has never been checked in the",
    "  background it is being applied to.",
    "Does the erdafitinib paediatric series report bone age? A 19 cm/year velocity with a bone-age",
    "  denominator would settle whether the FGFR arm spends reserve the way the GH combination does.",
    "Would GH be worth adding at bone age 16 given it spends 1.3-1.6 bone-age years per year, or is",
    "  the arm that adds the most velocity also the one that closes the window fastest?",
    "Does the infigratinib achondroplasia mouse really enlarge the hypertrophic zone while REDUCING",
    "  hypertrophic cell number - which would be an h_term gain bought with FEWER cells, the best",
    "  possible assignment? Seen only in a secondary summary; the primary is JBMR 2024;39(6):765.",
], 1):
    print("      " + (f"{i}. {q}" if not q.startswith("  ") else f"   {q.strip()}"))
print()
rule()
