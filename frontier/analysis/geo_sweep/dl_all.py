import json,os,urllib.request,gzip,re,sys
from concurrent.futures import ThreadPoolExecutor
recs=json.load(open('recs.json'))
os.makedirs('mat',exist_ok=True)
def one(r):
    a=r['acc']
    o='mat/%s.txt'%a
    if os.path.exists(o): return ('have',a)
    n=re.sub(r'\d{1,3}$','nnn',a)
    for suf in ['_series_matrix.txt.gz','-GPL_series_matrix.txt.gz']:
        u="https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/matrix/%s%s"%(n,a,a,suf)
        try:
            d=urllib.request.urlopen(u,timeout=120).read()
            if d[:2]==b'\x1f\x8b': d=gzip.decompress(d)
            open(o,'wb').write(d); return ('ok',a)
        except Exception as e: pass
    # multi-platform: list dir
    try:
        idx=urllib.request.urlopen("https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/matrix/"%(n,a),timeout=120).read().decode('utf8','replace')
        fs=re.findall(r'href="([^"]*series_matrix\.txt\.gz)"',idx)
        if fs:
            d=urllib.request.urlopen("https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/matrix/%s"%(n,a,fs[0]),timeout=120).read()
            if d[:2]==b'\x1f\x8b': d=gzip.decompress(d)
            open(o,'wb').write(d); return ('ok-multi',a)
    except Exception: pass
    return ('miss',a)
with ThreadPoolExecutor(12) as ex: res=list(ex.map(one,recs))
from collections import Counter
print(Counter(x[0] for x in res))
json.dump([x[1] for x in res if x[0]=='miss'],open('miss.json','w'))
