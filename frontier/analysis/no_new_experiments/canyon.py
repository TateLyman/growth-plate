import collections,random,statistics as st,gzip,bisect
CHR={'chr1':195471971,'chr2':182113224,'chr3':160039680,'chr4':156508116,'chr5':151834684,
'chr6':149736546,'chr10':130694993,'chr11':122082543,'chr12':120129022,'chr13':120421639,
'chr14':124902244,'chr15':104043685,'chr16':98207768,'chr17':94987271,'chr18':90702639,'chr19':61431566}
regs=collections.defaultdict(list)
with open('b23/dnmt1.narrowPeak') as f:
    f.readline()
    for line in f:
        p=line.rstrip('\n').split('\t')
        if len(p)<5 or p[0] not in CHR: continue
        regs[p[0]].append((int(p[1]),int(p[2])))
for c in regs: regs[c].sort()
tot=sum(len(v) for v in regs.values()); cov=sum(CHR.values()); dens=tot/cov*1e5

# CpG islands = proxy for canyon cores. Large CGIs (>=2kb) at developmental loci ~ DMVs.
cgi=collections.defaultdict(list)
with gzip.open('mm10_cpgIslandExt.txt.gz','rt') as f:
    for line in f:
        p=line.split('\t'); c,s,e=p[1],int(p[2]),int(p[3])
        if c in CHR: cgi[c].append((s,e))
for c in cgi: cgi[c].sort()
big=[(c,s,e) for c in cgi for s,e in cgi[c] if e-s>=2000]
print(f"mm10 CpG islands >=2 kb (DMV/canyon-core proxy): {len(big)}")

def n_in(c,s,e):
    L=regs.get(c,[]);  return sum(1 for rs,re in L if re>s and rs<e)

def test(label, wins):
    obs=sum(n_in(c,s,e) for c,s,e in wins)
    bp=sum(e-s for c,s,e in wins)
    exp=dens*bp/1e5
    random.seed(9); null=[]
    present=sorted(regs)
    for _ in range(300):
        n=0
        for c,s,e in wins:
            W=e-s
            cc=random.choices(present,weights=[CHR[x] for x in present])[0]
            st_=random.randint(3_000_000,CHR[cc]-W-3_000_000)
            n+=n_in(cc,st_,st_+W)
        null.append(n)
    mu=st.mean(null)
    p_dep=(sum(1 for x in null if x<=obs)+1)/(len(null)+1)
    p_enr=(sum(1 for x in null if x>=obs)+1)/(len(null)+1)
    print(f"{label:34s} {bp/1e6:7.2f} Mb  obs {obs:6d}  exp {mu:8.1f}  fold {obs/mu:5.2f}   "
          f"p(depl) {p_dep:.4f}  p(enr) {p_enr:.4f}")

test("CANYON CORES: CGI >=2 kb", big)
# flanks: 5 kb either side of those CGIs, excluding the core
fl=[]
for c,s,e in big:
    fl.append((c,max(0,s-5000),s)); fl.append((c,e,e+5000))
test("FLANKS: +/-5 kb around cores", fl)
# distal: 20-50 kb away
di=[]
for c,s,e in big:
    di.append((c,max(0,s-50000),max(0,s-20000))); di.append((c,e+20000,e+50000))
test("DISTAL: 20-50 kb away", di)
