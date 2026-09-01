import sys;sys.path.insert(0,'.')
import q,numpy as np,re,random,statistics
HIF=set('HIF1A EPAS1 ARNT VHL EGLN1 EGLN2 EGLN3 HIF1AN SLC2A1 SLC2A3 PGK1 LDHA ALDOA ENO1 PFKL PFKP HK2 BNIP3 BNIP3L ADM CA9 PDK1 ANKRD37 NDRG1 SLC16A3 DDIT4 VEGFA'.split())
random.seed(51)
def sc(acc,A,B,label,gs=HIF,nsim=1500):
    try: d=q.D(acc)
    except Exception: print('  %-48s (missing)'%label); return
    X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
    v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1);bg=float(np.nanmean(v[ok]))
    sel=[k for k,g in enumerate(d['g']) if str(g) in gs and ok[k] and np.isfinite(v[k])]
    if len(sel)<6: print('  %-48s (n=%d)'%(label,len(sel))); return
    pool=np.array([k for k in range(len(v)) if ok[k] and np.isfinite(v[k])])
    order={k:pool[np.argsort(np.abs(ex[pool]-ex[k]))[:120]] for k in sel}
    sims=[np.mean([v[random.choice(order[k])] for k in sel]) for _ in range(nsim)]
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    ign=float(np.nanmean(v[sel]))
    print('  %-48s HIF %+6.2f  z=%+6.2f  n=%d'%(label,ign-bg,(ign-mu)/sd if sd else 0,len(sel)))
def G(acc,rx):
    d=q.D(acc);return [i for i,l in enumerate(d['labels']) if re.search(rx,str(l),re.I)]
M='GSE114919_Mouse';R='GSE114919_Rat'
print('THE HYPOXIA / HIF PROGRAM ACROSS EVERY LENGTH AND AGE SYSTEM')
print('\n LONG minus SHORT (same age):')
sc(M,G(M,r'^1wT_PZ'),G(M,r'^1wP_PZ'),'MOUSE tibia vs phalanx, PZ')
sc(M,G(M,r'^1wT_HZ'),G(M,r'^1wPh_HZ'),'MOUSE tibia vs phalanx, HZ')
sc(R,G(R,r'^T1wk PZ'),G(R,r'^Ph1wk PZ'),'RAT tibia vs phalanx, PZ')
sc(R,G(R,r'^T1wk HZ'),G(R,r'^Ph1wk HZ'),'RAT tibia vs phalanx, HZ')
sc('GSE189528',[0,2,4],[1,3,5],'Longshanks (+12% tibia) vs control')
sc('GSE270640',[0,1,2,3],[4,5,6,7],'flox vs Dnmt1-cKO (long minus short)')
sc('GSE145821',[18,19,20,21,22,23],[6,7,8,9,10,11],'WT vs Fgfr3-GOF (long minus short)')
print('\n YOUNG minus OLD:')
sc(M,G(M,r'^1wT_PZ'),G(M,r'^4wT_PZ'),'MOUSE tibia PZ 1wk vs 4wk')
sc(R,G(R,r'^T1wk PZ'),G(R,r'^T4wk PZ'),'RAT tibia PZ 1wk vs 4wk')
sc('GSE18338',[4,5],[2,3],'HUMAN growth plate pre- vs late-puberty')
d=q.D('GSE113982');L=[str(x) for x in d['labels']]
g=lambda rx:[i for i,l in enumerate(L) if re.search(rx,l)]
sc('GSE113982',g(r'^p[23]_R'),g(r'^p28_R'),'MOUSE RESTING ZONE P2/P3 vs P28  <-- the pool')
sc('GSE113982',g(r'^p[23]_P'),g(r'^p28_P'),'MOUSE proliferative zone P2/P3 vs P28')
sc('GSE113982',g(r'^p[23]_H'),g(r'^p28_H'),'MOUSE hypertrophic zone P2/P3 vs P28')
print('\n castrated (oestrogen-independent) rat PZ:')
sc('GSE16981',[15,16,17,18,19],[30,31,32,33,34],'rat PZ 3wk vs 12wk, castrated')
