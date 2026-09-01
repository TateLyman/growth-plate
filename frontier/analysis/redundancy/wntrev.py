import numpy as np, gzip, json
sym=json.load(open("gpl17586_sym.json"))
print("annot entries:",len(sym))
ids=[];X=[]
with gzip.open("GSE211559_norm.txt.gz",'rt',errors='replace') as f:
    hdr=f.readline().rstrip('\n').split('\t')
    for l in f:
        p=l.rstrip('\n').split('\t')
        try: v=[float(x) for x in p[1:7]]
        except: continue
        ids.append(p[0]); X.append(v)
X=np.array(X); ids=np.array(ids)
cols=[c.replace('.CEL','') for c in hdr[1:7]]
T=[i for i,c in enumerate(cols) if c.endswith("TGFb")]
W=[i for i,c in enumerate(cols) if c.endswith("XAV")]
D=X[:,W].mean(1)-X[:,T].mean(1)
S=np.array([sym.get(i,"") for i in ids])
print("probes",X.shape,"mapped:",(S!="").sum())
expr=X.mean(1)>np.median(X.mean(1))
RZ=["PTHLH","SFRP5","SFRP1","GAS1","SPON1","WIF1","PRG4","FOXA2","GREM1","DKK2","NOTUM"]
CHON=["SOX9","ACAN","COL2A1","COL9A1","COL11A1"]
HYP=["COL10A1","IHH","MMP13","SPP1","RUNX2","ALPL"]
FIB=["COL1A1","COL3A1","POSTN","TNC","ACTA2"]
def z(vec,genes):
    idx=[i for i,s in enumerate(S) if s in genes and expr[i] and np.isfinite(vec[i])]
    if not idx: return float("nan"),0
    g=vec[expr&np.isfinite(vec)]
    return (np.nanmean(vec[idx])-g.mean())/(g.std()/np.sqrt(len(idx))), len(idx)
print("\n=== REVERSE WNT (XAV939 tankyrase inhibitor) vs TGFb, 3 paired human MSC lines ===")
for nm,pan in [("RESTING/STEM (N)",RZ),("chondrocyte",CHON),("hypertrophic",HYP),("fibrous",FIB)]:
    zz,n=z(D,set(pan)); print(f"  {nm:20s} z={zz:+6.2f}  (n={n})")
print("\n  per-gene (XAV - TGFb, log2):")
for g in RZ+CHON+HYP:
    idx=[i for i,s in enumerate(S) if s==g and expr[i]]
    if idx: print(f"   {g:9s} {np.nanmean(D[idx]):+6.2f}")
