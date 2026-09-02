#!/usr/bin/env python3
"""
Bone-age cost per centimetre, computed from published paired height/bone-age data.
Gap: g_l7_bone_age_cost_per_centimetre_across_the_stack

EVERY OUTPUT IS ATLAS ARITHMETIC ON PUBLISHED SUMMARY VALUES, NOT A MEASUREMENT.
Graded value_unverified. Bone-age reading error is ~0.5 y (Greulich-Pyle), which is
large relative to the annual increments here - propagated explicitly below.
"""
import math

def fmt(x, n=2): return f"{x:.{n}f}"

print("="*78)
print("AGENT 1 - ANASTROZOLE ADDED TO GROWTH HORMONE (mauras2008)")
print("="*78)
# Placebo-controlled. Linear growth COMPARABLE between arms (paper's own words).
# Bone age advance over 3 years: anastrozole +2.5 +/- 0.2, placebo +4.1 +/- 0.1 (P<0.0001)
ba_ana, ba_ana_se = 2.5, 0.2
ba_pbo, ba_pbo_se = 4.1, 0.1
ratio = ba_pbo / ba_ana
# ratio of (cm per BA-year); since cm is equal in both arms it cancels exactly
rel_se = math.sqrt((ba_ana_se/ba_ana)**2 + (ba_pbo_se/ba_pbo)**2)
lo, hi = ratio*(1-1.96*rel_se), ratio*(1+1.96*rel_se)
print(f"  bone age advance, 3 y : anastrozole+GH {ba_ana} y vs GH+placebo {ba_pbo} y")
print(f"  linear growth         : COMPARABLE between arms (stated by the paper)")
print(f"  -> cm per BA-year ratio = {fmt(ratio)}x  (95% CI {fmt(lo)}-{fmt(hi)})")
print("  THE HEIGHT TERM CANCELS. This is the most robust number in the table:")
print("  it needs no absolute height, only that growth was equal - which was measured.")

print()
print("="*78)
print("AGENT 2 - VOSORITIDE IN NON-FGFR3 CHILDREN (dauber2026)")
print("="*78)
# Own-control: 6 mo observation then 12 mo treatment.
v_pre, v_on = 4.53, 8.09              # cm/yr
baca_0, baca_0_sd = 0.94, 0.20        # BA/CA ratio at day 1
baca_12, baca_12_sd = 0.92, 0.17      # BA/CA ratio at month 12 (P=0.22)
ca0 = 7.0                             # mean chronological age; cohort 3-11 y
# BA advance over the treated year implied by the ratio change:
dBA = baca_12*(ca0+1.0) - baca_0*ca0
print(f"  velocity              : {v_pre} -> {v_on} cm/yr")
print(f"  BA/CA ratio           : {baca_0} -> {baca_12} (P=0.22, weak null)")
print(f"  implied BA advance    : {fmt(dBA)} y per 1.0 y chronological (at CA0={ca0} y)")
print(f"  -> ON TREATMENT       : {fmt(v_on/dBA,1)} cm per BA-year")
print(f"  -> PRE-TREATMENT      : {fmt(v_pre/baca_0,1)} cm per BA-year (ratio steady at {baca_0})")
print(f"  -> improvement        : {fmt((v_on/dBA)/(v_pre/baca_0))}x")
print()
print("  ERROR IS THE STORY HERE AND IT IS LARGE. A Greulich-Pyle reading carries")
print("  ~0.5 y of error; dBA is ~0.8 y. Propagating +/-0.5 y on dBA alone:")
for e in (-0.5, 0.0, +0.5):
    d = dBA + e
    print(f"    dBA = {fmt(d)} y -> {fmt(v_on/d,1)} cm per BA-year"
          f"  ({fmt((v_on/d)/(v_pre/baca_0))}x)")
print("  The direction survives the error band; the magnitude does not. And the")
print("  underlying null is P=0.22 over 12 months with NO equivalence margin given.")
print(f"  Sensitivity to the assumed mean age (cohort was 3-11 y):")
for c in (5.0, 7.0, 9.0):
    d = baca_12*(c+1.0) - baca_0*c
    print(f"    CA0 = {c} y -> dBA {fmt(d)} y -> {fmt(v_on/d,1)} cm per BA-year")

print()
print("="*78)
print("AGENT 3 - GROWTH HORMONE")
print("="*78)
print("  NOT PLACEABLE ON THIS AXIS, AND THAT IS THE FINDING.")
print("  chu2025 shows GH depletes the resting-zone progenitor pool by shifting")
print("  divisions toward the committed side. That cost is paid in PROGENITORS,")
print("  not in bone age, and a BA/CA ratio cannot see it. Two independent lines")
print("  converge on the same clinical signature - the waning of GH efficacy after")
print("  1-2 years (chu2025) and the authors of dauber2026 noting that GH gave")
print("  0.49/0.62/0.7 SD in these same three conditions but growth rates SLOWED in")
print("  subsequent years, whereas the CNP axis sustained multi-year gains.")
print("  A second currency is required before GH can be compared.")
