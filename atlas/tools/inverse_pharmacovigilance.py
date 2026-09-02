#!/usr/bin/env python3
"""
inverse_pharmacovigilance.py
============================
FIND A DRUG BY WHAT HAPPENED TO PEOPLE, NOT BY WHETHER A RESEARCHER MEASURED A BONE.

THE PROBLEM THIS EXISTS TO FIX
    Every compound sweep in this atlas has been shaped like "query X AND bone length
    endpoint". R302 ruled that a missing length endpoint is a GAP and not a
    disqualification, and the ledger still carries eight instances of "no length endpoint
    in any species" of which six sit beside a kill word. But the deeper damage is not the
    disposal - it is the SEARCH. Nobody was trying to make people taller, so nobody
    measured length, so a length-endpoint filter returns near-nothing BY CONSTRUCTION. It
    can only ever find agents whose developers already wanted what we want.

    Serendipitous effects are not found that way. Minoxidil, sildenafil, thalidomide and
    the GLP-1 agonists were all found because something unexpected happened to patients and
    somebody noticed. The instrument for that is pharmacovigilance, and this atlas has one
    passing FAERS reference and no query.

WHAT IT DOES
    Queries openFDA's FAERS endpoint for growth-related MedDRA preferred terms in BOTH
    directions and computes a proper disproportionality statistic per drug:

        PRR = [a / n_drug] / [c / (N - n_drug)]        (proportional reporting ratio)
        ROR = (a/b) / (c/d)                            with a 95% CI

    where a = reports naming the drug AND the reaction, n_drug = all reports naming the
    drug, c = reports with the reaction but not the drug, N = all reports.

    Raw counts are useless here and the tool refuses to present them alone: aspirin,
    paracetamol, metformin and omeprazole head the unadjusted "Body height increased" list
    purely because they appear in an enormous number of reports overall.

TERMS THAT ACTUALLY EXIST IN FAERS (checked 2026-08-15; several obvious ones do not)
    FAVOURABLE   Growth accelerated (227) · Body height increased (485)
    ADVERSE      Growth retardation (3694) · Epiphyses premature fusion (295)
    ABSENT       "Accelerated growth", "Tall stature", "Bone growth abnormal" - zero records

HOW TO READ THE OUTPUT - AND THE OBJECTION IS LARGER THAN THE SIGNAL
    ⛔ CONFOUNDING BY INDICATION DOMINATES THE FAVOURABLE DIRECTION. Triptorelin,
      leuprolide and histrelin top the raw "Growth accelerated" list, and they are GnRH
      agonists given FOR precocious puberty - the growth term is the indication being
      reported, or the post-treatment rebound, not a drug effect. Somatropin and burosumab
      are there because they are growth drugs. Stimulants are there because those children
      are the ones whose height is measured at every visit.
    ⛔ CHANNELLING, NOTORIETY AND CO-REPORTING all inflate PRR, and FAERS has no
      denominator of exposure - it is a spontaneous reporting system, not a cohort.
    ⭐ SO THE OUTPUT IS A HYPOTHESIS GENERATOR AND NOTHING MORE. A high PRR on a drug with
      no plausible indication link is worth a literature check; it is not evidence of an
      effect. The honest use is to surface the unexpected NAME, then go and look.
    ⭐ THE ADVERSE DIRECTION IS THE MORE TRUSTWORTHY HALF. "Epiphyses premature fusion" is
      a specific radiological event nobody reports as an indication, so a disproportionate
      signal there is far less likely to be manufactured by channelling - and a drug that
      closes plates is a contraindication this file can act on immediately.

USAGE
    python3 atlas/tools/inverse_pharmacovigilance.py
    python3 atlas/tools/inverse_pharmacovigilance.py --term "Epiphyses premature fusion"
    python3 atlas/tools/inverse_pharmacovigilance.py --json atlas/data/round437/faers.json
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request

API = "https://api.fda.gov/drug/event.json"
FIELD = "patient.drug.openfda.generic_name.exact"

FAVOURABLE = ["Growth accelerated", "Body height increased"]
ADVERSE = ["Epiphyses premature fusion", "Growth retardation"]


def get(url: str, tries: int = 3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=40) as fh:
                return json.load(fh)
        except Exception:
            if i == tries - 1:
                return None
            time.sleep(2 * (i + 1))
    return None


def total_reports() -> int:
    """N - every report in the database, via a search that matches everything."""
    d = get(API + "?search=receivedate:[19890101+TO+20991231]&limit=1")
    return d["meta"]["results"]["total"] if d else 0


def reaction_total(term: str) -> int:
    d = get("%s?search=patient.reaction.reactionmeddrapt:%s&limit=1"
            % (API, urllib.parse.quote('"%s"' % term)))
    return d["meta"]["results"]["total"] if d else 0


def drugs_for_reaction(term: str, limit: int = 40):
    d = get("%s?search=patient.reaction.reactionmeddrapt:%s&count=%s&limit=%d"
            % (API, urllib.parse.quote('"%s"' % term), FIELD, limit))
    return [(r["term"], r["count"]) for r in d.get("results", [])] if d else []


def drug_total(drug: str) -> int:
    d = get("%s?search=%s:%s&limit=1"
            % (API, FIELD, urllib.parse.quote('"%s"' % drug)))
    return d["meta"]["results"]["total"] if d else 0


def stats(a: int, n_drug: int, n_reaction: int, N: int):
    """PRR and ROR with a 95% CI. Returns None if the cell counts are unusable."""
    b = n_drug - a
    c = n_reaction - a
    d = N - n_drug - c
    if min(a, b, c, d) <= 0:
        return None
    prr = (a / n_drug) / (c / (N - n_drug))
    ror = (a / b) / (c / d)
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    return dict(a=a, n_drug=n_drug, prr=round(prr, 2), ror=round(ror, 2),
                ror_lo=round(math.exp(math.log(ror) - 1.96 * se), 2),
                ror_hi=round(math.exp(math.log(ror) + 1.96 * se), 2))


def run(term: str, N: int, top: int, min_a: int):
    n_reaction = reaction_total(term)
    rows = []
    for drug, a in drugs_for_reaction(term):
        if a < min_a:
            continue
        nd = drug_total(drug)
        if not nd:
            continue
        st = stats(a, nd, n_reaction, N)
        if st:
            rows.append(dict(drug=drug, term=term, **st))
        time.sleep(0.2)
    # A signal is only interesting if the lower bound of the CI clears 1.
    rows.sort(key=lambda r: -r["ror_lo"])
    return n_reaction, rows[:top]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--term", action="append")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--min-a", type=int, default=4,
                    help="minimum co-reports; below this the CI is meaningless")
    ap.add_argument("--json")
    args = ap.parse_args()

    terms = args.term or (FAVOURABLE + ADVERSE)
    N = total_reports()
    if not N:
        print("openFDA unreachable", file=sys.stderr)
        sys.exit(1)
    print("FAERS INVERSE PHARMACOVIGILANCE  (hypothesis generator, not evidence)")
    print("  total reports in the database: %s\n" % f"{N:,}")

    out = {"N": N, "terms": {}}
    for term in terms:
        n_reaction, rows = run(term, N, args.top, args.min_a)
        direction = "FAVOURABLE" if term in FAVOURABLE else "ADVERSE"
        print("=" * 78)
        print("%s  -  %s   (%s reports carry this term)"
              % (term.upper(), direction, f"{n_reaction:,}"))
        print("  %-34s %5s %9s %7s %7s  %s"
              % ("DRUG", "a", "n_drug", "PRR", "ROR", "95% CI"))
        for r in rows:
            flag = "*" if r["ror_lo"] > 1 else " "
            print(" %s%-34s %5d %9d %7.1f %7.1f  %.1f-%.1f"
                  % (flag, r["drug"][:34], r["a"], r["n_drug"], r["prr"], r["ror"],
                     r["ror_lo"], r["ror_hi"]))
        print("  * = 95%% CI lower bound above 1\n")
        out["terms"][term] = dict(direction=direction, n_reaction=n_reaction, rows=rows)

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        json.dump(out, open(args.json, "w"), indent=1)
        print("written: %s" % args.json)


if __name__ == "__main__":
    main()
