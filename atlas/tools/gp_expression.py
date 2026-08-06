#!/usr/bin/env python3
"""
gp_expression.py - is this gene expressed in a HUMAN growth plate at all?

WHY THIS EXISTS
---------------
Any screen that proposes a molecular target for the growth plate has one cheap, brutal
filter available before anything else: is the target transcribed in human growth-plate
tissue? A target that is not detected in any donor is not thereby excluded - transcript
absence is weak evidence and protein can exist below detection - but a target detected
in every donor at a high fraction of cells is materially more plausible than one seen
in none, and the difference is free to compute.

SOURCE
------
GSE288028 (Chagin / Savendahl). FOUR human epiphysiodesis needle biopsies from children
in puberty stages B2-B4.

**THE DONORS ARE NOT TYPICAL CHILDREN AND THIS PROPAGATES INTO EVERY ROW.** The surgery
was performed to PREVENT IDIOPATHIC TALL STATURE (Chu et al. 2025 preprint, Results).
These are constitutionally very tall Scandinavian adolescents whose growth plates were
being deliberately ablated. Any expression value here is from a plate selected for
growing too much. Whether that biases the transcriptome is unknown and untestable from
this dataset, because there is no normal-stature paediatric growth-plate scRNA-seq to
compare against - which is itself the reason this is the only such table in existence.

The GEO record describes the donors as ages 11-14; the preprint text says 12-15. The
discrepancy is unresolved and is recorded rather than reconciled. This script uses ONLY
the four samples processed directly:

    GSM9328218 donor1   GSM9328221 donor2   GSM9328224 donor3   GSM9328229 donor4

and deliberately EXCLUDES the vehicle- and GH-cultured arms, because 24 h of explant
culture changes exactly the thing a proliferation-related screen is most sensitive to.
The mouse samples in the same series are excluded.

The raw FASTQs were withheld from GEO for patient-identifiability reasons; the filtered
count matrices used here are the public deposit.

WHAT THE OUTPUT MEANS, AND WHAT IT DOES NOT
-------------------------------------------
`pct_donorN` = percentage of that donor's cells with a non-zero count for the gene. That
is a DETECTION rate in droplet scRNA-seq, and it is driven as much by sequencing depth
and capture efficiency as by biology - donor3 detects 26,836 genes and donor4 detects
20,953, so the same gene will read higher in donor3 for purely technical reasons.
Compare genes WITHIN a donor, and require agreement ACROSS donors, never average them.

`n_donors_detected` (of 4, at >=1% of cells) is the column to filter on, because it is
the one robust to depth.

This is bulk-of-the-plate, not zonal: these are whole needle biopsies dissociated
together, so a transcript confined to one zone is diluted. Absence here is therefore
much weaker evidence than presence.

DISSOCIATION BIAS, STATED PLAINLY: terminal hypertrophic chondrocytes are enormous and
fragile and are systematically lost in droplet protocols. Genes specific to them are
under-represented by an unknown factor. COL10A1 sits at 4.5 / 8.4 / 94.1 / 7.3 % across
the four donors, a 20-fold spread on the canonical hypertrophic marker, which is the
scale of the problem.

Usage:
  python3 atlas/tools/gp_expression.py --h5dir <dir with GSE288028 .h5 files>
"""
from __future__ import annotations
import argparse, csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_CSV = os.path.join(ROOT, "query", "human_growth_plate_expression.csv")

# ZONAL ASSIGNMENT, and what it is not.
#
# Chu et al. 2025 (bioRxiv 2025.03.14.642964, the PREPRINT of the Sci Transl Med paper)
# resolve the human pubertal growth plate into five chondrocyte subclusters GP1-GP5 and
# publish their markers: GP1/GP2 progenitors (SFRP5, APOE; GAS1 marks the quiescent
# GP1), GP3 proliferating (CCND1), GP4 pre-hypertrophic (IHH, MEF2C), GP5 hypertrophic
# (COL10A1).
#
# What follows is a MARKER-SCORE APPROXIMATION of those zones, not their clustering.
# Their cluster labels are not in the GEO deposit, so each cell is assigned to whichever
# marker set scores highest per 10k counts. That is cruder than their pipeline in three
# ways worth stating: it has no batch correction, it cannot separate GP1 from GP2 (the
# two share SFRP5/APOE and the distinction is a whole-transcriptome one), and it assigns
# every gated cell to some zone rather than leaving ambiguous cells out.
#
# The authors also regressed cell-cycle and stress signatures out of their embedding.
# This script does NOT, because the cycling signal is the thing a proliferation-related
# screen most needs - but that means the GP3 assignment here and theirs are not the
# same object.
ZONE_MARKERS = {
    "GP1_2_stem":          ["SFRP5", "APOE", "GAS1"],
    "GP3_proliferative":   ["CCND1", "MKI67", "TOP2A", "PCNA"],
    "GP4_prehypertrophic": ["IHH", "MEF2C"],
    "GP5_hypertrophic":    ["COL10A1", "IBSP", "SPP1"],
}
CHONDRO_GATE = ["COL2A1", "ACAN"]

FRESH = {  # ONLY the directly-processed human samples
    "GSM9328218_P30453_1001.h5": "donor1",
    "GSM9328221_P31011_1001.h5": "donor2",
    "GSM9328224_P25452_001.h5": "donor3",
    "GSM9328229_P22202_1015.h5": "donor4",
}
DETECT_PCT = 1.0          # a gene counts as detected in a donor at >=1% of cells


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h5dir", required=True)
    ap.add_argument("--zonal", action="store_true",
                    help="also emit per-zone detection using the Chu marker sets")
    a = ap.parse_args()
    import h5py, numpy as np, scipy.sparse as sp

    per, names0, ncells = {}, None, {}
    for fn, dn in FRESH.items():
        p = os.path.join(a.h5dir, fn)
        if not os.path.exists(p):
            print(f"MISSING {p} - refusing to build a partial table", file=sys.stderr)
            return 1
        with h5py.File(p, "r") as f:
            g = f["matrix"]
            shape = tuple(g["shape"][:])
            M = sp.csc_matrix((g["data"][:], g["indices"][:], g["indptr"][:]), shape=shape)
            names = np.array([x.decode() for x in g["features/name"][:]])
            if names0 is None:
                names0 = names
            elif not (names == names0).all():
                print("gene order differs between donors - refusing", file=sys.stderr)
                return 1
            ncells[dn] = int(shape[1])
            per[dn] = 100.0 * np.asarray((M > 0).sum(axis=1)).ravel() / shape[1]
        print(f"  {dn}: {ncells[dn]} cells")

    if a.zonal:
        zrows, zmeta = {}, {}
        for fn, dn in FRESH.items():
            with h5py.File(os.path.join(a.h5dir, fn), "r") as f:
                g = f["matrix"]
                shape = tuple(g["shape"][:])
                M = sp.csc_matrix((g["data"][:], g["indices"][:], g["indptr"][:]),
                                  shape=shape).tocsr()
                names = np.array([x.decode() for x in g["features/name"][:]])
                ix = {n: i for i, n in enumerate(names)}
                tot = np.asarray(M.sum(axis=0)).ravel()
                tot[tot == 0] = 1
                S = np.vstack([
                    np.asarray(M[[ix[m] for m in ms if m in ix], :].sum(axis=0)).ravel()
                    / tot for ms in ZONE_MARKERS.values()])
                gate = np.asarray(M[[ix[m] for m in CHONDRO_GATE if m in ix], :]
                                  .sum(axis=0)).ravel() > 0
                lab = np.array(list(ZONE_MARKERS))[S.argmax(axis=0)].astype(object)
                lab[~gate] = "non_chondrocyte"
                lab[(S.max(axis=0) == 0) & gate] = "unassigned"
                lab = lab.astype(str)
                zmeta[dn] = {z: int((lab == z).sum()) for z in np.unique(lab)}
                for z in ZONE_MARKERS:
                    sel = np.where(lab == z)[0]
                    if len(sel) < 30:          # too few cells to quote a rate
                        continue
                    sub = M[:, sel]
                    zrows.setdefault(z, {})[dn] = (
                        100.0 * np.asarray((sub > 0).sum(axis=1)).ravel() / len(sel))
            print(f"  {dn} zones: {zmeta[dn]}")
        zp = OUT_CSV.replace(".csv", ".byzone.csv")
        with open(zp, "w", newline="") as fh:
            w = csv.writer(fh)
            zs = list(ZONE_MARKERS)
            w.writerow(["gene"] + [f"{z}__{d}" for z in zs for d in zrows.get(z, {})])
            cols = [(z, d) for z in zs for d in zrows.get(z, {})]
            for i in range(len(names0)):
                vals = [zrows[z][d][i] for z, d in cols]
                if max(vals) < 1.0:
                    continue
                w.writerow([names0[i]] + [f"{v:.2f}" for v in vals])
        json.dump(zmeta, open(zp.replace(".csv", ".meta.json"), "w"), indent=1)
        print(f"wrote {zp}")

    donors = list(FRESH.values())
    keep = np.zeros(len(names0), dtype=bool)
    for d in donors:
        keep |= per[d] > 0
    idx = np.where(keep)[0]
    with open(OUT_CSV, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["gene"] + [f"pct_{d}" for d in donors] + ["n_donors_detected"])
        for i in idx:
            vals = [per[d][i] for d in donors]
            w.writerow([names0[i]] + [f"{v:.2f}" for v in vals]
                       + [sum(1 for v in vals if v >= DETECT_PCT)])
    meta = {"source": "GSE288028", "samples": FRESH, "n_cells": ncells,
            "detect_threshold_pct_of_cells": DETECT_PCT,
            "excluded": "cultured vehicle and GH arms; all mouse samples",
            "genes_written": int(len(idx)), "genes_total": int(len(names0))}
    json.dump(meta, open(OUT_CSV.replace(".csv", ".meta.json"), "w"), indent=1)
    print(f"wrote {OUT_CSV}  ({len(idx)} genes, {sum(ncells.values())} cells, "
          f"{len(donors)} donors)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
