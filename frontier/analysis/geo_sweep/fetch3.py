import json,urllib.request,urllib.parse,time
from concurrent.futures import ThreadPoolExecutor
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def get(u):
    for _ in range(5):
        try: return urllib.request.urlopen(u,timeout=120).read().decode()
        except Exception: time.sleep(4)
    return ''
Q=['UNC0638','UNC0642','G9a inhibitor','EHMT2 inhibitor','EHMT1 inhibitor','BIX-01294','A-366 G9a',
   'trichostatin A transcriptome','sodium butyrate transcriptome','valproic acid transcriptome',
   'romidepsin','vorinostat SAHA transcriptome','entinostat','CI-994 tacedinaline','HDAC inhibitor imprinted',
   'I-BET151','JQ1 BET inhibitor','GSK-J4 KDM6','DZNep EZH2','GSK126 EZH2 inhibitor',
   'topotecan transcriptome','irinotecan transcriptome','etoposide transcriptome','UBE3A unsilencing',
   'imprinted gene reactivation','loss of imprinting drug','Prader-Willi SNRPN reactivation',
   '5-azacytidine imprinted','decitabine imprinting','nicotinamide stem cell imprint',
   'imprinted gene network','Plagl1 Zac1','H19 ICR','IGF2 imprinting','Dlk1 Meg3 imprinted',
   'fracture callus time course','fracture healing transcriptome','distraction osteogenesis',
   'muscle satellite cell cardiotoxin regeneration imprinted','notexin regeneration Plagl1',
   'human growth plate','human epiphyseal cartilage age','human physis biopsy']
def one(q):
    u=E+'esearch.fcgi?'+urllib.parse.urlencode({'db':'gds','term':q+' AND "gse"[Entry Type]','retmax':800,'retmode':'json'})
    try:
        d=json.loads(get(u));return q,d['esearchresult']['idlist']
    except Exception: return q,[]
ids=set()
with ThreadPoolExecutor(4) as ex:
    for q,n in ex.map(one,Q):
        ids|=set(n);print('%-46s %5d  cum %d'%(q,len(n),len(ids)),flush=True)
open('uids3.txt','w').write('\n'.join(sorted(ids)))
print('UNIQUE:',len(ids))
