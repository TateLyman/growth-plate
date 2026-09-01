#!/usr/bin/env python3
"""
litfetch - legitimate literature discovery + retrieval for the growth-plate project.

Sources, all free and authorised:
  OpenAlex      - 250M works, full citation graph, no key needed
  Unpaywall     - locates legally-posted OA copies of paywalled DOIs
  Europe PMC    - abstracts + OA full text
  NCBI eutils   - PubMed, handles pre-1990 indexing well
  bioRxiv/medRxiv - preprints

Never touches shadow libraries.
"""
import json, sys, time, urllib.parse, urllib.request

UA = "growth-plate-research/1.0 (mailto:oa-contact@example.org)"

def _get(url, tries=3):
    for i in range(tries):
        try:
            r = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            return json.load(urllib.request.urlopen(r, timeout=60))
        except Exception as e:
            if i == tries-1: raise
            time.sleep(1.5*(i+1))

# ---------- OpenAlex: discovery + citation graph ----------
def oa_search(q, per_page=25, year_from=None, year_to=None, extra=None):
    f = []
    if year_from or year_to:
        f.append("publication_year:%s-%s" % (year_from or "", year_to or ""))
    if extra: f.append(extra)
    u = "https://api.openalex.org/works?search=%s&per-page=%d" % (urllib.parse.quote(q), per_page)
    if f: u += "&filter=" + urllib.parse.quote(",".join(f))
    return _get(u).get("results", [])

def oa_cited_by(openalex_id, per_page=50):
    """Everything that cites this work - the single best way to find follow-ups."""
    wid = openalex_id.rsplit("/",1)[-1]
    u = "https://api.openalex.org/works?filter=cites:%s&per-page=%d" % (wid, per_page)
    return _get(u).get("results", [])

def oa_refs(work):
    """What this work cites - finds the buried older primary sources."""
    out = []
    for rid in (work.get("referenced_works") or [])[:50]:
        try: out.append(_get(rid))
        except Exception: pass
    return out

def oa_by_doi(doi):
    return _get("https://api.openalex.org/works/https://doi.org/%s" % urllib.parse.quote(doi))

def fmt(w):
    loc = (w.get("primary_location") or {})
    src = ((loc.get("source") or {}).get("display_name") or "")[:34]
    oa  = (w.get("open_access") or {})
    pdf = oa.get("oa_url") or (loc.get("pdf_url") or "")
    ids = w.get("ids") or {}
    return "%s %-34s %-4s cites:%-5s %s%s" % (
        str(w.get("publication_year")), src, ("OA" if oa.get("is_oa") else "--"),
        w.get("cited_by_count"), (w.get("display_name") or "")[:96],
        ("\n        PDF: "+pdf) if pdf else "")

def show(ws, n=25):
    for w in ws[:n]: print("  " + fmt(w))

# ---------- Unpaywall: legal OA copy of a paywalled DOI ----------
def unpaywall(doi, email="oa-contact@example.org"):
    u = "https://api.unpaywall.org/v2/%s?email=%s" % (urllib.parse.quote(doi), email)
    d = _get(u)
    best = d.get("best_oa_location") or {}
    return {"is_oa": d.get("is_oa"), "title": d.get("title"),
            "pdf": best.get("url_for_pdf"), "landing": best.get("url"),
            "host": best.get("host_type"), "version": best.get("version"),
            "all": [(l.get("host_type"), l.get("url_for_pdf") or l.get("url")) for l in (d.get("oa_locations") or [])]}

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search": show(oa_search(" ".join(sys.argv[2:])))
    elif cmd == "cited": show(oa_cited_by(sys.argv[2]))
    elif cmd == "unpaywall": print(json.dumps(unpaywall(sys.argv[2]), indent=1))
