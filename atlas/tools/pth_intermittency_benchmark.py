#!/usr/bin/env python3
"""
ROUND 185 - THE INTERMITTENCY BENCHMARK. Does "intermittent" survive the trip from rat to human?

THE PROBLEM. Every positive result for PTH1R agonism at a growth plate depends on the dosing being
INTERMITTENT, and every negative one - Jansen, the humanized H223R mouse, the continuous arm of
liu2012, PTHrP-overexpression transgenics, the paediatric dialysis cohort - is a CONTINUOUS or
CHRONIC exposure. The sign of this drug class inverts with schedule. So the question is not "is the
dose right" but "is the SCHEDULE still intermittent once you move species".

"Intermittent" is not a property of a syringe. It is a ratio between the dosing interval and the
clock of the cell you are trying to move. This atlas already holds both clocks, measured, and they
differ by an order of magnitude:

    rat proliferative chondrocyte cycle    1.4 d   (hunziker1994, normal rats; wilsman1996 range)
    human proliferative chondrocyte cycle  ~20 d   (kember1976 via the round-177 human anchor)

The benchmark below converts every real dosing regimen into DOSES PER CHONDROCYTE CELL CYCLE, which
is the schedule as the target cell experiences it.

This metric is deliberately chosen because it is robust: it needs only the dosing frequency and the
cycle time, not the half-life, not the Cmax, not the tissue concentration - none of which has ever
been measured at a growth plate for any agent (see growth_plate_drug_exposure).
"""

import math

# ---------------------------------------------------------------------------
# CLOCKS. Both already in the atlas, both from primary sources read in full.
# ---------------------------------------------------------------------------
RAT_PZ_CYCLE_D = 1.4          # hunziker1994, normal unoperated rat, proliferative cell cycle time
RAT_PZ_CYCLE_RANGE = (1.29, 3.18)   # wilsman1996: 30.9 h proximal tibia to 76.3 h proximal radius
HUMAN_PZ_CYCLE_D = 20.0       # kember1976 -> ~1.2 new cells/column/day over ~24 proliferating cells
HUMAN_PZ_CYCLE_RANGE = (10.0, 30.0)  # the atlas has no error bar on this; bracket it generously

# ---------------------------------------------------------------------------
# REGIMENS. The rat experiment, and every human regimen that actually exists.
# ---------------------------------------------------------------------------
REGIMENS = [
    # label,                          doses per week, species
    ("ogawa2002 rat, 5 days/week",            5.0,   "rat"),
    ("teriparatide 20 ug DAILY",              7.0,   "human"),
    ("abaloparatide 80 ug DAILY",             7.0,   "human"),
    ("teriparatide 28.2 ug TWICE-WEEKLY",     2.0,   "human"),
    ("teriparatide 56.5 ug WEEKLY",           1.0,   "human"),
    ("hypothetical FORTNIGHTLY",              0.5,   "human"),
    ("hypothetical EVERY 3 WEEKS",            1/3,   "human"),
]


def doses_per_cycle(per_week, cycle_d):
    return (per_week / 7.0) * cycle_d


def banner(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


banner("THE SCHEDULE AS THE TARGET CELL EXPERIENCES IT")
print(f"  rat proliferative chondrocyte cycle    {RAT_PZ_CYCLE_D:5.2f} d   (hunziker1994)")
print(f"  human proliferative chondrocyte cycle  {HUMAN_PZ_CYCLE_D:5.1f} d   (kember1976)")
print(f"  ratio                                  {HUMAN_PZ_CYCLE_D/RAT_PZ_CYCLE_D:5.1f} x\n")
print(f"  {'regimen':38s} {'doses/wk':>9s} {'DOSES PER CELL CYCLE':>22s}")
rat_ref = None
rows = []
for label, per_week, sp in REGIMENS:
    cyc = RAT_PZ_CYCLE_D if sp == "rat" else HUMAN_PZ_CYCLE_D
    dpc = doses_per_cycle(per_week, cyc)
    if sp == "rat":
        rat_ref = dpc
    rows.append((label, per_week, sp, dpc))
    print(f"  {label:38s} {per_week:9.2f} {dpc:22.2f}")

banner("THE COMPARISON THAT MATTERS")
print(f"""
  THE RAT IN ogawa2002 RECEIVED {rat_ref:.2f} PULSES PER CHONDROCYTE CELL CYCLE.
  One pulse per cycle. The cell saw the drug once, then went a full cycle without it.
""")
print(f"  {'regimen':38s} {'x more often than the rat':>28s}")
for label, per_week, sp, dpc in rows:
    if sp == "rat":
        continue
    print(f"  {label:38s} {dpc/rat_ref:26.1f} x")

banner("WHAT DOSING INTERVAL REPRODUCES THE RAT'S SCHEDULE IN A HUMAN?")
target_per_week = rat_ref * 7.0 / HUMAN_PZ_CYCLE_D
interval_d = 7.0 / target_per_week
print(f"""
  To deliver {rat_ref:.2f} pulses per human chondrocyte cycle you dose every {interval_d:.0f} DAYS.

  That is the whole finding, and it falls out of the arithmetic rather than being argued:
  THE RAT GOT ROUGHLY ONE PULSE PER CELL CYCLE, SO THE HUMAN EQUIVALENT IS ROUGHLY ONE PULSE PER
  HUMAN CELL CYCLE - ABOUT ONCE EVERY THREE WEEKS. Daily dosing, which is what teriparatide and
  abaloparatide are licensed as and what any naive attempt would use, is {rows[1][3]/rat_ref:.0f} TIMES TOO FREQUENT
  relative to the clock of the cell being targeted.
""")

banner("SENSITIVITY - the human cycle time is the weakest input")
print(f"  {'human cycle (d)':>16s} {'daily = x rat':>15s} {'weekly = x rat':>16s} {'matching interval (d)':>22s}")
for hc in (10.0, 15.0, 20.0, 25.0, 30.0):
    d_daily = doses_per_cycle(7.0, hc) / rat_ref
    d_weekly = doses_per_cycle(1.0, hc) / rat_ref
    match = 7.0 / (rat_ref * 7.0 / hc)
    print(f"  {hc:16.0f} {d_daily:15.1f} {d_weekly:16.1f} {match:22.0f}")
print("""
  Daily dosing is 10 to 30 fold too frequent across the entire plausible range of the human cycle
  time. THE CONCLUSION DOES NOT DEPEND ON THE EXACT VALUE. Weekly dosing lands at 1.4x to 4.3x the
  rat's schedule over that same range - still too frequent, but within a factor of a few rather
  than an order of magnitude, and it is the only such regimen that actually exists as a product.""")

banner("SENSITIVITY - and if the rat cycle is at the other end of wilsman1996's range")
for rc in (RAT_PZ_CYCLE_RANGE[0], RAT_PZ_CYCLE_D, RAT_PZ_CYCLE_RANGE[1]):
    rr = doses_per_cycle(5.0, rc)
    match = 7.0 / (rr * 7.0 / HUMAN_PZ_CYCLE_D)
    print(f"  rat cycle {rc:4.2f} d -> rat got {rr:4.2f} pulses/cycle -> human matching interval {match:5.1f} d "
          f"(daily = {doses_per_cycle(7.0,HUMAN_PZ_CYCLE_D)/rr:4.1f}x)")
print("""
  Even taking the SLOWEST rat plate wilsman1996 measured - the proximal radius at 76.3 h, which is
  not the bone ogawa2002 used - daily human dosing is still 8-9 fold too frequent.""")

banner("THE DISANALOGY CHECK - why vosoritide's daily success does not rescue this")
print("""
  The obvious objection is that vosoritide is also a ~4 kDa peptide with a very short half-life,
  is also dosed daily, and works in humans - so short daily pulses of a peptide clearly can move a
  human growth plate. True, and it defeats the PHARMACOKINETIC objection completely.

  It does not defeat this one, because the two drugs have opposite schedule pharmacology. CNP
  works CONTINUOUSLY TOO - yasoda2004's chondrocyte-targeted CNP overexpression is permanent
  transgenic exposure and it rescues achondroplasia. CNP is schedule-INSENSITIVE, so daily dosing
  is safe for it in the only sense that matters here. PTH1R agonism INVERTS with schedule: the same
  molecule that lengthens bone in pulses shortens it when continuous, and every continuous exposure
  on record - Jansen, the humanized H223R mouse, liu2012's continuous arm, the PTHrP and
  constitutively-active-receptor transgenics - produces the same phenotype.

  For a schedule-inverting drug, moving to a species whose target cells run ten times slower
  without changing the dosing interval moves you TOWARD the harmful arm. That is the risk, and it
  is specific to this drug class.""")

banner("THE UNRESOLVED QUESTION THIS BENCHMARK RESTS ON")
print("""
  WHICH CLOCK SETS "INTERMITTENT"? There are two candidates and the literature does not settle it.

  (a) PTH1R DESENSITISATION AND RESENSITISATION - receptor-intrinsic, minutes to hours, and almost
      certainly similar in rat and human chondrocytes. If this is the operative clock, the duty
      cycle is species-invariant, daily dosing is genuinely intermittent in both species, and THIS
      ENTIRE BENCHMARK COLLAPSES.

  (b) THE CHONDROCYTE COMMITMENT CLOCK - the differentiation timer that decides when a proliferative
      cell turns hypertrophic. This scales with the cell cycle, so it is ~10x slower in human. If
      this is the operative clock, daily human dosing sits near the continuous end and the rat
      result may not merely fail to transfer, it may INVERT.

  THE EVIDENCE LEANS TOWARD (b) BUT DOES NOT ESTABLISH IT. The phenotype that defines the harmful
  arm is a DIFFERENTIATION-TIMING phenotype - reyes2023's Jansen plate has an expanded proliferative
  and prehypertrophic zone whose cells apoptose instead of hypertrophying. That is a commitment
  clock failing, not a receptor failing to resensitise. But the intermittent-versus-continuous
  distinction in BONE is usually attributed to signalling duration in osteoblasts, which is (a).

  Nobody has measured PTH1R resensitisation kinetics in chondrocytes of either species, and a
  focused search returns two papers on the topic, neither of them in cartilage.
""")
