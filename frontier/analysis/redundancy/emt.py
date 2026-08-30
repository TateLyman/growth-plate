import numpy as np, gzip
exec(open("steroid.py").read().split('Z={"Reserve"')[0])
ids,T,X=load("GSE9160_series_matrix.txt.gz"); A=ann("GPL570.annot.gz"); S=np.array([A.get(i,"") for i in ids])
Z={"Reserve":[i for i,t in enumerate(T) if t.startswith("Reserve")],
   "Prolif":[i for i,t in enumerate(T) if t.startswith("Proliferative")],
   "PreHyp":[i for i,t in enumerate(T) if t.startswith("Prehypertrophic")],
   "Hyper":[i for i,t in enumerate(T) if t.startswith("Hypertrophic")]}
order=["Reserve","Prolif","PreHyp","Hyper"]
EPI=["CDH1","CLDN6","COL4A1","KRT19","LAMC1"]
MES=["ACTA2","CTNNB1","SMAD3","SNAI1","SNAI2","ZEB1","VIM"]
TGF=["TGFB1","TGFB2","TGFB3","SMAD2","SMAD4","SMAD7","TGFBR1","TGFBR2"]
def prof(g):
    idx=[i for i,s in enumerate(S) if s==g]
    if not idx: return None,None
    v=np.array([np.nanmean(X[np.ix_(idx,Z[z])]) for z in order])
    return v, v/v.mean()
print("ZHOU 2015's CENTRAL CLAIM, TESTED IN HUMAN (GSE9160, LCM zones, 2 normal children)")
print("PREDICTION: epithelial HIGH in RZ and HZ, LOW in PZ  ->  ratio PZ/(RZ,HZ) < 1")
print("            mesenchymal the inverse                  ->  ratio PZ/(RZ,HZ) > 1\n")
def block(name,genes,pred):
    print(f"--- {name} (predicted {pred}) ---")
    print(f"{'gene':10s}"+"".join(f"{z:>9s}" for z in order)+"   PZ/mean(RZ,HZ)   matches?")
    rs=[]
    for g in genes:
        raw,nrm=prof(g)
        if raw is None: print(f"{g:10s}   no probe"); continue
        r=raw[1]/np.mean([raw[0],raw[3]])
        ok = (r<1) if pred=="PZ LOW" else (r>1)
        rs.append(r)
        print(f"{g:10s}"+"".join(f"{x:9.1f}" for x in raw)+f"   {r:9.2f}      {'YES' if ok else 'no'}")
    if rs:
        n=sum((r<1) if pred=="PZ LOW" else (r>1) for r in rs)
        print(f"   -> {n}/{len(rs)} genes match; median ratio {np.median(rs):.2f}\n")
block("EPITHELIAL (Zhou: high RZ+HZ, low PZ)",EPI,"PZ LOW")
block("MESENCHYMAL (Zhou: high PZ)",MES,"PZ HIGH")
block("TGF-beta / SMAD axis (Zhou: the gate)",TGF,"PZ HIGH")
