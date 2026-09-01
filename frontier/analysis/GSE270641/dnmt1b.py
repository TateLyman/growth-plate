import gzip,collections,bisect
regs=collections.defaultdict(list)
with open('b23/dnmt1.narrowPeak') as f:
    f.readline()
    for line in f:
        p=line.rstrip('\n').split('\t')
        if len(p)<5 or '_' in p[0]: continue
        regs[p[0]].append((int(p[1]),int(p[2]),float(p[4])))
for c in regs: regs[c].sort()

# genes of interest: Lui imprinted senescence network + branch levers
GOI={'Dlk1','Meg3','Rtl1','Meg8','Dio3','Mkrn3','Igf2','H19','Plagl1','Mest','Peg3','Grb10','Ndn',
     'Cdkn1c','Slc38a4','Mdk','Meis1','Gpc3','Zfp57','Peg10','Nnat','Sgce','Zim1',
     'Acan','Ccn2','Fgfr3','Igf1','Ihh','Hhip','Ptch1','Gli1','Sox9','Col2a1','Col10a1','Esr1','Cyp19a1',
     'Npr2','Nppc','Tsc1','Mtor','Kdm5a','Kdm5b','Ezh2','Dnmt1','Dnmt3a','Dnmt3b','Tet1','Tet2'}
loc=collections.defaultdict(list)
with gzip.open('mm10_refGene.txt.gz','rt') as f:
    for line in f:
        p=line.split('\t'); c,s,e,n=p[2],int(p[4]),int(p[5]),p[12]
        if '_' in c or n not in GOI: continue
        loc[n].append((c,s,e))
def span(n):
    v=loc.get(n)
    if not v: return None
    c=v[0][0]; return (c,min(x[1] for x in v),max(x[2] for x in v))
print(f"{'gene':10s} {'locus':28s} {'kb':>7s} {'regions':>8s} {'per 100kb':>10s}")
print("-"*70)
rows=[]
for g in sorted(GOI):
    sp=span(g)
    if not sp: continue
    c,s,e=sp; L=regs.get(c,[])
    n=sum(1 for rs,re,_ in L if re>s-5000 and rs<e+5000)
    kb=(e-s)/1000
    rows.append((n/max(kb,1)*100, g, f"{c}:{s}-{e}", kb, n))
# genome-wide density for comparison
tot=sum(len(v) for v in regs.values()); dens=tot/2.73e9*1e5
for d,g,l,kb,n in sorted(rows, reverse=True):
    flag='  <<<' if d>dens*2 else ''
    print(f"{g:10s} {l:28s} {kb:7.0f} {n:8d} {d:10.2f}{flag}")
print(f"\ngenome-wide density: {dens:.2f} regions per 100 kb")
