import h5py, numpy as np, glob
from scipy.sparse import csc_matrix
import statistics

def load(f):
    with h5py.File(f) as h:
        g=h['matrix']; shape=tuple(g['shape'][:])
        M=csc_matrix((g['data'][:],g['indices'][:],g['indptr'][:]),shape=shape)
        names=np.array([x.decode() for x in g['features']['name'][:]])
    return M.tocsr(), names

files=sorted(glob.glob('*.h5'))
lab={'GSM6068484_con116_4_count.h5':('CON','116'),
     'GSM6068485_filtered_control-116-3.h5':('CON','116'),
     'GSM6068486_con-119-3_count_filtered_feacutre_bc_matrix.h5':('CON','119'),
     'GSM6068487_mut-119-1_count_filtered_feacutre_bc_matrix.h5':('MUT','119'),
     'GSM6068488_mut-119-2_count_filtered_feacutre_bc_matrix.h5':('MUT','119'),
     'GSM6068489_mut_124_3_filtered_feature_bc_matrix.h5':('MUT','124')}

names=None; store={}
print('%-36s %4s %4s %7s %7s %9s'%('sample','grp','bat','ncell','pass','medUMI'))
for f in files:
    M,n=load(f); names=n if names is None else names
    umi=np.asarray(M.sum(axis=0)).ravel()
    ngene=np.asarray((M>0).sum(axis=0)).ravel()
    keep=(ngene>=200)&(umi>=500)
    store[f]=(M,keep,umi)
    print('%-36s %4s %4s %7d %7d %9.0f'%(f[:36],lab[f][0],lab[f][1],M.shape[1],keep.sum(),np.median(umi[keep]) if keep.sum() else 0))

idx={}
for i,g in enumerate(names): idx.setdefault(g,i)
def gi(gl): return [idx[g] for g in gl if g in idx]

REST=['Grem1','Ucma','Barx1','Bgn']
ENCH=['Cdsn','Tenm4','Sfrp5','Slc7a3']
HIF=['Vegfa','Slc2a1','Pgk1','Ldha','Aldoa','Pdk1','Bnip3','Ankrd37','Adm','P4ha1','Egln3']
SETS={'REST':REST,'ENCH':ENCH,'HIF':HIF,'ART':['Wif1','Creb5'],
      'MATRIX':['Matn1','Matn3','Col9a1','Cnmd','Acan','Col2a1'],'PROLIF':['Mki67','Top2a','Cenpf']}
GENES=['Tet1','Tet2','Tet3','Idh1','Grem1','Ucma','Sfrp5','Cdsn','Vegfa','Bnip3','Pgk1','Col2a1','Acan','Col10a1','Ihh','Pthlh','Fgfr3','Sox9']

def norm(M,keep,umi):
    sub=M[:,keep]; t=umi[keep]
    return sub, t

rows={}
for f in files:
    M,keep,umi=store[f]
    if keep.sum()<50: rows[f]=None; print('SKIP (too few cells):',f); continue
    sub,t=norm(M,keep,umi)
    d={}
    for k,gl in SETS.items():
        v=np.asarray(sub[gi(gl)].todense())/t*1e4
        d[k]=float(np.log1p(v).mean())
    # resting-high cell FRACTION (cluster-2 proxy): Grem1+ AND Ucma+ cells
    g1=np.asarray(sub[idx['Grem1']].todense()).ravel(); u1=np.asarray(sub[idx['Ucma']].todense()).ravel()
    d['%Grem1+Ucma+']=100.0*float(((g1>0)&(u1>0)).mean())
    d['%Grem1+']=100.0*float((g1>0).mean()); d['%Ucma+']=100.0*float((u1>0).mean())
    s5=np.asarray(sub[idx['Sfrp5']].todense()).ravel(); cd=np.asarray(sub[idx['Cdsn']].todense()).ravel()
    d['%Sfrp5+Cdsn+']=100.0*float(((s5>0)&(cd>0)).mean())
    for g in GENES:
        v=np.asarray(sub[idx[g]].todense()).ravel()/t*1e4
        d['e:'+g]=float(np.log1p(v).mean())
    d['n']=int(keep.sum()); rows[f]=d

cols=['n','REST','ENCH','ART','MATRIX','PROLIF','HIF','%Grem1+Ucma+','%Sfrp5+Cdsn+']
print('\n%-30s %4s '%('sample','bat')+' '.join('%13s'%c for c in cols))
for f in files:
    if rows[f] is None: continue
    print('%-30s %4s '%(lab[f][0]+' '+f[10:24],lab[f][1])+' '.join('%13.4f'%rows[f][c] for c in cols))

def grp(g,bat=None):
    return [rows[f] for f in files if rows[f] and lab[f][0]==g and (bat is None or lab[f][1]==bat)]

print('\n===== ALL SAMPLES (mut_124 excluded: %d cells) ====='%(store[files[5]][1].sum()))
print('%-16s %10s %10s %9s'%('metric','CON','MUT','MUT/CON'))
for c in cols[1:]:
    C=statistics.mean([r[c] for r in grp('CON')]); M_=statistics.mean([r[c] for r in grp('MUT')])
    print('%-16s %10.4f %10.4f %9.3f'%(c,C,M_,M_/C if C else float('nan')))

print('\n===== BATCH-MATCHED: litter 119 only (1 con vs 2 mut) =====')
print('%-16s %10s %10s %9s'%('metric','CON119','MUT119','ratio'))
for c in cols[1:]:
    C=statistics.mean([r[c] for r in grp('CON','119')]); M_=statistics.mean([r[c] for r in grp('MUT','119')])
    print('%-16s %10.4f %10.4f %9.3f'%(c,C,M_,M_/C if C else float('nan')))

print('\n===== PER-GENE (batch 119) =====')
print('%-10s %10s %10s %9s'%('gene','CON119','MUT119','ratio'))
for g in GENES:
    C=statistics.mean([r['e:'+g] for r in grp('CON','119')]); M_=statistics.mean([r['e:'+g] for r in grp('MUT','119')])
    print('%-10s %10.4f %10.4f %9.3f'%(g,C,M_,M_/C if C else float('nan')))
