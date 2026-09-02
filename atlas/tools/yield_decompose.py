#!/usr/bin/env python3
"""
DECOMPOSE THE YIELD into its two physical factors, from lui2018 S1 Data (CC-BY, mouse).

WHY
---
`the_exchange_rate_between_growth_and_pool_depletion` records HEIGHT = POOL x YIELD,
with the yield estimated at 14 um of bone per resting-zone cell in the metacarpal
(fuses at 2-3wk) against 146 in the femur (never fuses). But a length-yield is a
PRODUCT of two independent things:

    um of bone per RZ cell  =  (hypertrophic cells produced per RZ cell spent)
                               x  (um of bone per hypertrophic cell)
         YIELD_length       =        AMPLIFICATION            x    THC height

This matters because the atlas already has an arm on the second factor - the CNP
axis, which nakao2015 partitions onto the hypertrophic zone. If the 10-fold yield
gap is mostly THC height, then "yield" is h_term wearing a different name and there
is no new control point. If it is mostly AMPLIFICATION, yield is a genuinely
distinct lever and nothing in the stack touches it.

CONSTRUCTION
------------
Between-bone RATIOS are used, not absolute amplification, because the length-yield
is normalised per 500 um of plate width while THC height is per cell. The width
convention CANCELS in a between-bone ratio of yields; THC height needs no convention.

    amplification_ratio = yield_ratio / THC_ratio

so the fraction of the log yield gap attributable to cell size is
log(THC_ratio)/log(yield_ratio).

Every number is a RE-ANALYSIS of published per-animal values, graded value_unverified.
Data: doi:10.1371/journal.pbio.2005263 S1 Data, CC-BY 4.0.
"""
import sys, math
import numpy as np
import openpyxl

XLSX = sys.argv[1] if len(sys.argv) > 1 else "atlas/data/lui2018/lui2018_S1Data.xlsx"
BONES = ["femur", "tibia", "metacarpal", "phalanx"]
RNG = np.random.default_rng(20260809)
NBOOT = 20000

# yield_length values as already recorded in the atlas from yield_lui2018.py
# (um bone per RZ cell lost, per 500 um plate width), with their 95% intervals.
YIELD = {("femur", "2-3wk"): (146, 110, 208),
         ("tibia", "2-3wk"): (247, 98, 2774),
         ("metacarpal", "2-3wk"): (14, 12, 18)}


def age_weeks(a):
    if a is None: return None
    s = str(a).strip().lower()
    if s in ("e17", "e17.5", "nb"): return None
    if s.endswith("wk"): s = s[:-2]
    try: return float(s)
    except ValueError: return None


def harvest(ws, label):
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    top, sub = rows[0], rows[1]
    li = top.index(label)
    fem = next(i for i in range(li - 1, len(sub))
               if str(sub[i]).strip().lower() == "femur")
    age = max(i for i in range(fem) if str(sub[i]).strip().lower().startswith("age"))
    cols = {b: next(i for i in range(fem, len(sub))
                    if str(sub[i]).strip().lower() == b) for b in BONES}
    out = {}
    for r in rows[2:]:
        if age >= len(r): continue
        w = age_weeks(r[age])
        if w is None: continue
        for b, c in cols.items():
            v = r[c] if c < len(r) else None
            if isinstance(v, (int, float)) and v > 0:
                out.setdefault((b, w), []).append(float(v))
    return out


wb = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)
thc  = harvest(wb["Fig1C"], "THC height")      # MOUSE - ages E17,NB,1,2,3,4,8,12wk
thcR = harvest(wb["FigS2"], "THC height")      # RAT   - ages 1,2,4,8,12,16wk (FigS3 names the species)

print("=" * 78)
print("IS THE YIELD GAP CELL SIZE, OR IS IT DIVISIONS PER PROGENITOR?")
print("lui2018 S1 Data re-analysis, mouse. value_unverified.")
print("=" * 78)

print("\nTERMINAL HYPERTROPHIC CELL HEIGHT (um), mean +/- SD (n)")
print(f"{'age':<7}" + "".join(f"{b:>16}" for b in BONES))
ages = sorted({w for (_, w) in thc})
for w in ages:
    row = f"{w:g}wk   "
    for b in BONES:
        v = thc.get((b, w))
        row += f"{np.mean(v):>9.1f}+-{np.std(v,ddof=1):<4.1f}" if v and len(v) > 1 else f"{'-':>16}"
    print(row)

print("\nDECOMPOSITION over the 2-3wk interval (the interval the yield was computed on)")
print("-" * 78)
ref = "metacarpal"   # the bone that FUSES at 2-3wk
mc = [v for w in (2.0, 3.0) for v in thc.get((ref, w), [])]

for bone in ("femur", "tibia"):
    if (bone, "2-3wk") not in YIELD: continue
    y, ylo, yhi = YIELD[(bone, "2-3wk")]
    ym, ymlo, ymhi = YIELD[(ref, "2-3wk")]
    tb = [v for w in (2.0, 3.0) for v in thc.get((bone, w), [])]
    if not tb or not mc: continue

    yield_ratio = y / ym
    thc_ratio = np.mean(tb) / np.mean(mc)
    amp_ratio = yield_ratio / thc_ratio
    frac_size = math.log(thc_ratio) / math.log(yield_ratio)

    # bootstrap THC ratio; propagate the yield ratio through its published interval
    br = [np.mean(RNG.choice(tb, len(tb), True)) / np.mean(RNG.choice(mc, len(mc), True))
          for _ in range(NBOOT)]
    tlo, thi = np.percentile(br, [2.5, 97.5])
    ylo_r, yhi_r = ylo / ymhi, yhi / ymlo

    print(f"\n{bone.upper()} versus {ref.upper()}   (n_thc {len(tb)} vs {len(mc)})")
    print(f"  yield ratio (length)   {yield_ratio:7.1f}x     [{ylo_r:.1f}, {yhi_r:.1f}] from published intervals")
    print(f"  THC height ratio       {thc_ratio:7.2f}x     [{tlo:.2f}, {thi:.2f}] bootstrap")
    print(f"  -> AMPLIFICATION ratio {amp_ratio:7.1f}x     ({yield_ratio:.1f} / {thc_ratio:.2f})")
    print(f"  fraction of the log gap explained by CELL SIZE: {100*frac_size:.0f}%")
    print(f"  fraction explained by AMPLIFICATION:            {100*(1-frac_size):.0f}%")

print("""
SPECIES NOTE - THIS SCRIPT WAS WRONG ON ITS FIRST RUN AND THE FIX IS THE REASON
IT IS TRUSTWORTHY NOW. lui2018 S1 Data holds BOTH a mouse and a rat series.
Sheets Fig1C and Fig2B-G are MOUSE (ages E17, NB, 1, 2, 3, 4, 8, 12wk); sheet
FigS2 is RAT (ages 1, 2, 4, 8, 12, 16wk), which sheet FigS3 confirms by naming
the two series explicitly with exactly those age sets. The first run of this
script divided a MOUSE yield by a RAT cell height. Everything below is
single-species: mouse throughout, with the rat series used only as an
INDEPENDENT REPLICATION of the between-bone THC comparison.
""")

# ---------------------------------------------------------------------------
# PART 2 - RAT REPLICATION OF THE KEY SUB-CLAIM
# ---------------------------------------------------------------------------
print("=" * 78)
print("PART 2 - IS TERMINAL CELL HEIGHT CONSERVED BETWEEN BONES? RAT REPLICATION")
print("=" * 78)
print(f"\n{'age(wk)':<9}" + "".join(f"{b:>13}" for b in BONES) + f"{'fem/mc':>9}")
for w in sorted({a for (_, a) in thcR}):
    row = f"{w:<9g}"
    vals = {}
    for b in BONES:
        v = thcR.get((b, w))
        vals[b] = np.mean(v) if v else None
        row += f"{vals[b]:>13.1f}" if vals[b] else f"{'-':>13}"
    r = (vals['femur'] / vals['metacarpal']) if vals['femur'] and vals['metacarpal'] else None
    row += f"{r:>9.2f}" if r else f"{'-':>9}"
    print(row)

# ---------------------------------------------------------------------------
# PART 3 - MOUSE: CELL PRODUCTION PER COLUMN AND THE DRAW ON THE POOL
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 3 - MOUSE ONLY: CELL PRODUCTION PER COLUMN AND THE POOL DRAW")
print("=" * 78)
gr = harvest(wb["Fig1C"],   "Calcein labeled bone growth")   # mouse
rz = harvest(wb["Fig2B-G"], "Resting Zone Cell Count")       # mouse
print(f"\n{'bone':<12}{'age':>5}{'growth':>10}{'THC':>8}{'cells/col':>11}{'RZ cells':>10}")
print(f"{'':<12}{'wk':>5}{'um/day':>10}{'um':>8}{'per day':>11}{'/500um':>10}")
print("-" * 56)
for b in BONES:
    for w in sorted({a for (bb, a) in gr if bb == b}):
        g, t, r = gr.get((b, w)), thc.get((b, w)), rz.get((b, w))
        if not (g and t): continue
        gm, tm = np.mean(g), np.mean(t)
        rm = np.mean(r) if r else float('nan')
        print(f"{b:<12}{w:>5g}{gm:>10.0f}{tm:>8.1f}{gm/tm:>11.2f}{rm:>10.1f}")
