import glob,os,csv,numpy as np,re,random,statistics
IGN='IGF2 H19 DLK1 MEG3 RIAN MIRG MEST PEG3 ZIM1 PLAGL1 CDKN1C KCNQ1OT1 IGF2R NDN MAGEL2 GPC3 GRB10 PEG10 NNAT SGCE GNAS SLC38A4 PHLDA2 IMPACT NAP1L5 PPP1R9A BLCAP INPP5F'.split()
CHON='SOX9 ACAN COL2A1 COL9A1 COL11A1 COL10A1 IHH PTHLH'.split()
CYC='MKI67 CCNB1 TOP2A CDK1 RRM2 MCM2 PCNA CCNA2 BUB1 PLK1 AURKA TYMS TK1 BIRC5'.split()
D={}
for f in sorted(glob.glob('do_rna/*.txt')):
    nm=os.path.basename(f).replace('.counts.featureCounts.txt','')
    d={}
    with open(f) as fh:
        r=csv.reader(fh,delimiter='\t');hdr=next(r);ti=hdr.index('tpm')
        for row in r:
            if len(row)<=ti: continue
            g=row[0].upper()
            try: v=float(row[ti])
            except Exception: continue
            if g not in d or v>d[g]: d[g]=v
    D[nm]=d
genes=sorted(set.intersection(*[set(v) for v in D.values()]))
M={k:np.log2(np.array([v[g] for g in genes])+1) for k,v in D.items()}
gi={g:i for i,g in enumerate(genes)}
allv=np.array(list(M.values()));ex=allv.max(axis=0);ok=ex>np.percentile(ex,50)
def grp(rx): return [k for k in M if re.search(rx,k,re.I)]
random.seed(6)
def sc(A,B,gs,nsim=600):
    a=np.mean([M[k] for k in A],axis=0);b=np.mean([M[k] for k in B],axis=0)
    v=a-b;bg=float(v[ok].mean())
    sel=[gi[g] for g in gs if g in gi and ok[gi[g]]]
    if len(sel)<6: return None
    pool=np.array([i for i in range(len(v)) if ok[i]])
    order={i:pool[np.argsort(np.abs(ex[pool]-ex[i]))[:120]] for i in sel}
    sims=[np.mean([v[random.choice(order[i])] for i in sel]) for _ in range(nsim)]
    mu,sd=statistics.mean(sims),statistics.pstdev(sims)
    return float(v[sel].mean())-bg,(float(v[sel].mean())-mu)/sd if sd else 0,len(sel)
print('libraries:',len(M))
print('\n=== DISTRACTION OSTEOGENESIS (mechanical bone LENGTHENING) vs FRACTURE, sorted skeletal stem/progenitors ===')
for nm,A,B in [('DO POD10 vs Fx POD10',grp(r'POD10_DO'),grp(r'POD10_Fx|Fx-POD10')),
               ('DO POD15 vs Fx POD15',grp(r'POD15_DO'),grp(r'POD15_Fx')),
               ('DO (all) vs Fx (all)',grp(r'_DO_|DO-POD|POD15_DO'),grp(r'_Fx_|Fx-POD')),
               ('DO POD10 vs POD5 (baseline)',grp(r'POD10_DO'),grp(r'POD5_')),
               ('Fx POD10 vs POD5 (baseline)',grp(r'POD10_Fx|Fx-POD10'),grp(r'POD5_'))]:
    if not A or not B: print('  %-32s (missing %d/%d)'%(nm,len(A),len(B))); continue
    for lbl,gs in [('IMPRINTED',IGN),('chondrogenic',CHON),('cell cycle',CYC)]:
        r=sc(A,B,gs)
        if r: print('  %-30s %-14s %+6.2f  z=%+5.2f  n=%d'%(nm,lbl,r[0],r[1],r[2]))
    print()
