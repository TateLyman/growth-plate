#!/usr/bin/env python3
"""
F-R013 — recover and re-score the 87 corrupted rows of atlas/data/round436/coverage.json.

The bug: 87 rows carry a spreadsheet CELL REFERENCE ("A10", "D15", "G16") in the
`concept` field instead of the concept's name. The real name survives inside the
`note` field, which is a column-wise splice of the source spreadsheet row.

Consequence: every tier/n_nodes/n_gaps score on those rows was computed by grepping
the atlas for the string "A10" / "D15" / "G16". That is a coin toss:
  - 53 rows came back ZERO   -> false alarm  (the real concept IS covered)
  - 27 rows came back COVERED -> false all-clear (matched a garbage substring)

This script recovers the concept name and re-scores it against the real graph.
Read-only with respect to atlas/.
"""
import json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
COV  = os.path.join(ROOT, "atlas", "data", "round436", "coverage.json")
GRID = re.compile(r"^[A-Z]\d{2}$")

def recover_name(note):
    """The real concept name is the first segment after the spliced header."""
    if not note:
        return None
    # the header is the leading '**...**' run; the concept follows the first ': '
    segs = note.split(": ")
    if len(segs) < 2:
        return None
    cand = segs[1].split(" | ")[0].strip()
    cand = cand.strip("*").strip()
    return cand or None

def searchable_terms(name):
    """Turn a recovered concept name into greppable terms."""
    if not name or name.lower() in ("n/a", "none", "gene-level"):
        return []
    # gene symbols and distinctive multiword phrases
    terms = set()
    for sym in re.findall(r"\b[A-Z][A-Z0-9]{2,}[0-9A-Z]?\b", name):
        if sym not in ("DOES", "AND", "NOT", "THE", "HUMAN", "MOUSE", "INDEX", "NUMBER"):
            terms.add(sym)
    head = re.split(r"[—\-–(/|]", name)[0].strip().strip('"')
    words = head.split()
    # progressively shorter prefixes: a full-phrase grep undercounts badly
    # ("Groove of Ranvier progenitor" -> 3 files; "Groove of Ranvier" -> 42)
    for n in (len(words), 4, 3, 2):
        if 2 <= n <= len(words):
            frag = " ".join(words[:n])
            if len(frag) > 7:
                terms.add(frag)
    if not terms and len(name) > 5:
        terms.add(name[:40])
    return sorted(terms)

def grep_count(term):
    try:
        r = subprocess.run(
            ["grep", "-rilF", "--", term,
             os.path.join(ROOT, "atlas"), os.path.join(ROOT, "docs")],
            capture_output=True, text=True, timeout=120)
        return len([l for l in r.stdout.splitlines() if l.strip()])
    except Exception:
        return -1

def main():
    rows = json.load(open(COV))["rows"]
    grid = [r for r in rows if GRID.match(str(r.get("concept", "")))]
    print("corrupted (grid-reference) rows: %d of %d\n" % (len(grid), len(rows)))

    out, flips = [], {"false_alarm": 0, "false_all_clear": 0, "confirmed": 0, "unknown": 0}
    for r in grid:
        name  = recover_name(r.get("note"))
        terms = searchable_terms(name)
        best  = max((grep_count(t) for t in terms), default=-1) if terms else -1
        old, real = r["tier"], None
        if best < 0:
            real, k = "UNSCORABLE", "unknown"
        elif best == 0:
            real = "ZERO"
            k = "confirmed" if old == "ZERO" else "false_all_clear"
        elif best < 5:
            real = "THIN"
            k = "false_all_clear" if old == "COVERED" else ("false_alarm" if old == "ZERO" else "confirmed")
        else:
            real = "COVERED"
            k = "false_alarm" if old == "ZERO" else "confirmed"
        flips[k] += 1
        out.append({"cell": r["concept"], "domain": r["domain"], "recovered_concept": name,
                    "terms": terms, "files_matching": best,
                    "tier_as_recorded": old, "tier_recomputed": real, "verdict": k})

    for o in sorted(out, key=lambda x: -(x["files_matching"] or 0)):
        print("%-5s %-11s rec=%-9s was=%-9s files=%-4s  %s"
              % (o["cell"], o["verdict"][:11], o["tier_recomputed"], o["tier_as_recorded"],
                 o["files_matching"], (o["recovered_concept"] or "")[:64]))

    print("\n" + "=" * 78)
    print("false_alarm     (recorded ZERO, actually covered) : %d" % flips["false_alarm"])
    print("false_all_clear (recorded COVERED/THIN, actually thinner): %d" % flips["false_all_clear"])
    print("confirmed                                          : %d" % flips["confirmed"])
    print("unscorable                                         : %d" % flips["unknown"])
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "recovered.json"), "w"), indent=1)
    print("\nwrote recovered.json")

if __name__ == "__main__":
    main()
