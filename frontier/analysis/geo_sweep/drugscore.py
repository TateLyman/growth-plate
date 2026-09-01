import glob,os,csv,numpy as np,random,statistics
IGN=set('IGF2 H19 DLK1 MEG3 RIAN MIRG RTL1 MEST PEG3 ZIM1 ZIM2 PLAGL1 CDKN1C KCNQ1OT1 AIRN IGF2R MAGEL2 NDN SNRPN SNORD116 IPW GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT MKRN3 BLCAP INPP5F NAP1L5 FAM50B DLGAP2 PPP1R9A OSBPL5 ASCL2 UBE3A PEG13 TRAPPC9 ZNF597 MCTS2 H13 KCNK9 L3MBTL1 DIRAS3 TSSC4 CD81 MEG8 SNURF'.split())
# growth-promoting (paternally expressed) vs growth-suppressing (maternally expressed)
PAT=set('IGF2 DLK1 MEST PEG3 ZIM1 PLAGL1 PEG10 SGCE SNRPN SNURF NDN MAGEL2 MKRN3 NNAT IMPACT SLC38A4 RTL1 PEG13 MCTS2 BLCAP INPP5F NAP1L5 KCNK9 DIRAS3'.split())
MAT=set('H19 MEG3 RIAN MIRG CDKN1C IGF2R GRB10 PHLDA2 UBE3A ASCL2 OSBPL5 MEG8 GNAS ZNF597'.split())
def load(f):
    D={}
    with open(f) as fh:
        r=csv.reader(fh,delimiter='\t');hdr=next(r)
        gi=hdr.index('Associated.Gene.Name');li=hdr.index('logFC');pi=hdr.index('PValue');ci=hdr.index('logCPM')
        for row in r:
            if len(row)<=max(gi,li,pi,ci): continue
            try: lf=float(row[li]);cpm=float(row[ci]);pv=float(row[pi])
            except Exception: continue
            g=row[gi].upper()
            if g and (g not in D or cpm>D[g][1]): D[g]=(lf,cpm,pv)
    return D
random.seed(9)
print('%-44s %7s %7s %7s %7s %7s'%('contrast','IGN','PATgrow','MATsupp','bg','z(IGN)'))
print('-'*90)
for f in sorted(glob.glob('drug/*DEedgeR.tsv')):
    D=load(f)
    expressed={g:v for g,v in D.items() if v[1]>2}
    if len(expressed)<4000: continue
    bg=float(np.mean([v[0] for v in expressed.values()]))
    def m(S):
        vs=[expressed[g][0] for g in S if g in expressed]
        return (float(np.mean(vs)),len(vs)) if vs else (np.nan,0)
    ign,nign=m(IGN); pat,npat=m(PAT); mat,nmat=m(MAT)
    if nign<8: continue
    pool=list(expressed);lv={g:expressed[g][1] for g in pool}
    targ=[expressed[g][1] for g in IGN if g in expressed]
    arr=np.array([lv[g] for g in pool])
    sims=[]
    for _ in range(1500):
        s=0
        for t in targ:
            cand=[pool[k] for k in np.argsort(np.abs(arr-t))[:120]]
            s+=expressed[random.choice(cand)][0]
        sims.append(s/len(targ))
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    nm=os.path.basename(f).replace('GSE168763_','').replace('_DEedgeR.tsv','')
    print('%-44s %7.3f %7.3f %7.3f %7.3f %7.2f  (n=%d)'%(nm,ign-bg,pat-bg,mat-bg,bg,(ign-mu)/sd if sd else 0,nign))
