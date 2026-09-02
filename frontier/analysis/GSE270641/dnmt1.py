import gzip, collections, bisect, random, statistics as st

# --- load Dnmt1-dependent methylation regions ---
regs=collections.defaultdict(list)
tot=0
with open('b23/dnmt1.narrowPeak') as f:
    hdr=f.readline()
    for line in f:
        p=line.rstrip('\n').split('\t')
        if len(p)<5: continue
        c,s,e=p[0],int(p[1]),int(p[2])
        if '_' in c: continue
        regs[c].append((s,e,float(p[4])))
        tot+=1
for c in regs: regs[c].sort()
print(f"Dnmt1-dependent methylation regions (primary chroms): {tot}")
lens=[e-s for c in regs for s,e,_ in regs[c]]
print(f"  width: median {int(st.median(lens))} bp, mean {int(st.mean(lens))}, total {sum(lens)/1e6:.1f} Mb "
      f"({100*sum(lens)/2.73e9:.2f}% of the mm10 genome)")

# --- CpG islands ---
cgi=collections.defaultdict(list)
with gzip.open('mm10_cpgIslandExt.txt.gz','rt') as f:
    for line in f:
        p=line.split('\t'); c,s,e=p[1],int(p[2]),int(p[3])
        if '_' in c: continue
        cgi[c].append((s,e))
for c in cgi: cgi[c].sort()
ncgi=sum(len(v) for v in cgi.values()); cgibp=sum(e-s for v in cgi.values() for s,e in v)
print(f"mm10 CpG islands: {ncgi}, {cgibp/1e6:.1f} Mb ({100*cgibp/2.73e9:.2f}% of genome)")

# --- promoters (TSS +/- 1kb) and gene bodies ---
prom=collections.defaultdict(list); body=collections.defaultdict(list); genes={}
with gzip.open('mm10_refGene.txt.gz','rt') as f:
    for line in f:
        p=line.split('\t')
        c,strand,s,e,name=p[2],p[3],int(p[4]),int(p[5]),p[12]
        if '_' in c: continue
        tss = s if strand=='+' else e
        prom[c].append((max(0,tss-1000), tss+1000, name))
        body[c].append((s,e,name))
for d in (prom,body):
    for c in d: d[c].sort()

def merged_len(iv):
    out=[];
    for s,e,*_ in sorted(iv):
        if out and s<=out[-1][1]: out[-1][1]=max(out[-1][1],e)
        else: out.append([s,e])
    return sum(e-s for s,e in out), out

def overlaps(qc,qs,qe,d):
    L=d.get(qc)
    if not L: return []
    i=bisect.bisect_left(L,(qs-200000,))
    hit=[]
    for s,e,*rest in L[i:]:
        if s>qe: break
        if e>qs: hit.append((s,e,rest[0] if rest else None))
    return hit

def frac_hits(d,label):
    n=0
    for c,L in regs.items():
        for s,e,_ in L:
            if overlaps(c,s,e,d): n+=1
    print(f"  regions overlapping {label:22s}: {n:6d} / {tot}  = {100*n/tot:5.1f}%")
    return n

print("\n=== WHERE DO Dnmt1-DEPENDENT REGIONS FALL? ===")
n_cgi=frac_hits({c:[(s,e,None) for s,e in v] for c,v in cgi.items()}, "CpG islands")
n_prom=frac_hits(prom, "promoters (TSS+/-1kb)")
n_body=frac_hits(body, "gene bodies")

# background expectation by random shuffling within chromosomes
chrlen={}
with gzip.open('mm10_refGene.txt.gz','rt') as f:
    for line in f:
        p=line.split('\t'); c=p[2]
        if '_' in c: continue
        chrlen[c]=max(chrlen.get(c,0), int(p[5]))
random.seed(0)
def shuffle_frac(d, reps=3):
    fr=[]
    for _ in range(reps):
        n=0; m=0
        for c,L in regs.items():
            cl=chrlen.get(c,0)
            if cl<1e6: continue
            for s,e,_ in L:
                w=e-s; ns=random.randint(3000000, max(3000001,cl-w))
                m+=1
                if overlaps(c,ns,ns+w,d): n+=1
        fr.append(100*n/m)
    return st.mean(fr)
print("\n=== EXPECTED BY CHANCE (position-shuffled, 3 reps) ===")
print(f"  CpG islands : {shuffle_frac({c:[(s,e,None) for s,e in v] for c,v in cgi.items()}):5.1f}%")
print(f"  promoters   : {shuffle_frac(prom):5.1f}%")
print(f"  gene bodies : {shuffle_frac(body):5.1f}%")
