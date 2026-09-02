import numpy as np, json, gzip
dC=np.load("dCNP.npy"); dF=np.load("dFG.npy"); expr=np.load("expr.npy")
ids=json.load(open("GSE4481_meta.json"))["ids"]
sym={}
with gzip.open("GPL1261.annot.gz",'rt',errors='replace') as f:
    on=False
    for l in f:
        if l.startswith('!platform_table_begin'): on=True; next(f); continue
        if l.startswith('!platform_table_end'): break
        if on:
            p=l.split('\t')
            if len(p)>2 and p[2].strip(): sym[p[0]]=p[2].strip()
S=np.array([sym.get(i,"") for i in ids])
print("annotated:", (S!="").sum(), "/", len(S))

# marker panels
P={
 "N  resting/stem pool":["Pthlh","Sfrp5","Gdf5","Nt5e","Foxa2","Cd34","Ly6a","Gremlin1","Grem1","Wif1","Dkk3"],
 "A  proliferative/column":["Mki67","Ccnb1","Ccnd1","Top2a","Pcna","Col2a1","Acan","Sox5","Sox6","Birc5","Aurkb"],
 "h  hypertrophic/h_term":["Col10a1","Ihh","Mmp13","Sp7","Panx3","Alpl","Spp1","Bglap","Runx2","Vegfa","Mef2c"],
 "closure/vascular":["Mmp9","Vegfa","Pecam1","Ctsk","Acp5","Sost"],
}
def score(vec,genes):
    idx=[i for i,s in enumerate(S) if s in genes and expr[i] and np.isfinite(vec[i])]
    if not idx: return np.nan,0
    v=vec[idx]
    # z against genome-wide
    g=vec[expr&np.isfinite(vec)]
    return (v.mean()-g.mean())/(g.std()/np.sqrt(len(v))), len(idx)

print("\n=== ERDA-DIRECTION (FGFR3 blockade = WT - Fgfr3GOF): zone-panel z-scores ===")
print(f"{'panel':26s}" + "".join(f"   wk{w}  " for w in [1,2,3,4]))
for k,g in P.items():
    row=f"{k:26s}"
    for j in range(4):
        z,n=score(dF[j],set(g)); row+=f" {z:+6.2f}"
    z,n=score(dF[0],set(g)); row+=f"   (n={n})"
    print(row)
print("\n=== CNP direction: zone-panel z-scores ===")
print(f"{'panel':26s}" + "".join(f"  {z:5s}" for z in ["R/P","H","M"]))
for k,g in P.items():
    row=f"{k:26s}"
    for j in range(3):
        z,n=score(dC[j],set(g)); row+=f" {z:+6.2f}"
    print(row)
