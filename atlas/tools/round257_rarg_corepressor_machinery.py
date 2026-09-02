#!/usr/bin/env python3
"""
ROUND 257 ADDENDUM to round 256. Is the LIGAND-LESS REPRESSOR machinery present in the
human growth plate?

WHY. williams2009 (Dev Biol) shows that in mouse, cartilage-specific loss of RARalpha+
RARgamma (or RARbeta+RARgamma) causes SEVERE postnatal growth retardation with a collapse
in aggrecan, while RARalpha+RARbeta loss is virtually normal - so RARgamma is the
essential one. The mechanism they propose is the part that matters: the proliferative and
pre-hypertrophic zones are AVASCULAR and, by their own direct biochemical measurement,
LACK ENDOGENOUS RETINOIDS - so RARgamma there acts as a LIGAND-LESS REPRESSOR, and that
repression is what SUPPORTS growth. Aggrecan rose with RARgamma over-expression under
retinoid-free conditions, and rose further with the co-repressor ZAC1 (gene PLAGL1) or
with "pharmacologic agents that enhance RAR repressor function".

If that is right then an RARgamma INVERSE AGONIST does not remove RARgamma function - it
LOCKS IT INTO the repressor state, which is the growth-supporting state. Deleting a
repressor and locking it on are opposite manipulations, which is how williams2009's
retardation and koyama2021's plate expansion can both be true.

THIS SCRIPT ASKS whether the co-repressor machinery that model requires exists in HUMAN
growth plate, using the same four GSE288028 fresh donors and the same negative-control
floor as round 256.

AND IT TESTS ONE NEW THING. PLAGL1/ZAC1 is a member of the eleven-gene imprinted network
that arm3_pool_ceiling_is_imposed_not_intrinsic records as DECLINING with age in step
with growth rate (lui2008, lui2010). If PLAGL1 is the co-repressor that boosts RARgamma's
growth-supporting repression, then its age-decline is a candidate mechanism for the
senescence counter itself. That is a hypothesis; this script only asks whether the
components are co-expressed in the right cells.

Same three limits as round 256: cross-gene detection rates are confounded by capture
efficiency, droplet data under-detects, and marker gates are enrichments not clusters.
"""
import argparse, os, sys
import numpy as np

FRESH = {
    "GSM9328218_P30453_1001.h5": "donor1",
    "GSM9328221_P31011_1001.h5": "donor2",
    "GSM9328224_P25452_001.h5": "donor3",
    "GSM9328229_P22202_1015.h5": "donor4",
}

COREPRESSOR = ["PLAGL1", "NCOR1", "NCOR2", "HDAC3", "HDAC1", "TBL1X", "TBL1XR1"]
COACTIVATOR = ["NCOA1", "NCOA2", "NCOA3", "EP300", "CREBBP"]
TARGET = ["ACAN", "COL2A1", "SOX9", "SOX5", "SOX6"]
AXIS = ["RARG", "RXRA", "CYP26B1"]
NEGATIVE = ["ALB", "INS", "MYOD1", "CD19", "KRT14", "NEUROD1", "SFTPC"]
GATES = {"hypertrophic (COL10A1+)": "COL10A1",
         "proliferating (MKI67+)": "MKI67",
         "root-enriched (CYTL1+)": "CYTL1"}
ALL = COREPRESSOR + COACTIVATOR + TARGET + AXIS + NEGATIVE + list(GATES.values())


def load(path):
    import h5py, scipy.sparse as sp
    with h5py.File(path, "r") as f:
        g = f["matrix"]
        M = sp.csc_matrix((g["data"][:], g["indices"][:], g["indptr"][:]),
                          shape=tuple(g["shape"][:]))
        names = np.array([x.decode() for x in g["features"]["name"][:]])
    return M, names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h5dir", required=True)
    ap.add_argument("--min-umi", type=int, default=500)
    a = ap.parse_args()

    D = {}
    for fn, donor in FRESH.items():
        p = os.path.join(a.h5dir, fn)
        if not os.path.exists(p):
            print(f"MISSING {fn}", file=sys.stderr); continue
        M, names = load(p)
        umi = np.asarray(M.sum(axis=0)).ravel()
        keep = umi >= a.min_umi
        M, umi = M[:, keep], umi[keep]
        vec = {}
        for g in ALL:
            hit = np.nonzero(names == g)[0]
            vec[g] = np.asarray(M[hit[0], :].todense()).ravel() if len(hit) else None
        D[donor] = dict(vec=vec, umi=umi, n=M.shape[1])
    if not D:
        sys.exit("no h5 files")
    donors = list(D)

    def pct(d, g, mask=None):
        v = D[d]["vec"][g]
        if v is None:
            return float("nan")
        v = v if mask is None else v[mask]
        return 100.0 * (v > 0).mean() if len(v) else float("nan")

    floor = np.nanmean([np.nanmean([pct(d, g) for d in donors]) for g in NEGATIVE])
    print("=" * 92)
    print("ROUND 257 - THE LIGAND-LESS REPRESSOR MACHINERY IN THE HUMAN GROWTH PLATE")
    print(f"GSE288028, four fresh donors, {sum(D[d]['n'] for d in donors)} cells. "
          f"Negative-control floor {floor:.3f} % of cells.")
    print("=" * 92)

    def block(title, genes):
        print(f"\n{title}")
        print(f"  {'gene':<9}" + "".join(f"{d:>10}" for d in donors) + f"{'mean':>9}{'xfloor':>9}")
        for g in genes:
            vals = [pct(d, g) for d in donors]
            m = np.nanmean(vals)
            row = "".join(f"{v:>10.2f}" if v == v else f"{'-':>10}" for v in vals)
            print(f"  {g:<9}{row}{m:>9.2f}{m/floor:>9.1f}")

    block("CO-REPRESSOR MACHINERY (what the ligand-less repressor model requires)", COREPRESSOR)
    block("CO-ACTIVATOR MACHINERY (the opposing arm)", COACTIVATOR)
    block("THE REPRESSION TARGET williams2009 MEASURES", TARGET)
    block("THE AXIS, FOR REFERENCE (round 256 values)", AXIS)

    print("\n" + "=" * 92)
    print("ZONAL - is PLAGL1 where RARG is? Detection within marker gates (ENRICHMENTS, NOT CLUSTERS)")
    print("=" * 92)
    for gname, marker in GATES.items():
        print(f"\n  GATE {gname}")
        sizes = [int((D[d]['vec'][marker] >= 1).sum()) for d in donors]
        print("    n = " + ", ".join(f"{d}:{s}" for d, s in zip(donors, sizes)))
        print(f"    {'gene':<9}" + "".join(f"{d:>10}" for d in donors) + f"{'mean':>9}")
        for g in ["RARG", "PLAGL1", "NCOR1", "NCOR2", "HDAC3", "ACAN"]:
            vals = [pct(d, g, D[d]["vec"][marker] >= 1) for d in donors]
            row = "".join(f"{v:>10.2f}" if v == v else f"{'-':>10}" for v in vals)
            print(f"    {g:<9}{row}{np.nanmean(vals):>9.2f}")

    print("\n" + "=" * 92)
    print("CO-DETECTION - what fraction of RARG+ cells also carry the co-repressor?")
    print("Co-detection in droplet data UNDERSTATES co-expression badly (a zero is usually")
    print("a dropout, not an absence), so these are LOWER BOUNDS and nothing else.")
    print("=" * 92)
    for g in ["PLAGL1", "NCOR1", "NCOR2", "HDAC3", "ACAN"]:
        vals = []
        for d in donors:
            r = D[d]["vec"]["RARG"]
            if r is None or D[d]["vec"][g] is None:
                vals.append(float("nan")); continue
            m = r > 0
            vals.append(100.0 * (D[d]["vec"][g][m] > 0).mean() if m.sum() else float("nan"))
        row = "".join(f"{v:>10.2f}" if v == v else f"{'-':>10}" for v in vals)
        print(f"  {g:<9}{row}{np.nanmean(vals):>9.2f} % of RARG+ cells")


if __name__ == "__main__":
    main()
