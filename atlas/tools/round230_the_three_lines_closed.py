#!/usr/bin/env python3
"""
ROUND 230 - closing the three lines round 229 left open, and two corrections to round 229 itself.

  LINE 1  the reserve question: is the growth bought or borrowed? Round 228 established that no
          on-treatment bone age exists. Round 227 offered a mechanism by which the ONE qualitative
          observation that does exist - "physeal widening without apparent progression of bone
          maturation" - could be an artefact. THAT MECHANISM RUNS THE WRONG WAY, and a human
          cohort in the mirror-image metabolic state measures the direction.

  LEAD A  does the isolated phosphate arm carry a stature phenotype? Answered by the NIH natural
          history cohort, with CORR-233's own admissibility test applied to the silence.

  LEAD B  do phosphate and growth dissociate in treated humans? Answered in BOTH directions, from
          two patients already in this atlas's bibliography.

  AND TWO CORRECTIONS TO ROUND 229, both from one table in brizini2024 that names the drug each
  farouk2023 patient received.

No new numbers are invented here. Everything is either quoted from a source or arithmetic on
quoted values, and the arithmetic is shown.
"""

BAR = "=" * 96
SUB = "-" * 96


def line1():
    print(BAR)
    print("[LINE 1] THE MINERALISATION ARTEFACT RUNS THE WRONG WAY - round 227's mechanism is refuted")
    print(BAR)
    print("""
    WHAT ROUND 227 CLAIMED. A Greulich-Pyle bone age scores the appearance, size and fusion of
    MINERALISED ossification centres. Therefore an agent that IMPAIRS MINERALISATION would present
    as an unadvanced bone age while preserving no proliferative reserve whatever. On that reading,
    erdaseries2025's "atypical physeal widening without apparent progression of bone maturation"
    is an instrument artefact rather than a biological finding, and the growth is borrowed.

    THE MECHANISM REQUIRES HYPOMINERALISATION. That is not a quibble - it is the whole mechanism.
    Nothing else in the argument does any work.

    WHAT THE DRUG CLASS ACTUALLY DOES TO MINERAL, from five independent directions:
""")
    rows = [
        ("hyperphosphataemia incidence",
         "~75% of erdafitinib patients, ~4% grade 3 (held since round 213). PHOSPHATE IS RAISED, NOT LOWERED"),
        ("the radiographic finding itself",
         "erdaseries2025 reports METAPHYSEAL SCLEROSIS appearing with treatment and normalising after "
         "the halt. Sclerosis is INCREASED radiodensity - more mineral, not less"),
        ("ectopic calcification, pharmacological",
         "calcinosis cutis with selective FGFR inhibitors (ghimire2025); calciphylaxis with "
         "pemigatinib (chandana2024) and with futibatinib (slaymaker2025). THREE MOLECULES, "
         "MINERAL DEPOSITED WHERE IT SHOULD NOT BE"),
        ("ectopic calcification, genetic mirror",
         "those are the defining lesions of hyperphosphataemic familial tumoral calcinosis, which is "
         "genetic loss of the same signalling. The pharmacological and genetic phosphate arms "
         "converge on the SAME TISSUE PHENOTYPE in humans"),
        ("the absent finding",
         "a 104-result sweep for rickets, osteomalacia, metaphyseal lucency or hypomineralisation "
         "under any FGFR inhibitor returns NOT ONE CASE. The class has no demineralisation phenotype"),
    ]
    for k, v in rows:
        print(f"    {k}")
        print(f"        {v}\n")
    print("""    SO THE ARTEFACT ROUND 227 PROPOSED IS NOT AVAILABLE. The drug does not impair mineralisation;
    it raises phosphate and deposits mineral, including in places it does not belong.

    AND THE HUMAN MIRROR MEASURES THE DIRECTION, WHICH IS WHY THIS IS A REFUTATION RATHER THAN A
    QUIBBLE. soto2026 studied bone age in X-linked hypophosphataemia - chronic HYPOphosphataemia,
    impaired skeletal mineralisation, rickets - and states the artefact mechanism explicitly as a
    known concern: a delay in the appearance of epiphyseal bone centres has been described in
    rickets and may affect the interpretation of skeletal age. THEN IT MEASURES IT:

        56 children with XLH, four blinded readers, two methods
        bone age delay (chronological age minus bone age):   MALES 1.2 +/- 1.0 years
                                                             FEMALES 0.4 +/- 1.0 years   (p < .05)
        58% of males delayed 1-2 years; 11% delayed more than 2 years

    ROUND 227'S MECHANISM IS REAL. IT BELONGS TO THE OPPOSITE METABOLIC STATE. Impaired
    mineralisation does produce a falsely young bone age, by about a year, in humans - in the
    HYPOphosphataemic disease. Erdafitinib patients are HYPERphosphataemic with sclerotic
    metaphyses, so the correction runs the other way or not at all.

    WHAT THIS DOES AND DOES NOT SETTLE.
      IT DOES remove the only mechanism ever proposed for discounting the one maturation
        observation that exists. On the evidence available, "widening without apparent progression
        of bone maturation" should be read as what it says.
      IT DOES NOT produce a bone age. Round 228's closure stands: nobody has measured one. This is
        an argument about which of two readings is admissible, not a measurement, and it is graded
        as such.

    A SECOND THING soto2026 GIVES FREE, and it matters for how this atlas plans. In the same XLH
    children - a metabolic bone disease with rickets, deformity and surgery - bone-age-based ADULT
    HEIGHT PREDICTION still landed within about two inches, the range accepted in healthy children:
    4 males, achieved 171.2 +/- 5.3 cm against Bayley-Pinneau 176.3 +/- 11.7 and Tanner-Whitehouse
    173.0 +/- 6.8; 15 females, achieved 155.9 +/- 5.2 against 156.0 +/- 6.8 Bayley-Pinneau.
    SO A BONE AGE, IF ANYONE EVER TOOK ONE, WOULD STILL BE INTERPRETABLE UNDER A METABOLIC BONE
    DISEASE. The reason this question is open is not that the instrument is broken.
""")


def leadA():
    print(BAR)
    print("[LEAD A] THE ISOLATED PHOSPHATE ARM HAS NO STATURE PHENOTYPE - and the source could have said")
    print(BAR)
    print("""
    THE SETUP. Hyperphosphataemic familial tumoral calcinosis is loss of FGF23 signalling by FGF23,
    GALNT3 or KL mutation: LIFELONG hyperphosphataemia, from birth, at full effect, WITHOUT any
    inhibition of FGFR3 in cartilage - because FGF23 acts through FGFR1-Klotho in the kidney. It is
    erdafitinib's phosphate arm running alone for a whole childhood.

    ROUND 229 CLAIMED IT CARRIES NO HEIGHT, ON TWO CASE REPORTS AND A REVIEW'S FEATURE LIST. That
    is an argument from silence, and CORR-233 - written the same round - says an absence in a source
    is evidence ONLY IF THE SOURCE WAS IN A POSITION TO RECORD THE PRESENCE. Two case reports written
    by orthopaedic teams do not pass that test.

    ramnitz2016 PASSES IT. The NIH natural-history cohort of FTC/HHS, evaluated under protocol with
    biochemistry, DXA of spine, hip and radius, cardiac CT, dental radiographs and skeletal survey.

      IT MEASURED HEIGHT. The paper computes HEIGHT-ADJUSTED BMD Z-SCORES for subjects under 20.
        You cannot height-adjust without heights. The measurement was made.
      IT WAS HUNTING FOR NEW PHENOTYPES AND SAID SO. It reports as previously undescribed:
        heterotopic ossification, submucosal calcification of the large intestine, destruction of a
        shoulder joint to the point of ankylosis, and destruction of the ULNAR GROWTH PLATE.
      AND IT REPORTS NO STATURE OR GROWTH ABNORMALITY ANYWHERE.

    A group that publishes gut-wall calcification as a novel finding would not have omitted tall
    stature or accelerated growth. THE SILENCE IS ADMISSIBLE.

    AND THE ONE GROWTH-PLATE LESION IN THE COHORT POINTS THE OTHER WAY. Subject FTC8 had growth
    plate obliteration BY TUMORAL CALCINOSIS INVADING IT, with ULNAR SHORTENING. Where the phosphate
    arm touches a physis, it destroys it locally and the bone ends up SHORTER.

    WITH THE TWO SLIPPED EPIPHYSES ALREADY HELD - kashayichowdoj2025, a 9-year-old girl with a
    GALNT3 mutation; reddy2026, a 13-year-old boy with an FGF23 mutation and generalised
    osteosclerosis - THE ISOLATED PHOSPHATE ARM'S SKELETAL LEDGER READS:

        slipped capital femoral epiphysis .................. YES, twice, independently
        osteosclerosis and hyperostosis ................... YES
        pathological fracture ............................. YES
        ectopic and periarticular calcification ........... YES, definitionally
        local destruction of a growth plate ............... YES, with SHORTENING
        tall stature or accelerated linear growth ......... NOT REPORTED, in a cohort that
                                                            measured heights and hunted phenotypes

    LEAD A IS CLOSED. THE PHOSPHATE ARM CARRIES THE MECHANICAL FAILURE AND NONE OF THE HEIGHT.
""")


def leadB():
    print(BAR)
    print("[LEAD B] IN TREATED HUMANS, PHOSPHATE AND GROWTH DISSOCIATE IN BOTH DIRECTIONS")
    print(BAR)
    print("""
    The genetic argument says phosphate is not NECESSARY for the height. Two treated children,
    both already in this atlas's bibliography, say the same thing from inside the drug - and one of
    them says phosphate is not SUFFICIENT either.

    HIGH PHOSPHATE, NO GROWTH. brizini2024's patient - FDA case 1 - developed hyperphosphataemia at
    FOUR WEEKS "requiring chelation", and slipped a capital femoral epiphysis at twelve. On growth
    the paper is explicit rather than silent: it states that it did NOT see increased growth
    velocity in this patient, height sitting between the 25th and 50th centile. THE MECHANICAL
    FAILURE ARRIVED IN FULL WITH NO HEIGHT ATTACHED TO IT.

    GROWTH WHILE PHOSPHATE FELL. erdaseries2025 patient 1, serum phosphate in mmol/L against a
    reference range of 1.28-1.82:

        pre-erdafitinib ............... 2.47   RAISED - and this is BEFORE the drug
        3 months on erdafitinib ....... 1.88   raised, but LOWER than his own baseline
        6 months on erdafitinib ....... 2.01   raised, still LOWER than his own baseline
        2 months after stopping ....... 1.81   normal

    The dramatic growth spurt happened across the middle two columns - WHILE HIS PHOSPHATE WAS
    BELOW ITS OWN PRE-TREATMENT VALUE. His IGF-1 SDS fell over the same window, -0.04 to -1.4, and
    his testosterone was unmeasurable throughout at Tanner 1. So the growth ran with phosphate
    down, IGF-1 down and sex steroid absent.

    WHAT THE COHORT ADDS: NOTHING, AND THAT IS WORTH SAYING. farouk2023 reports hyperphosphataemia
    in 7 of 7 and growth in 7 of 7. WITH NO VARIANCE IN THE EXPOSURE THERE IS NO CORRELATION TO
    READ. The cohort cannot adjudicate this and should not be cited as if it could.

    SO: PHOSPHATE IS NEITHER NECESSARY NOR SUFFICIENT FOR THE HEIGHT, AND IS SUFFICIENT FOR THE SLIP.

    THE CAVEATS, STATED. Two patients. brizini's child had only twelve weeks of exposure, which the
    authors themselves offer as the explanation for his flat growth, and he was obese. Patient 1's
    2.47 is a single pre-treatment value with no replicate, and growth hormone - which he was
    receiving at 16 microgram/kg/day - itself raises tubular phosphate reabsorption, which is the
    likeliest reason his baseline was high in the first place. NEITHER CHILD IS AN EXPERIMENT.
    What they jointly rule out is the strong form: that the hyperphosphataemia is how the height
    is bought.

    AND THE ACTION THAT FOLLOWS IS NOT THE ONE ROUND 229 PROPOSED.
""")
    print(SUB)
    print("""    Round 229 said: bolt phosphate binders onto erdafitinib. That is still reasonable and still
    nearly free. BUT THE STRUCTURAL VERSION IS BETTER AND THIS ATLAS ALREADY HOLDS ITS NUMBERS.

    FGF23 SIGNALS THROUGH FGFR1. The hyperphosphataemia is an FGFR1 effect, which this atlas
    established at round 212. So the phosphate arm is not an unavoidable cost of inhibiting FGFR3 -
    IT IS THE PRICE OF INHIBITING FGFR1 ALONGSIDE IT. Held incidences:

        erdafitinib   pan-FGFR1-4       hyperphosphataemia ~75%   (~4% grade 3)
        TYRA-300      FGFR3-SELECTIVE   hyperphosphataemia   13%

    A SIX-FOLD REDUCTION IN THE ARM THAT CARRIES THE FAILURE AND NONE OF THE HEIGHT.

    AND THE HUMAN GENETICS SAYS THE SWITCH COSTS NOTHING ON THE OTHER SIDE. The one statement that
    survived the retraction of this atlas's receptor ledger (CORR-046, CORR-147, CORR-217) is that
    FGFR3 spans about 65 cm of human stature while FGFR1 AND FGFR4 HAVE NO HUMAN STATURE PHENOTYPE.
    Dropping FGFR1 and FGFR4 coverage should therefore drop the phosphate arm without dropping height.

    WHY THIS IS THE MOST VALUABLE THING IN THE ROUND. Rounds 228 and 229 established that the lever
    is DURATION, not dose - flat from 3 to 7 mg, largest gain on the longest exposure. And what ends
    the exposure is precisely the mechanical failure: ALL FIVE FDA CASES DISCONTINUED PERMANENTLY
    AND THREE REQUIRED SURGERY. REMOVING THE TERMINATOR IS THEREFORE WORTH MORE THAN RAISING THE
    DOSE, because the terminator is what caps the only variable that still buys height.
""")


def corrections():
    print(BAR)
    print("[CORRECTIONS TO ROUND 229] one table in brizini2024 fixes two things I got wrong yesterday")
    print(BAR)
    print("""
    brizini2024 carries a literature-review table of every published SCFE-on-FGFR-TKI case, WITH THE
    DRUG AND THE DURATION FOR EACH. Transcribed:

      1)  8/F   pilomyxoid astrocytoma, optic pathway   FGFR1 mut       SCFE b/l, AVN, fractures   9 mo   Debio1347
      2) 14/M   rosette-forming glioneuronal, cerebellum FGFR3-TACC3    SCFE, OCD, coxa valga     40 mo   Debio1347
      3) 12/M   diffuse brainstem glioma                FGFR2-VPS35     SCFE, fractures            5 mo   ERDAFITINIB
      4) 13/M   low-grade astrocytoma, optic chiasm     FGFR1-TKD-ITD   SCFE                       3 mo   ERDAFITINIB

    Rows 1, 2 and 3 are farouk2023 subjects 2, 3 and 6. Row 4 is brizini's own patient.

    CORRECTION ONE, AND IT IS THE HEADLINE OF ROUND 229. SUBJECT 3 WAS ON DEBIO1347, NOT ERDAFITINIB.
    The 40-month, +2.43 SD, 83rd-to->99.9th-centile patient - the closest human analogue to this case
    that exists - took an FGFR1-3 SELECTIVE inhibitor. Round 229 named both drugs in its methods and
    then framed him throughout as evidence about the agent in this stack. He is not.

      WHAT THIS COSTS: erdafitinib no longer owns the largest human growth response on record, and
        the longest exposure on record is not an erdafitinib exposure either.
      WHAT IT BUYS, AND IT IS MORE THAN IT COSTS: THE LARGEST HUMAN GROWTH RESPONSE EVER RECORDED
        CAME FROM AN AGENT THAT DOES NOT TOUCH FGFR4 AT ALL. Combined with the FGFR1 argument above,
        the height travels with FGFR3 and the class effect does not need the pan coverage. That is
        an argument FOR narrowing the molecule, made by the best data point in the field.

    CORRECTION TWO, TO CORR-233, WHICH IS ONE DAY OLD. I wrote that brizini2024 "never measured
    serial height at all". IT DID, AND IT SAYS SO: the authors state they did not see increased
    growth velocity in their patient, with height between the 25th and 50th centile. I asserted a
    source had not looked, without checking - WHICH IS THE EXACT ERROR CORR-233 WAS WRITTEN ABOUT,
    committed in the sentence that announced the rule.

    SO THE DISSOCIATION IS NOT WHOLLY DEAD, AND THE SURVIVING FORM IS INFORMATIVE. Of round 228's
    "three children", one was a double count and one grew +1.02 SD. THE THIRD IS REAL: brizini's
    patient failed mechanically with no growth. His exposure was TWELVE WEEKS.

    WHICH SUPPORTS THE DURATION THESIS RATHER THAN UNDERCUTTING IT. Set the two clocks side by side:

        time to slip, FDA five cases ............. median 137 days, range 84 to 274
        brizini's slip ........................... 84 days, with NO measurable height gain
        farouk subject 5, 5 months ............... +0.36 SD only
        farouk subject 6, 5 months ............... +1.02 SD, and he slipped at ~137 days
        farouk subject 3, 40 months .............. +2.43 SD

    THE FAILURE HAS A SHORTER LATENCY THAN THE BENEFIT. A slip can arrive at twelve weeks with
    nothing banked; the large gains need a year and upward. THAT IS THE WORST POSSIBLE SHAPE FOR
    THIS STACK, and it is exactly why the phosphate arm matters: every month bought by removing an
    avoidable cause of early discontinuation is a month spent on the part of the curve that pays.
""")


def opens():
    print(BAR)
    print("[WHAT OPENS] four questions, and none of them is rhetorical")
    print(BAR)
    print("""
    ONE - DOES AN FGFR3-SELECTIVE INHIBITOR GROW A HUMAN WITH A NORMAL FGFR3? This is now the
    load-bearing question for the whole recommendation above, and it is not answered. TYRA-300's
    length data is in MICE (round 208, wild-type C57BL/6J). Its human programme is adults with
    cancer, where nobody is growing, plus achondroplasia, where FGFR3 is mutant. NO HUMAN WITH A
    NORMAL FGFR3 HAS BEEN GIVEN AN FGFR3-SELECTIVE INHIBITOR AND MEASURED. Every human growth
    response on record comes from a pan-FGFR or FGFR1-3 agent.

    TWO - HOW MUCH OF SUBJECT 3'S RESPONSE WAS FGFR1? Debio1347 covers FGFR1, 2 and 3; TYRA-300
    covers FGFR3. If any part of the height came from FGFR1, narrowing the molecule trades height
    for safety rather than getting both. The human-genetics anchor says FGFR1 has no stature
    phenotype, which argues no - but that is loss-of-function genetics, and pharmacological
    inhibition of a receptor with no LOF phenotype can still do something in a growing plate.

    THREE - IS DEBIO1347 OBTAINABLE, AND WHAT DOSE DID SUBJECT 3 TAKE? He is the best data point in
    the field and this atlas does not know his dose, his schedule, or whether the compound still
    exists. farouk2021 is the parent study and its full text could not be retrieved.

    FOUR - DOES PHOSPHATE CONTROL ACTUALLY EXTEND EXPOSURE? The whole value of the phosphate
    argument is that it buys months. Nobody has reported time-on-drug against phosphate management
    in any FGFR-TKI series, and the FDA's five cases record the discontinuations without recording
    what was tried first.
""")
    print(BAR)


if __name__ == "__main__":
    line1()
    leadA()
    leadB()
    corrections()
    opens()
