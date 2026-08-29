import json,urllib.request,time
T={
 'Acan':      ('chr7',79053225,79115099),
 'Cyp19a1':   ('chr9',54165936,54268164),
 'Dnmt1':     ('chr9',20907205,20959888),
 'Igf2_H19':  ('chr7',142575529,142670000),
 'Cdkn1c':    ('chr7',143455000,143465000),
 'Peg3':      ('chr7',6705959,6730419),
 'Mkrn3':     ('chr7',62415000,62422000),
 'Hhip':      ('chr8',79965850,80058008),
 'Gpc3':      ('chrX',52272426,52400000),
 'POS_Dlk1':  ('chr12',109452822,109463336),
 'POS_Meg3':  ('chr12',109540995,109571729),
 'POS_Nnat':  ('chr2',157555000,157567000),
 'NEG_desert':('chr12',60000000,60100000),
}
out={}
for name,(c,s,e) in T.items():
    url=f"https://api.genome.ucsc.edu/getData/sequence?genome=mm10;chrom={c};start={s};end={e}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url,timeout=120) as r:
                d=json.load(r); out[name]=d['dna']; break
        except Exception as ex:
            print(name,'retry',attempt,ex); time.sleep(3)
    print(f"{name:12s} {len(out.get(name,'')):>9,} bp")
json.dump(out,open('sra/targets.json','w'))
