# Round 18 — Acquisition sweep: what exists, what is now on disk, and what I cannot get

**Date:** 2026-08-06 · **Branch:** `claude/growth-system-atlas-yl5esl`
**Instruction:** find everything needed to unlock height, download all obtainable, of any
obscurity, not limited to studies.

This is an inventory, not an argument. Every claim about what a resource *contains* is
either read from the resource or read from its metadata, and which one is stated.

---

## 0. The target chosen, and why

The previous round's coverage analysis found the atlas structurally lopsided:
**241 nodes on velocity/hypertrophy pharmacology against 77 on resting-zone stem cells,
of which only 9 are grade A and 32 record human evidence as ABSENT.** Every lever in the
atlas converges on 2–4% (pharmacology) to 7–8% (lifetime genetics), which is the
signature of a shared constraint rather than of many independent small effects. The
shared constraint the atlas names is the **division budget**: growth plate senescence is
*division*-dependent, not time-dependent, so velocity and duration draw on one pool.

So the sweep was aimed at the division-budget axis and at the human end of it, not at
more pharmacology.

---

## 1. What was swept

| Registry | Query set | Records returned |
|---|---|---|
| NCBI GEO (`gds`) | 9 queries: human growth plate/epiphysis, chondrocyte, cartilage development, physis/physeal, limb skeleton, closing-plate species, senescence, GH-treated | **1,139 unique series**, 832 growth-plate-relevant |
| Europe PMC | 10 queries, one per atlas unknown (histomorphometry by age, clonal tracing in non-mouse, senescence budget, why the mouse never closes, surgical-specimen routes, GH registries, chondrocyte cycle time, regeneration, human stem markers) | **2,832 unique records, 2,462 open access** |
| ClinicalTrials.gov v2 | 5 queries: any stature outcome measure, short stature, tall stature/epiphysiodesis, growth-plate drugs, paediatric sacubitril | **2,585 unique trials** |

Tools committed: `atlas/tools/geo_sweep.py`, `geo_triage.py`, `geo_get.py`,
`epmc_sweep.py`, `epmc_get.py`, `ctg_sweep.py`, `ctg_filter.py`, `ctg_results.py`,
`ctg_index.py`, `ctg_extract.py`, `hpo_tall.py`, `zone_enrich.py`.

---

## 2. What is now on disk

Raw data lives in `acquire/` and is **not committed** (1.8 GB); manifests, indices and
derived tables are in `query/acquisition/`.

### 2.1 Expression datasets (GEO), 1.7 GB

| Accession | Why it was taken | Status |
|---|---|---|
| **GSE18338** | **Human growth plate, tibia, PRE-puberty / EARLY puberty / LATE puberty — the same girl at Tanner B2 and B3.** A within-subject human growth plate age series. Nothing else like it exists. | matrix + RAW (62 MB) |
| **GSE16981** | Rat, spatial **and temporal** gene expression across the growth plate — the senescence axis in a species where growth ceases | RAW (88 MB) |
| **GSE114919** | Rat **and** mouse, "differential ageing of growth plate cartilage determines skeletal proportions" | normalised counts, both species |
| GSE233188 | *In vivo* clonal tracking of **human** skeletal stem cells with scRNA-seq readout | RAW (18 MB) |
| GSE246390 | Biomechanical loading in **human** growth plate cartilage, children, n=19 — the mechanical term of the flow model | raw + normalised counts |
| GSE267139 | Human cartilage development at single-cell resolution, fetal, n=25 | RAW (1.0 GB) |
| GSE209948 | Early human knee joint development, scRNA-seq | RAW (354 MB) |
| GSE107649, GSE17368, GSE6565, GSE40942, GSE54216 | Human growth-plate-specific genes; human epiphyseal cartilage; fetal cartilage; fetal MSC vs growth plate; rat zonal | matrices/RAW |

Triage of all 832 relevant series is in `query/acquisition/geo_triage.json`.

### 2.2 The clinical-trial corpus — the largest single acquisition

The losartan result came from a trial that prespecified height, posted the results, and
was never read for growth. That is a *shape* of record, so the whole registry was asked
for it.

- **678** trials carry a genuine stature/length endpoint (height, growth velocity, bone
  age, arm span, segment ratio — weight-for-height and growth *factors* excluded).
- **506** of those have **results posted**. All 506 full records downloaded.
- **269** of those are **in children, on an intervention that is not already a growth
  drug** — i.e. natural experiments on human height that nobody has aggregated.
- Extraction produced **5,445 arm-level height numbers and 340 posted p-values**
  (`query/acquisition/ctg_measures.csv`).

**Positive control, run before extraction and passed:** the extractor had to reproduce
NCT00429364's `Annual Rate of Change in Height` as 0.822 vs 0.935 cm/yr — the values this
atlas had already read by hand. It did. Had it failed, the other 505 would not have been
extracted.

Interventions in the unexamined set include tofacitinib and canakinumab (JIA),
burosumab (XLH), teduglutide, denosumab, nintedanib, sitagliptin, metformin,
liraglutide, topiramate/levetiracetam, atorvastatin, atomoxetine, pimecrolimus,
tezacaftor/ivacaftor, and the achondroplasia agents (vosoritide, recifercept,
navepegritide, infigratinib-class).

### 2.3 Human genetics

- **GIANT height GWAS summary statistics** — Yengo 2022 all-ancestry and European
  (1.37 M SNPs each), plus Wood 2014. The atlas had GWAS *nodes* and no GWAS *data*.
- **Human Phenotype Ontology** full annotation release (`genes_to_phenotype`,
  `phenotype_to_genes`, `phenotype.hpoa`, `hp.obo`).
  Derived: **180 human genes in which variation is annotated to cause TALL STATURE**
  (`query/acquisition/hpo_tall_genes.csv`), 1,483 for short stature, 74 in both.

### 2.4 Full text

- **773+ open-access full texts** harvested from Europe PMC (download still completing),
  keyed to the ten atlas unknowns.
- Read in full this round: **chu2025** (PNAS, open access) — see §4.
- Preprint PDFs: Avijgan 2025 (human resting-zone spatial transcriptomics),
  Herpelinck 2022 (integrated limb skeleton atlas).
- **To et al. 2024**, multi-omic atlas of human embryonic skeletal development —
  full text read, data availability extracted: **ArrayExpress E-MTAB-14385**, 194 files,
  324 samples, all *Homo sapiens*, **5.7–13 post-conception weeks**, knee/hip/shoulder/
  calvaria/skull base, snRNA + scATAC + Visium + ISS. Sample metadata downloaded.

---

## 3. The finding that came out of the acquisition, not the analysis

Cross-referencing §2.3 against §2.1 exposes a hole that is not in any paper:

> **Public human growth plate data covers 5.7–13 post-conception weeks (To 2024) and
> 11–15 years (Chu, GSE288028, GSE18338). Between birth and the pubertal spurt there is
> essentially nothing.**

The atlas has been reasoning about a fifteen-year process from two snapshots at its ends,
and the interval it cannot see is the interval in which most of adult height is laid down.
The one dataset that spans it — **Byers 2000**, quantitative histomorphometry of the human
growth plate from birth to adolescence, 46 costochondral autopsy specimens aged 11 days to
13.5 years — is paywalled and not in PMC. It is item 1 on the want list.

---

## 4. Read in full: chu2025, and what it changes

`chu2025` (PNAS, PMID 41289405, open access) was already in the bibliography flagged
`has_full_text` but had never actually been read. Reading it produced a mechanism the
atlas did not hold, now recorded as node
`atlas/nodes/L2_stem_and_progenitor_biology/stem_pool_population_asymmetry.yaml`
(grade **C**, mouse only, human evidence **absent**):

**Growth plate stem cells renew by POPULATION ASYMMETRY, not invariant asymmetry.**
Labelling all Col2a1+ cells in Col2-CreERT2;R26R-Confetti and chasing a month gives the
population-asymmetry signature — clone *number* falls while clone *size* rises.

This matters more than it sounds. Under invariant asymmetry the stem pool size is a
constant of the tissue and the only levers on height are velocity and duration — which is
exactly where all 241 velocity nodes live and exactly where everything tops out at 2–4%.
Under population asymmetry **the size of the pool is a set-point**, determined by the
ratio of self-renewing to lineage-restricted divisions, and that ratio is demonstrably
movable — because growth hormone moves it. GH reduces label-retaining cells in the resting
zone (n=4/group, P<0.001), reduces PTHrP+ cell number, and raises clone size in every zone
*including the resting zone*; GHR deletion in PTHrP+ cells impairs clone formation, so the
shift is cell-autonomous.

**Nobody has tried to move that ratio the other way.** That is now gap
`g_l2stem_renewal_fraction_lever` — an absence in the experimental record, not a negative
result, and the most direct restatement of the question this atlas exists to answer.

Two caveats recorded rather than smoothed: bone length did **not** differ in the GHR
knockouts (tibia 18.3±0.2 vs 17.9±0.3 mm, P=0.31; femur 13.2±0.2 vs 12.8±0.3, P=0.35),
attributed by the authors to low recombination — so the cellular phenotype is present and
the organ-level phenotype is absent in the same animals. And serum IGF-1 **fell** during
pharmacological GH, which the classical hepatic-IGF-1 model does not predict.

---

## 5. A test that was run and came back null

**Hypothesis:** if the resting zone is the rate-limiting compartment, human tall-stature
genes should concentrate there.

**Test:** the 180 HPO tall-stature genes against per-zone detection rates in human
pubertal growth plate (chu2026's deposited GSE288028, already reduced by this atlas),
donor-column rank-standardised, against a 2,000-draw background matched on overall
detection rank so that "expressed at all" cannot masquerade as "zone specific".

**Guards, declared before the answer was seen:** COL10A1 maximal in hypertrophic;
COL2A1 >50% in every zone; MKI67 higher in proliferative than hypertrophic. On the first
run the MKI67 guard **fired and the analysis refused to report** — correctly, though the
fault was a display bug of mine (8 donor-columns zipped against 4 zone names, silently
truncating). After the fix all three controls pass cleanly: COL10A1 21.1% hypertrophic vs
~5.5% elsewhere; COL2A1 >96% everywhere; MKI67 15.0% proliferative vs 0.4/1.0/0.7.

**Result — the hypothesis is not supported.**

| gene set | stem | proliferative | prehypertrophic | hypertrophic |
|---|---|---|---|---|
| tall only (n=97) | 0.686 (p=0.11) | 0.677 | 0.673 | 0.680 |
| short only (n=1,275) | 0.681 | **0.693 (p=0.0005)** | 0.680 | 0.681 |
| tall **and** short (n=69) | **0.721 (p=0.001)** | 0.706 | 0.682 | 0.697 |

Tall-stature genes show **no zone enrichment anywhere**. The better-powered short-stature
set enriches in the **proliferative** zone, not the resting zone. The only stem-zone
signal is from the 69 genes that can cause *either* tall or short stature depending on the
variant — which is suggestive (a gene whose dose pushes height either way sits at a control
point) but is one of twelve tests and survives Bonferroni only barely.

This is recorded as it came out. It is evidence *against* the framing that motivated the
sweep, and the sweep is not being re-run with a different gene set to improve it.

Caveats that limit it in both directions: 97 genes is little power; zone assignment is a
marker-score approximation, not Chu's clustering; two donors; and every donor was operated
on *to prevent tall stature*, so the tissue is selected on the phenotype being tested.

---

## 6. WANT LIST — what I could not get, ranked

Everything below was located and confirmed to exist; the barrier is access, not existence.

### Tier 1 — would change conclusions

1. **Byers S, Moore AJ, Byard RW, Fazzalari NL. Quantitative histomorphometric analysis
   of the human growth plate from birth to adolescence.** *Bone* 2000. **PMID 11033444.**
   The only quantitative description of the human growth plate across the age interval the
   atlas cannot see (§3). Not open access, not in PMC.
2. **Kember NF, Sissons HA. Quantitative histology of the human growth plate.**
   *J Bone Joint Surg Br* 1976. **PMID 1018028.** The original human cell-kinetic
   measurements — cell numbers, column counts, turnover. Every human kinetic parameter in
   the atlas ultimately traces here.
3. **Avijgan M et al. Human growth plates house resting zone sub-populations with features
   of quiescent stem cells.** *Bone Research* 2026, **doi 10.1038/s41413-026-00564-y**,
   PMID 42552306. Visium spatial transcriptomics on growth plate biopsies from 12–14-year-olds
   at epiphysiodesis for tall stature — quiescent human resting-zone cells, directly the
   weakest-evidenced area of the atlas. *The 2025 preprint PDF is on disk; the published
   version and its data accession are not.* **Wanted: the published paper and its GEO/EGA
   accession.**
4. **Chu NTL et al.** *Sci Transl Med* 2026, PMID 41984930 (the paper behind GSE288028,
   whose data the atlas has used since Phase 5) — full text never obtained.
5. **KIGS (83,803 children, 52 countries, 322,576 patient-years, closed 2012) and NCGS
   (65,205 children, ~220,000 GH-treatment years, closed 2010) individual-level data.**
   Route: **Vivli** and **CSDR** — these require a named researcher, an institutional
   affiliation and a written analysis proposal, which I cannot supply. The question they
   answer: does GH show diminishing returns and earlier fusion consistent with spending the
   stem pool (§4)? This is the largest existing human dataset bearing on it.

### Tier 2 — would fill a specific hole

6. **Roach HI et al. Temporal analysis of rat growth plates: cessation of growth with age
   despite presence of a physis.** *J Histochem Cytochem* 2003. **PMID 12588965.** Growth
   ceases while the physis persists — the cleanest dissociation of "plate present" from
   "plate working", in a species that is not mouse.
7. **Kember NF cell-kinetics series**, none open access: PMID 8219479 (1993, *Cell kinetics
   and the control of bone growth*), 2267417 (1990, avian comparative), 3502931 (1987).
8. **Lineage tracing in a growth plate that CLOSES.** Does not exist in any species. Every
   clonal number in this atlas — including §4 — comes from mouse, whose plate never closes.
   This is a request for an experiment, not a document.
9. **Paediatric sacubitril/valsartan growth data.** 6 paediatric sacubitril trials found;
   none posts a stature outcome. `hakata2024` shows sacubitril causes dose-dependent
   skeletal overgrowth in normal mice. Those children are measured at every clinic visit.
10. **Human growth plate tissue itself, at any age between 1 and 10 years.** Routes
    identified but not usable by me: HDBR (MRC/Wellcome, 3–20 weeks — *embryonic only, does
    not cover the gap*); paediatric autopsy collections; epiphysiodesis and limb-lengthening
    surgical waste. Byers 2000's specimens were costochondral junctions from 46 children at
    autopsy in Adelaide.

### Tier 3 — cheap, and I simply have not done them yet

11. Extract effect sizes from the **269-trial unexamined set** (§2.2). The data is on disk.
12. Analyse **GSE18338** — the within-subject human pubertal growth plate series (§2.1).
13. Analyse **GSE16981 / GSE114919** — the rat temporal senescence datasets.
14. Test **height GWAS signal against zonal expression** now that both are on disk — the
    human, higher-resolution version of the Renthal 2021 round-cell-layer analysis
    (PMID 34346115).

---

## 7. Honest accounting of this round

- One hypothesis of mine was tested and **not supported** (§5), and is recorded as such.
- One guard **fired correctly** and stopped a report; the fault was mine and is documented.
- One bibliography entry was flagged `has_full_text` and had never been read; reading it
  produced the round's main mechanistic result (§4). The provenance audit predicted exactly
  this class of defect — 1,006 refs flagged, 19 actually read — and this is the twentieth.
- Nothing in §2 has been interpreted beyond its metadata. The 1.7 GB of expression data is
  *acquired*, not *analysed*, and the report says so.
