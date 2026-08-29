import json,os,re,urllib.request,gzip
from concurrent.futures import ThreadPoolExecutor
R=json.load(open('recs2.json'))
have={os.path.basename(f)[:-4] for f in os.listdir('mat')}
GP=re.compile(r'(growth plate|epiphys|physis|chondrocyt|cartilage|chondro|skeletal stem|endochondral|bone growth|limb bud|osteochondr)',re.I)
todo=[r for r in R if r['acc'] not in have and int(r['n'] or 0)>=4 and GP.search(r['title']+' '+r['summary'])]
print('to fetch:',len(todo),flush=True)
def one(r):
    a=r['acc']; n=re.sub(r'\d{1,3}$','nnn',a)
    for suf in ['_series_matrix.txt.gz']:
        try:
            d=urllib.request.urlopen("https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/matrix/%s%s"%(n,a,a,suf),timeout=120).read()
            if d[:2]==b'\x1f\x8b': d=gzip.decompress(d)
            open('mat/%s.txt'%a,'wb').write(d); return 'ok'
        except Exception: pass
    return 'miss'
with ThreadPoolExecutor(10) as ex: res=list(ex.map(one,todo))
from collections import Counter; print(Counter(res),flush=True)
