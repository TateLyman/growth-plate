# P8-02 results — three of the four negatives do not survive

**Read `PREREGISTRATION.md` first.** §4.5 of that file promised, before any number was
seen, that a refutation would be reported with the same prominence as corroboration.
This is that report, and it is mostly a refutation of my own round-one headline.

```
python3 analysis.py --fetch      # GEO series + platform tables, live, not vendored
python3 analysis.py              # results/detection_by_dataset.csv, verdicts.json
python3 posthoc_stringency.py    # POST HOC sensitivity - see §4
```

---

## 0. The result in one table

| claim (P8-01) | verdict | consequence |
|---|---|---|
| **N1 — NPPC (CNP) is not detectable in human growth plate** | **REFUTED** | withdrawn |
| **N2 — no cGMP-hydrolysing PDE is detectable** | **REFUTED as a blanket claim** | rewritten gene by gene |
| **N3 — no local aromatase (CYP19A1) and no ERβ (ESR2)** | **CORROBORATED** | **D → C** |
| **N4 — MCT8 (SLC16A2) is not detectable** | **REFUTED** | withdrawn, gap re-opened |

**One of four survives.** The one that survives is now much stronger than it was: four
datasets, four platform families, roughly ten donors, with a working internal control.

## 1. All three datasets passed their gates

`PREREGISTRATION` §4.2 required COL2A1 and ACAN to be detected before a dataset could
testify. They are not merely detected — they are at the ceiling of every array:

| gene | GSE22855 (Illumina) | GSE32398 (Affymetrix GPL9828) | GSE18338 (Agilent) |
|---|---:|---:|---:|
| COL2A1 | **100.0** | **100.0** | **100.0** |
| ACAN | 91.3 | 99.9 | 99.9 |
| COL10A1 | 99.8 | 99.9 | 99.9 |
| SOX9 | 98.1 | 98.7 | 96.8 |

*(percentile of the gene's best probe within its own array, median across that dataset's
growth-plate arrays)*

These are unambiguously human growth-plate cartilage arrays. Whatever else is uncertain,
the tissue is not.

## 2. N1 — NPPC: refuted, and the reason is a single probe set

| | GPL570 (P8-01) | GSE22855 | GSE32398 | GSE18338 |
|---|---|---|---|---|
| probe sets | **1** | 2 | 2 | 2 |
| verdict | not detected | not detected | **DETECTED** | **DETECTED** |
| percentile in array | **bottom few %** (4–20 units against thresholds of 254–826) | 59.9 | **69.8** | **67.8** |
| survives p99 and above-median? | — | no | **yes, both** | **yes, both** |

NPPC sits at roughly the **70th percentile** of two independent human growth-plate arrays
on two different platforms, and it survives every stringency tested (§4). On GPL570 the
same transcript reads at the very bottom of the array.

That gap cannot be explained by a threshold choice. It is a **probe-level discrepancy**:
Affymetrix HG-U133 Plus 2.0 carries exactly one NPPC probe set (`221348_at`) and it does
not report the transcript.

**P8-01's headline negative is withdrawn.** CNP transcript *is* detectable in human
growth-plate tissue. The atlas claim built on it is removed and the gap it appeared to
close is re-opened — see `audit/corrections.md` **CORR-005**.

## 3. N4 — MCT8: refuted the same way

| | GPL570 (P8-01) | GSE22855 | GSE32398 | GSE18338 |
|---|---|---|---|---|
| SLC16A2 probe sets | **1** | 1 | 1 | 1 |
| verdict | not detected | **DETECTED** | **DETECTED** | **DETECTED** |
| percentile | bottom | 74.8 | 63.1 | 59.9 |

SLC16A10 is likewise detected in all three (81.8 / 47.9 / 69.2). SLCO1C1 is detected in
two of three and is left `PARTIALLY_CORROBORATED`.

**The claim that the human growth-plate chondrocyte is unlikely to depend on MCT8 is
withdrawn.** MCT8 transcript is present. The system-L transporters are still present too
— SLC7A5 is at the 78–95th percentile everywhere — so the *alternative* stands; what
falls is the argument from MCT8's absence.

### The generalisable lesson, and it should have been in the P8-01 preregistration

| claim | probe sets behind the P8-01 negative | outcome |
|---|---:|---|
| N1 NPPC | **1** | refuted |
| N4 SLC16A2 | **1** | refuted |
| N3 CYP19A1 + ESR2 | **13** (7 + 6) | corroborated |

**A single-probe non-detection is not a negative.** It is one oligonucleotide failing,
which is indistinguishable from a transcript being absent until a second platform is
asked. P8-01 stated the probe counts honestly in every table — 8 probe sets for PDE5A,
14 for PDE1, 6 for PIEZO2 — and then treated a 1-probe non-detection as the same kind of
object as a 13-probe one. That was the error, and it was in the design, not in the
execution.

## 4. POST HOC — how much of this depends on the threshold

`PREREGISTRATION` §4.1 reused P8-01's OR-null rule on three new platforms. On GPL570
that rule had a preregistered positive control. **On these three it has none.** The
consequence is visible immediately:

| dataset | fraction of the array clearing its own p95 threshold |
|---|---:|
| GSE9160 (GPL570, P8-01) | **18–32 %** |
| GSE22855 (GPL6884) | 38 % |
| GSE32398 (GPL9828) | 45 % |
| GSE18338 (GPL9324) | **58 %** |

On an array where 58 % of probes clear the bar, a `DETECTED` call is weak on its own. So
every verdict was re-run at three stringencies (`posthoc_stringency.py`), and each gene's
value is reported as a **percentile within its own array**, which is comparable across
platforms in a way an absolute threshold is not.

**The two refutations survive all three stringencies.** NPPC and SLC16A2 are called
detected at p95, p99 and above-median in the datasets that detect them. **The
corroboration also survives**: CYP19A1 (20–43rd percentile) and ESR2 (22–39th) are called
absent at every stringency in every dataset, while their internal control ESR1 is called
present at every stringency in every dataset.

Four genes are flagged as **detected only at the loosest threshold** and their calls are
correspondingly weak: PDE4A (GSE32398), SLC16A10 (GSE32398), SLCO1C1 (GSE18338), THRA
(GSE32398 and GSE18338). None of them changes a claim-level verdict.

**The preregistered verdicts stand as written.** Nothing was re-scored at a stringency
chosen after seeing which answer it gave.

## 5. N2 — the phosphodiesterase claim was too broad, and the truth is more interesting

The blanket statement *"no cGMP-hydrolysing phosphodiesterase is detectable"* is false.
Gene by gene, with the median percentile in each dataset:

| gene | GSE22855 | GSE32398 | GSE18338 | verdict |
|---|---:|---:|---:|---|
| **PDE3B** | 73.0 ✓ | 53.5 ✓ | 51.3 ✓ | **REFUTED** — detected in all three |
| **PDE5A** | **91.2** ✓ | 28.4 | 37.2 | partially — strong on one platform, absent on two |
| PDE2A | 77.9 ✓ | 45.5 | 72.9 ✓ | partially |
| PDE9A | 87.4 ✓ | 24.4 | 55.5 ✓ | partially |
| PDE1A | 75.3 ✓ | 10.2 | 12.4 | partially |
| PDE1B | 69.6 ✓ | 38.8 | 39.1 | partially |
| PDE1C | 33.2 | 12.7 | 12.8 | **CORROBORATED** |
| PDE3A | 61.4 | 22.0 | 12.8 | **CORROBORATED** |
| PDE10A | 48.0 | 12.7 | 8.7 | **CORROBORATED** |
| PDE11A | 42.5 | 23.7 | 24.3 | **CORROBORATED** |

Two things worth carrying:

- **PDE3B is detected in every dataset examined**, which matters because the paralog
  audit independently flagged `pde3b` as AT_RISK: the entire cGMP → K⁺ channel → TRPM7 →
  bone-elongation result rests on PDE3-**family** agents (cilostazol, milrinone) that
  cannot separate PDE3A from PDE3B. The transcript evidence now says PDE3B is present in
  human growth plate while **PDE3A is corroborated absent in all four datasets** —
  which points the family-selective pharmacology at PDE3B, not at PDE3A, and inverts the
  reading recorded on that node from the P8-01 data.
- **PDE5A is the sharpest platform disagreement in the study**: 91st percentile on
  Illumina, 28th and 37th on the other two, absent on GPL570 across 8 probe sets. That is
  a contradiction, not an average, and it is recorded as one.

## 6. What each dataset says about the internal controls, including where they disagree

The controls are not uniformly well-behaved, and pretending otherwise would misrepresent
how much these platforms agree:

- **NPR3 is not detected in any of the three** (43 / 29 / 14th percentile), although
  P8-01 detected it robustly in GSE9160's hypertrophic zone. A zonally-restricted
  transcript can be diluted below detection in whole-plate bulk — which is the mirror
  image of the bulk-is-more-sensitive argument in `PREREGISTRATION` §3, and shows that
  argument has a limit.
- **THRB is at the 6th percentile in GSE22855** and the 87–90th in the other two.
- **PDE4C is at the 99th percentile in GSE22855** and the 40th in GSE18338.

**Cross-platform agreement on detection in this tissue is mediocre.** That is itself a
finding about the reusability of human growth-plate expression data, and it bounds what
any of these datasets — including GSE9160 — can establish about absence.

## 7. What entered the graph

Per `PREREGISTRATION` §5, and traced in `audit/corrections.md` as **CORR-005**.

| object | change |
|---|---|
| `cnp_protein` | NPPC non-detection observation **withdrawn**; replaced with the refutation and the probe-set explanation |
| `mct8_transporter` | MCT8 non-detection **withdrawn**; the system-L alternative survives on its own evidence, not on MCT8's absence |
| `g_l11path_023` | **re-opened**; the P8-01 disposition `answered_by_reanalysis` is reversed |
| `aromatase_cyp19a1`, `estrogen_receptor_beta` | **D → C** — corroborated across four platforms with a working internal control |
| `pde5a`, `pde_isoform_inventory` | blanket claim replaced with the gene-by-gene table; PDE5A platform disagreement recorded as a contradiction |
| `pde3b` | P8-01's reading corrected: PDE3B is present in human growth plate, PDE3A is corroborated absent |
| `g_l3core_006` | disposition downgraded from `answered_by_reanalysis` to `partially_informed` |

## 8. What this round cannot do

- **Still transcript, still not protein.** Nothing here says CNP peptide is made in the
  human growth plate; it says the message is detectable.
- **Bulk cannot see zones**, and §6 shows bulk can also *lose* a zonally restricted
  transcript (NPR3). Presence and absence in bulk are not symmetric claims.
- **No platform here has a validated positive control for its detection rule.** §4 is a
  sensitivity analysis, not a validation. The right fix is a platform with published
  present-calls to check against, and none of these three has one.
- **Different ages and sites.** GSE32398 is prepubertal; GSE18338 is one girl's tibia
  through puberty; GSE22855's growth plates are controls in a tumour study. A transcript
  genuinely present at one age or site and absent at another would appear here as
  platform disagreement, and this design cannot separate the two.
