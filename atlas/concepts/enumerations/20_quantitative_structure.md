# DOMAIN 20 — THE QUANTITATIVE STRUCTURE OF GROWTH
## R436 full-concept-space enumeration (models, arithmetic, measurement)

**Method note.** Every row below was reached by EXTERNAL search only — Europe PMC REST
(`/europepmc/webservices/rest/search`, ~40 distinct queries) and NCBI eutils `efetch` for full abstracts.
No file in `/home/user/growth-plate` was consulted except the two briefs; nothing here is derived from the
atlas. All values are as stated in the abstract or full text retrieved; where a number comes from a review
or commentary rather than a primary report that is flagged in the row. Where I could not verify a number I
have written `UNVERIFIED` rather than guess. Species is carried on every row.
**81 rows; 48 marked OBSCURE.**

---

## TABLE

| # | TERM / MODEL / METHOD | WHAT IT QUANTIFIES | TYPICAL VALUE + UNITS | SPECIES | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| 1 | **Hunziker stereological quantitation of chondrocyte performance** | Whole-cell "performance" budget of a growth plate (cell height, cell volume, matrix volume per cell, turnover) | Late hypertrophic vs proliferative: **cell height ×4, cell volume ×10, matrix volume per cell ×3**; RER/Golgi surface ×2–5; **vascular invasion removes 1 chondrocyte per column every 3 h = 8 cells/column/day** | Rat (proximal tibia) | 3543020 | no |
| 2 | **Wilsman 8-variable kinetic decomposition of differential growth** | Partition of elongation into division / matrix / hypertrophy | Proximal tibia: **9% cell division, 32% matrix synthesis, 59% chondrocytic enlargement**. Slower plates shift to **44% enlargement, 49% matrix** (proximal radius) | Rat, 28 d, 4 plates | 8982136 | **yes** |
| 3 | **Chondrocyte production rate (cells/day/plate)** | Absolute throughput of a growth plate | **16,400/day (proximal tibia) vs 3,700/day (proximal radius)** — ~4× — and production ≈ loss at chondro-osseous junction (steady state verified) | Rat, 28 d | 8982136 | **yes** |
| 4 | **Proliferative-zone total cell cycle time (Tc)** | How fast a proliferative chondrocyte divides | **30.9 h (prox tibia), 34.0 h (distal radius), 48.7 h (distal tibia), 76.3 h (prox radius)** — a 2.5× spread within ONE animal | Rat, 28 d | 8764865 | **yes** |
| 5 | **Cell-cycle phase durations in the proliferative zone** | Where cycle-time regulation actually sits | **S 3.4–6.1 h, G2 3.0 h, M 0.5–0.6 h**; almost the entire between-plate difference is in **G1** | Rat | 8764865 | **yes** |
| 6 | **Hypertrophic cell volume ↔ elongation rate (Breur relation)** | The single strongest correlate of growth rate | Linear, **r = 0.98 (rat), r = 0.83 (pig)**; independent of plate location and age; slope species-specific | Rat + Yucatan pig, 21 & 35 d | 2010838 | no |
| 7 | **Two-phase kinetics of chondrocytic enlargement** | Where in time the volume is added | **~20% of final volume over first ~30 h at ~50 µm³/h; remaining ~80% over next ~20 h at ~800 µm³/h**; no change in final 5 h | Rat proximal tibia, 35 d | 7943757 | **yes** |
| 8 | **Within-animal range of physeal elongation rate** | Spread of the output variable being decomposed | **~50 to ~400 µm/24 h** across four plates in the same 28-day rat | Rat | 8764865 | no |
| 9 | **Avian kinetic decomposition (contrast case)** | Which term dominates in birds | Hypertrophic cell volume variation is **small**; the dominant determinant is **the size of the flat-cell (proliferative) zone** | Chicken, budgerigar, rhea + 5 further species | 2267417; 8146454 | **yes** |
| 10 | **Distal femoral physis share of femoral growth (histology + serial radiographs)** | Which physis makes the bone | **~66% of total femoral longitudinal growth**; authors explicitly warn rodent→human extrapolation is unsafe | **HUMAN** (post-mortem + radiographic) | 917957 | **yes** |
| 11 | **Pritchett lower-limb physeal shares** | Physis-by-physis contribution and cm/yr | Distal femur **~70% overall** (60% at age 7 → **90% at 14 (F) / 16 (M)**); proximal tibia **~57%** (50% → 80%). **Distal femur ≈ 1.3 cm/yr from age 7**, halving in the last two years | **HUMAN**, 244 children, 6-monthly to maturity | 1735225 | no |
| 12 | **Pritchett upper-limb physeal shares** | Contribution of each upper-limb centre | Proximal humerus **~80%** overall (→90% after age 11); distal ulna **~85%** (→95% after 8); distal radius **~80%** (→90% by 8) | **HUMAN**, n=200 | 2060215 | **yes** |
| 13 | **Upper-limb segment growth rates and segment/stature fractions** | cm/yr per bone and proportion of stature | Humerus **1.2 cm/yr (F), 1.3 (M)**; ulna 1.0/1.1; radius 0.9/1.0 cm/yr after age 7. Humerus = **18→20% of standing height**; radius **13→15%** | **HUMAN**, 244 children | 3356718 | **yes** |
| 14 | **Fibular physeal share** | Proximal vs distal fibula | Proximal fibula **61%** of fibular growth vs **57%** for proximal tibia | **HUMAN**, 244 children | 9005920 | **yes** |
| 15 | **In-vitro ³H-thymidine labelling of HUMAN growth plates** | Labelling index, proliferative cell number, hypertrophic cell height in human tissue | Values reported in paper; abstract gives no figures (**UNVERIFIED numerics**). Key qualitative result: **pig is kinetically intermediate between human and rodent**; 2 of 4 human specimens gave no labelled cells | **HUMAN** + pig | 3864550 | **yes** |
| 16 | **Stokes growth-rate sensitivity to sustained stress** | dGrowth/dStress — the mechanobiological gain | **17.1% per 0.1 MPa** mean (range **9.2–23.9%**); vertebra **15.0%**, proximal tibia **18.6%**. Control rates **30 µm/day (rat vertebra) → 366 µm/day (rabbit prox tibia)** | Rat, rabbit, calf; 2 sites | 16705695 | **yes** |
| 17 | **Which kinetic term carries mechanical growth modulation** | Attribution of load effect to a term | Multiple-regression coefficients: **proliferative cell number 0.72 vs chondrocytic enlargement 1.39** → enlargement contributes ~2× more; growth altered up to **53%** | Rat, calf, rabbit | 17532281 | **yes** |
| 18 | **Compression/distraction asymmetry in the same experiment** | Non-linearity of the mechanical term | Compressed vertebrae **52%** of control growth; distracted **113%**. HZ height **87%**, mean chondrocyte height **85%**, increase-in-cell-height **78%** of control | Rat caudal vertebra, 4 wk | 12377917 | no |
| 19 | **SITAR (SuperImposition by Translation And Rotation)** | 3-parameter shape-invariant summary: size, tempo, velocity | Explains **99% of variance**; residual SD **6–7 mm** in two independent cohorts; matches individually fitted Preece-Baines curves with one mean curve | **HUMAN** (3,245 boys; 105 Turner girls) | 20647267 | no |
| 20 | **Age at peak height velocity (APV) and peak velocity (PV) from SITAR** | The two "tempo" parameters | Harpenden mean APV **12.0 y (girls), 13.9 y (boys)** averaged over 10 anthropometric measures; **PV = 4–8 % per year** across measures | **HUMAN**, Harpenden (n=619) + ALSPAC (n=10,410) | 32429758 | no |
| 21 | **ICP model (Infancy–Childhood–Puberty, Karlberg)** | Decomposition of the postnatal height curve into 3 additive, partly overlapping components | Three components with separate onsets; age at onset of the **childhood component** is an individually detectable event and a predictor of stunting | **HUMAN** | 2488676 | no |
| 22 | **QEPS model (Quadratic–Exponential–Pubertal–Stop)** | 4-function decomposition from fetal life to adult height, with individual SDS and CIs | Separates a **specific pubertal function (P)** from basal growth (QES); pubertal gain from P is **independent of age at pubertal onset**; boys gain more from P, girls more from QES | **HUMAN**, GrowUp Gothenburg (n=2,280) | 27297288; 28424059 | **yes** |
| 23 | **Saltation and stasis** | Whether growth is continuous or pulsatile | Length accrued in discrete saltations of **0.5–2.5 cm** (measurement intervals 1 day–1 week) separated by stasis of up to ~60 days | **HUMAN** infants (n=31) | 1439787; 28548366 | no |
| 24 | **Knemometry / mini-knemometry (lower-leg length)** | Short-term (days–weeks) growth with sub-mm resolution | Technical error **0.31 mm** on a mean leg length of 98.49 mm (**CV 0.31%**); rod measurement SD **0.058 mm**. Preterm baseline lower-leg velocity **0.37 mm/day**, falling to negative on dexamethasone | **HUMAN** (preterm and children) | 8285753; 8285754 | no |
| 25 | **BoneXpert automated bone age — accuracy** | Error of an automated maturity read | SD vs Greulich–Pyle atlas **0.42 y** [0.37–0.47]; vs TW-rated images **0.80 y**; **precision of a single determination 0.17 y** | **HUMAN** (1,559 development images) | 19116188 | no |
| 26 | **BoneXpert precision in a modern trial cohort** | Minimal detectable bone-age change | Automated precision **0.08 y** → **minimal detectable difference 0.23 y**, against **manual rater precision 0.63 y**; androgen effect on BA detectable by **6 months** (0.24 y at 6 mo → 1.43 y at 24 mo) | **HUMAN**, 90 boys Klinefelter, 5 visits/2 y | 42045323 | **yes** |
| 27 | **Head-to-head error of adult-height prediction methods** | Which predictor is least wrong | % of predictions within **±1 SDS** of near-adult height: **RWT 77.4%, TW2 62.3%, Bayley-Pinneau 54.7%**; median PAH−NAH SDS: BP −0.5, RWT 0.0, TW2 +0.3 | **HUMAN**, 49 GHD children | 33900130 | no |
| 28 | **Mid-parental (target) height — variance explained and bias** | How much of adult height parents actually predict | Standard sex-adjusted MPH explains **36% of variance**, implied heritability **74%**, and children are on average **2.7 cm taller than predicted**. Corrected method: **40% / 80% / bias 0.14 cm** | **HUMAN**, 23 large nuclear families (~11 adult children each) | 39201851 | **yes** |
| 29 | **Regression-based target height (Luo/Karlberg)** | Target height as a regression, not an offset | **TH = 45.99 + 0.78 × MPH (boys); 37.85 + 0.75 × MPH (girls)**, 95% prediction interval **≈ ±10 cm**. Tanner method errs by **~6 cm** (under-estimate) at MPH ≤ −2 SDS. Heritability **0.75–0.78 (cm)**, **0.55–0.60 (SDS)** | **HUMAN**, n=2,402 | 9773847 | **yes** |
| 30 | **Twin heritability of adult height across 8 countries** | Ceiling on the genetic term | Men **h² 0.87–0.93** (AE model); women **0.68–0.84** (ACE), 0.89–0.93 where AE fits. Mean height range Italy 177 cm ♂ → Netherlands 184 cm ♂ | **HUMAN**, 30,111 twin pairs | 14624724 | no |
| 31 | **Age-dependence of height heritability in childhood** | Heritability is not a constant | Twin design <5 y: **0.57** (European), 0.48 (Asian). Parent-offspring: **0.46 at birth → 0.76 at 17 y**. Sibling design flat at **0.70** | **HUMAN**, 560,000 pairs of relatives | 39564936 | **yes** |
| 32 | **Paley multiplier method (and derivatives)** | Predicts mature limb/segment length as current length × an age- and sex-specific multiplier | Age-based multipliers; extended to **sitting height, cervical, thoracic and lumbar spine** multipliers; PHV-timing-based multipliers proposed as an alternative to age-based | **HUMAN** (longitudinal + cross-sectional databases) | 36421213; 33323887 | no |
| 33 | **LMS method (Cole)** | The machinery behind every modern SDS/Z-score: L = Box-Cox power (skew), M = median, S = coefficient of variation, fitted as penalised-likelihood cubic splines | Three smooth curves per reference; underpins WHO, CDC 2000, Dutch and British charts | **HUMAN** | 2354692; 1518992; 24992748 | no |
| 34 | **Known failure mode of LMS** | Where the standard SDS machinery breaks | Cole's own conclusion: **LMS should not be used to construct height-VELOCITY centiles in puberty** (title-only; abstract not retrievable — **UNVERIFIED numerics**) | **HUMAN** | 39570025 | **yes** |
| 35 | **Diurnal stature loss — magnitude in children** | Measurement noise floor competing with real growth | Mean **0.47 ± 0.05 cm** decrease from 09:00–10:00 to 15:00–16:00; individual range **+1.8 to −2.7 cm** | **HUMAN**, 478 children aged 3–15 | 16354217 | no |
| 36 | **Diurnal stature loss — time course and the "stretched" technique** | When the loss happens and whether technique fixes it | Loss is front-loaded: **0.31 cm (09:00→11:00), 0.20 cm (11:00→13:00), 0.045 cm (13:00→15:00)**; **stretching does NOT reduce diurnal loss** but raises recorded height by **0.28 cm**; reproducibility SD **0.30 vs 0.31 cm** | **HUMAN**, 53 children | 9389235 | no |
| 37 | **Within-subject daily stature amplitude and measurement SEM** | Best-case single-observer precision | **SEM 0.12 cm** from 292 duplicate measurements; mean daily decrease **0.98 ± 0.2 cm**; a similar decrease recurred after **2–3 h naps** | **HUMAN**, 1 boy, 328 daily assessments | 1734826 | **yes** |
| 38 | **Diurnal loss split standing vs sitting** | Which segment the diurnal artefact lives in | Standing loss **0.7 ± 0.7 cm = 0.43% of standing height**; sitting loss **0.7 ± 0.7 cm = 0.79% of sitting height** — i.e. **nearly all of the loss is axial** | **HUMAN**, 98 children with idiopathic scoliosis | 30689550 | **yes** |
| 39 | **Classic diurnal figures in adolescent boys** | Reference magnitudes | Stature **−2.0 mm (09:30→14:00)** and **−4.6 mm (10:00→17:00)**; sitting height **−2.0 mm** and **−2.8 mm** respectively | **HUMAN**, boys 12–14 y | 16431557 | **yes** |
| 40 | **Sitting-height:standing-height ratio reference charts** | Segment proportion normal range by age, sex and ancestry | NHANES III, **n = 9,569** aged 2–18. SitHt/Ht **falls prepuberty→early puberty and rises in late puberty**; **non-Hispanic Black children significantly lower** than NHW and Mexican-American throughout childhood | **HUMAN** | 32579888 | no |
| 41 | **Sitting height / leg length / SH-H references and their diagnostic yield** | How well proportion detects dysplasia | n = 14,500 Dutch children 0–21 y. Height-corrected SH/H cut-off sensitivity **80% for hypochondroplasia** but only **30% for Marfan**; SH/H SDS is **negatively correlated with height SDS**, so cut-offs must be height-corrected (+2.5 SD if height <−2 SDS; −2.2 SDS in very tall) | **HUMAN** | 15863466 | no |
| 42 | **Knee-height→stature prediction equations** | Proxy stature when standing height is not measurable | Head-to-head in 210 US children 7–12 y: **Rumapea equation reliable (p = 0.878)**, **Chumlea equation unreliable (p = 0.0376)** | **HUMAN** | 39072793 | **yes** |
| 43 | **Physeal diffusion-tensor imaging (DTI) tract volume** | A direct, radiation-free, in-vivo image-based measure of growth-plate activity in a living child | Distal femoral tract volume vs height velocity **r² = 0.49**, vs total height gain **r² = 0.46**. Multivariable model: **height velocity R² 0.63, RMSE 1.7 cm; total height gain R² 0.59, RMSE 1.8 cm** — versus bone-age models **R² 0.32/RMSE 2.9 cm** and **R² 0.42/RMSE 5.0 cm** | **HUMAN**, 89 + 70 children | 35315716 | **yes** |
| 44 | **DTI tibia:femur partition of knee growth potential** | Physis-by-physis growth potential imaged in vivo | At maximal height velocity (**160 months**), **proximal tibial tract volume 5.43 cc = 37.4% of total knee tract volume (14.53 cc)**; tract volume peaks **earlier in girls (140–160 vs 160–180 months)** | **HUMAN**, 108 children | 39516384 | **yes** |
| 45 | **Three-phase model of chondrocyte volume enlargement (quantitative phase microscopy)** | Mechanism and dry-mass accounting of the hypertrophy term | Three distinct phases including **massive swelling with significant dilution of cellular dry mass**; the phase that varies most between fast and slow plates is the **third — proportional dry-mass increase at low density** — and it is **IGF-dependent** | Mouse/mammalian growth plate | 23485973 | no |
| 46 | **Cell number as the shared driver of limb AND vertebral proportion** | Which term sets proportion between bones | **Cell number is the common driver** in both mouse and jerboa; hypertrophy contributes only to the extreme jerboa mid-tail. **Npr3 loss disproportionately elongates proximal + mid-tail vertebrae and the proximal limb** | Mouse + jerboa | 41073372 | **yes** |
| 47 | **Differential growth-plate senescence as the source of skeletal proportion** | Why a femur is ~20× a phalanx | Functional/structural/molecular senescence occurs **earlier in small bones (metacarpals, phalanges) than in femur/tibia**; declines in proliferation, hypertrophy and cell number in all zones | Mouse (with human framing) | 30036371 | no |
| 48 | **Kember clonal-behaviour simulation of the growth plate** | Column/clone architecture as a stochastic process | Best fit required a **distribution of clone lengths, 1,000–2,000 µm**, and a faster-moving metaphyseal end than epiphyseal end | Rabbit proximal tibia (simulation on measured data) | 2050577 | **yes** |
| 49 | **Mechanobiological continuum growth model of the juvenile femur** | In-silico coupling of load to growth rate | Octahedral shear stress **accelerates** and hydrostatic stress **retards** longitudinal growth, applied to a FE model of an **8-year-old boy's femur** including proximal + distal physes and apophyses | **HUMAN** geometry, in silico | 42458460 | **yes** |
| 50 | **Decomposition-based FE model of stress-modulated spinal growth** | Hueter-Volkmann implemented in large-deformation continuum mechanics | First implementation of the Hueter-Volkmann law in a **multiplicative growth-decomposition** finite-strain framework for AIS | **HUMAN** spine, in silico | 42244189 | **yes** |
| 51 | **Automated single-cell growth-plate histocytomorphometry ("GP Pro")** | Modern replacement for manual stereology: per-lacuna morphometry and spatial distribution across zones | Pipeline = whole-slide batch processing + SAM2 segmentation + single-cell lacuna analysis; explicitly framed as replacing "rudimentary metrics such as tissue thickness" | Multi-species | 41836565 | **yes** |
| 52 | **KIGS first-year growth-response prediction model (Ranke)** | How much of the response to GH is predictable, and from what | In idiopathic GHD **56% of the variance** in first-year response predicted from 6 variables (target-height SDS − height SDS, chronological age, injection frequency, GH dose, weight-for-height, birth-weight SDS). Later model: **61% of variance, SD 1.46 cm** with max GH response included; **45%, SD 1.72 cm** without | **HUMAN**, 472–593 children + validation cohorts | 8219483; 10199749 | no |
| 53 | **Adult-height-prediction RMSE, automated vs manual** | Absolute error of the prediction, in cm | Normal children: **BoneXpert AHP RMSE 3.3 cm (boys 10–15 y), 2.7 cm (girls 8–13 y)** vs TW3 3.5 / 3.1 cm. In idiopathic short stature: **Bayley-Pinneau RMSE 6.35 cm (boys), 4.55 cm (girls)** vs BX-AHP **4.71 / 3.72 cm**, improving to **4.46 / 3.35 cm** with parental height | **HUMAN**, Zurich longitudinal (231 + 198); Tübingen ISS (190) | 19926715; 23296315 | no |
| 54 | **Growth-remaining arithmetic: White-Menelaus** | The clinical "cm per remaining year" constant | Growth in the distal femoral and proximal tibial physes is **relatively constant at 9 mm and 6 mm per year of SKELETAL age**, respectively; skeletal age beats chronological age as the predictor | **HUMAN**, 441 healthy leg segments, 221 patients | 31169579 | **yes** |
| 55 | **Head-to-head accuracy of the four growth-remaining methods** | Which arithmetic is least wrong | **White-Menelaus with bone age + fixed inhibition** most accurate: prediction error **1.5 ± 1.5 cm (short leg), 1.0 ± 1.2 cm (long leg), 0.7 ± 0.7 cm (LLD)**; beat Green-Anderson, Moseley straight-line and multiplier (p ≤ 0.002) | **HUMAN**, 191 children 10–17 y to maturity | 39052759 | no |
| 56 | **Bone-age reader variability (GP vs TW3)** | Error term entering every bone-age-based prediction | Inter- and intra-observer ICC **> 0.9** for both methods in trained experts; mean absolute difference between GP and TW3-RUS ≈ **2.5–3.3 months** in most age bands, larger ≥180 months; GP significantly faster | **HUMAN**, 1,725 radiographs, 12 experts | 42001038 | no |
| 57 | **Fluorochrome inter-label distance — the reference method for growth rate** | Direct µm/day elongation from two timed calcein/oxytetracycline/xylenol labels | Manual, manual-digital, computer-assisted and fully automated measurement all showed **excellent agreement and ICC reliability**; computer-assisted methods faster with no loss of reliability | Rabbit (45 tibial physes); method used across all species above | 39868424 | **yes** |
| 58 | **Digital/AI-assisted stature and maturation measurement** | Emerging replacement for the stadiometer and hand radiograph | Prototype smartphone computer-vision app for growth and maturation monitoring in youth sport (**"Maturo"**, description-only, **UNVERIFIED accuracy**); ultrasound-based BAUSport and epiphyseal ossification angle proposed as radiation-free maturity | **HUMAN** | 41969894; 38188108; 41669470 | **yes** |
| 59 | **Resting-zone progenitor depletion as the quantitative substrate of senescence** | The "budget" term: number and proliferative capacity of RZ stem-like cells | Both the **proliferation rate of RZ chondrocytes (continuous BrdU)** and the **number of RZ chondrocytes per unit growth-plate area** decline with age; dexamethasone slows BOTH, conserving the budget | Rabbit | 16614378 | no |
| 60 | **Reversible vs irreversible components of senescence** | Which quantitative terms can be recovered and which cannot | Transient oestrogen: **STRUCTURAL** senescence (plate height, proliferative and hypertrophic cell number, RZ cell number) advanced **IRREVERSIBLY**; **FUNCTIONAL** terms (growth rate, proliferation rate, **hypertrophic cell size**) **NORMALISED** after withdrawal | Rabbit, ovariectomised, 5 wk on / 5 wk off | 24708243 | **yes** |
| 61 | **Senescence is division-counted, not time-counted** | Whether the clock can be paused | Growth inhibition by **hypothyroidism** and, independently, by **tryptophan deficiency** delayed structural, functional AND molecular senescence markers; catch-up growth then followed. Conclusion: senescence "depends on growth", not on age per se | Rat | 20974641; 18174286 | no |
| 62 | **Telomere shortening is NOT the counter** | Excludes one candidate mechanism for the finite budget | Telomere restriction fragment length **did not diminish measurably** in resting-zone chondrocytes at 1, 4, 8 and 56 weeks | Mouse (*Mus castaneus*) | 15795509 | **yes** |
| 63 | **Human spinal growth rate and the spine's share of stature** | The axial arithmetic | Childhood spine growth **1.55 ± 0.21 cm/yr (girls), 1.14 ± 0.23 cm/yr (boys)**, rising in the spurt to **1.75 ± 0.11** and **2.00 ± 0.11 cm/yr**. **At 90% of adult total height a child is 87% of adult SPINE height** — i.e. the spine is relatively behind the whole body at that landmark | **HUMAN**, 54 subjects to maturity | 39585607 | **yes** |
| 64 | **Secular trend in adult height** | The size of the environmental term at population scale | Largest 100-year gain **20.2 cm (South Korean women)** and a comparable gain in Iranian men, from **1,472 studies / 18.6 million participants / 200 countries**, birth cohorts 1896–1996 | **HUMAN** | 27458798 | no |
| 65 | **Preece-Baines model (PB1)** | 5-parameter parametric growth curve, the pre-SITAR standard | Fitted per individual; SITAR was explicitly built to replace it (SITAR matched PB fit with one curve, RSD 6–7 mm). PB1 recently re-endorsed as "essential reading" for growth-curve modelling | **HUMAN** | 39431721; 20647267 | no |
| 66 | **Loss of DNA methylation as a molecular senescence marker** | A molecular clock candidate for the plate | Growth-plate senescence is **associated with loss of DNA methylation** (proposed as the mechanism limiting proliferative capacity in place of telomeres) | Rat/rabbit | 16002553 | **yes** |
| 67 | **Zone-resolved transcriptional senescence** | Structural senescence quantified as declines in specific terms | With age: declines in **growth rate, proliferation rate, growth-plate height and cell number**, with large mRNA changes used as molecular senescence markers | Rat/mouse growth plate, microdissected by zone | 20096814 | no |
| 68 | **Cell-vs-matrix volume accounting between zones (Noonan/Hunziker)** | The single best-resolved measurement of the MATRIX SYNTHESIS term | Upper proliferative → lower hypertrophic: cell numerical density **110,000 → 59,900 cells/mm³**; **mean cell volume 1,174 → 5,530 µm³ (~4.7×)**; **total matrix volume per cell 8,040 → 11,760 µm³/cell (+46%)** — pericellular/territorial **4,580 → 7,390 (+61%)**, interterritorial **3,460 → 4,370 (+26%)**. Fibrillar collagen per cell **3,210 → 5,530 µm³/cell**. Net: cell increase **4,356 µm³** > matrix increase **3,720 µm³/cell** | Miniature pig, proximal tibia (n=6) | 9747793 | **yes** |
| 69 | **Organelle-level accounting of the synthetic apparatus** | Whether the hypertrophy term is bought by more machinery or faster machinery | Rough ER, Golgi and mitochondria measured by ultrastructural stereology at onset and end of hypertrophy; Hunziker 1987 reported **2–5× increases in RER and Golgi surface area and mitochondrial volume** in hypertrophic cells | Rat | 10460464; 3543020 | **yes** |
| 70 | **Cruz-Orive & Hunziker stereological toolbox for anisotropic cells** | The method that makes every number above unbiased | Vertical sections + cycloid test systems for surface area; Dimroth-Watson model for anisotropy; **disector** for cell number; point-sampled intercepts for volume-weighted mean cell volume; nested-design statistics to split biological from sampling variance | Method paper, growth-plate application | 3761364 | **yes** |
| 71 | **Onset and pattern of differential growth** | When the terms diverge between plates in one animal | In Long-Evans rats across 24 timepoints from E17 to P27, **differential growth is fully expressed by postnatal day 13**, and is **primarily associated with differences in hypertrophic cell volume manifested at growth deceleration**; a sharp perinatal fall in velocity affects all four plates simultaneously (systemic term) | Rat, 4 plates | 18404738 | **yes** |
| 72 | **Interspecific kinetic comparison — bat manus vs pes** | Extreme-rate natural experiment on the same terms | In the chiropteran manus **final hypertrophic cell size and shape are achieved EARLY in the hypertrophic zone**, unlike most mammals but like fast-growing frogs and precocial birds — i.e. the same terms are re-timed rather than re-scaled | Mouse (*Mus musculus*) vs big brown bat (*Eptesicus fuscus*) | 18160802; 18160801 | **yes** |
| 73 | **Age-based reference ranges for annual height velocity (LMS)** | The population distribution of the output variable | 3rd–97th HV percentiles from **>4,000 annual (12 ± 1 mo) measurements in ~1,500 US children** aged 5–19, with separate ranges for earlier/average/later maturers; built with the LMS method | **HUMAN** (Bone Mineral Density in Childhood Study) | 24601728 | no |
| 74 | **Tanner-Whitehouse clinical longitudinal height and height-velocity standards** | The original velocity-centile machinery, with tempo conditioning | Centiles given separately for **early, average and late maturers** — the first formal handling of tempo in a clinical chart (numerics not in the retrieved records: **UNVERIFIED**) | **HUMAN**, British 1965 and North American | 952550; 3875704; 8456221 | no |
| 75 | **EOS low-dose biplanar stereoradiography for limb length** | Measurement accuracy of the imaging modality used to track segment growth | Mean absolute error vs true femur length: **EOS-Slow 2.6 mm (0.5%), EOS-Fast 3.6 mm (0.8%), CT scanogram 6.3 mm (1.3%), conventional radiograph 42.2 mm (8.8%)**; ICC > 0.90; EOS-Fast skin dose **0.68 mrad** vs 29.01 mrad for conventional | **HUMAN** phantom + clinical | 24306706 | **yes** |
| 76 | **WHO 2006 standard vs CDC 2000 reference** | Which reference population you compute the Z-score against changes the answer | The WHO charts are **prescriptive** (breastfed, optimal-conditions international sample); the CDC charts are **descriptive** of a US population. Switching references changes measured prevalence of shortness/obesity and the frequency of percentile crossing | **HUMAN** | 17182816; 18619613; 21242198 | no |
| 77 | **Growth-plate stress sensitivity translated to the human spine ("vicious cycle" arithmetic)** | Whether the measured animal coefficient explains observed human deformity progression | Calculated spinal loading asymmetry × measured growth sensitivity to compression reproduces observed AIS progression rates — an explicit end-to-end quantitative test of a growth model against a human phenotype | Model, calibrated on animal data, tested against **HUMAN** curve progression | 17653775 | **yes** |
| 78 | **KIGS / prediction-model responsiveness as a "growth reserve" readout** | Studentised residual from a prediction model as a measure of individual responsiveness | Prediction models proposed as instruments to **measure GH responsiveness** rather than only to forecast; requires an explicit variance-explained figure (45–61%, above) to be interpretable | **HUMAN** | 11684876 | **yes** |
| 79 | **Continuum-based particle (agent-like) model of the growth plate with PTHrP–Ihh signalling** | In-silico test of whether a signalling timing rule can maintain plate architecture | Extends a continuum-particle tissue-morphogenesis model to include PTHrP and Ihh, coupling biochemical and mechanical regulation of individual cells, to ask how RZ PTHrP expression timing relative to SOC formation preserves the plate | In silico (mouse-parameterised) | 39549120 | **yes** |
| 80 | **Reaction-diffusion model of growth control by systemic + local feedback** | Formal analysis of when a growth field is stable vs patterns | Reaction-diffusion equations for endocrine signalling and inter-tissue communication; identifies bifurcation conditions for spatial-structure emergence in tissue growth | In silico (generic) | 40880457 | **yes** |
| 81 | **Hormone-gradient / IGF cell-kinetics model of the plate (Kember)** | Early attempt at a mechanistic ODE model of plate kinetics | Model based on IGF-I / IGF-II distribution and receptor occupancy driving proliferation, solved for the one-dimensional time-independent case | Mathematical (mammalian plate) | 7548445 | **yes** |

---

## THE COMPLETE SET OF MULTIPLICATIVE TERMS THAT PRODUCE LONGITUDINAL GROWTH, WITH MEASURED VALUES

Longitudinal growth is, in the literature retrieved here, decomposed at four nested levels. The terms
below are the complete set that appears in the primary kinetic literature; each is given with the measured
value and the species it was measured in.

### LEVEL 1 — the identity for ONE growth plate, per day
The elongation of a single plate per day is, in the Wilsman/Hunziker formulation, the number of new
chondrocytes each column produces per day multiplied by the height each of those cells ends up occupying
along the growth axis, that height being made of three separable parts:

**G (µm/day) = P (cells per column per day) × [ h_division + h_matrix + h_hypertrophy ]**

| term | what it is | measured value | species | PMID |
|---|---|---|---|---|
| **P — cell production per column per day** | throughput | **8 cells/column/day** (1 lost to vascular invasion every 3 h) | rat prox. tibia | 3543020 |
| **P (whole-plate form)** | absolute throughput | **16,400 cells/day** (prox. tibia) vs **3,700/day** (prox. radius) | rat, 28 d | 8982136 |
| **h_division** | height contributed by making the cell at all | **9%** of elongation (fast plate) | rat prox. tibia | 8982136 |
| **h_matrix** | height contributed by extracellular matrix laid down per cell | **32%** (fast plate) → **49%** (slow plate) | rat, 4 plates | 8982136 |
| **h_hypertrophy** | height contributed by chondrocytic enlargement | **59%** (fast plate) → **44%** (slow plate) | rat, 4 plates | 8982136 |

Sub-terms of P:
| term | measured value | species | PMID |
|---|---|---|---|
| total cell-cycle time Tc | **30.9 / 34.0 / 48.7 / 76.3 h** across four plates in ONE animal | rat, 28 d | 8764865 |
| S phase | **3.4–6.1 h** | rat | 8764865 |
| G2 | **3.0 h** | rat | 8764865 |
| M | **0.5–0.6 h** | rat | 8764865 |
| G1 | the residual — and it carries **almost all** the between-plate difference | rat | 8764865 |
| number of proliferative cells per column | the other multiplier of P; changes with mechanical load (regression coefficient **0.72**) | rat/calf/rabbit | 17532281 |

Sub-terms of h_hypertrophy:
| term | measured value | species | PMID |
|---|---|---|---|
| terminal hypertrophic cell VOLUME | correlates with growth rate at **r = 0.98 (rat), 0.83 (pig)** | rat, pig | 2010838 |
| cell height increase | **×4** proliferative → late hypertrophic | rat | 3543020 |
| cell volume increase | **×10** (rat); **1,174 → 5,530 µm³, ×4.7** (pig) | rat; pig | 3543020; 9747793 |
| rate of volume acquisition | **~50 µm³/h for 30 h, then ~800 µm³/h for 20 h** | rat | 7943757 |
| composition of the enlargement | 3 phases, one of which is **swelling with dry-mass dilution**; the phase that differs between fast and slow plates is the third (dry-mass increase at low density), and it is **IGF-dependent** | mouse/mammal | 23485973 |
| load sensitivity | regression coefficient **1.39** — ~2× the proliferation term | rat/calf/rabbit | 17532281 |

Sub-terms of h_matrix:
| term | measured value | species | PMID |
|---|---|---|---|
| total matrix volume per cell | **8,040 → 11,760 µm³/cell (+46%)** proliferative → hypertrophic | miniature pig | 9747793 |
| pericellular/territorial | **4,580 → 7,390 µm³/cell (+61%)** | pig | 9747793 |
| interterritorial | **3,460 → 4,370 µm³/cell (+26%)** | pig | 9747793 |
| fibrillar collagen per cell | **3,210 → 5,530 µm³/cell** | pig | 9747793 |
| cell vs matrix, head to head | cell increase **4,356 µm³** > matrix increase **3,720 µm³/cell** | pig | 9747793 |
| synthetic machinery | RER/Golgi surface and mitochondrial volume up **2–5×** in hypertrophy | rat | 3543020; 10460464 |

### LEVEL 2 — the budget that P draws down
Throughput is not free: it is drawn from a finite resting-zone progenitor pool.
| term | measured value | species | PMID |
|---|---|---|---|
| RZ progenitor NUMBER per unit plate area | declines with age; declines faster under oestrogen and **the decline is irreversible** | rabbit | 16614378; 24708243 |
| RZ progenitor PROLIFERATION rate | declines with age; **slowed by dexamethasone**, conserving the budget | rabbit | 16614378 |
| what the clock counts | growth, not time — hypothyroidism AND tryptophan deficiency both delay senescence markers | rat | 20974641; 18174286 |
| what the clock is NOT | **telomere length does not shorten** in RZ chondrocytes | mouse | 15795509 |
| clone architecture | best-fit clone length **1,000–2,000 µm** | rabbit | 2050577 |
| what is reversible vs not | structural terms (plate height, cell numbers) irreversible; functional terms (growth rate, proliferation rate, **hypertrophic cell size**) reversible | rabbit | 24708243 |

### LEVEL 3 — from one plate to one bone, and one bone to stature
| term | measured value | species | PMID |
|---|---|---|---|
| distal femur share of femoral growth | **~66%** (histology + serial radiographs); **~70%**, rising 60%→90% with age | **HUMAN** | 917957; 1735225 |
| proximal tibia share | **~57%**, rising 50%→80% | **HUMAN** | 1735225 |
| proximal fibula share | **61%** | **HUMAN** | 9005920 |
| proximal humerus share | **~80%**, →90% after age 11 | **HUMAN** | 2060215 |
| distal ulna / distal radius share | **~85% / ~80%**, → 95% / 90% | **HUMAN** | 2060215 |
| cm per skeletal year, distal femur / proximal tibia | **9 mm / 6 mm per skeletal year** | **HUMAN** | 31169579 |
| distal femur cm/yr from age 7 | **~1.3 cm/yr**, halving in the last two years | **HUMAN** | 1735225 |
| spine cm/yr | **1.55 (F) / 1.14 (M) cm/yr** in childhood; **1.75 / 2.00 cm/yr** in the spurt | **HUMAN** | 39585607 |
| spine as fraction of stature at a landmark | at **90% of adult total height** a child is **87% of adult spine height** | **HUMAN** | 39585607 |
| segment/stature fractions | humerus **18→20%** of standing height; radius **13→15%** | **HUMAN** | 3356718 |
| sitting-height:standing-height ratio | falls prepuberty→early puberty, rises in late puberty; ancestry-dependent | **HUMAN** | 32579888 |

### LEVEL 4 — the whole-organism curve
| term | measured value | species | PMID |
|---|---|---|---|
| age at peak height velocity | **12.0 y (girls), 13.9 y (boys)** | **HUMAN** | 32429758 |
| peak velocity | **4–8 % per year** across ten anthropometric measures | **HUMAN** | 32429758 |
| decomposition into phases | ICP (3 additive components); QEPS (4 shape-invariant functions with a separable pubertal term) | **HUMAN** | 2488676; 27297288 |
| curve-model fit | SITAR: **99% of variance, residual SD 6–7 mm** | **HUMAN** | 20647267 |
| discontinuity of the curve | saltations of **0.5–2.5 cm** separated by stasis | **HUMAN** infants | 1439787 |
| heritability | **0.87–0.93 (men)**, 0.68–0.93 (women) | **HUMAN** | 14624724 |
| environmental headroom | **20.2 cm** gain per century, best case | **HUMAN** | 27458798 |

### MODIFIER TERMS THAT MULTIPLY THE ABOVE
| term | measured value | species | PMID |
|---|---|---|---|
| sustained mechanical stress | **17.1% growth change per 0.1 MPa** (range 9.2–23.9%) | rat, rabbit, calf | 16705695 |
| control elongation rate range | **30 µm/day (rat vertebra) → 366 µm/day (rabbit prox. tibia)** | 3 species | 16705695 |
| compression vs distraction asymmetry | compression **52%**, distraction **113%** of control | rat | 12377917 |
| site-specific senescence timing | small bones senesce earlier than large ones — the origin of proportion | mouse | 30036371 |
| cell number as the proportion-setter | **cell number** is the common driver of limb AND vertebral proportion | mouse, jerboa | 41073372 |

---

## WHICH TERMS HAVE EVER BEEN MEASURED IN A HUMAN

**MEASURED IN HUMANS, WITH NUMBERS**
- Stature, sitting height, subischial length, arm span, knee height, segment proportions, and their
  references (32579888, 15863466, 39072793).
- Height velocity and its centiles, APV and PV (24601728, 32429758, 952550).
- The share of growth taken by each individual physis (917957 — the only human study that used HISTOLOGY of
  the plate combined with serial radiographs; 1735225, 2060215, 9005920, 3356718).
- Growth remaining per skeletal year at the knee: **9 mm distal femur, 6 mm proximal tibia** (31169579).
- Spinal growth rate in cm/yr and the spine's fraction of adult stature (39585607).
- Bone-age maturity and its error (19116188, 42045323, 42001038).
- Adult-height prediction error in centimetres (19926715, 23296315, 33900130, 39052759).
- Heritability, mid-parental regression and its bias (14624724, 39564936, 9773847, 39201851).
- Diurnal stature loss and measurement error (16354217, 9389235, 1734826, 30689550, 16431557).
- The secular trend (27458798).
- **In vivo physeal microstructure by DTI** — tract volume and length in the living distal femur and
  proximal tibia, correlating with subsequent height gain at r² ≈ 0.46–0.49 (35315716, 39516384). This is
  the closest anything comes to measuring a growth-plate kinetic term in a living child.

**MEASURED IN HUMAN TISSUE, BUT ESSENTIALLY ONCE AND WITHOUT PUBLIC NUMBERS**
- **Labelling index, number of proliferative-zone cells, and hypertrophic cell height** — Thurston & Kember
  1985 (3864550) labelled human growth plates in vitro with tritiated thymidine. **Four subjects; two gave
  no labelled cells at all.** The abstract states the parameters were measured but reports no values, so I
  record the numbers as **UNVERIFIED**. This appears to be the only direct cell-kinetic measurement of a
  human growth plate in the retrieved literature.

**NEVER MEASURED IN A HUMAN, AS FAR AS THESE SEARCHES REACH**
- **Cell-cycle time (Tc) of human proliferative chondrocytes**, and the durations of G1/S/G2/M. Every value
  in this domain is rat (8764865).
- **Cells produced per column per day** in a human plate. Human 8-cells/day-equivalents do not exist;
  Hunziker's figure is rat (3543020).
- **Terminal hypertrophic cell volume in a human plate**, and therefore the Breur volume-vs-rate regression
  in humans. All values are rat, pig, bird (2010838, 8146454).
- **Matrix volume per cell / matrix synthesis term in humans.** The best resolved measurement is miniature
  pig (9747793).
- **Resting-zone progenitor number across human pubertal stage** — the budget term. All values are rabbit
  (16614378, 24708243).
- **Elongation rate in µm/day of a named human physis measured by fluorochrome labelling.** Tetracycline and
  calcein labelling is the reference method (39868424) but is not performed in healthy children.
- Consequently: **the three-way percentage split of human longitudinal growth into division, matrix and
  hypertrophy has never been measured.** The 9/32/59 split is rat proximal tibia.

---

## HOW MUCH HEIGHT IS ARITHMETICALLY AVAILABLE FROM EACH TERM

Stated as: what the measured numbers imply about the maximum that could be extracted from moving each term,
and what the measurement noise floor is.

**1. HYPERTROPHY (h_term) — the largest single term.** 59% of elongation in a fast rat plate, 44% in a slow
one (8982136); volume correlates with rate at r = 0.98 (2010838); and it is the term that carries ~2× the
weight of proliferation under mechanical modulation (regression coefficients 1.39 vs 0.72, 17532281).
Arithmetically: the observed spread of terminal hypertrophic volume across plates within a single animal
tracks an **8-fold** spread of elongation rate (50→400 µm/day, 8764865). ⚠ But note the constraint from
24708243: hypertrophic cell size is one of the **reversible** functional terms — it normalises when a
perturbation is withdrawn — so it is a rate lever, not a budget lever.

**2. MATRIX (h_matrix) — 32–49% of elongation and larger in SLOW plates.** Per-cell matrix volume rises
only 46% across the plate against a ~470% rise in cell volume (9747793), so a proportional change in the
matrix term buys less than the same proportional change in the cell term. Its share is highest exactly
where growth is slowest, which is the awkward direction.

**3. DIVISION (h_division) — 9% directly, but it sets P.** The direct height contribution of making the
cell is small. The leverage is via **P**: a plate with Tc = 30.9 h produces ~4× the cells of one with
Tc = 76.3 h (16,400 vs 3,700/day, 8982136/8764865). But throughput draws on the budget, and the budget is
finite (16614378) and the clock counts divisions rather than time (20974641, 18174286) — so raising P
without raising the budget converts reserve into height sooner, not into more height.

**4. THE PERIOD (the budget) — the term with the largest theoretical headroom and no direct human number.**
Transient oestrogen exposure irreversibly advanced structural senescence and hastened fusion (24708243);
conversely growth-inhibiting conditions delayed it and were followed by catch-up (18174286). Arithmetically
the term is worth **9 mm per skeletal year at the distal femur plus 6 mm at the proximal tibia = ~1.5 cm of
leg per extra skeletal year** (31169579), plus **1.1–2.0 cm/yr of spine** (39585607) — i.e. of order
**2.5–3.5 cm of stature per extra skeletal year** at adolescent rates.

**5. SITE / WHICH PHYSIS.** Not all physes pay into stature. The distal femur carries ~70% of femoral growth
(1735225), the proximal humerus ~80% of humeral growth (2060215) — and the humerus contributes nothing to
standing height. At maximum height velocity, DTI puts the proximal tibia at **37.4%** and the distal femur
at ~62.6% of total knee growth potential (39516384), consistent with the 9:6 mm ratio.

**6. THE AXIAL COMPARTMENT.** Spine growth is **1.14–2.00 cm/yr** depending on sex and phase, and at 90% of
adult stature a child still has **13% of spine height** to come vs 10% of total height (39585607) — the
trunk is the compartment that finishes last.

**7. MECHANICAL MODULATION.** **17.1% of growth rate per 0.1 MPa** of sustained stress, apparently linear
and reasonably conserved across rat, rabbit and calf and two sites (16705695). Applied asymmetrically this
is what drives deformity; applied symmetrically it is a real but bounded lever on rate, not on budget.

**8. GENETICS vs ENVIRONMENT — the outer bounds.** Twin heritability of adult height is **0.87–0.93 in
men** (14624724), so the environmental term is small within an affluent population — yet the between-cohort
secular gain reached **20.2 cm per century** in the best case (27458798). Mid-parental height explains only
**36–40% of variance** and is biased **+2.7 cm** uncorrected (39201851).

**9. THE IRREDUCIBLE PREDICTION ERROR — the number that bounds every claim of effect.** Adult-height
prediction RMSE is **2.7–3.3 cm** in normal children with automated bone age and **4.6–6.4 cm** in short
children with Bayley-Pinneau (19926715, 23296315). DTI does better (**RMSE 1.7–1.8 cm**, 35315716). Growth
remaining at the knee is predicted to **0.7 ± 0.7 cm** for the discrepancy but only **1.5 ± 1.5 cm** for the
short leg (39052759). **Any intervention claiming less than ~2–3 cm cannot be resolved against prediction
error in an uncontrolled series.**

**10. THE MEASUREMENT NOISE FLOOR.** Diurnal stature loss is **0.47 cm** on average and up to **~1 cm**
within a subject (16354217, 1734826), **almost all of it axial** (0.79% of sitting height vs 0.43% of
standing height, 30689550), front-loaded into the morning (9389235). Single-observer SEM is **0.12 cm**
(1734826); routine reproducibility SD is **0.30–0.31 cm** (9389235). Automated bone age resolves **0.23
years** (42045323) against a manual precision of 0.63 y. **An unstandardised measurement time can create or
erase a centimetre of apparent annual growth.**

---

## WHAT I COULD NOT VERIFY

1. **The numeric results of the only human growth-plate cell-kinetic study.** Thurston & Kember 1985
   (3864550) report human labelling index, proliferative cell number and hypertrophic cell heights; the
   abstract contains no figures and I could not obtain the full text. Recorded as UNVERIFIED.
2. **Bayley-Pinneau's own percentage-of-adult-height tables** (the "how much per bone-age year" table). I
   found many head-to-head evaluations of the method but did not retrieve the original tabulated
   percentages. The White-Menelaus 9 mm / 6 mm constants (31169579) are the verified substitute.
3. **Tanner-Whitehouse velocity centile numeric values** (952550, 3875704, 8456221) — abstracts describe the
   charts but do not print centile values.
4. **Cole 2025 "The LMS method should not be used to construct velocity centiles in puberty"** (39570025) —
   title only; no abstract available, so the quantitative basis of that recommendation is unverified.
5. **Preece-Baines 1978 original parameter definitions and typical values** — I retrieved only a 2024
   commentary (39431721), not the 1978 primary.
6. **NCD-RisC 2016 country-level and sex-specific numbers beyond the headline 20.2 cm** — the author list
   swamped the abstract retrieval; only the headline figure is verified (27458798).
7. **Avian hypertrophic-volume regression slope** (8146454) — abstract truncated in retrieval; only the
   qualitative conclusion (flat-cell zone size dominates in birds) is verified, from 2267417.
8. **Any measured cell-cycle time, hypertrophic cell volume, matrix volume per cell or per-column cell
   production rate for a HUMAN growth plate.** I searched for these directly and found none. This is
   reported as an absence in the literature, not as a failure to retrieve — but I cannot exclude that such
   values exist in older monographs or non-indexed sources.
9. **Quantitative accuracy figures for the "Maturo" smartphone maturity app** (41969894) — a description
   paper only.
10. Europe PMC returned intermittent 503/504 errors during several queries; a small number of searches were
    re-run and may not have been fully exhaustive.
