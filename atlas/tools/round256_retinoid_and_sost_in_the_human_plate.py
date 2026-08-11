#!/usr/bin/env python3
"""
ROUND 256. Is the retinoid axis present in the HUMAN growth plate - and is SOST?

WHY. Round 255 opened the retinoid axis on koyama2021, which states that RARgamma is
"most abundantly expressed in growth plate" - IN MOUSE. The whole proposition rests on
that. g_l3_is_rargamma_expressed_in_the_human_growth_plate asks whether it transfers.
The same query answers a second standing gap for free: sclerostin_sost records that SOST
expression in growth plate cartilage HAS NEVER BEEN DEMONSTRATED, which is why the tall
stature of sclerosteosis cannot currently be attributed to the physis.

DATA. GSE288028 (chu2026), the four DIRECTLY-PROCESSED FRESH samples - the same four
round 244 used, chosen there for the same reason: the other samples are frozen/nuclei
preparations that are not comparable. These are pubertal human growth plates from donors
operated on to PREVENT IDIOPATHIC TALL STATURE, so every number comes from a plate
selected for growing too much.

WHAT THIS IS NOT. It is not a reproduction of chu2026's GP1-GP5 clustering. Re-deriving
those clusters from raw counts would be a different analysis with different boundaries.
Zonal statements here rest on MARKER GATES, which are enrichments, not clusters, and are
labelled as such throughout.

THREE THINGS THAT LIMIT WHAT CAN BE CONCLUDED, STATED UP FRONT
--------------------------------------------------------------
1. CROSS-GENE detection rates are confounded by transcript length, GC content and 10x
   capture efficiency. "RARG detected in more cells than RARA" is therefore WEAK evidence
   that RARG protein is more abundant. The comparison this script trusts is WITHIN a gene
   ACROSS zones, where the capture bias is shared.
2. Droplet data is sparse and zero-inflated. LOW DETECTION IS WEAK EVIDENCE OF ABSENCE.
   That is why negative controls are included - to establish what a gene that is genuinely
   absent from this tissue actually looks like in this dataset.
3. The COL2A1/ACAN chondrocyte gate used elsewhere in this atlas DEPLETES resting-zone
   cells, which carry the lowest mRNA content of any zone. All primary numbers here are
   UNGATED for that reason.
"""
import argparse, os, sys
import numpy as np

FRESH = {
    "GSM9328218_P30453_1001.h5": "donor1",
    "GSM9328221_P31011_1001.h5": "donor2",
    "GSM9328224_P25452_001.h5": "donor3",
    "GSM9328229_P22202_1015.h5": "donor4",
}

# --- the question -----------------------------------------------------------------
RETINOID_RECEPTORS = ["RARA", "RARB", "RARG", "RXRA", "RXRB", "RXRG"]
RETINOID_METABOLISM = ["CYP26A1", "CYP26B1", "CYP26C1",      # catabolism (koyama2021: DOWN on Hh block)
                       "ALDH1A1", "ALDH1A2", "ALDH1A3",      # synthesis  (koyama2021: Raldh3 UP)
                       "RDH10", "DHRS3", "STRA6",
                       "CRABP1", "CRABP2", "RBP1"]
WNT_BRAKE = ["SOST", "SOSTDC1", "LRP5", "LRP6", "DKK1"]

# --- calibration ------------------------------------------------------------------
# Positive controls: must be present, or the pipeline is wrong.
POSITIVE = ["COL2A1", "ACAN", "SOX9", "COL10A1", "IHH", "PTH1R", "PTHLH", "MKI67", "CYTL1"]
# Negative controls: genes with no business in growth plate cartilage. These define the
# floor - what "absent" looks like in THIS dataset at THIS depth.
NEGATIVE = ["ALB", "INS", "MYOD1", "CD19", "KRT14", "NEUROD1", "SFTPC"]

# --- zonal gates (ENRICHMENTS, NOT CLUSTERS) --------------------------------------
GATES = {
    "hypertrophic (COL10A1+)": ("COL10A1", 1),
    "proliferating (MKI67+)":  ("MKI67", 1),
    "root-enriched (CYTL1+)":  ("CYTL1", 1),
}

ALL = (RETINOID_RECEPTORS + RETINOID_METABOLISM + WNT_BRAKE + POSITIVE + NEGATIVE)


def load(path):
    import h5py, scipy.sparse as sp
    with h5py.File(path, "r") as f:
        g = f["matrix"]
        shape = tuple(g["shape"][:])                       # (n_genes, n_cells)
        M = sp.csc_matrix((g["data"][:], g["indices"][:], g["indptr"][:]), shape=shape)
        names = np.array([x.decode() for x in g["features"]["name"][:]])
    return M, names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h5dir", required=True)
    ap.add_argument("--min-umi", type=int, default=500)
    a = ap.parse_args()

    print("=" * 96)
    print("ROUND 256 - THE RETINOID AXIS AND SOST IN THE HUMAN PUBERTAL GROWTH PLATE")
    print("GSE288028, four directly-processed fresh donors. UNGATED unless a gate is named.")
    print("=" * 96)

    per_donor = {}
    for fn, donor in FRESH.items():
        path = os.path.join(a.h5dir, fn)
        if not os.path.exists(path):
            print(f"  MISSING {fn}", file=sys.stderr)
            continue
        M, names = load(path)
        umi = np.asarray(M.sum(axis=0)).ravel()
        keep = umi >= a.min_umi
        M = M[:, keep]
        umi = umi[keep]
        print(f"\n{donor}: {M.shape[1]} cells passing >= {a.min_umi} UMI "
              f"(median {int(np.median(umi))} UMI), {M.shape[0]} features")

        idx = {}
        for gene in ALL:
            hits = np.nonzero(names == gene)[0]
            idx[gene] = hits[0] if len(hits) else None

        # counts per gene per cell, as a dense 1-D vector (one gene at a time: cheap)
        vec = {}
        for gene, i in idx.items():
            vec[gene] = np.zeros(M.shape[1]) if i is None else np.asarray(M[i, :].todense()).ravel()

        per_donor[donor] = dict(vec=vec, umi=umi, n=M.shape[1], idx=idx)

    if not per_donor:
        sys.exit("no h5 files found")

    def det(donor, gene, mask=None):
        """percent of cells with >=1 count, and mean counts per 10k UMI"""
        d = per_donor[donor]
        v = d["vec"][gene]
        u = d["umi"]
        if mask is not None:
            v, u = v[mask], u[mask]
        if len(v) == 0:
            return float("nan"), float("nan")
        return 100.0 * (v > 0).mean(), float((v / u * 1e4).mean())

    donors = list(per_donor)

    def block(title, genes, note=""):
        print("\n" + "=" * 96)
        print(title)
        if note:
            print(note)
        print("=" * 96)
        print(f"{'gene':<10} " + "".join(f"{d+' %det':>14}" for d in donors) + f"{'mean %det':>12}  {'CP10K mean':>11}")
        for gene in genes:
            ds, cs = [], []
            for d in donors:
                if per_donor[d]["idx"][gene] is None:
                    ds.append(float("nan")); cs.append(float("nan")); continue
                p, c = det(d, gene)
                ds.append(p); cs.append(c)
            row = "".join(f"{x:>14.2f}" if x == x else f"{'absent':>14}" for x in ds)
            mp = np.nanmean(ds) if any(x == x for x in ds) else float("nan")
            mc = np.nanmean(cs) if any(x == x for x in cs) else float("nan")
            print(f"{gene:<10} {row}{mp:>12.2f}  {mc:>11.3f}")

    block("STEP 1 - CALIBRATION. What present and absent look like in THIS dataset.",
          POSITIVE + ["--"] * 0 + NEGATIVE,
          "Positive controls first, then negative controls. The negative block defines the floor:\n"
          "any test gene at or below it cannot be distinguished from absent at this depth.")

    block("STEP 2 - THE RETINOID RECEPTORS. Does RARG dominate in HUMAN as it does in mouse?",
          RETINOID_RECEPTORS,
          "CROSS-GENE COMPARISON IS CONFOUNDED by capture efficiency - read the ordering as\n"
          "suggestive, not quantitative. What IS interpretable: whether each gene clears the\n"
          "negative-control floor at all.")

    block("STEP 3 - THE RETINOID SYNTHESIS AND CATABOLISM MACHINERY.",
          RETINOID_METABOLISM,
          "koyama2021's mechanism is that hedgehog inhibition DROPS Cyp26b1 and RAISES Raldh3,\n"
          "raising local retinoid tone and closing the plate. Both enzymes have to exist here\n"
          "for that circuit to be available in man.")

    block("STEP 4 - THE WNT BRAKE, AND THE SCLEROSTEOSIS QUESTION.",
          WNT_BRAKE,
          "sclerostin_sost states SOST has never been demonstrated in growth plate cartilage.\n"
          "If SOST sits at the negative-control floor while LRP5/LRP6 do not, the tall stature\n"
          "of sclerosteosis is not a physeal SOST effect and that lever leaves this programme.")

    # ---- zonal ----------------------------------------------------------------
    print("\n" + "=" * 96)
    print("STEP 5 - ZONAL DISTRIBUTION BY MARKER GATE. Detection rate WITHIN each gate.")
    print("THESE GATES ARE ENRICHMENTS, NOT CLUSTERS. CYTL1+ is enriched for the root cluster")
    print("and will include some GP2 and some non-chondrocytes (round 244). The within-gene,")
    print("across-zone contrast is the one that is not confounded by capture efficiency.")
    print("=" * 96)
    zonal_genes = ["RARG", "RARA", "RARB", "CYP26B1", "ALDH1A3", "ALDH1A2", "CRABP1",
                   "SOST", "LRP5", "COL10A1", "MKI67", "CYTL1", "PTH1R"]
    for gname, (marker, thr) in GATES.items():
        print(f"\n  GATE: {gname}")
        sizes = []
        for d in donors:
            m = per_donor[d]["vec"][marker] >= thr
            sizes.append(int(m.sum()))
        print(f"    cells in gate: " + ", ".join(f"{d}={s}" for d, s in zip(donors, sizes)))
        print(f"    {'gene':<10}" + "".join(f"{d+' %det':>14}" for d in donors) + f"{'mean':>10}")
        for gene in zonal_genes:
            vals = []
            for d in donors:
                if per_donor[d]["idx"][gene] is None:
                    vals.append(float("nan")); continue
                m = per_donor[d]["vec"][marker] >= thr
                p, _ = det(d, gene, mask=m)
                vals.append(p)
            row = "".join(f"{x:>14.2f}" if x == x else f"{'absent':>14}" for x in vals)
            mv = np.nanmean(vals) if any(x == x for x in vals) else float("nan")
            print(f"    {gene:<10}{row}{mv:>10.2f}")

    # ---- the two verdicts -------------------------------------------------------
    print("\n" + "=" * 96)
    print("STEP 6 - THE TWO QUESTIONS, ANSWERED AGAINST THE NEGATIVE-CONTROL FLOOR")
    print("=" * 96)
    floor = np.nanmean([np.nanmean([det(d, g)[0] for d in donors
                                    if per_donor[d]["idx"][g] is not None])
                        for g in NEGATIVE
                        if any(per_donor[d]["idx"][g] is not None for d in donors)])
    print(f"  negative-control floor (mean detection across {len(NEGATIVE)} absent genes): {floor:.3f} % of cells")
    for gene in ["RARG", "RARA", "RARB", "CYP26B1", "ALDH1A3", "SOST", "LRP5", "LRP6"]:
        vals = [det(d, gene)[0] for d in donors if per_donor[d]["idx"][gene] is not None]
        if not vals:
            print(f"  {gene:<9} NOT IN THE FEATURE LIST")
            continue
        m = np.nanmean(vals)
        n_above = sum(1 for v in vals if v > floor * 3)
        verdict = ("CLEARS the floor in %d/%d donors" % (n_above, len(vals))) if n_above else "AT THE FLOOR"
        print(f"  {gene:<9} mean {m:>7.3f} %   ({m/floor:>6.1f}x floor)   {verdict}")

    print("\n  READ THIS AS: clearing the floor means the transcript is present in the tissue.")
    print("  It does NOT establish protein, zone, or that the receptor is rate-limiting.")


if __name__ == "__main__":
    main()
