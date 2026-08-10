#!/usr/bin/env python3
"""
ROUND 229 - how many of the atlas's 252 `primary_abstract_only` refs are actually readable?

WHY THIS EXISTS. farouk2023 was filed abstract-only in round 45 with the reason recorded in
its note: PMC10957205 is an author manuscript and Europe PMC reports isOpenAccess N. That is
true of Europe PMC and FALSE OF THE ARTICLE - NCBI eutils `efetch db=pmc` returns the whole
author manuscript, Table 1 included. The atlas then spent rounds 216 to 228 reconstructing
from single case reports a growth dataset that was sitting inside a reference it already had.

The question this answers is therefore not about one paper. It is: HOW MANY OTHER TIMES?

Method, and it makes no claim beyond what it measures:
  1. take every ref typed `primary_abstract_only` that carries a PMID
  2. resolve PMID -> PMCID in Europe PMC, in batches, recording isOpenAccess
  3. for each one with a PMCID, ask NCBI eutils for the full text and see whether a
     substantial body comes back
A "recoverable" verdict means eutils returned a document with a real body. It does NOT mean
the paper answers anything - only that the atlas can read it and has not.

Writes atlas/data/round229/abstract_only_unlock.tsv.
"""

import json
import os
import re
import time
import urllib.parse
import urllib.request

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "sources", "bibliography.yaml")
OUT = os.path.join(HERE, "..", "data", "round229", "abstract_only_unlock.tsv")

UA = {"User-Agent": "growth-plate-atlas/1.0 (research; contact via repository)"}
BODY_MIN = 8000          # characters of stripped text below which it is a stub, not a paper


def fetch(url, timeout=90):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers=UA), timeout=timeout).read().decode("utf-8", "replace")


def epmc_batch(pmids):
    """PMID -> (pmcid, isOpenAccess) for up to ~40 pmids per call."""
    q = " OR ".join(f"EXT_ID:{p}" for p in pmids)
    u = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="
         + urllib.parse.quote(q) + "&format=json&pageSize=100&resultType=lite")
    out = {}
    try:
        d = json.loads(fetch(u))
    except Exception:
        return out
    for r in d.get("resultList", {}).get("result", []):
        out[str(r.get("pmid"))] = (r.get("pmcid"), r.get("isOpenAccess"))
    return out


def body_len(pmcid):
    """Characters of real text eutils returns for this PMCID, or 0."""
    num = re.sub(r"[^0-9]", "", pmcid or "")
    if not num:
        return 0
    try:
        x = fetch(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={num}&rettype=xml")
    except Exception:
        return 0
    if "<body" not in x and "<sec" not in x:
        return 0
    return len(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x)))


def main():
    bib = yaml.safe_load(open(BIB))["refs"]
    targets = {k: str(v.get("pmid")) for k, v in bib.items()
               if v.get("type") == "primary_abstract_only" and v.get("pmid")}
    print(f"{len(targets)} refs typed primary_abstract_only carry a PMID "
          f"(of {sum(1 for v in bib.values() if v.get('type') == 'primary_abstract_only')} total)")

    items = sorted(targets.items())
    resolved = {}
    for i in range(0, len(items), 40):
        chunk = [p for _k, p in items[i:i + 40]]
        resolved.update(epmc_batch(chunk))
        print(f"  resolved {min(i+40, len(items))}/{len(items)}", flush=True)
        time.sleep(0.5)

    rows, recoverable, no_pmc = [], 0, 0
    for k, pmid in items:
        pmcid, oa = resolved.get(pmid, (None, None))
        if not pmcid:
            no_pmc += 1
            rows.append((k, pmid, "-", str(oa), "0", "no PMC record"))
            continue
        n = body_len(pmcid)
        time.sleep(0.36)                       # NCBI: stay under 3 requests/second
        verdict = "RECOVERABLE" if n >= BODY_MIN else ("stub only" if n else "eutils empty")
        if verdict == "RECOVERABLE":
            recoverable += 1
        rows.append((k, pmid, pmcid, str(oa), str(n), verdict))
        print(f"  {k:<24}{pmcid or '-':<14}OA={str(oa):<5}{n:>8}  {verdict}", flush=True)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write("ref_id\tpmid\tpmcid\tepmc_isOpenAccess\tchars\tverdict\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")

    hidden = [r for r in rows if r[5] == "RECOVERABLE" and r[3] in ("N", "None", "False")]
    print("\n" + "=" * 78)
    print(f"  refs probed                                    {len(rows)}")
    print(f"  no PMC record at all - genuinely abstract-only  {no_pmc}")
    print(f"  FULL TEXT RECOVERABLE THROUGH EUTILS            {recoverable}")
    print(f"    of which Europe PMC calls NOT open access     {len(hidden)}  <- the blind spot")
    print("=" * 78)
    print("""
  THE BLIND SPOT IS THE NUMBER THAT MATTERS. Those are refs the atlas classified as
  unreadable on the strength of a Europe PMC flag, for which NCBI returns the entire
  paper. Every one is a source already judged relevant enough to cite, carrying tables
  and methods nobody here has looked at. farouk2023 was one of them, and it held a
  seven-patient growth dataset.

  RULE THIS ESTABLISHES: `primary_abstract_only` is a statement about a retrieval attempt,
  not a property of a paper, and it must never again be treated as the second thing. Any
  abstract-only ref that is about to carry a conclusion gets one eutils attempt first.
""")
    print(f"  written: {OUT}")


if __name__ == "__main__":
    main()
