import sys, os
import numpy as np, pandas as pd, scanpy as sc, anndata as ad, scipy.sparse as sp
D=sys.argv[1]; CL=sys.argv[2]
FRESH={"GSM9328218_P30453_1001.h5":"donor1","GSM9328221_P31011_1001.h5":"donor2",
       "GSM9328224_P25452_001.h5":"donor3","GSM9328229_P22202_1015.h5":"donor4"}
cl=pd.read_csv(CL,index_col=0); ads=[]
for fn,dn in FRESH.items():
    a=sc.read_10x_h5(os.path.join(D,fn)); a.var_names_make_unique()
    a.obs_names=[f"{dn}_{b}" for b in a.obs_names]; ads.append(a)
A=ad.concat(ads,join="outer"); A.var_names_make_unique()
A=A[cl.index].copy(); A.obs["leiden"]=cl["leiden"].astype(str).values
A.obs["donor"]=cl["donor"].values
cls=sorted(A.obs.leiden.unique(),key=int)
idx={c:np.where(A.obs.leiden.values==c)[0] for c in cls}
def vec(cells,g):
    m=A[cells,g].X
    return np.asarray(m.todense()).ravel() if sp.issparse(m) else np.asarray(m).ravel()
def mn(c,g): return float(vec(idx[c],g).mean())
def pc(c,g): return 100*float((vec(idx[c],g)>0).mean())
imm=[c for c in cls if pc(c,"PTPRC")>=85 and mn(c,"PTPRC")>=3]
amb=np.mean([mn(c,"COL2A1") for c in imm])
print(f"ambient (immune {imm}) COL2A1 mean = {amb:.2f}; G2 ceiling 5x = {5*amb:.2f}\n")
print(f"{'cl':>3}{'n':>7}{'COL1A1mn':>10}{'PDGFRA%':>9}{'PTPRC%':>8}{'COL2A1mn':>10}{'/amb':>8}{'ACANmn':>9}{'GLI1mn':>8}  donors")
for c in cls:
    d=A.obs.loc[A.obs.leiden==c,"donor"].value_counts().to_dict()
    dd=",".join(f"{k[-1]}:{v}" for k,v in sorted(d.items()))
    print(f"{c:>3}{len(idx[c]):>7}{mn(c,'COL1A1'):>10.2f}{pc(c,'PDGFRA'):>9.1f}{pc(c,'PTPRC'):>8.1f}"
          f"{mn(c,'COL2A1'):>10.1f}{mn(c,'COL2A1')/amb:>8.1f}{mn(c,'ACAN'):>9.2f}{mn(c,'GLI1'):>8.3f}  {dd}")
