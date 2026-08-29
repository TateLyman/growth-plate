import csv, statistics as st, math
from scipy import stats
rows=list(csv.reader(open('query/human_growth_plate_expression.byzone.csv')))
hdr=rows[0][1:]
zones={}
for i,h in enumerate(hdr):
    z,d=h.split('__'); zones.setdefault(z,{})[d]=i
Z=['GP1_2_stem','GP3_proliferative','GP4_prehypertrophic','GP5_hypertrophic']
data={r[0]:[float(x) for x in r[1:]] for r in rows[1:] if len(r)==len(hdr)+1}
print(f"genes {len(data)}; zones/donors: " + ", ".join(f"{z}:{len(zones[z])}" for z in Z))
allv=[v for vs in data.values() for v in vs]
print(f"value scale: min {min(allv):.2f} max {max(allv):.2f} median {st.median(allv):.2f}  -> percentile-like\n")

def zmean(g,z):
    return st.mean(data[g][i] for i in zones[z].values())
def paired(g,z1,z2):
    ds=sorted(set(zones[z1])&set(zones[z2]))
    a=[data[g][zones[z1][d]] for d in ds]; b=[data[g][zones[z2][d]] for d in ds]
    t,p=stats.ttest_rel(a,b)
    return st.mean(b)-st.mean(a), p, len(ds)

GENES=['DNMT1','UHRF1','DNMT3A','DNMT3B','TET1','TET2','TET3','EZH2','EED','SUZ12','KDM6A','KDM6B',
       'NSD1','ACAN','CCN2','FGFR3','ESR1','CYP19A1','MEG3','RTL1','MKRN3','CDKN1C','PLAGL1','MEST','IGF1','IGF2']
print(f"{'gene':9s} {'stem':>7s} {'prolif':>7s} {'preHT':>7s} {'HT':>7s} | {'prolif-stem':>12s} {'p':>8s} | pct-rank")
print('-'*78)
srt=sorted(allv)
def pct(v): return 100*sum(1 for x in srt if x<v)/len(srt)
out=[]
for g in GENES:
    if g not in data: print(f"{g:9s} NOT IN TABLE"); continue
    m=[zmean(g,z) for z in Z]
    d,p,n=paired(g,'GP1_2_stem','GP3_proliferative')
    star='  **' if p<0.05 else ('  *' if p<0.10 else '')
    print(f"{g:9s} {m[0]:7.1f} {m[1]:7.1f} {m[2]:7.1f} {m[3]:7.1f} | {d:+12.1f} {p:8.4f}{star} | {pct(st.mean(m)):5.1f}")
