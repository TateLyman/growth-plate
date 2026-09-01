import collections,random,statistics as st
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
tot=sum(len(v) for v in regs.values()); cov=sum(CHR.values())
dens=tot/cov*1e5
print(f"Dnmt1-dependent regions: {tot} over {cov/1e6:.0f} Mb = {dens:.2f} per 100 kb\n")

# canonical Polycomb DNA-methylation-valley loci, mm10, all on covered chromosomes
T={
 'HoxA cluster':('chr6',52150000,52280000),
 'HoxB cluster':('chr11',96170000,96380000),
 'HoxC cluster':('chr15',102920000,103040000),
 'HoxD cluster':('chr2',74660000,74770000),
 'Hoxc13 (Heyn GOF hit)':('chr15',102920000,102935000),
 'Pax5 (Jackson 2026 hit)':('chr4',44520000,44710000),
 'Gata4':('chr14',63198000,63274000),
 'Nkx2-5':('chr17',26837000,26845000),
 'Wt1':('chr2',105110000,105180000),
 'Pax6':('chr2',105660000,105700000),
 'Six3':('chr17',85610000,85625000),
}
def n_in(c,s,e):
    return sum(1 for rs,re in regs.get(c,[]) if re>s and rs<e)
random.seed(5)
present=sorted(regs)
print(f"{'locus':26s} {'kb':>6s} {'obs':>4s} {'exp':>6s} {'fold':>6s} {'perm p':>9s}")
print('-'*66)
tot_o=0; tot_e=0
for name,(c,s,e) in T.items():
    W=e-s; obs=n_in(c,s,e)
    null=[]
    for _ in range(5000):
        cc=random.choices(present,weights=[CHR[x] for x in present])[0]
        st_=random.randint(3_000_000, CHR[cc]-W-3_000_000)
        null.append(n_in(cc,st_,st_+W))
    mu=st.mean(null)
    # depletion p: fraction of random windows with <= obs
    p=(sum(1 for x in null if x<=obs)+1)/(len(null)+1)
    tot_o+=obs; tot_e+=mu
    print(f"{name:26s} {W/1000:6.0f} {obs:4d} {mu:6.2f} {obs/mu if mu else 0:6.2f} {p:9.4f}")
print('-'*66)
print(f"{'ALL Polycomb DMV loci':26s} {'':6s} {tot_o:4d} {tot_e:6.2f} {tot_o/tot_e:6.2f}")
