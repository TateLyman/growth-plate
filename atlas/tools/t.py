import sys, json, urllib.parse, urllib.request
for Q in sys.argv[1:]:
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode(
      {"query":Q,"format":"json","pageSize":4,"resultType":"lite"})
    try:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"growth-atlas/1.0"}),timeout=60).read())
    except Exception as e:
        print("ERR",Q,e); continue
    print("== ",Q," hits:",d.get("hitCount"))
    for r in d.get("resultList",{}).get("result",[])[:4]:
        print("   PMID",r.get("pmid"),"|",r.get("pubYear"),"|",r.get("authorString","")[:40],"|",r.get("title"))
