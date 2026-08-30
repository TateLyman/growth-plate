import sys;sys.path.insert(0,'.')
import q,numpy as np,re,random,statistics
d=q.D('GSE3298');L=[str(x) for x in d['labels']];X=d['X']
gl=[str(g) for g in d['g']]
ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
pairs=[('1 day',3,2),('3 day',5,4),('1 week',7,6),('2 week',9,8),('3 week',11,10),('4 week',13,12),('6 week',15,14)]
SETS={
 'IMPRINTED NETWORK':'IGF2 H19 DLK1 MEG3 MEST PEG3 ZIM1 PLAGL1 CDKN1C IGF2R NDN GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT NAP1L5 PPP1R9A BLCAP INPP5F',
 'cell cycle':'MKI67 CCNB1 TOP2A CDK1 RRM2 MCM2 PCNA CCNA2 BUB1 PLK1 AURKA TYMS TK1 BIRC5 CENPF',
 'chondrogenic':'SOX9 ACAN COL2A1 COL9A1 COL11A1 COL10A1 IHH PTHLH',
 'HEDGEHOG':'SMO PTCH1 GLI1 GLI2 GLI3 IHH HHIP BOC CDON GAS1 SUFU DISP1 SCUBE3',
 'RZ/stem':'SFRP5 FRZB PTHLH GREM1 THBS1 THBS2 DCN CYTL1 PDGFRA SOX9',
 'CNP/NPR2':'NPR2 PRKG1 NPPC',
 'GH/IGF':'GHR IGF1 IGF1R IGFBP3 IGFBP5 STAT5B SOCS2',
 'hypoxia':'HIF1A VEGFA SLC2A1 PGK1 LDHA BNIP3 ADM P4HA1 PDK1',
 'methylation':'DNMT1 DNMT3A DNMT3B UHRF1 TET1 TET2 TET3',
 'invasion front':'CXCL12 ADAMTS5 TNFRSF11A KAZALD1 MMP13 SPP1 NPR1',
}
random.seed(7)
def sc(i,c,gs,nsim=500):
    v=X[:,i]-X[:,c];bg=float(np.nanmean(v[ok]))
    sel=[k for k,g in enumerate(gl) if g in gs and ok[k] and np.isfinite(v[k])]
    if len(sel)<5: return None
    pool=np.array([k for k in range(len(v)) if ok[k] and np.isfinite(v[k])])
    order={k:pool[np.argsort(np.abs(ex[pool]-ex[k]))[:120]] for k in sel}
    sims=[np.mean([v[random.choice(order[k])] for k in sel]) for _ in range(nsim)]
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    return float(np.nanmean(v[sel]))-bg,((float(np.nanmean(v[sel]))-mu)/sd if sd else 0),len(sel)
print('GSE3298 — rat PROXIMAL FEMORAL GROWTH PLATE after a distant MID-SHAFT FRACTURE')
print('  (fracture minus its own time-matched control; the fracture is far from the plate)\n')
hdr='%-22s'%'gene set'+''.join('%9s'%p[0] for p in pairs)
print(hdr); print('-'*len(hdr))
for nm,s in SETS.items():
    gs=set(s.split());row='%-22s'%nm
    for t,f,c in pairs:
        r=sc(f,c,gs)
        row+=('%9.2f'%r[0]) if r else '        .'
    print(row)
print('\nz-scores vs expression-matched null, IMPRINTED NETWORK only:')
for t,f,c in pairs:
    r=sc(f,c,set(SETS['IMPRINTED NETWORK'].split()),nsim=1500)
    if r: print('  %-9s  IGN %+6.2f   z=%+6.2f  (n=%d)'%(t,r[0],r[1],r[2]))
