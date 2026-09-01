import sys;sys.path.insert(0,'.')
import q,numpy as np,re
d=q.D('GSE113982');L=d['labels'];X=d['X']
def G(rx): return [i for i,l in enumerate(L) if re.search(rx,l)]
RZy,RZo=G(r'^p[23]_R'),G(r'^p28_R');PZy,PZo=G(r'^p[23]_P'),G(r'^p28_P');HZy,HZo=G(r'^p[23]_H'),G(r'^p28_H')
ex=np.nanmax(X,axis=1);ok=ex>np.nanpercentile(ex,55)
def bg(a,b):
    v=np.nanmean(X[:,a],axis=1)-np.nanmean(X[:,b],axis=1);return float(np.nanmean(v[ok]))
BG={'RZ':bg(RZo,RZy),'PZ':bg(PZo,PZy),'HZ':bg(HZo,HZy)}
CLS={
 'G9a / EHMT (H3K9me2)  [UNC0638/0642, MS152/1262]':['EHMT1','EHMT2','WIZ','CBX1','CBX3','CBX5','SUV39H1','SUV39H2','SETDB1','SETDB2','ATF7IP'],
 'HDAC class I  [TSA, butyrate, VPA, romidepsin, CI-994, SAHA]':['HDAC1','HDAC2','HDAC3','HDAC8','SIN3A','NCOR1','NCOR2','RBBP4','RBBP7','MTA1','MTA2','CHD4','MBD2','MBD3','GATAD2A'],
 'HDAC class II/IV':['HDAC4','HDAC5','HDAC6','HDAC7','HDAC9','HDAC10','HDAC11'],
 'sirtuins  [nicotinamide]':['SIRT1','SIRT2','SIRT3','SIRT6','SIRT7','NAMPT','NMNAT1'],
 'BET  [I-BET151, GSK726]':['BRD2','BRD3','BRD4','BRDT'],
 'TOP1/TOP2  [topotecan, indotecan, etoposide]':['TOP1','TOP1MT','TOP2A','TOP2B','TOP3A','TOP3B'],
 'PRC2 / KDM6  [DZNep, GSK-J4]':['EZH1','EZH2','SUZ12','EED','JARID2','KDM6A','KDM6B','KDM2B','RNF2','BMI1','CBX7','CBX2'],
 'DNA methylation':['DNMT1','DNMT3A','DNMT3B','DNMT3L','UHRF1','TET1','TET2','TET3'],
 'imprint maintenance':['ZFP57','TRIM28','ZNF445','CTCF','DAXX','ATRX','MPHOSPH8','TASOR','PPHLN1'],
 'CDK2/CDK5  [(S)-PHA533533 original target]':['CDK2','CDK5','CDK5R1','CDK5R2','CCNE1','CCNE2'],
}
print('CHROMATIN-DRUG TARGET CLASSES: change with age, ABOVE each zone`s background (log2)')
print('%-46s %7s %7s %7s'%('gene','RZ','PZ','HZ'))
for cls,gs in CLS.items():
    print('\n--- %s'%cls)
    vals=[]
    for g in gs:
        x=q.v(d,g)
        if x is None: continue
        r=np.nanmean(x[RZo])-np.nanmean(x[RZy])-BG['RZ']
        p=np.nanmean(x[PZo])-np.nanmean(x[PZy])-BG['PZ']
        h=np.nanmean(x[HZo])-np.nanmean(x[HZy])-BG['HZ']
        if not np.isfinite(r): continue
        vals.append(r); print('  %-44s %7.2f %7.2f %7.2f'%(g,r,p,h))
    if vals: print('  %-44s %7.2f  <== class mean (RZ)'%('',np.mean(vals)))
