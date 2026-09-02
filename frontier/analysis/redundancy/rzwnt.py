import gzip,statistics as st
def load(fn):
    rows=[];hdr=None;on=False;titles=None
    with gzip.open(fn,'rt',errors='replace') as f:
        for l in f:
            l=l.rstrip('\n')
            if l.startswith('!Sample_title'): titles=[x.strip('"') for x in l.split('\t')[1:]]
            if l.startswith('!series_matrix_table_begin'): on=True; continue
            if l.startswith('!series_matrix_table_end'): break
            if on:
                p=l.split('\t')
                if hdr is None: hdr=p; continue
                rows.append(p)
    return titles,hdr,rows
def ann(f):
    m={}
    with gzip.open(f,'rt',errors='replace') as fh:
        on=False
        for l in fh:
            if l.startswith('!platform_table_begin'): on=True; continue
            if l.startswith('!platform_table_end'): break
            if on:
                p=l.rstrip('\n').split('\t')
                if p[0]=='ID': continue
                if len(p)>2: m[p[0].strip('"')]=p[2].strip('"')
    return m
T,H,R=load('GSE9160_series_matrix.txt.gz')
A=ann('GPL570.annot.gz')
zones=[]
for t in T:
    tl=t.lower()
    for z in ['reserve','prolif','prehyp','hyper','perich']:
        if z in tl: zones.append(z); break
    else: zones.append('?')
idx={}
for i,z in enumerate(zones): idx.setdefault(z,[]).append(i)
order=['reserve','prolif','prehyp','hyper','perich']
order=[z for z in order if z in idx]
print("samples per zone:", {z:len(idx[z]) for z in order})
vals={}
for p in R:
    g=A.get(p[0].strip('"'))
    if not g: continue
    try: v=[float(x) if x not in ('','null','NA') else 0.0 for x in p[1:]]
    except: continue
    vals.setdefault(g,[]).append(v)
def prof(g):
    if g not in vals: return None
    # take probe with highest mean
    best=max(vals[g],key=lambda v: sum(v)/len(v))
    return [st.mean([best[i] for i in idx[z]]) for z in order]
GROUPS={
 "WNT TARGETS (output readouts)":["AXIN2","LEF1","TCF7","NKD1","RNF43","ZNRF3","SP5","NOTUM","CCND1","TNFRSF19","LGR5","ASCL2"],
 "WNT INHIBITORS (secreted)":["SFRP1","SFRP2","SFRP4","SFRP5","FRZB","DKK1","DKK3","WIF1","GREM1"],
 "RZ PROGENITOR MARKERS (Lui)":["SFRP5","NT5E","PTHLH","FGFR3","GDF5","PRRX1","CD34"],
 "SPIN FAMILY":["SPIN1","SPIN2A","SPIN3","SPIN4"],
 "CORE WNT MACHINERY":["CTNNB1","TCF7L2","GSK3B","APC","AXIN1","CSNK1A1","DVL1","DVL2","DVL3","CXXC5","TELO2"],
 "ZONE ID CONTROLS":["COL2A1","COL10A1","IHH","MKI67","SOX9","RUNX2"],
}
allv=[]
for g in vals:
    b=max(vals[g],key=lambda v:sum(v)/len(v)); allv.append(sum(b)/len(b))
allv.sort()
def pct(x):
    import bisect; return 100.0*bisect.bisect_left(allv,x)/len(allv)
for name,gs in GROUPS.items():
    print("\n=== %s ==="%name)
    print("%-9s %9s %9s %9s %9s %9s   %s"%("gene",*[z[:6].upper() for z in order],"RZ pctile"))
    for g in gs:
        p=prof(g)
        if p is None: print("%-9s  (no probe)"%g); continue
        print("%-9s "%g + " ".join("%9.1f"%x for x in p) + "   %5.1f"%pct(p[0]))
