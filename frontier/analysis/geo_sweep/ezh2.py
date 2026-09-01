import sys;sys.path.insert(0,'.')
import q,youth,numpy as np,random,statistics
IGN='IGF2 H19 DLK1 MEG3 RIAN MIRG MEST PEG3 ZIM1 PLAGL1 CDKN1C KCNQ1OT1 AIRN IGF2R MAGEL2 NDN GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT NAP1L5 PPP1R9A BLCAP INPP5F'.split()
d=q.D('GSE84198');X=d['X'];gl=[str(g) for g in d['g']]
ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
random.seed(31)
def sc(A,B,gs,nsim=2500):
    v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1);bg=float(np.nanmean(v[ok]))
    sel=[k for k,g in enumerate(gl) if g in gs and ok[k] and np.isfinite(v[k])]
    pool=np.array([k for k in range(len(v)) if ok[k] and np.isfinite(v[k])])
    order={k:pool[np.argsort(np.abs(ex[pool]-ex[k]))[:120]] for k in sel}
    sims=[np.mean([v[random.choice(order[k])] for k in sel]) for _ in range(nsim)]
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    return float(np.nanmean(v[sel]))-bg,(float(np.nanmean(v[sel]))-mu)/sd,len(sel),v
PZ_W,PZ_K=list(range(0,6)),list(range(6,12));HZ_W,HZ_K=list(range(12,18)),list(range(18,24))
print('Ezh2 cartilage-cKO vs WT littermates, LCM growth plate, P3, n=6/group')
for nm,K,W in [('proliferative zone',PZ_K,PZ_W),('hypertrophic zone',HZ_K,HZ_W)]:
    r=sc(K,W,set(IGN))
    print('  %-20s IMPRINTED NETWORK %+6.2f  z=%+6.2f  n=%d'%(nm,r[0],r[1],r[2]))
    for s,gs in [('cell cycle','MKI67 CCNB1 TOP2A CDK1 RRM2 MCM2 PCNA CCNA2 BUB1 PLK1 AURKA TYMS TK1'),
                 ('chondrogenic','SOX9 ACAN COL2A1 COL9A1 COL11A1 COL10A1 IHH PTHLH'),
                 ('EZH2/PRC2','EZH1 EZH2 SUZ12 EED JARID2 RNF2 CBX7')]:
        rr=sc(K,W,set(gs.split()))
        print('      %-16s %+6.2f  z=%+5.2f'%(s,rr[0],rr[1]))
    yy=youth.score('GSE84198',K,W,'')
    print('      youth axis (F-R109)  r=%+.3f p=%.1e'%(yy['r'],yy['p']))
_,_,_,v=sc(PZ_K,PZ_W,set(IGN))
print('\nimprinted genes, Ezh2 KO minus WT, proliferative zone:')
for g in sorted(set(IGN)):
    i=[k for k,x in enumerate(gl) if x==g and ok[k]]
    if i: print('  %-10s %+6.2f'%(g,v[i[0]]))
