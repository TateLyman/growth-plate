#!/usr/bin/env python3
"""
ROUND 264. WHERE TO ATTACK - computed from the graph, not recalled.

The height identity this atlas settled at round 247:

    HEIGHT = integral over time of  lambda * N * A * h_term  dt
             lambda = stem division rate     N = stem pool size
             A      = amplification          h_term = terminal cell height
             dt     = duration until fusion

Every agent must move one of those five. This script walks every node in the
atlas, finds the ones that are INTERVENTIONS or carry an X/A/B-graded claim about
an agent, and asks which term each one moves and with what grade of evidence for a
LENGTH endpoint. The output is the coverage table: which terms have an agent with
a length endpoint, which have an agent with only a proxy, and which have nothing.

It is deliberately mechanical. It reads claim_grades and quantitative rows and does
not use anything I remember. Where a node's term assignment is not recoverable from
its own text, it is listed as UNASSIGNED rather than guessed.
"""
import os, re, glob, yaml
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODES = glob.glob(os.path.join(ROOT, "nodes", "*", "*.yaml"))

# Term keywords, taken from the identity. A node is assigned to a term only if its
# own text names that term's vocabulary.
TERMS = {
    "N  (pool size)":      r"resting[- ]zone (cell )?(number|count)|pool size|pool expansion|progenitor number|stem cell number|reserve zone cell",
    "lambda (stem rate)":  r"resting[- ]zone (proliferation|cycle time|division)|stem cell cycle|pool consumption rate|recruitment rate",
    "A  (amplification)":  r"amplification|proliferative zone|cells per column|transit[- ]amplif|column length|residence time",
    "h_term (cell height)":r"terminal (hypertrophic )?cell (height|size|volume)|hypertrophic cell height|h_term",
    "dt (duration)":       r"fusion|epiphyseal clos|senescence|duration lever|delay(ed)? (fusion|closure)|time to fusion",
}

# Evidence tier for a LENGTH endpoint specifically.
LENGTH_POS = r"(bone|tibia|femur|femoral|tibial|body|naso-anal|limb|adult|final|near-final) (length|height)"
PROXY_ONLY = r"zone height|growth plate height|plate thickness|growth plate width|cross-sect|area"


def load(p):
    try:
        return yaml.safe_load(open(p))
    except Exception:
        return None


def text_of(d):
    parts = [str(d.get("name", "")), str(d.get("summary", ""))]
    for q in d.get("quantitative", []) or []:
        parts += [str(q.get("parameter", "")), str(q.get("value", "")), str(q.get("conditions", ""))]
    for c in d.get("claim_grades", []) or []:
        parts += [str(c.get("claim", "")), str(c.get("basis", ""))]
    return " ".join(parts)


def main():
    per_term = defaultdict(list)
    unassigned = []
    x_graded = []          # things explicitly refuted, i.e. attack surfaces already burned
    length_endpoints = []  # every node carrying an actual length measurement

    for p in NODES:
        d = load(p)
        if not d or d.get("stub"):
            continue
        t = text_of(d)
        nid = d.get("id", os.path.basename(p))
        typ = d.get("type", "")
        conf = d.get("confidence", "?")

        hits = [k for k, pat in TERMS.items() if re.search(pat, t, re.I)]
        has_len = bool(re.search(LENGTH_POS, t, re.I))
        has_proxy = bool(re.search(PROXY_ONLY, t, re.I))

        if has_len:
            length_endpoints.append((nid, conf, sorted(hits)))

        for c in d.get("claim_grades", []) or []:
            if str(c.get("grade", "")).upper() == "X":
                x_graded.append((nid, str(c.get("claim", ""))[:110]))

        if typ == "intervention":
            if hits:
                for h in hits:
                    per_term[h].append((nid, conf, "LENGTH" if has_len else ("proxy" if has_proxy else "-")))
            else:
                unassigned.append((nid, conf))

    print("=" * 94)
    print("WHERE TO ATTACK - TERM COVERAGE, COMPUTED FROM THE GRAPH")
    print(f"{len(NODES)} node files scanned")
    print("=" * 94)

    for term in TERMS:
        rows = sorted(set(per_term.get(term, [])))
        withlen = [r for r in rows if r[2] == "LENGTH"]
        print(f"\n### {term}")
        print(f"    intervention nodes touching this term: {len(rows)}")
        print(f"    of which carry a LENGTH endpoint:      {len(withlen)}")
        for r in rows[:8]:
            print(f"      [{r[2]:>6}] {r[1]:<3} {r[0][:72]}")
        if len(rows) > 8:
            print(f"      ... and {len(rows)-8} more")

    print("\n" + "=" * 94)
    print("INTERVENTION NODES WHOSE TERM CANNOT BE ASSIGNED FROM THEIR OWN TEXT")
    print("These are agents the atlas holds without saying what they move. Each is a")
    print("bookkeeping hole: it cannot be stacked, because stacking is a statement about terms.")
    print("=" * 94)
    for nid, conf in sorted(set(unassigned))[:25]:
        print(f"    {conf:<3} {nid[:80]}")
    print(f"    TOTAL UNASSIGNED: {len(set(unassigned))}")

    print("\n" + "=" * 94)
    print("ALREADY BURNED - claims this atlas has graded X (refuted)")
    print("An attack surface with an X on it is not a gap, it is a wall someone already hit.")
    print("=" * 94)
    print(f"    {len(x_graded)} X-graded claims across the graph")
    for nid, claim in x_graded[:18]:
        print(f"      {nid[:44]:<44} | {claim}")
    if len(x_graded) > 18:
        print(f"      ... and {len(x_graded)-18} more")

    print("\n" + "=" * 94)
    print("EVERY NODE CARRYING A REAL LENGTH ENDPOINT")
    print("This is the scarcest thing in the file and the only currency that converts.")
    print("=" * 94)
    print(f"    {len(length_endpoints)} nodes mention a bone/body length or height measurement")
    byterm = defaultdict(int)
    for nid, conf, hits in length_endpoints:
        for h in hits:
            byterm[h] += 1
    for k in TERMS:
        print(f"      {k:<22} {byterm.get(k,0)} length-endpoint nodes")


if __name__ == "__main__":
    main()
