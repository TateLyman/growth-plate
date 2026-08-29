import json,urllib.request,time,re
GENES=['PTCH1','PTCH2','SMO','GLI1','GLI2','GLI3','HHIP','SUFU','IHH','SHH','BOC','CDON','GAS1','EVC','EVC2','RARG','CYP26B1','ALDH1A3','SFRP5','THBS1','DCN','ACAN','DNMT3A']
def get(u):
    for _ in range(3):
        try:
            return json.load(urllib.request.urlopen(u,timeout=60))
        except Exception as e:
            time.sleep(3)
    return None
out={}
for g in GENES:
    d=get(f"https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByGene?geneName={g}&size=500")
    snps=[s['rsId'] for s in (d or {}).get('_embedded',{}).get('singleNucleotidePolymorphisms',[])]
    ht=[];bmd=[];other=0;traits={}
    for rs in snps:
        a=get(f"https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/{rs}/associations?projection=associationBySnp")
        for A in (a or {}).get('_embedded',{}).get('associations',[]):
            for t in A.get('efoTraits',[]):
                nm=t.get('trait','')
                traits[nm]=traits.get(nm,0)+1
                if nm.lower()=='body height':
                    ht.append((rs,A.get('pvalue')))
                elif 'bone' in nm.lower() and 'density' in nm.lower():
                    bmd.append((rs,A.get('pvalue')))
    ht.sort(key=lambda x: x[1] if x[1] else 1)
    out[g]=dict(nsnp=len(snps),height=len(ht),bmd=len(bmd),top=ht[:3],
                traits=sorted(traits.items(),key=lambda x:-x[1])[:5])
    print(f"{g:10s} snps={len(snps):4d}  HEIGHT={len(ht):4d}  BMD={len(bmd):3d}  top={ht[:2]}")
json.dump(out,open('hh_gwas.json','w'),indent=1)
