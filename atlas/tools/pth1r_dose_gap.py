#!/usr/bin/env python3
"""
ROUND 184 - HOW FAR IS THE APPROVED PTH1R DOSE FROM THE ONE THAT LENGTHENED A NORMAL RAT?

ogawa2002 is the only experiment this programme has found in which an agent RAISED the
longitudinal growth rate of a NORMAL, normally-loaded, growing animal. The dose it used is the
number that decides whether the finding is reachable with an approved drug or not, so it is
computed here rather than asserted.

Conversion is the FDA's body-surface-area method (Guidance for Industry, Estimating the Maximum
Safe Starting Dose in Initial Clinical Trials, 2005): human equivalent dose = animal dose divided
by the species Km ratio. Rat to human divides by 6.2. This is a SCALING CONVENTION for first-in-
human safety, not a pharmacological equivalence, and it is used here only to put the two doses on
one axis.
"""

RAT_DOSE_UG_KG_DAY = 80.0        # ogawa2002: hPTH(1-34), 5 days/week for 3 weeks, 6-week-old rats
RAT_DAYS_PER_WEEK = 5.0
KM_RAT_TO_HUMAN = 6.2            # FDA BSA conversion factor

SUBJECT_KG = 60.0                # adolescent, order-of-magnitude only

APPROVED = {
    "teriparatide (Forteo)": 20.0,      # micrograms/day subcutaneous, osteoporosis
    "abaloparatide (Tymlos)": 80.0,     # micrograms/day subcutaneous, osteoporosis
}
# Paediatric hypoparathyroidism replacement dosing, the only paediatric exposure that exists.
PAED_REPLACEMENT_UG_KG_DAY = (0.5, 1.0)


def main():
    print("=" * 76)
    print("THE DOSE THAT WORKED, IN A NORMAL ANIMAL")
    print("=" * 76)
    hed_per_kg = RAT_DOSE_UG_KG_DAY / KM_RAT_TO_HUMAN
    hed_total = hed_per_kg * SUBJECT_KG
    weekly_rat = RAT_DOSE_UG_KG_DAY * RAT_DAYS_PER_WEEK
    print(f"  ogawa2002 rat dose          {RAT_DOSE_UG_KG_DAY:6.1f} ug/kg/day, "
          f"{RAT_DAYS_PER_WEEK:.0f} d/wk  ({weekly_rat:.0f} ug/kg/week)")
    print(f"  FDA BSA conversion          divide by {KM_RAT_TO_HUMAN}")
    print(f"  human equivalent dose       {hed_per_kg:6.2f} ug/kg/day")
    print(f"  for a {SUBJECT_KG:.0f} kg subject         {hed_total:6.0f} ug/day on the same 5-days-a-week schedule")

    print("\n" + "=" * 76)
    print("AGAINST WHAT IS APPROVED")
    print("=" * 76)
    print(f"  {'agent':26s} {'ug/day':>8s} {'ug/kg/day':>11s} {'HED is this many x':>20s}")
    for name, dose in APPROVED.items():
        print(f"  {name:26s} {dose:8.0f} {dose/SUBJECT_KG:11.2f} {hed_total/dose:19.1f}x")

    lo, hi = PAED_REPLACEMENT_UG_KG_DAY
    print(f"\n  paediatric hypoparathyroid replacement, the only paediatric exposure that exists:")
    print(f"    {lo}-{hi} ug/kg/day = {lo*SUBJECT_KG:.0f}-{hi*SUBJECT_KG:.0f} ug/day for this subject"
          f"  ->  HED is {hed_total/(hi*SUBJECT_KG):.0f}-{hed_total/(lo*SUBJECT_KG):.0f}x that")

    print("\n" + "=" * 76)
    print("READ THIS BEFORE USING THE NUMBER")
    print("=" * 76)
    print(f"""
  THE GAP IS REAL AND IT IS THE MAIN QUANTITATIVE OBJECTION TO THIS CANDIDATE. The dose that
  raised longitudinal growth rate in a normal rat is, human-equivalent, about {hed_total/APPROVED['abaloparatide (Tymlos)']:.0f}x the approved
  abaloparatide dose and about {hed_total/APPROVED['teriparatide (Forteo)']:.0f}x the approved teriparatide dose.

  FOUR THINGS THAT CUT AGAINST TREATING IT AS FATAL, AND ONE THAT DOES NOT.
  1. ogawa2002 ran ONE dose. There is no dose-response, so the minimum effective dose is unknown
     and could be far below 80 ug/kg/day. Nobody has looked.
  2. BSA scaling is a safety convention for first-in-human starting doses, not a statement about
     where a pharmacodynamic effect appears. It routinely over- and under-predicts.
  3. Abaloparatide is dosed 4x higher than teriparatide and is a PTHrP analogue - the growth
     plate's own ligand - which shortens the gap and improves the mechanistic match at once.
  4. The osteoporosis dose was titrated to a BONE endpoint in adults with closed plates. Nobody
     has ever titrated a PTH1R agonist to a GROWTH PLATE endpoint in anybody.
  5. WHAT DOES NOT CUT AGAINST IT: the human paediatric exposure that exists is REPLACEMENT dosing
     in hypoparathyroidism, roughly {hed_total/(hi*SUBJECT_KG):.0f}-{hed_total/(lo*SUBJECT_KG):.0f}x below this HED. That literature reporting normal growth is
     a SAFETY observation at a dose never intended to do anything to a growth plate. It is not
     evidence the drug does not work, and it must not be cited as if it were.
""")


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# ROUND 186 ADDENDUM - THE SCHEDULE/DOSE TRADE-OFF.
# Round 185 showed the licensed DAILY schedule is ~20x too frequent relative to the human
# chondrocyte clock. Fixing the schedule by moving to weekly does not come free: it also cuts
# cumulative exposure. This section puts both axes on one table.
# ---------------------------------------------------------------------------
def addendum():
    RAT_WEEKLY_UG_KG = RAT_DOSE_UG_KG_DAY * RAT_DAYS_PER_WEEK          # 400 ug/kg/week
    HED_WEEKLY_UG_KG = RAT_WEEKLY_UG_KG / KM_RAT_TO_HUMAN              # BSA-scaled
    HED_WEEKLY_TOTAL = HED_WEEKLY_UG_KG * SUBJECT_KG

    print("\n" + "=" * 76)
    print("ADDENDUM - YOU CAN MATCH THE SCHEDULE OR THE DOSE, NOT BOTH WITH EXISTING PRODUCTS")
    print("=" * 76)
    print(f"  ogawa2002 weekly exposure   {RAT_WEEKLY_UG_KG:7.1f} ug/kg/week")
    print(f"  human equivalent            {HED_WEEKLY_UG_KG:7.1f} ug/kg/week"
          f"  = {HED_WEEKLY_TOTAL:6.0f} ug/week for {SUBJECT_KG:.0f} kg\n")
    regs = [
        ("teriparatide 20 ug DAILY",        20.0 * 7,   20.0,   7.0),
        ("abaloparatide 80 ug DAILY",       80.0 * 7,   20.0,   7.0),
        ("teriparatide 56.5 ug WEEKLY",     56.5,       20.0,   1.0),
        ("teriparatide 28.2 ug TWICE-WKLY", 28.2 * 2,   20.0,   2.0),
    ]
    print(f"  {'regimen':34s} {'ug/week':>9s} {'x below HED':>12s} {'pulses/cycle':>13s} {'x too frequent':>15s}")
    for label, per_week_ug, human_cycle_d, doses_wk in regs:
        shortfall = HED_WEEKLY_TOTAL / per_week_ug
        ppc = (doses_wk / 7.0) * human_cycle_d
        print(f"  {label:34s} {per_week_ug:9.1f} {shortfall:11.1f}x {ppc:13.1f} {ppc/1.0:14.1f}x")
    print(f"""
  READ THE TWO RIGHT-HAND COLUMNS TOGETHER. Daily abaloparatide is closest on CUMULATIVE dose
  (about 7x short) and worst on schedule (20 pulses per human chondrocyte cycle against the rat's
  one). Weekly teriparatide is closest on schedule (2.9) and worst on dose (about 69x short).
  NO EXISTING PRODUCT SATISFIES BOTH CONSTRAINTS AT ONCE.

  What would is a single large pulse at a long interval - on the order of {HED_WEEKLY_TOTAL*3:.0f} ug every
  three weeks, which is simply more of the same peptide at the interval the benchmark asks for.
  That is not a product, and no one has ever administered a PTH1R agonist that way.

  THE HONEST SUMMARY: the two corrections this atlas has made to the candidate - the schedule
  benchmark and the dose gap - pull in OPPOSITE directions across the available regimens, and the
  regimen that satisfies both has never been given to anyone.""")


if __name__ == "__main__":
    addendum()
