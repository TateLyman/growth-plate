#!/usr/bin/env python3
"""Round 244. Which soluble WNT inhibitors does the human root cell actually express?

WHY THIS EXISTS
---------------
chu2026's Fig. 3R states that of the 174 genes in KEGG:04310, the GP1 root cluster
expresses FOUR LIGANDS AND NINE SOLUBLE INHIBITORS. The nine are not named anywhere
in the main text, and the supplement supplied on 2026-08-11 does not name them
either. Round 241 recorded the count without the list, which makes the claim
pathway-level and undruggable. Round 243 recovered exactly one name, SFRP1, by
reading it off the ligand-receptor panel. This script tries to recover the rest
from the deposited data, GSE288028, which this atlas has held since Phase 5.

WHAT THIS IS AND IS NOT
-----------------------
This is NOT a reproduction of the authors' clustering. Re-deriving GP1 from raw
counts would be a different analysis with different cluster boundaries, and any
gene list from it would be mine, not theirs.

Instead this uses the paper's OWN discriminator. CYTL1 is the marker the authors
selected for GP1, validated by RNAscope and by immunofluorescence against RAMP3
for GP2. So the question asked here is narrow and answerable: AMONG CELLS FROM
THESE BIOPSIES, DO CYTL1-POSITIVE CELLS SHOW HIGHER DETECTION OF PARTICULAR
SOLUBLE WNT ANTAGONISTS THAN CYTL1-NEGATIVE CELLS? That is a marker-gated
contrast, it is weaker than the authors' cluster-level statement, and it is
graded as re-analysis.

THREE THINGS THAT LIMIT IT, PRINTED IN THE OUTPUT SO THEY CANNOT BE DROPPED
---------------------------------------------------------------------------
1. CYTL1-positive is not GP1. It is enriched for GP1 and will include some GP2
   and some non-chondrocytes.
2. The COL2A1/ACAN chondrocyte gate used elsewhere in this atlas EXCLUDES
   resting-zone cells, which carry the lowest mRNA content of any zone (CORR-042
   note). For a root-cell question that gate is actively wrong, so both gated and
   ungated numbers are printed and the ungated one is the primary.
3. Droplet detection is sparse. Low detection is weak evidence of absence.

The donors were operated on to PREVENT IDIOPATHIC TALL STATURE, so every number
here comes from a plate selected for growing too much.
"""
import argparse, os, sys

FRESH = {  # only the directly-processed fresh samples
    "GSM9328218_P30453_1001.h5": "donor1",
    "GSM9328221_P31011_1001.h5": "donor2",
    "GSM9328224_P25452_001.h5": "donor3",
    "GSM9328229_P22202_1015.h5": "donor4",
}

# Every secreted/soluble WNT antagonist with a gene symbol, so the list is not
# chosen to flatter the hypothesis. KEGG:04310 members are marked.
WNT_INHIBITORS = ["SFRP1", "SFRP2", "SFRP4", "SFRP5", "FRZB", "WIF1", "DKK1",
                  "DKK2", "DKK3", "DKK4", "SOST", "SOSTDC1", "NOTUM", "APCDD1",
                  "KREMEN1", "KREMEN2", "CER1", "GREM1", "SERPINF1", "TMEM88"]
TGFB_INHIBITORS = ["THBS1", "THBS2", "THBS3", "THBS4", "DCN", "BGN", "FMOD",
                   "LUM", "LTBP1", "LTBP3", "NBL1", "FST", "BAMBI", "SMAD7"]
WNT_LIGANDS = ["WNT1", "WNT2B", "WNT3", "WNT4", "WNT5A", "WNT5B", "WNT6",
               "WNT7B", "WNT9A", "WNT10A", "WNT10B", "WNT11", "WNT16"]
IDENTITY = ["CYTL1", "RAMP3", "PTHLH", "SFRP5", "APOE", "GAS1", "PRRX1",
            "COL2A1", "ACAN", "COL10A1", "MKI67", "GHR", "IGF1R"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h5dir", required=True)
    ap.add_argument("--gated", action="store_true",
                    help="apply the COL2A1/ACAN chondrocyte gate. OFF by default because "
                         "that gate depletes resting-zone cells, which is the population "
                         "this script is about.")
    a = ap.parse_args()
    import h5py, numpy as np, scipy.sparse as sp

    panels = [("SOLUBLE WNT ANTAGONISTS", WNT_INHIBITORS),
              ("SOLUBLE TGF-BETA ANTAGONISTS AND SINKS", TGFB_INHIBITORS),
              ("WNT LIGANDS", WNT_LIGANDS),
              ("IDENTITY AND CONTROLS", IDENTITY)]
    genes = sorted({g for _, p in panels for g in p})

    pos = {g: {} for g in genes}   # % detection in CYTL1+ cells
    neg = {g: {} for g in genes}
    counts = {}

    for fn, dn in FRESH.items():
        path = os.path.join(a.h5dir, fn)
        if not os.path.exists(path):
            print(f"MISSING {path} - refusing to build a partial table", file=sys.stderr)
            return 1
        with h5py.File(path, "r") as f:
            m = f["matrix"]
            shape = tuple(m["shape"][:])
            M = sp.csc_matrix((m["data"][:], m["indices"][:], m["indptr"][:]),
                              shape=shape).tocsr()
            names = np.array([x.decode() for x in m["features/name"][:]])

        def row(gn):
            i = np.where(names == gn)[0]
            return None if len(i) == 0 else M[i[0]].toarray().ravel()

        keep = np.ones(shape[1], dtype=bool)
        if a.gated:
            c2, ac = row("COL2A1"), row("ACAN")
            keep = (c2 > 0) & (ac > 0)
        cy = row("CYTL1")
        if cy is None:
            print(f"CYTL1 absent from {dn} feature list - cannot proceed", file=sys.stderr)
            return 1
        p_mask = keep & (cy > 0)
        n_mask = keep & (cy == 0)
        counts[dn] = (int(shape[1]), int(keep.sum()), int(p_mask.sum()), int(n_mask.sum()))

        for g in genes:
            r = row(g)
            if r is None:
                pos[g][dn] = neg[g][dn] = None
                continue
            pos[g][dn] = 100.0 * np.count_nonzero(r[p_mask]) / max(1, p_mask.sum())
            neg[g][dn] = 100.0 * np.count_nonzero(r[n_mask]) / max(1, n_mask.sum())

    dns = ["donor1", "donor2", "donor3", "donor4"]
    print("=" * 78)
    print("WHICH SOLUBLE ANTAGONISTS DOES THE HUMAN CYTL1+ (ROOT-ENRICHED) CELL EXPRESS?")
    print("GSE288028, four fresh human growth plate biopsies, epiphysiodesis for TALL stature")
    print("MODE:", "COL2A1/ACAN-GATED" if a.gated else "UNGATED (default - the gate depletes RZ cells)")
    print("=" * 78)
    print(f"{'donor':<9}{'all cells':>11}{'kept':>9}{'CYTL1+':>9}{'CYTL1-':>9}")
    for d in dns:
        t, k, p, n = counts[d]
        print(f"{d:<9}{t:>11}{k:>9}{p:>9}{n:>9}")
    print()

    for title, panel in panels:
        print("-" * 78)
        print(title, " -- per cent of cells with a detected transcript, CYTL1+ vs CYTL1-")
        print(f"  {'gene':<10}" + "".join(f"{d:>16}" for d in dns) + f"{'donors up':>11}")
        for g in panel:
            cells = ""
            up = 0
            for d in dns:
                if pos[g][d] is None:
                    cells += f"{'absent':>16}"
                    continue
                cells += f"{pos[g][d]:>7.1f}/{neg[g][d]:<8.1f}"
                if pos[g][d] > neg[g][d] and pos[g][d] >= 1.0:
                    up += 1
            print(f"  {g:<10}{cells}{up:>9}/4")
        print()

    print("=" * 78)
    print("HOW TO READ THIS, AND HOW NOT TO")
    print("=" * 78)
    print("Each cell is CYTL1-positive % / CYTL1-negative %. 'donors up' counts donors where")
    print("the gene is detected in at least 1% of CYTL1+ cells AND higher than in CYTL1- cells.")
    print()
    print("A GENE UP IN 4/4 DONORS IS A CANDIDATE FOR THE UNNAMED NINE. IT IS NOT A MEMBER OF")
    print("THEM. The authors' nine come from cluster-level differential expression against GP2")
    print("specifically; this contrast is CYTL1+ against everything else, which is a different")
    print("and coarser comparison. A gene can be root-enriched here and absent from their list,")
    print("or on their list and invisible here because droplet capture missed it.")
    print()
    print("CYTL1-POSITIVE IS NOT GP1. It is enriched for GP1 and contaminated by GP2 and by")
    print("non-chondrocytes. No claim about GP1 specifically may be made from this table.")
    print()
    print("THE DONORS WERE SELECTED FOR EXCESSIVE GROWTH. Whatever their root cells are doing,")
    print("they are doing it in plates that were growing too much, which is the population this")
    print("programme is trying to imitate but is not a normal-stature reference.")
    return 0


if __name__ == "__main__":
    sys.exit(main())


# ---------------------------------------------------------------------------
# Appended after the first run, because the first run showed a confound that
# would otherwise have been reported as a finding.
#
# In the raw contrast, THBS1/2/3/4, DCN, BGN, FMOD, LUM and LTBP1/3 are ALL up
# in CYTL1+ cells in 4/4 donors - but so is ACAN (92.1 vs 37.3 in donor1), and
# by a similar ratio. CYTL1+ cells in this dataset simply carry more matrix
# transcript. A matricellular gene that rises in step with ACAN is evidence of a
# matrix-rich cell, NOT of a targeted antagonist screen.
#
# This pass divides every gene's CYTL1+/CYTL1- ratio by ACAN's, so the question
# becomes: which genes are enriched BEYOND the general matrix-program effect?
# ---------------------------------------------------------------------------
