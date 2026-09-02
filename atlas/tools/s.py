import sys, json, urllib.parse, urllib.request
q = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv)>2 else 12
sort = sys.argv[3] if len(sys.argv)>3 else "CITED desc"
alen = int(sys.argv[4]) if len(sys.argv)>4 else 1200
url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
       + urllib.parse.quote(q) + f"&format=json&pageSize={n}&resultType=core&sort="+urllib.parse.quote(sort))
d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"growth-atlas/1.0"}), timeout=60).read().decode())
res = d.get("resultList",{}).get("result",[])
print(f"### HITS {d.get('hitCount')} shown {len(res)}")
for r in res:
    print("---")
    print("PMID:", r.get("pmid"), "| DOI:", r.get("doi"), "| YR:", r.get("pubYear"), "|", r.get("journalTitle"), "| cites:", r.get("citedByCount"))
    print("T:", r.get("title"))
    print("A:", (r.get("abstractText") or "")[:alen])
