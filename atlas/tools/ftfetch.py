import json, os, urllib.request, time, re
SP = "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad"
CD = SP + "/ftcache"
os.makedirs(CD, exist_ok=True)
m = json.load(open(SP + "/epmc_meta.json"))
targets = sorted({v["pmcid"] for v in m.values() if v.get("pmcid")})
print("pmcids", len(targets), flush=True)
ok = 0
for i, p in enumerate(targets):
    f = os.path.join(CD, p + ".xml")
    if os.path.exists(f):
        ok += 1
        continue
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML" % p
    try:
        d = urllib.request.urlopen(url, timeout=60).read()
        if len(d) > 500:
            open(f, "wb").write(d)
            ok += 1
        else:
            open(f, "wb").write(b"")
    except Exception as ex:
        open(f, "wb").write(b"")
    if i % 25 == 0:
        print(i, ok, flush=True)
print("done", ok, "of", len(targets))
