# Round 154 — is the phosphatase compound obtainable, and is anything cheaper good enough?

Retrieved by this atlas 2026-08-09.

## 1. `chembl_pp5_axis_panel.json`

ChEMBL curated activities filtered to PPP-family targets for six compounds. The decisive
column is **PP2A over PP5**, because `PPP5C` is a clean height locus running the wrong way
(rs3764613-G lowers height at p = 5e-18 and lowers PPP5C expression across seven tissues).

| compound | PP2Ac | PP5 | PP1γ | verdict on the PP5 axis |
|---|---|---|---|---|
| **fostriecin** | 3.4 nM (holo), 1.4 nM primary | **>1,000 / >10,000 nM** | 131,000 nM | **passes** |
| cantharidin | 160 nM | **400–600 nM** | 1,780 nM | **fails — ~3-fold, non-selective** |
| calyculin A | 0.25 nM | 3.0 nM | **0.14 nM** | **fails — hits PP1 hardest** |
| okadaic acid | 7.0 nM | *no PP5 record* | 20 nM | **undetermined**, and only ~3-fold over PP1 |
| norcantharidin | — | — | — | no curated phosphatase activity |
| endothall | — | — | — | no curated phosphatase activity |

**The cheap fallbacks fail the decisive test.** Cantharidin — the tool every positive result on
this arm was generated with — is ~3-fold PP2A over PP5, i.e. effectively non-selective, which is
the same failure mode as `li2024a` compound 28a (CORR-163), only without the direction being
reversed. Fostriecin remains the only compound with the required profile.

## 2. `swingle2009` — the primary SAR panel (PMC2766224, full text + Table 1 read)

Not archived here (copyright); numbers recorded in
`nodes/L12_pharmacology_as_mechanistic_probe/the_best_phosphatase_compound.yaml`.

| # | compound | PP2A | PP1 | PP5 |
|---|---|---|---|---|
| 1 | **fostriecin** | **0.0014 µM** | 72 µM | **60 µM** |
| 2 | cytostatin | 0.029 | >100 | >100 |
| 7 | **dephosphofostriecin** | **>100** | >100 | >100 |
| 8 | dephosphocytostatin | >100 | >100 | >100 |
| 9 | lactone-reduced | 2.1 | >100 | >100 |
| 10 | **lactone deleted** | **0.1** | ~100 | >100 |
| 11 | triene deleted | 4.2 | >100 | >100 |

Two results matter. **PP5 is measured at 60 µM**, retiring the `>10,000 nM` bound (~43,000-fold,
CORR-168). And **deleting the phosphate costs >71,000-fold**, converting the round-153
prodrug-not-analogue argument from inference to measurement.

**PP4 appears in no row of this panel.** Given `theobald2013` (PP4C knockdown alone reproduces
fostriecin's cellular phenotype; PP2AC knockdown does not), that absence is now the highest-value
missing number on this arm → gap `g_l12_fostriecin_pp4_versus_pp2a_attribution`.

## 3. Availability

- **NCI DTP `ChemData` NSC 339638** → FOSTRIECIN, `C19H27O9P.Na`, MW 453.0, CAS 87810-56-8
  (the **monosodium salt**), NCI60 5-dose + AIDS screen data attached. Cross-checked against
  PubChem SID 461173, depositor `DTP/NCI`, regid 339638, same CAS.
  **This is screening data, not inventory** — not evidence DTP can supply anything today.
- **PubChem CID 6913994** → 44 sources, ~15 chemical vendors (MedChemExpress, TargetMol,
  BOC Sciences, Ambinter, BLD Pharm, Biorbyt, Smolecule, CymitQuimica, A2B Chem, RR Scientific,
  AA BLOCKS, Starshine, EvitaChem, Clinivex, Chemieliva).
- **No price or quantity was obtained.** MedChemExpress → HTTP 403, TargetMol → HTTP 412,
  scbt → 403; CymitQuimica and Biorbyt render results in JavaScript. A listing is not a quotation
  and is not stock. Nothing here should be read as a verified price.

## 4. Routes to material

| route | status | cheap? |
|---|---|---|
| fermentation, *Streptomyces pulveraceus*, 73 kb PKS cluster (`kong2013`, `stampwala1983`) | the historical route — **the one that failed on supply in 1999**; no titre obtained | unknown, unproven |
| total synthesis, `jiang2025` | **9 steps** LLS from (R)-1,2,4-butanetriol vs 17–34 for 17 prior routes — but the key C–H oxidation needed **rational enzyme engineering + small-molecule additives** | no — needs an engineered biocatalyst |
| simplified analogue 10 | already synthesised (Boger lab, 2003/2006); MW ~322, no lactone | **yes** — but 70-fold weaker |

**Prodrug prior art: none.** Europe PMC `fostriecin AND prodrug` → 9 records, not one of them a
fostriecin prodrug. Nearest usable masking chemistry is `klootwyk2023` (boryl-allyloxy
phosphotriesters release phosphate monoesters under H₂O₂) — but an ROS trigger is wrong for
cartilage.

## 5. Partition arithmetic (recomputed; supersedes round 153 for the prodrug row)

| species | MW | charge | size | Donnan | **net** |
|---|---|---|---|---|---|
| fostriecin free acid | 430 | −2 | 0.95 | 0.22 | **0.21** |
| fostriecin masked prodrug | ~570 | 0 | 0.90 | 1.00 | **0.90** |
| analogue 10 free acid | 322 | −2 | 1.00 | 0.22 | **0.22** |
| analogue 10 masked | ~462 | 0 | 0.94 | 1.00 | **0.94** |

Masking fostriecin buys **~4.3×**, not the ~4.5× recorded at round 153 — the earlier figure applied
the *parent's* size term to the prodrug and ignored the promoiety's mass (CORR-167).

Potency × partition, relative to fostriecin free acid = 1.00: **masked fostriecin 4.5**,
analogue 10 free acid 0.01, masked analogue 10 0.06. **The cheap analogue is ~100× behind.**
