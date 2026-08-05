# Coverage — what this atlas knows, at what depth, and what it cannot do

Read this before trusting an answer.

> **Every number in this file is generated.** Regenerate with
> `python3 atlas/tools/coverage_report.py`; check for drift with `--check`. The
> interpretive prose is hand-written and lives outside the generated blocks, because a
> judgement about which layer to distrust is not something a script should invent.
>
> This became a rule after the Phase 7 falsification run found this file asserting 612
> nodes, 764 edges and "L8 = 3 nodes" against an actual 614, 1,181 and 39. A stale
> coverage file is worse than none: it warns about the wrong layers with the authority
> of a measurement.

---

## Canonical denominator

All coverage percentages are stated against **`researched_non_stub_nodes`** unless a
different base is named inline.

Defined: a node file with `stub: false`. **This now equals the total node count, because
stub resolution completed and zero stubs survive.** Earlier reports in this build used
654, 612 and 578 as bases at different moments; every figure in this file is against the
current count.

The one count that is still NOT interchangeable: **`claim_grades`** is populated on a
minority of nodes, and coverage figures about claim-level grading must name that base
explicitly.

## The one-line boundary

**The atlas cannot exceed the measurement record.** Where no one has taken the reading, it
returns the gap — not an estimate, not an extrapolation from the mouse, not a plausible
number. That is the whole design, and it is why several answers here are shorter and less
satisfying than what a language model would otherwise produce.

---

## Per-layer coverage, evidence quality, and measured predictive performance

<!-- COVERAGE:LAYERS:BEGIN -->
| Layer | Name | nodes | direct human | **replicated human** | high transl. risk | gaps | A/B | **hit rate %** |
|---|---|---:|---:|---:|---:|---:|---|---:|
| L0 | developmental_origin | 25 | 8 (32%) | 2 (8%) | 10 (40%) | 13 | 2/10 | **100** |
| L1 | growth_plate_architecture | 48 | 20 (41%) | 19 (39%) | 25 (52%) | 14 | 4/11 | **40** |
| L2 | stem_and_progenitor_biology | 35 | 5 (14%) | 0 (0%) | 24 (68%) | 14 | 0/3 | **0 †** |
| L3 | signaling_networks | 88 | 18 (20%) | 14 (15%) | 50 (56%) | 43 | 8/18 | **100** |
| L4 | endocrine_and_systemic | 72 | 46 (63%) | 33 (45%) | 15 (20%) | 24 | 32/16 | **40** |
| L5 | matrix_and_mineralization | 41 | 18 (43%) | 12 (29%) | 13 (31%) | 17 | 4/19 | **100** |
| L6 | mechanobiology | 31 | 10 (32%) | 10 (32%) | 14 (45%) | 23 | 4/6 | **100** |
| L7 | fusion_and_cessation | 34 | 26 (76%) | 26 (76%) | 4 (11%) | 18 | 15/6 | **75** |
| L8 | genetics_and_heritability | 39 | 38 (97%) | 35 (89%) | 0 (0%) | 22 | 18/18 | **20** |
| L9 | whole_organism_growth | 34 | 30 (88%) | 21 (61%) | 4 (11%) | 17 | 14/11 | **100** |
| L10 | environment_and_population | 34 | 29 (85%) | 18 (52%) | 4 (11%) | 13 | 9/16 | **100** |
| L11 | pathology_as_natural_experiment | 56 | 56 (100%) | 18 (32%) | 0 (0%) | 26 | 19/23 | **60** |
| L12 | pharmacology_as_mechanistic_probe | 36 | 30 (83%) | 26 (72%) | 6 (16%) | 30 | 16/10 | **50** |
| L13 | methods_and_data | 41 | 19 (46%) | 13 (31%) | 15 (36%) | 14 | 11/18 | **50** |
| | **TOTAL** | **614** | **353 (57.5%)** | **247 (40.2%)** | | **288** | | **64.0** |

`replicated human` = `human_evidence: direct` **and** ≥2 human primary sources. `hit rate` is the Phase 7 measured value, CORRECT / (CORRECT + WRONG + SILENTLY_ABSENT) — source: query/falsification_baseline.md, cutoff 2026-02-01, 63 held-out papers. † L2's denominator is 1: two of its three held-out papers were correct refusals, so the 0 is a small-sample artefact and not a verdict.
<!-- COVERAGE:LAYERS:END -->

### How to read this table — and the finding that changed how to read it

Until Phase 7 this section warned readers on the basis of **evidence quality**: distrust
the layers that are mostly mouse, trust the layers that are mostly human. That heuristic
was reasonable, it was stated with confidence, and the falsification run shows **it does
not predict what the atlas actually gets wrong.**

| | direct human | replicated human | high translation risk | **measured hit rate** |
|---|---:|---:|---:|---:|
| **L8** genetics | 97% | 89% | 0% | **20%** — the worst |
| **L3** signalling | 20% | 15% | 56% | **100%** |

L8 is the most human, most replicated, lowest-translation-risk layer in the atlas, and it
is the layer that failed hardest at anticipating findings it had not seen. L3 is the layer
this file previously named as its second warning, and it did not miss anything.

**Evidence quality and predictive power are different properties, and this atlas now
measures both.** A node can be graded A on impeccable human data and still sit in a
neighbourhood so weakly connected that nothing can be derived from it — which is exactly
what `structural_confidence` was introduced to expose, and what L8's 0.27–0.38 range says.

So the warnings now read:

**Distrust answers that must cross a layer boundary.** 14 of the 16 findings the graph
should have anticipated and did not were **cross-layer edges**. The layers are well built
and weakly welded. Three sub-patterns, all measured:

- **Pharmacology is terminal.** `recombinant_human_gh` has 5 outbound edges, all inside
  the GH/IGF axis. `npr2_receptor` has 24 and not one reaches a named skeletal site.
- **The atlas has exactly one growth plate.** Eight site-specific plate and synchondrosis
  nodes receive no signalling or pharmacology edge at all.
- **L8 is unwired.** 39 A-graded nodes with no edges to the L7/L9/L10 phenotypes they
  exist to explain.

**Distrust context-filtered answers until the fill rates below are met.** A Type 3 query
filtered on zone or sex returns `UNRELIABLE` with its annotation coverage attached rather
than a small, confident-looking result. That is the correct failure mode, but it is a
failure mode.

**L2 remains the layer with no replicated human evidence at all** — resting-zone stem cell
biology is mouse lineage tracing, which cannot be done in humans. Its 0% hit rate is *not*
evidence of that weakness: two of its three held-out papers were correct refusals, so the
denominator is 1. The old warning about L2 was right for the right reason and the new
number is too small to say anything.

---

## Structural coverage

<!-- COVERAGE:STRUCT:BEGIN -->
| | |
|---|---|
| Nodes | 614 (614 researched, 0 stubs) |
| Edges | 1181 — **778 usable for perturbation reasoning**, 403 flagged unusable |
| Gaps | 288, with 134 gap ids carrying reproducible search logs (147 log entries) |
| References | 1049, all machine-resolved against Europe PMC/NCBI |
| Quantitative values on nodes | 1520 |

**Context annotation, three-state** (MATCH / MISMATCH / UNANNOTATED — only MISMATCH excludes an edge; see `atlas/tools/context_filter.py`):

| axis | annotated | of edges | MR-004 target |
|---|---:|---:|---:|
| zone | 139/1181 | 11.8% | 40% |
| sex | 139/1181 | 11.8% | 30% |
| stage | 265/1181 | 22.4% | 40% |
| species | 1109/1181 | 93.9% | — |

Sign coverage on sign-bearing relations is the traversal gate and stands at **778/778 = 100%**. The 403 excluded edges are `precedes` (temporal), `binds` (no direction), `correlates_with` and `hypothesized_link` — signing them would be fabrication, so they are flagged `traversal_usable: false` rather than traversed.
<!-- COVERAGE:STRUCT:END -->

---

## Quantitative reliability

<!-- COVERAGE:QUANT:BEGIN -->
| reliability class | rows | share |
|---|---:|---:|
| `single_source_with_uncertainty` | 1228 | 80.8% |
| `range_value` | 118 | 7.8% |
| **`single_source_point_no_uncertainty`** | **65** | 4.3% |
| `spread_documented` | 55 | 3.6% |
| `unverified` | 40 | 2.6% |
| `multi_source` | 12 | 0.8% |
| `superseded` | 2 | 0.1% |
| | **1520** | |

`single_source_point_no_uncertainty` is the risk class: one source, a point value, and nothing to warn a reader. Phase 2e classified every row rather than hunting duplicate parameter names, because ~94% of parameter names appear exactly once — disagreement in this field is not encoded as duplicate rows.
<!-- COVERAGE:QUANT:END -->

Only a handful of rows in the entire atlas are genuinely multi-source. That is a property
of the field, not of this build: most growth-plate numbers have been measured once, by one
group, using one method.

---

## What the atlas covers well

1. **Negative space.** The gap register with reproducible search logs. Asking what is
   *not* known is the atlas's strongest query type, and every `search_established` gap
   carries the exact query, database, date and hit count so a reader can re-run it.
2. **Human pharmacological perturbation** (L12) — effect sizes, confidence intervals, and
   terminated programmes with their stop reasons classified as `scientific_null` /
   `strategic` / `logistical`, because only the first is negative evidence.
3. **Species discipline.** Every node carries `species_basis` and `translation_risk`.
4. **Disease as human experiment** (L11) — 100% direct human evidence.
5. **Known corrections, held in their corrected form** with the superseded version
   documented and its blast radius traced object by object (`atlas/audit/corrections.md`).
6. **Paralog attribution.** 91 nodes swept; 80 carry `paralog_audit: passed`, 9 carry
   `paralog_risk`. A node that has been checked and held is now distinguishable from a
   node that merely has not been contradicted.
7. **Prioritised experimental agenda.** `docs/experimental_agenda.md` ranks unmeasured
   parameters by their contribution to output uncertainty, with a discriminating
   experiment written for each.

## What the atlas covers poorly

1. **Zone-resolved anything in humans.** The only zone-resolved human growth-plate
   transcriptome is two children from 2007 — and the P8-01 re-analysis shows that for
   zonal contrast it is effectively **one** child, because the second donor's laser
   capture did not separate the compartments.
2. **Cross-layer traversal.** Measured at a 25% silent-failure rate by Phase 7. This is
   the single largest structural deficit and it is now quantified rather than suspected.
3. **Context-filtered perturbation** — zone, sex and stage fill rates are below target.
4. **Local concentration of anything.** The atlas can say what a pathway does; it can
   rarely say what concentration reaches a chondrocyte in a living human. The Phase 6
   flow model halts on exactly this.
5. **Anything outside human longitudinal skeletal growth.** See `adversarial.yaml` for
   the shape of the boundary — articular cartilage, oncology, veterinary, adult bone
   density, forensic and surgical management are all out of scope, and the protocol
   refuses rather than extrapolates.

---

## The honest summary

This atlas is a **map of a mostly-murine literature with the human evidence explicitly
marked**, plus a systematic register of what has never been measured, plus — since Phase
7 — a measurement of how often it can anticipate a finding it has not seen. That number
is **64%**, and the 36% is more informative than the 64%.

Two numbers set the ceiling on everything here: **259 human growth plates have ever been
examined histologically, 102 of them postnatal and growing, and exactly 2 at or
immediately before fusion.** No synthesis can exceed that record.
