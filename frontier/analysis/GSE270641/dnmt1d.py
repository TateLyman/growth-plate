import gzip,collections,random,statistics as st
regs=collections.defaultdict(list)
with open('b23/dnmt1.narrowPeak') as f:
    f.readline()
    for line in f:
        p=line.rstrip('\n').split('\t')
        if len(p)<5 or '_' in p[0]: continue
        regs[p[0]].append((int(p[1]),int(p[2])))
for c in regs: regs[c].sort()
CHR={'chr1':195471971,'chr2':182113224,'chr3':160039680,'chr4':156508116,'chr5':151834684,
'chr6':149736546,'chr7':145441459,'chr8':129401213,'chr9':124595110,'chr10':130694993,
'chr11':122082543,'chr12':120129022,'chr13':120421639,'chr14':124902244,'chr15':104043685,
'chr16':98207768,'chr17':94987271,'chr18':90702639,'chr19':61431566,'chrX':171031299}
present=sorted(regs)
covered=sum(CHR[c] for c in present)
tot=sum(len(v) for v in regs.values())
dens=tot/covered*1e5
print(f"chromosomes with data: {len(present)} of 20  ({covered/1e6:.0f} Mb of 2,725 Mb = {100*covered/2725e6:.0f}%)")
print(f"MISSING ENTIRELY: {sorted(set(CHR)-set(present))}")
print(f"regions {tot}; correct density = {dens:.2f} per 100 kb (NOT 3.08 - that wrongly divided by the whole genome)\n")

def n_in(c,s,e):
    L=regs.get(c,[]); return sum(1 for rs,re in L if re>s and rs<e)

# permutation test for the Dlk1-Dio3 domain vs random same-size windows on covered chroms
W=840000; s0,e0='chr12',109450000
obs=n_in('chr12',109450000,110290000)
random.seed(7); null=[]
for _ in range(20000):
    c=random.choices(present,weights=[CHR[x] for x in present])[0]
    st_=random.randint(3_000_000, CHR[c]-W-3_000_000)
    null.append(n_in(c,st_,st_+W))
mu=st.mean(null); p=(sum(1 for x in null if x>=obs)+1)/(len(null)+1)
print(f"Dlk1-Dio3 domain (chr12:109.45-110.29 Mb, 840 kb): {obs} regions")
print(f"  random 840-kb windows on the same chromosomes: mean {mu:.1f}, 95th pct {sorted(null)[int(.95*len(null))]}, max {max(null)}")
print(f"  fold = {obs/mu:.2f}x   permutation p = {p:.4g}   ({sum(1 for x in null if x>=obs)} of {len(null)} windows matched or exceeded it)")

print("\n--- per-gene, ONLY genes on chromosomes with data ---")
genes=collections.defaultdict(list)
with gzip.open('mm10_refGene.txt.gz','rt') as f:
    for line in f:
        p=line.split('\t'); c,s,e,n=p[2],int(p[4]),int(p[5]),p[12]
        if c in regs: genes[n].append((c,s,e))
GOI=['Dlk1','Meg3','Rtl1','Meg8','Dio3','Plagl1','Mest','Grb10','Slc38a4','Mdk','Meis1','Peg10','Nnat',
     'Sgce','Zfp57','Ccn2','Fgfr3','Igf1','Ihh','Gli1','Npr2','Nppc','Tsc1','Mtor','Sox9','Col2a1',
     'Col10a1','Esr1','Ptch1','Hhip','Ezh2','Kdm5a','Kdm5b','Dnmt3a','Dnmt3b','Tet1','Tet2']
out=[]
for g in GOI:
    v=genes.get(g)
    if not v: out.append((None,g,'NOT ON A COVERED CHROMOSOME',0,0)); continue
    c=v[0][0]; s=min(x[1] for x in v); e=max(x[2] for x in v)
    n=n_in(c,s,e); kb=(e-s)/1000
    out.append((n/max(kb,.5)*100,g,f"{c}:{s//1000}-{e//1000}kb",kb,n))
for d,g,l,kb,n in sorted(out,key=lambda x:(-1 if x[0] is None else x[0]),reverse=True):
    if d is None: print(f"{g:10s} {l}")
    else: print(f"{g:10s} {l:26s} {kb:6.0f}kb {n:4d} regions  {d:7.2f}/100kb  {d/dens:5.1f}x")
