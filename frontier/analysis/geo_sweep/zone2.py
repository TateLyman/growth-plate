import sys;sys.path.insert(0,'.')
import q,numpy as np
SPEC=[
 # acc, label, A-regex (stem/resting), B-regex (differentiated), species
 ('GSE16981','rat-Baron RZvPZ',    r'^Resting zone',            r'^Proliferative zone, Biol','rat'),
 ('GSE23432','rat-Baron RZvEPI',   r'^Resting zone',            r'^Epiphyseal cartilage','rat'),
 ('GSE9160', 'HUMAN RZvPZ',        r'^Reserve',                 r'^Proliferative','HUMAN'),
 ('GSE9537', 'rat-femur RZvPZ',    r'ReserveZone',              r'ProliferativeZone','rat'),
 ('GSE87605','MOUSE RoundvFlat',   r'^Round Cell',              r'^Flat Cell','mouse'),
 ('GSE18738','BOVINE RZvHZ',       r'reserve zone',             r'hypertrophic zone','bovine'),
 ('GSE160364','MOUSE LRC hi v lo', r'^High',                    r'^Low','mouse'),
 ('GSE54216','rat-10d RZvDeep',    r'^resting zone',            r'^intermediate/deep','rat'),
 ('GSE18568','CHICK PZvHZ',        r'^Proliferative',           r'^Hypertrophic','chick'),
]
PANEL={
 'Hedgehog':['SMO','PTCH1','PTCH2','GLI1','GLI2','GLI3','IHH','SHH','HHIP','BOC','CDON','GAS1','SUFU'],
 'RZ identity':['SFRP5','FRZB','PTHLH','GREM1','THBS1','THBS2','DCN','CYTL1','SOX9','PRG4','PDGFRA','FOXA2'],
 'Methylation':['DNMT1','DNMT3A','DNMT3B','UHRF1','TET1','TET2','TET3','TDG','MECP2','PCNA'],
 'Endocrine':['ESR1','ESR2','AR','GHR','IGF1','IGF1R','IGF2','NR3C1','NPR2','FGFR3','PTH1R'],
 'Cycle/senes':['MKI67','CDKN1A','CDKN2A','CDKN2B','CDKN2C','TP53','CCND1','GLB1'],
 'Wnt/TGFb':['WNT4','WNT5A','AXIN2','LEF1','CTNNB1','TGFBR2','TGFB1','SMAD3','BMP2'],
 'Imprinted':['H19','DLK1','MEG3','PLAGL1','GRB10','CDKN1C','PEG3'],
}
res={}
for acc,name,ra,rb,sp in SPEC:
    d=q.D(acc); A=q.grp(d,ra); B=q.grp(d,rb)
    res[name]=(d,A,B)
    print('%-22s %-8s nA=%d nB=%d genes=%d'%(name,sp,len(A),len(B),len(d['g'])))
print()
names=[s[1] for s in SPEC]
for cat,genes in PANEL.items():
    print('\n===== %s ====='%cat)
    print('%-9s'%'gene'+''.join('%9s'%n.split()[0][:8] for n in names)+'   verdict')
    for gn in genes:
        vals=[]
        for n in names:
            d,A,B=res[n]; x=q.v(d,gn)
            vals.append(None if x is None else float(np.nanmean(x[A])-np.nanmean(x[B])))
        got=[v for v in vals if v is not None]
        if not got: continue
        pos=sum(1 for v in got if v>0.25); neg=sum(1 for v in got if v<-0.25)
        vd='%d+/%d-/%d0 of %d'%(pos,neg,len(got)-pos-neg,len(got))
        print('%-9s'%gn+''.join(('%9.2f'%v if v is not None else '        .') for v in vals)+'   '+vd)
