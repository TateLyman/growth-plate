# Hedgehog pathway vs human height: full GWAS Catalog scan.
# Source: ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/
#         gwas-catalog-associations_ontology-annotated-full.zip
import csv,re,collections
csv.field_size_limit(10**8)
GENES=['PTCH1','PTCH2','SMO','GLI1','GLI2','GLI3','HHIP','SUFU','IHH','SHH','BOC','CDON',
       'GAS1','EVC','EVC2','RARG','CYP26B1','ALDH1A3','SFRP5','ACAN','DNMT3A','NPR2','FGFR3','SHOX']
res={g:{'height':[],'bmd':0,'other':collections.Counter()} for g in GENES}
with open('gwas-catalog-download-associations-alt-full.tsv',newline='',encoding='utf-8',errors='replace') as f:
    r=csv.reader(f,delimiter='\t'); next(r)
    for row in r:
        if len(row)<29 or not row[14]: continue
        genes=set(re.split(r'[ ,;\-x]+',row[14])); t=row[7].lower()
        try: p=float(row[27])
        except: p=None
        for g in GENES:
            if g in genes:
                if t in ('body height','height'): res[g]['height'].append(p or 1)
                elif 'bone mineral density' in t: res[g]['bmd']+=1
                else: res[g]['other'][row[7]]+=1
for g in GENES:
    h=res[g]['height']
    print('%-10s HEIGHT=%-4d minP=%-9s BMD=%d'%(g,len(h),('%.0e'%min(h) if h else '-'),res[g]['bmd']))
