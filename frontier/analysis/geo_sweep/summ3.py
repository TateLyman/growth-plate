import json,urllib.request,urllib.parse,time,sys
from concurrent.futures import ThreadPoolExecutor
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
ids=open('uids3.txt').read().split()
print('uids',len(ids))
def get(u,d=None):
    for _ in range(5):
        try: return urllib.request.urlopen(u,data=d,timeout=180).read().decode('utf8','replace')
        except Exception: time.sleep(4)
    return ''
def chunk(L,n):
    for i in range(0,len(L),n): yield L[i:i+n]
out={}
def one(c):
    d=urllib.parse.urlencode({'db':'gds','id':','.join(c),'retmode':'json'}).encode()
    t=get(E+'esummary.fcgi',d)
    try: j=json.loads(t)
    except Exception: return []
    r=[]
    for k in j.get('result',{}).get('uids',[]):
        x=j['result'][k]
        r.append(dict(acc=x.get('accession'),title=x.get('title',''),summary=x.get('summary',''),
                      org=x.get('taxon',''),n=x.get('n_samples',0),gdstype=x.get('gdstype',''),
                      pdat=x.get('pdat','')))
    return r
recs=[]
with ThreadPoolExecutor(3) as ex:
    for i,r in enumerate(ex.map(one,list(chunk(ids,300)))):
        recs+=r
        if i%3==0: print('  batch',i,len(recs),flush=True)
recs=[r for r in recs if r['acc'] and r['acc'].startswith('GSE')]
seen={};[seen.setdefault(r['acc'],r) for r in recs]
recs=list(seen.values())
json.dump(recs,open('recs3.json','w'))
print('SERIES:',len(recs))
