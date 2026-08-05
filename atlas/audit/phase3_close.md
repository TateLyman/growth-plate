# Phase 3 close — integration results

Recorded here because the L8 sweep's output was swept into the tree by a concurrent
merge while other commits were in flight, so its findings are in the repository but
were never described in a commit message. This file closes that provenance gap.

**State at close:** 614 nodes (0 stubs) · 1,181 edges · 279 gaps · 136 search logs ·
1,036 references · 0 validator errors · sign gate 100% of sign-bearing relations.
Confidence: A 156 · B 186 · C 184 · D 75 · E 11 · X 2.
**All 14 layers pass the gap quota.**

---

## 1. The structural result: the atlas stopped being fourteen lists

| seam | before | after |
|---|---:|---:|
| L4 → L3 — systemic hormone onto local pathway | **1** | **41** |
| L6 → L1 — mechanics onto architecture | 0 | 51 |
| L5 → L1 — matrix onto architecture | 0 | 49 |
| L11 → L3 — disease onto mechanism | 0 | 27 |
| L2 → L7 — stem biology onto fusion | 4 | 15 |
| L8 → L3 — genetic dosage onto mechanism | 0 | 12 |
| L6 → L5 — mechanics onto matrix | 0 | 11 |
| L1 ↔ L2 | 0 / 0 | 3 / 3 |

**Intra:cross ratio inverted from 1.3:1 to 0.65:1.** Cross-layer edges (717) now
outnumber intra-layer edges (464). Density 1.25 → 1.92 against a 3.0 target.

`timescale` went from 0% to 32% fill. Context fill rose but remains the weak spot:
zone 5.2%, stage 13.0%, sex 9.7%.

---

## 2. The propositional-replication rule, exercised for the first time

**2 accepted, 10 rejected — an 83% rejection rate.**

That number is the finding. The rule (MR-001 item 2) was written to measure how thin
genuinely replicated human evidence is. The answer: **five in six apparent
replications are not replications.** Two failure patterns account for all ten:

1. the node's grade was set by a **different claim** than the one the second paper
   tests (6 cases), and
2. the "replication" was a curation or aggregation **not source-independent** of
   ref_1 (2 cases).

**The sharpest rejection is `height_gwas`**, which an earlier audit in this same build
had nominated for re-upgrade to A. Rejected **on nesting**: Wood 2014 and Wainschtein
2026 sit *inside* Yengo 2022's 5.4 million participants. The field cannot
independently replicate its own flagship height estimate, because the candidate
replications are subsets of it.

`aggrecan_acan` failed in precisely the way the rule predicts — ACAN dosage is not
aggrecan turnover kinetics — which is the worked example the rule was written around.

The two **accepted** upgrades are genuine:
- `estrogen_receptor_alpha` B→A: mouse ERα-null continued growth **plus** the human
  ESR1-null case (204 cm, unfused epiphyses *despite elevated estradiol*). Different
  species, and the human case controls a confound the mouse cannot.
- `schmid_metaphyseal_chondrodysplasia` B→A: 1993 single-kindred linkage (lod 18.2)
  plus a 2025 128-unrelated-case mutation spectrum.

---

## 3. Two of the four Phase 3b ranking axes already disagree

Recorded as node `common_vs_rare_pathway_divergence` (grade C).

| ranking | dominated by |
|---|---|
| **Common-variant enrichment** (Weedon 2008, Lango Allen 2010, Wood 2014) | paracrine signalling and matrix — Hedgehog, FGF, WNT/β-catenin, chondroitin sulfate, mTOR |
| **Rare Mendelian burden** (771 disorders, 552 genes, ClinGen) | structural collagens and the GH–IGF endocrine axis |

**0 of 3 GWAS enrichment lists name the somatotropic axis** — the source of the
largest monogenic stature effects in medicine (GHR −4 to −10 SDS, STAT5B −7.8 SDS).
Convergence is limited to Hedgehog, CNP/NPR2 and proteoglycan/GAG synthesis.

This matters for Phase 3b: two of the four axes disagree *before* elasticity is
computed. The buffering explanation (common variation is depleted where rare variation
is catastrophic) is held at **grade E with a discriminating test**, not asserted.

---

## 4. The pattern that recurred three times

Three independent findings in this build share one shape: **a mechanism everyone
repeats, an alternative present in the system and never excluded, and no primary that
actually tested it.**

| finding | the untested alternative |
|---|---|
| **ANKH exports ATP, not PPi** (CORR-001) | ENPP1 was present in the cells where PPi transport was inferred |
| **PKG-II loss expands the plate 2.6×** while NPR2 loss shrinks it to 23% (CORR-003) | cGKI, co-expressed at *higher* zonal enrichment (5.9× vs 4.4×); the double knockout both primaries proposed has never been made |
| **IGF1R → mTORC1 in cartilage is unsubstantiated** | the one cartilage experiment coupling this family to mTORC1 used **insulin**, not IGF-1 |

CORR-003 sits in the effector step of the pathway vosoritide targets, and compounds
contradiction C-L3-03 and hypothesis H1 from MR-002 — three independent routes now
converge on the same suspicion about CNP-analogue mechanism.

---

## 5. Process notes worth keeping

- **A fully-researched cross-layer duplicate survived eight sweeps.**
  `acan_dosage_effect` (L5) and `acan_related_short_stature` (L11) were the same
  entity — same cohort (103 individuals, 20 families), same three headline numbers,
  two aliases verbatim in common. `graph.py --duplicates` is structurally blind to it
  because the two ids share no substring. DESIGN_DECISIONS D2 amended.
- **Searches falsified drafts mid-write**, twice: `epigenetic_clock_growth` was
  drafted at grade X, the search returned Simpkin 2017 and Kim 2024, and it was
  re-graded D with the gap re-scoped.
- **Every DOI hand-guessed during drafting turned out wrong** and was replaced from
  the live record — the anti-fabrication design doing exactly what it exists for.
- **An agent refused to pad an empty seam.** L6→L5 rests on one 48-hour swine explant
  study; three null sweeps (2,564 / 517 / 4,398 hits, 0 qualified). It wrote 11 edges
  against an explicit density target rather than manufacture more.

---

## 6. Outstanding at close

- **Density 1.92 vs 3.0.** Remaining headroom is in seams not yet worked (L0/L9/L10
  into the core beyond the first pass) and in intra-layer L3, the densest layer.
- **Phase 3b elasticity** not computed; Type 4 queries remain structurally
  unanswerable and QUERY.md says so.
- **Context fill** (zone 5.2%, sex 9.7%) still limits context-filtered perturbation.
- **Phase 3c** full cycle inventory with timescales: `timescale` is now 32% filled,
  enough to begin but not to complete.
