# Round 156 — the GC-B allosteric compounds, verified

Retrieved/computed by this atlas 2026-08-09.

## 1. The Thr640 / Ile624 assignment, verified independently

`andresen2023` maps its compound-20 selectivity to a single residue. Checked against UniProt directly
(sequences archived here):

- **P16066 (NPR1 / GC-A), 1061 aa** — residue **640 = T (Thr)**; context 630–650 `TLDWMFRYSLTNDIVKGMLFL`
- **P20594 (NPR2 / GC-B), 1047 aa** — residue **624 = I (Ile)**; context 614–634 `NLDWMFRYSLINDLVKGMAFL`

Aligned, the offset is a constant **16** (GC-A *n* ↔ GC-B *n*−16), which independently reproduces the
paper's chimera boundaries (GC-A 621–663 ↔ GC-B 605–647; 621−16=605, 663−16=647). Within the 21-residue
window shown, only three positions differ — 630/614 (T/N), 640/624 (**T/I**), 643/627 (I/L), 648/632
(L/A) — consistent with the paper's statement that nine residues differ across 621–663.

**The paper's headline is verified. Its internal caveat also stands:** compound 20 is inactive at GC-A
T640V but active at GC-B I624V — the same substitution, opposite outcomes — so context beyond one side
chain contributes.

## 2. Structures available

| PDB | domain | method | res. |
|---|---|---|---|
| 9BCP | **kinase homology domain, apo GC-A** | cryo-EM | 4.1 Å |
| 9BCO / 9BCS | intracellular domain, apo / +ANP | cryo-EM | 4.4 Å |
| 9BCL / 9BCN / 9BCQ | ectodomain, apo ×2 / +ANP | cryo-EM | 2.9–3.1 Å |
| 9BCV | cyclase domain +ANP | cryo-EM | 3.2 Å |
| 8TG9 / 8TGA | ectodomain + REGN5381 activating Fab | cryo-EM | 3.08 / 3.65 Å |

**NPR2 (P20594) has ZERO PDB entries.** Any structural work on the GC-B pocket must start from a GC-A
template or an AlphaFold model. Note the KHD structure is 4.1 Å — backbone placement only, side chains
not reliable at that resolution.

## 3. The two allosteric sites on GC-B

| | MCUF-42 (`ma2024`) | compound 20 (`andresen2023`) |
|---|---|---|
| site | **extracellular** domain, K_D 710 nM (SPR) | **intracellular** KHD, GC-A T640 / GC-B I624 |
| mechanism | raises CNP **affinity**, 2.6× on-rate | raises **efficacy**, +30% Eₘₐₓ |
| CNP curve | left-shift, **no Eₘₐₓ change**; 6.4× potency | Eₘₐₓ *and* potency (2.8× BNP) |
| phospho-dependence | not tested | **independent** — +183% on GC-A 7E |
| exists at wild-type GC-B? | **yes**, EC₅₀ 0.80 µM, Eₘₐₓ 86% | **no** — GC-B data are from the I624T mutant |
| GC-A cross-activity | none detected | it *is* the GC-A compound |

Never tested together. Opposite membrane faces.

## 4. MCUF-42 placed on the partition curve (the blank the PAM node flagged)

**CID 176516521**, `C19H18Cl2N2OS`, **MW 393.3**,
SMILES `C1CN(CCC1CCC#N)C(=S)C2=CC=C(O2)C3=C(C=CC(=C3)Cl)Cl`.
N-thioacyl piperidine → ring nitrogen **not basic** → **neutral at pH 7.4**.

Ideal Donnan (lesperance1992 FCD −0.19 to −0.35 M vs 0.15 M bath) × farnum2006 size term:

| compound | MW | charge | size | Donnan | **net** |
|---|---|---|---|---|---|
| **MCUF-42** | 393 | **0** | 0.97 | 1.00 | **0.97** |
| **cationic analogue (hypothetical)** | ~400 | **+1** | 0.97 | **2.26** | **~2.2** |
| MCUF-651 (GC-A sibling, +1) | 368 | +1 | 0.98 | 2.26 | 2.22 |
| vosoritide | 4102 | 0 | 0.47 | 1.00 | 0.47 |
| fostriecin free acid | 430 | −2 | 0.95 | 0.22 | 0.21 |

Monovalent-anion Donnan ratio λ = 0.55 (FCD −0.19) to 0.37 (−0.35); a **+1 cation** partitions at **1/λ =
1.82–2.70**, i.e. it is *concentrated*, not excluded.

**MCUF-42 is the best-partitioning agent this atlas has costed — but 0.97 is parity, not accumulation.**
A cationic analogue would be the first agent on this axis to *concentrate* in the target tissue, and
**MCUF-651 already carries a basic dimethylaminoethyl group**, so the scaffold tolerates one. Graded **E**:
ideal Donnan is least trustworthy for a lipophilic cation, which binds the very polyanions producing the
term.

## 5. The hard problem

**MCUF-42 oral bioavailability = 0.26%** in mice (detectable 2 h after 10 mg/kg PO; 8 h after 5 mg/kg IV).
Not an oral drug. The cationic sibling MCUF-651 **is** orally bioavailable and in preclinical development
for hypertension — so the same change argued for on partition grounds may also fix absorption.

Primary HTS: PubChem **AID 1920062**, 370,620 compounds at 10 µM, HEK293/GC-B + EC30 CNP, TR-FRET, Z′ ≈
0.87, S/B ≈ 4.2 → 399 hits → 86 GC-B-selective.
