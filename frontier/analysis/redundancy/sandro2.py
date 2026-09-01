import urllib.request,urllib.parse,json,time,re
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def get(u):
    for a in range(5):
        try: return urllib.request.urlopen(u,timeout=120).read().decode()
        except Exception as e:
            if a==4: print("  ERR",e)
            time.sleep(4)
    return ''
Q=["androgen bone","testosterone bone","dihydrotestosterone","androgen receptor",
   "orchiectomy","castration bone","anabolic androgenic steroid","oxandrolone",
   "growth plate","chondrocyte","cartilage growth","SHOX","Turner syndrome"]
seen={}
for q in Q:
    u=E+'esearch.fcgi?'+urllib.parse.urlencode({'db':'gds','term':f'"{q}" AND "gse"[Entry Type]','retmax':120,'retmode':'json'})
    r=get(u)
    try: ids=json.loads(r)['esearchresult']['idlist']
    except Exception: print(f"  {q}: parse fail"); continue
    print(f"  {q:32s} {len(ids)} ids")
    if not ids: continue
    for i in range(0,len(ids),60):
        d=get(E+'esummary.fcgi?'+urllib.parse.urlencode({'db':'gds','id':','.join(ids[i:i+60]),'retmode':'json'}))
        try: d=json.loads(d)
        except Exception: continue
        for k,v in d.get('result',{}).items():
            if k=='uids' or not isinstance(v,dict): continue
            a=v.get('accession','')
            if a.startswith('GSE'):
                seen.setdefault(a,{'t':v.get('title',''),'s':v.get('summary','')[:300],'o':v.get('taxon',''),'n':v.get('n_samples',0)})
        time.sleep(0.34)
print(f"\nTOTAL unique GSE: {len(seen)}")
A=re.compile(r'androgen|testosterone|dihydrotest|\bDHT\b|orchiect|castrat|anabolic steroid|oxandrol|nandrolone|stanozolol',re.I)
S=re.compile(r'growth plate|chondrocyte|cartilage|physe|epiphys|tibia|femur|skelet|\bbone\b',re.I)
hits=[(a,v) for a,v in seen.items() if (A.search(v['t']+v['s']) and S.search(v['t']+v['s']))]
print(f"ANDROGEN x SKELETAL: {len(hits)}\n")
for a,v in sorted(hits,key=lambda x:-x[1]['n'])[:35]:
    print(f"{a:12s} n={v['n']:<4} {v['o'][:14]:14s} {v['t'][:98]}")
json.dump(seen,open("androgen_search2.json","w"))
