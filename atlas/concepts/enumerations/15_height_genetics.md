# DOMAIN 15 — HUMAN HEIGHT GENETICS AT SCALE (complete inventory)
## R436 full-concept-space enumeration — EXTERNAL SEARCH ONLY

**Method.** Every row was reached by external query in this session: Europe PMC REST, NCBI eutils,
**GWAS Catalog REST API** (live study + ancestry counts), **IMPC Solr API** (live genotype–phenotype counts),
**HPO / ontology.jax.org API** (live gene–term counts and set intersections), **Open Targets GraphQL**
(live association counts). No file in `/home/user/growth-plate` other than the two briefs was read.
Anything not verified externally in this session is written `UNVERIFIED`. Species stated on every claim.

**Framing (per brief, CORR-358).** The load-bearing column is *DESIGN LIMITATION* — what the instrument
**cannot see by construction**. A heterozygous burden test cannot contain a recessive gene; a significance
threshold hides sub-threshold genes; a ratio outcome selects on the outcome; a fixed-content array can only
test variants somebody put on it; an ontology collapsed to the wrong unit cancels a gene against itself.
Every claim of the form "nothing is left" inherits every one of these decisions.

### LIVE NUMBERS PULLED THIS SESSION (all reproducible from the APIs named)

| query | result |
|---|---|
| GWAS Catalog, trait `body height` | **200 curated studies** |
| — ancestry tags across initial samples | European 103 · East Asian 59 · Hispanic/Latin American 32 · African-unspecified 23 · African-American 20 · South Asian 13 · NR 7 · Asian-unspecified 6 · Native American 5 · Greater Middle Eastern 3 · Oceanian 3 · Other 3 · Other-admixed 2 · Central Asian 2 · Sub-Saharan African 1 · SE Asian 1 |
| GWAS Catalog, `sitting height ratio` | **4 studies** (all one publication, PMID 41861830) |
| GWAS Catalog, `leg length` / `trunk length` / `birth length` / `childhood height` | **0 studies each under those trait names** |
| IMPC (mouse) `increased body length` | **63 significant calls, 60 unique genes** |
| IMPC (mouse) `decreased body length` | **351** → skew **5.6 : 1** against lengthening |
| IMPC (mouse) `long tibia` vs `short tibia` | **58 vs 275** → **4.7 : 1** |
| IMPC total genotype–phenotype rows | 67,350 |
| HPO `Tall stature` HP:0000098 | **180 genes / 237 diseases** |
| HPO `Short stature` HP:0004322 | **1,483 genes / 2,239 diseases** → **8.2 : 1** |
| HPO tall ∩ short | ⭐ **74 genes (41% of the tall list) are annotated BOTH ways** — incl. CYP19A1, FBN1, FGFR3, GLI3, DNMT3A, IGF2, DLK1, NF1, AKT1, COL2A1, HRAS, KRAS, KMT2C, MEG3, GPC4, HSPG2, KIF7, CDKN1C, EHMT1, ELN |
| HPO tall-only (directional) | **106 genes** — incl. NPR3, SPIN4, CHD8, EZH2, SUZ12, EED, ESR1, CBS, POR, AR, GPR101, MC2R, MRAP, STAR, NNT, TXNRD2, LOX, PLOD1, FBN2, EFEMP1, MFAP5, THSD4, ZNF469, TGFBR1, TGFBR2, SMAD3, TGFB1, TGFB2, DICER1, MEN1, CDKN1B, CDKN2B, GPC3, HERC1, DIS3L2, PDGFRB, PIGG, NELFA, KCNQ1, AMOTL1, HEY2, MYH11, MYLK, CHST14, DSE, FKBP14, FIBP, LRP4, MAT2A, LHCGR, HPGD, CCND1 |
| HPO `Delayed skeletal maturation` HP:0002750 / `Accelerated` HP:0005616 | 370 / 69 genes |
| HPO `Disproportionate tall stature` HP:0001519 | 42 genes |
| Open Targets `body height` (OBA_VT0001253) | **10,856 associated targets**; top: ZFAT, ADAMTS17, ACAN, NPR3, IGF1R, ADAMTS10, SERPINH1, PIEZO1, SCUBE3, FGFR3, SHOX, CRISPLD2, LCORL, DTL, IGF2BP2, GHRH, IHH, IRS1, STC2, CRISPLD1 |
| Open Targets `Tall stature` (HP_0000098) | **85 targets**; top: FBN1, EFEMP1, PDZD8, PMEPA1, DLG4, PTCH1, NSD1, SKI, CHD8, TGFBR1, FIBP |
| Open Targets `sitting height ratio` (EFO_0007118) | **12 targets**: NFATC2, BCKDHB, TBX2, UBXN2A, MYO18A, BOD1, TBX4, ATAD2B, CRYBA1, STC2, KLHL29, KCNG1 |

---

## TABLE — 146 ROWS (101 marked OBSCURE)

| # | RESOURCE/STUDY | WHAT IT MEASURES | DESIGN LIMITATION (what it excludes by construction) | QUERIED HERE? | PMID/URL | OBSCURE? |
|---|---|---|---|---|---|---|
| **A. COMMON-VARIANT GWAS, IN SEQUENCE (human)** |
| A1 | Weedon 2007 — HMGA2 rs1042725 | First reproducibly replicated common height variant. 4,921 discovery + 19,064 replication; ~0.4 cm/allele; ~0.3% of variance | Candidate follow-up on an era array; common SNPs only; no rare, no structural, no non-European | yes | 17767157 | no |
| A2 | Lettre 2008 (DGI/FUSION/SardiNIA) | 15,821 + >10,000 follow-up; 10 new + 2 known loci, ~2% variance. First to flag **let-7 targets, chromatin-remodelling proteins, Hedgehog** | 2.2M HapMap2-imputed SNPs; everything below MAF ~5% invisible; European | yes | 18391950 | no |
| A3 | Weedon 2008 | 13,665 + 16,482; **20 loci**; ~3% variance; names **IHH, HHIP, PTCH1, EFEMP1, ADAMTSL3, ACAN, CDK6, HMGA2, DLEU7** | Same MAF floor; P<5e-7 threshold of the era; European | yes | 18391952 | no |
| A4 | Gudbjartsson 2008 (deCODE) | 25,174 Icelanders + Dutch/EA/AA; **27 regions**; 0.3–0.6 cm/allele; 3.7% variance; strongest signal **ZBTB38** | Founder LD structure; single imputation reference; no rare variants | yes | 18391951 | no |
| A5 | Lettre 2008 — GDF5–UQCC | An osteoarthritis locus shown also to move height (~0.44 cm) | Candidate region; cannot resolve GDF5 vs UQCC | yes | 18193045 | no |
| A6 | **Lango Allen 2010 (GIANT)** | 183,727; **≥180 loci**; loci enriched for skeletal-growth-defect genes; ≥19 loci with multiple independent signals (allelic heterogeneity is normal) | ⭐ GIANT is a **meta-analysis of heterogeneously ascertained cohorts** — the exact design later shown to carry residual stratification (G7/G8) | yes | 20881960 | no |
| A7 | **Wood 2014 (GIANT)** | 253,288; **697 variants in 423 loci**, one-fifth of h²; all common variants = 60% of h². Adds **FGF signalling, WNT/β-catenin, chondroitin sulfate, mTOR, osteoglycin, hyaluronic-acid binding** | Same stratification exposure; MAF ≥1%; effect estimates later shown inflated vs UKB | yes | 25282103 | no |
| A8 | Yengo 2018 (GIANT+UKB) | ~700,000; **3,290 near-independent SNPs** at P<1e-8; 24.6% of variance out-of-sample; PGS r≈0.44 | European only. The revised 1e-8 threshold **discards everything between 5e-8 and 1e-8** | yes | 30124842 | no |
| A9 | ⭐ **Yengo 2022 "saturated map" (GIANT)** | **5.4M individuals, 5 ancestry groups. 12,111 independent SNPs accounting for nearly all common-SNP h². 7,209 non-overlapping segments, mean ~90 kb, ~21% of the genome. 40% (45%) of variance in EUR but only ~10–20% (14–24%) in other ancestries** | ⭐⭐ **"Saturation" = saturation of COMMON-SNP heritability in EUROPEANS.** Cannot see rare variants, structural variants, VNTRs, recessive effects, parent-of-origin, X/Y/PAR, mtDNA, GxE, or non-additive variance. Authors attribute the ancestry gap to LD + allele frequency, not different biology | yes | 36224396 (preprint PPR441118) | no |
| A10 | GWAS Catalog `body height` full curated set | 200 studies; ancestry table above | Curated from **published literature only** — preprints and unpublished biobank scans absent; curator-assigned trait names fragment synonymous traits (`leg length` returns zero) | yes (live API) | ebi.ac.uk/gwas/rest/api | **yes** |
| A11 | ⭐ **Bartell 2026 — skeletal proportions in two populations** | GWAS of **sitting height ratio** in ~450,000 European (UKB) + ~100,000 East Asian (China Kadoorie); **565 independent SHR loci**; 36 credible sets with heterogeneous cross-ancestry effects; also analyses sitting height and leg length separately | ⭐⭐ **A RATIO SELECTS ON THE OUTCOME.** The authors state fine-mapped SHR signals are often **distinct** from height signals — so a compartment coordinate derived from ratio-selected variants is an *allele* property, not a *gene* property, and cannot be read as "this gene grows the trunk" | yes | 41861830 (erratum AJHG 2026;113:1364) | no |
| A12 | Chan/Hirschhorn 2015 — genome-wide body-proportion analysis | Classifies height-associated variants **by mechanism of action** using body proportion; implicates skeletal-development genes | Pre-UKB n; ratio design as A11 | yes | 25865494 | **yes** |
| A13 | Jee/KCPS2 2025 — Korean GWAS | 153,950 Koreans, 36 quantitative traits incl. height; **301 previously unreported loci**; meta with KoGES + Biobank Japan + Taiwan Biobank + UKB → **4,588 loci not significant in any contributing GWAS** | East Asian discovery cannot recover EUR-private alleles; array + imputation | yes | 40436827 (GCST90662911) | **yes** |
| A14 | Taiwan Biobank × Biobank Japan × UKB, 36 traits | 102,900 TWB individuals; hundreds of novel loci across 36 quantitative traits incl. height | Trait harmonisation across biobanks is the limiting step | yes | 38116116 | **yes** |
| A15 | ⭐ **Verma 2024 — Million Veteran Program** | 635,969 diverse US veterans, **2,068 traits**, 13,672 risk loci; **1,608 significant only after including non-European participants**; 6,318 fine-mapped signals, one third from non-EUR | ⭐ **Veteran cohort: male-skewed, older, and passed a military-fitness screen — a height/health selection filter at enlistment.** Height is an EHR-derived minimum inv-normal field, not a research stadiometer | yes | 39024449 (GCST90479634-6) | **yes** |
| A16 | GIANT as an instrument, considered as such | The umbrella behind A6–A9 | ⭐ Cohorts differ in ascertainment, measurement (self-report vs measured) and geography. Berg 2019 / Sohail 2019 showed this manufactured a spurious selection signal. **Any conclusion computed on GIANT betas inherits it** | yes | see A6–A9, G7, G8 | no |
| A17 | Trans-ancestral GWAS of longitudinal pubertal height growth | Growth *trajectory*, not attained height; shared heritability with adult health outcomes | Longitudinal cohorts are small; requires repeated childhood measures that biobanks do not have | yes | 38229171 (+ correction 38773652) | **yes** |
| A18 | Pubertal height-growth GWAS, LIN28B and pubertal timing | 18,737 European samples with longitudinal height; 10 loci; separates prepubertal from pubertal growth | Small; European; parametric growth-curve fitting imposes a model | yes | 23449627 | **yes** |
| A19 | Northern Finland Birth Cohort 1966 — growth-parameter GWAS | Peak height velocity in infancy and puberty, timing of the spurt | Single birth cohort; candidate-variant era | yes | 19266077 | **yes** |
| **B. RARE / CODING VARIATION AND BURDEN TESTS (human)** |
| B1 | ⭐ **Marouli 2017 (ExomeChip)** | **83 coding height variants at MAF 0.1–4.8%, up to 2 cm/allele** — >10× the average common variant. Names **IHH, STC2, AR, CRISPLD2**; new candidates ADAMTS3, IL11RA, NOX4; proteoglycan/GAG synthesis. ⭐ **Rare height-INCREASING STC2 alleles (+1–2 cm/allele) shown to compromise proteolytic inhibition of PAPP-A → more IGFBP-4 cleavage → higher IGF bioavailability** | ⭐ **ExomeChip is a FIXED-CONTENT ARRAY.** It can only test variants someone put on the chip, drawn from ~12,000 mostly European exomes. Singletons and population-private variants are structurally absent | yes | 28146470 | no |
| B2 | ⭐⭐ **Kosmicki 2026 preprint — rare protein-coding variation, >1.4M individuals** | **826,066 discovery exomes → 207 height genes; 98% replicate in 624,567 more.** Singleton (<0.0001%) pLoF implicates **17 genes**, effects **−17 cm (ACAN) to +11 cm (FBN1) per allele, 52× the average common variant** and comparable to the 1% tails of a common-variant PGS. Explicitly names **TET1, DTL, IGF2BP2** as having effects at least as large as established Mendelian height genes **but no documented stature or skeletal-growth syndrome — and says this is particularly true for genes where rare variants INCREASE height** | ⭐⭐ **A HETEROZYGOUS GENE-BURDEN TEST. IT CANNOT CONTAIN A RECESSIVE GENE — no number of exomes fixes a zygosity model.** Also: coding only (enhancer, UTR, deep-intronic invisible); variants are collapsed into a mask, so the **mask definition sets the answer**; genes with too few living pLoF carriers are untestable; and the significance threshold hides sub-threshold genes | yes | PPR1258977 (preprint) | no |
| B3 | UKB whole-exome burden platforms in general | 450–500k exomes, gene-level burden across thousands of traits | Same zygosity + coding-only + mask limits as B2, plus UKB's **healthy-volunteer bias** | yes | see B2, C7 | no |
| B4 | ⭐ **Barton/Mukamel 2022 — spectrum of recessiveness in UK Biobank** | 3,475 rare curated ClinVar/OMIM **recessive-disease** variants imputed into ~500k; 102 trait associations. ⭐ **A POR missense implicated in Antley-Bixler syndrome associates with +1.76 cm (SE 0.27) in HETEROZYGOTES** | Sees only the **already-curated** recessive allele catalogue, and only variants that are imputable from a tagging haplotype | yes | 35649421 (PPR432527) | **yes** |
| B5 | ⭐ **Pakistan Genome Resource 2026** | 173,303 exomes+genomes with high familial relatedness; participants collectively carry **homozygous LoF in 6,476 genes**; biomarker associations and recall-by-genotype | ⭐ **THE INSTRUMENT THAT SEES EXACTLY WHAT B2 CANNOT.** But it is a different population, so EUR effect sizes do not transfer, and its own trait panel determines whether height was analysed at all (`UNVERIFIED` whether height was) | yes | 42310464 | **yes** |
| B6 | Exome/microarray in clinical **SHORT** stature cohorts | Diagnostic-yield studies and meta-analyses of ES + chromosomal microarray | ⭐ **ASCERTAINED ON BEING SHORT — structurally cannot return a height-INCREASING gene.** This is the selection bias as a study design | yes | 37695591; 34006472; 41712405; 41001785; 41076472; 39415983 | no |
| B7 | ⭐ **Exome sequencing in syndromic TALL stature** | 37 patients >97.7th percentile with syndromic features; diagnosis in 11; **four novel candidate overgrowth genes**; P/LP in **FBN1, PTEN, NSD1, SUZ12, CDH8, DEPDC5** | ⭐ Tiny n **because tall is not a disease**. Requires *syndromic* features, so non-syndromic tall stature is excluded by design | yes | 40577202 | **yes** |
| B8 | ⭐ **Familial tall stature — 786-gene panel + karyotype (Czech)** | 34 children with FTS; **genetic cause found in 11/34 (32.4%)** incl. **SUZ12 ×2, FGFR3, CHD8, GPC3, PPP2R5D**; 10 of the 34 had NO syndromic signs | Referral cohort; panel content bounds the answer; ACMG classification requires prior disease evidence | yes | 38307035 | **yes** |
| B9 | ⭐ **Non-familial tall stature, same programme** | 55 children; cause in only **6/55 (11%)**; **four were gonosomal aneuploidies (47,XXY ×2, 47,XXX, 48,XXXX)**, one SHOX duplication, one TGFBR2 (Loeys-Dietz) | ⭐ **Cytogenetic, not sequence, is the dominant finding in non-familial tall stature** — so a sequencing-only instrument misses most of it | yes | 40524006 | **yes** |
| B10 | Systematic genetic investigation of tall stature (Brazil) | 42 patients; sequential karyotype → CMA → MS-MLPA → panel → WES; **14/42 (33.3%) diagnosed**; FBN1 ×3, NSD1 ×2, NFIX, SUZ12, CHD8, MC4R, SHOX trisomy, Beckwith-Wiedemann ×2 | Only **1 of 12** non-syndromic patients got a diagnosis — the non-syndromic tall phenotype is essentially undiagnosable with current instruments | yes | 31751304 | **yes** |
| B11 | ⭐ **Oligogenic non-syndromic familial tall stature — ciliary genes** | Trio + family exome in a male at height +3.5 SD: shared damaging heterozygous variants in **CEP104, CROCC, NEK1, TOM1L2, TSTD2** — **three of five are ciliary genes**; all expressed in mouse growth plate | ⭐ n=1 family. Oligogenic models are **invisible to single-gene burden tests AND to single-variant GWAS** — no instrument in section A or B is designed to find them | yes | 34194391 | **yes** |
| B12 | ⭐ **NAV2 and isolated tall stature** | Three-generation pedigree, tallest man 211 cm; six shared damaging heterozygous variants; **IFT140, NAV2, SCAF11** also associated with height in GWAS; NAV2 knockout in Xenopus supports a growth-promoting role | Single pedigree; the Xenopus result shows NAV2 *promotes* growth, i.e. loss would shorten — direction must be read carefully | yes | 38152138 | **yes** |
| B13 | SHOX duplications in idiopathic tall stature | 81 girls with idiopathic tall stature and normal karyotype: **one extra SHOX copy in 3 (3.7%)**, heights +2.87 to +3.98 SD, all with **low sitting-height/height ratios** | qPCR/MLPA dosage only; small; girls only | yes | 28667773 | **yes** |
| B14 | Rare COL11A1 variant and adult height in Han Chinese | Single rare variant strongly associated with adult height | Single gene, single population, small, not biobank-replicated here | yes | 27614704 | **yes** |
| B15 | International guideline on genetic testing of children with short stature (2026) | Consensus on when to sequence a short child | ⭐ **Institutionalises the short-only ascertainment of B6** — there is no equivalent guideline for tall children | yes | 41543979 | **yes** |
| **C. WHOLE-GENOME SEQUENCING AND HERITABILITY (human)** |
| C1 | Silventoinen 2003 — twin cohorts, 8 countries | 30,111 complete twin pairs; the canonical **h² ≈ 0.8** and its cross-country variation | ⭐ Twin h² assumes **equal environments and random mating**; height is the archetypal assorted trait (H5). Self-reported height in 7 of 8 populations | yes | 14624724 | no |
| C2 | Twin h² without zygosity in LMICs | Mixture models on 249 Demographic & Health Surveys | Under-5 height ≠ adult height; no zygosity | yes | 35242993 | **yes** |
| C3 | Self-report vs measured height in Australian twins | Quantifies measurement error and its effect on h² | Shows the phenotype itself is an instrument with error | yes | 16933140 | **yes** |
| C4 | Yang 2010 — common SNPs explain a large fraction of h² | Founded the SNP-heritability / missing-heritability programme | ⭐ **SNP-h² is by definition the variance TAGGED BY THE GENOTYPED SNPs.** Rare, structural and non-additive variance is outside it by construction | yes | 20562875 | no |
| C5 | Yang 2015 — imputed variants, negligible missing h² | Imputation recovers most pedigree h² for height and BMI | The imputation reference panel sets the floor; European | yes | 26323059 | no |
| C6 | ⭐ **Wainschtein 2022 — WGS heritability** | 25,465 unrelated European WGS: **h²(height) = 0.68 (SE 0.10)**; low-MAF variants in low-LD regions carry the recovered fraction | Small n for WGS-GREML; European; **cannot localise the recovered variance to any gene** | yes | 35256806 (PPR74125) | no |
| C7 | ⭐ **2026 — Estimation and mapping of missing heritability** | **347,630 UKB European WGS, 40 million variants (MAF>0.01%), 34 traits: WGS captures ~88% of pedigree narrow-sense h² — 20% from rare (MAF<1%) and 68% from common** | ⭐ Floor at MAF 0.01% — **ultra-rare and de-novo variation is below it**; European; additive model only | yes | 41225014 | **yes** |
| C8 | ⭐ **UK Biobank WGS Consortium 2025 — 490,640 genomes** | Full UKB WGS; structural variants and exonic/UTR variation genotyped accurately; standing height (field 50) sumstats deposited | ⭐ Ancestry: **457,377 non-Finnish European vs 9,091 African / 9,388 South Asian / 2,854 Ashkenazi** — a >45:1 imbalance bounding every non-EUR analysis | yes | 40770095 (GCST90474621, GCST90667746) | **yes** |
| C9 | ⭐⭐ **Hawkes 2024 — rare NON-CODING WGS association for height** | **333,100 individuals (UKB 200,003 + TOPMed 87,652 + All of Us 45,445). Rare (<0.1% MAF) single-variant and aggregate testing of proximal-regulatory, intergenic-regulatory and deep-intronic variants. 29 independent variants at P<6e-10 after conditioning, effects −7 cm to +4.7 cm. A non-coding aggregate proximal to HMGA1 gives +5 cm; conserved variants in MIR497HG on chr17 replicate** | ⭐⭐ **THIS IS THE CLASS OF VARIATION AN EXOME BURDEN TEST CANNOT SEE AT ALL, AND THE EFFECT SIZES ARE THE SAME ORDER AS CODING pLoF.** Its own limits: MAF<0.1% floor, and it must **pre-define regulatory annotation categories** — a regulatory element not in the annotation set cannot be tested | yes | 39362880 | **yes** |
| C10 | ⭐ **2026 preprint — pitfalls in ultra-rare-variant heritability** | 5,330,210 exome singletons in 305,813 unrelated UKB Europeans: population stratification biases singleton h² **both upward and downward**; estimates also **capture non-additive effects** | ⭐ Directly attacks the interpretation of B2-class results — a singleton burden h² is not cleanly "rare-variant heritability" | yes | PPR1266381 (preprint) | **yes** |
| C11 | Approximate-message-passing joint WGS modelling of height | Fits all WGS variants jointly | Methods paper; no new biology | yes | 41713425 (also PPR) | **yes** |
| C12 | h² of height by parental education, infancy→adulthood | The classic GxE-flavoured stratified h² design | Small; cohort-specific; education is a proxy for many things | yes | 32409744 | **yes** |
| C13 | Quantifying genetic heterogeneity between continental populations for height | Asks whether the same variants act the same way across continents | Common variants only; cannot address rare or population-private alleles (see G1) | yes | 33664403 | **yes** |
| **D. STRUCTURAL VARIATION, REPEATS, CNV (human)** |
| D1 | ⭐ **Mukamel 2021 — protein-coding VNTRs (Science)** | 118 protein-altering VNTRs estimated from exome data, imputed into 415,280 UKB, tested against 786 phenotypes: **among the strongest known common-variant associations with human phenotypes, HEIGHT NAMED EXPLICITLY**. Accounting for large-effect VNTRs also improved fine-mapping of nearby coding variants | ⭐⭐ **VNTRs ARE INVISIBLE TO SNP ARRAYS AND TO STANDARD SHORT-READ CALLING** — every GWAS in section A silently omits this class. Only 118 loci were tested, and imputation requires a tagging SNP haplotype, so untagged VNTRs remain invisible | yes | 34554798 (PPR269301) | **yes** |
| D2 | Mukamel 2023 — non-coding VNTRs | 9,561 autosomal VNTRs imputed into 418,136 UKB + 838 GTEx; 58 VNTRs fine-mapped to a trait, 18 also modulating expression/splicing | 99% of VNTRs are non-coding and most remain untested; imputation-based | yes | 37527660 (PPR558028) | **yes** |
| D3 | DNA repeat expansions in ~900,000 biobank participants (2026) | UKB + **All of Us**; germline vs blood-somatic instability; GWAS of somatic expansion found 29 modifier loci | Focused on ~15 highly polymorphic CAG loci — **not a genome-wide repeat scan**, and height was not a target trait | yes | 41501457 (PPR946446) | **yes** |
| D4 | Population-scale pathogenic repeat expansions, 1,020,833 samples | 37 disease-associated STR loci; associations with **7,671 BINARY traits** | ⭐ **Binary traits only — a quantitative trait such as height is outside the analysed phenotype set by construction** | yes | 41951733 | **yes** |
| D5 | eSTR map in GTEx | >28,000 STRs whose repeat number associates with nearby gene expression; top 1,400 fine-mapped | Expression, not height; GTEx tissues **do not include growth plate** | yes | 31676866 | **yes** |
| D6 | CNV burden and short stature | Clinical CGH cohort: short-stature subjects had greater **global CNV burden and longer average CNV** (p<0.002) | Clinical referral cohort ascertained on shortness; array-CGH resolution; **again cannot return a tall-direction result** | yes | 22118881 | no |
| D7 | CNV–height GWAS in Chinese, Korean, Japanese populations | 12q24 microdeletion influencing height in Koreans; NEDD4L CNV in Japanese; four suggestive CNVs in 618 Chinese | None survived multiple testing in the Chinese study; small n throughout | yes | 21193156; 23147675; 30776764 | **yes** |
| D8 | Asian tandem-repeat catalogue SG10K-TR (2026 preprint) | 916,274 autosomal TR loci in 9,490 Chinese/Malay/Indian individuals; TR variation selectively constrained in coding and promoter regions | Catalogue, not an association study; n far too small for height | yes | PPR1291806 (preprint) | **yes** |
| D9 | ⭐ **GHRd3 — ancient polymorphic deletion of exon 3 of the growth hormone receptor** | A **common structural deletion in GHR**; reported nearly fixed in the ancestral population of modern humans and Neanderthals then adaptively reduced; **sex-specific phenotypic effects** | ⭐ A common exon-level deletion in the central GH-axis receptor that **SNP arrays do not genotype directly**. Its association with adult height is contested — one study reports association in a Saudi population, another finds no association with height in healthy young adults | yes | 34559564; 38356830; refuted by 24893921 | **yes** |
| D10 | ⭐ **Biobank-scale CNV / structural-variant association with height** | Four separate query routes (recurrent CNV × biobank × height; structural variant × UK Biobank × quantitative trait; CNV × UK Biobank × height; structural variation × biobank × height 2020–2026) all returned **ZERO** records | ⭐⭐ **A GAP, NOT A NEGATIVE.** The capability now exists — the 490,640-genome UKB WGS release explicitly reports improved structural-variant genotyping — but **no biobank-scale SV/CNV association analysis for height was found in this session.** Every CNV–height study located (D6, D7) is a small clinical or array-era cohort ascertained on shortness | yes (nothing found) | see C8 for the capability | **yes** |
| **E. SEX CHROMOSOMES, PAR, SHOX (human)** |
| E1 | ⭐ **SHOX / PAR1 dosage** | SHOX sits in PAR1 and escapes X-inactivation. Haploinsufficiency → Léri-Weill dyschondrosteosis and idiopathic short stature; nullizygosity → Langer mesomelic dysplasia; **three copies → tall stature** | ⭐⭐ **PAR1 IS EXCLUDED FROM MOST GWAS BY DEFAULT** (X-handling and ploidy coding). SHOX returns nothing from a standard autosomal scan despite being one of the largest single-gene contributors to human stature | yes | 10549307; 27194969; 40229560 | no |
| E2 | ⭐ **SHOX enhancer CNVs** | ~35% of LWD cases are non-coding deletions **downstream** of SHOX; a 563 bp limb enhancer identified by transgenic mouse assay; ≥7–8 conserved non-coding elements; far-downstream deletions also pathogenic | ⭐ Enhancer CNVs are missed by coding-only sequencing **and** by MLPA panels that tile only exons — so the reported SHOX-deficiency rate is a floor | yes | 30250174; 34811950; 35319168; 37601716; 26040210 | **yes** |
| E3 | ⭐ **SHOX sex-biased random monoallelic expression (preprint)** | Reports SHOX expression lower in female than male **cartilage** with DNA-methylation differences, offered as a contributor to the ~13 cm male–female gap | ⭐ Preprint; peer-reviewed publication status **UNVERIFIED**. If correct, SHOX dosage is not simply 2-vs-2 and the escape-from-XCI assumption is incomplete | yes | PPR387405 (preprint) | **yes** |
| E4 | Sex-chromosome aneuploidy dose–response | 305 SCA patients: **increasing sex-chromosome number affects height NON-LINEARLY (inverted U)**; SHOX copy number evaluated | Cross-sectional, clinically ascertained; mosaicism confounds | yes | 20425825 | **yes** |
| E5 | SCA effects on height/weight/BMI in childhood and adolescence | 177 youth across **8 SCA karyotypes** (XXX, XXY, XYY, XXXX, …); norm-derived z-scores; age-varying effects | Small n per karyotype; **<15% of SCA is clinically diagnosed**, so referral bias is severe | yes | 37768018 | **yes** |
| E6 | SCA by genomic (not clinical) ascertainment in MVP | 47,XXY / 47,XYY prevalence, morbidity, mortality in a diverse cohort; tall stature phenotype | Male veterans, adults only | yes | 38551561 (PPR692063) | **yes** |
| E7 | ⭐ **GCY — the Y-chromosome "growth control" locus** | Yq deletion mapping places a stature gene in a **~700 kb interval near the Y centromere**; FISH deletion mapping converges on a single location | ⭐ **NEVER RESOLVED TO A GENE, and Y is excluded from essentially every height GWAS.** One report of a Y + aromatase contribution to ~4 cm of male height was explicitly **not replicated** in an independent UK sample | yes | 10922386; 12114485; 11549641; refuted by 12864794 | **yes** |
| E8 | Turner / Klinefelter genotype–phenotype series | Decade of SCA cytogenetic + clinical data incl. rare variants and mosaics | Single centre; retrospective | yes | 41457053 | no |
| E9 | X-chromosome handling in height GWAS generally | Dosage-compensation coding (hemizygous males coded as 2) is an assumption that changes every X effect size | ⭐ **The X coding model is a design decision, not a measurement.** A per-dosage-unit beta for an X-linked gene is not a per-carrier beta for a hemizygous male | yes (method noted in B2's own text) | see B2 | **yes** |
| **F. NON-NUCLEAR, PARENT-OF-ORIGIN, SEX-SPECIFIC (human)** |
| F1 | ⭐⭐ **Gudbjartsson 2016 — parent-of-origin height variants (deCODE)** | 31.6M variants from WGS of 8,453 Icelanders imputed into 88,835. **13 novel associations across four models including parent-of-origin, \|β\| = 0.4–10.6 cm.** Three POO signals lower height **only when paternally inherited** and lie inside the imprinted **IGF2–H19** and **DLK1–MEG3** regions. IGF2-H19 and **TET1** also associate with birth length. Opposing parental effects observed | ⭐⭐ **A STANDARD ADDITIVE GWAS CANNOT DETECT A PARENT-OF-ORIGIN EFFECT AT ALL** — it requires phased parental origin, i.e. genealogy or trios. Iceland has both; UK Biobank, MVP and All of Us largely do not. **Every imprinted contribution to height is therefore invisible to the instruments in section A** | yes | 27848971 | **yes** |
| F2 | ⭐ **Mitochondrial DNA and adult height** | Targeted queries returned **NO mtDNA–adult-height association study**. Nearest hits: leukocyte mtDNA copy number vs anthropometry, and height as a disease-burden marker in mitochondrial disease | ⭐⭐ **mtDNA is dropped from essentially every height GWAS pipeline.** This is an **unexamined axis, not a measured negative** — a maternally inherited genome with no height instrument pointed at it | yes (nothing found) | 27367031; 30423112 | **yes** |
| F3 | Sex differences in height — genetic and hormonal (2025 review) | Reviews the ~13 cm male–female gap: sex chromosomes, SHOX, sex steroids | Review = index, not source | yes | 40813449 | no |
| F4 | Genome-wide genetic homogeneity between sexes and populations for height | Finds essentially the same additive architecture across sexes and continental groups | ⭐ Tests homogeneity **of common-SNP effects**; cannot address sex-specific rare effects, X-linked effects, or Y | yes | 26494901; 33664403 | **yes** |
| F5 | Quantitative-genetic model for indirect genetic effects **and genomic imprinting** under assortative mating (2026) | Derives how genetic variance changes under maternal, paternal and parent-of-origin effects, with and without assortment | Theory; no height estimate | yes | 41677404 | **yes** |
| **G. POPULATION, ANCESTRY, SELECTION, CONSANGUINITY (human unless stated)** |
| G1 | ⭐ **Chen 2020 — FBN1 E1297G in Peruvians** | Population-specific missense at 4.7% frequency: **−2.2 cm per copy, −4.4 cm homozygous** — stated as the largest known effect for a common height-associated variant. Under positive selection in non-Africans; skin microfibrils structurally altered | ⭐⭐ **Invisible to any European-discovery GWAS** because the allele is essentially private to Native American ancestry. **Directly demonstrates that "saturation" is population-scoped.** Also note the direction conflict with FBN1 het pLoF (+11 cm in B2) — FBN1 is not monotone | yes | 32499652 | **yes** |
| G2 | ⭐⭐ **Inbreeding depression on human height** | >35,000 people across 21 population samples: highly significant inverse association of genomic inbreeding with adult height | ⭐⭐ **DIRECT EVIDENCE OF RECESSIVE GENETIC VARIANCE FOR HEIGHT — precisely the component the het burden test (B2) is blind to.** But it is an aggregate estimate and **names no gene**, so it establishes the existence of a blind spot without filling it | yes | 22829771 | **yes** |
| G3 | ROH and height in an endogamous African population (Himba, Namibia) | Tests the inverse ROH–height relation inside an African population | Small; single population | yes | 36790690 | **yes** |
| G4 | ROH scan identifying a recessive height locus at 12q21.31 | Genome-wide ROH analysis, 998 discovery subjects | Small; array-era ROH calling; not replicated at biobank scale | yes | 20466785 | **yes** |
| G5 | Consanguinity in paediatric endocrinology | Consanguineous pedigrees as the classical route to recessive growth genes; ~8.5% of children worldwide have consanguineous parents | Case-driven; ascertained on disease | yes | 34847552; 25041402 | **yes** |
| G6 | ROH, demographic history and complex traits (2025 preprint) | ROH are ubiquitous in outbred populations, enriched for deleterious variants, and associated with height and lung function | Preprint; simulation-heavy | yes | PPR1231104 (preprint) | **yes** |
| G7 | ⭐⭐ **Berg 2019 — reduced signal for polygenic adaptation of height in UK Biobank** | Re-runs the European height-selection analyses with UKB effect estimates: signals **strongly attenuated or absent**; provides direct evidence that earlier analyses were confounded by population stratification | ⭐⭐ **THE CANONICAL DEMONSTRATION THAT AN INSTRUMENT'S DESIGN DECISION PROPAGATED INTO A DECADE OF DOWNSTREAM CONCLUSIONS.** Applies to anything computed on GIANT betas, not just selection tests | yes | 30895923 (PPR8165) | no |
| G8 | ⭐⭐ **Sohail 2019 — polygenic adaptation on height overestimated due to uncorrected stratification** | Same conclusion by an independent route; notes UKB is "much more homogeneously designed" | As G7 | yes | 30895926 (PPR7300) | no |
| G9 | Sardinia re-examination using **Biobank Japan**-ascertained loci | Deliberately breaks the European-ascertainment circularity by taking height loci from BBJ; recovers a selection signal in Sardinians and mainland Europeans | Depends on BBJ transferability; Sardinia is a founder isolate | yes | 32533944 (PPR93068) | **yes** |
| G10 | ⭐ **2026 preprint — converging evidence of positive selection at height loci in Europe** | Integrates multi-ancestry **and within-family** GWAS with allele frequencies from 13 European populations; selection signal survives correction for ancient admixture, but is **largely driven by allele-frequency differences between the Netherlands and other Europeans** | Preprint; within-family betas are noisy; "driven by one population" is a fragile base | yes | PPR1227225 (preprint) | **yes** |
| G11 | Predicting skeletal stature from ancient DNA (preprint) | Genetic scores in ancient individuals vs stature inferred from skeletons (n≈167 West Eurasian) | Preprint; tiny n; skeletal stature is itself estimated from femur length | yes | PPR305610 (preprint) | **yes** |
| G12 | Ancient DNA PGS in Eastern Eurasia | 1,245 ancient genomes; **height results explicitly "mixed" and non-linear with time before present** | ⭐ A PGS applied maximally far outside its training population — the portability problem at its most severe | yes | 39881595 | **yes** |
| G13 | African-American height GWAS (WHI SHARe) and admixture-mapping designs | Height GWAS in African-American women; two-stage admixture testing | Small relative to EUR; admixture LD blocks are long so resolution is poor | yes | 22021425; 21754915 | **yes** |
| G14 | Chinese stature GWAS — ethnic-specific loci; FLNB and SBF2 | Loci not seen in European scans | Small; array era; limited replication | yes | 19030899; 19039035 | **yes** |
| G15 | Taiwan Biobank height GWAS — NABP2, RASA2, RNF41, SLC39A5 | Four genes reported as novel for human height | Single population; replication limited | yes | 34270706 | **yes** |
| G16 | ⭐ **Neanderthal growth hormone receptor (2026)** | Neanderthal **GHR** carried two amino-acid changes plus a deletion. Cells expressing it proliferate faster on **pituitary** GH but not placental GH. **Some present-day humans have inherited it**, and tend to have more muscle mass and Neanderthal-like craniofacial traits | ⭐ Archaic introgressed haplotypes are commonly filtered out or poorly imputed in biobank pipelines. **No height endpoint reported** — this is a mechanism on the GH axis, not a stature result | yes | 42556345 | **yes** |
| G17 | Neanderthal/Denisovan **GLI3** R1537C knocked into mice | An archaic hedgehog-pathway variant altering downstream regulation and producing anatomical variation | Mouse; anatomical, not stature; single variant | yes | 38020913 (PPR685572) | **yes** |
| G18 | Positively selected variation and height generally | Signs of selective pressure on height-affecting variants | Superseded by G7/G8's stratification critique | yes | 22096598 | **yes** |
| **H. FAMILY DESIGNS, ASSORTATIVE MATING, GxE (human)** |
| H1 | ⭐⭐ **Howe 2022 — within-sibship GWAS (Nat Genet)** | 178,086 siblings from 19 cohorts; population (between-family) vs within-sibship estimates for 25 phenotypes. **Within-sibship estimates were SMALLER than population estimates for HEIGHT** (and for educational attainment, age at first birth, number of children, cognitive ability) | ⭐⭐ **POPULATION GWAS BETAS FOR HEIGHT CONTAIN DEMOGRAPHY (stratification, assortative mating) AND INDIRECT GENETIC EFFECTS FROM RELATIVES.** Within-sibship removes them at a large cost in power — so the true *direct* genetic effect on height is smaller than every number in section A | yes | 35534559 | **yes** |
| H2 | Within-family h² from ~500,000 sibling pairs, diverse ancestries (2025 preprint) | Robust within-family h² estimates, first for non-European ancestries | Preprint; whether height point estimates are reported is **UNVERIFIED** | yes | PPR1086679 (preprint) | **yes** |
| H3 | **Assortative mating for height — meta-analysis** | Systematic review of spousal height correlation: positive in Western populations but **not universal** | Phenotypic correlation only; cannot separate mate choice from post-mating convergence or confounding | yes | 27637175 | no |
| H4 | Height-associated variants demonstrate genetic assortative mating | Quantifies *genetic* (not merely phenotypic) assortment at height loci | Depends on the same GIANT-era loci | yes | 29146993 | **yes** |
| H5 | ⭐⭐ **Assortative mating biases marker-based heritability estimators** | Mathematical + simulation proof that **both method-of-moments and likelihood-based h² estimators are biased under assortative mating**; corrected estimators derived; common population-structure corrections do **not** mitigate it | ⭐⭐ **EVERY SNP-h² NUMBER IN SECTION C ASSUMES RANDOM MATING, AND HEIGHT IS THE ARCHETYPAL ASSORTED TRAIT.** So the SNP-h² baseline against which "saturation" (A9) is declared is itself biased | yes | 35115518 (PPR300875) | **yes** |
| H6 | Parental-haplotype reconstruction in up to 440,209 individuals (2025 preprint) | Detects **recent** assortative-mating dynamics that gametic-phase-disequilibrium estimates (cumulative over generations) cannot | Preprint | yes | PPR1091048 (preprint) | **yes** |
| H7 | MR of assortative mating in 51,664 UK Biobank couples | 118 assorted phenotypes; 54% show a causal partner-to-partner relationship | Couples in UKB are a self-selected subset | yes | PPR486135 / PPR493758 (preprints) | **yes** |
| H8 | Within-family Mendelian randomization | Shows dynastic, assortative-mating and stratification biases in MR; 61,008 + 222,368 siblings | Method paper; height used as an exemplar | yes | 32665587 | no |
| H9 | Modelling assortative mating between partners, siblings and in-laws (MoBa) | Genetic similarity between in-laws as a consequence of assortment | Educational attainment is the headline trait; height secondary | yes | 35233010 | **yes** |
| H10 | ⭐ **Gene–environment interaction on height** | A targeted `gene-environment AND height/stature` title query returned **ZERO** records. Nearest usable designs are h²-by-parental-education (C12) and PGS-expressivity-by-social-adversity (which found an effect for cognitive ability **but explicitly NOT for height**) | ⭐⭐ **A GENUINE HOLE. Height GxE is essentially not studied as such at biobank scale, despite the secular trend being the largest known environmental effect on human stature.** The one direct test found reports height PGS expressivity as robust to social adversity | yes (nothing found) | 32409744; 35393928 | **yes** |
| **I. POLYGENIC SCORES AND MENDELIAN RANDOMIZATION (human)** |
| I1 | Height PGS portability | Yengo 2022: 40–45% of variance in EUR vs ~10–24% in other ancestries | ⭐ The authors attribute the gap to **LD and allele-frequency differences within associated regions**, not different causal biology — so a portability failure is **not** evidence of population-specific mechanism | yes | 36224396 | no |
| I2 | Ancestry-modelled PGS in admixed US Latinos (HCHS/SOL) | Adds genetic-ancestry PCs alongside PGS to improve height prediction | Improves prediction; adds no biology | yes | 41904631 (PPR992907) | **yes** |
| I3 | Population-specific height PGS: Han Chinese/Taiwan, Korean forensic, Greek | Prediction, incl. forensic externally-visible-characteristic prediction | Prediction-only; small training sets; forensic use raises its own selection issues | yes | 39910149; 39120737; 40432881 | **yes** |
| I4 | ⭐ **Height PGS applied to idiopathic short stature** | 534 paediatric BioVU participants: PGS_height identifies non-familial ISS children carrying an **unmeasured polygenic predisposition to shorter height** not accounted for by existing measures | ⭐ Uses the PGS as a *diagnostic residual*, not as a lever. EHR-linked biobank; European-trained score applied to a paediatric US population | yes | 40108664 (PPR924504) | **yes** |
| I5 | Novel signals + height PGS in Southwestern American Indians | Longitudinal Preece-Baines growth parameters 1965–2007; asks how EUR-derived height variants act during adolescence | Single community; historical cohort | yes | 38483351 | **yes** |
| I6 | Geographic variation in height PGS within Japan | Tests whether the ~century-old north–south Japanese height gradient has a genetic component | Ecological; the G7/G8 stratification caveat applies within a country too | yes | 33900438 | **yes** |
| I7 | Cross-population "core SNPs" for height (2026 preprint) | Variants consistently in extreme PGS-weight ranks across ancestries, proposed as an interpretable core set | Preprint; PGS weights are not causal effects | yes | PPR1184240 (preprint) | **yes** |
| I8 | ⭐ **Genome-wide MR screen for drugs affecting body height (2024)** | Systematic screen of gene→height causal effects mapped to interacting drugs, explicitly to find drugs that "promote or delay growth" | ⭐⭐ **eQTL instruments come from GTEx tissues that DO NOT INCLUDE GROWTH PLATE**, and the drug-direction annotation is **curated from prior literature rather than derived** — so the direction column can inherit the literature's own errors | yes | 39649642 | **yes** |
| I9 | MR with height as **EXPOSURE** (CAD, stroke, cancer, diabetes, Alzheimer's, intelligence) | Large literature instrumenting height to test downstream disease | Height instruments carry the stratification and assortative-mating baggage of H1/H5; horizontal pleiotropy is extreme for a trait with 12,111 causal variants across 21% of the genome | yes | 38959188; 40106116; 39142240; 40004442; 42095392 | no |
| I10 | MR with height as **OUTCOME** — IGF-1, vitamin D, menarche, childhood obesity, GABA receptors | Two-sample MR asking what causally raises height | ⭐ Reverse-direction MR into height is weakly powered and pleiotropy-dominated. The GABA-receptor study exists **because supplements are marketed**, not because of prior biology — an ascertainment bias in the MR literature itself | yes | 41017432; 40898525; 39278795; 39878765; 41398882 | **yes** |
| I11 | Non-genetic component of height as a surrogate for childhood SEP (2026 preprint) | Residualises measured height on genetically predicted height to index early-life conditions | ⭐ **Inverts the usual use of a PGS: the RESIDUAL is the signal.** Requires the PGS to be well calibrated in the target ancestry, which it is not in admixed cohorts | yes | PPR1266289 (preprint) | **yes** |
| **J. FUNCTIONAL FOLLOW-UP OF HEIGHT LOCI** |
| J1 | ⭐ **Guo 2017 — epigenetic profiling of growth-plate chondrocytes (mouse femoral growth plate + human GWAS)** | Open-chromatin profiling of murine growth plates. Regions recapitulate chondrocyte biology, are **enriched at height GWAS loci**, particularly near differentially expressed growth-plate genes, and are enriched for chondrocyte TF motifs | ⭐ **MOUSE tissue used as the proxy because human growth plate is nearly unobtainable.** The most-cited functional bridge in this domain and it is cross-species by necessity | yes | 29205154 | no |
| J2 | ⭐⭐ **Baronas/Hirschhorn 2023 — genome-wide CRISPR knockout screen of chondrocyte maturation (Cell Genomics)** | Pairs human height GWAS with **genome-wide KO screens of growth-plate chondrocyte proliferation and maturation in vitro**. **145 genes** alter chondrocyte proliferation/maturation, 90% validating in secondary screening; enriched for monogenic growth-disorder genes and endochondral-ossification KEGG pathways. **Common variants near these genes capture height heritability INDEPENDENT of genes computationally prioritised from GWAS** | ⭐ **An in-vitro screen can only knock out a gene the cells actually transcribe** — an unexpressed gene returns an uninformative null, not a refutation. It reads chondrocyte proliferation/maturation **in culture**, not bone length. The screened cell type, the culture conditions and the sorting/readout marker (not named in the abstract, `UNVERIFIED`) all bound what it can return | yes | 37228756 | **yes** |
| J3 | ⭐ **Round-cell (resting) layer expression specificity is enriched in height GWAS** | Regressed layer-specificity scores from **dissected murine newborn tibial growth plate (resting/round, proliferative/flat, hypertrophic)** against gene-level height GWAS p-values: **specificity for the ROUND CELL layer is significantly associated with height GWAS signal (p = 8.5e-9)**, surviving conditioning on the other layers and on an OMIM skeletal-dysplasia gene set | ⭐ Mouse, newborn; three dissected layers only. Points the genetics at the **resting/stem-cell compartment**, which is the compartment with the fewest available human data | yes | 34346115 | **yes** |
| J4 | Lui 2012 — synthesising height GWAS with growth-plate expression | Used mouse/rat growth-plate expression microarrays + human disease databases + a mouse KO phenotype database to prioritise genes within the 180 GWAS loci: **78 genes strongly implicated**, incl. multiple PTHrP–IHH, BMP and CNP signalling genes | Rodent expression as the filter; prioritisation, not causal proof | yes | 22914739 | **yes** |
| J5 | ⭐⭐ **Chondrocyte eQTL / caQTL / 3D chromatin — the resource EXISTS but is aimed elsewhere** | Response eQTLs, chromatin accessibility and 3D chromatin structure mapped in **primary human ARTICULAR chondrocytes** from 101 donors in resting and OA-mimicking conditions; 3,782 eGenes; colocalisation with **osteoarthritis** GWAS gave 13 putative risk genes | ⭐⭐ **WRONG CARTILAGE AND WRONG TRAIT.** Articular chondrocytes are permanent cartilage; the growth plate is transient cartilage. The map was built for OA and has **not been colocalised with height**. There is still **no growth-plate eQTL or caQTL map in any species** | yes | 39788104 (+ 39605710, 42064961) | **yes** |
| J6 | ⭐ **MPRA on height variants** | Targeted queries for MPRA/massively-parallel reporter assays on height-associated variants returned **ZERO** records; the nearest work is a modular MPRA over type-2-diabetes/metabolic regions which explicitly shows MPRA results are **context- and promoter-dependent** | ⭐⭐ **No height locus has been through a massively parallel reporter assay in a chondrogenic context.** And the T2D work shows that if one were run in a generic cell line with a housekeeping promoter, the answer could be an artefact of that context | yes (nothing found) | 41952336 (PPR738884) as the method exemplar | **yes** |
| J7 | 3D genome folding and height (2025 preprint) | Akita sequence-based deep-learning predictions of 3D contact disruption applied to **9,917 height-associated regions**; only a small fraction predicted to disrupt 3D structure | ⭐ Prediction, not measurement. **No Hi-C in human growth plate or cartilage tied to height exists** — a targeted query returned nothing | yes | PPR1083538 (preprint) | **yes** |
| J8 | Fgfr3 −29 kb enhancer deletion (mouse) | A cartilage enhancer 29 kb upstream of Fgfr3; CRISPR deletion **halves Fgfr3 in that domain in otherwise wild-type mice with no adverse phenotype**, and largely normalises long-bone **and vertebral body** growth plus canal/foramen stenosis in an achondroplasia model; conserved in humans | ⭐ The wild-type arm shows "**no adverse phenotype**" — not increased length. It is a rescue result, not an elevation result | yes | 39817451 | **yes** |
| J9 | Neanderthal variants raising **SOX9** enhancer activity in craniofacial progenitors | EC1.45, an enhancer cluster 1.45 Mb upstream of SOX9 whose deletion causes Pierre Robin sequence; archaic SNVs alter its activity | Craniofacial, not longitudinal growth; iPSC-derived progenitors | yes | 41208708 (PPR915353) | **yes** |
| J10 | Jee & Baron 2018 — differential ageing of growth-plate cartilage sets skeletal proportions (rodent) | Explains why different bones stop elongating at different times | Rodent; a mechanism, not a genetic instrument | yes | 30036371 | no |
| J11 | Bone-area GWAS overlapping height (deCODE) | 12 loci for DXA hip/spine bone area that also affect height, BMD, OA or fracture; strongest MIR196A2 | DXA area is a proxy; adults only | yes | 31053729 | **yes** |
| J12 | Hoxc8 chondrocyte-specific enhancer (mouse) | Identifies a chondrocyte-specific regulatory element in a Hox gene controlling thoracolumbar skeletal identity | Mouse; developmental patterning, no height endpoint | yes | 38390956 | **yes** |
| **K. CONSTRAINT METRICS** |
| K1 | gnomAD **pLI / LOEUF / o-e** | Depletion of pLoF variation relative to expectation; the standard filter for "is this gene tolerant of inhibition?" | ⭐⭐ **A CONSTRAINT METRIC MEASURES SELECTION ON THE GENE, NOT DIRECTION ON A TRAIT.** A gene may be constrained for reasons unrelated to height. LOEUF is unreliable or undefined for short genes and for several X-linked genes | metric definitions verified; per-gene values not pulled | gnomad.broadinstitute.org | no |
| K2 | **s_het** (selection coefficient on heterozygous LoF) | A continuous, better-powered alternative to pLI | Same trait-blindness; estimation depends on an assumed demographic model. A targeted query for s_het + height returned only plant work — **no height-specific s_het analysis found** | yes (nothing found) | `UNVERIFIED` for height | **yes** |
| K3 | **MisZ** / regional missense constraint | Depletion of missense variation | ⭐ **Cannot distinguish gain-of-function from loss-of-function missense** — which is exactly the split that matters for HHIP (pLoF vs GoF missense), FBN1 (het pLoF tall vs E1297G short) and CYP19A1 (deficiency tall vs excess short) | no | `UNVERIFIED` | **yes** |
| K4 | Constraint × height burden as a drug-target filter | Whether a height gene is constrained determines whether pharmacological inhibition is likely tolerated | ⭐ The informative pattern is the **DISCORDANCE**: a gene tolerant of loss at population scale **and** taller on loss is the druggable configuration. Constraint alone cannot identify it, and neither can a burden test alone | partially | see B2, K1 | **yes** |
| **L. DATABASES AND RESOURCES — WHAT EACH WOULD RETURN FOR HEIGHT** |
| L1 | **GWAS Catalog** | 200 curated `body height` studies; 4 `sitting height ratio`; per-study ancestry breakdown; summary statistics for many | Curated **from published literature only** — preprints and unpublished biobank scans absent. Curator-assigned trait names fragment synonyms, so `leg length`, `trunk length`, `birth length` and `childhood height` all return zero | yes (live) | ebi.ac.uk/gwas/rest/api | no |
| L2 | **Open Targets Platform** | `body height` = **10,856 associated targets** with a ranked score; `Tall stature` = 85; `sitting height ratio` = 12 | ⭐⭐ **The "known drugs" field lists CLINICAL AND APPROVED AGENTS ONLY — tool compounds and chemical probes are invisible to it, so a zero there is not an absence of chemical matter.** The association score is an aggregation and **carries no direction** — it never says whether loss raises or lowers height | yes (live GraphQL) | api.platform.opentargets.org | no |
| L3 | **IMPC** | Live: **60 genes with `increased body length`**; 351 `decreased`; `long tibia` 58 vs `short tibia` 275 | ⭐⭐ **A GENE WITH NO ROW IS NOT A NULL** — it may never have been phenotyped, or phenotyped in a pipeline that did not include a length parameter. And with a ~5:1 shortening skew, **a negative result carries almost no information; only the rare positive direction does** | yes (live Solr) | ebi.ac.uk/mi/impc/solr | no |
| L4 | **MGI** | Decodes MP terms; carries non-IMPC alleles including conditionals and doubles | ⭐ **The gene symbol on an MP row is not the experiment — the ALLELE STRING is.** Tissue-restricted Cre genotypes and double knockouts are filed under a single gene symbol | not queried this session | informatics.jax.org | no |
| L5 | **HPO** | Live: Tall 180 genes, Short 1,483, both-ways 74, tall-only 106; delayed maturation 370, accelerated 69 | ⭐⭐ **DIRECTION MUST BE KEYED PER (GENE, DISEASE), NEVER PER GENE.** 41% of tall genes are also short genes because opposite conditions of one gene — aromatase deficiency vs aromatase excess at CYP19A1 — both attach to the symbol and **cancel in a set difference**. HPO also records the same condition twice, once as OMIM and once as ORPHA, with different annotations, so joining on disease ID splits one condition in two | yes (live) | ontology.jax.org/api | **yes** |
| L6 | **OMIM** | The curated Mendelian gene–phenotype map | Ascertained on **clinically recognised syndromes**. A gene whose loss makes people 2 cm taller and nothing else will never enter it | not queried | omim.org | no |
| L7 | **ClinVar** | Variant-level pathogenicity assertions | Same disease ascertainment; "benign" is assigned relative to **disease**, not to a quantitative trait — so a height-raising variant is classified benign and disappears | partly (via B4) | ncbi.nlm.nih.gov/clinvar | no |
| L8 | **gnomAD** | Allele frequencies, constraint, structural variants | ⭐ **Population reference, NOT PHENOTYPED — it cannot associate anything with height.** Ancestry composition skewed European/Latino | values not pulled | gnomad.broadinstitute.org | no |
| L9 | **DECIPHER** | CNVs and SNVs with phenotypes from developmental-disorder clinics | Ascertained on developmental disorder; height entries are almost entirely short-stature and overgrowth syndromes | not queried | deciphergenomics.org | no |
| L10 | **Monarch Initiative** | Cross-species phenotype integration (HPO ↔ MP) | ⭐ Inherits every ascertainment bias of its sources, and the mapping of human "tall stature" to mouse "increased body length" is **an assumption, not a measurement** | not queried | monarchinitiative.org | **yes** |
| L11 | **Human Cell Atlas** | Single-cell reference atlases across human tissues | ⭐ Whether any release contains a **paediatric vertebral growth plate** is `UNVERIFIED`; the axial physis is a tissue that is essentially never sampled | not queried | humancellatlas.org | **yes** |
| L12 | **UK Biobank** | ~500k; measured standing **and sitting** height; array + WES + WGS | ⭐ Volunteer cohort with **healthy-participant bias**; recruited age 40–69, so **childhood growth is unobservable**; ~94% European | yes (via A8, C7, C8, C9, D1) | ukbiobank.ac.uk | no |
| L13 | **All of Us** | Diverse US cohort with WGS | ⭐ **No dedicated All of Us height GWAS was found in this session.** It appears only as a contributing arm (45,445 in Hawkes 2024, and in the repeat-expansion work) — so its diversity advantage is largely **unspent on height** | yes | 39362880; 41501457 | **yes** |
| L14 | **FinnGen** | ~500k Finns; bottleneck-enriched deleterious alleles — in principle an excellent recessive instrument | ⭐ **Disease-endpoint-focused; height is not a core FinnGen endpoint.** Targeted search returned FinnGen height data only as an MR summary-statistic source. **The Finnish bottleneck's enrichment for homozygous deleterious variants has not been turned on height** | yes (nothing height-specific found) | finngen.fi | **yes** |
| L15 | **Biobank Japan** | ~200k Japanese; quantitative traits incl. height; public summary statistics released | Hospital-based recruitment on disease; Japanese only | yes | 34897183; 39196245 | no |
| L16 | **China Kadoorie Biobank** | ~500k Chinese; supplied the ~100k East Asian arm of the SHR GWAS (A11) | Regional sampling within China; adults only | yes | via 41861830 | no |
| L17 | **Million Veteran Program** | 635,969; 2,068 traits; the most ancestrally diverse large US biobank | See A15 — military-eligibility selection, male-skewed, older | yes | 39024449 | no |
| L18 | Regional biobanks now producing independent height loci — Taiwan, Korean KCPS2/KoGES, Qatar, SG10K | Each generating population-specific signal | Each is single-population; cross-biobank harmonisation is the limiting step | yes | 38116116; 40436827; 36131251; PPR1291806 | **yes** |
| L19 | **GTEx** | Bulk eQTL across 49+ tissues; the default resource behind every height-locus colocalisation and every drug-MR screen | ⭐⭐ **GTEx CONTAINS NO GROWTH PLATE AND NO EPIPHYSEAL CARTILAGE, and its donors are post-mortem ADULTS in whom the growth plate no longer exists.** Every functional assignment for a height variant that uses GTEx is therefore made in a tissue that cannot make bone length | yes (indirectly, via I8/D5) | gtexportal.org | no |
| L20 | **TOPMed** | WGS across diverse US cohorts; supplied 87,652 of Hawkes 2024 | Assembly of many small cohorts with heterogeneous phenotyping | yes | 39362880 | **yes** |

---

## PROSE 1 — EVERY LARGE HUMAN GENETIC INSTRUMENT FOR HEIGHT AND WHAT EACH ONE CANNOT SEE

**1. The common-variant GWAS series (Weedon 2007 → Yengo 2022).** This is the best-powered instrument in
human genetics and it terminates in an explicit saturation claim: 12,111 independent SNPs across 7,209
segments covering ~21% of the genome account for **nearly all common-SNP heritability**. What the sentence
actually says is narrower than how it is usually read. It is saturation of **common** SNP heritability, in
**Europeans**, under an **additive** model, on the **autosomes**, using **array-genotyped or imputed
biallelic** variation. Everything outside that box is untouched by the claim: rare coding variants
(section B), rare non-coding variants (C9), VNTRs and repeats (D1–D4), recessive/homozygous effects
(B5, G2), parent-of-origin effects (F1), the pseudoautosomal region and SHOX (E1), the Y chromosome (E7),
mitochondrial DNA (F2), gene–environment interaction (H10), and non-additive variance (flagged by C10).
The same 12,111-SNP result also states the portability failure directly — ~40–45% of variance in Europeans
versus ~10–24% elsewhere — and attributes it to LD and allele frequency, not to different biology.

**2. GIANT as an instrument, and the stratification lesson.** GIANT is a meta-analysis of heterogeneously
ascertained cohorts. Berg 2019 and Sohail 2019 independently showed that its residual population structure
manufactured a decade-long literature on polygenic adaptation for height that **largely disappears when
UK Biobank effect estimates are substituted**. This is the cleanest available demonstration of the brief's
premise: a design decision propagated silently into every downstream conclusion computed on those betas.
A 2026 preprint now reports converging evidence for selection using multi-ancestry plus within-family data,
so the question is reopening — but on a different instrument, which is the point.

**3. The exome burden test (Marouli 2017 → Kosmicki 2026).** Kosmicki's 826,066-exome discovery with 98%
replication in 624,567 more is the largest rare-coding instrument ever built for height, and it produces
the biggest effect sizes in the field: singleton pLoF from −17 cm (ACAN) to +11 cm (FBN1), 52× the average
common variant. **It is a heterozygous gene-burden test and therefore cannot contain a recessive gene** —
no quantity of exomes fixes a zygosity model. It is also coding-only, so it is blind to the class Hawkes
2024 shows carries effects of the same magnitude (−7 cm to +4.7 cm, including a +5 cm non-coding aggregate
near HMGA1). And it collapses variants into masks, so the **mask definition sets the answer**; the
significance threshold hides sub-threshold genes; and genes with too few living pLoF carriers are untestable
regardless of effect size. Marouli 2017 has an additional and more absolute limit: **ExomeChip is a fixed
content array** and can only test variants somebody had already put on it.

**4. The instruments that see recessive architecture — and how thin they are.** Inbreeding depression on
height is established across >35,000 people in 21 samples, so recessive variance for height demonstrably
exists; but that estimate is an aggregate and names no gene. ROH scans have produced one candidate locus
(12q21.31) at tiny sample size. The one large purpose-built instrument is the **Pakistan Genome Resource**
(173,303 people carrying homozygous LoF across 6,476 genes), and whether height was among its analysed
traits is `UNVERIFIED`. FinnGen — a bottleneck population enriched for exactly this variant class — has not
turned that advantage on height, because it is disease-endpoint-focused. **The recessive architecture of
human height is known to exist and is essentially unmapped.**

**5. Family designs.** Howe 2022's within-sibship GWAS across 178,086 siblings found within-family estimates
for height **smaller than population estimates**. Population betas therefore contain demography and indirect
genetic effects. Assortative mating compounds this: it is proven to bias both method-of-moments and
likelihood-based h² estimators, and standard population-structure corrections do not fix it. Since height is
the archetypal assorted trait, **the SNP-h² denominator against which "saturation" is declared is itself
biased.**

**6. Sex chromosomes.** SHOX is one of the largest single-gene contributors to human stature and sits in
PAR1, which most GWAS pipelines exclude by default. ~35% of SHOX-deficiency cases are non-coding enhancer
deletions that coding-only sequencing and exon-tiling MLPA both miss. Sex-chromosome dosage affects height
**non-linearly** (inverted-U across 305 aneuploidy patients). The Y-chromosome stature locus GCY was mapped
to a ~700 kb interval and **never resolved to a gene**; a claimed Y + aromatase contribution to ~4 cm of
male height failed replication.

**7. Parent-of-origin and mtDNA.** deCODE's genealogy-plus-WGS design found parent-of-origin height effects
up to |β| 10.6 cm in the imprinted IGF2–H19 and DLK1–MEG3 regions, acting **only when paternally inherited**.
A standard additive GWAS cannot detect these at all — it needs phased parental origin, which UK Biobank, MVP
and All of Us largely lack. For mitochondrial DNA the honest statement is stronger: a targeted search
returned **no mtDNA–adult-height association study at all**. mtDNA is dropped from height GWAS pipelines, so
this is an unexamined axis rather than a measured negative.

**8. Functional follow-up — and the tissue problem.** There *is* more here than an outside reader would
expect: a genome-wide CRISPR screen of chondrocyte maturation paired with height GWAS (145 genes, 90%
validating, capturing height heritability independent of computationally prioritised genes); growth-plate
open-chromatin profiling enriched at height loci; and a regression showing that **resting/round-cell-layer
expression specificity is significantly associated with height GWAS signal (p = 8.5e-9)**. But all three are
**mouse tissue or in-vitro culture**. On the human side: **no growth-plate eQTL map, no growth-plate caQTL
map, no cartilage Hi-C tied to height, and no MPRA on any height variant.** The one high-quality human
chondrocyte resource with eQTLs, chromatin accessibility and 3D structure was built in **articular**
chondrocytes for **osteoarthritis** and has not been colocalised with height. GTEx — the default eQTL source
for every height colocalisation and for the genome-wide drug-MR screen — contains no growth plate and no
epiphyseal cartilage, and its donors are adults in whom the growth plate no longer exists.

**9. Constraint metrics.** pLI, LOEUF, s_het and MisZ all measure **selection on the gene, not direction on
the trait**. MisZ in particular cannot separate gain- from loss-of-function missense, which is exactly the
distinction that matters for the genes where it matters most (FBN1 het pLoF tall vs FBN1 E1297G short;
CYP19A1 deficiency tall vs excess short). No height-specific s_het analysis was found.

**10. The trait definition itself.** Standing height is the measured phenotype in essentially every
instrument. **Sitting height ratio has 4 curated GWAS in the entire GWAS Catalog against 200 for height, and
`leg length`, `trunk length`, `birth length` and `childhood height` return zero studies under those trait
names.** Open Targets lists 12 targets for sitting height ratio against 10,856 for body height. And the one
large SHR study states that fine-mapped SHR signals are **often distinct** from height signals — meaning a
compartment coordinate derived from ratio-selected variants is an allele property, not a gene property.

---

## PROSE 2 — GENES WHOSE LOSS-OF-FUNCTION INCREASES HUMAN HEIGHT, FROM EVERY INSTRUMENT, NOT JUST ONE

Assembled below from **eight independent instruments**. Direction is stated per instrument, because most
resources do not carry one.

**(i) Rare coding burden — Kosmicki 2026 (826,066 + 624,567 exomes).** Singleton pLoF effects run from
**−17 cm (ACAN) to +11 cm (FBN1)**. The abstract explicitly names **TET1, DTL and IGF2BP2** as having effects
at least as large as established Mendelian height genes **while lacking any documented stature or
skeletal-growth syndrome — and states this is particularly true for genes in which rare variants associate
with INCREASED height.** That sentence is the single most important line in this domain: it says the
height-increasing direction is systematically under-documented in clinical genetics, which is exactly what
an 8.2:1 short:tall HPO ratio would predict.

**(ii) Rare coding, ExomeChip — Marouli 2017.** **STC2** is the worked case: rare height-**increasing**
alleles giving +1–2 cm per allele, shown functionally to **compromise STC2's proteolytic inhibition of
PAPP-A**, increasing IGFBP-4 cleavage and raising IGF bioavailability. Loss of an inhibitor → taller, with
mechanism. Also named at this scale: IHH, AR, CRISPLD2 (direction per-variant, not stated as LoF here).

**(iii) Rare NON-coding — Hawkes 2024 (333,100 WGS).** 29 conditionally independent variants with effects
**−7 cm to +4.7 cm**; a non-coding aggregate **proximal to HMGA1 associated with +5 cm**; conserved variants
in **MIR497HG**. This is the height-increasing direction arriving from a variant class no exome study can see.

**(iv) Recessive-disease variants in heterozygotes — Barton/Mukamel 2022.** A **POR** missense implicated in
Antley-Bixler syndrome associates with **+1.76 cm (SE 0.27)** in heterozygous carriers of ~500k UK Biobank
participants. POR is the obligate electron donor for microsomal P450s including aromatase.

**(v) Parent-of-origin — deCODE 2016.** Effects up to **|β| 10.6 cm** at imprinted **IGF2–H19** and
**DLK1–MEG3**, with the minor alleles reducing height **only when paternally inherited** — i.e. the
maternally inherited copy of the same allele is neutral. **TET1** also appears here, on birth length,
independently of (i).

**(vi) Human phenotype ontology, tall-only set (106 genes, pulled live).** Directional after removing the 74
both-ways genes: **NPR3, SPIN4, CHD8, EZH2, SUZ12, EED, ESR1, CBS, POR, AR, GPR101, MC2R, MRAP, STAR, NNT,
TXNRD2, LOX, PLOD1, FBN2, EFEMP1, MFAP5, THSD4, ZNF469, TGFBR1, TGFBR2, SMAD3, TGFB1, TGFB2, DICER1, MEN1,
CDKN1B, CDKN2B, GPC3, HERC1, DIS3L2, PDGFRB, PIGG, NELFA, KCNQ1, AMOTL1, HEY2, MYH11, MYLK, CHST14, DSE,
FKBP14, FIBP, LRP4, MAT2A, LHCGR, HPGD, CCND1** and others. ⚠ **HPO carries no direction of molecular
effect** — some of these are gain-of-function alleles (PDGFRB, AKT1-adjacent, GPR101 duplication), so this
list is "tall-associated genes", not "LoF→tall genes", and must be filtered per allele.

**(vii) Clinical tall-stature cohorts — the mirror of the short-stature literature, and it barely exists.**
Familial tall stature, 786-gene panel + karyotype: **11/34 (32.4%) solved — SUZ12 ×2, FGFR3, CHD8, GPC3,
PPP2R5D**, and 10 of the 34 had no syndromic signs at all. Non-familial tall stature: only **6/55 (11%)**
solved and **four of the six were sex-chromosome aneuploidies**. Brazilian series: **14/42 (33.3%)** solved
(FBN1 ×3, NSD1 ×2, NFIX, SUZ12, CHD8, MC4R, SHOX trisomy, Beckwith-Wiedemann ×2) but only **1 of 12
non-syndromic** patients. Syndromic tall stature exome: FBN1, PTEN, NSD1, SUZ12, CDH8, DEPDC5 plus four
novel candidates. Oligogenic non-syndromic FTS: **CEP104, CROCC, NEK1, TOM1L2, TSTD2 — three of five
ciliary.** Isolated tall stature pedigree: **IFT140, NAV2, SCAF11**. **SHOX duplication in 3.7% of girls
with idiopathic tall stature and normal karyotype.**

**(viii) Mouse — IMPC, pulled live.** **60 genes whose knockout significantly increases body length**:
*4931422A03Rik, 6430503K07Rik, Acat2, Acbd5, Acot8, Adprs, **Agtr2**, Ankrd9, Arhgef4, Arpc2, Commd3,
Cpgi5563, **Dis3l2**, **Drg2**, Ebf4, **Ecrg4**, Etl4, **Fgfr4**, Gpha2, **Hltf**, Hpdl, **Insig2**,
**Jarid2**, Ldha, **Limk2**, **Lingo2**, Lrrc3, **Lta4h**, Lyrm2, Lyz3, M1ap, **Med28**, Mfsd2b, **Mob1a**,
Mrps17, Ncaph, Ndfip2, Nhp2, **Nr1d1**, **Pik3cg**, Pnpla1, Ppp1r1a, Prss53, Rad18, Rnd2, Rnf10, Rnf31,
Rtbdn, Sel1l2, Sergef, Serpinb7, Snx11, Spata20, Spn, Sult2a8, Trim8, Trpm6, Txndc16, Uso1, **Zhx3**.*
Against 351 decreased-body-length calls — so the **positive direction is ~5× rarer and correspondingly more
informative**. Note Dis3l2 appears in both this list and the human HPO tall-only list, an unusual
cross-species concordance.

**Two cautions that apply to the whole section.** First, **direction is not monotone across allele classes
within a gene**: FBN1 heterozygous pLoF is +11 cm in the burden test while the Peruvian FBN1 E1297G missense
is **−2.2 cm per copy**. Second, **41% of HPO's tall genes are also short genes**, and the mechanism is
CYP19A1-shaped — aromatase deficiency is tall, aromatase excess is short, both annotate to the same symbol,
and a gene-level set operation cancels them. Direction must be keyed per (gene, disease, allele class), never
per gene.

---

## PROSE 2b — THE GENE FAMILIES THE INSTRUMENTS KEEP RETURNING, AND WHICH INSTRUMENT RETURNED EACH

Recorded because the *recurrence* is the finding — the same families reappear from array GWAS, exome burden,
mouse knockout, clinical cohorts and ontology, which are largely independent instruments.

| family | genes named by the instruments queried here | instrument(s) |
|---|---|---|
| **Hedgehog** | IHH, HHIP, PTCH1, GLI1, GLI3, KIF7, SCUBE3, (archaic GLI3 R1537C) | Weedon 2008 (A3), Marouli 2017 (B1), Open Targets, HPO, G17 |
| **Extracellular matrix / microfibril / proteoglycan** | ACAN, FBN1, FBN2, EFEMP1, ADAMTSL3, ADAMTS10, ADAMTS17, ADAMTS3, COL2A1, COL1A1, COL1A2, COL11A1, HSPG2, ELN, MFAP5, THSD4, ZNF469, LOX, PLOD1, CHST14, DSE, CRISPLD1/2, SERPINH1 | A3, A7 (chondroitin sulfate + GAG pathways), B1, B2, Open Targets, HPO |
| **IGF / GH axis** | IGF1R, IRS1, GHRH, GHR (incl. the GHRd3 deletion and the Neanderthal allele), STC2, PAPP-A (via STC2 mechanism), IGF2, IGF2BP2, IGFALS-adjacent | B1 (STC2→PAPP-A→IGFBP-4 mechanism), B2, D9, G16, Open Targets |
| **Chromatin / epigenetic writers and readers** | EZH2, SUZ12, EED, NSD1, DNMT3A, CHD8, SETD2-adjacent, KMT2C, EHMT1, KDM2B, KDM6B, SPIN4, JARID2 (mouse), TET1 | B2 (TET1), B7–B10 (SUZ12, CHD8, NSD1), HPO tall list, IMPC (Jarid2) |
| **TGF-β / BMP** | TGFBR1, TGFBR2, SMAD3, TGFB1, TGFB2, BMP4, SKI, PMEPA1, LTBP-adjacent | HPO tall list, Open Targets Tall stature, B9 (TGFBR2/Loeys-Dietz) |
| **CNP / natriuretic** | NPR3, NPPC-adjacent | HPO tall-only, Open Targets body height (NPR3 rank 4) |
| **Chondrocyte transcription factors** | SOX9, RUNX2-adjacent, ZBTB38, ZFAT, LCORL, TBX2, TBX4 | A4 (ZBTB38), Open Targets (ZFAT rank 1, LCORL), A11/Open Targets SHR (TBX2, TBX4) |
| **Cell cycle / proliferation** | CDK6, CDKN1B, CDKN2B, CCND1, DTL, HMGA1, HMGA2, MED28 (mouse), NCAPH (mouse) | A1/A3 (HMGA2), B2 (DTL), C9 (HMGA1), HPO, IMPC |
| **Nuclear hormone receptors / steroidogenesis** | ESR1, AR, CYP19A1, POR, MC2R, MRAP, STAR, NNT, TXNRD2, LHCGR | B1 (AR), B4 (POR), HPO tall-only, HPO both-ways (CYP19A1) |
| **Cilium / intraflagellar transport** | CEP104, CROCC, NEK1, IFT140, DYNC2LI1-adjacent | B11, B12 — a family that appears **only** in the small tall-stature pedigree literature and in no large instrument |
| **let-7 / microRNA** | LIN28B, MIR497HG, MIR196A2 | A2 (let-7 targets), A18 (LIN28B), C9 (MIR497HG), J11 (MIR196A2) |
| **Mechanosensation / channels** | PIEZO1, TRPM6 (mouse), KCNQ1 | Open Targets (PIEZO1 rank 8), IMPC, HPO |

⚠ **This table is a record of what the instruments name, not a claim that any of these is a lever.** Direction
is absent for most rows, and several families appear only because they were the *ascertainment* of a
clinical cohort.

---

## PROSE 3 — WHAT A NON-EUROPEAN OR NON-BIOBANK COHORT WOULD ADD

**The measured size of the gap.** Of 200 GWAS Catalog `body height` studies, 103 carry a European ancestry
tag; East Asian 59; Hispanic/Latin American 32; African-unspecified 23; African-American 20; South Asian 13;
Native American 5; Greater Middle Eastern 3; Oceanian 3; Central Asian 2; Sub-Saharan African 1; SE Asian 1.
UK Biobank's WGS release is 457,377 non-Finnish European against 9,091 African and 9,388 South Asian — a
>45:1 imbalance. Height PGS trained in Europeans recover 40–45% of variance in Europeans and ~10–24%
elsewhere.

**What non-European cohorts have already added, concretely.**
- **Population-private large-effect alleles that no European study could have found.** The Peruvian FBN1
  E1297G is the flagship: 4.7% frequency, **−2.2 cm per copy and −4.4 cm homozygous**, reported as the largest
  known effect for a common height variant. It is essentially absent outside Native American ancestry.
- **Loci that only exist when non-Europeans are included.** Million Veteran Program: of 13,672 genomic risk
  loci across 2,068 traits, **1,608 were significant only after including non-European participants**, and
  one third of fine-mapped causal signals came from non-European participants.
- **Power from meta-analysis across East Asian biobanks.** KCPS2 + KoGES + Biobank Japan + Taiwan Biobank +
  UK Biobank identified **4,588 loci not significant in any contributing GWAS**; KCPS2 alone contributed 301
  previously unreported loci; the Taiwan Biobank study added hundreds across 36 traits.
- **Fine-mapping resolution.** Different LD structures break European haplotype blocks. Bartell 2026 used
  UK Biobank plus China Kadoorie to identify **36 credible sets with heterogeneous effects across
  ancestries** for skeletal proportion specifically.
- **Breaking ascertainment circularity.** The Sardinian selection re-analysis deliberately used
  **Biobank-Japan-ascertained** height loci to avoid European-discovery circularity — a design move only
  possible because a large non-European instrument exists.

**What a non-biobank cohort structure would add, and this is the larger prize.**
- **Recessive architecture.** Inbreeding depression proves recessive variance for height exists across
  >35,000 people, and the het burden test that produced the 207 genes cannot contain a single recessive gene.
  The **Pakistan Genome Resource** (173,303 people, homozygous LoF in 6,476 genes) is purpose-built for this;
  whether height was among its analysed traits is `UNVERIFIED`, and that is the single cheapest question in
  this domain. **FinnGen's bottleneck enrichment is a second such instrument and has not been pointed at
  height at all.** Consanguineous pedigrees remain the classical route and are essentially untapped at scale.
- **Parent-of-origin effects.** These require **genealogy or trios**, not sample size. Iceland has both, which
  is why deCODE is the only source of the |β| up to 10.6 cm imprinted signals. No volunteer biobank can
  replicate that design however large it grows.
- **Childhood and pubertal growth.** UK Biobank recruited at ages 40–69, so growth trajectory is
  unobservable. Every longitudinal instrument here — NFBC1966, the trans-ancestral pubertal-growth GWAS, the
  Southwestern American Indian Preece-Baines cohort — is small, and that is why the genetics of *growth* is
  far weaker than the genetics of *attained height*.
- **Family-based cohorts.** Within-sibship analysis showed population height betas are inflated by
  demography and indirect genetic effects. The sibling-pair resources that fix this (178,086 in Howe 2022;
  ~500,000 in a 2025 preprint) are assembled from many cohorts, not from any single biobank.
- **Clinical tall-stature cohorts.** The largest anywhere in this enumeration is 55 children. Against ~1,483
  HPO-annotated short-stature genes there are 180 tall. **A tall-stature cohort of even a few thousand would
  be, per participant, the highest-yield instrument in this entire domain for the height-INCREASING
  direction**, which is the direction Kosmicki 2026 explicitly identifies as under-documented.
- **All of Us** is the most diverse US WGS cohort and appears in this enumeration only as a contributing arm
  (45,445 of Hawkes 2024, plus repeat-expansion work). **No dedicated All of Us height GWAS was found.** Its
  diversity advantage is currently largely unspent on this trait.

**One caveat against over-reading ancestry differences.** Two independent analyses report broadly homogeneous
additive genetic architecture for height across sexes and continental populations, and Yengo 2022 attributes
the PGS portability failure to LD and allele frequency rather than to different causal biology. So the
argument for diverse cohorts here is **power, resolution, and access to variant classes and family
structures** — not a claim that height works differently in different populations.

---

## WHAT I COULD NOT VERIFY

1. **Whether height was analysed in the Pakistan Genome Resource.** The abstract describes homozygous LoF in
   6,476 genes and biomarker associations but does not name height. `UNVERIFIED` — and it is the highest-value
   open question in this enumeration.
2. **Kosmicki 2026 is a PREPRINT (PPR1258977).** Peer-reviewed publication status, final gene count and final
   effect sizes are `UNVERIFIED`. I have quoted only what its own abstract states.
3. **Per-gene effect sizes from Kosmicki's 207.** I did not access Supplementary Table 6 or any per-gene
   burden table. Only ACAN (−17 cm), FBN1 (+11 cm) and the named TET1/DTL/IGF2BP2 are from the abstract; every
   other per-gene centimetre figure is `UNVERIFIED` by me.
4. **Per-gene constraint values (pLI, LOEUF, s_het, MisZ) for any height gene.** Metric definitions verified;
   values not pulled. No height-specific s_het analysis was found at all.
5. **The SHOX sex-biased monoallelic-expression result (PPR387405)** is a preprint; peer-reviewed status
   `UNVERIFIED`.
6. **Whether the Human Cell Atlas contains any paediatric vertebral growth plate.** Not queried.
7. **MGI, OMIM, ClinVar, DECIPHER, Monarch, gnomAD** were characterised from their documented design, not
   queried directly this session. Their per-gene height content is `UNVERIFIED`.
8. **Whether any 2024–2026 All of Us or FinnGen height GWAS exists** that my queries missed. I found none;
   absence of evidence from two query routes is weak.
9. **Effect direction for the 106 HPO tall-only genes.** HPO records phenotype association, not molecular
   direction — several are certainly gain-of-function. The list must not be read as "LoF → tall".
10. **Whether the 60 IMPC increased-body-length genes are single-gene, non-conditional knockouts.** I pulled
    marker symbol, zygosity, p-value and effect size but **did not inspect the allele string**, so
    tissue-restricted Cre or double-knockout genotypes may be present in that list.
11. **Full texts.** Everything above is from abstracts, structured summaries and API responses. No paywalled
    full text was read except the portions of PubMed abstract records quoted.
12. **Numbers I deliberately did not carry forward:** any claim I could only find in a review, and any
    per-variant centimetre figure not stated in the source abstract.
