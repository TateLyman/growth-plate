import json,os,re,urllib.request,gzip
from concurrent.futures import ThreadPoolExecutor
A=json.load(open('drug_accs.json'))
def one(a):
    o='mat/%s.txt'%a
    if os.path.exists(o) and os.path.getsize(o)>1000: return 'have'
    n=re.sub(r'\d{1,3}$','nnn',a)
    try:
        d=urllib.request.urlopen("https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/matrix/%s_series_matrix.txt.gz"%(n,a,a),timeout=180).read()
        if d[:2]==b'\x1f\x8b': d=gzip.decompress(d)
        open(o,'wb').write(d); return 'ok'
    except Exception: return 'miss'
with ThreadPoolExecutor(10) as ex: r=list(ex.map(one,A))
from collections import Counter;print(Counter(r),flush=True)
