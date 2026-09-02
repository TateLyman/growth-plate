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
g=lambda pre:[i for i,t in enumerate(T) if t.startswith(pre)]
P3, AU, AMF = g("P3_bulk"), g("Adult_uninjured"), g("Adult_MF_bulk")
print("n:",len(P3),len(AU),len(AMF))
expr=np.nanmean(X,1)>np.nanmedian(np.nanmean(X,1))
YOUTH = np.nanmean(X[:,P3],1)-np.nanmean(X[:,AU],1)     # young vs adult
ACT   = np.nanmean(X[:,AMF],1)-np.nanmean(X[:,AU],1)    # microfracture activation, ADULT
m=expr&np.isfinite(YOUTH)&np.isfinite(ACT)
print(f"\n*** DOES ADULT MICROFRACTURE MOVE THE TISSUE TOWARD THE YOUNG STATE? ***")
print(f"    r(activation, youth) = {np.corrcoef(ACT[m],YOUTH[m])[0,1]:+.3f}   (n={m.sum()} probes)")
# N signature
RZ=["Pthlh","Sfrp5","Sfrp1","Gas1","Spon1","Wif1","Prg4","Foxa2","Grem1","Sox9","Acan","Col2a1"]
FIB=["Col1a1","Col3a1","Postn","Tnc","Fn1","Acta2","Serpine1"]
BONE=["Sp7","Bglap","Alpl","Runx2","Ibsp"]
def z(vec,genes):
    idx=[i for i,s in enumerate(S) if s in genes and expr[i] and np.isfinite(vec[i])]
    gg=vec[expr&np.isfinite(vec)]
    return (np.nanmean(vec[idx])-gg.mean())/(gg.std()/np.sqrt(len(idx))), len(idx)
print("\n=== PANELS: adult microfracture activation vs uninjured adult ===")
for nm,pan in [("stem/chondro (N)",RZ),("FIBROUS",FIB),("BONE/osteogenic",BONE)]:
    zz,n=z(ACT,set(pan)); print(f"  {nm:20s} z={zz:+6.2f}  (n={n})")
print("\n=== per-gene, adult MF vs uninjured ===")
for gg in RZ+FIB:
    idx=[i for i,s in enumerate(S) if s==gg and expr[i]]
    if idx: print(f"   {gg:9s} {np.nanmean(ACT[idx]):+6.2f}")
# BMP2 / VEGFr1 on sorted SSC (n=1 each, report as-is)
c=[i for i,t in enumerate(T) if t=="Adult_MF_mSSC_control"][0]
b=[i for i,t in enumerate(T) if t=="Adult_MF_mSSC_BMP2"][0]
v=[i for i,t in enumerate(T) if t=="Adult_MF_mSSC_VEGFr1"][0]
dB=X[:,b]-X[:,c]; dV=X[:,v]-X[:,c]
print("\n=== SORTED mSSC: BMP2 and sVEGFR1 vs control (n=1 each - directional only) ===")
for nm,pan in [("stem/chondro (N)",RZ),("FIBROUS",FIB),("BONE/osteogenic",BONE)]:
    zb,_=z(dB,set(pan)); zv,_=z(dV,set(pan)); print(f"  {nm:20s} BMP2 z={zb:+6.2f}   sVEGFR1 z={zv:+6.2f}")
