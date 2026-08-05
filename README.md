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
**Totals** — 614 nodes (614 researched, 0 stubs) ·
1181 edges · 288 gaps (147 search logs) · 1049 references

```
nodes  ██████████░░░░░░░░░░ 614/1200 (51%)
edges  █████████░░░░░░░░░░░ 1181/2500 (47%)
gaps   ████████████████████ 288/150 (100%)
```

| Layer | Name | Nodes | Researched | Edges out | Gaps | Quota | Doc | Fig |
|---|---|---:|---:|---:|---:|:--:|:--:|:--:|
| L0 | developmental_origin | 25 | 25 | 31 | 13 | ✅ | ✅ | ✅ |
| L1 | growth_plate_architecture | 48 | 48 | 48 | 14 | ✅ | ✅ | ✅ |
| L2 | stem_and_progenitor_biology | 35 | 35 | 56 | 14 | ✅ | ✅ | ✅ |
| L3 | signaling_networks | 88 | 88 | 228 | 43 | ✅ | ✅ | ✅ |
| L4 | endocrine_and_systemic | 72 | 72 | 217 | 24 | ✅ | ✅ | ✅ |
| L5 | matrix_and_mineralization | 41 | 41 | 101 | 17 | ✅ | ✅ | ✅ |
| L6 | mechanobiology | 31 | 31 | 94 | 23 | ✅ | ✅ | ✅ |
| L7 | fusion_and_cessation | 34 | 34 | 33 | 18 | ✅ | ✅ | ✅ |
| L8 | genetics_and_heritability | 39 | 39 | 66 | 22 | ✅ | ✅ | — |
| L9 | whole_organism_growth | 34 | 34 | 47 | 17 | ✅ | ✅ | — |
| L10 | environment_and_population | 34 | 34 | 58 | 13 | ✅ | ✅ | — |
| L11 | pathology_as_natural_experiment | 56 | 56 | 83 | 26 | ✅ | ✅ | ✅ |
| L12 | pharmacology_as_mechanistic_probe | 36 | 36 | 79 | 30 | ✅ | ✅ | — |
| L13 | methods_and_data | 41 | 41 | 40 | 14 | ✅ | — | — |
| | **total** | **614** | **614** | **1181** | **288** | | | |

**Confidence distribution** (researched nodes): **A** 156 · **B** 185 · **C** 184 · **D** 76 · **E** 11 · **X** 2

**Gap types**: `contradiction` 26 · `known_unknown` 70 · `method_blocked` 12 · `quantitative_gap` 67 · `scale_gap` 11 · `search_established` 80 · `species_gap` 22

**Quantitative**: 1520 values on nodes · 1520 rows in `quant/parameters.csv`

**Reference verification** (`tools/verify_refs.py`): 1 verified · 0 mismatched · 0 unresolved · 0 manual

### Evidence quality

These are tracked instead of treating the A-grade count as a target. Direct,
replicated human evidence in growth-plate biology is genuinely scarce; a falling
A-count alongside rising propositional rigour is a successful run, not a shortfall.

The `edges_per_node ≥ 3.0` target was **retired** (MR-004): additional bare edges at
low context fill increase graph size without increasing answerability. The live
structural target is context fill on existing edges — zone ≥40%, sex ≥30%, stage ≥40% —
reported by `atlas/tools/context_filter.py --coverage-report` and in
`query/coverage.md`. All three are met.

| metric | value | target |
|---|---:|---:|
| `human_evidence_fraction` — researched nodes with `human_evidence: direct` | **57.5%** | — |
| `replicated_human_fraction` — direct human evidence **and** ≥2 human primaries | **40.2%** | — |
| `edges_per_node` | **1.92** | target retired — see note above |
| `refs_per_researched` | **3.13** | ≥3.0 |
| `quant_node_coverage` | **68.4%** | ≥60% |
| `stub_fraction` | **0.0%** | 0% |

| Layer | researched | human_evidence: direct | replicated human |
|---|---:|---:|---:|
| L0 | 25 | 8 (32%) | 2 (8%) |
| L1 | 48 | 20 (42%) | 19 (40%) |
| L2 | 35 | 5 (14%) | 0 (0%) |
| L3 | 88 | 18 (20%) | 14 (16%) |
| L4 | 72 | 46 (64%) | 33 (46%) |
| L5 | 41 | 18 (44%) | 12 (29%) |
| L6 | 31 | 10 (32%) | 10 (32%) |
| L7 | 34 | 26 (76%) | 26 (76%) |
| L8 | 39 | 38 (97%) | 35 (90%) |
| L9 | 34 | 30 (88%) | 21 (62%) |
| L10 | 34 | 29 (85%) | 18 (53%) |
| L11 | 56 | 56 (100%) | 18 (32%) |
| L12 | 36 | 30 (83%) | 26 (72%) |
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

## The ceiling

**The atlas cannot exceed the measurement record.** Where no one has taken the reading,
it returns the gap. It does not interpolate, it does not average across species to fill
a hole, and it does not let a plausible sentence stand in for a number nobody has
measured.

What it can do, and what nothing else currently does, is **state exactly where the
readings are missing, rank them by how much they matter, and say what it would take to
get them.**

That claim is now concrete rather than aspirational. The Phase 6 parameter-flow model
(`atlas/quant/notebooks/flow_model.py`) does not run: seven of eight named sites halt
at the same step, because terminal hypertrophic cell height in micrometres has never
been measured in any species. Propagating the recorded spreads gives an output range of
0.58–33.1 cm/yr — a 57-fold band — and **98% of that uncertainty rests on five
parameters that have never been measured.** `docs/experimental_agenda.md` ranks them,
names the discriminating experiment for each, and states the falsifiable prediction the
top one would test.

That is the ceiling, and it is worth reaching.

## Entry points

- New here → this file, then `atlas/docs/L1_growth_plate_architecture.md`.
- Want the open problems → `atlas/gaps/gaps.yaml` and the ranked list in the dashboard.
- Want the numbers → `atlas/quant/parameters.csv`.
- Want to check my work → `atlas/audit/` and `python3 atlas/tools/verify_refs.py`.
- Resuming the build → `atlas/state/progress.yaml`.
