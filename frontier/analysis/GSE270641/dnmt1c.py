import gzip,collections,random,statistics as st
from scipy import stats
regs=collections.defaultdict(list)
with open('b23/dnmt1.narrowPeak') as f:
    f.readline()
    for line in f:
        p=line.rstrip('\n').split('\t')
        if len(p)<5 or '_' in p[0]: continue
        regs[p[0]].append((int(p[1]),int(p[2])))
for c in regs: regs[c].sort()

genes=collections.defaultdict(list)
with gzip.open('mm10_refGene.txt.gz','rt') as f:
    for line in f:
        p=line.split('\t'); c,s,e,n=p[2],int(p[4]),int(p[5]),p[12]
        if '_' in c: continue
        genes[n].append((c,s,e))
span={}
for n,v in genes.items():
    c=v[0][0]
    if any(x[0]!=c for x in v): continue
    span[n]=(c,min(x[1] for x in v),max(x[2] for x in v))

def count(g):
    c,s,e=span[g]; L=regs.get(c,[])
    return sum(1 for rs,re in L if re>s and rs<e), e-s

IMPRINTED=['Dlk1','Meg3','Rtl1','Meg8','Dio3','Mkrn3','Igf2','H19','Plagl1','Mest','Peg3','Grb10',
           'Ndn','Cdkn1c','Slc38a4','Mdk','Meis1','Gpc3','Peg10','Nnat','Sgce','Zim1','Zfp57']
present=[g for g in IMPRINTED if g in span and span[g][0] in regs]
obs=sum(count(g)[0] for g in present); L=sum(count(g)[1] for g in present)
print(f"Imprinted-network genes present: {len(present)}/{len(IMPRINTED)}   total span {L/1000:.0f} kb   regions {obs}")

# length-matched random gene sets
allg=[g for g in span if span[g][0] in regs]
bylen=sorted(allg, key=lambda g: span[g][2]-span[g][1])
idx={g:i for i,g in enumerate(bylen)}
random.seed(1); null=[]
for _ in range(2000):
    tot=0
    for g in present:
        i=idx[g]; lo,hi=max(0,i-250),min(len(bylen)-1,i+250)
        pick=bylen[random.randint(lo,hi)]
        tot+=count(pick)[0]
    null.append(tot)
mu=st.mean(null); sd=st.stdev(null)
p=(sum(1 for x in null if x>=obs)+1)/(len(null)+1)
print(f"length-matched null: mean {mu:.1f} +/- {sd:.1f}   observed {obs}   fold {obs/mu:.2f}x   empirical p = {p:.4g}")

print("\n--- the 14q32.2 / Dlk1-Dio3 locus itself (mouse chr12 distal) ---")
c,s,e='chr12',109450000,110290000
n=sum(1 for rs,re in regs['chr12'] if re>s and rs<e)
dens_here=n/((e-s)/1e5); dens_all=sum(len(v) for v in regs.values())/2.73e9*1e5
print(f"  chr12:{s}-{e} ({(e-s)/1000:.0f} kb, Dlk1 through Dio3): {n} regions = {dens_here:.2f}/100kb vs {dens_all:.2f} genome-wide = {dens_here/dens_all:.1f}x")
# poisson test
pv=stats.poisson.sf(n-1, dens_all*((e-s)/1e5))
print(f"  Poisson p = {pv:.3g}")
