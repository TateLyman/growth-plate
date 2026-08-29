import sys;sys.path.insert(0,'.')
import q,numpy as np,re
d=q.D('GSE213574');L=[str(x) for x in d['labels']]
def G(rx): return [i for i,l in enumerate(L) if re.search(rx,l,re.I)]
A=G(r'callus SSC|SSC injured|callus BCSP|BCSP Injured');B=G(r'Uninjured SSC|SSC uninjured|BCSP Uninjured')
X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,50)
v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1);bg=float(np.nanmean(v[ok]))
SETS={
 'IMPRINTED NETWORK':'IGF2 H19 DLK1 MEG3 MEST PEG3 ZIM1 PLAGL1 CDKN1C IGF2R NDN GPC3 GRB10 PEG10 NNAT SGCE SLC38A4 PHLDA2 IMPACT NAP1L5 PPP1R9A',
 'cell cycle':'MKI67 CCNB1 TOP2A CDK1 RRM2 MCM2 PCNA CCNA2 BUB1 PLK1 AURKA FOXM1 TYMS TK1 BIRC5 CENPF',
 'HYPOXIA / HIF':'HIF1A EPAS1 VEGFA SLC2A1 PGK1 LDHA CA9 BNIP3 ADM P4HA1 PDK1 ANKRD37 EGLN3',
 'BMP':'BMP2 BMP4 BMP6 BMP7 ID1 ID2 ID3 ID4 SMAD1 SMAD5 SMAD9 BAMBI',
 'WNT':'WNT5A WNT4 AXIN2 LEF1 TCF7 NOTUM SP5 WIF1 DKK1 CTNNB1',
 'NOTCH':'NOTCH1 NOTCH2 NOTCH3 JAG1 DLL1 HES1 HEY1 HEYL RBPJ',
 'TGF-beta':'TGFB1 TGFB2 TGFB3 TGFBR1 TGFBR2 SMAD3 SERPINE1 SKIL',
 'YAP/TAZ mechano':'YAP1 WWTR1 CTGF CCN2 CYR61 CCN1 ANKRD1 AMOTL2 THBS1',
 'inflammation':'IL6 IL1B TNF CXCL1 CXCL2 CCL2 PTGS2 NFKBIA SOCS3',
 'PDGF/FGF':'PDGFA PDGFB PDGFRA PDGFRB FGF2 FGF18 FGFR1 FGFR2',
 'chondrogenic':'SOX9 ACAN COL2A1 COL9A1 COL11A1 COL10A1 IHH PTHLH',
 'stemness/pluripotency':'KLF4 MYC SOX2 POU5F1 NANOG LIN28A LIN28B SALL4 DPPA3 ZFP42',
 'senescence/SASP':'CDKN2A CDKN1A TP53 IL6 SERPINE1 MMP3 GLB1 TRP53',
 'DNA damage':'ATM ATR CHEK1 CHEK2 H2AX MDM2 GADD45A GADD45B RAD51 BRCA1',
}
print('%-24s %8s  %s'%('gene set','delta','(callus SSC/BCSP minus uninjured, above background)'))
print('-'*76)
for nm,s in SETS.items():
    gs=s.split();vals=[]
    for g in gs:
        i=[k for k,x in enumerate(d['g']) if str(x)==g and ok[k]]
        if i and np.isfinite(v[i[0]]): vals.append(v[i[0]])
    if vals: print('%-24s %8.2f  (n=%d)'%(nm,np.mean(vals)-bg,len(vals)))
o=np.argsort(-np.where(ok,v,-99))
print('\nTOP genes up in fracture callus stem cells:')
print('  '+', '.join('%s %.1f'%(d['g'][i],v[i]-bg) for i in o[:45]))
