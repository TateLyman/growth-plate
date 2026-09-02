#!/usr/bin/env python3
"""
ROUND 334. THE CHEMICAL-MATTER SWEEP I SHOULD HAVE RUN BEFORE EVER WRITING "NO COMPOUND".

WHY THIS EXISTS. Rounds 298, 300, 312, 313 and 331 all reported chemical matter using Open
Targets KNOWN DRUGS, which lists clinical and approved agents only. Tool compounds, chemical
probes and preclinical inhibitors are INVISIBLE to that query. CPI-455 - a well characterised
pan-KDM5 inhibitor - does not appear, and round 333 consequently wrote that the KDM5 class had
"no clinical-stage inhibitor" as though that meant no chemical matter. It does not.
This is failure mode 13 (CORR-312, "asserting a target has no chemical matter") and failure
mode 29 (CORR-335, "calling a target no-chemical-matter off ONE database") for the third time.

WHAT THIS DOES INSTEAD. Queries ChEMBL bioactivity directly, per target:
  - resolve the human SINGLE PROTEIN target
  - count DISTINCT molecules with a pChEMBL value (>=5, i.e. <=10 uM) and the best potency
  - report the maximum clinical phase reached by any molecule with activity on that target
  - flag PROTEIN-PROTEIN INTERACTION / cereblon targets, which indicate DEGRADERS exist

READ THE OUTPUT AS: n_molecules is chemical matter. max_phase is clinical maturity. They are
DIFFERENT QUESTIONS and this atlas conflated them.
"""
import json, sys, time, urllib.request

BASE = "https://www.ebi.ac.uk/chembl/api/data"

def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            if i == tries - 1:
                return {"_err": str(e)}
            time.sleep(2 * (i + 1))
    return {}

def resolve(gene):
    d = get(f"{BASE}/target/search.json?q={gene}&limit=25")
    single, degrader = None, False
    for t in d.get("targets", []):
        if t.get("organism") != "Homo sapiens":
            continue
        name = (t.get("pref_name") or "").lower()
        if t.get("target_type") == "SINGLE PROTEIN" and single is None:
            for c in t.get("target_components", []):
                for syn in c.get("target_component_synonyms", []):
                    if syn.get("component_synonym", "").upper() == gene.upper():
                        single = t
                        break
                if single: break
        if t.get("target_type") == "PROTEIN-PROTEIN INTERACTION" and "cereblon" in name:
            degrader = True
    if single is None:
        for t in d.get("targets", []):
            if t.get("organism") == "Homo sapiens" and t.get("target_type") == "SINGLE PROTEIN":
                single = t
                break
    return single, degrader

def activity(tid):
    mols, best = set(), None
    url = (f"{BASE}/activity.json?target_chembl_id={tid}"
           f"&pchembl_value__gte=5&limit=1000")
    n_pages = 0
    while url and n_pages < 6:
        d = get(url)
        if "_err" in d:
            break
        for a in d.get("activities", []):
            m = a.get("molecule_chembl_id")
            if m: mols.add(m)
            try:
                v = float(a.get("pchembl_value"))
                if best is None or v > best: best = v
            except (TypeError, ValueError):
                pass
        nxt = d.get("page_meta", {}).get("next")
        url = ("https://www.ebi.ac.uk" + nxt) if nxt else None
        n_pages += 1
    return mols, best

def max_phase(tid):
    d = get(f"{BASE}/mechanism.json?target_chembl_id={tid}&limit=200")
    if "_err" in d: return None, []
    names = []
    for m in d.get("mechanisms", []):
        mid = m.get("molecule_chembl_id")
        if mid: names.append((mid, m.get("mechanism_of_action")))
    return len(names), names[:6]

def main(genes):
    out = {}
    for g in genes:
        t, degrader = resolve(g)
        if t is None:
            out[g] = {"chembl_target": None, "n_molecules": 0, "best_pchembl": None,
                      "degrader_target": degrader, "note": "no human target in ChEMBL"}
            print(f"{g:10s} NO HUMAN CHEMBL TARGET")
            continue
        tid = t["target_chembl_id"]
        mols, best = activity(tid)
        nmech, mech = max_phase(tid)
        out[g] = {"chembl_target": tid, "pref_name": t.get("pref_name"),
                  "n_molecules_pchembl_ge5": len(mols), "best_pchembl": best,
                  "n_mechanism_records": nmech, "example_mechanisms": mech,
                  "degrader_target_exists": degrader}
        print(f"{g:10s} {tid:15s} mols={len(mols):5d} bestpChEMBL={best if best else '-':>5} "
              f"mech={nmech} degrader={'Y' if degrader else '-'}")
        sys.stdout.flush()
        time.sleep(0.3)
    return out

if __name__ == "__main__":
    GENES = sys.argv[1].split(",") if len(sys.argv) > 1 else []
    res = main(GENES)
    dest = "/home/user/growth-plate/atlas/data/round334/chembl_sweep.json"
    import os; os.makedirs(os.path.dirname(dest), exist_ok=True)
    prev = {}
    if os.path.exists(dest):
        prev = json.load(open(dest))
    prev.update(res)
    json.dump(prev, open(dest, "w"), indent=1)
    print("wrote", dest, len(prev), "genes")
