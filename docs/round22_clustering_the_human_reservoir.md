# Round 22 — clustering the human growth plate, and what the reservoir turned out to be

**Date:** 2026-08-06 · **Branch:** `claude/growth-system-atlas-yl5esl`

Step 1 of the clock programme, run to an answer. CORR-019 had recorded that three public human
datasets could not test it. That was true of the *gates* I had built, not of the data. Clustering
the data the way its authors did recovers the populations, and the question becomes answerable.

---

## The question

`qu2025` shows in mouse that the long-lived progenitors driving postnatal growth descend from
**Gli1+ cells that sit outside the cartilage**, that cartilage damage recruits them, and that
recruitment restores normal growth. That is the only mechanism in this atlas by which the division
budget could be **added to** rather than merely spent more slowly. Everything downstream of "slow
the clock" depends on whether a human equivalent exists.

## The answer, in one line

**The cells exist. The signalling does not.**

---

## What was found

**Data.** GSE288028, the four **directly processed** biopsies only — the other ten libraries are
24 h explant arms, and 24 h of culture changes exactly what a progenitor question is most
sensitive to. 27,704 cells → 27,620 after QC. Harmony on donor, leiden 1.0, 28 clusters.

**A genuine human stromal population — cluster 0, 1,374 cells, three donors (797/495/82):**

| marker | stromal | chondrocyte | ratio |
|---|---|---|---|
| COL1A1 | 101.0 | 0.18 | **572.8×** |
| PRRX1 | 3.49 | 0.26 | **13.3×** |
| PDGFRA | 2.82 | 2.30 | 1.2× (78% of cells positive) |
| COL2A1 | 6.39 | 579.0 | 0.01× — **at its own donors' ambient floor** |

**And Hedgehog is off in it:**

| gene | stromal | chondrocyte | ratio |
|---|---|---|---|
| **GLI1** | 0.053 | 0.180 | **0.30** |
| **PTCH1** | 0.787 | 9.787 | **0.08** |
| **HHIP** | 0.114 | 3.501 | **0.03** |
| GLI2 | 0.630 | 2.866 | 0.22 |
| GLI3 | 2.545 | 3.537 | 0.72 |

GLI1 cleared its pre-declared 50-count floor (233 pooled), so the comparison was made rather than
refused. **Every direct Hedgehog target is depleted.** The mouse reservoir is *defined* by Gli1 —
it is found, traced and recruited through Hedgehog responsiveness. The human population that
matches it on COL1A1, PRRX1 and PDGFRA does not match it on the property that makes it a reservoir.

**Where GLI1 is instead.** Inside the cartilage. The highest GLI1 clusters are 6 (0.289) and 12
(0.283); the only two clusters carrying the resting-zone marker SFRP5 above 0.08 are cluster 6
(1.831) and cluster 7 (4.279), and both are in the **top four of 28** for GLI1. The stromal cluster
is 0.053 and immune clusters run 0.004–0.052. Recorded as a **descriptive ordering, not a
correlation** — cluster 12 is GLI1-high with SFRP5 at 0.074, so this is not a clean axis, and a
rank statistic on two SFRP5-positive clusters would be a weak test I did not run. What it supports
is the negative: whatever GLI1 marks in the human pubertal plate, it is **not** the
extra-cartilaginous stroma. `avijgan2026br` independently places SFRP5+ cells in the resting zone,
on a different sample set with a different instrument.

---

## The method that made it readable, and the two ways I got it wrong

**Ambient RNA is the whole problem.** In a ~95%-cartilage biopsy, COL2A1 is "detected" in 90% of
cells in a cluster that is 98% PTPRC-positive. Detection fraction is useless, and every threshold
I could pick would be a parameter chosen to get an answer. **CORR-018** and the first clustering
guard both died on this.

**The fix is an internal control.** Immune cells cannot transcribe COL2A1, so their COL2A1 level
*is* the ambient floor, measured in the sample, with no parameter to choose. Measured: immune
1.78, chondrocyte 579.0 — **326× separation.**

That method is right. I then applied it twice wrongly.

**CORR-020 — a swallowed exception silently downgraded the method and the log line lied about
why.** `try: harmony_integrate(...) except: rep="X_pca"` printed *"harmonypy unavailable."*
harmonypy was installed and harmony ran to convergence; what raised was scanpy transposing
harmonypy 2.0's already-correct `Z_corr` orientation. Clustering ran on **uncorrected PCA** while
reporting a cause the exception had never established. Fixed by calling harmonypy directly, with
an explicit shape expectation and an assertion that the coordinates actually moved. No `except`.

**CORR-021 — ambient RNA is a property of a library, and I measured it globally.** With harmony
applied the stromal cluster got *better* on every marker and then **failed** its COL2A1 guard at
15.1× ambient — after passing at 2.3× on the broken clustering. The guard was right, the reference
was wrong:

| donor | cells | immune cells | own COL2A1 ambient |
|---|---|---|---|
| donor1 | 5,243 | 1,498 | 2.00 |
| donor2 | 12,891 | 6,382 | 2.71 |
| **donor3** | 9,111 | **9** | not measurable |
| donor4 | 375 | 71 | 0.62 |

The immune compartment is ~99% donor1+donor2; donor3 is the cartilage-saturated library. Batch
correction did its job and merged donor3 cells into the stromal cluster, and scoring them against
a donor1/2 floor inflated its apparent COL2A1 sixfold. **The fix is a per-donor floor, not a
looser ceiling** — and **donor3 is dropped entirely** rather than judged against someone else's
reference, which costs the most cartilage-rich library and cuts the chondrocyte comparison group
from ~7,900 cells to 890. That is the honest price.

**The near-miss is the part worth keeping.** v1's guards passed *because* the clustering was
broken — the uncorrected run left donor3 out of the stromal cluster, so the global floor happened
to fit. **A guard that passes for a reason you have not checked has not passed.**

**One v1 number reversed and is withdrawn.** GLI3 was 5.05× enriched in the stromal population on
uncorrected clusters and is **0.72×** on corrected ones. The sentence "only GLI3, predominantly a
Hedgehog repressor, is up" is retracted — no Hedgehog gene is up. The primary verdict held and
strengthened, 0.47 → 0.30.

---

## What this does and does not license

**It does not show that no human reservoir exists.** It shows that **GLI1 is the wrong handle** on
which to find or recruit one in the human pubertal plate. Three things it cannot reach:

1. **Position.** Dissociated scRNA-seq infers "outside the cartilage" from transcriptome. These
   cells are COL2A1-negative and COL1A1-high, which is an identity, not a location.
2. **Recruitment.** `qu2025` recruits the reserve by cartilage **damage**. A population that is
   Hedgehog-off *at rest* is not thereby Hedgehog-**unresponsive**. No human sample can be taken
   under that condition.
3. **The constitution window.** These biopsies are 12–14 y, Tanner 2–4. The mouse reserve is
   constituted at about 3 postnatal weeks. The human equivalent of that window is unsampled.

**Grading.** The three human rows are this atlas's own re-analysis and are graded **D
individually** — one public dataset, four libraries of which one is excluded, no positional
information, no independent cohort, no published cluster annotation to check against. The node
holds at **C**. A re-analysis is graded as anyone else's would be. What changed is the node's
**reach**: `progenitor_reservoir_outside_the_plate` goes `human_evidence: absent → direct`, and
`g_l2_human_progenitor_reservoir` goes from unasked to partly answered with the residue stated.

## What the remaining experiment now is

The cheap route is spent. It took three instruments, four guard failures and four corrections to
reach a readable answer, and the spatial data is too shallow for Hedgehog components (PTCH1 45,
GLI1 60 pooled counts across 14 sections). What is left is specific:

1. **A targeted in-situ panel** — Xenium or RNAscope — for GLI1, PTCH1, PDGFRA, COL1A1, COL2A1 on
   an **intact** human growth plate section. Supplies the position dissociation destroys and the
   depth RRST lacks.
2. **`chu2026`'s explant, injured.** It survives two months. The mouse result is about recruitment
   on damage, and nothing observed at rest can test it. This is the one experiment in the list
   that a human tissue model can actually run.
3. **A younger cohort**, to sample the window in which the reserve would be constituted rather
   than the pubertal window in which it would already be spent.

---

## Atlas state

632 nodes · 1,226 edges · 311 gaps · 1,120 refs · **0 validator errors**
Confidence: A 156 · B 191 · C 188 · D 82 · E 13 · X 2

Tools: `cluster_gse288028.py` (harmony fixed), `reservoir_v2.py` (per-donor ambient reference).
Outputs: `query/clusterout_harmony/`, `query/reservoir_v2.json`.
Corrections **CORR-020**, **CORR-021**.
