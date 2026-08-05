# Coverage — what this atlas knows, at what depth, and what it cannot do

Read this before trusting an answer. A question asked in a layer that is 69% rodent-derived
should carry that warning **before** the answer, not after it.

Generated from the compiled artifacts. Regenerate with `atlas/tools/compile_query.py`.

---

## Canonical denominator

All coverage percentages in this atlas are stated against **`researched_non_stub_nodes`**
unless a different base is named inline.

Defined: a node file with `stub: false`. **As of Phase 3 close this equals the total node
count, because stub resolution completed and zero stubs survive: 614 = 614.** Before that
pass the two numbers differed (578 researched of 612 files, 34 stubs), and earlier reports
in this build used 654 and 612 as bases at different moments. Any figure in this file
predating the stub-resolution pass is restated below against the current 614.

The one count that is still NOT interchangeable: **`claim_grades`** is populated on a
minority of nodes, and coverage figures about claim-level grading must name that base
explicitly rather than implying it applies to all 614.

## The one-line boundary

**The atlas cannot exceed the measurement record.** Where no one has taken the reading, it
returns the gap — not an estimate, not an extrapolation from the mouse, not a plausible
number. That is the whole design, and it is why several answers here are shorter and less
satisfying than what a language model would otherwise produce.

---

## Per-layer coverage and evidence quality

| Layer | Name | nodes | direct human | **replicated human** | high transl. risk | gaps | A/B |
|---|---|---:|---:|---:|---:|---:|---|
| L0 | developmental_origin | 25 | 8 (32%) | 2 (8%) | 10 (40%) | 12 | 2/10 |
| L1 | growth_plate_architecture | 48 | 20 (42%) | 19 (40%) | 25 (52%) | 14 | 4/11 |
| **L2** | **stem_and_progenitor_biology** | 35 | 5 (14%) | **0 (0%)** | **24 (69%)** | 11 | 0/3 |
| L3 | signaling_networks | 87 | 18 (21%) | 10 (11%) | 49 (56%) | 26 | 8/19 |
| L4 | endocrine_and_systemic | 72 | 46 (64%) | 32 (44%) | 15 (21%) | 12 | 31/17 |
| L5 | matrix_and_mineralization | 42 | 19 (45%) | 13 (31%) | 13 (31%) | 10 | 5/19 |
| L6 | mechanobiology | 31 | 10 (32%) | 10 (32%) | 14 (45%) | 14 | 4/6 |
| L7 | fusion_and_cessation | 34 | 26 (76%) | 26 (76%) | 4 (12%) | 13 | 15/6 |
| L8 | genetics_and_heritability | 3 | 3 (100%) | 2 (67%) | 0 (0%) | 2 | 2/1 |
| L9 | whole_organism_growth | 34 | 30 (88%) | 21 (62%) | 4 (12%) | 17 | 14/11 |
| L10 | environment_and_population | 34 | 29 (85%) | 18 (53%) | 4 (12%) | 12 | 9/16 |
| L11 | pathology_as_natural_experiment | 56 | 56 (100%) | 17 (30%) | 0 (0%) | 25 | 18/24 |
| L12 | pharmacology_as_mechanistic_probe | 36 | 30 (83%) | 26 (72%) | 6 (17%) | 28 | 16/10 |
| L13 | methods_and_data | 41 | 19 (46%) | 13 (32%) | 15 (37%) | 14 | 11/18 |
| | **TOTAL** | **578** | **319 (55.2%)** | **209 (36.2%)** | | **210** | |

`replicated human` = `human_evidence: direct` **and** ≥2 human primary sources.

### How to read this table

**L2 is the layer to distrust.** Stem and progenitor biology has **zero** nodes with
replicated human evidence and 69% carrying high translation risk. Everything there is mouse
lineage tracing, which cannot be done in humans at all. An answer about resting-zone stem
cells is an answer about *mice*, and the atlas will say so.

**L3 is the second warning.** Signalling is the densest layer (87 nodes, 26 gaps) and only
11% replicated-human. This is where a language model's fluency is most dangerous, because
the murine pathway literature is enormous and reads as settled.

**L11, L12, L9, L10 are the strong layers** — 83–100% direct human evidence, because they
are built from human disease, human trials and human population data. L12 in particular is
72% replicated-human: randomised human perturbation is the strongest causal evidence here.

**L8 is nearly empty (3 nodes).** It has not been swept. Do not read low gap counts there as
"few unknowns" — read them as "not yet examined."

---

## Structural coverage

| | |
|---|---|
| Nodes | 612 (578 researched, 34 stubs) |
| Edges | 764 — **468 usable for perturbation reasoning**, 296 flagged unusable |
| Cycles | 27 — 17 negative/stabilising, 10 positive/amplifying |
| Gaps | 210, with 102 reproducible search logs |
| References | 946, all machine-resolved against Europe PMC/NCBI |
| Quantitative rows | ~1,700 |

### What the edge set can and cannot support

Only **61.3%** of edges can carry a directional answer. The excluded 296 are `precedes`
(temporal, no sign), `binds` (no direction), `correlates_with` (direction not inferable from
relation type) and `hypothesized_link` (speculative). Traversing them would produce paths
with no directional meaning, so the protocol forbids it.

**Context filtering is weak.** Edge context strings mention species 94% of the time, but
zone only **5.5%**, developmental stage/age **11.3%**, and sex **6.2%**. A perturbation query
filtered by zone or sex will therefore exclude most of the graph, and any such answer is
weakly constrained. The protocol requires that this be stated in the answer.

### Quantitative reliability

**1,264 parameters rest on a single source.** That is the majority of the quantitative
record, and it is a property of the field rather than of this build — most growth-plate
numbers have been measured once. Only 5 parameters have enough independent sources to
register as disputed. 37 rows are flagged `value_unverified`; 1 is flagged
`superseded_model` and retained for provenance only.

---

## What the atlas covers well

1. **Negative space.** 210 gaps with 102 reproducible search logs. Asking what is *not*
   known is the atlas's strongest query type, and the search logs make each null checkable.
2. **Human pharmacological perturbation** (L12) — effect sizes, CIs, terminated programmes
   with their stop reasons classified.
3. **Species discipline.** Every node carries `species_basis` and `translation_risk`. The
   mouse/human boundary is the thing this atlas is most careful about.
4. **Disease as human experiment** (L11) — 100% direct human evidence, genotype→stature chains.
5. **Known corrections.** ANKH, zonal stiffness, CNP exposure, target height and mouse
   fusion are all held in their corrected form with the superseded version documented.

## What the atlas covers poorly

1. **Zone-resolved anything in humans.** No human spatial transcriptomics exists; the only
   zone-resolved human transcriptome is two children from 2007.
2. **Context-filtered perturbation** — zone/stage/sex fill rates are too low (§ above).
3. **L8 genetics** — 3 nodes, unswept.
4. **Cross-layer traversal** — edge density is 1.25/node; intra-layer edges dominate, so
   long mechanistic chains break at layer boundaries.
5. **Anything outside human longitudinal skeletal growth** — see `adversarial.yaml` for the
   shape of the boundary. Articular cartilage, oncology, veterinary, adult bone density,
   forensic applications and surgical management are all out of scope.

---

## The honest summary

This atlas is a **map of a mostly-murine literature with the human evidence explicitly
marked**, plus a systematic register of what has never been measured. Its most valuable
outputs are the gaps and the species tags, not the mechanisms — because the mechanisms are
largely available elsewhere, and the honest accounting of which of them are human is not.

Two numbers set the ceiling on everything here: **259 human growth plates have ever been
examined histologically, 102 of them postnatal and growing, and exactly 2 at or immediately
before fusion.** No synthesis can exceed that record.
