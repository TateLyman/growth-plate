# Preregistration — P8-01

**Re-analysis of GSE9160: zone-resolved transcriptome of the human growth plate**

Phase 8 (`primary_reanalysis`). This file was written and committed **before** any
gene of interest was looked up. What was inspected beforehand is listed in §6 so the
claim is auditable rather than asserted.

---

## 1. Why this dataset

`atlas/quant/dataset_inventory.csv` records GSE9160 as *the* highest-value re-analysis
target in the atlas, on this ground: it is the only publicly deposited **zone-resolved
transcriptome of a human growth plate**. Reserve, proliferative, prehypertrophic and
hypertrophic zones plus perichondrium were laser-capture microdissected separately from
each of two donors.

- Series: `GSE9160`, "Gene Expression Across the Human Growth Plate", GPL570
  (Affymetrix HG-U133 Plus 2.0), 54,675 probe sets.
- Samples: 10 = 5 compartments × 2 donors.
- Donor 1: Caucasian female, 11 y 10 m, long bone growth plate, morphology normal.
- Donor 2: Caucasian male, 13 y 3 m, same, morphology normal.
- Values used: the GEO series matrix (linear, MAS5-scale intensities as deposited).
  Raw CEL files exist (`GSE9160_RAW.tar`) but are not used — see §5.

Seven gaps in `atlas/gaps/gaps.yaml` were tagged in the dataset inventory as
potentially answerable from this series. Every one of them is a *localisation* or
*which-isoform* question, which is exactly the class Phase 8 says to prioritise, and
not a functional question, which this design cannot address.

## 2. The measurement question, stated before looking

For each gene in the locked list of §4:

- **Q1 (detection).** Is the transcript detectable above array background in human
  growth-plate tissue at 11–13 years, in each of the five compartments?
- **Q2 (zonal profile).** Does its abundance vary across the zonal axis
  RZ → PZ → PHZ → HZ, and in which direction?
- **Q3 (donor concordance).** Do the two donors — who differ in sex and in age by
  1 y 5 m — agree?

## 3. Analysis plan, fixed in advance

### 3.1 Background null and the detection rule

There are no MAS5 present/absent calls in the series matrix, and the AFFX spike-in
controls on these arrays cannot be used as a limit of detection: the poly-A controls
(`AFFX-r2-Bs-dap/lys/phe/thr`) run in the **inverse** of their nominal concentration
order, which means they were not spiked in, and the bacterial controls (BioB/BioC/
BioD/CreX) sit one to two orders of magnitude above the array median, which would
call essentially the whole transcriptome absent.

Instead the background is estimated **empirically, from the arrays themselves**:

> **Null set.** All probe sets whose GPL570 gene symbol matches an intact olfactory
> receptor gene (`OR\d+[A-Z]\d*[A-Z]?`) — 128 probe sets on this platform. Olfactory
> receptors are not expressed in cartilage; their intensity distribution on a given
> array is that array's non-specific hybridisation.
>
> **DETECTED in an array** ⇔ intensity > the 95th percentile of that array's OR null.
>
> **DETECTED in a compartment** ⇔ detected in **both** donors. One donor alone is
> recorded as `one_donor_only`, never as detected.

Direction of bias is stated in advance: a minority of olfactory receptors are
ectopically transcribed at low level in non-olfactory tissue, so this null is if
anything inflated, and the rule is therefore **conservative for presence** — it will
miss weakly expressed genes before it will invent expression. Non-detection under this
rule is bounded evidence of absence, not proof of it.

**Positive control on the rule, declared in advance:** the GEO record for this series
reports 12,193 and 18,454 probe sets present in patients 1 and 2 respectively, by the
original authors' own calls. If the OR-null rule is sound it should reproduce both the
magnitude and the donor asymmetry of those two numbers. If it does not, the rule is
abandoned and only §3.2 (which needs no threshold) is reported.

### 3.2 Zonal profile

For each probe set and **each donor separately**:

    rel(zone) = intensity(zone) / mean(intensity over that donor's 5 compartments)

Donors are **never averaged**. n = 2 is not a sample; averaging two donors would
manufacture a false central tendency and hide exactly the disagreement Q3 asks about.

- Zonal axis for ordering: RZ → PZ → PHZ → HZ. Perichondrium is a **separate
  compartment**, not a point on that axis, and is reported alongside rather than within
  the gradient.
- `fold_range` = max(rel) / min(rel) across the four zones, per donor.
- **Concordant** ⇔ the two donors place the maximum in the same zone, or in adjacent
  zones on the ordered axis. Anything else is `discordant`.

### 3.3 Multi-probe genes

Probe sets are reported **individually and never averaged**. Two probe sets for one
gene can target different 3′ regions or different isoforms, and disagreement between
them is information about isoform usage, not noise to be smoothed away.

### 3.4 No inferential statistics

**No p-values will be computed and none will be reported.** With one array per
compartment per donor there is no within-condition replicate, so any test statistic
would be an artefact of treating probe sets as replicates. This analysis is
**descriptive**. Concordance between two independent donors is the only replication
available and is reported as such.

### 3.5 Between-gene comparisons are graded lower, by rule

Comparing the intensity of probe set A against probe set B is **not quantitative** on
Affymetrix: different probe sets have different hybridisation efficiency, and a
two-fold difference between two genes' intensities is not a two-fold difference in
abundance. Therefore:

- **Within a probe set, across compartments** — valid. Any claim of this shape may
  enter the graph.
- **Between different probe sets** ("gene A is more abundant than gene B") — **not
  valid** as an abundance statement. Where such a comparison is reported at all it is
  labelled `cross_probe_comparison: true`, graded **E**, and phrased as *signal rank*,
  never as abundance.

This rule bites hardest on the paralog questions of §4 group B, which are exactly the
questions one wants to answer this way. It is stated in advance so that it cannot be
quietly relaxed once the numbers are in.

## 4. Locked gene list

Fixed before running. Genes added after seeing results would be recorded in RESULTS.md
as post hoc and graded separately; the intent is that none are.

### Group A — the seven gaps tagged in the dataset inventory

| gap | genes |
|---|---|
| `g_l3core_006` cGMP phosphodiesterases | PDE1A/1B/1C, PDE2A, PDE3A/3B, PDE4A/4B/4C/4D, PDE5A, PDE7A/7B, PDE8A/8B, PDE9A, PDE10A, PDE11A |
| `g_l4endo_003` glucocorticoid receptor | NR3C1, NR3C2, HSD11B1, HSD11B2 |
| `g_l4endo_009` IGF binding proteins | IGFBP1–7, IGF1, IGF2, IGF1R, IGF2R, PAPPA, PAPPA2, STC1, STC2 |
| `g_l3rest_007` WNT antagonists in cartilage | SOST, DKK1, DKK2, SFRP1–4, WIF1, LRP5, LRP6 |
| `g_l3rest_009` Notch across human zones | NOTCH1–4, JAG1, JAG2, DLL1, DLL3, DLL4, HES1, HES5, HEY1, HEY2, RBPJ, PSEN1 |
| `g_l6mech_007` PIEZO in human physis | PIEZO1, PIEZO2, TRPV4 |
| `g_l11path_023` thyroid hormone uptake | SLC16A2, SLC16A10, SLCO1C1, SLC7A5, SLC7A8, DIO1, DIO2, DIO3, THRA, THRB |

### Group B — paralog attribution (MR-004 item 5), asked of human tissue

Each of these is a case where the atlas records a mechanism attributed to a specific
molecule while a paralog was co-present and never excluded. The human zonal
transcriptome cannot settle attribution — only a selective perturbation can — but it
can establish whether the alternative is **present in the relevant human zone at all**,
which is the precondition for the alternative being live.

| pair | why it is on the list |
|---|---|
| **PRKG1 vs PRKG2** | CORR-003. PKG-II loss expands the plate while NPR2 loss shrinks it; cGKI was reported co-expressed at higher zonal enrichment in mouse and the double knockout has never been made. This is the human check. |
| **ANKH vs ENPP1** | CORR-001. ANKH exports ATP, not PPi; ENPP1 was present in the cells where PPi transport was inferred. Plus ALPL, ENPP2, ENPP3, PHOSPHO1. |
| **IGF1R vs INSR** | the one cartilage experiment coupling this family to mTORC1 used insulin, not IGF-1. |
| FGFR1/2/3/4 | + FGF2, FGF9, FGF18 |
| NPR1/2/3 | + NPPB, NPPC |
| ESR1 / ESR2 / GPER1 | + AR, CYP19A1 — L7 fusion is estrogen-driven in humans |
| PTH1R / PTH2R | + PTHLH, IHH, GLI1/2/3, PTCH1, SMO |
| SOX5 / SOX6 / SOX9 | the trio is treated as one unit throughout L3 |

## 5. What this design cannot do, stated before it produces anything

1. **n = 2.** Two donors, one female one male, 11 y 10 m and 13 y 3 m. Nothing here
   generalises to fetal, infant, or peripubertal-male-specific biology, and nothing
   here separates sex from age because the two donors differ in both.
2. **Transcript ≠ protein.** `g_l6mech_007` asks whether PIEZO1/2 *protein* is present.
   Transcript detection cannot close it; it can only make the protein question worth
   asking. Gaps of this shape are marked `partially_informed`, never `answered`.
3. **Anatomical site is "long bone" and is not further specified** in the GEO record.
   Site-specific behaviour (L1) cannot be addressed.
4. **LCM captures the compartment, not the cell type.** A perichondrial sample contains
   several cell types; a zone sample contains chondrocytes plus whatever matrix-adherent
   material survived microdissection.
5. **CEL files are not reprocessed.** The deposited series-matrix values are used as
   given. Re-normalising from raw would change absolute values; it would not change the
   within-probe-set zonal ratios that carry §3.2, which is the load-bearing analysis.
6. **The array is from 2003.** A gene absent from GPL570, or represented only by a
   poorly-annotated probe set, is invisible here and that is a property of the platform,
   not of the tissue.

## 6. What was inspected before this file was written

Full disclosure, so "preregistered" means something:

- the series matrix header (sample titles, donor characteristics, compartment labels);
- the value scale of the matrix (linear, median ≈ 140–290 per array);
- the AFFX control probe values, in order to reject them as a threshold — §3.1;
- the count of olfactory-receptor probe sets (128) and the number of probe sets above
  the OR-null p95 per array, in order to confirm the rule was computable at all.

**No gene from the §4 list was looked up.** No zonal profile of any target was computed.
The §3.1 positive control was specified before it was checked.

## 7. Disposition rules, fixed in advance

Each gap ends in exactly one of:

- **`answered_by_reanalysis`** — the result addresses the question as posed. Gap moved,
  notebook committed, new/updated node claim graded **D** (§8).
- **`partially_informed`** — the result constrains the question but cannot close it
  (e.g. a protein question answered at transcript level). Gap **stays open**, rewritten
  to state precisely what is now known and what remains.
- **`attempted_inconclusive`** — detection in one donor only, discordant profiles, or
  the gene is not on the platform. Recorded with the reason.

A negative result — a gene the atlas expects to be there and that is not detected —
is reported with the same prominence as a positive one, and is the single most
informative outcome this analysis can produce.

## 8. Grade ceiling

Per the Phase 8 constraint: *never let a re-analysis result enter the graph at a higher
grade than the data supports; grade your own analysis as you would grade anyone else's.*

- Any claim entering the graph from this notebook is capped at **D** — single dataset,
  n = 2, single platform, single analyst, no independent replication.
- `human_evidence: direct` is correct — the tissue is human.
- `species_basis: human`, `translation_risk: low` on the species axis, but the D grade
  carries the real uncertainty.
- Every such claim carries `reanalysis: p8_01_gse9160_human_zonal` so it can be found
  and reversed as one set.
- Cross-probe-set comparisons (§3.5) are capped at **E**.

---

*Committed before execution. The analysis script is `analysis.py`; the result is
`RESULTS.md` and `results/*.csv`.*
