import sys;sys.path.insert(0,'.')
import q,numpy as np,re,random,statistics
d=q.D('GSE9160');L=[str(x) for x in d['labels']]
for i,l in enumerate(L): print(i,l[:120])
def find(zone,age): return [i for i,l in enumerate(L) if re.search(zone,l,re.I) and age in l]
Y='11-10/12';O='13-3/12'
print('\nAges present:',[a for a in [Y,O] if any(a in l for l in L)])
IGN=set('IGF2 H19 DLK1 MEG3 RTL1 MEST PEG3 ZIM1 PLAGL1 CDKN1C KCNQ1OT1 IGF2R MAGEL2 NDN SNRPN GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT MKRN3 BLCAP INPP5F NAP1L5 FAM50B DLGAP2 PPP1R9A OSBPL5 ASCL2 UBE3A DIRAS3 L3MBTL1 ZNF597 MEG8'.split())
X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
random.seed(2)
print('\n=== HUMAN growth plate: OLDER (13y3m) minus YOUNGER (11y10m), per zone ===')
res={}
for zn,rx in [('RESERVE',r'^Reserve'),('proliferative',r'^Proliferative'),('prehypertrophic',r'^Prehypertrophic'),('hypertrophic',r'^Hypertrophic'),('perichondrium',r'^Perichondrium')]:
    a=find(rx,O);b=find(rx,Y)
    if not a or not b: print(' %s: missing'%zn); continue
    v=X[:,a[0]]-X[:,b[0]]
    bg=float(np.nanmean(v[ok]))
    sel=[i for i,g in enumerate(d['g']) if str(g) in IGN and ok[i] and np.isfinite(v[i])]
    pool=[i for i in range(len(v)) if ok[i] and np.isfinite(v[i])];arr=ex[pool]
    sims=[]
    for _ in range(2000):
        s=0
        for i in sel:
            cand=[pool[k] for k in np.argsort(np.abs(arr-ex[i]))[:120]]
            s+=v[random.choice(cand)]
        sims.append(s/len(sel))
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    ign=float(np.nanmean(v[sel]))
    res[zn]=(ign-bg,(ign-mu)/sd,len(sel))
    print(' %-16s IGN %+6.2f (above bg)   z=%+5.2f   n=%d'%(zn,ign-bg,(ign-mu)/sd,len(sel)))
a=find(r'^Reserve',O);b=find(r'^Reserve',Y)
v=X[:,a[0]]-X[:,b[0]]
print('\n  individual imprinted genes, human RESERVE zone, 13y3m minus 11y10m:')
for g in sorted(IGN):
    i=[k for k,x in enumerate(d['g']) if str(x)==g and ok[k]]
    if i: print('    %-10s %+6.2f'%(g,v[i[0]]))
