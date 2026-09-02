# Confidence grade changes

Every change to a node's confidence grade is recorded here with its justification.
Grades are claims about evidence strength, so changing one silently would defeat the
purpose of having them.

---

## 2026-08-05 — Baseline A/B-tier audit and re-grade (DOWNGRADES)

Run before any synthesis was built on the grades, per the density diagnostics.
Tool: `atlas/tools/grade_audit.py` (criteria encoded there, not applied by hand).

**Criteria tested**
- **A** = "replicated in humans with direct measurement or interventional data"
  → operationalised as ≥2 primary-type refs **and** `human_evidence: direct` **and**
  `human` in `species_basis`.
- **B** = "strong animal mechanism + consistent human correlative/genetic support"
  → requires `human_evidence` ≠ `absent` and ≥2 refs.

**Result: A-tier inflation 28.2% (35/124), B-tier 18.2% (16/88). 51 nodes downgraded.**

| | before | after |
|---|---:|---:|
| A | 124 | **89** |
| B | 88 | **106** |
| C | 134 | **150** |
| D | 52 | **53** |
| E | 11 | 11 |
| X | 1 | 1 |

### The finding that matters more than the rate

**Zero A-grade nodes failed on human-evidence or species grounds.** Every single
failure was citation *thinness* — fewer than two primary sources. Not one A-grade node
was passing animal data off as human fact, and not one lacked `human` in its
`species_basis`.

That distinction is the whole point of running the audit. An inflation rate driven by
species laundering would mean the atlas's core epistemic discipline had failed and the
content needed re-reading. An inflation rate driven by citation count means the grades
were *directionally honest* but over-claimed on replication — the content is sound and
the fix is to add a second independent primary, not to re-examine the biology.

### Method correction made during the audit

The first implementation downgraded any single-reference A node to **D**. That produced
an obviously wrong result: `height_gwas` — a meta-analysis of **5.4 million** individuals,
the strongest human evidence in the atlas — was scored "D: single study, in vitro only,
or conflicting reports". The rule was wrong, not the node.

Two fixes, applied before any grade was written:
1. **Downgrade by one grade, not to a floor.** A node failing only on citation count is
   under-evidenced, not unreliable.
2. **Meta-analyses and systematic reviews count as internally replicated.** A pooled
   analysis of many cohorts satisfies the spirit of A's "replicated" requirement even as
   a lone reference, provided the human-evidence criteria are met.

`height_gwas` accordingly sits at **B**, and is a prime candidate for re-upgrade once a
second independent primary is attached.

### Disposition

These 51 downgrades are **not final**. L8 is designed as the confidence-upgrade engine:
each monogenic locus is a human dosage experiment attached to a mechanistic node, and
attaching it supplies exactly the second human primary these nodes lack. Upgrades earned
that way are logged below with the evidence that justified them.

---

## Upgrade admissibility — replication is PROPOSITIONAL, not topical

An upgrade is admissible only if the second reference **independently tests the same
proposition by a different route**. Topical adjacency is not replication. A paper on
*ACAN* dosage does not replicate a claim about aggrecan turnover kinetics merely
because both concern aggrecan; two papers agreeing that a molecule "matters" replicate
nothing.

**Every upgrade must record all of these fields. An entry missing any of them is not an
upgrade, it is citation-stacking, and is rejected.**

```yaml
# STEP 0 (precondition, MR-004 item 3): ref_2 MUST NOT already appear in the
# node's key_refs. Three of the first ten rejections failed here - the proposed
# 'replication' was a reference the node already cited, i.e. evidence already
# priced into the original grade. Check novelty BEFORE assessing propositionality.
- node_id:
  proposition_tested:     # ONE falsifiable sentence. If you cannot state it in one
                          # sentence, the node is making several claims and needs
                          # claim_grades (see below), not an upgrade.
  ref_1:
    ref_id:
    what_it_shows:        # what THIS paper demonstrates about THAT proposition
  ref_2:
    ref_id:
    what_it_shows:
  independence_basis:     # different method | different cohort | different direction
                          # of perturbation (gain- vs loss-of-function) | different
                          # species with human confirmation. State which.
  grade_before:
  grade_after:
```

**Rejected attempts are logged too.** The rejection rate is itself a measurement: it
quantifies how thin genuinely replicated human evidence is in this field, which is a
finding this atlas is positioned to make and most reviews are not.


### Rejection pattern analysis (MR-004 item 3) — the stated tally was wrong

The Phase 3 report claimed two patterns covering all ten rejections, with counts 6 and 2.
That sums to 8, and MR-004 was right to challenge it. Re-reading all ten rejection rows
gives **five** patterns, not two — and the largest one had not been named at all.

| # | pattern | count | rejections |
|---|---|---:|---|
| **B** | **NO NEW REFERENCE — the candidate "replication" was ALREADY cited on the node** | **3** | `npr2_receptor`, `cnp_protein`, `pth1r_receptor` |
| A | node's grade was set by a **different claim** than the second paper tests | 4 | `aggrecan_acan`, `ihh_protein`, `fgfr3_receptor`, `comp_protein` |
| C | second source **not independent** of the first (curation/aggregation) | 1 | `spondyloepiphyseal_dysplasia` (ClinGen curates the same primary) |
| D | evidence **quality** insufficient — lone primary, remaining refs review/abstract-only | 1 | `collagen_type_ii` |
| E | **species or developmental-window mismatch** between the two sources | 1 | `growth_plate_senescence` (rabbit; human methylome at 7–21 post-conception weeks) |

**Pattern B is the unanticipated one, it is the most common, and it is the most
informative.** In three of ten attempts the proposed "second primary" was a reference the
node already cited. That is not a weak replication — it is **double-counting evidence
already priced into the original grade**. An upgrade granted on pattern B would have
inflated a grade using nothing new whatsoever, and no propositional test would have caught
it, because the proposition genuinely is supported by that reference. What fails is
*novelty*, not relevance.

**Rule amendment, now in force:** before assessing propositional independence, check that
ref_2 is **not already present in the node's `key_refs`**. This is a cheap mechanical
precondition and it screens the single largest failure mode. Added as step 0 of the
upgrade schema above.

Corrected headline: **2 accepted, 10 rejected, five distinct failure patterns**, of which
the largest — 3 of 10 — is a reference the node already had.

### Upgrades — accepted

Recorded during the L8 completion sweep (shard `l8gen`, 2026-08-05). Twelve node/proposition pairs
were assessed against the admissibility rule above; two were admitted.

| date | node | proposition | ref_1 | ref_2 | independence basis | from → to |
|---|---|---|---|---|---|---|
| 2026-08-05 | `estrogen_receptor_alpha` | ERalpha function is required for epiphyseal fusion, so losing it permits continued longitudinal growth past the normal age of closure. | `brjesson2012` | `smith1994` | different species with human confirmation | B → **A** |
| 2026-08-05 | `schmid_metaphyseal_chondrodysplasia` | Mutations in COL10A1 cause Schmid metaphyseal chondrodysplasia. | `warman1993` | `meng2025` | different method and different cohort | B → **A** |

```yaml
# STEP 0 (precondition, MR-004 item 3): ref_2 MUST NOT already appear in the
# node's key_refs. Three of the first ten rejections failed here - the proposed
# 'replication' was a reference the node already cited, i.e. evidence already
# priced into the original grade. Check novelty BEFORE assessing propositionality.
- node_id: estrogen_receptor_alpha
  proposition_tested: >-
    ERalpha function is required for epiphyseal fusion, so losing it permits continued
    longitudinal growth past the normal age of closure.
  ref_1:
    ref_id: brjesson2012
    what_it_shows: >-
      Old female ERalpha-null mice continue growing: tibiae 8.3% longer (P<0.01) and growth
      plate height 18% greater (P<0.05) than wild type. An engineered germline deletion, with
      histomorphometric and long-bone-length readouts, in a species that does not normally fuse.
  ref_2:
    ref_id: smith1994
    what_it_shows: >-
      A 28-year-old man homozygous for a disruptive ESR1 mutation reached 204 cm with
      radiographically incomplete epiphyseal closure and a documented history of continued linear
      growth into adulthood, despite ELEVATED serum estradiol and estrone and normal testosterone
      with normal masculinisation. A natural human null, with adult stature and radiographic
      closure as readouts, in which ligand and androgen action are demonstrably intact.
  independence_basis: >-
    different species with human confirmation. Also different perturbation route (engineered
    deletion versus natural disruptive mutation) and different readout (tibial length and plate
    histomorphometry versus adult stature and radiographic epiphyseal status). Crucially the human
    case controls for the confound the mouse cannot: estradiol was high, so the phenotype cannot be
    attributed to absent ligand. Supported further by bernard2017 (three ESR1 R394H homozygous
    siblings with delayed bone maturation), an independent family.
  grade_before: B
  grade_after: A

- node_id: schmid_metaphyseal_chondrodysplasia
  proposition_tested: >-
    Mutations in COL10A1 cause Schmid metaphyseal chondrodysplasia.
  ref_1:
    ref_id: warman1993
    what_it_shows: >-
      Linkage of the disorder to a 13 bp COL10A1 deletion in a single large Mormon kindred at
      lod 18.2 (theta = 0), the deletion producing a frameshift that shortens the alpha-1(X) chain
      by nine residues in the conserved NC1 domain. A family-based linkage design.
  ref_2:
    ref_id: meng2025
    what_it_shows: >-
      COL10A1 variants across 128 unrelated cases (4 new plus 124 published), with
      genotype-phenotype stratification: height Z -3.62 +/- 1.95 for missense versus
      -1.99 +/- 1.28 for truncating variants (P=0.013) and median onset 12 versus 72 months for
      NC1 versus non-NC1 variants (P=0.0014). An unrelated-case mutation-spectrum design.
  independence_basis: >-
    different method and different cohort. Linkage within one extended pedigree versus mutation
    spectrum across 128 unrelated probands three decades later, with no sample overlap. The two
    designs fail in different ways - linkage can be confounded by a linked variant segregating in
    one family, spectrum analysis by ascertainment - and neither failure mode is shared.
  grade_before: B
  grade_after: A
```

### Upgrades — REJECTED (citation-stacking attempts)

Ten of twelve candidate upgrades assessed during the L8 sweep were rejected.
**Rejection rate: 10/12 = 83%.**

That number is the finding. Every rejected candidate had a plausible-looking second human reference
attached to the same molecule; none of them tested the same *proposition*. The L8 layer supplies a
large amount of new human genetic evidence, and almost all of it lands on propositions the target
node was not the weakest on. Two failure patterns account for all ten:

1. **The node's grade is set by a different claim.** Six rejections. A gene node supplies a human
   dosage result; the mechanistic node is graded B or C because of an unresolved mechanistic
   sub-claim that the dosage result does not touch. The correct remedy is `claim_grades`, not an
   upgrade — which is what the admissibility rule already says.
2. **The second reference is not source-independent.** Two rejections, both where the candidate
   "replication" was a systematic aggregation or curation whose input was the published case
   literature that includes ref_1.

| date | node | proposition | why rejected |
|---|---|---|---|
| 2026-08-05 | `npr2_receptor` | Reduced NPR2 signalling reduces human stature and increased NPR2 signalling raises it. | No new reference. The node already cites `olney2006`, `bartels2004`, `hannema2013` and `lauffer2020`, so the proposition is already replicated within it. Its B grade is set by a different, explicitly unresolved claim — what sets the zonal partition of the CNP effect — which no genetic dosage result addresses. |
| 2026-08-05 | `cnp_protein` | CNP gene dosage sets human longitudinal bone growth bidirectionally. | No new reference; `hisadooliva2018`, `bocciardi2007` and `moncla2007` are already on the node. The weakest claim is the downstream effector assignment, which carries a retraction (CORR-003) and is untouched by ligand-dosage genetics. |
| 2026-08-05 | `aggrecan_acan` | Aggrecan synthesis and breakdown are fastest in the resting/proliferative zone. | The canonical inadmissible case, and it arose for real. `gkourogianni2017` (ACAN haploinsufficiency, adult height -2.8 SDS) and `nilsson2014_2` concern aggrecan *dosage*; `shapses1994` concerns aggrecan *turnover kinetics* in bovine explant. Both concern aggrecan and they replicate nothing about each other. |
| 2026-08-05 | `pth1r_receptor` | Constitutive PTH1R activation delays hypertrophic differentiation. | No new reference: `schipani1995` (human H223R) and `schipani1997` (mouse targeted H223R transgene) are both already on the node. Nothing in the L8 sweep is independent of them. |
| 2026-08-05 | `ihh_protein` | Reduced IHH gene dosage reduces human stature. | `sentchordimont2020` (16 heterozygous IHH probands) is genuinely new to this node, but the node's grade is set by the transfer of an embryonic mouse proliferation/PTHrP mechanism (12.5–18.5 dpc, null dies at birth) to the postnatal growth plate. A human dosage series does not replicate that mechanism. Added as a `claim_grade` instead. |
| 2026-08-05 | `fgfr3_receptor` | FGFR3 is a negative regulator of bone growth: reducing its signalling lengthens bone. | `toydemir2006` (human FGFR3 p.R621H partial loss of function, CATSHL tall stature) genuinely completes the human bidirectional series alongside the mouse nulls `colvin1996`/`deng1996`. But the node's grade is set by a contradiction in *sign* over c-Cbl-mediated ubiquitination (`cho2004` versus Monsonego-Ornan 2004, logged as g_l2d_003), which a stature phenotype cannot adjudicate. The node makes several claims and needs `claim_grades`, which the rule above says explicitly. |
| 2026-08-05 | `comp_protein` | Pathogenic COMP variants are concentrated in the calcium-binding type-3 thrombospondin repeats. | Topical, not propositional. `thur2001` shows selected mutations abolish calcium binding — a mechanistic claim about a handful of alleles. `ni2026` shows 87.7% of 471 probands carry a T3-domain variant — a distributional claim. They are different propositions that happen to name the same domain. |
| 2026-08-05 | `collagen_type_ii` | Collagen II dosage and structure set long-bone length. | `zhan2025` (7 SEDC families) is a single primary and the node's other refs are a review and an abstract-only immunoelectron-microscopy paper. The node's grade is anyway set by compositional claims (fibril diameter determined by collagen XI content, MMP-13 cleavage in the lower hypertrophic zone) that no COL2A1 genotype series tests. |
| 2026-08-05 | `spondyloepiphyseal_dysplasia` | The severity of type II collagenopathy tracks mutation class, with triple-helical glycine substitutions more severe than null alleles. | `webb2026` (ClinGen curation) is not source-independent of `zhan2025`: ClinGen classifies gene-disease validity by reviewing the same published case literature. Stacking a curation onto a primary is exactly the pattern the rule forbids. The real deficiency is quantitative and is recorded as gap `g_l8gen_005`. |
| 2026-08-05 | `growth_plate_senescence` | Growth plate senescence is accompanied by progressive loss of DNA methylation. | `nilsson2005` is rabbit. `mcdonnell2024` maps the human chondrocyte methylome but at 7–21 post-conception weeks, i.e. before the postnatal physis exists. Same molecular readout, different developmental epoch, different species, different proposition. Recorded as gap `g_l8gen_013` instead. |
| 2026-08-05 | `height_gwas` | Common variants jointly explain roughly 40–60% of adult height phenotypic variance. | The audit above nominated this node as "a prime candidate for re-upgrade". It fails on independence: `wood2014` (n=253,288) and `wainschtein2026` (UK Biobank, n=347,630) are drawn from cohorts nested inside `yengo2022`'s 5.4 million. Every large height analysis reuses the same biobanks, so the field cannot currently supply an independent replication of its own flagship estimate. Left at B deliberately. This is a statement about the structure of human genetics, not about this node's quality. |

Note on the denominator: twelve is the number of node/proposition pairs formally assessed, not the
number of nodes touched. Several nodes (`aromatase_cyp19a1`, `gh_receptor`, `stat5b_tf`,
`als_igfals`, `pappa2_protease`, `igf1_receptor`, `collagen_type_x`, `hdac4_protein`,
`acan_related_short_stature`, `npr2_heterozygous_short_stature`, `pseudoachondroplasia`) already
held grade A and were not candidates.

