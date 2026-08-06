#!/usr/bin/env python3
"""Does a GLI1+ stromal population sit outside the human growth plate cartilage?
Version 2: batch-corrected clusters, and a PER-DONOR ambient reference.

WHY V2 EXISTS. v1 (reservoir_final.py) ran on clusters built from UNCORRECTED
PCA, because sc.external.pp.harmony_integrate raises against harmonypy 2.0 and
the exception was swallowed (CORR-020). With harmony actually applied, the
stromal cluster gets better on every marker - COL1A1 mean 29.5 -> 124, and all
four donors instead of one cell from donor4 - and then FAILS the v1 COL2A1
guard, at 15.1x ambient against a 5x ceiling.

The guard was right and the reference was wrong. AMBIENT RNA IS A PROPERTY OF A
LIBRARY, NOT OF AN EXPERIMENT. The immune clusters that define the floor are
~99% donor1+donor2; donor3 is the cartilage-saturated library, whose chondrocyte
clusters carry 900-2,270 COL2A1 counts against 375 in the donor1/2-dominated
one. Pooling donor3 cells into a cluster and then scoring them against a
donor1/2 floor inflates the cluster's apparent COL2A1. The floor must be
measured in the same library as the cell it judges.

CONSEQUENCE, AND IT IS A COST. donor3 has essentially no immune cells (9 across
all immune clusters), so NO ambient reference can be built for it, and its cells
cannot be judged at all. They are dropped - not compared against someone else's
floor. That removes the most cartilage-rich library from both groups.

GUARDS, declared before the reservoir result is read:
  G0 A donor is retained only if it has >= 30 cells in immune clusters, i.e.
     only if its own ambient floor can be measured. Dropped donors are reported.
  G1 The ambient reference must be valid within the retained donors: immune
     COL2A1 at least 100-fold below chondrocyte COL2A1.
  G2 The stromal cluster must be COL1A1-high, PDGFRA-high, PTPRC-low, and at the
     ambient floor (mean within 5x of the immune mean) - all computed on
     retained donors only.
  G3 The stromal population must appear in MORE THAN ONE retained donor,
     >= 20 cells each.
  G4 GLI1 must clear a count floor: >= 50 total counts in the compared groups
     pooled, or the comparison is not made and that is reported.
"""
import sys, os, json
import numpy as np, pandas as pd, scanpy as sc, anndata as ad, scipy.sparse as sp

D=sys.argv[1]; CL=sys.argv[2]
OUT=sys.argv[3] if len(sys.argv)>3 else "/home/user/growth-plate/query/reservoir_v2.json"
FRESH={"GSM9328218_P30453_1001.h5":"donor1","GSM9328221_P31011_1001.h5":"donor2",
       "GSM9328224_P25452_001.h5":"donor3","GSM9328229_P22202_1015.h5":"donor4"}
cl=pd.read_csv(CL,index_col=0)
ads=[]
for fn,dn in FRESH.items():
    a=sc.read_10x_h5(os.path.join(D,fn)); a.var_names_make_unique()
    a.obs_names=[f"{dn}_{b}" for b in a.obs_names]; ads.append(a)
A=ad.concat(ads,join="outer"); A.var_names_make_unique()
A=A[cl.index].copy()
A.obs["leiden"]=cl["leiden"].astype(str).values
A.obs["donor"]=cl["donor"].values
LE=A.obs.leiden.values; DO=A.obs.donor.values
cls=sorted(set(LE), key=int)

def vec(mask,g):
    if g not in A.var_names: return np.zeros(int(mask.sum()))
    m=A[mask,g].X
    return np.asarray(m.todense()).ravel() if sp.issparse(m) else np.asarray(m).ravel()
def mn(mask,g):
    v=vec(mask,g); return float(v.mean()) if len(v) else float("nan")
def pcd(mask,g):
    v=vec(mask,g); return 100*float((v>0).mean()) if len(v) else float("nan")

# immune and chondrocyte clusters are identified on ALL cells; they define the
# two reference compartments, not the result.
immune=[c for c in cls if pcd(LE==c,"PTPRC")>=85 and mn(LE==c,"PTPRC")>=3]
chond =[c for c in cls if mn(LE==c,"COL2A1")>=500]
if not immune or not chond:
    print("no immune or no chondrocyte cluster; cannot build ambient reference"); sys.exit(1)
imm_mask=np.isin(LE,immune)

# ---- G0: which donors can be judged at all ----
print("PER-DONOR AMBIENT REFERENCE")
print(f"{'donor':<8}{'cells':>8}{'immune cells':>14}{'COL2A1 ambient':>17}")
amb_d={}; keep=[]
for d in sorted(set(DO)):
    n_imm=int((imm_mask&(DO==d)).sum())
    a=mn(imm_mask&(DO==d),"COL2A1") if n_imm else float("nan")
    amb_d[d]=a
    ok = n_imm>=30
    if ok: keep.append(d)
    print(f"{d:<8}{int((DO==d).sum()):>8}{n_imm:>14}{a:>17.2f}" + ("" if ok else"   <- DROPPED, floor not measurable"))
if len(keep)<2:
    print("\nG0 FAILED: fewer than two donors have a measurable ambient floor. REFUSING TO REPORT."); sys.exit(1)
print(f"\nretained donors: {keep}   dropped: {[d for d in sorted(set(DO)) if d not in keep]}")
K=np.isin(DO,keep)

amb=float(np.mean([amb_d[d] for d in keep]))
chm=mn(np.isin(LE,chond)&K,"COL2A1")
print(f"\nG1 ambient {amb:.2f} vs chondrocyte {chm:.1f}  -> {chm/amb:.0f}x separation")
fail=[]
if chm/amb < 100: fail.append(f"G1 FAILED: ambient separation only {chm/amb:.0f}x")

# ---- G2/G3: stromal identification, retained donors only ----
stromal=[c for c in cls if mn((LE==c)&K,"COL1A1")>=5 and pcd((LE==c)&K,"PDGFRA")>=40
         and pcd((LE==c)&K,"PTPRC")<40 and mn((LE==c)&K,"COL2A1")<=5*amb]
print(f"\nSTROMAL CANDIDATES (retained donors only): {stromal}")
for c in cls:
    if mn((LE==c)&K,"COL1A1")>=5:
        print(f"   cl{c}: COL1A1 {mn((LE==c)&K,'COL1A1'):.1f}  PDGFRA {pcd((LE==c)&K,'PDGFRA'):.0f}%  "
              f"PTPRC {pcd((LE==c)&K,'PTPRC'):.0f}%  COL2A1 {mn((LE==c)&K,'COL2A1'):.1f} = {mn((LE==c)&K,'COL2A1')/amb:.1f}x ambient")
if not stromal: fail.append("G2 FAILED: no cluster meets the stromal description")
else:
    dn={}
    for c in stromal:
        for d,n in pd.Series(DO[(LE==c)&K]).value_counts().items(): dn[d]=dn.get(d,0)+int(n)
    print(f"   donor composition (retained): {dn}")
    if sum(1 for v in dn.values() if v>=20) < 2: fail.append(f"G3 FAILED: not in >1 retained donor -> {dn}")
if fail: print("\n"+"\n".join(fail)+"\nREFUSING TO REPORT."); sys.exit(1)
print("guards G0-G3 PASS\n")

s_mask=np.isin(LE,stromal)&K; c_mask=np.isin(LE,chond)&K
print(f"{'gene':<9}{'stromal mean':>14}{'chondro mean':>14}{'ratio':>9}{'strom cts':>11}{'chond cts':>11}")
res={}
for g in ("COL1A1","PDGFRA","COL2A1","ACAN","PTPRC","GLI1","PTCH1","HHIP","GLI2","GLI3","SFRP5","PRRX1","THY1"):
    s=vec(s_mask,g); c=vec(c_mask,g)
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
print(f"\nstromal cells {int(s_mask.sum())}, chondrocyte cells {int(c_mask.sum())}")

# where does GLI1 actually sit? report per cluster, retained donors only.
print(f"\nGLI1 BY CLUSTER (retained donors):\n{'cl':>3}{'n':>7}{'GLI1 mean':>11}{'GLI1 cts':>10}{'SFRP5 mean':>12}{'COL2A1 mean':>13}")
percl={}
for c in cls:
    m=(LE==c)&K
    if m.sum()<20: continue
    percl[c]=dict(n=int(m.sum()),gli1_mean=mn(m,"GLI1"),gli1_counts=int(vec(m,"GLI1").sum()),
                  sfrp5_mean=mn(m,"SFRP5"),col2a1_mean=mn(m,"COL2A1"))
    print(f"{c:>3}{int(m.sum()):>7}{mn(m,'GLI1'):>11.3f}{int(vec(m,'GLI1').sum()):>10}{mn(m,'SFRP5'):>12.3f}{mn(m,'COL2A1'):>13.1f}")

json.dump({"retained_donors":keep,"dropped_donors":[d for d in sorted(set(DO)) if d not in keep],
           "ambient_per_donor":{k:(None if np.isnan(v) else float(v)) for k,v in amb_d.items()},
           "ambient_ratio":chm/amb,"immune_clusters":immune,"stromal_clusters":stromal,
           "chondrocyte_clusters":chond,"genes":res,"verdict":verdict,
           "n_stromal":int(s_mask.sum()),"n_chondro":int(c_mask.sum()),"per_cluster":percl},
          open(OUT,"w"),indent=1)
print(f"\nwrote {OUT}")
