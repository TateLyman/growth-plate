#!/usr/bin/env python3
"""Minimal Europe PMC / NCBI query helper. Never fabricates: prints what the API returns."""
import json,sys,urllib.parse,urllib.request

UA={'User-Agent':'height-frontier-research/0.1 (mailto:hello@tateprograms.com)'}

def epmc(q,n=10,synonym=False):
    url=("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
         +urllib.parse.quote(q)+f"&format=json&pageSize={n}&resultType=core&synonym={'true' if synonym else 'false'}")
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    d=json.load(r)
    return d.get('hitCount'),d.get('resultList',{}).get('result',[])

def show(q,n=10,abstract=0):
    hits,res=epmc(q,n)
    print(f"\n### QUERY: {q}\n### hitCount: {hits}")
    for r in res:
        print(f"- PMID {r.get('pmid','-')} | PMCID {r.get('pmcid','-')} | {r.get('pubYear')} | {r.get('journalTitle','')[:40]}")
        print(f"  {r.get('title','')[:300]}")
        if abstract and r.get('abstractText'):
            print("  ABS:",r['abstractText'][:abstract].replace('\n',' '))
    return hits,res

if __name__=='__main__':
    a=int(sys.argv[3]) if len(sys.argv)>3 else 0
    show(sys.argv[1], int(sys.argv[2]) if len(sys.argv)>2 else 10, a)
