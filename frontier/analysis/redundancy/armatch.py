import numpy as np, gzip
exec(open("steroid.py").read().split('Z={"Reserve"')[0])
ids,T,X=load("GSE9160_series_matrix.txt.gz"); A=ann("GPL570.annot.gz"); S=np.array([A.get(i,"") for i in ids])
Z={"Reserve":[i for i,t in enumerate(T) if t.startswith("Reserve")],
   "Prolif":[i for i,t in enumerate(T) if t.startswith("Proliferative")],
   "PreHyp":[i for i,t in enumerate(T) if t.startswith("Prehypertrophic")],
   "Hyper":[i for i,t in enumerate(T) if t.startswith("Hypertrophic")]}
order=["Reserve","Prolif","PreHyp","Hyper"]
def prof(g):
    idx=[i for i,s in enumerate(S) if s==g]
    if not idx: return None
    v=np.array([np.nanmean(X[np.ix_(idx,Z[z])]) for z in order])
    return v/v.mean()
RZ=["PTHLH","SFRP5","SFRP1","GAS1","SPON1","WIF1","PRG4","FOXA2","GREM1","APOE","NT5E","CD73"]
print("ZONAL SHAPE, normalised to each gene's own mean across the four cartilage zones")
print(f"{'gene':10s}"+"".join(f"{z:>9s}" for z in order)+"   RZ-enriched?")
sig=[]
for g in RZ:
    v=prof(g)
    if v is None: print(f"{g:10s}   no probe"); continue
    sig.append(v); print(f"{g:10s}"+"".join(f"{x:9.2f}" for x in v)+f"   {'YES' if v[0]==v.max() else ''}")
sig=np.array(sig); m=sig.mean(0)
print(f"{'RZ MEAN':10s}"+"".join(f"{x:9.2f}" for x in m))
print()
for g in ["AR","ESR1","ESR2","GPER1","NR3C1","SRD5A1","SRD5A3","CYP19A1"]:
    v=prof(g)
    if v is None: continue
    r=np.corrcoef(v,m)[0,1]
    print(f"{g:10s}"+"".join(f"{x:9.2f}" for x in v)+f"   r vs RZ signature = {r:+.3f}")
print("\n(4 zones only, so r has 2 df — directional, not inferential.)")
print("\n=== ABSOLUTE LEVELS IN THE RESTING ZONE, ranked ===")
lv=[]
for g in ["AR","ESR1","ESR2","GPER1","PGR","NR3C1","CYP19A1","SRD5A1","SRD5A2","SRD5A3","PTHLH","SFRP5"]:
    idx=[i for i,s in enumerate(S) if s==g]
    if idx: lv.append((g,np.nanmean(X[np.ix_(idx,Z["Reserve"])])))
for g,v in sorted(lv,key=lambda x:-x[1]): print(f"   {g:10s} {v:9.1f}")
