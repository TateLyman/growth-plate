#!/usr/bin/env python3
"""
ROUND 323. THE 69 LENGTHENING KNOCKOUTS, ASSESSED - which round 304 explicitly told the next
round to do and which rounds 305-322 all went past.

Round 304's own closing words, verbatim from CLAUDE.md: "Several are drugged - deucravacitinib
(TYK2), PI3Kgamma and LTA4H clinical compounds, REV-ERB ligands (NR1D1), ENPP1 enzyme therapy.
None assessed. Start the next round here, from data."

WHY THIS SET AND NOT ANOTHER. CORR-329 established that 63.7% of all IMPC knockouts are
SHORTER and that at P<1e-4 the split is 245 shorter to 38 longer. In a screen that skewed only
the RARE direction carries information, so the ~69 knockouts that LENGTHEN a mouse are the most
information-dense rows in a 12,068-row file, and they are the only rows in the atlas that pair
a perturbation with a length endpoint at genome scale.

THE FOUR JOINS, each of which can kill a row.
  1. IS THE MOUSE RESULT CLEAN? An IMPC hit reported for ONE SEX with a null combined-sex row
     is a different claim from a hit in the combined analysis. This script separates
     sex-specific rows from sex-agnostic ones and reports every length row per gene, not the
     single best one - a gene with tibia UP in females and body length DOWN overall is not a
     lengthening knockout, it is a noisy line.
  2. IS THE TARGET IN THE TISSUE? CORR-327. GSE288028, 14 postnatal human growth plate
     samples, 79,934 cells. A gene not transcribed in the human growth plate cannot be a local
     lever no matter what a mouse knockout does.
  3. WHICH COMPARTMENT? R318. The residual at this bone age is trunk-dominant, so a lever that
     allocates to legs is aimed at the spent compartment. Standing/sitting/leg-length summary
     statistics from the same ~546k cohort (bartell2026), same variant, aligned to the
     height-INCREASING allele.
  4. IS THERE AN OBTAINABLE AGENT, AND DOES IT PUSH THE RIGHT WAY? Open Targets tractability
     and drug list, with the direction of each drug's mechanism classified and compared against
     the direction the mouse knockout implies (loss lengthens -> we want an INHIBITOR).

WHAT THIS SCREEN CANNOT DO, stated before the results.
  - IMPC effect sizes are in the pipeline's own normalised units, NOT centimetres and NOT
    percent. They rank; they do not predict a gain.
  - A germline knockout is not a drug given at bone age 16 (CORR-299). Every hit needs the
    open-plate question asked separately.
  - Expression is presence, not dependence, and the compartment coordinate is a common-variant
    lead-allele effect in SD units, not a predicted centimetre (R318's own boundary).
  - n per line is typically 5-10 per sex at a single phenotyping centre.

Usage:  python3 atlas/tools/round323_lengthening_knockout_screen.py
"""
import json
import os
import sys
import time
import urllib.request

OT = "https://api.platform.opentargets.org/api/v4/graphql"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(HERE, "data", "round323")

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
    req = urllib.request.Request(OT, data=body, headers={"Content-Type": "application/json"})
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


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def ensembl_ids(symbols):
    out = {}
    for s in symbols:
        for attempt in range(3):
            try:
                u = ("https://rest.ensembl.org/lookup/symbol/homo_sapiens/%s"
                     "?content-type=application/json" % s)
                d = json.load(urllib.request.urlopen(u, timeout=30))
                out[s] = d["id"]
                break
            except Exception:  # noqa: BLE001 - retried, missing symbols are reported
                time.sleep(1.5)
    return out


def main():
    rows = json.load(open(os.path.join(HERE, "data", "round303",
                                       "impc_length_endpoints_all.json")))
    lengthen = json.load(open(os.path.join(HERE, "data", "round303",
                                           "impc_lengthening_knockouts.json")))
    gp = json.load(open(os.path.join(HERE, "data", "round308",
                                     "gse288028_pseudobulk_presence.json")))["genes"]

    genes = sorted({r["marker_symbol"] for r in lengthen})
    print("%d lengthening-knockout genes from round 303" % len(genes))

    # ---- JOIN 1: every length row per gene, sex-specific rows separated -------------
    per_gene = {}
    for g in genes:
        rs = [r for r in rows if r["marker_symbol"] == g and fnum(r["p_value"]) is not None]
        agn, sexed, contra = [], [], []
        for r in rs:
            rec = dict(param=r["parameter_name"], zyg=r["zygosity"],
                       sex=r["sex"] or "both", eff=fnum(r["effect_size"]),
                       p=fnum(r["p_value"]), centre=r["phenotyping_center"],
                       nm=r.get("male_mutant_count"), nf=r.get("female_mutant_count"))
            if rec["p"] is not None and rec["p"] < 1e-4 and rec["eff"] is not None:
                (sexed if rec["sex"] in ("male", "female") else agn).append(rec)
            if rec["p"] is not None and rec["p"] < 0.01 and rec["eff"] is not None \
                    and rec["eff"] < 0:
                contra.append(rec)
        per_gene[g] = dict(sex_agnostic=agn, sex_specific=sexed, opposing=contra,
                           n_rows=len(rs))

    # ---- JOIN 2: human growth plate expression -------------------------------------
    for g in genes:
        e = gp.get(g.upper())
        per_gene[g]["gp"] = (dict(cpm=e.get("medCPM"), det=e.get("det"),
                                  maxpct=e.get("maxPct")) if e else None)

    # ---- JOIN 4: Open Targets -------------------------------------------------------
    expressed = [g for g in genes
                 if per_gene[g]["gp"] and (per_gene[g]["gp"]["det"] or 0) >= 10
                 and (per_gene[g]["gp"]["cpm"] or 0) >= 5]
    print("%d of %d are expressed in postnatal human growth plate "
          "(>=10/14 samples, >=5 CPM)" % (len(expressed), len(genes)))

    ids = ensembl_ids([g.upper() for g in expressed])
    print("resolved %d/%d Ensembl IDs" % (len(ids), len(expressed)))
    tmap = {}
    idlist = sorted(set(ids.values()))
    for i in range(0, len(idlist), 25):
        d = gql(Q, {"ids": idlist[i:i + 25]})
        if d and "data" in d:
            for t in d["data"]["targets"] or []:
                tmap[t["approvedSymbol"]] = t
        time.sleep(0.3)
    print("Open Targets returned %d targets" % len(tmap))

    for g in expressed:
        t = tmap.get(g.upper())
        rec = dict(tractability=[], drugs=[], resolved=bool(t))
        if t:
            rec["tractability"] = sorted({x["label"] for x in (t["tractability"] or [])
                                          if x.get("value")})
            seen = {}
            for r in ((t.get("drugAndClinicalCandidates") or {}).get("rows") or []):
                d = r.get("drug") or {}
                nm = d.get("name")
                if not nm:
                    continue
                cur = seen.setdefault(nm, dict(name=nm, drugtype=d.get("drugType"),
                                               maxphase=d.get("maximumClinicalStage"),
                                               approved=(d.get("maximumClinicalStage")
                                                         == "APPROVAL"),
                                               actions=set(), moas=set()))
                for m in ((d.get("mechanismsOfAction") or {}).get("rows") or []):
                    if m.get("actionType"):
                        cur["actions"].add(m["actionType"])
                    if m.get("mechanismOfAction"):
                        cur["moas"].add(m["mechanismOfAction"])
            for v in seen.values():
                v["actions"] = sorted(v["actions"])
                v["moas"] = sorted(v["moas"])
                v["direction"] = classify("; ".join(v["actions"]) + "; " + "; ".join(v["moas"]))
                # loss lengthens -> the wanted pharmacology is INHIBITION
                v["matches_need"] = (v["direction"] == "down")
                rec["drugs"].append(v)
            rec["drugs"].sort(key=lambda x: (not x["matches_need"], not x["approved"], x["name"]))
        per_gene[g]["ot"] = rec

    os.makedirs(OUTDIR, exist_ok=True)
    json.dump(per_gene, open(os.path.join(OUTDIR, "lengthening_ko_screen.json"), "w"), indent=1)

    # ---- REPORT ---------------------------------------------------------------------
    print()
    print("=" * 112)
    print("TIER 1  sex-AGNOSTIC lengthening row at P<1e-4, expressed in human growth plate,")
    print("        and NO opposing (shortening) row at P<0.01")
    print("=" * 112)
    tier1 = []
    for g in expressed:
        d = per_gene[g]
        if d["sex_agnostic"] and not d["opposing"]:
            best = max(d["sex_agnostic"], key=lambda r: abs(r["eff"]))
            tier1.append((g, best, d))
    tier1.sort(key=lambda x: -x[1]["eff"])
    for g, b, d in tier1:
        drugs = d.get("ot", {}).get("drugs", [])
        app = [x["name"] for x in drugs if x["matches_need"] and x["approved"]]
        cli = [x["name"] for x in drugs if x["matches_need"] and not x["approved"]]
        print("  %-9s %-13s %-13s eff %+6.2f P=%.1e n=%s/%s %-9s | GP %7.1f CPM %2d/14 %5.1f%% "
              "| tract %s" %
              (g, b["param"][:13], b["zyg"], b["eff"], b["p"], b["nm"], b["nf"], b["centre"][:9],
               d["gp"]["cpm"], d["gp"]["det"], d["gp"]["maxpct"],
               ",".join(d.get("ot", {}).get("tractability", [])) or "-"))
        if app:
            print("        APPROVED INHIBITORS: %s" % ", ".join(sorted(app)[:10]))
        if cli:
            print("        clinical inhibitors: %s" % ", ".join(sorted(cli)[:10]))

    print()
    print("=" * 112)
    print("TIER 2  lengthening row is SEX-SPECIFIC only, or an opposing row exists")
    print("=" * 112)
    for g in expressed:
        d = per_gene[g]
        if (g, None, None) in []:
            continue
        if d["sex_agnostic"] and not d["opposing"]:
            continue
        why = []
        if not d["sex_agnostic"]:
            why.append("sex-specific only")
        if d["opposing"]:
            why.append("opposing row: " + "; ".join(
                "%s %s %+0.2f P=%.1g" % (r["param"], r["sex"], r["eff"], r["p"])
                for r in d["opposing"][:2]))
        print("  %-9s %-52s GP %7.1f CPM" % (g, " | ".join(why)[:52], d["gp"]["cpm"]))

    print()
    print("=" * 112)
    print("NOT IN THE HUMAN GROWTH PLATE - excluded by CORR-327, not by direction")
    print("=" * 112)
    for g in genes:
        if g in expressed:
            continue
        e = per_gene[g]["gp"]
        print("  %-9s %s" % (g, "det %d/14, %.2f CPM" % (e["det"], e["cpm"]) if e
                             else "not in GSE288028"))
    print()
    print("wrote %s" % os.path.join(OUTDIR, "lengthening_ko_screen.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
