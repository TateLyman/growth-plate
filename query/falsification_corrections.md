# Phase 7 — test-driven corrections register

Companion to `query/falsification_baseline.md`. Every defect the falsification run exposed
is entered here with its own record, so that the **baseline number and any post-fix number
stay distinguishable forever**.

## Headline

| | |
|---|---|
| Baseline hit rate (before any fix) | **32 / 50 scored = 64.0%** · raw 32/63 = 50.8% |
| SILENTLY_ABSENT at baseline | **16** |
| **Graph edits applied** | **ZERO** |
| Post-fix hit rate | **32 / 50 = 64.0% — unchanged, because nothing was changed** |

## Why zero edits, stated plainly

The brief permits fixing a structural defect the test exposes — a missing node, an absent
edge, a wrong sign. Every candidate fix below fails the same test:

> **The only evidence that the edge belongs in the graph is the held-out paper that scored
> the miss.**

Adding `vosoritide → cranial_base_synchondrosis` because P55 scored SILENTLY_ABSENT is
adding an edge whose sole warrant is the item it would convert to a hit. That is a graph
edited to predict its own test set, which is the one outcome the exercise exists to prevent.

The correct disposal is therefore: **record the defect, do not close it here, and route the
evidence through a normal sweep** where the held-out paper is ingested on its merits with a
`ref_id`, a tier, a species tag and a grade — after which it is no longer held-out, and the
edge is no longer a fix to a test.

Two defects (C-06, C-07) are *not* claim-bearing and could be applied without importing any
held-out evidence. They are still deferred, for a narrower reason given in each entry.

---

## Register

### C-01 — Pharmacology (L12) is a terminal layer
- **Status:** DEFERRED — requires held-out evidence
- **Exposed by:** P21, P23, P55, P56, P60 (5 of 16 SILENTLY_ABSENT)
- **Defect:** No growth intervention has an outbound edge to any consequence outside the
  axis it targets. `recombinant_human_gh` — 5 outbound edges, all GH/IGF axis or
  whole-organism velocity. `vosoritide` — 4, all inside the CNP/FGFR3 cassette.
- **Class:** absent edges, cross-layer (L12→L1/L4/L6/L7/L9)
- **What would close it:** ingest the five held-out papers through a normal L12 sweep, then
  add signed edges with their real contexts. Do **not** hand-add edges from this document.
- **Effect on the number if closed:** would convert up to 5 SILENTLY_ABSENT. Any figure
  quoted after that is a **post-ingestion** number and must be labelled as such — it is not
  comparable to the 64.0% baseline.

### C-02 — The atlas has one growth plate
- **Status:** DEFERRED — requires held-out evidence
- **Exposed by:** P06, P23, P55, P56, P64 (5 of 16)
- **Defect:** 8 site-specific plate/synchondrosis nodes exist
  (`vertebral_growth_plate`, `cranial_base_synchondrosis`, `metacarpal_plate`,
  `distal_femur_plate`, `proximal_tibia_plate`, `distal_radius_plate`,
  `proximal_humerus_plate`, `mandibular_condylar_cartilage`) and **none** receives a
  signalling or pharmacology edge. `cranial_base_synchondrosis` has 2 outbound edges, both
  `traversal_usable: false`. `vertebral_growth_plate` has 5 inbound, all mechanics/proportion.
- **Class:** absent edges + a missing organising claim (site-specific responsiveness)
- **Note:** this one is partly closable from **already-ingested** material — the atlas
  already holds `site_specific_growth_rate`, `elongation_budget` and per-plate nodes. What
  it lacks is any statement that a systemically delivered agent reaches different plates
  differently, and `g_l12b_002` ("what concentration does any growth-modifying drug reach
  within human growth plate cartilage") shows the atlas knows that is unmeasured. Closing
  it as a *gap-linked* structure rather than an evidence edge is the honest route.

### C-03 — L8 nodes are unwired to the phenotypes they explain
- **Status:** DEFERRED — requires held-out evidence
- **Exposed by:** P37, P39, P41 (3 of 16) and P42 (1 of 2 WRONG)
- **Defect:** L8 was rebuilt from 3 to 39 A-graded nodes and never connected to L7/L9/L10.
  `sitting_height_ratio` (L9) has 2 edges, both unusable, neither to L8.
  `structural_confidence`: `height_gwas` 0.319, `height_polygenic_score` 0.380,
  `rare_variant_height` 0.380, `sitting_height_ratio` 0.269.
- **Class:** absent edges, cross-layer (L8→L7/L9/L10)
- **Independent corroboration:** the atlas already holds `shox_haploinsufficiency` as a
  worked genetic→limb-segment-proportion example, so the *pattern* is present in one
  instance and never generalised.

### C-04 — Rare-variant share of height heritability is a point estimate where a spread is required
- **Status:** DEFERRED — requires held-out evidence to state the spread
- **Exposed by:** P42 (WRONG_PREDICTION)
- **Defect:** `rare_variant_height` and `missing_heritability_height` both state
  `wainschtein2026`'s "~20% rare, ~68% common" without recording that the figure is
  method- and denominator-dependent. `parameters.disputed` holds 5 numeric keys; this is
  not among them. `QUERY.md` type-7 requires "the spread and the methodological reason,
  never a central estimate".
- **Class:** wrong-form quantity (not a wrong sign)
- **Why deferred:** stating the spread requires the second value, which is the held-out
  paper's. Flagging the existing value as method-dependent **without** the second value
  would be a defensible partial fix; it is deferred with C-03 so the L8 seam is repaired in
  one pass rather than two.

### C-05 — EVC2 → GLI1 sign conflict
- **Status:** OPEN — candidate contradiction, not a defect to fix
- **Exposed by:** P09 (WRONG_PREDICTION)
- **Detail:** `evc_evc2_complex` asserts Ptch1/Gli1 **reduced** in Evc-null growth plate
  (`ruizperez2007`); the held-out paper reports Gli1 **augmented** under conditional Evc2
  loss in Gli1+ TMJ enthesis cells.
- **Disposal:** this is what `atlas/audit/contradictions.md` §1 is for. It is **not** a
  graph edit: the site and genetic design differ, so the correct action is a contradiction
  ledger entry with both contexts, not a sign flip. `QUERY.md` §0 is explicit — a conflict
  is "a finding to report, not a correction to apply silently".

### C-06 — `coverage.md` is stale and its warnings do not track predictive performance
- **Status:** DEFERRED — no held-out evidence needed, but see below
- **Exposed by:** the whole run
- **Detail:** `coverage.md` states **612 nodes / 764 edges**; actual is **614 / 1181**. It
  states **L8 = 3 nodes, "not yet examined"**; actual is **39**. It names **L2 as "the layer
  to distrust"** — L2 produced zero wrong answers here — and does not flag L8, L4 or L12,
  which produced 8 of the 16 silent absences between them.
- **Class:** documentation defect, no graph change
- **Why deferred anyway:** `coverage.md` is generated by `atlas/tools/compile_query.py`.
  Hand-editing it would desynchronise it from its generator; regenerating it is a build
  action outside this run's remit and would change artefacts the baseline was measured
  against. Logged for the next build pass.

### C-07 — Non-ingestion verification is not concurrency-safe
- **Status:** APPLIED (procedure only — no atlas artefact modified)
- **Exposed by:** P38 (see `falsification_baseline.md` §1.1)
- **Detail:** `bibliography.yaml` gained a ref (1036→1037) mid-session from a concurrent
  process, and that ref was one of the held-out papers. A sweep-time-only check missed it.
- **Fix applied:** the held-out set was re-verified at **scoring time** against **both**
  `bibliography.yaml` and `graph.json.refs`; the contaminated item was excluded from all
  counts, and the exclusion is reported in the baseline rather than absorbed.
- **Standing rule for any future falsification run:** re-run non-ingestion immediately
  before scoring, against the graph's own `refs` as well as the bibliography, and report
  exclusions explicitly. Note the direction of the error: the contaminated item would have
  scored CORRECT and raised the worst layer's hit rate from 20% to 33%.

### C-08 — Two whole subsystems are absent with no gap claiming them
- **Status:** OPEN — coverage backlog, logged to `query/coverage_gaps.yaml`
- **Exposed by:** P08 (adrenergic), P02 + P13 (chondrocyte/SSPC energy metabolism)
- **Detail:** across 614 nodes there is **no autonomic or neural input to the growth plate**
  (`adrenergic` → 0 nodes, `catecholamine` → 0 nodes) and **no chondrocyte energy
  metabolism** (`glycolysis` → 0 nodes, `oxidative phosphorylation` → 0 nodes), despite
  `hypertrophic_chondrocyte` recording a 2–5× mitochondrial expansion.
- **Disposal:** these scored CORRECTLY_OUTSIDE — the atlas claimed no coverage and was
  right. But a missing subsystem with no gap asserting its absence is invisible to a
  negative-space query, which is the atlas's strongest query type. Logged as coverage gaps
  so the next sweep can decide in or out deliberately.

---

## Rule for anyone quoting a number from this work

- **64.0% (32/50 scored), 16 SILENTLY_ABSENT** — the baseline. Blinded, pre-fix, 63 held-out
  propositions across 14 layers, cutoff 2026-02-01.
- **62.5% (30/48)** — the same baseline discounting P31 and P32, whose source programme the
  atlas already indexes (`falsification_baseline.md` §2.3).
- Any number produced after the held-out papers are ingested is a **post-ingestion** number.
  It measures a different object and must never be presented as an improvement on 64.0%.

---

## Post-Phase-6/8 delta — required by the Phase 7 protocol, and it is zero

The protocol asks for a baseline now and a re-run after Phase 6, on the grounds that
*"the delta measures whether the remaining work improved predictive power or only
coverage. Those are different achievements and should not be conflated."*

**The delta is zero, and it is zero for a reason that can be checked without re-scoring
a single proposition.**

Between the baseline commit and this one, the graph's topology is byte-for-byte
identical:

| | at baseline (`6c916e3`) | now |
|---|---:|---:|
| node files | 614 | **614** |
| edges | 1,181 | **1,181** |

Everything landed since then adds *content to existing objects*, never a node and never
an edge:

- **Phase 6** produced `flow_model.py`, `consistency_report.md` and
  `docs/experimental_agenda.md`. No graph object.
- **Phase 8** (`p8_01_gse9160_human_zonal`) added observations to 17 nodes and rewrote 7
  gaps. No edges.
- **The paralog audit** annotated 91 nodes and opened 9 gaps. No edges.
- **The context-fill campaign** rewrote the `context` string on 1,177 edges and changed
  no other field on any of them.

`SILENTLY_ABSENT` is defined as *no path existed*. Adding annotation to an existing edge
cannot create a path, so no item in that bucket can convert. A targeted check confirms
it from the other direction: scanning all 63 held-out propositions for overlap with the
Phase 8 subject matter returns nine candidates (P07, P09, P11, P15, P46, P55, P56, P57,
P60), and every one of them is a pharmacological or phenotypic claim that a transcript
localisation result does not bear on.

**So the answer to the protocol's question is explicit: the work since the baseline
improved coverage, diagnosis and honesty, and did not improve predictive power.** That
is the correct outcome for work that deliberately applied zero graph edits, and it is
worth stating rather than leaving the reader to infer that a re-run was skipped.

The number that would move this is C-01/C-02/C-03 — the cross-layer wiring — and those
are deferred for the reason at the top of this file, not because they are hard.
