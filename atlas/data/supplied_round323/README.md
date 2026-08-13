# Operator-supplied 2026-08-12, round 323. STORED, NOT YET ANALYSED.

The operator's instruction on delivery was "don't do anything yet just store these", and this
directory is exactly that. Nothing here has been read beyond the minimum needed to name the files
correctly, and no claim anywhere in the atlas rests on them yet.

## baffi2004_devbiol_2004_276_124-142.pdf
`baffi2004`, PMID 15531369, Developmental Biology 2004;276:124-142, identified from the embedded
DOI 10.1016/j.ydbio.2004.08.027.
**This is the paper round 323 asked for.** Its abstract states that Col2a-Cre;Tgfbr2 conditional
knockout mice surviving postnatally "showed alterations in the length of specific bones" and does
NOT give the direction. That direction is the only postnatal bone-LENGTH readout for
chondrocyte-restricted TGF-beta loss in any species, and it decides the sign of the axis that two
independent screens converged on in round 323.
Open gap: `g_l12_what_is_the_postnatal_bone_length_direction_in_col2a_cre_tgfbr2_null_mice`.

## richard2025_supplement1_ATAC.xlsx (18 MB)
`richard2025`, PMID 39549696, Cell 2025;188(1):15-32.e24. ATAC-seq supplement. 49 sheets:
per-site peak sets at E54 and E67, site-`specific` sets, **LUMBAR and THORACIC**, GREAT annotations
per site, and four motif-enrichment sheets.
Relevant because round 323 established with a preregistered control panel that the LUMBAR and
THORACIC peak sheets in GSE252289 compare tissue COMPOSITION rather than chondrocyte regulation
(CORR-339) - fetal vertebral bodies are haematopoietic, the top axial hits are the MHC plus B2M,
and ACAN and COL9A1 come out appendicular. Whether the GREAT and motif sheets here are affected by
the same confound has not been checked.

## richard2025_supplement2_RNAseq.xlsx (4.3 MB)
Same paper, RNA-seq supplement. 37 sheets: per-site expression, per-site `_UP` sets, joint-level
differential expression (KNEE_DE, HIP_DE, SHOULDER_DE, ELBOW_DE), HIND-vs-FORE, LATE-EARLY with its
enrichment, per-site and per-joint time series, and a **DECONVOLUTION** sheet.
The DECONVOLUTION sheet is the one that bears directly on CORR-339, because the failure it names is
a cell-composition failure. Not opened.

## richard2025_supplement3.xlsx (26 MB) - supplied second batch, 2026-08-13
12 sheets: `COJO Height Variants`, `Sig. Height Variants`, `Variant Enrichments - E54`,
`Variant Enrichments - E67`, `LDSC Variant Enrichments`, `Height Gene-set enrichments`,
**`Limb-Length GWAS`**, `Gene Ranking Results`, `Tissue-Specific Ranking`, `ANOVA`, `Modularity`, `MAGMA`.
Coordinates are hg19, which matches the ATAC peak build determined in round 323.
`Limb-Length GWAS` is the sheet that bears on CORR-341 - the finding that a compartment coordinate is
ALLELE-specific, not gene-specific.

## richard2025_supplement4.xlsx (6.5 MB)
7 sheets: `PAINTOR Results`, `Paintor Fn`, `Variant Contacts`, `QTL Analysis`, `QTL - HIC`, `QTL - Height`,
`QTL - Reg`. Fine-mapping posteriors and chromatin-contact-based variant-to-gene assignment - the thing
round 318 and round 323 both lacked when assigning lead variants to genes by proximity.

## richard2025_supplement5.xlsx (0.4 MB)
7 sheets: `Module Definition`, `Module Height Assoc`, `Module Network Analyses`, `Module-Heritability`,
`Module Motifs`, `Motif-Biases`, `SLDP Analysis`. Co-expression modules with per-module height association
and partitioned heritability; CD1 (909 genes) contains COL2A1.

## richard2025_supplement6.xlsx (0.3 MB)
2 sheets: `Module Definition`, `Module T2D Assoc`. The same modules scored against type 2 diabetes rather
than height - useful only as a specificity control for supplement 5.

## richard2025_supplement7.pdf (49 pages)
Same paper, supplementary figures. Contents not inspected.

## STATUS UPDATE 2026-08-13
`baffi2004` HAS NOW BEEN READ. The gap it was requested for is closed - the postnatal direction is
SHORTER; see `atlas/data/round323/baffi2004_extracted_tables.json` and the round 323 node. The
richard2025 supplements remain unanalysed.

## What was NOT supplied and is still open
`greene2021` (PMID 34532615) supplementary data - whether any femur or tibia length was recorded in
the WILD-TYPE littermates dosed with the pan-TGF-beta antibody 1D11. See
`g_l12_does_a_tgf_beta_lowering_agent_lengthen_bone_in_a_normal_growing_animal`.


# SECOND DELIVERY, 2026-08-13

## alvarez2001_devdyn_221_311-321.pdf  — READ IN FULL
`alvarez2001`, PMID 11458391, Dev Dyn 2001;221:311-321. **The reference was already in this bibliography
(added 2026-08-06) but only at abstract level; the full text was not.** It is the compartment-selective
experiment with a LENGTH endpoint in normal tissue - TGF-beta1 shortens perichondrium-intact metatarsal
rudiments dose-dependently and does nothing to perichondrium-free ones, and the chondrocyte proliferation
response REVERSES when the perichondrium is stripped. See the round 323 node.

## NIHMS668225_supplement.pptx — READ, AND IT CONTAINS NOTHING USEFUL
Two slides, both "Supplemental Figure 1": AngII +/- losartan phospho-p38 and total-p38 westerns, and
RANKL +/- losartan phospho-JNK and total-JNK westerns, at 0/10/30/60 minutes. **No bone dimension of any
kind.** This closes the question of whether chen2015's supplement holds the missing femur length: it does
not.

## greene2021_supplementary_figure_S1.tif.gz — READ, AND IT CORRECTED THIS ATLAS
The file is an uncompressed TIFF despite the .gz name. Four panels: BV/TV, Tb.N, Tb.Sp, Tb.Th, with groups
WT/13C4, G610C/13C4, and four G610C/1D11 dosing schedules. **The wild-type arm receives 13C4, the isotype
CONTROL - not 1D11.** Confirmed against the methods. The round 323 node had claimed greene2021 dosed
wild-type littermates with 1D11; that claim is withdrawn (CORR-340). No longitudinal dimension in the
figure, and the paper's measured sites are lumbar vertebra L6 and femur.

## STILL NOT OBTAINED
`alvarez2002`, PMID 11934857, Development 2002;129:1913-1924 - "TGFbeta2 mediates the effects of hedgehog on
hypertrophic differentiation and PTHrP expression". Three lawful routes tried and refused: the publisher
PDF (HTTP 403), the publisher HTML (abstract only), and Europe PMC (isOpenAccess N, inEPMC N, listed as
"Free after 6 months" at the retired dev.biologists.org host, which no longer serves it).
**Its marginal value has DROPPED now that alvarez2001 is in hand** - alvarez2002 is the Ihh -> TGF-beta2 ->
PTHrP relay, i.e. mechanism, whereas alvarez2001 carries the length endpoint. Not worth chasing further
unless the relay becomes decision-relevant.
