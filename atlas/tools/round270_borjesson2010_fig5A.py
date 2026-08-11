#!/usr/bin/env python3
"""
ROUND 270 - digitise Figure 5A of borjesson2010 (J Bone Miner Res 25:2690-2700).

The paper's text states only that 1-year-old cartilage-specific ERalpha-null mice
had "increased femur length" versus controls, and gives NO number anywhere in the
text. The magnitude is the whole question - this is the only bone LENGTH gain on
the oestrogen arm of this atlas - so it is read off the figure against the
figure's own axis, the same method round 253 used on newton2018 Fig 2A.

METHOD, AND ITS SELF-CHECKS
  1. Calibration. The y-axis carries six printed labels (17,0 down to 14,5 in
     0.5 mm steps) above an axis break. Their rows are taken from the LABEL TEXT
     blocks rather than from the tick marks, because the axis spine is drawn ~7
     px thick and swallows its own ticks. A straight line is fitted to the six
     and the residual is reported; if the worst tick is off by more than 1.5 px
     the calibration is declared untrusted and the run is flagged.
  2. Bar tops. The two control bars are solid black and the two knockout bars are
     white with a black outline, so neither "darkest column" nor "topmost dark
     pixel" works for both - and the error whisker, a thin central line rising
     ABOVE each bar, defeats the naive approach entirely. Instead every row in
     the plot window is scanned for a HORIZONTAL DARK RUN whose length matches
     the bar width. That run is the solid fill of a black bar and the top rule
     of an open bar, and a whisker is far too narrow to produce one.
  3. The four runs found are checked to be four, and to alternate in x.

Everything printed is a measurement off a published figure, not a number the
authors reported. It is graded accordingly in the node - the paper's own
statistics (asterisk, n = 9 to 12, mean +/- SEM) are what carry significance.

Usage: round270_borjesson2010_fig5A.py fig_101.png
"""
import sys

import numpy as np
from PIL import Image

TICKS = [17.0, 16.5, 16.0, 15.5, 15.0, 14.5]  # top to bottom, mm
DARK = 110


def main():
    png = sys.argv[1] if len(sys.argv) > 1 else "fig_101.png"
    a = np.asarray(Image.open(png).convert("L")).astype(float)
    # Panel A is the left ~30 per cent of this three-panel figure.
    panel = a[:, : int(a.shape[1] * 0.30)]
    dark = panel < DARK

    # ---- 1. axis spine and calibration ------------------------------------
    colsum = dark.sum(axis=0)
    axis_col = int(np.argmax(colsum[: panel.shape[1] // 2]))

    lab = dark[:, 40 : max(45, axis_col - 5)]
    prof = lab.sum(axis=1)
    rows = np.where(prof > 3)[0]
    groups, cur = [], [rows[0]]
    for r in rows[1:]:
        if r - cur[-1] <= 4:
            cur.append(r)
        else:
            groups.append(cur)
            cur = [r]
    groups.append(cur)
    blocks = [(float(np.mean(g)), len(g), int(prof[g].sum())) for g in groups if g]
    blocks = [b for b in blocks if 25 <= b[1] <= 50 and b[2] > 800]
    centres = sorted(b[0] for b in blocks)[: len(TICKS)]
    if len(centres) != len(TICKS):
        print("FAILED: found %d axis labels, need %d" % (len(centres), len(TICKS)))
        return 1

    A = np.vstack([centres, np.ones(len(centres))]).T
    (m, c), *_ = np.linalg.lstsq(A, np.array(TICKS), rcond=None)
    resid = np.abs(A @ np.array([m, c]) - np.array(TICKS))
    px_per_mm = 1.0 / abs(m)
    print("axis spine column %d; label rows %s" % (axis_col, ["%.1f" % x for x in centres]))
    print("calibration %.5f mm/px  =>  %.2f px/mm" % (m, px_per_mm))
    print("worst tick residual %.4f mm = %.2f px" % (resid.max(), resid.max() * px_per_mm))
    if resid.max() * px_per_mm > 1.5:
        print("WARNING: axis non-linear beyond 1.5 px - calibration UNTRUSTED")

    def value(row):
        return m * row + c

    ceiling = int(min(centres) - px_per_mm * 0.05)
    baseline = int(max(centres) + px_per_mm * 0.30)

    # ---- 2. bar width, from the solid control bars ------------------------
    probe = baseline - int(px_per_mm * 0.10)
    on = dark[probe, :]
    runs, start = [], None
    for x in range(axis_col + 8, panel.shape[1]):
        if on[x] and start is None:
            start = x
        elif not on[x] and start is not None:
            runs.append((start, x))
            start = None
    solid = [r for r in runs if (r[1] - r[0]) > px_per_mm * 0.30]
    if not solid:
        print("FAILED: no solid bar found to set the bar width")
        return 1
    barw = int(np.median([r[1] - r[0] for r in solid]))
    print("bar width from solid control bars: %d px (%.3f mm)" % (barw, barw / px_per_mm))

    # ---- 3. horizontal top rules -----------------------------------------
    found = []
    for r in range(ceiling, baseline):
        row = dark[r, :]
        x, n = axis_col + 8, panel.shape[1]
        while x < n:
            if row[x]:
                x0 = x
                while x < n and row[x]:
                    x += 1
                if abs((x - x0) - barw) <= max(3, 0.06 * barw):
                    found.append((r, x0, x))
            else:
                x += 1
    # keep, for each distinct x-position, the HIGHEST such rule (the bar top)
    tops = {}
    for r, x0, x1 in found:
        key = None
        for k in tops:
            if abs(k - x0) <= barw * 0.5:
                key = k
                break
        if key is None:
            tops[x0] = (r, x0, x1)
        elif r < tops[key][0]:
            tops[key] = (r, x0, x1)
    bars = sorted(tops.values(), key=lambda t: t[1])

    print("\nbar tops (x0-x1, row, mm):")
    for r, x0, x1 in bars:
        print("  x %4d-%4d  row %4d  ->  %.3f mm" % (x0, x1, r, value(r)))

    if len(bars) != 4:
        print("\nFAILED: expected 4 bars, found %d - not reporting a read-off" % len(bars))
        return 1

    m4c, m4k, m12c, m12k = [value(b[0]) for b in bars]
    print("\n--- READ-OFF (means; the paper reports mean +/- SEM, n = 9 to 12) ---")
    print("   4 months : control %.3f  KO %.3f   diff %+.3f mm (%+.2f%%)  [n.s. in paper]"
          % (m4c, m4k, m4k - m4c, 100 * (m4k - m4c) / m4c))
    print("  12 months : control %.3f  KO %.3f   diff %+.3f mm (%+.2f%%)  [* in paper]"
          % (m12c, m12k, m12k - m12c, 100 * (m12k - m12c) / m12c))
    print("  growth 4->12 mo : control %+.3f mm   KO %+.3f mm   ratio %.2fx"
          % (m12c - m4c, m12k - m4k, (m12k - m4k) / (m12c - m4c)))
    print("\n  The INCREMENT is the paper's claim ('continued to grow after 4 months,")
    print("  whereas very little growth was seen in control mice'); the 12-month")
    print("  difference is what carries the asterisk.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
