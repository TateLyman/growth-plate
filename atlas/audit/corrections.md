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

---

## CORR-002 — reserved

Next correction entry goes here. Corrections are appended, never overwritten.
