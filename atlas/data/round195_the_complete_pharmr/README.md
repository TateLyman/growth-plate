# Round 195 — the complete NDA 21-318 package, the randomised paediatric trial, and the source data

## Legibility

6-up is fine. Two of the five bundles carried intact text layers and needed no OCR at all
(`02_PTH_REGULATORY_AND_GROWTH_PAPERS`, `03_CHU_AND_SOURCE_DATA` — 435 kB and 118 kB of clean
text). The three FORTEO review bundles are scans; OCRed quadrant-wise at 300 dpi
(`ocr6.py`, 2 cols × 3 rows), which recovers prose reliably. Numeric tables still have to be
read off page renders — two are archived here as PNGs.

## What was in the bundles

| bundle | contents |
|---|---|
| `01_FORTEO_NDA_21318_COMPLETE_PHARMR_6up` | NDA 21-318 Pharmacology Review Parts 1–4, 240 original pages: second carcinogenicity study, the 1995/1997 IND reviews, the monkey study X95-11, the rabbit studies, the 1-year bone quality study R00796/R04296, the FIRST carcinogenicity study, ECAC minutes |
| `FORTEO_Pharmr_P2_condensed`, `..._P4_condensed` | overlapping condensed Parts 2 and 4 (rabbit studies; reproductive toxicology) |
| `02_PTH_REGULATORY_AND_GROWTH_PAPERS` | Tymlos NDA 208743 review complete (181 pp), **Vahle 2004**, **Winer 2010 JCEM RCT**, **Winer 2018 J Pediatr**, **Kindblom 2002** |
| `03_CHU_AND_SOURCE_DATA` | Chu 2026 full paper, Chu source figure media 3 and 4, **Hallett 2021 Fig 4c Source Data 1** |

## The findings

**The sex split.** Every femoral-length increase in the whole package is female and travels with
a body-weight increase. Every intact-male arm is null — 18 d at 4 wk of age (16, 80 µg/kg/d),
140 d (to 100 µg/kg/d), and 1 year from 18–20 wk (8, 40 µg/kg/d, n=20–30/group). The 26-week
study carries the contrast inside one protocol: females +2/+3/+4 % femur length with body
weight +7/+10/+10 %, weight gain ×1.4–1.8 and food efficiency ×1.4–1.7; males *"change not
seen"*, body weight −3.8 %, food efficiency ×0.7.

**The regulator contradicts `vahle2002`.** *"All effects were dose-dependent … except for the
effect on femur length in males which was maximal at the low dose."* And the FDA's own reading
of the whole-femur result — length +6 %, width +33 %, wet weight +60 % — is *"indicating effect
of LY mainly on periosteal expansion."*

**The human comparison is randomised and null.** `winer2010`: 12 children, 8 male, 3 years,
twice-daily PTH(1-34) vs twice-daily calcitriol. Height percentile 47 ± 13 vs 53 ± 15, P = 0.76,
no difference across time. `winer2018`: same cohort to 10 years, height velocity Z normal
throughout.

**The rabbit request closes negatively.** CG3-06 (mature ovary-intact NZW, 140 d) and CG3-13
(9-month-old NZW, 35/70 d) — neither measured bone length.

**Hallett Fig 4c source data** gives the label-dilution curve per replicate. Biphasic: λ = 0.546/wk
(wk 0–5, R² 0.993) and λ = 0.1225/wk (wk 5–12, R² 0.942). Mouse resting-zone cycle time ≥ **57 d**
as a lower bound (loss = division + efflux).

## Figures archived

| file | what it shows |
|---|---|
| `hallett2021_fig4c_source_data_workbook.png` | the per-replicate label-dilution table, weeks 0–12 |
| `winer2018_fig1_height_velocity_z.png` | HT Vel-Z boxplots by study year — medians near zero, and the only panel of six without a p-value against reference |

## Tools run

- `atlas/tools/pth1r_complete_length_ledger.py` → `complete_length_ledger_output.txt`
  All fourteen length observations with method, sex, dose, duration and the concurrent
  body-weight effect attached to each.
- `atlas/tools/pth1r_length_versus_bodyweight_allometry.py` → `allometry_output.txt`
  Tests the female gains against isometric scaling (Δlength/length ≈ ⅓ · Δmass/mass).
  26-week study: predicted +2.3/+3.3/+3.3 %, observed +2.0/+3.0/+4.0 %. **No residual.**
  2-year study: predicted +3.5 %, observed +6 % by caliper — and that is the arm with +33 %
  width.
- `atlas/tools/hallett2021_label_dilution_fit.py` → `hallett_dilution_output.txt`
  Transcription reproduces the workbook's own means exactly before fitting.

## Corrections

**CORR-191** — the round-194 interim positives are female-only and sit inside the body-weight
confound. The age-gate retirement survives (that comparison is internal to one sex); reading
them as a plate effect available to a male does not. Also records the regulator/paper conflict
on `vahle2002` dose-dependence.

## Conflict flagged, not resolved

Mouse resting-zone T_stem ≥ 57 d against `hunziker1994`'s 6 d in intact rats — tenfold.
Round 183's *ratios* survive (common scale error cancels); its absolute amplification figure of
23–32 cells per progenitor does not, and is now `value_unverified`.
