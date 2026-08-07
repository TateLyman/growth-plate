#!/usr/bin/env python3
"""Is the FGFR/klotho axis actually expressed in a HUMAN growth plate?

WHY THIS EXISTS
---------------
Two rounds of this atlas argued about whether FGFR4 inhibition should be pro-growth,
on the strength of a mouse paper in which FGF19 signals through FGFR4 WITH BETA-KLOTHO
to restrain cartilage growth. Neither round checked whether the ligand or the obligate
co-receptor are present in human growth plate. They are not (CORR-041). This script is
the check, kept so it cannot be skipped again.

SOURCE AND ITS BIAS
-------------------
GSE288028 (Chagin / Savendahl): four human epiphysiodesis needle biopsies, the ONLY
directly-processed fresh human samples in the series. THE DONORS ARE NOT TYPICAL - the
surgery was performed to PREVENT IDIOPATHIC TALL STATURE, so every value here comes from
a plate selected for growing too much.

WHAT A LOW NUMBER MEANS
-----------------------
Droplet scRNA-seq detection is sparse. Low detection is WEAK evidence of absence and
protein can exist below it. A gene at 0% in all four donors alongside a positive control
at 90% is informative; a gene at 2% is not clearly anything. The threshold below is
arbitrary and is printed so it can be argued with.

Usage:
  python3 fgfr_axis_expression.py --h5dir <dir with the four GSM .h5 files>
"""
import argparse, os, sys

FRESH = {  # ONLY the directly-processed fresh human samples
    "GSM9328218_P30453_1001.h5": "donor1",
    "GSM9328221_P31011_1001.h5": "donor2",
    "GSM9328224_P25452_001.h5": "donor3",
    "GSM9328229_P22202_1015.h5": "donor4",
}
DETECT_PCT = 1.0

PANELS = {
    "FGFR receptors": ["FGFR1", "FGFR2", "FGFR3", "FGFR4"],
    "klotho co-receptors (endocrine FGF signalling requires these)": ["KLB", "KL"],
    "endocrine FGF ligands": ["FGF19", "FGF21", "FGF23"],
    "paracrine FGF ligands": ["FGF2", "FGF18"],
    "CNP axis": ["NPPC", "NPR2", "NPR3"],
    "reservoir markers (qu2025)": ["GLI1", "PDGFRA", "PTCH1", "AXIN2"],
    "Wnt antagonists (the FGF19/FGFR4 output)": ["SFRP1", "WIF1", "DKK2"],
    "cartilage controls": ["COL2A1", "ACAN", "COL10A1"],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h5dir", required=True)
    a = ap.parse_args()
    import h5py, numpy as np, scipy.sparse as sp

    genes = [g for panel in PANELS.values() for g in panel]
    res = {g: {} for g in genes}
    ncells = {}
    for fn, dn in FRESH.items():
        p = os.path.join(a.h5dir, fn)
        if not os.path.exists(p):
            print(f"MISSING {p} - refusing to build a partial table", file=sys.stderr)
            return 1
        with h5py.File(p, "r") as f:
            g = f["matrix"]
            shape = tuple(g["shape"][:])
            M = sp.csc_matrix((g["data"][:], g["indices"][:], g["indptr"][:]),
                              shape=shape).tocsr()
            names = np.array([x.decode() for x in g["features/name"][:]])
        ncells[dn] = int(shape[1])
        for gene in genes:
            idx = np.where(names == gene)[0]
            res[gene][dn] = (None if len(idx) == 0 else
                             100.0 * np.count_nonzero(M[idx[0]].toarray().ravel()) / shape[1])

    dns = ["donor1", "donor2", "donor3", "donor4"]
    print("GSE288028 - four fresh human growth plate biopsies (epiphysiodesis for TALL stature)")
    print("cells per donor:", {d: ncells[d] for d in dns})
    print(f"detection threshold: >= {DETECT_PCT}% of cells\n")
    for title, panel in PANELS.items():
        print(title)
        print(f"  {'gene':<9}" + "".join(f"{d:>10}" for d in dns) + "   n donors")
        for gene in panel:
            r = res[gene]
            cells = "".join(f"{r[d]:>9.2f}%" if r[d] is not None else f"{'absent':>10}"
                            for d in dns)
            det = sum(1 for d in dns if r[d] is not None and r[d] >= DETECT_PCT)
            print(f"  {gene:<9}{cells}   {det}/4")
        print()
    print("READ THIS BEFORE USING THE TABLE: donor3 is by far the most chondrocyte-pure and")
    print("hypertrophic-rich sample (COL2A1 100%, COL10A1 94%), so its values are not")
    print("comparable to the others - a gene high only in donor3 is plausibly hypertrophic-zone")
    print("restricted rather than more abundant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
