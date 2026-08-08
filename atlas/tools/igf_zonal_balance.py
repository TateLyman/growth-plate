#!/usr/bin/env python3
"""
igf_zonal_balance.py - RECREATE, as far as transcriptomes allow, the measurement
nobody has made: is IGF-1 bioavailability RESTRAINED in the human hypertrophic zone?

WHY THIS EXISTS
---------------
cooper2013 shows terminal chondrocyte enlargement has three phases and that PHASE 3 -
the one whose duration varies most between fast and slow growth plates - is abolished in
Igf1-null mice. cooper2013 states the mechanism is LOCALLY regulated. Whether local free
IGF-1 is actually lower where phase 3 happens has NEVER BEEN MEASURED, in any species.
Three independent Europe PMC searches returned nothing.

WHAT THIS IS, STATED BEFORE THE NUMBERS
---------------------------------------
NOT a free-IGF measurement. It cannot be. It is a zone-resolved PSEUDOBULK TRANSCRIPT
BALANCE between IGF ligands, the six IGF-binding proteins that sequester them, and the
pappalysins/stanniocalcins that set how much gets released. Four things break the chain
from this to a free-IGF concentration and all four are fatal to any quantitative claim:

  1. Transcript is not protein, and IGFBPs are stable secreted proteins whose local
     concentration reflects accumulated secretion plus delivery from serum, not the
     instantaneous transcription of the nearest cell.
  2. These are SECRETED, DIFFUSIBLE molecules. Zone-of-transcription is not
     zone-of-protein for anything that leaves the cell.
  3. Droplet scRNA-seq systematically under-recovers terminal hypertrophic chondrocytes
     (see chondrocyte_dissociation_bias), so the hypertrophic column is the least
     trustworthy one in the table - which is exactly the column of interest.
  4. Donor4 contributes 13-62 cells per zone. Any per-donor zonal value from donor4 is
     noise; the script reports per-donor values so this is visible rather than averaged
     away.

So this outputs a DIRECTION and a CONSISTENCY CHECK ACROSS DONORS, not a number to put
in a model. It is graded as a re-analysis. Its real value is that it is falsifiable: if
the binder:ligand ratio does NOT rise into the hypertrophic zone, the restraint
hypothesis loses its only supporting observation and should be dropped.

WHAT IT ADDS OVER THE EXISTING TABLE
------------------------------------
query/human_growth_plate_expression.byzone.csv reports DETECTION RATE - the percentage
of cells with a non-zero count. That is driven by sequencing depth as much as biology and
CANNOT be summed across genes to form a ratio. This script computes CP10K-normalised
MEAN EXPRESSION per zone, which can be summed, and reports both so they can be compared.

USAGE
  python3 atlas/tools/igf_zonal_balance.py --h5dir <dir with GSE288028 .h5 files>
"""
import os, sys, json, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from gp_expression import FRESH, ZONE_MARKERS, CHONDRO_GATE   # reuse the SAME zone calls

LIGAND = ["IGF1", "IGF2"]
BINDER = ["IGFBP1", "IGFBP2", "IGFBP3", "IGFBP4", "IGFBP5", "IGFBP6"]
RELEASE = ["PAPPA", "PAPPA2"]
INHIB = ["STC1", "STC2"]
RECEPTOR = ["IGF1R", "INSR", "IGF2R"]
ALL = LIGAND + BINDER + RELEASE + INHIB + RECEPTOR + ["IGFALS", "COL10A1", "COL2A1"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h5dir", required=True)
    a = ap.parse_args()
    import h5py, numpy as np, scipy.sparse as sp

    out = {}
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
        ix = {n: i for i, n in enumerate(names)}
        tot = np.asarray(M.sum(axis=0)).ravel()
        tot[tot == 0] = 1
        # zone call - identical logic to gp_expression.py so the two tables are comparable
        S = np.vstack([
            np.asarray(M[[ix[m] for m in ms if m in ix], :].sum(axis=0)).ravel() / tot
            for ms in ZONE_MARKERS.values()])
        gate = np.asarray(M[[ix[m] for m in CHONDRO_GATE if m in ix], :]
                          .sum(axis=0)).ravel() > 0
        lab = np.array(list(ZONE_MARKERS))[S.argmax(axis=0)].astype(object)
        lab[~gate] = "non_chondrocyte"
        lab[(S.max(axis=0) == 0) & gate] = "unassigned"
        lab = lab.astype(str)
        # CP10K per cell, then mean across cells in the zone
        CP = M.multiply(sp.csr_matrix(1e4 / tot))          # counts per 10k
        for z in ZONE_MARKERS:
            sel = np.where(lab == z)[0]
            rec = out.setdefault(z, {}).setdefault(dn, {"n_cells": int(len(sel))})
            if len(sel) < 30:
                rec["insufficient"] = True
                continue
            sub = CP[:, sel]
            for gname in ALL:
                if gname not in ix:
                    rec[gname] = None
                    continue
                rec[gname] = float(np.asarray(sub[ix[gname], :].todense()).ravel().mean())
        print(f"  {dn}: " + ", ".join(f"{z}={out[z][dn]['n_cells']}" for z in ZONE_MARKERS))

    op = os.path.join(ROOT, "query", "igf_zonal_balance.json")
    json.dump(out, open(op, "w"), indent=1)
    print("wrote", op)

    zs = list(ZONE_MARKERS)
    print("\nCP10K MEAN EXPRESSION, per donor, per zone (donors with >=30 cells in zone)")
    print("ratio = sum(IGFBP1-6) / sum(IGF1+IGF2).  HIGHER = MORE SEQUESTRATION.\n")
    hdr = f"{'donor':8}" + "".join(f"{z.split('_',1)[1][:11]:>13}" for z in zs)
    print(hdr)
    for dn in FRESH.values():
        row, ok = f"{dn:8}", False
        for z in zs:
            r = out[z].get(dn, {})
            if r.get("insufficient") or r.get("n_cells", 0) < 30:
                row += f"{'--':>13}"; continue
            lig = sum(r.get(g) or 0 for g in LIGAND)
            bnd = sum(r.get(g) or 0 for g in BINDER)
            row += f"{(bnd/lig if lig > 0 else float('inf')):13.2f}"; ok = True
        if ok:
            print(row)
    print("\nCOMPONENTS (CP10K mean), donor-by-donor, hypertrophic vs proliferative:")
    for gname in LIGAND + BINDER + RELEASE + INHIB + ["IGF1R", "IGFALS", "COL10A1"]:
        parts = []
        for dn in FRESH.values():
            pz = out["GP3_proliferative"].get(dn, {})
            hz = out["GP5_hypertrophic"].get(dn, {})
            if pz.get("insufficient") or hz.get("insufficient"):
                continue
            v1, v2 = pz.get(gname), hz.get(gname)
            if v1 is None or v2 is None:
                continue
            parts.append(f"{dn}:{v1:.2f}->{v2:.2f}")
        print(f"  {gname:9} " + "  ".join(parts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
