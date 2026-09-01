import h5py, numpy as np, glob
from scipy.sparse import csc_matrix
from scipy.stats import wilcoxon
GP1_SIG=['SFRP5','THBS1','THBS2','DCN','CYTL1','FRZB']
GENES=['PTCH1','SMO','GLI1','GLI2','GLI3','HHIP','SUFU','IHH','BOC','CDON','GAS1','EVC2','ARL13B','PTHLH','MKI67','TOP2A','COL2A1','ACAN']+GP1_SIG
res={}
for f in sorted(glob.glob('GSM*.h5')):
    with h5py.File(f,'r') as h:
        if h['matrix/shape'][0]!=36601: continue
        names=np.array([x.decode() for x in h['matrix/features/name'][:]])
        M=csc_matrix((h['matrix/data'][:],h['matrix/indices'][:],h['matrix/indptr'][:]),
                     shape=tuple(h['matrix/shape'][:])).tocsr()
    idx={g:np.where(names==g)[0][0] for g in set(GENES) if (names==g).any()}
    missing=[g for g in GENES if g not in idx]
    tot=np.asarray(M.sum(axis=0)).ravel(); ng=np.asarray((M>0).sum(axis=0)).ravel()
    R=lambda g: np.asarray(M[idx[g]].todense()).ravel()
    keep=(ng>=500)&(ng<=8000)&(tot>=1000)&((R('COL2A1')>0)|(R('ACAN')>0))
    if keep.sum()<200: continue
    sf=1e4/np.maximum(tot,1)
    d={g:np.log1p(R(g)*sf)[keep] for g in idx}
    g1=np.mean([d[g] for g in GP1_SIG if g in d],axis=0)
    pr=np.mean([d[g] for g in ['MKI67','TOP2A'] if g in d],axis=0)
    root=(g1>=np.quantile(g1,0.80))&(pr==0); lo=(g1<np.quantile(g1,0.5))
    res[f]=dict(d=d,root=root,lo=lo,n=int(keep.sum()),miss=missing)
    print('%-28s cells=%5d root=%5d missing=%s'%(f[:28],keep.sum(),root.sum(),missing))

print('\n=== ABSOLUTE: %% of GP1-root cells with detected transcript (per sample) ===')
print('%-10s'%'gene', ' '.join('S%d'%i for i in range(1,len(res)+1)), '  median')
for g in ['PTCH1','SMO','GLI1','GLI2','HHIP','SUFU','BOC','IHH','PTHLH']:
    v=[100*(r['d'][g][r['root']]>0).mean() for r in res.values() if g in r['d']]
    print('%-10s'%g, ' '.join('%4.0f'%x for x in v), '  %5.1f%%'%np.median(v))

print('\n=== ENRICHMENT root vs GP1-lo: per-sample log2 fold, paired Wilcoxon across samples ===')
print('%-8s %-46s %8s %8s'%('gene','per-sample log2FC','median','p'))
for g in ['PTCH1','SMO','GLI1','GLI2','HHIP','SUFU','BOC','CDON','IHH','EVC2','ARL13B']:
    fc=[]
    for r in res.values():
        if g not in r['d']: continue
        a=r['d'][g][r['root']].mean(); b=r['d'][g][r['lo']].mean()
        fc.append(np.log2((np.expm1(a)+1e-4)/(np.expm1(b)+1e-4)))
    fc=np.array(fc)
    try: p=wilcoxon(fc).pvalue
    except Exception: p=np.nan
    print('%-8s %-46s %8.2f %8.4f'%(g,' '.join('%+.1f'%x for x in fc),np.median(fc),p))
