#!/usr/bin/env python3
"""
ROUND 187 - THE ABALOPARATIDE REGIMEN, AND A CORRECTION TO THIS ATLAS'S OWN ROUND-185 BENCHMARK.

Round 185 argued that "intermittent" is a ratio between the dosing interval and the chondrocyte's
clock, that a human chondrocyte cycles ~14x slower than a rat one, and that daily dosing is therefore
20-fold too frequent and drifting toward the harmful continuous arm. That argument is now
SUBSTANTIALLY WEAKENED by three facts, two of them from the TYMLOS label itself.

  (1) HALF-LIFE ~1 HOUR (label, Section 12.3). An 80 mcg subcutaneous dose is down to roughly 3 per
      cent of Cmax by five half-lives, so the exposure window is about 5-6 h in every 24 - a duty
      cycle of about 21-25 per cent, and that number is a property of the DRUG, not of the species.

  (2) "PRE-DOSE SERUM CALCIUM WAS SIMILAR TO BASELINE IN BOTH GROUPS" (label, Section 6.1). This is
      direct in-vivo human evidence that the pharmacodynamic effect of a daily dose FULLY RESOLVES
      within 24 hours. Daily dosing in a human is pulsatile by the only readout anyone has.

  (3) DAILY TERIPARATIDE AND ABALOPARATIDE ARE ANABOLIC IN HUMANS. If the species-scaling argument
      were right - human target cells are slow, so daily dosing is effectively continuous - then
      daily PTH1R agonism in a human should behave like continuous infusion and be CATABOLIC. It is
      not. It is the approved anabolic regimen with fracture-reduction data. That is the same drug,
      the same schedule and the same species, in the adjacent tissue where the intermittent/continuous
      inversion was originally described.

So the operative clock looks like the DRUG's exposure window, not the target cell's cycle time, and
the right invariant to match is EXPOSURE WINDOWS PER WEEK rather than pulses per cell cycle. That
invariant needs no half-life assumption for the rat and no cell-cycle estimate for either species:
ogawa2002 dosed FIVE DAYS A WEEK.

The residual uncertainty is not gone - see g_l12_which_clock_sets_intermittency_at_the_growth_plate -
but it now argues for hedging rather than for abandoning daily dosing.
"""

SUBJECT_KG = 60.0

# --- TYMLOS label, verified from the DailyMed SPL 2026-08-09 -------------------------------
LABEL = {
    "dose_ug": 80.0,              # 2.1 Recommended Dosage, once daily subcutaneous
    "half_life_h": 1.0,           # 12.3 Elimination
    "bioavailability": 0.36,      # 12.3, healthy women, 80 mcg dose
    "protein_binding": 0.70,      # 12.3
    "vd_L": 50.0,                 # 12.3
    "mw_da": 3961.0,              # 11 Description
    "homology_pthrp": 0.76,       # 11 Description - 76% to hPTHrP(1-34)
    "homology_pth": 0.41,         # 11 Description - 41% to hPTH(1-34)
    "hyperCa_pct": 3.0,           # 6.1, albumin-corrected Ca >=10.7 mg/dL at 4 h post-injection
    "hyperCa_placebo_pct": 0.1,
    "max_duration_y": 2.0,        # 2.3 Treatment Duration
    "trial_duration_mo": 18.0,    # 6.1 ACTIVE
}

# ogawa2002, the only wild-type longitudinal-growth experiment.
RAT = {"dose_ug_kg_day": 80.0, "days_per_week": 5.0, "weeks": 3.0, "km_rat_to_human": 6.2}


def banner(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


banner("STEP 1 - MATCH THE SCHEDULE THAT ACTUALLY WORKED")
print(f"""
  ogawa2002 dosed FIVE DAYS A WEEK for three weeks. That is the exposure pattern behind the only
  measured increase in the longitudinal growth rate of a normal animal.

  Matching it in a human needs no species scaling at all - it is five exposure windows per week
  against five. Both drugs clear in hours in both species, so the windows are comparable without
  assuming a rat half-life.

  {'regimen':32s} {'windows/wk':>11s} {'vs ogawa2002':>13s}""")
for label, dpw in [("abaloparatide daily, 7/7", 7.0),
                   ("abaloparatide 5 on / 2 off", 5.0),
                   ("twice weekly", 2.0),
                   ("weekly", 1.0)]:
    print(f"  {label:32s} {dpw:11.0f} {dpw/RAT['days_per_week']:12.2f}x")
print("""
  5-ON / 2-OFF IS AN EXACT MATCH. It is also the only option that preserves a genuine 48-hour
  washout every week, which is the cheap hedge against the round-185 model being right after all.""")

banner("STEP 2 - THE PER-PULSE DOSE. 80 mcg IS THE CEILING WITH HUMAN DATA BEHIND IT")
print(f"""
  80 mcg is both the approved dose and the TOP of the phase-2 dose range (20 / 40 / 80 mcg).
  There is no human pharmacokinetic or safety data above it for this molecule.

  For a {SUBJECT_KG:.0f} kg subject that is {LABEL['dose_ug']/SUBJECT_KG:.2f} mcg/kg per dose - close to the per-kilogram exposure
  of the postmenopausal trial population, so the fixed 80 mcg dose needs no weight adjustment.

  THE DOSE-LIMITING TOXICITY IS HYPERCALCAEMIA AND IT SCALES WITH PER-PULSE SIZE.
  Label: albumin-corrected serum calcium >= 10.7 mg/dL AT 4 HOURS post-injection occurred in
  {LABEL['hyperCa_pct']:.0f} per cent of treated patients against {LABEL['hyperCa_placebo_pct']:.1f} per cent on placebo. Two patients (0.2 per cent)
  discontinued for it. Pre-dose calcium stayed at baseline, so the excursion is transient.
  Escalating above 80 mcg is the one change that attacks the DLT directly, with no human data.""")

banner("STEP 3 - WHAT THE REGIMEN DELIVERS AGAINST THE RAT")
rat_wk = RAT["dose_ug_kg_day"] * RAT["days_per_week"]
hed_wk = rat_wk / RAT["km_rat_to_human"]
hed_total_wk = hed_wk * SUBJECT_KG
print(f"  ogawa2002 weekly       {rat_wk:8.0f} mcg/kg/week")
print(f"  human equivalent       {hed_wk:8.1f} mcg/kg/week  = {hed_total_wk:6.0f} mcg/week at {SUBJECT_KG:.0f} kg\n")
print(f"  {'regimen':32s} {'mcg/week':>9s} {'mcg/kg/wk':>10s} {'x below HED':>12s}")
for label, dpw in [("abaloparatide daily, 7/7", 7.0), ("abaloparatide 5 on / 2 off", 5.0)]:
    wk = LABEL["dose_ug"] * dpw
    print(f"  {label:32s} {wk:9.0f} {wk/SUBJECT_KG:10.2f} {hed_total_wk/wk:11.1f}x")
print(f"""
  THE RESIDUAL GAP IS REAL AND CANNOT BE CLOSED AT THE APPROVED PER-PULSE DOSE. 5-on/2-off sits
  about 9.7-fold below the body-surface-area-scaled rat exposure; going to 7/7 buys 40 per cent more
  and closes it only to 6.9-fold, at the cost of two exposure windows a week the rat never had.

  THAT TRADE IS NOT WORTH TAKING. The downside of the schedule being wrong is that this drug class
  INVERTS SIGN and shortens bone; the downside of 40 per cent less exposure is a proportionally
  smaller effect on an effect that is already modest. Asymmetric downside, so match the experiment.

  AND BSA SCALING IS A SAFETY CONVENTION, NOT A PHARMACODYNAMIC EQUIVALENCE. ogawa2002 ran a SINGLE
  dose chosen for maximal bone effect, not a titration against the growth plate. There is no
  dose-response, so the minimum effective dose is unknown and could be well below 80 mcg/kg/day. The
  9.7-fold figure is the distance to an arbitrary point, not to a threshold.""")

banner("STEP 4 - TIMING. FREE, AND THE ONE OPTIMISATION NOBODY HAS TRIED")
print(f"""
  Give it in the EVENING, at a consistent time, immediately before lying down.

  TWO INDEPENDENT REASONS CONVERGE.
  1. noonan2004, already in this atlas: implanted microtransducers in lambs show AT LEAST 90 PER
     CENT of tibial elongation occurs during RECUMBENCY, and almost none during standing or
     locomotion. With a ~1 h half-life the drug's window is about 5-6 h, so a bedtime dose lays the
     exposure directly over the early nocturnal growth period rather than over the part of the day
     when the plate is barely elongating.
  2. The label instructs administering TYMLOS where the patient can sit or lie down, because of
     orthostatic hypotension in the hours after injection. Bedtime satisfies that by construction.

  GRADE E. This is an inference from a lamb loading study and a drug half-life, not a tested
  hypothesis, and PTH is known to reset the cartilage circadian clock - so if it is done, the timing
  must be CONSISTENT rather than drifting. It costs nothing and it is the only free variable left.""")

banner("STEP 5 - MONITORING THAT ACTUALLY CHANGES THE DOSE")
print("""
  ALBUMIN-CORRECTED SERUM CALCIUM AT 4 HOURS POST-DOSE. This is the label's own detection window and
  the dose-limiting toxicity. Baseline, then at one month, then periodically.

  PRE-DOSE SERUM CALCIUM. This is the one that matters mechanistically rather than just for safety.
  The label's finding that pre-dose calcium stays at baseline is the evidence that each dose is a
  PULSE. If pre-dose calcium starts to drift upward, the exposure is no longer clearing between
  doses and the regimen has moved toward the continuous arm - which is the arm where this drug class
  shortens bone. That is a reason to lengthen the interval, not merely a safety flag.

  BONE AGE EVERY SIX MONTHS. Not on the label and specific to this use. The whole point is final
  height, and no one has ever measured whether PTH1R agonism accelerates skeletal maturation. If it
  advances bone age faster than it adds height, it is self-defeating - that is the duration term
  eating the yield term, and this atlas has been caught by exactly that trade before.

  CALCIUM AND VITAMIN D. The label directs supplementation if dietary intake is inadequate, and
  PTH1R agonism mobilises calcium, so this is not optional here.""")

banner("STEP 6 - INTERACTION WITH WHAT IS ALREADY IN THE STACK")
print("""
  ERDAFITINIB. xie2012 attributes intermittent PTH(1-34)'s rescue of achondroplastic mice partly to
  DOWNREGULATED FGFR3. If PTH1R agonism works partly by lowering FGFR3 signalling, then it and an
  FGFR inhibitor may be acting through a shared node and CANNOT BE ASSUMED ADDITIVE. Untested.

  GROWTH HORMONE. Round 183 established GH buys rate almost entirely by spending the resting pool
  faster - amplification 0.77. If abaloparatide turns out to do the same thing, the two stack in
  COST rather than in benefit, and that is the specific way this fails in a late case.

  VOSORITIDE. Independent axis, no known interaction, and it is the h_term agent while this is
  proposed as a flux agent. This is the one pairing the term decomposition actually supports.""")

banner("THE REGIMEN")
print(f"""
  ABALOPARATIDE 80 mcg SUBCUTANEOUS, ONCE DAILY, FIVE CONSECUTIVE DAYS PER WEEK, TWO DAYS OFF.
  Evening dose, consistent time, immediately before lying down. Periumbilical, rotating sites.
  Calcium and vitamin D replete. Duration bounded by the remaining growth window.

  WHY EACH PART:
    80 mcg      the approved dose and the top of the tested range - the ceiling with human data
    5 on / 2 off exactly reproduces ogawa2002's exposure pattern, and preserves a weekly washout
    evening     lays the ~5-6 h window over the nocturnal period when >90 per cent of elongation happens
    2 days off  the cheap hedge against the round-185 clock model being right after all

  WHAT THIS IS NOT. It is not a validated regimen. The molecule differs from the one that produced
  the only wild-type result - abaloparatide is {LABEL['homology_pthrp']:.0%} homologous to hPTHrP(1-34) and only {LABEL['homology_pth']:.0%} to
  hPTH(1-34), which is what ogawa2002 used. The exposure is about ten-fold below the BSA-scaled rat
  dose. Whether the growth-rate gain is amplification or faster pool consumption is unmeasured, and
  that is the question that turned growth hormone from an apparent yield agent into a pool-spending
  one. And the label states plainly that use is to be AVOIDED in patients with open epiphyses on
  osteosarcoma grounds - which is the reason no human growth data exists for any PTH1R agonist.
""")
