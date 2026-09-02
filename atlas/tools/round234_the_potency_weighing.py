#!/usr/bin/env python3
"""
ROUND 234 - the challenge: does erdafitinib's FGFR3 strength outweigh its FGFR1 cost?

The premise under test is that erdafitinib is significantly more potent at FGFR3 than the
FGFR3-selective agent, so that switching would trade away growth to buy safety.

THE PREMISE IS TESTABLE AND IT FAILS, ON THREE INDEPENDENT AXES. And then a fourth argument
makes the whole comparison moot. Everything below is sourced; the arithmetic is shown.

  [1] IS THERE AN FGFR3 ADVANTAGE?  in vitro, in vivo head-to-head, and in humans
  [2] WOULD IT MATTER IF THERE WERE?  the human growth response across the coverage range
  [3] WHAT DOES THE FGFR1 SIDE COST?
  [4] THE BMI FIGURE cross-checks the FDA's height number for erdaseries2025 patient 1
  [5] WHAT WOULD OVERTURN THIS
"""

from math import sqrt

BAR = "=" * 96
SUB = "-" * 96


def axis1():
    print(BAR)
    print("[1] IS ERDAFITINIB ACTUALLY STRONGER AT FGFR3? THREE READOUTS, NONE OF THEM SAYS YES")
    print(BAR)
    print("""
    AXIS A - IN VITRO POTENCY. The atlas holds Ba/F3 cellular FGFR3 IC50s of 1.35 nmol/L for
    erdafitinib and 1.75 nmol/L for dabogratinib (TYRA-300). THAT IS A 1.30-FOLD DIFFERENCE, which
    is inside the run-to-run variation of a cellular proliferation assay and is not a
    pharmacological distinction. The manufacturer's own peer-reviewed paper puts it plainly:
    dabogratinib has demonstrated SIMILAR IN VITRO POTENCY IN FGFR3-DRIVEN CELL LINES AS PAN-FGFR
    INHIBITORS. Its selectivity is 19-fold over FGFR2, 63-FOLD OVER FGFR1 and 55-fold over FGFR4.

    AXIS B - IN VIVO, HEAD TO HEAD, SAME MODEL, SAME EXPERIMENT, STATISTICALLY TESTED. UM-UC-14
    xenograft driven by an FGFR3 S249C activating mutation, tumour growth inhibition at 21 days:

        dabogratinib   6 mg/kg once daily ............  46%   (not significant)
        dabogratinib  12 mg/kg once daily ............  80%
        dabogratinib  18 mg/kg once daily ............  96%
        dabogratinib   3 mg/kg twice daily ...........  no TGI
        dabogratinib   6 mg/kg twice daily ...........  53%   (not significant)
        dabogratinib   9 mg/kg twice daily ...........  90%
        ERDAFITINIB 12.5 mg/kg TWICE DAILY ...........  91%

        dabogratinib 18 mg/kg once daily BEAT erdafitinib 12.5 mg/kg twice daily, P = 0.0244

    THE SELECTIVE AGENT WON, ON AN FGFR3-DRIVEN READOUT, IN A DIRECT COMPARISON, WITH A P VALUE.

    AXIS C - IN HUMANS, AND THIS ONE NEEDS NO PHARMACOKINETIC ASSUMPTION AT ALL. Both drugs have
    been given to people with FGFR3-altered metastatic urothelial carcinoma - a disease driven by
    the same receptor we are trying to inhibit. Response rate is a direct clinical readout of
    FGFR3 target engagement, and it is immune to every argument about protein binding:

        erdafitinib .... ORR 35.3%, median PFS 5.6 months, OS 12.1 months
                         serious AEs 41%; dose INTERRUPTION 68%, REDUCTION 53%,
                         PERMANENT DISCONTINUATION 21%
        dabogratinib ... 6 CONFIRMED PARTIAL RESPONSES IN 11 EVALUABLE PATIENTS = 54.5%
                         at dosages >= 90 mg once daily, with a very low frequency of
                         grade 3 treatment-related adverse events

    SO ON EVERY AXIS THAT HAS BEEN MEASURED, THE FGFR3-SELECTIVE AGENT IS AT LEAST AS GOOD AT
    FGFR3 AND BETTER TOLERATED. There is no FGFR3 advantage to weigh against the FGFR1 cost.
""")


def axis2():
    print(BAR)
    print("[2] AND IF THERE WERE AN ADVANTAGE IT WOULD BUY NOTHING - THE HUMAN CURVE IS FLAT")
    print(BAR)
    # free multiples of each drug's own Ba/F3 FGFR3 cellular IC50, held from round 213
    erda = {3: 1.72, 5: 2.86, 7: 4.01, 8: 4.58, 9: 5.16}
    tyra = {40: 0.95, 90: 4.33}
    print("    Free steady-state average as a multiple of each drug's OWN FGFR3 cellular IC50")
    print("    (erdafitinib fu 0.3%, IC50 1.35 nmol/L; dabogratinib fu ~1.0%, IC50 1.75 nmol/L)\n")
    print("        erdafitinib   " + "   ".join(f"{d} mg={v:.2f}x" for d, v in erda.items()))
    print("        dabogratinib  " + "   ".join(f"{d} mg={v:.2f}x" for d, v in tyra.items())
          + f"   120 mg={tyra[90]*120/90:.2f}x (linear extrapolation)")
    print(f"""
    EVEN TAKEN AT FACE VALUE THE GAP IS SMALL. Erdafitinib's LABEL MAXIMUM of 9 mg gives {erda[9]:.2f}x.
    Dabogratinib at 90 mg gives {tyra[90]:.2f}x, and doses through 100 mg once daily are cleared with the
    dose range explored to 120 mg - which extrapolates to {tyra[90]*120/90:.2f}x, ABOVE ERDAFITINIB'S CEILING.
    And erdafitinib's 9 mg is not reachable in the patients who matter: the three quantified
    children took 3, 5 and 7 mg, and the 8-to-9 mg step is triggered by a SERUM PHOSPHATE reading.

    NOW THE PART THAT SETTLES IT. What did a rise in free FGFR3 coverage actually buy in a human?
    Round 228 unspliced the two quantified children. Between them they span 1.72x to 4.01x - a
    2.33-fold span of the axis - and their midpoints differ 1.50-fold:
""")
    pts = [("erdaseries2025 patient 1 / FDA case 4", "5 mg then 3 mg", erda[3], erda[5], 19.6),
           ("erdachild2024 / FDA case 3", "7 mg then 5 mg", erda[5], erda[7], 19.1)]
    print(f"    {'child':<40}{'dose':<16}{'x IC50 range':<16}{'cm/year':>9}")
    for name, dose, lo, hi, v in pts:
        print(f"    {name:<40}{dose:<16}{f'{lo:.2f} - {hi:.2f}':<16}{v:>9.1f}")
    lo_mid, hi_mid = (erda[3] + erda[5]) / 2, (erda[5] + erda[7]) / 2
    print(f"""
    Midpoint coverage {lo_mid:.2f}x against {hi_mid:.2f}x - a {hi_mid/lo_mid:.2f}-fold rise on the midpoints, across a
    span of {erda[3]:.2f}x to {erda[7]:.2f}x overall - and the velocities are 19.6 and 19.1 cm/year, a difference of
    {abs(19.6-19.1)/19.6*100:.1f} PER CENT IN THE WRONG DIRECTION.

    THE HUMAN FGFR3 GROWTH RESPONSE IS SATURATED AT THE BOTTOM OF THE CLINICAL RANGE. Somewhere at
    or below about 2x the cellular IC50, more FGFR3 engagement stops buying height. EVERY AGENT
    UNDER DISCUSSION IS ALREADY PAST THAT POINT AT ITS LOWEST CLINICAL DOSE. So the FGFR3 axis is
    not where the remaining height is, and a 1.3-fold potency difference on that axis is worth
    nothing even if it were real.

    THIS ALSO CORRECTS THIS ATLAS. Round 213 built a growth-versus-coverage curve reading "1.72x
    gave about 10 cm/year, 4.01x gave 19.06 cm/year - a 2.3-fold rise in free concentration for a
    1.9-fold rise in velocity". The 10 cm/year child was assigned 3 mg. THAT CHILD'S DOSE IS STATED
    NOWHERE - erdaseries2025 gives a dose for patient 1 only, confirmed by re-reading the full text
    this round - and round 228 established the 19.6 cm/year figure for the child who actually took
    3 mg. THE RISING CURVE WAS THE SPLICED ANCHOR AGAIN, AND UNSPLICED IT IS FLAT.
""")


def axis3():
    print(BAR)
    print("[3] WHAT THE FGFR1 SIDE COSTS, WHICH IS THE ONLY SIDE WITH ANYTHING ON IT")
    print(BAR)
    print("""
        hyperphosphataemia, agents COVERING FGFR1 ...... erdafitinib ~75%, Debio1347 4/5 = 80%
        hyperphosphataemia, agent SPARING FGFR1 ........ TYRA-300 13%
        dabogratinib selectivity, FGFR3 over FGFR1 ..... 63-fold
        the receptor that drives the dose UP ........... FGFR1 - the label escalates 8 to 9 mg
                                                         when phosphate is below 5.5 mg/dL, and
                                                         41% of patients were escalated on that basis
        commonest cause of dose INTERRUPTION ........... hyperphosphataemia, 24%
        what the phosphate arm produces ................ soft tissue mineralization, cutaneous
                                                         calcinosis, non-uremic calciphylaxis,
                                                         vascular calcification (label section 5.2)
        what the phosphate arm produces in genetics .... slipped capital femoral epiphysis, twice
                                                         independently, in FGF23 loss - AND NO HEIGHT
        what ends treatment in the five FDA children ... all five discontinued, three had surgery

    AND THE COST IS PAID IN THE ONE CURRENCY THAT STILL BUYS HEIGHT. Rounds 228 and 229 established
    that DURATION is the lever - flat dose-response, largest gain on the longest exposure. The FGFR1
    arm is the commonest reason the drug is interrupted, and the mechanical failures it contributes
    to are why every one of the five FDA children stopped permanently. SPENDING FGFR1 COVERAGE BUYS
    NO HEIGHT AND SHORTENS THE ONLY VARIABLE THAT DOES.
""")


def bmi_check():
    print(BAR)
    print("[4] THE SUPPLIED BMI FIGURE INDEPENDENTLY CROSS-CHECKS THE FDA'S HEIGHT NUMBER")
    print(BAR)
    print("""
    erdaseries2025's Supplementary Figure 1 plots BMI for both patients with treatment start and
    stop marked, and states that the BMI DECREASE WAS MAINLY CAUSED BY INCREASE OF BODY HEIGHT.
    Patient 1 starts erdafitinib at about age 14.0 with BMI near 24.5 and reaches a nadir near 21.3
    at about age 14.4, when treatment stops; BMI then recovers to about 25 by age 15.5.

    BMI = weight / height^2, so at CONSTANT WEIGHT a fall in BMI is exactly a rise in height:
""")
    b0, b1 = 24.5, 21.3
    ratio = sqrt(b0 / b1)
    print(f"        BMI {b0} -> {b1}  implies height x {ratio:.4f}, i.e. +{(ratio-1)*100:.2f}% at constant weight\n")
    print(f"    {'starting height (cm)':<26}{'implied gain (cm)':>20}")
    for h in (140, 150, 155, 160, 165):
        print(f"    {h:<26}{h*(ratio-1):>20.1f}")
    print(f"""
    THE FDA REPORTS 9.8 cm OVER 6 MONTHS FOR THIS CHILD, and the BMI nadir sits about 5 to 6 months
    after treatment start. A boy of 140 to 155 cm - which is what a GH-treated panhypopituitary
    13.8-year-old plausibly is - gives an implied gain of {140*(ratio-1):.1f} to {155*(ratio-1):.1f} cm at constant weight.
    THE TWO INDEPENDENT SOURCES AGREE, with the small excess absorbed by the weight gain the caption
    already concedes is not zero.

    THIS IS A CONSISTENCY CHECK AND NOT A MEASUREMENT. The BMI values are read off a printed chart
    to about +/- 0.3 units, the starting height is not reported anywhere, and the caption says
    "mainly" rather than "entirely". What it establishes is that the FDA's 9.8 cm is not a
    transcription error, which matters because round 228's flat dose-response rests on it.
""")


def limits():
    print(BAR)
    print("[5] WHAT WOULD OVERTURN THIS, STATED PLAINLY")
    print(BAR)
    print("""
    A TUMOUR IS NOT A GROWTH PLATE. Every potency comparison above is an FGFR3-driven ONCOLOGY
    readout - a Ba/F3 line, a bladder xenograft, a urothelial response rate. Killing an
    FGFR3-mutant tumour cell and driving a chondrocyte through its proliferative programme are
    different jobs, and CARTILAGE PENETRATION IS UNMEASURED FOR BOTH DRUGS IN EVERY SPECIES. A
    molecule could win all three axes above and still reach the physis less well.

    THE TUMOURS CARRY ACTIVATING FGFR3 MUTATIONS AND THIS CASE DOES NOT. Dabogratinib was designed
    against oncogenic mutants and gatekeeper resistance, which is a reason to ask whether it
    engages WILD-TYPE FGFR3 as well. THE ATLAS ALREADY HOLDS THE ANSWER AND IT IS YES - round 208
    records TYRA-300 raising nasoanal and tail length in WILD-TYPE C57BL/6J mice dosed from 4 to 8
    weeks. Wild-type, whole animal, length. That is the right control and it exists.

    THE CLINICAL COMPARISON IS CROSS-TRIAL. 54.5% is 6 responses in 11 phase-I patients; 35.3% is a
    phase-III population with different prior lines. Small numerator, no randomisation, and phase-I
    response rates are routinely flattered. IT IS EVIDENCE THAT FGFR3 ENGAGEMENT IS NOT INFERIOR,
    NOT EVIDENCE THAT IT IS SUPERIOR.

    THE FLAT HUMAN CURVE IS TWO CHILDREN, one of whom was also receiving growth hormone.

    AND THE DECISIVE UNCERTAINTY IS UNCHANGED BY ANY OF THIS. It was never about potency. NO HUMAN
    WITH A NORMAL FGFR3 HAS EVER BEEN GIVEN AN FGFR3-SELECTIVE INHIBITOR AND MEASURED, and no trial
    anywhere is scheduled to do it - every dabogratinib study is adults with cancer or children aged
    3 to 10 with achondroplasia. THAT is the gap, and no amount of potency arithmetic closes it.
""")
    print(BAR)


if __name__ == "__main__":
    axis1()
    axis2()
    axis3()
    bmi_check()
    limits()
