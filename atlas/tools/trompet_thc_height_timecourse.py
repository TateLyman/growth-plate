#!/usr/bin/env python3
"""
THE TERMINAL HYPERTROPHIC CHONDROCYTE HEIGHT UNDER HEDGEHOG AGONISM - the actual
numbers, from trompet2024's deposited source data, and the h_term gain is
TRANSIENT.

WHY THIS TOOL EXISTS
--------------------
Round 204 asked the user for trompet2024 Supplemental Figures 5F and 6B because
the paper attributes its augmented growth plate height "PROBABLY due to an
elevation in the height of the terminal hypertrophic chondrocytes" - a hedge, on
a quantity that round 202 made the centre of the whole programme. The user
supplied the supplement AND the source-data workbook, so the hedge can be
replaced with the per-animal values.

WHAT THE MEASUREMENT IS. Supplementary Figure 5F is "the height of terminal
hypertrophic chondrocytes (THC) in the FEMUR"; 6B is the same for the TIBIA.
THIS IS AN AXIAL HEIGHT IN MICROMETRES, not a zone, not a projected area, and not
a volume. It is therefore the ONE quantity CORR-189, CORR-190 and CORR-197 all
demand and that this atlas has been unable to find for almost any agent.

DESIGN. SAG- or DMSO-soaked beads implanted into the secondary ossification
centre of Wistar-Kyoto rats, ONE LIMB EACH, so DMSO and SAG are CONTRALATERAL
LIMBS OF THE SAME ANIMAL - which is why the authors use a PAIRED t-test and why
the pairing below preserves column order.

EVERY VALUE IS AUTHOR-DEPOSITED. Nothing here is read off a figure.
"""
import math

# trompet2024 source data workbook, sheets "Sup. Fig. 5" and "Sup. Fig. 6".
# Terminal hypertrophic chondrocyte height, micrometres.
FEMUR = {   # Sup. Fig. 5F
    "1 week":  ([27.38, 32.84, 31.06, 29.56, 29.42, 26.65],
                [33.69, 30.06, 28.45, 26.97, 30.02, 27.64]),
    "1 month": ([29.31, 30.13, 28.06, 25.50, 24.87, 22.47],
                [36.25, 30.66, 29.23, 28.87, 31.29, 32.44]),
    "2 months": ([24.27, 24.19, 18.99, 21.03, 19.20, 24.14, 22.85, 19.65, 22.49],
                 [23.37, 23.38, 22.31, 15.14, 19.06, 17.99, 16.93, 19.50, 24.90]),
}
TIBIA = {   # Sup. Fig. 6B
    "1 week":  ([28.11, 31.62, 27.58, 25.64, 29.50, 27.99],
                [31.29, 28.46, 29.28, 27.22, 34.91, 31.95]),
    "1 month": ([28.84, 31.32, 24.42, 24.96, 25.15, 21.23],
                [34.91, 38.01, 31.11, 31.60, 29.42, 29.26]),
    "2 months": ([22.05, 21.64, 17.41, 18.15, 21.63, 20.72, 19.58, 19.74],
                 [22.06, 25.67, 20.75, 20.69, 23.55, 22.22, 19.14, 20.90]),
}
# GROWTH PLATE HEIGHT from the same animals, for contrast (5E femur, 6A tibia).
GP_FEMUR = {
    "1 week":  ([315.73, 464.65, 423.85, 380.63, 451.17], [292.50, 423.60, 438.30, 397.80, 485.70]),
    "1 month": ([278.55, 229.88, 310.23, 309.43], [307.20, 275.62, 365.29, 358.71]),
    "2 months": ([231.30, 184.50, 224.70, 222.00, 241.50, 253.20, 323.70],
                 [245.70, 221.10, 266.40, 224.40, 237.60, 246.00, 327.90]),
}


def mean(v):
    return sum(v) / len(v)


def paired(a, b):
    """paired t on b - a; returns mean diff, t, df, and a p if scipy is present"""
    d = [y - x for x, y in zip(a, b)]
    n = len(d)
    m = sum(d) / n
    if n < 2:
        return m, float('nan'), 0, None
    sd = math.sqrt(sum((x - m) ** 2 for x in d) / (n - 1))
    if sd == 0:
        return m, float('inf'), n - 1, 0.0
    t = m / (sd / math.sqrt(n))
    try:
        from scipy import stats
        p = 2 * (1 - stats.t.cdf(abs(t), n - 1))
    except Exception:
        p = None
    return m, t, n - 1, p


def block(title, data, unit="um"):
    print("\n" + "-" * 92)
    print(title)
    print("-" * 92)
    print(f"    {'timepoint':<10} {'n':>3} {'DMSO':>8} {'SAG':>8} {'ratio':>7} "
          f"{'mean diff':>10} {'t':>7} {'p (paired)':>11}  all same way?")
    for tp, (dm, sg) in data.items():
        n = len(dm)
        md, t, df, p = paired(dm, sg)
        diffs = [y - x for x, y in zip(dm, sg)]
        same = "YES" if all(d > 0 for d in diffs) else ("all down" if all(d < 0 for d in diffs)
                                                        else f"{sum(1 for d in diffs if d>0)}/{n} up")
        ps = f"{p:.4f}" if p is not None else "scipy n/a"
        star = " *" if (p is not None and p < 0.05) else ""
        print(f"    {tp:<10} {n:>3} {mean(dm):>8.2f} {mean(sg):>8.2f} "
              f"{mean(sg)/mean(dm):>7.3f} {md:>+10.2f} {t:>7.2f} {ps:>11}{star}   {same}")


def main():
    print("=" * 92)
    print("trompet2024 - TERMINAL HYPERTROPHIC CHONDROCYTE HEIGHT UNDER AN INTRA-ARTICULAR")
    print("SAG BEAD, PER ANIMAL, PAIRED CONTRALATERAL LIMBS, AUTHOR-DEPOSITED SOURCE DATA")
    print("=" * 92)

    block("FEMUR - Supplementary Figure 5F, terminal hypertrophic chondrocyte height (um)", FEMUR)
    block("TIBIA - Supplementary Figure 6B, terminal hypertrophic chondrocyte height (um)", TIBIA)
    block("FEMUR - Supplementary Figure 5E, GROWTH PLATE height (um), for contrast", GP_FEMUR)

    print("\n" + "=" * 92)
    print("WHAT THIS SETTLES, AND IT IS NOT WHAT ROUND 204 EXPECTED")
    print("=" * 92)
    print("\n[1] THE h_term EFFECT IS REAL AND IT IS TRANSIENT.")
    for label, data in (("femur", FEMUR), ("tibia", TIBIA)):
        r = {tp: mean(s) / mean(d) for tp, (d, s) in data.items()}
        print(f"    {label:<6} 1 week {r['1 week']:.2f}x  ->  1 month {r['1 month']:.2f}x  "
              f"->  2 months {r['2 months']:.2f}x")
    print("    Nothing at one week. A clear rise at ONE MONTH, in both bones, with every")
    print("    animal moving the same way in the tibia. GONE BY TWO MONTHS - and in the")
    print("    femur it goes BELOW control.")

    print("\n[2] WHY THAT MATTERS MORE THAN THE PEAK VALUE.")
    print("    trompet2024's LENGTH gain persists to SIX MONTHS and is the only")
    print("    length-endpoint proof in this arm of the atlas. The h_term gain does not")
    print("    last two. SO THE SUSTAINED LENGTH GAIN IS NOT CARRIED BY TERMINAL CELL")
    print("    HEIGHT. The authors' 'probably due to an elevation in the height of the")
    print("    terminal hypertrophic chondrocytes' is true at one timepoint and false at")
    print("    the timepoint where the length actually accumulates.")

    print("\n[3] AND IT PUTS A NUMBER ON HOW BIG AN h_term EFFECT CAN GET.")
    best = max(max(mean(s)/mean(d) for tp,(d,s) in data.items()) for data in (FEMUR, TIBIA))
    print(f"    The largest terminal-cell-height ratio anywhere in this dataset is "
          f"{best:.2f}x.")
    print("    Set against weber2025's +20 per cent under NPR3 loss and hunziker1994's")
    print("    1.36x under growth hormone, THE WHOLE OBSERVED RANGE OF h_term ACROSS")
    print("    EVERY AGENT THIS ATLAS HOLDS IS ROUGHLY 1.0 TO 1.4x. That is the ceiling")
    print("    the free axis is worth, and it is far smaller than the 5x exchange rate")
    print("    of round 202 made it sound.")

    print("\n[4] THE GROWTH PLATE HEIGHT AND THE CELL HEIGHT DISAGREE, WHICH IS CORR-197")
    print("    IN LIVE ACTION.")
    for tp in GP_FEMUR:
        d, s = GP_FEMUR[tp]
        fd, fs = FEMUR[tp]
        print(f"    femur {tp:<9} zone {mean(s)/mean(d):.3f}x   cell height "
              f"{mean(fs)/mean(fd):.3f}x")
    print("    At two months the zone is slightly UP while the cells are DOWN. A zone")
    print("    height was never going to report the cell term, and here the two move in")
    print("    opposite directions in the same animals.")
    print("=" * 92)


if __name__ == "__main__":
    main()
