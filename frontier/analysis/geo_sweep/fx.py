import sys;sys.path.insert(0,'.')
import q,numpy as np,re,random,statistics
IGN=set('IGF2 H19 DLK1 MEG3 RTL1 MEST PEG3 ZIM1 PLAGL1 CDKN1C KCNQ1OT1 IGF2R MAGEL2 NDN SNRPN GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT MKRN3 BLCAP INPP5F NAP1L5 DLGAP2 PPP1R9A OSBPL5 ASCL2 UBE3A DIRAS3 MEG8 RIAN MIRG'.split())
random.seed(1)
def ignscore(d,A,B,label,nsim=600):
    X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
    v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1)
    bg=float(np.nanmean(v[ok]))
    sel=[i for i,g in enumerate(d['g']) if str(g) in IGN and ok[i] and np.isfinite(v[i])]
    if len(sel)<8: print('  %-44s (too few)'%label); return
    pool=np.array([i for i in range(len(v)) if ok[i] and np.isfinite(v[i])]);arr=ex[pool]
    order={i:pool[np.argsort(np.abs(arr-ex[i]))[:120]] for i in sel}
    sims=[np.mean([v[random.choice(order[i])] for i in sel]) for _ in range(nsim)]
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    ign=float(np.nanmean(v[sel]))
    print('  %-44s IGN %+6.2f  z=%+6.2f  n=%d'%(label,ign-bg,(ign-mu)/sd if sd else 0,len(sel)))
if __name__=='__main__':
    d=q.D('GSE213574');L=[str(x) for x in d['labels']]
    def G(rx): return [i for i,l in enumerate(L) if re.search(rx,l,re.I)]
    print('=== GSE213574: fracture callus vs uninjured, sorted skeletal stem/progenitor cells ===')
    ignscore(d,G(r'callus SSC|SSC injured'),G(r'Uninjured SSC|SSC uninjured'),'SSC: callus vs uninjured')
    ignscore(d,G(r'callus BCSP|BCSP Injured'),G(r'BCSP Uninjured'),'BCSP: callus vs uninjured')
    ignscore(d,G(r'^OB |^OS '),G(r'^OUB|^OUS'),'OVX+fracture vs OVX uninjured')
    ignscore(d,G(r'^EB |^ES '),G(r'^OUB|^OUS'),'OVX+fracture+E2 vs OVX uninjured')
    ignscore(d,G(r'^OB |^OS '),G(r'^EB |^ES '),'OVX+fx vs OVX+fx+E2  (E2 blocks it?)')
