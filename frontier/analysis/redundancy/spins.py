import numpy as np, gzip
exec(open("steroid.py").read().split('Z={"Reserve"')[0])
ids,T,X=load("GSE9160_series_matrix.txt.gz"); A=ann("GPL570.annot.gz"); S=np.array([A.get(i,"") for i in ids])
Z={"Reserve":[i for i,t in enumerate(T) if t.startswith("Reserve")],
   "Prolif":[i for i,t in enumerate(T) if t.startswith("Proliferative")],
   "PreHyp":[i for i,t in enumerate(T) if t.startswith("Prehypertrophic")],
   "Hyper":[i for i,t in enumerate(T) if t.startswith("Hypertrophic")],
   "Perich":[i for i,t in enumerate(T) if t.startswith("Perichondrium")]}
order=["Reserve","Prolif","PreHyp","Hyper","Perich"]
allv=X[np.isfinite(X)]
p25,p50,p75=np.percentile(allv,[25,50,75])
print("HUMAN GROWTH PLATE, LCM zone-resolved (GSE9160). Array percentiles:")
print(f"  25th={p25:.1f}  50th={p50:.1f}  75th={p75:.1f}   (atlas calibrators: NPPC<=19.8 absent; PTHLH 308.6 present)\n")
print(f"{'gene':10s}"+"".join(f"{z:>10s}" for z in order)+"    call")
fam=["SPIN1","SPIN2A","SPIN2B","SPIN3","SPIN4","SPINT1","SPINT2"]
for g in fam:
    idx=[i for i,s in enumerate(S) if s==g]
    if not idx: print(f"{g:10s}   NO PROBE ON ARRAY"); continue
    v=[np.nanmean(X[np.ix_(idx,Z[z])]) for z in order]
    mx=max(v)
    call = "EXPRESSED" if mx>p50 else ("low" if mx>p25 else "ABSENT/floor")
    print(f"{g:10s}"+"".join(f"{x:10.1f}" for x in v)+f"    {call}  (n probe={len(idx)})")
print("\n--- reference points on the same array ---")
for g in ["PTHLH","COL2A1","SOX9","AR","ESR1","NPPC","CTNNB1","AXIN2","LEF1","TCF7"]:
    idx=[i for i,s in enumerate(S) if s==g]
    if idx:
        v=[np.nanmean(X[np.ix_(idx,Z[z])]) for z in order]
        print(f"{g:10s}"+"".join(f"{x:10.1f}" for x in v))
