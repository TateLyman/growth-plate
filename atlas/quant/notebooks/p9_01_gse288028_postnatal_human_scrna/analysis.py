#!/usr/bin/env python3
"""
GSE288028 - POSTNATAL HUMAN GROWTH PLATE single-cell RNA-seq. Operator-supplied 2026-08-11,
unopened until round 308.

WHY THIS MATTERS MORE THAN ANY OTHER DATASET IN THIS ATLAS. Every expression call this file
has made about human growth plate - PDE3B, AGTR1, TNKS, the Gs-receptor shelf, HHIP, NRK,
LOXL2, the whole CORR-327 receiver rule - rests on GSE9160: a 2007 microarray, TWO donors,
one of whom had a failed dissection, and a platform demonstrably blind to low-abundance
transcripts. Its own notebook records that it missed NPPC - vosoritide's own ligand - by one
to two orders of magnitude while detecting NPR2 and NPR3. Every "absent" call in this atlas
therefore carries an unquantified false-negative rate.

THE PREREGISTERED CONTROL, DECLARED BEFORE LOOKING. NPPC is the calibrator. GSE9160 scored it
0/5 in both donors. If this dataset detects NPPC in a reasonable fraction of chondrocytes,
then (a) the sensitivity gap is demonstrated rather than assumed, and (b) every GSE9160
non-detection in this atlas becomes provisional and must be re-checked here. If this dataset
ALSO misses NPPC, the GSE9160 calls stand and this notebook has settled that too.

METHOD, deliberately conservative.
  - Raw CellRanger h5 per sample; no integration, no batch correction, no clustering in this
    pass. Presence/absence and abundance only.
  - Two statistics per gene per sample: PSEUDOBULK CPM (sum of counts over cells, per million)
    and PERCENT OF CELLS with at least one count. The second is what a microarray cannot give
    and is the honest presence statistic for a sparse assay.
  - A gene is called DETECTED in a sample at >=1% of cells AND >=1 CPM. Reported per sample,
    never pooled, so a single outlier sample cannot manufacture a call.
  - Duplicate gene symbols are summed (CellRanger carries multiple IDs per symbol).

WHAT THIS PASS CANNOT DO. Fourteen samples with no metadata parsed here - donor age, sex,
anatomical site and zone are NOT resolved, so this gives WHOLE-TISSUE presence and nothing
zonal. GSE9160 remains the only zone-resolved human source and this does not replace it; it
calibrates it. Cell-type assignment is left to a second pass.

Usage: python3 analysis.py <dir_of_h5>
"""
import os
import sys
import glob
import numpy as np
import h5py
from scipy.sparse import csc_matrix


def load(path):
    with h5py.File(path, "r") as f:
        g = f["matrix"]
        data = g["data"][:]
        indices = g["indices"][:]
        indptr = g["indptr"][:]
        shape = tuple(g["shape"][:])
        names = np.array([x.decode() for x in g["features"]["name"][:]])
    # CellRanger stores CSC with genes as rows, cells as columns
    m = csc_matrix((data, indices, indptr), shape=shape)
    return m, names


def summarise(m, names):
    """Return per-gene total counts and number of cells with >=1 count."""
    m = m.tocsr()
    total = np.asarray(m.sum(axis=1)).ravel()
    ncell = np.asarray((m > 0).sum(axis=1)).ravel()
    # collapse duplicate symbols
    order = {}
    for i, s in enumerate(names):
        order.setdefault(s, []).append(i)
    syms = sorted(order)
    tot = np.array([total[order[s]].sum() for s in syms], dtype=float)
    nc = np.array([ncell[order[s]].max() for s in syms], dtype=float)
    return syms, tot, nc, m.shape[1]


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    files = sorted(glob.glob(os.path.join(d, "*.h5")))
    print("GSE288028 - postnatal human growth plate scRNA-seq; %d samples" % len(files))
    per = []
    for fp in files:
        m, names = load(fp)
        syms, tot, nc, ncells = summarise(m, names)
        cpm = tot / max(tot.sum(), 1) * 1e6
        pct = nc / max(ncells, 1) * 100.0
        per.append((os.path.basename(fp), dict(zip(syms, zip(cpm, pct))), ncells))
        print("  %-34s %6d cells  %8d counts" % (os.path.basename(fp), ncells, int(tot.sum())))
    return per


if __name__ == "__main__":
    main()
