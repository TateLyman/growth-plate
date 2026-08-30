import numpy as np, gzip
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
ids,T,X=load("GSE151303-GPL1261_series_matrix.txt.gz")
if np.nanmax(X)>50: X=np.log2(np.clip(X,1,None))
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
g=lambda p:[i for i,t in enumerate(T) if t.startswith(p)]
P3,AU,AMF=g("P3_bulk"),g("Adult_uninjured"),g("Adult_MF_bulk")
YOUTH=np.nanmean(X[:,P3],1)-np.nanmean(X[:,AU],1)
ACT  =np.nanmean(X[:,AMF],1)-np.nanmean(X[:,AU],1)
sdA  =np.nanstd(X[:,AMF],1); sdU=np.nanstd(X[:,AU],1)
expr=np.nanmean(X,1)>np.nanmedian(np.nanmean(X,1))
m=expr&np.isfinite(YOUTH)&np.isfinite(ACT)&(S!="")

# THE REJUVENATING CORE: up in activation AND up in youth
both=m&(ACT>0.6)&(YOUTH>0.6)
print(f"genes UP in adult microfracture AND UP in youth: {both.sum()}")
order=np.argsort(-(ACT+YOUTH)*both)
seen=set(); rows=[]
for i in order:
    if not both[i]: continue
    if S[i] in seen: continue
    seen.add(S[i]); rows.append((S[i],ACT[i],YOUTH[i]))
    if len(rows)>=60: break
print(f"\n{'gene':12s}{'ACT':>7s}{'YOUTH':>8s}")
for s,a,y in rows: print(f"{s:12s}{a:+7.2f}{y:+8.2f}")
np.save("ACT.npy",ACT); np.save("YOUTH.npy",YOUTH); np.save("mask.npy",m)
import json; json.dump([str(x) for x in S],open("S151303.json","w"))
