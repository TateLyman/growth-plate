# DOMAIN 13 — THE AXIAL SKELETON AND TRUNK
## R436 full-concept-space enumeration

**Method.** Every row below was reached by **external search only** — Europe PMC REST API,
NCBI eutils efetch, and targeted web lookups. Nothing was derived from the atlas repository.
Species is stated on every claim. Where I could not verify a figure I have written `UNVERIFIED`
rather than guess. Reviews are marked **INDEX**, not source.

**Why this domain matters here.** The subject's residual growth is trunk-dominant, and essentially
the entire growth-pharmacology literature uses **femur, tibia, or naso-anal/body length** as its
endpoint. The two things this enumeration is built to deliver are (a) every agent in any species
with a **measured vertebral or trunk length endpoint**, and (b) what is **mechanistically
different** about a vertebral growth plate from a limb one — because a limb result is not
transferable by default.

**Headline.** **174 rows, 122 marked OBSCURE.** Three findings dominate:
1. **Leptin regulates the vertebral and tibial growth plates in OPPOSITE directions**, and
   leptin-deficient mice have **shorter tibiae and LONGER vertebrae** (PMID 28569158).
2. **Npr3-null mice show disproportionate elongation of the proximal and mid-tail VERTEBRAE**
   as well as the proximal limb — the only genetic perturbation I found with an explicit
   vertebral *elongation* phenotype in a normal animal (PMID 41073372).
3. **Sitting-height-to-standing-height ratio FALLS from prepuberty into early puberty and RISES
   again in LATE puberty** in 9,569 US children — the population-scale confirmation that the
   residual at the end of growth is trunk-weighted (PMID 32579888).

---

## TABLE

Columns: **# | AXIAL STRUCTURE/MECHANISM | CONTRIBUTION TO HEIGHT | CLOSURE TIMING | AGENT WITH AN AXIAL ENDPOINT? | EVIDENCE (PMID) | OBSCURE?**

### A. THE VERTEBRAL BODY AND ITS GROWTH CENTRES

| # | Structure / mechanism | Contribution to height | Closure timing | Agent with an axial endpoint? | Evidence (PMID) | Obscure? |
|---|---|---|---|---|---|---|
| A1 | **Vertebral endplate physis (superior + inferior), one pair per vertebral body** — a 24-vertebra presacral column carries ~48 physes vs 4 at the knee | Whole of vertebral-body height. **T1–S1 ≈ 49% of sitting height at maturity; ~18 cm at birth → ~45 cm at maturity** (Dimeglio data, secondary source) | Fuse with the ring apophysis; see A2 | Yes — see section G | 24147251 (INDEX, Canavese & Dimeglio); 39585607 | no |
| A2 | **Ring apophysis (annular epiphysis)** — a *ring*-shaped traction epiphysis at the vertebral rim into which the disc inserts; NOT a load-bearing epiphysis | Indirect: marks and mechanically completes maturation of the vertebra–disc junction | High-resolution CT, T1→sacrum: **ring apophysis maturation correlates with age R=0.892, p<0.001; HIGH-THORACIC and LOW-LUMBAR fuse EARLIEST, MID-THORACIC LATEST**; around peak growth spurt girls' mid-thoracic levels are less mature than boys' | No agent | 34362001 | **YES** |
| A3 | **Neurocentral synchondrosis (NCS)** — bipolar cartilage between centrum and neural arch; feeds vertebral body, canal AND posterior elements | Contributes to vertebral body dimensions and canal diameter | Cadaveric study across C/T/L, ages 1–18 y: closure is region-dependent; earlier literature range quoted **2–16 y**. C2–C7 morphology mapped on CT ages 1–6 y; MRI morphometry in the skeletally immature spine | No agent | 27137907; 39160634; 20042959 | **YES** |
| A4 | **Primary ossification centres — one centrum + paired neural centres per vertebra** | Sets initial vertebral body height | Prenatal appearance; L5 centre characterised in 3D in human fetuses | No | 41300235 | **YES** |
| A5 | **PIEZO1–GPX4–ferroptosis axis in the VERTEBRAL growth plate** | Compressive stress → PIEZO1 up → GPX4 down → ferroptosis of vertebral growth-plate chondrocytes → pathological ossification | n/a | **YES — PIEZO1 pharmacological inhibitor + Col2a1-CreERT;Piezo1^fl/fl mouse; decelerated scoliosis. Systemic inhibition caused OSTEOPOROSIS, so the authors built micro-endoscopy-guided HYDROGEL delivery of the inhibitor into vertebral growth-plate cartilage** | 40714837 | **YES** |
| A6 | **PIEZO1–primary cilium axis, compressive stress, AIS growth plate** | Growth-plate degeneration and premature ossification | n/a | Mechanistic | 41194970 | **YES** |
| A7 | **Vertebral growth plate REACTIVATION on unloading** | Rat caudal model: after 3 weeks of correction, **hypertrophic-layer height and chondrocyte height on the concave side DOUBLED**, and chondrocyte height/cartilage thickness returned to control values | n/a | **YES — mechanical (asymmetric compression then release), rat, vertebral growth-plate histology** | 36232897 | **YES** |
| A8 | **Vertebral proportion is set by CELL NUMBER, not (usually) by hypertrophy** | Jerboa vs mouse tail: **cell number is the common driver of both limb and vertebral proportion**; chondrocyte HYPERTROPHY — the major driver of proportion in all mammalian LIMBS — is used for vertebral proportion only in the extreme jerboa mid-tail | n/a | **YES — Npr3-null mouse (see G3)** | 41073372 | **YES** |
| A9 | **Vertebral and limb genetic programmes overlap only partially** | Genes associated with differential growth in the vertebral skeleton overlap *significantly but not substantially* with genes associated with limb proportion | n/a | n/a | 41073372 | **YES** |
| A10 | **Skeletal-element-specific vs global height variants** — epigenomic/transcriptomic maps of chondrocytes sampled from growth plates at **different sites across developing human skeletons** | Height GWAS signal partitions into element-specific and global-acting regulatory variants; regulatory pleiotropy dominates | n/a | No agent | 39549696 | no |
| A11 | **Site-specific skeletal stem cell diversity in humans** | Human skeletal development and regeneration are shaped by **functional diversity of stem cells ACROSS SKELETAL SITES** — the cellular basis for axial ≠ appendicular | n/a | No | 40118065 | **YES** |
| A12 | **Vertebral body intraosseous arterial microvasculature** | Governs endplate nutrition and the ossification front | n/a | No | 42158060 | **YES** |
| A13 | **Limbus vertebra** — disc material herniating through the un-fused ring apophysis | Focal loss of vertebral height | Only possible while the apophysis is unfused | No | 38746486 | **YES** |
| A14 | **Vertebral wedging** | Reduces measured sitting height without reducing residual growth capacity | n/a | Growth-modulation devices reduce wedging (F13) | 37773144 | no |
| A15 | **Heat stress → impaired vertebral chondrocyte proliferation; RFLNA/cytoskeleton mitigates (pig)** | Environmental input specific to vertebral development | n/a | Gene-level, pig | 41981703 | **YES** |
| A16 | **Vertebral body surface roughness as an age marker** | Not a height mechanism — a maturity readout | n/a | No | 40722542 | **YES** |
| A17 | **Hnrnpk → HIF1α–glycolysis axis maintains growth-plate chondrocyte survival** | Growth-plate metabolism; the vertebral plate is the more hypoxic of the two | n/a | Gene-level | 36127325 | **YES** |
| A18 | **gp130/STAT3 required for homeostatic proliferation and anabolism in postnatal growth plate chondrocytes** | Growth-plate maintenance | n/a | Gene-level; IL-6 family is drugged (tocilizumab) but no axial endpoint | 35039652 | **YES** |

### B. THE INTERVERTEBRAL DISC AS A HEIGHT COMPONENT

| # | Structure / mechanism | Contribution to height | Closure timing | Agent with an axial endpoint? | Evidence (PMID) | Obscure? |
|---|---|---|---|---|---|---|
| B1 | **Total intervertebral disc height (23 discs)** — a NON-fusing, osmotically-set height component | A substantial fraction of spinal column height (a commonly quoted ~20–25% could NOT be verified from a primary source in this search) | Never "fuses"; but discal height growth is distinct from vertebral height growth | See B7, B10 | 41900984 (INDEX) | no |
| B2 | **Nucleus pulposus FIXED CHARGE DENSITY** — proteoglycan-bound negative charge draws water osmotically and sets disc height against load | Directly sets disc height, diurnal recovery and creep | n/a | **Baseline FCD characterised in HUMAN cervical discs** | 39892283 | **YES** |
| B3 | **Notochordal cells in the nucleus pulposus** — humans lose them early; pig and non-chondrodystrophic dog retain them | Notochordal cells maintain NP matrix and therefore disc height | Human loss in childhood/adolescence (exact age contested) | Postnatal notochord-derived NP subpopulations described; degenerate NP cells reprogrammed to notochordal-like cells by defined factors (no height endpoint) | 38085183; 38879755; 39051200 (INDEX) | **YES** |
| B4 | **Cartilage endplate (CEP)** — hyaline layer between vertebral physis and disc; the disc's only nutrient route | Its progressive ossification ends disc nutrition and locks disc height | Progressive with age | **Fibroblast activation protein-α inhibition reduced vascular invasion of the cartilage endplate (rodent)** | 41531174; 40725395 | **YES** |
| B5 | **Diurnal disc height loss ("spinal shrinkage")** | **Measured on CBCT in 32 children aged 2.7–16.1 y: median T11→L4 spine-length reduction −1.0 mm over a day (range −3.9 to +0.1), p<0.001** — and NOT correlated with the 4.0–9.5 h interval between scans (ρ=−0.01, p=0.95) | n/a | Not an agent — a **measurement-protocol requirement** | 39568059 | **YES** |
| B6 | **Sustained axial unloading raises disc height** | 5 days of **dry immersion** changed human lumbar disc proteoglycan and water content; lumbar disc height increased after long-duration ISS missions | Fully reversible on reloading | Not an agent; and prolonged unloading destabilises the lumbar spine and raises herniation risk | 32466473; 27779600; 28962911 | no |
| B7 | **Sustained tensile DISTRACTION lengthens vertebrae AND raises disc height** | **Mouse caudal spine, custom springs at ~2× body mass across C7–C9: tensile force LENGTHENED THE VERTEBRAE in both the 6-week (14 wk of tension) and 12-week (8 wk) cohorts. IVD height increased in the 6-week cohort but NOT the 12-week cohort. No degeneration or loss of IVD mechanical performance. Endplate porosity rose then progressively recovered** | n/a | **YES — mechanical, mouse, direct VERTEBRAL LENGTH endpoint; and the age dependence is explicit** | 40179155 | **YES** |
| B8 | **Discal vs vertebral height growth diverge with age** | The scoliosis stereoradiographic literature reports discal height growth as effectively ending in early adolescence while vertebral growth continues; **I could not retrieve the primary for this in this search** | n/a | n/a | UNVERIFIED | **YES** |
| B9 | **Rapid pubertal growth is a RISK FACTOR for disc degeneration — a cost of trunk growth** | Prospective MRI, 59 healthy Finns at ages 11 and 18: adjusted **OR for Pfirrmann ≥3 at 18 was 7.92 (1.19–52.7) per additional 10% increase in SITTING HEIGHT** and 10.5 (1.60–68.7) per 10% total height; in the top BSA-increase tertile, 76% had ≥1 degenerate disc vs 10% in the lowest | n/a | n/a | 39332689 | **YES** |
| B10 | **Age-related pathologic disc calcification** | Reduces disc height and compliance | n/a | **ORAL CITRATE mitigated age-associated pathologic IVD calcification in LG/J mice — an oral agent with a disc endpoint** | 39930949 | **YES** |
| B11 | **Iron status and disc development** | Iron deficiency has dual effects on IVD development and on injury-induced degeneration (rodent) | n/a | Dietary iron, rodent | 40456894 | **YES** |
| B12 | **DDRGK1 / UFMylation preserves IVD development** | Required for normal disc development, mouse | n/a | Gene-level | 41460352 | **YES** |
| B13 | **EVC regulates SHH signalling in HUMAN IVD development** | Hedgehog in disc development and degeneration; EVC is a ciliary Hh modulator | n/a | Gene-level | 41550739 | **YES** |
| B14 | **Biglycan fragment → TGF-β activity in the disc via an eIF6-coupled path** | Matrix fragment controls disc TGF-β | n/a | Mechanistic | 39951526 | **YES** |
| B15 | **Runx1 overexpression → early-onset disc degeneration (mouse)** | Loss of disc height | n/a | Gene-level | 40932696 | **YES** |
| B16 | **Perlecan (HSPG2) in the disc** | Multiple repair roles; HSPG2 loss = dyssegmental dysplasia (E4) | n/a | Gene-level | 39081381 (INDEX); 38424183 | **YES** |
| B17 | **Notochordal remnants persisting in discs and vertebrae — TRPV4 SMD-Kozlowski** | Abnormal ossification + retained notochordal tissue in a human short-trunk dysplasia | n/a | n/a | 28687525 | **YES** |
| B18 | **Sirt6 deficiency → senescence and age-associated disc degeneration (mouse)** | Disc height | n/a | Gene-level; sirtuin activators exist, no axial endpoint | 40335469 | **YES** |
| B19 | **FOXO transcription factors required for disc homeostasis during ageing** | Disc height maintenance | n/a | Gene-level | 29963746 | **YES** |
| B20 | **Immune cells induce human NP ossification** | Converts disc to bone — irreversible height component loss | n/a | Human single-cell | 37638033 | **YES** |
| B21 | **Advanced glycation end-products / type 2 diabetes and the disc** | Loss of disc height and compliance | n/a | Diet/metabolic | 35992525 (INDEX); 41047888 | **YES** |
| B22 | **Denosumab inhibits endplate osteochondral remodelling adjacent to lumbar fusion (OVX rat)** | Endplate endpoint | n/a | **YES — pharmacological, rodent, ENDPLATE endpoint. Direction is discharge-blockade, i.e. it preserves cartilage rather than lengthening bone** | 34049577 | **YES** |
| B23 | **Calcitonin protects against fusion-induced adjacent-segment disc degeneration (OVX rat)** | Disc endpoint | n/a | **YES — pharmacological, rodent** | 26552386 | **YES** |
| B24 | **Spinal lymphatic system — an emerging fluid-homeostasis pathway in the spine** | Could bear on disc osmotic loading; entirely unexamined for growth | n/a | No | 41781379 (INDEX) | **YES** |

### C. OTHER AXIAL SEGMENTS AND THE SKULL BASE

| # | Structure / mechanism | Contribution to height | Closure timing | Agent with an axial endpoint? | Evidence (PMID) | Obscure? |
|---|---|---|---|---|---|---|
| C1 | **Sacrum (S1–S5)** | Only S1 enters conventional sitting-height measurement; segmentation anomalies alter sacral morphology | Sacral bodies fuse progressively into adulthood (exact ages UNVERIFIED) | No | 36787761; 41303779 | no |
| C2 | **Coccyx** | Effectively zero contribution to standing height | Variable; sacralisation of coccygeal vertebrae described | No | 35919212 | **YES** |
| C3 | **Spheno-occipital synchondrosis (SOS)** — the last major skull-base growth centre | Cranial base length; contributes to head height and facial projection | Fusion staged on CT; a **systematic review and meta-analysis** validates it as a skeletal maturity indicator; AI staging systems now published | No agent — **but it is the synchondrosis that fuses prematurely in achondroplasia, producing foramen magnum stenosis** | 40464024; 40891390; 41312140; 41722072 | no |
| C4 | **Spheno-ethmoidal synchondrosis** | Anterior cranial base length | Fuses earlier than SOS — **exact age UNVERIFIED; I found no primary in this search** | No | UNVERIFIED | **YES** |
| C5 | **Head height as a fixed component of standing height** | Standing height = head + neck + trunk + subischial leg; head height is largely fixed by early childhood, so it dilutes rather than contributes to adolescent height gain | Neurocranium near-adult early (exact % UNVERIFIED) | No | UNVERIFIED | **YES** |
| C6 | **Cervical spine (C1–C7)** | Small absolute contribution to sitting height, but the cervical ring apophysis is among the last axial structures to mature — cervical vertebral maturation (CVM) staging is used forensically into the third decade | Latest-maturing axial marker | No | 41766013; 41595939 | **YES** |
| C7 | **Thoracic vs lumbar contributions** | **Two-thirds of T1–S1 growth is thoracic, one-third lumbar** (Dimeglio, secondary source). Their ring apophyses mature on different schedules (A2) | see A2 | No | 24147251 (INDEX); 34362001 | **YES** |
| C8 | **Thoracic cage as a constraint on spinal growth** | Fusion of 50–75% of the thoracic spine before age 7 causes thoracic insufficiency syndrome | n/a | VEPTR (F7) | 24147251 (INDEX); 39941426 | no |
| C9 | **Atlas and axis (C1/C2) ossification pattern** | Craniocervical height | Characterised on CT | No | 22576894; 22105393 | **YES** |
| C10 | **Sacroiliac joint maturation** | Not a height component but a maturity read that is axial rather than appendicular | "What is normal" across ages described | No | 38559314 | **YES** |

### D. DEVELOPMENTAL ORIGIN, SEGMENTATION AND AXIAL IDENTITY

| # | Structure / mechanism | Contribution to height | Closure timing | Agent with an axial endpoint? | Evidence (PMID) | Obscure? |
|---|---|---|---|---|---|---|
| D1 | **Segmentation clock — HES7, LFNG, DLL3, MESP2, TBX6, RIPPLY2** | Sets vertebral NUMBER and segmentation fidelity; biallelic loss → spondylocostal dysostosis, short trunk with normal limbs | Prenatal | No agent | 37038048; 37323197; 33572886 (INDEX); 38418851 (INDEX) | no |
| D2 | **TBX6 hypomorphic haplotype (TACS)** — commonest known genetic cause of congenital scoliosis | Vertebral malformation → segmental trunk loss + curve | Prenatal | No agent; surgical outcomes stratified by genotype | 39833922; 38951757; 27437870 (INDEX) | no |
| D3 | **MSGN1 / mesogenin 1** — controls differentiation and movement of presomitic mesoderm progenitors; downstream of WNT+TBX6 | Axis elongation | Prenatal | No | 23172917; 17668009 | **YES** |
| D4 | **PAX1 / PAX9 → BAPX1 (NKX3-2)** sclerotome chondrogenic cascade | Vertebral body formation. **NKX3-2 biallelic inactivation → spondylo-megaepiphyseal-metaphyseal dysplasia (human)**; Bapx1-null mouse = lethal skeletal dysplasia with asplenia | Prenatal | No | 12490554; 20004766; 10572046; 10886375 | **YES** |
| D5 | **PAX1 sex-associated regulatory region (an AIS locus) — deletion in mouse** | Disc degeneration, instability and vertebral rotation | Postnatal phenotype from a developmental locus | Gene-level | 42039795 | **YES** |
| D6 | **MEOX1 / MEOX2** — required for Bapx1 expression; **MEOX1 mutations cause Klippel–Feil anomaly** (cervical fusion, short neck) | Removes cervical segment height | Prenatal | No | 23290072; 19520072; 15024065 | **YES** |
| D7 | **UNCX** — somite rostro-caudal polarity | Vertebral morphology | Prenatal | No | 35111756 (INDEX) | **YES** |
| D8 | **HOX code along the axis — mapped in the DEVELOPING HUMAN SPINE** | Sets vertebral identity, hence the thoracic:lumbar split and therefore trunk length | Prenatal | No | 39567486 | **YES** |
| D9 | **NR6A1 — "master regulator of vertebrate TRUNK development"; controls Hox dynamics** | Directly sets trunk length / vertebral number in mouse; **NR6A1 is one of three genes associated with human lumbar and rib numerical variation in UK Biobank**; and **human NR6A1 variants cause a novel oculo-vertebral-renal syndrome** | Prenatal | No agent | 36522318; 41261143; 40610405 | **YES** |
| D10 | **GDF11 / trunk-to-tail transition; Protogenin modulates GDF11–SMAD2** | Sets where the trunk ends → number of trunk vertebrae | Prenatal | GDF11 is a circulating TGF-β-superfamily ligand with active pharmacology interest, but **no axial length agent** | 39702818 | **YES** |
| D11 | **Engineered change of mammalian axial formulae** ("breaking constraint of mammalian axial formulae") | Proof that vertebral NUMBER is genetically tractable in mammals | Prenatal | No | 35017475 | **YES** |
| D12 | **Lin28a/let-7 modulates the Hox code via Polycomb during axial patterning** | Heterochronic control of axial identity | Prenatal | No agent | 32479258 | **YES** |
| D13 | **Jmjd3 (KDM6B) required for temporal collinear Hox activation in body axial patterning** | Axial identity | Prenatal | KDM6B tool inhibitors exist; **no axial endpoint** | 34368113 | **YES** |
| D14 | **Maternal SMCHD1 regulates Hox expression and patterning** | Axial identity; maternal-effect epigenetic | Prenatal | No | 35879318 | **YES** |
| D15 | **VRTN** — a vertebral-number gene long known in pig breeding, **reported for the first time in HUMANS in 2025** as influencing vertebral development | Number of thoracic/lumbar vertebrae → trunk length | Prenatal | No | 41261143 | **YES** |
| D16 | **GPC3 (glypican-3)** — associated with human lumbar/rib numerical variation; GPC3 loss = Simpson–Golabi–Behmel **overgrowth** syndrome | Both vertebral number and overall growth | Prenatal + postnatal | No | 41261143 | **YES** |
| D17 | **Supt20 required for axial skeleton development (mouse)** | Axial patterning | Prenatal | No | 27894818 | **YES** |
| D18 | **Fat4–Dchs1 signalling controls cell proliferation in DEVELOPING VERTEBRAE** | Vertebral size | Prenatal | No | 27381226 | **YES** |
| D19 | **Noggin + Gremlin1 cooperative activity in axial skeleton development** | BMP antagonism sets vertebral morphogenesis | Prenatal | No | 21303853 | **YES** |
| D20 | **TGF-β signalling required for sclerotome RESEGMENTATION (chick)** | Resegmentation is what makes each vertebral body span two half-somites; failure → segmentation defects | Prenatal | No | 35644252 | **YES** |
| D21 | **Notochord is required for amniote vertebral column segmentation** | Patterns the vertebral bodies and forms the nucleus pulposus | Prenatal | No | 29654746 | **YES** |
| D22 | **Spatio-temporal requirement for Sonic hedgehog in sclerotome-derived vertebrae and ribs** | Vertebral body formation is Hh-dependent in a defined window | Prenatal | Hh agonists exist; **no axial LENGTH endpoint found** | 38891790 | **YES** |
| D23 | **Extracellular volume expansion drives vertebrate axis elongation** | A physical rather than signalling driver of axial extension | Prenatal | No | 39879975 | **YES** |
| D24 | **Large-scale mouse mutagenesis screen for genes affecting VERTEBRAL ANATOMY** | An unbiased vertebral-specific gene list — the axial analogue of a limb-length screen | n/a | No | 41644829 | **YES** |
| D25 | **SOX9 transactivation middle-domain variants → axial skeleton dysplasia + scoliosis** | Axial-selective SOX9 dysfunction | Prenatal/postnatal | No | 39854231 | **YES** |
| D26 | **ADGRG6 / GPR126** — adhesion GPCR required in cartilaginous and dense connective tissue to maintain **spine alignment**; also maintains growth-plate homeostasis via IHH | Axial alignment and growth-plate IHH | Postnatal | No agent | 34318745; 39236220 | **YES** |
| D27 | **COL11A1 variation associated with AIS; and COL11A1 implicated in age-related spinal curvature by Mendelian randomisation** | Axial | n/a | No | 38277211; 40652108 | no |
| D28 | **c-Jun N-terminal kinases 1/2 deficiency → impaired annulus fibrosus development and VERTEBRAL FUSION with severe scoliosis (mouse)** | Vertebral fusion removes growth centres | Postnatal | JNK inhibitors exist; no axial length endpoint | 30664861 | **YES** |
| D29 | **A transcriptional and regulatory map of mouse somite maturation** | Reference resource for axial-specific gene discovery | n/a | No | 37499658 | **YES** |
| D30 | **Human paraxial mesoderm / somite organoids and a recapitulated human segmentation clock** | Enables human-specific axial-identity experiments in vitro | n/a | No | 35088712; 32238941 | **YES** |
| D31 | **Human evolutionary specialisation of the vertebral body and disc for bipedalism; hominin bipedalism in two steps** | Explains why human axial loading (and therefore Hueter–Volkmann at the vertebra) differs from quadrupeds — a caution on transferring quadruped vertebral results | n/a | No | 41900984 (INDEX); 40866708 | **YES** |

### E. AXIAL-SELECTIVE DYSPLASIAS AND NATURAL EXPERIMENTS

| # | Condition / gene | Contribution to height | Closure timing | Agent with an axial endpoint? | Evidence (PMID) | Obscure? |
|---|---|---|---|---|---|---|
| E1 | **SEDC / Kniest / SEMD — COL2A1** | Short trunk with platyspondyly — the canonical type-II-collagenopathy trunk phenotype | n/a | No axial-length agent | 31824186; 41378240; 35052477 | no |
| E2 | **X-linked SED tarda — TRAPPC2 (sedlin)** | Short trunk emerging in mid-childhood; **repeatedly misdiagnosed as GH deficiency**, so rhGH has been given without an axial benefit being demonstrated | Post-childhood onset | rhGH (by misdiagnosis) | 42288746; 41059451; 41732158 | no |
| E3 | **Brachyolmia / SMD Kozlowski / metatropic dysplasia — TRPV4** | Short trunk, platyspondyly. **TRPV4 is a mechanosensitive Ca²⁺ channel and BOTH gain- and loss-of-function give short-trunk dysplasia** — an axial band with both ends bad | n/a | TRPV4 modulators exist (pain, pulmonary); **no axial endpoint** | 41225599; 21658220; 35170874; 28687525 | no |
| E4 | **Dyssegmental dysplasia (Silverman–Handmaker, Rolland–Desbuquois) — HSPG2/perlecan** | **Anisospondyly** — vertebrae of different sizes; the purest "vertebral-size" gene known | Prenatal/lethal | No | 40503612; 38424183 | **YES** |
| E5 | **Spondylocostal dysostosis — DLL3, MESP2, LFNG, HES7, TBX6, RIPPLY2** | Short trunk from segmentation failure **with normal limbs** — the archetypal dissociation of trunk from limb | Prenatal | No | 37038048; 36506336 (INDEX) | no |
| E6 | **Spondylothoracic dysostosis (Jarcho–Levin) — MESP2** | "Crab-like" thorax; severe trunk shortening with normal limb length | Prenatal | No | 39836964; 39836966 | no |
| E7 | **Achondroplasia (FGFR3) — the AXIAL component specifically** | Thoracolumbar kyphosis, caudal interpedicular narrowing, spinal stenosis, foramen magnum stenosis from premature spheno-occipital fusion. Trunk length is relatively preserved while limbs are short | Premature synchondrosis fusion | **YES — vosoritide spine morphology, G1** | 41783511; 41722072; 42074943 | no |
| E8 | **Mucopolysaccharidosis IVA (Morquio, GALNS) and MPS I/II** | Short trunk with platyspondyly and odontoid hypoplasia; ERT does not restore spine growth | n/a | ERT (limited bone benefit); new MPS IVA model built for bone-targeted therapy testing | 41783940; 35822096; 41141144 | no |
| E9 | **Spondylo-megaepiphyseal-metaphyseal dysplasia — NKX3-2 biallelic** | Short trunk | Prenatal | No | 20004766 | **YES** |
| E10 | **Osteogenesis imperfecta — vertebral compression and reshaping** | Loss of vertebral height by fracture, partly recoverable | n/a | **YES — bisphosphonates/zoledronate; vertebral body RESHAPING is the recognised index (G10)** | 37843393; 38198649; 35693066 | no |
| E11 | **Aggrecanopathy (ACAN)** | Short stature with variable trunk involvement | n/a | rhGH 3-year response reported | 39502477; 42041619 | no |
| E12 | **SHOX deficiency / Léri-Weill / Turner** | The **mirror case**: LIMB-selective shortening with relatively preserved trunk → HIGH sitting-height ratio. The natural experiment that defines the axial/appendicular axis clinically | n/a | rhGH — body proportions reported in Turner and in SHOX deficiency | 37476877; 37014306; 36611397 | no |
| E13 | **Marfan / FBN1** | The other mirror: long limbs, relatively spared trunk → LOW upper:lower segment ratio | n/a | No | 42058477 (INDEX) | no |
| E14 | **Klippel–Feil (MEOX1 and others)** | Congenital cervical fusion → fixed loss of neck height | Prenatal | No | 23290072 | no |
| E15 | **Scheuermann kyphosis** | Anterior vertebral wedging over ≥3 consecutive vertebrae; measured-height loss plus true endplate pathology | Adolescent onset | Bracing; a long-term controlled cohort exists | 41594596 (INDEX); 37746785; 37615931 | no |
| E16 | **Congenital vertebral malformation — the wider molecular landscape** | Hemivertebra, block vertebra, unsegmented bar → segmental trunk height loss | Prenatal | No | 38291488 (INDEX); 41751889; 40004644 (INDEX) | no |
| E17 | **SPONASTRIME dysplasia — TONSL** | Short trunk; a GH-treated case reported | n/a | rhGH, case-level | 40794898 | **YES** |
| E18 | **Spondyloenchondrodysplasia — ACP5** | Axial dysplasia with immune dysregulation; **JAK inhibitors used therapeutically (immune indication, not growth)** | n/a | JAK inhibitor — no axial length endpoint | 41993173 | **YES** |
| E19 | **Weaver syndrome (EZH2)** — overgrowth including vertebral | Tall stature class; relevant as the axial arm of an overgrowth syndrome | n/a | EZH2 inhibitors exist and run the wrong way | 40922349 | no |
| E20 | **Pudgy mouse — rib deformities from abnormal PARAVERTEBRAL LONGITUDINAL cartilage/bone accumulations** | A distinct axial-specific mechanism of deformity | Prenatal | No | 38252118 | **YES** |

### F. MECHANICAL AND DEVICE MODULATION OF AXIAL GROWTH

| # | Structure / mechanism | Contribution to height | Closure timing | Agent with an axial endpoint? | Evidence (PMID) | Obscure? |
|---|---|---|---|---|---|---|
| F1 | **Hueter–Volkmann at the vertebral endplate** — sustained compression slows, tension/distraction accelerates growth | The basis of every growth-modulation device and of the "vicious cycle" model of curve progression | n/a | **YES — mechanical, several species** | 36593421; 16845350; 17049077 (INDEX); 33392452 (INDEX) | no |
| F2 | **Anterior vertebral body tethering (VBT)** | Modulates growth to correct a curve while preserving motion | Requires remaining growth; Risser and Sanders stage predict outcome | **YES — the only widely used clinical growth-modulation implant** | 42425513; 41236616; 41285586; 40484922 | no |
| F3 | **Posterior VBT in a kyphotic porcine model — tether tension is BIPHASIC** | **High-tension single-level tethering gave 53±43% growth modulation at 2 weeks vs −1±15% low-tension (p=0.03) and vs controls (p=0.01); by 2–4 weeks the two normalised (14±11% vs 10±10%, p=0.6).** FEA: growth-plate stress distribution worsens as post-realignment disc height falls | n/a | **YES — mechanical, pig, fluorochrome-labelled regional VERTEBRAL GROWTH RATES** | 40836185; 41417440 | **YES** |
| F4 | **Vertebral body stapling (nitinol / shape-memory alloy)** | Growth modulation without a cord | n/a | **YES — mechanical, swine and bovine** | 23814625; 32145672; 21173627 | **YES** |
| F5 | **Distraction-based growing rods, traditional and magnetically controlled (MCGR)** | Repeated distraction of the whole spine; **T1–S1 length is the standard endpoint of this entire literature** | Used to "graduation" at skeletal maturity | **YES — device, human, spinal-length endpoint** | 39313723; 41580553; 40437325; 39797260 | no |
| F6 | **Spring Distraction System vs One-Way Self-Expanding Rod (BiPOWR randomised trial)** | Continuous vs ratcheting distraction compared head-to-head | n/a | **YES — device, RANDOMISED, human, spinal length** | 40432854 | **YES** |
| F7 | **VEPTR (vertical expandable prosthetic titanium rib)** | Expands thorax and indirectly the spine in thoracic insufficiency | n/a | YES — device | 40385246 | no |
| F8 | **Posterior (convex) centre-of-rotation, length-stable implant vs anterior COR** | **FEA + swine: a POSTERIOR centre of rotation increased disc height, redistributed physeal stress to PROMOTE growth; an anterior COR decreased disc height and INHIBITED growth. The posterior implant achieved +24±10% appositional metaphyseal growth modulation vs −11±13% in controls (p=0.001)** | n/a | **YES — the only explicitly GROWTH-PROMOTING vertebral device result I found** | 41041616 | **YES** |
| F9 | **Anterior vertebral PERIOSTEAL transection as growth modulation (swine)** | **NEGATIVE: 170±19 µm/day control vs 155±25 µm/day treated, p=0.054 — periosteal resection did NOT accelerate vertebral growth.** The axial analogue of periosteal release in long bones, and it failed | n/a | **YES — surgical, swine, vertebral growth RATE endpoint; result is null/negative** | 41041616 | **YES** |
| F10 | **Direct electrical current applied to vertebral growth (animal)** | Modulated vertebral growth; proposed for scoliosis | n/a | **YES — physical agent, animal, vertebral endpoint** | 20502237 | **YES** |
| F11 | **Halo-gravity traction** | Preoperative axial traction with measurable curve and length change | n/a | YES — mechanical, human | 41480511 (INDEX); 40868497; 38792417 | no |
| F12 | **Crankshaft phenomenon** — continued ANTERIOR vertebral growth after posterior-only fusion | Direct proof that the anterior column keeps growing after the posterior column is tethered; risk stratified by NCS status and Risser stage | Occurs while the NCS and anterior physes remain open | An unwanted natural experiment demonstrating residual axial growth | 42291699; 40691841; 39985050 (INDEX); 40022041 | no |
| F13 | **Dual rod-plate system improving vertebral wedging while permitting spinal growth** | Corrects wedging without arresting growth | n/a | YES — device | 37773144 | **YES** |
| F14 | **Segmental trans-endplate pedicle screws do NOT induce deformity (porcine)** | Useful NEGATIVE control: crossing the endplate physis with hardware did not deform the spine | n/a | YES — mechanical, pig | 41910710 | **YES** |
| F15 | **Dynamic growth rod inducing spinal growth modulation** | New device class | n/a | YES — device | 39801572 | **YES** |
| F16 | **Modern Luque trolley (guided growth)** | Prospective cohort; fewer reoperations than other growth-friendly techniques | n/a | YES — device | 40437325 | no |
| F17 | **A novel fusionless vertebral PHYSEAL device inducing spinal growth modulation** | Acts directly on the vertebral physis rather than across the disc | n/a | YES — device | 18712419 | **YES** |
| F18 | **Whole-body vibration and long-term disc injury** | A mechanical exposure with a disc endpoint (occupational) | n/a | Physical exposure | 10664303 | **YES** |
| F19 | **Deep vs shallow water running and spinal shrinkage** | Water immersion reduces axial load and therefore spinal shrinkage — a modality directly targeting B5 | n/a | Physical | 9562163 | **YES** |
| F20 | **Dorsal arthrodesis in prepubertal rabbits followed to maturity — effect on thoracic dimensions and spine growth** | The classic controlled animal demonstration that fusing the posterior spine constrains axial growth | n/a | YES — surgical, rabbit, spinal length | 20165672 | **YES** |
| F21 | **Bracing in AIS** | Alters the mechanical environment of the growing spine; the effect on axial LENGTH (rather than curve) is essentially never reported | n/a | Mechanical, human | 41952967 (INDEX); 42181829 | no |

### G. AGENTS WITH A MEASURED AXIAL / VERTEBRAL / TRUNK ENDPOINT

| # | Agent | Axial endpoint and result | Species | Class | Evidence (PMID) | Obscure? |
|---|---|---|---|---|---|---|
| G1 | **VOSORITIDE (CNP analogue) — spine morphology, randomised double-blind placebo-controlled phase 2, CANOPY ACH-2I / NCT03583697, 75 children aged 0–<5 y with achondroplasia** | **L4 interpedicular distance LSM difference 0.509 mm (95% CI −0.034 to 1.052), P=.066; L4 sagittal canal width 1.433 mm (0.547–2.320), P=.002; pathological (≥20°) thoracolumbar kyphosis in 33.3% vs 59.3% placebo, P=.037.** ⚠ The endpoints are CANAL WIDTH and KYPHOSIS ANGLE — **not vertebral body HEIGHT** | human | CNP | 41783511 | no |
| G2 | **CNP analogues (vosoritide + navepegritide) — meta-analysis of 4 RCTs, n=326** | AGV +1.36 cm/yr (1.05–1.68); standing height +1.24 cm (0.47–2.01, P=.002); **NO short-term effect on upper-to-lower segment (ULS) ratio** | human | CNP | 42306228 | no |
| G3 | ⭐ **NPR3 (natriuretic peptide clearance receptor) LOSS — mouse** | **Disproportionate elongation of the PROXIMAL AND MID-TAIL VERTEBRAE, in addition to the proximal limb.** The only genetic perturbation I found producing explicit vertebral *elongation* in an otherwise normal animal | mouse | genetic; NPR3 is a druggable clearance receptor | 41073372 | **YES** |
| G4 | ⭐ **LEPTIN — the axial/appendicular divergence with a length endpoint in BOTH compartments in the SAME animals** | **8-week-old leptin-deficient (ob/ob) mice had SHORTER TIBIAE and LONGER VERTEBRAE than wild type.** Disturbed columnar structure in the tibial plate but NOT the vertebral plate. In primary culture, leptin INHIBITED vertebral growth-plate chondrocyte proliferation and PROMOTED apoptosis, downregulating COL2A1, aggrecan, PCNA, SOX9 and SMAD4 dose-dependently — while STIMULATING tibial growth-plate chondrocytes at physiological doses (10 and 50 ng/mL). Ob-Rb expression is itself vertebral/appendicular region-specific | mouse | endogenous hormone | 28569158 | **YES** |
| G5 | **OESTRADIOL at the VERTEBRAL growth plate — bipedal rat scoliosis model, 120 animals** | OVX and triptorelin groups (low oestrogen) had a **significantly LONGER hypertrophic zone in the VERTEBRAL cartilage growth plate**, more collagen X, less collagen II, and **higher Ki67 proliferation** than intact-female and OVX+E2 groups. Anterior column grew slower and posterior column faster in the high-oestrogen groups (T11–T13 on CT) | rat | sex steroid | 30405118 | **YES** |
| G6 | **TRIPTORELIN (GnRH agonist) — same study** | Decreased scoliosis incidence and curve magnitude; vertebral growth-plate hypertrophic zone longer than in intact females | rat | GnRHa | 30405118 | **YES** |
| G7 | ⭐ **TYRA-300 (FGFR3-selective inhibitor) — two FGFR3-driven chondrodysplasia mouse models (ACH Fgfr3^Y367C/+ and an HCH model)** | **"TYRA-300 INCREASED THE LUMBAR VERTEBRAE LENGTH and improved the shape of the intervertebral discs in BOTH models"**, alongside increased nasoanal, tibia and femur length, and improved skull/foramen magnum size and shape. **An explicit VERTEBRAL LENGTH endpoint under a drug — the only small molecule in this enumeration with one.** ⚠ Both models are FGFR3 gain-of-function, so this is restoration, not elevation above normal | mouse | FGFR3-selective TKI | 40178985 | no |
| G8 | ⭐ **Fgfr3 ENHANCER (−29E) deletion — mouse** | Deleting a cartilage enhancer 29 kb upstream of Fgfr3 in an achondroplasia model **"largely normalized long bone AND VERTEBRAL BODY GROWTH, markedly reduced spinal canal and foramen magnum stenosis"**. **A vertebral body growth endpoint.** ⚠ Again a rescue in an FGFR3 gain-of-function model | mouse | genetic (enhancer) | 39817451 | no |
| G9 | **Infigratinib / NVP-BGJ398 — FGFR3 TKI, mouse ACH model + human PROPEL/PROPEL 2** | Functionally improves FGFR3-related dwarfism; human trials report height velocity and proportions. **Vertebral-specific endpoint UNVERIFIED** | mouse + human | FGFR3 TKI | 27064282; 35342457 | no |
| G10 | **PIEZO1 INHIBITOR delivered locally by hydrogel to the vertebral growth plate** | Decelerated scoliosis progression; **systemic inhibition caused osteoporosis, which is why local delivery was engineered** | mouse | ion-channel blocker | 40714837 | **YES** |
| G11 | **ORAL CITRATE — LG/J mouse** | Mitigated age-associated pathologic **intervertebral disc calcification** | mouse | oral small molecule | 39930949 | **YES** |
| G12 | **DENOSUMAB (anti-RANKL) — OVX rat** | Inhibited **endplate osteochondral remodelling** and vertebral osteoporosis adjacent to lumbar fusion | rat | biologic | 34049577 | **YES** |
| G13 | **CALCITONIN — OVX rat** | Protective against fusion-induced adjacent-segment disc degeneration | rat | peptide hormone | 26552386 | **YES** |
| G14 | **BISPHOSPHONATES / ZOLEDRONATE — children** | **VERTEBRAL BODY RESHAPING after fracture is an established index of recovery** in glucocorticoid-treated children; zoledronate reduces fractures in paediatric skeletal fragility. This is restoration of lost vertebral height, not elevation above normal | human | bisphosphonate | 37843393; 39324646; 35693066 | no |
| G15 | **MINODRONATE — AIS mouse model** | Improved low bone mass and **reduced progressive THORACIC SCOLIOSIS** | mouse | bisphosphonate | 30138335 | **YES** |
| G16 | **EXOGENOUS MELATONIN — melatonin-deficient C57BL/6J mice** | Reduced scoliotic curvature and improved bone quality | mouse | hormone | 30996275 | **YES** |
| G17 | ⭐ **CRANIOSPINAL IRRADIATION — human, 1149 GH-treated childhood cancer survivors** | 5-year ΔHeight-SDS: craniopharyngioma (cranial RT only) **1.6 (0.3–3.0)**; medulloblastoma (**craniospinal RT**) **0.9 (0.0–1.9)**; leukaemia after TBI **0.3 (0–0.7)** vs without RT 0.5 (0–0.9), P<0.001. Authors: **both craniospinal and epiphyseal irradiation negatively affect the growth response to GH.** The cleanest human demonstration that the axial growth reserve is separately destructible and separately rate-limiting | human | ionising radiation | 32706856 | no |
| G18 | **GLUCOCORTICOIDS — human children** | Vertebral fractures and impaired vertebral reshaping; the spine is the first site of glucocorticoid skeletal harm | human | steroid | 37843393; 39126675 (INDEX) | no |
| G19 | **rhGH in Turner syndrome — body proportions** | Sitting height / proportion endpoints reported on GH | human | GH | 37476877 | no |
| G20 | **rhGH in SHOX deficiency** | Long-term real-life efficacy; the proportion response is informative because SHOX is limb-selective | human | GH | 37014306 | no |
| G21 | **rhGH and SPINAL growth / scoliosis specifically** | Dedicated review of GH's effect on **spinal** growth and of rhGH's relation to AIS; findings across studies are divergent and contradictory | human | GH | 39524395 (INDEX) | **YES** |
| G22 | **Vosoritide in HYPOCHONDROPLASIA, phase 2** | Growth velocity endpoint; whether an axial/proportion endpoint was reported is **UNVERIFIED** | human | CNP | 38813446 | no |
| G23 | **TERIPARATIDE / PTH 1-34 in children with familial hypoparathyroidism** | **Bone health AND linear growth reported in treated children** — one of very few paediatric PTH growth datasets. Axial component UNVERIFIED | human | PTH | 39883563 | **YES** |
| G24 | **PTH → osteoblast Slit3 reduces aberrant sensory innervation in degenerated VERTEBRAL ENDPLATES (mouse)** | Endplate endpoint (pain, not height) | mouse | PTH | 41571628 | **YES** |
| G25 | **TGF-β1 inhibition of osteoclast differentiation and abnormal angiogenesis in IVD degeneration** | Disc/endplate endpoint | animal | TGF-β | 38014468 | **YES** |
| G26 | **Fibroblast activation protein-α inhibition — reduced vascular invasion of the CARTILAGE ENDPLATE** | Endplate endpoint | animal | small molecule | 41531174 | **YES** |
| G27 | **HUMANIN — glucocorticoid-treated DMD mouse** | Bone health including spine; **whether vertebral LENGTH was measured is UNVERIFIED** | mouse | peptide | 41550496 | **YES** |
| G28 | **SULFURETIN (Nrf2 activation) — zebrafish** | Stimulated chondrocyte differentiation and **increased bone lengths** — but zebrafish have a vertebral column without a mammalian physis, so transfer is weak | zebrafish | natural product | 37748761 | **YES** |
| G29 | **Enzyme replacement therapy in MPS** | Spine growth and platyspondyly largely NOT rescued — a recorded negative for the axial compartment | human | ERT | 35822096; 41783940 | no |
| G30 | **Vamorolone (dissociative steroid) in DMD** | Chosen partly to spare growth; **no vertebral length endpoint** | human | steroid | 41427054 | **YES** |
| G31 | **Aromatase inhibitor used in X-linked hypophosphataemic rickets with advanced bone age** | A case in which an AI was deployed for period extension in a condition with an axial component | human | AI | 37140989 | **YES** |

### H. MEASUREMENT OF TRUNK GROWTH, AND ITS CONFOUNDS

| # | Structure / mechanism | Contribution to height | Closure timing | Agent? | Evidence (PMID) | Obscure? |
|---|---|---|---|---|---|---|
| H1 | **Sitting height / subischial leg length / upper:lower segment ratio** | The only routine clinical partition of stature into axial and appendicular | n/a | Used as an endpoint in G2, G19, G20 | 42306228; 41909446 | no |
| H2 | ⭐ **Sitting-height-to-standing-height ratio REFERENCE CHARTS (NHANES III, 9,569 US children aged 2–18)** | **SitHt/Ht DECREASES from prepuberty into early puberty and INCREASES again in LATE puberty, in both sexes.** Non-Hispanic Black children have significantly lower SitHt/Ht throughout childhood, so ancestry-specific charts are required | n/a | n/a | 32579888 | **YES** |
| H3 | ⭐ **Spinal growth velocity, longitudinal normal cohort followed to maturity (n=54)** | **Childhood: 1.55±0.21 cm/yr girls, 1.14±0.23 cm/yr boys. During the growth spurt: 1.75±0.11 cm/yr girls, 2.00±0.11 cm/yr boys. At PHV90%, children are 90% of adult TOTAL height but only 87% of adult SPINE height** | The spine finishes AFTER total height | n/a | 39585607 | **YES** |
| H4 | **Multipliers of remaining spinal growth relative to PHV90% / Peak Growth Age** | Allow prediction of adult spine length from current spine length and maturity | n/a | n/a | 39585607 | **YES** |
| H5 | ⭐ **Thoracic spine growth re-measured on CT in 144 children, challenging the classical Dimeglio curve** | **T1–T12 growth: 1.71 cm/yr (1–4 y), 0.55 (4–8 y), 0.74 (8–10 y), 0.69 (10–12 y), and 1.61 cm/yr (12–16 y).** Two break points — end of year 4 and beginning of year 12 | n/a | n/a | 28609322 | **YES** |
| H6 | **Classical Dimeglio spinal growth data** | T1–S1 ≈18 cm at birth → ≈45 cm at maturity; ≈49% of sitting height at maturity, two-thirds thoracic and one-third lumbar; thoracic spine ≈1.3 cm/yr birth–5 y, 0.7 cm/yr 5–10 y, 1.1 cm/yr in puberty. **Quoted from a secondary source (review by the original author) — the primary monograph was not retrieved** | n/a | n/a | 24147251 (INDEX); 21874626 (INDEX) | no |
| H7 | **Diurnal spine-length variation must be controlled in any trunk measurement** | −1.0 mm median T11→L4 in children over a day; the whole-column effect is larger | n/a | Protocol requirement | 39568059 | **YES** |
| H8 | **Height estimation from lumbar length on postmortem CT, age-corrected** | A new age-adjusted formula linking lumbar length to stature | n/a | n/a | 41632800 | **YES** |
| H9 | **Cobb angle → measured height loss** | Curvature converts true spinal length into lost measured height; surgical correction recovers part of it | n/a | Surgical | **formula UNVERIFIED** | no |
| H10 | ⭐ **Ring apophysis maturation (RAM) as a SPINE-SPECIFIC maturity index, distinct from hand bone age** | RAM correlates with age at R=0.892 and differs by level and by sex; **AIS girls have significantly DELAYED ring apophysis maturation vs the normal population** | n/a | n/a | 34362001; 38849690 | **YES** |
| H11 | **Risser sign (iliac apophysis) and Sanders stage** | The conventional indices used to decide whether axial growth remains; both predict VBT outcome | n/a | n/a | 41236616; 18946691 | no |
| H12 | **Cervical vertebral maturation + spheno-occipital synchondrosis on CT — a probabilistic age framework** | An entirely axial skeletal maturity read, independent of the hand | n/a | n/a | 41766013 | **YES** |
| H13 | **Age-related increase in spinal curvature — UK Biobank DXA, 41,212 participants** | **Kyphotic angle increases 2.42° per decade and lordotic angle 1.48° per decade**; greater curvature is associated with lower muscle mass and lower BMD. MR implicates COL11A1, PTHLH, ETFA, TWIST1, RAD9A, MMS22L, HIF1A, RAB28 | n/a | n/a | 40652108 | **YES** |
| H14 | **Cormic index / sitting-height ratio secular change** | **In 20,336 Japanese subjects, the Cormic index rose until 1942, fell to a nadir in the 1970s, then rose again to 1995 — and nearly HALF the spirometric deviation from European reference values was explained by cohort differences in the Cormic index.** Direct evidence that the trunk:leg partition shifts with environment within a population | n/a | n/a | 25254426 | **YES** |
| H15 | **Low lung function in low-income settings is "analogous to stunting"** | Indirect: relative leg vs trunk growth tracks the environment | n/a | n/a | 33381655 (INDEX) | **YES** |
| H16 | **Sitting-height index of build, (mass)/(sitting height)³** | An alternative index arguing sitting height is the better scaling denominator than stature | n/a | n/a | 29470414 | **YES** |
| H17 | **Spinal sagittal and coronal morphology in children with SHORT STATURE** | Directly asks what the spine looks like in the short-stature population | n/a | n/a | PMC11847212 (no PMID retrieved) | **YES** |
| H18 | **EOS / biplanar low-dose radiography for repeated 3D spine length** | Enables serial T1–S1 measurement at low dose | n/a | n/a | **specific PMID UNVERIFIED** | no |
| H19 | **Spinal irradiation dose–response and vertebral growth in radiotherapy planning** | The dosimetric literature explicitly models vertebral growth impairment (whole-vertebra irradiation to reduce asymmetric growth) | n/a | Radiation | 30481777 (INDEX); 25403639 (INDEX) | no |

---

## PROSE 1 — EVERY AGENT IN ANY SPECIES WITH A MEASURED VERTEBRAL OR TRUNK LENGTH ENDPOINT

This is the answer to the brief's central question, and the honest summary is: **the list is very
short, and only two entries are a true vertebral-elongation result in a normal animal.**

### Tier 1 — a VERTEBRAL LENGTH endpoint, in an otherwise normal animal, in the favourable direction

1. **Npr3 loss of function, mouse (PMID 41073372).** Loss of Natriuretic Peptide Receptor 3
   causes **disproportionate elongation of the proximal and mid-tail vertebrae, in addition to the
   proximal limb**. This came out of a study whose whole purpose was to ask how *individual
   vertebrae* set their proportion, so the vertebral measurement is primary rather than incidental.
   It is the single most decision-relevant row in this enumeration: NPR3 is a secreted-ligand
   clearance receptor, i.e. a druggable extracellular node, and it is the only such node with a
   direct vertebral length result.
2. **Leptin deficiency (ob/ob), mouse (PMID 28569158).** 8-week-old ob/ob mice had **shorter
   tibiae and LONGER VERTEBRAE** than wild type. Because both compartments were measured in the
   same animals, this is simultaneously a vertebral length result and the cleanest demonstration
   of axial/appendicular divergence anywhere in this domain. Direction: **less leptin signalling =
   longer vertebrae**, with the mechanism reproduced in primary vertebral growth-plate chondrocytes
   (leptin inhibited their proliferation and promoted apoptosis, while stimulating tibial
   chondrocytes at physiological concentrations).
3. **Sustained tensile distraction, mouse caudal spine (PMID 40179155).** Not a molecule, but a
   direct length endpoint: springs delivering ~2× body mass **lengthened the vertebrae** in both a
   6-week-old and a 12-week-old cohort, and **raised IVD height in the adolescent cohort only**.
   No degeneration, no loss of IVD mechanical performance, and endplate porosity recovered. This
   is the axial analogue of distraction osteogenesis and it has an explicit age dependence.

### Tier 1b — a VERTEBRAL LENGTH endpoint under a pharmacological or genetic intervention, but in a DEFICIT model (restoration, not elevation)

3b. ⭐ **TYRA-300, FGFR3-selective inhibitor, mouse (PMID 40178985).** **"TYRA-300 increased the
   lumbar vertebrae length and improved the shape of the intervertebral discs in both models"** —
   in an Fgfr3^Y367C/+ achondroplasia model and a hypochondroplasia model, alongside nasoanal,
   tibia and femur length and improved skull/foramen magnum shape. **This is the only small
   molecule in the whole enumeration with an explicit vertebral length endpoint.** Because both
   models carry an activating FGFR3 allele, the result is a rescue toward normal — it does not
   establish that the compound elongates a normal vertebra.
3c. ⭐ **Fgfr3 −29E cartilage enhancer deletion, mouse (PMID 39817451).** Deleting a cartilage
   enhancer 29 kb upstream of Fgfr3 **"largely normalized long bone AND vertebral body growth,
   markedly reduced spinal canal and foramen magnum stenosis"**. Same caveat: rescue in a
   gain-of-function model. But together with 3b these establish that **the FGFR3 axis demonstrably
   reaches the vertebral body, which almost nothing else in the growth pharmacopoeia has been
   shown to do.**

### Tier 2 — a vertebral GROWTH RATE or growth-plate histology endpoint under an intervention

4. **PIEZO1 inhibitor delivered locally into vertebral growth-plate cartilage, mouse
   (PMID 40714837).** Pharmacological and genetic PIEZO1 blockade decelerated scoliosis; a hydrogel
   micro-endoscopic delivery system was built specifically because *systemic* PIEZO1 inhibition
   caused osteoporosis. Endpoint is growth-plate ferroptosis and curve progression, not length.
5. **Oestradiol and triptorelin, bipedal rat (PMID 30405118).** Vertebral cartilage growth-plate
   hypertrophic zone length, collagen X/II, and Ki67 measured directly. Low-oestrogen groups (OVX,
   triptorelin) had **longer vertebral hypertrophic zones and more proliferation**. This is the
   oestrogen arm measured *at the vertebral plate* rather than inferred from limb data.
6. **Posterior-centre-of-rotation length-stable implant, swine (PMID 41041616).** **+24±10%
   appositional metaphyseal growth modulation vs −11±13% in controls (p=0.001)** — a
   growth-*promoting* mechanical intervention with a vertebral growth endpoint.
7. **Anterior vertebral periosteal transection, swine (PMID 41041616).** **NEGATIVE: 170±19 vs
   155±25 µm/day, p=0.054.** Recorded because negatives are part of the map — the axial version of
   periosteal release does not work.
8. **Posterior vertebral body tethering tension, kyphotic pig (PMID 40836185).** Fluorochrome-
   labelled **regional vertebral growth rates**: 53±43% modulation at high tension vs −1±15% at low
   tension at 2 weeks, converging by 4 weeks. The tension–growth relation is **biphasic in time**.
9. **Asymmetric compression then release, rat caudal growth plate (PMID 36232897).** Hypertrophic
   layer height and chondrocyte height on the concave side **doubled** after 3 weeks of correction.
10. **Direct electrical current, animal (PMID 20502237).** Modulated vertebral growth.

### Tier 3 — human agents with an axial/proportion endpoint (none of which is vertebral body height)

11. **Vosoritide, randomised phase 2, achondroplasia (PMID 41783511).** L4 canal width +1.433 mm
    (P=.002); pathological thoracolumbar kyphosis 33.3% vs 59.3% (P=.037); L4 interpedicular
    distance P=.066. ⚠ These are **canal and angle** endpoints, not vertebral height.
12. **CNP analogues, meta-analysis of 4 RCTs, n=326 (PMID 42306228).** AGV +1.36 cm/yr, standing
    height +1.24 cm — and **no short-term change in the upper:lower segment ratio**, i.e. the
    height gain was not preferentially axial or preferentially appendicular over that window.
13. **Craniospinal irradiation (PMID 32706856).** The only large human dataset that isolates the
    axial growth reserve as a separate, separately-destructible quantity: 5-year ΔHtSDS on GH was
    **1.6 after cranial-only RT vs 0.9 after craniospinal RT**.
14. **Bisphosphonates/zoledronate in children (PMIDs 37843393, 39324646, 35693066).** Vertebral
    body **reshaping** after fracture — a real human vertebral-height endpoint, but recovery of lost
    height, not elevation.
15. **rhGH in Turner and in SHOX deficiency (PMIDs 37476877, 37014306).** Proportion endpoints.
16. **Growing rods / MCGR / VBT / halo traction (F5, F6, F11).** T1–S1 length is the routine
    endpoint of this entire device literature. The BiPOWR trial (PMID 40432854) is randomised.

### Tier 4 — a DISC or ENDPLATE endpoint under an agent
Oral citrate (39930949) · denosumab (34049577) · calcitonin (26552386) · TGF-β1 (38014468) ·
FAP-α inhibition (41531174) · PTH–Slit3 (41571628) · minodronate (30138335) · melatonin (30996275).

### What is conspicuously ABSENT
I found **no agent of any class given to a normal growing mammal with vertebral body height, T1–S1
length or sitting height as a pre-specified primary endpoint.** Specifically:
- **No GH, IGF-1, aromatase-inhibitor, oestrogen-receptor, hedgehog, Wnt, PTH1R, thyroid or
  glucocorticoid study I retrieved reports a vertebral length number in a NORMAL animal.**
- **The FGFR3-selective class is the exception and it is unambiguous** (TYRA-300, PMID 40178985:
  lumbar vertebrae length increased; −29E enhancer deletion, PMID 39817451: vertebral body growth
  normalised). Infigratinib (27064282) very likely has comparable data that I could not verify
  from the abstract. **Every one of these is in an FGFR3 gain-of-function model.**
- The entire scoliosis device literature measures spinal LENGTH routinely, and the entire
  growth-pharmacology literature measures LIMB length routinely, and **the two literatures have
  essentially never been crossed.**
- **The single most efficient unfilled experiment in this domain is trivially cheap: any group
  already dosing a growing normal rodent for a limb-length endpoint could add a caliper or µCT
  measurement of lumbar vertebral body height and T1–S1 length at necropsy.** The tissue is
  already in the animal; nobody measures it.

---

## PROSE 2 — WHAT IS DIFFERENT ABOUT THE VERTEBRAL GROWTH PLATE FROM A LIMB GROWTH PLATE

This section is the reason a limb result cannot be assumed to transfer. Differences are ordered by
how much they should change a prediction.

**1. THE SAME HORMONE CAN HAVE THE OPPOSITE SIGN.** This is not hypothetical. Leptin
**stimulates** proliferation and chondrogenic differentiation in tibial growth-plate chondrocytes
at physiological concentrations, and **inhibits** proliferation and **promotes apoptosis** in
vertebral growth-plate chondrocytes, downregulating COL2A1, aggrecan, PCNA, SOX9 and SMAD4
dose-dependently. Consistently, ob/ob mice have **shorter tibiae and longer vertebrae**. The
authors attribute this to region-specific expression of the leptin receptor Ob-Rb itself
(PMID 28569158). **Any agent whose receptor has a different abundance in axial vs appendicular
cartilage can behave this way, and almost none has been checked.**

**2. THE ARCHITECTURE IS DIFFERENT: NO EPIPHYSEAL SECONDARY OSSIFICATION CENTRE.** A limb physis
sits between a metaphysis and a bony **epiphysis** containing a secondary ossification centre. A
vertebral endplate physis sits between the vertebral body (metaphyseal side) and the **cartilage
endplate and then the intervertebral disc** — an avascular, osmotically loaded tissue — on the
other side. The **ring apophysis is a peripheral traction epiphysis at the rim**, not a
load-bearing epiphysis over the plate (PMID 34362001). Consequences that follow directly:
   - The limb resting zone abuts a vascularised secondary ossification centre; **the vertebral
     resting zone abuts a disc.** Any model in which the SOC is the source of a maintaining signal
     for the resting-zone stem cell niche has no straightforward vertebral counterpart.
   - Nutrient supply to the vertebral physis comes from the vertebral body side; the disc side is
     avascular and shares its nutrient route with the disc through the cartilage endplate
     (PMIDs 42158060, 40725395). **Delivery arithmetic for a limb plate does not transfer.**

**3. THERE ARE ~48 PRESACRAL PHYSES, NOT 4, AND THEY DO NOT CLOSE TOGETHER.** Ring apophysis
maturation runs on a **level-specific and sex-specific schedule**: high-thoracic and low-lumbar
levels fuse earliest, mid-thoracic latest, and around the peak of the growth spurt girls'
mid-thoracic levels are less mature than boys' (PMID 34362001). A single "bone age" from the hand
therefore under-specifies the axial state, which is why a spine-specific index (RAM) and cervical
vertebral maturation staging exist at all (PMIDs 34362001, 41766013).

**4. THERE IS A THIRD GROWTH CENTRE PER VERTEBRA WITH NO LIMB ANALOGUE — THE NEUROCENTRAL
SYNCHONDROSIS.** It is bipolar, it feeds the body, the canal and the posterior elements
simultaneously, and its closure age is region-dependent and reported across a 2–16 year range
(PMIDs 27137907, 39160634, 20042959). The **crankshaft phenomenon** — continued anterior vertebral
growth after posterior-only fusion (PMIDs 42291699, 40691841) — exists precisely because the
anterior and posterior columns are separately-driven growth systems in the axial skeleton and are
not in the limb.

**5. VERTEBRAL PROPORTION IS SET MAINLY BY CELL NUMBER, NOT BY HYPERTROPHY.** In the mouse/jerboa
comparison, cell number drives both limb and vertebral proportion, but **chondrocyte hypertrophy —
the major driver of proportion in all mammalian limbs — is used for vertebral proportion only in
the extreme case** (PMID 41073372). If the largest term in limb elongation is hypertrophic cell
volume, that term may be a **smaller** lever in a vertebra, and pool/cell-number levers
correspondingly **larger**.

**6. THE GENETIC PROGRAMMES OVERLAP ONLY PARTIALLY.** Genes associated with differential vertebral
growth overlap **significantly but not substantially** with genes associated with limb proportion
(PMID 41073372); human skeletal stem cells show **functional diversity across skeletal sites**
(PMID 40118065); and height GWAS signal partitions into skeletal-element-specific and global
variants (PMID 39549696). Sitting-height-ratio GWAS in ~450,000 Europeans and ~100,000 East Asians
found **565 independent SHR loci whose fine-mapped signals are often DISTINCT from height signals**
(PMID 41861830), building on the earlier finding that SHR is 26–39% heritable with SHR-specific
loci including TBX2 and IGFBP3 (PMID 25865494).

**7. THE MECHANICAL ENVIRONMENT IS CATEGORICALLY DIFFERENT — AND HUMAN-SPECIFIC.** The vertebral
physis is loaded through a **fluid-pressurised, osmotically swollen disc**, not through a joint.
Disc pressure, not bone-on-bone contact, is what a tether or brace changes — which is why FEA of
vertebral growth modulation is expressed in terms of disc height and physeal stress distribution
(PMIDs 40836185, 41041616), and why moving the centre of rotation *posteriorly* preserves disc
height and **promotes** growth while an anterior centre of rotation inhibits it. Human bipedalism
means quadruped vertebral loading results transfer poorly (PMIDs 41900984, 40866708) — and the
scoliosis field's standard oestrogen model is a *bipedal* rat for exactly this reason
(PMID 30405118).

**8. THE VERTEBRAL PLATE HAS ITS OWN MECHANOTRANSDUCTION PATHOLOGY.** Compressive stress →
**PIEZO1 up → GPX4 down → ferroptosis in vertebral growth-plate chondrocytes → pathological
ossification** (PMID 40714837), with a parallel PIEZO1–primary cilium arm (PMID 41194970). The
same channel in the limb plate is generally discussed in terms of endochondral ossification and
osteoarthritis, not ferroptotic loss of a physis.

**9. A NON-PHYSEAL HEIGHT COMPONENT EXISTS ONLY IN THE AXIAL SKELETON.** ~23 intervertebral discs
contribute height by **osmotic swelling against load**, set by nucleus pulposus fixed charge
density (PMID 39892283), and they never "fuse". This component is reversible within a day
(PMID 39568059), responds to unloading within days (PMID 32466473), and can be increased by
sustained tension in a growing animal (PMID 40179155). **No limb bone has an equivalent.**

**10. GROWTH-PLATE CLOSURE IN THE AXIAL SKELETON RUNS LATER.** See PROSE 3.

**11. THE AXIAL SKELETON IS SEPARATELY DESTRUCTIBLE.** Craniospinal irradiation halves the GH
growth response relative to cranial-only irradiation (PMID 32706856); a fused thoracic spine before
age 7 causes thoracic insufficiency (PMID 24147251). The axial reserve can be lost without the
appendicular reserve being touched.

**12. WHOLE CLASSES OF DISEASE ARE AXIAL-ONLY.** Spondylocostal and spondylothoracic dysostosis
produce short trunk **with normal limbs** from segmentation-clock failure (PMIDs 37038048,
39836964); dyssegmental dysplasia produces vertebrae of unequal size (anisospondyly)
(PMID 38424183). The mirror set — SHOX/Léri-Weill/Turner (limb-selective shortening) and Marfan
(limb-selective lengthening) — completes the demonstration that the two compartments are
independently addressable in humans.

---

## PROSE 3 — HOW LATE DOES AXIAL GROWTH ACTUALLY RUN, WITH NUMBERS

**The proportion data say the residual is trunk-weighted, and this is a population-scale result.**
In 9,569 US children aged 2–18 (NHANES III), the sitting-height-to-standing-height ratio
**falls from prepuberty into early puberty and rises again in late puberty, in both sexes**
(PMID 32579888). The fall is legs outgrowing trunk; the rise is trunk still growing after the legs
have largely stopped. This is the single cleanest population confirmation that **late-pubertal
residual growth is axial**.

**The spine finishes later than total height.** In a longitudinal cohort of 54 normal children
followed to maturity: **at PHV90% (the point at which 90% of final height is achieved), children
were 90% of adult TOTAL height but only 87% of adult SPINE height** (PMID 39585607). That 3-point
gap is the arithmetic statement that the last of growth is disproportionately spine.

**Spinal growth velocity, normal children (PMID 39585607):**
- Childhood: **1.55 ± 0.21 cm/yr (girls), 1.14 ± 0.23 cm/yr (boys)**
- Growth spurt: **1.75 ± 0.11 cm/yr (girls), 2.00 ± 0.11 cm/yr (boys)**
The paper also supplies multipliers of remaining spinal growth indexed to timing relative to
PHV90%/Peak Growth Age, which is the axial analogue of a limb-length multiplier method.

**Thoracic spine specifically, re-measured on CT in 144 children without deformity
(PMID 28609322):**
- 1–4 y: **1.71 cm/yr** · 4–8 y: **0.55** · 8–10 y: **0.74** · 10–12 y: **0.69** ·
  **12–16 y: 1.61 cm/yr**
Two break points — end of the 4th year and beginning of the 12th. **The adolescent thoracic growth
rate (1.61 cm/yr from 12 to 16) is nearly as high as the infantile rate**, and it runs to 16.

**Classical (Dimeglio) figures, quoted from the original author's own review (PMID 24147251,
INDEX; also 21874626):** T1–S1 ≈**18 cm at birth → ≈45 cm at maturity**, i.e. ≈27 cm of axial
growth; T1–S1 is ≈**49% of sitting height at maturity**, two-thirds thoracic and one-third lumbar;
thoracic spine ≈1.3 cm/yr birth–5 y, ≈0.7 cm/yr 5–10 y, ≈1.1 cm/yr in puberty; T1–S1 phase rates
≈2 cm/yr, then 1 cm/yr, then 1.8 cm/yr. ⚠ These are secondary-source numbers and the CT
re-measurement above (PMID 28609322) explicitly argues the fastest phase is confined to a younger
age group than the classical curve implies.

**Axial maturity markers run into the third decade.** Cervical vertebral maturation staged with
spheno-occipital synchondrosis fusion is used as a **forensic age-estimation framework in living
adults** (PMID 41766013), and spheno-occipital synchondrosis fusion staging is itself a validated
maturity indicator with its own systematic review and meta-analysis (PMID 40464024). The ring
apophysis correlates with age at R=0.892 and its **mid-thoracic levels fuse last** (PMID 34362001).
⚠ These are **peripheral rim/synchondrosis maturity markers, not measurements of remaining
vertebral body growth** — a late-maturing marker is evidence the axial skeleton matures late, not
a guarantee of remaining height.

**The disc component runs on a different, non-fusing clock.** Disc height responds to unloading in
**5 days** in humans (dry immersion, PMID 32466473), varies by **−1.0 mm (T11→L4 alone) over a
single day in children** (PMID 39568059), and can be increased by sustained tension in a growing
mouse (PMID 40179155). Against that, rapid pubertal trunk growth is itself a risk factor for disc
degeneration: **OR 7.92 (1.19–52.7) for Pfirrmann ≥3 at age 18 per additional 10% increase in
sitting height between 11 and 18** (PMID 39332689). Beyond growth, **kyphotic angle increases
2.42° and lordotic angle 1.48° per decade of adult life** in 41,212 UK Biobank participants
(PMID 40652108) — a curvature-driven loss of *measured* trunk height that begins long before any
disc height is lost.

**And the trunk:leg partition is environmentally plastic within a population.** In 20,336 Japanese
subjects the Cormic index (sitting height / standing height) rose to 1942, fell to a nadir in the
1970s, then rose again to 1995, and **nearly half the deviation of spirometric values from European
reference equations was explained by these cohort differences in body frame** (PMID 25254426).
Relative leg length is the classically environment-sensitive component; the trunk is the more
canalised one.

---

## WHAT I COULD NOT VERIFY

1. **The exact fraction of standing height contributed by the intervertebral discs.** ~20–25% is
   widely repeated; I did not retrieve a primary measurement. Marked UNVERIFIED (row B1).
2. **The age at which discal height growth ceases.** The scoliosis stereoradiographic literature
   is the standard source for a near-zero discal growth contribution after early adolescence, and I
   could not retrieve the primary in this search (row B8). This is a load-bearing number for the
   trunk question and should be chased.
3. **Spheno-ethmoidal synchondrosis fusion age** — no primary retrieved (row C4). Every search
   returned spheno-occipital work instead.
4. **Head height as a percentage of standing height, and the age at which it is fixed** (row C5).
5. **Sacral segment fusion ages** (row C1) — I retrieved morphology and anomaly papers, not a
   fusion-timing series.
6. ✅ **RESOLVED DURING THIS ROUND.** TYRA-300 (40178985) states that it **increased lumbar
   vertebrae length**, and the Fgfr3 −29E enhancer deletion (39817451) states that it **largely
   normalized vertebral body growth**. Both are now Tier-1b rows. **What remains unverified is
   the magnitude** (the numbers are in the figures, not the abstracts) and whether **infigratinib
   (27064282)** has an equivalent vertebral measurement.
7. **Whether vosoritide in hypochondroplasia (38813446) reported a proportion endpoint** (row G22).
8. **Whether the Humanin DMD study (41550496) or the paediatric PTH 1-34 study (39883563) measured
   a vertebral length** (rows G27, G23).
9. **A quantitative Cobb-angle-to-height-loss formula** (row H9) — widely used clinically, no
   primary retrieved.
10. **Astronaut stature/spine lengthening in centimetres.** Every search returned disc height,
    paraspinal muscle and low-back-pain outcomes (27779600, 39660277) rather than a stature figure.
11. **A specific PMID for EOS biplanar radiography of spine length** (row H18).
12. **PMC11847212** ("Spinal sagittal and coronal morphology characteristics in children with short
    stature", Quant Imaging Med Surg 2025) returned a PMCID but no PMID through the API (row H17).
13. **Europe PMC returned intermittent 502/503/504 errors** during two batches; those queries were
    retried and completed, but I cannot exclude that a few results were lost to transient failures.
14. **Paywalled/abstract-only throughout.** All numbers above come from abstracts or freely
    available full text. Where a figure exists only in a figure panel (e.g. exact vertebral lengths
    in 41073372, exact reshaping percentages in 37843393) I have not quoted it.
15. **I did not verify the classical Dimeglio primary monograph**; row H6 is explicitly flagged as
    a secondary-source quotation, and PMID 28609322 partially contradicts it.

---

### ROW COUNT
**174 rows** — A (vertebral body & growth centres) 18 · B (intervertebral disc) 24 ·
C (other axial segments & skull base) 10 · D (development, segmentation, axial identity) 31 ·
E (axial-selective dysplasias & natural experiments) 20 · F (mechanical & device modulation) 21 ·
G (agents with an axial endpoint) 31 · H (measurement & confounds) 19.
**122 rows marked OBSCURE (70%).** The high obscure fraction is itself the result: the axial
skeleton is enumerated almost entirely outside the mainstream growth-pharmacology literature — it
lives in paediatric spine surgery, forensic age estimation, developmental somitogenesis, and the
disc-degeneration field, none of which talks to the other three or to endocrinology.
