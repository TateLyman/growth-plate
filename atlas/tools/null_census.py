"""Every reported human with complete loss of oestrogen SIGNAL or SYNTHESIS.

Two classes:
  ESR1 loss of function  - the receptor is gone; oestrogen cannot close the plate,
                           so these people CANNOT be stopped pharmacologically.
  CYP19A1 deficiency     - the ligand is gone; oestrogen replacement WORKS, so
                           these people ARE stopped, and their heights are censored.

The point of the census is that the second class's published heights are
observations at intervention, not endpoints - and the first class is the only place
an endpoint could ever be seen.
"""
import json, urllib.request, urllib.parse, time, re, sys
UA={"User-Agent":"growth-plate-atlas/1.0 (mailto:hello@tateprograms.com)"}
B="https://www.ebi.ac.uk/europepmc/webservices/rest/search"
def s(q, cap=200):
    out, cur = [], "*"
    while len(out) < cap:
        u=B+"?"+urllib.parse.urlencode({"query":q,"format":"json","pageSize":100,
                                        "cursorMark":cur,"resultType":"core"})
        try: d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read())
        except Exception as e: print("ERR",e,file=sys.stderr); break
        r=d.get("resultList",{}).get("result",[]); out.extend(r)
        nxt=d.get("nextCursorMark")
        if not r or nxt==cur: break
        cur=nxt; time.sleep(0.25)
    return out

QUERIES = {
 "CYP19A1_male": '(CYP19A1 OR "aromatase deficiency" OR "aromatase deficient") AND (male OR man OR boy OR men)',
 "CYP19A1_any":  '"aromatase deficiency" OR "congenital aromatase deficiency" OR "aromatase gene mutation"',
 "ESR1_lof":     '(ESR1 OR "estrogen receptor alpha" OR "oestrogen receptor alpha" OR "estrogen resistance" OR "estrogen insensitivity") AND (mutation OR variant OR "loss of function" OR resistance OR insensitivity) AND (patient OR case OR man OR woman OR proband)',
 "CYP17D":       '("17alpha-hydroxylase" OR "17-hydroxylase" OR "17,20-lyase" OR CYP17A1) AND (deficiency OR deficient) AND (height OR stature OR "bone age" OR growth)',
}
store={}
for k,q in QUERIES.items():
    r=s(q)
    for x in r:
        i=x.get("id")
        if i: store.setdefault(i,{"rec":x,"found_by":[]})["found_by"].append(k)
    print(f"{k}: {len(r)} hits, cumulative unique {len(store)}", flush=True)
json.dump({k:{"pmid":v["rec"].get("pmid"),"pmcid":v["rec"].get("pmcid"),"yr":v["rec"].get("pubYear"),
              "title":v["rec"].get("title"),"journal":v["rec"].get("journalTitle"),
              "oa":v["rec"].get("isOpenAccess"),"auth":v["rec"].get("authorString","")[:90],
              "abs":v["rec"].get("abstractText") or "", "found_by":v["found_by"]}
           for k,v in store.items()}, open("null_census.raw.json","w"))
print(f"\n{len(store)} unique records")
