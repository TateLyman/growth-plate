# F-R108 headline analysis: cell-cycle load relative to matrix output, across every
# contrast in the corpus where the phenotype is bone length or plate closure.
# Run from the sweep scratch dir (needs cache/*.npz built by build_cache.py).
import sys;sys.path.insert(0,'.')
import q,numpy as np
CART=['ACAN','COL2A1','COL9A1','COL9A2','COL11A1','COMP','MATN1','MATN3','SOX9','COL11A2',
      'CILP','SPARC','HAPLN1','FMOD','LUM','EPYC','CHAD']
CYC=['MKI67','RRM2','MYBL2','CLSPN','LIG1','CDC25B','CCNB1','TOP2A','PCNA','CCNA2','CDK1','BUB1',
     'PLK1','AURKA','AURKB','MCM2','MCM3','MCM4','MCM5','MCM6','MCM7','TYMS','TK1','E2F1','FOXM1',
     'KIF11','NUSAP1','UBE2C','BIRC5','CENPF','ASPM','TTK','RAD51','CHEK1','ESCO2','GINS2','POLA1',
     'PRIM1','DHFR','CDT1']
CON=[('GSE189528',[0,2,4],[1,3,5],'Longshanks LONGER','+'),
     ('GSE53277',list(range(6)),[6,7,8,9,10],'GreatDane LONGER','+'),
     ('GSE22855',list(range(7)),[9,10],'enchondroma vs GP (persist)','+'),
     ('GSE30835',[2,6,7,8,10,14,20],[23,24],'enchondroma vs GP (2nd set)','+'),
     ('GSE190744',[6,7,8,9,10,11],[0,1,2,3,4,5],'dexamethasone (banking)','+'),
     ('GSE270640',[4,5,6,7],[0,1,2,3],'Dnmt1cKO SHORT','-'),
     ('GSE145821',[6,7,8,9,10,11],[18,19,20,21,22,23],'Fgfr3GOF SHORT (3-4wk)','-'),
     ('GSE145821',list(range(6)),list(range(12,18)),'Fgfr3GOF (1-2wk, pre-phenotype)','-'),
     ('GSE18338',[2,3],[4,5],'HUMAN late vs pre puberty','-'),
     ('GSE18338',[2,3],[0,1],'HUMAN late vs early puberty','-'),
     ('GSE16981',[30,31,32,33,34],[15,16,17,18,19],'rat PZ 12wk vs 3wk','-')]
def mm(d,A,B,gs):
    vs=[]
    for g in gs:
        x=q.v(d,g)
        if x is None: continue
        v=np.nanmean(x[A])-np.nanmean(x[B])
        if np.isfinite(v): vs.append(v)
    return (float(np.mean(vs)),len(vs)) if vs else (np.nan,0)
if __name__=='__main__':
    ok=0
    for acc,A,B,nm,exp in CON:
        d=q.D(acc); c,_=mm(d,A,B,CART); y,n=mm(d,A,B,CYC); yc=y-c
        good=(yc<0) if exp=='+' else (yc>0); ok+=good
        print('%-34s %s  CART %+5.2f  CYCLE-minus-CART %+5.2f  n=%d  %s'%(nm,exp,c,yc,n,'OK' if good else 'XX'))
    print('\n%d/%d contrasts: cell-cycle load relative to matrix runs OPPOSITE to length.'%(ok,len(CON)))
