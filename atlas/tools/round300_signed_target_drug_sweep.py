#!/usr/bin/env python3
"""
ROUND 300. The compound sweep, run against SIGNED human effect sizes.

WHY THIS IS DIFFERENT FROM ROUND 298. Round 298 swept 368 symbols from the atlas's own
ontology against Open Targets and reported how many had drugs. It could not say whether a
drug should be given, because the gene set carried no direction: the atlas nominated genes
because they were interesting, not because anyone knew which way to push them. CORR-295 is
the standing rule that an enumeration with no sign and no magnitude is not actionable, and
round 298 was exactly that enumeration.

kosmicki2026 Supplementary Table 6 removes the excuse. It reports, for all 207
genome-wide-significant genes, the burden effect in CENTIMETRES with a standard error and a
P-value, per variant class and per allele-frequency bin. Every gene therefore arrives with a
direction and a magnitude measured in 1.45M humans.

THE RULE THIS SCRIPT APPLIES. For each gene take the most significant pure-pLoF row, which
is the closest genetic analogue of pharmacological loss of function:
  beta > 0  loss of function makes humans TALLER  -> we want an INHIBITOR / ANTAGONIST /
            BLOCKER / DEGRADER. An approved inhibitor here is a candidate.
  beta < 0  loss of function makes humans SHORTER -> we want an AGONIST / ACTIVATOR /
            supply of the product. An approved INHIBITOR here is a CONTRAINDICATION, and
            the atlas has never run that screen in either direction.

CAVEATS CARRIED, NOT BURIED.
  - CORR-299: germline heterozygous loss from conception is not the same manipulation as
    inhibiting a protein in an open plate. This produces a TARGET list, not a prescription.
    The open-plate test still has to be run per gene.
  - CORR-310: this script does NOT filter on the paper's own 1.75e-9 gene-P threshold for
    the sub-tests. A burden row at P=9e-5 inside a gene that cleared gene-P is carried
    through and graded as what it is.
  - Mechanism-of-action strings come from Open Targets / ChEMBL and are matched by keyword.
    A keyword match is a triage step, not a reading of the drug label.

Usage:  python3 atlas/tools/round300_signed_target_drug_sweep.py
Writes: atlas/data/round300/signed_target_drug_table.json
        atlas/data/round300/signed_target_drug_table.tsv
"""
import json
import os
import sys
import time
import urllib.request

OT = "https://api.platform.opentargets.org/api/v4/graphql"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(HERE, "data", "round300")

INHIBIT_WORDS = ("inhibitor", "antagonist", "blocker", "negative modulator", "degrader",
                 "inverse agonist", "disrupting agent", "suppressor")
ACTIVATE_WORDS = ("agonist", "activator", "positive modulator", "stimulant", "opener",
                  "potentiator", "substitute", "replacement")

Q = """query($ids:[String!]!){targets(ensemblIds:$ids){
  id approvedSymbol
  tractability{label modality value}
  drugAndClinicalCandidates{count rows{drug{id name drugType maximumClinicalStage
    mechanismsOfAction{rows{actionType mechanismOfAction}}}}}
}}"""


def gql(query, variables, tries=4):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(OT, data=body,
                                 headers={"Content-Type": "application/json"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001 - network, retried
            if i == tries - 1:
                print("  ! %s" % e, file=sys.stderr)
                return None
            time.sleep(2 ** i)
    return None


def classify(action):
    a = (action or "").lower()
    if any(w in a for w in INHIBIT_WORDS):
        return "down"
    if any(w in a for w in ACTIVATE_WORDS):
        return "up"
    return "?"


def main():
    per_gene = json.load(open(os.path.join(OUTDIR, "s6_per_gene_direction.json")))
    ens = {}
    recs = json.load(open(os.path.join(OUTDIR, "s6_burden_effects.json")))
    # Ensembl IDs live in the S4/S6 extraction; re-read them from the workbook copy we kept.
    import openpyxl
    wb = openpyxl.load_workbook(
        os.path.join(HERE, "data", "supplied_2026_08_12",
                     "kosmicki2026_supp_tables_S1_S29.xlsx"), read_only=True)
    ws = wb["Table S4"]
    for r in list(ws.iter_rows(values_only=True))[2:]:
        if r and r[0] and r[1]:
            ens[str(r[0])] = str(r[1])

    genes = {g["gene"]: g for g in per_gene}
    ids = [ens[g] for g in genes if g in ens]
    print("resolving %d of %d genes to Ensembl IDs" % (len(ids), len(genes)))

    tmap = {}
    for i in range(0, len(ids), 25):
        chunk = ids[i:i + 25]
        d = gql(Q, {"ids": chunk})
        if not d or "data" not in d:
            print("  chunk %d failed" % i, file=sys.stderr)
            continue
        for t in d["data"]["targets"] or []:
            tmap[t["approvedSymbol"]] = t
        print("  %d/%d" % (min(i + 25, len(ids)), len(ids)))
        time.sleep(0.3)

    out = []
    for sym, info in genes.items():
        t = tmap.get(sym)
        beta = info.get("plof_eff")
        want = None
        if beta is not None:
            want = "down" if beta > 0 else "up"
        row = dict(gene=sym, plof_cm=beta, plof_p=info.get("plof_p"),
                   plof_aaf=info.get("plof_aaf"), plof_het=info.get("plof_het"),
                   any_cm=info.get("any_eff"), any_p=info.get("any_p"),
                   any_cat=info.get("any_cat"), omim=info.get("omim"),
                   want=want, resolved=bool(t), tractability=[], drugs=[])
        if t:
            row["tractability"] = sorted({x["label"] for x in (t["tractability"] or [])
                                          if x.get("value")})
            seen = {}
            for r in ((t.get("drugAndClinicalCandidates") or {}).get("rows") or []):
                d = r.get("drug") or {}
                nm = d.get("name")
                if not nm:
                    continue
                stage = d.get("maximumClinicalStage")
                acts, moas = set(), set()
                for m in ((d.get("mechanismsOfAction") or {}).get("rows") or []):
                    if m.get("actionType"):
                        acts.add(m["actionType"])
                    if m.get("mechanismOfAction"):
                        moas.add(m["mechanismOfAction"])
                cur = seen.setdefault(nm, dict(name=nm,
                                               approved=(stage == "APPROVAL"),
                                               maxphase=stage,
                                               drugtype=d.get("drugType"),
                                               actions=set(), moas=set()))
                cur["actions"] |= acts
                cur["moas"] |= moas
            for v in seen.values():
                acts = sorted(v["actions"])
                v["actions"] = acts
                v["moas"] = sorted(v["moas"])
                v["direction"] = classify("; ".join(acts) + "; " + "; ".join(v["moas"]))
                v["matches_need"] = (want is not None and v["direction"] == want)
                row["drugs"].append(v)
            row["drugs"].sort(key=lambda x: (not x["matches_need"], not x["approved"],
                                             x["name"]))
        out.append(row)

    out.sort(key=lambda r: -(abs(r["plof_cm"]) if r["plof_cm"] is not None else 0))
    json.dump(out, open(os.path.join(OUTDIR, "signed_target_drug_table.json"), "w"),
              indent=1)

    with open(os.path.join(OUTDIR, "signed_target_drug_table.tsv"), "w") as fh:
        fh.write("gene\tplof_cm\tplof_p\twant\ttractability\t"
                 "matching_approved\tmatching_clinical\tcontra_approved\n")
        for r in out:
            m_app = [d["name"] for d in r["drugs"] if d["matches_need"] and d["approved"]]
            m_cli = [d["name"] for d in r["drugs"]
                     if d["matches_need"] and not d["approved"]]
            contra = [d["name"] for d in r["drugs"]
                      if r["want"] and d["direction"] not in ("?", r["want"])
                      and d["approved"]]
            fh.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
                r["gene"], r["plof_cm"], r["plof_p"], r["want"],
                ",".join(r["tractability"]), ";".join(m_app[:12]),
                ";".join(m_cli[:12]), ";".join(contra[:12])))

    print("\n" + "=" * 96)
    print("GENES WHOSE LOSS MAKES HUMANS TALLER, WITH A DRUG THAT PUSHES THAT WAY")
    print("=" * 96)
    for r in out:
        if r["want"] != "down" or r["plof_p"] is None or r["plof_p"] > 1e-4:
            continue
        hits = [d for d in r["drugs"] if d["matches_need"]]
        if not hits:
            continue
        app = [d["name"] for d in hits if d["approved"]]
        cli = [d["name"] for d in hits if not d["approved"]]
        print("\n%-10s %+6.2f cm  P=%.1e  (%s)" % (r["gene"], r["plof_cm"], r["plof_p"],
                                                   ",".join(r["tractability"]) or "-"))
        if app:
            print("   APPROVED : %s" % ", ".join(sorted(app)[:14]))
        if cli:
            print("   clinical : %s" % ", ".join(sorted(cli)[:14]))

    print("\n" + "=" * 96)
    print("CONTRAINDICATION SCREEN - approved INHIBITORS of genes whose loss SHORTENS")
    print("=" * 96)
    for r in out:
        if r["want"] != "up" or r["plof_cm"] is None or r["plof_cm"] > -2:
            continue
        bad = [d["name"] for d in r["drugs"] if d["direction"] == "down" and d["approved"]]
        if bad:
            print("%-10s %+6.2f cm : %s" % (r["gene"], r["plof_cm"],
                                            ", ".join(sorted(bad)[:14])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
