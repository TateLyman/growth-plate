import urllib.request,urllib.parse,json,time,re
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def get(u):
    for _ in range(4):
        try: return urllib.request.urlopen(u,timeout=90).read().decode()
        except Exception as e: time.sleep(3)
    return ''
Q=["growth plate injury regeneration","physeal injury","growth plate fracture","epiphyseal injury cartilage",
   "Wnt inhibition chondrocyte","beta-catenin cartilage knockout growth plate","porcupine inhibitor cartilage",
   "Foxa2 cartilage","resting zone chondrocyte injury","skeletal stem cell expansion bone",
   "cartilage regeneration stem cell expansion","bone fracture callus early time course",
   "Wnt inhibitor bone LGK974","tankyrase inhibitor bone","Dkk1 antibody bone","sclerostin antibody bone growth plate"]
seen={}
for q in Q:
    u=E+'esearch.fcgi?'+urllib.parse.urlencode({'db':'gds','term':q+' AND "gse"[Entry Type]','retmax':60,'retmode':'json'})
    try: ids=json.loads(get(u))['esearchresult']['idlist']
    except Exception: continue
    if not ids: continue
    su=E+'esummary.fcgi?'+urllib.parse.urlencode({'db':'gds','id':','.join(ids),'retmode':'json'})
    try: d=json.loads(get(su))
    except Exception: continue
    for k,v in d.get('result',{}).items():
        if k=='uids' or not isinstance(v,dict): continue
        acc=v.get('accession','')
        if not acc.startswith('GSE'): continue
        seen.setdefault(acc,{'t':v.get('title',''),'o':v.get('taxon',''),'n':v.get('n_samples',0),'q':[]})
        seen[acc]['q'].append(q)
    time.sleep(0.3)
print("unique GSE:",len(seen))
KEY=re.compile(r'growth plate|physe|epiphys|chondrocyte|cartilage|Wnt|beta-catenin|Foxa2|skeletal stem',re.I)
hits=[(a,v) for a,v in seen.items() if KEY.search(v['t'])]
print("keyword-relevant:",len(hits))
for a,v in sorted(hits,key=lambda x:-x[1]['n'])[:45]:
    print(f"{a:12s} n={v['n']:<4} {v['o'][:16]:16s} {v['t'][:105]}")
json.dump(seen,open("search2.json","w"))
