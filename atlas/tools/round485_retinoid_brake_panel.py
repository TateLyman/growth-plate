#!/usr/bin/env python3
"""
R485 - THE RETINOID BRAKE PANEL, RE-RUN AGAINST R431's OWN NUMBERS.

WHY.  saxena2022 (Curr Biol 2022;32:289-303, PMID 34793695), read in full this
round, states that endogenous retinoic acid REPRESSES growth in mouse
metatarsals and that the jerboa de-represses it.  Its cited basis is
deluca2000 (Endocrinology 2000;141:346-53, PMID 10614657), whose abstract says
that in the ABSENCE of exogenous RA an RAR antagonist ACCELERATED bone growth,
as did an RA-specific NEUTRALISING ANTIBODY.

R431 closed the retinoid arm on two grounds:
  (a) koyama2021's CD2665 monotherapy null on mouse TIBIA length in vivo, and
  (b) a purity-corrected read of the human plate that "already holds retinoic
      acid near zero", quoted as CYP26A1 47.9x, CRABP2 7.6x, CRABP1 4.3x,
      ALDH1A2 0.02, ALDH1A1 0.31, RARG 1.08, RARA 0.42, RARB 0.31.

This script re-derives every one of those numbers with R411's sex-corrected
split so they can be checked rather than carried, and adds the genes R431 did
not have: CRABP1's partner set, the RA-inducible inhibitory ligand GDF10, and
the BMP inhibitor MAB21L2 - the two de-repression genes saxena2022 identifies
alongside CRABP1.

CORR-363 GOVERNS.  A purity ratio measures INVESTMENT, not rate-limitation, and
is structurally blind to universal machinery.  What is interpretable is the
INTERNAL CONTRAST between modules scored against one comparator.

Method identical to round480_vm_matrix_panel.py: GSE288028, 12 human samples
(R344 removed the 2 mouse ones), sex called from XIST vs the Y panel, split
WITHIN the 9 males by COL2A1, median CPM in the purest half over the median in
the contaminated half.

Output: atlas/data/round485/retinoid_panel.json
"""
import json
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(DATA, "round485")

PANEL = {
    # --- R431's own quoted panel, so its numbers can be checked
    "ra_synthesis": ["ALDH1A1", "ALDH1A2", "ALDH1A3", "RDH10", "DHRS3", "STRA6", "RBP1", "RBP4"],
    "ra_clearance": ["CYP26A1", "CYP26B1", "CYP26C1"],
    "ra_binding": ["CRABP1", "CRABP2", "FABP5"],
    "ra_receptors": ["RARA", "RARB", "RARG", "RXRA", "RXRB", "RXRG"],
    "ra_corepressors": ["NCOR1", "NCOR2", "SIN3A", "HDAC3"],
    # --- saxena2022's de-repression set, none of which R431 had
    "saxena_derepression": ["CRABP1", "GDF10", "MAB21L2"],
    "saxena_nodes": ["SHOX2", "SHOX", "PRRX1", "PAX1", "HOXB9", "HOXB13", "RSRC1"],
    # --- the BMP arm MAB21L2 inhibits, to see whether the receiver is there
    "bmp_receiver": ["BMP2", "BMP4", "BMPR1A", "BMPR1B", "BMPR2", "SMAD1", "SMAD4", "SMAD5"],
    # --- GDF10's own receptor set (TGF-beta/activin type)
    "gdf10_receiver": ["ACVR1", "ACVR1B", "ACVR2A", "ACVR2B", "TGFBR1", "TGFBR2", "GDF11", "MSTN"],
    "calibrators_cartilage": ["COL2A1", "ACAN", "IHH", "COL10A1"],
    "calibrators_blood": ["PTPRC", "HBB", "AGTR1", "MME"],
}


def main():
    genes = json.load(open(os.path.join(DATA, "round344", "gse288028_gene_names.json")))
    cpm = np.load(os.path.join(DATA, "round344", "gse288028_human12_cpm.npy"))
    meta = json.load(open(os.path.join(DATA, "round344", "gse288028_purity_corrected.json")))

    idx = {g: i for i, g in enumerate(genes)}
    samples = list(meta["purest_samples"]) + list(meta["contaminated_samples"])
    if len(samples) != cpm.shape[0]:
        samples = list(meta["col2a1_by_sample"].keys())
    assert len(samples) == cpm.shape[0]

    ypanel = [g for g in ("RPS4Y1", "UTY", "USP9Y", "DDX3Y", "EIF2S3Y", "KDM5D") if g in idx]
    xist = cpm[:, idx["XIST"]] if "XIST" in idx else np.zeros(cpm.shape[0])
    yexp = cpm[:, [idx[g] for g in ypanel]].sum(axis=1) if ypanel else np.zeros(cpm.shape[0])
    sex = ["F" if (x > y) else "M" for x, y in zip(xist, yexp)]

    col2 = cpm[:, idx["COL2A1"]]
    males = [i for i, s in enumerate(sex) if s == "M"]
    males_sorted = sorted(males, key=lambda i: -col2[i])
    n = len(males_sorted) // 2
    pure_i, cont_i = males_sorted[:n], males_sorted[-n:]

    def row(g):
        if g not in idx:
            return None
        v = cpm[:, idx[g]]
        p, c = float(np.median(v[pure_i])), float(np.median(v[cont_i]))
        return {
            "gene": g,
            "pure_med_cpm": round(p, 2),
            "contam_med_cpm": round(c, 2),
            "purity_ratio": round(p / c, 2) if c > 0 else None,
            "ratio_is_infinite": c == 0 and p > 0,
            "detected_of_12": int((v > 0).sum()),
        }

    out = {"note": __doc__.strip(), "male_pure": [samples[i] for i in pure_i],
           "male_contaminated": [samples[i] for i in cont_i], "modules": {}}
    for mod, gl in PANEL.items():
        out["modules"][mod] = [r for r in (row(g) for g in gl) if r]

    os.makedirs(OUT, exist_ok=True)
    json.dump(out, open(os.path.join(OUT, "retinoid_panel.json"), "w"), indent=1)

    for mod, rows in out["modules"].items():
        print(f"\n--- {mod}")
        for r in sorted(rows, key=lambda r: -(r["purity_ratio"] or 0)):
            inf = "  INF" if r["ratio_is_infinite"] else ""
            print(f"   {r['gene']:10s} pure {r['pure_med_cpm']:9.2f}  contam "
                  f"{r['contam_med_cpm']:9.2f}  ratio {str(r['purity_ratio']):>7s}"
                  f"  det {r['detected_of_12']}/12{inf}")


if __name__ == "__main__":
    main()
