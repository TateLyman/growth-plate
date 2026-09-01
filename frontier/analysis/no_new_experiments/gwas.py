import json,urllib.request,collections,time,sys
ids=sorted(set(open('rsids.txt').read().split()))
print("unique SNPs:",len(ids),flush=True)
res=[]
for i,r in enumerate(ids):
    u=f"https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/{r}/associations?projection=associationBySnp"
    for a in range(3):
        try:
            with urllib.request.urlopen(u,timeout=60) as f: d=json.load(f); break
        except Exception as e:
            if a==2: d={}
            time.sleep(1)
    for x in d.get('_embedded',{}).get('associations',[]):
        traits=[t.get('trait') for t in x.get('efoTraits',[])]
        loci=x.get('loci',[])
        ra=None
        for L in loci:
            for sa in L.get('strongestRiskAlleles',[]):
                ra=sa.get('riskAlleleName')
        res.append(dict(rs=r,traits=traits,beta=x.get('betaNum'),dir=x.get('betaDirection'),
                        unit=x.get('betaUnit'),or_=x.get('orPerCopyNum'),p=x.get('pvalue'),allele=ra))
    if i%40==0: print(f"  {i}/{len(ids)}",flush=True)
json.dump(res,open('gwas_assoc.json','w'))
print("associations:",len(res))
c=collections.Counter()
for x in res:
    for t in x['traits']: c[t]+=1
print("\nTOP TRAITS AT THE DNMT3A LOCUS:")
for t,n in c.most_common(45): print(f"  {n:4d}  {t}")
