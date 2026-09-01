import numpy as np, re, urllib.request, gzip, io
L=open('matrix.txt',encoding='utf-8',errors='replace').read().split('\n')
title=[x.strip('"') for x in [l for l in L if l.startswith('!Sample_title')][0].split('\t')[1:]]
i=[n for n,l in enumerate(L) if l.startswith('!series_matrix_table_begin')][0]
j=[n for n,l in enumerate(L) if l.startswith('!series_matrix_table_end')][0]
rows=[l.split('\t') for l in L[i+2:j] if l.strip()]
ids=np.array([r[0].strip('"') for r in rows])
X=np.array([[float(v) if v not in ('','null','NA') else np.nan for v in r[1:]] for r in rows])
# PZ time course from titles
wk=[]; sel=[]
for n,t in enumerate(title):
    m=re.search(r'Proliferative zone_(\d+)wk',t)
    if m: sel.append(n); wk.append(int(m.group(1)))
sel=np.array(sel); t=np.array(wk,float)
Y=X[:,sel]; ok=~np.isnan(Y).any(axis=1)
Y=Y[ok]; I=ids[ok]
print('PZ samples n=%d ages %s ; probes %d'%(len(t),sorted(set(t)),Y.shape[0]))
lt=np.log(t); Yc=Y-Y.mean(1,keepdims=True); lc=lt-lt.mean()
r=(Yc@lc)/np.sqrt((Yc**2).sum(1)*(lc**2).sum())
# map probes -> gene symbols from the platform
try:
    u='https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL341nnn/GPL341/annot/GPL341.annot.gz'
    raw=gzip.decompress(urllib.request.urlopen(u,timeout=120).read()).decode('utf-8','replace')
    sym={}
    for l in raw.split('\n'):
        if l.startswith('#') or l.startswith('!') or '\t' not in l: continue
        p=l.split('\t')
        if len(p)>2: sym[p[0]]=p[1]
    print('annotation loaded:',len(sym))
except Exception as e:
    sym={}; print('annot failed',e)
g=np.array([sym.get(x,x) for x in I])
o=np.argsort(r)
print('\n=== 30 genes DOWN with age in the proliferative zone (senescence signature) ===')
seen=set()
for k in o:
    if g[k] in seen or g[k]=='' : continue
    seen.add(g[k]); print('  %-16s r=%+.3f'%(g[k][:16],r[k]))
    if len(seen)>=30: break
print('\n=== 30 genes UP with age ===')
seen=set()
for k in o[::-1]:
    if g[k] in seen or g[k]=='': continue
    seen.add(g[k]); print('  %-16s r=%+.3f'%(g[k][:16],r[k]))
    if len(seen)>=30: break
np.save('r.npy',r); np.save('genes.npy',g)
