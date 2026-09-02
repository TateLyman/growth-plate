# Paywalled / hard-to-reach sources needed, by priority

Priority key: **P1** blocks a whole subsystem · **P2** refines a number · **P3** nice-to-have

Each row states the SPECIFIC item needed (figure, table, panel), not just the paper.

> **A queue entry is an unmeasured parameter with a known address, and it should be ranked
> by what it blocks — not filed as a bibliographic nicety.** Row L1-2 sat here as P1 while
> three nodes recorded its numbers as "behind a paywall" and the flow model built a
> DECLARED_SPAN to stand in for them. The span was 4.0-73.2 µm wide, the closure prediction
> derived under it was wrong by 9.6 %, and the paper had contained the right answer since
> 1985. **Rows below that block a model parameter are marked ⛔ and take precedence over
> rows that refine a number already held.** (`audit/corrections.md` CORR-006.)

| # | Pri | Citation | DOI/PMID | What I need from it | Blocks |
|---|-----|----------|----------|---------------------|--------|
| 1 | P2 | Yengo L et al. A saturated map of common genetic variants associated with human height. Nature 2022 | 10.1038/s41586-022-05275-y | Supplementary tables: the **distribution** of the 7,209 segment sizes (to settle whether ~90 kb is the mean or the median — the Nature text and the bioRxiv preprint disagree, logged as contradiction c001). Paper itself is open access; it is the supplementary table I need parsed. | `height_gwas` segment-size row |
| 2 | P1 | Chu NTL et al. A transcriptional atlas of the pubertal human growth plate reveals two populations of stem cells and direct effect of growth hormone. Sci Transl Med 2026 | PMID 41984930 / 10.1126/scitranslmed.adw3590 | The figure showing PTHLH expression across the human resting-zone clusters, plus the marker list defining the "root" vs second stem-like population, plus n (number of human donors, ages, sex, anatomical site) and the Prrx1 clonal tracing clone-size data. Needed to grade the claim that the human resting-zone stem cell is PTHLH-negative, which contradicts the entire murine PTHrP literature (contradiction C-L2-05). Only the abstract was accessible. | `prrx1_root_stem_cell`, `human_resting_zone_chondrocyte`, `pthrp_positive_resting_chondrocyte`, gaps g_l2stem_001 and g_l2stem_009 |
| 3 | P2 | Newton PT et al. A radical switch in clonality reveals a stem cell niche in the epiphyseal growth plate. Nature 2019;567:234-238 | PMID 30814736 / 10.1038/s41586-019-0989-6 | Figures 1-3 and Extended Data: the actual clonal kinetics — clone-size distributions before and after the switch, the postnatal day at which monoclonality is reached, the fraction of columns that are monoclonal at each age, and the exact relationship asserted to the SOC (is SOC stage scored per animal, or only cited as coincident?). No PMC deposit; abstract only. This determines whether the SOC-triggers-stemness claim is even correlational at the level of individual bones. | `monoclonal_column_formation`, `soc_formation_triggers_stemness`, `clonal_exhaustion`, gap g_l2stem_003 |
| 4 | P2 | Zhou BO et al. Leptin-receptor-expressing mesenchymal stromal cells... Cell Stem Cell 2014;15:154-168 | PMID 24953181 / 10.1016/j.stem.2014.06.008 | Quantitative panels behind the 0.3% / 10% CFU-F / 94% figures (n, SD, mouse ages) and the fate-mapping timecourse showing the absence of cartilage contribution. Abstract-level numbers only were used. | `lepr_positive_stromal_cell` quantitative rows |
| L3-1 | P1 | Nakao K et al. The local CNP/GC-B system in growth plate is responsible for physiological endochondral bone growth. Sci Rep 2015;5:10554 | PMID 26014585 | The **n per genotype and the dispersion** behind Fig 2d/2e and Fig 6d/6e zonal thickness percentages (hypertrophic layer 34.6% and 23.0% of control; non-hypertrophic 76.7% and 71.1%). Full text was read and the percentages are stated in the Results, but sample sizes are not given in the text and the error bars are only in the figures. These four numbers are the atlas's entire quantitative basis for the zonal partition of the CNP effect. | `cnp_protein`, `npr2_receptor` quantitative rows; gap g_l3core_003 |
| L3-2 | P2 | Agoston H et al. C-type natriuretic peptide regulates endochondral bone growth through p38 MAP kinase-dependent and -independent pathways. BMC Dev Biol 2007;7:18 | PMID 17374144 | The **zonal microarray panel**: relative NPR2/GC-B expression in resting vs proliferative vs hypertrophic zones, and the PKG-I / PKG-II fold-differences between zones, with n and statistics. This is the evidence that the CNP receptor is uniform while the effector is zoned — contradiction C-L3-03, which decides whether the zonal partition of CNP action is set at the receptor or downstream. Abstract read only. | `npr2_receptor`, `pkg2_kinase`, contradiction C-L3-03 |
| L3-3 | P2 | Olney RC et al. Heterozygous mutations in NPR2 are associated with short stature. J Clin Endocrinol Metab 2006;91:1229-32 | PMID 16384845 | Table with **per-individual height z-scores, ages and sexes** for the 16 carriers and 23 non-carriers, and the body-proportion measurements (sitting height / subischial leg length ratios). Needed to state the heterozygous NPR2 effect size as a difference with a CI rather than as two means read from the abstract. | `npr2_receptor` quantitative rows; gap g_l3core_011 |
| L3-4 | P2 | Wagner BM et al. Prevention of guanylyl cyclase-B dephosphorylation rescues achondroplastic dwarfism. JCI Insight 2021;6:e147589 | PMID 33784257 | The **absolute long bone lengths and hypertrophic zone areas per genotype and sex** (Figs 2-5), and the sex-dependence (male-only effect at 2 weeks in FGFR3-G380R, female-only in GC-B 7E/7E). Currently recorded only as a directional rescue. This is the single strongest quantitative link between the FGFR3 and NPR2 arms. | `fgfr3_npr2_crosstalk` quantitative row |
| L3-5 | P3 | Bartels CF et al. Mutations in the transmembrane natriuretic peptide receptor NPR-B impair skeletal growth and cause acromesomelic dysplasia, type Maroteaux. Am J Hum Genet 2004;75:27-34 | PMID 15146390 | The **obligate-carrier height data**: how many carriers, what the mean deficit versus matched controls was, and the matching procedure. The abstract states only that carriers "have heights that are below the mean for matched controls" with no effect size. | `npr2_receptor` quantitative rows; gap g_l3core_011 |
| 5 | P3 | Yang L, Tsang KY et al. Hypertrophic chondrocytes can become osteoblasts and osteocytes in endochondral bone formation. PNAS 2014;111:12097-12102 | PMID 25092332 / 10.1073/pnas.1302703111 | Quantification of the labelled osteoblast/osteocyte fraction in this system, to compare against the ~60% figure from the independent Col10a1-Cre study. PMC deposit contains front matter only. | `hypertrophic_chondrocyte_survival`, `chondrocyte_to_osteoblast_transdifferentiation` |
| L1-1 | P1 | Brighton CT, Heppenstall RB. Oxygen tension in zones of the epiphyseal plate, the metaphysis and diaphysis. An in vitro and in vivo study in rats and rabbits. J Bone Joint Surg Am 1971;53:719-728 | PMID 5580029 / 10.2106/00004623-197153040-00011 | The **actual pO2 values in mmHg per zone** (resting, proliferative, hypertrophic, metaphysis, diaphysis) with species, n and in vivo versus in vitro condition. No abstract is indexed anywhere; this single 1971 paper is the source of essentially every "the growth plate is hypoxic" statement in the field and the atlas currently cannot state a single number from it. | `oxygen_gradient_growth_plate`, `nutrient_diffusion_growth_plate`, gap g_l1arch_007 |
| ~~L1-2~~ | **CLOSED 2026-08-06** | ~~Thurston MN, Kember NF. In vitro thymidine labelling in human and porcine growth plates. Cell Tissue Kinet 1985;18:575-582~~ | PMID 3864550 | **OBTAINED** (user-supplied full-text PDF). All requested numbers entered: labelling index 4.4 / 3.4 / 4.0 % human and 4.0-10.6 % pig; proliferation zone 28 / 13 cells human and 30-36 pig; hypertrophic cell height **20.5 / 26 um human** and 22-35 um pig; inert zone 700-1000 um. This row was **P1 and it was right to be**: the height it held closed the largest single source of uncertainty in the flow model (45 % -> 0 %) and falsified a written prediction by 9.6 %. See `audit/corrections.md` CORR-006. | ~~closed~~ |
| L1-3 | P1 | Heinrichs C, Munson PJ, Counts DR, Cutler GB Jr, Baron J. Patterns of human growth. Science 1995;268:442-447 | PMID 7716552 / 10.1126/science.7716552 | The **entire content**: what was measured, in which species/subjects, with what precision, and the statistical argument against saltation and stasis. PubMed and Europe PMC hold no abstract for this record. It is one of the two primary counterweights to Lampl 1992 and the atlas currently cites it without being able to state what it showed. | `saltation_stasis_growth`, gap g_l1arch_005 |
| L1-4 | P2 | Byers S, Moore AJ, Byard RW, Fazzalari NL. Quantitative histomorphometric analysis of the human growth plate from birth to adolescence. Bone 2000;27:495-501 | PMID 11033444 / 10.1016/s8756-3282(00)00357-4 | ⛔ **9 %** — `N_p_cells`. Human zonal dimensions in um; the model's cells-per-column span is still DECLARED at +/-50 % because no dispersion exists anywhere. The **absolute values in um** for proliferative zone height, hypertrophic zone height, primary spongiosa height, cartilage septal thickness and septal number at each age band, with n per band. The abstract gives only directions of change. These are the best available human zonal dimensions. | `growth_plate_height`, `proliferative_zone`, `hypertrophic_zone`, `primary_spongiosa`, `column_density` |
| ~~L1-5~~ | P2 | Wilsman NJ, Farnum CE, Leiferman EM, Fry M, Barreto C. Differential growth by growth plates as a function of multiple parameters of chondrocytic kinetics. J Orthop Res 1996;14:927-936 | PMID 8982136 / 10.1002/jor.1100140613 | **CLOSED 2026-08-06 — OBTAINED (user-supplied full text).** Per-plate table recovered for all four plates, and the decisive correction with it: the **cell** share of junction volume (0.504–0.685 = division + enlargement) is the right comparator for a measured cell height, not the 0.44–0.59 enlargement share. The atlas — and `flow_model.py` — had been using the wrong one. Also: growth fraction 0.89–0.99 measured to plateau. See CORR-008. | ~~closed~~ |
| ~~L1-6~~ | P2 | Kember NF, Sissons HA. Quantitative histology of the human growth plate. J Bone Joint Surg Br 1976;58-B:426-435 | PMID 1018028 / 10.1302/0301-620x.58b4.1018028 | **CLOSED 2026-08-06 — OBTAINED (user-supplied full text).** It answered the crux and overturned CORR-006: Kember did NOT assume a cell height, he **measured** it at **33 ± 5 µm** (12 subjects, 29–38 µm, celloidin, 13 % shrinkage corrected) and states the derivation in full. Also recovered: N_p = 24 is **not a count** — the measured quantity is 36, split two-thirds by a **rabbit** ratio — and an author-stated 16-day lower bound. Creates contradiction C-L1-07 against thurston1985's 20.5 µm. See CORR-008. | ~~closed~~ |
| L7-1 | P1 | Carani C, Qin K, Simoni M, Faustini-Fustini M, Serpente S, Boyd J, Korach KS, Simpson ER. Effect of testosterone and estradiol in a man with aromatase deficiency. N Engl J Med 1997;337:91-95 | PMID 9211678 / 10.1056/NEJM199707103370204 | The **actual case numbers**: height in cm at presentation and after treatment, bone age in years before and after transdermal estradiol, the estradiol dose and duration, and the radiographic description of epiphyseal closure. Europe PMC holds no abstract for this record at all, so the atlas currently states this result only via a review restatement (rochira2015). This is the single interventional demonstration that estradiol, not testosterone, closes the human growth plate. | `estrogen_driven_fusion` (marked `pending_source`), edges e00001, e00003 |
| L7-2 | P2 | Bilezikian JP, Morishima A, Bell J, Grumbach MM. Increased bone mass as a result of estrogen therapy in a man with aromatase deficiency. N Engl J Med 1998;339:599-603 | PMID 9718379 / 10.1056/NEJM199808273390905 | Serial BMD values with dates and the estradiol dose, plus whether epiphyseal closure was documented radiographically in this patient (the Morishima 1995 sib). No abstract in Europe PMC. Needed to state the bone-mass response to estrogen replacement in aromatase deficiency as numbers rather than a direction. | `estrogen_driven_fusion` quantitative rows |
| L7-3 | P2 | The primary behind the obese-versus-lean Tanner G5 estradiol/bone-age comparison cited as ref 17 in Rochira V, Kara E, Carani C, Int J Endocrinol 2015;2015:165215 | via PMC4383300 reference list | The primary study reporting median serum E2 34.8 pg/mL (25.6-41.1) with bone age ~18 y and fused epiphyses in obese boys versus 15.7 pg/mL (13.2-21.0) with bone age ~16 y and unfused epiphyses in lean boys, at genital Tanner stage 5, with n and the E2 assay used (immunoassay vs LC-MS/MS changes the threshold materially). Currently recorded from the review with `value_unverified: true`. | `estradiol_threshold_fusion` quantitative rows |
| L7-4 | P2 | Khamis HJ, Roche AF. Predicting adult stature without using skeletal age: the Khamis-Roche method. Pediatrics 1994;94:504-507 | PMID 7936860 | The **numeric prediction errors** for Khamis-Roche versus RWT, by sex and age, behind the phrase "only slightly larger". This single comparison is the atlas's best evidence on how much bone age actually contributes to remaining-growth prediction, and it is currently stated only qualitatively. | `remaining_growth_prediction`, `fels_method`, gap g_l7fuse_007 |
| L7-5 | P3 | Roche AF, Chumlea WC, Thissen D. Assessing the Skeletal Maturity of the Hand-Wrist: Fels Method. Charles C Thomas, 1988 | book; no PMID | The per-case standard error of the Fels skeletal age estimate, and any published inter-rater/intra-rater error in years. No journal primary reporting Fels reader error was located in this sweep. | `fels_method` (confidence currently D for this reason), gap g_l7fuse_008 |

| P2 | Meng L et al. Clinical, Molecular Characteristics, and Genotype-Phenotype Relationships of Metaphyseal Chondrodysplasia Type Schmid. 2025. PMID 41454937 | - | Need Table 1: adult/final height in cm and height SDS for COL10A1 heterozygotes, to quantify how mild Schmid MCD actually is (L5 collagen_type_x, schmid comparison) | l5matrix |
| P2 | Sergerie K et al. Mechanical properties of the porcine growth plate and its three zones from unconfined compression tests. J Biomech 2009. PMID 19185303 | 10.1016/j.jbiomech.2008.12.002 | Need Table 2: absolute values of E1, E3, k1, nu21, nu31 per zone in MPa - abstract gives only fold-differences (L5 zonal_stiffness_gradient) | l5matrix |
| P3 | Eyre DR. Collagen cross-linking in human bone and articular cartilage. Biochem J 1988. PMID 3415669 | 10.1042/bj2520495 | Need Table: hydroxylysylpyridinoline residues per collagen molecule in human cartilage by age - full text body not retrievable via Europe PMC (L5 collagen_crosslinking) | l5matrix |
| P2 | Mendler M et al. Cartilage contains mixed fibrils of collagen types II, IX, and XI. J Cell Biol 1989. PMID 2463256 | 10.1083/jcb.108.1.191 | Need the biochemical quantitation in Results giving the II:IX:XI mass ratio; PMC record is reference-list only, body is scanned PDF (L5 collagen_fibril_stoichiometry) | l5matrix |

| P2 | Sasagawa S et al. SIK3 is essential for chondrocyte hypertrophy during skeletal development in mice. Development 2012;139:1153-63. PMID 22318228 | 10.1242/dev.072652 | Need the figure panels quantifying HDAC4 nuclear versus cytoplasmic distribution in wild-type versus Sik3-null chondrocytes (fraction of cells, n per genotype), and the age at which SIK3-overexpressing growth plates close. Abstract only was read; the atlas currently states the localisation switch qualitatively (L3 salt_inducible_kinase3, hdac4_protein, gap g_l3rest_013) | l3rest |
| P2 | Vega RB et al. Histone deacetylase 4 controls chondrocyte hypertrophy during skeletogenesis. Cell 2004;119:555-66. PMID 15537544 | 10.1016/j.cell.2004.10.024 | Need the zonal quantification behind the Hdac4-null premature-hypertrophy phenotype: hypertrophic zone height and Col10a1 domain length in mutant versus control, with n, and the HDAC4-Runx2 binding stoichiometry. Abstract only was read (L3 hdac4_protein, runx2_tf) | l3rest |
| P2 | Brighton CT, Heppenstall RB. J Bone Joint Surg Am 1971;53:719-728. PMID 5580029 — SEE ROW L1-1 | 10.2106/00004623-197153040-00011 | Same request as L1-1 (per-zone pO2 in mmHg with species and n). Additionally blocks L3: it is the only direct oxygen measurement anywhere in the growth plate literature and is the nearest evidence for gap g_l3rest_011 (has human growth plate oxygen tension ever been measured). `hypoxic_gradient_signaling` is marked pending_source on this reference | l3rest |

| P1 | Merker A, Neumeyer L, Hertel NT, et al. Growth in achondroplasia: Development of height, weight, head circumference, and body mass index in a European cohort. Am J Med Genet A 2018;176:1723-1734. PMID 30070757 | 10.1002/ajmg.a.38853 | Need the height reference TABLES: adult height in cm for men and women with the SD around the mean and n contributing at the terminal age, plus the height-SDS trajectory over the first 2 years. The abstract gives only the point values 132 cm and 124 cm with no dispersion, so the atlas cannot state an SD for the single most-cited number in the FGFR3 series (L11 achondroplasia; gap g_l11path_001) | l11path |
| P1 | Horton WA, Rotter JI, Rimoin DL, Scott CI, Hall JG. Standard growth curves for achondroplasia. J Pediatr 1978;93:435-438. PMID 690757 | 10.1016/s0022-3476(78)81152-4 | Need the actual curves and their tabulated percentiles: adult height by sex, growth velocity by age, and upper/lower segment values, with the n contributing at each age band out of the 400 individuals. This is the founding achondroplasia auxology paper and the atlas currently holds only the abstract's summary sentence (L11 achondroplasia) | l11path |
| P1 | Woods KA, Camacho-Hübner C, Savage MO, Clark AJL. Intrauterine growth retardation and postnatal growth failure associated with deletion of the insulin-like growth factor I gene. N Engl J Med 1996;335:1363-1367. PMID 8857020 | 10.1056/NEJM199611073351904 | Need the case NUMBERS: birth weight and length SDS, height in cm and SDS at presentation, head circumference SDS, serum GH profile values and the exact extent of the IGF1 deletion. Europe PMC holds no abstract for this record. This is the only human homozygous IGF1 null and the atlas can currently state none of its measurements (L11 igf1_deficiency_human; gap g_l11path_008) | l11path |
| P2 | Kim HY, Lee YA, Shin CH, Cho TJ, Ko JM. Clinical Manifestations and Outcomes of 20 Korean Hypochondroplasia Patients with the FGFR3 N540K variant. Exp Clin Endocrinol Diabetes 2023;131:339-346. PMID 36442838 | 10.1055/a-1976-9209 | Need the auxology table: height SDS at presentation and at last follow-up, and attained adult height in cm by sex for any patient who reached it, plus the GH-treated versus untreated split. Hypochondroplasia currently has NO published adult height in cm, which leaves the middle rung of the FGFR3 dose ladder empty (L11 hypochondroplasia; gap g_l11path_003) | l11path |
| P2 | Ko JM, Bae JS, Choi JS, et al. Skeletal overgrowth syndrome caused by overexpression of C-type natriuretic peptide in a girl with balanced chromosomal translocation, t(1;2)(q41;q37.1). Am J Med Genet A 2015;167A:1033-1038. PMID 25728306 | 10.1002/ajmg.a.36884 | Need the patient's height in cm and SDS with age, and the measured serum NT-proCNP value with its reference range. The abstract states only that NT-proCNP was "elevated". Together with Bocciardi 2007 this is one of only two human NPPC-overexpression cases and the pair is the basis for the CNP gain-of-function effect size (L11 nppc_duplication_tall_stature; gap g_l11path_006) | l11path |
| P2 | Gkourogianni A, Andrew M, Tyzinski L, et al. Clinical Characterization of Patients With Autosomal Dominant Short Stature due to Aggrecan Mutations. J Clin Endocrinol Metab 2017;102:460-469. PMID 27870580 | 10.1210/jc.2016-3313 | Need the per-family table linking each ACAN variant to adult height SDS and to bone-age advance, so that adult height can be regressed on bone-age advance (the direct test in gap g_l11path_011). The abstract gives only pooled medians and ranges (L11 acan_related_short_stature) | l11path |
| P3 | Bellus GA, Spector EB, Speiser PW, et al. Distinct missense mutations of the FGFR3 lys650 codon modulate receptor kinase activation and the severity of the skeletal dysplasia phenotype. Am J Hum Genet 2000;67:1411-1421. PMID 11055896 | 10.1086/316892 | Need the quantitative kinase-activation values for K650N, K650Q, K650E and K650M on one scale (fold over wild type, with n and dispersion) and the heights of the six K650N/K650Q individuals. This is the only paper that puts four alleles of one codon on a common activation axis and is the backbone of the FGFR3 dose-response (L11 hypochondroplasia, saddan_syndrome; gap g_l11path_004) | l11path |

| P1 | Stokes IA, Aronsson DD, Dimock AN, Cortright V, Beck S. Endochondral growth in growth plates of three species at two anatomical locations modulated by mechanical compression and tension. J Orthop Res 2006;24:1327-34. PMID 16705695 | 10.1002/jor.20189 | Need Table 2 / Figure 3: the per-plate regression of percent growth modulation on applied stress - slope, intercept, R2, 95% CI and n per group for each of the six species-site combinations, plus the exact applied stress levels used. The abstract gives only the pooled mean 17.1%/0.1 MPa and the range 9.2-23.9. This is the single most load-bearing number in L6 (hueter_volkmann_law, strain_magnitude_dependence, physeal_stress_in_vivo; gaps g_l6mech_001, g_l6mech_002) and the atlas currently cannot state its uncertainty. Europe PMC and NCBI both refuse full-text XML (publisher restriction) | l6mech |
| P2 | Stokes IA, Clark KC, Farnum CE, Aronsson DD. Alterations in the growth plate associated with growth modulation by sustained compression or distraction. Bone 2007;41:197-205. PMID 17532281 | 10.1016/j.bone.2007.04.180 | Need the multiple-regression table: standardised coefficients, standard errors and R2 for proliferative cell number per unit width and maximum hypertrophic cell height as predictors of growth rate, with n per species-site. The abstract gives coefficients 0.72 and 1.39 and correlations 0.38 and 0.56 with no dispersion (L6 loading_effect_plate_height, hueter_volkmann_law) | l6mech |
| P2 | Ilizarov GA. The tension-stress effect on the genesis and growth of tissues: Part II. The influence of the rate and frequency of distraction. Clin Orthop Relat Res 1989;239:263-85. PMID 2912628 | none | Need the histomorphometric grading data behind the rate and rhythm conclusions: how many canine tibiae per rate-frequency cell, what fraction showed premature consolidation at 0.5 mm/day and soft-tissue injury at 2.0 mm/day, and the grading scale used. The 1 mm/day in 4 increments prescription used worldwide rests entirely on this qualitative report (L6 distraction_rate_dose_response; gap g_l6mech_011) | l6mech |
| P3 | Beunen G, Malina RM, Baxter-Jones A. Blunted growth velocity in female artistic gymnasts. Med Sci Sports Exerc 2006. PMID 16540852 | none | No abstract is indexed in Europe PMC. Need the actual claim and any velocity numbers so the node can cite it for content rather than title (L6 gymnastics_stature_effect) | l6mech |

| P2 | Metcalf D, Greenhalgh CJ, Viney E, et al. Gigantism in mice lacking suppressor of cytokine signalling-2. Nature 2000;405:1069-1073. PMID 10890450 | 10.1038/35016611 | Need the body/skeletal size table: percent increase in body weight, nose-to-tail length and long bone length in Socs2-/- vs littermates, with n per group and dispersion, and the circulating GH and IGF-1 values that are described as "normal". The atlas currently records "30-40%" with value_unverified: true because only the abstract was read, and this is the single largest overgrowth effect size in the GH axis (L4 socs2_protein; gap g_l4endo_010) | l4endo |
| P2 | Ong KK, Elks CE, Li S, et al. Genetic variation in LIN28B is associated with the timing of puberty. Nat Genet 2009;41:729-733. PMID 19448623 | 10.1038/ng.382 | Need the adult-height effect size per allele in cm or SD units with its CI (the abstract reports only P=3.6e-7 in 17,274 women and P=0.006 in 9,840 men and the direction "shorter"). Without it the timing-versus-height trade-off cannot be quantified against the 0.12 y/allele menarche effect (L4 lin28b_gene, pubertal_growth_spurt) | l4endo |
| P2 | Caruso-Nicoletti M, Cassorla F, Skerda M, Ross JL, Loriaux DL, Cutler GB Jr. Short term, low dose estradiol accelerates ulnar growth in boys. J Clin Endocrinol Metab 1985;61:896-898. PMID 4044777 | 10.1210/jcem-61-5-896 | Need the figure showing the three-dose growth response with individual subject data, and the referenced earlier Turner-syndrome ethinyl estradiol biphasic dose-response paper. This n=5 study is the ONLY direct human estradiol dose-response with a linear-growth endpoint and is now the anchor of the biphasic node; the atlas needs to know whether the between-dose differences were formally tested (L4 estrogen_biphasic_dose_effect; gap g_l4endo_004) | l4endo |
| P3 | Roelfsema F, Biermasz NR, Veldhuis JD, et al. Growth Hormone Dynamics in Healthy Adults Are Related to Age and Sex and Strongly Dependent on Body Mass Index. Neuroendocrinology 2016;103:335-344. PMID 26228064 | 10.1159/000438904 | Need Table 2: absolute deconvolution parameters (pulse frequency per 24 h, burst mass, basal secretion, half-life) by age decade and sex in the 130-subject cohort. The abstract gives only correlation directions and P values, so the atlas quotes pulse frequency from a smaller n=37 study instead (L4 gh_secretion_pulsatility) | l4endo |

| P2 | Cooper KL, Oh S, Sung Y, Dasari RR, Kirschner MW, Tabin CJ. Multiple phases of chondrocyte enlargement underlie differences in skeletal proportions. Nature 2013;495:375-378. PMID 23485973 | 10.1038/nature11940 | Need the per-phase volume data: absolute chondrocyte volume and dry mass at each of the three phases, per bone (fast vs slow plate), with n and dispersion, and the IGF-dependence experiment for phase 3. This is one side of contradiction c002 (hypertrophic volume vs proliferation per column as the dominant determinant of site-specific elongation rate) and the atlas currently states its conclusion from the abstract only (L0 gap g_l0dev_009; L1 hypertrophic_volume_increase, site_specific_growth_rate) | l0dev |
| P2 | Rux DR, Song JY, Swinehart IT, et al. Regionally Restricted Hox Function in Adult Bone Marrow Multipotent Mesenchymal Stem/Stromal Cells. Dev Cell 2016;39:653-666. PMID 27939685 | 10.1016/j.devcel.2016.11.008 | Need the Hoxa11-EGFP reporter images and the flow quantification showing WHICH compartments are negative - specifically whether growth plate chondrocytes (resting, proliferative, hypertrophic) were examined and scored, or simply not reported. The word 'exclusively' in the abstract is the sole basis for the claim that retained HOX identity sits outside the cartilage, which decides whether every postnatal HOX effect on elongation acts through marrow/perichondrium rather than through the plate (L0 hox_code_limb, hoxa11_gene; gap g_l0dev_004) | l0dev |
| P3 | Song JY, Pineault KM, Dones JM, Raines RT, Wellik DM. Hox genes maintain critical roles in the adult skeleton. PNAS 2020;117:7296-7304. PMID 32170021 | 10.1073/pnas.1920860117 | Need the histology and quantification of the adult Hoxd11 conditional deletion: whether the growth plate itself was examined at the deletion timepoint, and any measurement of plate height or chondrocyte number alongside the reported osteoblast maturation arrest. Read from abstract only (L0 hoxd11_gene) | l0dev |

| P2 | Powell GF, Brasel JA, Blizzard RM. Emotional deprivation and growth retardation simulating idiopathic hypopituitarism. I. Clinical evaluation of the syndrome. N Engl J Med 1967;276:1271-1278. PMID 6024346 | 10.1056/NEJM196706082762301 | Need the case-series numbers: n, ages, height and weight SDS at presentation, and the documented dietary intake showing the children were NOT undernourished. Europe PMC holds no abstract for this record, so L10 psychosocial_dwarfism currently rests on the title alone (L10 psychosocial_dwarfism; gap g_l10env_012) | l10env |
| P2 | Powell GF, Brasel JA, Raiti S, Blizzard RM. Emotional deprivation and growth retardation simulating idiopathic hypopituitarism. II. Endocrinologic evaluation of the syndrome. N Engl J Med 1967;276:1279-1283. PMID 6024347 | 10.1056/NEJM196706082762302 | Need the actual endocrine data: GH stimulation test peaks before and after removal from the adverse environment, with n per test and the time course of normalisation, plus growth velocity in cm/yr in each phase. This is the sole basis for the claim that psychosocial short stature is a reversible GH-secretory lesion, which is the edge L10 psychosocial_dwarfism -> L4 gh_secretion_pulsatility (L10 psychosocial_dwarfism; gap g_l10env_012) | l10env |

| P1 | Kember NF, Sissons HA. Quantitative histology of the human growth plate. J Bone Joint Surg Br 1976;58-B:426-435. PMID 1018028 | 10.1302/0301-620x.58b4.1018028 | Need the number of DONORS and their ages/sexes contributing the femoral sections, and the per-donor cell-count data behind "24 cells per column". This paper is the sole source of the ~20-day human proliferative cycle time used throughout L1/L2, and the donor count is a required cell in atlas/quant/human_growth_plate_donor_census.csv (L13 histomorphometry_physis, human_growth_plate_tissue_scarcity; gaps g_l1arch_002, g_l13b_007) | l13b |
| P1 | Emons J, Chagin AS, Hultenby K, et al. Epiphyseal fusion in the human growth plate does not involve classical apoptosis. Pediatr Res 2009;66:654-659. PMID 19730156 | 10.1203/pdr.0b013e3181beaa8c | Need the Methods table of specimens: how many human growth plates, from how many donors, at which pubertal stages, and the provenance of the single "unique late pubertal growth plate which was about to fuse". This is the only human peri-fusion histology in existence and its donor count is required for the census (L13 human_growth_plate_tissue_scarcity; L7 gap g_l7fuse_002) | l13b |
| P2 | Byers S, Moore AJ, Byard RW, Fazzalari NL. Quantitative histomorphometric analysis of the human growth plate from birth to adolescence. Bone 2000;27:495-501. PMID 11033444 | 10.1016/s8756-3282(00)00357-4 | Need the donor table: number of autopsy donors, age distribution, cause of death, and the absolute zone heights in um by age band. One of only two quantitative human histomorphometry series across the growing years (L13 histomorphometry_physis, human_growth_plate_tissue_scarcity) | l13b |
| P2 | Xie C, Li W, Yao X, et al. Physical and chemical niche of human growth plate for polarized bone development. Nat Commun 2025;16. PMID 40781081 | 10.1038/s41467-025-62711-z | Need the absolute nanoindentation moduli in MPa or GPa with n and dispersion for each region (epiphysis, GP-epiphysis interface, growth plate, GP-metaphysis interface, metaphysis). The atlas currently records the modulus profile qualitatively because only the interface behaviour was extractable; these are the only human physeal moduli that exist and they are the anchor for gap g_l5matrix_001 (L13 atomic_force_microscopy_cartilage; L5 gaps g_l5matrix_001, g_l5matrix_008) | l13b |
| P2 | Reilly T, Tyrrell A, Troup JD. Circadian variation in human stature. Chronobiol Int 1984;1:121-126. PMID 6600017 | 10.3109/07420528409059129 | Need the magnitude of diurnal stature loss in mm with its dispersion and the time course across the waking day. The atlas records the phenomenon qualitatively, but the number sets the floor on stadiometric velocity error and is needed to weigh gap g_l6mech_014 (L13 stadiometry_measurement_error) | l13b |
| P3 | Dymerska B, Bohndorf K, Schennach P, et al. In vivo phase imaging of human epiphyseal cartilage at 7 T. Magn Reson Med 2018;79:2149-2155. PMID 28758241 | 10.1002/mrm.26858 | Need the acquired voxel size and in-plane resolution of the gradient-echo protocol, to state the achievable in vivo resolution against the 10-20 um chondrocyte and 100-1000 um zone dimensions rather than describing it qualitatively (L13 mri_physis_imaging; gap g_l13b_012) | l13b |
| P3 | Avijgan M, Perez AR, Galicia LA, et al. Human growth plates house resting zone sub-populations with features of quiescent stem cells. bioRxiv 2025 | 10.1101/2025.03.12.642613 | Need the donor count, ages, sexes, anatomical sites and tissue provenance. Full text could not be retrieved from the preprint server in this session; the study is a required row in atlas/quant/human_growth_plate_donor_census.csv, where it is currently recorded as not_stated (L13 human_growth_plate_tissue_scarcity) | l13b |

| P1 | Tanner JM, Whitehouse RH, Takaishi M. Standards from birth to maturity for height, weight, height velocity, and weight velocity: British children, 1965. Part II. Arch Dis Child 1966;41:613-635. PMID 5927918 | 10.1136/adc.41.220.613 | Need the height-velocity centile TABLES (3rd, 10th, 25th, 50th, 75th, 90th, 97th) by whole year of age and sex, ideally the underlying SDs. The atlas has PHV magnitude and timing with dispersion from three modern SITAR cohorts but NO childhood (age 3-9) velocity dispersion at all - the entire pre-pubertal population variance in cm/yr is currently missing from atlas/quant/organism_targets.csv (L9 growth_velocity_curve; gap g_l9organism_001) | l9organism |
| P1 | Berkey CS, Dockery DW, Wang X, Wypij D, Ferris B Jr. Longitudinal height velocity standards for U.S. adolescents. Stat Med 1993;12:403-414. PMID 8456221 | 10.1002/sim.4780120503 | Need the 3rd-97th centile velocity curves as numbers, by sex and by maturation group (early/average/late), ages 7-18, from the 6532-child Six Cities sample. Together with the Tanner tables above this is the only route to a defensible population SD for height velocity at each age (L9 growth_velocity_curve) | l9organism |
| P2 | Emons JA, Boersma B, Baron J, Wit JM. Catch-up growth: testing the hypothesis of delayed growth plate senescence in humans. J Pediatr 2005;147:843-846. PMID 16356444 | 10.1016/j.jpeds.2005.07.033 | Europe PMC holds no abstract. Need the design and the result: which human cohort, what measure of "senescence" was used, and whether catch-up magnitude tracked duration of preceding suppression. This is the only direct human test of the plate-intrinsic account of catch-up and is the discriminating evidence for gap g_l9organism_006 (L9 canalization_growth) | l9organism |
| P2 | Jolicoeur P, Pontier J, Abidi H. Asymptotic models for the longitudinal growth of human stature. Am J Hum Biol 1992;4:461-468. PMID 28524389 | 10.1002/ajhb.1310040405 | Need the reported residual/goodness-of-fit statistics for JPA-2 and the dataset they were computed on, plus the parameter count. The atlas currently grades "JPA-2 fits better than Preece-Baines" as X because no residual figure for JPA-2 exists in any retrieved source (L9 jpa2_model; gap g_l9organism_002) | l9organism |
| P2 | Hermanussen M, Cole J. The calculation of target height reconsidered. Horm Res 2003;59:180-183. PMID 12649571 | 10.1159/000069321 | Europe PMC holds no abstract. Need the proposed correction and, critically, any residual SD or prediction interval the authors compute, so that a third independent estimate can be set beside zeevi2024 (4.4-4.7 cm) and luo1998 (~5.1 cm) (L9 mid_parental_target_height, target_height_predictive_sd; gaps g_l9organism_004, g_l9organism_005) | l9organism |
| P2 | Schuelke M, Wagner KR, Stolz LE, et al. Myostatin mutation associated with gross muscle hypertrophy in a child. N Engl J Med 2004;350:2682-2688. PMID 15215484 | 10.1056/NEJMoa040933 | Europe PMC holds no abstract. Need the child's LENGTH/HEIGHT and, if reported, parental heights - not the muscle phenotype. Whether a lifelong myostatin-null human is taller than target height is the decisive test of whether muscle force drives longitudinal growth (L9 myostatin_mstn; gap g_l9organism_012) | l9organism |
| P3 | Demirjian A, Goldstein H, Tanner JM. A new system of dental age assessment. Hum Biol 1973;45:211-227. PMID 4714564 | - | Need the stage definitions and the maturity-score-to-dental-age conversion tables with their published SDs, so the dental clock's own measurement precision can be stated alongside the 1.68-year dental/skeletal dissociation (L9 tooth_mineralization_stages; gap g_l9organism_009) | l9organism |
| P3 | Smith DW, Truog W, Rogers JE, et al. Shifting linear growth during infancy. J Pediatr 1976;89:225-230. PMID 940016 | 10.1016/s0022-3476(76)80453-2 | Need n, the proportion of infants shifting up versus down, and the magnitude of the shift in centiles or SDS. The atlas records catch-down qualitatively because the abstract carries no rates (L9 catch_down_growth; gap g_l9organism_007) | l9organism |

| P2 | Kemp SF (2006), "Efficacy and safety of mecasermin rinfabate", Expert Opin Biol Ther 6(5):533-8 | 10.1517/14712598.6.5.533 | The height-velocity tables for children treated with the rhIGF-1/rhIGFBP-3 complex, and any head-to-head comparison against uncomplexed mecasermin — needed to close gap g_l12b_012 (L12). |
| P1 | FDA multidisciplinary and pharmacology/toxicology reviews, NDA 214938 (vosoritide) and NDA 219164 (navepegritide), accessdata.fda.gov | n/a | The nonclinical tissue-distribution / quantitative whole-body autoradiography sections only — specifically any cartilage or growth-plate concentration relative to plasma. Closes or sharply constrains gap g_l12b_002 and g_l12b_024 (L12) at no experimental cost. |
| P2 | Ursachi VC et al. (2026), "Infigratinib is a weak inhibitor of the FGFR3-N540K mutant associated with hypochondroplasia", J Bone Miner Res | 10.1093/jbmr/zjag017 | The IC50 values and assay conditions (ATP concentration, substrate, readout) behind the "weak inhibitor" claim — needed to adjudicate contradiction gap g_l12b_004 against Demuynck 2025. |
| MR2-1 | **P1** | FDA Clinical Pharmacology / Biopharmaceutics Review, vosoritide (VOXZOGO), NDA 214938 | Drugs@FDA | **Dose-justification section only.** Was the approved 15 µg/kg/day selected on an EFFICACY PLATEAU or on a BLOOD-PRESSURE / tolerability limit? This single fact discriminates hypothesis H3 (tolerability cap) from H1 (downstream gating) for the whole CNP-analogue exposure question. The label alone does not distinguish "saturated" from "as high as we dared go". | `cnp_analog_pk_challenge`, g_mr002_h3 |
| MR2-2 | **P1** | NCT00572156 — 6-year GH + IGF-1 combination trial, terminated for "strategic reasons" | ClinicalTrials.gov | Full posted results tables and any published secondary analyses. Year-1 height velocities were posted at 9.3/10.1/9.7/11.2 cm/yr and the programme ran 6 years. A strategic termination is NOT evidence about biology, so this dataset is retrievable positive-signal evidence that appears never to have been analysed for the growth question. | `igf1_gh_combination_therapy` |
| MR2-3 | **P1** | Infigratinib / FGFR3-inhibitor potency against **G380R**-activated FGFR3 — patents, INDs, regulatory submissions | Google Patents, Espacenet, FDA | Any IC50 or cellular potency value against the TRANSMEMBRANE G380R allele. All published potency data are on kinase-domain alleles (K650E, K650M, N540K). Achondroplasia is G380R. Patents are the most likely repository of the missing panel. | `infigratinib_growth`, `fgfr3_tyrosine_kinase_inhibitor`, g_mr002_allele |

| P2 | Sergerie K, Parent S, Beauchemin P-F, Londono I, Moldovan F, Villemure I. Growth plate explants respond differently to in vitro static and dynamic loadings. J Orthop Res 2011;29(4):473-480. PMID 21337387 | 10.1002/jor.21282 | **Figure/Results: the MMP-13 immunohistochemistry panel only.** MMP-13 was assayed alongside aggrecan, collagen II and collagen X under matched static (10% strain) and dynamic (7-13%, 0.1 Hz) compression of swine ulnar physeal explants, but the abstract reports only the aggrecan/collagen results. MMP-13 is the chondrocyte-intrinsic collagenase of the hypertrophic zone and its load-responsiveness would be the only existing link from mechanical load to a growth plate protease. Needed to complete edges e00052-e00054 in the l6l5seam shard and to constrain gap g_l6l5_003 | l6l5seam |

## Phase 2d canonical-mechanism audit (shard l2daudit, 2026-08-05)

Every row below blocked a specific audit question in `atlas/audit/mechanism_audit.md`.

| Priority | Citation | DOI | What is needed (specific figure/panel/table) | Shard |
|---|---|---|---|---|
| P1 | Baron J, Klein KO, Colli MJ, et al. Catch-up growth after glucocorticoid excess: a mechanism intrinsic to the growth plate. Endocrinology 1994;135:1367-1371. PMID 7925098 | 10.1210/endo.135.4.7925098 | **The local-versus-systemic comparison figure and its numbers only**: growth (in mm or mm/day) of the locally dexamethasone-infused rabbit growth plate against the contralateral untreated plate in the SAME animal, during and after treatment, with n. This single experiment is the entire basis for the atlas claim that catch-up growth does not require a central size sensor, and it is unread — `catch_up_growth` is marked `pending_source` on it. It also anchors the "intrinsic and local" clause of `growth_plate_senescence` | l2daudit |
| P2 | Gafni RI, Weise M, Robrecht DT, et al. Catch-up growth is associated with delayed senescence of the growth plate in rabbits. Pediatr Res 2001;50:618-623. PMID 11641457 | 10.1203/00006450-200111000-00014 | **The histomorphometry table**: absolute growth plate height, proliferative zone height, hypertrophic cell size and column density in catching-up versus age-matched control rabbit plates, with n per group. Needed to state numerically what "less senescent" means; the atlas currently carries the claim with no numbers at all | l2daudit |
| P2 | Rosati R, Horan GS, Pinero GJ, et al. Normal long bone growth and development in type X collagen-null mice. Nat Genet 1994;8:129-135. PMID 7842010 | 10.1038/ng1094-129 | **The growth plate histomorphometry and the survival data, if any**: what was measured, at what age, with what n and what detectable difference. CORR-002 rests on Gress 2000 finding phenotype in the same line; the power of the original negative result is the missing quantity and `p00536` records "power not stated" | l2daudit |
| P2 | Ozasa A, Komatsu Y, Yasoda A, et al. Complementary antagonistic actions between C-type natriuretic peptide and the MAPK pathway through FGFR-3 in ATDC5 cells. Bone 2005;36:1056-1064. PMID 15869918 | 10.1016/j.bone.2005.03.006 | **The GC-B Western blot panel and the RAF-1 phosphorylation panel**: whether GC-B protein level was quantified (not merely shown unchanged) and at what FGF dose, and the RAF-1 versus MEK versus ERK phosphorylation series establishing where CNP blocks the cascade. Both underpin `fgfr3_npr2_crosstalk` and `fgfr3_mapk_branch` and both are cited from the abstract only | l2daudit |
| P2 | Pfeifer A, Aszodi A, Seidler U, Ruth P, Hofmann F, Fassler R. Intestinal secretory defects and dwarfism in mice lacking cGMP-dependent protein kinase II. Science 1996;274:2082-2086. PMID 8953039 | 10.1126/science.274.5295.2082 | **The growth plate histology panel and any zone measurements**: whether the Prkg2-null mouse plate is expanded as in the KMI rat, and by how much. This is the mouse counterpart of the sign conflict in CORR-003 and gap g_l2d_001; without it the conflict rests on one species | l2daudit |
| P3 | Schrier L, Ferns SP, Barnes KM, et al. Depletion of resting zone chondrocytes during growth plate senescence. J Endocrinol 2006;189:27-36. PMID 16614378 | 10.1677/joe.1.06489 | **The resting-zone cell-count-versus-age table**: cells per unit area or per column by age with n, and the proliferation-rate series. `growth_plate_senescence` states "fewer resting zone cells per unit area" with no number attached | l2daudit |
| P3 | Jobert AS, Zhang P, Couvineau A, et al. Absence of functional receptors for parathyroid hormone and parathyroid hormone-related peptide in Blomstrand chondrodysplasia. J Clin Invest 1998;102:34-40. PMID 9649554 | 10.1172/JCI2918 | **The paternal-allele analysis only**: what was done to establish non-expression of the paternal PTH1R allele and what was excluded. PMC509062 is a scanned page-image deposit with no machine-readable body. Needed for gap g_l2d_007 | l2daudit |


---

## Published corrections whose NOTICE BODY could not be retrieved (added 2026-08-06)

The standing sweep (`atlas/tools/standing.py`) found **33 references carrying a published
correction or erratum**, and **not one notice body is retrievable through the open API** —
Europe PMC indexes the notice's existence and title (`Department of Error`, `Publisher
Correction: ...`) and nothing else. An erratum can silently change a figure this atlas
quotes a number from, so each is flagged `has_published_correction: true` with
`correction_checked: false` in the bibliography and listed here.

**21 of the 33 supply quantitative rows.** Those are the ones where an unread correction
can move a number, and they are ordered by how many rows depend on them.

| Pri | Ref | quant rows | notice types | Nodes affected |
|---|---|---:|---|---|
| P1 | `bethlehem2022` | 13 | comment, correction, erratum, preprint_in | allometry_organ_scaling, brain_growth_trajectory, head_circumference_growth |
| P1 | `smith1994` | 8 | comment, erratum | central_precocious_puberty, esr1_gene, estrogen_driven_fusion, estrogen_receptor_alpha |
| P1 | `ogawa2025` | 7 | erratum | genomic_imprinting_growth, igf2_h19_imprinting |
| P1 | `karlberg1995` | 6 | erratum | intrauterine_growth_restriction, sga_catch_up, small_for_gestational_age |
| P1 | `wilson2021` | 5 | correction, erratum | column_density, growth_plate, growth_plate_height, hypertrophic_zone |
| P1 | `savarirayan2020` | 5 | erratum | cnp_analog_pk_challenge, cnp_protein, fgfr3_npr2_crosstalk, vosoritide |
| P2 | `zhang2023` | 4 | correction, erratum | hypoxic_gradient_signaling, nutrient_diffusion_growth_plate, oxygen_gradient_growth_plate |
| P2 | `williams2001` | 3 | erratum | chondron, finite_element_model_physis, ovine_growth_plate_model, zonal_stiffness_gradient |
| P2 | `kusumbe2014` | 3 | comment, erratum | metaphyseal_funnelization, metaphyseal_vasculature, primary_spongiosa, stem_cell_niche_vascular_coupling |
| P2 | `domen2009` | 3 | erratum | als_igfals, igfals_gene |
| P2 | `preece1978` | 2 | erratum | preece_baines_model |
| P2 | `matsushita2025` | 2 | correction, erratum | meclizine_repurposing |
| P2 | `khamis1994` | 2 | erratum | fels_method, remaining_growth_prediction |
| P2 | `cui2025` | 2 | erratum | aromatase_inhibitor_anastrozole, aromatase_inhibitor_letrozole |
| P2 | `wolthers2017` | 1 | erratum | knemometry |
| P2 | `ruizperez2000` | 1 | comment, erratum | evc_evc2_complex |
| P2 | `glasson2005` | 1 | erratum | adamts5 |
| P2 | `frisancho1991` | 1 | erratum | lead_exposure_growth |
| P2 | `farebrother2018` | 1 | erratum | iodine_deficiency_growth |
| P2 | `clemens2026` | 1 | correction, erratum | deflazacort, glucocorticoid_sparing_strategy |
| P2 | `anderson2004` | 1 | erratum | matrix_vesicle, pi_ppi_ratio, tnap_alpl |
| P3 | `victora2008` | 0 | erratum | dohad_hypothesis, intrauterine_growth_restriction, maternal_nutrition_offspring_height, placental_function_growth |
| P3 | `stjacques1999` | 0 | erratum | bone_collar_formation, ihh_bmp_crosstalk, ihh_protein, in_situ_hybridization_cartilage |
| P3 | `sjgren2000` | 0 | erratum | gh_receptor |
| P3 | `sayers2013` | 0 | erratum | preece_baines_model |
| P3 | `savarirayan2026` | 0 | erratum | infigratinib_growth, navepegritide, tyrosine_kinase_inhibitor_growth_toxicity |
| P3 | `sacchetti2007` | 0 | erratum | human_skeletal_stem_cell, marrow_stromal_cell |
| P3 | `martin2019` | 0 | comment, correction, erratum, preprint_in | — |
| P3 | `legeaimallet1998` | 0 | erratum | fgf9_ligand, fgfr3_receptor, fgfr3_stat1_branch |
| P3 | `kawasaki2008` | 0 | erratum | pkg2_kinase |
| P3 | `karimian2024` | 0 | correction, erratum | congenital_hypothyroidism |
| P3 | `hoppe2006` | 0 | erratum | milk_consumption_height |
| P3 | `basson1997` | 0 | correction, erratum | limb_bud_initiation, pitx1_gene, tbx5_gene |

What is needed from each: **the notice body**, and specifically whether it changes any
numeric value, figure or table that this atlas cites. Three were spot-checked and even
their titles are uninformative — `savarirayan2020` (the vosoritide phase 3, 5 quant rows)
carries a Lancet *Department of Error*; `wilson2021` (growth-plate morphometry, 5 quant
rows) carries a corrigendum on the very morphometric parameters the atlas quotes.

Until these are read, every number sourced from a flagged reference should be treated as
`value_unverified` in spirit even where the field says otherwise.
---

## Round 134 — the two documents standing between the phosphatase branch and a number

Both are paywalled and both were attempted through lawful routes only (Europe PMC, publisher
landing page). No paywall was bypassed. AACR returned HTTP 403 to a plain request.

**RESOLVED 2026-08-08 — both P0 and P1 below were supplied by the project owner as PDFs and read in
full. Endothall Cmax at the human MTD is 11.5–34.3 ng/mL (62–184 nM). The entries are kept for the
record; the P2 items remain open.**

| P0 (resolved) | `feng2023` | PMID 37584370, DOI 10.4155/bio-2023-0078, *Bioanalysis* | **The patient
concentration–time data for LB-100 and endothall from NCT04560972.** This is the single number
`g_l12_endothall_exposure_and_juvenile_tolerability` turns on: whether achievable human plasma
endothall clears the 95 nM IC50. The abstract gives only the validated calibration range,
2.5–500 ng/mL, which brackets 95 nM (= 17.7 ng/mL at MW 186.16) but is not a measurement of
anything. Everything the atlas currently says about clinical exposure on this branch is
inference from that range and is graded E. |

| P1 (resolved) | `chung2017` | PMID 28039265, DOI 10.1158/1078-0432.CCR-16-2299, *Clin Cancer Res* | **The
pharmacokinetics section.** The abstract gives doses, DLT and RP2D — all already in the atlas —
but no Cmax, no AUC, no half-life. With the PK, the mouse-to-human body-surface-area conversion
in `the_tool_compound_is_a_prodrug_and_it_kills_juvenile_mice` could be replaced by a direct
exposure comparison, which is a far stronger argument than an allometric convention. |

| P2 | `rollema2025` | PMID 39909155, DOI 10.1016/j.ijpharm.2025.125317, *Int J Pharm* | Full text
for the hydrolysis kinetics. The abstract is unusually complete — half-lives, both IC50s, the
DMSO-stock artefact — and CORR-127 is written from it, but the atlas holds it as
`primary_abstract_only` and the figure-level data have not been seen. |

| P2 | `potter1998` | PMID 9485390, *Biochemistry* | Full text for the homologous-desensitisation
time course and the fraction of receptor dephosphorylated. The abstract states "approximately
one-half" of the NPR-B population is completely dephosphorylated; the kinetics are not in it. |

---

## Round 135 — THE GET-LIST for the decisive experiment

Full reasoning in
`nodes/L12_pharmacology_as_mechanistic_probe/the_experiment_specified_and_what_is_missing.yaml`.
Ordered by how much each item moves the design. Everything below was attempted through
lawful routes first; failures are noted.

### BLOCKING — the design cannot be finished without it

| P0 | **"Endothall: HED Chapter of the Reregistration Eligibility Decision Document"**, dated
18 April 2005, corrected 30 September 2005, EPA docket **OPP-2004-0370** (also indexed
EPA-HQ-OPP-2004-0370). | Contains EPA's review of the mammalian **metabolism and
pharmacokinetics** studies — guideline 870.7485, **MRIDs 42169502, 44263501, 42200101** —
i.e. absorption fraction, Tmax, half-life, tissue distribution and excretion for endothall
**dosed as endothall**. This is the only plausible public home for the one number that is
blocking: endothall's own clearance, currently confounded with fractional conversion in every
dataset that exists. `downloads.regulations.gov` returned **HTTP 403** to every direct
request from this session except one item that came via a search-result link. |

### DOSE-SETTING

| P1 | **EPA MRID 42787702** — Gallacher (1993), *Dipotassium Endothall — Dissociation
Constant*, Ricerca Inc., 54 pp. | The pKa values. They decide whether the Donnan penalty on a
growth-plate-bound anion is ~3-fold or ~7-fold. Unpublished; summarised in the same HED
chapter. A published pKa from any peer-reviewed source would substitute. |

| P1 | **Endothall plasma protein binding / free fraction**, any species. | Unmeasured
anywhere this atlas can find. Enters both the clearance estimate and the Donnan calculation,
which uses *free* plasma concentration. |

| P2 | **C57BL/6J body-weight growth curve, PND21 → PND56**, sexes separate. | Converts a
fixed-output pump into a dose trajectory. Publicly available (JAX phenotype data); simply not
yet fetched. Currently ASSUMED values in `atlas/tools/endothall_experiment_design.py`. |

### INTERPRETATION-SETTING

| P1 | **shuhaibar2021 (JCI Insight 6:e141426) Figure 1F** — the per-concentration values,
n and mean ± error, for 1 / 5 / 10 µM LB-100 and 10 µM cantharidin. | There is **no
source-data workbook** for this paper, and the PMC OA package (`PMC8262325.tar.gz`) 404s. The
in-tissue concentration requirement is currently three qualitative points rather than a fitted
curve. A screenshot of panel F at readable resolution would be enough; the authors' source
values would be better. |

| P1 | **EPA MRID 42776301** — Trutter (1993), *Rat Developmental Toxicity Study with Disodium
Salt of Endothall*, Hazleton Washington, 289 pp. | Prenatal developmental toxicity studies
routinely include **fetal skeletal and ossification examinations**. If they exist, these are
the **only skeletal data for endothall at any dose in any species**. The RED says only "did not
induce developmental toxicity", which does not tell us whether bones were measured. |

| P2 | **EPA MRID 43152101** — the two-generation rat reproduction study. | Source of *every*
systemic endpoint in the endothall dossier, including the chronic LOAEL of 2 mg/kg/day and the
decreased pup body weight at 60 mg/kg/day. Worth seeing whether pup **length** was recorded
alongside weight. |

### LOGISTICS

| P2 | **Osmotic pump manufacturer specifications** — flow rate, reservoir volume, duration and
**filled mass** for the 28-day and 42-day models. | The 10-%-of-body-weight convention against
an ~8.5 g weanling gives a ≤0.85 g budget. If the long-duration pumps exceed it, the design has
to change (later start, serial short pumps, or drinking water). |

| P3 | **Endothall aqueous solubility** and stability at 37 °C over 28–42 days. | Required
reservoir concentration is only ~1.4–2.4 mg/mL, so solubility is unlikely to bind — but
stability in a pump at body temperature for six weeks is unmeasured. |

| P3 | **chung2017 refs 13 and 14** — the two preclinical studies behind the claim that maximum
PP2A inhibition in xenografts occurs 2–4 h after a single injection with full recovery taking
≥24 h. | This is the tissue pharmacodynamic time course. If target engagement really outlasts
plasma by that much, continuous dosing may be unnecessary and the whole plasma-versus-medium
comparison is the wrong frame. |

### NOT FETCHABLE — bench work, listed so it is not mistaken for a documentary gap

- Whether **endothall itself**, as distinct from LB-100, blocks FGF-induced NPR2
  dephosphorylation. Never tested in any system.
- **Cartilage concentration** of endothall (or of any PPP inhibitor) in any species.

---

## Round 136 — get-list update after the SERA risk assessment and Figure 1F

**RESOLVED by `sera_endothall_2009` (SERA TR-052-16-04a, USDA Forest Service, Durkin 2009), supplied
by the project owner:** the P0 blocking item (endothall's own PK), the pKa values, the solubility, the
oral-absorption fraction, the parenteral toxicity, and the skeletal observation. **RESOLVED by the
supplied Figure 1F panel:** the concentration–response, now fitted at EC₅₀ 0.69 µM endothall, Hill
slope 5.4.

**The two EPA RED PDFs supplied are the same document already fetched at round 134** (EPA 738-R-05-008),
re-laid-out N-up. Nothing new in them.

### STILL OPEN, and now much more specific

| P0 | **Volume of distribution of endothall**, any species. | This is now the single largest source of
spread in the dose calculation. The required infusion rate spans 0.03–0.31 mg/kg/day for the target
concentration, and ~half that spread is the assumed Vd of 0.20–0.26 L/kg. The 1990 EPA IV study
(**MRID 42169502**) that produced the half-lives will contain Vd and clearance directly. SERA states
this study "cannot be identified" and has no cleared review — so this needs the **EPA HED Chapter**
(18 Apr 2005 / corrected 30 Sep 2005, docket OPP-2004-0370) or a FOIA request. |

| P1 | **Soo et al. 1967**, the only published endothall PK paper (rat, ¹⁴C, Table III has the
per-organ time course). | SERA quotes fragments. The full table would give tissue:plasma ratios for
every organ — the nearest available proxy for what cartilage might do, and the check on whether the
kidney-concentration story holds quantitatively. Journal not identified in SERA's citation line as
extracted; likely *J Agric Food Chem* 1967, p. 1020. |

| P1 | **Gaines & Lindner 1986**, *Fund Appl Toxicol* 7:299–308 — acute toxicity in **adult AND
weanling** rats. | SERA quotes only the adult LD₅₀s (57 M / 46 F). The paper's whole point is the
adult-versus-weanling comparison, and our experiment doses weanlings. If juveniles are markedly more
sensitive, every dose in the design moves. |

| P2 | **Graziano & Casida 1987** and **Kawamura et al. 1990** — the two parenteral mouse studies. |
Kawamura gives the IP LD₅₀ of 14 mg/kg that the therapeutic-window calculation now leans on; Graziano
describes the 10 mg/kg IP syndrome (liver enlargement, lethargy, death in 60–90 min). Both are needed
to know whether a *continuous low-rate* IP infusion shares that mechanism. |

| P2 | **osmotic pump filled mass** for the 28- and 42-day models. | Unchanged from round 135. The
10 %-of-body-weight limit against an ~8.5 g weanling is still the one logistical constraint that could
force a redesign. |

| P3 | **C57BL/6J PND21–56 growth curve**; **endothall stability at 37 °C for 4–6 weeks**. | Unchanged. |

### THE THREE THINGS NO DOCUMENT CAN ANSWER

1. Does **endothall itself** — not LB-100 — block FGF-induced NPR2 dephosphorylation? Never tested.
   One Phos-tag gel or one cGi500 tibia answers it, and everything downstream assumes it.
2. What is the **cartilage** concentration of endothall at a given plasma concentration? The Donnan
   calculation predicts 14–30 % of free plasma; nobody has measured it for this or any compound of
   this class.
3. Does continuous endothall change a **bone length** in a growing animal? That is the experiment.

---

## Round 137 — get-list after five more documents

**RESOLVED:** the ALZET pump masses (1.1 g empty, ~1.3 g filled — the 28/42-day models **fail** the
10 %-of-body-weight limit until ~13 g / PND28-30); Gaines & Linder (endothall **was never tested in
weanlings**); Kawamura (IP LD₅₀ 14 mg/kg confirmed, plus the r = 0.95 toxicity-versus-binding
correlation); Graziano (endothall was dosed at **75** mg/kg, not 10 — SERA mis-transcribed); and the EPA
Toxicology Chapter, which shows the dose-dependent half-lives are **oral**, not intravenous.

### STILL OPEN — now only four things, and two of them are small

| P0 | **Volume of distribution and clearance of endothall after the intravenous dose** — MRID 42169502
(Hallifax 1990, *Endothall Technical: Absorption, Distribution, Metabolism and Excretion Study in the
Rat*, Life Science Research, Lab Project 89/0122 / PSV/026, **381 pages**). | Still the largest single
source of spread. The EPA Toxicology Chapter summarises this study but reports only excretion for the IV
arm. The 381-page **full study report**, or the EPA **Data Evaluation Record** for it, would give the
plasma concentration–time curve after 0.9 mg/kg IV — from which Vd, CL and the true elimination half-life
all fall out, and the 1.3–2.3× margin becomes a real number instead of a bound. Route: FOIA to EPA OPP
for MRID 42169502, or the DER if one exists. |

| P1 | **ALZET 100-series filled mass** (models 1002 and 1004 — 0.25 µL/h × 14 d and 0.11 µL/h × 28 d,
100 µL reservoir). | The design now needs serial 100-series pumps from weaning because the 200-series is
too heavy. `martiniova2011` used a 1002 in mice, so it is feasible in an adult; the number needed is the
filled mass against an 8.5 g weanling. Same manufacturer table as the 2004/2006 data already supplied. |

| P2 | **Soo et al. 1967, Table III** — the per-organ ¹⁴C time course in rat. | Unchanged from round 135.
Now the only remaining source for tissue:plasma ratios, and the check on both the kidney-concentration
story and the SERA-versus-EPA disagreement about whether endothall accumulates. |

| P3 | **Li, Mackintosh & Casida 1993**, *Protein phosphatase 2A and its [³H]cantharidin/[³H]endothall
thioanhydride binding site* (PMID 8240393). | Turned up while searching for Kawamura. This is the paper
that identifies the Kawamura binding site **as PP2A** and gives inhibitor specificity — it would tell us
which PPP family members endothall itself hits and at what IC₅₀, which is the one selectivity question
the atlas has never been able to answer for the active species rather than the prodrug. |

### UNCHANGED — the three things no document can answer

1. Does **endothall itself** block FGF-induced NPR2 dephosphorylation? Never tested.
2. What is the **cartilage** concentration at a given plasma concentration? Predicted 14–30 % of free
   plasma; never measured.
3. Does continuous endothall change a **bone length** in a growing animal?

---

## Round 138 — the P0 is answered by derivation, not by fetching

The project owner judged MRID 42169502 unobtainable. That is almost certainly right — it is a 381-page
unpublished industry report with no cleared review. **The information in it has now been obtained
another way.** The 1992 **EPA Drinking Water Criteria Document for Endothall** (EPAX 9205-0075) — a
scanned 76-page document, OCRed by this atlas — reproduces **Soo et al. 1967 Tables III-1 to III-4 in
full**, including the per-organ ¹⁴C time course with **blood, muscle and fat**, which neither the RED
nor the SERA assessment carried. From those tables:

- **Vd = 0.20–0.34 L/kg** and **CL = 48–107 mL/h/kg**, derived two independent ways.
- Blood **7.8–9.5 µM** one hour after 5 mg/kg orally.
- Tissue:blood at 1 h — kidney **3.46**, liver 0.78, lung 0.68, heart 0.44, spleen 0.23, **muscle 0.16**,
  **brain 0.14**, **fat 0.00**.
- And the safety margin turns out to be **algebraically independent of the absorbed fraction**.

So the P0 is closed on the parameters that mattered. What the MRID would still add — a true intravenous
concentration–time curve, and the 15-day repeat-dose kinetics — would tighten the estimate but no longer
changes the design. **It is demoted to P3.**

### WHAT IS ACTUALLY LEFT

| P1 | **rollema2025 full text** (Int J Pharm, PMID 39909155). | To adjudicate the tenfold IC₅₀
disagreement with `li1993` — 95 nM versus 970 nM for endothall against PP2A. The atlas has taken li1993
as primary (CORR-136), but that decision rests on reading only rollema2025's abstract. The methods and
substrate would settle it. |

| P2 | **A dry-weight fraction for rat whole blood**, or the Soo 1967 paper itself with wet-weight
concentrations. | The one assumption in the Vd/CL derivation that does *not* cancel; worth about 20 % on
the margin. Soo et al. 1967 has still not been located as a primary paper — SERA cites "Table III,
p. 1020" without a journal that this atlas could resolve. |

| P3 | **MRID 42169502** IV concentration–time curve and 15-day repeat-dose kinetics. | Would replace a
derivation with a measurement. No longer blocking. |

| P3 | **Pump behaviour at 37 °C over 42 days with endothall specifically** — stability and delivery-rate
verification. | The only untested logistical assumption left in the protocol. |

### AND THE THREE THINGS THAT ARE STILL BENCH WORK, UNCHANGED

1. Does **endothall itself** block FGF-induced NPR2 dephosphorylation? Never tested — and now that the
   atlas is recommending endothall over LB-100, this is the single highest-value experiment in the thread.
2. **Cartilage concentration** at a given plasma concentration. Best proxy now available: muscle at 0.16
   of blood, with a predicted further 3–7× Donnan penalty for a dianion in an anionic matrix.
3. Does continuous endothall change a **bone length** in a growing animal.

---

## Round 139 — four of five closed without a download; here is what is genuinely left

Before asking for more, I chased all five items myself. **Four are closed.**

- **Soo et al. 1967 — IDENTIFIED EXACTLY.** SERA's bibliography line, matched against CrossRef:
  **Soo Alexander, Tinsley Ian J, Fang Sheng Chung. "Metabolism of endothall-14C in rats."
  *J Agric Food Chem* 1967;15(6):1018–1021. DOI 10.1021/jf60154a030.** Not indexed in Europe PMC
  (which is why `addref.py` refused the DOI) and not open access (Unpaywall: no OA locations).
- **The IC₅₀ dispute — SETTLED without rollema2025.** The 90 nM figure in circulation traces to a
  dropped digit from li1993's 970 (CORR-138), confirmed by li1993's own stated 5-fold PP2A:PP1 ratio.
- **The blood dry-weight fraction — RETIRED.** Bounded from inside the source by cross-checking Soo's
  two tables against each other (CORR-139).
- **Pump stability — RETIRED.** It is a bench step the manufacturer expects the investigator to run,
  not a document (CORR-139).

### WHAT IS ACTUALLY LEFT — three items, all verification rather than blocking

| V1 | **Soo et al. 1967** — J Agric Food Chem 15(6):1018–1021, **DOI 10.1021/jf60154a030**. | Everything
this atlas says about endothall distribution is read from that paper's tables **as reproduced in the 1992
EPA document and OCRed from a scan**. The paper itself would (a) verify the OCR'd numbers against the
original, (b) supply anything the EPA adaptation dropped — wet weights, the 24/48/72 h columns, the
lactation arm in detail. **Routes, in order of likely success:** any university library with ACS legacy
access (the whole JAFC back-file is standard); ACS pay-per-view at the DOI; interlibrary loan;
or — the long shot worth one try — **ScholarsArchive@OSU** (`ir.library.oregonstate.edu`, search
"endothall"), because Tinsley and Fang were Oregon State faculty and "Soo Alexander" reads like a
graduate student, so a 1966–67 OSU thesis containing the same data may be deposited free. Their catalogue
is a JavaScript app I cannot scrape; a human search takes ten seconds. |

| V2 | **rollema2025** — Int J Pharm 672:125317, **DOI 10.1016/j.ijpharm.2025.125317**, PMID 39909155.
Closed access, no repository copy (checked Unpaywall and OpenAIRE; Dutch OA mandate did not produce a
deposited manuscript). | **No longer on the critical path.** Its two contributions were the hydrolysis
half-life — independently corroborated at ~5 h by another group — and the IC₅₀, now settled against
li1993. Worth having only to confirm whether its 95 nM was measured or inherited. Cheapest route is an
email to the corresponding author. |

| V3 | **The independent LB-100 hydrolysis / PP5-selectivity paper.** The 2026 RSC review (PMC12772682,
open) says *"Li and coworkers… showed LB-100 readily hydrolyzes in water with only 14 % remaining after
8 h and a half-life of 5 h in plasma"* — its reference 68. I could not resolve that reference from the
OCR of the review's citation list; **Ahanin et al. 2023, Cell Chem Biol (PMID 37527661)** is the most
likely candidate but is unconfirmed. | This would replace a review citation with a primary for the
hydrolysis half-life, which is currently doing real work in the Figure 1F conversion. Low cost: the
review's reference 68 can be read straight off the published article's reference list. |

### AND THE THREE BENCH ITEMS, UNCHANGED

1. Does **endothall itself** block FGF-induced NPR2 dephosphorylation? Never tested.
2. **Cartilage concentration** at a given plasma concentration. Best proxy: muscle at 0.16 of blood.
3. Does continuous endothall change a **bone length** in a growing animal.

---

## Round 139b — the remaining items, chased without email

**V3 RESOLVED.** Reference 68 of the 2026 RSC review, parsed out of its PMC XML: **Li Z, Guo M, Gu M,
Cai Z, Wu Q, Yu J, Tang M, He C, Wang Y, Sun P, You Q, Wang L. "Design and Synthesis of
7-Oxabicyclo[2.2.1]heptane-2,3-dicarboxylic Acid Derivatives as PP5 Inhibitors To Reverse Temozolomide
Resistance in Glioblastoma Multiforme." *J Med Chem* 2024;67(17):15691–15710. DOI
10.1021/acs.jmedchem.4c01304, PMID 39136241.** Closed access; the abstract alone carried the two findings
that mattered (38-fold PP5 selectivity, 82 % oral bioavailability — CORR-141) and corroborated the
hydrolysis half-life. Full text would add the LB-100 stability curve and the full selectivity panel.

**V1 DOWNGRADED — I read the table instead of chasing the paper.** Rendering the scanned Soo Table III-2
at 400 dpi and reading it visually recovered the complete nine-point blood row, which the OCR had
mangled (CORR-140). The number Soo 1967 was wanted for is now transcribed at a resolution where every
digit is unambiguous. What the paper would still add: wet-weight concentrations, the per-animal spread,
and the methods detail. **Verification only.**

Access routes attempted and their outcomes, for the record:
- Unpaywall on DOI 10.1021/jf60154a030 — no OA locations.
- OpenAIRE keyword search — returns the journal article only; **no thesis version exists** in any
  indexed repository.
- ScholarsArchive@OSU (`ir.library.oregonstate.edu`) — the catalogue is a JavaScript app behind bot
  detection; `catalog.json`, the Hyrax `concern` path and a rendered fetch all failed. **A human search
  for "endothall" there is still the one untried route**, and worth ten seconds given Tinsley and Fang
  were OSU faculty.

**V2 rollema2025 — no lawful open copy exists.** Checked Unpaywall, OpenAIRE, and the Dutch OA mandate
route (Schellens is Utrecht). Its two contributions are now both settled elsewhere: the IC₅₀ against
li1993 (CORR-138), the hydrolysis half-life against li2024a. **Off the critical path entirely.**

### WHAT REMAINS — all optional

| Optional | `soo1967` — J Agric Food Chem 15(6):1018–1021, DOI 10.1021/jf60154a030 | wet weights, per-animal spread. ACS legacy access at any university library. |
| Optional | `li2024a` — DOI 10.1021/acs.jmedchem.4c01304 | LB-100 stability curve and the full PPP selectivity panel for the redesigned scaffold. |
| Optional | `rollema2025` — DOI 10.1016/j.ijpharm.2025.125317 | only to see whether its 95 nM was measured or inherited. |

### THE THREE BENCH ITEMS — the only things now standing between the atlas and an answer

1. Does **endothall itself** block FGF-induced NPR2 dephosphorylation?
2. What is the **cartilage** concentration at a given plasma concentration?
3. Does continuous endothall change a **bone length** in a growing animal?

## Round 141 — CNP axis site-and-age verdict

**Cleared this round (read at source, no longer needed):**
- `rua2025` — Real-World Safety and Effectiveness of Vosoritide, Portugal, n=27. PMC12313777, open access.
  Read in full. Changed the round's conclusion (CORR-146).
- `reincke2025` — Real-world Outcome of Vosoritide, Germany, n=34. PMC11932077, open access. Read in full.
  Corrected a unit error (CORR-145).
- `cnpmeta2026` — pooled estimates re-verified word for word against the open-access full text.

**Still outstanding — the four RCTs pooled by `cnpmeta2026` are used only through the pooled estimate:**
the meta-analytic ULS ratio, height Z-score and the age subgroup all currently rest on the review's
arithmetic rather than on four independent source reads. The pooled numbers were verified against the
review's own full text, which is NOT the same as verifying them against the trials. Two of this round's
three defects came from trusting a tabulation, so these should be read at source before any grade here
moves up:
- Savarirayan et al. vosoritide phase 3 (the pivotal RCT)
- the navepegritide (TransCon CNP) phase 2/3 RCT
- the two remaining placebo-controlled trials in the pooled set of four

**Lower priority, would extend rather than check the finding:**
- Albuquerque et al. 2026, PMID 41424367 — a SECOND, independent systematic review and meta-analysis of
  real-world vosoritide outcomes. Useful as an agreement check on the age gradient.
- Any vertebral-body-height (as opposed to canal-dimension) endpoint under CNP-analogue treatment, at any
  age. Nothing found so far measures the growth of vertebral BODIES, which is the compartment this case
  depends on.
