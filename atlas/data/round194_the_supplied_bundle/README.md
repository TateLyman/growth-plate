# Round 194 — the supplied bundle

Three PDFs supplied by the user, plus what was pulled to close the questions they opened.

## Legibility of the 4-up compression

**Yes, all three are fully readable, and two of them did not even need OCR.**

- `01_PTH1R_primary_papers_4up.pdf` (9 sheets) — carries an intact text layer. Extracted
  losslessly to `01_primary.txt` (155 kB). No OCR involved, so nothing is at risk from
  the compression.
- `03_Hallett_resting_zone_4up.pdf` (6 sheets) — same, `03_hallett.txt` (91 kB).
- `02_FDA_PTH1R_reviews_4up.pdf` (61 sheets) — a scan, no text layer. OCRed at 300 dpi
  **quadrant by quadrant** rather than whole-sheet (`ocr_fda.py`), which recovers running
  prose cleanly. Numeric **tables** survive OCR poorly — the cell values scramble — so the
  three tables that mattered were read directly off 400 dpi renders and are archived here
  as PNGs. Every number quoted in the round-194 node comes from those images, not from the
  OCR text.

**4-up is fine for prose. For dense numeric tables, page images are what get used anyway.**

## What was in the bundle

`01_PTH1R_primary_papers_4up.pdf`
1. **Jolette 2017**, Regul Toxicol Pharmacol 86:356–365 — abaloparatide vs PTH(1-34),
   2-y F344 rat carcinogenicity, dosing from 7–8 weeks of age. DXA femoral BMC only.
   **No bone length.**
2. **Jolette 2006**, Toxicol Pathol 34:929–940 — rhPTH(1-84) 10/50/150 µg/kg/d, 2 y, F344.
   Contains the **delayed-start group** (dosing from 8 months of age) and the BMA-inferred
   femoral elongation claim now withdrawn under CORR-190.
3. **Wang 2023**, Eur J Orthod — already held (`cjac069`, deflated in round 193).

`02_FDA_PTH1R_reviews_4up.pdf`
- Sheets 1–15: **NDA 21-318 (FORTEO, teriparatide) Pharmacology Review(s)** — the review
  of Lilly studies R00100/R00200 (published as `vahle2004`), plus IND-review reproductions
  of Nonclinical Pharmacology Reports 01 and CG3-04 from 25 Sep 1995.
- Sheets 16–61: **NDA 208743 (TYMLOS, abaloparatide) Pharmacology/Toxicology Review**,
  Kuijpers.

`03_Hallett_resting_zone_4up.pdf`
- **Hallett 2021**, eLife 10:e64513, complete with methods and references.

## The three tables that decided the round

| file | what it shows |
|---|---|
| `fda_nda21318_interim_femur_length_table.png` | QCT femur length, both interim sacrifices. 2–8 mo window: 32.8 / 33.3\* / 33.9\* mm at 0/5/30 µg/kg/d. 6–12 mo window: 34.2 / 34.7\* / 35.2\* mm. **The age gate is retired.** |
| `fda_nda21318_terminal_femur_length_table.png` | Terminal sacrifice, 26 months of age, eight arms including two dosed continuously to termination. **Femur length = 35 mm in every arm, no asterisk**, while every other row of the same table is starred. |
| `fda_nda21318_cg3_04_18day_young_rat.png` | Unpublished Lilly CG3-04: 4-week-old SD rats, 18 d, 0/16/80 µg/kg/d. Body weight gain +20 %, tibial parameters +10–50 %, **"femur length was the same in all groups"**. |

## Pulled to close questions the bundle opened

- `preotact_epar_scientific_discussion.txt` — EMA EPAR for Preotact (rhPTH 1-84), fetched to
  look for the Jolette 2006 delayed-start femoral BMA per group. It confirms the design
  ("an additional high-dose group was added to begin dosing at 8 months of age") and
  **reports no femoral BMA or length per group**. The delayed-start length comparison
  remains unmade.
- `chu2026.txt` — already-held human pubertal growth plate scRNA-seq, re-read for PTH1R
  zonal assignment after Hallett raised the question in mouse.

## Tools run

- `atlas/tools/pth1r_final_length_ledger.py` → `final_length_ledger_output.txt`
  Every femoral-length observation under a PTH1R agonist in one table with its measurement
  method attached; recovers an implied SD from the significance boundary of the interim data
  (0.47 mm, CV 1.3 %, **inferred, value_unverified**) and bounds the terminal null at ~2 % of
  final length at 80 % power — which excludes the `vahle2002` caliper claim and does not
  exclude a ~1 % gain.
- `atlas/tools/hallett2021_resting_zone_cycle_time.py` → `hallett_cycle_time_output.txt`
  LRC:non-LRC EdU ratio (3.45 at 1 wk, 2.48 at 2 wk) is assumption-free. The absolute mouse
  resting-zone cycle time is a declared sweep over assumed S-phase duration and EdU window,
  10–59 d, and the labelling index's lower 1 s.d. bound is within noise of zero, so this
  dataset **bounds T_stem from below only**.

## Corrections this round

**CORR-190** — `jolette2006`'s femoral elongation is inferred from bone mineral *area*, which
is length × width. Withdrawn as a length measurement; it is not a replication of `vahle2002`.
The rule from CORR-189 now extends explicitly to DXA/pQCT projected areas.
