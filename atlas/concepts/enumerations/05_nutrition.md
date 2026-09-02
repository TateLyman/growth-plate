# DOMAIN 05 — NUTRITION AND METABOLISM — FULL CONCEPT-SPACE ENUMERATION (R436)

**80 rows · 38 marked OBSCURE · 98 distinct PMIDs · 18 explicit UNVERIFIED flags.**
Sections: A energy/macronutrients (1–14) · B foods (15–25) · C micronutrients (26–42) ·
D metabolic states (43–54) · E growth-plate cellular metabolism (55–66) · F population evidence (67–80).

**Method.** Every row below was reached by EXTERNAL search (Europe PMC REST API sorted by
citation count, NCBI eutils efetch for abstracts, WebSearch/WebFetch for registries and
regulatory/consensus documents). Nothing was derived from the atlas. PMIDs are copied from
the API response; where I could not verify a number I have written `UNVERIFIED`.

**Reading the DEFICIENCY vs TRUE ELEVATION column.** This is the column that matters most and
it is the column the nutrition literature is worst at. Almost the entire evidence base is
*deficiency correction in a depleted population*. A result from a deficient organism is a
claim about the deficit (this is the single most common error in the field). I have marked
`TRUE ELEVATION` only where a supra-adequate intake was given to an organism that was already
replete AND a linear-growth endpoint moved.

**Effect-size convention.** Where the source reports height-for-age Z (HAZ) or an SD effect
size rather than centimetres I say so; 1 HAZ ≈ 3–4 cm in mid-childhood but converting is the
author's inference, not the trial's, so I do not silently convert.

---

## THE TABLE

| # | INPUT | DIRECTION | HUMAN EFFECT (cm) | EVIDENCE + PMID | DEFICIENCY-CORRECTION OR TRUE ELEVATION? | OBSCURE? |
|---|---|---|---|---|---|---|
| **A. ENERGY AND MACRONUTRIENTS** |
| 1 | Total dietary energy (chronic deficit) | ↓ height when deficient; no gain above adequacy | Stunting = −2 HAZ by definition; INCAP Atole (energy+protein+micronutrients, first 1000 d) raised adult body size in those supplemented through age 3 y | INCAP randomised-by-village trial, review PMID 28117514; cohort profile PMID 18285366; long-term human-capital review PMID 20032473 | **DEFICIENCY CORRECTION.** No trial has raised energy above adequacy in a replete child and gained height | no |
| 2 | Community supplementary feeding (extra food, LMIC) | ↑ small when baseline deficient | Cochrane: effects on height "small and inconsistent"; typically <0.2 HAZ | Cochrane review PMID 22696347 | DEFICIENCY CORRECTION | no |
| 3 | Small-quantity lipid-based nutrient supplements (SQ-LNS) | ↑ small | Pooled LAZ gain modest; expressed as "height-age" and "proportion of maximal benefit", PMB well under 100% | Meta-analysis of SQ-LNS trials PMID 41125609; Burkina Faso trial PMID 25816354 | DEFICIENCY CORRECTION | no |
| 4 | Total protein QUANTITY in a child already meeting requirement | ~0 | 18 trials of supplemental protein/AA in children 6–35 mo: 8 hospital catch-up studies needed *higher* protein for accelerated catch-up; **10 community studies showed no consistent benefit** | Arsenault & Brown, Nutr Rev, PMID 28938793 | Catch-up arm = deficiency correction; community arm ≈ TRUE-ELEVATION TEST, and it is NULL | no |
| 5 | High protein in infant formula (early-protein hypothesis) | ↑ weight, ↑ IGF-1; height effect small/absent | European Childhood Obesity Trial: 1138 formula-fed infants randomised high vs low cow-milk protein → higher IGF-1, insulin, BCAAs and weight gain | PMID 21849603; systematic review PMID 35261578 | TRUE ELEVATION (well-nourished European infants) — but the endpoint that moved was **adiposity, not stature** | no |
| 6 | Protein QUALITY / limiting amino acid (lysine) in cereal-based diets | ↑ some status indices; height endpoint weak | Lysine-fortified wheat flour trials in Pakistan, China, Syria: improved some nutritional/immune indices; **no convincing linear-growth endpoint** | PMID 15214256 (Pakistan), 15214257 (China), 18947029 (Syria); overview PMID 15214255 | DEFICIENCY CORRECTION of a limiting AA; growth endpoint UNVERIFIED/weak | **YES** |
| 7 | Branched-chain amino acids / leucine (mTORC1 signal) | mechanistic ↑ mTORC1; no human height endpoint | Circulating BCAAs track obesity and future insulin resistance in children — i.e. the marker of high BCAA exposure is a *metabolic* not a *stature* phenotype | PMID 22961720; mTOR in skeletal development review PMID 29423330 | Neither — no elevation trial with a length endpoint exists | **YES** |
| 8 | Arginine / ornithine (GH secretagogue) | ↑ acute GH pulse; no height endpoint | Arginine is a standard GH-stimulation *test* agent; chronic oral arginine has no randomised linear-growth endpoint I could find | UNVERIFIED for a height RCT | Would be TRUE ELEVATION if tested; untested | **YES** |
| 9 | Glutamine | mechanistic; substrate for α-KG and collagen hydroxylation | Glut1 deletion in postnatal cartilage reprograms chondrocytes toward **enhanced glutamine oxidation**; glutamine flux → α-KG → proline/lysine hydroxylation on collagen | Glut1 PMID 34426569 (mouse); HIF-1α/glutamine/collagen PMID 30651640 (mouse, Nature); review PMID 36120644 | Mechanism only; no human elevation trial | **YES** |
| 10 | Methionine / cysteine / taurine (sulfur amino acids) | substrate for the sulfate pool | No human linear-growth RCT located. Taurine's growth literature is aquaculture/livestock, not human stature | UNVERIFIED | Untested as elevation | **YES** |
| 11 | Dietary fat quantity / lipid AVAILABILITY | ↓ lipid favours CHONDROGENESIS | **Lipid scarcity drives skeletal progenitors toward cartilage via FOXO→SOX9**; abundant lipid pushes them to bone | van Gastel et al., Nature, PMID 32103177 (mouse) | Mechanism, direction is *counter-intuitive*: LESS lipid = more chondrogenic. No human height endpoint | **YES** |
| 12 | Dietary cholesterol / cholesterol synthesis | required for hedgehog signalling; deficiency → dysplasia + short stature | Smith–Lemli–Opitz (DHCR7 deficiency) — cholesterol supplementation is standard care; growth endpoint modest | UNVERIFIED for a randomised height endpoint | DEFICIENCY CORRECTION in a genetic disease | **YES** |
| 13 | n-3 LC-PUFA / fish oil | no reliable height effect | Fish-consumption RCT meta-analysis in children reports micronutrient-status outcomes, not stature | PMID 42344871 (micronutrient status, not height) | Neither established | no |
| 14 | Glycaemic load / high-sugar diet | ↑ insulin & IGF-1, ↑ adiposity, earlier puberty | No height RCT; observational only | Review PMID 25538876 (nutrition & pubertal development) | Weak/observational | no |
| **B. FOODS WITH CLAIMED HEIGHT EFFECTS** |
| 15 | **MILK — in well-nourished children 6–18 y** | **NO height effect** | Meta-analysis of **17 RCTs, n=2844**: milk raised body weight (+0.48 kg) and lean mass (+0.21 kg) but **height, fat mass and waist were UNCHANGED** | Kang, Sotunde & Weiler, Adv Nutr, PMID 30839054 | **TRUE-ELEVATION TEST, AND IT IS NULL FOR HEIGHT.** The single most important negative in this domain | no |
| 16 | Milk — in socioeconomically disadvantaged children | ↑ trivially | Free school milk RCT, 581 UK children aged 7–8, 190 mL/d for 6 terms: **+2.93 mm over 21.5 months** (P<0.05); authors state the benefit in an unselected population would be smaller still | Baker et al., PMID 6892711 | DEFICIENCY CORRECTION, and the size is ~3 mm | no |
| 17 | Milk fortified with calcium ± vitamin D (Chinese girls, 10 y at baseline) | ↑ sitting height only | 3 y after withdrawal: calcium-fortified-milk group had **+0.9 ± 0.3% greater gain in SITTING height** (P=0.02); no sustained BMC/BMD difference; no change in menarcheal age | Zhu et al., PMID 16522922 | Mixed; population had low calcium intake | **YES** (the effect is TRUNK-specific and almost never quoted) |
| 18 | **Milk raises IGF-1, and it is NOT the protein** | ↑ IGF-1 | 24 boys aged 8 y, 7 days: 1.5 L skimmed milk raised **s-IGF-I by 19%** and IGF-I/IGFBP-3 by 13%; **the same protein load as MEAT did nothing** | Hoppe et al., PMID 15054433; also PMID 19174829 (whole milk, late infancy) | **TRUE ELEVATION** in healthy well-nourished boys — but the endpoint is IGF-1, not height | no |
| 19 | Animal protein intake ↔ IGF-1 in affluent children | ↑ IGF-1, ↑ height association | 2.5-y-old Danish children: animal (esp. milk) protein associated with sIGF-I and height | Hoppe et al., PMID 15277169 | Observational; population already replete | no |
| 20 | **EGGS — Lulun Project, Ecuador** | **↑↑ linear growth** | 1 egg/day for 6 months from age 6–9 mo: **LAZ +0.63 (95% CI 0.38–0.88)**, stunting prevalence −47% | Iannotti et al., Pediatrics, PMID 28588101; mechanism (choline, DHA, B12) PMID 29092879 | DEFICIENCY CORRECTION in a stunting population — the largest single-food effect in the literature | no |
| 21 | **EGGS — Mazira Project, Malawi (the replication)** | **NULL** | Individually randomised, **n=660**, 1 egg/day 6 months, same age band: no effect on linear growth | Stewart et al., AJCN, PMID 31386106 | Same design, different setting → **the Lulun effect did not replicate.** Treat "eggs raise height" as unproven | no |
| 22 | Meat as complementary food | ↑ growth, not adiposity | Breastfed infants randomised to meat-based complementary food: greater growth without greater adiposity | PMID 25332329 | DEFICIENCY CORRECTION / quality substitution | no |
| 23 | Micronutrient-fortified milk | ↑ small | Double-masked RCT in Indian children 1–4 y: improved iron status, anaemia and growth | PMID 20730057 | DEFICIENCY CORRECTION | no |
| 24 | Soy / phytoestrogen exposure | no established height effect | No randomised height endpoint located | UNVERIFIED | — | no |
| 25 | Vegan / vegetarian diets in children | ↓ small, plus B12/D risk | Scoping review of vegan diets in child health flags growth risk with poorly-planned diets | PMID 40411748 (scoping review — an INDEX, not a source) | Deficiency risk, not elevation | no |
| **C. MICRONUTRIENTS** |
| 26 | **ZINC** | ↑ in deficient/stunted children | Pooled effect size on height **0.35 SD** (95% CI 0.19–0.51) across 33 RCTs; expressed absolutely, **10 mg/d × 24 wk → +0.37 (±0.25) cm** vs placebo | Brown et al. AJCN PMID 12036814; Imdad & Bhutta PMID 21501440; Cochrane PMID 24826920 | **DEFICIENCY CORRECTION.** Response was *greater in children with low baseline WAZ/HAZ*, i.e. it is the deficit that predicts the gain | no |
| 27 | Zinc + IGF-1 mechanism | ↑ IGF-1 | Growth-retarded Vietnamese children: zinc raised growth and circulating IGF-I | PMID 8599314 | DEFICIENCY CORRECTION | no |
| 28 | Zinc in replete children | ≈0 | Mexican preschoolers: zinc reduced morbidity but **neither zinc nor iron affected growth or body composition** | PMID 8988907 | Closest thing to a null in a less-deficient group | no |
| 29 | **IRON** | ↑ only if anaemic | Anaemic Kenyan schoolchildren: iron improved **appetite and growth**. In non-anaemic children, growth effects absent; iron carries infection/malaria risk | PMID 8169656; risk review PMID 17158406; Pakistan MNP trial PMID 23602230 | DEFICIENCY CORRECTION, and **supplementing the replete is harmful, not neutral** | no |
| 30 | **IODINE** | ↓ height when severely deficient (via thyroid) | Severe deficiency → cretinism with growth retardation; correction restores growth. No evidence supra-adequate iodine adds height | PMID 21802524 (role of iodine in growth, review); PMID 8054857 | DEFICIENCY CORRECTION, and it acts through T4/T3, not directly on the plate | no |
| 31 | **CALCIUM — bone density vs height** | ↑ BMD, **0 height** | 162 Chinese children, 300 mg/d × 18 mo on a 280 mg/d habitual intake: BMC +16.5% vs 13.97%, **"no effect on height increment"** | Lee et al. PMID 7619105; also PMID 7547823; BMD meta-analysis PMID 16980314 | Deficiency correction for BONE; **null for stature** | no |
| 32 | ⚠️ **CALCIUM — the adult-height endpoint, and it is NEGATIVE** | **↓ FINAL HEIGHT** | Gambian boys, 1000 mg Ca/d for 12 mo at age 8–12, followed to 21–25 y: **+2.0 cm taller at 15.5 y**, **age of peak height velocity advanced 7.4 months**, then stopped growing earlier and were **−3.5 ± 1.1 cm SHORTER at 23.5 y (P=0.002)** | Prentice, Dibba, Sawo & Cole, AJCN, PMID 22990031 | **TRUE ELEVATION toward international recommendations — and it COST 3.5 cm of adult stature by advancing puberty.** Velocity bought by spending the growth window | **YES — the single most important row in this table** |
| 33 | **VITAMIN D** | **0 on linear growth** | MDIG trial, Bangladesh, n=1300 pregnancies, 5 arms up to 28,000 IU/wk prenatal ± 26 wk postpartum: **no difference in infant length-for-age Z at 1 y (P=0.23)** in a population with widespread deficiency | Roth et al. NEJM PMID 30089075; meta-analysis PMID 29813153; child meta-analysis PMID 41502896 (no HAZ effect) | **TRUE-ELEVATION TEST IN A DEFICIENT POPULATION — AND IT IS NULL.** Vitamin D corrects rickets; it does not lengthen bone | no |
| 34 | **VITAMIN A** | 0 on HAZ | Meta-analysis 12 RCTs, 6340 children: vitamin A alone **no effect on HAZ, WAZ or WHZ** | PMID 41502896 | Null | no |
| 35 | Vitamin A EXCESS / retinoid exposure | ↓ (premature epiphyseal closure) | Hypervitaminosis A and therapeutic retinoids are a recognised cause of premature physeal closure and bone toxicity | UNVERIFIED for a quantified paediatric height loss | **HARM FROM SUPRA-ADEQUATE INTAKE** — the clearest case in the domain that more is worse | **YES** |
| 36 | Vitamin C / ascorbate | required for collagen prolyl/lysyl hydroxylation | Scurvy is a skeletal disease with subperiosteal haemorrhage and physeal changes; ascorbate is required for hypertrophic differentiation in chondrocyte culture | PMID 1991793 (chick chondrocyte culture: ascorbate alone drives hypertrophic phenotype) | DEFICIENCY CORRECTION; **no megadose height trial exists** | **YES** |
| 37 | Vitamin K1/K2 | no established height effect | Matrix Gla protein is vitamin-K-dependent and regulates hypertrophic cartilage mineralisation; constitutive MGP blocks endochondral ossification in limb | PMID 10579728 (mouse/chick); no human height RCT | Mechanism only; **direction ambiguous** — MGP INHIBITS mineralisation, which the plate requires | **YES** |
| 38 | Vitamin B12 / folate / one-carbon | ↓ if deficient (esp. maternal) | Maternal B12/folate status predicts offspring size and insulin resistance (Pune Maternal Nutrition Study) — observational | PMID 17851649 | Deficiency; observational | no |
| 39 | Choline | plausible mediator of the egg effect | Egg intervention raised choline-pathway biomarkers, B12, vitamin A and DHA alongside the LAZ +0.63 | PMID 29092879 | Mediator hypothesis, not isolated | **YES** |
| 40 | Multiple micronutrient powders (MNP) | ↑ marginal | Cluster-randomised Pakistan MNP ± zinc trial: effects on growth small | PMID 23602230; MMN meta PMID 41451061 | DEFICIENCY CORRECTION | no |
| 41 | Selenium, copper, manganese, boron, silicon | UNVERIFIED for human height | No randomised human linear-growth endpoint located for any of these five. Copper deficiency causes skeletal changes; boron/silicon claims are bone-density and largely animal/in-vitro | UNVERIFIED | Untested | **YES** (five nutrients with essentially no human stature evidence) |
| 42 | Phosphate | ↓ height when deficient (rickets) | Hypophosphataemic rickets is a classic cause of short stature; phosphate is also a direct signal for chondrocyte maturation and apoptosis-associated mineralisation in vitro | PMID 12929932 (ATDC5, in vitro) | DEFICIENCY CORRECTION; excess phosphate drives premature hypertrophic maturation | no |
| **D. METABOLIC STATES** |
| 43 | Stunting / chronic undernutrition | ↓↓ | ~150 million children affected; the reference condition for everything else in this table | PMID 25310000 (review — an INDEX); PMID 21929633 | DEFICIENCY | no |
| 44 | Environmental enteric dysfunction / subclinical gut inflammation | ↓ | Stunted Zimbabwean infants show chronic inflammation and suppressed GH–IGF axis | PMID 24558364 | Not a nutrient at all — the *absorptive/inflammatory* limit on nutrition | no |
| 45 | ⚠️ **WASH (sanitation) vs FEEDING — the decisive factorial trials** | feeding ↑ small; **sanitation 0** | SHINE (Zimbabwe) and WASH Benefits (Bangladesh, Kenya): **improved complementary feeding modestly reduced stunting; basic WASH did NOT**, in three large factorial trials | SHINE PMID 30554749; consensus statement on all three PMID 31462230 | Tells you the *nutritional* arm is the one that works, and that its size is small | no |
| 46 | Obesity / high BMI in childhood | ↑ childhood height, advanced bone age, **no adult-height gain** | Obese children are taller as children with advanced maturation; nationwide Israeli study of 2.79 M adolescents examined obesity against the secular height trend | PMID 31040397; PMID 11128347 (obesity + increased linear growth) | **Velocity without period** — the same trade as row 32 | no |
| 47 | Insulin / hyperinsulinaemia | ↑ IGF-1 bioavailability (lowers IGFBP-1) | Mechanistic; underlies the tall-for-age phenotype of obese children | UNVERIFIED for a randomised height endpoint | — | no |
| 48 | Poorly controlled type 1 diabetes (Mauriac syndrome) | ↓ | Growth failure with hepatomegaly in chronic insulin underdosing; reversed by glycaemic control | UNVERIFIED (PMID not retrieved) | Deficiency of insulin action = deficiency correction | **YES** |
| 49 | **KETOGENIC DIET** | **↓ height velocity** | 22 children on KD: weight, height, BMI and **height velocity all fell significantly**; height velocity correlated **negatively with β-hydroxybutyrate**, and growth was less sensitive to a given IGF-I level on the diet | Spulber et al., Epilepsia, PMID 18727678; cohort PMID 12455855; long-term PMID 24749520 | **A REAL METABOLIC-STATE EFFECT IN NON-DEFICIENT CHILDREN, AND IT IS NEGATIVE.** Ketosis itself, dose-dependently, suppresses linear growth | **YES** |
| 50 | Dietary/energy restriction then refeeding | ↓ then catch-up | Catch-up growth after restriction is real but the literature's endpoint is almost always *weight* and metabolic risk, not banked adult height | PMID 9331546; PMID 28301849 | Loan repaid, not height banked | no |
| 51 | Fasting / intermittent fasting in children | UNVERIFIED | No randomised linear-growth endpoint located | UNVERIFIED | — | **YES** |
| 52 | Rapid infant weight gain ("growth acceleration") | ↑ weight, ↑ later obesity | Consistent observational signal; the intervention literature deliberately tries to *avoid* it | PMID 28301849 | A cost, not a lever | no |
| 53 | Aflatoxin (dietary mycotoxin) | ↓ in observational data; **null when removed by RCT** | Benin cohort: dose-related growth impairment; Gambia cohort: impaired growth + IGF-axis suppression. **But the Kenya cluster-RCT that actually removed aflatoxin cut serum AFB1-lysine adducts and had NO effect on endline LAZ or stunting** | Cohorts PMID 15345349, 30413157; **RCT PMID 30588341**; rat mechanism (hepatic GH resistance) PMID 25938735 | Neither — a *contaminant*, and the removal experiment is negative | **YES** |
| 54 | Coeliac disease / gluten (in susceptible people) | ↓ then catch-up | Malabsorption + restrictive gluten-free diet both cause deficiency; growth recovers on treatment | PMID 41374032 (narrative review — an INDEX) | DEFICIENCY CORRECTION | no |
| **E. CELLULAR METABOLISM OF THE GROWTH PLATE** (all mouse/in-vitro unless stated; none has a human height endpoint) |
| 55 | Hypoxia / HIF-1α and glucose oxidation | prolonged HIF-1α → **skeletal dysplasia** | Chondrocytes are avascular and the plate centre is hypoxic. Prolonged HIF-1α ↓ glucose oxidation → energy deficit → less proliferation, UPR activation, less collagen; but ↑ glutamine flux → ↑ α-KG → **over-hydroxylation of collagen proline/lysine** → protease-resistant matrix | Stegen et al., Nature, PMID 30651640 (mouse) | Neither — a mechanistic BAND: too much HIF-1α is dysplastic | **YES** |
| 56 | Glucose uptake (GLUT1/SLC2A1) | required | Glut1 deletion in postnatal cartilage impairs chondrocyte proliferation and matrix production in the growth plate and reprograms cells to glutamine oxidation | PMID 34426569 (mouse) | Requirement, not a lever | **YES** |
| 57 | **Lipid availability → SOX9** | **LESS lipid = MORE chondrogenic** | Blocking vascular invasion (and hence lipid supply) favours chondrogenesis over osteogenesis; lipid scarcity activates FOXO → SOX9 | van Gastel et al., Nature, PMID 32103177 (mouse) | Mechanism. **Direction is the opposite of nutritional intuition** and nobody has tested a dietary-lipid manipulation against bone length | **YES** |
| 58 | **mTORC1 nutrient sensing in cartilage** | required for growth; but its INACTIVATION is required for differentiation | Cartilage-specific mTOR or Raptor deletion → reduced skeletal growth via reduced protein synthesis; TSC1 deletion (hyperactive mTORC1) **uncouples proliferation from differentiation** via PTHrP and also stunts | PMID 24948603 (cartilage mTOR/Raptor); PMID 27039827 (chondrocyte TSC1); PMID 28069737 (**Osterix-Cre PREosteoblast** Raptor deletion → reduced limb length + smaller epiphyseal growth plates — note this arm is osteoblastic, not chondrocytic) — all mouse | **A BAND with the optimum at wild type** — both loss and gain shorten | **YES** |
| 59 | **Autophagy as the growth-plate's nutrient-recycling arm** | needed for bone growth | **mTORC1 hyperactivation arrests bone growth in lysosomal storage disorders by SUPPRESSING AUTOPHAGY** | PMID 28872463 (mouse) | Mechanism; suggests autophagy induction is the theoretical lever and nothing has been dosed | **YES** |
| 60 | AMPK / energy-charge sensing | UNVERIFIED in growth plate | No growth-plate length endpoint located for AMPK manipulation | UNVERIFIED | — | **YES** |
| 61 | Sirtuins / NAD⁺ | UNVERIFIED for linear growth | The skeletal sirtuin literature is bone mass and osteoarthritis, not longitudinal growth | Family review PMID 36581622 (an INDEX) | — | **YES** |
| 62 | Polyamines (ODC/spermidine) | UNVERIFIED for bone length | ODC is a c-Myc target and the classic proliferation enzyme; ODC-null is embryonic lethal. **No bone-length endpoint located** | PMID 8356088, PMID 11533243 (mouse, non-skeletal) | Untested against stature | **YES** |
| 63 | **Sulfate supply → PAPS → proteoglycan sulfation** | ↓ height when limited | **Brachymorphic mouse = PAPSS2 (SK2) mutation → postnatal chondrodysplasia**; human PAPSS2 loss = brachyolmia; SLC26A2/DTDST loss = achondrogenesis 1B / atelosteogenesis II / diastrophic dysplasia / rMED. Undersulfated CSPGs disrupt **Indian hedgehog** signalling in the growth plate | PAPSS2/brachymorphic PMID 9671738; SLC26A2 PMID 8571951, 15703192, 9575183; Ihh mechanism PMID 19369399 (all mouse/human genetic) | **DEFICIENCY CORRECTION at the genetic level. Nobody has raised sulfate above normal in a replete animal and measured a bone** | **YES** |
| 64 | Hexosamine pathway / O-GlcNAc / glucosamine | UNVERIFIED for length | Glucosamine inhibits aggrecanase-mediated aggrecan catabolism in cartilage explants; no growth-plate length endpoint | PMID 9742213 (in vitro) | Untested | **YES** |
| 65 | Ascorbate as a 2-OG dioxygenase cofactor (collagen hydroxylation) | required | Ascorbate alone drove the hypertrophic phenotype in chick vertebral chondrocyte culture; maximal mineralisation needed ascorbate + β-glycerophosphate | PMID 1991793 (chick, in vitro) | Requirement; **megadose untested and mechanistically two-sided** (it also feeds the JmjC/TET dioxygenases) | **YES** |
| 66 | Inorganic phosphate as a differentiation SIGNAL | ↑ maturation/apoptosis | Pi is a *specific signal* for ATDC5 chondrocyte maturation and apoptosis-associated mineralisation | PMID 12929932 (in vitro) | Mechanism; a nutrient acting as a morphogen, not as a substrate | **YES** |
| **F. POPULATION EVIDENCE AND THE SECULAR TREND** |
| 67 | **The secular trend accrues in INFANCY, not adolescence** | ↑↑ | SITAR analysis of 50 y of Japanese and South Korean data: the growth period **advanced in timing and SHRANK in duration**, and **"most of the height increment seen in adults had already accrued by age 1.5 years"** | Cole & Mori, PMID 28833849 | Population-level deficiency correction — the authors call the secular trend **"the inverse of stunting"** | **YES — this is the most under-quoted fact in the domain** |
| 68 | The Dutch plateau | trend has STOPPED | Dutch height in 2009 was identical to 1997; final height 183.8 cm (M) / 170.7 cm (F) after 150 y of increase; cause "unclear" — either the optimum has been reached or growth-promoting factors have stabilised | Schönbeck et al., PMID 23222908 | **The ceiling exists and a rich population has hit it.** Adding more nutrition to a replete population does nothing | no |
| 69 | Global height trajectories 1985–2019 | mixed | NCD-RisC pooled 2181 studies, 200 countries: height and BMI trajectories diverge by country; some countries gained height without gaining BMI and vice versa | PMID 33160572 | Ecological | no |
| 70 | North vs South Korea | ↓ ~10 cm in the North | Common ancestry, divergent childhood environments from the late-1940s birth cohorts. Pre-school children in the North up to **13 cm shorter**; North Koreans did *not* experience the 20th-century secular increase | Schwekendiek, PMID 18647440; also PMID 29301183 | **The cleanest natural experiment: environment (mostly food + infection), not genes** | no |
| 71 | **The milk hypothesis for the Japanese secular trend** | **NOT SUPPORTED as a sufficient cause** | Japanese children grew taller in *pre-war* years when animal-protein supply was ~zero, and **stopped growing taller in the early 1990s while per-capita milk consumption was still rising** | Takahashi, Hum Biol 1984, PMID 6489988; critique summarised at [scirp.org paper 89648](https://www.scirp.org/journal/paperinformation?paperid=89648) | Ecological; the temporal mismatch is the argument | **YES** |
| 72 | Socioeconomic development as the proximate driver | ↑ | Chinese national surveys 1975–2010 vs UN development indicators: development indices, not any single nutrient, track the height trend | PMID 26452198 | Ecological | no |
| 73 | Education/SES gradient within a rich country | ↑ 5.1 cm | 371,105 Dutch conscripts: **5.1 cm gradient from lowest to highest education level** | PMID 25487837 | Observational; shows the environmental term is still large *inside* a replete population | **YES** |
| 74 | Migration studies (Maya in the USA, South Asians in NL) | ↑ | South Asian children in the Netherlands show a secular trend and differ from Asian-Indian references | PMID 24963814; Turkish/Moroccan children in NL PMID 25938671 | Environmental | no |
| 75 | Family size / resource dilution | ↓ per additional sibling | 389,287 Dutch conscripts: sibship size and birth order relate inversely to height | PMID 30410298 | Environmental, not nutrient-specific | **YES** |
| 76 | **MC3R — the receptor that tells the growth axis how much fuel there is** | LoF → ↓ linear growth, later puberty, ↓ IGF-1 | Humans with MC3R loss-of-function (including a homozygote) have later puberty, **reduced linear growth, reduced lean mass and lower IGF-1**; mice concur. MC4R controls calorie *acquisition*; **MC3R controls the DISPOSITION of calories into growth** | Lam et al., Nature, PMID 34732894 (human + mouse) | **Not a nutrient — the sensor.** Defines the node at which nutritional state is converted into stature, and it is druggable in principle | **YES** |
| 77 | Human milk oligosaccharides / microbiota | ↑ in undernutrition models | Sialylated HMOs are lower in mothers of severely stunted Malawian infants; transferring them into gnotobiotic mice/piglets promotes microbiota-dependent growth | PMID 26898329 (human observational + gnotobiotic animal); PMID 28079170 | DEFICIENCY-CORRECTION context; **the effect is microbiota-dependent, i.e. not a direct nutrient** | **YES** |
| 78 | Breastfeeding vs formula | complex; height effect small | Formula raises early weight gain and IGF-1 more than breast milk (see row 5); no convincing adult-height advantage either way | PMID 21849603; PMID 30110887 | — | no |
| 79 | Probiotics + calcium, 10-y follow-up to adolescence | ~0 | 238 adolescents re-enrolled 10 y after 6 mo of childhood probiotic/calcium milk supplementation; long-term height/weight assessed | PMID 34088920 | Long-term follow-up of a supplementation trial — the right design, and no large durable effect | **YES** |
| 80 | Spirulina in malnourished children | ↑ claimed | Meta-analysis of spirulina in chronic malnutrition | PMID 41541825 (weak: small heterogeneous trials) | DEFICIENCY CONTEXT; **flag as weak evidence** | **YES** |

---

## INTERVENTIONS WITH A HUMAN RANDOMISED HEIGHT ENDPOINT

This is the short list. Almost everything else in the nutrition literature is observational, uses a
proxy (bone density, IGF-1, weight, HAZ in a stunted population) or has no length endpoint at all.

**Randomised, positive, with a real linear-growth endpoint:**

1. **Zinc.** The best-evidenced nutrient in the domain. Pooled height effect **0.35 SD** across 33 RCTs
   (PMID 12036814); in absolute terms **10 mg/d for 24 weeks bought +0.37 cm** (PMID 21501440). The
   meta-regression is the important part: **the gain scaled with how deficient the child was at
   baseline.** In replete children it goes to zero (PMID 8988907).
2. **Eggs — once.** Lulun, Ecuador: 1 egg/day for 6 months, **LAZ +0.63** (PMID 28588101). Then the same
   team ran **Mazira in Malawi with n=660 and got nothing** (PMID 31386106). One trial replicated by
   its own authors and failing is not a finding; it is a warning about setting-dependence.
3. **Improved complementary feeding** in the SHINE factorial trial (PMID 30554749) — small reduction in
   stunting. The paired arm (water/sanitation/hygiene) did nothing, and across all three large factorial
   WASH trials the consensus was **no effect of WASH on stunting** (PMID 31462230).
4. **Micronutrient-fortified milk** in Indian preschoolers (PMID 20730057) — small.
5. **Free school milk** in disadvantaged UK 7–8-year-olds: **+2.93 mm over 21.5 months** (PMID 6892711).
   The authors themselves say the effect in an unselected population would be smaller.
6. **INCAP Atole, Guatemala** — randomised by village, energy + high-quality protein + micronutrients in
   the first 1000 days; adult body size increased in those supplemented through age 3 (PMID 28117514,
   18285366, 20032473). The only intervention here with a plausible adult-stature effect.

**Randomised, and NULL or NEGATIVE — these matter more:**

7. ⚠️ **Calcium is the one intervention with a randomised ADULT-height endpoint, and it is NEGATIVE.**
   Gambian boys, 1000 mg/d for 12 months at age 8–12, followed to 21–25 y: taller at 15.5 y by 2.0 cm,
   **age of peak height velocity advanced by 7.4 months**, and **3.5 cm SHORTER as adults** (P=0.002)
   (PMID 22990031). This is the archetype of the failure mode where velocity is bought by spending the
   growth window. Every trial in this domain that stops at 12 months is blind to it.
8. **Vitamin D.** The MDIG trial (NEJM, PMID 30089075) randomised 1300 Bangladeshi pregnancies to up to
   28,000 IU/week in a population with widespread deficiency and measured infant **length-for-age Z at
   1 year as the PRIMARY outcome**: P=0.23 across five arms. Child meta-analysis agrees — no HAZ effect
   (PMID 41502896). Vitamin D cures rickets; it does not lengthen bone.
9. **Vitamin A.** No effect on HAZ (PMID 41502896).
10. **Calcium in Chinese children** raised bone mineral content and explicitly **"no effect on height
    increment"** (PMID 7619105).
11. **Milk in well-nourished 6–18-year-olds.** 17 RCTs, n=2844: weight ↑, lean mass ↑, **height
    unchanged** (PMID 30839054). This is the cleanest true-elevation test in the whole domain and it
    is null.
12. **Protein/amino-acid supplementation.** 10 community trials in children 6–35 months showed **no
    consistent benefit**; only hospitalised children in catch-up needed more (PMID 28938793).
13. **Aflatoxin removal.** Kenya cluster-RCT reduced serum AFB1-lysine adducts and had **no effect on
    endline LAZ or stunting** (PMID 30588341), despite strong observational associations.
14. **Iron in the non-anaemic.** No growth benefit and a real infection/malaria hazard (PMID 17158406).

**The pattern.** Every positive is deficiency correction; the size is fractions of a centimetre to at
most ~0.6 HAZ; and the one trial that followed subjects to adult height found the supplement had made
them *shorter*. There is, as far as I can find, **no randomised trial in which a supra-adequate intake
of any nutrient given to a replete human increased attained adult height.**

---

## WHAT ACTUALLY DROVE THE SECULAR TREND

The honest answer is that no single nutrient did, and the strongest evidence points at something the
nutrition-supplement framing does not capture.

**1. It happened in infancy, not adolescence — and this is measured, not inferred.**
Cole & Mori's SITAR analysis of 50 years of Japanese and South Korean data (PMID 28833849) decomposes
the trend into size, timing and intensity and reports that **most of the adult height increment had
already accrued by age 1.5 years**, while the growth period **advanced in timing and shrank in
duration**. Their own summary is that the secular trend "represents increased growth in the long bones
during infancy, so it can be viewed as **the inverse of stunting**." That single sentence reorganises
the whole domain: the secular trend is not a story about better adolescent nutrition raising a ceiling,
it is a story about the removal of an early-life insult.

**2. The milk hypothesis fails on timing.** It is the most popular folk explanation, and the Japanese
data refuse it twice: Japanese children grew taller in the **pre-war** period when animal-protein supply
was essentially zero, and they **stopped growing taller in the early 1990s while per-capita milk
consumption was still rising** (Takahashi PMID 6489988 for the original correlation; the temporal
mismatch is laid out in the Japan/Korea food-consumption comparisons). Milk *does* raise IGF-1 in
well-nourished boys, and by something other than its protein (PMID 15054433) — but the randomised height
endpoint in well-nourished children is null (PMID 30839054). **Milk moves the biomarker and not the
bone.**

**3. What the natural experiments say.** North vs South Korea is the cleanest available design — shared
ancestry, divergent environments from the late-1940s birth cohorts, and a gap of roughly 10 cm in adults
with pre-school children up to 13 cm shorter in the North (PMID 18647440). North Korea is also the one
population that **did not participate in the 20th-century secular increase at all**. Whatever drove the
trend elsewhere, its absence there is not genetic.

**4. Infection and the gut are at least as important as the diet, and possibly more —
but the sanitation trials failed anyway.** Stunting is characterised by chronic inflammation and a
suppressed GH–IGF axis (PMID 24558364), and environmental enteric dysfunction was the leading candidate
mechanism (PMID 26542185). Three large factorial trials then tested it and found **no effect of basic
WASH on stunting** (consensus statement PMID 31462230; SHINE PMID 30554749). So: infection is
mechanistically implicated, *basic* sanitation interventions do not fix it, and the feeding arm produces
only a small effect. The realistic reading is that the secular trend was driven by a **bundle** — food
quantity and quality, infectious-disease burden, sanitation, medical care, maternal education, smaller
families, and reduced physical workload in childhood — acting mainly in the first two years, and that no
component of that bundle reproduces the effect on its own.

**5. The trend has a ceiling and rich populations have reached it.** Dutch height stopped increasing
after 150 years; final height 183.8 cm in men and 170.7 cm in women, identical in 1997 and 2009
(PMID 23222908). Chinese national data track the trend to composite socioeconomic development rather
than to any nutrient (PMID 26452198). **Yet a 5.1 cm education gradient persists inside the Netherlands**
(PMID 25487837), which means the environmental term is still large even at the ceiling — it is just not
a term any supplement addresses.

**6. The trend has a cost side that is rarely stated.** The same analyses that show the height trend
show **puberty advancing and the growth period shortening**. Anything that accelerates maturation buys
childhood height and can lose adult height — which is exactly what the Gambian calcium trial measured
directly (PMID 22990031) and what the obesity/height literature implies (PMID 31040397, 11128347).

---

## THE ANALYTICAL RESULT: DEFICIENCY CORRECTION vs TRUE ELEVATION

Counted across the 80 rows:

- **Deficiency correction with a positive height endpoint:** zinc, iodine, iron (if anaemic), protein in
  catch-up, energy in stunting, eggs (once), complementary feeding, INCAP. ~10 rows.
- **True-elevation TESTS that were actually run:** milk in replete 6–18-year-olds (null for height),
  vitamin D at high dose in a deficient population (null for length), high-protein formula in European
  infants (moved weight and IGF-1, not stature), calcium toward international recommendations
  (**negative for adult height**), community protein supplementation (null). **Every one is null or
  negative.**
- **True elevation with a positive height endpoint:** **none found.**
- **Supra-adequate intake that is HARMFUL:** vitamin A / retinoids (premature physeal closure), iron in
  the replete (infection), calcium in pre-pubertal boys (−3.5 cm adult height), ketosis (dose-dependent
  suppression of height velocity).

**The cellular-metabolism rows (55–66) are where the unexploited space is**, and they share one
property: they are all **bands with the optimum at or near wild type**. mTORC1 loss and mTORC1 gain both
shorten. HIF-1α is needed but prolonged HIF-1α is dysplastic. Lipid scarcity — not abundance — is what
pushes progenitors toward cartilage. That shape is fatal to a "more of the nutrient" strategy and it is
the reason the nutrition literature keeps returning nulls in replete organisms: **the plate is a
regulated system operating near its optimum, and food is a permissive input, not a throttle.**

**The one exception worth naming is the sulfation axis (row 63).** It is the only substrate-supply chain
in the growth plate where a *quantitative* deficiency of a simple inorganic anion produces a graded
series of human chondrodysplasias (PAPSS2 → brachyolmia; SLC26A2 → achondrogenesis 1B through recessive
MED), where the mechanism is mapped to Indian hedgehog signalling (PMID 19369399), and where — as far as
I can establish — **nobody has ever raised sulfate above normal in a replete growing animal and put a
caliper on a bone.**

---

## WHAT I COULD NOT VERIFY

Honest reporting of the gaps in this enumeration.

1. **Trace elements — selenium, copper, manganese, boron, silicon.** I could not find a single
   randomised human trial with a linear-growth endpoint for any of these. Searches returned cuproptosis
   and cancer biology for copper, and bone-density/animal work for boron and silicon. Row 41 is marked
   UNVERIFIED and that is the honest state of it.
2. **Taurine, arginine, tryptophan, glutamine as human height interventions.** Arginine is a standard GH
   *stimulation-test* agent, but I found no chronic oral supplementation trial with a stature endpoint.
   The taurine growth literature that exists is aquaculture and livestock.
3. **Mauriac syndrome (row 48).** I did not retrieve a specific PMID; the entry rests on general clinical
   knowledge and is flagged UNVERIFIED.
4. **Vitamin A excess → premature epiphyseal closure (row 35).** I am confident the phenomenon is real
   and reported for hypervitaminosis A and therapeutic retinoids, but **I did not retrieve a paper with a
   quantified paediatric height loss**, so no number is given.
5. **Polyamines, NAD⁺/sirtuins, AMPK and the hexosamine pathway in the growth plate** (rows 60–62, 64).
   Searches were repeatedly captured by the osteoarthritis and cancer literatures. I could not establish
   that any of these has a *longitudinal bone-growth* endpoint in any species. If one exists I did not
   find it, and the rows are marked UNVERIFIED rather than negative.
6. **Effect sizes in centimetres.** Most of this literature reports HAZ/LAZ or SD effect sizes. I have
   NOT converted them, because the conversion depends on age and on the reference SD and would be my
   arithmetic, not the trial's. Only rows 16, 21, 26, 32, 67, 68, 70 and 73 carry a real published
   centimetre figure.
7. **The INCAP adult-height number.** I could confirm that Atole improved adult body size and work
   capacity in those supplemented through age 3 (PMID 20032473, 28117514) but **did not retrieve the
   specific centimetre estimate** from the 1988–89 or 2002–04 follow-up papers.
8. **Full texts.** Everything here is title + abstract from the Europe PMC `resultType=core` response or
   the NCBI eutils abstract endpoint. I did not read full texts, so subgroup analyses, adverse effects
   and dose-response detail beyond the abstract are not captured.
9. **Reviews used as an INDEX, not a source** (declared per the common brief): PMID 25310000 (stunting
   syndrome), 21802524 (iodine), 40411748 (vegan diets), 41374032 (coeliac), 36581622 (sirtuins),
   29423330 (mTOR in skeleton), 36120644 (amino acid metabolism in skeletal cells), 41541825 (spirulina),
   28301849 (catch-up growth).
10. **Weak-evidence flags.** Row 80 (spirulina) and row 17 (sitting-height effect of calcium-fortified
    milk) rest on small or single studies. Row 71's milk-hypothesis critique rests partly on a
    non-PubMed-indexed comparative paper, cited by URL rather than PMID.
