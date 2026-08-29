import json,urllib.request,urllib.parse,time
def get(u):
    for _ in range(4):
        try: return urllib.request.urlopen(u,timeout=120).read().decode()
        except Exception: time.sleep(3)
    return ''
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
uids=open('uids.txt').read().split()
recs=[]
for i in range(0,len(uids),150):
    chunk=uids[i:i+150]
    u=E+'esummary.fcgi?'+urllib.parse.urlencode({'db':'gds','id':','.join(chunk),'retmode':'json'})
    try:
        d=json.loads(get(u))
        for k,v in d.get('result',{}).items():
            if k=='uids': continue
            recs.append(dict(acc=v.get('accession',''),title=v.get('title',''),
                             summary=(v.get('summary','') or '')[:600],
                             org=v.get('taxon',''),n=v.get('n_samples',0),
                             gdstype=v.get('gdstype',''),pdat=v.get('pdat','')))
    except Exception as e: print('chunk err',e)
    time.sleep(0.4)
recs=[r for r in recs if r['acc'].startswith('GSE')]
json.dump(recs,open('recs.json','w'),indent=1)
print('series fetched:',len(recs))
