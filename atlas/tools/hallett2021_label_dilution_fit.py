#!/usr/bin/env python3
"""
Mouse resting-zone division rate from the Hallett 2021 Figure 4c SOURCE DATA.

WHAT THIS IS
------------
Round 194 estimated the mouse resting-zone cycle time from EdU labelling indices
and could only bound it loosely (10-59 d) because no S-phase duration is
reported. Round 195 has the actual label-dilution curve: Hallett 2021 Figure 4c
Source Data 1, per biological replicate, supplied by the user as a workbook
preview. This is a direct kinetic measurement and needs no S-phase assumption.

AUTHOR-STATED INPUTS (transcribed from the source-data workbook; the quantity is
"% of Col2a1CE-tdT+ cells with H2B-EGFP above 10^4 units", by weeks in chase)

WHAT CAN AND CANNOT BE CONCLUDED
--------------------------------
Cells leave the label-retaining gate by DIVIDING (each division halves H2B-EGFP)
or by LEAVING the resting zone (differentiation into the proliferative column).
The observed decay rate is therefore

    lambda_obs = lambda_division + lambda_efflux  >=  lambda_division

so the interval derived from the decay is a LOWER BOUND on the resting-zone
cycle time, not an estimate of it. Everything below is reported that way.
"""
import math

# week -> list of biological replicates, % of cells > 10^4 H2B-EGFP
DATA = {
    0:  [92.3, 92.4, 90.0, 84.4, 82.2, 87.9, 87.8, 77.9, 82.6],
    1:  [49.8, 50.5, 46.1, 44.0, 58.9, 40.0, 43.5, 39.2, 56.1],
    2:  [25.7, 31.4, 28.7, 19.2, 18.8, 18.4, 23.1],
    3:  [17.1, 21.4, 18.2, 14.3, 15.1, 11.9],
    4:  [10.3, 11.7, 10.0, 10.5, 7.75, 11.1],
    5:  [4.29, 6.91, 4.89, 4.34, 4.69, 5.76, 5.01],
    6:  [4.83, 3.93, 5.55, 4.40, 5.10],
    7:  [2.96, 5.28, 2.48],
    8:  [2.60, 2.76, 3.84],
    10: [2.26, 3.03, 2.56],
    12: [1.90, 2.13, 2.66],
}
# workbook-stated summary, used only to check the transcription
STATED_MEAN = {0: 86.39, 1: 47.57, 2: 23.61, 3: 16.33, 4: 10.23, 5: 5.13,
               6: 4.76, 7: 3.57, 8: 3.07, 10: 2.62, 12: 2.23}


def mean(xs):
    return sum(xs) / len(xs)


def loglinfit(pts):
    """least squares on ln(y) vs t; returns (intercept, slope, r2)"""
    n = len(pts)
    xs = [p[0] for p in pts]
    ys = [math.log(p[1]) for p in pts]
    mx, my = sum(xs) / n, sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    b = sxy / sxx
    a = my - b * mx
    ss_res = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys)
    return a, b, 1 - ss_res / ss_tot


def main():
    print("=" * 76)
    print("HALLETT 2021 FIG 4c SOURCE DATA -- LABEL DILUTION FIT")
    print("=" * 76)

    print("\n[0] TRANSCRIPTION CHECK against the workbook's own Mean column")
    bad = 0
    for wk in sorted(DATA):
        m = mean(DATA[wk])
        ok = abs(m - STATED_MEAN[wk]) < 0.02
        bad += 0 if ok else 1
        print(f"    wk {wk:>2}  n={len(DATA[wk])}  computed {m:6.2f}  "
              f"stated {STATED_MEAN[wk]:6.2f}  {'ok' if ok else 'MISMATCH'}")
    print(f"    {'all replicate means reproduce the workbook' if not bad else 'TRANSCRIPTION ERROR'}")

    print("\n[1] THE CURVE IS BIPHASIC, WHICH IS THE POINT")
    print("    Weeks 0-5 fall 86.4 -> 5.13, a 16.8-fold loss. Weeks 5-12 fall")
    print("    5.13 -> 2.23, a 2.3-fold loss over a longer interval. The fast")
    print("    phase is the bulk proliferative population diluting out; the")
    print("    tail is the slow-cycling population the paper is about.")

    for tag, wks in (("FAST PHASE (wk 0-5)", [0, 1, 2, 3, 4, 5]),
                     ("SLOW TAIL  (wk 5-12)", [5, 6, 7, 8, 10, 12])):
        pts = [(w, mean(DATA[w])) for w in wks]
        a, b, r2 = loglinfit(pts)
        lam = -b                      # per week
        print(f"\n    --- {tag} ---")
        print(f"      decay constant lambda   : {lam:.4f} / week   (R2 = {r2:.4f})")
        print(f"      half-time of the fraction: {math.log(2) / lam:7.2f} weeks"
              f"  = {7 * math.log(2) / lam:6.1f} days")
        print(f"      mean residence 1/lambda  : {1 / lam:7.2f} weeks"
              f"  = {7 / lam:6.1f} days")

    print("\n[2] WHAT THE SLOW TAIL BOUNDS")
    pts = [(w, mean(DATA[w])) for w in (5, 6, 7, 8, 10, 12)]
    a, b, r2 = loglinfit(pts)
    lam = -b
    print(f"    lambda_obs = {lam:.4f}/week combines division and efflux.")
    print(f"    Since lambda_division <= lambda_obs,")
    print(f"      T_stem(mouse resting zone) >= {7 / lam:.0f} days"
          "        [LOWER BOUND]")
    print("    If efflux out of the resting zone accounts for half the loss,")
    print(f"      T_stem >= {14 / lam:.0f} days.")
    print("    Both readings are far slower than any rat value in the graph.")

    print("\n[3] AGREEMENT WITH THE ROUND-194 EdU BOUND")
    print("    Round 194 swept the EdU labelling index over assumed S-phase")
    print("    durations and got 10-59 d, with the upper end unbounded because")
    print("    the labelling index's lower 1 s.d. bound touches zero.")
    print(f"    The dilution tail lands at {7 / lam:.0f} d, at the far end of that")
    print("    sweep. Two independent readouts of the same mice converge on the")
    print("    SLOW answer. The mouse resting zone divides on a timescale of")
    print("    months, not days.")

    print("\n[4] THE CONFLICT THIS CREATES WITH hunziker1994, AND WHY ROUND 183")
    print("    SURVIVES IT")
    print("    hunziker1994 author-stated T_stem, rat proximal tibia:")
    print("      hypophysectomised 50 d | +IGF-I 15 d | +GH 8 d | intact 6 d")
    print(f"    Mouse lower bound here: {7 / lam:.0f} d. That is 10x the intact rat")
    print("    value and the two cannot both describe the same quantity.")
    print("    Three candidate reconciliations, none excluded by these data:")
    print("      (a) the LRC gate (top 10% H2B-EGFP) selects the slowest tail of")
    print("          a heterogeneous resting zone, so this is not the mean;")
    print("      (b) mouse and rat resting zones genuinely differ;")
    print("      (c) hunziker1994's 'germinal cell' compartment is broader than")
    print("          the label-retaining fraction and includes faster cells.")
    print("    ROUND 183 IS NOT AFFECTED. Its conclusion is a set of RATIOS")
    print("    between four conditions measured by ONE method in ONE paper -")
    print("    GH gives 5.00x pool consumption, 1.36x terminal cell height and")
    print("    0.77x amplification. A systematic scale error in T_stem common to")
    print("    all four conditions cancels in every ratio. What does not survive")
    print("    is the ABSOLUTE amplification figure of 23-32 cells per")
    print("    progenitor, which scales inversely with T_stem and is now")
    print("    value_unverified.")
    print("=" * 76)


if __name__ == "__main__":
    main()
