#!/usr/bin/env python3
"""
MULTI-SOURCE LITERATURE SEARCH — the permanent fix for the corpora Europe PMC cannot see.

Europe PMC / PubMed are BIOMEDICAL indexes. They systematically under-cover:
  · animal science / livestock nutrition (J Anim Sci, Animal, Poult Sci, J Dairy Sci partly)
  · agricultural and veterinary journals
  · sports nutrition and exercise science
  · food science, feed science
  · theses, reports, conference proceedings

Sources here, all free, all key-less:
  OPENALEX  — 250M+ works, every discipline, full boolean + filters. The main fix.
  CROSSREF  — 150M+ DOIs, publisher metadata, good for journal-scoped sweeps.
  AGRIS     — FAO agricultural index; the livestock/feed literature Europe PMC misses.
  SEMSCHOL  — Semantic Scholar; good abstracts + citation graph.

Usage:
  python3 litsearch.py openalex "leucine AND bone length" 25
  python3 litsearch.py all "hydroxymethylbutyrate withers height" 15
"""
import json,sys,time,urllib.parse,urllib.request

UA={'User-Agent':'height-frontier/0.2 (mailto:hello@tateprograms.com)'}
def get(url,timeout=60,tries=5):
    last=None
    for i in range(tries):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout))
        except Exception as e:
            last=e
            code=getattr(e,'code',None)
            if code in (429,500,502,503,504):
                time.sleep(3*(i+1)); continue
            raise
    raise last

def openalex(q,n=25,extra=""):
    url=("https://api.openalex.org/works?search="+urllib.parse.quote(q)
         +f"&per-page={min(n,200)}&mailto=hello@tateprograms.com"+extra)
    d=get(url); out=[]
    for w in d.get('results',[]):
        inv=w.get('abstract_inverted_index')
        abst=""
        if inv:
            pos={}
            for word,ps in inv.items():
                for p in ps: pos[p]=word
            abst=" ".join(pos[k] for k in sorted(pos))
        out.append(dict(src='openalex',id=w.get('id'),doi=w.get('doi'),year=w.get('publication_year'),
            title=w.get('title'),venue=((w.get('primary_location') or {}).get('source') or {}).get('display_name'),
            cited=w.get('cited_by_count'),oa=(w.get('open_access') or {}).get('oa_url'),abstract=abst))
    return d.get('meta',{}).get('count'),out

def crossref(q,n=25):
    url="https://api.crossref.org/works?query="+urllib.parse.quote(q)+f"&rows={n}&mailto=hello@tateprograms.com"
    d=get(url); out=[]
    for w in d['message'].get('items',[]):
        out.append(dict(src='crossref',doi=w.get('DOI'),year=(w.get('issued',{}).get('date-parts') or [[None]])[0][0],
            title=(w.get('title') or [''])[0],venue=(w.get('container-title') or [''])[0],
            cited=w.get('is-referenced-by-count'),abstract=(w.get('abstract') or '')[:600]))
    return d['message'].get('total-results'),out

def semanticscholar(q,n=25):
    url=("https://api.semanticscholar.org/graph/v1/paper/search?query="+urllib.parse.quote(q)
         +f"&limit={min(n,100)}&fields=title,year,venue,abstract,externalIds,citationCount,openAccessPdf")
    d=get(url); out=[]
    for w in d.get('data',[]):
        out.append(dict(src='semscholar',year=w.get('year'),title=w.get('title'),venue=w.get('venue'),
            cited=w.get('citationCount'),doi=(w.get('externalIds') or {}).get('DOI'),
            pmid=(w.get('externalIds') or {}).get('PubMed'),
            oa=(w.get('openAccessPdf') or {}).get('url'),abstract=(w.get('abstract') or '')))
    return d.get('total'),out

def show(rows,total,label,abstract=0):
    print(f"\n### {label} — total {total}")
    for r in rows:
        pm=f" PMID {r['pmid']}" if r.get('pmid') else ""
        print(f"- {r.get('year')} | {str(r.get('venue'))[:46]}{pm}")
        print(f"  {str(r.get('title'))[:190]}")
        if r.get('doi'): print(f"  doi:{str(r['doi']).replace('https://doi.org/','')}  cited:{r.get('cited')}"
                               + (f"  OA:{r['oa'][:70]}" if r.get('oa') else ""))
        if abstract and r.get('abstract'): print(f"  ABS: {r['abstract'][:abstract]}")

if __name__=='__main__':
    mode=sys.argv[1]; q=sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 20
    a=int(sys.argv[4]) if len(sys.argv)>4 else 0
    if mode in ('openalex','all'):
        try: t,r=openalex(q,n); show(r,t,'OPENALEX',a)
        except Exception as e: print("openalex failed:",e)
    if mode in ('crossref','all'):
        try: t,r=crossref(q,n); show(r,t,'CROSSREF',a)
        except Exception as e: print("crossref failed:",e)
    if mode in ('semscholar','all'):
        try: t,r=semanticscholar(q,n); show(r,t,'SEMANTIC SCHOLAR',a)
        except Exception as e: print("semanticscholar failed:",e)
