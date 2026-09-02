import json, urllib.parse, urllib.request, time, sys

ING = json.load(open('/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad/ingested.json'))
DOIS = set(ING['dois']); PMIDS = set(ING['pmids'])
CUT = '2026-02-01'
DATE = 'AND (FIRST_PDATE:[2026-02-01 TO 2026-12-31])'
NOREV = 'AND (PUB_TYPE:"Journal Article" NOT PUB_TYPE:"Review")'

QUERIES = {
 'L0': ['(limb bud OR "skeletal element" OR "cartilage anlage" OR mesenchymal condensation) AND (SOX9 OR chondrogenesis) AND human',
        '("secondary ossification center" OR "growth plate") AND (fetal OR embryonic) AND human'],
 'L1': ['("growth plate" OR physis) AND ("hypertrophic zone" OR "proliferative zone" OR "resting zone") AND (human OR patient)',
        '("growth plate") AND (histology OR morphometry OR "chondrocyte column")'],
 'L2': ['("growth plate" OR physis) AND ("skeletal stem cell" OR "progenitor" OR "lineage tracing" OR PTHrP)',
        '("resting zone" OR "borderline zone") AND (stem OR clonal)'],
 'L3': ['("growth plate" OR chondrocyte) AND (FGFR3 OR CNP OR NPR2 OR "Indian hedgehog" OR IHH OR PTHrP OR WNT OR BMP)',
        '(chondrocyte hypertrophy) AND (signaling OR signalling) AND (mTOR OR HIF OR RUNX2 OR SOX9)'],
 'L4': ['("growth hormone" OR IGF-1 OR IGF1) AND (stature OR "height velocity" OR "growth plate") AND (children OR child)',
        '(estrogen OR estradiol OR androgen OR thyroid OR glucocorticoid) AND (growth OR stature) AND (children OR puberty)'],
 'L5': ['("growth plate" OR cartilage) AND (mineralization OR "collagen X" OR COL2A1 OR aggrecan OR "extracellular matrix") AND (bone OR physis)',
        '(hypophosphatasia OR "X-linked hypophosphatemia" OR pyrophosphate OR ENPP1) AND (growth OR skeletal)'],
 'L6': ['("growth plate" OR physis) AND (mechanical OR loading OR compression OR "Hueter-Volkmann" OR stiffness)',
        '(bone growth) AND (physical activity OR mechanical loading) AND (children OR adolescent)'],
 'L7': ['("growth plate") AND (fusion OR closure OR senescence) AND (epiphys OR estrogen)',
        '("bone age" OR "skeletal maturity" OR "epiphyseal fusion") AND (adolescent OR puberty)'],
 'L8': ['(GWAS OR "genome-wide association" OR polygenic) AND (height OR stature)',
        '(heritability OR "polygenic score") AND (adult height OR stature)'],
 'L9': ['("growth velocity" OR "height velocity" OR "adult height" OR "final height") AND (longitudinal OR cohort) AND children',
        '("pubertal growth spurt" OR "peak height velocity") AND cohort'],
 'L10': ['(stunting OR "child growth" OR "height-for-age") AND (nutrition OR population OR secular trend)',
         '("secular trend" OR "population height") AND (adult height)'],
 'L11': ['(achondroplasia OR hypochondroplasia OR "SHOX deficiency" OR "Turner syndrome" OR "skeletal dysplasia") AND (growth OR height OR stature)',
         '("short stature" OR "tall stature") AND (variant OR mutation OR gene) AND (children OR cohort)'],
 'L12': ['(vosoritide OR infigratinib OR navepegritide OR TransCon OR "growth hormone" OR somapacitan OR lonapegsomatropin) AND (trial OR efficacy OR safety)',
         '(aromatase inhibitor OR letrozole OR anastrozole OR GnRH analog) AND (height OR growth) AND (trial OR children)'],
 'L13': ['("growth plate" OR chondrocyte) AND ("single-cell" OR "spatial transcriptomics" OR scRNA-seq OR organoid)',
         '(auxology OR "growth chart" OR "growth reference" OR "height measurement") AND (method OR model OR validation)'],
}

def search(q, n=60):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({
        'query': q, 'format':'json','pageSize':n,'resultType':'core','sort':'CITED desc'})
    for _ in range(3):
        try:
            return json.load(urllib.request.urlopen(url, timeout=60))
        except Exception as e:
            time.sleep(3)
    return {'resultList':{'result':[]},'hitCount':0}

out = {}
for layer, qs in QUERIES.items():
    out[layer] = []
    for base in qs:
        q = f'({base}) {DATE} {NOREV}'
        d = search(q)
        for r in d['resultList']['result']:
            doi = (r.get('doi') or '').lower().strip()
            pmid = str(r.get('pmid') or '').strip()
            if doi and doi in DOIS: continue
            if pmid and pmid in PMIDS: continue
            fpd = r.get('firstPublicationDate') or ''
            if fpd < CUT: continue
            if not r.get('abstractText'): continue
            out[layer].append({'doi':doi,'pmid':pmid,'date':fpd,'title':r.get('title'),
                'journal':r.get('journalTitle'),'abstract':r.get('abstractText'),
                'cited':r.get('citedByCount'),'type':r.get('pubTypeList',{}).get('pubType')})
        time.sleep(1)
    # dedupe
    seen=set(); dd=[]
    for r in out[layer]:
        k = r['doi'] or r['pmid']
        if k in seen: continue
        seen.add(k); dd.append(r)
    out[layer]=dd
    print(layer, len(dd), file=sys.stderr)

json.dump(out, open('/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad/candidates.json','w'), indent=1)
