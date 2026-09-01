import sys;sys.path.insert(0,'.')
import q,numpy as np,re,random,statistics
from scipy import stats
d=q.D('GSE16981');L=[str(x) for x in d['labels']];X=d['X'];gl=[str(g) for g in d['g']]
ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
AGES=[('3wk',r'_3wk'),('6wk',r'_6wk'),('9wk',r'_9wk'),('12wk',r'_12wk')]
G={a:[i for i,l in enumerate(L) if re.search(p,l)] for a,p in AGES}
print('CASTRATED rat proliferative zone (oestrogen absent from 3wk) — the human aromatase-deficiency model')
print('sample counts:',{a:len(v) for a,v in G.items()})
SETS={'IMPRINTED NETWORK':'IGF2 H19 DLK1 MEG3 MEST PEG3 ZIM1 PLAGL1 CDKN1C IGF2R NDN GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT NAP1L5 PPP1R9A BLCAP INPP5F',
 'cell cycle':'MKI67 CCNB1 TOP2A CDK1 RRM2 MCM2 PCNA CCNA2 BUB1 PLK1 AURKA TYMS TK1 BIRC5',
 'chondrogenic':'SOX9 ACAN COL2A1 COL9A1 COL11A1 COL10A1 IHH PTHLH',
 'HEDGEHOG ligand-side':'IHH SHH BOC CDON GAS1 DISP1 SCUBE3 GPC3',
 'HHIP+SMO':'HHIP SMO PTCH1'}
random.seed(11)
def sc(A,B,gs,nsim=1200):
    v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1);bg=float(np.nanmean(v[ok]))
    sel=[k for k,g in enumerate(gl) if g in gs and ok[k] and np.isfinite(v[k])]
    if len(sel)<5: return None
    pool=np.array([k for k in range(len(v)) if ok[k] and np.isfinite(v[k])])
    order={k:pool[np.argsort(np.abs(ex[pool]-ex[k]))[:120]] for k in sel}
    sims=[np.mean([v[random.choice(order[k])] for k in sel]) for _ in range(nsim)]
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    return float(np.nanmean(v[sel]))-bg,((float(np.nanmean(v[sel]))-mu)/sd if sd else 0),len(sel)
print('\n%-24s %18s %18s %18s'%('gene set','6wk vs 3wk','9wk vs 3wk','12wk vs 3wk'))
for nm,s in SETS.items():
    gs=set(s.split());row='%-24s'%nm
    for a in ['6wk','9wk','12wk']:
        r=sc(G[a],G['3wk'],gs)
        row+=('   %+6.2f (z=%+5.1f)'%(r[0],r[1])) if r else '                  .'
    print(row)
# per-gene imprinted trajectory
print('\nimprinted genes, castrated PZ, 12wk minus 3wk:')
v=np.nanmean(X[:,G['12wk']],axis=1)-np.nanmean(X[:,G['3wk']],axis=1)
for g in sorted(set(SETS['IMPRINTED NETWORK'].split())):
    i=[k for k,x in enumerate(gl) if x==g and ok[k]]
    if i: print('  %-10s %+6.2f'%(g,v[i[0]]))
