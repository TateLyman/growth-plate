# 9q22.3: does the human height signal map to PTCH1 or to the let-7 cluster?
# Same source file as hh_height_gwas.py
import csv,re
csv.field_size_limit(10**8)
GRP={'550kb common region':['PTCH1','C9orf3','ACTL7A','ACTL7B','FANCC','MIR23B','MIR27B','MIR24-1','MIR3074','MIR6081'],
     'let-7 cluster (outside, deleted in 10/11)':['MIRLET7A1','MIRLET7F1','MIRLET7D','MIRLET7DHG'],
     'Lin28 axis (control)':['LIN28B','LIN28A']}
hits={g:[] for gs in GRP.values() for g in gs}
with open('gwas-catalog-download-associations-alt-full.tsv',newline='',encoding='utf-8',errors='replace') as f:
    r=csv.reader(f,delimiter='\t'); next(r)
    for row in r:
        if len(row)<29 or not row[14] or row[7].lower() not in ('body height','height'): continue
        genes=set(re.split(r'[ ,;\-x/]+',row[14].upper()))|set(re.split(r'[ ,;/]+',row[14].upper()))
        try: p=float(row[27])
        except: p=None
        for g in hits:
            if g.upper() in genes: hits[g].append(p or 1)
for grp,gs in GRP.items():
    print('\n===',grp)
    for g in gs:
        h=hits[g]; print('  %-14s n=%-4d minP=%s'%(g,len(h),('%.0e'%min(h) if h else '-')))
