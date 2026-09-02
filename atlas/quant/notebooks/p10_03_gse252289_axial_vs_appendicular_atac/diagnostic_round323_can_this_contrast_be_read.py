#!/usr/bin/env python3
"""
ROUND 323 DIAGNOSTIC, run because the first pass FAILED ITS OWN CONTROLS and the honest
response to that is to find out why rather than to report the table anyway.

WHAT THE FIRST PASS PRODUCED. A base-rate distribution whose 90th percentile was log2 = +11.8,
which can only happen when the appendicular denominator is exactly zero across a tenth of the
genome. The "discovery" list was then dominated by one contiguous block: HLA-A, HLA-E, HLA-F,
HLA-DPA1, HLA-DPB1, B2M, TAPBP, BAG6, PRRC2A, CSNK2B, SKIV2L, RXRB, RING1, VPS52 - the MHC on
chr6 plus its antigen-presentation partner B2M on chr15. And B2M was one of the HOUSEKEEPING
controls that was written down in advance as MUST-BE-NEITHER.

THE MEASUREMENT. chr6:29-33 Mb carries 223,681 bp of peak in LUMBAR and 220,492 in THORACIC
against 0 to 4,511 bp in each of the eight E67 appendicular sheets - a 50-200 fold difference
in one 4 Mb block, while every chromosome's share of total peak bp matches to within a few
tenths of a percent across all sheets. So it is not a whole-chromosome dropout and it is not
depth.

THE LIKELY CAUSE, and it is biological but not the biology wanted: FETAL VERTEBRAL BODIES ARE
A HAEMATOPOIETIC ORGAN. An antigen-presentation signature (MHC class I, class II, B2M, TAPBP)
appearing in vertebral tissue and not in limb cartilage is what marrow or blood contamination
looks like. Either way the contrast between axial and appendicular sheets is not a clean
cartilage-versus-cartilage comparison.

THIS SCRIPT re-runs the same contrast with three corrections and re-reads the controls:
  1. chr6:28-34 Mb excluded outright.
  2. pseudocount = the genome-wide MEDIAN window density rather than 1e-3, so a zero
     denominator cannot manufacture a log2 of 16.
  3. windows required to have signal in BOTH arms.
The controls are the same ones written before the first pass. If they still do not separate,
the dataset answers a different question than the one asked and that is the result.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis import (AXIAL, APP54, APP67, FLANK, build_index, covered_bp,  # noqa: E402
                      load_genes, load_peaks)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
OUT = os.path.join(ROOT, "data", "round323")
GTF = os.environ["GRCH37_GTF"]
MHC = ("chr6", 28000000, 34000000)

CONTROLS = [
    ("TBX5", "APPENDICULAR"), ("TBX4", "APPENDICULAR"), ("PITX1", "APPENDICULAR"),
    ("HOXA13", "APPENDICULAR"), ("HOXD13", "APPENDICULAR"), ("SHOX2", "APPENDICULAR"),
    ("PAX1", "AXIAL"), ("PAX9", "AXIAL"), ("NKX3-2", "AXIAL"), ("MEOX1", "AXIAL"),
    ("UNCX", "AXIAL"), ("TBX6", "AXIAL"),
    ("ACTB", "NEITHER"), ("GAPDH", "NEITHER"), ("RPL13A", "NEITHER"), ("B2M", "NEITHER"),
    ("COL2A1", "NEITHER"), ("ACAN", "NEITHER"), ("SOX9", "NEITHER"), ("COL9A1", "NEITHER"),
]


def main():
    peaks = load_peaks()
    idx, tot = build_index(peaks)
    genes = load_genes(GTF)

    def dens(sheets, ch, lo, hi):
        return sum(covered_bp(idx[s], ch, lo, hi) / float(tot[s]) * 1e6
                   for s in sheets) / len(sheets)

    rows = {}
    for sym, (ch, st, en) in genes.items():
        lo, hi = max(1, st - FLANK), en + FLANK
        if ch == MHC[0] and hi > MHC[1] and lo < MHC[2]:
            continue                                  # correction 1
        a, p67, p54 = dens(AXIAL, ch, lo, hi), dens(APP67, ch, lo, hi), dens(APP54, ch, lo, hi)
        rows[sym] = (a, p67, p54)

    both = [v for v in rows.values() if v[0] > 0 and v[1] > 0]
    med = sorted(v[1] for v in both)[len(both) // 2]   # correction 2: pseudocount
    print("windows outside MHC: %d; with signal in BOTH arms: %d; median appendicular "
          "density %.2f (used as pseudocount)" % (len(rows), len(both), med))

    l2 = {s: math.log((v[0] + med) / (v[1] + med), 2)
          for s, v in rows.items() if v[0] > 0 and v[1] > 0}   # correction 3
    vals = sorted(l2.values())
    n = len(vals)

    def pct(x):
        import bisect
        return 100.0 * bisect.bisect_left(vals, x) / n

    print("\nBASE RATE after corrections, n=%d" % n)
    print("  p1 %+0.2f  p10 %+0.2f  p25 %+0.2f  MEDIAN %+0.2f  p75 %+0.2f  p90 %+0.2f  p99 %+0.2f"
          % (vals[n // 100], vals[n // 10], vals[n // 4], vals[n // 2], vals[3 * n // 4],
             vals[9 * n // 10], vals[99 * n // 100]))
    print("  fraction above the median is 50%% by construction; the spread is what matters")

    print("\nCONTROLS")
    print("  %-9s %8s %8s  %7s %7s  %s" % ("gene", "axial", "app67", "l2", "pctile", "expected"))
    ok = bad = 0
    ctrl_out = []
    for sym, exp in CONTROLS:
        if sym not in l2:
            print("  %-9s excluded (MHC window or no signal)" % sym)
            continue
        a, p67, p54 = rows[sym]
        v, p = l2[sym], pct(l2[sym])
        call = "AXIAL" if p >= 80 else ("APPENDICULAR" if p <= 20 else "NEITHER")
        good = (call == exp)
        ok += good
        bad += (not good)
        ctrl_out.append(dict(gene=sym, expected=exp, axial=a, app67=p67, l2=v, pctile=p,
                             call=call, correct=good))
        print("  %-9s %8.2f %8.2f  %+7.2f %6.1f  %-12s %s"
              % (sym, a, p67, v, p, exp, "OK" if good else "<<< FAILS"))
    print("\n  controls passed %d / %d" % (ok, ok + bad))
    verdict = ("READABLE" if ok >= 0.75 * (ok + bad) else
               "NOT READABLE - the contrast does not recover known limb/axial identity")
    print("  VERDICT: %s" % verdict)

    json.dump(dict(verdict=verdict, n_controls=ok + bad, n_passed=ok, controls=ctrl_out,
                   base_rate={"n": n, "p10": vals[n // 10], "median": vals[n // 2],
                              "p90": vals[9 * n // 10], "p99": vals[99 * n // 100]},
                   mhc_note="chr6:28-34Mb excluded; axial sheets carry ~220kb of MHC peak "
                            "against 0-4.5kb appendicular"),
              open(os.path.join(OUT, "axial_atac_control_diagnostic.json"), "w"), indent=1)
    print("\nwrote axial_atac_control_diagnostic.json")


if __name__ == "__main__":
    main()
