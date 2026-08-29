import json,urllib.request,urllib.parse,time,sys
from concurrent.futures import ThreadPoolExecutor
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def get(u):
    for _ in range(5):
        try: return urllib.request.urlopen(u,timeout=120).read().decode()
        except Exception: time.sleep(4)
    return ''
Q=[ # zone / plate
 'growth plate','epiphyseal plate','resting zone chondrocyte','reserve zone chondrocyte','physis cartilage',
 'epiphyseal chondrocyte','growth plate senescence','growth plate closure','growth plate fusion',
 'chondrocyte hypertrophy','endochondral ossification','longitudinal bone growth','bone elongation',
 'proliferative zone chondrocyte','hypertrophic chondrocyte','perichondrium','groove of Ranvier',
 'secondary ossification center','epiphysis cartilage','tibial growth plate','femoral growth plate',
 # stem / progenitor
 'skeletal stem cell','chondroprogenitor','cartilage stem cell','PTHrP chondrocyte','Gli1 skeletal',
 'label retaining chondrocyte','slow cycling chondrocyte','quiescent chondrocyte','chondrocyte clonal',
 'Col2 lineage tracing cartilage','Acan lineage','Prx1 mesenchymal progenitor','Sox9 progenitor cartilage',
 # age / senescence
 'chondrocyte aging','cartilage aging','growth plate age','chondrocyte senescence','skeletal aging',
 'postnatal bone development time course','juvenile adult cartilage','catch-up growth',
 # endocrine / drugs
 'growth hormone cartilage','IGF-1 chondrocyte','estrogen growth plate','androgen growth plate',
 'glucocorticoid chondrocyte','dexamethasone cartilage','thyroid hormone growth plate',
 'aromatase inhibitor bone','CNP natriuretic chondrocyte','vosoritide','FGFR3 achondroplasia',
 'PTH1R cartilage','parathyroid hormone related peptide bone',
 # hedgehog / pathways
 'Indian hedgehog cartilage','sonic hedgehog limb','smoothened agonist','Gli chondrocyte',
 'Wnt chondrocyte','BMP chondrocyte','TGF-beta chondrocyte','Notch chondrocyte',
 # epigenetics / reprogramming
 'DNA methylation cartilage','chondrocyte methylome','partial reprogramming OSK','Yamanaka factors in vivo',
 'rejuvenation reprogramming skeletal','TET chondrocyte','DNMT cartilage','histone chondrocyte',
 # short stature / dysplasia / stature
 'skeletal dysplasia transcriptome','short stature gene expression','achondroplasia','chondrodysplasia',
 'height gene expression','body size selection mouse','dwarfism mouse growth plate',
 'brachymorphic','diastrophic dysplasia','enchondroma','Ollier','multiple hereditary exostoses',
 # sulfation / matrix / metabolism
 'proteoglycan sulfation cartilage','glycosaminoglycan chondrocyte','aggrecan cartilage',
 'chondrocyte metabolism glycolysis','hypoxia chondrocyte',
 # species / systems
 'zebrafish bone growth','chick growth plate','bovine growth plate','pig growth plate','human fetal cartilage',
 'organoid cartilage','iPSC chondrocyte','limb bud development',
]
def one(q):
    u=E+'esearch.fcgi?'+urllib.parse.urlencode({'db':'gds','term':q+' AND "gse"[Entry Type]','retmax':2000,'retmode':'json'})
    try:
        d=json.loads(get(u)); return q,d['esearchresult']['idlist']
    except Exception: return q,[]
ids=set()
with ThreadPoolExecutor(4) as ex:
    for q,n in ex.map(one,Q):
        ids|=set(n); print('%-40s %5d  (cum %d)'%(q,len(n),len(ids)),flush=True)
print('\nUNIQUE UIDs:',len(ids))
open('uids2.txt','w').write('\n'.join(sorted(ids)))
