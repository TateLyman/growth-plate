#!/usr/bin/env python3
"""
THE FIRST YIELD UNDER A DRUG.

schrier2006 proposed that oestrogen accelerates senescence by lowering the PROLIFERATIVE
CAPACITY SPENT PER CELL CYCLE - a yield term - after excluding both observable state
variables of the pool by measurement. nilsson2014 restated it as "fewer proliferative
chondrocyte replications per lost resting zone chondrocyte" and never gave a number.
Twenty years and neither paper computed it, because the two terms sit in two figures.

Both figures are now in hand (user-supplied panels, digitised by eye):
  Fig 2 G  resting zone, cells per mm growth-plate width   -> the DENOMINATOR
  Fig 3 B  proximal tibial growth rate, mm per 2.5 weeks   -> the NUMERATOR (length)
  Fig 3 E  hypertrophic cell size, um                      -> converts length to CELLS
  Fig 3 C  BrdU-labelled cells per column                  -> independent flux check

DESIGN: ovariectomised juvenile rabbits. TREATMENT 11-16 wk. WASHOUT 16-21 wk, no drug
in either arm.

WHY THE UNITS PROBLEM DOES NOT BITE HERE. The yield mixes a per-column numerator with a
per-mm-width denominator, so its ABSOLUTE value carries an arbitrary convention - the
same caveat that limits the lui2018 between-bone estimates. But this is ONE BONE, ONE
EXPERIMENT, TWO ARMS. The convention is identical in both arms and CANCELS EXACTLY in
the estradiol-to-vehicle ratio. The ratio is the result; the absolute value is scaffolding.

EVERY VALUE IS READ OFF A PUBLISHED PLOT BY EYE. value_unverified.
"""
# ---- Fig 3B, proximal tibial growth rate, mm per 2.5-week interval -------------
# four consecutive intervals spanning 11-21 wk, plotted at their midpoints
GROWTH = {              # (vehicle, estradiol) mm per 2.5 wk
    (11.0, 13.5): (4.68, 4.15),   # on treatment
    (13.5, 16.0): (3.30, 2.98),   # on treatment
    (16.0, 18.5): (2.38, 2.05),   # washout
    (18.5, 21.0): (1.55, 1.48),   # washout
}
# ---- Fig 3E, terminal hypertrophic cell size, um, proximal tibia ---------------
THC = {11: (72.5, 72.5), 16: (66.5, 60.0), 21: (48.5, 47.0)}
# ---- Fig 2G, resting zone, cells per mm growth-plate width, proximal tibia -----
RZ  = {11: (35.3, 35.3), 16: (26.3, 21.2), 21: (17.7, 14.3)}
# ---- Fig 3C, BrdU-labelled cells per column, proximal tibia -------------------
BRDU = {11: (7.6, 7.6), 16: (4.35, 2.65), 21: (2.2, 1.95)}
ARMS = ("vehicle", "estradiol")

def grown(t0, t1, i):
    return sum(v[i] for (a, b), v in GROWTH.items() if a >= t0 and b <= t1) * 1000.0  # um

print("=" * 78)
print("THE YIELD UNDER A DRUG - nilsson2014, rabbit proximal tibia")
print("=" * 78)
for label, (t0, t1) in (("ON TREATMENT  11-16 wk", (11.0, 16.0)),
                        ("WASHOUT       16-21 wk", (16.0, 21.0))):
    print(f"\n{label}")
    print(f"  {'':<12}{'grown um':>10}{'RZ lost':>9}{'YIELD':>9}{'THC mean':>10}"
          f"{'cells made':>12}{'AMPLIF':>9}")
    out = {}
    for i, arm in enumerate(ARMS):
        g = grown(t0, t1, i)
        lost = RZ[int(t0)][i] - RZ[int(t1)][i]
        thc = 0.5 * (THC[int(t0)][i] + THC[int(t1)][i])
        cells = g / thc
        out[arm] = (g, lost, g / lost, thc, cells, cells / lost)
        print(f"  {arm:<12}{g:>10.0f}{lost:>9.1f}{g/lost:>9.0f}{thc:>10.1f}"
              f"{cells:>12.1f}{cells/lost:>9.2f}")
    v, e = out["vehicle"], out["estradiol"]
    print(f"  {'RATIO E2/veh':<12}{e[0]/v[0]:>10.2f}{e[1]/v[1]:>9.2f}{e[2]/v[2]:>9.2f}"
          f"{e[3]/v[3]:>10.2f}{e[4]/v[4]:>12.2f}{e[5]/v[5]:>9.2f}")

print("\n" + "=" * 78)
print("DECOMPOSITION OF THE OESTROGEN EFFECT ON YIELD, ON TREATMENT")
print("=" * 78)
g_v, g_e = grown(11, 16, 0), grown(11, 16, 1)
l_v, l_e = RZ[11][0] - RZ[16][0], RZ[11][1] - RZ[16][1]
t_v, t_e = 0.5*(THC[11][0]+THC[16][0]), 0.5*(THC[11][1]+THC[16][1])
y_v, y_e = g_v/l_v, g_e/l_e
a_v, a_e = (g_v/t_v)/l_v, (g_e/t_e)/l_e
import math
print(f"  yield ratio          {y_e/y_v:6.3f}")
print(f"  terminal cell size   {t_e/t_v:6.3f}   ({100*math.log(t_e/t_v)/math.log(y_e/y_v):4.0f}% of the log effect)")
print(f"  amplification        {a_e/a_v:6.3f}   ({100*math.log(a_e/a_v)/math.log(y_e/y_v):4.0f}% of the log effect)")
print("""
  SAME ANSWER AS THE BETWEEN-BONE DECOMPOSITION, IN A DIFFERENT SPECIES AND A
  DIFFERENT KIND OF CONTRAST. Round 174 found 88 per cent of the between-bone yield
  gap was amplification, in mouse. Here a DRUG lowers the yield in RABBIT and the
  split is the same shape - cell size barely moves, amplification carries it.
""")
print("=" * 78)
print("INDEPENDENT CHECK - BrdU flux per column (Fig 3C), no length term at all")
print("=" * 78)
for label, (t0, t1) in (("on treatment", (11, 16)), ("washout", (16, 21))):
    yrs = (t1 - t0) / 52.0 * 7 * 52 / 7
    for i, arm in enumerate(ARMS):
        integ = 0.5 * (BRDU[t0][i] + BRDU[t1][i]) * (t1 - t0)   # cell-weeks per column
        lost = RZ[t0][i] - RZ[t1][i]
        print(f"  {label:<14}{arm:<11}BrdU integral {integ:6.1f} / RZ lost {lost:5.1f}"
              f" = {integ/lost:6.2f}")
    print()
print("""LIMITS - carried with every number above
 1 READ OFF PLOTS BY EYE. Not measurements. Read error roughly half a minor gridline.
 2 NET, NOT GROSS resting-zone loss - so every absolute yield is an UPPER BOUND. Both
   arms are biased the same way, which is why the RATIO is the reported result.
 3 The growth-rate panel exists for PROXIMAL TIBIA ONLY, so the full yield cannot be
   computed for the distal radius even though its zone data are published.
 4 Mixed units (per column over per mm width). Cancels in the within-experiment ratio.
 5 Rabbit, ovariectomised, juvenile. One experiment.
""")
