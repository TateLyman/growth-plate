# Mechanism corrections and their blast radius

A mechanism correction never stays local. Every entry here traces **every** node,
edge, gap and quantitative row that assumed the superseded mechanism, and records
what was done to each. An entry is not closed until the trace is complete.

---

## CORR-001 — ANKH exports ATP, not pyrophosphate

**Date traced:** 2026-08-05
**Superseded model:** ANKH is a plasma-membrane PPi transporter carrying intracellular
PPi to the extracellular space, where it inhibits hydroxyapatite nucleation.
**Corrected model:** ANKH exports nucleoside triphosphates, predominantly ATP. ENPP1
then hydrolyses that ATP extracellularly to PPi + AMP. ANKH is therefore **upstream of
ENPP1**, not a parallel PPi source.

**Primary evidence:** In HEK293 cells engineered to lack ENPP1 entirely, introducing
ANKH produces robust ATP release with **no** increase in extracellular PPi. `Enpp1−/−`
mouse bone contains **<2.5%** of wild-type PPi despite intact *Ank*. The same holds for
ABCC6, so both transporters maintaining plasma PPi do so by extruding NTPs. Quantitative
split: ANKH supplies ~25% of plasma PPi, ABCC6 60–70%.

### Blast radius — traced

| Object | Status | Action |
|---|---|---|
| `ankh_transporter` (node) | **Corrected at authoring** | States the superseded model explicitly, then refutes it with the ENPP1-null experiment. `contradicts: [wang2005]`. Graded **B**, `human_evidence: indirect`. |
| `enpp1_enzyme` (node) | **Corrected at authoring** | Repositioned as downstream of every known PPi-generating route rather than one of several. |
| `inorganic_pyrophosphate` (node) | **Corrected at authoring** | Carries the ANKH→ATP→ENPP1→PPi chain in `key_refs.one_line_finding`. |
| `pi_ppi_ratio` (node) | Consistent | Ratio logic is mechanism-agnostic; unaffected by which protein generates PPi. |
| `e00544` `ankh_transporter --precedes--> enpp1_enzyme` | **Correct topology** | Note records: *"Supersedes the earlier model in which ANK transports PPi directly."* |
| `e00543` `enpp1_enzyme --activates--> inorganic_pyrophosphate` | **Correct topology** | PPi generation attributed to ENPP1, not ANKH. |
| Direct `ankh_transporter --> inorganic_pyrophosphate` edge | **Absent — correct** | No such edge exists. Under the superseded model it would have been the central edge of this cluster. Its absence is the structural signature that the correction landed. |
| Remaining 16 edges in the PPi/mineralization cluster | Unaffected | TNAP degradation of PPi, PPi inhibition of hydroxyapatite nucleation, matrix-vesicle and fetuin-A/OPN/MGP inhibitor edges are all downstream of PPi *existing* and are indifferent to its source. |
| `g_l5matrix_006` (gap) | **Open, correctly framed** | Asks the discriminating question directly and names the decisive experiment: repeat the *Ank*-manipulation chondrocyte phenotype in an `Enpp1`-null background. Under ATP-export, the wang2005 phenotype is abolished; under PPi-transport it persists. |
| Quantitative rows | Checked | No row attributes a PPi flux or concentration to ANKH transport. The ~25% / 60–70% plasma-PPi split is attributed to ANKH and ABCC6 as *sources of the ATP substrate*, which is correct under the new model. |

### Verification performed

Repository-wide regex for any surviving assertion that ANK/ANKH transports, exports or
effluxes PPi returned **zero** positives. Every textual hit for "ANKH … PPi" is a correct
statement of the corrected mechanism or the gap that interrogates it.

### Why the blast radius was small

The correction was made **at authoring time** by the L5 sweep, which refused the
consensus framing while writing rather than inheriting it and being corrected later.
This is the argument for `phase 2d`: auditing canonical mechanisms against primary data
*before* building on them costs far less than retrofitting a correction through a graph
that has already grown around the error. Had this landed after cross-layer edge
construction, the trace would have run through L1 mineralization-front architecture and
L11 hypophosphatasia/XLH nodes as well.

### Residual risk

`wang2005` (the chondrocyte *Ank* manipulation study) is **not retracted and not wrong
as an observation** — blocking Ank does change chondrocyte PPi handling. What is wrong is
the *mechanistic interpretation* placed on it. The node keeps the observation and rejects
the interpretation, which is the correct disposition and is why `contradicts` points at
the reference rather than the finding being discarded.

### Extended sweep (MR-001 item 4) — prose is not the only place a dead mechanism hides

The first sweep matched prose assertions only. Re-run across the three forms a
superseded mechanism actually survives in:

| Form | Matches | Genuine | Disposition |
|---|---:|---:|---|
| **(a) Paraphrase** — "ANK-mediated PPi efflux", "ANK-dependent PPi", "ANK/ENPP1 as PPi sources" | 3 | 3 | All three were *correct* under the new model (they assert ENPP1 is required), but the wording "ANK-dependent PPi" is readable as ANK transporting PPi. **Tightened** to "ANK-attributable PPi, i.e. PPi arising downstream of ANKH ATP export" in 3 nodes. |
| **(b) Quantitative rows** | 13 | **7** | 6 were substring artefacts (`bioBANK`, `RANK order`, `ANKle`). Of the 7 genuine rows, 6 are correctly framed under the new model — note that `inorganic_pyrophosphate` already says "ANKH-mediated **NTP efflux**", not PPi transport. **1 row required action**: "Fraction of mouse bone PPi attributable to Ank activity (older estimate) = ~75%" is an old-model figure. Now carries `superseded_model: true`, propagated into `parameters.csv` as a machine-readable column so a downstream consumer cannot use it naively. |
| **(c) Gap phrasing** | 12 | **1** | 11 were substring artefacts. The one genuine ANK gap, `g_l5matrix_006`, is already framed as the *discriminating question* between the two models and names the decisive experiment. **No malformed gaps found** — no gap presupposes the dead mechanism. |

**Counts: (a) 3 tightened · (b) 1 flagged superseded, 6 already correct · (c) 0 malformed.**

The lesson worth carrying: the substring false-positive rate here was ~50% (19 of 32
matches were `biobank`/`rank`/`ankle`). A correction sweep that reports raw match counts
overstates its own blast radius. Every match must be read, not tallied.

### Reference disposition classification (MR-001 item 5, now standing policy)

On every mechanism correction, each affected reference is classified:

| Ref | Classification | Reasoning |
|---|---|---|
| `wang2005` (chondrocyte *Ank* manipulation) | **interpretation_superseded** | Blocking Ank *does* change chondrocyte PPi handling — that measurement stands. Only the causal story attached to it (ANK as a PPi transporter) died. `contradicts` therefore points at the reference rather than the finding being discarded. |
| `szeri2022` (ANKH exports ATP) | **observation_stands** | The correcting evidence itself. |

Discarding sound data along with the wrong story is the default failure mode of a
correction pass, and is now explicitly forbidden: a measurement is retired only when
classified `both_invalid`, which requires the measurement itself to be unreliable, not
merely its explanation.

---

## CORR-002 — reserved

Next correction entry goes here. Corrections are appended, never overwritten.
