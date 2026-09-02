#!/usr/bin/env python3
"""
ROUND 326. THE AKT-AXIS ACCESSIBLE-AGENT SCREEN.

WHY THIS SCREEN AND WHY NOW. Rounds 324 and 325 converged, from two unrelated targets, on one axis:
PI3K-AKT-mTOR is the growth-POSITIVE direction for this tissue, and it sets CELL SIZE, which is h_term -
roughly 80 per cent of longitudinal growth and the term round 296 concluded had no upward-pointing agent
after sweeping six compound classes. The direction is fixed by four independent human nodes (PTEN, AKT1 and
PIK3CA give overgrowth and tall stature; MTOR pLoF is -3.65 cm) and by one drug (rapamycin halves a rat's
longitudinal growth rate). Neither of the two targets that led here is usable: NRK is Tdark and its
function is kinase-independent; PTP-MEG2 has a superb tool compound with no supplier, a mouse null that is
smaller, and a Step-0 collision.

SO THE QUESTION IS NO LONGER "WHICH GENE" BUT "WHICH ACCESSIBLE MOLECULE MOVES THIS AXIS UPWARD".
This script asks it systematically instead of by association, which is how the atlas has answered it so far.

THE METHOD.
  1. Enumerate the axis - receptors, lipid kinases and phosphatases, the kinase core, the mTORC1/2
     complexes, the negative regulators, and the readouts. Include the tyrosine phosphatases that act on the
     receptors, because that is where round 325's chemistry lives.
  2. For every gene, ask which direction RAISES AKT output. A negative regulator (PTEN, TSC1/2, INPPL1,
     PTPN1/9, FOXO, DEPDC5, NPRL2/3, SESN2) must be INHIBITED; a positive component (PIK3CA, AKT1/2/3, MTOR,
     RHEB, PDPK1, IRS1/2, INSR, IGF1R) must be ACTIVATED. That sign is set by hand from pathway biology and
     recorded per gene, not inferred by keyword.
  3. Pull every drug and clinical candidate from Open Targets with its mechanism direction, and keep only
     agents pointing the way that RAISES AKT. Report approved separately from clinical.
  4. Filter by CORR-327 - is the target in the postnatal human growth plate at all (GSE288028).
  5. Report the CONTRAINDICATION side in the same pass: approved agents that push the axis DOWN. That half
     is at least as valuable, because the stack may already contain one.

WHAT THIS CANNOT DO, STATED FIRST.
  - Open Targets mechanism strings are keyword-classified. A match is triage, not a drug label.
  - "Raises AKT" is a pathway-level statement. Compartmentalisation is real (CORR-332) and none of these
     agents has ever been shown to raise phospho-AKT in a growth plate.
  - Systemic AKT activation is the mechanism of several overgrowth-with-cancer syndromes. Nothing here is
     a recommendation; the output is a ranked list of things that could be tested, with their liabilities.
  - No agent on this axis has a bone-LENGTH endpoint in a normal growing animal. That gap is the point.

Usage:  python3 atlas/tools/round326_akt_axis_accessible_agent_screen.py
"""
import json
import os
import sys
import time
import urllib.request

OT = "https://api.platform.opentargets.org/api/v4/graphql"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(HERE, "data", "round326")

# gene -> (direction that RAISES AKT output, role)
AXIS = {
    # receptors and adaptors - activate
    "INSR": ("up", "insulin receptor"), "IGF1R": ("up", "IGF-1 receptor"),
    "IRS1": ("up", "adaptor"), "IRS2": ("up", "adaptor"),
    "FGFR3": ("skip", "in the stack already"),
    # lipid kinases - activate
    "PIK3CA": ("up", "PI3K p110a"), "PIK3CB": ("up", "PI3K p110b"),
    "PIK3CD": ("up", "PI3K p110d"), "PIK3R1": ("up", "PI3K regulatory"),
    # lipid phosphatases - inhibit
    "PTEN": ("down", "PIP3 phosphatase - brake"),
    "INPPL1": ("down", "SHIP2 - brake"), "INPP4B": ("down", "brake"),
    "PIK3IP1": ("down", "brake"),
    # protein tyrosine phosphatases on the receptors - inhibit
    "PTPN1": ("down", "PTP1B - dephosphorylates IR/IGF1R"),
    "PTPN9": ("down", "PTP-MEG2 - round 325"),
    "PTPN2": ("down", "TC-PTP"), "PTPN11": ("skip", "SHP2 is POSITIVE for RAS/MAPK - sign ambiguous"),
    # kinase core - activate
    "AKT1": ("up", "AKT1"), "AKT2": ("up", "AKT2"), "AKT3": ("up", "AKT3"),
    "PDPK1": ("up", "PDK1"), "RICTOR": ("up", "mTORC2"), "MTOR": ("up", "mTOR"),
    "RHEB": ("up", "mTORC1 activator"), "RPTOR": ("up", "raptor"),
    "RPS6KB1": ("up", "S6K1"), "EIF4EBP1": ("down", "4E-BP1 is a brake on translation"),
    # negative regulators of mTORC1 - inhibit
    "TSC1": ("down", "brake"), "TSC2": ("down", "brake"),
    "DEPDC5": ("down", "GATOR1 brake"), "NPRL2": ("down", "GATOR1 brake"),
    "NPRL3": ("down", "GATOR1 brake"), "SESN2": ("down", "sestrin2 brake"),
    "PRKAA1": ("down", "AMPK - inhibits mTORC1"), "PRKAA2": ("down", "AMPK"),
    # AKT's own brakes and readouts
    "PHLPP1": ("down", "dephosphorylates AKT S473"), "PHLPP2": ("down", "same"),
    "FOXO1": ("down", "AKT-inhibited TF"), "FOXO3": ("down", "same"),
    "GSK3B": ("down", "AKT-inhibited kinase"),
    "CSNK2A1": ("up", "CK2 inactivates PTEN - round 324"),
    "CSNK2B": ("up", "CK2 beta - round 324"),
    "NRK": ("down", "brake on CK2 - round 324"),
}

INHIBIT_WORDS = ("inhibitor", "antagonist", "blocker", "negative modulator", "degrader",
                 "inverse agonist", "disrupting agent", "suppressor")
ACTIVATE_WORDS = ("agonist", "activator", "positive modulator", "stimulant", "opener",
                  "potentiator", "substitute", "replacement")

Q = """query($ids:[String!]!){targets(ensemblIds:$ids){
  id approvedSymbol
  tractability{label modality value}
  drugAndClinicalCandidates{count rows{drug{id name drugType maximumClinicalStage
    mechanismsOfAction{rows{actionType mechanismOfAction targets{approvedSymbol}}}}}}
}}"""


def gql(query, variables, tries=4):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(OT, data=body, headers={"Content-Type": "application/json"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001
            if i == tries - 1:
                print("  ! %s" % e, file=sys.stderr)
                return None
            time.sleep(2 ** i)
    return None


def classify(a):
    a = (a or "").lower()
    if any(w in a for w in INHIBIT_WORDS):
        return "down"
    if any(w in a for w in ACTIVATE_WORDS):
        return "up"
    return "?"


def ens_ids(symbols):
    """One POST instead of N GETs - the per-symbol endpoint made this script slower than the
    Open Targets query it feeds."""
    out = {}
    for i in range(0, len(symbols), 40):
        chunk = symbols[i:i + 40]
        body = json.dumps({"symbols": chunk}).encode()
        req = urllib.request.Request(
            "https://rest.ensembl.org/lookup/symbol/homo_sapiens",
            data=body, headers={"Content-Type": "application/json",
                                "Accept": "application/json"})
        for _ in range(3):
            try:
                d = json.loads(urllib.request.urlopen(req, timeout=60).read().decode())
                for k, v in d.items():
                    if isinstance(v, dict) and v.get("id"):
                        out[k] = v["id"]
                break
            except Exception:  # noqa: BLE001
                time.sleep(1.5)
    return out


def main():
    gp = json.load(open(os.path.join(HERE, "data", "round308",
                                     "gse288028_pseudobulk_presence.json")))["genes"]
    genes = [g for g, (d, _) in AXIS.items() if d != "skip"]
    ids = ens_ids(genes)
    print("resolved %d/%d Ensembl IDs" % (len(ids), len(genes)))
    tmap = {}
    idl = sorted(set(ids.values()))
    for i in range(0, len(idl), 25):
        d = gql(Q, {"ids": idl[i:i + 25]})
        if d and "data" in d:
            for t in d["data"]["targets"] or []:
                tmap[t["approvedSymbol"]] = t
        time.sleep(0.25)
    print("Open Targets returned %d targets\n" % len(tmap))

    rows = []
    for g in genes:
        want, role = AXIS[g]
        t = tmap.get(g)
        e = gp.get(g)
        rec = dict(gene=g, want=want, role=role,
                   gp_cpm=(e or {}).get("medCPM"), gp_det=(e or {}).get("det"),
                   gp_pct=(e or {}).get("maxPct"),
                   tractability=[], pro=[], contra=[])
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
                                               approved=(d.get("maximumClinicalStage") == "APPROVAL"),
                                               phase=d.get("maximumClinicalStage"),
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
                if v["direction"] == want:
                    rec["pro"].append(v)
                elif v["direction"] != "?":
                    rec["contra"].append(v)
        rows.append(rec)

    os.makedirs(OUTDIR, exist_ok=True)
    json.dump(rows, open(os.path.join(OUTDIR, "akt_axis_agents.json"), "w"), indent=1)

    print("=" * 108)
    print("PRO - AGENTS THAT PUSH THE AXIS THE WAY THAT RAISES AKT")
    print("     (for a brake the wanted action is INHIBIT; for a positive node, ACTIVATE)")
    print("=" * 108)
    for r in sorted(rows, key=lambda r: -(r["gp_cpm"] or 0)):
        if not r["pro"]:
            continue
        app = sorted({d["name"] for d in r["pro"] if d["approved"]})
        cli = sorted({d["name"] for d in r["pro"] if not d["approved"]})
        print("\n  %-9s want=%-5s %-42s GP %s" %
              (r["gene"], r["want"], r["role"][:42],
               ("%7.1f CPM %2d/14 %5.1f%%" % (r["gp_cpm"], r["gp_det"], r["gp_pct"]))
               if r["gp_cpm"] is not None else "not in matrix"))
        if app:
            print("      APPROVED  : %s" % ", ".join(app[:14]))
        if cli:
            print("      clinical  : %s" % ", ".join(cli[:14]))

    print()
    print("=" * 108)
    print("CONTRA - APPROVED AGENTS THAT PUSH THE AXIS DOWN (check the stack and the medication list)")
    print("=" * 108)
    for r in sorted(rows, key=lambda r: -(r["gp_cpm"] or 0)):
        bad = sorted({d["name"] for d in r["contra"] if d["approved"]})
        if bad:
            print("  %-9s %-40s %s" % (r["gene"], r["role"][:40], ", ".join(bad[:12])))

    print()
    print("=" * 108)
    print("NO AGENT IN THE WANTED DIRECTION")
    print("=" * 108)
    print("  " + ", ".join(r["gene"] for r in rows if not r["pro"]))
    print("\nwrote %s" % os.path.join(OUTDIR, "akt_axis_agents.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
