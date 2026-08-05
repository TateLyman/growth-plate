# Residual debt report

MR-003 item 3 asked for status on every item that had gone unreported since before
Phase 5, on the grounds that a build which reports only its successes is not audited.
This file is that report, and it is kept as a standing ledger: an item is not removed
when it is done, it is marked done with the number it produced.

**State at writing:** 614 nodes (0 stubs) · 1,181 edges · 279 gaps · 136 search logs ·
1,036 references · 0 validator errors. See the README dashboard for live counts.

---

## 1. Items MR-003 named

| item | status | what it produced |
|---|---|---|
| **MR-001 #1** — ledger reconciliation, 51 vs 53 | **closed** | Neither figure was right. Git reconstruction of the grade-change commits gave **51 files carrying 52 grade events**. The extra event was a rule violation, not a bookkeeping error: `mouse_does_not_fuse` had been moved A→D, three grades in one step, against the one-grade-drop rule. Corrected to A→C. The discrepancy was worth chasing because it surfaced a defect, which is the argument for reconciling ledgers at all. |
| **MR-001 #2** — propositional replication rule + rejected-upgrade log | **closed** | `audit/confidence_upgrades.md`. **2 accepted, 10 rejected — 83% rejection on first exercise.** Five failure patterns, not the two originally reported; see §2 below, because the tally was itself defective and MR-004 #3 caught it. |
| **MR-001 #4** — CORR-001 sweep extension counts | **closed** | `audit/corrections.md` traces the blast radius of each correction object by object: nodes corrected at authoring, edge topology checked (including the diagnostic *absence* of a direct `ankh_transporter → inorganic_pyrophosphate` edge), gap re-framed, quantitative rows checked with the finding that no row attributed a PPi flux to ANKH transport. |
| **Phase 2c** — stub disposition counts | **closed** | `audit/stub_disposition.md`. **Stub fraction is 0.0%**; every stub was either researched or deleted with a stated reason under the admission rule, one line per deletion. |
| **Phase 2d** — canonical-mechanism audit incl. confirmations | **closed** | `audit/mechanism_audit.md`. 12 targets: **4 CONFIRMED · 6 SCOPED · 2 SUPERSEDED · 0 UNVERIFIABLE.** Opened CORR-002 (collagen X) and CORR-003 (PKG-II). 21 references upgraded `primary_abstract_only` → `primary`. Confirmations are recorded, because a node that has been checked and held is a different object from a node that merely has not been contradicted. |
| **Phase 2e** — 5 disputed keys in 811+ rows is implausibly low | **closed, and MR-003 was right** | The criterion was the defect. Keying on the exact parameter-name string meant `peak height velocity, boys` and `peak height velocity (boys)`, written by different sweeps, never matched. Re-run with token-normalised keys **and** with the realisation that **~94% of parameter names appear exactly once**, so disagreement in this atlas is not encoded as duplicate rows at all — it lives in the row's own uncertainty text or in a range-valued `value`. **All 1,350 rows were then classified rather than searched for duplicates.** See §3. |
| **Phase 3** — edge density 0.88 vs ≥3.0 | **superseded by MR-004 #2** | Reached **1.92** with the cross-layer/intra-layer ratio inverted from 1.3:1 to 0.65:1 and every seam populated. MR-004 #2 then retired the 3.0 target on the argument that bare edges at 5% zone fill add size without answerability. The live target is context fill, tracked in §4. |
| **Phase 3b** — elasticity never ran | **closed, and reshaped** | `docs/pathway_matrix.md`. 17 pathways × 5 axes, alphabetical, **no ranking anywhere**, per MR-004 #6. 22 of 85 cells `unmeasured`; final-height elasticity unmeasured for 13 of 17 pathways. Type 4 queries are answerable to the extent the matrix has cells, and the matrix says plainly where it does not. |

## 2. The rejection tally was defective, and the correction is the informative part

Reported as "two patterns covering all ten rejections, counts 6 and 2." That sums to 8.
MR-004 #3 asked which it was — a missing third pattern or a broken tally — and the
answer was both: re-reading the ten gave **five** patterns, and the largest was the one
never named.

**Pattern B — the candidate paper was already cited on the node — accounts for 3 of 10**,
more than any other. A "replication" that is already in the node's own reference list is
not new evidence about the proposition; it is the evidence that produced the grade. A
**STEP 0 novelty precondition** was added to the upgrade rule: before assessing whether
a candidate independently tests the proposition, check that it is not already cited.

## 3. Phase 2e, re-run: what 1,350 rows actually look like

| reliability class | rows |
|---|---:|
| `single_source_with_uncertainty` | 1,226 |
| `range_value` | 116 |
| **`single_source_point_no_uncertainty`** | **65** |
| `spread_documented` | 55 |
| `unverified` | 40 |
| `multi_source` | 12 |
| `superseded` | 2 |

`single_source_point_no_uncertainty` is the risk class and is named as such in the
policy string that ships with `query/parameters.json`: one source, a point value, no
stated uncertainty, nothing to warn a reader. **65 rows, not 5.** Only **12 rows** in
the whole atlas are genuinely multi-source, which is the real answer to MR-003's
suspicion — the field does not re-measure, so the atlas cannot show disputes it was
never given.

## 4. Debt still open

Carried honestly rather than closed by assertion.

| item | state |
|---|---|
| **Context fill** | The live density target under MR-004 #2. Zone, sex, stage and timescale fills are reported by `atlas/tools/context_filter.py --coverage-report` against thresholds of 40/30/40/30%. Until they are met, context-filtered Type 3 answers return **UNRELIABLE** with the coverage figure attached rather than a small-looking result — which is the correct failure mode, but it is a failure mode, not a feature. |
| **Reachability and context filtering share a defect class** | Both were shipped with null-as-exclusion semantics and both were wrong. The second one shipped a benchmark answer that was wrong by more than 30×. No third field has been audited for the same defect. Any future field that can be absent must be checked before it is filtered on. |
| **`structural_confidence` is uncalibrated** | It is computed, not asserted, and it is explicitly not evidential — but nothing has established that 0.807 on `epiphyseal_fusion` and 0.053 on `height_gwas` are on a scale a reader can use. It orders neighbourhoods; it does not yet mean anything absolute. |
| **Grade D is the ceiling on everything the P8 re-analysis produced** | Correct by the preregistered rule, and it means four genuinely useful negatives (NPPC, cGMP-PDEs, aromatase/ERβ, MCT8) enter the graph at the same grade as a single weak study. The grade scale has no way to say "a clean negative from the only dataset that exists." |
| **26 orphan non-stub nodes** | Reported by the validator on every run. Most are L13 methods entities that legitimately have no mechanistic edge, but the set has not been triaged one by one, so "most" is an estimate rather than a count. |
| **The exposure hole (MR-002)** | Elevated as instructed and still open: the atlas can say what a pathway does but rarely what concentration of anything reaches a chondrocyte in a human. Phase 6 confirmed the cost — in-vivo physeal stress is recorded verbatim as "not measured" and the flow model halts on it. |
| **Phase 8 is one dataset** | GSE9160 was the highest-value re-analysis target and it has been done. `atlas/quant/dataset_inventory.csv` holds 61 entries and the remainder are untouched. The flagship human scRNA-seq series (GSE288028) is **not fully reusable** — its raw human files were withheld from GEO for identifiability reasons — which is itself a recorded structural limit on what anyone can re-analyse. |

## 4b. Closed after this ledger was written

| item | what happened |
|---|---|
| **Reference verification had never been run in full** | The report on disk held **one** entry — every prior run was scoped with `--only`. The README therefore advertised "1 verified" against 1,049 references. Full run: **1,005 resolved OK, 0 metadata mismatches, 0 unresolved, 44 manual, 1 retraction-related.** |
| **A withdrawn paper was load-bearing** | That one flag was `wu2013`, withdrawn by *J Biol Chem* in 2020, carrying the atlas's only demonstrated environment-to-signalling seam. Traced as **CORR-004**; `validate.py` now errors on an undeclared retracted citation. |
| **`parameters.csv` was stale** | 820 rows against 1,520 on the nodes. Any figure quoted from the CSV rather than from the nodes was against two-thirds of the record. Regenerated. |
| **`progress.yaml` was five phases stale** | Claimed phase 2, 633 stubs, "no edges written yet", four sweeps in flight. A resuming session would have restarted finished work. Rewritten. |
| **`coverage.md` warned about the wrong layers** | Not just stale counts — its evidence-quality heuristic does not predict what the atlas gets wrong. Regenerated from the repository, with the measured per-layer hit rate alongside. |
| **Context fill** | All MR-004 targets met: zone 53.9%, sex 30.5%, stage 63.8%. Every edge is now determined-from-source or explicitly `unknown`; no nulls remain. |
| **Five layers had no figure** | L8, L9, L10, L12, L13 generated from the graph. All 14 layers now carry a synthesis and a figure. |

Four of these seven were **tools reporting on themselves incorrectly** rather than work
left undone — a verification that had never been run at scale, a CSV regenerated from a
stale tree, a resume file nobody re-read, a coverage file warning on the wrong axis.
That is the same shape as §5 below and it is worth naming: in a build this long, the
instruments drift faster than the data.

## 5. What this ledger is for

Three items in §1 were closed only because a mid-run correction asked for a number and
the number did not exist. Two of them (Phase 2e, the rejection tally) turned out to be
defects rather than omissions. That ratio is the argument for keeping the ledger: the
items nobody asks about are the ones that stay wrong.
