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
def ann(f):
    s={}
    with gzip.open(f,'rt',errors='replace') as fh:
        on=False
        for l in fh:
            if l.startswith('!platform_table_begin'): on=True; next(fh); continue
            if l.startswith('!platform_table_end'): break
            if on:
                p=l.split('\t')
                if len(p)>2 and p[2].strip(): s[p[0]]=p[2].strip()
    return s
ids,T,X=load("GSE9160_series_matrix.txt.gz"); A=ann("GPL570.annot.gz"); S=np.array([A.get(i,"") for i in ids])
Z={"Reserve":[i for i,t in enumerate(T) if t.startswith("Reserve")],
   "Prolif":[i for i,t in enumerate(T) if t.startswith("Proliferative")],
   "PreHyp":[i for i,t in enumerate(T) if t.startswith("Prehypertrophic")],
   "Hyper":[i for i,t in enumerate(T) if t.startswith("Hypertrophic")],
   "Perich":[i for i,t in enumerate(T) if t.startswith("Perichondrium")]}
order=["Reserve","Prolif","PreHyp","Hyper","Perich"]
print("HUMAN GROWTH PLATE, LCM zone-resolved, 2 normal children (F 11y10m, M 13y3m)")
print("Affymetrix HG-U133 Plus 2.0, globally scaled — values comparable to the atlas's")
print("own GSE9160 calibrators (NPPC never >19.8; PTHLH 308.6; GDF5 603.8; COL2A1 >100,000)\n")
groups=[("--- CALIBRATORS (sanity) ---",["COL2A1","COL10A1","ACAN","PTHLH","IHH","SPP1"]),
        ("--- RECEPTORS: does the plate SEE androgen? ---",["AR","ESR1","ESR2","GPER1","PGR","NR3C1"]),
        ("--- LOCAL SYNTHESIS: can the plate MAKE DHT or E2? ---",["SRD5A1","SRD5A2","SRD5A3","CYP19A1","HSD17B3","HSD17B2","HSD17B1","STS","SULT2B1"]),
        ("--- ANDROGEN'S GROWTH MECHANISM ---",["IGF1","IGF1R","IGF2","IGFBP3","IGFBP5","SHBG"]),
        ("--- AR COACTIVATORS / TARGET ---",["FKBP5","KLK3","NKX3-1","TMPRSS2"])]
for hdr,genes in groups:
    print(hdr); print(f"{'gene':10s}"+"".join(f"{z:>10s}" for z in order))
    for g in genes:
        idx=[i for i,s in enumerate(S) if s==g]
        if not idx: print(f"{g:10s}   (no probe)"); continue
        v=[np.nanmean(X[np.ix_(idx,Z[z])]) for z in order]
        print(f"{g:10s}"+"".join(f"{x:10.1f}" for x in v))
    print()
