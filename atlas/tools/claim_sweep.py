#!/usr/bin/env python3
"""
Find nodes whose summary makes claims of UNEVEN evidential support, so that a
single node-level `confidence` is either optimistic or lossy.

The canonical pattern: a node that states both
  (a) an ASSOCIATION or population/clinical outcome  - often A/B grade, and
  (b) a MOLECULAR MECHANISM                          - often C/D grade,
and reports one number for both. height_gwas is the archetype: internally
replicated for "these variants associate with height at these effect sizes",
far too generous for "pathway X is causally active in the plate".

Also flags nodes mixing a human clinical claim with an animal mechanistic claim,
which is the same defect wearing different clothes.

Usage:
  python3 atlas/tools/claim_sweep.py              # report candidates
  python3 atlas/tools/claim_sweep.py --stub-in    # insert a claim_grades scaffold
"""
import os, sys, glob, re, argparse
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSOC = re.compile(
    r"\b(associat\w+|correlat\w+|GWAS|genome-wide|polygenic|heritab\w+|"
    r"odds ratio|hazard ratio|variance explained|prevalen\w+|incidence|"
    r"epidemiolog\w+|cohort|meta-analys\w+|SDS|standard deviation score|"
    r"effect size|predict\w+|population)\b", re.I)

MECH = re.compile(
    r"\b(binds?|phosphorylat\w+|dephosphorylat\w+|ubiquitinat\w+|transcrib\w+|"
    r"receptor|ligand|signall?ing|pathway|kinase|promoter|enhancer|"
    r"secret\w+|cleav\w+|catalys\w+|transport\w+|dimeris\w+|dimeriz\w+|"
    r"downstream of|upstream of|activat\w+ the|inhibit\w+ the)\b", re.I)

HUMAN_CLIN = re.compile(r"\b(patients?|children|trial|randomi[sz]ed|treated|"
                        r"clinical|cohort|human)\b", re.I)
ANIMAL_MECH = re.compile(r"\b(mouse|mice|murine|rat|rabbit|porcine|bovine|"
                         r"knockout|knock-in|Cre|transgenic|-/-)\b", re.I)


def load(p):
    with open(p) as f:
        return yaml.safe_load(f) or {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stub-in", action="store_true")
    a = ap.parse_args()

    hits = []
    for p in sorted(glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"),
                              recursive=True)):
        n = load(p)
        if not isinstance(n, dict) or n.get("stub"):
            continue
        if n.get("claim_grades"):
            continue
        s = " ".join(str(n.get("summary") or "").split())
        if not s:
            continue
        na, nm = len(ASSOC.findall(s)), len(MECH.findall(s))
        nh, nan = len(HUMAN_CLIN.findall(s)), len(ANIMAL_MECH.findall(s))
        why = []
        if na >= 2 and nm >= 2:
            why.append(f"association({na}) + mechanism({nm})")
        if nh >= 2 and nan >= 2:
            why.append(f"human-clinical({nh}) + animal-mechanism({nan})")
        if why:
            hits.append((n["id"], n.get("layer"), n.get("confidence"),
                         n.get("human_evidence"), "; ".join(why), p))

    print(f"nodes with divergent-support summaries: {len(hits)}\n")
    bylayer = {}
    for nid, L, c, he, why, p in hits:
        bylayer.setdefault(L, []).append(nid)
        print(f"  [{L}] {nid}  (conf={c}, he={he})")
        print(f"        {why}")
    print("\nby layer:", {k: len(v) for k, v in sorted(
        bylayer.items(), key=lambda x: int(x[0][1:]))})

    if a.stub_in:
        added = 0
        for nid, L, c, he, why, p in hits:
            txt = open(p).read()
            if "claim_grades:" in txt:
                continue
            scaffold = (
                "claim_grades:   # POPULATED BY SWEEP - grade each claim separately\n"
                f"  - claim: 'TODO: state the association/outcome claim in one sentence'\n"
                f"    grade: {c}\n"
                "    basis: 'TODO'\n"
                f"  - claim: 'TODO: state the mechanistic claim in one sentence'\n"
                "    grade: TODO\n"
                "    basis: 'TODO'\n")
            txt = re.sub(r"^(confidence:\s*\S+\s*)$", r"\1\n" + scaffold,
                         txt, count=1, flags=re.M)
            open(p, "w").write(txt)
            added += 1
        print(f"\nclaim_grades scaffold inserted into {added} nodes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
