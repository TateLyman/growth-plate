import sys;sys.path.insert(0,'.')
import q,youth,numpy as np
from scipy import stats
d=q.D('GSE202057');KO=[2,3];WT=[0,1]
IGN=['IGF2','H19','DLK1','MEG3','RIAN','MIRG','MEST','PEG3','ZIM1','PLAGL1','CDKN1C','KCNQ1OT1','AIRN','IGF2R','MAGEL2','NDN','GPC3','GRB10','PEG10','NNAT','SGCE','GNAS','SLC38A4','PHLDA2','PLAG1','IMPACT','CD81']
print('labels',list(d['labels']))
print('\nTrim28 KO vs WT, rib cartilage (log2):')
vs=[]
for g in ['TRIM28','ZFP57','SETDB1','GREM1','DNMT1','UHRF1']+IGN:
    x=q.v(d,g)
    if x is None: continue
    v=float(np.nanmean(x[KO])-np.nanmean(x[WT]))
    if not np.isfinite(v): continue
    print('%-11s %8.2f%s'%(g,v,'   <- IGN' if g in IGN else ''))
    if g in IGN: vs.append(v)
X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,55)
bgv=np.nanmean(X[:,KO],axis=1)-np.nanmean(X[:,WT],axis=1)
bg=float(np.nanmean(bgv[ok]))
print('\nIGN mean %+.2f | background %+.2f | IGN-minus-bg %+.2f (n=%d)'%(np.mean(vs),bg,np.mean(vs)-bg,len(vs)))
r=youth.score('GSE202057',KO,WT,'Trim28 KO')
print('Trim28 KO on the F-R109 (PZ/HZ) youth axis: r=%+.3f p=%.1e n=%d'%(r['r'],r['p'],r['n']))
rz=np.load('rz_age.npy');rzg=np.load('rz_genes.npy',allow_pickle=True)
RZ={str(a).upper():float(b) for a,b in zip(rzg,rz) if np.isfinite(b)}
vv={str(g):float(bgv[i]) for i,g in enumerate(d['g']) if ok[i] and np.isfinite(bgv[i])}
sh=sorted(set(vv)&set(RZ))
rr,pp=stats.pearsonr([vv[g] for g in sh],[RZ[g] for g in sh])
print('Trim28 KO vs the RESTING-ZONE youth vector: r=%+.3f n=%d p=%.0e'%(rr,len(sh),pp))
