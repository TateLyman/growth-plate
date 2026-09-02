# P8-01 results — re-analysis of GSE9160

**Read `PREREGISTRATION.md` first.** Every rule applied here was fixed before any gene
of interest was looked up. Departures from the plan, and everything added after seeing
data, are marked **POST HOC** in place.

Reproduce with:

```
python3 analysis.py --fetch      # pulls GSE9160 + GPL570 from GEO, ~80 MB, not vendored
python3 analysis.py              # results/zonal_profiles.csv, gene_summary.csv, background_control.json
python3 posthoc_method_controls.py
python3 donor_separation.py
```

**Reproducibility checked, not assumed.** `_data/` was deleted and the whole chain
re-run from a cold fetch of the live GEO records. Every committed file in `results/`
came back byte-identical, including the background control (10,063 / 17,639).

---

## 0. The headline, before the detail

Two results matter more than the gene-by-gene table, and one of them is about the
dataset rather than about biology.

1. **The only public zone-resolved human growth-plate transcriptome is, for zonal
   purposes, effectively n = 1.** Donor 1's laser capture separated the zones; donor
   2's largely did not. COL10A1 — a transcript that defines the hypertrophic zone —
   sits at **0.6 % of its hypertrophic-zone level in donor 1's resting zone, and at
   15–36 % in donor 2's.** Genome-wide, 9.6 % of donor 1's detected probe sets vary
   more than five-fold across the zonal axis against **1.0 %** of donor 2's. Any zonal
   claim drawn from this series that pools the two donors is diluted by a factor that
   nobody has previously reported, because the deposit has no accompanying publication
   (§6).

2. **CNP transcript (NPPC) is not detectable in human growth-plate tissue at 11–13
   years, in either donor, while its receptor NPR2 and its clearance receptor NPR3
   both are.** NPPC runs at 4–20 arbitrary units against per-array detection
   thresholds of 254–826 — one to two orders of magnitude below background. This is
   the ligand of the pathway that vosoritide is designed to amplify.

Everything below is grade **D** or lower by the preregistered ceiling: one dataset,
two donors, one platform, one analyst.

---

## 1. The background rule passed its preregistered control

| | authors' present-calls | this analysis (median across that donor's 5 arrays) | ratio |
|---|---:|---:|---:|
| donor 1 (F, 11 y 10 m) | 12,193 | 10,063 | 0.83 |
| donor 2 (M, 13 y 3 m) | 18,454 | 17,639 | 0.96 |

The olfactory-receptor empirical null (128 probe sets, 95th percentile per array)
reproduces both the magnitude and the direction of the donor asymmetry in the original
submitters' own MAS5 present-calls, without ever seeing them. **Verdict: PASS.** The
threshold is used for the rest of the analysis.

Per-array detection thresholds, which every number below should be read against:

| donor | RZ | PZ | PHZ | HZ | PC |
|---|---:|---:|---:|---:|---:|
| 1 | 789 | 746 | 646 | 720 | 826 |
| 2 | 330 | 254 | 348 | 330 | 451 |

**Donor 2's arrays are roughly twice as sensitive.** That single fact governs how the
`one_donor_only` category must be read — see §3.

## 2. POST HOC — the method controls, and what they exposed

`PREREGISTRATION.md` preregistered a positive control for the *background rule* but
not for the *zonal profile method*. That was an oversight in the plan. Eight canonical
markers were therefore run afterwards, declared as post hoc, and used only to test the
method — nothing from them enters the graph.

| gene | expected peak | donor 1 peak | donor 2 peak | fold range d1 / d2 |
|---|---|---|---|---|
| COL10A1 | HZ | **HZ** | **HZ** | 169 / 5.3 |
| COL2A1 | all cartilage | detected everywhere | detected everywhere | 1.5 / 1.5 |
| MMP13 | HZ | PHZ *(adjacent)* | **HZ** | 5.7 / 1.3 |
| IBSP | HZ | **HZ** | PZ | 5157 / 1.2 |
| SPP1 | HZ | **HZ** | PZ | 29.8 / 1.1 |
| COL1A1 | PC | RZ | PHZ | 2.0 / 1.5 |
| SP7 | PC | HZ | HZ | 9.4 / 1.6 |
| MKI67 | — | PZ | PHZ | 3.5 / 2.3 |

Two of these "failures" are mine, not the data's:

- **SP7 (osterix)** peaks in HZ in *both* donors, concordantly. Osterix is expressed in
  hypertrophic chondrocytes as well as in osteoblasts, so "expect perichondrium" was a
  wrong expectation. The method recovered a real and concordant localisation.
- **COL1A1** is high everywhere (30,000–80,000 units in every compartment of both
  donors). That is not a zonal profile failure; it says COL1A1 signal pervades these
  laser-captured cartilage samples, which is a caveat about LCM purity worth carrying.

The remaining pattern is not mine. **Donor 1 recovers the expected compartment for
COL10A1, IBSP, SPP1, and MMP13-adjacent; donor 2 recovers it for COL10A1 and MMP13
only, and its fold ranges collapse toward 1.1–1.6.**

## 3. POST HOC — the dataset has one usable dissection, not two

Quantified genome-wide rather than from markers (`donor_separation.py`):

| | donor 1 | donor 2 |
|---|---:|---:|
| probe sets detected in all four zones | 5,161 | 13,792 |
| median zonal fold range | 2.32 | 1.66 |
| 90th percentile | 4.91 | 2.64 |
| 99th percentile | **12.26** | **4.99** |
| fraction varying > 5× across zones | **9.6 %** | **1.0 %** |
| fraction varying > 10× | 1.7 % | 0.1 % |

And the direct bleed-through read-out — COL10A1 measured in the **resting**-zone sample,
as a percentage of the same donor's hypertrophic zone:

| probe set | donor 1 | donor 2 |
|---|---:|---:|
| 205941_s_at | **0.6 %** | **35.8 %** |
| 217428_s_at | **0.6 %** | **15.1 %** |

A hypertrophic-zone-defining transcript at a third of its hypertrophic level in the
resting-zone sample is cross-contamination, not biology. Donor 2's compartments are
substantially mixed.

### Three consequences, stated rather than quietly absorbed

1. **The preregistered concordance rule is now known to be biased.** Requiring both
   donors to place the maximum in the same or an adjacent zone penalises genes for
   donor 2's dissection. It is **not relaxed retroactively** — every table below
   reports the preregistered verdict. Where donor 1 alone gives a clean profile, that
   is reported as a labelled donor-1 observation and graded no higher.
2. **Detection is unaffected, and the asymmetry runs the useful way.** Donor 2's
   arrays are the more sensitive. Of the 352 one-donor compartment calls in the locked
   gene list, **304 (86.4 %) come from donor 2**; genome-wide the figure is **87.1 %**.
   So `one_donor_only` means "seen only by the more sensitive array" — i.e. *low but
   plausibly present* — and **`not_detected` in both donors is a genuinely strong
   negative**, because it survived both the more sensitive array and the cleaner
   dissection.
3. **Zonal claims from this series in the literature inherit the dilution.** No
   accusation is intended and none is made: the deposit carries no publication, so
   nobody has had the chance to report this.

## 4. Group A — the seven gaps tagged against this dataset

Detection verdicts are the preregistered both-donors rule. `1-donor` means detected by
donor 2's more sensitive arrays only, and should be read as low-but-plausible.

### 4.1 `g_l3core_006` — which phosphodiesterase carries cGMP tone in the human plate?

**Result: none of the cGMP-hydrolysing phosphodiesterases is detected across the zonal
axis in both donors. The detected phosphodiesterases are predominantly
cAMP-preferring.**

| detected in both donors | compartments | not detected in either |
|---|---|---|
| **PDE4A** | RZ, PZ, PHZ, HZ, PC | PDE1A (7 probe sets), PDE1B, PDE1C (6), **PDE5A (8 probe sets)**, PDE9A, PDE10A, PDE11A, PDE3B, PDE7B, PDE8B |
| **PDE4B** | RZ, PZ, PHZ, HZ | |
| **PDE4C** | RZ, PZ, PHZ, HZ, PC | |
| **PDE4D** | HZ | |
| **PDE7A** | HZ, PC | |
| **PDE8A** | PZ, PHZ, PC | |
| PDE2A | RZ, PC | |
| PDE3A | PC | |

**PDE5A is represented by eight probe sets on this platform and not one of them clears
background in either donor.** PDE1 is represented by fourteen and likewise. The
cGMP-degrading capacity of the human growth plate is therefore not carried by the
isoforms that dominate the pharmacological literature, or is carried below this
platform's sensitivity.

**Disposition: `answered_by_reanalysis`** for the negative half — which cGMP-PDEs are
*not* detectable — and the gap is rewritten rather than closed, because "which isoform
carries the dominant hydrolysing activity" is an enzymatic-activity question that
transcript data cannot answer. PDE2A (cGMP-stimulated, RZ) is the one candidate the
data leaves standing, in one zone, and that is a testable lead rather than an answer.

### 4.2 `g_l4endo_003` — is the glucocorticoid receptor zonally graded in humans?

**Result: yes, modestly, and toward the hypertrophic zone. NR3C1 is detected in all
five compartments of both donors (4 of 5 probe sets) and peaks in HZ in both donors
independently** — fold range 2.9 (donor 1) and 4.2 (donor 2), one of the very few
genes where donor 2 shows the *larger* range.

- **NR3C2** (mineralocorticoid receptor): not detected. Glucocorticoid action on the
  human physis is unlikely to run through MR.
- **HSD11B1 / HSD11B2**: neither detected. No evidence of local pre-receptor cortisol
  interconversion in this tissue at this age — which means the growth plate is exposed
  to whatever the circulation delivers, with no local gate.

**Disposition: `answered_by_reanalysis`** for the zonal-distribution half. The second
half of the question — what fraction of receptor is ligand-occupied at physiological
versus therapeutic cortisol — is an occupancy measurement and remains open. The gap is
rewritten to that residue.

### 4.3 `g_l4endo_009` — do the IGF binding proteins form a zonal gradient?

**Result: five of seven IGFBPs are present, and the strongest and most concordant
signal in the whole IGF module is not an IGFBP at all — it is STC2.**

| gene | detected | donor 1 peak | donor 2 peak | notes |
|---|---|---|---|---|
| **STC2** | PZ, PHZ, HZ | **HZ** | **HZ** | fold 23.3 / 12.5 — concordant, and large in *both* donors |
| PAPPA2 | PHZ, HZ, PC | PHZ | PHZ | concordant |
| IGFBP3 | RZ, PHZ, HZ, PC | HZ | RZ | discordant |
| IGFBP4 | RZ, HZ, PC | RZ | HZ | discordant |
| IGFBP5 | RZ, HZ, PC | RZ | PZ | 3 of 6 probe sets |
| IGFBP6 | RZ, PC | RZ | PZ | |
| IGFBP7 | RZ, HZ, PC | RZ | RZ | concordant |
| IGFBP1, IGFBP2 | not detected | | | |
| **IGF1** | **1-donor only, every compartment** | | | see below |
| IGF2 | all five compartments | PHZ | PZ | robust, 202409_at only |

Two things worth carrying:

- **STC2, an inhibitor of PAPP-A, is strongly hypertrophic-zone-enriched in both
  donors** while PAPPA2 peaks prehypertrophically. Read together these say local IGF
  bioavailability is being *restrained* precisely where hypertrophy occurs. That is a
  coherent, concordant, testable reading and it is the single cleanest new mechanistic
  observation in this notebook.
- **IGF1 transcript is detected only by donor 2's more sensitive arrays, in every
  compartment, and by donor 1 in none.** Under the preregistered rule that is
  `one_donor_only` and not a detection. Given §3.2 it should be read as *present at
  low abundance*, not absent — and either way it is far below IGF2, which is robustly
  detected across all five compartments. **In this tissue at this age, IGF2 is the
  abundant local IGF and IGF1 is not.**

**Disposition: `answered_by_reanalysis`.** A zonal gradient exists; it is a gradient of
IGF *restraint* (STC2/PAPPA2) more clearly than of the binding proteins themselves.

### 4.4 `g_l3rest_007` — are SOST and DKK1 in cartilage, or only in bone?

**DKK1: yes, in cartilage.** Detected in PZ, PHZ and HZ in both donors. In donor 1 —
the clean dissection — it rises 30-fold from resting to hypertrophic zone (376 → 11,530).

**SOST: the most extreme donor disagreement in the dataset, and it is not resolvable
here.** Donor 1: 45, 8, 24, 48 across the four zones — nothing, against a threshold of
~700. Donor 2: 6,618, 7,105, 11,320, 4,274 — enormous, against a threshold of ~300, and
then only **151 in donor 2's perichondrium**. So in one donor SOST is absent from
cartilage; in the other it is abundant in cartilage and absent from the perichondrium,
which is the *opposite* of the bone-derived expectation.

This is a ~100-fold discrepancy between two donors on a single probe set. It cannot be
explained by donor 2's sensitivity advantage (about 2×) or by its dissection quality
(which would blur, not create, signal). It is either real biological variation between
an 11-year-old girl and a 13-year-old boy, a sample-specific artefact, or bone
contamination of donor 2's cartilage samples — and this dataset cannot distinguish
them.

**Disposition: `answered_by_reanalysis` for DKK1; `attempted_inconclusive` for SOST,**
with the discrepancy recorded as the reason and as a specific, cheap experiment worth
doing (SOST in situ or qPCR across zones in more than two donors).

Also: SFRP1 (RZ), SFRP2 (PC), SFRP4 (RZ, HZ), FRZB/SFRP3 (RZ, PZ, PC) and LRP6 detected;
LRP5, DKK2 and WIF1 not detected.

### 4.5 `g_l3rest_009` — where is Notch active across human zones?

**Result: the Notch machinery is present, broadly, and the resting zone is where donor
1 puts almost all of it — but donor 2 disagrees on nearly every member, and §3 explains
why that disagreement is uninformative.**

Detected in both donors: NOTCH1, NOTCH2, NOTCH3, JAG1, JAG2, DLL1, HES1, HEY1, HEY2,
RBPJ, PSEN1. Not detected: NOTCH4, DLL3, DLL4, HES5.

NOTCH2, RBPJ, PSEN1, JAG2 and HEY2 are detected in all five compartments of both
donors — the pathway is not zonally restricted at the level of its components. Donor 1
places the maximum in RZ for NOTCH1, NOTCH2, NOTCH3, JAG1, JAG2, HES1, HEY1 and PSEN1
(NOTCH3 at a 110-fold range); donor 2 places it variously, with fold ranges of
1.15–2.3, i.e. essentially flat.

**Disposition: `partially_informed`.** Component presence is established. Where the
pathway is *active* requires target-gene readout in tissue that can resolve zones, and
one donor's profile is not that. The gap stays open with the component list added and
the specific residue named.

### 4.6 `g_l6mech_007` — is PIEZO1 or PIEZO2 in the human physis?

**PIEZO1: yes, in all five compartments of both donors**, and robustly — probe set
202771_at runs 8,986–24,442 in donor 1 and 8,572–16,411 in donor 2, an order of
magnitude above threshold everywhere.

**PIEZO2: no.** Six probe sets, none detected in both donors in any compartment.

**TRPV4: yes**, in PZ, PHZ and HZ, PZ-max in both donors.

**Disposition: `partially_informed`, not answered.** The gap asks about **protein**.
Transcript cannot close it. What has changed is that the protein question is now
sharply pointed: PIEZO1 and TRPV4 are worth staining for in human growth plate; PIEZO2
is not, on this evidence.

### 4.7 `g_l11path_023` — does the human chondrocyte use MCT8 for T3 uptake?

**Result: the thyroid hormone machinery is present but the canonical transporter is
not. This is the cleanest positive finding in the notebook.**

| gene | role | detected in both donors |
|---|---|---|
| **THRA** | receptor α | **all five compartments** |
| **THRB** | receptor β | **all five compartments**, HZ-max in both donors |
| **DIO2** | T4 → T3 activation | RZ, PZ, PC |
| **SLC7A5** (LAT1) | system-L amino acid transporter | **RZ, PZ, PHZ, HZ — all four zones, both donors** |
| **SLC7A8** (LAT2) | system-L | RZ, PZ, PC |
| **SLC16A2** (MCT8) | canonical TH transporter | **not detected** (1-donor, PZ only) |
| SLC16A10 (MCT10) | | not detected (3 probe sets) |
| SLCO1C1 (OATP1C1) | | not detected (2 probe sets) |
| DIO1, DIO3 | | not detected |

So: receptors present, local T4→T3 activation present, **and the transporter whose loss
causes Allan–Herndon–Dudley syndrome is not detectable while the system-L transporters
are.** The gap asked exactly this question and the answer the data gives is that the
human growth plate chondrocyte is unlikely to depend on MCT8.

**Disposition: `answered_by_reanalysis`.** With the standing caveat that a transporter
can be functionally decisive at transcript levels below this platform's floor, so this
is evidence against dependence, not proof of independence.

## 5. Group B — paralog attribution asked of human tissue

The audit question (MR-004 item 5) is whether the alternative to an attributed
mechanism is even present in the relevant human zone. Per PREREGISTRATION §3.5,
**no statement below compares the abundance of one gene against another** — each is a
presence call against that array's own background.

| pair | result | what it does to the attribution |
|---|---|---|
| **PRKG1 vs PRKG2** (CORR-003) | **both detected.** PRKG2 in PHZ and HZ only. PRKG1 (cGKI) in **RZ, PHZ, HZ and perichondrium** — including the resting zone, where PRKG2 is not detected. | The alternative is live in human tissue, and is detected in a zone where the attributed effector is not. CORR-003's suspicion survives contact with human data. |
| **ANKH vs ENPP1** (CORR-001) | **both detected**, ENPP1 in all five compartments of both donors, ANKH in RZ, PZ, PHZ, PC. ALPL detected PHZ/HZ (canonical). PHOSPHO1, ENPP3 not detected. | The confound is not a mouse-only artefact. ENPP1 is co-present with ANKH throughout the human plate. |
| **IGF1R vs INSR** | **both detected in all five compartments of both donors.** IRS1 and IRS2 also detected. | An experiment using insulin in human cartilage cannot be read as an IGF1R experiment. The receptor it would act on is there. |
| **FGFR1/2/3/4** | **all four detected.** FGFR3 very high (204379_s_at: 5,910 → 54,361 across donor 1's zones). FGFR1 in all five compartments. FGFR2 in PZ, HZ. FGFR4 in all four zones. | FGFR3-attributed effects have three co-present paralogs in human tissue. Selectivity data is required for any inhibitor claim. |
| ligands | **FGF2 and FGF18 not detected; FGF9 detected in perichondrium only.** | The FGFR3 ligand is not detectable inside the cartilage. |
| **NPR1/2/3** | NPR2 detected (PZ/PHZ/HZ, PHZ-max in donor 1 — canonical); NPR3 detected in HZ, 27× and 10× fold range; NPR1 detected in RZ. **NPPC and NPPB not detected in either donor.** | See §0. Receptor and clearance receptor present, ligand not detectable. |
| **ESR1 / ESR2 / GPER1** | **ESR1 detected** (RZ, PZ, PHZ, PC; PZ-max in both donors). **ESR2 not detected** (6 probe sets). GPER1 PHZ only. **CYP19A1 (aromatase) not detected** (7 probe sets). AR detected (RZ, PHZ, PC). | Estrogen action on the human physis runs through ERα, on circulating estrogen — there is no detectable local aromatase to make it. |
| **PTH1R / PTH2R** | PTH1R detected in all five compartments; **PTH2R not detected**; **PTHLH (PTHrP) not detected in either donor, any probe set, any compartment**. IHH textbook (229358_at: 203 → 20,856 RZ → HZ in donor 1, 461 → 16,564 in donor 2). | PTH1R attribution is clean of PTH2R. The PTHrP result is discussed below. |
| **SOX5 / SOX6 / SOX9** | all three detected. SOX9 in all five compartments both donors. | No absence-based discrimination available. |

### The PTHrP negative, and why it is a caveat about the dissection rather than a finding

PTHLH is not detected on any of three probe sets in either donor. Taken at face value
that contradicts the canonical PTHrP–IHH loop — but IHH in the *same samples* is
textbook-perfect in both donors, so the assay is working.

The resolution is almost certainly anatomical. PTHrP in the growth plate is produced by
the periarticular/resting-zone border and the perichondrial groove, not uniformly by
the compartment this study labelled "reserve". A laser capture of reserve-zone
chondrocytes can miss the PTHrP source entirely while capturing everything it signals
to. **This is recorded as a limit on what "reserve zone" means in this dataset**, and
it is a caveat that applies to every other resting-zone claim above, including the
Notch and SFRP1 results.

## 6. The deposit has no publication

A Europe PMC search for the submitters (Mougey EB, Olney RC, Soteropoulos P) in
connection with this work returns no paper describing GSE9160. Three later papers cite
the accession as a reused resource. The GEO record's own design statement is the only
methods description that exists: distal femoral growth plate, left or right, Leica
AS-LMD laser microdissection of cryostat sections, T7 linear amplification.

Consequences carried forward:

- The dissection quality problem in §3 was never peer reviewed because there was
  nothing to review.
- **T7 linear amplification** introduces 3′ bias; probe sets targeting 5′ regions are
  systematically disadvantaged, which is one plausible contributor to probe-set
  disagreement within a gene (e.g. PRKG1 detected on 1 of 3 probe sets, ESR1 on 1 of 9).
- **PREREGISTRATION §5.3 was wrong** and is corrected here: the anatomical site *is*
  specified — distal femur. Site-specific reasoning is therefore available, but only
  for distal femur.

## 7. What entered the graph, and at what grade

Per PREREGISTRATION §8, everything is capped at **D** and tagged
`reanalysis: p8_01_gse9160_human_zonal` so it can be found and reversed as one set.
`human_evidence: direct`, `species_basis: human`.

Nothing in §5 that compares two genes' abundance entered the graph at all — those
comparisons were not made, by rule.

| gap | disposition |
|---|---|
| `g_l3core_006` | `answered_by_reanalysis` (negative half), rewritten to the activity question |
| `g_l4endo_003` | `answered_by_reanalysis` (distribution), rewritten to the occupancy question |
| `g_l4endo_009` | `answered_by_reanalysis` |
| `g_l3rest_007` | `answered_by_reanalysis` (DKK1) + `attempted_inconclusive` (SOST) |
| `g_l3rest_009` | `partially_informed` |
| `g_l6mech_007` | `partially_informed` — protein question, transcript answer |
| `g_l11path_023` | `answered_by_reanalysis` |

Four negatives are recorded as findings in their own right, because under §3.2 a
both-donor non-detection is the strongest thing this design produces:

1. **NPPC (CNP) not detectable** while NPR2 and NPR3 are.
2. **No cGMP-hydrolysing PDE detectable across the zonal axis** — PDE5A on 8 probe
   sets, PDE1 on 14.
3. **CYP19A1 (aromatase) and ESR2 not detectable** while ESR1 is.
4. **SLC16A2 (MCT8) not detectable** while THRA, THRB, DIO2, SLC7A5 are.

## 8. What this notebook did not do

- No CEL-level reprocessing, so no MAS5 detection p-values and no probe-level
  background correction. The empirical null in §1 is a substitute, validated against
  the submitters' own calls but not identical to them.
- No statistical test of any kind, by design (PREREGISTRATION §3.4).
- **No repair of the concordance rule.** It is biased, §3 says so and quantifies it,
  and it was left in place because changing a preregistered criterion after seeing
  which genes it rejects is how a preregistration stops meaning anything.
- No claim about protein for any gene.
- No extension of the locked gene list. The only genes run outside it are the eight
  post-hoc method controls in §2 and the five bleed-through markers in §3, none of
  which enter the graph.
