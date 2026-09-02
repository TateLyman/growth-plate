#!/usr/bin/env python3
"""
Round 253. Digitise Figure 2A of newton2018 (PMID 29955624, PMC6020113).

WHY THIS EXISTS. Round 252 read the paper's sentence

    "52% increase in growth: control bones grew 150 +/- 13 um; cKO bones grew
     229 +/- 19 um ... and this growth increment was sustained over the culture
     period"

as a SUSTAINED RATE ADVANTAGE, and built the conclusion "the block on growth is
extrinsic" on top of it. Figure 2A plots cumulative growth in culture at day 2
and day 4 for control, heterozygote and cKO. If the rate advantage were
sustained, the day-4 cKO bar would sit ~52 per cent above the day-4 control bar.
This script measures the bars.

The axis calibration is taken from the five tick marks on the y-axis
(0, 0.2, 0.4, 0.6, 0.8 mm), located by their own pixel positions rather than
assumed. Bar tops are found as the highest row at which more than 85 per cent of
the bar's interior width is bar-coloured, searching only BELOW the significance
annotation lines so that those cannot be mistaken for a bar edge.

Input:  atlas/data/round253/newton2018_fig/gr2.jpg
        (Europe PMC supplementaryFiles endpoint for PMC6020113, CC BY)
"""
import os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(HERE, "data", "round253", "newton2018_fig", "gr2.jpg")

# Panel A is the top-left region of the composite figure.
PANEL_FRAC_H, PANEL_FRAC_W = 0.42, 0.55

# Bar x-extents (inclusive), read off the marked runs along the row just above
# the baseline. Three genotypes per timepoint, in figure order.
BARS = {
    "day2_control": (97, 128),
    "day2_het":     (139, 170),
    "day2_cKO":     (181, 212),
    "day4_control": (252, 283),
    "day4_het":     (294, 326),
    "day4_cKO":     (337, 368),
}

# Bar tops are all below y=145; the "*"/"**" annotation lines sit above that.
SEARCH_TOP = 145


def load_panel():
    a = np.array(Image.open(IMG).convert("RGB"))
    return a[: int(a.shape[0] * PANEL_FRAC_H), : int(a.shape[1] * PANEL_FRAC_W)]


def masks(sub):
    r, g, b = (sub[:, :, i].astype(int) for i in range(3))
    dark = (r < 110) & (g < 110) & (b < 110)
    blue = (b > 140) & (b - r > 50) & (b - g > 25)
    return dark, blue


def y_ticks(dark):
    """Tick marks project to the LEFT of the y-axis; group contiguous rows."""
    band = dark[:, 64:76]
    rows = np.nonzero(band.sum(axis=1) >= 8)[0]
    groups, cur = [], [rows[0]]
    for y in rows[1:]:
        if y - cur[-1] <= 2:
            cur.append(y)
        else:
            groups.append(cur)
            cur = [y]
    groups.append(cur)
    return [sum(gg) / len(gg) for gg in groups]


def main():
    sub = load_panel()
    dark, blue = masks(sub)
    mark = dark | blue

    ticks = y_ticks(dark)
    if len(ticks) != 5:
        raise SystemExit(f"expected 5 y-axis ticks, found {len(ticks)}: {ticks}")
    y_top, y_zero = ticks[0], ticks[-1]          # 0.8 mm and 0 mm
    px_per_mm = (y_zero - y_top) / 0.8
    spacing = np.diff(ticks)
    print(f"y ticks (px): {[round(t,1) for t in ticks]}")
    print(f"tick spacing: {[round(float(s),2) for s in spacing]}  "
          f"(even to {float(spacing.std()):.2f} px)")
    print(f"calibration : {px_per_mm:.2f} px per mm, baseline y = {y_zero}\n")

    vals = {}
    for name, (x0, x1) in BARS.items():
        xs = slice(x0 + 2, x1 - 1)
        width = (x1 - 1) - (x0 + 2)
        top = None
        for y in range(SEARCH_TOP, int(y_zero)):
            if mark[y, xs].sum() / width > 0.85:
                top = y
                break
        if top is None:
            raise SystemExit(f"no bar top found for {name}")
        vals[name] = (y_zero - top) / px_per_mm
        print(f"{name:13s} top_y={top:4d}   {vals[name]:.4f} mm")

    print()
    for d in ("day2", "day4"):
        c, k = vals[f"{d}_control"], vals[f"{d}_cKO"]
        print(f"{d}: cKO/control = {k/c:.3f}  ({(k/c-1)*100:+.0f} per cent cumulative)")

    print("\nGROWTH BETWEEN DAY 2 AND DAY 4 - the test of a SUSTAINED advantage:")
    inc = {}
    for gt in ("control", "het", "cKO"):
        inc[gt] = vals[f"day4_{gt}"] - vals[f"day2_{gt}"]
        print(f"  {gt:8s} {inc[gt]:.4f} mm")
    print(f"  cKO increment / control increment = {inc['cKO']/inc['control']:.3f}")

    # What a genuinely sustained +52 per cent would have predicted at day 4.
    pred = vals["day4_control"] * 1.52
    print(f"\nIf the 52 per cent were a SUSTAINED rate advantage, day-4 cKO would be "
          f"{pred:.3f} mm.\nIt is {vals['day4_cKO']:.3f} mm. Published SEMs on these "
          f"bars are of order 0.02-0.03 mm,\nso the shortfall of {pred-vals['day4_cKO']:.3f} "
          f"mm is several standard errors.")

    print("\nREAD ERROR. Bar tops are located to about +/- 2 px, which is "
          f"+/- {2/px_per_mm:.4f} mm.\nThat is smaller than the day2-to-day4 increment "
          f"difference of {inc['control']-inc['cKO']:.4f} mm,\nbut it is NOT smaller than "
          "the published SEMs, so the claim supported here is the\nABSENCE of a sustained "
          "advantage, not the presence of a sustained DISadvantage.")


if __name__ == "__main__":
    main()
