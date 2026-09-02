#!/usr/bin/env python3
"""
STANDING SURVEILLANCE — is every source still standing?

WHY THIS IS SEPARATE FROM verify_refs.py
`verify_refs.py` answers *does this source exist and is it the paper we think it is*.
That is the anti-fabrication gate and it passed on 1,005 references with zero mismatches
— while a withdrawn paper sat inside the graph carrying a chokepoint. CORR-004.

An anti-fabrication system built around EXISTENCE is silent about STANDING. Existence is
a fact about the past and does not change. Standing changes underneath a static
bibliography, which is exactly why this has to recur rather than run once.

WHAT IT CHECKS, per reference

  Europe PMC  publication types (Retracted Publication, Expression of Concern, ...) and
              the commentCorrectionList, which carries "Retraction in", "Erratum in",
              "Expression of concern in", "Comment in", "Republished in"
  Crossref    the `updated-by` relation, whose type vocabulary covers retraction,
              withdrawal, removal, partial_retraction, expression_of_concern,
              correction, erratum, new_edition, and — importantly — Crossref ingests the
              RETRACTION WATCH database, so this is Retraction Watch coverage without a
              separate subscription. wu2013's notice carries BOTH a publisher
              "withdrawal" and a retraction-watch "retraction" label; either alone would
              have been enough, and having both is what let CORR-004 be resolved
              precisely.
  PubPeer     requires a developer key (POST /v3/publications?devkey=...). If
              PUBPEER_DEVKEY is not set in the environment, every reference is recorded
              as `pubpeer: not_checked` and the summary says so. It is NEVER recorded as
              clean. An unchecked source must not look like a checked one.

SEVERITY, and why corrections are not waved through

  FATAL      retraction / withdrawal / removal / partial_retraction
             -> the claim cannot stand on this source. Trace the blast radius in
                audit/corrections.md and declare `retracted: true` on every key_ref.
  SERIOUS    expression_of_concern
             -> not a retraction, but the record is under challenge. Any claim above
                grade D resting solely on it must be re-examined.
  CHECK      correction / erratum / republication
             -> an erratum can silently change a FIGURE the atlas quotes a number from.
                These are listed with the affected node so a human can check the number,
                and are not auto-cleared.

Usage:
  python3 atlas/tools/standing.py                 # full sweep, writes the report
  python3 atlas/tools/standing.py --only wu2013
  python3 atlas/tools/standing.py --since 2026-08-05   # refs not checked since a date
  python3 atlas/tools/standing.py --report        # re-print from the stored report
"""
import os, sys, json, time, argparse, glob, urllib.parse, urllib.request
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")
OUT = os.path.join(ROOT, "sources", "standing_report.yaml")
UA = {"User-Agent": "growth-atlas-standing/1.0 (mailto:hello@tateprograms.com)"}

FATAL = {"retraction", "withdrawal", "removal", "partial_retraction"}
SERIOUS = {"expression_of_concern", "expression-of-concern"}
CHECK = {"correction", "erratum", "corrigendum", "new_edition", "republication"}

EPMC_TYPE_MAP = {
    "retraction in": "retraction", "retraction of": "retraction",
    "expression of concern in": "expression_of_concern",
    "expression of concern for": "expression_of_concern",
    "erratum in": "erratum", "erratum for": "erratum",
    "corrected and republished in": "republication",
    "republished in": "republication", "comment in": "comment",
    "comment on": "comment", "update in": "correction",
}


def jget(url, tries=3, timeout=40):
    for i in range(tries):
        try:
            with urllib.request.urlopen(
                    urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if i == tries - 1:
                return {"__error__": str(e)}
            time.sleep(1.5 * (i + 1))


def epmc_standing(pmid):
    if not pmid:
        return None
    q = urllib.parse.quote(f"EXT_ID:{pmid} AND SRC:MED")
    d = jget("https://www.ebi.ac.uk/europepmc/webservices/rest/search"
             f"?query={q}&resultType=core&format=json&pageSize=1")
    if "__error__" in d:
        return {"error": d["__error__"]}
    res = (d.get("resultList") or {}).get("result") or []
    if not res:
        return {"error": "no record"}
    r = res[0]
    pt = [str(x).lower() for x in (r.get("pubTypeList") or {}).get("pubType", [])]
    notices = []
    for c in (r.get("commentCorrectionList") or {}).get("commentCorrection", []):
        t = str(c.get("type") or "").strip().lower()
        notices.append({"type": EPMC_TYPE_MAP.get(t, t.replace(" ", "_")),
                        "raw": c.get("type"), "reference": c.get("reference"),
                        "id": c.get("id")})
    if any("retract" in x for x in pt):
        notices.append({"type": "retraction", "raw": "pubTypeList",
                        "reference": "publication type", "id": None})
    if any("expression of concern" in x for x in pt):
        notices.append({"type": "expression_of_concern", "raw": "pubTypeList",
                        "reference": "publication type", "id": None})
    return {"pubtypes": pt, "notices": notices}


def crossref_standing(doi):
    if not doi:
        return None
    d = jget("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if "__error__" in d:
        return {"error": d["__error__"]}
    m = d.get("message") or {}
    out = []
    for u in (m.get("updated-by") or []):
        out.append({"type": str(u.get("type") or "").lower(),
                    "label": u.get("label"), "source": u.get("source"),
                    "doi": u.get("DOI"),
                    "date": "-".join(str(x) for x in
                                     (u.get("updated") or {}).get("date-parts", [[]])[0])})
    return {"updated_by": out, "type": m.get("type")}


def pubpeer(dois):
    """POST /v3/publications with a devkey. Without a key, return None - and the caller
    records `not_checked`, never `clean`."""
    key = os.environ.get("PUBPEER_DEVKEY")
    if not key:
        return None
    try:
        body = json.dumps({"dois": list(dois)}).encode()
        req = urllib.request.Request(
            f"https://pubpeer.com/v3/publications?devkey={urllib.parse.quote(key)}",
            data=body, headers={**UA, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"__error__": str(e)}


def severity(notices):
    kinds = {n["type"] for n in notices}
    if kinds & FATAL:
        return "FATAL"
    if kinds & SERIOUS:
        return "SERIOUS"
    if kinds & CHECK:
        return "CHECK"
    return "OK"


def cited_by(rid):
    """Which nodes cite this reference - so a CHECK lands on a human with an address."""
    hits = []
    for p in glob.glob(os.path.join(ROOT, "nodes", "*", "*.yaml")):
        try:
            t = open(p).read()
        except Exception:
            continue
        if rid in t:
            hits.append(os.path.basename(p)[:-5])
    return sorted(hits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--since", help="re-check refs whose last standing check predates this")
    ap.add_argument("--sleep", type=float, default=0.2)
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()

    prior = {}
    if os.path.exists(OUT):
        prior = (yaml.safe_load(open(OUT)) or {}).get("refs", {})

    if a.report:
        summarise(prior)
        return 0

    refs = (yaml.safe_load(open(BIB)) or {}).get("refs", {})
    today = time.strftime("%Y-%m-%d")
    out = dict(prior)
    pubpeer_key = bool(os.environ.get("PUBPEER_DEVKEY"))

    todo = []
    for rid, rv in refs.items():
        if a.only and rid != a.only:
            continue
        if a.since and prior.get(rid, {}).get("checked", "0000-00-00") >= a.since:
            continue
        if isinstance(rv, dict):
            todo.append((rid, rv))
    print(f"checking standing for {len(todo)} references "
          f"(pubpeer {'enabled' if pubpeer_key else 'NOT CONFIGURED'})")

    for i, (rid, rv) in enumerate(todo, 1):
        pmid, doi = rv.get("pmid"), rv.get("doi")
        rec = {"checked": today, "pmid": pmid, "doi": doi, "notices": []}
        if not pmid and not doi:
            rec["status"] = "NO_IDENTIFIER"
            rec["note"] = ("non-indexed source (accession, regulatory label, registry "
                           "entry) - has no publication record that could carry a "
                           "notice, and is therefore UNCHECKABLE by this tool, not clean")
            out[rid] = rec
            continue
        e = epmc_standing(pmid) if pmid else None
        c = crossref_standing(doi) if doi else None
        time.sleep(a.sleep)
        notices = list((e or {}).get("notices") or [])
        for u in ((c or {}).get("updated_by") or []):
            notices.append({"type": u["type"], "raw": u.get("label"),
                            "reference": u.get("doi"), "source": u.get("source"),
                            "date": u.get("date")})
        # de-dup on (type, reference)
        seen, ded = set(), []
        for n in notices:
            k = (n["type"], str(n.get("reference")))
            if k in seen:
                continue
            seen.add(k); ded.append(n)
        rec["notices"] = ded
        rec["status"] = severity(ded)
        rec["pubpeer"] = "not_checked_no_devkey" if not pubpeer_key else "pending"
        if rec["status"] != "OK":
            rec["cited_by_nodes"] = cited_by(rid)
        out[rid] = rec
        if i % 100 == 0:
            print(f"  {i}/{len(todo)} ...", flush=True)

    counts = {}
    for r in out.values():
        counts[r.get("status", "?")] = counts.get(r.get("status", "?"), 0) + 1
    yaml.safe_dump({"checked": today,
                    "pubpeer_configured": pubpeer_key,
                    "counts": counts, "refs": out},
                   open(OUT, "w"), sort_keys=True, width=100, allow_unicode=True)
    summarise(out)
    return 0


def summarise(refs):
    counts = {}
    for r in refs.values():
        counts[r.get("status", "?")] = counts.get(r.get("status", "?"), 0) + 1
    print("\nSTANDING:", json.dumps(counts))
    for sev in ("FATAL", "SERIOUS", "CHECK"):
        rows = [(k, v) for k, v in sorted(refs.items()) if v.get("status") == sev]
        if not rows:
            continue
        print(f"\n=== {sev} ({len(rows)}) ===")
        for k, v in rows[:60]:
            kinds = sorted({n["type"] for n in v.get("notices", [])})
            nodes = v.get("cited_by_nodes") or []
            print(f"  {k:26s} {','.join(kinds):40s} "
                  f"cited on {len(nodes)} node(s): {', '.join(nodes[:4])}")
    if not any(r.get("pubpeer", "").startswith("not_checked") for r in refs.values()):
        return
    print("\nPubPeer: NOT CHECKED - PUBPEER_DEVKEY is not set in this environment. "
          "Every reference above is unchecked on PubPeer, not clean on PubPeer.")


if __name__ == "__main__":
    sys.exit(main())
