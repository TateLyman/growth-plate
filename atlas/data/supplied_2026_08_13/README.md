# Datasets acquired 2026-08-13

Operator-supplied list plus one found by hunting. All registered in `atlas/quant/dataset_inventory.csv`.
**Total on disk: 466 MB.** Large binaries are gitignored; this manifest is committed.

## Acquired in full

| accession | what | why it matters | status |
|---|---|---|---|
| **GSE252288** | 69 human **in vivo** chondrocyte RNA-seq, multiple skeletal SITES and stages | attacks "the atlas has one generic growth plate" | `APPENDICULAR_RNA_quants.xlsx` (18 MB) |
| **GSE252289** | 89 human chondrocyte **ATAC-seq** | height GWAS → regulatory DNA → gene → site | `ATAC_peaks.xlsx` (18 MB) |
| **GSE225878** | genome-wide **CRISPR KO screen**, 22,624 genes, primary+secondary, D4+D15 | association → **causation** | 4 LFC tables ⚠ **see blocker** |
| **GSE225879** | RNA-seq of the sorted populations the screen selected on | tells you what the screen's axis *means* | xlsx (12 MB) |
| **GSE225796** | WT differentiation time course D1/3/5/10 | maps CRISPR hits onto a maturation trajectory | xlsx (4 MB) |
| **GSE114919** | mouse+rat, age × **zone** × **site**, 60 samples | the PERIOD: what changes as velocity falls | 4 xlsx (13 MB) |
| **GSE18338** | **human** growth plate across **puberty**, incl. same-patient early→late | endocrine → molecular → architecture, in human | RAW.tar (65 MB) |
| **GSE233188 / GSE234040** | barcoded **human** skeletal stem/progenitor clones + scRNA fate | real clonal behaviour, not pseudotime | RAW.tar (77 MB) ⚠ **FETAL — quarantined** |
| **PXD055563** | mouse chondrocyte proteome + phosphoproteome | biochemical STATE layer | `mzTab` only ⚠ **see blocker** |
| **HPO** | genes_to_phenotype + phenotype_to_genes | gene → tall/short/bone-age/proportion, computationally | 88 MB |

## Found by hunting — not on the supplied list

| accession | what | why |
|---|---|---|
| **GCST90728588** | **SITTING HEIGHT RATIO** GWAS, **545,982 people**, FULL SUMMARY STATISTICS (173 MB) | The residual here is **trunk-dominant**; every stack agent was characterised on **long bones**; CLAUDE.md calls the axial/appendicular split its most decision-relevant compartment fact. **First dataset able to separate genes that shift PROPORTION from genes that shift overall height.** |

Also located, not yet pulled: `GCST90728585` (451,921 EUR) and `GCST90727384` (72,471 Chinese) — same study,
single-ancestry arms, useful as replication. **Bone-age GWAS exists but is tiny** — `GCST90095044`, n=4,557,
CYP11B1 via alternative splicing, no summary statistics posted. Worth noting that CYP11B1 is 11β-hydroxylase
and R298 found the plate strongly glucocorticoid-**responsive** (NR3C1 19/25) while making no cortisol itself.

## ⚠ TWO BLOCKERS — things the operator can get that I cannot

1. **GSE225878 CRISPR screen: sign convention is uncalibrated and no gene clears multiple testing.**
   The deposited files give per-gene average LFC and −log(p) only. Across 22,624 genes the largest −log(p)
   among every atlas lead is ~2, so nothing survives correction, and the internal controls do NOT resolve the
   direction: `Sox9 −0.82` and `Runx2 −0.64` fit "required gene depleted", but `Npr2 +1.19` and `Pth1r +0.84`
   do not fit a growth axis. CORR-296 forbids assigning direction here.
   **NEEDED: the source publication for GSE225880 — its methods (what was selected on, and which direction
   is "early" vs "late" maturation) and its own hit list / the 145 implicated genes.**
2. **PXD055563: PRIDE holds only raw spectra.** 24 `.raw` + 24 `.mgf` plus a single `mzTab` which is
   IDENTIFICATION-mode — 8,100 proteins and 285,605 PSMs, so presence but **no quantification**. Re-searching
   raw spectra is not possible here.
   **NEEDED: the paper's supplementary phosphosite table** (site-level quant, WT vs Phlpp1 perturbation).

Neither blocker stops the other eight datasets from being used.
