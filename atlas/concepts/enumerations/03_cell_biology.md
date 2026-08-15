# DOMAIN 03 — GROWTH PLATE CELL BIOLOGY: COMPLETE PARTS LIST (R436 enumeration)

**Method.** Every row below was reached by EXTERNAL search only — Europe PMC REST API
(`/europepmc/webservices/rest/search`) and NCBI eutils, plus targeted web search. No file in
`/home/user/growth-plate` was read except the two briefs. PMIDs are copied verbatim from the API
response; where a record returned no PMID (preprint / non-indexed) the row says `UNVERIFIED-PMID`
and names the venue instead. Species is stated for every claim. Reviews are flagged as INDEX.

**Reading the OBSCURE column.** `yes` = the item is rarely or never discussed in the mainstream
human-growth / short-stature literature, even where a substantial cell-biology literature exists.
Those rows are the high-value ones.

**Counts.** **149 rows** — A cell types 30 · B transitions 30 · C structure 17 · D processes 37 ·
E fusion 20 · F comparative/extreme 15. **106 marked OBSCURE = yes**, 43 = no. **181 unique PMIDs**
cited. **PMID verification:** 154 of the 181 were re-resolved through NCBI esummary and every one
returned the title claimed here; no citation in this file failed verification.

---

## TABLE

| # | CELL TYPE / PROCESS / STRUCTURE | ROLE IN LENGTH | EVIDENCE (species + PMID) | REGULATORS | OBSCURE? |
|---|---|---|---|---|---|

### A. CELL TYPES IN AND AROUND THE PLATE

| A1 | **Resting / reserve zone chondrocyte** | The pool. Sets how long the plate can run; depletion is the proximate cause of senescence and fusion | rabbit, PMID 16614378 (depletion of resting zone chondrocytes during growth plate senescence); rabbit, PMID 24708243 (oestrogen hastens fusion by irreversibly depleting resting-zone progenitor number) | oestrogen; Wnt tone; hedgehog; mTORC1 | no |
| A2 | **Epiphyseal skeletal stem cell (ESSC) / PTHrP+ resting cell** | Self-renewing stem cell that forms the columns; acquired at SOC formation | mouse, PMID 30401834 (resting zone houses a unique class of skeletal stem cells, Nature) ; review INDEX PMID 41096725 (growth-plate skeletal stem cells and the niche) | hedgehog, PTHrP, Wnt-low niche | no |
| A3 | **Wnt-inhibitory resting-zone niche** | Resting cells are held in a LOW canonical-Wnt environment; that state is what keeps them slow-cycling | mouse, PMID 34309509 (eLife: chondrocytes in the resting zone are maintained in a Wnt-inhibitory environment) | secreted Wnt antagonists | no |
| A4 | **ApoE+ resting chondrocyte (pan-RZ marker)** | Newly proposed marker of ALL resting-zone chondrocytes — i.e. the RZ may be one population, not a rare stem cell plus bulk | mouse, PMID 40025030 (Bone Res: apolipoprotein E is a marker of all chondrocytes in the growth plate resting zone) | UNVERIFIED | **yes** |
| A5 | **Human RZ quiescent sub-populations** | Human tissue evidence that the RZ contains sub-populations with quiescent-stem features — the human counterpart of A2 | human, preprint/record without PMID in EPMC ("Human growth plates house resting zone sub-populations with features of quiescent stem cells", 2025) — `UNVERIFIED-PMID` | UNVERIFIED | **yes** |
| A6 | **Proliferative (columnar/flat) chondrocyte** | Generates cell number; one of the two multiplicands of yield | mouse, PMID 39269144 (eLife: limited column formation in the embryonic plate — pre- vs postnatal growth mechanisms differ) | FGFR3, CNP, IGF-1, PTHrP/Ihh loop | no |
| A7 | **Prehypertrophic chondrocyte** | Commitment step; the Ihh source and the PTHrP-loop receiver | mouse, review INDEX PMID 36980807 (local soluble factors maintaining the growth plate) | Ihh, PTH1R, RUNX2, MEF2C | no |
| A8 | **Hypertrophic chondrocyte** | Volume increase is the largest single contributor to elongation | multi-species, review INDEX PMID 34137454 ("The hypertrophic chondrocyte: to be or not to be"); PMID 37485234 (hypertrophic chondrocytes at the junction of musculoskeletal structures) | RUNX2, MEF2C, HDAC4, SOX9 withdrawal | no |
| A9 | **Terminal hypertrophic chondrocyte** | The cell that is either cleared or converted; the discharge step | mouse, PMID 34805821 (Runx2 required for hypertrophic-chondrocyte-mediated degradation of cartilage matrix) | RUNX2, MMP13, VEGFA | no |
| A10 | **Seven morphological subphases of the growth-plate chondrocyte** | Confocal thick-section work resolves SEVEN subphases, not the textbook 3–4 zones — the standard zonal model under-resolves the trajectory | UNVERIFIED species (mammalian growth plate), PMID 32332842 (Sci Rep: a simple method based on confocal microscopy recognises seven subphases in growth plate chondrocytes) | — | **yes** |
| A11 | **"Light vs dark" chondrocytes** | A classical morphological dichotomy still being re-examined; possible metabolic/secretory states rather than lineage | veterinary/comparative, PMID 40494256 (Res Vet Sci 2025: light vs dark chondrocytes and their possible role in endochondral ossification) | — | **yes** |
| A12 | **Borderline chondrocyte (plate periphery)** | Peripheral cells behaving as transient mesenchymal precursors; a lateral exit route from the plate feeding metaphyseal stroma | mouse, PMID 30888720 (JBMR 2019: growth plate borderline chondrocytes behave as transient mesenchymal precursor cells); mouse, PMID 31329317 (JBMR 2019: a new source of metaphyseal mesenchymal precursors) | — | **yes** |
| A13 | **Groove of Ranvier progenitor** | Circumferential/latitudinal growth and a lateral progenitor reservoir feeding the plate | mouse, PMID 36443296 (Nat Commun: the fate of early perichondrial cells in developing bones); PMID 41253754 (Gli1+ stromal cells are reparative precursors of long-lived chondroprogenitors, fetal murine limb) | Gli1, hedgehog, BMP | **yes** |
| A14 | **Perichondrial ring of LaCroix** | Mechanical hoop restraint around the plate AND a cell reservoir; failure is a physeal-fracture / slip determinant | chick, PMID 16652202 (Int Orthop 2006: the perichondrial ring as a reservoir for precartilaginous cells, in vivo young chick epiphysis); human clinical INDEX PMID 33995857 (management of physeal fractures) | mechanical | **yes** |
| A15 | **Perichondrium layers (distinct progenitor pools)** | Different perichondrial LAYERS have different progenitor identity and different tumour potential — the perichondrium is not one compartment | mouse, PMID 42070715 (Bone 2026: progenitors from distinct perichondrium layers initiate tumour formation in hereditary multiple osteochondromas) | BMP; EXT1/EXT2 | **yes** |
| A16 | **Osteoblast (metaphyseal / primary spongiosa)** | Consumes the cartilage template; does not itself set length but sets what the length is made of | mouse, PMID 41663374 (Bone Res 2026: modelling the chondrocyte-derived osteoblast formation process) | RUNX2, SP7, Wnt | no |
| A17 | **Osteoclast at the chondro-osseous junction** | Resorption of the last septa; blocking it JAMS the plate rather than preserving it | mouse, PMID 42157948 (Int J Biol Sci 2026: Piezo1 in hypertrophic chondrocytes regulates osteoclastogenesis in endochondral ossification) | RANKL/OPG, CSF1, Piezo1 | no |
| A18 | **Chondroclast (distinct from osteoclast)** | Transcriptionally distinct catabolic cell acting on cartilage rather than bone | comparative transcriptomics, PMID 32650826 (Arthritis Res Ther: distinct molecular signatures and regulatory networks of chondroclasts vs osteoclasts) ; review INDEX PMID 26818783 ("the cast of clasts") | RANKL; MMP9; CTSK | **yes** |
| A19 | **Septoclast** | Perivascular cell that digests the LAST transverse septum, permitting vascular invasion — the physical gatekeeper of discharge. ⭐ **AND IT HAS A LENGTH ENDPOINT: the sEH inhibitor TPPU raised septoclast activity (MMP9, FABP5) and PROMOTED LONG-BONE GROWTH in newborn mice via endothelial→mesenchymal NOTCH (PMID 42297360, Cell Prolif 2026)** | mouse, PMID 35091558 (Nat Commun: mesenchymal stromal cell-derived septoclasts resorb cartilage during developmental ossification and fracture healing); mouse, PMID 40387924 (ETS1 drives Ctsb/Mmp13 during septoclast differentiation from pericytes); mouse, PMID 41319243 (J Anat 2026: perichondrium origin of the pericyte–septoclast lineage) | ETS1, CTSB, MMP13, retinoic acid (PMID 28500502), Notch (PMID 42297360) | **yes** |
| A20 | **Endothelial cell acting as a chondroclast** | Endothelium itself can resorb cartilage — reassigns part of the "clast" job away from the myeloid lineage | mouse, PMID 30936470 (Nat Cell Biol: endothelial cells revealed as chondroclasts) | VEGF; MMPs | **yes** |
| A21 | **Type H vessel endothelium (CD31hi EMCNhi)** | Metaphyseal vessel subtype that couples angiogenesis to osteogenesis at the invasion front | mouse, review INDEX PMID 38353470 (targeting type H vessels in bone-related diseases) | HIF-1α, VEGF, Notch, SLIT3, PDGF-BB | no |
| A22 | **Pericyte (metaphyseal)** | Source of septoclasts; vessel stabilisation at the invasion front | mouse, PMID 40387924; mouse, PMID 39524152 (FOXO1–mTOR in vascular pericytes controls type H vessel formation) | FOXO1, mTOR, PDGFRβ | **yes** |
| A23 | **Cartilage canal (epiphyseal vascular channel)** | Carries vessels into epiphyseal cartilage; its failure is the lesion of osteochondrosis and it seeds the SOC | pig, PMID 37431760 / PMID 35716161 (osteochondrosis lesions arise at cartilage canals); human, PMID 31442281 (morphogenesis of the human femur) | VEGF; mechanical | **yes** |
| A24 | **Periarticular mesenchymal progenitor (SOC initiator)** | Initiates and contributes to the secondary ossification centre — the SOC is not simply "the plate turning to bone" | mouse, PMID 30681752 (Stem Cells: periarticular mesenchymal progenitors initiate and contribute to SOC formation) | UNVERIFIED | **yes** |
| A25 | **Bone-marrow lymphatic vessel** | Lymphatics exist in bone and expand to support regeneration — an almost entirely unexamined compartment for growth | mouse, PMID 36669473 (Cell: lymphatic vessels in bone support regeneration after injury) | VEGF-C/VEGFR3; CXCL12 | **yes** |
| A26 | **Sensory (somatosensory) nerve at the physis** | Nerves drive pathological bony-bar formation after physeal injury — first causal nerve→physis link | mouse, PMID 42555751 (Sci Transl Med 2026: somatosensory nerves drive pathologic bony bar formation through pleiotrophin) | pleiotrophin (PTN); NGF/TrkA | **yes** |
| A27 | **Osteal macrophage / osteomac** | Resident macrophage at the bone surface and marrow; isolation protocols now exist for human | human, PMID 41900896 (Life 2026: isolation of human osteal macrophages) | CSF1R | **yes** |
| A28 | **Marrow stromal / mesenchymal progenitor of the metaphysis** | Receives the chondrocyte-derived lineage; the destination compartment | mouse, review INDEX PMID 37301964 (emerging studies on mesenchymal progenitors in the long bone) | PDGFRα, LEPR, Gli1 | no |
| A29 | **Marrow adipocyte** | Competing fate for the same stromal pool; expands where bone formation contracts | review INDEX PMID 38275607 (pericytes as orchestrators of vasculature and adipogenesis) | PPARγ | **yes** for growth |
| A30 | **Growth-plate immune cells / IL-6 axis** | Systemic inflammatory tone acting locally on the plate; a recognised paediatric growth-disorder axis | review INDEX PMID 42312209 (Front Endocrinol 2026: stress-induced IL-6 regulation in paediatric bone growth disorders) | IL-6, TNF, IL-1β | no |

### B. STATE TRANSITIONS AND THEIR REGULATORS

| # | CELL TYPE / PROCESS / STRUCTURE | ROLE IN LENGTH | EVIDENCE (species + PMID) | REGULATORS | OBSCURE? |
|---|---|---|---|---|---|
| B1 | **Quiescence entry / exit of the resting cell** | The rate-limiting step for pool preservation. A 2026 systematic review argues "quiescence" in the RZ is asserted more than demonstrated | mouse+human, systematic review INDEX PMID 41795828 (Stem Cells 2026: "Quiescence" in the resting zone of the growth plate: a systematic review) | Wnt-low niche; hedgehog; nutrient state | **yes** (the *review's* sceptical conclusion is obscure) |
| B2 | **Metabolic proliferation→quiescence transition (FLIM-measured)** | Chondrocytes switch metabolic state as they become quiescent; measurable label-free in intact joints | mouse, PMID 42186485 (J Tissue Eng 2026: chondrocyte metabolic transition from proliferation to quiescence revealed by FLIM in postnatal knee) | NAD(P)H redox state | **yes** |
| B3 | **Reduced glycolysis as the resting-cell state** | Lowering glycolytic flux is proposed to be what keeps RZ cells slow-cycling — a metabolic, not signalling, control of the pool | mouse, `UNVERIFIED-PMID` (EPMC record 2023 "Reduced glycolysis links resting zone chondrocyte proliferation in the growth plate", no PMID returned — preprint) | LDHA/ACLY; acetyl-CoA; histone acetylation | **yes** |
| B4 | **Nutrient-regulated chondroprogenitor dynamics** | Dietary/nutrient state directly moves progenitor number in the postnatal plate | mouse, PMID 37080994 (Bone Res 2023: nutrient-regulated dynamics of chondroprogenitors in the postnatal murine growth plate) | IGF-1/PI3K/Akt; feeding state | no |
| B5 | **Growth hormone acting ON the stem-cell population** | GH does not only raise throughput — it changes the composition of the stem pool | mouse, PMID 41289405 (PNAS 2025: growth hormone regulates the stem cell population in the growth plate) | GHR/JAK2/STAT5 | **yes** |
| B6 | **Hedgehog-driven "transient clonal competency"** | Hh activation makes RZ cells transiently able to form clones AND biases them to osteogenic fate — a dose/timing-dependent switch | mouse, PMID 38051593 (JCI Insight 2024: hedgehog activation promotes osteogenic fates of RZ chondrocytes through transient clonal competency) | SMO, GLI, PTCH1 | no |
| B7 | **FGFR3-driven failure of RZ turnover via CREB** | Achondroplasia is (in part) a resting-zone TURNOVER defect, not only a proliferation defect | mouse, PMID 41748604 (Nat Commun 2026: excess FGFR3 signalling disrupts turnover of resting zone chondrocytes via CREB) | FGFR3→CREB | no |
| B8 | **Clonal column formation (oriented division + rearrangement)** | Converts one stem division into many stacked cells — the amplification term | mouse, PMID 28994649 (eLife 2017: PCP signalling coordinates oriented cell division and cell rearrangement in clonally expanding growth plate cartilage) | WNT5A, VANGL2, PRICKLE, ROR2 | no |
| B9 | **Column formation is POSTNATAL, not embryonic** | Embryonic elongation occurs largely WITHOUT columns — so pre- and postnatal growth use different mechanisms and embryonic models may not transfer | mouse, PMID 39269144 (eLife 2024: limited column formation in the embryonic growth plate implies divergent growth mechanisms) | — | **yes** |
| B10 | **Cell-adhesion-dependent column architecture (N-cadherin + β1 integrin)** | Physical mechanism of stacking; loss disorganises the plate | mouse, PMID 38294852 (Mol Biol Cell 2024: N-cadherin and β1 integrin coordinately regulate growth plate cartilage architecture); PMID 24764078 (Development 2014: a dynamic cell adhesion surface regulates tissue architecture) | CDH2, ITGB1, RAC1 | **yes** |
| B11 | **α-parvin / focal-adhesion control of column formation** | An IPP-complex component required for columns and for long-bone length | mouse, PMID 37607905 (Bone Res 2023: α-parvin controls chondrocyte column formation and regulates long bone development) | PARVA, ILK, PINCH | **yes** |
| B12 | **Morphological sequence of chondrocyte shape change (3D MAPs)** | Whole-plate single-cell morphometrics defines the actual shape trajectory; GDF5 regulates it | mouse, PMID 34508093 (Nat Commun 2021: 3D MAPs pipeline identifies the morphological sequence chondrocytes undergo and the regulatory role of GDF5) | GDF5 | **yes** |
| B13 | **Commitment to prehypertrophic (PTHrP–Ihh loop)** | Sets WHERE along the column a cell leaves the proliferative pool — i.e. column length | mouse, PMID 40088130 (Dev Dyn 2025: PTHrP/Ihh feedback loop and the unusual growth plate location in mammalian metatarsals and pisiforms) | PTHrP, IHH, PTH1R, GLI3 | no |
| B14 | **Hypertrophy phase 1–3 (volume increase)** | The dominant contributor to elongation rate; distinct phases with distinct machinery | multi-species, review INDEX PMID 34137454; mechanobiology review INDEX PMID 42317771 (2026) | mTORC1, IGF-1, SOX9 withdrawal, ion/water flux | no |
| B15 | **Terminal differentiation → matrix degradation** | RUNX2-dependent; the hypertrophic cell digests its own septa | mouse, PMID 34805821 (Runx2 required for hypertrophic-chondrocyte-mediated cartilage matrix degradation) | RUNX2, MMP13, MMP9 | no |
| B16 | **Apoptosis of the terminal hypertrophic cell** | Classical model of clearance; now known to be only part of the story | mouse, review INDEX PMID 27929439 (cell death in chondrocytes, osteoblasts and osteocytes); mouse, PMID 31848143 (Prmt5 mutant, terminal hypertrophic differentiation) | caspases; phosphate; PRMT5 | no |
| B17 | **TRANSDIFFERENTIATION of hypertrophic chondrocyte → osteoblast (CONTESTED)** | If real, a large fraction of metaphyseal osteoblasts are ex-chondrocytes; changes what "discharge" means | mouse, PMID 33253203 (PLoS Genet 2020: Runx2 essential for chondrocyte→osteoblast transdifferentiation); mouse, PMID 31121357 (persistent Sox9 SUPPRESSES transdifferentiation); modelling PMID 41663374 (Bone Res 2026) | RUNX2, SOX9 withdrawal, β-catenin, KDM6A (PMID 42212366), NF-κB (PMID 34934622), PRG4 (PMID 40973917) | no (but the DEBATE is under-reported) |
| B18 | **Descendants of hypertrophic chondrocytes secreting THBS4 to drive angiogenesis** | The ex-chondrocyte is not passive — it actively recruits vessels | mouse, PMID 41207902 (Bone Res 2025: descendants of hypertrophic chondrocytes promote angiogenesis by secreting THBS4 during bone growth and injury repair) | THBS4 | **yes** |
| B19 | **Autophagy in growth-plate chondrocytes** | Survival of the hypoxic, avascular, high-secretory-load cell; loss shortens bone | mouse/broiler, see PMID 40331700 (ER stress and endochondral ossification in broilers) and review INDEX PMID 42003749 | ATG genes, mTOR, FOXO3 | no |
| B20 | **Dedifferentiation / re-entry to a progenitor state** | Would allow the pool to be replenished rather than only spent; demonstrated in fracture and in vitro but NOT in a normal plate | mouse, review INDEX PMID 42098082 (Chin Med J 2026: chondrocytes in fracture healing); PMID 40660304 (calcium–MYC axis blocks early chondrocyte dedifferentiation) | MYC, Ca2+, retinoic acid | **yes** |
| B21 | **Borderline chondrocyte → metaphyseal mesenchymal precursor** | A lateral exit route from the plate feeding metaphyseal stroma | mouse, PMID 30888720 (JBMR 2019: growth plate borderline chondrocytes behave as transient mesenchymal precursor cells); PMID 31329317 (JBMR 2019: a new source of metaphyseal mesenchymal precursors) | — | **yes** |
| B22 | **Growth-plate senescence (division-counted, not time-counted)** | The programme that ends growth; oestrogen accelerates rather than initiates it | rabbit, PMID 16614378; rabbit, PMID 24708243; review INDEX PMID 21865751 (growth plate senescence and catch-up growth) | oestrogen, division number, glucocorticoid | no |
| B23 | **Differential aging BETWEEN plates sets proportion** | Plates in different bones senesce at different rates — that is what makes the skeleton the shape it is | mouse, PMID 30036371 (PLoS Biol 2018: differential aging of growth plate cartilage underlies differences in bone length and helps determine skeletal proportions) | — | **yes** |
| B24 | **Retinoid suppression of chondrocyte identity** | RA signalling actively removes chondrocyte identity — a switch, not a modifier | UNVERIFIED species, `UNVERIFIED-PMID` (EPMC 2024 record "Retinoic acid signaling suppresses chondrocyte identity during cartilage development and regeneration", no PMID returned) ; and PMID 40714875 (a retinoid ANTAGONIST attenuates growth inhibition after physeal injury, mouse) | RARγ, CYP26 | **yes** |
| B25 | **Ferroptosis of growth-plate chondrocytes** | An iron/lipid-peroxidation death mode distinct from apoptosis, implicated in mechanically-driven plate failure | rodent, PMID 40714837 (Adv Sci 2025: PIEZO1–GPX4 axis mediates mechanical-stress-induced vertebral growth plate dysplasia via ferroptosis) | GPX4, PIEZO1, SLC7A11 | **yes** |
| B26 | **Chondrocyte pentose-phosphate pathway → oxidative protein folding** | Links metabolism directly to secretory capacity and to ferroptosis resistance | mouse, PMID 39794539 (Nat Metab 2025: the pentose phosphate pathway controls oxidative protein folding and prevents ferroptosis in chondrocytes) | G6PD, NADPH | **yes** |
| B27 | **Lipid metabolism control in chondrocytes** | Directly required for skeletal growth — a metabolic input largely absent from the growth literature | mouse, PMID 42224593 (PNAS 2026: control of lipid metabolism in chondrocytes is critical for skeletal growth) | UNVERIFIED (see paper) | **yes** |
| B28 | **NAD salvage pathway in mesenchymal cells** | Indispensable for skeletal development — NAMPT-dependent | mouse, PMID 37330524 (Nat Commun 2023: the NAD salvage pathway in mesenchymal cells is indispensable for skeletal development) | NAMPT | **yes** |
| B29 | **Histone lactylation under intermittent hypoxia** | Metabolite→chromatin route by which a systemic condition (sleep apnoea) shortens long bones | rodent, PMID 40722170 (J Transl Med 2025: chronic intermittent hypoxia impairs BM-MSC osteogenesis and long bone growth through histone lactylation) | lactate, LDHA, p300 | **yes** |
| B30 | **Senescent-cell clearance in the growing skeleton** | Epigenetic targeting of senescent cells prevents skeletal harm from obstructive sleep apnoea — a senolytic-adjacent result in a GROWING animal | rodent, PMID 41387208 (Adv Sci 2026: epigenetic targeting of senescent cells prevents deleterious effects of obstructive sleep apnoea on growing skeleton) | UNVERIFIED | **yes** |

### C. STRUCTURE AND GEOMETRY

| # | CELL TYPE / PROCESS / STRUCTURE | ROLE IN LENGTH | EVIDENCE (species + PMID) | REGULATORS | OBSCURE? |
|---|---|---|---|---|---|
| C1 | **Zone heights (RZ/PZ/PHZ/HZ)** | The standard readout; but height is not the same as flux and a taller zone can mean a jam | multi-species, methods PMID 41836565 (J Orthop Translat 2026: spatially resolved single-cell-based histocytomorphometry for growth plate analysis across multiple species) | — | no |
| C2 | **Cells per column (amplification)** | Divisions per stem cell before commitment; distinct from proliferation RATE | mouse, PMID 39269144; PMID 28994649 | PCP; residence time | **yes** |
| C3 | **Clonal architecture (monoclonal vs polyclonal columns)** | Whether a column is one clone determines whether the RZ is a true stem compartment | mouse, PMID 30401834; PMID 39269144 (embryonic columns are NOT clonal in the same way) | — | no |
| C4 | **Longitudinal septa / transverse septa** | The matrix scaffold that must be dissolved for discharge; transverse septum removal is the septoclast's job | mouse, PMID 35091558; PMID 36602038 (J Anat 2023: integrin expression and ECM adhesion of septoclasts, pericytes and endothelial cells at the chondro-osseous junction) | MMP9/13, CTSB, CTSK | **yes** |
| C5 | **Chondro-osseous junction (the discharge interface)** | Where cartilage becomes bone; the physical rate-limiter for the whole plate | mouse, PMID 38480819 (Commun Biol 2024: endothelial SMAD1/5 couples angiogenesis to osteogenesis in juvenile bone); PMID 39911634 (periostin/osteopontin-null callus COJ abnormalities) | VEGFA, MMP9, SMAD1/5, POSTN, SPP1 | no |
| C6 | **Secondary ossification centre** | Creates the stem-cell niche; before it forms the plate behaves differently (no self-renewal) | mouse, PMID 30681752 (periarticular progenitors initiate SOC); computational PMID 39549120 (timing of RZ PTHrP expression affects plate maintenance during SOC formation) | VEGF, hedgehog, mechanical | no |
| C7 | **Primary spongiosa** | The bone made from the template; a readout of discharge, not of elongation | mouse, PMID 42157948; methods PMID 41087406 (deep-learning trabecular compartment analysis, mouse tibia) | osteoclast/osteoblast balance | no |
| C8 | **Cartilage canals** | Vascular entry into epiphyseal cartilage; failure = osteochondrosis; also the SOC seed | pig, PMID 37431760; pig, PMID 35716161; pig imaging PMID 40783804 | VEGF; mechanical | **yes** |
| C9 | **Physical/chemical niche gradients across the HUMAN plate** | Stiffness and chemistry gradients that polarise development — measured in human tissue | human, PMID 40781081 (Nat Commun 2025: physical and chemical niche of human growth plate for polarized bone development) | matrix stiffness, ion gradients | **yes** |
| C10 | **Pericellular matrix / chondron** | The mechanical transducer immediately around each chondrocyte; sets what force the cell actually feels | mouse/human, PMID 40315311 (Sci Adv 2025: development of the mechanoresponsive pericellular matrix of chondrons); PMID 39956307 (MMPs accelerate PCM breakdown and disrupt mechanotransduction) | COL6, perlecan/HSPG2, MMP2/3/7 | **yes** |
| C11 | **Vertebral (axial) growth plate / endplate** | Produces the trunk; mechanically loaded differently and biologically distinct from long bone | rodent, PMID 40714837 (vertebral growth plate dysplasia via PIEZO1–GPX4); rodent, PMID 42082502 (simulated microgravity rescues PIEZO1-driven growth plate ossification, AIS model) | PIEZO1, GPX4, mechanical load | **yes** |
| C12 | **Ring apophysis (vertebral)** | Peripheral vertebral growth centre; matures very late (into the third decade) and is DELAYED in adolescent idiopathic scoliosis | human, PMID 38849690 (Spine Deform 2024: maturation of the vertebral ring apophysis is delayed in girls with AIS); human MRI PMID 42084790 (cervical ring apophysis maturation, legal age thresholds) | — | **yes** |
| C13 | **Synchondrosis (cranial base) as a bidirectional plate** | A growth plate with two mirror-image halves — a natural experiment in plate geometry | mouse, PMID 40442075 (Bone Res 2025: RUNX2 essential for maintaining synchondrosis chondrocytes and cranial base growth); PMID 40854917 (HIF-1α in spheno-occipital synchondrosis) | RUNX2, HIF-1α, TNAP (PMID 28377728) | **yes** |
| C14 | **Unusual plate LOCATION in metatarsals/pisiform** | Some bones have single-ended or displaced plates — the PTHrP/Ihh loop explains where a plate can sit | mouse, PMID 40088130 (Dev Dyn 2025) | PTHrP/IHH | **yes** |
| C15 | **Perichondrial ring as a precartilaginous reservoir** | In vivo evidence the ring supplies cells to the plate | chick, PMID 16652202 (Int Orthop 2006: the perichondrial ring as a reservoir for precartilaginous cells, in vivo model in young chicks) | — | **yes** |
| C16 | **Physeal shape / undulation (mammillary processes)** | Non-planar geometry resists shear; shape of the proximal femoral plate is implicated in SCFE aetiology | human, PMID 23138967 (Int Orthop: shape of the proximal femoral growth plate in children and its significance in SCFE aetiology) | mechanical | **yes** |
| C17 | **Physeal bar / bony bridge** | The pathological structure that ends growth locally; now shown to be NERVE-driven | mouse, PMID 42555751; swine, PMID 41485130 (physeal allograft transfer for physeal bars — safety/feasibility); mouse, PMID 39033138 (b-series ganglioside depletion prevents limb-length discrepancy after growth plate injury) | pleiotrophin, gangliosides | **yes** |

### D. PHYSICAL AND CELLULAR PROCESSES

| # | CELL TYPE / PROCESS / STRUCTURE | ROLE IN LENGTH | EVIDENCE (species + PMID) | REGULATORS | OBSCURE? |
|---|---|---|---|---|---|
| D1 | **Cell volume regulation / regulatory volume decrease (RVD)** | The machinery that OPPOSES hypertrophic swelling; blocking RVD should in principle enlarge the cell | human/bovine chondrocyte, PMID 25450844 (rate of hypo-osmotic challenge influences RVD); PMID 35130619 (substrate-stiffness-dependent RVD and Ca2+ signalling); PMID 31937149 (volume reduction protects in-situ chondrocytes from impact) | K-Cl cotransporters, TRPV4, Ca2+, substrate stiffness | **yes** |
| D2 | **Regulatory volume INCREASE via NKCC1** | The uptake arm; siRNA against NKCC1 blocks RVI in a chondrocyte line | human chondrocyte line C-20/A4, PMID 21847667 (J Membr Biol 2011: siRNA-mediated inhibition of NKCC1 and regulatory volume increase) | SLC12A2, WNK/SPAK | **yes** |
| D3 | **NHE1 (SLC9A1) + AE2 (SLC4A2) pair across the chondrocyte membrane** | pH/volume handling explicitly framed for LONGITUDINAL BONE GROWTH rather than for cartilage disease | review INDEX PMID 35877910 (Membranes 2022: roles of NHE1 and AE2 across chondrocyte plasma membrane during longitudinal bone growth) | intracellular pH, HCO3− | **yes** |
| D4 | **Na+/K+ ATPase setting bone LENGTH** | A pump whose activity level maps onto bone-length variation between mouse strains — direct length endpoint | mouse, PMID 34970538 (Front Cell Dev Biol 2021: a Na+/K+ ATPase pump regulates chondrocyte differentiation and bone length variation in mice) | ATP1A1/ATP1B | **yes** |
| D5 | **WNK2 and the hyperosmotic-stress response** | Familial-OA WNK2 variants change how chondrocytes handle osmotic stress; the WNK–SPAK–CCC axis is the chondrocyte's volume controller | human, PMID 40592720 (RMD Open 2025: WNK2 variants associated with familial osteoarthritis alter the chondrocyte response to hyperosmotic stress) | WNK2, SPAK/OSR1 | **yes** |
| D6 | **Swelling-activated / acid-sensitive chloride currents (ClC-3, ASOR/PAC)** | The anion arm of volume control; largely characterised in articular not growth-plate chondrocytes | human, PMID 33282866 (acid- and volume-sensitive chloride currents in human chondrocytes); PMID 33383561 (swelling-activated ClC-3 in OUMS-27 chondrocytes) | CLCN3, PACC1 | **yes** |
| D7 | **Aquaporins in chondrocytes** | Water channels — the obvious route for hypertrophic water gain, and essentially unstudied at the physis | human, PMID 38015518 (aquaporin 1-mediated chondrocyte degeneration); PMID 39691700 (miR-181a/b-1 downregulates aquaporin-9 in chondroprogenitors) | AQP1, AQP9 | **yes** |
| D8 | **Primary cilium (structure)** | The organelle in which ALL hedgehog transduction occurs; also a mechanosensor; orientation is a growth-plate variable | mouse review INDEX PMID 41613437 (Fundam Res 2025: primary cilia in growth plates orchestrate long bone development); PMID 30002136 (primary cilia necessary for Prx1-expressing cells to contribute to postnatal skeletogenesis) | IFT88, IFT80, KIF3A, EVC/EVC2 | no |
| D9 | **Cilium ORIENTATION uncoupled from centriole** | Cilia in the growing limb are preferentially oriented — a polarity axis independent of the centriole, i.e. a second polarity system | UNVERIFIED species (growing limb), `UNVERIFIED-PMID` (EPMC 2025 record "Primary cilia in the growing limb are preferentially orientated, uncoupled from centriolar position") | PCP | **yes** |
| D10 | **PIEZO1–cilium mechanotransduction axis** | Compressive stress → PIEZO1 → cilium → plate degeneration/ossification; a mechanical route to premature closure | rodent/human AIS, PMID 41194970 (JOR Spine 2025: PIEZO1–primary cilia axis mediates compressive-stress-induced growth plate degeneration and ossification in AIS) | PIEZO1, IFT88 | **yes** |
| D11 | **Mechanical UNLOADING rescuing PIEZO1-driven closure** | Simulated microgravity reverses PIEZO1-overexpression plate ossification — an unloading experiment with a plate endpoint | rodent, PMID 42082502 (NPJ Microgravity 2026) | PIEZO1; load | **yes** |
| D12 | **TRPV4 mechanosensing** | Skeletal-dysplasia TRPV4 mutations change the chondrocyte's transcriptomic response to LOADING; small-molecule rescue exists | mouse/human, PMID 40019039 (Am J Physiol Cell Physiol 2025: skeletal-dysplasia-causing TRPV4 mutations alter the chondrocyte transcriptomic response to mechanical loading); PMID 41574606 (JCI Insight 2026: small-molecule inhibition rescues the skeletal dysplasia phenotype of Trpv4 mutant mice) | TRPV4 | no |
| D13 | **PIEZO modulation by L-type / T-type voltage-sensitive channels** | The mechanosensor's gain is set by other channels — a tuning layer nobody works on for growth | chondrocyte, PMID 41399468 (Osteoarthr Cartil Open 2026: PIEZO mechanosensitivity differentially modulated by L-type and T-type voltage-sensitive ion channels) | CACNA1C, CACNA1G | **yes** |
| D14 | **Actin cytoskeleton organisation under load → column formation** | Mechanical loading reorganises actin and that is what builds columns | mouse/rodent, PMID 28539407 (Mol Biol Cell 2017: mechanical loading regulates organization of the actin cytoskeleton and column formation in postnatal growth plate) | RHOA/ROCK, RAC1 | **yes** |
| D15 | **Human growth-plate response to biomechanical loading (transcriptome)** | The only human dataset of its kind — ADOLESCENT human plate tissue transcriptionally profiled under load | human, PMID 39655393 (Cartilage 2024: genomic effects of biomechanical loading in adolescent human growth plate cartilage — pilot) | — | **yes** |
| D16 | **Mitochondrial function / OXPHOS in chondrocytes** | The hypoxic plate is assumed glycolytic; mitochondrial structure changes track mineralisation | mouse ATDC5, PMID 38860464 (relationships between matrix mineralization, oxidative metabolism and mitochondrial structure during chondroprogenitor differentiation); review INDEX PMID 39394187 (metabolic reprogramming in skeletal cell differentiation) | HIF-1α, PGC1α | no |
| D17 | **Mitochondrial transfer between cells via Cx43** | MSCs can donate mitochondria to chondrocytes through connexin-43 channels — an entirely unexploited route | human, PMID 39390589 (Stem Cell Res Ther 2024: connexin 43 regulates intercellular mitochondrial transfer from human MSCs to chondrocytes) | GJA1 | **yes** |
| D18 | **Gap junctions / connexin hemichannels** | Coupling within columns; a Cx43 point mutation causes a human craniometaphyseal dysplasia in mouse model | mouse, PMID 39848944 (Bone Res 2025: skeletal abnormalities caused by a Connexin43 R239Q mutation, autosomal recessive craniometaphyseal dysplasia model); PMID 39641271 (activation of connexin hemichannels enhances mechanosensitivity and anabolism in bone) | GJA1 | **yes** |
| D19 | **ER stress / secretory load in the chondrocyte** | The plate secretes COL2A1 at extreme levels; folding capacity is a candidate throughput limit, and ER stress shortens bone directly | mouse, PMID 39778777 (ER stress causes long bone shortening in P4hb C402R/+ mice, Cole-Carpenter model); human variant, PMID 41877217 (Clin Transl Med 2026: MMP13 frameshift causes short stature via MMP13–HSPA5 interaction and ER stress); broiler, PMID 40331700 | HSPA5/BiP, PERK, ATF6, P4HB | **yes** |
| D20 | **ER-resident protein network in cartilage/bone homeostasis** | An explicit review of ER-resident proteins as skeletal players | review INDEX PMID 41278200 (Front Cell Dev Biol 2025: ER-resident proteins are key players in cartilage and bone homeostasis) | SERPINH1/HSP47, PDIs | **yes** |
| D21 | **Matrix vesicles (biogenesis and function)** | The initiation site of mineralisation at the discharge front; biogenesis route (exosomal vs ectosomal) is contested | multi-species, review INDEX PMID 40448594 (JBMR 2025: taking a closer look at matrix vesicle biogenesis); PMID 39877729 (a protein corona modulates the function of mineralization-competent matrix vesicles) | ANXA5, TNAP/ALPL, PHOSPHO1, ENPP1 | no |
| D22 | **Membrane lipid composition of matrix vesicles (ceramide/curvature)** | Physical chemistry of the vesicle membrane sets whether mineral nucleates | in-vitro biophysics, PMID 41019624 (ACS Phys Chem Au 2025: effect of ceramide ratio on membrane curvature of mimetic models of matrix vesicles) | SMPD3, ceramide | **yes** |
| D23 | **TNAP/ALPL and pyrophosphate balance at the front** | Sets whether the last septa mineralise on time; TNAP loss deranges synchondrosis growth | mouse, PMID 28377728 (Front Physiol 2017: TNAP regulates cranial base growth and synchondrosis maturation) | ALPL, ENPP1, ANKH, PHOSPHO1 | no |
| D24 | **Cell–matrix adhesion (β1 integrin, ILK/PINCH/parvin)** | Physically holds the column together and is required for length | mouse, PMID 37607905 (α-parvin); PMID 38294852 (N-cadherin + β1 integrin); PMID 36602038 (integrin expression of septoclasts/pericytes/endothelium at the COJ) | ITGB1, ILK, PARVA, CDH2 | **yes** |
| D25 | **Discoidin domain receptor 2 (collagen receptor)** | A non-integrin collagen sensor with a skeletal phenotype | mouse, PMID 39746922 (Bone Res 2025: DDR2 is an important modulator of BMP signalling during heterotopic bone formation); review INDEX PMID 38222874 | DDR2 | **yes** |
| D26 | **Hypoxia / HIF-1α in the avascular plate** | Sets survival and the metabolic state of the deepest chondrocytes; also links to the circadian clock | mouse, PMID 40854917 (HIF-1α regulates proliferation/differentiation of synchondrosis chondrocytes); PMID 38534356 (hypoxia modulates chondrogenesis through the circadian clock via HIF-1α) | HIF1A, VHL, EGLN | no |
| D27 | **Circadian clock in cartilage (BMAL1/REV-ERBα)** | A timing layer over the plate; disruption changes cartilage behaviour under load | mouse, review INDEX PMID 39870641 (Bone Res 2025: BMAL1 regulating bone and cartilage metabolism); PMID 40606845 (inhibiting REV-ERBα protects against overloading-induced cartilage clock disruption) | BMAL1, CLOCK, NR1D1, RORβ (PMID 40654192) | **yes** for growth |
| D28 | **Nutrient/mechanical gradient across the plate (physical niche)** | Human measurement of stiffness/chemistry gradients that polarise the plate | human, PMID 40781081 (Nat Commun 2025) | matrix composition | **yes** |
| D29 | **microRNA layer in growth-plate cartilage** | Post-transcriptional control; a conditional miR-433 perturbation moves plate dynamics; miR-140 is developmental more than degenerative | mouse, PMID 41342396 (JBMR 2026: miR-433 targets BMP and Ihh signalling to coordinate postnatal growth plate dynamics); PMID 41242538 (miR-140 more functional in joint development than disease); review INDEX PMID 40225327 | miR-433, miR-140, miR-26b | **yes** |
| D30 | **Exosome/EV-mediated delivery INTO the growth plate** | The plate is avascular; EV nanoparticles have been used to deliver siRNA and GH to it | rodent, PMID 38639394 (Adv Sci 2024: targeting siRNA and growth hormone delivery to the growth plate using exosome nanoparticles for idiopathic short stature) | — | **yes** |
| D31 | **Growth-plate-targeting nanoparticles** | A second, independent demonstration that the plate can be drug-targeted | mouse, PMID 42338508 (Bioact Mater 2026: growth plate cartilage-targeting nanoparticles for pharmacological treatment of hypochondroplasia) | — | **yes** |
| D32 | **Engineered growth-plate organoid** | The in-vitro system that would allow a length-analogue endpoint; explicitly reviewed as unsolved | in vitro, PMID 41643409 (Biomater Adv 2026: construction of growth plate organoids via a layered induction 3D system); review INDEX PMID 40104770 (challenges of engineering a functional growth plate in vitro) | — | **yes** |
| D33 | **Site-specific skeletal stem-cell diversity (human)** | Stem cells from different skeletal sites are functionally different — a cell-biological basis for why plates differ by bone | human, PMID 40118065 (Cell Stem Cell 2025: human skeletal development and regeneration are shaped by functional diversity of stem cells across skeletal sites) | HOX code | **yes** |
| D34 | **3D chondrocyte hypertrophy morphometry (uremic model)** | Shows hypertrophy can be deranged in shape as well as size, and that GH changes the shape trajectory | rat, PMID 32630463 (Int J Mol Sci 2020: innovative 3D microscopic analysis of the uremic growth plate discloses alterations in chondrocyte hypertrophy; effects of GH) | GH; uraemia | **yes** |
| D35 | **Capillary end morphology invading the plate** | SEM of the actual vascular tips that penetrate the last septa — the physical act of invasion | rat, PMID 35537657 (J Oral Biosci 2022: morphological variety of capillary ends invading the epiphyseal plate in rat femora, SEM with osmium maceration) | VEGF | **yes** |
| D36 | **Endothelial SMAD1/5 coupling angiogenesis to osteogenesis** | The endothelial-side switch at the invasion front in JUVENILE bone | mouse, PMID 38480819 (Commun Biol 2024) | BMP/SMAD1/5 | **yes** |
| D37 | **Lacunar morphology / mineralisation gradients in epiphyseal cartilage** | Physical architecture that reflects mechanical function of the epiphysis | mouse, PMID 40472918 (Acta Biomater 2025: gradients in lacunar morphology and cartilage mineralization reflect the mechanical function of the mouse femoral head epiphysis) | mechanical | **yes** |

### E. FUSION — WHAT IS ACTUALLY KNOWN ABOUT THE TERMINAL EVENT

| # | CELL TYPE / PROCESS / STRUCTURE | ROLE IN LENGTH | EVIDENCE (species + PMID) | REGULATORS | OBSCURE? |
|---|---|---|---|---|---|
| E1 | **Human epiphyseal fusion does NOT use classical apoptosis** | The single most important negative result on the terminal event: in a HUMAN growth plate captured while fusing, TUNEL was negative and the fusing plate contained disorganised large chondrocytes ringed by dense cortical-like bone | human, PMID 19730156 (Epiphyseal fusion in the human growth plate does not involve classical apoptosis) | — | **yes** |
| E2 | **Four competing hypotheses of fusion (no consensus)** | The field's own statement that the mechanism is unresolved, and that rodents cannot answer it because they do not fuse | review INDEX PMID 21540578 (mechanisms of growth plate maturation and epiphyseal fusion — four postulated hypotheses/theories) | oestrogen; senescence | no |
| E3 | **The species problem: mice and rats do not fuse** | The reason there is no mechanism — the standard model organism lacks the phenotype | mouse, PMID 40478277 (Calcif Tissue Int 2025: mineral content and ECM protein expression in mouse growth plates during epiphyseal fusion — explicitly notes mouse plates never fuse completely); human/rabbit comparison in PMID 21540578 | — | no (but under-weighted) |
| E4 | **Mineral redistribution during fusion (SEM/EDS)** | Direct physical measurement of what happens to mineral as the plate closes | mouse, PMID 40478277 | — | **yes** |
| E5 | **VEGF as the oestrogen-responsive fusion effector** | Oestradiol raises growth-plate VEGF and VEGF rises through puberty — a candidate mechanism linking the hormone to vascular closure | rat + in vitro, PMID 20093283 (Expression of VEGF in the growth plate is stimulated by estradiol and increases during pubertal development) | E2, ERα, VEGFA | **yes** |
| E6 | **RUNX2 implicated by human pubertal transcriptomics** | Two growth plates from ONE girl at consecutive Tanner stages; the whole-genome contrast nominates RUNX2 in epiphyseal maturation | human (n=1, two specimens), PMID 21307122 (Genome-wide screening in human growth plates during puberty suggests a role for RUNX2 in epiphyseal maturation) | RUNX2, oestrogen | **yes** |
| E7 | **Human physis molecular identity by RNA-seq** | Baseline human physis transcriptome against articular cartilage and bone — the reference the fusion question needs | human, PMID 29775757 (Molecular characterization of physis tissue by RNA sequencing) | — | **yes** |
| E8 | **Fusion as pool exhaustion (senescence model)** | Fusion occurs when proliferative capacity approaches zero; oestrogen accelerates, does not initiate | rabbit, PMID 16614378; rabbit, PMID 24708243; INDEX PMID 21865751 | division count; oestrogen | no |
| E9 | **Pharmacologically-induced premature closure — hedgehog antagonist** | Sonidegib closes a normal juvenile plate; a retinoid antagonist PREVENTS it — a rescuable closure | mouse, PMID 33724538 (premature growth plate closure caused by a hedgehog cancer drug is preventable by co-administration of a retinoid antagonist) | SMO; RARγ | **yes** |
| E10 | **Pharmacologically-induced closure — all-trans retinoic acid** | ATRA drives premature closure with a multi-omic mechanism worked out | rat + ATDC5, PMID 41239925 (Impact of all-trans retinoic acid on skeletal development: mechanisms of growth plate closure) | RAR | **yes** |
| E11 | **Pharmacologically-induced closure — imatinib** | A kinase inhibitor that closes plates in vivo | rodent, PMID 19626049 (imatinib mesylate causes growth plate closure in vivo) | PDGFR/KIT/ABL | **yes** |
| E12 | **Pharmacologically-induced closure — FGF7 and methylphenidate** | Two further agents with plate-closing activity, both essentially absent from growth pharmacology discussions | mouse, PMID 39638118 (FGF7 causes premature growth plate closure); in vitro, PMID 36835608 (methylphenidate promotes premature growth plate closure: in vitro evidence) | FGFR2b; DAT/NET | **yes** |
| E13 | **Ligand-side closure: CNP knockout rats close EARLY and are rescued** | Loss of CNP causes early plate closure and exogenous CNP-53 prevents it — the cleanest "closure is preventable" result | rat, PMID 30235256 (exogenous C-type natriuretic peptide restores normal growth and prevents early growth plate closure in its deficient rats) | NPPC/NPR2 | no |
| E14 | **Fusion timing measured in humans by MRI** | The actual human timetable across six sites, both sexes, with pubertal-stage correlation | human, PMID 33047349 (cross-sectional MRI study of factors influencing growth plate closure in adolescents and young adults, n=958) | sex, puberty, BMI, activity | no |
| E15 | **Growth continuing BEYOND expected closure** | Human evidence that "closed" by bone-age convention is not the end of growth in some conditions | human, PMID 31968095 (continued statural growth in older adolescents/young adults with Crohn's disease and ulcerative colitis beyond the time of expected growth plate closure) | inflammation; delayed maturation | **yes** |
| E16 | **Accelerated fusion when SOCS2 is absent** | A specific genetic accelerator of fusion, with a downstream joint cost | mouse, PMID 35272487 (Bone Joint Res 2022: the role of accelerated growth plate fusion in the absence of SOCS2 on osteoarthritis vulnerability) | SOCS2, GH signalling | **yes** |
| E17 | **Physeal bar as "local fusion" — and it is nerve-driven** | The one form of plate closure with a newly identified causal upstream signal | mouse, PMID 42555751 (pleiotrophin from somatosensory nerves); mouse, PMID 39033138 (b-series ganglioside depletion prevents limb-length discrepancy after growth plate injury) | PTN; gangliosides | **yes** |
| E18 | **Physeal allograft transfer (replacing a fused/barred plate)** | The surgical analogue of "restart the plate" — feasibility now tested in a large animal | swine, PMID 41485130 (J Orthop Res 2026: physeal allograft transfer for physeal bars — a safety and feasibility study in a domestic swine model) | — | **yes** |
| E19 | **MSC therapy for physeal growth arrest** | Systematic review of attempts to biologically restore an arrested plate | human/animal, systematic review INDEX PMID 41141171 (Cureus 2025: mesenchymal stem cells in pediatric physeal growth arrest) | — | **yes** |
| E20 | **Regenerative medicine for physeal injury (state of the field)** | Index of what has been tried to rebuild a plate | review INDEX PMID 41419720 (Ann Biomed Eng 2026: growth plate injuries — advances and future directions in regenerative medicine) | — | **yes** |

### F. COMPARATIVE, EXTREME AND ADJACENT MODELS (the parts list seen from outside the mouse tibia)

| # | CELL TYPE / PROCESS / STRUCTURE | ROLE IN LENGTH | EVIDENCE (species + PMID) | REGULATORS | OBSCURE? |
|---|---|---|---|---|---|
| F1 | **DUAL stem-cell organisation of the HUMAN pubertal plate** | Two distinct stem-like RZ populations in human tissue; the "root" cells are **PTHrP-NEGATIVE**, express skeletal-stem markers, sit in a **low-WNT AND low-TGF-β** microenvironment, and are marked by **Prrx1** in mouse; GH acts DIRECTLY on human explants (JAK/STAT, TGF-β, ERK up; AKT down) | human + mouse, PMID 41984930 (Sci Transl Med 2026: a transcriptional atlas of the pubertal human growth plate reveals two populations of stem cells and direct effect of growth hormone) | WNT-low, TGFβ-low niche; PRRX1; GH | **yes** (published 2026; supersedes single-stem-cell models) |
| F2 | **Hypertrophic chondrocytes as a RESERVOIR for marrow SSPCs, osteoblasts AND adipocytes** | The transdifferentiation destination is not only osteoblast — it includes marrow stroma and fat | mouse, PMID 35179487 (eLife 2022: hypertrophic chondrocytes serve as a reservoir for marrow-associated skeletal stem and progenitor cells, osteoblasts, and adipocytes during skeletal development) | — | **yes** |
| F3 | **Deer antler: centimetre-per-day elongation** | The fastest-elongating bone structure known; driven by a vast stem-progenitor pool + dense vasculature + HYBRID ossification — a natural experiment in what a plate could do | deer, PMID 41472858 (Imeta 2025: a vast stem-progenitor cell pool, richly vascular system, and hybrid ossification drive the daily centimeter-scale elongation of bony antlers); PMID 41383963 (single-cell transcriptome of antler elongation) | RXFP2 (PMID 40263536) | **yes** |
| F4 | **Jerboa disproportionate limb growth** | Interspecies transcriptomics identifying what makes ONE bone in one animal grow more than another | jerboa/mouse, PMID 34793695 (Curr Biol 2022: interspecies transcriptomics identify genes that underlie disproportionate foot growth in jerboas); PMID 41073372 (Nat Commun 2025: cellular and genetic mechanisms shaping tail VERTEBRAL proportion in mice and jerboas) | — | **yes** |
| F5 | **Zebrafish cell-expansion mechanics (INPPL1)** | Cell expansion as a shared physical mechanism between notochord and endochondral lengthening; INPPL1 is also a human opsismodysplasia gene | zebrafish, PMID 40209709 (Curr Biol 2025: cell expansion for notochord mechanics and endochondral bone lengthening depends on the 5'-inositol phosphatase Inppl1a) | INPPL1/SHIP2 | **yes** |
| F6 | **Physiological regulation of skeletal PROPORTION** | Why different bones stop at different lengths — the comparative framing of the same cell biology | multi-species review INDEX PMID 33369789 (Exp Physiol 2021: physiological regulation of bone length and skeletal proportion in mammals); PMID 31180500 (developmental and evolutionary allometry of the mammalian limb skeleton) | HOX; differential senescence | **yes** |
| F7 | **hPSC-derived skeletal assembloid / sclerotomal progenitor models** | An in-vitro human system that recapitulates endochondral ossification — the route to a human length-analogue assay | human iPSC, PMID 40118845 (Nat Commun 2025: recapitulation of endochondral ossification by hPSC-derived SOX9+ sclerotomal progenitors); PMID 37126720 (PNAS 2023: modeling human skeletal development using hPSCs); PMID 40577622 (self-organized hyaline cartilage in hPSC multi-tissue organoids) | — | **yes** |
| F8 | **Medullary cavity expansion by distinct cell populations** | The marrow side of the same event; distinct populations rather than one clast | mouse, PMID 41980979 (Nat Commun 2026: medullary cavity expansion is mediated by distinct cell populations during fetal bone development); PMID 35689447 (osteoclasts and macrophages in marrow cavity formation) | — | **yes** |
| F9 | **Articular–epiphyseal cartilage complex (AECC)** | The epiphyseal cartilage above the SOC is a growth engine too, and its failure is osteochondritis dissecans | human/pig, PMID 40432951 (evaluating the etiology of osteochondritis dissecans of the knee: the role of the articular-epiphyseal cartilage complex) | vascular supply | **yes** |
| F10 | **Tibial dyschondroplasia (avian)** | A spontaneous, high-frequency failure of vascular invasion and hypertrophic clearance in a fast-growing animal — a natural jam model | chicken, PMID 38136788 (homeostatic regulation of pro- and anti-angiogenic proteins via hedgehog, Notch and ephrin signalling in tibial dyschondroplasia) | VEGF, Hh, Notch, ephrin | **yes** |
| F11 | **Meckel's cartilage / synchondrosis as non-canonical plates** | Cartilage growth centres with different rules; useful controls for what is generic vs plate-specific | mouse, PMID 41545657 (Cell Tissue Res 2026: Meckel's cartilage midsegment); PMID 35195769 (septoclasts in mouse Meckel's cartilage) | — | **yes** |
| F12 | **Enthesis / tendon fibrocartilage progenitors (Tnn+, Trpv4+)** | Adjacent chondro-lineage compartments that share machinery with the plate | mouse, PMID 42009636 (Bone Res 2026: Tnn+ progenitors form tendon enthesis fibrocartilage); PMID 42437668 (exercise-primed Trpv4+ progenitors in enthesis regeneration) | TNN, TRPV4 | **yes** |
| F13 | **Marrow Adipoq-lineage cells as a local IGF-1 source** | Marrow fat is not inert — it secretes IGF-1 onto bone surfaces | mouse, PMID 41798725 (JBMR Plus 2026: IGF-1 from bone marrow Adipoq-lineage cells stimulates endocortical bone formation) | ADIPOQ, IGF1 | **yes** |
| F14 | **Cross-species growth-plate histocytomorphometry method** | The measurement standard that would let plate architecture be compared across species and studies | multi-species, PMID 41836565 (J Orthop Translat 2026: spatially resolved single-cell-based histocytomorphometry for growth plate analysis across multiple species) | — | **yes** |
| F15 | **Uremic / systemic-disease derangement of hypertrophy shape** | Shows the hypertrophic trajectory is a separable, measurable, disease-modifiable variable | rat, PMID 32630463 | GH; uraemia | **yes** |

---

## CONTESTED OR UNRESOLVED QUESTIONS

**1. Transdifferentiation vs apoptosis — how contested is it actually?**
The transdifferentiation of hypertrophic chondrocytes into osteoblasts is now supported by many
independent lineage-tracing studies (mouse, PMID 33253203; PMID 35179487; PMID 41663374), and the
destination list has *widened* rather than narrowed — hypertrophic chondrocytes are reported to
supply marrow skeletal stem/progenitor cells, osteoblasts **and adipocytes** (PMID 35179487). What
remains genuinely contested is the **fraction**, the **species-generality**, and whether the surviving
cell is a "transdifferentiated" osteoblast or a **dedifferentiated progenitor** that then
re-differentiates. Mechanistically the switch is being pinned on RUNX2 (required, PMID 33253203) and
on the *withdrawal* of SOX9 (persistent SOX9 suppresses it, PMID 31121357), with β-catenin,
KDM6A (PMID 42212366) and NF-κB (PMID 34934622) modulating. Apoptosis is not abolished by this — the
honest position is that both occur and nobody has measured the split in a human plate.

**2. Is the resting zone a stem-cell compartment, and how many populations?**
Three incompatible pictures are live simultaneously: (a) a **rare PTHrP+ skeletal stem cell**
(mouse, PMID 30401834); (b) **ApoE as a marker of ALL resting-zone chondrocytes** (mouse,
PMID 40025030), which would mean the RZ is one population rather than stem + bulk; (c) the 2026
human atlas showing **TWO** stem-like RZ populations, of which the deeper "root" population is
**PTHrP-NEGATIVE**, Prrx1-marked in mouse, and sits in a niche low in **both** WNT and TGF-β
(PMID 41984930). These are not reconciled. A 2026 PRISMA systematic review goes further and argues
the word "quiescent" has been applied to RZ chondrocytes for decades with **limited molecular and
functional characterisation** and no consensus definition (PMID 41795828).

**3. Does the embryonic plate work the same way as the postnatal plate?**
No. Column formation is **limited or absent embryonically**, implying divergent growth mechanisms
before and after birth (mouse, PMID 39269144). Self-renewal in the RZ is described as being acquired
around **secondary ossification centre formation**. This is a direct warning that embryonic
conditional knockouts — the majority of the skeletal literature — may not report on an open
adolescent plate.

**4. What actually happens at fusion?**
The single most important result is a negative one in **human** tissue: a growth plate captured while
fusing contained **no TUNEL-positive cells at all**, so epiphyseal fusion in humans does not proceed
by classical apoptosis (PMID 19730156). The field's own review lists **four competing hypotheses**
and states the mechanism is unresolved (PMID 21540578). The structural obstacle is species: mouse and
rat plates **never fuse completely** (stated explicitly in PMID 40478277), so the standard model
organism lacks the phenotype. Candidate effectors with human/rat support are **VEGF** (oestradiol-
stimulated, rising through puberty; PMID 20093283) and **RUNX2** (nominated by a two-timepoint human
pubertal transcriptome, n=1; PMID 21307122). Pool-exhaustion (senescence) remains the leading
framework (rabbit; PMID 16614378, PMID 24708243).

**5. Which cell resorbs the last septum — septoclast, chondroclast, osteoclast, or endothelium?**
All four have claims. Septoclasts are now traced to **pericytes** (PMID 40387924) and to the
**perichondrium** (PMID 41319243) and separately to **mesenchymal stromal cells** (PMID 35091558) —
three origins in three papers. Chondroclasts are transcriptionally distinct from osteoclasts
(PMID 32650826). And **endothelial cells themselves have been shown to act as chondroclasts**
(PMID 30936470). This is a genuinely unsettled cell-identity question sitting at the exact step that
limits discharge.

**6. Is volume increase swelling, biosynthesis, or both — and what is the controller?**
The machinery is present and drugged in the wrong direction. Volume DECREASE (RVD) is well
characterised in articular chondrocytes; volume INCREASE via NKCC1 has a direct siRNA demonstration
(PMID 21847667); an Na+/K+ ATPase has been shown to set **bone length variation between mouse
strains** (PMID 34970538); NHE1/AE2 have been reviewed explicitly for longitudinal growth
(PMID 35877910); and WNK2 variants change the chondrocyte's osmotic response in humans
(PMID 40592720). Almost none of this has been read out on a bone-length endpoint in a normal
growing animal.

**7. Does the AXIAL plate obey the same rules?**
Unresolved and barely asked. The vertebral growth plate has its own mechanically-driven failure mode
(PIEZO1→GPX4→ferroptosis; PMID 40714837), which is rescued by unloading (PMID 42082502), and the
vertebral **ring apophysis** matures very late and is **delayed in adolescent idiopathic scoliosis**
(PMID 38849690). Whether the axial plate's cell biology differs from the long-bone plate at the level
of stem-cell identity or hypertrophic behaviour has, as far as this search reached, never been tested
directly.

**8. Primary cilium: signalling antenna, mechanosensor, or polarity marker?**
All three are claimed. New work reports cilia in the growing limb are **preferentially oriented and
uncoupled from centriolar position** (`UNVERIFIED-PMID`, 2025 record), i.e. there is a polarity axis
distinct from the classical centriole-based one; and PIEZO1 signals *through* the cilium in
compressive plate degeneration (PMID 41194970). The cilium is simultaneously the site of all hedgehog
transduction (review PMID 41613437).

**9. Is the "resting zone" metabolically defined rather than transcriptionally defined?**
A live alternative: reduced glycolysis has been proposed as what makes RZ chondrocytes slow-cycling
(`UNVERIFIED-PMID`, 2023 record), and FLIM now shows a measurable metabolic transition from
proliferation to quiescence in intact joints (PMID 42186485). If the RZ state is metabolic, markers
are downstream and the lever is metabolic.

---

## PROCESSES NOBODY HAS PERTURBED (with a bone-length endpoint, in a normal growing animal)

These are the rows where a cell-biological mechanism is established but the caliper has never been
used. Ranked by how load-bearing the process is for elongation.

1. **Chondrocyte volume-DECREASE machinery (RVD).** Every published manipulation of chondrocyte
   volume regulation is in **articular** cartilage and reads out on OA, stiffness or viability — never
   on bone length. Blocking RVD is the arithmetically obvious way to enlarge the hypertrophic cell,
   and the specific effectors (K-Cl cotransport, ClC-3/PAC anion currents, aquaporins, WNK2–SPAK) have
   **no length endpoint in any species**. PMIDs 25450844, 33282866, 33383561, 38015518, 40592720.
2. **Septoclast biology — PARTLY FALSIFIED WITHIN THIS ROUND, and the correction is the more useful
   result.** I drafted "nobody has perturbed septoclasts with a length endpoint" and then read
   **PMID 42297360** (Cell Prolif 2026), which does exactly that: the **soluble epoxide hydrolase
   inhibitor TPPU** promoted **long-bone growth in newborn mice**, reduced the hypertrophic:proliferative
   width ratio, and **raised septoclast activity (MMP9, FABP5) in the metaphysis**, acting through
   endothelial→mesenchymal **NOTCH** signalling. TPPU is an obtainable tool compound. What remains
   true and unperturbed: the septoclast's **three competing origins** (PMIDs 35091558 mesenchymal
   stromal, 40387924 pericyte, 41319243 perichondrium) have never been reconciled, no
   septoclast-specific genetic ablation with a length endpoint exists, and ETS1 — its one named
   transcription factor — has never been perturbed with a caliper.
3. **Endothelial-cell chondroclast function.** PMID 30936470 reassigns cartilage resorption to
   endothelium; no follow-up perturbation with a length endpoint was found.
4. **Bone lymphatics.** Lymphatic vessels exist in bone and expand on injury (PMID 36669473). No
   study has asked whether they exist at, or matter to, the growth plate.
5. **Sensory innervation of the physis.** Nerves have just been shown to *cause* bony-bar formation
   via pleiotrophin (PMID 42555751). Nobody has asked whether physeal innervation modulates NORMAL
   elongation — denervation with a length endpoint appears not to exist.
6. **The perichondrial ring of LaCroix as a cell source.** One in-vivo chick experiment
   (PMID 16652202) and essentially nothing since; no mammalian perturbation with a length endpoint.
7. **Groove of Ranvier.** Named in every textbook, traced by Gli1 in fetal mouse (PMID 41253754),
   never ablated or expanded postnatally with a length readout.
8. **Cilium ORIENTATION (as distinct from cilium presence).** IFT knockouts are abundant; nobody has
   perturbed cilium *orientation* and measured length.
9. **Mitochondrial transfer into chondrocytes.** Demonstrated MSC→chondrocyte via Cx43
   (PMID 39390589); never attempted at a growth plate, never with a length endpoint.
10. **Matrix-vesicle membrane lipid composition.** Ceramide content sets vesicle curvature and
    therefore mineral nucleation (PMID 41019624) — pure biophysics, no in-vivo skeletal experiment.
11. **ER folding capacity as a throughput limit.** ER stress *shortens* bone (PMIDs 39778777,
    41877217), but nobody has **raised** chaperone capacity in a normal plate and measured length.
12. **Marrow adipocyte lineage as a competing sink** for the ex-chondrocyte pool (PMID 35179487) —
    no experiment redirects that fate and measures a bone.
13. **Gap-junctional coupling within a column.** Cx43 mutations cause skeletal disease
    (PMID 39848944), but no column-specific coupling manipulation with a length endpoint exists.
14. **Circadian control of the plate.** BMAL1/REV-ERBα work is entirely cartilage-degeneration
    framed; no chondrocyte-clock deletion with a longitudinal-growth endpoint was found.
15. **Borderline chondrocytes.** Two 2019 papers established the population (PMIDs 30888720,
    31329317) and nothing since perturbs it.
16. **The "root" PTHrP-NEGATIVE stem population** identified in human plates in 2026
    (PMID 41984930) — brand new, no perturbation of any kind yet.
17. **Growth-plate organoids as a length-analogue assay.** The system is being built
    (PMID 41643409) and its inadequacy is explicitly reviewed (PMID 40104770); it is not yet a
    screening platform.
18. **The AXIAL plate.** Almost every mechanism above has been tested, if at all, in a long bone.

---

## WHAT I COULD NOT VERIFY

- **Records returned by Europe PMC with NO PMID.** Several relevant items are indexed as preprints or
  non-MEDLINE records and returned `pmid: -`. I have marked these `UNVERIFIED-PMID` and quoted the
  title as returned, without asserting a journal: "Human growth plates house resting zone
  sub-populations with features of quiescent stem cells" (2025); "Reduced glycolysis links resting
  zone chondrocyte proliferation in the growth plate" (2023); "Primary cilia in the growing limb are
  preferentially orientated, uncoupled from centriolar position" (2025); "Bone elongation in the
  embryo occurs without column formation in the growth plate" (2023 — almost certainly the preprint of
  PMID 39269144, but I did not confirm that); "Retinoic acid signaling suppresses chondrocyte identity
  during cartilage development and regeneration" (2024); "Modeling human limb skeletal development
  using human pluripotent stem cell-derived skeletal assembloids" (2025).
- **Species not stated in the API record.** For PMID 32332842 (seven morphological subphases) the
  species was not recoverable from title/abstract fields I retrieved; recorded as UNVERIFIED species.
- **Effect sizes.** I deliberately quote NO numeric effect sizes except where they appeared verbatim
  in an abstract I retrieved in full (PMIDs 41984930, 41795828, 30401834, 19730156, 21540578,
  20093283, 21307122, 40478277, 33724538). Everything else is direction-only.
- **Full texts.** I read abstracts via NCBI eutils for a small number of load-bearing papers only.
  No paywalled full text was obtained. In particular I did **not** verify (a) the fraction of
  metaphyseal osteoblasts that are chondrocyte-derived in any study, (b) the marker panel of the
  "root" stem population beyond what the PMID 41984930 abstract states, (c) whether PMID 40025030's
  ApoE claim is exclusive of the PTHrP+ population.
- **Two brief items I could not resolve to a primary source.** (i) A primary *functional* study of
  the **perichondrial ring of LaCroix** in a mammal — I found only the chick reservoir study
  (PMID 16652202) and clinical/anatomical reviews. (ii) A dedicated study of **lymphatics at the
  growth plate** specifically — PMID 36669473 establishes bone lymphatics but not physeal ones.
- **Search reach.** All searching was Europe PMC + NCBI eutils. I did not use WebSearch/WebFetch in
  this round, so clinicaltrials.gov, regulatory documents, patents and conference abstracts are NOT
  covered by this enumeration. Older literature (pre-2000) is under-represented because Europe PMC
  relevance ranking favours recent records; several classical growth-plate cell-biology results
  (e.g. Hunziker's stereology, Farnum & Wilsman's kinetics) will exist and are not cited here.
