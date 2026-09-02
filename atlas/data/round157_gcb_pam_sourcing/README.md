# Round 157 — the GC-B PAM series: which one, and where to get it

Computed by this atlas 2026-08-09 from PubChem PUG REST + RDKit. Files: `sets.json` (active-CID sets),
`sel_props.json` (properties of the 253 selective actives), `cationic_selective.json`, `charge.py`.

## 1. The selectivity set, computed from raw screening data

The GC-B and GC-A primary screens from the same Mayo/Sanford-Burnham programme ran the **same
370,293-compound library**, so selectivity is directly computable:

| set | n |
|---|---|
| AID 1920062 GC-B primary actives | 399 |
| AID 1671463 GC-A primary actives | 519 |
| AID 1671466 GC-A confirmatory actives | 196 |
| GC-B ∩ GC-A primary | 146 |
| **GC-B active AND NOT GC-A active** | **253** |

Not the paper's own 86-compound triage (28% threshold + 10% difference) — a different, more permissive
rule. A single 10 µM point is a hypothesis, not a potency.

## 2. Nearest neighbours to MCUF-42 among the 253 (Morgan r=2, 2048 bit)

| Tanimoto | CID | MW | scaffold difference vs MCUF-42 | HTS %act @10 µM |
|---|---|---|---|---|
| **0.709** | **647514** | 394.3 | **piperazine** for piperidine → **compound 1** | **96.67** |
| 0.604 | 786411 | 342.2 | morpholine | 43.42 |
| **0.593** | **3588620** | 355.3 | **N-methylpiperazine** | **50.37** |
| 0.500 | 647949 | 394.3 | cyanoethylpiperazine, 3,4-diCl | 61.33 |
| 0.492 | 2291818 | 359.9 | cyanoethylpiperazine, 3-Cl | 72.74 |
| 0.393 | 732502 | 307.8 | morpholine, 3-Cl | 35.32 |

**CID 647514 is compound 1.** `ma2024`: *"the piperidine analog 24 retained the potency of the
piperazine-containing primary hit 1."* Published: **EC₅₀ 0.74 µM, Eₘₐₓ 112%**, no GC-A activity to 67 µM
— vs MCUF-42's 0.80 µM / 86%.

## 3. Availability — the decisive practical fact

| compound | CID | chemical vendors |
|---|---|---|
| **MCUF-42** | 176516521 | **0** (only IUPHAR/BPS) |
| **compound 1** | 647514 | **14**, CAS **332862-27-8** |
| N-methylpiperazine analogue | 3588620 | 7 |

`ma2024` states MCUF-42 "was not represented in the commercial space." Confirmed.

**Catalogue handles (verified; no price obtainable — 403/404/JS on every vendor page):**

- **CID 647514** — Life Chemicals `F3271-0034` · `MolPort-000-284-234` · `MCULE-4898734944` ·
  Chem-Space `CSSS00160775461` · Vitas-M `STK839994` · InterBioScreen `STOCK2S-75892` ·
  Ambinter `1484440` · AKos `AKOS000604525` · + Asinex, A2B, AA Blocks, Angene, BenchChem, RR Scientific
- **CID 3588620** — Chem-Space `CSSS00132906775` · `MolPort-002-635-462` · `MCULE-1698746129` ·
  Vitas-M `STL349320` · AKos `AKOS022112541` · InterBioScreen `STOCK5S-22988`

MLSMR batch IDs `MLS-0020283.P031` and `MLS-0302874.P029` are direct evidence the NIH library bought these
commercially in screening quantities.

## 4. Charge — corrected (CORR-173)

SMARTS screen of the 253: 229 neutral, **15 (+1)**, 1 (+2), 8 (−1).

**The rule is wrong for compound 1.** Its free piperazine N bears a **2-cyanoethyl** *and* sits across the
ring from a **thioamide** — both strongly electron-withdrawing. It is almost certainly **neutral at pH
7.4**, partition ~0.97, **no Donnan gain**. The SMARTS rule tests connectivity and is blind to inductive
effects through bonds it doesn't match.

**CID 3588620 (N-methylpiperazine) is the real charge probe** — no cyanoethyl, only thioamide
deactivation.

**No pKa measured or found** for any series member; PubChem has none even for 1-acetylpiperazine. Only
anchor: piperazine pKa₁ 9.73 / pKa₂ 5.33 (CID 4837).

## 5. The SAR forbids the obvious fix

`ma2024`: R2 = H (free piperazine NH — most basic) → **inactive** (cpd 11); aryl and benzyl → inactive.
Position *requires* a small electron-withdrawing H-bonding group (nitrile ✓, CO₂Et ✓, 2-pyridinyl
moderate, methyl ether ✗). **The site that would most easily carry a base must carry an EWG.** N-methyl
was never reported as tested and *is* an independent screening active — the one opening.

## 6. Why the basic nitrogen was deleted

`ma2024`: *"Alkyl or acyl piperazines can have metabolic and potential toxic liabilities."* A generic
chronic-dosing preference for a cardiology indication — **not a measured liability of compound 1**. The
cardiac programme optimised away the exact property this indication wants.

## 7. The cationic premise — validated, with a warning

`hakim2025`: cationic carriers penetrate cartilage *because* net charge drives Donnan partitioning against
aggrecan fixed charge. **But** hydrophobic residues promote competitive binding and impair deep
penetration; the design rule is evenly distributed cations, **minimal hydrophobicity**. This chemotype is
lipophilic (XLogP ≈ 3.8, dichlorophenyl) — a cationic analogue risks avid surface binding with poor
distribution. Caveat: +14 arginine peptides in *articular* cartilage ≠ 355 Da small molecule in growth
plate.
