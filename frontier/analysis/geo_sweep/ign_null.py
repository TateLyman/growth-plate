import sys;sys.path.insert(0,'.')
import q,numpy as np,re,random,statistics
d=q.D('GSE113982');L=d['labels'];X=d['X']
def G(rx): return [i for i,l in enumerate(L) if re.search(rx,l)]
Z={'RZ':(G(r'^p[23]_R'),G(r'^p28_R')),'PZ':(G(r'^p[23]_P'),G(r'^p28_P')),'HZ':(G(r'^p[23]_H'),G(r'^p28_H'))}
IGN=set('IGF2 H19 DLK1 MEG3 RIAN MIRG MEST PEG3 ZIM1 PLAGL1 CDKN1C KCNQ1OT1 AIRN IGF2R MAGEL2 NDN GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 PLAG1 IMPACT CD81'.split())
CYC=set('MKI67 CCNB1 TOP2A CDK1 RRM2 MCM2 MCM3 MCM4 MCM5 MCM6 MCM7 PCNA CCNA2 BUB1 PLK1 AURKA AURKB TYMS TK1 FOXM1 KIF11 NUSAP1 UBE2C BIRC5 CENPF ASPM TTK RAD51 CHEK1 ESCO2 GINS2 POLA1 PRIM1 DHFR CDT1 CLSPN LIG1 MYBL2 CDC25B'.split())
ex=np.nanmax(X,axis=1); ok=ex>np.nanpercentile(ex,55)
gl=[str(x) for x in d['g']]
idx={g:i for i,g in enumerate(gl)}
lvl=np.nanmean(X,axis=1)
random.seed(3)
print('%-4s %10s %10s %10s %10s %10s'%('zone','IGN','CYCLE','background','null mean','null sd  -> IGN z'))
for z,(y,o) in Z.items():
    v=np.nanmean(X[:,o],axis=1)-np.nanmean(X[:,y],axis=1)
    bg=float(np.nanmean(v[ok]))
    def m(S):
        vals=[v[idx[g]] for g in S if g in idx and ok[idx[g]] and np.isfinite(v[idx[g]])]
        return (float(np.mean(vals)),len(vals)) if vals else (np.nan,0)
    ign,nign=m(IGN); cyc,_=m(CYC)
    # expression-level-matched null
    pool=[i for i in range(len(gl)) if ok[i] and np.isfinite(v[i])]
    plvl=np.array([lvl[i] for i in pool])
    targ=[lvl[idx[g]] for g in IGN if g in idx and ok[idx[g]] and np.isfinite(v[idx[g]])]
    sims=[]
    for _ in range(4000):
        s=0
        for t in targ:
            cand=[pool[k] for k in np.argsort(np.abs(plvl-t))[:150]]
            s+=v[random.choice(cand)]
        sims.append(s/len(targ))
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    print('%-4s %10.2f %10.2f %10.2f %10.2f %10.2f  z=%+.2f  p<%.4f'%(z,ign,cyc,bg,mu,sd,(ign-mu)/sd,
          (sum(1 for s in sims if s<=ign)+1)/(len(sims)+1)))
