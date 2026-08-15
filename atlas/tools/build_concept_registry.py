#!/usr/bin/env python3
"""
build_concept_registry.py
=========================
Turns the EXTERNAL domain enumerations in atlas/concepts/enumerations/*.md into the
machine-readable registry that concept_coverage_map.py scores against the atlas.

WHY IT IS A SEPARATE STEP
    The enumerations are written by agents searching the outside literature, deliberately
    without reading this repository (deriving the concept list from the node graph is
    circular and returns exactly what is already there). This tool is the only place the
    two ever meet, and it does no judging - it just normalises.

WHAT IT PARSES
    Any GitHub-flavoured markdown table whose header row's FIRST column names the concept.
    Column meanings are inferred from the header text, because each domain brief specifies
    a different layout:
        first column          -> concept
        header contains DIRECTION / EFFECT / HEIGHT   -> direction
        header contains OBSCURE                       -> obscure flag
        header contains PMID / EVIDENCE / SOURCE      -> source
        header contains GENE                          -> extra aliases
        anything else                                 -> folded into note
    Rows whose first cell is empty, a separator, or a repeated header are dropped.

ALIASES - THE PART THAT MATTERS (CORR-353)
    A grep that misses on vocabulary is still a failed grep: this project called energy
    restriction DIETARY RESTRICTION and a search for "caloric restriction" returned nothing
    while a fully worked node had existed for 250 rounds. So aliases are generated, not
    optional:
      * parenthetical content            "Aggrecan (ACAN)"        -> ACAN
      * slash and 'or' alternatives      "CNP/NPPC"               -> CNP, NPPC
      * gene-symbol-shaped tokens        SOX9, SLC26A2, IGF1R     -> kept verbatim
      * numeric family expansion         "PLOD1-3"                -> PLOD1, PLOD2, PLOD3
      * the GENES column where present
    Aliases shorter than 3 characters are dropped - they generate noise, not hits.

USAGE
    python3 atlas/tools/build_concept_registry.py
    python3 atlas/tools/build_concept_registry.py --check      # parse, report, write nothing
"""
from __future__ import annotations

import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("pyyaml required", file=sys.stderr)
    raise

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(HERE)
ENUM_DIR = os.path.join(HERE, "concepts", "enumerations")
OUT = os.path.join(HERE, "concepts", "concept_registry.yaml")

# Tokens that look like gene symbols / identifiers worth keeping as aliases.
GENEISH = re.compile(r"^[A-Z][A-Z0-9]{1,9}[0-9A-Z]$")
FAMILY = re.compile(r"^([A-Z]+?)(\d+)\s*[-–]\s*(\d+)$")
STOPWORDS = {
    "THE", "AND", "FOR", "NOT", "YES", "ALL", "ANY", "NONE", "N/A", "NA", "TBD",
    "UNVERIFIED", "UNKNOWN", "HUMAN", "MOUSE", "RAT", "PMID", "OBSCURE", "TALL",
    "SHORT", "BOTH", "MIXED", "UP", "DOWN", "NULL",
}


def split_row(line: str) -> list[str] | None:
    s = line.strip()
    if not s.startswith("|"):
        return None
    cells = [c.strip() for c in s.strip("|").split("|")]
    return cells


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells if c != "")


def strip_md(s: str) -> str:
    """Agents write **bold**, *italic*, `code` and stray backslashes into cells."""
    s = re.sub(r"[*`\\]", "", str(s or "")).strip()
    return re.sub(r"\s+", " ", s)


def concept_col(headers: list[str]) -> int:
    """Several agents prepend a row-number column headed '#'. The concept is then in
    column 1, not column 0, and taking column 0 silently drops the entire table."""
    h0 = strip_md(headers[0]).upper() if headers else ""
    if h0 in ("#", "N", "NO", "NO.", "ID", "IDX", "ROW", "") and len(headers) > 1:
        return 1
    return 0


def classify_headers(headers: list[str]) -> dict:
    c0 = concept_col(headers)
    role = {}
    for i, h in enumerate(headers):
        H = strip_md(h).upper()
        if i == c0:
            role[i] = "concept"
            continue
        if i < c0:
            role[i] = "index"
        elif "OBSCURE" in H:
            role[i] = "obscure"
        elif "DIRECTION" in H or "EFFECT" in H or ("HEIGHT" in H and "DIRECTION" not in H):
            role.setdefault(i, "direction")
        elif "PMID" in H or "EVIDENCE" in H or "SOURCE" in H or "URL" in H:
            role.setdefault(i, "source")
        elif "GENE" in H:
            role.setdefault(i, "genes")
        else:
            role[i] = "note:" + h.strip()
    return role


def expand_family(tok: str) -> list[str]:
    m = FAMILY.match(tok)
    if not m:
        return []
    stem, a, b = m.group(1), int(m.group(2)), int(m.group(3))
    if b < a or b - a > 12:
        return []
    return ["%s%d" % (stem, n) for n in range(a, b + 1)]


def derive_aliases(concept: str, genes_cell: str) -> list[str]:
    out: list[str] = []

    # parenthetical content
    for chunk in re.findall(r"\(([^)]{2,60})\)", concept):
        for part in re.split(r"[,/;]| or ", chunk):
            part = part.strip()
            if len(part) >= 3:
                out.append(part)

    # slash / 'or' alternatives in the bare concept (parentheses stripped)
    bare = re.sub(r"\([^)]*\)", " ", concept)
    if "/" in bare:
        for part in bare.split("/"):
            part = part.strip(" -–.,;")
            if 3 <= len(part) <= 40 and part.upper() not in STOPWORDS:
                out.append(part)

    # gene-symbol-shaped tokens anywhere in the concept and in the GENES column
    for src in (concept, genes_cell or ""):
        for tok in re.split(r"[^A-Za-z0-9\-]+", src):
            tok = tok.strip("-")
            if not tok or tok.upper() in STOPWORDS:
                continue
            fam = expand_family(tok.upper())
            if fam:
                out.extend(fam)
                continue
            if GENEISH.match(tok) and len(tok) >= 3:
                out.append(tok)

    seen, uniq = set(), []
    for a in out:
        k = a.lower()
        if k in seen or len(a) < 3 or a.lower() == concept.lower():
            continue
        seen.add(k)
        uniq.append(a)
    return uniq[:14]


def parse_file(path: str, domain: str) -> list[dict]:
    concepts: list[dict] = []
    headers: list[str] | None = None
    role: dict = {}

    with open(path, encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            cells = split_row(line)
            if cells is None:
                # a blank line or prose ends the current table
                if line.strip() == "":
                    headers = None
                continue
            if is_separator(cells):
                continue
            if headers is None:
                headers = cells
                role = classify_headers(cells)
                continue
            if not cells:
                continue
            cidx = concept_col(headers)
            # a section-divider row like "| **A. ENERGY AND MACRONUTRIENTS** |" has one real cell
            if sum(1 for c in cells if c.strip()) <= 1:
                continue
            if cidx >= len(cells):
                continue
            first = cells[cidx]
            if not first.strip():
                continue
            # a repeated header inside the same table
            if strip_md(first).upper() == strip_md(headers[cidx] if cidx < len(headers) else "").upper():
                continue
            name = strip_md(first)
            name = re.sub(r"^\d+[.)]?\s+", "", name)
            if len(name) < 3 or name.upper() in STOPWORDS:
                continue

            rec: dict = {"concept": name, "domain": domain}
            notes: list[str] = []
            genes_cell = ""
            for i, cell in enumerate(cells):
                r = role.get(i)
                if not r or r == "index" or i == cidx or not cell:
                    continue
                cell = strip_md(cell)
                if not cell:
                    continue
                if r == "obscure":
                    rec["obscure"] = strip_md(cell).lower().startswith("y")
                elif r == "direction":
                    rec.setdefault("direction", cell)
                elif r == "source":
                    rec.setdefault("source", cell)
                elif r == "genes":
                    genes_cell = cell
                    notes.append("genes: " + cell)
                elif r.startswith("note:"):
                    notes.append(r[5:] + ": " + cell)
            al = derive_aliases(name, genes_cell)
            if al:
                rec["aliases"] = al
            if notes:
                rec["note"] = " | ".join(notes)[:400]
            concepts.append(rec)
    return concepts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--out", default=OUT)
    args = ap.parse_args()

    if not os.path.isdir(ENUM_DIR):
        print("no enumerations at %s" % os.path.relpath(ENUM_DIR, ROOT), file=sys.stderr)
        sys.exit(1)

    all_concepts: list[dict] = []
    per_file: list[tuple[str, int]] = []
    for fn in sorted(os.listdir(ENUM_DIR)):
        if not fn.endswith(".md"):
            continue
        domain = re.sub(r"^\d+_", "", fn[:-3])
        got = parse_file(os.path.join(ENUM_DIR, fn), domain)
        per_file.append((fn, len(got)))
        all_concepts.extend(got)

    # de-duplicate on lowercased concept name, keeping the first and merging aliases
    merged: dict[str, dict] = {}
    for c in all_concepts:
        k = c["concept"].lower()
        if k in merged:
            a = set(merged[k].get("aliases") or []) | set(c.get("aliases") or [])
            if a:
                merged[k]["aliases"] = sorted(a)[:14]
            if c["domain"] not in merged[k]["domain"]:
                merged[k]["domain"] = merged[k]["domain"] + "+" + c["domain"]
        else:
            merged[k] = c

    rows = list(merged.values())
    n_obscure = sum(1 for r in rows if r.get("obscure"))
    print("parsed %d files" % len(per_file))
    for fn, n in per_file:
        print("  %-44s %4d rows" % (fn, n))
    print("total %d rows -> %d unique concepts (%d marked obscure)"
          % (len(all_concepts), len(rows), n_obscure))

    if args.check:
        return
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        fh.write("# GENERATED by atlas/tools/build_concept_registry.py - do not hand-edit.\n")
        fh.write("# Source: atlas/concepts/enumerations/*.md (external enumeration, R436).\n")
        yaml.safe_dump({"concepts": rows}, fh, sort_keys=False, allow_unicode=True, width=100)
    print("written: %s" % os.path.relpath(args.out, ROOT))


if __name__ == "__main__":
    main()
