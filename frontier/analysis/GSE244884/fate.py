import h5py, numpy as np
from scipy.sparse import csc_matrix
SETS={
 'RZ_stem'   :['Pthlh','Sfrp5','Cytl1','Thbs1','Thbs2','Dcn','Grem1','Fgfr3','Sox9'],
 'prolif'    :['Mki67','Top2a','Ccnb1','Cdk1','Birc5'],
 'preHT_HT'  :['Ihh','Col10a1','Mef2c','Ibsp','Spp1','Panx3'],
 'osteoblast':['Col1a1','Sp7','Bglap','Runx2','Alpl','Postn','Ifitm5'],
 'stromal'   :['Cxcl12','Lepr','Adipoq','Kitl'],
}
HH=['Ptch1','Gli1','Hhip','Smo','Ptch2']
def load(f):
    with h5py.File(f,'r') as h:
        names=np.array([x.decode() for x in h['matrix/features/name'][:]])
        M=csc_matrix((h['matrix/data'][:],h['matrix/indices'][:],h['matrix/indptr'][:]),
                     shape=tuple(h['matrix/shape'][:])).tocsr()
    return M,names
for lab,f in [('Ptch1 cHET (fl/+)','GSM7831319.h5'),('Ptch1 cKO (fl/fl)','GSM7831318.h5')]:
    M,names=load(f)
    tot=np.asarray(M.sum(axis=0)).ravel(); ng=np.asarray((M>0).sum(axis=0)).ravel()
    mito=[i for i,n in enumerate(names) if n.startswith('mt-')]
    mfrac=np.asarray(M[mito].sum(axis=0)).ravel()/np.maximum(tot,1)
    keep=(ng>=1000)&(mfrac<0.15)
    idx={n:i for i,n in enumerate(names)}
    sf=1e4/np.maximum(tot,1)
    def sc(gs):
        gs=[g for g in gs if g in idx]
        X=np.log1p(np.asarray(M[[idx[g] for g in gs]].todense())*sf)
        return X.mean(axis=0)[keep]
    S={k:sc(v) for k,v in SETS.items()}
    lab_arr=np.array(list(S.keys()))
    stack=np.vstack([S[k] for k in lab_arr])
    assign=lab_arr[stack.argmax(axis=0)]
    n=keep.sum()
    print('\n=== %-20s  cells passing QC: %d'%(lab,n))
    for k in SETS:
        print('   %-12s %6.1f%%'%(k,100*(assign==k).mean()))
    print('   -- Hh pathway (mean log-norm, all QC cells):')
    for g in HH:
        if g in idx:
            v=np.log1p(np.asarray(M[idx[g]].todense()).ravel()*sf)[keep]
            print('      %-6s %.4f  (%.1f%% cells+)'%(g,v.mean(),100*(v>0).mean()))
