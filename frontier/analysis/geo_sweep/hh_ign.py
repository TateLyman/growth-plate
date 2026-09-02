import sys;sys.path.insert(0,'.')
import q,numpy as np,re,random,statistics
IGN=set('IGF2 H19 DLK1 MEG3 RIAN MIRG MEST PEG3 ZIM1 PLAGL1 CDKN1C KCNQ1OT1 IGF2R NDN MAGEL2 GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT NAP1L5 PPP1R9A BLCAP INPP5F AIRN SNRPN'.split())
random.seed(13)
def sc(acc,A,B,label,nsim=1200):
    try: d=q.D(acc)
    except Exception: return
    X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
    v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1);bg=float(np.nanmean(v[ok]))
    sel=[k for k,g in enumerate(d['g']) if str(g) in IGN and ok[k] and np.isfinite(v[k])]
    if len(sel)<7: print('  %-46s (n=%d too few)'%(label,len(sel))); return
    pool=np.array([k for k in range(len(v)) if ok[k] and np.isfinite(v[k])])
    order={k:pool[np.argsort(np.abs(ex[pool]-ex[k]))[:120]] for k in sel}
    sims=[np.mean([v[random.choice(order[k])] for k in sel]) for _ in range(nsim)]
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    ign=float(np.nanmean(v[sel]))
    print('  %-46s IGN %+6.2f  z=%+6.2f  n=%d'%(label,ign-bg,(ign-mu)/sd if sd else 0,len(sel)))
if __name__=='__main__':
    print('DOES HEDGEHOG ACTIVATION MOVE THE IMPRINTED NETWORK?')
    d=q.D('GSE249831');print('  GSE249831 labels',[str(x) for x in d['labels']])
    sc('GSE249831',[0,1,2],[3,4,5],'Gli1+ progenitors vs Gli1- cells')
    sc('GSE254020',[4,5,6,7],[0,1,2,3],'SAG vs DMSO, sorted epSSC (contaminated)')
    d=q.D('GSE23432');L=[str(x) for x in d['labels']]
    R=[i for i,l in enumerate(L) if 'Resting' in l];P=[i for i,l in enumerate(L) if 'Proliferative zone' in l]
    E=[i for i,l in enumerate(L) if 'Epiphyseal' in l];H=[i for i,l in enumerate(L) if 'Hypertrophic' in l]
    sc('GSE23432',R,P,'rat RZ vs PZ (Hh-low vs Hh-high compartment)')
    sc('GSE23432',R,H,'rat RZ vs HZ')
    sc('GSE23432',E,R,'epiphyseal cartilage vs RZ')
