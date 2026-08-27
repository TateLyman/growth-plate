#!/usr/bin/env python3
"""
THE RENEWAL FRACTION REQUIRED FOR INDETERMINATE GROWTH.

Model. Resting-zone progenitors renew by POPULATION asymmetry (chu2025/newton2019: clone
number falls while clone size rises). Let p = probability that a daughter of a stem-cell
division remains a stem cell. Each division cycle multiplies the pool by 2p.

  2p > 1  -> pool grows          -> growth never ceases
  2p = 1  -> pool constant       -> INDETERMINATE GROWTH.  p = 0.500 exactly.
  2p < 1  -> pool decays geometrically -> a finite growth period

So the entire question "why does a human stop growing" reduces to: how far below 0.500 does
the human resting zone sit?

We do not know p. But we know how long the pool lasts (the human growth period) and roughly
how often it divides. p is then determined, and — the point of this script — p depends only
LOGARITHMICALLY on both, so the answer is robust to large errors in either.
"""
import math

def p_required(years, cycle_days, frac_remaining):
    n = years*365.25/cycle_days                    # number of stem divisions in the period
    two_p = frac_remaining**(1.0/n)                # (2p)^n = frac_remaining
    return two_p/2.0, n

print(__doc__)
print("="*92)
print("SENSITIVITY SWEEP — human post-SOC growth period, resting-zone cycle time, exhaustion criterion")
print("="*92)
print(f"{'growth yrs':>10} {'RZ cycle d':>11} {'end frac':>9} {'n divisions':>12} {'p (renewal)':>12} {'gap to 0.500':>13}")
res=[]
for years in (14,16,18):
    for cyc in (20,30,60,90,120,180):
        for frac in (0.01,0.001):
            p,n=p_required(years,cyc,frac)
            res.append(p)
            print(f"{years:>10} {cyc:>11} {frac:>9} {n:>12.0f} {p:>12.4f} {0.5-p:>13.4f}")
print("-"*92)
print(f"ACROSS ALL {len(res)} PARAMETER COMBINATIONS: p ranges {min(res):.4f} to {max(res):.4f}")
print(f"  mean {sum(res)/len(res):.4f} | every value is BELOW 0.5 and the largest shortfall is {0.5-min(res):.4f}")
print(f"  i.e. the human resting zone misses indeterminate growth by {100*(0.5-max(res)):.2f}-{100*(0.5-min(res)):.2f}"
      f" PERCENTAGE POINTS of self-renewal probability ({100*(0.5-max(res))/0.5:.1f}-{100*(0.5-min(res))/0.5:.1f}% in relative terms).")

print("\n"+"="*92)
print("WHAT A SMALL CHANGE IN p BUYS — growth period as a function of p (16 y baseline, 60 d cycle)")
print("="*92)
p0,n0=p_required(16,60,0.01)
print(f"baseline p = {p0:.4f}  ({n0:.0f} divisions, 16.0 y)\n")
print(f"{'p':>8} {'2p':>8} {'divisions to 1%':>17} {'growth period (y)':>19} {'x baseline':>11}")
for dp in (0,0.002,0.005,0.010,0.0116,0.015,0.020,0.0232,0.025):
    p=p0+dp
    if 2*p>=1:
        print(f"{p:>8.4f} {2*p:>8.4f} {'INFINITE':>17} {'INDETERMINATE':>19} {'-':>11}")
        continue
    n=math.log(0.01)/math.log(2*p)
    yrs=n*60/365.25
    print(f"{p:>8.4f} {2*p:>8.4f} {n:>17.0f} {yrs:>19.1f} {yrs/16.0:>11.2f}")

print("\n"+"="*92)
print("THE SAME THING AS A HEIGHT ESTIMATE (crude, terminal-velocity integration)")
print("="*92)
print("carani1997 is the only man followed far enough to give a decay shape: 1.31 cm/yr from 18-31,")
print("then 0.43 cm/yr from 31-38 with plates never closed. Take the extra years at that envelope.")
for dp,label in ((0.005,'+0.005'),(0.010,'+0.010'),(0.0232,'+0.0232 (to threshold)')):
    p=p0+dp
    if 2*p>=1: print(f"  p {label}: INDETERMINATE — no endpoint"); continue
    n=math.log(0.01)/math.log(2*p); yrs=n*60/365.25; extra=yrs-16.0
    cm=min(extra,13)*1.31 + max(0.0,extra-13)*0.43
    print(f"  p {label}: growth period {yrs:.1f} y (+{extra:.1f} y) -> roughly +{cm:.0f} cm on the terminal envelope")

print("\n"+"="*92)
print("THE CORRECT DURATION — the POOL-limited period, not the hormone-limited one")
print("="*92)
print("A normal plate is switched OFF by oestrogen with capacity to spare (CEILING_CENSUS).")
print("The duration that measures the POOL is the oestrogen-null one: herrmann2002 grew until 24 y")
print("untreated with epiphyses still open at 27; carani1997 was still growing at 38. The SOC forms")
print("~1-5 y, so the post-SOC pool-limited period is ~20-35 y, not 16.")
print(f"\n{'post-SOC yrs':>13} {'cycle d':>8} {'p':>9} {'gap to 0.500':>13}")
best=[]
for years in (20,24,30,35):
    for cyc in (30,60):
        p,n=p_required(years,cyc,0.01)
        best.append(p)
        print(f"{years:>13} {cyc:>8} {p:>9.4f} {0.5-p:>13.4f}")
print(f"\n  -> using the pool-limited duration the gap NARROWS to "
      f"{100*(0.5-max(best)):.2f}-{100*(0.5-min(best)):.2f} percentage points.")
print("     The better the estimate of how long a plate lasts when nothing switches it off,")
print("     the CLOSER the human resting zone sits to the indeterminate-growth threshold.")
