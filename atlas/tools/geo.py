import sys, json, urllib.parse, urllib.request, time
def esearch(q, n=25, db="gds"):
    u=("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db="+db+"&term="
       +urllib.parse.quote(q)+f"&retmax={n}&retmode=json")
    return json.load(urllib.request.urlopen(u,timeout=60))["esearchresult"]
def esummary(ids, db="gds"):
    u=("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db="+db+"&id="
       +",".join(ids)+"&retmode=json")
    return json.load(urllib.request.urlopen(u,timeout=60))["result"]
q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 25
r=esearch(q,n); print("COUNT:",r["count"])
ids=r["idlist"]
if ids:
    d=esummary(ids)
    for i in ids:
        v=d.get(i,{})
        print("---", v.get("accession"), "|", v.get("gdstype"), "| n=", v.get("n_samples"), "|", v.get("taxon"))
        print("  ", (v.get("title") or "")[:170])
