import glob,re,os,collections
RZ=re.compile(r'(resting zone|reserve zone|restingzone|reservezone|round cell|round chondrocyt|epiphyseal zone|stem cell zone|germinal zone|quiescent zone|\bRZ[-_ ]|_RZ\b)',re.I)
PATS=[r'\bage\s*[:=]\s*([^|\n]{1,40})',
      r'\b(\d+)\s*(?:wk|week|weeks)\b',
      r'\b(\d+)\s*(?:mo|month|months)\b',
      r'\bP(\d{1,3})\b',
      r'\bE(\d{1,2}\.?\d?)\b',
      r'\b(\d+)[- ]?(?:d|day|days)[- ]?(?:old|postnatal)\b',
      r'developmental stage\s*[:=]\s*([^|\n]{1,40})',
      r'\b(fetal|newborn|neonatal|juvenile|adult|prepubertal|pubertal|adolescent|aged|young|old)\b']
AGEPAT=[re.compile(p,re.I) for p in PATS]
hits=[]
for f in sorted(glob.glob('soft/*.txt')):
    acc=os.path.basename(f)[:-4]
    t=open(f,encoding='utf8',errors='replace').read()
    if not RZ.search(t): continue
    samples=re.split(r'\^SAMPLE\s*=\s*',t)[1:]
    rz=[s for s in samples if RZ.search(s)]
    if len(rz)<2: continue
    ages=collections.Counter()
    for s in rz:
        found=set()
        for p in AGEPAT:
            for m in p.finditer(s):
                v=(m.group(1) if m.groups() else m.group(0)).strip().lower()
                if v and len(v)<40: found.add(v)
        for v in found: ages[v]+=1
    hits.append((acc,len(samples),len(rz),ages))
print('series with >=2 resting/reserve-zone samples:',len(hits))
for acc,ns,nrz,ages in sorted(hits,key=lambda x:-x[2]):
    print('\n%-11s samples=%-4d RZ-samples=%-3d'%(acc,ns,nrz))
    print('   ages:',dict(list(ages.most_common(16))))
