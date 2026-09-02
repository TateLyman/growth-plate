#!/usr/bin/env python3
"""
Repair citations whose ref_id points at the wrong bibliography entry.

WHY THIS EXISTS
Two different papers can independently receive the same generated ref_id in two
different shards (e.g. two 2026 papers by different authors named Li both slug to
`li2026`). On merge, one keeps the id and the other is renamed `li2026_2`, and the
rename has to be rewritten across the files that cited it. Two things can leave a
citation pointing at the wrong paper:

  1. a rewrite applied with too broad a scope (fixed: rewrites are now scoped to
     the supplying shard's layer), and
  2. a race - a subagent rewriting its node files while a merge is in progress,
     so the merge's rewrite is overwritten by the agent's older text.

Neither is detectable by "does this id resolve" - the id always resolves, just to
the wrong study. The node's own `pmid` field is the ground truth, because the
agent wrote it from the record it actually read.

WHAT IT DOES
For every node key_ref that declares a pmid, compare against the bibliography
entry its ref_id names. On disagreement, repoint the ref_id at whichever entry
actually carries that pmid. Also repairs `source_ref` on quantitative rows that
used the same wrong id.

Run after every merge_shards.py, and again once all sweeps have finished.

Usage:
  python3 atlas/tools/fix_citations.py            # repair
  python3 atlas/tools/fix_citations.py --check    # report only
"""
import os, sys, glob, re, argparse
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    bib_p = os.path.join(ROOT, "sources", "bibliography.yaml")
    bib = (yaml.safe_load(open(bib_p)) or {}).get("refs", {})

    pmid2rid = {}
    for k, v in bib.items():
        if not isinstance(v, dict):
            continue
        pm = str(v.get("pmid") or "").strip()
        if pm:
            pmid2rid.setdefault(pm, k)

    fixed, unfixable, checked = [], [], 0
    for p in sorted(glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"),
                              recursive=True)):
        txt = open(p).read()
        try:
            n = yaml.safe_load(txt) or {}
        except Exception:
            continue
        if not isinstance(n, dict):
            continue
        changes = []
        for kr in (n.get("key_refs") or []):
            if not isinstance(kr, dict):
                continue
            rid = kr.get("ref_id")
            pm = str(kr.get("pmid") or "").strip()
            if not rid or not pm or rid not in bib:
                continue
            checked += 1
            canon = str(bib[rid].get("pmid") or "").strip()
            if canon and pm != canon:
                correct = pmid2rid.get(pm)
                if correct and correct != rid:
                    changes.append((rid, correct))
                else:
                    # The ref_id resolves but the declared pmid matches nothing in
                    # the bibliography. Almost always a typed-digit error rather than
                    # a missing reference - report it as such, with what the ref_id
                    # actually points at, so it can be judged rather than guessed.
                    unfixable.append((os.path.basename(p), rid, pm,
                                      str(bib[rid].get("pmid")),
                                      str(bib[rid].get("title"))[:60]))
        if changes and not a.check:
            new = txt
            for old, cor in changes:
                new = re.sub(rf"(ref_id:\s*){re.escape(old)}(?![\w-])",
                             rf"\g<1>{cor}", new)
                new = re.sub(rf"(source_ref:\s*){re.escape(old)}(?![\w-])",
                             rf"\g<1>{cor}", new)
            if new != txt:
                open(p, "w").write(new)
        if changes:
            fixed.append((os.path.relpath(p, ROOT), changes))

    print(f"key_refs cross-checked : {checked}")
    print(f"files {'needing repair' if a.check else 'repaired'} : {len(fixed)}")
    for f, c in fixed[:30]:
        print(f"  {f}: {c}")
    if unfixable:
        print(f"\nUNFIXABLE ({len(unfixable)}) - node declares a pmid that is in no "
              f"bibliography entry; add it with addref.py:")
        for row in unfixable[:20]:
            f, rid, pm = row[0], row[1], row[2]
            canon = row[3] if len(row) > 3 else "?"
            title = row[4] if len(row) > 4 else ""
            print(f"  {f}: ref_id '{rid}' declares pmid {pm}, but that ref_id points "
                  f"at pmid {canon} ({title}). PROBABLE TYPO - verify both pmids "
                  f"against the live record before editing.")
    return 1 if (a.check and fixed) else 0


if __name__ == "__main__":
    sys.exit(main())
