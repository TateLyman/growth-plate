#!/usr/bin/env python3
"""
shape_screen.py - what changes when a chondrocyte changes SHAPE, in human tissue.

WHY THIS EXISTS
---------------
hunziker1989 measured which variable carries a physiological change in growth rate, and
the answer was not the one the field targets. A +20 % rise in rat growth rate is
accounted for by a +23 % rise in terminal cell HEIGHT while the lateral diameter FALLS
14 % and the cell VOLUME FALLS 13 %. Matrix per cell, cells produced per column per day,
and the duration of the hypertrophic phase are all unchanged.

So physiological acceleration is a cell-SHAPE change at constant-or-lower volume -
Hunziker's "phenotype modulation" - and every therapeutic programme in this space
(CNP analogues, FGFR3 inhibitors) targets hypertrophic ENLARGEMENT instead.

`target_screen.py` inherited that error: it ranked by the flow model's uncertainty, where
h_term is a scalar and volume and height are not distinguished. This script asks a
different question, and asks it of human tissue rather than of the graph:

    which genes change between the human proliferative zone and the human hypertrophic
    zone - the transition in which the cell actually changes shape - and which of those
    are druggable?

WHY NOT JUST QUERY THE GRAPH
----------------------------
Because the graph cannot answer it. The atlas has no cell-shape layer: `chondrocyte
_hypertrophy` has 31 incoming edges and none of them is about aspect ratio. A screen over
the graph would return what the graph happens to contain, which is what round 1 did.
Deriving the gene set from the tissue is independent of the atlas's coverage.

METHOD, AND ITS CIRCULARITY
---------------------------
Zones are assigned by marker score (see gp_expression.py), then GP5 (hypertrophic) is
contrasted against GP3 (proliferative) as a per-donor pseudobulk log2 fold change, and a
gene is kept only if it moves the same way in at least 3 of 4 donors.

**The marker genes used to assign the zones are excluded from the output**, because a
gene that defines GP5 will always appear up in GP5. That is circular by construction and
the exclusion is the only defence. It also means the screen cannot rediscover COL10A1,
IHH or MEF2C - which is correct, because it did not find them, it assumed them.

WHAT THIS CANNOT DO
-------------------
1. The contrast is PZ vs HZ, a DIFFERENTIATION step. Hunziker's comparison is the same
   zone at two ages under two growth rates. These are different axes. A gene up in HZ vs
   PZ is part of becoming hypertrophic; it is not thereby a gene that sets how TALL the
   cell gets. This screen narrows the search space; it does not identify a lever.
2. Droplet scRNA-seq under-recovers large fragile hypertrophic cells, so the GP5 pool is
   a biased sample of the cells whose shape matters most.
3. The donors are children being operated on to PREVENT tall stature (see
   gp_expression.py header).

Usage:
  python3 atlas/tools/shape_screen.py --h5dir <dir with GSE288028 .h5>
"""
from __future__ import annotations
import argparse, csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "query", "target_screen")

FRESH = {"GSM9328218_P30453_1001.h5": "d1", "GSM9328221_P31011_1001.h5": "d2",
         "GSM9328224_P25452_001.h5": "d3", "GSM9328229_P22202_1015.h5": "d4"}
# CHU'S PUBLISHED MARKERS ONLY. The first version of this script added IBSP and SPP1 to
# the GP5 set on the assumption that they mark hypertrophic cartilage. They do not - they
# are BONE matrix genes - and they dragged osteoblasts and primary-spongiosa cells into
# the "hypertrophic" pool. The resulting top hits were BGLAP (osteocalcin), DMP1, MEPE,
# SATB2, COL1A1 and COL1A2: a clean osteoblast signature that would have been reported as
# the machinery of chondrocyte shape change. Only markers the source paper actually
# assigns to a cluster are used now.
ZONE_MARKERS = {
    "GP1_2_stem": ["SFRP5", "APOE", "GAS1"],
    "GP3_proliferative": ["CCND1"],
    "GP4_prehypertrophic": ["IHH", "MEF2C"],
    "GP5_hypertrophic": ["COL10A1"],
}
CHONDRO_GATE = ["COL2A1", "ACAN"]

# Osteoblast / osteocyte lineage. Any cell expressing these is removed BEFORE zone
# assignment: the chondro-osseous junction is where hypertrophic chondrocytes and
# osteoblasts are physically interleaved, so a permissive COL2A1 gate alone does not
# separate them.
OSTEO_EXCLUDE = ["BGLAP", "COL1A1", "COL1A2", "DMP1", "MEPE", "SATB2", "SP7", "IBSP"]

# Haematopoietic / immune. The second version of this script, having removed the
# osteoblasts, returned LAPTM5, FYB1, SAMHD1, CXCR4, BIRC3 and CD44 near the top - a
# marrow signature. The chondro-osseous junction is continuous with marrow, so a
# COL2A1-positive gate does not exclude leukocytes riding along in the same droplet
# neighbourhood. Two successive contamination signatures is the honest reason this
# analysis is reported with the confidence it is.
BLOOD_EXCLUDE = ["PTPRC", "LAPTM5", "FYB1", "CD52", "CORO1A", "LCP1", "HBB", "HBA1",
                 "SRGN", "CD37", "ARHGDIB", "CXCR4", "TYROBP", "FCER1G", "AIF1"]

EXCLUDE = ({g for ms in ZONE_MARKERS.values() for g in ms}
           | set(CHONDRO_GATE) | set(OSTEO_EXCLUDE) | set(BLOOD_EXCLUDE))

# A cell is assigned to a zone only if that zone's markers are actually expressed.
# Without this, argmax forces every gated cell into some zone, so cells with a single
# stray COL10A1 count land in the hypertrophic pool.
MIN_ZONE_MARKER_CPM = 200.0

MIN_CELLS = 30
MIN_LFC = 1.0
MIN_DONORS = 3


def zone_pseudobulk(path):
    import h5py, numpy as np, scipy.sparse as sp
    with h5py.File(path, "r") as f:
        g = f["matrix"]
        shape = tuple(g["shape"][:])
        M = sp.csc_matrix((g["data"][:], g["indices"][:], g["indptr"][:]),
                          shape=shape).tocsr()
        names = np.array([x.decode() for x in g["features/name"][:]])
    ix = {n: i for i, n in enumerate(names)}
    tot = np.asarray(M.sum(axis=0)).ravel()
    tot[tot == 0] = 1
    S = np.vstack([np.asarray(M[[ix[m] for m in ms if m in ix], :].sum(axis=0)).ravel()
                   / tot for ms in ZONE_MARKERS.values()])
    # chondrocyte gate: COL2A1/ACAN must be a real fraction of the cell, not one count
    chon_cpm = (np.asarray(M[[ix[m] for m in CHONDRO_GATE if m in ix], :]
                           .sum(axis=0)).ravel() / tot) * 1e6
    osteo_cpm = (np.asarray(M[[ix[m] for m in OSTEO_EXCLUDE if m in ix], :]
                            .sum(axis=0)).ravel() / tot) * 1e6
    blood_cpm = (np.asarray(M[[ix[m] for m in BLOOD_EXCLUDE if m in ix], :]
                            .sum(axis=0)).ravel() / tot) * 1e6
    gate = ((chon_cpm > 1000) & (osteo_cpm < chon_cpm) & (blood_cpm < 0.2 * chon_cpm))
    lab = np.array(list(ZONE_MARKERS))[S.argmax(axis=0)].astype(object)
    lab[~gate] = "x"
    lab[(S.max(axis=0) * 1e6) < MIN_ZONE_MARKER_CPM] = "x"   # no marker, no assignment
    lab = lab.astype(str)
    out = {}
    for z in ZONE_MARKERS:
        sel = np.where(lab == z)[0]
        if len(sel) < MIN_CELLS:
            continue
        v = np.asarray(M[:, sel].sum(axis=1)).ravel().astype(float)
        out[z] = (v / max(v.sum(), 1) * 1e6, len(sel))
    return out, names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h5dir", required=True)
    a = ap.parse_args()
    import numpy as np

    lfc, names0, ncell = {}, None, {}
    for fn, dn in FRESH.items():
        zb, names = zone_pseudobulk(os.path.join(a.h5dir, fn))
        if names0 is None:
            names0 = names
        if "GP5_hypertrophic" not in zb or "GP3_proliferative" not in zb:
            print(f"  {dn}: missing a zone, skipped")
            continue
        hz, nh = zb["GP5_hypertrophic"]
        pz, npz = zb["GP3_proliferative"]
        lfc[dn] = np.log2((hz + 1) / (pz + 1))
        ncell[dn] = {"GP5": nh, "GP3": npz}
        print(f"  {dn}: GP5 n={nh}, GP3 n={npz}")

    donors = list(lfc)
    if len(donors) < MIN_DONORS:
        print(f"\n{'='*72}\nREFUSING TO REPORT: only {len(donors)} donor(s) yield both a "
              f"GP3 and a GP5 pool at\ndefensible stringency, against a requirement of "
              f"{MIN_DONORS}.\n\nThis is not a threshold to be relaxed. Loosening the gate is "
              f"exactly what produced\nthe two discarded versions of this screen: first an "
              f"osteoblast signature (BGLAP,\nDMP1, MEPE, SATB2), then a marrow signature "
              f"(LAPTM5, FYB1, SAMHD1). The small\ndonors' zone pools were being filled by "
              f"contaminating lineages, not by chondrocytes.\n\nThe underlying fact is that "
              f"the four GSE288028 libraries are not comparable:\ndonor 3 has ~2x the median "
              f"UMI of the others AND 71% of its cells COL10A1-high\nagainst 2-4% in donors "
              f"1 and 2. Any cross-donor contrast is donor 3 alone.\n{'='*72}")
        return 1
    L = np.vstack([lfc[d] for d in donors])
    up = ((L > MIN_LFC).sum(axis=0) >= MIN_DONORS)
    dn_ = ((L < -MIN_LFC).sum(axis=0) >= MIN_DONORS)
    mean = L.mean(axis=0)

    rows = []
    for i in np.where(up | dn_)[0]:
        g = names0[i]
        if g in EXCLUDE:
            continue
        rows.append({"gene": g, "direction": "up_in_HZ" if up[i] else "down_in_HZ",
                     "mean_log2FC": round(float(mean[i]), 3),
                     **{f"lfc_{d}": round(float(lfc[d][i]), 3) for d in donors}})
    rows.sort(key=lambda r: -abs(r["mean_log2FC"]))
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "hz_vs_pz_human.csv")
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    json.dump({"donors": donors, "n_cells": ncell, "min_log2FC": MIN_LFC,
               "min_donors_agreeing": MIN_DONORS,
               "excluded_marker_genes": sorted(EXCLUDE),
               "contrast": "GP5 hypertrophic vs GP3 proliferative, per-donor pseudobulk CPM",
               "WARNING": "PZ->HZ is a DIFFERENTIATION contrast. hunziker1989's result is "
                          "about the same zone at two growth rates. A gene up in HZ is part "
                          "of becoming hypertrophic; that does not make it a lever on how "
                          "tall the cell gets."},
              open(p.replace(".csv", ".meta.json"), "w"), indent=1)
    nu = sum(1 for r in rows if r["direction"] == "up_in_HZ")
    print(f"\n{len(rows)} genes consistent in >={MIN_DONORS}/{len(donors)} donors "
          f"at |log2FC|>{MIN_LFC}  ({nu} up in HZ, {len(rows)-nu} down)")
    print(f"wrote {p}")
    print("\ntop 25 UP in hypertrophic zone:")
    for r in [r for r in rows if r["direction"] == "up_in_HZ"][:25]:
        print(f"  {r['gene']:14s} {r['mean_log2FC']:+6.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
