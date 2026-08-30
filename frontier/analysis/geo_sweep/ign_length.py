import sys;sys.path.insert(0,'.')
import q,numpy as np,re,random,statistics
IGN=set('IGF2 H19 DLK1 MEG3 RIAN MIRG RTL1 MEST PEG3 ZIM1 PLAGL1 CDKN1C KCNQ1OT1 AIRN IGF2R MAGEL2 NDN SNRPN GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT MKRN3 BLCAP INPP5F NAP1L5 PPP1R9A DLGAP2 OSBPL5 ASCL2 FAM50B MEG8'.split())
random.seed(41)
def sc(acc,A,B,label,nsim=2000):
    try: d=q.D(acc)
    except Exception: print('  %-46s (missing)'%label); return
    X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
    v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1);bg=float(np.nanmean(v[ok]))
    sel=[k for k,g in enumerate(d['g']) if str(g) in IGN and ok[k] and np.isfinite(v[k])]
    if len(sel)<8: print('  %-46s (n=%d too few)'%(label,len(sel))); return
    pool=np.array([k for k in range(len(v)) if ok[k] and np.isfinite(v[k])])
    order={k:pool[np.argsort(np.abs(ex[pool]-ex[k]))[:120]] for k in sel}
    sims=[np.mean([v[random.choice(order[k])] for k in sel]) for _ in range(nsim)]
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    ign=float(np.nanmean(v[sel]))
    print('  %-46s IGN %+6.2f  z=%+6.2f  n=%d'%(label,ign-bg,(ign-mu)/sd if sd else 0,len(sel)))
def G(acc,rx):
    d=q.D(acc);return [i for i,l in enumerate(d['labels']) if re.search(rx,str(l),re.I)]
M='GSE114919_Mouse';R='GSE114919_Rat'
print('IS THE IMPRINTED NETWORK HIGHER IN A LONG BONE THAN A SHORT ONE, AT THE SAME AGE?')
print('  (within-animal, same dissection, same zone - the cleanest length contrast that exists)')
sc(M,G(M,r'^1wT_PZ'),G(M,r'^1wP_PZ'),'MOUSE tibia vs phalanx, PROLIFERATIVE zone, 1wk')
sc(M,G(M,r'^1wT_HZ'),G(M,r'^1wPh_HZ'),'MOUSE tibia vs phalanx, HYPERTROPHIC zone, 1wk')
sc(R,G(R,r'^T1wk PZ'),G(R,r'^Ph1wk PZ'),'RAT   tibia vs phalanx, PROLIFERATIVE zone, 1wk')
sc(R,G(R,r'^T1wk HZ'),G(R,r'^Ph1wk HZ'),'RAT   tibia vs phalanx, HYPERTROPHIC zone, 1wk')
print('\n  and the age control in the same datasets (young vs old, same bone):')
sc(M,G(M,r'^1wT_PZ'),G(M,r'^4wT_PZ'),'MOUSE tibia PZ 1wk vs 4wk')
sc(R,G(R,r'^T1wk PZ'),G(R,r'^T4wk PZ'),'RAT   tibia PZ 1wk vs 4wk')
print('\nTHE OTHER LENGTH SYSTEMS:')
sc('GSE189528',[0,2,4],[1,3,5],'Longshanks (+12% tibia) vs control')
sc('GSE53277',[0,1,2,3,4,5],[6,7,8,9,10],'Great Dane vs Miniature Poodle growth plate')
sc('GSE270640',[0,1,2,3],[4,5,6,7],'flox vs Dnmt1-cKO (long minus short)')
sc('GSE145821',[18,19,20,21,22,23],[6,7,8,9,10,11],'WT vs Fgfr3-GOF 3-4wk (long minus short)')
