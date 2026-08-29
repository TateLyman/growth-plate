import gzip,collections,bisect,random,statistics as st
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
tot=sum(len(v) for v in regs.values())

def load_iv(kind):
    d=collections.defaultdict(list)
    if kind=='cgi':
        with gzip.open('mm10_cpgIslandExt.txt.gz','rt') as f:
            for line in f:
                p=line.split('\t')
                if p[1] in CHR: d[p[1]].append((int(p[2]),int(p[3])))
    else:
        with gzip.open('mm10_refGene.txt.gz','rt') as f:
            for line in f:
                p=line.split('\t'); c,strand,s,e=p[2],p[3],int(p[4]),int(p[5])
                if c not in CHR: continue
                if kind=='prom':
                    t=s if strand=='+' else e; d[c].append((max(0,t-1000),t+1000))
                else: d[c].append((s,e))
    for c in d:
        d[c].sort(); m=[]
        for s,e in d[c]:
            if m and s<=m[-1][1]: m[-1][1]=max(m[-1][1],e)
            else: m.append([s,e])
        d[c]=[(s,e) for s,e in m]
    return d
IV={k:load_iv(k) for k in ('cgi','prom','body')}
def hit(d,c,s,e):
    L=d.get(c)
    if not L: return False
    i=bisect.bisect_right(L,(s,10**12))-1
    for j in (i,i+1):
        if 0<=j<len(L) and L[j][1]>s and L[j][0]<e: return True
    return False
print(f"regions analysed: {tot} on {len(regs)} chromosomes ({sum(CHR.values())/1e6:.0f} Mb)")
print(f"{'compartment':16s} {'observed':>9s} {'shuffled':>9s} {'fold':>6s}")
random.seed(11)
for k,label in (('cgi','CpG islands'),('prom','promoters +/-1kb'),('body','gene bodies')):
    o=sum(1 for c,L in regs.items() for s,e in L if hit(IV[k],c,s,e))
    sh=[]
    for _ in range(10):
        n=0
        for c,L in regs.items():
            cl=CHR[c]
            for s,e in L:
                ns=random.randint(3_000_000, cl-(e-s)-3_000_000)
                if hit(IV[k],c,ns,ns+(e-s)): n+=1
        sh.append(100*n/tot)
    m=st.mean(sh)
    print(f"{label:16s} {100*o/tot:8.1f}% {m:8.1f}% {100*o/tot/m:5.2f}x")
inter=sum(1 for c,L in regs.items() for s,e in L if not hit(IV['body'],c,s,e) and not hit(IV['prom'],c,s,e))
print(f"\nneither gene body nor promoter (intergenic): {100*inter/tot:.1f}%")
o=sum(1 for c,L in regs.items() for s,e in L if hit(IV['prom'],c,s,e) or hit(IV['cgi'],c,s,e))
print(f"promoter OR CpG island: {100*o/tot:.1f}%  -> {100-100*o/tot:.1f}% of Dnmt1-dependent methylation is OUTSIDE the promoter/island compartment")
