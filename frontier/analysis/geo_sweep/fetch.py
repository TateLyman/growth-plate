import json,urllib.request,urllib.parse,time,sys
def get(url):
    for _ in range(4):
        try: return urllib.request.urlopen(url,timeout=90).read().decode()
        except Exception as e: time.sleep(3)
    return ''
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
queries=['growth plate','epiphyseal plate','resting zone chondrocyte','physis cartilage',
         'epiphyseal chondrocyte','growth plate senescence','chondrocyte hypertrophy',
         'endochondral ossification','skeletal stem cell cartilage','longitudinal bone growth']
ids=set()
for q in queries:
    u=E+'esearch.fcgi?'+urllib.parse.urlencode({'db':'gds','term':q+' AND "gse"[Entry Type]','retmax':300,'retmode':'json'})
    try:
        d=json.loads(get(u)); n=d['esearchresult']['idlist']; ids|=set(n); print('%-32s %4d'%(q,len(n)))
    except Exception as e: print(q,'ERR',e)
print('\nunique UIDs:',len(ids))
open('uids.txt','w').write('\n'.join(sorted(ids)))
