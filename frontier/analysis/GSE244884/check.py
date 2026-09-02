import h5py,numpy as np
from scipy.sparse import csc_matrix
from scipy.stats import chi2_contingency, mannwhitneyu
SETS={'RZ_stem':['Pthlh','Sfrp5','Cytl1','Thbs1','Thbs2','Dcn','Grem1','Fgfr3','Sox9'],
 'prolif':['Mki67','Top2a','Ccnb1','Cdk1','Birc5'],
 'preHT_HT':['Ihh','Col10a1','Mef2c','Ibsp','Spp1','Panx3'],
 'osteoblast':['Col1a1','Sp7','Bglap','Runx2','Alpl','Postn','Ifitm5'],
 'stromal':['Cxcl12','Lepr','Adipoq','Kitl']}
ALT={'RZ_stem':['Pthlh','Sfrp5','Cytl1'],'prolif':['Mki67','Top2a'],
     'preHT_HT':['Col10a1','Ihh'],'osteoblast':['Col1a1','Sp7','Bglap'],'stromal':['Cxcl12','Lepr']}
def prep(f,minlog=1000):
    with h5py.File(f,'r') as h:
        names=np.array([x.decode() for x in h['matrix/features/name'][:]])
        M=csc_matrix((h['matrix/data'][:],h['matrix/indices'][:],h['matrix/indptr'][:]),
                     shape=tuple(h['matrix/shape'][:])).tocsr()
    tot=np.asarray(M.sum(axis=0)).ravel(); ng=np.asarray((M>0).sum(axis=0)).ravel()
    mito=[i for i,n in enumerate(names) if n.startswith('mt-')]
    mf=np.asarray(M[mito].sum(axis=0)).ravel()/np.maximum(tot,1)
    keep=(ng>=minlog)&(mf<0.15)
    idx={n:i for i,n in enumerate(names)}; sf=1e4/np.maximum(tot,1)
    return M,idx,sf,keep
def assign(M,idx,sf,keep,sets):
    ks=list(sets); st=[]
    for k in ks:
        gs=[g for g in sets[k] if g in idx]
        st.append(np.log1p(np.asarray(M[[idx[g] for g in gs]].todense())*sf).mean(axis=0)[keep])
    return np.array(ks)[np.vstack(st).argmax(axis=0)]
def row(M,idx,sf,keep,g): return np.log1p(np.asarray(M[idx[g]].todense()).ravel()*sf)[keep]

for tag,setname,sets,q in [('primary markers, nGene>=1000','A',SETS,1000),
                           ('reduced markers, nGene>=1000','B',ALT,1000),
                           ('primary markers, nGene>=2000','C',SETS,2000)]:
    out={}
    for lab,f in [('cHET','GSM7831319.h5'),('cKO','GSM7831318.h5')]:
        M,idx,sf,keep=prep(f,q); a=assign(M,idx,sf,keep,sets)
        out[lab]=(a,keep.sum(),M,idx,sf,keep)
    ks=list(sets)
    tab=np.array([[ (out[l][0]==k).sum() for k in ks] for l in ('cHET','cKO')])
    chi2,p,_,_=chi2_contingency(tab)
    print('\n--- %s'%tag)
    print('   n: cHET=%d cKO=%d   chi2 p=%.3g'%(out['cHET'][1],out['cKO'][1],p))
    for i,k in enumerate(ks):
        print('   %-11s cHET %5.1f%%   cKO %5.1f%%'%(k,100*tab[0,i]/tab[0].sum(),100*tab[1,i]/tab[1].sum()))

# Gli1 within stem cells only - is the pathway actually more active in cKO?
print('\n=== Gli1 / Hh target within RZ_stem-assigned cells only ===')
vals={}
for lab,f in [('cHET','GSM7831319.h5'),('cKO','GSM7831318.h5')]:
    M,idx,sf,keep=prep(f); a=assign(M,idx,sf,keep,SETS)
    m=(a=='RZ_stem')
    for g in ['Gli1','Ptch1','Hhip','Ccnd1']:
        v=row(M,idx,sf,keep,g)[m]; vals.setdefault(g,{})[lab]=v
        print('  %-6s %-5s mean=%.4f  pct+=%.1f%%  n=%d'%(g,lab,v.mean(),100*(v>0).mean(),len(v)))
for g in vals:
    u,p=mannwhitneyu(vals[g]['cHET'],vals[g]['cKO'])
    print('  %-6s cHET vs cKO  p=%.3g'%(g,p))
