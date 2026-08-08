#!/usr/bin/env python3
"""
cnp_zonal_system.py - is the human growth plate a CONSUMER of circulating CNP, or its
own PRODUCER?

WHY THIS EXISTS
---------------
thread_3_the_dose_ceiling_is_a_systemic_safety_margin argues that the CNP arm is capped
by a SYSTEMIC cardiovascular exposure margin while its efficacy depends on a GROWTH-PLATE
concentration nobody has ever measured. That argument has an unexamined premise: it
assumes the plate concentration of CNP is set by what arrives from the blood.

If NPPC - the CNP gene - is strongly transcribed BY THE PLATE ITSELF, that premise is
wrong in a way that matters in both directions:

  AGAINST the thread - a systemically delivered analogue is not filling an empty
  compartment. It is adding to a locally generated ligand pool that may already be far
  above plasma concentration, so the marginal effect of raising plasma is small and a
  cartilage-targeted molecule inherits the same problem.

  FOR the thread - if the plate makes its own CNP and STILL responds to an exogenous
  analogue with a monotonic dose-response (savarirayan2023), then local production is
  evidently not saturating NPR2, and the receptor has headroom that a better-delivered
  molecule could occupy.

The two readings are distinguished by the RATIO of ligand to receptor to clearance, not
by ligand alone, which is why this script reports the whole local system:

    NPPC   the ligand, CNP precursor
    NPR2   the signalling receptor (guanylate cyclase B)
    NPR3   the CLEARANCE receptor - internalises and degrades CNP, no cyclase
    MME    neprilysin - the protease that degrades CNP; the target of sacubitril
    FURIN  processes proCNP to the secreted forms

WHAT THIS IS, STATED BEFORE THE NUMBERS
---------------------------------------
NOT a concentration measurement. It cannot be one. It is a zone-resolved PSEUDOBULK
TRANSCRIPT profile, and the same four limits that govern igf_zonal_balance.py govern it:

  1. Transcript is not protein, and CNP is a SECRETED, RAPIDLY DEGRADED peptide whose
     local concentration depends on protease and clearance-receptor activity far more
     than on the transcription of the nearest cell.
  2. Zone-of-transcription is not zone-of-protein for anything diffusible.
  3. Droplet scRNA-seq systematically under-recovers terminal hypertrophic chondrocytes,
     so the hypertrophic column is the least trustworthy and it is the zone the CNP axis
     is known to act on (nakao2015).
  4. Donor4 contributes few cells per zone; per-donor values are printed so this is
     visible rather than averaged away.

AND THE DONORS ARE NOT TYPICAL. GSE288028 is four epiphysiodesis biopsies from children
being treated to PREVENT IDIOPATHIC TALL STATURE. Every value is from a plate selected
for growing too much. For this project's question that is an unusually apt population,
but it is still a selected one and no normal-stature paediatric comparison exists.

PRE-REGISTERED READING, WRITTEN BEFORE THE SCRIPT WAS RUN
--------------------------------------------------------
  - NPPC at or below the detection floor in all four donors => the plate is a CONSUMER;
    plasma delivery is the whole story and the thread's premise holds unmodified.
  - NPPC comparable to or above NPR2 in CP10K => the plate is a PRODUCER; the thread must
    be restated as "raise occupancy above a local baseline" rather than "deliver the
    ligand", and the burden shifts to showing the receptor is not already saturated.
  - NPR3 (clearance) high relative to NPR2 (signalling) => local ligand is actively
    destroyed, which would explain how a locally produced peptide can coexist with an
    unsaturated receptor, and would make clearance-receptor blockade a distinct lever
    from ligand supply.

No outcome of this script establishes a concentration, and none of them can promote the
thread above its current D grade on their own.

Usage:
  python3 atlas/tools/cnp_zonal_system.py --h5dir <dir with GSE288028 .h5 files>
"""
from __future__ import annotations
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# Identical to gp_expression.py / igf_zonal_balance.py so all three tables are comparable
FRESH = {
    "GSM9328218_P30453_1001.h5": "donor1",
    "GSM9328221_P31011_1001.h5": "donor2",
    "GSM9328224_P25452_001.h5": "donor3",
    "GSM9328229_P22202_1015.h5": "donor4",
}
ZONE_MARKERS = {
    "GP1_resting":       ["SFRP5", "APOE", "GAS1"],
    "GP3_proliferative": ["MKI67", "TOP2A", "CCNB1"],
    "GP5_hypertrophic":  ["COL10A1", "IBSP", "SPP1"],
}
CHONDRO_GATE = ["COL2A1", "ACAN"]

LIGAND    = ["NPPC"]
RECEPTOR  = ["NPR2"]
CLEARANCE = ["NPR3"]
PROTEASE  = ["MME"]
PROCESS   = ["FURIN"]
# comparators: NPPA/NPPB are the cardiac natriuretic peptides and should be ABSENT in
# cartilage - they are the negative control for this panel.
CONTROL   = ["NPPA", "NPPB", "NPR1"]
ALL = LIGAND + RECEPTOR + CLEARANCE + PROTEASE + PROCESS + CONTROL + \
      ["COL10A1", "COL2A1", "ACAN", "FGFR3"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h5dir", required=True)
    a = ap.parse_args()
    import h5py, numpy as np, scipy.sparse as sp

    out, det = {}, {}
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

        S = np.vstack([
            np.asarray(M[[ix[m] for m in ms if m in ix], :].sum(axis=0)).ravel() / tot
            for ms in ZONE_MARKERS.values()])
        gate = np.asarray(M[[ix[m] for m in CHONDRO_GATE if m in ix], :]
                          .sum(axis=0)).ravel() > 0
        lab = np.array(list(ZONE_MARKERS))[S.argmax(axis=0)].astype(object)
        lab[~gate] = "non_chondrocyte"
        lab[(S.max(axis=0) == 0) & gate] = "unassigned"
        lab = lab.astype(str)

        CP = M.multiply(sp.csr_matrix(1e4 / tot))          # counts per 10k
        for z in ZONE_MARKERS:
            sel = np.where(lab == z)[0]
            rec = out.setdefault(z, {}).setdefault(dn, {"n_cells": int(len(sel))})
            drec = det.setdefault(z, {}).setdefault(dn, {})
            if len(sel) < 30:
                rec["insufficient"] = True
                continue
            sub = CP[:, sel]
            raw = M[:, sel]
            for gname in ALL:
                if gname not in ix:
                    rec[gname] = None; drec[gname] = None
                    continue
                rec[gname] = float(np.asarray(sub[ix[gname], :].todense()).ravel().mean())
                drec[gname] = float((np.asarray(raw[ix[gname], :].todense()).ravel() > 0).mean() * 100)
        print(f"  {dn}: " + ", ".join(f"{z}={out[z][dn]['n_cells']}" for z in ZONE_MARKERS))

    op = os.path.join(ROOT, "query", "cnp_zonal_system.json")
    json.dump({"cp10k": out, "detection_pct": det}, open(op, "w"), indent=1)
    print("wrote", op)

    zs = list(ZONE_MARKERS)
    print("\nCP10K MEAN EXPRESSION, per donor, per zone (donors with >=30 cells in zone)")
    print("CP10K is an EXPRESSION LEVEL. Detection %% is the FRACTION OF CELLS and is a")
    print("different quantity - CORR-104 was caused by ratioing detection rates across")
    print("genes. Both are printed; only CP10K is ratioed.\n")

    for gname in LIGAND + RECEPTOR + CLEARANCE + PROTEASE + PROCESS + CONTROL:
        print(f"\n  {gname}")
        for dn in FRESH.values():
            row, ok = f"    {dn:8}", False
            for z in zs:
                r = out[z].get(dn, {}); d = det[z].get(dn, {})
                if r.get("insufficient") or r.get("n_cells", 0) < 30:
                    row += f"{'--':>20}"; continue
                v, dv = r.get(gname), d.get(gname)
                row += f"{(f'{v:.3f} ({dv:.1f}%)' if v is not None else 'absent'):>20}"
                ok = True
            if ok:
                print(row)

    print("\n\nTHE RATIO THAT DECIDES THE READING: ligand NPPC / receptor NPR2, CP10K")
    print("  >=1 favours PRODUCER, <<1 favours CONSUMER. See the pre-registered reading.\n")
    hdr = f"  {'donor':8}" + "".join(f"{z.split('_',1)[1][:11]:>14}" for z in zs)
    print(hdr)
    for dn in FRESH.values():
        row, ok = f"  {dn:8}", False
        for z in zs:
            r = out[z].get(dn, {})
            if r.get("insufficient") or r.get("n_cells", 0) < 30:
                row += f"{'--':>14}"; continue
            lig, rcp = r.get("NPPC"), r.get("NPR2")
            if lig is None or rcp is None:
                row += f"{'NA':>14}"; continue
            row += f"{(lig / rcp if rcp > 0 else float('inf')):14.3f}"; ok = True
        if ok:
            print(row)

    print("\nCLEARANCE PRESSURE: NPR3 / NPR2, CP10K. HIGHER = local ligand more actively")
    print("destroyed, which permits a produced ligand to coexist with a free receptor.\n")
    print(hdr)
    for dn in FRESH.values():
        row, ok = f"  {dn:8}", False
        for z in zs:
            r = out[z].get(dn, {})
            if r.get("insufficient") or r.get("n_cells", 0) < 30:
                row += f"{'--':>14}"; continue
            cl, rcp = r.get("NPR3"), r.get("NPR2")
            if cl is None or rcp is None:
                row += f"{'NA':>14}"; continue
            row += f"{(cl / rcp if rcp > 0 else float('inf')):14.3f}"; ok = True
        if ok:
            print(row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
