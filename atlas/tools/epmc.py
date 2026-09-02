import sys, json, urllib.parse, urllib.request
q = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv)>2 else 20
url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
       + urllib.parse.quote(q) + f"&format=json&pageSize={n}&resultType=core")
d = json.load(urllib.request.urlopen(url, timeout=60))
print("HITS:", d.get("hitCount"))
for r in d["resultList"]["result"]:
    print("---")
    print("PMID:", r.get("pmid"), "| PMCID:", r.get("pmcid"), "| OA:", r.get("isOpenAccess"), "|", r.get("pubYear"))
    print("T:", r.get("title"))
    print("J:", (r.get("journalInfo") or {}).get("journal",{}).get("title"))
    ab = (r.get("abstractText") or "").replace("\n"," ")
    print("A:", ab[:1100])
