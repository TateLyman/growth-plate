#!/usr/bin/env python3
"""
Add a reference to sources/bibliography.yaml by fetching its CANONICAL metadata
from Europe PMC / NCBI. Authors, years, titles and journals are never typed from
memory - they are written by this script from the resolved record.

This is a design decision, not a convenience: if a PMID does not exist, this
script refuses to create the entry, so a fabricated citation cannot enter the
atlas in the first place.

Usage:
  python3 atlas/tools/addref.py --pmid 30356214 --tier T1 --type primary
  python3 atlas/tools/addref.py --doi 10.1038/s41586-018-0662-5 --tier T1 --type primary
  python3 atlas/tools/addref.py --pmid 12345 --finding "CNP raises cGMP in PZ"
  python3 atlas/tools/addref.py --batch pmids.txt --tier T1 --type primary
  python3 atlas/tools/addref.py --manual --ref-id fda_vosoritide_2021 \
      --url https://... --title "..." --tier T2 --type regulatory --year 2021 \
      --first-author "FDA CDER"

Prints the assigned ref_id(s) to stdout for immediate use in node files.
"""
import os, sys, json, time, argparse, urllib.parse, urllib.request, re
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")  # overridable via --bib (sharding)
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
UA = {"User-Agent": "growth-atlas/1.0 (research use)"}


def get(url, tries=3, timeout=30):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA),
                                        timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if i == tries - 1:
                return {"__error__": str(e)}
            time.sleep(2 ** i)
    return {"__error__": "unreachable"}


def epmc_lookup(pmid=None, doi=None):
    if pmid:
        q = f"EXT_ID:{pmid} AND SRC:MED"
    else:
        q = f'DOI:"{doi}"'
    d = get(f"{EPMC}?query={urllib.parse.quote(q)}&format=json&pageSize=1&resultType=core")
    if "__error__" in d:
        return None, d["__error__"]
    rl = d.get("resultList", {}).get("result", [])
    if not rl:
        return None, "not found in Europe PMC"
    return rl[0], None


def slug(author, year, extra=""):
    a = re.sub(r"[^a-z]", "", (author or "anon").split()[0].lower())[:14] or "anon"
    return f"{a}{year or 'nd'}{extra}"


def load_bib():
    if os.path.exists(BIB):
        with open(BIB) as f:
            b = yaml.safe_load(f) or {}
    else:
        b = {}
    b.setdefault("refs", {})
    return b


def save_bib(b):
    with open(BIB, "w") as f:
        yaml.safe_dump(b, f, sort_keys=True, default_flow_style=False,
                       width=120, allow_unicode=True)


def add_one(bib, pmid=None, doi=None, tier=None, rtype=None, finding=None,
            note=None, force_id=None):
    rec, err = epmc_lookup(pmid=pmid, doi=doi)
    if err:
        return None, f"REFUSED (id does not resolve): {err}"

    first_author = (rec.get("authorString", "") or "").split(",")[0].strip()
    year = str(rec.get("pubYear", "") or "")
    got_pmid = rec.get("pmid") or (str(pmid) if pmid else None)
    got_doi = rec.get("doi") or doi

    # de-dupe on pmid/doi
    for rid, rv in bib["refs"].items():
        if got_pmid and str(rv.get("pmid")) == str(got_pmid):
            return rid, "already present (pmid)"
        if got_doi and rv.get("doi") == got_doi:
            return rid, "already present (doi)"

    rid = force_id or slug(first_author, year)
    base, i = rid, 1
    while rid in bib["refs"]:
        i += 1
        rid = f"{base}{chr(ord('a') + i - 2)}"

    is_preprint = "preprint" in (rec.get("pubType", "") or "").lower()
    entry = {
        "ref_id": rid,
        "first_author": first_author,
        "year": int(year) if year.isdigit() else year,
        "title": rec.get("title", "").strip().rstrip("."),
        "journal": (rec.get("journalInfo", {}) or {}).get("journal", {}).get("title")
                   or rec.get("bookOrReportDetails", {}).get("publisher") or "",
        "pmid": got_pmid,
        "doi": got_doi,
        "tier": tier or ("T6" if is_preprint else None),
        "type": rtype or ("preprint" if is_preprint else None),
        "is_preprint": is_preprint,
        "open_access": rec.get("isOpenAccess") == "Y",
        "has_full_text": rec.get("hasTextMinedTerms") == "Y" or rec.get("inEPMC") == "Y",
        "cited_by": rec.get("citedByCount"),
        "added": time.strftime("%Y-%m-%d"),
    }
    if finding:
        entry["one_line_finding"] = finding
    if note:
        entry["note"] = note
    bib["refs"][rid] = entry
    return rid, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pmid"); ap.add_argument("--doi")
    ap.add_argument("--batch", help="file with one pmid or doi per line")
    ap.add_argument("--tier"); ap.add_argument("--type", dest="rtype")
    ap.add_argument("--finding"); ap.add_argument("--note")
    ap.add_argument("--ref-id")
    ap.add_argument("--manual", action="store_true",
                    help="add a non-indexed source (regulatory doc, dataset, patent)")
    ap.add_argument("--url"); ap.add_argument("--title")
    ap.add_argument("--year"); ap.add_argument("--first-author")
    ap.add_argument("--accession")
    ap.add_argument("--bib", help="write to this bibliography shard instead of the canonical file")
    a = ap.parse_args()

    global BIB
    if a.bib:
        BIB = a.bib if os.path.isabs(a.bib) else os.path.join(ROOT, "sources", "shards", a.bib)
        os.makedirs(os.path.dirname(BIB), exist_ok=True)

    bib = load_bib()

    if a.manual:
        if not a.ref_id or not (a.url or a.accession) or not a.title:
            print("manual mode needs --ref-id, --title, and --url or --accession")
            return 2
        bib["refs"][a.ref_id] = {
            "ref_id": a.ref_id, "first_author": a.first_author or "",
            "year": int(a.year) if (a.year or "").isdigit() else a.year,
            "title": a.title, "url": a.url, "accession": a.accession,
            "tier": a.tier, "type": a.rtype,
            "verify_by_hand": True, "added": time.strftime("%Y-%m-%d"),
        }
        if a.finding:
            bib["refs"][a.ref_id]["one_line_finding"] = a.finding
        save_bib(bib)
        print(f"OK {a.ref_id} (manual - flagged verify_by_hand)")
        return 0

    targets = []
    if a.batch:
        with open(a.batch) as f:
            for line in f:
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                targets.append(("doi", s) if s.startswith("10.") else ("pmid", s))
    elif a.pmid:
        targets = [("pmid", a.pmid)]
    elif a.doi:
        targets = [("doi", a.doi)]
    else:
        print("need --pmid, --doi, --batch, or --manual")
        return 2

    ok = fail = 0
    for kind, val in targets:
        rid, err = add_one(bib, pmid=val if kind == "pmid" else None,
                           doi=val if kind == "doi" else None,
                           tier=a.tier, rtype=a.rtype, finding=a.finding,
                           note=a.note, force_id=a.ref_id if len(targets) == 1 else None)
        if rid is None:
            print(f"FAIL {kind}={val}: {err}"); fail += 1
        else:
            r = bib["refs"][rid]
            print(f"OK   {rid:22s} {r.get('first_author','')} {r.get('year','')} "
                  f"| {str(r.get('title',''))[:70]}"
                  + (f"  [{err}]" if err else ""))
            ok += 1
        time.sleep(0.2)

    save_bib(bib)
    print(f"\nadded/matched {ok}, refused {fail}; bibliography now {len(bib['refs'])} refs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
