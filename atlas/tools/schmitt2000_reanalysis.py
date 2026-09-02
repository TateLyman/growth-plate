#!/usr/bin/env python3
"""
Re-analysis of schmitt2000 Table 1 and Table 2: does intermittent PTH(1-37)
lengthen a PAIR-FED HEALTHY rat, or only a uraemic one?

WHY THIS MATTERS
----------------
Round 195 closed on a specific demand: every femoral-length gain under a PTH1R
agonist was female and rode on a body-weight gain, and the discriminating
experiment named in gap g_l12_is_the_pth1r_length_gain_only_body_weight was a
PAIR-FED arm. schmitt2000 experiment 2 IS that arm - sham-operated pair-fed
controls, and the authors state PTH "did not influence body weight gain and
food conversion ratio. However, there was a significant increase in length
gain in uremic animals, as well as in sham-operated pair fed controls."

If that holds, the body-weight explanation dies and the line reopens. So it has
to be checked rather than accepted, in both directions: the positive claim on
length AND the null claim on weight.

AUTHOR-STATED INPUTS, mean +/- SEM, transcribed from the paper's tables.
The paper analysed by ANOVA followed by DUNCAN'S multiple range test, which is
among the most permissive post-hoc procedures available. Recomputing the
pairwise contrasts as two-sample t-tests is not a criticism of the paper; it is
the only way to know how much of the reported significance is Duncan's.
"""
import math
from scipy import stats

# experiment 2: 14 d, PTH(1-37) 30 ug/kg b.i.d., n=7/group, PAIR-FED controls
EXP2 = {
    "weight gain (g)": {
        "controls solvent": (44.4, 2.5, 7), "controls PTH": (52.8, 8.1, 7),
        "uremia solvent":   (41.2, 3.2, 7), "uremia PTH":   (51.3, 7.9, 7),
    },
    "food conversion ratio (g/g)": {
        "controls solvent": (0.23, 0.01, 7), "controls PTH": (0.26, 0.03, 7),
        "uremia solvent":   (0.23, 0.01, 7), "uremia PTH":   (0.26, 0.02, 7),
    },
    "length gain, snout to tail tip (cm)": {
        "controls solvent": (5.35, 0.37, 7), "controls PTH": (6.19, 0.47, 7),
        "uremia solvent":   (4.78, 0.20, 7), "uremia PTH":   (6.17, 0.36, 7),
    },
}
# experiment 3: 21 d, uraemic only, n=11/group
EXP3 = {
    "weight gain (g)": {"solvent": (37.4, 1.9, 11), "PTH": (45.2, 2.9, 11)},
    "food intake (g)": {"solvent": (213, 6, 11),    "PTH": (210, 7, 11)},
    "food conversion ratio (g/g)": {"solvent": (0.18, 0.01, 11),
                                    "PTH": (0.21, 0.01, 11)},
}


def sd(sem, n):
    return sem * math.sqrt(n)


def ttest(a, b):
    m1, s1, n1 = a
    m2, s2, n2 = b
    sd1, sd2 = sd(s1, n1), sd(s2, n2)
    sp = math.sqrt(((n1 - 1) * sd1 ** 2 + (n2 - 1) * sd2 ** 2) / (n1 + n2 - 2))
    se = sp * math.sqrt(1.0 / n1 + 1.0 / n2)
    t = (m2 - m1) / se
    df = n1 + n2 - 2
    p = 2 * (1 - stats.t.cdf(abs(t), df))
    d = (m2 - m1) / sp
    tcrit = stats.t.ppf(0.975, df)
    mdd80 = (tcrit + 0.84) * se
    return t, df, p, d, sp, mdd80


def block(title, contrasts):
    print(f"\n--- {title} ---")
    print(f"    {'contrast':>42} {'diff':>8} {'t':>6} {'p':>8} "
          f"{'Cohen d':>8} {'MDD@80%':>9}")
    for lab, a, b in contrasts:
        t, df, p, d, sp, mdd = ttest(a, b)
        flag = "  <-- sig" if p < 0.05 else ""
        print(f"    {lab:>42} {b[0] - a[0]:>8.2f} {t:>6.2f} {p:>8.4f} "
              f"{d:>8.2f} {mdd:>9.2f}{flag}")


def main():
    print("=" * 92)
    print("schmitt2000 RE-ANALYSIS -- PAIR-FED CONTROLS, INTERMITTENT PTH(1-37)")
    print("=" * 92)
    print("Design: female Sprague-Dawley rats, 133.5 g at start (actively")
    print("growing), two-stage subtotal nephrectomy or sham, 14 d of PTH(1-37)")
    print("30 ug/kg TWICE DAILY subcutaneously = 60 ug/kg/day. Sham controls in")
    print("experiment 2 were PAIR FED. Endpoint: snout-to-tail-tip length.")

    for measure, g in EXP2.items():
        block(f"experiment 2, {measure}",
              [("sham pair-fed: solvent vs PTH",
                g["controls solvent"], g["controls PTH"]),
               ("uraemic: solvent vs PTH",
                g["uremia solvent"], g["uremia PTH"]),
               ("solvent: sham vs uraemic",
                g["controls solvent"], g["uremia solvent"])])

    for measure, g in EXP3.items():
        block(f"experiment 3 (uraemic only, n=11), {measure}",
              [("solvent vs PTH", g["solvent"], g["PTH"])])

    print("\n" + "=" * 92)
    print("[1] THE HEADLINE SPLITS IN TWO AND ONLY HALF OF IT SURVIVES")
    print("=" * 92)
    t, df, p, d, sp, mdd = ttest(EXP2["length gain, snout to tail tip (cm)"]["controls solvent"],
                                 EXP2["length gain, snout to tail tip (cm)"]["controls PTH"])
    print(f"    SHAM PAIR-FED length gain: +0.84 cm, t={t:.2f}, p={p:.3f}, "
          f"d={d:.2f}")
    print("    -> NOT significant as a two-sample t-test. The paper's")
    print("       significance for this contrast comes from ANOVA followed by")
    print("       DUNCAN'S test across four groups.")
    t, df, p, d, sp, mdd = ttest(EXP2["length gain, snout to tail tip (cm)"]["uremia solvent"],
                                 EXP2["length gain, snout to tail tip (cm)"]["uremia PTH"])
    print(f"    URAEMIC length gain      : +1.39 cm, t={t:.2f}, p={p:.4f}, "
          f"d={d:.2f}")
    print("    -> robustly significant by any test.")

    print("\n[2] THE PATTERN IS RESCUE, NOT SUPRANORMAL GROWTH")
    print("    sham solvent 5.35 -> sham PTH 6.19 (ns on recomputation)")
    print("    uraemic solvent 4.78 -> uraemic PTH 6.17")
    print("    Uraemia costs 0.57 cm of length gain. PTH restores the uraemic")
    print("    animal to 6.17, which is the SAME as the treated sham (6.19) and")
    print("    above the untreated sham (5.35). Whether PTH pushes a healthy")
    print("    animal past its own ceiling is exactly the contrast that fails")
    print("    to reach significance.")

    print("\n[3] THE 'NO WEIGHT EFFECT' CLAIM IS AN UNDERPOWERED NULL")
    t, df, p, d, sp, mdd = ttest(EXP2["weight gain (g)"]["controls solvent"],
                                 EXP2["weight gain (g)"]["controls PTH"])
    print(f"    sham pair-fed weight gain: 44.4 -> 52.8 g, +19%, p={p:.2f}")
    print(f"    minimum detectable difference at 80% power: {mdd:.1f} g, i.e.")
    print(f"    {100 * mdd / 44.4:.0f}% of the control's own weight gain.")
    print("    A 19% weight-gain difference is not detectable in this design.")
    print("    'Did not influence body weight gain' therefore does not")
    print("    establish that body weight is uninvolved.")
    t, df, p, d, sp, mdd = ttest(EXP3["weight gain (g)"]["solvent"],
                                 EXP3["weight gain (g)"]["PTH"])
    print(f"    AND IN EXPERIMENT 3, WITH n=11, IT IS SIGNIFICANT: 37.4 -> "
          f"45.2 g, p={p:.4f},")
    print("    at IDENTICAL food intake (213 vs 210 g, ns) - so PTH raised feed")
    print("    efficiency. The larger experiment finds the weight effect the")
    print("    smaller one was too small to see.")

    print("\n[4] WHAT SURVIVES, PRECISELY")
    print("    (a) CONTINUOUS infusion of PTH(1-37) at the same daily dose did")
    print("        NOT alter length gain; INTERMITTENT did. That schedule")
    print("        contrast is internal to the paper and is the cleanest thing")
    print("        in it.")
    print("    (b) In URAEMIC growing rats, intermittent PTH(1-37) restores")
    print("        length gain. Robust.")
    print("    (c) In HEALTHY pair-fed growing rats the point estimate is +16%")
    print("        but the contrast does not survive a pairwise test at n=7.")
    print("    (d) The pair-feeding does NOT settle the body-weight question,")
    print("        because pair-feeding equalises INTAKE, not weight, and PTH")
    print("        raised feed efficiency in the experiment large enough to see")
    print("        it.")

    print("\n[5] WHAT IS STILL NOT MEASURED HERE")
    print("    Snout-to-tail-tip is not a bone. No femur or tibia length, no")
    print("    growth plate histology, no cells per column, no terminal")
    print("    hypertrophic cell height. pQCT was cross-sectional only")
    print("    (metaphysis and diaphysis), so it carries no length information.")
    print("=" * 92)


if __name__ == "__main__":
    main()
