import json,urllib.request,urllib.parse,collections,time,sys
def snps(gene):
    u=f"https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByGene?geneName={gene}&size=500"
    try:
        with urllib.request.urlopen(u,timeout=90) as f: d=json.load(f)
    except Exception as e: return []
    return sorted({x['rsId'] for x in d.get('_embedded',{}).get('singleNucleotidePolymorphisms',[])})
def assoc(rs):
    u=f"https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/{rs}/associations?projection=associationBySnp"
    for a in range(3):
        try:
            with urllib.request.urlopen(u,timeout=60) as f: return json.load(f).get('_embedded',{}).get('associations',[])
        except Exception: time.sleep(1)
    return []
WANT=['body height','bone mineral density','bone tissue density','bone density','estimated bone mineral density']
for gene in sys.argv[1:]:
    ss=snps(gene)
    print(f"\n{'='*70}\n{gene}: {len(ss)} mapped SNPs")
    hits=collections.defaultdict(list)
    for rs in ss:
        for x in assoc(rs):
            tr=[t.get('trait','') for t in x.get('efoTraits',[])]
            if not any(any(w in (t or '').lower() for w in WANT) for t in tr): continue
            al=None
            for L in x.get('loci',[]):
                for sa in L.get('strongestRiskAlleles',[]): al=sa.get('riskAlleleName')
            hits[rs].append((tr,al,x.get('betaNum'),x.get('betaDirection'),x.get('pvalue')))
    both=[r for r,v in hits.items() if any('height' in ' '.join(t[0]).lower() for t in v)
                                   and any('bone' in ' '.join(t[0]).lower() for t in v)]
    for rs,v in sorted(hits.items()):
        mark=' <<< BOTH TRAITS' if rs in both else ''
        print(f"  {rs}{mark}")
        for tr,al,b,d,p in sorted(v,key=lambda z:z[4] or 1):
            print(f"      {str(tr)[:44]:46s} allele={al} beta={b} {d} p={p:.2g}")
