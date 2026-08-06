#!/usr/bin/env python3
"""
provenance_audit.py - find the numbers whose grade lives in a paper nobody read.

WHY THIS EXISTS
---------------
CORR-009 and CORR-010 are the same defect twice.

hunziker1989's terminal cell height carried three rounds of this atlas's reasoning and a
proposed compound class. It is not a measurement. It is a super-egg model output equal to
cell volume divided by a cell-width second moment, and the paper that says so is
cruzorive1986 - cited in hunziker1989's second sentence, forty pages long, unread here until
the number had already been built on. rubin2021 was then accepted from its abstract on the
other side of the same dispute, and its height is a bounding box fitted to an ellipsoid
fitted to the cell.

The lesson both times: A NUMBER'S GRADE IS A PROPERTY OF HOW IT WAS OBTAINED, AND THAT IS
USUALLY DOCUMENTED SOMEWHERE OTHER THAN THE PAPER YOU ARE CITING. The atlas has a
`has_full_text` flag per reference. It has no flag for whether the METHOD behind the number
was ever checked, and at the time of writing 1,006 of 1,068 references carry `has_full_text`
against 19 carrying `full_text_read`.

WHAT THIS TOOL IS, AND WHAT IT IS EMPHATICALLY NOT
--------------------------------------------------
It is a TRIAGE RANKER. It scores every quantitative row in the atlas by how much would be at
stake if its provenance turned out to be model-derived rather than measured, and by how many
warning signs the row itself carries. It emits a ranked reading list.

IT DOES NOT FIND DEFECTS. A high score is a reading assignment, not a finding. Every one of
CORR-009's claims came from reading a paper, and nothing in this file could have produced
them. Publishing this tool's output as though it were a list of errors would be exactly the
laundering of speculation the atlas exists to prevent - and the ranking is deliberately not
thresholded into a pass/fail, so there is no way to read a verdict off it.

The verdicts live in query/provenance_audit/verdicts.yaml, they are written by hand after
reading the source, and each one names the evidence.

SIGNALS
-------
STAKE - how much rests on the row
  contradiction   the row's node appears in the contradiction ledger
  flow_model      the row's param_id is consumed by the quantitative model
  grade_A_B       the node is graded A or B, i.e. the atlas's strongest claims
  screen          the node appears in the compound screen's outputs

SUSPICION - how likely the value is a derivation rather than a reading
  derivation_word the row's own conditions/uncertainty text uses derivation language
  no_dispersion   no n, no CI, no +/-, no p - nothing that would reveal the estimator
  unread_source   the cited reference has never been marked full_text_read
  sole_source     no second source gives a value for the same parameter on the same node

Rows already labelled "DERIVED BY THIS ATLAS" score ZERO suspicion for derivation language:
they are declared, which is the behaviour being asked for, not the defect being hunted.

Usage:
  python3 atlas/tools/provenance_audit.py            # write ranked worklist + summary
  python3 atlas/tools/provenance_audit.py --top 40   # also print the top N
"""
from __future__ import annotations
import argparse, csv, glob, json, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PARAMS = os.path.join(ROOT, "atlas", "quant", "parameters.csv")
BIB = os.path.join(ROOT, "atlas", "sources", "bibliography.yaml")
CONTRA = os.path.join(ROOT, "atlas", "audit", "contradictions.md")
FLOW = os.path.join(ROOT, "atlas", "quant", "notebooks", "flow_model.py")
NODES = os.path.join(ROOT, "atlas", "nodes")
SCREEN = os.path.join(ROOT, "query", "target_screen")
OUT = os.path.join(ROOT, "query", "provenance_audit")

# Language that says a number was computed rather than read off an instrument. Tuned to be
# recall-heavy: a false positive costs one minute of reading, a false negative is CORR-009.
DERIVATION = re.compile(
    r"\b(derived|derivation|estimated|estimate[sd]?\s+(?:from|using)|calculat|computed|"
    r"back-?calculat|inferred|extrapolat|interpolat|modell?ed|model[- ]based|shape model|"
    r"assum|approximat|unfolding|stereolog|curve[- ]fit|regression|fitted|imputed|"
    r"converted from|normalised to|normalized to|scaled from|predicted)\b", re.I)
# Anything that reveals the estimator had a spread, and therefore a method behind it.
DISPERSION = re.compile(r"(\bn\s*=|\bSD\b|\bSEM\b|\bCI\b|\bIQR\b|±|\+/-|\bp\s*[<=>]|"
                        r"\br\s*=|\bCE\b|%\s*CE|range|\bSE\b)", re.I)
SELF_DECLARED = re.compile(r"DERIVED BY THIS ATLAS|SCORED BY THIS ATLAS|NOTED BY THIS ATLAS|"
                           r"RE-ANALYSIS|AUDIT BY THIS ATLAS", re.I)

WEIGHTS = {"contradiction": 3, "flow_model": 3, "grade_A_B": 2, "screen": 1,
           "derivation_word": 3, "no_dispersion": 2, "unread_source": 1, "sole_source": 1}


def node_confidences():
    out = {}
    import yaml
    for p in glob.glob(os.path.join(NODES, "**", "*.yaml"), recursive=True):
        try:
            d = yaml.safe_load(open(p))
        except Exception:
            continue
        if isinstance(d, dict) and d.get("id"):
            out[d["id"]] = d.get("confidence")
    return out


def main():
    import yaml
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=25)
    a = ap.parse_args()

    rows = list(csv.DictReader(open(PARAMS)))
    bib = yaml.safe_load(open(BIB))
    refs = bib.get("refs", bib)
    conf = node_confidences()

    contra_txt = open(CONTRA).read()
    contra_nodes = set(re.findall(r"`([a-z0-9_]{4,})`", contra_txt)) & set(conf)
    flow_ids = set(re.findall(r"p_[0-9a-f]{10}", open(FLOW).read()))
    screen_nodes = set()
    for p in glob.glob(os.path.join(SCREEN, "*")):
        try:
            screen_nodes |= set(re.findall(r"[a-z0-9_]{4,}", open(p, errors="ignore").read()))
        except Exception:
            pass
    screen_nodes &= set(conf)

    # a parameter is sole-sourced if no other row on the same node names the same parameter
    seen = defaultdict(set)
    for r in rows:
        seen[(r["node_id"], r["parameter"].lower())].add(r["source_ref"])

    scored = []
    for r in rows:
        txt = f"{r['conditions']} {r['uncertainty']}"
        declared = bool(SELF_DECLARED.search(txt))
        sig = {
            "contradiction": r["node_id"] in contra_nodes,
            "flow_model": r["param_id"] in flow_ids,
            "grade_A_B": conf.get(r["node_id"]) in ("A", "B"),
            "screen": r["node_id"] in screen_nodes,
            "derivation_word": bool(DERIVATION.search(txt)) and not declared,
            "no_dispersion": not DISPERSION.search(txt),
            "unread_source": not refs.get(r["source_ref"], {}).get("full_text_read"),
            "sole_source": len(seen[(r["node_id"], r["parameter"].lower())]) == 1,
        }
        stake = sum(WEIGHTS[k] for k in ("contradiction", "flow_model", "grade_A_B", "screen")
                    if sig[k])
        susp = sum(WEIGHTS[k] for k in ("derivation_word", "no_dispersion", "unread_source",
                                        "sole_source") if sig[k])
        if stake == 0:
            continue                      # nothing rests on it; not worth anyone's reading time
        scored.append({"score": stake * susp, "stake": stake, "suspicion": susp,
                       "param_id": r["param_id"], "node_id": r["node_id"], "layer": r["layer"],
                       "parameter": r["parameter"][:90], "value": r["value"][:40],
                       "unit": r["unit"][:24], "species": r["species"],
                       "source_ref": r["source_ref"], "self_declared": declared,
                       "signals": "|".join(k for k, v in sig.items() if v)})
    scored.sort(key=lambda x: (-x["score"], x["node_id"]))

    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "worklist.csv")
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(scored[0]))
        w.writeheader()
        w.writerows(scored)

    json.dump({
        "n_quant_rows_total": len(rows),
        "n_rows_with_stake": len(scored),
        "n_refs": len(refs),
        "n_refs_has_full_text": sum(1 for v in refs.values() if v.get("has_full_text")),
        "n_refs_full_text_read": sum(1 for v in refs.values() if v.get("full_text_read")),
        "weights": WEIGHTS,
        "WHAT_A_SCORE_IS": "a reading assignment, ranked by what would be at stake if the "
                           "provenance turned out to be model-derived. IT IS NOT A DEFECT AND "
                           "NOT A FINDING. No threshold separates pass from fail, on purpose. "
                           "Verdicts are written by hand in verdicts.yaml after reading the "
                           "source, and each names its evidence.",
        "WHY_unread_source_IS_WEIGHTED_LOW": "almost every reference is unread by this "
                                             "standard (19 of 1,068), so on its own the signal "
                                             "separates nothing. It is kept because it "
                                             "compounds with the others.",
    }, open(os.path.join(OUT, "summary.json"), "w"), indent=1)

    print(f"{len(rows)} quantitative rows; {len(scored)} carry stake "
          f"(in a contradiction, in the flow model, on an A/B node, or in the compound screen)")
    print(f"references: {len(refs)} total, "
          f"{sum(1 for v in refs.values() if v.get('has_full_text'))} with full text obtained, "
          f"{sum(1 for v in refs.values() if v.get('full_text_read'))} marked as READ")
    print(f"wrote {p}\n")
    print(f"top {a.top} reading assignments (NOT findings):")
    print(f"  {'score':>5} {'node':32s} {'parameter':46s} {'src':16s} signals")
    for r in scored[:a.top]:
        print(f"  {r['score']:5d} {r['node_id'][:32]:32s} {r['parameter'][:46]:46s} "
              f"{r['source_ref'][:16]:16s} {r['signals']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
