"""Is TET1 actually expressed in the human growth plate? This is the check that
killed SPIN4 (1/10 arrays = background). Same corrected threshold: 60th percentile
of all 54,675 probes, with COL2A1/ACAN as positive and COL10A1/IHH as zonal controls."""
import gzip
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
T,H,R=load('GSE9160_series_matrix.txt.gz'); A=ann('GPL570.annot.gz')
n=len(T); cols=[[] for _ in range(n)]; byg={}
for p in R:
    pid=p[0].strip('"'); sym=A.get(pid,'')
    try: v=[float(x) if x not in ('','NA','null') else 0.0 for x in p[1:1+n]]
    except ValueError: continue
    if len(v)<n: continue
    for i in range(n): cols[i].append(v[i])
    if sym: byg.setdefault(sym,[]).append((pid,v))
THR=0.60
bg=[sorted(c)[int(THR*len(c))] for c in cols]
print("arrays: %d"%n)
print("zones :"," | ".join(t[:26] for t in T))
print("thresh:"," ".join("%d"%b for b in bg))
print()
GENES=['COL2A1','ACAN','COL10A1','IHH',              # controls
       'TET1','TET2','TET3',                          # the arm
       'DNMT1','DNMT3A','DNMT3B','UHRF1',             # the writers
       'IDH1','IDH2','OGDH',                          # 2-OG supply
       'EGLN1','EGLN2','EGLN3','HIF1A','EPAS1',       # the PHI class
       'KDM6B','KDM4A','FTO','SLC2A1']
def show(g):
    if g not in byg: print("%-9s (no probe)"%g); return
    for pid,v in byg[g]:
        det=sum(1 for i in range(n) if v[i]>bg[i])
        flag="OK " if det>=n*0.6 else ("low" if det>0 else "OFF")
        print("%-9s %-13s %2d/%-2d %s  %s"%(g,pid,det,n,flag," ".join("%7.0f"%x for x in v)))
for g in GENES:
    show(g)
