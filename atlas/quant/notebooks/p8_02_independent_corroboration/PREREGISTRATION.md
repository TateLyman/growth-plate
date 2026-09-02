# Preregistration — P8-02

**Do the four P8-01 negatives survive independent human donors and independent
platforms?**

Phase 8 round two (FINAL-01 items E and F). Written and committed **before** any target
gene was looked up in any of the three new datasets. §7 lists exactly what was inspected
first.

---

## 1. Why this, and not the Phase 6c ranking

FINAL-01 item E says to select round-two targets by the Phase 6c uncertainty ranking:
which never-measured parameters dominating flow-model uncertainty are answerable from
data that already exists?

**Checked, and the honest answer is none of them.** The five parameters carrying 98 % of
the flow model's output uncertainty are:

| rank | parameter | share | answerable from an expression dataset? |
|---|---|---:|---|
| 1 | terminal hypertrophic cell **height** (µm) | 45 % | **No** — morphometry |
| 2 | human proliferative **cell cycle time** | 40 % | **No** — kinetic labelling |
| 3 | **cells per column** | 6 % | **No** — morphometry |
| 4 | in-vivo **physeal stress** | 4 % | **No** — mechanics in a living human |
| 5 | zonal **stiffness** ratio | 3 % | **No** — micro-mechanical testing |

Every one is a measurement on tissue, not on RNA. **No re-analysis of any deposited
dataset can produce a cell height in micrometres.** That is not a failure of the search;
it is what `docs/experimental_agenda.md` already says — the dominant uncertainties need
new tissue measurements, and re-analysis cannot reach them. Recording it here closes
item E's first question rather than leaving it implied.

So round two targets the next-most-valuable thing re-analysis *can* do: **test whether
the four negatives P8-01 produced are real, or artefacts of one platform and two
donors.** That is item F, and it is the single largest threat to the most useful output
of round one.

## 2. The claims under test

P8-01 produced four both-donor non-detections in human growth plate at 11–13 y, on
Affymetrix HG-U133 Plus 2.0, in two donors:

| # | claim | why it matters |
|---|---|---|
| **N1** | **NPPC (CNP) is not detectable** while NPR2 and NPR3 are | the ligand of the pathway vosoritide amplifies |
| **N2** | **no cGMP-hydrolysing phosphodiesterase is detectable** (PDE5A on 8 probe sets, PDE1 on 14); the detected set is cAMP-preferring | PDE5-inhibitor reasoning does not transfer to the physis |
| **N3** | **CYP19A1 and ESR2 are not detectable** while ESR1 is | estrogen acts at the human physis via ERα on circulating hormone, with no local aromatase |
| **N4** | **SLC16A2 (MCT8), SLC16A10 and SLCO1C1 are not detectable** while THRA, THRB, DIO2 and SLC7A5 are | the human chondrocyte is unlikely to depend on MCT8 |

**These are detection-level claims across both donors, and they are therefore robust to
the donor-2 zonal dissection failure** — that failure degrades zonal *contrast*, not
detection, and donor 2's arrays are the more sensitive of the two (87 % of all one-donor
calls genome-wide are donor 2's). This is stated here so a reader does not discount all
four on the n = 1-for-zones concern, which applies to §4 of P8-01 RESULTS and not to §0.

What they are *not* robust to is **one platform**. A probe set can fail for reasons that
have nothing to do with the transcript: bad probe design, a 3′ bias from T7
amplification, a transcript isoform the 2003 array does not represent. That is what this
round tests.

## 3. The independent evidence, fixed in advance

Three human growth-plate expression series, **no donor and no platform shared with
GSE9160**:

| series | platform | growth-plate samples | donors | note |
|---|---|---:|---|---|
| **GSE22855** | Illumina HumanWG-6 v3 (GPL6884) | 2 (`L1142`, `L1234`) | independent | growth plate used as normal control against enchondroma |
| **GSE32398** | Affymetrix (GPL9828) | 5 | independent, prepubertal | growth plate vs articular cartilage |
| **GSE18338** | Agilent (GPL9324) | 6 | **one girl**, tibia, pre → early → late puberty | within-subject pubertal series |

**13 growth-plate arrays, 3 platform families, at least 8 donors, none of them the two in
GSE9160.** All are whole-plate bulk, which is exactly right here: the claims under test
are presence/absence, and bulk tissue is the *more* sensitive test of presence because no
zone is diluted away by microdissection of a different one.

GSE18338's six arrays come from a single subject and are therefore **one donor, not
six**; it is treated as n = 1 throughout and is used only as a third platform, never as
independent replication on its own.

## 4. Analysis plan, fixed in advance

### 4.1 Detection rule — the same empirical null as P8-01

For each array: the background is the intensity distribution of probes annotated to
**intact olfactory receptor genes**, which are not expressed in cartilage.

> **DETECTED in an array** ⇔ intensity > the 95th percentile of that array's OR null.
> **DETECTED in a dataset** ⇔ detected in a **majority** of that dataset's growth-plate
> arrays.

This rule passed a preregistered positive control in P8-01, reproducing the original
submitters' own present-calls (10,063 / 12,193 and 17,639 / 18,454) without seeing them.

**Platform fallback, declared now.** If a platform carries fewer than 20 usable OR probes,
the OR null is not estimable and that dataset is dropped for that reason and reported as
dropped — **not** silently replaced with a percentile-of-array threshold, which would
make presence/absence a function of an arbitrary cut.

### 4.2 Positive-control gate — a dataset must earn the right to testify

A dataset is used **only if** `COL2A1` **and** `ACAN` are DETECTED in its growth-plate
samples. A human growth-plate array in which the two most abundant cartilage transcripts
do not clear background is not measuring growth plate, and any negative it produces is
uninterpretable. Datasets failing the gate are reported as failing it and excluded.

Secondary controls reported but not gating: `COL10A1`, `SOX9`, `IHH`.

### 4.3 Internal positive controls inside each claim

Each negative travels with genes P8-01 found **positive**, on the same arrays:

| claim | must be NOT detected | must be DETECTED (internal control) |
|---|---|---|
| N1 | NPPC | NPR2, NPR3 |
| N2 | PDE1A/1B/1C, PDE2A, PDE3A/3B, PDE5A, PDE9A, PDE10A, PDE11A | PDE4A, PDE4B, PDE4C |
| N3 | CYP19A1, ESR2 | ESR1 |
| N4 | SLC16A2, SLC16A10, SLCO1C1 | THRA, THRB, DIO2, SLC7A5 |

If the internal controls fail in a dataset, that dataset says nothing about that claim,
and the result is `INCONCLUSIVE` rather than corroboration.

### 4.4 Verdicts, fixed in advance

Per gene per dataset: `DETECTED` / `NOT_DETECTED` / `NO_PROBE`.

Per claim, across the datasets that pass §4.2:

- **CORROBORATED** — `NOT_DETECTED` in **every** dataset that has a probe for it and
  whose internal controls hold, with at least one such dataset.
- **REFUTED** — `DETECTED` in **any** qualifying dataset. One good detection beats any
  number of non-detections, because absence is the weaker claim.
- **PARTIALLY CORROBORATED** — mixed across datasets. Reported gene by gene; **not
  resolved by majority vote**, because a platform difference is a mechanistic hypothesis
  about probe design, not noise to average away.
- **INCONCLUSIVE** — no probe anywhere, or no dataset passes the gates.

### 4.5 What a refutation would mean, stated before it can happen

If NPPC is detected in independent human growth plate, then **P8-01's headline negative
is a probe artefact of a single Affymetrix probe set (221348_at)**, the corresponding
node claim must be withdrawn, and the gap re-opened. That outcome is reported with the
same prominence as corroboration, and this sentence exists so that promise is on the
record before the numbers are.

### 4.6 No new statistics

Same as P8-01: **no p-values.** Detection is a threshold call against an empirical null;
agreement across independent datasets and platforms is the evidence, not a test
statistic. No dataset's samples are pooled with another's.

## 5. Grade consequences, fixed in advance

Per the Phase 8 constraint — grade your own analysis as you would grade a stranger's.

- A **CORROBORATED** negative moves from **D** to **C**: replicated across independent
  donors and independent platforms, still transcript-only, still human, still no
  functional test. It does **not** reach B — a B requires human genetic or interventional
  support, and a non-detection in bulk tissue is neither.
- A **REFUTED** negative is **withdrawn**, the node claim deleted, and the reversal
  recorded in `audit/corrections.md` with the same trace discipline as CORR-004.
- **PARTIALLY CORROBORATED** stays at **D** with the disagreement recorded as a
  contradiction entry naming the platforms.
- Everything carries `reanalysis: p8_02_independent_corroboration`.

## 6. What this design cannot do

1. **Transcript, not protein.** Unchanged from round one. A protein present from a
   transcript below detection is not excluded by any number of arrays.
2. **Bulk, not zonal.** These datasets cannot say *where* anything is. They can only test
   presence, which is what the four claims assert.
3. **Small numbers.** 2 + 5 + 1 donors. Independence across platforms is the strength
   here, not sample size.
4. **Different ages and sites.** GSE32398 is prepubertal; GSE18338 is a pubertal series
   in one girl's tibia; GSE22855's growth-plate controls come from an enchondroma study.
   A transcript absent at 11–13 y in distal femur and present at 6 y in another bone
   would show up as disagreement, and would be a real biological finding rather than a
   platform artefact — the analysis cannot distinguish the two and will say so.
5. **Enchondroma-study controls.** GSE22855's growth-plate samples are controls in a
   tumour study. They are normal tissue by the submitters' description; nothing here
   verifies that independently.

## 7. What was inspected before this file was written

- The Phase 6c sensitivity ranking, to establish that none of the top five parameters is
  answerable from expression data (§1).
- `atlas/quant/dataset_inventory.csv`, filtered to human, to find candidate datasets.
- For the three chosen series: the **series matrix headers only** — platform id, sample
  titles, source names, and characteristics — to confirm which arrays are growth plate
  and that the donors do not overlap GSE9160.
- The HTTP retrievability of the three series matrices.

**No expression value from any of the three datasets was read.** No target gene from §3
was looked up in any of them.

---

*Committed before execution. Script: `analysis.py`. Result: `RESULTS.md`, `results/*.csv`.*
