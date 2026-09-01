#!/usr/bin/env python3
"""
R480 - THE v(m) PANEL.

WHY. The frontier branch (F-R058) verified the growth identity to 0.1%:

    dL/dt = flux x v(d),    v(d) = v(c) + v(m)

where v(d) is the TERMINAL CHONDROCYTIC DOMAIN VOLUME - the terminal hypertrophic
cell PLUS the matrix volume attributable to that cell. Wilsman 1996's own source
decomposition of the daily turned-over volume is:

    fast plate   9% cell duplication / 32% MATRIX / 59% cell enlargement
    slow plate   7% cell duplication / 49% MATRIX / 44% cell enlargement

F-R185 then screened 23 h_term genes for every compound that touches them and
declared the dominant node pharmacologically empty. Its 23 genes are:
PAPPA PAPPA2 STC2 IGFBP4 IGFBP5 IGF1 IGF1R | NPPC NPR2 NPR3 OSTN MME |
IHH SOX9 RUNX2 GLI2 PTH1R HDAC4 SMO | MTOR FGFR3 INPPL1.

Every one of those is v(c) - cell swelling, CNP, hypertrophy timing, mTOR.
NOT ONE MATRIX-SYNTHESIS GENE. So the "empty" verdict covers 59% of h_term in a
fast plate and 44% in a slow one. Human plates are the slow case, where matrix is
the LARGER half.

This screens the unscreened half against the tissue.

METHOD. R411's sex-corrected purity split on GSE288028, reproduced exactly:
  - 12 human samples, 4 patients (R344 removed 2 mouse samples R308 counted as human)
  - XIST identifies 9 male / 3 female; all 3 females sit in the contaminated half,
    so the R344 split is confounded with sex. Split WITHIN the 9 males only.
  - on that split COL2A1 = 7.65 and ACAN = 1.96, so 1.96 is the cartilage benchmark
  - PTPRC = 0.00 and HBB = 0.03 are the blood calibrators

CORR-363 GOVERNS AND IS APPLIED HERE. A purity ratio measures INVESTMENT, not
rate-limitation, and the screen is structurally blind to universal machinery. A low
ratio on a ubiquitous secretory/Golgi gene is NOT a kill (R447 established this by
showing CREB3L2, SEC23A, SEC24D and MIA3 all score contaminant-leaning while every
one of them has a human or mouse LENGTH endpoint). What is interpretable is the
INTERNAL CONTRAST between modules scored against one comparator.

Output: atlas/data/round480/vm_panel.json
"""
import json
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(DATA, "round480")

# ---------------------------------------------------------------- the panel
# Every gene here is on the v(m) side of v(d) = v(c) + v(m): it makes, modifies,
# exports or sizes the MATRIX the terminal chondrocyte is responsible for.
PANEL = {
    "core_protein": [
        "ACAN", "VCAN", "HAPLN1", "BGN", "DCN", "FMOD", "LUM", "PRELP",
        "EPYC", "OGN", "ASPN", "CHAD", "COMP", "MATN1", "MATN3",
    ],
    "collagen_fibrillar": [
        "COL2A1", "COL9A1", "COL9A2", "COL9A3", "COL11A1", "COL11A2",
        "COL10A1", "COL27A1",
    ],
    "gag_chain_initiation": [
        "XYLT1", "XYLT2", "B4GALT7", "B3GALT6", "B3GAT3", "FAM20B",
    ],
    "gag_chain_elongation": [
        "CSGALNACT1", "CSGALNACT2", "CHSY1", "CHSY3", "CHPF", "CHPF2",
    ],
    "sulfation": [
        "CHST3", "CHST11", "CHST12", "CHST13", "CHST14", "CHST7", "UST",
        "PAPSS1", "PAPSS2", "SLC35B2", "SLC35B3", "SLC26A2", "IMPAD1", "BPNT1",
    ],
    "hyaluronan": ["HAS1", "HAS2", "HAS3", "HYAL1", "HYAL2", "CD44"],
    "collagen_folding_pt m": [
        "SERPINH1", "P4HA1", "P4HA2", "P4HB", "P3H1", "P3H2", "P3H3",
        "CRTAP", "PPIB", "PLOD1", "PLOD2", "PLOD3", "FKBP10", "FKBP14",
    ],
    "secretory_export": [
        "MIA3", "MIA2", "SEC23A", "SEC23B", "SEC24D", "SEC24C", "SEC13",
        "SEC31A", "SAR1A", "SAR1B", "TANGO2", "CREB3L2", "CREB3L1",
        "TRAPPC2", "KDELR1", "KDELR2", "TMED9", "TMED2", "TMED10", "SURF4",
    ],
    "golgi_nucleotide_sugar": [
        "SLC35D1", "SLC35A1", "SLC35A2", "SLC35A3", "UGDH", "UXS1",
        "UGP2", "GALE", "CANT1", "ENTPD5", "TMEM165",
    ],
    "matrix_turnover": [
        "MMP13", "MMP9", "ADAMTS4", "ADAMTS5", "TIMP1", "TIMP3",
    ],
    "calibrators_cartilage": ["COL2A1", "ACAN", "IHH", "COL10A1"],
    "calibrators_blood": ["PTPRC", "HBB", "AGTR1", "MME"],
    "fr185_vc_screen": [
        "PAPPA", "PAPPA2", "STC2", "IGFBP4", "IGFBP5", "IGF1", "IGF1R",
        "NPPC", "NPR2", "NPR3", "OSTN", "MME", "IHH", "SOX9", "RUNX2",
        "GLI2", "PTH1R", "HDAC4", "SMO", "MTOR", "FGFR3", "INPPL1",
    ],
}


def main():
    genes = json.load(open(os.path.join(DATA, "round344", "gse288028_gene_names.json")))
    cpm = np.load(os.path.join(DATA, "round344", "gse288028_human12_cpm.npy"))
    meta = json.load(open(os.path.join(DATA, "round344", "gse288028_purity_corrected.json")))

    idx = {g: i for i, g in enumerate(genes)}
    # sample order in the npy is the order of purest + contaminated as recorded in R344
    samples = list(meta["purest_samples"]) + list(meta["contaminated_samples"])
    if len(samples) != cpm.shape[0]:
        # fall back to the col2a1_by_sample key ordering
        samples = list(meta["col2a1_by_sample"].keys())
    assert len(samples) == cpm.shape[0], (len(samples), cpm.shape)

    # --- sex call from XIST and the Y panel, exactly as R411 did
    ypanel = [g for g in ("RPS4Y1", "UTY", "USP9Y", "DDX3Y", "EIF2S3Y", "KDM5D") if g in idx]
    xist = cpm[:, idx["XIST"]] if "XIST" in idx else np.zeros(cpm.shape[0])
    yexp = cpm[:, [idx[g] for g in ypanel]].sum(axis=1) if ypanel else np.zeros(cpm.shape[0])
    sex = ["F" if (x > y) else "M" for x, y in zip(xist, yexp)]

    col2 = cpm[:, idx["COL2A1"]]
    males = [i for i, s in enumerate(sex) if s == "M"]
    males_sorted = sorted(males, key=lambda i: -col2[i])
    n = len(males_sorted) // 2
    pure_i = males_sorted[:n]
    cont_i = males_sorted[-n:]

    def row(g):
        if g not in idx:
            return None
        v = cpm[:, idx[g]]
        p = float(np.median(v[pure_i]))
        c = float(np.median(v[cont_i]))
        det = int((v > 0).sum())
        ratio = round(p / c, 2) if c > 0 else (float("inf") if p > 0 else 0.0)
        return {
            "gene": g,
            "pure_med_cpm": round(p, 2),
            "contam_med_cpm": round(c, 2),
            "purity_ratio": ratio if ratio != float("inf") else None,
            "ratio_is_infinite": c == 0 and p > 0,
            "detected_of_12": det,
        }

    out = {
        "note": __doc__.strip(),
        "samples": samples,
        "sex_calls": dict(zip(samples, sex)),
        "xist_cpm": {s: round(float(x), 2) for s, x in zip(samples, xist)},
        "y_panel_cpm": {s: round(float(y), 2) for s, y in zip(samples, yexp)},
        "male_pure": [samples[i] for i in pure_i],
        "male_contaminated": [samples[i] for i in cont_i],
        "benchmark": "ACAN on this split is the cartilage benchmark; PTPRC/HBB are blood",
        "modules": {},
    }
    for mod, gl in PANEL.items():
        rows = [row(g) for g in gl]
        out["modules"][mod] = [r for r in rows if r]
        missing = [g for g, r in zip(gl, rows) if r is None]
        if missing:
            out.setdefault("not_on_platform", {})[mod] = missing

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "vm_panel.json"), "w") as fh:
        json.dump(out, fh, indent=1)

    # --- readable summary
    print("sex calls:", dict(zip(samples, sex)))
    print("male pure:", out["male_pure"])
    print("male contaminated:", out["male_contaminated"])
    print()
    for mod in PANEL:
        rows = sorted(out["modules"][mod], key=lambda r: -(r["purity_ratio"] or 999))
        print(f"=== {mod} ===")
        for r in rows:
            rr = "INF" if r["ratio_is_infinite"] else r["purity_ratio"]
            print(f"  {r['gene']:12s} pure {r['pure_med_cpm']:10.1f}  ratio {str(rr):>7s}  det {r['detected_of_12']}/12")
        print()


if __name__ == "__main__":
    main()
