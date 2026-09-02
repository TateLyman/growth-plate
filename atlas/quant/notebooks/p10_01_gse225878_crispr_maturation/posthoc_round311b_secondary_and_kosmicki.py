#!/usr/bin/env python3
"""
ROUND 311b. Three checks that must run BEFORE any hit from the primary screen is believed.

CHECK 1 - THE ARTEFACT STRUCTURE OF THE DELAYED DIRECTION. The strongest delayer in the whole
screen is Cd200 itself, which is the SORTING MARKER. Knocking out the antigen the sort is
performed on makes a cell CD-200-low, which the assay must score as immature. That is a pure
readout artefact and it is rank 1. Everything below it has to be read knowing that. The second
signature is multicopy families: histone H2ac* genes and dozens of Gm* predicted genes appear
with IDENTICAL log fold changes, which is what happens when one guide maps to many paralogous
loci and the cell dies of multiple double-strand breaks rather than of anything to do with
cartilage. This check counts both so the contamination is quantified, not hand-waved.

CHECK 2 - THE SECONDARY SCREEN. baronas2023 re-screened 162 significant genes plus 47 controls.
A primary hit that did not go forward, or went forward and failed, is not a validated hit.

CHECK 3 - CROSS AGAINST kosmicki2026's 207 HUMAN HEIGHT GENES. This is the join the atlas has
wanted since round 283: human burden effect in centimetres on one axis, causal chondrocyte
maturation timing on the other. A gene with a POSITIVE human beta (loss makes people taller)
whose knockout DELAYS maturation is coherent - longer period, taller adult. A positive human
beta whose knockout ACCELERATES maturation is incoherent and the human effect is then probably
not mediated by cell-autonomous chondrocyte timing.
"""
import os
import re
import sys
import json
import collections

sys.path.insert(0, os.path.dirname(__file__))
from analysis import load, LFC_MATURE, LFC_IMMATURE  # noqa: E402

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "..", "..", "data", "round311")
S6 = os.path.join(HERE, "..", "..", "..", "data", "round300", "s6_burden_effects.json")


def main():
    d4, d15 = load("prim_d4"), load("prim_d15")
    s4, s15 = load("sec_d4"), load("sec_d15")

    def best(g, a, b):
        r = None
        for tag, v in (("D4", a.get(g)), ("D15", b.get(g))):
            if v and v[1] >= 3.0 and (v[0] > LFC_MATURE or v[0] < LFC_IMMATURE):
                if r is None or v[1] > r[2]:
                    r = (tag, v[0], v[1])
        return r

    delayed, early = [], []
    for g in d4:
        r = best(g, d4, d15)
        if not r:
            continue
        (delayed if r[1] < 0 else early).append((g, r))

    # ---------------- CHECK 1 ----------------
    print("=" * 78)
    print("CHECK 1  ARTEFACT STRUCTURE OF THE DELAYED DIRECTION")
    print("=" * 78)
    is_predicted = re.compile(r"^(Gm\d+|\d+\w*Rik|Speer|Rps\d|Rpl\d)")
    is_histone = re.compile(r"^(H1f|H2a|H2b|H3c|H4c|Hist)")
    lfc_groups = collections.Counter(round(r[1], 3) for _, r in delayed)
    dup = {k: v for k, v in lfc_groups.items() if v >= 3}
    npred = sum(1 for g, _ in delayed if is_predicted.match(g))
    nhist = sum(1 for g, _ in delayed if is_histone.match(g))
    ndup = sum(v for v in dup.values())
    print("  delayed n=%d   accelerated n=%d" % (len(delayed), len(early)))
    print("  Cd200 (the sorting antigen itself) rank in delayed list: %d"
          % (1 + sorted(delayed, key=lambda x: -x[1][2]).index(
              [d for d in delayed if d[0] == "Cd200"][0])))
    print("  predicted/pseudogene/ribosomal symbols : %3d  (%.0f%%)" % (npred, 100.0 * npred / len(delayed)))
    print("  histone-cluster symbols                : %3d  (%.0f%%)" % (nhist, 100.0 * nhist / len(delayed)))
    print("  in an LFC value shared by >=3 genes     : %3d  (%.0f%%)  <- one guide, many paralogues"
          % (ndup, 100.0 * ndup / len(delayed)))
    clean = [(g, r) for g, r in delayed
             if not is_predicted.match(g) and not is_histone.match(g)
             and lfc_groups[round(r[1], 3)] < 3 and g != "Cd200"]
    print("  SURVIVING CLEAN DELAYERS               : %3d" % len(clean))
    # same for accelerated
    epred = sum(1 for g, _ in early if is_predicted.match(g) or is_histone.match(g))
    print("  (accelerated direction, same filters   : %d of %d are predicted/histone)"
          % (epred, len(early)))
    print()
    print("  CLEAN DELAYERS, ranked:")
    for g, r in sorted(clean, key=lambda x: -x[1][2]):
        print("    %-12s %s LFC %+7.3f  -log10p %6.2f" % (g, r[0], r[1], r[2]))
    print()
    print("  ACCELERATORS (rare direction), ranked:")
    for g, r in sorted(early, key=lambda x: -x[1][2])[:30]:
        print("    %-12s %s LFC %+7.3f  -log10p %6.2f" % (g, r[0], r[1], r[2]))

    # ---------------- CHECK 2 ----------------
    print()
    print("=" * 78)
    print("CHECK 2  SECONDARY SCREEN (%d genes carried forward)" % len(s4))
    print("=" * 78)
    watch = ["Chd8", "Prkar1a", "Kdm1a", "Brd2", "Cop1", "Sufu", "Ptch1", "Eed", "Ezh2",
             "Suz12", "Gnas", "Cd200", "Atp2b1", "Ywhae", "Med26", "Ccm2"]
    for g in watch:
        a, b = s4.get(g), s15.get(g)
        pa = d4.get(g), d15.get(g)
        fa = "%+.3f p%.2f" % (a[0], a[1]) if a else "not carried forward"
        fb = "%+.3f p%.2f" % (b[0], b[1]) if b else "not carried forward"
        print("  %-9s primary D4 %+7.3f / D15 %+7.3f  ->  secondary D4 %-18s D15 %s"
              % (g, pa[0][0] if pa[0] else float("nan"),
                 pa[1][0] if pa[1] else float("nan"), fa, fb))

    # ---------------- CHECK 3 ----------------
    print()
    print("=" * 78)
    print("CHECK 3  CROSS AGAINST kosmicki2026's HUMAN HEIGHT GENES (cm per allele)")
    print("=" * 78)
    if not os.path.exists(S6):
        print("  s6_burden_effects.json not found - skipped")
        return
    s6 = json.load(open(S6))
    # Schema of s6_burden_effects.json (round 300): a flat list of dicts with keys
    # gene / cat / aaf / eff (centimetres) / se / p / aac_het / omim / constrained.
    # Take the most significant PURE pLoF row per gene - the closest genetic analogue of
    # pharmacological loss of function, and the same rule round 300 used.
    human = {}
    for r in s6:
        if r.get("cat") != "pLoF":
            continue
        g = r["gene"]
        if g not in human or r["p"] < human[g][1]:
            human[g] = (r["eff"], r["p"])
    print("  parsed %d human genes with a pure-pLoF row" % len(human))

    both = []
    for g, r in delayed + early:
        h = g.upper()
        if h in human:
            beta, p = human[h]
            coherent = (beta > 0 and r[1] < 0) or (beta < 0 and r[1] > 0)
            both.append((h, beta, p, r[0], r[1], r[2], coherent))
    both.sort(key=lambda x: -abs(x[1]))
    if not both:
        print("  no overlap")
    for h, beta, p, tp, lfc, nlp, coh in both:
        print("    %-9s human %+7.2f cm (P=%.1e)   screen %s LFC %+6.3f (p %.2f)   %s"
              % (h, beta, p, tp, lfc, nlp,
                 "COHERENT - longer period, taller" if coh else "INCOHERENT"))

    json.dump({"clean_delayers": [[g, r[0], r[1], r[2]] for g, r in clean],
               "accelerators": [[g, r[0], r[1], r[2]] for g, r in early],
               "artefact_counts": {"predicted": npred, "histone": nhist,
                                   "shared_lfc": ndup, "total_delayed": len(delayed)},
               "kosmicki_join": both},
              open(os.path.join(OUT, "gse225878_filtered_and_joined.json"), "w"), indent=1)
    print()
    print("  wrote gse225878_filtered_and_joined.json")


if __name__ == "__main__":
    main()
