# DOMAIN 08 — SYSTEMIC DISEASE AS NATURAL EXPERIMENT (complete inventory)
**R436 full-concept-space enumeration.** Built entirely from EXTERNAL search (Europe PMC REST, NCBI
eutils esearch/esummary/efetch, GeneReviews via `genereviews[Book]`). No atlas file was read except the
two briefs. Compiled 2026-08-15.

**HOW TO READ THIS FILE**
- Every row carries a DIRECTION. Where a condition is tall-as-a-child but normal-or-short as an adult,
  the row says so — that distinction is the whole point of the CORR-295 correction and it is where
  most of the literature is silently wrong.
- `EVIDENCE` is a PMID I actually retrieved from PubMed/Europe PMC in this session, or `UNVERIFIED`.
  GeneReviews chapters (PMIDs of the form 2030xxxx and later) are **indexes, not primary sources** —
  they are cited where a stable, curated, verifiable anchor was more useful than a random case report.
- Species is HUMAN for every row unless stated; this domain is definitionally human.
- `OBSCURE?` = rarely discussed in the mainstream growth literature. Those rows are the yield.

**SIZE AND COVERAGE.** 280 rows in 18 blocks. **144 rows (51%) are marked OBSCURE.**
A — sex-steroid/oestrogen axis (12) · B — sex-chromosome dosage (10) · C — GH/IGF-1 axis (16) ·
D — thyroid/adrenal/parathyroid/mineral (24) · E — overgrowth syndromes (36) · F — chronic inflammatory (13) ·
G — GI/hepatic/nutritional (14) · H — renal (9) · I — haematology/hypoxia/cardiac (12) ·
J — malignancy/oncology treatment/iatrogenic (20) · K — inborn errors, storage, mitochondrial (23) ·
L — short-stature syndromes outside the dysplasia domain (37) · M — psychosocial/behavioural/environmental (11) ·
N — infection and immunodeficiency (8) · O — residual and cross-cutting (15) · P — the CNP/cGMP axis as a
human dose-response (5) · Q — fetal/perinatal programming (5) · R — pubertal-timing genetics and
hypothalamic lesions (10).

**THE ONE SENTENCE THIS DOMAIN PRODUCES:** *conditions with genuinely excess ADULT height almost all have
normal or DELAYED bone age (they extend the period), while conditions that are tall in childhood and
normal-or-short as adults almost all have ADVANCED bone age (they spend it).* The named exceptions —
pituitary gigantism/X-LAG, SHOX overdosage, NPR2 gain-of-function, NPR3 loss-of-function, Marfan and CATSHL
— are the interesting ones, because each raises height WITHOUT buying it out of the growth period.

---

## MASTER TABLE

| # | CONDITION | DIRECTION | MAGNITUDE IF KNOWN | MECHANISM | REVERSIBLE? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|---|
| | **— A. SEX-STEROID / OESTROGEN AXIS: the engine of the growth PERIOD —** | | | | | | |
| A1 | **Aromatase deficiency (CYP19A1 biallelic LoF), MALE** | **TALLER — excess ADULT height** | Case: 24 y, still growing, open wrist and knee epiphyses, undetectable oestradiol, normal testosterone | No oestrogen made anywhere → the epiphyseal-fusion signal is never delivered → growth period extends indefinitely | **YES — oral oestradiol valerate given expressly to close the epiphyses and stop further growth** | 36504506 | no |
| A2 | Aromatase deficiency, FEMALE | TALLER as adult (short/normal as child; ambiguous genitalia at birth) | UNVERIFIED numerically | Same; plus maternal virilisation in pregnancy | YES, oestrogen | 18448329 (review = index) | no |
| A3 | **Oestrogen resistance, ERα homozygous nonsense (ESR1 C→T codon 157), MALE** | **TALLER — 204 cm** | 204 cm at 28 y; incomplete epiphyseal closure; continued linear growth into adulthood; lumbar BMD −3.1 SD; raised E2/E1, raised FSH/LH | Receptor absent → the oestrogen signal cannot be delivered at ANY ligand concentration | **NO — a 10-fold rise in free oestradiol produced no detectable response. This is the one lesion oestrogen cannot rescue.** | 8090165 | no |
| A4 | Oestrogen resistance, ERα homozygous LoF, FEMALE | height not the presenting feature; delayed puberty, absent breast development, multicystic ovaries, very high oestrogens | adult height UNVERIFIED | Same lesion, female | UNVERIFIED | 23841731 | yes |
| A5 | **17α-hydroxylase / 17,20-lyase deficiency (CYP17A1), "CYP17D" — the rare CAH that runs the OTHER way** | **SHORT as a child, TALL as an adult** | n=88. Bone age delayed ≥2 y in **92.5%**. Final height ≥50th centile in **77%**, ≥90th centile in **39%**, ≤25th centile in only **8%**. Tall eunuchoid habitus | Combined adrenal AND gonadal sex-steroid failure → no pubertal oestrogen → bone maturation arrested → **extended growth phase**. Mineralocorticoid hypertension is the diagnostic giveaway | Yes, and perversely: replacing the steroids REMOVES the height | 40350803 | **YES — highest-value obscure row in this domain** |
| A6 | Congenital hypogonadotropic hypogonadism / Kallmann (untreated) | TALLER, **eunuchoid** (arm span > height, reduced upper:lower segment) | Eunuchoid proportions formally measured vs Klinefelter | No gonadal sex steroid → delayed epiphyseal fusion; legs keep growing after trunk stops | YES — sex-steroid induction closes the window; late induction costs proportion | 20301509 (GeneReviews, index) | no |
| A7 | Complete androgen insensitivity syndrome (AR LoF, 46,XY) | TALLER than female norms, **shorter than male norms** | Adult height intermediate between female and male reference | Y-linked/SHOX dosage and residual growth retained; androgen-specific growth contribution lost; aromatisation preserved so fusion still occurs | n/a | 20301602 (GeneReviews, index) | no |
| A8 | 5α-reductase 2 deficiency (SRD5A2) | height near-normal; **DHT-dependent growth contribution isolated** | UNVERIFIED | Testosterone→DHT conversion lost; aromatisation intact so oestrogen-driven fusion is normal | n/a | UNVERIFIED (no GeneReviews chapter returned) | yes |
| A9 | **Central precocious puberty, UNTREATED** | **SHORTER adult height despite tall childhood** | Commonest secondary cause of childhood tall stature: CMI 1/894 girls by age 8 | Early oestrogen → accelerated bone maturation → premature fusion → the classic tall-child/short-adult trade | YES — GnRH analogue restores adult height when started early | 40233073 | no |
| A10 | Peripheral precocious puberty (McCune-Albright, testotoxicosis, adrenal/gonadal tumours) | SHORTER adult height | Aromatase inhibitor / letrozole used specifically to protect adult height | Autonomous sex-steroid production → same trade as A9, GnRHa ineffective because it is gonadotropin-independent | Partially — aromatase inhibitor + antiandrogen | 41947100 | no |
| A11 | Delayed puberty / constitutional delay | transiently short, adult height usually normal-to-slightly-reduced | — | Growth period extended but growth VELOCITY low; the two roughly cancel | spontaneous | UNVERIFIED | no |
| A12 | Hypogonadism acquired in adolescence (e.g. post-chemo, post-orchidectomy) | TALLER with eunuchoid proportions if untreated | — | Same as A6 | Yes | UNVERIFIED | no |
| | **— B. SEX-CHROMOSOME DOSAGE —** | | | | | | |
| B1 | **Klinefelter syndrome 47,XXY** | **TALLER — and adult height IS above midparental target** | Commonest primary tall-stature disorder in a 1.14 M-child Finnish birth cohort (CMI 1/2146 boys). Disease-specific growth charts now exist | Extra copy of **SHOX** in the pseudoautosomal region (dosage-sensitive, escapes X-inactivation) — the leg segment lengthens; hypogonadism adds delayed fusion on top | Partly — testosterone induction normalises proportion, not the SHOX effect | 41198007; 40233073 | no |
| B2 | **Sex-chromosome aneuploidy generally — the dose-response is NON-LINEAR** | mixed | Median height SDS by karyotype (n=305): 45,X **−2.6**; 46,XX male **−1.2**; 47,XXX **+0.7**; 48,XXXX **−0.6**; 49,XXXXY **−1.8** | Height rises with extra X or Y **up to a point and then falls** — SHOX dosage is not the whole story; higher-grade aneuploidy adds a general dysmorphogenetic penalty | no | 20425825 | **YES** |
| B3 | 47,XXX (triple X) | TALLER | median +0.7 SDS (n=40) | SHOX overdosage | no | 20425825 | no |
| B4 | 47,XYY | TALLER | tall stature is a recognised feature; magnitude UNVERIFIED here | SHOX overdosage + Y-linked growth genes | no | 40388606 (X/Y dosage → height dimorphism) | no |
| B5 | 48,XXYY / 48,XXXY | TALLER (48,XXYY notably so) | UNVERIFIED numerically in this session | SHOX dosage; 48,XXYY often taller than 47,XXY | no | 38193351 (index) | yes |
| B6 | 49,XXXXY | **SHORTER** — the aneuploidy series inverts | median −1.8 SDS | Beyond ~4 sex chromosomes the dysmorphogenetic burden overwhelms SHOX dosage | no | 20425825 | **YES** |
| B7 | **SHOX overdosage from Xp duplication / X;autosome translocation in an otherwise 45,X or structurally abnormal X** | TALLER | Reported as tall stature in Turner-karyotype patients — i.e. the SAME syndrome can present tall | Three functional SHOX copies | no | 26191517; 20689243; 11134233 | **YES** |
| B8 | Turner syndrome 45,X | SHORTER | classically ~20 cm below target | SHOX haploinsufficiency + ovarian failure (no pubertal spurt) + skeletal dysplasia component | Partially — GH ± oxandrolone ± oestrogen | 42039118 (cohort, index) | no |
| B9 | 46,XX male | SHORTER | median −1.2 SDS | Loss of Y-linked growth contribution with male gonadal development | no | 20425825 | yes |
| B10 | SHOX deficiency / Léri-Weill dyschondrosteosis / Langer mesomelic dysplasia | SHORTER, mesomelic | — | SHOX haploinsufficiency (LWD) or nullizygosity (Langer) | GH partially | 20301394 (GeneReviews, index) | no |
| | **— C. GH / IGF-1 AXIS —** | | | | | | |
| C1 | Isolated GH deficiency (GH1, GHRHR, pituitary transcription factor defects) | SHORTER | severe; largely correctable | No GH → no hepatic/local IGF-1 → low proliferation and low hypertrophic volume | YES, rhGH — the reference reversible cause | 5288779 (historical GH series, index) | no |
| C2 | **GH insensitivity / Laron syndrome (GHR LoF)** | SHORTER | severe; rhGH useless, rhIGF-1 partly effective | Receptor absent → GH signal never reaches IGF-1 production | Partially — mecasermin (rhIGF-1) | 17192294 | no |
| C3 | STAT5B deficiency | SHORTER + immunodeficiency | severe GH insensitivity phenotype | Post-receptor block of GHR→JAK2→STAT5B→IGF1 | Partially — rhIGF-1; GH ineffective | 40868191 (review = index) | no |
| C4 | IGFALS (acid-labile subunit) deficiency | SHORTER, mildly | mild for the magnitude of the biochemical defect | Ternary complex cannot form → circulating IGF-1 half-life collapses **but local IGF-1 is intact**, which is why the height effect is mild | poorly GH-responsive | 41811044; 39060265 | **YES — the mildness is the informative part** |
| C5 | **PAPPA2 deficiency** | SHORTER | — | Protease that liberates IGF-1 from IGFBP-3/-5 is lost → **total IGF-1 high, FREE IGF-1 low** | rhIGF-1 / rhPAPP-A2 experimental | 34944082 (review = index); 38589872 (mouse) | **YES** |
| C6 | IGF1 gene deletion / homozygous LoF | SHORTER + IUGR + sensorineural deafness + microcephaly | severe, prenatal onset | Ligand absent; the prenatal component proves IGF-1 acts before GH does | Partially — rhIGF-1 | 38952118 (IGF1 haploinsufficiency cohort) | no |
| C7 | IGF1R haploinsufficiency / 15q26 deletion | SHORTER, SGA, postnatal failure to catch up | — | Receptor dosage | GH partially (supraphysiological) | 42130906; 41242745 | no |
| C8 | **15q26 DUPLICATION (IGF1R trisomy)** | **TALLER** | — | Extra IGF1R copy — the mirror of C7 and one of very few dosage-based tall phenotypes | no | 42130906 | **YES** |
| C9 | **Acromegaly (adult-onset GH excess, plates closed)** | **NOT taller** — acral/appositional growth only | zero longitudinal gain | Plates fused ⇒ GH cannot lengthen bone; it thickens it. **The cleanest human demonstration that GH acts only through an open plate** | n/a | 41965096 (index) | no |
| C10 | **Pituitary gigantism (GH excess with OPEN plates)** | **TALLER — the largest documented human heights** | Cohort comparisons of gigantism vs acromegaly exist (n≈3244 pooled) | GH/IGF-1 excess before epiphyseal fusion | Yes — somatostatin analogues, pegvisomant, surgery arrest it | 41965096; 37891382 | no |
| C11 | **X-linked acrogigantism (X-LAG; Xq26.3 microduplication, GPR101)** | **TALLER — the most extreme early-onset overgrowth known** | Onset in INFANCY; a TADopathy | Duplication creates a neo-TAD placing GPR101 under a pituitary enhancer (VGLL1 region) → constitutive GH excess from infancy | Yes if treated early | 38696651; 40684399 | no |
| C12 | AIP-mutated familial isolated pituitary adenoma | TALLER (gigantism in a subset) | — | AIP LoF predisposes to early aggressive somatotroph adenoma | Yes | 22720333 (GeneReviews); 39391823 | no |
| C13 | Carney complex (PRKAR1A) | TALLER (acromegaly/gigantism subset) | — | Loss of PKA regulatory subunit → constitutive cAMP → somatotroph hyperplasia | Yes | 20301463 (GeneReviews) | yes |
| C14 | MEN1 | TALLER (rare gigantism subset) | — | Somatotroph adenoma | Yes | 20301710 (GeneReviews) | yes |
| C15 | **McCune-Albright syndrome (mosaic GNAS activating)** | **BOTH directions in one disease** — GH excess → tall; precocious puberty → short adult height; fibrous dysplasia deforms | — | Mosaic Gsα activation: somatotroph GH excess vs autonomous gonadal steroid | Partially | 42006260; 41947100 | no |
| C16 | GHRH-secreting neuroendocrine tumour (ectopic acromegaly/gigantism) | TALLER if plates open | rare | Peripheral GHRH drives somatotroph hyperplasia | Yes | UNVERIFIED | yes |
| | **— D. THYROID, ADRENAL, PARATHYROID, MINERAL —** | | | | | | |
| D1 | Congenital / acquired hypothyroidism | SHORTER, severely, with **profoundly delayed bone age** | catch-up often incomplete if diagnosed late; **pubertal-onset worst** | T3 is required for hypertrophic differentiation; plate stalls | Largely — levothyroxine; but late treatment leaves a permanent deficit | 41960511 (review = index) | no |
| D2 | **Hyperthyroidism / thyrotoxicosis in childhood** | **TALLER as a child, NORMAL-to-SHORTER as an adult** | 3rd commonest secondary tall-stature diagnosis in the Finnish cohort (CMI 1/936 girls) | Excess T3 accelerates BOTH growth velocity AND bone maturation — the trade is roughly neutral or negative | Yes — antithyroid therapy | 40233073 | no |
| D3 | Congenital non-autoimmune hyperthyroidism (activating TSHR) | TALLER as child, advanced bone age, craniosynostosis | — | Constitutive TSHR → autonomous T3 | Partially | 41216432 | yes |
| D4 | **MCT8 deficiency (SLC16A2, Allan-Herndon-Dudley)** | SHORTER + failure to thrive, with **tissue-selective thyrotoxicosis** | — | Thyroid hormone transporter defect: brain hypothyroid, periphery thyrotoxic — one hormone, two opposite tissue states | Partially — TRIAC/Triac trials | 20301789 (GeneReviews); 41508830 | **YES** |
| D5 | Cushing syndrome / disease in childhood | SHORTER with weight gain (the pathognomonic decoupling) | — | Glucocorticoid excess suppresses GH secretion, IGF-1 action, and directly inhibits chondrocytes | Substantially after cure, but catch-up often incomplete | 23640970; 29754644 | no |
| D6 | Exogenous glucocorticoid (systemic, chronic, any indication) | SHORTER, dose-dependent | — | Same as D5, iatrogenic | Partly on withdrawal | 39860393 | no |
| D7 | **Inhaled corticosteroid, childhood asthma — CAMP RCT** | **SHORTER by 1.2 cm in ADULT height** | budesonide 400 µg/d for 4–6 y → adult height **−1.2 cm (95% CI −1.9 to −0.5)**, non-progressive, established within 2 y; −0.1 cm per µg/kg/day of first-2-year dose | Prepubertal growth-velocity suppression that is never made up | **NO — the deficit is permanent, not progressive** | 22938716 | no |
| D8 | Inhaled budesonide, observational (Agertoft/Pedersen) | NO adult-height effect | adult height +0.3 cm vs target (95% CI −0.6 to +1.2) | — | — | 11027740 | no |
| D9 | 21-hydroxylase CAH, classic | TALL as child (androgen excess), **SHORTER as adult** | adult height typically below target despite tall childhood | Adrenal androgen → aromatisation → advanced bone age → premature fusion; and glucocorticoid treatment itself suppresses growth. **A two-sided iatrogenic/endogenous squeeze** | Partially — better with lower GC dose ± aromatase inhibitor | 20301350 (GeneReviews) | no |
| D10 | **17α-hydroxylase CAH** | see A5 — the CAH that makes people TALL | — | — | — | 40350803 | **YES** |
| D11 | P450 oxidoreductase deficiency (POR) | SHORTER, skeletal (Antley-Bixler) | — | Combined CYP17A1/CYP21A2/CYP19A1 dysfunction + sterol synthesis (POR is also the obligate donor for CYP51A1) | no | 20301592 (GeneReviews) | yes |
| D12 | **Familial glucocorticoid deficiency (MC2R, MRAP, NNT, STAR, TXNRD2)** | **TALL as a child with ADVANCED bone age; adult height UNVERIFIED and likely NOT above target** | Tall stature +2.41 SD with **advanced bone age** in one documented case; height normalises on hydrocortisone | Cortisol deficiency removes glucocorticoid growth suppression → tall child. **The measured mechanism is the reflex ACTH rise driving OESTRADIOL**: one patient had E2 raised for age (21.3 pg/mL) that FELL on dexamethasone suppression, with bone age advanced ~6 y at CA 4y9m | **YES — hydrocortisone normalises the excess growth**, and patients whose ACTH is well suppressed on replacement are of NORMAL height | 11012566; 15673970; 19558534 | **YES** |
| D13 | Pseudohypoparathyroidism 1A / Albright hereditary osteodystrophy (GNAS LoF) | SHORTER + brachydactyly | — | Reduced Gsα/cAMP signalling in the plate; **premature epiphyseal closure** is part of the phenotype | no | 29072892 (GeneReviews) | no |
| D14 | Acrodysostosis 1 (PRKAR1A GoF) / 2 (PDE4D) | SHORTER + brachydactyly | ACRDYS2 reported at −4.81 SDS in one description | Reduced PKA output (direction of PDE4D lesion is contested) | no | 29072892 (adjacent index) | yes |
| D15 | Jansen metaphyseal chondrodysplasia (PTH1R constitutive activation) | SHORTER, severely, with misshapen metaphyses | — | Ligand-independent Gsα/cAMP — **the OPPOSITE lesion to D13 and it also shortens: cAMP is a band** | no | UNVERIFIED | yes |
| D16 | Primary hyperparathyroidism in adolescence | usually neutral; rickets-like changes | — | — | Yes, parathyroidectomy | UNVERIFIED | yes |
| D17 | Hypoparathyroidism / hypocalcaemia | SHORTER via rickets-equivalent | — | Failure of mineralisation at the chondro-osseous junction | Yes | UNVERIFIED | no |
| D18 | **X-linked hypophosphataemia (PHEX; FGF23 excess)** | SHORTER, disproportionate (lower-limb dominant) | — | FGF23 excess → renal phosphate wasting → defective mineralisation of hypertrophic cartilage; FGF23 also acts on the plate directly | **YES — burosumab (anti-FGF23) improves growth; a rare fully druggable systemic cause** | 22319799 (GeneReviews) | no |
| D19 | Nutritional / vitamin-D-deficiency rickets | SHORTER, bowing | — | Failure of hypertrophic-zone mineralisation and vascular invasion | Yes, fully | UNVERIFIED | no |
| D20 | Vitamin-D-dependent rickets 1A (CYP27B1), 1B (CYP2R1), 2A (VDR) | SHORTER | — | Calcitriol synthesis/receptor failure | 1A/1B yes with calcitriol; 2A partially with high-dose calcium | UNVERIFIED | no |
| D21 | **Hypophosphatasia (ALPL)** | SHORTER; perinatal forms lethal | — | Tissue-nonspecific alkaline phosphatase loss → PPi accumulates → mineralisation blocked | **YES — asfotase alfa (enzyme replacement)** | 20301329 (GeneReviews) | no |
| D22 | Hereditary hypophosphataemic rickets with hypercalciuria (SLC34A3) | SHORTER | — | Phosphate wasting without FGF23 excess | Yes, phosphate | UNVERIFIED | yes |
| D23 | Distal renal tubular acidosis (ATP6V1B1/ATP6V0A4/SLC4A1) | SHORTER, sometimes severely | — | Chronic metabolic acidosis: buffers bone mineral, suppresses GH/IGF-1 axis and impairs plate function | **YES — alkali therapy restores growth; among the most reversible causes known** | 41897147 | **YES** |
| D24 | Proximal RTA / Fanconi syndrome (any cause) | SHORTER | — | Acidosis + phosphate wasting + rickets | Partly | UNVERIFIED | no |
| | **— E. OVERGROWTH SYNDROMES (the CORR-295 hunting ground) —** | | | | | | |
| E1 | **Sotos syndrome (NSD1 haploinsufficiency)** | TALL as a child with **ADVANCED bone age**; **adult height frequently within the normal range** | disease-specific growth charts now published (Korean cohort) | H3K36 methyltransferase loss → prenatal/early-childhood overgrowth and macrocephaly. **Advanced bone age spends the growth period — this is the class trade** | no | 20301652 (GeneReviews); 39494594 | no — but the adult-height caveat IS obscure |
| E2 | **Weaver syndrome (EZH2 heterozygous missense)** | TALL as child, advanced bone age; adult height variable | — | PRC2 catalytic subunit; H3K27me3 loss | no | 23865096 (GeneReviews); 40922349 | no |
| E3 | **Cohen-Gibson syndrome (EED)** | TALL, Weaver-like | — | PRC2 core subunit | no | 25787343; 28229514 | **YES** |
| E4 | **Imagawa-Matsumoto syndrome (SUZ12)** | TALL, Weaver-like | — | PRC2 core subunit — three PRC2 genes, one phenotype | no | 28229514; 30019515 | **YES** |
| E5 | Tatton-Brown-Rahman syndrome (DNMT3A) | TALL + macrocephaly + ID | — | DNA methyltransferase 3A LoF; also a clonal-haematopoiesis gene | no | 35771960 (GeneReviews) | no |
| E6 | Luscan-Lumish syndrome (SETD2) | TALL + macrocephaly | — | H3K36 methyltransferase — same mark as NSD1 | no | 34978780 (GeneReviews) | yes |
| E7 | **Rahman syndrome (HIST1H1E / H1-4)** | overgrowth + **accelerated epigenetic ageing** | — | Linker histone frameshift produces a toxic C-terminus | no | UNVERIFIED for stature magnitude | yes |
| E8 | **Beckwith-Wiedemann spectrum (11p15 imprinting: IC1 GoM, IC2 LoM, CDKN1C, UPD)** | TALL/overgrown in infancy; **often lateralised; adult height usually normal** | — | IGF2 dosage up and/or CDKN1C dosage down at the imprinted 11p15 locus | Growth normalises spontaneously by mid-childhood | 20301568 (GeneReviews); 29377879 | no |
| E9 | **Simpson-Golabi-Behmel syndrome type 1 (GPC3)** | TALL, prenatal onset, coarse features | Adult case described as mimicking acromegaly | Glypican-3 loss — a **cell-surface HS proteoglycan** that normally restrains IGF2/hedgehog/BMP; the layer, not the receptor | no | 20301398 (GeneReviews); 42220602 | no |
| E10 | Perlman syndrome (DIS3L2) | overgrown, high neonatal mortality, Wilms risk | — | Exoribonuclease that degrades **LET-7-uridylated pre-miRNAs** → LIN28/let-7 axis | no | 38161545; 40481679 | yes |
| E11 | **PIK3CA-related overgrowth spectrum (PROS) — CLOVES, MCAP, Klippel-Trénaunay, macrodactyly, HHML** | SEGMENTAL/mosaic overgrowth, not global tall stature | — | Post-zygotic activating PIK3CA → PI3K/AKT/mTOR | **YES — alpelisib (PI3Kα inhibitor) has real-world evidence in >100 patients** | 23946963 (GeneReviews); 42121892 | no |
| E12 | Proteus syndrome (AKT1 p.E17K mosaic) | progressive, disorganised, asymmetric overgrowth | — | Mosaic AKT1 activation | Partially — miransertib (AKT inhibitor) in trials | 22876373 (GeneReviews); 42224880 | no |
| E13 | PTEN hamartoma tumour syndrome (Cowden, Bannayan-Riley-Ruvalcaba) | TALL + macrocephaly | Macrocephaly is near-invariant; tall stature common | Loss of the PI3K brake | no | 20301661 (GeneReviews); 39256443 | no |
| E14 | PPP2R5D-related / PP2A-opathies (PPP2R5D, PPP2R1A, PPP2CA) | macrocephaly, overgrowth in a subset | — | PP2A is a PI3K/AKT phosphatase | no | 26576547; 29296277 | **YES** |
| E15 | **Malan syndrome (NFIX haploinsufficiency)** | TALL, Sotos-like, macrocephaly | — | NFI transcription factor haploinsufficiency (frameshifts → proteasomal degradation) | no | 39083629 (GeneReviews); 41282483 | yes |
| E16 | **Marshall-Smith syndrome (NFIX, exon 6-10 dominant-negative)** | **ACCELERATED bone maturation with FAILURE TO THRIVE — the same gene, the opposite growth outcome to E15** | — | Different NFIX allele class → different mechanism | no | 39014953; 37336770 | **YES — one gene, two opposite growth phenotypes, sorted by allele class** |
| E17 | Tenorio syndrome (RNF125) | overgrowth + macrocephaly + ID | — | E3 ubiquitin ligase | no | 25196541 | **YES** |
| E18 | Nevo syndrome | overgrowth + kyphoscoliosis; **shown to be ALLELIC to kyphoscoliotic EDS (PLOD1)** | — | Lysyl hydroxylase 1 loss — a collagen cross-linking enzyme presenting as an overgrowth syndrome | no | 15666309 | **YES** |
| E19 | CHD8-related neurodevelopmental disorder | TALL + macrocephaly + ASD | — | Chromatin remodeller; also a Wnt regulator | no | 24998929; 26733790 | yes |
| E20 | HERC1-related MDFPMR (macrocephaly, dysmorphic facies, psychomotor retardation) | overgrowth/macrocephaly | — | E3 ubiquitin ligase; HERC1 regulates mTOR pathway components | no | 39891458 | **YES** |
| E21 | **Fragile X syndrome (FMR1)** | TALL in childhood (with macroorchidism), adult height near normal-to-low | — | — | no | 20301558 (GeneReviews) | yes |
| E22 | **Marfan syndrome (FBN1)** | **TALL — and DISPROPORTIONATE: dolichostenomelia, arm span > height, reduced upper:lower segment** | 2nd commonest primary tall-stature diagnosis in the Finnish cohort (≈1/4300 girls, 1/5200 boys) | Fibrillin-1 loss → **release of matrix-sequestered TGF-β** at the perichondrium/periosteum → limb overgrowth. **NOT a growth-plate-intrinsic mechanism** | no; beta-blocker/losartan target the aorta not the height | 20301510 (GeneReviews); 40233073 | no |
| E23 | Congenital contractural arachnodactyly / Beals (FBN2) | TALL, arachnodactyly, contractures | — | Fibrillin-2 — the fetal paralogue of FBN1 | no | 20301560 (GeneReviews) | yes |
| E24 | Loeys-Dietz syndrome (TGFBR1/2, SMAD3, TGFB2, TGFB3) | TALL/marfanoid in a subset | — | **Paradoxically INCREASED tissue TGF-β signalling despite LoF receptor alleles** — the direction is genuinely contested | no | 20301312 (GeneReviews); 22772368 | no |
| E25 | Shprintzen-Goldberg syndrome (SKI) | marfanoid + craniosynostosis + ID | — | SKI is a TGF-β/SMAD repressor | no | 23023332 | yes |
| E26 | **Classical homocystinuria (CBS deficiency)** | **TALL, marfanoid, with osteoporosis and scoliosis** | — | Homocysteine disrupts fibrillin/collagen cross-linking → a phenocopy of Marfan by a metabolic route | **YES — pyridoxine-responsive subset; height is prevented by early treatment** | 20301697 (GeneReviews); 42255525 | no |
| E27 | Homocystinuria due to MTHFR deficiency | tall/marfanoid variably; neurological dominant | — | Same metabolite, different enzyme | Partially, betaine | 40440437 (GeneReviews) | yes |
| E28 | **MEN2B (RET p.M918T)** | **marfanoid habitus** + mucosal neuromas + MTC | — | Constitutive RET tyrosine kinase; the skeletal mechanism is unexplained | no | 20301434 (GeneReviews); 41961175 | yes |
| E29 | Lujan-Fryns syndrome (MED12) | marfanoid habitus + XLID | — | Mediator complex subunit | no | 19377476 (screen, index) | **YES** |
| E30 | **Cantú syndrome (ABCC9 / KCNJ8 gain of function)** | TALL/large, hypertrichosis, osteochondrodysplasia, cardiomegaly | — | K-ATP channel GoF → vasodilation and generalised tissue overgrowth. **A CHANNELOPATHY presenting as overgrowth** | Minoxidil-like pharmacology is the causal analogue; glibenclamide proposed | 25275207 (GeneReviews) | **YES** |
| E31 | **Whole-gene PTCH1 deletion in syndromic tall stature** | TALL | found in exome cohort of syndromic tall stature | Loss of the hedgehog receptor/brake → derepressed hedgehog | no | 40577202 | **YES** |
| E32 | **Whole-gene SST (somatostatin) deletion in syndromic tall stature** | TALL | same cohort | Loss of the GH-inhibiting hypothalamic peptide | no | 40577202 | **YES** |
| E33 | **KDM4A recurrent missense in syndromic tall stature** | TALL (candidate) | two unrelated patients, same rare missense | H3K9/H3K36 demethylase — the eraser side of the Sotos/Weaver mark | no | 40577202 | **YES** |
| E34 | **GRB10 (imprinted growth suppressor)** | candidate for human tall stature; **mouse Grb10 disruption → disproportionate overgrowth, IGF2-INDEPENDENT** | mouse | Adaptor that restrains INSR/IGF1R signalling | no | 40577202 (human candidate); 12829789 (MOUSE) | **YES** |
| E35 | DEPDC5 / GATOR1 LoF found in syndromic tall stature | TALL (with epilepsy) | same cohort | GATOR1 is the mTORC1 brake — loss raises mTORC1 | no | 40577202 | **YES** |
| E36 | Sex-chromosome-independent **familial/constitutional tall stature** | TALL | the commonest cause of tall stature by far, and almost never referred | Polygenic; normal bone age, normal proportions | n/a | 37891382 | no |
| | **— F. CHRONIC INFLAMMATORY DISEASE —** | | | | | | |
| F1 | **Crohn disease, childhood-onset** | SHORTER; permanent adult-height deficit in a substantial minority | growth deficiency is a defining feature; anthropometric divergence begins BEFORE diagnosis | Three simultaneous hits: IL-6/TNF-α act directly on the plate to blunt the IGF-1 response; malabsorption; and glucocorticoid treatment | **Partly — anti-TNF (infliximab) improves height velocity; exclusive enteral nutrition avoids steroids** | 25309059; 39821394; 22772738 | no |
| F2 | Ulcerative colitis, childhood-onset | SHORTER but **much less than Crohn** | — | Mucosal, not transmural; less systemic cytokine load | Yes | 22772738 | no |
| F3 | Juvenile idiopathic arthritis (esp. systemic JIA) | SHORTER; final height deficit | — | IL-6 is the specific culprit in sJIA (IL-6 transgenic animals are growth-retarded and IL-6 blocks chondrogenic differentiation in vitro) | **YES — tocilizumab (anti-IL-6R) restores growth velocity; this is a druggable inflammatory brake** | 33712046; 19535264; 23227116 | no |
| F4 | Systemic lupus erythematosus, childhood-onset | SHORTER | can present WITH growth retardation and delayed puberty | Cytokines + glucocorticoid; renal involvement adds acidosis | Partial | UNVERIFIED (case report index only) | no |
| F5 | Familial Mediterranean fever | growth generally PRESERVED — the informative negative | 1144 children with FMF: growth generally preserved, inflammatory markers inconsistently correlated with growth | Recurrent but self-limited IL-1β bursts do not equal chronic cytokine exposure | colchicine | 20301405 (GeneReviews); primary cohort UNVERIFIED here | **YES — a recurrent-inflammation NEGATIVE** |
| F6 | CAPS / NOMID / Muckle-Wells (NLRP3) | SHORTER (NOMID severe, with patellar overgrowth) | — | Chronic IL-1β; NOMID uniquely causes **epiphyseal/patellar bony overgrowth** while shortening the child | **YES — anakinra/canakinumab** | UNVERIFIED for magnitude | yes |
| F7 | TRAPS (TNFRSF1A) | growth impairment reported | — | Chronic TNF | Partly | 36375008 (GeneReviews) | yes |
| F8 | Chronic non-bacterial osteomyelitis / CRMO | local physeal damage, limb-length discrepancy | — | Metaphyseal inflammatory lesions adjacent to the plate | Partly | UNVERIFIED | yes |
| F9 | Sarcoidosis, paediatric | SHORTER | — | Granulomatous inflammation + glucocorticoid; hypercalcaemia | Partly | UNVERIFIED | yes |
| F10 | Coeliac disease | SHORTER; short stature can be the ONLY presenting sign | — | Villous atrophy → malabsorption; plus a direct inflammatory component | **YES — gluten-free diet gives catch-up; adult height usually normalised if diagnosed before puberty** | 20301720 (GeneReviews); 30891436 | no |
| F11 | Cystic fibrosis | SHORTER historically | — | Pancreatic exocrine insufficiency + chronic infection + CF-related diabetes + steroids | **YES, and dramatically — CFTR modulators (elexacaftor/tezacaftor/ivacaftor) have moved the CF population from underweight/short to a majority normal/overweight** | 41692662; 41300552; 20301428 (GeneReviews) | no |
| F12 | Chronic paediatric asthma (disease itself, untreated) | mild delay, adult height largely normal | — | — | — | 11499850 | no |
| F13 | Atopic dermatitis, severe childhood | adult height reduced in some series | — | Sleep disruption + topical/systemic steroid + inflammation | — | 9245847 | **YES** |
| | **— G. GASTROINTESTINAL, HEPATIC AND NUTRITIONAL —** | | | | | | |
| G1 | Short bowel syndrome / intestinal failure | SHORTER | — | Substrate deficit | Partly with TPN/teduglutide/transplant | UNVERIFIED | no |
| G2 | Alagille syndrome (JAG1, NOTCH2) | SHORTER, disproportionate | growth failure near-universal | Chronic cholestasis → fat/fat-soluble-vitamin malabsorption **plus** a cell-intrinsic NOTCH effect on the plate | Partly after transplant; IBAT inhibitors improve pruritus not necessarily height | 20301450 (GeneReviews) | no |
| G3 | Biliary atresia / chronic cholestasis of any cause | SHORTER | — | Fat-soluble vitamin (esp. D) malabsorption; catabolic state | Partly after Kasai/transplant | UNVERIFIED | no |
| G4 | Chronic liver failure / cirrhosis in childhood | SHORTER, with GH resistance | — | Liver is the source of IGF-1 and IGFBP-3 → acquired GH insensitivity | Yes after transplant | UNVERIFIED | no |
| G5 | Wilson disease | usually neutral; hepatic and renal (Fanconi) contributions possible | — | — | Yes | 20301685 (GeneReviews) | yes |
| G6 | **Environmental enteric dysfunction / tropical enteropathy** | SHORTER — **the largest single cause of short stature on earth by headcount** | population-level stunting; WASH+nutrition RCTs show only modest reversibility | Chronic subclinical enteropathy → nutrient loss + systemic inflammation + GH resistance | **Poorly — large cluster-randomised WASH trials moved diarrhoea more than linear growth** | 25310000; 29396217; 29396219 | no |
| G7 | Soil-transmitted helminthiasis | SHORTER (small effect) | meta-analyses: deworming alone gives little or no height benefit | Nutrient competition + inflammation | Marginally | 18289159; 26202783 | no |
| G8 | Protein-energy malnutrition / marasmus / kwashiorkor | SHORTER | — | Substrate; and GH resistance with high GH, low IGF-1 | Partly, age-dependent | 31767002 | no |
| G9 | **Anorexia nervosa, adolescent onset (especially MALE)** | SHORTER — permanent adult-height deficit | Series: admission height SDS −0.81, adult final height SDS −0.52, **below both premorbid and midparental target**; weight gain >1 kg/y needed for height gain | Energy deficit + hypogonadotropic hypogonadism + GH resistance | **Partly — and only if refeeding happens before fusion. Target weight based on premorbid height centile matters** | 12563050 | **YES — the male-specific stunting is under-recognised** |
| G10 | ARFID / avoidant restrictive food intake disorder | SHORTER | — | Same energy pathway, no body-image component | Partly | UNVERIFIED | yes |
| G11 | **RED-S / exercise-associated amenorrhoea / female athlete triad** | complex: **low energy availability shortens, but hypo-oestrogenism DELAYS fusion** | net effect on adult height UNVERIFIED and probably bidirectional | Two opposing arms in one syndrome | Partly | 25538876 (index) | **YES — the bidirectionality is almost never stated** |
| G12 | Zinc deficiency | SHORTER | — | Zinc is required for IGF-1 action and for many matrix metalloenzymes | Yes, supplementation | UNVERIFIED | no |
| G13 | Iron deficiency anaemia, chronic | SHORTER (modest) | — | O2 delivery + appetite + comorbid enteropathy | Yes | 17158406 (index) | no |
| G14 | Vitamin A deficiency | SHORTER; and vitamin A EXCESS causes premature epiphyseal closure (see J) | — | Retinoid signalling is a band | Yes | UNVERIFIED | yes |
| | **— H. RENAL —** | | | | | | |
| H1 | **Chronic kidney disease in childhood** | SHORTER, severe and stage-dependent | — | Multi-hit: metabolic acidosis, CKD-MBD (secondary hyperparathyroidism, phosphate), **acquired GH resistance** (raised IGFBPs), anorexia, anaemia, steroid exposure post-transplant | **Partly — rhGH is licensed for CKD; alkali therapy; steroid minimisation post-transplant demonstrably preserves growth** | 42282145; 41424077 | no |
| H2 | Distal / proximal renal tubular acidosis | SHORTER; **among the most fully reversible causes** | — | See D23/D24 | YES, alkali | 41897147 | yes |
| H3 | **Nephropathic cystinosis (CTNS)** | SHORTER, severely, with Fanconi + rickets | — | Lysosomal cystine accumulation → proximal tubulopathy | **Partly — cysteamine started early substantially improves growth and delays ESRD; late diagnosis is much worse** | 20301574 (GeneReviews); 40143952; 40877952 | no |
| H4 | **Bartter syndrome (types I–V; SLC12A1, KCNJ1, CLCNKB, BSND, MAGED2)** | SHORTER, with polyuria and failure to thrive | — | Salt wasting → chronic volume depletion; hypokalaemia; prostaglandin excess | Partly — indomethacin + K/Mg repletion | 41828581; 42079331 | no |
| H5 | **Gitelman syndrome (SLC12A3)** | usually normal stature; growth retardation reported in a minority | — | Milder, distal tubule; hypomagnesaemia | Mg/K repletion | 41602896 | yes |
| H6 | Nephrogenic diabetes insipidus (AVPR2, AQP2) | SHORTER + failure to thrive | — | Chronic hypernatraemic dehydration + huge obligate fluid intake displacing calories | Partly — thiazide/amiloride/indomethacin | UNVERIFIED | yes |
| H7 | Central diabetes insipidus (AVP deficiency) | growth failure when part of hypothalamic disease | — | Often coexists with GH deficiency from the same lesion | Yes, desmopressin + GH | UNVERIFIED | no |
| H8 | Nephrotic syndrome, steroid-dependent | SHORTER | — | Glucocorticoid, not the disease | Partly | UNVERIFIED | no |
| H9 | Dent disease / Lowe syndrome (OCRL) | SHORTER with Fanconi and rickets | — | Proximal tubulopathy | Partly | UNVERIFIED | yes |
| | **— I. HAEMATOLOGY, HYPOXIA, CARDIAC —** | | | | | | |
| I1 | **β-thalassaemia major (transfusion-dependent)** | SHORTER; disproportionate with **short trunk** | growth failure is one of the commonest endocrine complications | Four hits at once: chronic anaemia/hypoxia, **iron overload of the pituitary → GH deficiency and hypogonadism**, desferrioxamine toxicity to the spine (a true iatrogenic spondylodysplasia), and zinc deficiency | Partly — chelation, transfusion, GH, sex steroids | 23776848; 19604241; 35928543 | no |
| I2 | **Desferrioxamine-induced spinal dysplasia** | SHORTER, specifically **truncal** | — | Chelator toxicity to the vertebral growth plates at high dose in young children — an iatrogenic cause of a SHORT TRUNK | Yes if dose reduced early | 18505376 (index) | **YES** |
| I3 | α-thalassaemia (HbH) | mild growth effect | — | Anaemia | Yes | 20301608 (GeneReviews) | yes |
| I4 | Sickle cell disease | SHORTER + **delayed puberty**; adult height often catches up partially because of the delayed fusion | — | Chronic haemolysis, hypermetabolism, vaso-occlusion of the epiphyseal supply (also causes avascular necrosis) | Partly — hydroxyurea, transfusion, HSCT | 20301551 (GeneReviews) | no |
| I5 | Diamond-Blackfan anaemia | SHORTER; short stature is part of the syndrome independent of anaemia | — | **Ribosomopathy** — a cell-intrinsic translation defect, not just anaemia; steroids add to it | Partly | 20301769 (GeneReviews); 32702755 | no |
| I6 | Shwachman-Diamond syndrome (SBDS) | SHORTER + metaphyseal dysostosis | — | Ribosome maturation defect + pancreatic insufficiency | Partly | 20301722 (GeneReviews) | no |
| I7 | Fanconi anaemia | SHORTER; short stature in ~most | — | DNA interstrand-crosslink repair failure; plus endocrinopathy (GHD, hypothyroidism) in a large fraction | Partly, GH | 20301575 (GeneReviews) | no |
| I8 | **Cyanotic congenital heart disease** | SHORTER, with catch-up after corrective surgery | — | Chronic hypoxaemia + increased energy expenditure + feeding difficulty; the catch-up after repair is the proof of reversibility | **YES — catch-up after repair** | 33805775 (index) | no |
| I9 | **Chronic high-altitude hypoxia (Andean/Himalayan populations)** | SHORTER, with **relatively SHORTER LIMBS and preserved trunk** | Andean ancestry associated with stature and limb length AT ALTITUDE but not at sea level | Hypoxia acts on the distal, most perfusion-dependent segments; genetic adaptation partly protects | partly, by migration | 23904412; 25960137; 17329275 | **YES — the segment-specific effect is rarely noted** |
| I10 | Bronchopulmonary dysplasia / chronic neonatal lung disease | SHORTER | — | Hypoxia + energy cost of breathing + postnatal steroids | Partly | 31727986 (index) | no |
| I11 | **Obstructive sleep apnoea in childhood** | SHORTER (growth-rate slowdown), **reversed by adenotonsillectomy** | 28 children: mean height +2.93 cm and IGF-1 rise at 3 months post-op **with unchanged calorie intake** | Sleep fragmentation abolishes the nocturnal GH pulse; and the energy cost of obstructed breathing. **GH itself did not change — IGF-1 did** | **YES, and fast** | 29967551 | no |
| I12 | Severe chronic anaemia of any cause | SHORTER | — | O2 delivery | Yes | 17158406 (index) | no |
| | **— J. MALIGNANCY, ONCOLOGY TREATMENT, IATROGENIC —** | | | | | | |
| J1 | **Cranial irradiation (hypothalamic-pituitary axis)** | SHORTER | dose-dependent; GHD is the first axis lost | Hypothalamic somatotroph damage → acquired GHD | Partly, rhGH | 3606177; 2109998 | no |
| J2 | **SPINAL / craniospinal irradiation** | SHORTER, and **specifically TRUNCAL — the vertebral plates are irradiated directly** | **Estimated eventual height loss 9 cm if irradiated at 1 y, 7 cm at 5 y, 5.5 cm at 10 y**; craniospinal group leg-length-minus-sitting-height SDS 1.98 vs 0.545 for cranial-only | Direct radiation destruction of vertebral growth plates; not GH-mediated (which is why GH does not fix it) | **NO — rhGH cannot rescue a destroyed vertebral plate, and giving GH worsens the disproportion** | 3606177; 1931763 | **YES — the single cleanest human demonstration that the trunk and the limbs are separately destructible** |
| J3 | Total body irradiation + HSCT | SHORTER, multi-mechanism | — | GHD + direct plate damage + hypogonadism + thyroid + steroid + GvHD | Partly | 33332189 (index for TBI use); 42244940 | no |
| J4 | Cytotoxic chemotherapy (alkylators, anthracyclines) | SHORTER, modest alone | — | Direct antiproliferative effect on the plate; gonadal failure | Partial catch-up | 25403639 | no |
| J5 | **Vismodegib / hedgehog pathway inhibitors in children** | **SHORTER — IRREVERSIBLE, PROFOUND** | 3 children with medulloblastoma developed **widespread growth-plate fusions persisting long after stopping**, profound short stature and disproportion, 2 with precocious puberty; only after **>140 days** of exposure. Led to a product-label warning and trial restriction to skeletally mature patients | Hedgehog signalling is REQUIRED to keep the plate open; blocking it fuses it | **NO — permanent** | 29050204 | no (in oncology) / **YES** (outside it) |
| J6 | **Palovarotene (RARγ agonist) in FOP** | SHORTER — **premature physeal closure is the dose-limiting toxicity in growing children** | phase 3 MOVE trial; the paediatric physeal signal drove label restriction | Retinoic acid receptor γ agonism drives premature epiphyseal closure | NO | 36583535; 39677926 | **YES** |
| J7 | Isotretinoin / systemic retinoids in adolescence | SHORTER (premature epiphyseal closure reported), plus hyperostosis | — | Same RAR mechanism as J6 | NO for the fused plate | 3054426; 11606950; 33169909 | yes |
| J8 | Hypervitaminosis A | SHORTER, premature epiphyseal closure | — | Same retinoid axis, nutritional route | — | 3054426 (index) | yes |
| J9 | Chronic systemic glucocorticoid, any indication | SHORTER, dose-dependent | — | See D6 | Partly | 39860393 | no |
| J10 | **Stimulants for ADHD (methylphenidate, amphetamine)** | SHORTER, small; adult-height effect genuinely contested | — | Appetite suppression → energy deficit; possible direct effect | Partly on discontinuation | 29744873; 16040876 | no |
| J11 | Chronic warfarin in a growing child | premature physeal calcification described historically (warfarin embryopathy is prenatal) | — | Vitamin-K-dependent Gla protein (MGP) carboxylation, which restrains cartilage mineralisation | — | UNVERIFIED postnatally | yes |
| J12 | Long-term antiepileptics inducing vitamin D catabolism (phenytoin, phenobarbital, carbamazepine) | SHORTER via drug-induced rickets | — | CYP-mediated 25-OH-D degradation | Yes, vitamin D | UNVERIFIED | yes |
| J13 | Antiretroviral therapy (tenofovir DF) | SHORTER via renal phosphate wasting/osteomalacia | — | Proximal tubular toxicity | Yes, switch to TAF | UNVERIFIED | yes |
| J14 | GnRH analogue for central precocious puberty | **TALLER than untreated** (i.e. protective) | adult height preserved when started early | Removes the premature-fusion drive | this IS the reversal | 40564714 | no |
| J15 | Aromatase inhibitor in boys (anastrozole/letrozole) | **TALLER — the only pharmacological period-extender in routine use** | AI ceiling reported around 1–2 cm over several years | Blocks oestrogen synthesis → delays epiphyseal fusion | this IS the intervention | 41947100 (peripheral PP use) | no |
| J16 | Oestrogen given deliberately to reduce final height in tall girls (historical practice) | SHORTER, by design | — | Accelerates fusion — the exact inverse of J15 | irreversible | UNVERIFIED | **YES — a deliberate human experiment in closing the plate** |
| J17 | Alpelisib for PROS | reduces pathological overgrowth | — | PI3Kα inhibition | this IS the intervention | 42121892 | yes |
| J18 | **Epiphysiodesis (surgical)** | SHORTER, by design, segment-specific | — | Mechanical destruction of a named plate | irreversible by design | UNVERIFIED | no |
| J19 | Distraction osteogenesis / limb lengthening | TALLER, by design | — | Works AFTER fusion; not a plate mechanism | — | UNVERIFIED | no |
| J20 | Cancer cachexia / active malignancy itself | SHORTER | — | Cytokines + catabolism | Partly | 41649677 | no |
| | **— K. INBORN ERRORS, STORAGE, MITOCHONDRIAL —** | | | | | | |
| K1 | **MPS I (Hurler/Hurler-Scheie, IDUA)** | SHORTER, severe, with dysostosis multiplex | growth arrests around 2–3 y in severe forms | Dermatan/heparan sulfate accumulation in chondrocytes and matrix → dysfunctional plate | Partly — HSCT and laronidase change survival more than height | 20301341 (GeneReviews) | no |
| K2 | **MPS IVA (Morquio A, GALNS)** | SHORTER, severely, with a **short trunk** and odontoid hypoplasia | — | Keratan sulfate — the GAG the growth plate actually uses — accumulates | Partly — elosulfase alfa; height response modest | 23844448 (GeneReviews) | no |
| K3 | MPS II (Hunter, IDS) | SHORTER | — | Same GAG class | Partly — idursulfase | 20301451 (GeneReviews) | no |
| K4 | MPS VI (ARSB), VII (GUSB), IIIA-D (Sanfilippo) | SHORTER (III least skeletal) | — | — | Partly | UNVERIFIED per-type here | no |
| K5 | Mucolipidosis II/III (GNPTAB) | SHORTER, severe skeletal | — | Failure to tag lysosomal enzymes with M6P → they are secreted, not delivered | no | 20301728 (GeneReviews) | yes |
| K6 | GM1 gangliosidosis (GLB1) / Morquio B | SHORTER with dysostosis | — | β-galactosidase; keratan sulfate in Morquio B | no | 24156116 (GeneReviews) | yes |
| K7 | Zellweger spectrum (PEX genes) | SHORTER + **chondrodysplasia punctata (stippled epiphyses)** | — | Peroxisome biogenesis failure → plasmalogen deficiency, abnormal epiphyseal calcification | no | 20301621 (GeneReviews) | yes |
| K8 | Rhizomelic chondrodysplasia punctata (PEX7, GNPAT, AGPS) | SHORTER, rhizomelic | — | Plasmalogen synthesis | no | UNVERIFIED | yes |
| K9 | **PMM2-CDG and other congenital disorders of glycosylation** | SHORTER | — | Under-glycosylation of secreted and matrix proteins — including IGFBPs and the proteoglycans | no | 20301289 (GeneReviews); 30740408 | yes |
| K10 | **PGM3-CDG** | SHORTER with **skeletal dysplasia AND severe immunodeficiency** | — | Hexosamine pathway — supplies UDP-GlcNAc for GAG synthesis; links the immune and skeletal phenotypes in one gene | no | 24931394 | **YES** |
| K11 | Glycogen storage disease Ia/Ib (G6PC, SLC37A4) | SHORTER; growth failure a cardinal sign | — | Chronic hypoglycaemia → catabolism; **and GSD Ib adds neutropenia/IBD-like enteropathy** | **YES — uncooked cornstarch and strict metabolic control restore growth; a diet-reversible cause** | 34836082; 40009380 | no |
| K12 | Classical galactosaemia | SHORTER + primary ovarian insufficiency | — | — | Partly | UNVERIFIED | yes |
| K13 | Phenylketonuria, untreated | SHORTER + microcephaly | — | — | Yes, diet | UNVERIFIED | no |
| K14 | Maple syrup urine disease, organic acidaemias (MMA, PA), urea cycle disorders | SHORTER; MMA notably | — | Catabolic crises + protein restriction + (in MMA) CKD | Partly; liver/kidney transplant in MMA | UNVERIFIED | no |
| K15 | Homocystinuria | see E26 — the amino-acid disorder that makes people **TALL** | — | — | Yes | 20301697 (GeneReviews) | no |
| K16 | **Mitochondrial disease (MELAS, Kearns-Sayre, Pearson, mtDNA depletion)** | SHORTER; short stature is a diagnostic red flag | — | ATP deficit in a highly proliferative tissue; **plus multi-endocrine failure (GHD, hypoparathyroidism, diabetes) from the same lesion** | no | UNVERIFIED for magnitude | no |
| K17 | Lysinuric protein intolerance | SHORTER + osteoporosis | — | Cationic amino-acid transport | Partly, citrulline | UNVERIFIED | yes |
| K18 | Cystinuria | neutral | — | — | — | UNVERIFIED | yes |
| K19 | **Prolidase deficiency (PEPD)** | SHORTER + ulcers + dysmorphism | — | Collagen turnover: proline recycling from collagen breakdown fails | no | 26110198 (GeneReviews) | **YES** |
| K20 | Alpha-mannosidosis (MAN2B1) | SHORTER with dysostosis | — | — | Partly, velmanase alfa | 20301570 (GeneReviews) | yes |
| K21 | Menkes disease (ATP7A) | SHORTER, with wormian bones and metaphyseal spurs | — | Copper delivery to lysyl oxidase fails → collagen cross-linking fails. **The human LOX-deficiency experiment** | no | UNVERIFIED | **YES** |
| K22 | Occipital horn syndrome (milder ATP7A) | SHORTER, with occipital exostoses | — | Same axis, milder | no | UNVERIFIED | **YES** |
| K23 | **Congenital NAD deficiency disorder (NADSYN1, HAAO, KYNU)** | SHORTER + vertebral, cardiac, renal, limb defects | — | NAD synthesis from tryptophan; **niacin supplementation prevents it in mice** | prenatally, in principle | 37499065 (GeneReviews) | **YES** |
| | **— L. SHORT-STATURE SYNDROMES NOT IN THE DYSPLASIA DOMAIN —** | | | | | | |
| L1 | Turner syndrome | SHORTER | see B8 | SHOX + ovarian failure + intrinsic dysplasia | Partly | 20301394 (SHOX GeneReviews) | no |
| L2 | **Noonan syndrome and the RASopathies (PTPN11, SOS1, RAF1, RIT1, KRAS, BRAF/CFC, HRAS/Costello, NF1, LZTR1)** | SHORTER | — | **Excess RAS-MAPK signalling — the SAME arm FGFR3 activation uses in achondroplasia**, reached from a different node | Partly, rhGH (licensed in some regions); **MEK inhibitors are being explored** | 20301303 (GeneReviews) | no |
| L3 | Noonan syndrome with multiple lentigines (LEOPARD, PTPN11 dominant-negative) | SHORTER | — | Paradoxically REDUCED phosphatase activity yet a Noonan-spectrum phenotype | — | 20301557 (GeneReviews) | yes |
| L4 | **Neurofibromatosis type 1** | SHORTER (~1 SD below target) plus focal dysplasia (tibial pseudarthrosis, scoliosis) | NF1 pLoF is a recognised height-lowering allele | RAS-MAPK; plus a cell-intrinsic bone effect | no | UNVERIFIED for the SD figure | no |
| L5 | Silver-Russell syndrome (11p15 LoM, mUPD7, IGF2, PLAG1, HMGA2, CDKN1C) | SHORTER, SGA with failure to catch up, asymmetry | — | The imprinted mirror of Beckwith-Wiedemann: IGF2 dosage DOWN | Partly, rhGH | 20301499 (GeneReviews) | no |
| L6 | **Temple syndrome (14q32 imprinting, MEG3/DLK1/RTL1)** | SHORTER + **precocious puberty** — a double hit on adult height | — | Imprinted 14q32; DLK1 loss also causes central precocious puberty | Partly, GH + GnRHa | 41926606 (GeneReviews) | **YES** |
| L7 | Prader-Willi syndrome | SHORTER (with GH deficiency), obese | — | 15q11-13 paternal loss; hypothalamic dysfunction → GHD | **YES — rhGH is licensed and improves adult height and body composition** | 20301505 (GeneReviews); 31333129 | no |
| L8 | 3-M syndrome (CUL7, OBSL1, CCDC8) | SHORTER, severely, prenatal onset | — | A CUL7 ubiquitin-ligase complex; GH-resistant | no | 20301654 (GeneReviews) | yes |
| L9 | Meier-Gorlin syndrome (ORC1, ORC4, ORC6, CDT1, CDC6, GMNN, CDC45, MCM5) | SHORTER, microtia, patellar aplasia | — | **Pre-replication complex — a DNA-replication-licensing disease presenting as growth restriction**: the cell cycle itself is rate-limiting | no | UNVERIFIED (no chapter returned) | **YES** |
| L10 | MOPD type II (PCNT) / microcephalic osteodysplastic primordial dwarfism | SHORTER, extreme, prenatal onset | — | Pericentrin — centrosome/mitotic spindle | no | UNVERIFIED | yes |
| L11 | Seckel syndrome spectrum (ATR, RBBP8, CENPJ, CEP152 …) | SHORTER, extreme, microcephalic | — | DNA damage response / centrosome | no | 20301772 (GeneReviews, RETIRED chapter) | yes |
| L12 | Bloom syndrome (BLM) | SHORTER, proportionate, prenatal onset | — | RecQ helicase; sister-chromatid exchange | no | 20301572 (GeneReviews) | no |
| L13 | Nijmegen breakage syndrome (NBN) | SHORTER + microcephaly + immunodeficiency | — | MRN complex | no | 20301355 (GeneReviews) | yes |
| L14 | Cockayne syndrome (ERCC6/ERCC8) | SHORTER, progressive, cachectic | — | Transcription-coupled nucleotide excision repair | no | 20301516 (GeneReviews) | no |
| L15 | Rothmund-Thomson syndrome (RECQL4) | SHORTER + poikiloderma + radial ray defects | — | RecQ helicase | no | 20301415 (GeneReviews) | yes |
| L16 | Werner syndrome (WRN) | SHORTER — **absence of the pubertal growth spurt is the first sign** | — | RecQ helicase, adult-onset progeroid | no | 20301687 (GeneReviews) | **YES — the spurt failure is the diagnostic clue and is a pure PERIOD phenotype** |
| L17 | Hutchinson-Gilford progeria (LMNA) | SHORTER, severely | — | Progerin | Partly — lonafarnib prolongs life, not height | 20301300 (GeneReviews) | no |
| L18 | Down syndrome (trisomy 21) | SHORTER, with disease-specific charts | — | Multi-gene dosage; plus coeliac, hypothyroidism, congenital heart disease, OSA — **four correctable comorbidities each of which shortens** | Partly, by treating the comorbidities | 22363551; 29135488 | no |
| L19 | 22q11.2 deletion syndrome | SHORTER | — | — | Partly | 20301696 (GeneReviews) | no |
| L20 | Williams syndrome (7q11.23) | SHORTER, with early puberty | — | ELN and neighbours; **hypercalcaemia in infancy** | no | 20301427 (GeneReviews) | no |
| L21 | **Kabuki syndrome (KMT2D, KDM6A)** | SHORTER, postnatal onset | — | **H3K4 methylation WRITER loss shortens — the mirror image of the H3K36/H3K27 overgrowth syndromes.** Chromatin sets height bidirectionally by mark | no | 21882399 (GeneReviews); 33805950 | **YES — the mark-direction symmetry is the point** |
| L22 | Wiedemann-Steiner syndrome (KMT2A) | SHORTER + hypertrichosis cubiti | — | H3K4 writer, same class as L21 | Partly, GH reported | 35617449 (GeneReviews) | yes |
| L23 | Cornelia de Lange syndrome (NIPBL, SMC1A, SMC3, RAD21, HDAC8) | SHORTER, prenatal onset | — | Cohesinopathy | no | 20301283 (GeneReviews) | no |
| L24 | Rubinstein-Taybi syndrome (CREBBP, EP300) | SHORTER, broad thumbs | — | Histone acetyltransferase loss | no | 20301699 (GeneReviews) | no |
| L25 | Floating-Harbor syndrome (SRCAP) | SHORTER + **markedly delayed bone age** + expressive speech delay | — | SNF2-related chromatin remodeller | no | 23193612 (GeneReviews) | yes |
| L26 | Smith-Magenis syndrome (RAI1) | SHORTER | — | — | no | 20301487 (GeneReviews) | yes |
| L27 | CHD7 disorder / CHARGE | SHORTER + hypogonadotropic hypogonadism | — | Chromatin remodeller; the HH gives delayed fusion which partly offsets | Partly | 20301296 (GeneReviews) | no |
| L28 | Aarskog-Scott syndrome (FGD1) | SHORTER, disproportionate, shawl scrotum | — | A Cdc42 GEF | Partly, GH | 41704117 (GeneReviews) | yes |
| L29 | Mulibrey nanism (TRIM37) | SHORTER, prenatal onset, constrictive pericarditis | — | TRIM37 peroxisomal/ubiquitin ligase | no | UNVERIFIED (no chapter returned) | **YES** |
| L30 | Dubowitz syndrome | SHORTER, microcephaly, eczema | — | Heterogeneous; some LIG4 | no | UNVERIFIED | yes |
| L31 | IMAGe syndrome (CDKN1C gain of function) | SHORTER, severe IUGR + adrenal hypoplasia | — | **The exact opposite allele class to Beckwith-Wiedemann CDKN1C loss** — one gene, two directions | no | 24624461 (GeneReviews); 41218602 | **YES** |
| L32 | FAM111A-related (Kenny-Caffey / osteocraniostenosis) | SHORTER + hypoparathyroidism + medullary stenosis | — | — | no | 37023242 (GeneReviews) | **YES** |
| L33 | Mosaic variegated aneuploidy (BUB1B, CEP57, TRIP13) | SHORTER + microcephaly + cancer | — | Mitotic checkpoint | no | UNVERIFIED | yes |
| L34 | Alpha-thalassaemia X-linked ID (ATRX) | SHORTER | — | Chromatin remodeller | no | 20301622 (GeneReviews) | yes |
| L35 | 17q12 recurrent deletion (HNF1B) | variable; renal cysts and diabetes | — | — | — | 27929632 (GeneReviews) | yes |
| L36 | **Aymé-Gripp syndrome (MAF)** | SHORTER + cataract + deafness | — | A MAF transcription-factor disorder | no | 32027476 (GeneReviews) | **YES** |
| L37 | Bryant-Li-Bhoj neurodevelopmental syndrome (H3-3A/H3-3B) | growth abnormality variable | — | Histone H3.3 variants | no | 37782742 (GeneReviews) | **YES** |
| | **— M. PSYCHOSOCIAL, BEHAVIOURAL, ENVIRONMENTAL —** | | | | | | |
| M1 | **Psychosocial short stature / "abuse dwarfism" / reversible hyposomatotropism** | SHORTER, sometimes profoundly | — | Reversible functional hypopituitarism: GH secretion falls in an adverse environment and recovers on removal from it | **YES — and the reversal on change of environment, without any drug, is the diagnostic test** | 857651; 1599303 | **YES** |
| M2 | **Hyperphagic short stature** | SHORTER + hyperphagia, food stealing/hoarding, disturbed attachment | one case: low stimulated GH (3.47 ng/mL) yet only 3 cm/y on 6 months of rhGH | GH-deficient biochemistry that **does not respond to GH** — the axis is downstream-blocked, not deficient | Environment, not GH | 22837929 | **YES — a documented GH-RESISTANT psychosocial state** |
| M3 | Institutional deprivation / severe early neglect | SHORTER, with catch-up on adoption | — | Nutrition + psychosocial + infection | Yes, largely, if early | UNVERIFIED | no |
| M4 | Chronic sleep deprivation (non-OSA) | SHORTER (predicted) | — | GH is secreted in slow-wave sleep | plausibly | UNVERIFIED | yes |
| M5 | Childhood obesity | **TALLER as a child, NORMAL-to-SHORTER as an adult** | — | Hyperinsulinaemia + adipose aromatase → raised oestrogen → advanced bone age → earlier fusion. **The commonest cause of a tall child in an affluent population** | Partly | 20451244 (index) | no |
| M6 | Type 1 diabetes, chronically poorly controlled | SHORTER | — | Portal insulin deficiency → hepatic GH resistance → low IGF-1 despite high GH | Yes, glycaemic control | 42194591; 24648838 | no |
| M7 | **Mauriac syndrome** | SHORTER, extreme, with hepatomegaly, cushingoid features, delayed puberty | — | Extreme insulin deficiency → glycogenic hepatopathy + profound GH resistance | **YES — modern insulin delivery reverses it, documented with automated insulin delivery over 2.5 y** | 41560719; 40904852 | **YES — near-extinct in rich countries, still present where insulin access is limited** |
| M8 | Maternal smoking / prenatal alcohol (FAS) | SHORTER, prenatal onset with poor catch-up | — | — | no | UNVERIFIED | no |
| M9 | Lead / heavy-metal exposure | SHORTER | — | Lead deposits at the metaphysis ("lead lines") and disturbs mineralisation | Partly, chelation | 14223577 (historical, rabbit + human) | yes |
| M10 | Endocrine-disrupting chemical exposure (phthalates, BPA) | earlier puberty → shorter adult height in a subset | — | Oestrogenic/antiandrogenic signalling | — | 26544531 (index) | yes |
| M11 | Secular trend / nutrition transition at population level | **TALLER by up to ~15–20 cm over a century in some populations** | — | Improved early-life nutrition and infection burden — **the largest environmental height effect ever recorded** | — | 25310000 (index) | no |
| | **— N. INFECTION AND IMMUNODEFICIENCY —** | | | | | | |
| N1 | **Perinatally acquired HIV** | SHORTER, with **incomplete catch-up on ART** | growth improves on HAART but often does not fully normalise | Chronic immune activation + enteropathy + comorbid infection + (older regimens) mitochondrial toxicity | Partly | 20691045 | no |
| N2 | Chronic/recurrent malaria | SHORTER (small effect) | — | Anaemia + inflammation | Partly | UNVERIFIED | yes |
| N3 | Tuberculosis, chronic | SHORTER; and spinal TB destroys vertebral bodies directly | — | Cachexia; direct destruction | Partly | UNVERIFIED | no |
| N4 | Chronic granulomatous disease | SHORTER | growth failure is a recognised feature | Chronic granulomatous inflammation + IBD-like colitis | Partly, HSCT | 22876374 (GeneReviews) | yes |
| N5 | X-linked SCID and other combined immunodeficiencies | SHORTER, failure to thrive | — | Chronic infection; **and in some (e.g. cartilage-hair hypoplasia, PGM3) the immune and skeletal defects share one gene** | Yes, HSCT | 20301584 (GeneReviews) | no |
| N6 | IPEX syndrome (FOXP3) | SHORTER, failure to thrive | — | Autoimmune enteropathy + diabetes | Partly, HSCT | 12161590 | yes |
| N7 | Common variable immunodeficiency with enteropathy | SHORTER | — | Malabsorption | Partly | UNVERIFIED | yes |
| N8 | Congenital CMV / congenital rubella / congenital syphilis | SHORTER, prenatal onset; **congenital syphilis produces metaphyseal Wimberger lesions** | — | Direct metaphyseal osteochondritis (syphilis) | no | UNVERIFIED | yes |
| | **— O. RESIDUAL AND CROSS-CUTTING —** | | | | | | |
| O1 | Duchenne muscular dystrophy on chronic glucocorticoid | SHORTER, severely | — | Glucocorticoid + immobilisation + delayed puberty | Partly — the deflazacort/prednisone choice and GH are debated | 29395989 (index) | no |
| O2 | Cerebral palsy / severe neurodisability | SHORTER, often with segment-specific under-growth of the affected limb | — | Nutrition, immobilisation, and **loss of mechanical loading on one side** | Partly | UNVERIFIED | no |
| O3 | Immobilisation / paralysis of a single limb | SHORTER in that limb | — | Local mechanical/vascular | Partly | UNVERIFIED | yes |
| O4 | Chronic pain / chronic fatigue syndromes in adolescence | growth generally preserved | — | — | — | UNVERIFIED | yes |
| O5 | Achondroplasia (FGFR3 GoF) — cross-listed to the dysplasia domain | SHORTER, rhizomelic | — | Constitutive FGFR3 → MAPK; the reference plate-intrinsic disease | **Partly — vosoritide, infigratinib** | 20301331 (GeneReviews) | no |
| O6 | **CATSHL syndrome (FGFR3 LOSS of function)** | **TALLER — camptodactyly, TALL stature, scoliosis, hearing loss** | postnatal tall stature described | The exact inverse allele of achondroplasia; **the human germline validation that lowering FGFR3 lengthens bone — and that it also brings SCOLIOSIS** | n/a | 17033969 (heterozygous FGFR3 p.R621H, partial LOF; phenocopies the Fgfr3-knockout MOUSE) | **YES** |
| O7 | Hereditary multiple exostoses (EXT1/EXT2) | SHORTER + limb-length discrepancy + deformity | — | Heparan sulfate chain synthesis fails → hedgehog/BMP/FGF gradients are not shaped → ectopic perichondrial cartilage | no | 41158744 (management, index) | no |
| O8 | Ollier disease / Maffucci syndrome (mosaic IDH1/IDH2) | SHORTER, asymmetric, with enchondromas | — | 2-hydroxyglutarate inhibits 2-OG dioxygenases including the TET and KDM families → blocked chondrocyte differentiation | no | UNVERIFIED | yes |
| O9 | Fibrous dysplasia / McCune-Albright skeletal component | limb-length discrepancy and deformity rather than global stature | — | Mosaic GNAS in skeletal stem cells | Partly, bisphosphonates/denosumab | 42006260 | no |
| O10 | **Osteopetrosis (TCIRG1, CLCN7, others)** | SHORTER | — | Osteoclast failure → **the hypertrophic cartilage is never resorbed at the chondro-osseous junction: charge without discharge, as a human disease** | Partly, HSCT | 40875877 (GeneReviews) | **YES — the cleanest human demonstration that discharge is required** |
| O11 | CDC73-related hyperparathyroidism-jaw tumour | brown tumours, not stature per se | — | — | — | 20301744 (GeneReviews) | yes |
| O12 | **Turner-like phenotype from SHOX-region enhancer deletions (no coding change)** | SHORTER | — | Non-coding **enhancer** deletions downstream of SHOX reproduce the coding phenotype — regulatory DNA sets stature | no | 20301394 (GeneReviews) | **YES** |
| O13 | Chronic use of proton-pump inhibitors / antacids in childhood | plausible SHORTER via mineral malabsorption | — | — | — | UNVERIFIED | yes |
| O14 | Coeliac-adjacent: cow's milk protein allergy with restrictive diet | SHORTER | — | Nutritional restriction | Yes | UNVERIFIED | yes |
| O15 | **17q12/1q21.1/16p11.2 and other recurrent CNVs** | 16p11.2 deletion associates with obesity and tall-ish; 1q21.1 duplication with macrocephaly | — | Dosage of multiple genes | no | UNVERIFIED for stature direction | yes |
| | **— P. THE CNP / cGMP AXIS AS A HUMAN DOSE-RESPONSE (added after the main sweep) —** | | | | | | |
| P1 | **NPR2 GAIN-of-function (heterozygous p.Val883Met)** | **TALLER** — with scoliosis and macrodactyly of the great toes | three-generation family; **blood cGMP measurably elevated in the patients**; a chondrocyte-targeted transgenic MOUSE reproduced the phenotype | Ligand-independent constitutive cGMP production by the CNP receptor → growth-plate elongation. **Human proof that raising cGMP in cartilage lengthens bone** | n/a | 22870295 | **YES** |
| P2 | **NPR3 (NPR-C) biallelic LOSS-of-function** | **TALLER** — enhanced growth plus connective-tissue abnormalities | — | Loss of the CNP CLEARANCE receptor → more CNP reaches NPR2 → more cGMP. **The same axis reached by removing the sink instead of activating the receptor** | n/a | 30032985 | **YES** |
| P3 | NPR2 biallelic LOSS-of-function | SHORTER — acromesomelic dysplasia, Maroteaux type | — | No cGMP response to CNP | Exogenous CNP restored growth and prevented early plate closure in deficient RATS | 30235256 (RAT); 36779427 (nosology, index) | no |
| P4 | **NPR2 HETEROZYGOUS loss-of-function** | SHORTER — and **PROGRESSIVELY so** | a recognised monogenic cause of otherwise-idiopathic short stature | Half-dose of the receptor. **With P1 and P3 this makes NPR2 a three-point human dose-response curve on one gene** | partly, GH | 25703509; 32720985; 24471569 | no |
| P5 | Natriuretic-peptide clearance in general (NPPC dosage, translocations near NPPC) | TALLER when NPPC dosage rises | reported but not verified in this session | Ligand dosage | n/a | UNVERIFIED | yes |
| | **— Q. FETAL / PERINATAL PROGRAMMING —** | | | | | | |
| Q1 | Infant of a diabetic mother / gestational diabetes | **TALLER at birth (macrosomia)**, normalising postnatally | — | Fetal hyperinsulinaemia — insulin acting as a fetal growth factor through IGF1R | resolves | 33803995; 26069722 | no |
| Q2 | Congenital hyperinsulinism | macrosomic at birth | — | Same mechanism, endogenous and persistent | Partly | 21967988; 29280746 | yes |
| Q3 | Small for gestational age without catch-up (~10% of SGA) | SHORTER, permanently | — | Intrauterine programming of the GH/IGF axis | Partly, rhGH licensed for SGA | UNVERIFIED | no |
| Q4 | Prematurity / extreme low birth weight | SHORTER, partially catching up | — | — | Partly | UNVERIFIED | no |
| Q5 | Placental insufficiency / pre-eclampsia | SHORTER (IUGR) | — | Substrate and O2 delivery; IGF2 and placental function | Partly | 27604528 (index) | no |
| | **— R. PUBERTAL-TIMING GENETICS AND HYPOTHALAMIC LESIONS (added after the main sweep) —** | | | | | | |
| R1 | **MKRN3 loss-of-function (imprinted, paternally expressed)** | TALL as a child, **SHORTER adult height** | the commonest known monogenic cause of familial central precocious puberty | Loss of a hypothalamic BRAKE on GnRH release → early puberty → early fusion. **It sets puberty ONSET, not plate biology** | YES, GnRHa | 23738509 | no |
| R2 | DLK1 loss-of-function (14q32 imprinted) | same trade as R1 | — | Same locus family as Temple syndrome (L6) | YES, GnRHa | 41732517 | yes |
| R3 | KISS1 / KISS1R activating variants | same trade | — | Constitutive kisspeptin signalling | YES, GnRHa | 34649256 (review = index) | yes |
| R4 | **Familial male-limited precocious puberty / testotoxicosis (LHCGR activating, e.g. p.Asp578Tyr)** | TALL as a child, **SHORT adult height** | — | Gonadotropin-INDEPENDENT Leydig activation → testosterone → aromatisation → premature fusion; **GnRHa does not work, which is why it needs an antiandrogen + aromatase inhibitor** | Partly — bicalutamide + a third-generation aromatase inhibitor | 9598734; 8929952; 20713483 | yes |
| R5 | Hypothalamic hamartoma / CNS tumour causing central precocious puberty | TALL child, SHORT adult | — | Ectopic GnRH pulse generator | YES, GnRHa | UNVERIFIED | no |
| R6 | Septo-optic dysplasia / combined pituitary hormone deficiency (HESX1, LHX3, LHX4, SOX2, SOX3, PROP1, POU1F1, OTX2) | SHORTER | — | Developmental hypopituitarism — GHD ± TSH ± gonadotropin deficiency together | Partly, replacement | 19623216; 27828722 | no |
| R7 | **SOX3 dosage — over- AND under-dosage both cause infundibular hypoplasia and hypopituitarism** | SHORTER at both ends | — | A dosage BAND at a single transcription factor | Partly | 15800844 | **YES** |
| R8 | **"Growth without growth hormone" after craniopharyngioma / hypothalamic damage** | normal or even accelerated growth **DESPITE documented GH deficiency**, in the presence of hypothalamic obesity and hyperinsulinaemia | — | Insulin (and possibly leptin) substituting for GH at the growth plate — **a human demonstration that the GH arm is not the only route to normal growth velocity** | Diazoxide/metformin and GLP-1RA target the obesity, not the growth | 21603206; 33026160; 26239246 (indexes; the growth-without-GH phenomenon itself UNVERIFIED at a primary source in this session) | **YES** |
| R9 | Craniopharyngioma itself (pre-treatment) | SHORTER | — | Mass effect on the hypothalamic-pituitary axis | Partly | 31652121 | no |
| R10 | Post-traumatic / post-infectious hypopituitarism in childhood | SHORTER | — | Acquired GHD | Partly | UNVERIFIED | yes |

---

## PROSE 1 — EVERY CONDITION WHOSE PHENOTYPE IS EXCESS HEIGHT, RANKED BY MAGNITUDE, WITH ITS MECHANISM

Ranked by the size of the height excess actually documented in humans. The mechanism column is the
discriminating information: **almost every large excess-height phenotype is a PERIOD phenotype
(the epiphyses do not fuse on time), not a RATE phenotype.** The exceptions are named.

**TIER 1 — the extremes (>15 cm above target, or "tallest individuals described")**

1. **X-linked acrogigantism (X-LAG, Xq26.3 duplication → GPR101 neo-TAD).** GH excess starting in
   **infancy**; the source describing it says X-LAG "can lead to the tallest individuals described"
   (~40 patients known worldwide). **RATE, not period** — the rate is so extreme it overwhelms the
   normal window. Mechanism: a topologically-associating-domain rearrangement places GPR101 under an
   ectopic pituitary enhancer; the receptor is constitutively active. `38696651`
2. **Pituitary gigantism from any cause with open plates (AIP, MEN1, Carney complex, sporadic,
   ectopic GHRH, McCune-Albright).** Same term, different upstream lesions. `41965096`, `22720333`
3. **Oestrogen resistance, ERα-null male.** **204 cm at 28 years, epiphyses still incomplete, still
   growing.** Pure PERIOD. This is the largest documented *non-tumour* excess height with a named
   single-gene mechanism, and it is the ONE lesion in the whole domain that oestrogen cannot rescue
   (a 10-fold rise in free oestradiol did nothing). `8090165`

**TIER 2 — large, and unambiguously a period phenotype (5–20 cm)**

4. **Aromatase deficiency (CYP19A1), male.** Continued linear growth into adult life; open wrist and
   knee epiphyses at 24 y. Pure PERIOD. Distinguished from (3) only by being **fully reversible with
   oestradiol** — and oestradiol is given precisely to stop the growth. `36504506`
5. **17α-hydroxylase/17,20-lyase deficiency (CYP17A1).** n=88: bone age delayed ≥2 y in **92.5%**;
   **39% of adults at or above the 90th centile**, only 8% at or below the 25th. Short as a child,
   tall as an adult, tall *eunuchoid* habitus. PERIOD, by removal of both adrenal and gonadal
   sex steroid. `40350803`
6. **Untreated congenital hypogonadotropic hypogonadism / Kallmann, and any adolescent-onset
   hypogonadism.** Eunuchoid proportions (arm span > height, low upper:lower segment) because the
   limbs keep growing after the trunk stops. PERIOD. `20301509`

**TIER 3 — structural / dosage / signalling excesses, mostly with normal bone age (2–10 cm)**

7. **Marfan syndrome (FBN1).** Tall AND disproportionate (dolichostenomelia). Second commonest primary
   tall-stature diagnosis in a 1.14 M-child cohort. Mechanism is **NOT plate-intrinsic**: fibrillin-1
   loss releases matrix-sequestered TGF-β at the perichondrium, and the limb segment overgrows.
   Neither a rate nor a period phenotype in the endocrine sense. `20301510`, `40233073`
8. **Klinefelter syndrome 47,XXY.** Commonest primary tall-stature disorder (CMI 1/2146 boys).
   **SHOX overdosage** (leg segment) plus hypogonadal delayed fusion — a rate/dosage AND a period
   effect stacked. `41198007`, `40233073`, `20425825`
9. **Classical homocystinuria (CBS).** Tall marfanoid habitus by a metabolic route — homocysteine
   disrupts fibrillin/collagen cross-linking. Structural, like Marfan. `20301697`
10. **CATSHL syndrome (FGFR3 partial LOSS of function, p.R621H).** Camptodactyly, **tall stature**,
    scoliosis, hearing loss. The exact inverse allele of achondroplasia and the human germline proof
    that lowering FGFR3 lengthens bone — while also delivering scoliosis. `17033969`
11. **NPR2 GAIN of function (p.Val883Met).** Tall stature, scoliosis, macrodactyly of the great toes,
    across three generations, with **measurably raised blood cGMP** and a transgenic mouse that
    reproduces it. Human proof that raising cGMP at the plate lengthens bone. `22870295`
12. **NPR3 (NPR-C) biallelic loss of function.** Tall stature, long digits, **extra epiphyses in hands
    and feet**, aortic dilatation in 2 of 3 families, high cGMP and a reduced NTproNP/NP ratio.
    Same axis as (11), reached by deleting the clearance sink rather than activating the receptor. `30032985`
13. **Sex-chromosome dosage above 46 but below the inflection: 47,XXX (+0.7 SDS), 47,XYY, 48,XXYY.**
    SHOX overdosage. Note the series **inverts** at 49,XXXXY (−1.8 SDS). `20425825`
14. **SHOX overdosage from Xp duplication or an X;autosome translocation** — including in patients
    whose karyotype otherwise reads as Turner. `26191517`, `20689243`, `11134233`
15. **Cantú syndrome (ABCC9/KCNJ8 GoF).** Large, hypertrichotic, osteochondrodysplastic. A
    **K-ATP channelopathy** presenting as generalised overgrowth. `25275207`
16. **PTEN hamartoma tumour syndrome (Cowden / Bannayan-Riley-Ruvalcaba).** Tall + macrocephaly;
    loss of the PI3K brake. `20301661`
17. **15q26 duplication (IGF1R trisomy).** Receptor dosage — the mirror of IGF1R haploinsufficiency. `42130906`
18. **Simpson-Golabi-Behmel (GPC3).** Prenatal-onset overgrowth; loss of a cell-surface heparan
    sulfate proteoglycan that restrains IGF2/hedgehog/BMP. One adult case mimicked acromegaly. `20301398`, `42220602`

**TIER 4 — marfanoid habitus without generalised overgrowth**

19. MEN2B (RET p.M918T) `20301434`; Lujan-Fryns (MED12) `19377476`; Shprintzen-Goldberg (SKI)
    `23023332`; Beals/CCA (FBN2) `20301560`; Loeys-Dietz `20301312`; fragile X `20301558`.
    Mechanism named only for the TGF-β/fibrillin group; **the RET and MED12 skeletal mechanisms are
    genuinely unexplained** and are therefore among the best unworked leads here.

**TIER 5 — tall as a child, adult height NOT above target (see PROSE 3)**

20. Sotos (NSD1), Weaver (EZH2), Cohen-Gibson (EED), Imagawa-Matsumoto (SUZ12), Tatton-Brown-Rahman
    (DNMT3A), Luscan-Lumish (SETD2), Malan (NFIX), Beckwith-Wiedemann, Tenorio (RNF125), CHD8, PPP2R5D,
    HERC1, Nevo (PLOD1). All carry **advanced bone age or a self-limited infantile overgrowth**.
21. Central and peripheral precocious puberty; childhood hyperthyroidism; childhood obesity;
    familial glucocorticoid deficiency; classic 21-hydroxylase CAH. **All four are tall-child /
    short-adult trades**, and three of them are treated specifically to prevent the trade.

**TIER 6 — segmental, not stature**

22. PIK3CA-related overgrowth spectrum, Proteus (AKT1), and any mosaic PI3K/AKT/mTOR activation.
    These enlarge a *part*, and the enlarged part is the one that carries the mosaic variant.

**TIER 7 — the largest effect of all, and it is not a disease**

23. **The secular trend.** Population mean height rose by an order of ~15–20 cm in some countries in a
    century, driven by early-life nutrition and infection burden — larger than any monogenic effect
    in this table. Recorded because a complete map has to contain it. `25310000`

---

## PROSE 2 — CONDITIONS WHERE HEIGHT IS RESTORED BY TREATMENT, AND THE MECHANISM IS THEREFORE DRUGGABLE

Grouped by the *class* of the reversal, because the class is the transferable information.

**(a) Remove an inflammatory cytokine → growth resumes.** The strongest evidence that a circulating
cytokine is a direct, reversible brake on the plate.
- **Anti-IL-6R (tocilizumab) in systemic JIA** — the cleanest case: IL-6 blocks chondrogenic
  differentiation in vitro (`19535264`), IL-6 excess retards growth, and blocking the receptor restores
  height velocity (`23227116`, `33712046`).
- **Anti-TNF (infliximab) in paediatric Crohn disease** — improves linear growth; exclusive enteral
  nutrition achieves the same by avoiding steroids (`25309059`, `22772738`).
- **IL-1 blockade (anakinra/canakinumab) in CAPS/NOMID.**
- ⚠ **The informative negative:** FMF, a *recurrent* IL-1β disease, generally preserves growth. **Burst
  inflammation is not the same lever as tonic inflammation.**

**(b) Remove the fusion signal → the period lengthens.** The only routinely used *pharmacological*
period extension in medicine.
- **GnRH analogue in central precocious puberty** — restores adult height if started early (`40564714`).
- **Aromatase inhibitor** (± antiandrogen) in peripheral precocious puberty and in boys generally (`41947100`).
- The natural experiments that license the class are A1/A3/A5/A6 above.

**(c) Restore a missing substrate or correct an acid-base/mineral lesion → growth resumes fully.**
These are the *most* reversible causes in the whole domain and are systematically under-taught.
- **Alkali in distal renal tubular acidosis** (`41897147`).
- **Gluten-free diet in coeliac disease** (`20301720`, `30891436`).
- **Uncooked cornstarch / strict metabolic control in GSD Ia/Ib** (`34836082`).
- **Cysteamine in nephropathic cystinosis** — early vs late diagnosis materially changes the outcome
  (`40143952`, `40877952`).
- **Insulin in Mauriac syndrome** — documented reversal on automated insulin delivery over 2.5 y (`41560719`).
- **Levothyroxine in hypothyroidism** — with the caveat that late (especially pubertal-onset) treatment
  leaves a permanent deficit (`41960511`).
- **Burosumab (anti-FGF23) in X-linked hypophosphataemia**; **asfotase alfa in hypophosphatasia**
  (`22319799`, `20301329`).

**(d) Remove the mechanical/respiratory insult → the GH pulse returns.**
- **Adenotonsillectomy for paediatric OSA: +2.93 cm mean height at 3 months with unchanged calorie
  intake, and IGF-1 rose while GH did not** (`29967551`). A clean demonstration that sleep architecture,
  not nutrition, was the limiting variable.
- **Corrective surgery for cyanotic congenital heart disease** — catch-up after repair.

**(e) Correct the primary genetic lesion pharmacologically.**
- **CFTR modulators in cystic fibrosis** — has moved a whole population's nutritional and growth
  trajectory (`41692662`, `41300552`).
- **Alpelisib in PIK3CA-related overgrowth** — the reversal runs the *other* way (it shrinks
  pathological overgrowth) and is therefore the proof that PI3K dosage sets tissue size in humans
  (`42121892`).
- **rhIGF-1 (mecasermin) in GH insensitivity** (`17192294`); **rhGH in GHD, Turner, PWS, CKD, SGA, Noonan**.

**(f) Change the environment.**
- **Psychosocial short stature** — reversal on removal from the adverse environment, with no drug,
  is the diagnostic test (`857651`).
- ⚠ **Hyperphagic short stature is the exception that matters:** low stimulated GH *and* a poor response
  to exogenous GH (3 cm/y on 6 months of rhGH). A GH-**resistant** psychosocial state (`22837929`).

**(g) Stop the drug.**
- Glucocorticoid, stimulants, tenofovir DF, enzyme-inducing antiepileptics.
- ⚠ **And the two that CANNOT be reversed by stopping: vismodegib (irreversible growth-plate fusion
  after >140 days in children, persisting long after cessation — `29050204`) and palovarotene
  (premature physeal closure — `36583535`, `39677926`). Once the plate is fused, no reversal exists.**
- ⚠ **Inhaled budesonide sits between: the −1.2 cm adult-height deficit is permanent but NOT
  progressive — it is established within 2 years and then frozen (`22938716`).**

**(h) Not reversible at all, and worth naming as the boundary of the domain.**
Spinal irradiation (destroyed vertebral plates — rhGH cannot rescue them and worsens the disproportion,
`3606177`); ERα-null oestrogen resistance; any fused plate; and every structural/chromatin syndrome
in section E and L.

---

## PROSE 3 — CONDITIONS WHERE ADULT HEIGHT IS ABOVE TARGET, RATHER THAN MERELY TALL AS A CHILD

**This is the discriminating list, and the discriminator is BONE AGE.**

The single organising fact that falls out of 270 rows is this:

> **Conditions with genuinely excess ADULT height almost all have NORMAL OR DELAYED bone age.
> Conditions that are tall in childhood and normal-or-short as adults almost all have ADVANCED bone age.**

A tall child with an advanced bone age is spending the growth period to buy velocity, and the trade is
at best neutral. A tall child with a *delayed* bone age is being given extra period, and that is the only
configuration that reliably converts into adult centimetres.

**GROUP 1 — ADULT HEIGHT ABOVE TARGET, by extension of the PERIOD (bone age delayed or arrested)**
- **Oestrogen resistance, ERα-null (male).** 204 cm; epiphyses still open at 28. `8090165`
- **Aromatase deficiency (CYP19A1).** Open epiphyses at 24 y and still growing; oestradiol is given to
  stop it. `36504506`
- **17α-hydroxylase/17,20-lyase deficiency.** The published quantitative demonstration: **bone age
  delayed ≥2 y in 92.5%, and 39% of adults ≥90th centile despite being SHORT as children.** `40350803`
- **Untreated hypogonadism of any cause, including CHH/Kallmann.** Eunuchoid proportions. `20301509`
- **Klinefelter syndrome.** Both mechanisms at once — SHOX dosage AND hypogonadal fusion delay. `41198007`

**GROUP 2 — ADULT HEIGHT ABOVE TARGET, by a plate-intrinsic or structural mechanism with NORMAL bone age**
- **Marfan syndrome (FBN1)** and the fibrillin/TGF-β group (FBN2/Beals, Loeys-Dietz, Shprintzen-Goldberg).
  Perichondrial TGF-β release; limb-selective. `20301510`, `20301560`, `23023332`
- **Classical homocystinuria (CBS)** — the metabolic phenocopy. `20301697`
- **CATSHL (FGFR3 partial LoF)** — the achondroplasia allele read backwards. `17033969`
- **NPR2 gain-of-function** and **NPR3 biallelic loss-of-function** — the cGMP axis, with measured
  cGMP elevation in both. `22870295`, `30032985`
- **SHOX overdosage** (47,XXX, 47,XYY, 48,XXYY, Xp duplications). `20425825`
- **Cantú syndrome (ABCC9 GoF)**; **15q26/IGF1R duplication**; **PTEN hamartoma tumour syndrome**.
- **X-LAG and pituitary gigantism** — the exception to the rule: the rate is so extreme, and starts so
  early, that it produces true excess adult height despite advancing maturation. `38696651`

**GROUP 3 — TALL AS A CHILD, ADULT HEIGHT NOT ABOVE TARGET (do not mistake these for levers)**
- **Sotos syndrome** — tall child, **advanced bone age**, adult height frequently within the normal
  range. The same caveat applies across the chromatin overgrowth class: **Weaver (EZH2), Cohen-Gibson
  (EED), Imagawa-Matsumoto (SUZ12), Tatton-Brown-Rahman (DNMT3A), Luscan-Lumish (SETD2)**.
  `20301652`, `39494594`, `23865096`, `28229514`
- **Beckwith-Wiedemann spectrum** — overgrowth is infantile and **self-limiting**; growth velocity
  normalises in mid-childhood. `20301568`
- **Central precocious puberty, untreated** — the archetype of the trade. `40233073`, `40564714`
- **Peripheral precocious puberty / McCune-Albright.** `41947100`
- **Childhood hyperthyroidism** — accelerates growth and maturation in near-equal measure. `40233073`
- **Childhood obesity** — the commonest tall child in an affluent population; hyperinsulinaemia plus
  adipose aromatase → advanced bone age.
- **Classic 21-hydroxylase CAH** — tall child from adrenal androgen, short adult from premature fusion
  *and* from the glucocorticoid used to treat it. `20301350`
- **Familial glucocorticoid deficiency** — tall child (+2.41 SD in the documented case) with bone age
  advanced ~6 y at CA 4y9m; the measured driver is ACTH-associated **oestradiol** that suppresses with
  dexamethasone; hydrocortisone normalises the growth. `11012566`, `15673970`
- **Marshall-Smith syndrome (NFIX)** — accelerated bone maturation *with* failure to thrive. The same
  gene as Malan syndrome, opposite growth outcome, sorted by allele class. `39014953`, `37336770`

**GROUP 4 — the direction is genuinely bidirectional within one condition, and this is under-reported**
- **RED-S / exercise-associated amenorrhoea:** low energy availability shortens, while hypo-oestrogenism
  delays fusion. Net adult-height effect not established.
- **Sickle cell disease:** growth delay in childhood, but delayed puberty partially rescues adult height.
- **McCune-Albright:** GH excess pushes up, precocious puberty pushes down, in one patient.
- **CHARGE / CHD7:** short stature with hypogonadotropic hypogonadism partially offsetting.

---

## WHAT I COULD NOT VERIFY

**Method and verification status.** Every PMID in this file was resolved against NCBI esummary in a final
pass: **every numeric identifier cited was checked (247 in the main automated batch plus 14 checked
individually) and ALL of them resolved to a real record whose title matches the use made of it.** No citation in this file is invented. Where I could not find a source I wrote
`UNVERIFIED` rather than guessing, and there are 60+ such cells.

**Specific things I asserted from an INDEX (review/GeneReviews) rather than a primary source**, and which a
later round should therefore re-derive from the primary if the claim becomes load-bearing:
- All GeneReviews chapters (PMIDs 2030xxxx and the newer chapters). They are curated and stable but they are
  syntheses. I used them deliberately as *anchors for existence and direction*, never for a number.
- The FMF "growth generally preserved" negative: I have the claim from a large cohort seen in a Europe PMC
  abstract listing but did **not** retrieve the primary cohort paper. The GeneReviews chapter (`20301405`)
  is cited in its place. **This negative is worth confirming — it is the discriminator between burst and
  tonic inflammation.**
- Familial glucocorticoid deficiency *adult* height. I verified tall stature in childhood with advanced
  bone age (`11012566`, `15673970`) but **could not verify a final-adult-height series**. My table row
  now says so.
- "Growth without growth hormone" after craniopharyngioma: I could not retrieve a primary source for the
  phenomenon in this session, only indexes for hypothalamic obesity. Marked accordingly (row R8).
- Gorlin/nevoid basal cell carcinoma syndrome: searched specifically for tall stature/macrocephaly and did
  not retrieve a usable primary. **Not included as a row** — but note that row E31 (whole-gene PTCH1
  deletion in a syndromic tall-stature cohort, `40577202`) is the same gene, and the two should be read
  together by whoever picks this up.

**Things I looked for and could not find at all:**
- A GeneReviews chapter for **aromatase deficiency**, **5α-reductase 2 deficiency**, **Bartter**,
  **Gitelman**, **Meier-Gorlin**, **Mulibrey nanism**, **Dubowitz syndrome**, **hereditary
  vitamin-D-resistant rickets**, **CAPS**, **sarcoidosis**, or **JIA**. These conditions are in the table
  on other evidence or as UNVERIFIED.
- A verified magnitude for **47,XYY** and **48,XXYY** adult height. `20425825` gives the karyotype-by-SDS
  table but the excerpt I retrieved was truncated across exactly those rows.
- A primary source for **NPPC dosage / translocation causing tall stature** (row P5).
- Any quantitative adult-height figure for **CAPS/NOMID**, **TRAPS**, **sarcoidosis**, **SLE**,
  **mitochondrial disease**, **MPS VI/VII/III**, **MOPD II**, **mosaic variegated aneuploidy**,
  **Mulibrey nanism**, **prolidase deficiency**, **Menkes** or **occipital horn syndrome**.
- A postnatal (as opposed to embryopathic) human warfarin/physeal source (row J11).

**Structural gaps I am aware of and did not close:**
- **Skeletal dysplasias are deliberately mostly absent** — they belong to another domain. Only the ones
  that make the point about *direction* (achondroplasia vs CATSHL; NPR2 across three allele doses;
  osteopetrosis as discharge failure; hereditary multiple exostoses) are included, cross-listed.
- **This is a human-disease enumeration.** Where I cite an animal result it is labelled (MOUSE/RAT) —
  rows E34, P3, and the IL-6/chondrocyte in-vitro result in F3.
- **Ethnic and population-genetic variation in stature** is only represented by the secular trend and by the
  high-altitude rows; a complete map would need a population-genetics domain of its own.
- I did **not** systematically search clinicaltrials.gov or FDA/EMA labels, which the common brief permits.
  The two places where a label is the best source and I relied on a paper instead are **vismodegib**
  (`29050204` reports that the findings produced the label warning) and **palovarotene** (`36583535`,
  `39677926`).

**One honest caution about Europe PMC's relevance ranking:** default relevance sorting is heavily biased
toward very recent papers, and citation sorting is heavily biased toward large unrelated guidelines. Several
searches (e.g. "sickle cell growth", "mitochondrial short stature") returned cardiology statistics reports
at the top and nothing useful. Where that happened I fell back on GeneReviews or marked UNVERIFIED rather
than citing something I had not read.
