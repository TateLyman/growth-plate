#!/usr/bin/env python3
"""Is there a GLI1+/PDGFRA+ population in HUMAN growth plate tissue that is NOT
chondrocyte - the human counterpart of the qu2025 reservoir?

qu2025 (mouse): the long-lived cartilage progenitors that drive postnatal growth
descend from Gli1+ cells, and the reparative ones originate from Pdgfra+ cells
OUTSIDE the cartilage. If no such population exists in human tissue, the most
promising route in this atlas closes.

DATA: GSE288028 (chu2026), four fresh human epiphysiodesis biopsies, ages 11-14.
The biopsies are whole tissue - chu2026 report T cells, myeloid, NK, plasma, B,
endothelial, vascular smooth muscle and an MSC/osteoblast cluster alongside the
chondrocytes - so the non-cartilage neighbourhood IS in these libraries.

GATES. The first version used binary detection (>0 counts) and its THY1 guard FAILED.
The cause is ambient RNA: this tissue is about 95% chondrocyte, so ambient COL2A1
appears in nearly every droplet and a "NOT COL2A1" gate selects low-RNA-content
cells rather than stromal ones. THE FIX IS DECLARED HERE AND THE GUARDS ARE
UNCHANGED - gate on COUNT THRESHOLDS rather than on detection:
  CHONDROCYTE : COL2A1 or ACAN at >= CHON_MIN counts
  STROMAL     : COL1A1 and PDGFRA each >= 1 count, and COL2A1 and ACAN each
                BELOW CHON_MIN
  Everything else is left unassigned rather than forced.
If the guards fail again the result is reported as a failure of this dataset to
answer the question, not retuned further.

GUARDS (declared before results):
  G1 The stromal gate must be ENRICHED for PDGFRB and THY1 versus chondrocytes.
     These are not in the gate.
  G2 The stromal gate must be DEPLETED of COL9A1 and COL11A1 versus chondrocytes.
     These are cartilage collagens and are NOT in the gate, so this is an
     independent check that the gate is not simply relabelling chondrocytes.
  G3 HEDGEHOG COHERENCE. GLI1 is a direct Hedgehog target. GLI1+ cells must be
     ENRICHED for PTCH1, also a direct target, relative to GLI1- cells. If GLI1
     detection is dropout noise this will fail and nothing is reported.
  G4 SHH must stay near zero. Growth plate Hedgehog is IHH-driven; appreciable
     SHH would mean the tissue is not what it is supposed to be.
"""
import os, sys, glob, json
import numpy as np, h5py, scipy.sparse as sp

CHON_MIN = 3   # counts; declared before re-running
FRESH = {"GSM9328218_P30453_1001.h5":"donor1","GSM9328221_P31011_1001.h5":"donor2",
         "GSM9328224_P25452_001.h5":"donor3","GSM9328229_P22202_1015.h5":"donor4"}
CHONDRO=["COL2A1","ACAN"]; STROMA=["COL1A1","PDGFRA"]
PROBE=["GLI1","PDGFRA","PTCH1","HHIP","GLI2","GLI3","SMO","IHH","SHH","DHH",
       "PDGFRB","THY1","PRRX1","COL1A1","COL9A1","COL11A1","COL2A1","ACAN",
       "SFRP5","PTHLH","CTSK","LEPR","GREM1","MKI67"]

def load(path):
    with h5py.File(path,"r") as f:
        g=f["matrix"]; shape=tuple(g["shape"][:])
        M=sp.csc_matrix((g["data"][:],g["indices"][:],g["indptr"][:]),shape=shape).tocsr()
        names=np.array([x.decode() for x in g["features/name"][:]])
    return M, names

def pct(M, ix, cells):
    if len(cells)==0 or ix is None: return float("nan")
    return 100.0*float((M[ix, cells]>0).sum())/len(cells)

def main(d):
    files=[f for f in FRESH if os.path.exists(os.path.join(d,f))]
    if len(files)<3: print(f"need the GSE288028 h5 files in {d}",file=sys.stderr); return 1
    rows={}; totals={"chondro":0,"stromal":0,"all":0}
    per_donor={}
    for fn in files:
        dn=FRESH[fn]; M,names=load(os.path.join(d,fn))
        ix={n:i for i,n in enumerate(names)}
        def g(n): return ix.get(n)
        def counts(n):
            i=g(n)
            return np.asarray(M[i,:].todense()).ravel() if i is not None else np.zeros(M.shape[1])
        chon = (counts("COL2A1")>=CHON_MIN) | (counts("ACAN")>=CHON_MIN)
        strom = ((counts("COL1A1")>=1) & (counts("PDGFRA")>=1)
                 & (counts("COL2A1")<CHON_MIN) & (counts("ACAN")<CHON_MIN))
        ci=np.where(chon)[0]; si=np.where(strom)[0]
        totals["chondro"]+=len(ci); totals["stromal"]+=len(si); totals["all"]+=M.shape[1]
        gl=g("GLI1"); gli_pos=np.asarray(M[gl,:].todense()).ravel()>0 if gl is not None else np.zeros(M.shape[1],bool)
        per_donor[dn]=dict(n_cells=int(M.shape[1]), n_chondro=int(len(ci)), n_stromal=int(len(si)),
            pct_stromal=round(100*len(si)/M.shape[1],2),
            gli1_in_stromal=round(pct(M,gl,si),2), gli1_in_chondro=round(pct(M,gl,ci),2),
            ptch1_in_gli1pos=round(pct(M,g("PTCH1"),np.where(gli_pos)[0]),2),
            ptch1_in_gli1neg=round(pct(M,g("PTCH1"),np.where(~gli_pos)[0]),2))
        for p in PROBE:
            rows.setdefault(p,{})[dn]=dict(chondro=round(pct(M,g(p),ci),2), stromal=round(pct(M,g(p),si),2))
        print(f"  {dn}: {M.shape[1]} cells -> {len(ci)} chondrocyte, {len(si)} stromal "
              f"({100*len(si)/M.shape[1]:.1f}%)", flush=True)

    def mean(p,k): 
        v=[rows[p][d][k] for d in rows[p] if not np.isnan(rows[p][d][k])]
        return float(np.mean(v)) if v else float("nan")
    fail=[]
    for gname in ("PDGFRB","THY1"):
        if not (mean(gname,"stromal") > mean(gname,"chondro")):
            fail.append(f"G1 FAILED: {gname} not enriched in the stromal gate "
                        f"({mean(gname,'stromal'):.2f} vs {mean(gname,'chondro'):.2f})")
    for gname in ("COL9A1","COL11A1"):
        if not (mean(gname,"stromal") < mean(gname,"chondro")):
            fail.append(f"G2 FAILED: {gname} not depleted in the stromal gate "
                        f"({mean(gname,'stromal'):.2f} vs {mean(gname,'chondro'):.2f})")
    pp=np.mean([per_donor[d]["ptch1_in_gli1pos"] for d in per_donor])
    pn=np.mean([per_donor[d]["ptch1_in_gli1neg"] for d in per_donor])
    if not (pp>pn): fail.append(f"G3 FAILED: PTCH1 not enriched in GLI1+ cells ({pp:.2f} vs {pn:.2f}) - GLI1 signal is not coherent Hedgehog activity")
    if mean("SHH","chondro")>1.0: fail.append(f"G4 FAILED: SHH detected at {mean('SHH','chondro'):.2f}% in chondrocytes")
    if fail:
        print("\n".join(fail)); print("\nREFUSING TO REPORT."); return 1
    print(f"\nguards PASS - PDGFRB {mean('PDGFRB','stromal'):.1f} vs {mean('PDGFRB','chondro'):.1f}; "
          f"THY1 {mean('THY1','stromal'):.1f} vs {mean('THY1','chondro'):.1f}; "
          f"COL9A1 {mean('COL9A1','stromal'):.1f} vs {mean('COL9A1','chondro'):.1f}; "
          f"PTCH1 in GLI1+ {pp:.1f} vs GLI1- {pn:.1f}; SHH {mean('SHH','chondro'):.2f}\n")

    print(f"cells: {totals['all']} total, {totals['chondro']} chondrocyte, {totals['stromal']} stromal "
          f"({100*totals['stromal']/totals['all']:.1f}% of all cells)\n")
    print(f"{'gene':<10} {'chondrocyte %':>14} {'stromal %':>11}   ratio")
    for p in PROBE:
        c,s=mean(p,"chondro"),mean(p,"stromal")
        r = (s/c) if c>0 else float('inf')
        print(f"{p:<10} {c:>14.2f} {s:>11.2f}   {r:>6.2f}")
    print("\nper donor:")
    for d,v in per_donor.items(): print(f"  {d}: {json.dumps(v)}")
    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","query","reservoir_screen.json")
    json.dump({"per_gene":rows,"per_donor":per_donor,"totals":totals}, open(out,"w"), indent=1)
    print(f"\nwrote {os.path.normpath(out)}")
    return 0

if __name__=="__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else "."))
