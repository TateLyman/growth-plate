import json, urllib.parse, urllib.request, time

SEL = [
 # (layer, doi)
 ('L0','10.1016/j.jot.2026.101123'),
 ('L0','10.1038/s41598-026-46913-z'),
 ('L0','10.1038/s41467-026-71952-5'),
 ('L1','10.3390/ijms27073324'),
 ('L1','10.1016/j.bone.2026.117913'),
 ('L2','10.1016/j.bone.2026.117980'),
 ('L2','10.1002/advs.75725'),
 ('L3','10.1016/j.jbc.2026.113111'),
 ('L4','10.1016/j.molmet.2026.102355'),
 ('L5','10.1016/j.jbc.2026.111459'),
]
# main picks assembled by title match from candidates/supp
TITLE_PICKS = [
 ('L0','Xp22.33 Duplication'),
 ('L0','Ubiquitin-specific protease 26'),
 ('L1','adrenoceptor signaling in chondrocytes'),
 ('L1','Prepubertal blue light exposure'),
 ('L1','Modeling the chondrocyte-derived osteoblasts'),
 ('L1','Multiple Metaphyseal Hole Creation'),
 ('L2','Inherent tissue homeostasis of the juvenile metaphysis'),
 ('L3','synonymous NPR2 variant causes acromesomelic'),
 ('L3','Dkk1 inhibition restores mandibular growth'),
 ('L3','KDM6A modulates'),
 ('L3','Palmitic Acid Alters Longitudinal Bone Growth'),
 ('L4','somapacitan enhances linear growth in girls with Turner'),
 ('L4','Growth Hormone Withdrawal in Mid-Puberty'),
 ('L4','Sex-specific hormonal rescue of bone growth in PAPPA2'),
 ('L4','Dose-response relationship between growth hormone treatment and the development of scoliosis'),
 ('L5','burosumab in infants with X-linked hypophosphataemia'),
 ('L5','Determinants of final height in X-linked hypophosphatemia'),
 ('L5','ENPP1 inhibition as a therapeutic approach'),
 ('L5','Treatment of Children and Adults With X-Linked Hypophosphatemia With Calcitriol Alone'),
 ('L6','Finite element analysis of the proximal femoral growth plate'),
 ('L6','Computational mechanobiological model combining epiphyseal'),
 ('L6','impact of physical activity on linear growth in children'),
 ('L7','Distal Phalangeal Physeal Closure Preceding Ossification'),
 ('L7','Analysis of pubertal height gain in post-menarche girls'),
 ('L7','Comparison Between Chronological and Bone Age at Menarche in Girls with Laron'),
 ('L7','Determinants of pubertal progression and final height in premature pubarche'),
 ('L8','Genetics of skeletal proportions across two different populations'),
 ('L9','Real-World Outcomes of Vosoritide Treatment in Chinese Children'),
 ('L9','Prednisone, not vamorolone'),
 ('L9','Unlocking growth potential: Ivacaftor'),
 ('L9','Early Initiation of rhGH Therapy'),
 ('L10','Secular Trend and Socioeconomic Variation in Body Height of Young Polish Men'),
 ('L10','Long-term trends in height, weight and body mass index of children and adolescents in Macao'),
 ('L10','Trends in central precocious puberty incidence in Japan'),
 ('L11','Genomic inversion at 6p22.3'),
 ('L11','frameshift variants in the last exon of FGFR1'),
 ('L11','Karyotype-phenotype associations in turner syndrome'),
 ('L11','Genomic Insights into Short Stature in Children Born Small for Gestational Age'),
 ('L11','Biallelic Variants in MIMS1'),
 ('L11','Foramen Magnum Development in Patients with Achondroplasia'),
 ('L12','Effect of vosoritide on spine morphology'),
 ('L12','Adult Height After Growth Hormone and Aromatase Inhibitor Therapy'),
 ('L12','Efficacy and Safety of Somapacitan vs Daily Growth Hormone'),
 ('L12','Influence of long-acting growth hormone analogs on other hypothalamic'),
 ('L12','Transient gonadotropin suppression by exogenous testosterone'),
 ('L13','Dual-input deep learning bone age assessment'),
 ('L13','SITAR-d'),
 ('L13','Comparison of WHO and Centers for Disease Control and Prevention Growth References'),
 ('L13','Identifying developmental vulnerability through linear growth screening'),
]

EXTRA_DOI = [
 ('L8','10.1016/j.xhgg.2026.100597'),
 ('L8','10.1186/s13059-026-04140-9'),
 ('L8','10.1016/j.ajhg.2026.05.013'),
 ('L8','10.1016/j.ajcnut.2026.101425'),
 ('L8','10.1038/s41586-026-10358-1'),
]

pool = {}
for f in ['candidates.json','supp.json']:
    d = json.load(open('/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad/'+f))
    for L, rs in d.items():
        for r in rs:
            pool[(r['doi'] or r['pmid'])] = r

def by_doi(doi):
    for k,v in pool.items():
        if v.get('doi')==doi: return v
    u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode(
        {'query':f'DOI:"{doi}"','format':'json','pageSize':1,'resultType':'core'})
    d=json.load(urllib.request.urlopen(u,timeout=60))
    rs=d['resultList']['result']
    time.sleep(0.5)
    if not rs: return None
    r=rs[0]
    return {'doi':(r.get('doi') or '').lower(),'pmid':str(r.get('pmid') or ''),
            'date':r.get('firstPublicationDate'),'title':r.get('title'),
            'journal':r.get('journalTitle'),'abstract':r.get('abstractText')}

def by_title(frag):
    for k,v in pool.items():
        if frag.lower() in (v.get('title') or '').lower(): return v
    return None

out=[]
miss=[]
for L,doi in SEL+EXTRA_DOI:
    r=by_doi(doi)
    if r: out.append((L,r))
    else: miss.append((L,doi))
for L,frag in TITLE_PICKS:
    r=by_title(frag)
    if r: out.append((L,r))
    else: miss.append((L,frag))

print('found',len(out),'missing',miss)
json.dump([{'layer':L,**r} for L,r in out],
          open('/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad/heldout.json','w'),indent=1)
