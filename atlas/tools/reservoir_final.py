#!/usr/bin/env python3
"""Does a GLI1+ stromal population sit outside the human growth plate cartilage?

THE METRIC IS THE POINT. Detection fraction (% of cells with >0 counts) is useless
here: COL2A1 is "detected" in 90% of cells in a cluster that is 99% PTPRC-positive,
because a ~95%-cartilage biopsy leaves ambient COL2A1 in every droplet. That is why
the earlier gate (CORR-018) and the first clustering guard both mis-fired.

THE FIX IS AN INTERNAL CONTROL, NOT A THRESHOLD. Immune cells CANNOT transcribe
COL2A1. Their COL2A1 level therefore measures the ambient floor directly, in this
sample, with no parameter to choose. Any cluster at that floor is COL2A1-negative
however often COL2A1 is "detected" in it.

  measured here: immune clusters carry COL2A1 at a median of 2 counts;
                 chondrocyte clusters carry it at a median of 2,209.

GUARDS, declared before the reservoir result is read:
  G1 The ambient reference must be valid: immune clusters (PTPRC-high) must have a
     COL2A1 mean at least 100-fold below chondrocyte clusters. If not, immune cells
     are not clean and the reference fails.
  G2 The stromal cluster must be COL1A1-high, PDGFRA-high, PTPRC-low, and at the
     COL2A1 ambient floor (mean within 5x of the immune mean).
  G3 The stromal population must appear in MORE THAN ONE DONOR. A population
     carried by one library is a finding about that library.
  G4 GLI1 must clear a count floor: >= 50 total counts in the compared groups
     pooled, or the comparison is not made and that is reported.
"""
import sys, os, json
import numpy as np, pandas as pd, scanpy as sc, anndata as ad, scipy.sparse as sp

D=sys.argv[1]; CL=sys.argv[2]
OUT=sys.argv[3] if len(sys.argv)>3 else "/home/user/growth-plate/query/reservoir_final.json"
FRESH={"GSM9328218_P30453_1001.h5":"donor1","GSM9328221_P31011_1001.h5":"donor2",
       "GSM9328224_P25452_001.h5":"donor3","GSM9328229_P22202_1015.h5":"donor4"}
cl=pd.read_csv(CL,index_col=0)
ads=[]
for fn,dn in FRESH.items():
    a=sc.read_10x_h5(os.path.join(D,fn)); a.var_names_make_unique()
    a.obs_names=[f"{dn}_{b}" for b in a.obs_names]; ads.append(a)
A=ad.concat(ads,join="outer"); A.var_names_make_unique()
A=A[cl.index].copy(); A.obs["leiden"]=cl["leiden"].astype(str).values
A.obs["donor"]=cl["donor"].values

def vec(cells,g):
    if g not in A.var_names: return np.zeros(len(cells))
    m=A[cells,g].X
    return np.asarray(m.todense()).ravel() if sp.issparse(m) else np.asarray(m).ravel()
cls=sorted(A.obs.leiden.unique(), key=int)
idx={c:np.where(A.obs.leiden.values==c)[0] for c in cls}
def mn(c,g): return float(vec(idx[c],g).mean())
def pc(c,g): return 100*float((vec(idx[c],g)>0).mean())
def tot(c,g): return int(vec(idx[c],g).sum())

immune=[c for c in cls if pc(c,"PTPRC")>=85 and mn(c,"PTPRC")>=3]
chond =[c for c in cls if mn(c,"COL2A1")>=500]
if not immune or not chond: print("no immune or no chondrocyte cluster; cannot build ambient reference"); sys.exit(1)
amb=float(np.mean([mn(c,"COL2A1") for c in immune]))
chm=float(np.mean([mn(c,"COL2A1") for c in chond]))
print(f"AMBIENT REFERENCE  immune clusters {immune}: COL2A1 mean {amb:.2f}")
print(f"                   chondrocyte clusters: COL2A1 mean {chm:.1f}   ratio {chm/amb:.0f}x")
fail=[]
if chm/amb < 100: fail.append(f"G1 FAILED: ambient separation only {chm/amb:.0f}x")

stromal=[c for c in cls if mn(c,"COL1A1")>=5 and pc(c,"PDGFRA")>=40
         and pc(c,"PTPRC")<40 and mn(c,"COL2A1")<=5*amb]
print(f"\nSTROMAL CANDIDATES (COL1A1-high, PDGFRA-high, PTPRC-low, COL2A1 at ambient): {stromal}")
if not stromal: fail.append("G2 FAILED: no cluster meets the stromal description")
else:
    dn={}
    for c in stromal:
        for d,n in A.obs.loc[A.obs.leiden==c,"donor"].value_counts().items(): dn[d]=dn.get(d,0)+int(n)
    print(f"   donor composition pooled: {dn}")
    if sum(1 for v in dn.values() if v>=20) < 2: fail.append(f"G3 FAILED: stromal population not in >1 donor -> {dn}")
if fail: print("\n"+"\n".join(fail)+"\nREFUSING TO REPORT."); sys.exit(1)
print("guards G1-G3 PASS\n")

sc_i=np.concatenate([idx[c] for c in stromal]); ch_i=np.concatenate([idx[c] for c in chond])
print(f"{'gene':<9}{'stromal mean':>14}{'chondro mean':>14}{'ratio':>9}{'strom cts':>11}{'chond cts':>11}")
res={}
for g in ("COL1A1","PDGFRA","COL2A1","ACAN","PTPRC","GLI1","PTCH1","HHIP","GLI2","GLI3","SFRP5","PRRX1","THY1"):
    s=vec(sc_i,g); c=vec(ch_i,g)
    r=(s.mean()/c.mean()) if c.mean()>0 else float("inf")
    res[g]=dict(stromal_mean=float(s.mean()),chondro_mean=float(c.mean()),ratio=float(r),
                stromal_counts=int(s.sum()),chondro_counts=int(c.sum()),
                stromal_pct=100*float((s>0).mean()),chondro_pct=100*float((c>0).mean()))
    print(f"{g:<9}{s.mean():>14.3f}{c.mean():>14.3f}{r:>9.2f}{int(s.sum()):>11}{int(c.sum()):>11}")
g1=res["GLI1"]["stromal_counts"]+res["GLI1"]["chondro_counts"]
print(f"\nG4: GLI1 total counts in the compared groups = {g1}")
if g1 < 50:
    print("BELOW THE FLOOR - the GLI1 comparison is NOT made."); verdict="GLI1 below count floor"
else:
    r=res["GLI1"]["ratio"]
    verdict=("GLI1 ENRICHED in stromal" if r>=2 else
             "GLI1 DEPLETED in stromal" if r<=0.5 else "GLI1 NOT differentially enriched")
    print(f"VERDICT: {verdict}  (stromal/chondrocyte ratio {r:.2f})")
print(f"\nstromal cells {len(sc_i)}, chondrocyte cells {len(ch_i)}")
json.dump({"ambient_ratio":chm/amb,"immune_clusters":immune,"stromal_clusters":stromal,
           "chondrocyte_clusters":chond,"genes":res,"verdict":verdict,
           "n_stromal":int(len(sc_i)),"n_chondro":int(len(ch_i))},
          open(OUT,"w"),indent=1)
print(f"wrote {OUT}")
