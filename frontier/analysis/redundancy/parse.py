import gzip, numpy as np, re, json
def load(gse):
    rows=[]; hdr=None; inTab=False; meta={}
    with gzip.open(gse+".txt.gz",'rt',errors='replace') as f:
        for l in f:
            l=l.rstrip('\n')
            if l.startswith('!Sample_title'):
                meta['title']=[x.strip('"') for x in l.split('\t')[1:]]
            if l.startswith('!series_matrix_table_begin'): inTab=True; continue
            if l.startswith('!series_matrix_table_end'): break
            if inTab:
                p=l.split('\t')
                if hdr is None: hdr=[x.strip('"') for x in p]; continue
                rows.append(p)
    ids=[r[0].strip('"') for r in rows]
    X=np.full((len(rows),len(hdr)-1), np.nan)
    for i,r in enumerate(rows):
        for j in range(1,min(len(r),len(hdr))):
            try: X[i,j-1]=float(r[j])
            except: pass
    return ids, hdr[1:], X, meta['title']

for g in ["GSE4481","GSE145821"]:
    ids,cols,X,titles = load(g)
    print(g, "probes",len(ids), "samples",X.shape[1])
    print("  range", np.nanmin(X), np.nanmax(X))
    print("  titles", titles[:6])
    np.save(f"{g}_X.npy", X); json.dump({"ids":ids,"titles":titles}, open(f"{g}_meta.json","w"))
