import numpy as np, gzip, re
def load(fn):
    rows=[];hdr=None;on=False;titles=None
    with gzip.open(fn,'rt',errors='replace') as f:
        for l in f:
            l=l.rstrip('\n')
            if l.startswith('!Sample_title'): titles=[x.strip('"') for x in l.split('\t')[1:]]
            if l.startswith('!series_matrix_table_begin'): on=True; continue
            if l.startswith('!series_matrix_table_end'): break
            if on:
                p=l.split('\t')
                if hdr is None: hdr=p; continue
                rows.append(p)
    ids=[r[0].strip('"') for r in rows]
    X=np.full((len(rows),len(hdr)-1),np.nan)
    for i,r in enumerate(rows):
        for j in range(1,min(len(r),len(hdr))):
            try: X[i,j-1]=float(r[j])
            except: pass
    return ids,titles,X
ids,titles,X=load("GSE16981_series_matrix.txt.gz")
X=np.log2(np.clip(X,1,None))
sym={}
with gzip.open("GPL1355.annot.gz",'rt',errors='replace') as f:
    on=False
    for l in f:
        if l.startswith('!platform_table_begin'): on=True; next(f); continue
        if l.startswith('!platform_table_end'): break
        if on:
            p=l.split('\t')
            if len(p)>2 and p[2].strip(): sym[p[0]]=p[2].strip()
S=np.array([sym.get(i,"") for i in ids])
# age series in PZ
ages=[3,6,9,12]
cols={a:[i for i,t in enumerate(titles) if f"_{a}wk" in t] for a in ages}
print("PZ age series n:", {a:len(cols[a]) for a in ages})
genes=["Npr2","Npr3","Mme","Nppc","Nppa","Nppb","Prkg2","Pth1r","Ihh","Col10a1","Mki67","Fgfr3","Ostn"]
print(f"\n{'gene':8s}" + "".join(f"{a:>8}wk" for a in ages) + "   slope/log2age   r")
print("-"*62)
la=np.log2(ages)
for g in genes:
    idx=[i for i,s in enumerate(S) if s==g]
    if not idx: print(f"{g:8s}  (no probe)"); continue
    m=[np.nanmean(X[np.ix_(idx,cols[a])]) for a in ages]
    if not np.all(np.isfinite(m)): print(f"{g:8s}  (nan)"); continue
    sl=np.polyfit(la,m,1)[0]; r=np.corrcoef(la,m)[0,1]
    print(f"{g:8s}" + "".join(f"{v:10.2f}" for v in m) + f"   {sl:+7.3f}     {r:+.3f}")

print("\n=== ZONE comparison at the young timepoint (RZ / PZ / HZ) ===")
zc={"RZ":[i for i,t in enumerate(titles) if t.startswith("Resting")],
    "PZ":[i for i,t in enumerate(titles) if t.startswith("Proliferative zone,")],
    "HZ":[i for i,t in enumerate(titles) if t.startswith("Hypertrophic")]}
print({k:len(v) for k,v in zc.items()})
print(f"{'gene':8s}" + "".join(f"{z:>9s}" for z in ["RZ","PZ","HZ"]))
for g in ["Npr2","Npr3","Mme","Prkg2","Pth1r","Ihh","Col10a1"]:
    idx=[i for i,s in enumerate(S) if s==g]
    if not idx: continue
    print(f"{g:8s}" + "".join(f"{np.nanmean(X[np.ix_(idx,zc[z])]):9.2f}" for z in ["RZ","PZ","HZ"]))
