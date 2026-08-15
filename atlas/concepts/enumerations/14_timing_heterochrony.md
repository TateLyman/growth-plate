# DOMAIN 14 — TIMING, HETEROCHRONY, SENESCENCE AND EPIGENETICS
## R436 full-concept-space enumeration — EXTERNAL SEARCH ONLY

**Method.** Everything below was found by external query (Europe PMC REST API `search` endpoint sorted by
citation count, and NCBI eutils `efetch` for abstracts). No file in `/home/user/growth-plate` was read
except the two briefs. Species is carried on every row. `UNVERIFIED` means I could not confirm the
identifier or number against a primary record I actually retrieved in this session. Reviews are marked
`(review)` — an index, not a source.

**Framing.** The subject is bone age 16+, so the PERIOD (how long the plate keeps running) is worth more
than the RATE. Rows are tagged accordingly. Where a mechanism moves both, both are stated.

---

## TABLE

| # | MECHANISM | SETS RATE OR PERIOD? | DIRECTION | EVIDENCE (species + PMID) | AGENT? | OBSCURE? |
|---|---|---|---|---|---|---|
| **A. THE SENESCENCE PROGRAMME — WHAT COUNTS DOWN** |
| A1 | **Growth-plate senescence as a programmed, plate-intrinsic decline** — growth rate, chondrocyte proliferation rate, plate height, proliferative-cell number, hypertrophic-cell number and terminal hypertrophic cell size all fall spontaneously with age | **PERIOD** (and rate) | Declines with age; endpoint is fusion | rabbit, PMID 11381135; review PMID 15380808 | none | no |
| A2 | **The counter is DIVISIONS, not time** — growth-inhibiting conditions conserve proliferative capacity and thereby delay senescence | **PERIOD** | Slowing proliferation *extends* the period | rabbit PMID 11641457; rat PMID 20974641 | any growth-suppressing agent (with a cost) | no |
| A3 | **Hypothyroidism delays senescence** — propylthiouracil in newborn rats, then withdrawal, gives catch-up because plates are less senescent for age | **PERIOD** | Delays | rat, PMID 18174286 | PTU / methimazole (harmful in itself) | no |
| A4 | **Glucocorticoid excess delays senescence** by slowing resting-zone proliferation and conserving replicative capacity | **PERIOD** | Delays (but suppresses rate hard) | rabbit PMID 7925098; review PMID 21164272 | dexamethasone | no |
| A5 | **Loss of DNA methylation in resting-zone chondrocytes tracks senescence in vivo, and the limit is NOT a Hayflick limit** — population doublings in culture did not depend on donor age; methylation fell only with slow in-vivo RZ proliferation, not with fast PZ proliferation, not in culture, not in liver | **PERIOD** | 5mC loss accompanies exhaustion | rabbit, PMID 16002553 | none | **yes** |
| A6 | **CXXC5 rises with senescence and its deletion delays senescence and lengthens tibia** — negative Wnt regulator, elevated as Wnt/β-catenin falls in the senescing rodent plate; *Cxxc5*−/− mice show delayed growth-plate senescence and tibial elongation | **PERIOD** | Removing CXXC5 extends | mouse/rodent, PMID 30971423 | CXXC5–Dishevelled interface peptide (paper's own approach) | **yes** |
| A7 | **Differential aging by anatomical site** — plates in different bones age at different rates, and this is what sets skeletal proportion (femur vs phalanx) | **PERIOD**, site-specific | Site-specific clocks | mouse, PMID 30036371 | none | **yes** |
| A8 | **Estrogen accelerates the entire senescence programme rather than causing fusion directly** — accelerated all seven senescence parameters in ovariectomised rabbits | **PERIOD** | Accelerates (shortens) | rabbit, PMID 11381135 | aromatase inhibitors / GnRHa reverse it | no |
| A9 | **Estrogen irreversibly depletes resting-zone progenitor NUMBER** — 5 wk estradiol then 5 wk washout: RZ cell depletion persisted | **PERIOD** | Irreversible loss | rabbit, PMID 24708243 | AI to prevent | no |
| A10 | **Prior estrogen exposure predicts poor growth on GnRHa** — in 100 girls with central precocious puberty, height velocity on GnRHa was inversely related to severity of prior estrogen exposure | **PERIOD** | Damage already done | human, PMID 14715835 | earlier GnRHa | no |
| A11 | **Aggrecan haploinsufficiency = accelerated bone maturation and early growth cessation** — human *ACAN* truncating variants: short stature, advanced bone age, early cessation | **PERIOD** | Accelerates | human, PMID 24762113 | none | no |
| A12 | **…but ACAN deficiency does NOT sensitise to estrogen-driven senescence** — *Acan*+/− mouse; advanced maturation is not an estrogen-sensitivity phenomenon | **PERIOD** | Negative result, mechanism unresolved | mouse, PMID 42582486 | — | **yes** |
| A13 | **All-trans retinoic acid drives premature growth-plate closure / senescence** — multiomics in rat + ATDC5 | **PERIOD** | Accelerates (harm) | rat + cell line, PMID 41239925 | avoid ATRA / isotretinoin | no |
| A14 | **Raloxifene acts as an estrogen AGONIST at the rabbit plate** — a SERM that hastens fusion rather than sparing it | **PERIOD** | Accelerates | rabbit, PMID 12639932 | avoid raloxifene | **yes** |
| A15 | **SOCS2 loss accelerates growth-plate fusion** (and *Socs2*−/− mice are gigantic) — coupling of GH signalling gain to earlier plate closure | **PERIOD** + rate | More GH signalling → earlier fusion | mouse, PMID 35272487; gigantism PMID 10890450 | — | **yes** |
| A16 | **Resveratrol delays growth-plate fusion and improves bone growth** — the only small molecule I found with an explicit *delayed fusion* endpoint in a fusing species | **PERIOD** | **Delays fusion** | female rabbit, PMID 23840780 | resveratrol (oral) | **yes** |
| A17 | **Rodents (mouse, rat) never fuse their growth plates** — the species barrier that makes most of the mechanistic literature unable to test the period question | **PERIOD** | Species-level absence of fusion | mouse/rat vs rabbit/human, review PMID 21540578 | — | no |
| A18 | **Hox11 paralogues regulate postnatal longitudinal growth and plate proliferation** — dose-dependent; loss abolishes plate establishment in the zeugopod | rate (period at the extreme) | Positional identity gates plate persistence | mouse, PMID 26500224 | none | **yes** |
| **B. THE RESTING-ZONE POOL, STEM CELLS AND CLONAL DYNAMICS** |
| B1 | **Resting zone houses a distinct skeletal stem cell class (PTHrP+)** that generates columnar chondrocytes; formation of the secondary ossification centre confers the stem-cell state | **PERIOD** | Pool size = remaining growth | mouse, PMID 30401834 | none | no |
| B2 | **Resting zone is functionally necessary and sufficient** — ablate PZ+HZ leaving RZ and a full plate regenerates within a week; ectopic RZ reorients columns | **PERIOD** | RZ is the origin | rabbit, PMID 11956168 | none | no |
| B3 | **Resting-zone chondrocyte number and proliferation rate both fall with age** — direct depletion evidence | **PERIOD** | Depletion | rabbit, PMID 16614378 | none | no |
| B4 | **RZ chondrocytes are maintained in a Wnt-INHIBITORY environment** — slow-cycling H2B-GFP label-retaining chondrocytes | **PERIOD** | Low Wnt = pool maintenance | mouse, PMID 34309509 | Wnt modulators | **yes** |
| B5 | **Hedgehog activation makes RZ chondrocytes transiently clonally competent, then diverts them to osteogenic fate** | **PERIOD** | Sustained Hh spends the pool | mouse, PMID 38051593 | SMO agonists (two-edged) | **yes** |
| B6 | **ApoE is a pan-marker of ALL resting-zone chondrocytes** — previous markers only partially label the RZ, i.e. the RZ is heterogeneous and prior pool counts were incomplete | **PERIOD** (measurement) | Redefines the denominator | mouse, PMID 40025030 | none | **yes** |
| B7 | **"Quiescence" in the RZ has never been rigorously defined** — systematic review finds the term used for decades without the standard quiescence criteria being tested | **PERIOD** (concept) | Knowledge gap | systematic review, PMID 41795828 | — | **yes** |
| B8 | **Human RZ contains sub-populations with quiescent-stem-cell features** — spatial transcriptomics on rare healthy adolescent human growth-plate biopsies; NKX3-2, SGMS2, WNK4 zone-restricted | **PERIOD** | Human confirmation | human, PMC preprint (2025), PMID UNVERIFIED | none | **yes** |
| B9 | **Excess FGFR3 disrupts RZ turnover via CREB** — Fgfr3^Ach knock-in shows an EXPANDED resting zone with impaired stem-like behaviour, i.e. a jam not a pool | **PERIOD** | Expanded RZ ≠ more growth | mouse, PMID 41748604 | FGFR3 inhibitors | **yes** |
| B10 | **Timing of RZ PTHrP expression relative to SOC formation determines whether the plate is maintained** (computational) | **PERIOD** | Timing-sensitive | in silico, PMID 39549120 | none | **yes** |
| B11 | **Thyroid hormone acts directly on plate chondrocytes to promote hypertrophy and INHIBIT clonal expansion** — the clearest direct link between a systemic hormone and clone size | rate + **PERIOD** | T3 spends clones | rat, PMID 11014246 | thyroid status management | **yes** |
| **C. CATCH-UP GROWTH AND "PLATE MEMORY"** |
| C1 | **Catch-up growth is intrinsic to the plate, not a CNS "sizostat"** — local glucocorticoid to ONE plate was followed by local catch-up in that plate alone | **PERIOD** | Local memory exists | rabbit, PMID 7925098 | — | no |
| C2 | **Catch-up = delayed senescence** — the formal statement of the model | **PERIOD** | Conserved capacity is repaid | rabbit, PMID 11641457; review PMID 23428687 | — | no |
| C3 | **Catch-up occurs ex vivo in cultured metatarsals after dexamethasone withdrawal** — no systemic factor needed | **PERIOD** | Cell-autonomous | rat metatarsal, PMID 19815587 | — | **yes** |
| C4 | **Catch-up also has cell-NONautonomous local and systemic components** — mosaic p21 induction in chondrocytes triggers compensatory responses in unaffected cells | **PERIOD** | Both local and systemic | mouse, PMID 29944650 | — | **yes** |
| C5 | **Nutrition-induced catch-up raises growth-plate HIF-1α** | rate | Refeeding signal | rat, PMID 18201948 | — | **yes** |
| C6 | **Nutrition-induced catch-up restores GHR and IGF-1R protein in the plate** | rate | Local receptor recovery | mouse, PMID 18924581 | — | **yes** |
| C7 | **Leptin limits catch-up by stimulating aromatase IN the growth plate** — refeeding raises leptin → local estrogen → senescence | **PERIOD** | Explains incomplete catch-up | rat, PMID 29615477 | local aromatase inhibition | **yes** |
| C8 | **Short-term fasting then refeeding produces measurable catch-up in bone elongation rate** | rate | Reversible | rat, PMID 12508079 | — | no |
| C9 | **Compensatory/catch-up skeletal elongation in cattle after energy restriction and realimentation** — same phenomenon in a large ungulate; dietary protein modifies it | rate | Species generality | cattle, PMID 33630953 | dietary protein | **yes** |
| C10 | **Catch-up is frequently INCOMPLETE** — permanent deficit after malnutrition; reviews of nutritional catch-up | **PERIOD** | Loss is partly irreversible | human + rat, reviews PMID 25594438, PMID 23428685 | — | no |
| C11 | **Human test of the delayed-senescence hypothesis** — explicitly framed and tested in humans | **PERIOD** | Human evidence | human, PMID 16356444 | — | **yes** |
| C12 | **Casein vs whey during catch-up changes bone quality and efficiency of catch-up** | rate | Protein source matters | rat, PMID 27189324 | dietary protein type | **yes** |
| **D. THE MULTI-ORGAN JUVENILE GROWTH-LIMITING PROGRAMME (the "extended" clock)** |
| D1 | **An imprinted gene network (incl. Igf2, Dlk1, Mest, Plagl1, Peg3, Grb10) is coordinately DOWN-regulated during postnatal growth deceleration in multiple organs** | **PERIOD** | Body-wide, not plate-specific | mouse, PMID 18448610 | none | **yes** |
| D2 | **An extensive genetic program occurs during postnatal growth in multiple tissues** — thousands of genes change in concert | **PERIOD** | Body-wide clock | mouse, PMID 19036884 | none | **yes** |
| D3 | **Coordinated postnatal down-regulation of multiple growth-promoting genes = a genetic program limiting organ growth** | **PERIOD** | The programme, named | mouse, PMID 20371622 | none | **yes** |
| D4 | **Many "aging" expression changes actually ORIGINATE during juvenile growth** — the aging signature and the growth-deceleration signature are partly the same thing | **PERIOD** | Reframes aging biomarkers | mouse, PMID 20816690 | — | **yes** |
| D5 | **E2F3 drives postnatal Igf2 down-regulation** — a transcription-factor handle on the programme | **PERIOD** | Named driver | mouse, PMID 23530192 | none | **yes** |
| D6 | **miR-29 up-regulation contributes to postnatal body-growth deceleration** | **PERIOD** | A miRNA arm of the clock | mouse, PMID 25866874 | anti-miR-29 | **yes** |
| D7 | **"Mechanisms limiting body growth in mammals"** — the synthesis of the above | **PERIOD** | (review) | review, PMID 21441345 | — | no |
| D8 | **Regulation of body growth by microRNAs** — the miRNA-level statement of the same programme | **PERIOD** | (review) | review, PMID 27789392 | — | **yes** |
| D9 | **Spatial and temporal regulation of gene expression in the mammalian growth plate** — the zone × age expression atlas that the senescence programme was read from | **PERIOD** | Descriptive | rat/mouse, PMID 20096814 | — | **yes** |
| D10 | **GWAS height loci + growth-plate expression jointly nominate genes acting IN the plate** | rate/period | Method | human, PMID 22914739 | — | **yes** |
| **E. HETEROCHRONIC RNA — lin-4 / let-7 / LIN28 / HMGA2 / IGF2BP** |
| E1 | **let-7 is THE heterochronic switch gene** — loss reiterates larval fates, gain causes precocious adult fates | **PERIOD** (developmental timing) | Canonical timer | *C. elegans*, PMID 10706289 | — | no |
| E2 | **let-7 sequence and temporal expression are conserved across bilateria** — the timer is ancient | **PERIOD** | Conservation | many species, PMID 11081512 | — | no |
| E3 | **LIN28A and LIN28B block let-7 biogenesis by DIFFERENT mechanisms** (cytoplasmic TUT4 vs nuclear Microprocessor sequestration) — they are not interchangeable | **PERIOD** | Two distinct handles | human cells, PMID 22118463 | LIN28 inhibitors exist (oncology) | **yes** |
| E4 | **LIN28B variation sets human pubertal timing** — rs314276, age at menarche, and also earlier breast development, voice breaking, pubic hair | **PERIOD** | Direct human timing gene | human, PMID 19448623 | none | no |
| E5 | **Distinct LIN28B variants influence height growth from birth to adulthood** — separable effects on pubertal vs prepubertal growth | **PERIOD** | Trajectory-level | human (Finnish cohorts), PMID 20398887 | none | no |
| E6 | **Lin28a transgenic mice reproduce BOTH the size and puberty phenotypes** — increased body size AND delayed puberty in one animal | **PERIOD + size** | **Gain of LIN28A = bigger and later** | mouse, PMID 20512147 | none obtainable | no |
| E7 | **let-7 and miR-140 coordinately regulate skeletal development; Lin28a overexpression in growth-plate chondrocytes blocks let-7 biogenesis** — the heterochronic axis operating INSIDE the plate | **PERIOD** | Direct plate evidence | mouse, PMID 23940373 | none | **yes** |
| E8 | **LIN28B variation also associates with 2D:4D digit ratio** — a second skeletal (metacarpal) readout of the same locus | rate | Skeletal patterning | human, PMID 20303062 | — | **yes** |
| E9 | **LIN28B rs314276 effect on BMI/weight/height varies across the life course** | **PERIOD** | Age-dependent effect | human, PMID 20962026 | — | **yes** |
| E10 | **Lin28/let-7 axis regulates glucose metabolism and insulin sensitivity** — the metabolic arm that confounds "is the size effect the GH/IGF axis?" | rate | Confound | mouse, PMID 21962509; PMID 22160727 | — | no |
| E11 | **HMGA2 common variant is one of the first-discovered adult and childhood height loci** | rate | Height gene | human, PMID 17767157 | none | no |
| E12 | **HMGA2 (Hmgi-c) disruption IS the mouse pygmy mutation** — the causal skeletal proof for the height locus | size | Loss → small | mouse, PMID 7651535 | none | no |
| E13 | **let-7 targets include IGF2BP1/HMGA2/MYC/KRAS** — the effector set through which the heterochronic timer touches growth | rate | Effector layer | human cells, PMID 17699775 (let-7 represses proliferation pathways) | — | no |
| E14 | **LIN28B is a potent oncogene in many tissues** — the hard ceiling on ever raising LIN28 therapeutically | — | **Cost** | human, PMID 21512136 and others | — | no |
| E15 | **IGF2BP2 / IGF2BP family as let-7 targets and human height/growth genes** | rate | Effector | human, PMID UNVERIFIED (specific IGF2BP2-height paper not retrieved) | — | **yes** |
| **F. OTHER GROWTH-PLATE microRNAs, lncRNAs, circRNAs** |
| F1 | **miR-140 is cartilage-specific, Sox9-driven, and required for chondrocyte proliferation** — knockdown arrests chondrogenic proliferation in limb-bud micromass | rate | Required | mouse, PMID 21872590 | — | no |
| F2 | **miR-1 is specifically expressed in growth-plate cartilage and represses HDAC4 in the hypertrophic zone** | rate | Zone-specific | mouse, PMID 24858276 | — | **yes** |
| F3 | **miR-140 regulates MMP13 and IGFBP-5 in chondrocytes** | rate | Matrix turnover | human, PMID 19948051 | — | no |
| F4 | **Estrogen down-regulates miR-140 (targeting MMP13) in chondrocytes** — a route by which the fusion hormone acts through the cartilage miRNA layer | rate/period | E2 → miRNA → matrix | human, PMID 27165343 | — | **yes** |
| F5 | **miR-221 controls CDKN1C/p57 and CDKN1B/p27** — a miRNA directly on the chondrocyte cell-cycle brakes | rate | Cell-cycle | human, PMID 18521080 | — | **yes** |
| F6 | **miR-433 / miR-26b / miR-145 / miR-483 / miR-675 in cartilage** — named in the brief; I found the general cartilage-miRNA review but not individual growth-plate length endpoints | rate | Unresolved | review, PMID 32745689 ("MicroRNAs in cartilage development and dysplasia"); individual PMIDs UNVERIFIED | — | **yes** |
| F7 | **circRNAs act as miRNA sponges in cartilage** (e.g. a circRNA sponging miR-136 to control MMP13) — the class exists in chondrocytes; no growth-plate length endpoint found | rate | Class exists | human cartilage, PMID 26931159 | — | **yes** |
| F8 | **H19 lncRNA controls the Imprinted Gene Network by recruiting MBD1** — links the lncRNA layer directly to the D1 growth-limiting network | **PERIOD** | Network hub | mouse, PMID 24297921 | — | **yes** |
| F9 | **lncRNA layer in growth-plate cartilage specifically** — searched; the cartilage lncRNA literature is overwhelmingly osteoarthritis/disc, not physis | — | Gap | — | — | **yes** |
| **G. RNA MODIFICATION** |
| G1 | **m6A writer METTL3 controls MSC fate and bone mass; conditional KO gives osteoporosis phenotype** — the closest verified skeletal m6A result | rate | Skeletal m6A is real | mouse, PMID 30429466 | STM2457 (METTL3 inhibitor) | no |
| G2 | **m6A/METTL3 in GROWTH-PLATE chondrocytes specifically** — repeated Europe PMC queries returned no growth-plate-specific m6A paper I could verify | — | Gap | PMID UNVERIFIED | — | **yes** |
| G3 | **m5C (NSUN2/ALYREF) and pseudouridine in cartilage or physis** — searched; no skeletal-timing paper retrieved | — | Gap | PMID UNVERIFIED | — | **yes** |
| G4 | **FTO (m6A eraser) is the canonical obesity locus and obesity advances bone age** — an indirect but real route from an RNA-modification gene to skeletal timing | **PERIOD** | Indirect | human, review PMID 35409166 | — | **yes** |
| **H. DNA METHYLATION, METHYL DONORS AND CLOCKS** |
| H1 | **Horvath multi-tissue DNA-methylation age** — the reference clock; establishes that a methylation-based age exists across human tissues | **PERIOD** (biomarker) | Measurement | human, PMID 24138928 | — | no |
| H2 | **Universal mammalian methylation clock across species** — a cross-species age predictor, i.e. the clock is a conserved property not a human artefact | **PERIOD** | Conserved | ~185 mammal species, PMID 37563227 | — | **yes** |
| H3 | **Skin & blood epigenetic clock** — a tissue-specific clock precedent for building a CARTILAGE clock | — | Method | human, PMID 30048243 | — | **yes** |
| H4 | **NSD1 loss accelerates the epigenetic aging clock** — screen of genes that move epigenetic age nominates the H3K36 methyltransferase mutated in Sotos overgrowth | **PERIOD** | Overgrowth gene = clock gene | human, PMID 31409373 | — | **yes** |
| H5 | **Growth-plate senescence is accompanied by global 5mC loss in the resting zone** (see A5) | **PERIOD** | The plate's own clock | rabbit, PMID 16002553 | methyl donors (untested) | **yes** |
| H6 | **DNMT3A loss-of-function = Tatton-Brown–Rahman overgrowth with tall stature** | size/period | Writer loss → overgrowth | human, PMID UNVERIFIED (not retrieved this session) | — | no |
| H7 | **DNMT3B mutation = ICF syndrome** — a human DNA-methyltransferase disease with growth phenotype | rate | Writer loss | human, PMID 10588719 | — | **yes** |
| H8 | **Folate/methyl-donor supply sets DNA methylation** — the substrate layer under H5 | **PERIOD** (hypothetical) | Substrate | human/rodent, review PMID 22332098 | folate, choline, betaine, B12 | no |
| H9 | **NNMT is a metabolic methylation SINK** — consumes SAM and can globally lower methylation; bisubstrate inhibitors exist | **PERIOD** (hypothetical) | Removing the sink raises SAM | human cells, PMID 23455543; inhibitors PMID 31265285 | NNMT bisubstrate inhibitors | **yes** |
| H10 | **Transposable elements are targets for early nutritional effects on epigenetic gene regulation** (agouti) — the proof that diet moves methylation and phenotype | — | Principle | mouse, PMID 12861015 | — | no |
| H11 | **UHRF1/UHRF2, TET1/2/3 in the growth plate specifically** — searched; no growth-plate-length endpoint retrieved for any of them | — | Gap | PMID UNVERIFIED | — | **yes** |
| H12 | **Lin28A binds active promoters and recruits TET1** — a direct physical bridge between the heterochronic RNA layer and the DNA-demethylation layer | **PERIOD** | Layer bridge | mouse ESC, PMID 26711009 | — | **yes** |
| **I. HISTONE MODIFICATION AND CHROMATIN** |
| I1 | **EZH1 and EZH2 PROMOTE skeletal growth by repressing inhibitors of chondrocyte proliferation and hypertrophy** — PRC2 loss in cartilage SHORTENS | rate | PRC2 is pro-growth in the plate | mouse, PMID 27897169 | EZH2 inhibitors would shorten | no |
| I2 | **Ezh2 controls skeletal development epigenetically** | rate | Same direction | mouse, PMID 26424790 | — | no |
| I3 | **EZH2 loss-of-function = Weaver overgrowth syndrome in humans** — the direction that looks opposite to I1/I2 and is the classic trap | size | Germline whole-organism ≠ cartilage-restricted | human, PMID 29244146 | — | no |
| I4 | **NSD1 haploinsufficiency = Sotos syndrome (overgrowth, advanced bone age)** | size + **PERIOD** | Overgrowth with bone-age advance | human, PMID 11896389; PMID 15942875 | — | no |
| I5 | **NSD1 mutations generate a genome-wide DNA methylation signature** — H3K36 writer loss reprograms 5mC; the two epigenetic layers are coupled | — | Coupling | human, PMID 26690673 | — | **yes** |
| I6 | **JMJD3/KDM6B promotes chondrocyte proliferation and hypertrophy during endochondral bone formation** | rate | H3K27 demethylase is pro-growth | mouse, PMID 25587042 | GSK-J4 would oppose | **yes** |
| I7 | **DOT1L safeguards cartilage homeostasis** and the DOT1L locus is a GWAS hit for cartilage thickness | rate | H3K79 | mouse + human, PMID 28627522, PMID 22566624 | pinometostat (would oppose) | **yes** |
| I8 | **HDAC4 haploinsufficiency = brachydactyly–mental retardation syndrome (2q37 deletion)** — a human skeletal-shortening phenotype from a class-IIa HDAC | rate | Human dosage | human, PMID 20691407 | HDAC inhibitors are two-edged | no |
| I9 | **HDAC4 represses MEF2C and thereby chondrocyte hypertrophy** — the canonical brake on the discharge step (miR-1 sits upstream, F2) | rate | Brake | mouse, PMID 24858276 (via miR-1) | — | no |
| I10 | **SIRT6 regulates postnatal growth-plate differentiation and proliferation via Ihh** | rate | Sirtuin in the plate | mouse, PMID 24149372 | — | **yes** |
| I11 | **Sirt6 deficiency promotes senescence and disc degeneration** — the axial-cartilage arm | — | Cost | mouse, PMID 40335469 | — | **yes** |
| I12 | **SIRT1 regulates cartilage-specific gene expression together with NAMPT** — the NAD+ arm touching cartilage | rate | NAD+ | human chondrocyte, PMID 18957417 | NAD+ precursors (untested for length) | **yes** |
| I13 | **CHD7 (chromatin remodeller) mutation causes CHARGE syndrome AND isolated hypogonadotropic hypogonadism / Kallmann** — a remodeller whose loss produces the *hypogonadism* that itself delays fusion | **PERIOD** | Remodeller → puberty | human, PMID 18834967; PMID 16155193 | — | **yes** |
| I14 | **SMARCA4/SMARCA2 (SWI/SNF) mutation = Coffin–Siris syndrome with growth phenotype** | rate | Remodeller | human, PMID 24700502 | — | **yes** |
| I15 | **BET/BRD4 in growth-plate chondrocytes** — searched; no physis-specific result retrieved | — | Gap | PMID UNVERIFIED | — | **yes** |
| I16 | **ISWI / INO80 in cartilage or physis** — searched; nothing skeletal-timing retrieved | — | Gap | PMID UNVERIFIED | — | **yes** |
| **J. 3D GENOME, ENHANCERS, IMPRINTING** |
| J1 | **CTCF at the H19 ICR sets higher-order chromatin conformation restricting enhancer access to Igf2** — the archetypal 3D-genome control of a growth gene | rate | Architecture → growth | mouse, PMID 16815976 | — | no |
| J2 | **Imprinted IGF2/H19 dosage sets body size** — parental imprinting of Igf2 | size | Dosage | mouse, PMID 1997210; PMID 7536897 | — | no |
| J3 | **CDKN1C/p57 is the major regulator of embryonic growth in its imprinted domain; human mutations cause Beckwith–Wiedemann overgrowth and IMAGe/Russell–Silver growth restriction** | size + rate | Bidirectional | mouse PMID 17517131; human PMID 26077438, PMID 22634751, PMID 24065356 | — | no |
| J4 | **MKRN3 (imprinted, paternally expressed) loss causes central precocious puberty** — the clearest single-gene imprinted determinant of PUBERTAL TIMING | **PERIOD** | Loss → early puberty → early fusion | human, PMID 23738509; PMID 31041429 | — | no |
| J5 | **MKRN3 acts by ubiquitinating MBD3 — an epigenetic switch for puberty** | **PERIOD** | Imprinting → chromatin → timing | mouse, PMID 34692086 | — | **yes** |
| J6 | **Circulating MKRN3 declines before pubertal onset** — a measurable timing biomarker | **PERIOD** | Biomarker | human girls, PMID 25695892 | — | **yes** |
| J7 | **DLK1 loss / Temple syndrome (upd(14)mat) → precocious puberty and short stature** | **PERIOD** | Imprinted locus sets timing | human, PMID 24891339; PMID 10356135 | — | **yes** |
| J8 | **Dlk1 (Pref-1) null mice: growth retardation and accelerated adiposity** | size | Imprinted growth gene | mouse, PMID 12101250 | — | **yes** |
| J9 | **The Dlk1–Dio3 locus carries a large imprinted miRNA cluster** — the imprinting layer and the miRNA layer are physically the same locus | **PERIOD** | Layer convergence | mouse, PMID 15310658; PMID 18471925 | — | **yes** |
| J10 | **ZFP57/KAP1 reads a methylated hexanucleotide to maintain ICRs** — the trans-acting machinery that could be perturbed | — | Machinery | mouse ESC, PMID 22055183 | — | **yes** |
| J11 | **Trim28 haploinsufficiency triggers a BI-STABLE epigenetic body-size phenotype** — genetically identical animals fall into two size classes | size | Epigenetic bistability of body size | mouse, PMID 26824653 | — | **yes** |
| J12 | **Limb/growth-plate-specific enhancers and TAD disruption cause limb malformation** — searched; the general principle is established but I retrieved no growth-plate-timing-specific enhancer paper | — | Gap | PMID UNVERIFIED | — | **yes** |
| **K. TELOMERES, SENESCENCE, SASP, REPROGRAMMING** |
| K1 | **The growth-plate limit is NOT a telomere/Hayflick limit** — RZ chondrocyte population doublings in culture were independent of donor age | **PERIOD** | **Telomerase is the wrong target** | rabbit, PMID 16002553 | — | **yes** |
| K2 | **Chondrocyte telomere loss during ex vivo expansion equals decades of in-vivo aging** — telomeres do shorten, just not as the in-vivo limiter | — | Culture artefact caution | human, PMID 14647922 | — | **yes** |
| K3 | **hTERT transduction fails to prevent chondrocyte senescence at 21% O2 but 5% O2 extends doublings to 60 PD** — OXYGEN, not telomerase, is the dominant variable in vitro | — | Stress-induced not replicative | human, PMID 15071075 | hypoxic culture | **yes** |
| K4 | **hTERT extends chondrocyte lifespan while preserving phenotype** (OA chondrocytes) | — | Partial | human, PMID 11920404 | — | **yes** |
| K5 | **p16INK4a is a biomarker of chondrocyte aging but does NOT cause osteoarthritis** — a direct negative on the p16-causal model in cartilage | — | Negative | mouse, PMID 29744983 | senolytics unlikely to help | no |
| K6 | **Targeted clearance of p21-positive (not p16-positive) senescent cells prevents radiation-induced bone loss** — if a senolytic arm exists in bone it is p21, not p16 | — | Which marker | mouse, PMID 35363946 | dasatinib+quercetin, navitoclax | **yes** |
| K7 | **Controlled induction and elimination of p16-expressing chondrocytes in cartilage explant** — the tool exists | — | Method | mouse explant, PMID 31408372 | — | **yes** |
| K8 | **Replicative vs chemically-induced senescence in articular chondrocytes are molecularly distinct** — do not equate them | — | Distinction | human/animal chondrocyte, PMID 41730836 | — | **yes** |
| K9 | **BMP–SMAD–ID promotes reprogramming by inhibiting p16-dependent senescence** — a route from a growth-plate morphogen family to the senescence brake | — | Bridge | mouse, PMID 27794120 | — | **yes** |
| K10 | **Partial/full reprogramming of a GROWTH PLATE** — searched; no report retrieved of OSK(M) applied to physeal chondrocytes with a length endpoint | — | Gap | PMID UNVERIFIED | — | **yes** |
| K11 | **Telomerase protects Werner-syndrome MESENCHYMAL lineage stem cells from premature aging** — lineage-specific; mesenchyme is the vulnerable lineage | — | Lineage specificity | human iPSC, PMID 24749076 | — | **yes** |
| **L. QUIESCENCE, DORMANCY, DIAPAUSE** |
| L1 | **Embryonic diapause is a reversible, MYC-suppressed dormant state** — the existence proof that a mammalian developmental clock can be paused and resumed | **PERIOD** | Pausable programme | mouse, PMID 26871632; PMID 33417832 | mTOR inhibition (in that context) | **yes** |
| L2 | **daf-2/daf-16 insulin signalling and daf-12 nuclear receptor gate dauer diapause and "developmental age"** | **PERIOD** | The canonical pause switch | *C. elegans*, PMID 9252323; PMID 10859169 | — | **yes** |
| L3 | **HSC hibernation is imposed by niche signals (TGF-β, non-myelinating Schwann cells)** — a mammalian precedent for niche-enforced deep quiescence in a stem pool | **PERIOD** | Niche sets depth of quiescence | mouse, PMID 22118468; PMID 18945958 | — | **yes** |
| L4 | **Hibernation is associated with slow life histories and increased survival** — organismal precedent for slowing a developmental clock | **PERIOD** | Whole-animal | mammals, PMID 21450735 | — | **yes** |
| L5 | **RZ chondrocytes are slow-cycling label-retaining cells maintained in low Wnt** (see B4) — the physis's own version of L3 | **PERIOD** | Same principle | mouse, PMID 34309509 | — | **yes** |
| **M. CELL-CYCLE MACHINERY IN CHONDROCYTES** |
| M1 | **p21 (CDKN1A) mosaic induction in chondrocytes is the tool that proved local + systemic catch-up** | rate | Direct arrest | mouse, PMID 29944650 | — | **yes** |
| M2 | **Raf/MEK/ERK regulates p21 expression in chondrocytes** — links the FGFR3 arm to the cell-cycle brake | rate | Pathway → brake | chondrocyte, PMID 10514521 | FGFR/MEK inhibitors | **yes** |
| M3 | **p27Kip1-deficient mice show gigantism with multiorgan hyperplasia** — losing a CDK inhibitor increases body size | size | Brake removal → bigger | mouse, PMID 8646781 | — | no |
| M4 | **c-Myc regulates mammalian body size by controlling cell NUMBER, not cell size** | size | Number not size | mouse, PMID 11742404 | — | no |
| M5 | **Reduced MYC expression increases longevity and healthspan** — the lifespan/size trade-off in one allele | size vs lifespan | Trade-off | mouse, PMID 25619689 | — | **yes** |
| M6 | **RB family ablation deregulates G1 and causes immortalisation** — the archetype for period extension by removing the G1 gate (and for the cancer cost) | — | Cost | mouse cells, PMID 11114893 | — | no |
| M7 | **Rb is required for appropriate osteoblast differentiation and bone development** | rate | Skeletal Rb | mouse, PMID 18819932 | — | **yes** |
| M8 | **HIF-1α is essential for chondrocyte GROWTH ARREST and survival in the hypoxic plate interior** — arrest is actively imposed, not passive | rate | Active arrest | mouse, PMID 11691837 | — | no |
| M9 | **mTOR inhibition (rapamycin) markedly alters the growth plate and retards growth in young rats** — a real, measured PERIOD/rate cost of an mTOR agent in a growing animal | rate (pool cost) | Slows growth | rat, PMID 17370095; PMID 19144108 | rapalogs = contraindicated | no |
| **N. GROWTH TRAJECTORY MODELS AND PHASES** |
| N1 | **Tanner height-velocity standards from birth to maturity** — the reference frame for every velocity statement | — | Reference | human, PMID 5957718 | — | no |
| N2 | **Infancy–Childhood–Puberty (ICP) model (Karlberg)** — three additive, partly independent components with different endocrine drivers | **PERIOD** structure | Framework | human, PMID UNVERIFIED (original Karlberg papers not retrieved) | — | no |
| N3 | **Mid-childhood/juvenile growth spurt** — searched; I could not retrieve a definitive primary. Adrenarche is its usual proposed driver | rate | Weak/contested | PMID UNVERIFIED | — | **yes** |
| N4 | **Adrenarche = rise in adrenal androgen biosynthesis (DHEA/DHEAS), dissociable from gonadarche** | rate + bone age | Independent axis | human, PMID 15635501; PMID 6447708 | — | no |
| N5 | **11-ketotestosterone is the dominant circulating bioactive androgen at adrenarche** — the potent androgen most clinicians never measure | rate/bone age | Re-identifies the ligand | human, PMID 30137510 | — | **yes** |
| N6 | **Peak height velocity timing predicted from the ELBOW (Sauvegrain)** — elbow maturity tracks PHV better than hand during the spurt | **PERIOD** measurement | Timing | human, PMID 19034174 | — | **yes** |
| N7 | **The adolescent spurt follows a UNIFORM pattern of growth and skeletal maturation** — Sanders; the basis for using hand stages to place a child on the growth curve | **PERIOD** measurement | Framework | human, PMID 29196711 | — | **yes** |
| N8 | **Pubertal "tempo" (rate of maturation) is separable from pubertal "timing"** — and has independent consequences | **PERIOD** | Two parameters | human, PMID 20822243 | — | **yes** |
| N9 | **Catch-up growth in infancy predicts earlier menarche and earlier pubertal spurt in SGA girls** — early nutrition sets later timing | **PERIOD** | Programming | human, PMID 36554686 | — | **yes** |
| N10 | **Age at menarche: 30 loci → 389 loci** — puberty timing is highly polygenic; the 2017 study links puberty timing to cancer risk | **PERIOD** | Polygenic architecture | human, PMID 21102462; PMID 28436984 | — | no |
| N11 | **Male puberty timing GWAS (voice breaking) shares genetic basis with hair colour and lifespan** | **PERIOD** | Male-specific data | human, PMID 32210231 | — | **yes** |
| N12 | **Seasonality of growth** — documented for weight/height gain in children under three in rural Malawi; food-security driven rather than photoperiod | rate | Real but nutritional | human, PMID 12801119 | — | **yes** |
| N13 | **Circannual/circadian contributions to childhood growth and adiposity** | rate | Weak | human, PMID 30845969 | — | **yes** |
| N14 | **Chondrocytes contain an autonomous circadian clock regulating cartilage-homeostasis genes** | rate | Local clock exists | mouse, PMID 23896777 | — | **yes** |
| N15 | **Circadian control of the collagen secretory pathway** — the matrix output itself is time-of-day gated | rate | Output timing | mouse, PMID 31907414 | — | **yes** |
| N16 | **Bmal1 deficiency gives low bone mass** — the clock gene has a skeletal phenotype | rate | Clock → bone | mouse, PMID 26789548 | — | **yes** |
| **O. BONE AGE / SKELETAL MATURITY ASSESSMENT** |
| O1 | **Greulich–Pyle atlas** — the default method; population- and era-dependent, with documented mismatch in non-US populations | measurement | Reference | human, e.g. PMID 11737745, PMID 17391883 | — | no |
| O2 | **Tanner–Whitehouse 2 / 3 (RUS)** — scoring rather than atlas matching; TW2→TW3 rescaling changes maturity classification materially | measurement | Reference | human, PMID 29082464; US90 reference PMID 9255189 | — | no |
| O3 | **Fels method** — named in the brief; I retrieved no usable primary this session | measurement | — | PMID UNVERIFIED | — | **yes** |
| O4 | **BoneXpert automated bone age** — reconstructs 15 bones, computes 13 intrinsic bone ages, converts to GP or TW; auto-rejects abnormal images | measurement | Removes rater variance | human, PMID 19116188; validated in short stature PMID 19333590 | — | no |
| O5 | **BoneXpert Bone Health Index (BHI)** — metacarpal cortical thickness from the SAME hand film, correlates with cortical BMD | measurement (cortical bone) | Free extra channel | human, PMID 27014874 | — | **yes** |
| O6 | **Deep-learning bone age from hand radiographs** — performance comparable to expert readers | measurement | Automation | human, PMID 29095675; PMID 31993795 | — | no |
| O7 | **Sauvegrain elbow method** — the only maturity index with resolution *during* the two years of the pubertal spurt, when the hand is least informative | measurement | Fills the spurt window | human, PMID 16085606; PMID 33569105 | — | **yes** |
| O8 | **Olecranon apophysis staging** for scoliosis at Risser 0 — a second elbow-based index for the spurt | measurement | Same window | human, PMID 18056507; PMID 33974573 | — | **yes** |
| O9 | **Risser sign (iliac apophysis)** — widely used and repeatedly shown to be *less* accurate than chronological age as a predictor of skeletal age | measurement | **Poor** | human, PMID 7962495; PMID 19002685 | — | no |
| O10 | **US vs French Risser grading systems differ materially despite the same name** | measurement | Trap | human, PMID 15995440 | — | **yes** |
| O11 | **Sanders hand staging** — validated for curve progression, and mismatches Risser in a high proportion of patients | measurement | Better than Risser | human, PMID 26356067; PMID 31923164 | — | no |
| O12 | **Sanders 7b (ulnar physis appearance)** — refines brace-weaning decisions | measurement | Fine grain at the end | human, PMID 33380190 | — | **yes** |
| O13 | **Thumb Ossification Composite Index (TOCI)** — validated stage-to-stage against TW and Sanders | measurement | Alternative | human, PMID 29975274 | — | **yes** |
| O14 | **Distal radius and ulna (DRU) classification** — combined with Sanders reduces growth-assessment mismatch | measurement | Complement | human, PMID 34036944 | — | **yes** |
| O15 | **Calcaneal apophyseal ossification vs PHV** | measurement | Alternative site | human, PMID 26637689 | — | **yes** |
| O16 | **Triradiate cartilage closure** — a mid-spurt landmark used with Risser 0 | measurement | Landmark | human, PMID 7822354, PMID 18056507 | — | no |
| O17 | **Ultrasonographic version of the GP atlas** — no radiation; unreliable at the extremes of delayed/advanced bone age | measurement | Radiation-free but limited | human, PMID 12862266; review PMID 26568655 | — | **yes** |
| O18 | **MRI-based skeletal maturity and the FOPE zone** — focal periphyseal edema on adolescent knee MRI as an imaging signature of *physiological physeal fusion in progress* | **PERIOD** measurement | Sees fusion happening | human, PMID 21940591 | — | **yes** |
| O19 | **EOS / biplanar low-dose stereoradiography** — hand repositioning during spinal EOS allows concurrent Sanders staging at no extra dose | measurement | Efficiency | human, PMID 29886909 | — | **yes** |
| O20 | **Thiemann–Nitz atlas** — a European alternative to GP with comparable forensic accuracy | measurement | Alternative | human, PMID 17401574 | — | **yes** |
| O21 | **Intra/inter-observer error of GP is large enough to matter forensically** | measurement | Error floor | human, PMID 18602233; training effect PMID 4313463 | — | no |
| **P. ADULT HEIGHT PREDICTION** |
| P1 | **Bayley–Pinneau tables** — predict adult height from GP skeletal age; the original tables | prediction | Standard | human, PMID 14918032 | — | no |
| P2 | **Tanner–Whitehouse (TW Mark 2/3) prediction equations** | prediction | Standard | human, PMID UNVERIFIED (original TW prediction paper not retrieved) | — | no |
| P3 | **Roche–Wainer–Thissen (RWT)** — uses weight and midparental height as well as skeletal age | prediction | Standard | human, PMID UNVERIFIED | — | no |
| P4 | **Khamis–Roche** — predicts adult height WITHOUT a radiograph | prediction | No radiation | human, PMID UNVERIFIED (retrieved only as a comparator name) | — | **yes** |
| P5 | **Paley multiplier method** — a single age/sex multiplier predicts limb length and adult height; validated against Sanders and White–Menelaus | prediction | Simplest | human, PMID 11057472; PMID 15502579; comparison PMID 34166322 | — | **yes** |
| P6 | **Prediction error is the load-bearing weakness** — bone-age method spread alone shifts predicted adult height; Risser adds nothing over chronological age | prediction | **Error dominates** | human, PMID 7962495 and the O-series above | — | no |
| **Q. DELAYED OR ABSENT EPIPHYSEAL FUSION — CAUSES** (expanded in prose below) |
| Q1 | **ESR1 (estrogen receptor α) disruptive mutation in a man** — 204 cm, INCOMPLETE EPIPHYSEAL CLOSURE, history of continued linear growth into adulthood | **PERIOD** | **Absent fusion** | human, PMID 8090165 | — | no |
| Q2 | **CYP19A1 aromatase deficiency in men** — all reported men: tall stature, delayed bone maturation, **unfused epiphyses**, eunuchoid proportions, osteopenia | **PERIOD** | **Absent fusion** | human, PMID 8530621; PMID 19707181; PMID 16480891 | estrogen replacement closes them | no |
| Q3 | **Estrogen replacement in aromatase-deficient men closes the epiphyses and stops growth** — the causal reversal | **PERIOD** | Confirms causality | human, PMID 9211678; PMID 12466340; PMID 10843162; PMID 18590994 | estradiol | no |
| Q4 | **ERα knockout (and αβ double KO) mice have decreased longitudinal growth — ERβ KO does not** — ERα is the operative receptor for skeletal growth/maturation in males | **PERIOD** | Receptor identity | mouse, PMID 10805804 | — | no |
| Q5 | **Aromatase-knockout (ArKO) mouse bone has a sexually dimorphic response** — decreased femur growth in ArKO males | **PERIOD** | Species caveat: mice don't fuse | mouse, PMID 10750565 | — | **yes** |
| Q6 | **Untreated hypogonadism / eunuchoidism** — the classical clinical cause of continued growth and eunuchoid proportions | **PERIOD** | Delayed fusion | human, reviews PMID 31147553 | testosterone (aromatisable) closes | no |
| Q7 | **Klinefelter 47,XXY — tall stature** (SHOX dosage plus hypogonadism) | **PERIOD** + size | Two mechanisms | human, PMID 27644703; growth/IGF data PMID 17940117 | — | no |
| Q8 | **47,XYY — tall stature** — extra Y, extra SHOX copy, NOT hypogonadal | size | Gene dosage not hormone | human, PMID 23810129; PMID 17940117 | — | no |
| Q9 | **SHOX dosage sets long-bone growth** — haploinsufficiency (Léri–Weill, Turner) shortens; extra copies lengthen | size | Dosage | human, PMID 10749976; PMID 9590292; PMID 21325865 | GH partially | no |
| Q10 | **Pituitary gigantism / X-LAG (GPR101 Xq26 microduplication)** — GH excess BEFORE epiphyseal fusion gives extreme height; fusion itself is often also delayed by associated hypogonadism | rate (+period) | Extreme phenotype | human, PMID 25470569; PMID 26187128 | — | no |
| Q11 | **Persistent physis in adults is a real, documented anatomical entity** — case reports of fracture through a persistent OLECRANON physis in adults, persistent distal fibular physis, bilateral proximal tibial stress fractures through persistent physes | **PERIOD** | Fusion can simply fail locally | human, PMID 8423189; PMID 12665964; PMID 30631624; PMID 30101168 | — | **yes** |
| Q12 | **Symptomatic persistent olecranon physis in adolescent baseball players with cartilage degeneration** — repetitive loading appears to prevent local fusion | **PERIOD** | Mechanical cause | human, PMID 25580304; PMID 28139383 | — | **yes** |
| Q13 | **Delayed puberty / constitutional delay** — delays bone age and prolongs the growth period (usually without net adult-height gain) | **PERIOD** | Delayed fusion | human, review PMID 31220230 | — | no |
| Q14 | **MC4R deficiency** — increased linear growth and increased final height with incompletely suppressed GH secretion | rate + period | Obesity gene that raises height | human, PMID 21047921 | — | **yes** |
| Q15 | **Rodents as a whole: growth plates persist for life** — the species-level "absent fusion" | **PERIOD** | Baseline | mouse/rat, review PMID 21540578 | — | no |
| **R. TEMPO, SPECIES CLOCKS, AND EXTREME GROWTH** |
| R1 | **Species-specific developmental tempo tracks PROTEIN STABILITY and degradation rates**, not signalling logic — human motor-neuron programme runs >2× slower than mouse | **PERIOD** | Biochemical rate sets tempo | human vs mouse ESC, PMID 32943498 | — | **yes** |
| R2 | **"Stem cell zoo": segmentation-clock period scales with EMBRYOGENESIS TIME, not body weight**, across marmoset, rabbit, cattle, rhinoceros, mouse, human | **PERIOD** | Intracellular scaling | 6 mammals, PMID 37343565 | — | **yes** |
| R3 | **Deer antler: the fastest organ growth in the animal kingdom (>2 cm/day) by modified endochondral ossification, regenerated annually from stem cells** | rate + **PERIOD** | Existence proof of repeatable endochondral growth in an adult mammal | red deer, PMID 15293809; PMID 31165741; PMID 22457177 | — | **yes** |
| R4 | **Genetic basis of ruminant headgear and rapid antler regeneration** | rate | Genomic basis | deer/ruminants, PMID 31221830 | — | **yes** |
| R5 | **Indeterminate growth in fish/reptiles** — a whole-clade absence of the fusion endpoint | **PERIOD** | Clade-level | teleosts, PMID 21525308 (myotomal muscle) and general | — | **yes** |
| R6 | **Four loci explain 83% of horse size variation** (incl. LCORL/NCAPG, HMGA2) — extreme within-species size range under few loci | size | Architecture | horse, PMID 22808074 | — | **yes** |
| R7 | **African pygmy phenotype arose convergently and is under positive selection; associated with GH/IGF-1 axis alteration** — a natural human experiment in early growth cessation | **PERIOD** | Human variation | human, PMID 25136101; PMID 19246118; IGF-1 PMID 7024810 | — | **yes** |
| R8 | **Transgenic mud loach with extraordinary gigantism** — the ceiling when a growth axis is unconstrained in an indeterminate grower | size | Comparative | fish, PMID 11592714 | — | **yes** |
| R9 | **Sauropod gigantism: evolution of extreme body size** — the biomechanical/physiological envelope | size | Comparative | dinosaurs, PMID 21251189 | — | **yes** |
| **S. FUSION MECHANISM AND WHETHER IT CAN BE UNDONE** |
| S1 | **Mechanisms of growth-plate maturation and epiphyseal fusion** — the mechanistic review, explicitly noting the rabbit-vs-rodent species problem | **PERIOD** | (review) | review, PMID 21540578 | — | no |
| S2 | **Micro-CT method for understanding epiphyseal growth-plate fusion** — fusion imaged in 3D as bony bridging | **PERIOD** | Method | PMID 29417047 | — | **yes** |
| S3 | **Growth-plate closure and therapeutic interventions** — recent review of what could in principle delay closure | **PERIOD** | (review) | review, PMID 39463341 | — | no |
| S4 | **Physeal bar resection can restore growth if <50% of the plate and enough growth remains; secondary tethers are a common failure mode** | **PERIOD** | *Partial* restoration | human, PMID 12461380; PMID 29628701 | interposition graft | no |
| S5 | **Physeal allograft transfer for physeal bars — safety and feasibility in swine** | **PERIOD** | New attempt | swine, PMID 41485130 | — | **yes** |
| S6 | **MSC-based and scaffold-based growth-plate regeneration** — repeatedly attempted in ovine, rabbit and rat injury models; none restores a normal functioning physis | **PERIOD** | **Fails so far** | ovine PMID 20721323; rabbit PMID 32283887; rat PMID 28715376; review PMID 28830302 | — | no |
| S7 | **Chondrodiatasis — mechanical distraction THROUGH the physis** — the one clinical technique that exploits the plate itself for lengthening; risks premature fusion | **PERIOD** | Mechanical | human + rabbit, PMID 3733829; PMID 3733828 | Ilizarov | **yes** |
| S8 | **Reopening a FUSED physis: no report found in any species** — targeted queries returned only physeal-bar resection (a *partially* fused plate) and tissue-engineering attempts | **PERIOD** | **Absent** | PMID UNVERIFIED — searched, nothing found | — | no |
| S9 | **Distraction osteogenesis is the workaround** — lengthening without any growth plate, and it works after fusion | **PERIOD**-independent | Bypass | human, e.g. PMID 22112021 | — | no |
| **T. PHARMACOLOGICAL PERIOD EXTENSION IN HUMANS (the direct evidence)** |
| T1 | **Letrozole raises PREDICTED adult height in boys with idiopathic short stature — randomised controlled trial** | **PERIOD** | Extends | human boys, PMID 16189252 | letrozole | no |
| T2 | **Letrozole + testosterone in boys with constitutionally delayed puberty raises predicted adult height — RCT** | **PERIOD** | Extends | human boys, PMID 11403810 | letrozole | no |
| T3 | **Tamoxifen in McCune–Albright precocious puberty slows bone-age advancement — multicentre trial** | **PERIOD** | Slows the clock | human girls, PMID 12915825 | tamoxifen | no |
| T4 | **Letrozole long-term outcomes in McCune–Albright girls** | **PERIOD** | Slows | human, PMID 27562402 | letrozole | **yes** |
| T5 | **GnRH agonist for central precocious puberty preserves adult height only if started early** — the value is entirely about how much senescence has already been spent (see A10) | **PERIOD** | Conditional | human, PMID 14715835 | GnRHa | no |
| T6 | **"Can we increase pubertal growth?" — the explicit review of the levers** | **PERIOD** | (review) | review, PMID 25538878 | — | **yes** |
| T7 | **Aromatase inhibitors in men: effects and options** — dosing/effects reference for the adult male | **PERIOD** | (review) | review, PMID 21693046 | anastrozole/letrozole | no |
| **U. MEASUREMENT AND PREDICTION — ADDITIONS** |
| U1 | **FELS method of hand-wrist skeletal maturity** — the third classical system, with an explicit statistical update | measurement | Alternative | human, PMID 28514006; update PMID 23992229 | — | **yes** |
| U2 | **Modified Fels KNEE skeletal maturity system** — a knee-based maturity index, used for limb-length prediction | measurement | Knee, not hand | human, PMID 35667054; PMID 37972990 | — | **yes** |
| U3 | **Optimized Oxford hip skeletal maturity system** — pelvis-based, resilient to rotational variation | measurement | Hip | human, PMID 35089879; PMID 36537250 | — | **yes** |
| U4 | **Khamis–Roche method predicts adult stature WITHOUT skeletal age** (uses child height, weight, midparental height) | prediction | Zero radiation | human, PMID 7936860 | — | **yes** |
| U5 | **Estimating age at PHV: methods disagree** — formal comparison of modelling approaches | prediction | Method-dependence | human, PMID 29113497 | — | **yes** |
| U6 | **EOS scanner alternative maturity methods, 934 patients** | measurement | Low-dose | human, PMID 35522608 | — | **yes** |
| U7 | **Ultrasound (BAUSport) vs BoneXpert vs Fels in young athletes** — validity of radiation-free automatic skeletal age | measurement | Radiation-free | human, PMID 38188108 | — | **yes** |
| U8 | **Polygenic risk score predicting future adult SHORT stature in children** — genomic prediction as a complement to bone age | prediction | Genomic | human, PMID 33788949 | — | **yes** |
| U9 | **Tooth microstructure (enamel cross-striations, perikymata) records the pace of life history** — an independent, non-skeletal developmental clock readable in one individual | **PERIOD** measurement | Second clock | hominins/human, PMID 17015331; PMID 20855313 | — | **yes** |
| **V. EPIGENETIC WRITERS WITH BIDIRECTIONAL HUMAN GROWTH PHENOTYPES** |
| V1 | **DNMT3A loss of function = Tatton-Brown–Rahman overgrowth syndrome with TALL stature** | size + **PERIOD** | Loss → overgrowth | human, PMID 24614070; series PMID 29900417 | — | no |
| V2 | **DNMT3A GAIN of function = microcephalic DWARFISM with hypermethylation of Polycomb-regulated regions** — the same gene, opposite dose, opposite size | size | **Bidirectional; a band** | human, PMID 30478443 | — | **yes** |
| V3 | **H3K36me2 recruits DNMT3A and shapes intergenic methylation** — the mechanistic link explaining why NSD1 (Sotos) loss produces a DNA-methylation signature and an accelerated methylation clock | — | Layer coupling | human/mouse, PMID 31485078 (with PMID 26690673, PMID 31409373) | — | **yes** |
| V4 | **DNMT3B mutation = ICF syndrome** | rate | Writer loss | human, PMID 10588719 | — | **yes** |
| **W. THE ONE NAMED SMALL MOLECULE THAT DELAYS SENESCENCE** |
| W1 | ⭐ **KY19382 — an indirubin derivative that antagonises the CXXC5–Dishevelled interaction — ELONGATED TIBIAL LENGTH THROUGH DELAYED GROWTH-PLATE SENESCENCE AND FURTHER ACTIVATION OF THE GROWTH PLATE IN *ADOLESCENT* MICE** | **PERIOD** | **Extends** | mouse, PMID 30971423 | **KY19382 (indirubin analogue)** | **yes** |
| W2 | **KY19382 has since been developed as a topical/transdermal Wnt activator for hair regrowth and wound healing** — i.e. real formulation and delivery work exists on this molecule, in another indication | — | Obtainability | mouse/human skin, PMID 33751552; PMID 32093032 (transdermal micellar formulation); PMID 37511501 | KY19382 | **yes** |
| W3 | ⚠ **But the direction is Wnt-RAISING** — CXXC5 is a negative Wnt regulator, so blocking it raises canonical Wnt in the plate; a stimulatory Wnt agent must be reconciled against any model in which lower canonical Wnt preserves the resting-zone pool (cf. B4) | — | **Unresolved conflict** | mouse, PMID 30971423 vs PMID 34309509 | — | **yes** |

---
