# F-R110: growth hormone on human growth plate cells, scored on the F-R109 youth axis.
# GSE288028 (Chu et al.) 10x .h5 matrices: 4 vehicle + 4 GH libraries, 29,042 cells after QC.
import h5py,numpy as np,scipy.sparse as sp,collections
def load(f):
    with h5py.File(f,'r') as h:
        k=list(h.keys())[0]; g=h[k]
        names=np.array([x.decode() for x in (g['features']['name'][:] if 'features' in g else g['gene_names'][:])])
        X=sp.csc_matrix((g['data'][:],g['indices'][:],g['indptr'][:]),shape=g['shape'][:])
    return names,X
GRP={'veh':['GSM9328219_P30453_1002','GSM9328222_P31011_1002','GSM9328225_P25452_004','GSM9328226_P25452_005'],
     'gh' :['GSM9328220_P30453_1003','GSM9328223_P31011_1003','GSM9328227_P25452_007','GSM9328228_P25452_008']}
def pb(f):
    n,X=load(f+'.h5')
    keep=np.asarray(X.sum(axis=0)).ravel()>500      # real cells
    s=np.asarray(X[:,keep].sum(axis=1)).ravel(); s=s/s.sum()*1e6
    d=collections.defaultdict(float)
    for nm,v in zip(n,np.log2(s+1)):
        if v>d[nm]: d[nm]=v
    return d
V=[pb(f) for f in GRP['veh']]; G=[pb(f) for f in GRP['gh']]
genes=sorted(set.intersection(*[set(d) for d in V+G]))
delta=np.array([np.mean([d[g] for g in [x]]) for x in genes])  # placeholder
delta=np.array([np.mean([d[x] for d in G])-np.mean([d[x] for d in V]) for x in genes])
np.save('gh_delta.npy',delta); np.save('gh_genes.npy',np.array(genes))
print('genes',len(genes))
