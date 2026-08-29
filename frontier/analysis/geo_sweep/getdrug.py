import json,os,re,urllib.request,gzip
from concurrent.futures import ThreadPoolExecutor
ACC=['GSE168763','GSE71422','GSE222616','GSE138102','GSE280605','GSE280606','GSE91395','GSE73966',
     'GSE74036','GSE78102','GSE35218','GSE35506','GSE108223','GSE297702','GSE104473','GSE1371',
     'GSE1685','GSE260749','GSE262132','GSE196583','GSE103309','GSE199377','GSE114679','GSE246390',
     'GSE225878','GSE225879','GSE148069','GSE17589','GSE202559','GSE140394','GSE213292','GSE33624']
def one(a):
    if os.path.exists('mat/%s.txt'%a) and os.path.getsize('mat/%s.txt'%a)>1000: return 'have'
    n=re.sub(r'\d{1,3}$','nnn',a)
    for suf in ['_series_matrix.txt.gz']:
        try:
            d=urllib.request.urlopen("https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/matrix/%s%s"%(n,a,a,suf),timeout=180).read()
            if d[:2]==b'\x1f\x8b': d=gzip.decompress(d)
            open('mat/%s.txt'%a,'wb').write(d); return 'ok'
        except Exception: pass
    return 'miss'
with ThreadPoolExecutor(8) as ex: r=list(ex.map(one,ACC))
from collections import Counter;print(Counter(r))
# suppl listings + downloads for empties
def sup(a):
    n=re.sub(r'\d{1,3}$','nnn',a)
    try:
        h=urllib.request.urlopen("https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/suppl/"%(n,a),timeout=120).read().decode('utf8','replace')
        return a,[f for f in re.findall(r'href="([^"/][^"]*)"',h) if not f.endswith('/')]
    except Exception: return a,[]
with ThreadPoolExecutor(8) as ex: S=dict(ex.map(sup,ACC))
old=json.load(open('suppl.json')); old.update(S); json.dump(old,open('suppl.json','w'))
for a,fs in S.items(): print(a,fs[:5])
