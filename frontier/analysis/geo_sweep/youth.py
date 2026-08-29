import sys,os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import q,numpy as np,re,json
from scipy import stats
DROP=set(('PTPRC CD74 SYK MPEG1 NCKAP1L CD84 PLCB2 PIK3R5 TLR3 GIMAP4 SLFN2 IFI47 OASL2 CD38 RASGRP1 '
 'PLBD1 CYTH4 ITGAM ADGRE1 CSF1R LYZ2 FCGR3 C1QA C1QB C1QC TYROBP FCER1G AIF1 LAPTM5 CORO1A LCP1 CD52 '
 'CD68 MRC1 MSR1 CTSS CTSK ACP5 MMP9 TNFRSF11A CCL3 CCL4 CXCL9 CXCL10 IFNG B2M EMCN TIE1 ESAM SOX18 '
 'CAV2 CAV1 PECAM1 CDH5 KDR FLT1 VWF CLDN5 EGFL7 ROBO4 TEK ENG PLVAP AQP1 RAMP2 CD34 BGLAP BGLAP2 IBSP '
 'COL1A1 COL1A2 SP7 DMP1 SOST MEPE PHEX MYH8 MYH4 MYH3 MYH1 MYH2 ACTA1 CASQ1 PLN TNNT3 TNNI2 MYL1 MYLPF '
 'DES CKM MB TTN NEB ACTN2 TMOD1 TPM3 MYBPC1 TRIM55 MYOD1 MYOG HBB HBA1 GATA1 KLF1 TRIM58 SLC25A37 ALAS2 '
 'ERMAP UROD GLRX5 CD79A MS4A1 ELANE MPO PRTN3 CAMP LTF NGP S100A8 S100A9 S100A12 TBX5 TBX4 HOXA13 HOXD13').split())
def _vec(acc,A,B,minpct=55):
    d=q.D(acc);X=d['X'];ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,minpct)
    v=np.nanmean(X[:,A],axis=1)-np.nanmean(X[:,B],axis=1);v[~ok]=np.nan
    return {str(g):float(x) for g,x in zip(d['g'],v) if np.isfinite(x) and str(g) not in DROP}
def _G(a,rx):
    d=q.D(a);return [i for i,l in enumerate(d['labels']) if re.search(rx,l,re.I)]
def build():
    """YOUTH axis: + = younger AND longer. 8 zone-matched axes, mouse+rat, contamination removed."""
    M='GSE114919_Mouse';R='GSE114919_Rat'
    AX={'mPZ_age':_vec(M,_G(M,r'^1wT_PZ'),_G(M,r'^4wT_PZ')),
        'mHZ_age':_vec(M,_G(M,r'^1wT_HZ'),_G(M,r'^4wT_HZ')),
        'mPZ_len':_vec(M,_G(M,r'^1wT_PZ'),_G(M,r'^1wP_PZ')),
        'mHZ_len':_vec(M,_G(M,r'^1wT_HZ'),_G(M,r'^1wPh_HZ')),
        'rPZ_age':_vec(R,_G(R,r'^T1wk PZ'),_G(R,r'^T4wk PZ')),
        'rHZ_age':_vec(R,_G(R,r'^T1wk HZ'),_G(R,r'^T4wk HZ')),
        'rPZ_len':_vec(R,_G(R,r'^T1wk PZ'),_G(R,r'^Ph1wk PZ')),
        'rHZ_len':_vec(R,_G(R,r'^T1wk HZ'),_G(R,r'^Ph1wk HZ'))}
    sh=set.intersection(*[set(v) for v in AX.values()])
    Z={}
    for k,v in AX.items():
        a=np.array([v[g] for g in sh]);m,s=a.mean(),a.std()
        Z[k]={g:(v[g]-m)/s for g in sh}
    return {g:float(np.mean([Z[k][g] for k in Z])) for g in sh}
YOUTH=build() if __name__!='__x__' else None
def score(acc,A,B,name='',minshared=250):
    d=q.D(acc)
    v=_vec(acc,A,B)
    sh=sorted(set(v)&set(YOUTH))
    if len(sh)<minshared: return None
    x=np.array([v[g] for g in sh]);y=np.array([YOUTH[g] for g in sh])
    r,p=stats.pearsonr(x,y)
    return dict(acc=acc,name=name,r=float(r),p=float(p),n=len(sh))
if __name__=='__main__':
    print('YOUTH axis genes:',len(YOUTH))
    top=sorted(YOUTH.items(),key=lambda kv:-kv[1])[:30]
    bot=sorted(YOUTH.items(),key=lambda kv:kv[1])[:30]
    print('\nYOUNG+LONG:',', '.join('%s %.1f'%(g,v) for g,v in top))
    print('\nOLD+SHORT :',', '.join('%s %.1f'%(g,v) for g,v in bot))
