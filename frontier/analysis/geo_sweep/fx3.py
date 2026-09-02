import sys;sys.path.insert(0,'.')
import q,numpy as np,re
d=q.D('GSE1371');L=[str(x) for x in d['labels']]
IGN='IGF2 H19 DLK1 MEG3 MEST PEG3 PLAGL1 CDKN1C IGF2R NDN GPC3 GRB10 PEG10 NNAT SGCE SLC38A4 PHLDA2 IMPACT NAP1L5 PPP1R9A GNAS BLCAP'.split()
CYC='MKI67 CCNB1 TOP2A CDK1 RRM2 MCM2 PCNA CCNA2 BUB1 PLK1 AURKA TYMS TK1 BIRC5'.split()
CHON='SOX9 ACAN COL2A1 COL9A1 COL11A1 COL10A1 IHH PTHLH'.split()
X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
gl=[str(g) for g in d['g']]
def sc(i,c,gs):
    v=X[:,i]-X[:,c];bg=float(np.nanmean(v[ok]))
    vals=[v[k] for k,g in enumerate(gl) if g in gs and ok[k] and np.isfinite(v[k])]
    return (np.mean(vals)-bg) if vals else np.nan
grid={}
for i,l in enumerate(L):
    m=re.search(r'(young|adult|old)',l,re.I);t=re.search(r'(no fracture|3 days|1 week|2 weeks|4 weeks|6 weeks)',l,re.I)
    if m and t: grid[(m.group(1).lower(),t.group(1).lower())]=i
print('genes',len(gl),'grid cells',len(grid))
TS=['3 days','1 week','2 weeks','4 weeks','6 weeks']
for nm,gs in [('IMPRINTED NETWORK',IGN),('cell cycle',CYC),('chondrogenic',CHON)]:
    print('\n=== %s : fracture minus that age`s unfractured control ==='%nm)
    print('%-8s'%'age'+''.join('%10s'%t for t in TS))
    for age in ['young','adult','old']:
        c=grid.get((age,'no fracture'))
        if c is None: continue
        print('%-8s'%age+''.join(('%10.2f'%sc(grid[(age,t)],c,gs)) if (age,t) in grid else '         .' for t in TS))
