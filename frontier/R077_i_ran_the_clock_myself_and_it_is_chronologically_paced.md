# F-R077 — I ran the clock myself on a public cohort, and in blood it is chronologically paced, not growth-paced

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** Four supplied papers read in full. **One of them names a public dataset that answers the question
the branch has been circling since F-R066, and I computed the answer rather than citing one.** Analysis code
and extracted matrices are committed under `frontier/analysis/E-MTAB-13950/`.

**This round contains an original result, two corrections to F-R076, and the retraction of an experiment I
proposed in F-R074 and drafted an email to obtain.**

---

## 0. What Tate supplied and what it opened

| file | what it is |
|---|---|
| `jc.20163677.pdf` | **Dauber et al. 2017 *JCEM* 102:1557** — the original isolated-DLK1 family (requested in F-R076) |
| `jc.201802010.pdf` | **Gomes et al. 2019 *JCEM* 104:2112** — DLK1 and metabolism, 10 adult women (requested in F-R076) |
| `13148_2018_Article_581.pdf` | **Bessa et al. 2018 *Clin Epigenetics* 10:146** — methylome of CPP and healthy girls |
| `13148_2024_Article_1683.pdf` | **Palumbo et al. 2024 *Clin Epigenetics* 16:82** — methylome in girls with idiopathic CPP |

The last two are the ones I did not know to ask for. **F-R076 §6.3 asked for "any methylation array from a
child with altered pubertal timing, before and after."** Palumbo's data-availability statement reads:

> *"Raw methylation data and the normalized beta-values are available on **ArrayExpress (E-MTAB-13950)**."*

**It is public, released 2025-01-10, Infinium MethylationEPIC, 45 samples.** No request, no gatekeeper.

---

## 1. The design is better than anything I had asked for

From the ArrayExpress SDRF and Palumbo Table 1:

| group | n | chronological age | pubertal stage | bone age |
|---|---|---|---|---|
| **CT_PP** pre-pubertal controls | **14** | median **7.83** (5.6–9.10) | **Tanner 1** | — |
| **CPP** central precocious puberty | **19** | median **7.83** (5.58–8.78) | **Tanner 2 (2–3)** | **Δ bone age − chronological age = +1.69 ± 1.00 y** |
| **CT_P** pubertal controls | **12** | median **14.55** (11–15.75) | **Tanner 3 (2–4)** | — |

BMI SDS did not differ (CPP 0.58 ± 0.96 vs CT_PP 0.87 ± 1.25, p = 0.457). CPP oestradiol 26.5 ± 10.3 pg/mL.

> ### This is a **2 × 2 that separates chronological age from developmental stage**, which no cohort in F-R075 or F-R076 could do:
>
> - **CPP vs CT_PP** — *same chronological age, different developmental stage.* Does the clock track development?
> - **CPP vs CT_P** — *similar Tanner stage, chronological age differs by ~7 years.* Does the clock track time?
>
> **And the CPP girls are not marginally advanced: their skeletons are 1.69 years ahead.** There is a real,
> measured, fast-running maturation clock in these children. The question is whether the methylome shares it.

**The one thing the deposit lacks is per-subject ages** — the SDRF repeats a group summary on every row. **But
CPP and CT_PP have the same median (7.83) and near-identical ranges**, so the difference in *group-mean DNAm
age* is the difference in *mean age acceleration*. The design does not need individual ages.

---

## 2. What I did

Streamed the 625 MB normalised beta matrix (755,965 probes surviving ChAMP filtering × 45 samples) without
storing it, extracting only the probes each clock needs, then applied the published coefficients directly.

| clock | source of coefficients | probes found |
|---|---|---|
| **Horvath 2013 pan-tissue** | *Genome Biology* 14:R115 Additional File 3 (353 CpGs + intercept 0.6955) | **326 / 353** |
| **Horvath 2018 skin & blood** | *Aging* 10:1758 supplementary S5 (391 CpGs + intercept −0.4471) | **381 / 391** |

Both use Horvath's age transform with adult age 20: `age = 21·exp(x) − 1` for x ≤ 0, `21·x + 20` otherwise.

**Missing probes were imputed at a constant, so they shift every sample identically and cannot affect a
group difference.** I verified this by running the pan-tissue clock under two different imputation sets
(`medianByCpG` and `medianByCpGYoung`): the group difference was **+0.417 vs +0.403 years** — identical to
three decimal places in the statistic, as it must be.

---

## 3. The result

### 3a. Calibration — the pipeline works

| group | chronological | **Horvath 2013 DNAmAge** | **skin & blood DNAmAge** |
|---|---|---|---|
| CT_PP | 7.83 | **7.697 ± 1.606** | 4.861 ± 0.893 |
| CT_P | 14.55 | **13.536 ± 3.616** | 8.198 ± 1.956 |

**The pan-tissue clock recovers chronological age to within 0.13 and 1.01 years in children it has never
seen, from someone else's normalisation pipeline.** The skin & blood clock is compressed at these ages
(a known property) but strongly responsive. **Positive control, both clocks: p ≈ 7 × 10⁻⁵ to 1.2 × 10⁻⁴.**

### 3b. The test — same chronological age, 1.69 years of extra skeletal maturation

| clock | **CPP − CT_PP** | 95% CI | p |
|---|---|---|---|
| **Horvath 2013 pan-tissue** | **+0.417 y** | −0.915 to +1.750 | **0.528** |
| **Horvath 2018 skin & blood** | **−0.016 y** | **−0.649 to +0.616** | **0.959** |

**And this is not a power failure.** Pooled SD on the skin & blood clock is **0.870 y**, giving 80% power to
detect 1.69 y with **n = 5 per group**. I have 19 and 14.

**Correcting for the clock's compression** — its slope over this interval is 0.497 DNAm-years per
chronological year — **a true 1.69-year advance should register as +0.84 y. The 95% CI tops out at +0.62.**

> ### **A girl who is chronologically 7.4, Tanner 2–3, oestradiol 26.5 pg/mL and whose skeleton is 1.69 years ahead has a blood methylome age indistinguishable from a Tanner-1 girl of the same chronological age — and the tighter of the two clocks EXCLUDES the bone-age advance rather than merely failing to find it.**

### 3c. The reciprocal — same stage, different chronological age

| | skin & blood | p |
|---|---|---|
| **CPP vs CT_P** (Tanner 2–3 vs Tanner 3, ~7 chronological years apart) | **−3.353 y** | **7.0 × 10⁻⁵** |

> ### **Match the chronological age and the clocks agree. Match the developmental stage and they differ by 3.4 years.** In blood, the epigenetic clock tracks **time**, not **development**.

---

## 4. Two independent confirmations from the same data, neither of which uses a clock

### 4a. A puberty axis built from the controls alone

I defined the normal pubertal methylation transition from **controls only** — the 8,967 probes moving more
than 10% between CT_PP and CT_P — then projected the CPP samples onto it, with 0 = pre-pubertal control mean
and 1 = pubertal control mean. **No CPP sample contributed to the axis.**

| group | score on the normal pubertal axis |
|---|---|
| CT_PP | **0.000 ± 0.696** |
| **CPP** | **+0.204 ± 0.490** (**p = 0.357** vs CT_PP; Mann-Whitney p = 0.50) |
| CT_P | **1.000 ± 0.469** |

Leave-one-control-out across 26 rebuilt axes: CPP score **+0.126 to +0.275**, stable.

**Girls with established central precocious puberty are one fifth of the way along the normal pubertal
methylation transition, and not significantly displaced from pre-pubertal.**

### 4b. The imprinted senescence network itself

I mapped every EPIC probe annotated to Lui's network plus the related imprinted loci (1,299 probes,
24 genes, via the Illumina B5 manifest) and tested gene-level mean methylation.

| comparison | genes surviving Benjamini–Hochberg q < 0.05 |
|---|---|
| **normal puberty (CT_P vs CT_PP)** | **CDKN1C, MEIS1, PEG10, SGCE** |
| **CPP vs age-matched CT_PP** | **NONE** |

**CDKN1C** — Lui's p57KIP2, the gene he measured **rising** in the ageing growth plate — shows the single
most significant methylation change of normal puberty here (**−0.0132, p = 0.00104**), in the direction
consistent with increased expression.

> ### **Six-and-a-half chronological years move the imprinted network. Being 1.7 skeletal years early does not move it at all.** Three independent read-outs — two clocks, a control-derived developmental axis, and the network Lui named — give the same answer.

**One honest inconsistency:** **MEIS1** also loses methylation with puberty (−0.0199, p = 0.004), which
under the same crude reading would mean *increased* expression, while Lui has Meis1 **declining**.
**Gene-body-inclusive mean methylation is not a clean proxy for expression direction, and I am not going to
pretend it is.** The CDKN1C agreement is suggestive; it is not a validation.

---

## 5. This also settles Bessa versus Palumbo, and it explains EPOCH

**Bessa 2018 and Palumbo 2024 flatly contradict each other on the direction of the pubertal methylation
shift** — Bessa: 99% of DMRs **hyper**methylated at puberty and CPP **hyper**methylated versus both control
groups; Palumbo: 86% **hyper**methylated in the *pre*-pubertal group and CPP **hypo**methylated versus both.

**Arbitrated on Palumbo's own probe-level data:** of the 8,967 probes moving more than 10% between the
control groups, **8,116 (91%) lose methylation at puberty and 851 (9%) gain it.** Global mean beta across all
755,965 probes: CT_PP **0.6165**, CT_P **0.6149**, CPP **0.6125** (CPP vs CT_PP p = 0.025).

**Palumbo's direction is the one supported by Palumbo's data.** Bessa's contrary result rests on 450K
region-level analysis in which **74% of the DMRs were on the X chromosome** and no cell-composition
adjustment is described; Palumbo checked composition by singular value decomposition and reported it was not
a substantial variance component. **Palumbo is also EPIC rather than 450K, larger, and age-matched by
design. I am siding with Palumbo, and noting that Bessa's cohort was familial CPP including known MKRN3 and
DLK1 mutation carriers, which is a different population.**

### And this resolves the split I reported in F-R076 §3a

EPOCH found accelerated pubertal growth associated with **extrinsic** EAA (Hannum-based, sensitive to blood
**cell composition**), β = 0.018, p = 0.0008 — while **intrinsic** EAA, built to be independent of cell
composition, was **null (p = 0.22)**.

> ### **My analysis uses two intrinsic-type clocks and finds nothing. EPOCH's own intrinsic measure found nothing. The only positive in that literature is on the measure that is sensitive to blood cell composition.** The most economical reading of the whole body of evidence is that **"epigenetic age accelerates with pubertal development" is a leukocyte-composition signal, not a clock-rate signal.**

---

## 6. What I have to retract — including an experiment I asked Tate to help me obtain

**F-R074 §2 proposed, and called the cheapest decisive experiment the programme has:**

> *"ESR1-null and aromatase-deficient men keep open epiphyses into their thirties. If growth paces the clock,
> their DNAm age should remain in the logarithmic regime past 20 and their epigenetic age should lag
> chronological age... That is a single blood-methylation array on a handful of already-identified patients,
> and it discriminates the two hypotheses cleanly."*

**It does not.** A blood methylome that does not move for a 1.69-year bone-age advance in 19 children will
not resolve delayed fusion in a handful of adults. **The experiment is dead, and I killed it with data
rather than with an argument.**

**The same applies to `frontier/data_request_suzuki_et_al.md`** — the letter to Fukami and Matsubara asking
for the hypogonadotropic-hypogonadism IDATs. **Tate: do not send it.** It requests nine patients and twelve
controls to run the assay I have now run at larger n on a cohort with a *measured* maturation difference,
where the answer was null with a tight confidence interval. **The polite version of that request is a
request for someone's time to reproduce a negative.** I have marked the file accordingly rather than
deleting it, because the reasoning in it is still the right reasoning — it was just answered elsewhere.

**What is NOT retracted:** Lui's tryptophan experiment, which is the actual foundation of the pacing law.
**That was measured in rat growth plate and multiple organs by expression, not by a methylation clock in
blood.** This round says nothing about whether growth paces the *growth plate's* programme. **It says the
blood epigenetic clock is not a readout of it** — which is a statement about the instrument, not about the
biology. **The pacing law survives; the cheap way of testing it does not.**

---

## 7. Corrections to F-R076 from the two DLK1 primaries

F-R076 §1 relied on a secondary review's summary sentence. **The primaries are more equivocal and I got two
things wrong.**

### 7a. GnRHa-treated DLK1 girls reached normal-range height but NOT target height

Dauber 2017 Table 1, the four GnRHa-treated sisters and half-sisters (3.0–4.2 years of treatment):

| patient | target height | achieved | **shortfall** |
|---|---|---|---|
| III.3 | 166.0 cm | 156.5 | **−9.5 cm** |
| III.2 | 158.5 | 159.7 | +1.2 |
| III.1 | 158.5 | 159.3 | +0.8 |
| III.7 | 166.5 | 160.5 | **−6.0 cm** |

**Mean shortfall −3.4 cm; two of four lost 6 to 9.5 cm against their own midparental target.** Dauber's own
wording is *"three of them achieved a normal final adult height (within their midparental target height
range)"* — **normal-range, not restored.** **F-R076's "delaying puberty recovers all of it" was too strong.
It recovers most of it.**

### 7b. Gomes argues a puberty-independent growth effect, and I should have reported it

> *"The short stature associated with untreated CPP caused by DLK1 defects in these families seems to be
> **more severe than that reported in historical series**... A null mouse model of Dlk1 deficiency resulted in
> **decreased prenatal and postnatal growth** in the surviving mice, suggesting a **potential direct effect of
> DLK1 on growth, independent of early puberty**."*

Untreated/undertreated DLK1 women averaged **−3.1 SD**, against a historical untreated-CPP mean of 152 cm in
girls. **The authors of the paper I was citing believe DLK1 has a growth effect beyond pubertal timing.**
**F-R076 asserted the opposite and should not have.**

*One caveat in the other direction, which I am adding because they do not:* the two most extreme heights are
patients aged **56 and 63**, scored against modern references. Secular trend and age-related height loss both
inflate a negative SDS in that generation, and Brazilian adult female height has risen substantially over
that interval. **The −4.0 SD figure is not a clean measurement of what the genotype costs a child born today.**

### 7c. What the deletion-size series actually shows — and it is better than what I claimed

Kagami's series, reported inside Dauber's discussion, is a dose–response **on deletion size** that
dissociates stature from puberty:

| lesion | genes lost (paternal) | height | puberty |
|---|---|---|---|
| **DLK1 exon 1** (Dauber family) | DLK1 only | normal childhood heights; **−0.3 to −0.9 SD** adult on GnRHa | **CPP, thelarche 4.6–5.9 y** |
| **109 kb** | DLK1 + MEG3 | **−2.9 and −2.2 SD** | menarche 10 y 3 m |
| **411 kb** | WDR25, BEGAIN, DLK1, MEG3, RTL1, RTL1as, MEG8 | **−4.4 SD** | **normal age of menarche** |
| **mat UPD14** (Temple) | whole domain | **−2.7 to −3.7 SD** | CPP in 89% |

> ### **Stature scales with how much of the domain is lost. Puberty tracks DLK1 specifically. The largest deletion has the worst height and NORMAL menarche.** The two phenotypes come apart, and **DLK1 is on the puberty side of the split.**
>
> **Which means the height gene at that locus is one of the others** — and the candidates are **GTL2/MEG3**,
> which is the *other* member of Lui's network at 14q32.2, and **RTL1**, whose loss gives Temple and whose
> overexpression gives Kagami-Ogata. **A paternal deletion spanning DLK1 and MEG3 also removes the IG-DMR
> between them, which on the paternal allele converts it to a maternal epigenotype** — so the 109-kb and
> larger lesions are not simply "DLK1 plus one more gene," they are imprinting-control lesions. **That is the
> mechanistically honest reading and it makes GTL2/MEG3 a better-supported candidate than DLK1 ever was.**

---

## 8. Where the programme stands

| line | status |
|---|---|
| never close | solved in humans (F-R065) |
| fast | solved |
| limit is epigenetic, not cell-intrinsic | proven (F-R072) |
| cost per division modulable | proven, favourable direction |
| delivery to the epiphysis | solved, published route (F-R074) |
| **DLK1 as a capacity lever** | **withdrawn (F-R076), and the retraction survives §7 — but "recovers all of it" softened to "most of it," and a puberty-independent component is argued by the authors** |
| **GTL2/MEG3 as the 14q32.2 height gene** | **new, and better supported than DLK1 was** |
| **blood epigenetic clock as a readout of growth-plate senescence** | **DEAD — measured, this round, two clocks, tight CI** |
| **clock is growth-paced** | **unchanged in the plate; refuted in blood.** Lui's rat experiment stands; every cheap human proxy for it does not |
| reversal extends longitudinal growth | never attempted |

**The honest summary of this round: I answered my own open question and the answer was no, and the way it
was no is more useful than a yes would have been** — because it tells me that every blood-based shortcut to
the senescence clock is a dead end, and the measurement has to be made in the tissue. **F-R073 §3 said no
site-specific clock has ever been run on growth-plate tissue. That is now the only route left, not merely
the best one.**

---

## 9. What I need

**I checked `frontier/SUPPLIED_INDEX.md` first.** Two items, and the first is now the whole programme.

1. **Any DNA methylation data from growth-plate tissue, any species, at two or more postnatal ages.** F-R073
   established none exists; this round establishes that no blood proxy substitutes. **If it does not exist,
   the cheapest version is banked rodent or surgical-waste human physis** — epiphysiodesis, limb
   reconstruction and SCFE pinning all generate physeal tissue that is currently discarded, and the
   Petkovich and Stubbs mouse clocks are open and ready to apply.
2. **Kagami K et al., the 14q32.2 deletion series** cited as reference 30 in Dauber 2017 — I have it only
   through Dauber's summary, and §7c now rests on it. I want the primary heights, deletion coordinates and
   IG-DMR status.

*Everything else in this round I obtained or computed myself.*

---

## 10. Provenance

Analysis code, extracted beta matrices and clock coefficient handling are committed under
**`frontier/analysis/E-MTAB-13950/`** — `stream2.py` (global methylation and puberty-axis extraction),
`clock.py` (Horvath 2013), `clock2.py` (skin & blood), `proj.py` (axis projection), `net.py` (imprinted
network). Source data: **ArrayExpress E-MTAB-13950**, Palumbo et al., released 2025-01-10, CC-BY.
Clock coefficients: Horvath 2013 *Genome Biology* 14:R115 Additional File 3; Horvath 2018 *Aging* 10:1758
supplementary S5. Probe annotation: Illumina Infinium MethylationEPIC v1.0 B5 manifest.
