#!/usr/bin/env python3
"""
Network verification of every reference in sources/bibliography.yaml.

This is the atlas's anti-fabrication gate. For each ref it:
  - resolves the PMID via NCBI ESummary and/or the DOI via Europe PMC
  - compares the STORED first_author surname and year against the RESOLVED record
  - flags mismatches (wrong year, wrong author, non-existent id) as FABRICATION_RISK
  - checks PubMed publication types for Retracted Publication / retraction notices
  - writes results back to sources/verification_report.yaml

A ref that cannot be resolved is not silently dropped: it is marked
status: unresolved so it shows up in the audit.

Usage:
  python3 atlas/tools/verify_refs.py                 # verify all
  python3 atlas/tools/verify_refs.py --only r0012    # single ref
  python3 atlas/tools/verify_refs.py --stale-only    # only refs never verified
"""
import os, sys, json, time, argparse, urllib.parse, urllib.request
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")
OUT = os.path.join(ROOT, "sources", "verification_report.yaml")

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
ESUM = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
UA = {"User-Agent": "growth-atlas-verifier/1.0 (research use)"}


def get(url, tries=3, timeout=30):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            if i == tries - 1:
                return {"__error__": str(e)}
            time.sleep(2 ** i)
    return {"__error__": "unreachable"}


def norm_author(s):
    if not s:
        return ""
    s = str(s).strip()
    # "Mizuhashi K" / "Mizuhashi, Koji" / "Mizuhashi" -> "mizuhashi"
    s = s.split(",")[0].strip()
    parts = s.split()
    if len(parts) > 1 and len(parts[-1]) <= 3 and parts[-1].isupper():
        parts = parts[:-1]                      # drop trailing initials
    return " ".join(parts).lower()


def resolve_pmid(pmid):
    url = f"{ESUM}?db=pubmed&id={urllib.parse.quote(str(pmid))}&retmode=json"
    d = get(url)
    if "__error__" in d:
        return {"status": "network_error", "detail": d["__error__"]}
    res = d.get("result", {})
    if str(pmid) not in res:
        return {"status": "not_found"}
    rec = res[str(pmid)]
    if rec.get("error"):
        return {"status": "not_found", "detail": rec["error"]}
    pubtypes = [p for p in rec.get("pubtype", [])]
    return {
        "status": "ok",
        "title": rec.get("title", ""),
        "year": (rec.get("pubdate", "") or "")[:4],
        "first_author": rec.get("sortfirstauthor", ""),
        "journal": rec.get("source", ""),
        "pubtypes": pubtypes,
        "retraction_flag": any("Retract" in p for p in pubtypes),
        "doi": next((a.get("value") for a in rec.get("articleids", [])
                     if a.get("idtype") == "doi"), None),
    }


def resolve_doi(doi):
    q = f'DOI:"{doi}"'
    url = f"{EPMC}?query={urllib.parse.quote(q)}&format=json&pageSize=1&resultType=core"
    d = get(url)
    if "__error__" in d:
        return {"status": "network_error", "detail": d["__error__"]}
    rl = d.get("resultList", {}).get("result", [])
    if not rl:
        return {"status": "not_found"}
    r = rl[0]
    return {
        "status": "ok",
        "title": r.get("title", ""),
        "year": str(r.get("pubYear", "")),
        "first_author": (r.get("authorString", "") or "").split(",")[0],
        "journal": r.get("journalInfo", {}).get("journal", {}).get("title", ""),
        "pmid": r.get("pmid"),
        "is_preprint": r.get("pubType", "").find("preprint") >= 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--stale-only", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.34)  # NCBI rate limit
    a = ap.parse_args()

    with open(BIB) as f:
        bib = yaml.safe_load(f) or {}
    refs = bib.get("refs", {})

    prior = {}
    if os.path.exists(OUT):
        with open(OUT) as f:
            prior = (yaml.safe_load(f) or {}).get("verified", {})

    report, counts = {}, {"ok": 0, "mismatch": 0, "unresolved": 0,
                          "no_identifier": 0, "retracted": 0, "skipped": 0}

    for rid, rv in refs.items():
        if a.only and rid != a.only:
            continue
        if a.stale_only and rid in prior and prior[rid].get("status") == "ok":
            report[rid] = prior[rid]; counts["skipped"] += 1; continue
        if not isinstance(rv, dict):
            continue

        pmid, doi = rv.get("pmid"), rv.get("doi")
        entry = {"stored_first_author": rv.get("first_author"),
                 "stored_year": rv.get("year"), "problems": []}

        if not pmid and not doi:
            if rv.get("url") or rv.get("accession"):
                entry["status"] = "no_identifier_manual"
                entry["problems"].append("url/accession only - verify by hand")
                counts["no_identifier"] += 1
            else:
                entry["status"] = "no_identifier"
                entry["problems"].append("no pmid/doi/url/accession")
                counts["no_identifier"] += 1
            report[rid] = entry
            continue

        res = resolve_pmid(pmid) if pmid else resolve_doi(doi)
        if res.get("status") != "ok" and doi and pmid:
            res = resolve_doi(doi)          # fall back to the other identifier
        time.sleep(a.sleep)

        entry["resolved"] = res
        if res.get("status") != "ok":
            entry["status"] = "unresolved"
            entry["problems"].append(f"could not resolve: {res.get('status')} "
                                     f"{res.get('detail','')}".strip())
            counts["unresolved"] += 1
            report[rid] = entry
            continue

        entry["resolved_title"] = res.get("title", "")[:160]
        entry["resolved_year"] = res.get("year")
        entry["resolved_first_author"] = res.get("first_author")

        sa, ra = norm_author(rv.get("first_author")), norm_author(res.get("first_author"))
        if sa and ra and sa != ra and not (sa in ra or ra in sa):
            entry["problems"].append(
                f"FABRICATION_RISK author mismatch: stored '{rv.get('first_author')}' "
                f"vs resolved '{res.get('first_author')}'")
        sy, ry = str(rv.get("year") or ""), str(res.get("year") or "")
        if sy and ry and sy != ry:
            # allow 1y epub/print drift, still record it
            try:
                drift = abs(int(sy) - int(ry))
            except ValueError:
                drift = 99
            msg = "year drift (epub/print?)" if drift == 1 else "FABRICATION_RISK year mismatch"
            entry["problems"].append(f"{msg}: stored {sy} vs resolved {ry}")
        if res.get("retraction_flag"):
            entry["problems"].append("RETRACTION-RELATED pubtype - check "
                                     "sources/retracted_or_disputed.md")
            counts["retracted"] += 1

        hard = [p for p in entry["problems"] if "FABRICATION_RISK" in p]
        entry["status"] = "mismatch" if hard else "ok"
        counts["mismatch" if hard else "ok"] += 1
        report[rid] = entry

    with open(OUT, "w") as f:
        yaml.safe_dump({"verified": report, "counts": counts}, f,
                       sort_keys=True, default_flow_style=False, width=100)

    print(json.dumps(counts, indent=2))
    bad = {k: v for k, v in report.items()
           if v.get("status") in ("mismatch", "unresolved", "no_identifier")}
    if bad:
        print(f"\n--- {len(bad)} refs need attention ---")
        for k, v in list(bad.items())[:40]:
            print(f"  {k} [{v['status']}]: {'; '.join(v.get('problems', []))}")
    return 1 if counts["mismatch"] else 0


if __name__ == "__main__":
    sys.exit(main())
