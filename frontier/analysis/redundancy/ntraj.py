import numpy as np, gzip
RZ=["Gas1","Spon1","Wif1","Pthlh","Sfrp5","Prg4","Sfrp1","Dkk2","Notum","Fzd6"]
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
    return ids,titles,np.log2(np.clip(X,1,None))
ids,titles,X=load("GSE16981_series_matrix.txt.gz")
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
zc={"RZ":[i for i,t in enumerate(titles) if t.startswith("Resting")],
    "PZ":[i for i,t in enumerate(titles) if t.startswith("Proliferative zone,")],
    "HZ":[i for i,t in enumerate(titles) if t.startswith("Hypertrophic")]}
print("=== RZ SIGNATURE: is it zone-specific in rat? (validates the panel) ===")
print(f"{'gene':8s}{'RZ':>8s}{'PZ':>8s}{'HZ':>8s}   RZ-HZ")
tot=[]
for g in RZ:
    idx=[i for i,s in enumerate(S) if s==g]
    if not idx: print(f"{g:8s}  no probe"); continue
    v=[np.nanmean(X[np.ix_(idx,zc[z])]) for z in ["RZ","PZ","HZ"]]
    tot.append(v); print(f"{g:8s}"+"".join(f"{x:8.2f}" for x in v)+f"   {v[0]-v[2]:+.2f}")
t=np.array(tot); print(f"{'MEAN':8s}"+"".join(f"{x:8.2f}" for x in t.mean(0))+f"   {t.mean(0)[0]-t.mean(0)[2]:+.2f}")

ages=[3,6,9,12]; cols={a:[i for i,t in enumerate(titles) if f"_{a}wk" in t] for a in ages}
print("\n=== N TRAJECTORY: RZ signature in the PROLIFERATIVE zone across age ===")
print(f"{'gene':8s}"+"".join(f"{a:>8}wk" for a in ages)+"    r vs log-age")
la=np.log2(ages); rows=[]
for g in RZ:
    idx=[i for i,s in enumerate(S) if s==g]
    if not idx: continue
    m=[np.nanmean(X[np.ix_(idx,cols[a])]) for a in ages]
    if not np.all(np.isfinite(m)): continue
    rows.append(m); print(f"{g:8s}"+"".join(f"{v:10.2f}" for v in m)+f"    {np.corrcoef(la,m)[0,1]:+.3f}")
R=np.array(rows); m=R.mean(0)
print(f"{'MEAN':8s}"+"".join(f"{v:10.2f}" for v in m)+f"    {np.corrcoef(la,m)[0,1]:+.3f}")
print(f"\ntotal decline 3->12wk: {m[-1]-m[0]:+.3f} log2 = {2**(m[-1]-m[0]):.2f}x")
