import sys, json, urllib.parse, urllib.request
for pm in sys.argv[1:]:
    q=f"EXT_ID:{pm} AND SRC:MED"
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode({"query":q,"format":"json","pageSize":1,"resultType":"core"})
    d=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"growth-atlas/1.0"}),timeout=60).read())
    rl=d.get("resultList",{}).get("result",[])
    if not rl: print(pm,"NOT FOUND"); continue
    r=rl[0]
    print("=====",pm,"|",r.get("pubYear"),"| PMCID",r.get("pmcid"),"| OA",r.get("isOpenAccess"))
    print("T:",r.get("title"))
    print("A:",(r.get("abstractText") or "NO ABSTRACT")[:2500])
