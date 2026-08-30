import urllib.request,urllib.parse,json,sys
def q(query,n=8):
    u="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode(
        {"query":query,"format":"json","pageSize":n,"resultType":"core"})
    try:
        d=json.load(urllib.request.urlopen(u,timeout=60))
    except Exception as e:
        print("ERR",e); return
    print("### ",query," -> ",d.get("hitCount"))
    for r in d.get("resultList",{}).get("result",[])[:n]:
        ab=(r.get("abstractText") or "").replace("\n"," ")
        print("-",r.get("journalTitle"),r.get("pubYear"),"|",r.get("title"))
        print("   ",ab[:700])
    print()
for s in sys.argv[1:]: q(s)
