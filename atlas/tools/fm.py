import json, urllib.parse, urllib.request, os, sys, time
SP = "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad"
refs = json.load(open(SP + "/refs.json"))
pmids = sorted({str(v['pmid']) for v in refs.values() if v.get('pmid')})
out = {}
if os.path.exists(SP + "/epmc_meta.json"):
    out = json.load(open(SP + "/epmc_meta.json"))
todo = [p for p in pmids if p not in out]
B = 40
for i in range(0, len(todo), B):
    chunk = todo[i:i + B]
    q = " OR ".join("EXT_ID:%s" % p for p in chunk)
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
        {"query": q, "format": "json", "pageSize": str(B * 2), "resultType": "core"})
    r = None
    for attempt in range(4):
        try:
            r = json.load(urllib.request.urlopen(url, timeout=90))
            break
        except Exception as ex:
            print("retry", i, ex, flush=True); time.sleep(3)
    if r is None:
        continue
    for res in r.get("resultList", {}).get("result", []):
        pid = res.get("pmid")
        if not pid:
            continue
        out[pid] = {"pmcid": res.get("pmcid"), "oa": res.get("isOpenAccess"),
                    "inepmc": res.get("inEPMC"), "title": res.get("title"),
                    "abstract": res.get("abstractText") or "",
                    "journal": (res.get("journalInfo") or {}).get("journal", {}).get("title"),
                    "year": res.get("pubYear")}
    print(i, len(out), flush=True)
    json.dump(out, open(SP + "/epmc_meta.json", "w"))
json.dump(out, open(SP + "/epmc_meta.json", "w"))
print("done", len(out), "of", len(pmids))
