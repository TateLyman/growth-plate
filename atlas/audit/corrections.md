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

## CORR-002 — the collagen X null compresses the PROLIFERATIVE zone, not the hypertrophic zone

**Date traced:** 2026-08-05 (phase 2d canonical-mechanism audit, shard `l2daudit`)

**Superseded model:** `Col10a1`-null mice have a compressed growth plate with **reduced
hypertrophic zone height**, and the phenotype is otherwise negligible — a "subtle" refinement
of the original normal-phenotype report. `COL10A1`^−/− human iPSC chondrocytes show no
detectable difference.

**Corrected model:** In the `Col10a1` null the **proliferative zone is more compressed than
the hypertrophic zone** — the *opposite* of the collagen-X dominant-interference transgenic,
and the authors of the primary say so explicitly. The null is also not phenotypically silent:
≈10.8% perinatal lethality at week 3, further deaths to ≈14% total by 12 weeks, marrow aplasia
and lymphatic organs at ≈80% of control. In human `COL10A1`^−/− iPSC chondrocytes the
transplanted bone-area fraction is **significantly larger** in one of two iPSC backgrounds and
the hypertrophic transcriptome shifts from proliferating-phase toward calcification-phase
genes. Both systems point the same way: losing collagen X does not block hypertrophy, it
**shifts the proliferation/ossification balance toward ossification**.

**Primary evidence:** `gress2000` (PMC2174562, full text) — "Overall, when compared with
controls, the **proliferative zone in all KO mice was more compressed than the hypertrophic,
which was opposite that seen in the Tg mice**"; ≈14% overall decrease in growth plate width at
day 21 versus >18% in the transgenic; ≈10.8% perinatal lethality; total lethality ≈14%.
`kamakura2023` (PMC10184020, full text) — bone-area fraction significantly larger in
`COL10A1`^−/− 414C2-derived transplants, authors' reading "suggesting the acceleration of
differentiation".

**Why the field lost it:** `gress2000` corrected `rosati1994`, and reviews absorbed the
correction only as "a subtle growth plate phenotype", discarding both the **zone** and the
**lethality**. The zone reversal is the load-bearing part, because it is the only evidence that
collagen X acts non-cell-autonomously: the protein is expressed **exclusively** in hypertrophic
chondrocytes yet its clearest histological effect is one zone upstream.

### Blast radius — traced

| Object | Status | Action |
|---|---|---|
| `collagen_type_x` (node) | **Corrected** | Summary now states proliferative-zone compression, the ≈14% plate-width reduction, the ≈14% lethality and marrow/lymphoid involvement, and reframes `kamakura2023` as accelerated differentiation rather than a null. |
| `collagen_type_x` `key_refs.gress2000.one_line_finding` | **Corrected** | Was "growth plate compression and altered haematopoiesis"; now names the zone and the lethality. |
| `p00536` (quant: `Col10a1` deletion → long bone length, `rosati1994`, "0 detectable difference") | **Flagged** | `superseded_model: true`. The *measurement* — no detectable long-bone length difference in the original characterisation — **stands** (see reference disposition). What is superseded is its use as evidence that the null has no phenotype: `gress2000` re-examined the same null line and found lethality and plate compression. Note added pointing at `gress2000`. |
| `p00537` (quant: `COL10A1`^−/− iPSC → "0 detectable difference in differentiation markers") | **Re-stated, not retired** | Value kept for the *differentiation-marker* readout, which is genuinely null. Conditions and uncertainty rewritten to record that the *bone-area fraction* readout was **not** null (significant in 414C2). A second row `p90001` added carrying the positive bone-fraction result so a downstream consumer cannot read this node as uniformly negative. |
| `e00568` `collagen_type_x --hypothesized_link--> mineralization_front` (refs `rosati1994`, `kamakura2023`, `gress2000`, confidence `speculative`) | **Topology correct, note added** | Confidence `speculative` was already the right grade. Note now records that the two loss-of-function systems shift the balance *toward* ossification, so any hypothesised link must explain an inhibitory or organising role, not a structural prerequisite. |
| `e00249` `collagen_type_x --required_for--> schmid_metaphyseal_chondrodysplasia` | Unaffected | Human haploinsufficiency phenotype; independent of the mouse zonal question. |
| `e00299`, `e00374`, `e00382`, `e00392` (Smad1/5/8, Runx2, Mef2c, FoxA → `collagen_type_x`) | Unaffected | Upstream transcriptional control of *Col10a1*; indifferent to what the protein then does. |
| `e00575` `pi_ppi_ratio --activates--> collagen_type_x` | Unaffected | Regulation of expression, not of collagen X function. |
| `g_l5matrix_005` (gap, open question on this node) | **Re-read, re-phrased** | The gap did not presuppose hypertrophic-zone compression, so it was not malformed, but its `what_is_known` said "reduced hypertrophic zone height". Corrected in place. |
| `cartilage_organoid`, `ipsc_chondrogenesis` (L13 nodes citing `gress2000`/`kamakura2023`) | **Checked, unaffected** | Both cite these refs as *method* exemplars (organoid/iPSC chondrogenesis systems), not for the zonal claim. No text asserts hypertrophic-zone compression. |
| `g_l13b` gap citing `gress2000` | **Checked, unaffected** | Cites the null as a model-system availability point. |
| Remaining hypertrophy/mineralization edges | Unaffected | All are downstream of hypertrophy *occurring*, which collagen X does not gate in any of the three systems. |

**Match audit:** repository-wide search for surviving assertions that collagen X loss reduces
hypertrophic zone height returned **3** textual matches, of which **1** was genuine (the node
summary), **1** was the `key_refs` one-liner and **1** was the gap `what_is_known`. All three
corrected. Substring false positives ("collagen type XI", "COL10A1-Cre" lineage-tracing rows in
`parameters.csv`) were read individually and excluded — the `Col10a1-Cre` transdifferentiation
rows `p00330`/`p00332` use the promoter as a lineage driver and are entirely unaffected by what
the protein does.

### Reference disposition classification

| Ref | Classification | Reasoning |
|---|---|---|
| `rosati1994` | **interpretation_superseded** | The original measurement — no detectable difference in long bone growth and development in the null — is a real observation on a real line, later re-examined by `gress2000` on the **same** mice with more sensitive histomorphometry and colony-scale survival data. The measurement stands; the inference "collagen X is dispensable, full stop" does not. Not retired. |
| `gress2000` | **observation_stands** | The correcting evidence. |
| `kamakura2023` | **observation_stands** | Correctly reported by the authors; the atlas, not the paper, flattened it into a null. |

Standing policy applied: no measurement was discarded because its published explanation
failed. `p00536` keeps its value and gains a flag.

---

## CORR-003 — PKG-II is a prehypertrophic protein, and the *Prkg2* growth plate is expanded, not reduced

**Date traced:** 2026-08-05 (phase 2d canonical-mechanism audit, shard `l2daudit`)

**Superseded model:** PKG-II is *the* effector carrying CNP/NPR2 signalling to chondrocyte
hypertrophy, and its **hypertrophic-zone enrichment** is the best available explanation for why
the CNP/NPR2 effect is partitioned onto the hypertrophic zone despite uniform receptor
expression.

**Corrected model:** Two independent failures.

1. **Zone.** The only **protein-level** map of PKG-II in growth plate places it in **late
   proliferative and prehypertrophic** chondrocytes, "preceding the start of hypertrophic
   differentiation" (`chikuda2004`, rat tibia, IHC, Fig. 3A). The hypertrophic enrichment the
   atlas relied on is **mRNA** (`agoston2007`, Prkg2 4.4-fold), from micro-dissected mouse
   tibia whose zones are **resting/proliferative combined, hypertrophic, and mineralized** —
   the study contains no RZ-versus-PZ comparison at all. mRNA and protein disagree, across two
   species and two assay types, and only the mRNA reached the node.
2. **Direction.** A linear CNP → GC-B → cGMP → PKG-II chain predicts that losing PKG-II
   phenocopies losing GC-B. It does the opposite. The `Prkg2`-mutant KMI rat growth plate is
   **2.6× expanded** — 665 ± 47 µm vs 255 ± 34 µm wild type, n = 8 — through an accumulated
   intermediate layer of **postmitotic non-hypertrophic** chondrocytes (`chikuda2004`). The
   cartilage-specific `Npr2` knockout hypertrophic layer is **23.0% of control** with a thinner
   plate overall (`nakao2015`). Same nominal pathway, opposite sign.

**All three primaries flag this themselves and the field has not absorbed it.**
`chikuda2004`: "there is a marked difference between CNP^−/− and cGKII^−/− mice in the histology
of the growth plate: the growth plate of the former is reduced in height … whereas that of the
latter is increased in height. **This may indicate the involvement of other signaling
pathway(s)** in the CNP-mediated endochondral ossification." `nakao2015`: "there still remains
elusive problem that the narrowed growth plate of CNP or GC-B knockout is quite different from
the extraordinary widened growth plate of cGKII knockout mice." `agoston2007`: "the cartilage
phenotypes of cGKII- and CNP-deficient mice are **not identical**, suggesting the possibility of
an additional role of cGKI."

**The named, untested alternative.** Both `chikuda2004` and `agoston2007` independently propose
the same decisive experiment and it has still not been done: the **cGKI/cGKII double knockout**.
`agoston2007` reports Prkg1 at **5.9-fold** zonal enrichment, *higher* than Prkg2's 4.4-fold, so
the isoform the atlas named as the effector is not even the more enriched of the two. This is
the ANKH-shaped failure: the mechanism was assigned in a system where the alternative — cGKI —
was present, expressed at higher level, and never removed.

**A second effector arm, also missed.** `miyazaki2022` (eLife 2022, full text) shows
CNP-facilitated bone growth in tibia explant is **abolished** by chondrocyte-specific *Trpm7*
ablation, via PKG acting on the **BK channel** → hyperpolarisation → TRPM7 Ca²⁺ entry → CaMKII.
That is a necessity result on a PKG substrate other than SOX9 or GSK-3β. The reference was
already in the bibliography but was not linked from `pkg2_kinase`, `cnp_protein` or
`npr2_receptor`.

### Blast radius — traced

| Object | Status | Action |
|---|---|---|
| `pkg2_kinase` (node) | **Corrected, regraded B → C** | The zonal-explanation sentence is removed and replaced by the protein/mRNA disagreement stated explicitly; the KMI expansion figure (665 vs 255 µm) added as a quantitative row; the phenotype-direction conflict with `nakao2015` stated; cGKI named as the untested alternative; `miyazaki2022` added. `contradicts: [agoston2007, nakao2015]`. Grade C is correct: animal-only, conflicting. |
| `npr2_receptor` (node) | **Corrected** | The sentence "PKG-I/II are far higher in hypertrophic cells … which is the explanation for the zonal partition" is replaced. Two independent attribution errors also fixed (see mechanism_audit): the prehypertrophic GC-B IHC map is **not** `nakao2015` data, and `agoston2007`'s zones are not RZ/PZ/HZ. |
| `cnp_protein` (node) | **Corrected** | Zonal partition restated as graded rather than exclusive (BrdU significantly reduced in the `Npr2` cKO); `miyazaki2022` linked. |
| `cgmp_second_messenger` (node) | **Annotated** | Already said cGMP "acts through PKG-II **and PKG-I**" — the only node in the graph that had it right. Note added recording that the relative weighting is undetermined and that the double knockout is the discriminating experiment. **No correction needed; this is the node that would have caught the error.** |
| `pthrp_cnp_crosstalk` (node) | **Checked, annotated** | Uses `chikuda2004` for the SOX9-nuclear-entry mechanism, which is intact — the SOX9 result is sound; only the zonal and phenotype-direction inferences failed. Note added. |
| `e00108` `cgmp_second_messenger --activates--> pkg2_kinase` (B) | **Topology correct** | Note added: cGKI is co-expressed at higher zonal enrichment and is not excluded. |
| `e00109` `pkg2_kinase --inhibits--> sox9_tf` (C) | **Topology correct, grade correct** | `chikuda2004`'s SOX9 nuclear-entry data are direct and were reproduced by RNAi rescue; unaffected by the zonal error. |
| `e00110` `pkg2_kinase --phosphorylates--> gsk3b_kinase` (C) | Unaffected | Biochemical, zone-independent. |
| `e00120` `cnp_protein --activates--> pkg2_kinase` (C, ref `agoston2007`) | **Downgraded evidence note** | `agoston2007` is a *correlative zonal expression* study; it does not show CNP activating PKG-II. Note records that the supporting evidence is co-expression, and that `chikuda2004` Fig. 4D (CNP fails to rescue KMI chondrocytes) is the actual epistasis evidence. Refs corrected to `[chikuda2004, agoston2007]`. |
| `e00149` `cnp_protein --required_for--> pkg2_kinase` (B, `dazgonzlez2022`) | **Direction queried, note added** | The human PRKG2 acromesomelic phenotype shows PKG-II is required for the CNP output, not that CNP is required for PKG-II. Flagged for the edge-audit pass rather than silently reversed here. |
| `e00718` `pkg2_kinase --required_for--> npr2_agonist_class` (speculative) | Unaffected | Already `speculative`; the therapeutic inference is unchanged since vosoritide acts at the receptor. |
| `p90002` (new quant row) | **Added** | KMI growth plate height 665 ± 47 µm vs wild-type 255 ± 34 µm, n = 8, rat, `chikuda2004`. The atlas previously carried **no** quantitative row for the *Prkg2* phenotype, which is why the sign conflict was invisible to any numeric check. |
| `nakao2015` hypertrophic-zone rows (`npr2_receptor` 23.0%, `cnp_protein` 34.6%) | **Retained, n added** | These measurements are correct and unaffected. `n = 5` per group added from the figure legend. |
| `g_l3core_003`, `g_l3core_004` (gaps on this cluster) | **Re-read** | Neither presupposes the dead mechanism. `g_l3core_003`'s `what_is_known` already cited `miyazaki2022` — the gap was ahead of the nodes. **No malformed gaps.** |
| `g_l12b`, `l11path`, `mr002` gaps mentioning PKG | **Checked, unaffected** | Pharmacology and pathology framings; none asserts the zonal explanation. |
| `vosoritide`, `npr2_agonist_class` (L12 nodes) | **Checked, unaffected** | Both act at NPR2; neither claims PKG-II zonal partition. |

**Match audit:** 11 nodes/gaps matched `PKG|cGKII|Prkg`. **4** carried the superseded framing
(`pkg2_kinase`, `npr2_receptor`, `cnp_protein` indirectly, `pthrp_cnp_crosstalk` marginally);
**1** (`cgmp_second_messenger`) was already correct; **6** were unaffected mentions. As in
CORR-001, raw match count (11) overstates blast radius (4) by ~2.75×. Every match was read.

### Reference disposition classification

| Ref | Classification | Reasoning |
|---|---|---|
| `agoston2007` | **interpretation_superseded** | The microarray measurements are sound and are retained in full — Prkg1 5.9-fold, Prkg2 4.4-fold, Npr2/Nppc/Npr3 flat, Npr3 induced 16-fold by CNP. What failed is the atlas's inference from them: mRNA enrichment in a combined resting/proliferative-vs-hypertrophic contrast was read as a protein map across RZ/PZ/HZ, and as *the* explanation for zonal partition. The paper itself never claims more than "can explain". Measurements retained; two of them (Prkg1 enrichment, Npr3 induction) are newly surfaced by this audit. |
| `chikuda2004` | **observation_stands** | Both the correcting observations (prehypertrophic PKG-II protein; expanded KMI plate) and the mechanism it does establish (SOX9 nuclear entry, RNAi rescue) stand. |
| `nakao2015` | **observation_stands** | Correcting evidence for the phenotype-direction conflict; its own measurements were already correctly recorded. |
| `pfeifer1996` | **observation_stands** | The `Prkg2`-null dwarfism with expanded plate is the mouse counterpart of the KMI result and is consistent with the corrected model. Not read in full (not open access); queued. |
| `miyazaki2022` | **observation_stands** | The alternative-effector evidence. |
| `dazgonzlez2022` | **observation_stands** | Human biallelic *PRKG2* acromesomelic dysplasia is unaffected by the zonal question — PKG-II is genuinely required for the pathway output in humans. This is precisely the disposition CORR-001 established: the human genetics survives intact even though the murine zonal story it was attached to did not. |

Standing policy applied: **no measurement retired.** The correction is entirely to
interpretation and to one grade.

---

## CORR-004 — reserved

Next correction entry goes here. Corrections are appended, never overwritten.

---

## CORR-004 — a withdrawn paper was carrying an L10→L3 seam

**Date traced:** 2026-08-05
**Trigger:** the first full `verify_refs.py` run over all 1,049 references. Every prior
run had been scoped, and the report on disk held **one** entry.
**Finding:** `wu2013` (PMID 23940039, *J Biol Chem*) carries the Europe PMC publication
type **Retracted Publication**. The notice is a **Withdrawal**, *J Biol Chem* 2020;
295(37):13137, PMID 32917830.

**Disposition: `both_invalid`.** The notice has no retrievable statement of reason, so
there is no basis on which to keep the observation while discarding the interpretation.
Where a retraction notice explains itself, `observation_stands` can be argued; here it
cannot, and inventing a reason to preserve a convenient result is the failure this
taxonomy exists to prevent.

**`wu2012` (PMID 22696219), from the same laboratory, carries no retraction or
correction notice and stands.** It was checked specifically, not assumed.

### What the withdrawn paper was holding up

`wu2013` was the **in vivo** half of the FGF21 story: four weeks of food restriction
raising LEPROT/LEPROTL1 in liver *and* tibial growth plate, absent in `Fgf21`-knockout
mice, restored by rhFGF21 add-back. That knockout-plus-rescue design is what made the
pathway causal rather than correlative — and it was, on the atlas's own reading, *"the
only DEMONSTRATED molecular entry point from the environment layer into a local
signalling node that does not route through GH or IGF-1 systemically."*

Removing it does not weaken a detail. It removes the demonstration.

### Blast radius — traced

| Object | Status | Action |
|---|---|---|
| `wu2013` (bibliography) | **Flagged** | `retracted: true`, notice PMID, disposition `both_invalid`, and a note recording that `wu2012` was checked and is clean. |
| `klotho_beta_cofactor` (node) | **Corrected** | Summary rewritten to state plainly what stands and what has fallen away. Node confidence stays **D**. |
| — claim 1, *KLB expressed in growth plate chondrocytes* | **C → D** | It was graded C for being replicated across `wu2012` and `wu2013`. The replication is gone, so it takes the one-grade drop to D. This is the propositional-replication rule running in reverse for the first time. |
| — claim 2, *FGF21 mediates undernutrition GH insensitivity* | **C → X** | Rested entirely on `wu2013`. Graded **X** — circulates in the literature, not traceable to standing primary data — rather than deleted, because deleting it makes the atlas silent about a claim readers will still meet. |
| — quantitative row *"4 weeks of food restriction"* | **Voided, tombstoned** | Value replaced with `WITHDRAWN`, `value_unverified: true`, and text explaining what happened, so a reader who saw the number in an earlier version can find out why it is gone. |
| `e01055` `energy_availability_growth --activates--> klotho_beta_cofactor` | **`activates` C → `hypothesized_link` speculative** | Not regraded — reclassified. With no in vivo result there is no demonstration left to grade. `traversal_usable: false`, `gap_id: g_l0l9_009`. **The L10→L3 seam this edge carried is now open, and that is the true state.** |
| `e01056` `energy_availability_growth --activates--> fgfr1_receptor` | **Kept at D, magnitude edited** | The siRNA epistasis is `wu2012` and unaffected. The LEPROT/LEPROTL1 clause was `wu2013` and has been removed from the magnitude statement; `wu2013` removed from refs. |
| `e01057` `stunting --hypothesized_link--> klotho_beta_cofactor` | **Already speculative** | Magnitude annotated: the murine result that motivated the hypothesis is withdrawn, which weakens it further without removing it — the human exposure question was never answered either way. |
| `g_l0l9_001`, `g_l0l9_009`, `g_para_007` | **Widened, not closed** | Each carries the withdrawal note and a statement of how its question changed. `g_l0l9_009` is the sharpest: it asked whether the FGF21 route is *mouse-specific*, and there is now no standing in vivo demonstration in the mouse either, so the comparison has lost one of its sides. |
| `audit/paralog_audit.md` | **Cross-referenced** | Its `pde3b`-style reasoning for `klotho_beta_cofactor` cited `wu2013` as the ligand-selective result that made receptor identity secondary. Noted on the node. |

### A second correction fell out of the same trace

The `paralog_risk` note on `klotho_beta_cofactor` argued that FGFR3 must carry the
effect **because FGFR1 is not expressed in the human growth plate** (`delezoide1998`).

The P8-01 re-analysis of GSE9160 contradicts that premise: **FGFR1 is detected on 5 of 7
probe sets in all five compartments of both human donors**, alongside FGFR3, FGFR4 and
FGFR2. All four FGFRs are present in the human physis. The receptor-assignment question
is therefore *open* in humans, not settled against FGFR1, and it can no longer be argued
from absence in either direction. Recorded on the node and in `g_para_007`.

### Verification performed

- Retraction confirmed from the live Europe PMC record: pubtype `Retracted Publication`,
  `commentCorrectionList` giving `Retraction in: J Biol Chem 2020;295(37):13137`.
- Retraction notice retrieved (PMID 32917830, title begins "Withdrawal:"). No abstract or
  reason text is available through the API; **no reason is asserted here.**
- `wu2012` queried separately: pubtypes clean, `commentCorrectionList` null.
- Repository-wide `grep` for `wu2013` across nodes, edges, gaps, shards, quant rows and
  audit files; every hit is accounted for in the table above.

### The check that would have caught this earlier, now installed

`validate.py` now **errors** when a node cites a `ref_id` flagged `retracted` in the
bibliography without declaring `retracted: true` on its own `key_ref`. Negative-tested:
removing the declaration produces the error, restoring it clears it.

This is the failure mode that gets *worse* with time rather than better. The paper stays
resolvable, the PMID stays valid, `addref.py` stays happy, `verify_refs.py` reports `ok`
— the retraction only shows up in a publication-type field that nothing was gating on.
The lesson is not "check for retractions"; it is that **an anti-fabrication system built
around *does this source exist* is silent about *is this source still standing*.**

---

## CORR-005 — three of my own four negatives did not survive independent platforms

**Date traced:** 2026-08-06
**Trigger:** P8-02, run for the purpose of trying to break P8-01's results
(`atlas/quant/notebooks/p8_02_independent_corroboration/`).
**Superseded model:** four both-donor non-detections in human growth plate, reported by
P8-01 on Affymetrix HG-U133 Plus 2.0 in two donors, and entered into the graph at grade
D on 2026-08-05.

**Disposition: `both_invalid` for N1 and N4, `interpretation_superseded` for N2,
`observation_stands and strengthened` for N3.**

### What was tested

Three human growth-plate expression series sharing **no donor and no platform** with
GSE9160: GSE22855 (Illumina HumanWG-6), GSE32398 (Affymetrix GPL9828, prepubertal),
GSE18338 (Agilent, one girl through puberty). 13 growth-plate arrays, three platform
families, at least eight donors. All three passed the preregistered tissue gate with
COL2A1 at the 100th percentile of every array.

### Result

| claim | verdict | action |
|---|---|---|
| **N1** NPPC (CNP) undetectable | **REFUTED** — detected at the ~70th percentile in 2 of 3, at every stringency | withdrawn |
| **N2** no cGMP-hydrolysing PDE detectable | **REFUTED as a blanket** — PDE3B in all 3, PDE5A at the 91st percentile in 1 | rewritten gene by gene |
| **N3** no CYP19A1, no ESR2 | **CORROBORATED** at every stringency in all 3, with ESR1 detected as internal control | **D → C** |
| **N4** MCT8 undetectable | **REFUTED** — SLC16A2 detected in all 3 at every stringency | withdrawn, gap re-opened |

### Blast radius — traced

| Object | Action |
|---|---|
| `cnp_protein` | NPPC non-detection observation and its quantitative row **removed**; replaced with the refutation, the percentiles, and the probe-set explanation. The species discrepancy P8-01 raised against the mouse cartilage-specific *Nppc* knockout is **withdrawn with it** — local CNP message is present in human plate, as in mouse. |
| `mct8_transporter` | MCT8 non-detection **removed**. The system-L alternative survives on its own evidence (SLC7A5 at the 78th–95th percentile in all three), not on MCT8's absence. |
| `g_l11path_023` | **RE-OPENED.** `answered_by_reanalysis` reversed to `REOPENED_by_p8_02`. `what_is_missing` rewritten: both candidate routes are transcriptionally present, so the question can no longer be narrowed by absence. |
| `g_l3core_006` | Downgraded `answered_by_reanalysis` → `partially_informed_after_p8_02`. |
| `aromatase_cyp19a1`, `estrogen_receptor_beta` | **D → C.** Four datasets, four platform families, ~10 donors, working internal control. Explicitly **not** B: a non-detection in bulk tissue is neither human genetic nor interventional evidence. |
| `pde_isoform_inventory` | Blanket claim replaced by the gene-by-gene table. |
| `pde5a` | Platform disagreement recorded as a contradiction, not averaged. Grade unchanged at D. |
| `pde3b` | **Reading inverted.** PDE3B is present in human growth plate on every platform; PDE3A is absent on all four. The paralog audit's AT_RISK verdict is not removed — it is pointed at PDE3B rather than PDE3A. |

### The design error, named

| claim | probe sets behind the P8-01 negative | outcome |
|---|---:|---|
| N1 NPPC | **1** | refuted |
| N4 SLC16A2 | **1** | refuted |
| N3 CYP19A1 + ESR2 | **13** | corroborated |

**A single-probe non-detection is not a negative.** P8-01 reported every probe count
honestly and then treated a 1-probe non-detection as the same kind of object as a
13-probe one. The rule now stated: *a non-detection may enter the graph only if the
platform carries more than one probe for the transcript, or a second platform agrees.*

### What this says about the P8-01 preregistration

It worked. The design was strong enough that the numbers could be checked, the probe
counts were on the table for anyone to notice, and the refutation was possible precisely
because nothing was hidden. What it lacked was the multi-probe rule above — a design
omission, found by the round that was built to attack it.

`PREREGISTRATION.md` §4.5 of P8-02 committed, before any number was seen, to reporting a
refutation with the same prominence as a corroboration. This entry is that promise being
kept.
