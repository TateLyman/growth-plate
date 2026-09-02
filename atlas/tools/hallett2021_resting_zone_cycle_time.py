#!/usr/bin/env python3
"""
Mouse resting-zone cell-cycle time from Hallett 2021 EdU labelling indices.

WHY THIS EXISTS
---------------
The Hunziker identity used throughout this atlas is

    GR = A * D * h_term ,  with  D = N_rest / T_stem

and T_stem -- the resting-zone (stem) cell-cycle time -- has so far been
available only from Hunziker 1994's rat hypophysectomy series (6-50 d,
author-stated). Round 194 adds an independent, species-different anchor:
Hallett 2021 (eLife 10:e64513) reports flow-cytometry EdU labelling indices
for label-retaining chondrocytes (LRCs, the slow-cycling resting-zone
population) versus non-LRCs in mouse growth plate.

AUTHOR-STATED INPUTS (Hallett 2021, Results / Figure 4e; mean +/- s.d.)
    EdU pulses: two doses, 6 h and 3 h before sacrifice.
    1 week chase (P28):  LRC 2.04 +/- 1.67 %   non-LRC 7.04 +/- 2.30 %  n=6  p=0.002
    2 week chase (P35):  LRC 1.13 +/- 0.74 %   non-LRC 2.80 +/- 1.00 %  n=8  p=0.047
    4 week chase (P49):  LRC 2.40 +/- 0.85 %   non-LRC 4.34 +/- 1.89 %  n=4  p=0.200 (ns)

WHAT IS DERIVED HERE AND WHAT IS ASSUMED
----------------------------------------
Ratio LRC:non-LRC is a direct quotient of author-stated numbers. It needs no
assumption beyond "S-phase duration is similar in the two populations".

Absolute cycle time needs T_c = T_eff / LI, where T_eff = T_S + w is the
effective labelling window (S-phase duration plus the time EdU was
bioavailable). NEITHER T_S NOR w IS REPORTED BY HALLETT. They are swept here
over a declared range and every output is labelled value_unverified. Do not
promote any single number out of this sweep into the graph as a measurement.

Also assumed: every LRC is cycling (growth fraction = 1). If a fraction of
LRCs is permanently out of cycle, the true cycle time of the cycling subset is
SHORTER than computed here and the pool is more heterogeneous than one number.
"""

# ---------------------------------------------------------------- inputs
# author-stated, Hallett 2021 Figure 4e
LI = {
    #  chase weeks : (LRC %, LRC sd, nonLRC %, nonLRC sd, n, p)
    1: (2.04, 1.67, 7.04, 2.30, 6, 0.002),
    2: (1.13, 0.74, 2.80, 1.00, 8, 0.047),
    4: (2.40, 0.85, 4.34, 1.89, 4, 0.200),
}

# assumed, NOT from Hallett -- swept
T_S_RANGE = [4.0, 6.0, 8.0, 10.0]      # hours, S-phase duration
W_RANGE = [1.0, 3.0, 6.0]              # hours, EdU bioavailability window
                                       # 1 h  = short-bioavailability assumption
                                       # 3 h  = second pulse to sacrifice
                                       # 6 h  = first pulse to sacrifice


def main():
    print("=" * 74)
    print("HALLETT 2021 -- MOUSE RESTING-ZONE CYCLING, DERIVED")
    print("=" * 74)

    print("\n[1] ASSUMPTION-FREE QUANTITY: LRC / non-LRC labelling ratio")
    print("    (valid if S-phase duration is comparable in the two fractions)")
    print(f"    {'chase':>6} {'LRC %':>8} {'nonLRC %':>9} {'ratio':>8}  {'p':>6}")
    for wk, (l, lsd, n, nsd, nn, p) in LI.items():
        print(f"    {wk:>5}w {l:>8.2f} {n:>9.2f} {n / l:>8.2f}  {p:>6.3f}")
    print("\n    The resting-zone fraction incorporates EdU 2.5-3.5x less often")
    print("    than the non-resting fraction. At 4 weeks the separation is not")
    print("    significant (n=4) -- the 4-week point does not support the claim.")

    print("\n[2] ABSOLUTE CYCLE TIME -- ASSUMPTION-DEPENDENT SWEEP")
    print("    T_c = (T_S + w) / LI ;  T_S and w are ASSUMED, not measured.")
    for wk in (1, 2):
        l, lsd, n, nsd, nn, p = LI[wk]
        print(f"\n    --- {wk} week chase --- LRC LI = {l:.2f}% "
              f"(sd {lsd:.2f}, n={nn})")
        print(f"      {'T_S(h)':>7} " + " ".join(f"{'w=%.0fh' % w:>12}" for w in W_RANGE))
        for ts in T_S_RANGE:
            cells = []
            for w in W_RANGE:
                tc_h = (ts + w) / (l / 100.0)
                cells.append(f"{tc_h / 24.0:>9.1f} d")
            print(f"      {ts:>7.1f} " + " ".join(f"{c:>12}" for c in cells))

    print("\n[3] RANGE ACROSS THE WHOLE SWEEP (1- and 2-week chase, LRC)")
    vals = []
    for wk in (1, 2):
        l = LI[wk][0]
        for ts in T_S_RANGE:
            for w in W_RANGE:
                vals.append((ts + w) / (l / 100.0) / 24.0)
    print(f"    T_stem(mouse, LRC) = {min(vals):.1f} to {max(vals):.1f} days"
          "   [value_unverified: true]")

    print("\n[4] SENSITIVITY TO THE LABELLING INDEX ITSELF")
    print("    The s.d. on the 1-week LRC index (1.67 on a mean of 2.04) is")
    print("    82% of the mean. Propagating +/-1 s.d. at T_S=6 h, w=3 h:")
    l, lsd = LI[1][0], LI[1][1]
    for tag, li in (("mean - 1sd", l - lsd), ("mean", l), ("mean + 1sd", l + lsd)):
        if li <= 0:
            print(f"      {tag:>11}: LI <= 0, cycle time unbounded")
            continue
        print(f"      {tag:>11}: LI={li:5.2f}%  T_c = {9.0 / (li / 100.0) / 24.0:7.1f} d")
    print("    The lower bound on LI is within noise of zero, so the upper")
    print("    bound on T_stem from this dataset is UNBOUNDED. This measurement")
    print("    constrains T_stem from below only.")

    print("\n[5] COMPARISON WITH THE RAT ANCHOR ALREADY IN THE GRAPH")
    print("    Hunziker 1994 T_stem (rat proximal tibia, author-stated):")
    print("      hypophysectomised + NaCl : 50 d")
    print("      hypox + IGF-I            : 15 d")
    print("      hypox + GH               :  8 d")
    print("      intact normal            :  6 d")
    print("    The mouse LRC sweep overlaps the hypophysectomised end of that")
    print("    range and not the intact end. Two readings are possible and this")
    print("    dataset cannot separate them:")
    print("      (a) mouse resting-zone turnover really is slower than rat, or")
    print("      (b) the LRC gate (top 10% H2B-EGFP) selects the slowest tail")
    print("          of a heterogeneous resting zone, so the LI understates")
    print("          mean resting-zone cycling.")
    print("    (b) is the gating definition Hallett states, so (b) cannot be")
    print("    excluded. Recorded as a range, not a point, grade E.")

    print("\n[6] WHAT THIS DOES *NOT* ANSWER")
    print("    No PTH1R agonist was administered in Hallett 2021. This supplies")
    print("    a baseline T_stem for mouse; it does not supply T_stem under")
    print("    teriparatide, which remains unmeasured in every species.")
    print("=" * 74)


if __name__ == "__main__":
    main()
