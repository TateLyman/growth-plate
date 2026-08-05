# Human Growth System Atlas

A machine-readable, citation-grounded, quantitative map of the mechanisms that
determine how a human body grows in size and shape — from zygote to epiphyseal
fusion — **including an explicit, systematically-established map of what is not known.**

> **Status: under construction.** The coverage dashboard below is generated from the
> repository itself by `atlas/tools/dashboard.py` and reflects real counts, not targets.
> Empty numbers mean the work is not done. They are never padded.

## Three obligations, in priority order

1. **Truth** — every claim traceable to a real, verifiable source with a confidence grade.
2. **Completeness** — no layer omitted, from HOX patterning to population secular trend.
3. **Negative space** — the unknowns are a first-class deliverable. A gap *established by
   systematic search* is worth more than a paragraph paraphrased from a review.

## How truth is enforced mechanically

This atlas is built so that a fabricated citation cannot enter it quietly.

- **`atlas/tools/addref.py`** — bibliography entries are *machine-populated* from the live
  Europe PMC / NCBI record. Author, year, title and journal are never typed from memory.
  A PMID that does not resolve is **refused** (negative-tested with a fake PMID).
- **`atlas/tools/verify_refs.py`** — re-resolves every reference and cross-checks the stored
  first author and year against the resolved record. Mismatches are reported as
  `FABRICATION_RISK`. Also flags retraction-related publication types.
- **`atlas/tools/validate.py`** — structural gate: controlled vocabulary, required fields,
  dangling edge endpoints, ghost `ref_id`s, and the rule that a `hypothesized_link` edge
  must carry `confidence: speculative` **and** a real `gap_id`. Negative-tested: caught
  10/10 deliberately injected defects.
- **Gap admissibility** — a gap typed `search_established` is *rejected by the validator*
  unless a matching entry exists in `gaps/search_log.yaml` giving the exact query string,
  database, date, and hit count, so any reader can re-run it and reproduce the null.

Unverified is acceptable and is marked (`value_unverified: true`). Invented is fatal.

## Coverage dashboard

<!-- DASHBOARD:BEGIN -->
**Totals** — 610 nodes (576 researched, 34 stubs) ·
713 edges · 155 gaps (78 search logs) · 941 references

```
nodes  ██████████░░░░░░░░░░ 610/1200 (50%)
edges  █████░░░░░░░░░░░░░░░ 713/2500 (28%)
gaps   ████████████████████ 155/150 (100%)
```

| Layer | Name | Nodes | Researched | Edges out | Gaps | Quota | Doc | Fig |
|---|---|---:|---:|---:|---:|:--:|:--:|:--:|
| L0 | developmental_origin | 25 | 25 | 27 | 12 | ✅ | — | ✅ |
| L1 | growth_plate_architecture | 48 | 48 | 45 | 14 | ✅ | — | ✅ |
| L2 | stem_and_progenitor_biology | 35 | 35 | 42 | 11 | ✅ | ✅ | ✅ |
| L3 | signaling_networks | 88 | 87 | 222 | 26 | ✅ | — | ✅ |
| L4 | endocrine_and_systemic | 72 | 72 | 110 | 12 | ✅ | — | ✅ |
| L5 | matrix_and_mineralization | 42 | 42 | 50 | 10 | ✅ | — | ✅ |
| L6 | mechanobiology | 31 | 31 | 32 | 14 | ✅ | — | ✅ |
| L7 | fusion_and_cessation | 34 | 34 | 33 | 13 | ✅ | — | ✅ |
| L8 | genetics_and_heritability | 36 | 3 | 3 | 2 | 2/8·2/3 | — | — |
| L9 | whole_organism_growth | 33 | 33 | 40 | 0 | 0/8·0/3 | — | — |
| L10 | environment_and_population | 34 | 34 | 55 | 12 | ✅ | — | — |
| L11 | pathology_as_natural_experiment | 56 | 56 | 38 | 25 | ✅ | — | ✅ |
| L12 | pharmacology_as_mechanistic_probe | 35 | 35 | 1 | 2 | 2/8·2/3 | — | — |
| L13 | methods_and_data | 41 | 41 | 15 | 2 | 2/8·2/3 | — | — |
| | **total** | **610** | **576** | **713** | **155** | | | |

**Confidence distribution** (researched nodes): **A** 141 · **B** 169 · **C** 180 · **D** 73 · **E** 11 · **X** 2

**Gap types**: `contradiction` 15 · `known_unknown` 28 · `method_blocked` 5 · `quantitative_gap` 43 · `scale_gap` 6 · `search_established` 44 · `species_gap` 14

**Quantitative**: 1338 values on nodes · 811 rows in `quant/parameters.csv`

**Reference verification** (`tools/verify_refs.py`): 1 verified · 0 mismatched · 0 unresolved · 0 manual

### Evidence quality

These are tracked instead of treating the A-grade count as a target. Direct,
replicated human evidence in growth-plate biology is genuinely scarce; a falling
A-count alongside rising propositional rigour is a successful run, not a shortfall.

| metric | value | target |
|---|---:|---:|
| `human_evidence_fraction` — researched nodes with `human_evidence: direct` | **55.0%** | — |
| `replicated_human_fraction` — direct human evidence **and** ≥2 human primaries | **35.9%** | — |
| `edges_per_node` | **1.17** | ≥3.0 |
| `refs_per_researched` | **3.07** | ≥3.0 |
| `quant_node_coverage` | **65.8%** | ≥60% |
| `stub_fraction` | **5.6%** | 0% |

| Layer | researched | human_evidence: direct | replicated human |
|---|---:|---:|---:|
| L0 | 25 | 8 (32%) | 2 (8%) |
| L1 | 48 | 20 (42%) | 19 (40%) |
| L2 | 35 | 5 (14%) | 0 (0%) |
| L3 | 87 | 18 (21%) | 10 (11%) |
| L4 | 72 | 46 (64%) | 32 (44%) |
| L5 | 42 | 19 (45%) | 13 (31%) |
| L6 | 31 | 10 (32%) | 10 (32%) |
| L7 | 34 | 26 (76%) | 26 (76%) |
| L8 | 3 | 3 (100%) | 2 (67%) |
| L9 | 33 | 29 (88%) | 20 (61%) |
| L10 | 34 | 29 (85%) | 18 (53%) |
| L11 | 56 | 56 (100%) | 17 (30%) |
| L12 | 35 | 29 (83%) | 25 (71%) |
| L13 | 41 | 19 (46%) | 13 (32%) |

_Quota column: ≥8 gaps per layer, ≥3 of which are `search_established` or
`quantitative_gap`. Generated by `atlas/tools/dashboard.py`._
<!-- DASHBOARD:END -->

## Layout

```
atlas/
  nodes/<layer>/<node_id>.yaml   one file per entity (schema: schema/node.schema.yaml)
  edges/edges.yaml               all relations, append-only
  docs/<layer>.md                human-readable synthesis per layer
  gaps/gaps.yaml                 the unknown registry
  gaps/search_log.yaml           falsifiable evidence that a gap is real
  quant/parameters.csv           every number, with units + source + uncertainty
  quant/notebooks/               re-analyses actually run
  sources/bibliography.yaml      canonical refs, deduped, machine-populated
  sources/access_queue.md        paywalled items escalated to the user
  sources/retracted_or_disputed.md
  audit/contradictions.md        claim vs counter-claim; X-grade claims
  audit/redteam_<date>.md        self-critique passes
  figures/*.mmd                  Mermaid graphs per subsystem
  state/progress.yaml            resume state
  state/environment.md           what works, what is blocked
  schema/                        node/edge schemas + controlled vocabulary
  tools/                         validator, reference verifier, bibliography builder
```

## The 14 layers

| Layer | Name | Scope |
|---|---|---|
| L0 | developmental_origin | gastrulation → somitogenesis → limb bud → condensation → ossification centers |
| L1 | growth_plate_architecture | zonal anatomy, column mechanics, the elongation budget, site-specific behavior |
| L2 | stem_and_progenitor_biology | resting-zone niche, skeletal stem cell hierarchies, clonal exhaustion |
| L3 | signaling_networks | PTHrP/IHH, CNP/NPR2/cGMP, FGFR3, BMP/TGF-β, WNT, Notch, mTORC1, HIF-1α, SOX9/RUNX2 |
| L4 | endocrine_and_systemic | GH/IGF-1, thyroid, glucocorticoid, sex steroids, leptin, vitamin D/PTH/FGF23 |
| L5 | matrix_and_mineralization | collagens, aggrecan, proteases, TNAP/PPi, matrix vesicles, zonal stiffness |
| L6 | mechanobiology | Hueter-Volkmann, PIEZO/TRPV4/YAP-TAZ, loading, disuse, distraction osteogenesis |
| L7 | fusion_and_cessation | **the central human-specific problem** — mice do not fuse |
| L8 | genetics_and_heritability | height GWAS saturation, monogenic loci, dosage effects, PGS transferability |
| L9 | whole_organism_growth | muscle, adipose, viscera, brain, dental clock, craniofacial, allometry, growth-curve math |
| L10 | environment_and_population | nutrition, DOHaD, stunting, microbiome, altitude, secular trend |
| L11 | pathology_as_natural_experiment | each disorder = a perturbation experiment already run in humans |
| L12 | pharmacology_as_mechanistic_probe | CNP analogs, FGFR3 inhibitors, GH, IGF-1, AIs, GnRHa — including the failures |
| L13 | methods_and_data | how we know what we know, and what the methods cannot see |

## Reading conventions

**Confidence grades.** `A` replicated in humans with direct/interventional data · `B` strong
animal mechanism + human genetic/correlative support · `C` animal only, replicated ·
`D` single study, in vitro only, or conflicting · `E` flagged inference from adjacent
biology · `X` repeated in reviews but **not traceable to primary data** — every X is
logged in `audit/contradictions.md` and treated as a finding, not filler.

**Species tagging is mandatory.** Nearly all growth-plate mechanism is murine, and mice do
not undergo epiphyseal fusion. Every node carries `species_basis` and a
`translation_risk` grade with a stated reason. Mouse data is never presented as human fact.

## Entry points

- New here → this file, then `atlas/docs/L1_growth_plate_architecture.md`.
- Want the open problems → `atlas/gaps/gaps.yaml` and the ranked list in the dashboard.
- Want the numbers → `atlas/quant/parameters.csv`.
- Want to check my work → `atlas/audit/` and `python3 atlas/tools/verify_refs.py`.
- Resuming the build → `atlas/state/progress.yaml`.
