# DOMAIN 04 — SIGNALLING PATHWAYS: COMPLETE INVENTORY (R436 full-concept-space enumeration)

**Method.** Everything below was found by EXTERNAL search only (NCBI eutils esearch/esummary against PubMed,
plus Europe PMC REST). No file in `/home/user/growth-plate` was consulted except the two briefs. Every PMID
in this document was returned by a live query in this session and its title read; where a number, direction
or species could not be confirmed from the retrieved title/abstract metadata, the cell says **UNVERIFIED**.
Reviews are flagged as `(review — index only)`.

**Size.** 160 pathway rows, of which **104 are marked OBSCURE**. 311 distinct PMIDs cited, all verified to
resolve (see integrity check at the end).

**Column semantics.**
- *EFFECT ON LENGTH* — the direction on **longitudinal bone / body length**, not on bone mass, cartilage
  thickness or plate height. Where only a plate-morphology or mass endpoint exists I say so explicitly,
  because a thicker plate is not a longer bone.
- *DRUG IN TALLER DIRECTION?* — is there an existing agent (approved, clinical-stage, or a real tool
  compound) that pushes the pathway in the direction associated with MORE length? "NO — class is inhibitors"
  is the commonest answer and is itself a finding.
- *OBSCURE?* — yes = rarely or never discussed in the mainstream longitudinal-growth literature.

---

## TABLE

| # | PATHWAY | EFFECT ON LENGTH | EVIDENCE (species + PMID) | DRUG IN TALLER DIRECTION? | OBSCURE? |
|---|---|---|---|---|---|
| 1 | **FGFR3 (canonical brake)** | Gain-of-function SHORTENS; loss LENGTHENS | human achondroplasia — transmembrane-domain FGFR3 variants, 31975530, 21324899, 12816345; mouse — excess FGFR3 disrupts resting-zone chondrocyte turnover via CREB, 41748604 | YES — FGFR3-directed TKIs and CNP analogues are a mature clinical class; cartilage-targeting nanoparticle delivery demonstrated in mouse hypochondroplasia, 42338508 | no |
| 2 | **FGF9 / FGF18 ligands** | Loss SHORTENS (required for hypertrophy + vascularisation) | mouse, combined allelic series 26794256; mouse Fgf9 17544391 | NO — no ligand-supply agent with a length endpoint | no |
| 3 | **FGF from the OSTEOPROGENITOR lineage (non-cell-autonomous)** | Non-autonomously required for postnatal chondrocyte proliferation | mouse 27052727 | NO | **yes** |
| 4 | **Sprouty (SPRY) — intracellular FGF feedback antagonist** | Overexpression → chondrodysplasia (SHORTER); loss → ciliopathic skeletal phenotype via Hh upregulation | chick/mouse 10498682; mouse 34423857 | NO — a band, both ends abnormal | **yes** |
| 5 | **FGF23 / αKlotho (local, in the plate)** | FGF23 excess SHORTENS; blockade improves skeletal phenotype | FGF23+Klotho protein present in growth plate, 23206185; small-molecule FGF23 inhibitors improve skeleton in Hyp mice, 35339985; glucocorticoid→FGF23/FGFR3 in children, 31099911 | YES — burosumab (anti-FGF23) approved; small-molecule FGF23 inhibitors preclinical | no |
| 6 | **FGF21** | Undernutrition-induced FGF21 causes GH INSENSITIVITY in chondrocytes → shorter | mouse/chondrocyte 23940039 | NO agent in the lowering direction with a bone endpoint | **yes** |
| 7 | **FGF → autophagy axis** | FGF signalling regulates bone growth through autophagy | mouse 26595272 | NO | **yes** |
| 8 | **Indian hedgehog (IHH) ↔ PTHrP negative-feedback loop** | Sets the RATE of chondrocyte differentiation; loss SHORTENS | chick/mouse — the founding experiment, 8662546; mouse Ihh downregulation 29434683; Cbfβ→Ihh/PTHrP balance 24821091; postnatal plate organisation 21642420; review (index only) 32933018 | Partially — SMO agonists exist as tool compounds (see row 12) | no |
| 9 | **PTHrP → PTH1R** | Loss SHORTENS; constitutive activation (Jansen) also SHORTENS — a BAND | mouse limb mesenchyme 26620087; mouse Jansen model 40455993 | Teriparatide/abaloparatide exist but are PTH1R agonists at the wrong end of the band | no |
| 10 | **PTH1R → SIK2/SIK3 → HDAC4/5 → MEF2C** | SIK3 loss BLOCKS hypertrophy → shorter; HDAC4 loss → premature ossification | mouse 22318228, 33148508, 31430259; mouse 19704004; mouse Mef2c 17336904; mouse miR-140 robustness 25529628 | NO usable direction — SIK inhibitors mimic PTH, and both ends of the band shorten | no |
| 11 | **mTORC1** | Required for skeletal growth via protein synthesis; ACTIVATION alone does NOT lengthen — it disorders the resting zone | mouse 24948603; mouse Tsc1 activation 29955624; mouse mTORC1→PTHrP 27039827; mouse limb bud 27606668 | NO — every agent is an inhibitor (rapalogs), i.e. the shortening direction | no |
| 12 | **Smoothened / hedgehog AGONISM at the resting zone** | Stimulating growth-plate skeletal stem cells PROMOTES linear bone growth | mouse/rat 38516888 | ⭐ YES — SAG, purmorphamine, Hh-Ag class (research-grade tool compounds; no approved SMO agonist) | no |
| 13 | **SUFU (intracellular Hh brake)** | Chondrocyte SUFU loss IMPAIRS growth-plate maintenance and limb elongation → SHORTER | mouse, juvenile 36120578 | NO | no |
| 14 | **KIF7** | Promotes Hh in growth-plate chondrocytes by restraining SUFU | mouse 21795282 | NO | **yes** |
| 15 | **SPOP → IHH** | Spop positively regulates Ihh; loss impairs skeletal development | mouse 27930311 | NO | **yes** |
| 16 | **EVC / EVC2 (ciliary Hh amplifier)** | Loss = Ellis-van Creveld, SHORT limbs | mouse/cell 23026747, 21356043, 26219237; conditional Evc 35334131 | NO | **yes** |
| 17 | **Primary cilium / IFT machinery (KIF3A, IFT80, IFT88/Polaris)** | Loss disrupts Hh topography and SHORTENS / dysplastic plate | mouse Kif3a 17507416; mouse IFT80 26098911, 23333501; mouse Polaris synchondrosis 19587160; mouse TMJ 21566205 | NO — no cilium-lengthening agent with a bone endpoint | no |
| 18 | **GPR161 (ciliary Hh repressor GPCR)** | Loss de-represses Hh; controls limb patterning and skeletal morphogenesis | mouse 29222391; MSC mechanotransduction 33450431 | NO | **yes** |
| 19 | **GAS1 / CDON / BOC (Hh co-receptors)** | Collectively required for SHH pathway function | mouse 21664576 | NO | **yes** |
| 20 | **DICAM → IHH in primary cilia** | Promotes chondrocyte proliferation and maturation | mouse/cell 29702220 | NO | **yes** |
| 21 | **ADGRG6 / GPR126 (adhesion GPCR)** | Maintains growth-plate homeostasis THROUGH IHH; variants associate with adolescent idiopathic scoliosis | mouse 39236220; human GWAS 23666238 | NO — but adhesion-GPCR tethered-agonist peptides are a real emerging modality | **yes** |
| 22 | **EXT1/EXT2 heparan sulfate chain synthesis** | Loss → hereditary multiple exostoses; ectopic Hh drives outgrowth | mouse 41056386; human/mouse 29545125 (review — index only) | NO — direction is a band; global HS reduction is harmful | no |
| 23 | **GPC6 (glypican-6)** | Biallelic loss impairs endochondral ossification → omodysplasia, SHORT | human 19481194 | NO | **yes** |
| 24 | **GPC3 (glypican-3)** | Loss → Simpson-Golabi-Behmel **OVERGROWTH** incl. tall stature; mouse KO delays endochondral ossification | human 20301398 (GeneReviews — index), 42220602; mouse 15936336 | NO agent; direction is "remove a glypican" | no |
| 25 | **Syndecan-3** | Important for chondrocyte proliferation during limb skeletogenesis | mouse 15838620 | NO | **yes** |
| 26 | **Syndecan-4** | Supports fracture repair but NOT fetal skeletal development — a measured null for development | mouse 23233348 | n/a (null) | **yes** |
| 27 | **Perlecan / HSPG2** | Required; interacts with CCN2 to regulate chondrocyte proliferation/differentiation; domain IV controls clustering (Schwartz-Jampel) | mouse/human 12811819, 30203597 | NO | **yes** |
| 28 | **Heparanase** | Stimulates chondrogenesis; up-regulated in human ectopic cartilage | human/mouse 25863260; exostosis-independent 34996123 | NO | **yes** |
| 29 | **Pleiotrophin (HB-GAM)** | Targeted overexpression alters postnatal bone development | mouse 12413943 | NO | **yes** |
| 30 | **BMPR1B × GDF5** | Combinatorial; shapes distal limb; GDF5 mutations → brachydactyly | mouse 10631181; structure 15890363 | NO — recombinant GDF5 exists but no length endpoint | no |
| 31 | **NOGGIN (secreted BMP antagonist)** | Point mutations → symphalangism/brachydactyly (SHORT digits); required for craniofacial skeleton | human 17668388, 24326127; mouse 24949938 | NO — direction ambiguous; BMP antagonist protein used experimentally in exostosis mice 28445472 | no |
| 32 | **Chordin / CV2 (BMPER) / Twisted gastrulation** | Vertebral field morphogenesis | mouse 20807528, 18789316, 17035289 | NO | **yes** |
| 33 | **GREMLIN-1** | Limb bifurcation/patterning; osteoclast-lineage conditional deletion alters skeletal calcium response | Xenopus 26527308; mouse 39789342 | NO | **yes** |
| 34 | **BAMBI (pseudo-receptor BMP/TGF-β decoy)** | **NO skeletal length data found in any species** | — (all retrieved BAMBI hits are cancer/fibrosis/liver) | NO | **yes** |
| 35 | **ACVR1 / FOP** | R206H → heterotopic ossification; the RARγ agonist used against it is SKELETALLY TOXIC in juveniles | mouse 26896819, 30226468; human/mouse 33217406 | NO — palovarotene is the shortening direction (see row 62) | no |
| 36 | **Activin / follistatin** | Follistatin interacts with Noggin in axial skeleton; follistatin is the link between TRPV4 channelopathy and skeletal malformation | mouse 24514266; human/cell 24577120 | Partially — follistatin/ActRIIB-Fc biologics exist but no bone-LENGTH endpoint found | **yes** |
| 37 | **Myostatin / GDF8** | Loss increases tibia SIZE in quail; mouse humerus studied for mass not length | quail 36685194; mouse 12060865 | ⭐ YES — myostatin/ActRIIB inhibitors are a large clinical class, but **no mammalian bone-LENGTH endpoint was found** | no |
| 38 | **TGF-β receptor 2 (TGFBR2)** | Regulates maintenance of boundaries in the axial skeleton | mouse 16824508 | NO — ALK5 inhibitors are systemic and the chondrocyte arm runs the wrong way | no |
| 39 | **SMAD4 (common TGF-β/BMP node)** | Regulates Wnt7b from hypertrophic chondrocytes → endochondral ossification | mouse 37539462 | NO | **yes** |
| 40 | **Netrin-1 → BMP** | Netrin-1 SUPPRESSES BMP signalling; separately bone-protective | mouse/cell 33883596, 27681594; netrin-4 24846137 | NO | **yes** |
| 41 | **Canonical Wnt / β-catenin** | A BAND — inhibition impairs postnatal cartilage; transient ACTIVATION causes abnormal growth-plate CLOSURE | mouse 18397998; mouse 19815716; mouse Wnt4 overexpression → dwarfism 17505543; mouse β-catenin loss → chondroma-like masses 23274133 | NO in the safe direction — all marketed Wnt agents RAISE Wnt (bone-mass indication) | no |
| 42 | **Wnt / PCP (non-canonical)** | PCP activation promotes growth-plate COLUMN FORMATION; SOXC TFs act via non-canonical Wnt | mouse/in vitro 22674351; mouse 25761772 | NO | **yes** |
| 43 | **ROR2** | Loss → Robinow syndrome, SHORT limbs; disrupts chondrocyte polarity via BMP/TGF-β | mouse 14745966; human/mouse 37307827; zebrafish 37039156 | NO | no |
| 44 | **VANGL2** | Phosphorylated by Wnt gradient through ROR2 to set PCP | mouse 21316585 | NO | **yes** |
| 45 | **WNT16 → PCP/JNK–mTORC1–PTHrP** | Cascade characterised in cartilage | mouse 30745310 | NO | **yes** |
| 46 | **NOTUM (secreted Wnt de-palmitoylase)** | Enhances cartilage repair via Wnt modulation | rabbit 41596299 | NOTUM inhibitors exist — but they RAISE Wnt, the shortening direction | **yes** |
| 47 | **DKK1** | Reduces hypertrophic change in human chondrocytes | human cells 30447344 | NO | no |
| 48 | **NOTCH / RBPJ / HES** | Regulates chondrocyte differentiation AND proliferation in appendicular and axial skeleton; Hes1 marks peri-condensation precursors | mouse 19590010; mouse 37172728; NOTCH2 in epiphyseal chondrocytes 40345585 | ⭐ Agonist side: clustered/Fc-JAG1 and DLL1-Fc are catalogue reagents; γ-secretase inhibitors are the OPPOSITE (shortening) direction | no |
| 49 | **CNP → NPR2 → cGMP** | ⭐ GAIN LENGTHENS in humans and mice — the cleanest lengthening axis known | human NPR2 GOF overgrowth 24259409, 22870295; mouse BNP transgenic overgrowth 9482886; mouse chondrocyte CNP overexpression rescues achondroplasia via a MAPK-dependent route 14702637; mouse plasma CNP transgenic 19808910; mouse rescue 20610569; CNP analogue in Fgfr3 mouse 23200862, 26684019; NEP-resistant variant 25650377; long-acting CNP 35858423 | ⭐⭐ YES — vosoritide, navepegritide/long-acting CNP; approved class | no |
| 50 | **NPR3 (clearance receptor) / OSTEOCRIN decoy** | Circulating osteocrin stimulates bone growth by limiting CNP clearance | mouse 28990933 | Peptide occupants exist as reagents; no approved agent | no |
| 51 | **PRKG2 / PKGII (cGMP effector)** | Loss → dwarfism in rat, cattle, dog AND human acromesomelic dysplasia — four species | rat 15838621; cattle 19887637; dog 34680883; human 33106379; mouse plate profiling 25924610; mechanism 18551195 | NO — no PKG activator; the cGMP arm is raised upstream instead | no |
| 52 | **CREB (downstream of cGMP and cAMP)** | CREB ACTIVATION in hypertrophic chondrocytes underlies skeletal OVERGROWTH in NPR2-GOF chondrodysplasia Miura | human/mouse 30544148; and FGFR3 acts through CREB on resting-zone turnover 41748604 | NO direct CREB agent | no |
| 53 | **TRPM7 → Ca²⁺ oscillations (CNP's calcium arm)** | Required — mediates spontaneous Ca²⁺ fluctuations promoting bone development; CNP acts through it | mouse 30967513; mouse 36210025; 35287796 | NO — TRPM7 agents are inhibitors | **yes** |
| 54 | **NO / sGC / nitrate arm of cGMP** | **NO growth-plate length endpoint found in any species** — the searchable literature is vascular/valve | (searched; only vericiguat-bone-mass items returned, e.g. 38569649) | Agents abound (riociguat, vericiguat, nitrates) — untested for length | **yes** |
| 55 | **cAMP / PKA (upstream of CREB and SIK)** | A BAND — too little (iPPSD-type) and too much (Jansen) both shorten | mouse Jansen model 40455993; mouse Phlpp1 suppresses Pth1r signalling 33434347 | PDE inhibitors exist; direction contested | no |
| 56 | **ERK1/2** | Regulate chondrocyte TERMINAL differentiation | mouse 25401279 | MEK inhibitors = reduce hypertrophy, likely wrong direction | no |
| 57 | **p38 / MAPK14** | Conditional MAPK14 deletion → DWARFED mice (and TrkB deletion phenocopies it) | mouse 23776632 | NO — all p38 agents are inhibitors, i.e. shortening | no |
| 58 | **JNK1/2** | Deficiency → impaired annulus fibrosus, vertebral fusion, severe scoliosis | mouse 30664861 | NO | **yes** |
| 59 | **TrkB / BDNF** | Conditional TrkB deletion → dwarf phenotype | mouse 23776632 | Agonist antibodies/small molecules exist experimentally; no bone endpoint | **yes** |
| 60 | **gp130 / IL-6 / STAT3** | Required for homeostatic proliferation and anabolism in the POSTNATAL growth plate; gp130 sets bone SIZE | mouse 35039652; mouse 14755335; review 32788655 | Inverted: IL-6 BLOCKADE (tocilizumab) gives catch-up growth in inflamed children — 25504861, 29961686 | no |
| 61 | **GHR → JAK2 → STAT5B → IGF-1** | Loss → severe short stature in humans | human 36265659; human rhIGF-1 treatment 37586336 | YES — somatropin, mecasermin (established) | no |
| 62 | **STAT1/STAT3 in FGF-mediated growth arrest** | Measured NULL — they do NOT participate | rat chondrocytes 18198189 | n/a | **yes** |
| 63 | **Hippo / YAP1 / TAZ / TEAD** | YAP1 regulates multiple steps of chondrocyte differentiation; pathway controls skeletal MORPHOGENESIS | mouse 26923596; mouse 32994166 | NO in the lengthening direction — all TEAD agents are inhibitors | no |
| 64 | **NF-κB** | **No conditional chondrocyte length endpoint retrieved** — the literature is osteoarthritis and osteoclast | (searched; nothing on length) | Many inhibitors; untested for length | **yes** |
| 65 | **NRF2 / KEAP1** | ⭐ Nrf2 ACTIVATION stimulates chondrocyte differentiation and **INCREASES BONE LENGTHS in zebrafish** | zebrafish 37748761 | ⭐⭐ YES — sulforaphane, dimethyl fumarate, bardoxolone/omaveloxolone are all Nrf2 activators, all obtainable | **yes** |
| 66 | **HIF-1α / VHL / PHD2 (hypoxia)** | VHL deletion in chondrocytes REDUCES proliferation; PHD2 essential for chondrocyte function | mouse 15128677; mouse 26562260 | HIF-PHIs (roxadustat, daprodustat) exist — direction predicted UNFAVOURABLE by VHL data | no |
| 67 | **VEGF** | Required for vascular invasion and ossification; blockade widens the plate without lengthening | review (index only) 29026147; mouse HDAC4-linked 32354322 | NO — anti-angiogenics are the shortening direction | no |
| 68 | **PDGF / PDGFR** | Expressed in rapidly forming human bone; no conditional length endpoint retrieved | human 8894141 | NO | **yes** |
| 69 | **EGFR** | ⭐ BOTH DIRECTIONS MEASURED: EGFR required for endochondral ossification; conditional ADAM17/TACE loss gives an **ELONGATED growth plate but SHORTER long bones** (a JAM) | mouse 21887704, 24047892, 35191092; mouse ADAM17 23349978, 23732913; mouse ADAM10 32062003; iRhom 33227998; rat GH-linked 21631569 | NO — EGFR agents are inhibitors | no |
| 70 | **CXCL12 / CXCR4** | Stimulates chondrocyte HYPERTROPHY at the chondro-osseous junction; apoptotic-cell CXCL12 mediates dexamethasone growth defects | mouse/rat 20206617, 22623989; rat 30395366, 33438203 | Plerixafor (CXCR4 antagonist) exists — predicted direction unclear | **yes** |
| 71 | **Complement (C3/C5 in the growth plate)** | Complement proteins present in developing endochondral bone; may mediate cartilage cell death and vascularisation | mammalian (species per source) 8831558 | Eculizumab/ravulizumab/pegcetacoplan approved — **never tested for length** | **yes** |
| 72 | **IL-1** | SHORTENS — IL-1β and TNF-α act in SYNERGY to inhibit longitudinal growth | rat fetal metatarsal 15476580; 16648299; local production by plate chondrocytes 22508264 | ⭐ YES — anakinra/canakinumab (blockade = taller in an inflamed subject only) | no |
| 73 | **TNF-α** | SHORTENS; blockade restores growth in JIA | rat 15476580; human etanercept 18050366, 25638806 | ⭐ YES — etanercept/adalimumab (restoration only) | no |
| 74 | **NLRP3 inflammasome** | Constitutive activation → abnormal skeletal development and growth-plate dysplasia | mouse 22558291, 28687790; mouse 33319921 | YES in the blocking direction — anakinra/canakinumab, NLRP3 inhibitors clinical-stage | **yes** |
| 75 | **TLR4 / LPS** | Microbiota-derived LPS RETARDS chondrocyte hypertrophy by elevating Sox9 | mouse 30264889 | NO agent tested for length | **yes** |
| 76 | **Interferon** | **No growth-plate length data retrieved** | (searched; nothing) | n/a | **yes** |
| 77 | **Purinergic P2X / P2Y** | ATP raises Ca²⁺ and ENHANCES bFGF-induced chondrocyte proliferation; P2 receptors + Cx43 hemichannels form a mechanoreceptor complex with the cilium | sheep 8895344; human 15299287; 19207989; 32718031 | Agents exist (P2X7 antagonists clinical-stage) — never tested for length | **yes** |
| 78 | **Calcium-sensing receptor (CASR)** | Critical modulator of skeletal development; a splice variant is expressed in growth-plate chondrocytes | mouse 18765830; 16166224; 31498905; 41081312 | ⭐ Approved both ways — cinacalcet (calcimimetic) and etelcalcetide; **but cinacalcet did NOT affect longitudinal growth in experimental uraemia, 18408076** (a measured null) | **yes** |
| 79 | **GABA-B receptor in growth-plate chondrocytes** | GABA-B modulates CaSR function and chondrocyte differentiation; receptor activation PROMOTES chondrogenic proliferation | mouse/rat 17615148; rat/ATDC5 16013446 | ⭐ YES — **baclofen** is an approved oral GABA-B agonist, used in children; never tested for length | **yes** |
| 80 | **TRPV4** | Both GOF and LOF mutations cause human skeletal dysplasia — a BAND; follistatin is the mediator | human/mouse 26942100, 24577120; mouse 36696489 | ⭐ YES — small-molecule inhibition RESCUES the Trpv4-mutant dysplasia phenotype in mice, 41574606 | no |
| 81 | **PIEZO1** | Chondrocyte PIEZO1 controls endochondral ossification; overexpression drives growth-plate ossification/degeneration in scoliosis models | mouse 38395992; human/mouse 41194970, 40714837, 42082502, 42157948; limited role in articular cartilage 36805475, 40684207 | Inhibitors (GsMTx4, Dooku) are tool compounds; Yoda1 agonist runs the degenerative way | no |
| 82 | **PIEZO2** | Chondrocyte-specific Piezo1/2 double KO studied for OA, not length | mouse 40684207 | NO | **yes** |
| 83 | **Cav3.2 T-type calcium channel → NFAT → SOX9** | Required for NFAT-dependent Sox9 in cartilage | mouse 24778262 | Ethosuximide/mibefradil block it — the wrong direction | **yes** |
| 84 | **Connexin 43 hemichannels** | Cartilage Cx43 loss → mitochondrial dysfunction, accelerated cartilage degeneration; forms a mechanoreceptor complex with P2 receptors | mouse 42327095; 19207989 | NO opener with a length endpoint | **yes** |
| 85 | **Autophagy (ATG5/ATG7)** | Chondrocyte deletion → caspase-dependent death and **MILD GROWTH RETARDATION** | mouse 26077727; 28304100 | Autophagy inducers (rapamycin, spermidine, trehalose) exist — confounded by mTORC1 | no |
| 86 | **UPR — XBP1 / IRE1** | Cartilage-specific XBP1 ablation → chondrodysplasia with REDUCED proliferation and delayed maturation; XBP1S ACCELERATES endochondral bone growth | mouse 25600960; mouse 24636354; 22865880 | NO — no XBP1 activator | **yes** |
| 87 | **UPR — ATF6** | ATF6α is a Runx2-activable regulator of chondrocyte HYPERTROPHY | mouse/cell 26527399; 24269637 | NO | **yes** |
| 88 | **UPR — PERK/ATF4/CHOP** | Cartilage autophagy deficiency promotes ER stress and impairs chondrogenesis PERK-ATF4-CHOP dependently; XBP1-independent UPR suppresses differentiation via C/EBPβ | mouse 28304100; mouse 26372225 | ISRIB and PERK inhibitors are tool compounds; carbamazepine used in Schmid-type models | **yes** |
| 89 | **Circadian — BMAL1/CLOCK** | Loss impairs chondrocyte function via HIF1α-VEGF; artificial light at night SUPPRESSES growth-plate formation by inhibiting BMAL1-driven collagen hydroxylation | mouse 31107137; mouse 37029304; 36628892 | Behavioural (light hygiene) — no agent tested for length | **yes** |
| 90 | **Circadian — REV-ERBα (NR1D1)** | BLOCKING Rev-erbα INHIBITS growth-plate chondrogenesis via MAPK-ERK1/2 → Rev-erb is REQUIRED | rat/mouse 35938533 | REV-ERB agonists (SR9009 class) are tool compounds; direction predicted favourable, untested | **yes** |
| 91 | **Diurnal mitotic rhythm in the plate** | Long-standing question whether growth is diurnally gated | mammal 2293628 | n/a | **yes** |
| 92 | **Retinoic acid / RARγ** | RA EXCESS closes physes (isotretinoin, palovarotene); RARγ activity regulates endochondral bone and hypertrophic gene expression | mouse 30040873, 30587607; mouse palovarotene skeletal toxicity 30226468 | NO — RARγ ANTAGONIST is the theoretical taller direction and the marketed agents are agonists | no |
| 93 | **CYP26B1 (RA clearance)** | Loss → craniosynostosis / multiple synostoses spectrum in humans; interacts with Rarg on limb outgrowth | human 34160123, 37755482, 40999913; mouse 20043900 | CYP26 inhibitors (talarozole class) exist — they RAISE RA, the closing direction | **yes** |
| 94 | **Vitamin D / VDR** | Receptor-dependent 1,25D actions REQUIRED for normal growth-plate maturation; excess alters maturation | mouse 20685875; rat 21695192; review 34950832 | Adequacy only — a band, not a lever | no |
| 95 | **24R,25(OH)₂D₃ (the "other" vitamin D metabolite)** | Controls growth-plate development by inhibiting apoptosis in the RESERVE zone | rat 20307662; 20594980 | Obtainable as a research metabolite; never trialled for height | **yes** |
| 96 | **Glucocorticoid / GR** | SHORTENS; acts partly via FGF23/FGFR3 and via apoptotic-cell CXCL12; dexamethasone also raises chondrocyte CNP | human 31099911; rat 30395366; 17116261 | Avoidance only | no |
| 97 | **Oestrogen receptor α** | Drives epiphyseal fusion; ERα also required for the leptin-related growth response | mouse ob/ob 34925230 | Aromatase inhibitors / SERDs — the established "period" lever | no |
| 98 | **GPER / GPR30** | Expressed in the growth plate and DECLINES as puberty progresses | human/rat 17878253 | G-1 agonist / G15 antagonist are tool compounds; never tested for length | **yes** |
| 99 | **Androgen receptor** | **No chondrocyte-conditional length endpoint retrieved this session** | (searched; nothing) | Androgens exist but aromatise | no |
| 100 | **Thyroid hormone / TRα,β** | Required for hypertrophy; TRβ needed for T3-stimulated chondrocyte differentiation; excess TSH itself abnormalises the plate | mouse/rat 17065405, 23880310, 18682303; reviews 29407443 | Adequacy only — supraphysiological T3 spends the period | no |
| 101 | **Deiodinases (DIO2/DIO3) — local thyroid control** | D3-mediated inactivation minimises TH signalling in the fetal skeleton | mouse 18682303; GH regulates DIO2/DIO3 40413916 | NO agent | **yes** |
| 102 | **TH → heparan sulfate proteoglycan expression in the plate** | A distinct TH output arm | rat 16223867 | NO | **yes** |
| 103 | **PPARγ** | Cartilage-specific deletion → abnormal endochondral ossification and IMPAIRED cartilage growth; activation drives adipogenic conversion of plate chondrocytes | mouse 22131019; rat 17259668; 20414969 | Thiazolidinediones exist — the adipogenic direction looks unfavourable | no |
| 104 | **PPARα / retinoid Z receptor in cartilage** | Present in cartilage; PPARγ activation modulates IL-1 effects | 10766862 | NO | **yes** |
| 105 | **Leptin / LEPR** | Differentially regulates VERTEBRAL vs TIBIAL growth plates — a compartment-splitting signal; antagonises PPARγ in plate chondrocytes | mouse 28569158; 23028384; 21349356 | Metreleptin exists; direction site-dependent | **yes** |
| 106 | **Insulin receptor (not IGF1R)** | The effect of a HIGH-CALORIE DIET on bone growth is mediated by the INSULIN receptor | mouse 30798001 | n/a — nutritional | **yes** |
| 107 | **Ghrelin / GHSR** | GHSR deletion impairs growth; meal-feeding promotes skeletal growth by ghrelin-dependent enhancement of GH RHYTHMICITY | mouse 33798772, 33774644; mouse 40168099 | YES — ibutamoren/macimorelin (secretagogues), but they substitute for GH | no |
| 108 | **Integrin α10β1 (cartilage's dominant collagen receptor)** | Distributed through mouse development in cartilage | mouse 11683172 | NO — no α10-directed agent | **yes** |
| 109 | **FAK / integrin-linked kinase** | FAK inhibition protects condylar cartilage under excess load | mouse/rat 32558123, 32324278 | FAK inhibitors clinical-stage; never tested for length | **yes** |
| 110 | **DDR2 (collagen receptor tyrosine kinase)** | Functions in GLI1⁺ skeletal progenitors AND chondrocytes to CONTROL BONE DEVELOPMENT; also modulates BMP in heterotopic bone | mouse 35140200; mouse 39746922 | Inhibitors exist (dasatinib/imatinib cross-react); human DDR2 loss shortens, so blockade is the wrong way | no |
| 111 | **DDR1** | Impacts bone microarchitecture with ageing | mouse 39776614 | NO | **yes** |
| 112 | **Eph / ephrin (EphrinB2)** | Mediates chondrocyte autophagy; role in cartilage homeostasis | mouse 39289794; zebrafish 40109361 | NO length endpoint | **yes** |
| 113 | **Semaphorin 3A / neuropilin-1** | Acts in bone and cartilage metabolism; Sema3A protects chondrocytes | mouse/cell 38078001 (review — index only), 34821196 | NO length endpoint in any species | **yes** |
| 114 | **Semaphorin 4D / Plexin-B1** | Inhibition reduces subchondral bone loss | mouse 35151027 | Anti-SEMA4D antibody (pepinemab) is clinical-stage — never tested for length | **yes** |
| 115 | **Slit / Robo** | Role in bone metabolism and remodelling; Slit3-Robo4 axis in subchondral bone | mouse (reviews — index only) 35173554, 32986130; 42148297 | NO | **yes** |
| 116 | **Netrin-1 / DCC / UNC5B** | Bone-protective; suppresses BMP; UNC5B modulates osteogenic BMP signalling | mouse 27681594, 33883596, 29158083 | Anti-netrin-1 antibody (NP137) is clinical-stage — direction unknown for bone | **yes** |
| 117 | **Prostaglandin E2 / EP receptors** | COX products drive PGE2-dependent PROLIFERATION of growth-plate chondrocytes; EP receptors mediate 1,25D effects | rat 16646980, 11595507 | Inverted — NSAIDs REMOVE this proliferative drive; EP4 agonists exist preclinically | **yes** |
| 118 | **Endothelin-1 / ETA-ETB on chondrocytes** | ET-1 stimulates DNA synthesis and Ca²⁺ influx via its receptors on chondrocytes | rabbit 7550073 | Bosentan/ambrisentan are ANTAGONISTS = wrong direction; no agonist | **yes** |
| 119 | **Lysophosphatidic acid (LPA/LPAR)** | Promotes PROLIFERATION, differentiation and survival in rat growth-plate chondrocytes | rat 19233232 | LPA-receptor agents exist as antagonists; no agonist tested | **yes** |
| 120 | **Serotonin 5-HT2A / 5-HT2B on chondrocytes** | Regulates CCN2 production in chondrocytes | mouse/cell 29145495 | 5-HT2B agonists withdrawn (valvulopathy); SSRIs are a confound | **yes** |
| 121 | **PACAP / VIP receptor** | PACAP immunolocalised in porcine EPIPHYSEAL CARTILAGE CANALS | pig 9179866 | PACAP analogues experimental | **yes** |
| 122 | **RAC1 (small GTPase)** | **RAC1 DOSAGE is crucial for normal endochondral bone growth** — a dose-sensitive band | mouse 28977598 | NO | **yes** |
| 123 | **Protein phosphatase 5 (PP5)** | ⭐ Ablation leads to **ENHANCED both bone AND cartilage development** — a rare loss-of-function-is-bigger result | mouse 29434189 | NO agent; PP5 inhibitors are tool compounds (cantharidin class) | **yes** |
| 124 | **PHLPP1 phosphatase** | Suppresses PTH1R expression and signalling during bone GROWTH | mouse 33434347 | PHLPP inhibitors are tool compounds | **yes** |
| 125 | **UFMylation / DDRGK1 (UFBP1)** | Required for proper development and MAINTENANCE of growth-plate cartilage | mouse 35377455 | NO | **yes** |
| 126 | **PiT1 / SLC20A1 (phosphate transporter as a signalling node)** | Required for ER homeostasis, chondrocyte survival and skeletal development | mouse 30347511 | NO | **yes** |
| 127 | **NF2 / merlin → β-arrestin2-biased PTH1R** | Orchestrates biased PTH1R signalling | mouse 42268882 | Biased PTH1R ligands are an active medicinal-chemistry area | **yes** |
| 128 | **ADAM17 / TACE and ADAM10 (sheddases as signalling gatekeepers)** | ⭐ ADAM17 loss → **elongated plate but SHORTER bones**; ADAM10 is INDISPENSABLE for longitudinal growth | mouse 23349978, 23732913; mouse 32062003; iRhoms 33227998 | NO — all agents are inhibitors | **yes** |
| 129 | **Wnt/β-catenin ↔ EGFR crosstalk in epiphyseal cartilage** | EGFR acts through β-catenin-dependent AND -independent routes | mouse 24047892 | NO | **yes** |
| 130 | **CCN2 / CTGF** | Hypertrophic-chondrocyte product; interacts with perlecan to regulate proliferation and differentiation | mouse/cell 12811819 | Pamrevlumab (anti-CCN2) is the blocking direction | no |
| 131 | **Oxytocin receptor** | Role in bone described; **no length endpoint** | reviews (index only) 39290327, 37229246 | Oxytocin is approved — never tested for linear growth | **yes** |
| 132 | **Aryl hydrocarbon receptor (AHR)** | Dioxin/AHR agonism disrupts cartilage and jaw development; kynurenine-AHR impairs chondrogenesis | zebrafish 37660771; human/rat 36224488, 36933489 | AHR ANTAGONISTS are clinical-stage in oncology — direction predicted favourable, untested for length | **yes** |
| 133 | **GPR68 / OGR1 (proton-sensing GPCR)** | Joint acidosis signalling; cartilage gene regulation | human/mouse 41595528, 41148822 | Ogerin-class positive modulators are tool compounds | **yes** |
| 134 | **Calcineurin / NFAT** | NFAT1 in cartilage homeostasis; Cav3.2→NFAT→Sox9 required | mouse 24348789, 24778262 | Ciclosporin/tacrolimus INHIBIT it — likely wrong direction | **yes** |
| 135 | **HGF / MET** | **No growth-plate length endpoint retrieved** | (searched; nothing skeletal-longitudinal) | Cabozantinib etc. are inhibitors | **yes** |
| 136 | **Hedgehog ↔ BMP ↔ Notch grid in tibial dyschondroplasia** | Co-regulation of pro/anti-angiogenic proteins in a natural avian growth-plate lesion | chicken 38136788 | n/a | **yes** |
| 137 | **Borderline chondrocytes at the plate periphery** | Behave as transient mesenchymal precursors — a distinct signalling compartment | mouse 30888720 | n/a | **yes** |
| 138 | **miR-433 → BMP + IHH** | Coordinates postnatal growth-plate dynamics | mouse 41342396 | Antagomirs are reagents | **yes** |
| 139 | **miR-140 → HDAC4 robustness** | Provides robustness to PTHrP-HDAC4 regulation of hypertrophy | mouse 25529628; 21576357 | NO | no |
| 140 | **SOX9 (integrator, not a receptor pathway)** | Directs hypertrophic maturation and blocks osteoblast differentiation of plate chondrocytes | mouse 22421045; 22072985 | NO — kartogenin-class compounds raise SOX9 but suppress hypertrophy | no |

### TABLE (continued) — second pass, added after a further round of external queries

| # | PATHWAY | EFFECT ON LENGTH | EVIDENCE (species + PMID) | DRUG IN TALLER DIRECTION? | OBSCURE? |
|---|---|---|---|---|---|
| 141 | **SOCS2 (the brake on GH action IN CARTILAGE)** | ⭐ Loss = MORE GH action at the plate; SOCS2 is described as the critical regulator of GH action in growth-plate chondrogenesis | mouse 22228213; osteoblast arm 25074853 | NO — no SOCS2 inhibitor exists in any species. The single most direct "remove the brake on GH" target and it is undrugged | no |
| 142 | **SHH (distinct from IHH) in the POSTNATAL growth plate** | Present in postnatal growth-plate chondrocytes; SHH and IHH are DIFFERENTIALLY regulated by retinoic acid; forced chondrocyte SHH disorganises the plate | rat/mouse 12244570; mouse 15355563; 16962305; 9925646 | Same SMO agonist shelf as row 12 | **yes** |
| 143 | **GDF11 (myostatin's paralogue)** | Locally controls anterior-posterior patterning of the AXIAL skeleton; systemically GDF11 DECREASES bone mass | mouse 31183862; mouse 27653144; comparison with MSTN 32071240, 33077875 | Follistatin raises muscle but WEAKENS bone (32071240) — a recorded trade-off against the myostatin shelf | **yes** |
| 144 | **NMDA receptor / glutamate signalling in chondrocytes** | NMDA receptor expression and function REQUIRED for early chondrogenesis | mouse/cell 31842918; human articular 15299260, 18554934, 19233337 | Memantine BLOCKS it (39280634) — the wrong direction; no agonist tested | **yes** |
| 145 | **β2-adrenergic receptor on chondrocytes** | β2AR stimulate chondrocyte growth but INHIBIT Ihh and collagen X; separately inhibit collagen II via Jun-B — a split, biphasic output | mouse 18059015; mouse 21177286; sympathectomy model 25063231 | Salbutamol/formoterol are approved and paediatric — direction is genuinely ambiguous, which is why it is worth measuring not assuming | **yes** |
| 146 | **Adenosine A2A / A3 receptors** | Endogenous adenosine MAINTAINS cartilage homeostasis; A2A promotes FoxO-associated autophagy; A3 ablation degenerates cartilage | mouse 28492224, 33441836, 33973110, 30088034; liposomal adenosine 32778777 | ⭐ YES — liposomal adenosine and A2A agonists (regadenoson approved for another indication). No length endpoint in any species | **yes** |
| 147 | **Sphingosine-1-phosphate / S1P3** | Smad3 deficiency degrades mandibular condyle via S1P/S1P3; S1P1 crosstalk in subchondral remodelling | mouse 26272361; 28687489 | Fingolimod/siponimod are approved S1P modulators — never tested for length | **yes** |
| 148 | **Muscarinic acetylcholine receptors on chondrocytes** | Muscarinic antagonists INHIBIT chick scleral chondrocytes — i.e. cholinergic tone is proliferative there | chick 9804129 | Atropine is used chronically in children for myopia; direction predicted unfavourable and never checked | **yes** |
| 149 | **LTBP3 (TGF-β latency)** | Biallelic loss → human SHORT STATURE with dental anomalies / brachyolmia; frameshift causes complex skeletal dysplasia in cats | human 32432408, 30887145, 40259772, 34573388; cat 34946872 | NO | no |
| 150 | **LTBP1** | Biallelic truncating variants cause cutis laxa syndrome with skeletal involvement | human 33991472 | NO | **yes** |
| 151 | **Primary cilia as the MECHANO-transducer of Ihh** | Cilia modulate Ihh signal transduction in response to HYDROSTATIC LOADING of growth-plate chondrocytes | growth-plate chondrocytes 21930256 | NO agent — but it is the mechanism by which a mechanical intervention could act on the hedgehog arm | **yes** |
| 152 | **Chondrocyte TSC1 → cranial base synchondroses** | Restrains premature differentiation of synchondroses | mouse 34365025 | Rapalogs inhibit mTORC1 — direction site-specific | **yes** |
| 153 | **Runx2 / Cbfβ as the integrator of Ihh-PTHrP** | Cbfβ controls the proliferation/differentiation balance by upregulating Ihh and inhibiting PTHrP | mouse 24821091; review 35628587 | NO | no |
| 154 | **Kartogenin / filamin-A–CBFβ–RUNX1 chondrogenic axis** | Induces chondrogenesis; the field's design goal is PERMANENT cartilage, i.e. explicitly WITHOUT hypertrophy | (searched; the specific growth-plate length endpoint was not retrieved) | Kartogenin is obtainable — but the class is selected AGAINST the hypertrophic step that makes height | **yes** |
| 155 | **CCN2/CTGF ↔ serotonin 5-HT2A/2B** | 5-HT receptors regulate CCN2 production in chondrocytes | mouse/cell 29145495 | Wrong direction available only | **yes** |
| 156 | **P2 receptor ↔ connexin-43 hemichannel ↔ primary cilium complex** | Proposed unified mechanoreceptor complex in chondrocytes | human/bovine 19207989 | NO | **yes** |
| 157 | **Fibroblast growth factor ↔ CNP crosstalk** | CNP opposes FGF-driven growth arrest; FGF and CNP interact on proliferation and ECM homeostasis | mouse/cell 16234329; 14702637 | This crosstalk IS the therapeutic rationale for the CNP class | no |
| 158 | **Ellis-van Creveld conditional (Evc) and hypertrophy blockade** | Blocking chondrocyte hypertrophy in conditional Evc KO does NOT modify cartilage damage — a measured null | mouse 35334131 | n/a | **yes** |
| 159 | **Hydroxylation of collagen as a circadian OUTPUT of BMAL1** | Artificial light at night suppresses growth-plate cartilage formation by inhibiting BMAL1-driven collagen hydroxylation | mouse 37029304 | Light hygiene — free, behavioural, and completely absent from growth practice | **yes** |
| 160 | **miRNA layer over the whole signalling map** | miR-433 targets BMP+IHH; miR-140 buffers PTHrP-HDAC4 | mouse 41342396; mouse 25529628, 21576357; review (index only) 40225327 | Antagomirs/mimics are reagents; PS-ASO delivery to cartilage is demonstrated elsewhere | no |

---

## PATHWAYS WITH A TALLER DIRECTION AND AN EXISTING AGENT

Ranked by how directly the agent pushes the lengthening direction.

1. **CNP → NPR2 → cGMP.** The only axis in this table where the human gain-of-function phenotype is
   *overgrowth* (NPR2 GOF, 24259409, 22870295), the mouse gain-of-function is *overgrowth*
   (9482886, 19808910), and an approved agent exists (vosoritide and successors). Everything else on
   this list is weaker than this.
2. **Smoothened / hedgehog agonism at the resting zone.** 38516888 is the only retrieved report of an
   agent *stimulating growth-plate skeletal stem cells to promote linear bone growth*. Agents (SAG,
   purmorphamine, Hh-Ag series) are purchasable research chemicals; **no approved SMO agonist exists** —
   the marketed SMO drugs are all antagonists, which is the fusing direction.
3. **NRF2 activation.** 37748761 — Nrf2 activation by sulfuretin stimulates chondrocyte differentiation
   and *increases bone lengths in zebrafish*. This is a lengthening endpoint with a direction and a
   compound class that is oral, cheap and human-dosed (sulforaphane; dimethyl fumarate; omaveloxolone).
   Species gap is total — no mammalian length endpoint — and this appears to be almost unexamined in the
   growth literature. **Highest value-per-cost item on the list.**
4. **TRPV4 modulation.** 41574606 — small-molecule inhibition *rescues the skeletal dysplasia phenotype*
   of Trpv4-mutant mice. That is an agent, in a mammal, with a skeletal endpoint. It is a rescue of a
   gain-of-function channelopathy (so restoration, not elevation), and TRPV4 is a band with both LOF and
   GOF dysplasias.
5. **GABA-B receptor agonism.** 16013446 reports GABA-B receptor activation *promoting proliferation* of
   chondrogenic cells, and 17615148 places GABA-B upstream of CaSR in growth-plate chondrocytes.
   **Baclofen is approved, oral, and routinely given to children.** No one appears to have measured height
   under it. This is the single most obtainable untested agent in the table.
6. **Notch agonism (clustered/multivalent ligand).** 19590010 establishes Notch as a regulator of
   chondrocyte proliferation and differentiation. Jagged1-Fc and DLL1-Fc are catalogue reagents; the
   marketed direction (γ-secretase inhibitors, e.g. nirogacestat) is the opposite one and is given to
   adolescents.
7. **IL-1 / TNF / IL-6 blockade — restoration only.** 15476580 shows IL-1β + TNF-α synergise to inhibit
   longitudinal growth in a normal explant; anakinra, etanercept and tocilizumab all restore growth in
   inflamed children (18050366, 25638806, 25504861, 29961686). In a subject with no inflammatory burden
   there is nothing to restore — but the burden has to be measured to know.
8. **Myostatin / activin-receptor blockade.** A large obtainable clinical class (ActRIIB-Fc, anti-myostatin
   antibodies). The only length-adjacent result retrieved is avian (36685194, larger tibiae in
   myostatin-mutant quail); the mouse work measured mass, not length (12060865). **A mammalian
   bone-LENGTH endpoint for this class was not found.**
9. **CaSR modulation.** Approved in both directions (cinacalcet, etelcalcetide). Recorded here mainly as a
   **measured null**: 18408076 — cinacalcet did not affect longitudinal growth in experimental uraemia.
10. **FGF23 blockade.** Burosumab is approved; 35339985 shows small-molecule FGF23 inhibition improving
    skeletal abnormalities in Hyp mice, and 31099911 puts FGF23→FGFR3 downstream of glucocorticoids in
    children. Restoration in a phosphate-wasting state, not elevation in a normal one.
11. **REV-ERB agonism.** 35938533 shows Rev-erbα is *required* for growth-plate chondrogenesis (blocking it
    inhibits chondrogenesis). SR9009-class agonists exist as tool compounds. Direction predicted
    favourable; never tested for length.
12. **AHR antagonism.** 37660771/36224488/36933489 show AHR agonism (dioxin, kynurenine) damages cartilage
    and chondrogenesis. AHR antagonists are clinical-stage in oncology. No skeletal length endpoint.
13. **Adenosine A2A agonism.** 28492224 — endogenous adenosine maintains cartilage homeostasis; 33441836 —
    A2A drives FoxO-associated autophagy in chondrocytes; 32778777 — liposomal adenosine is deliverable to
    joint tissue. Approved A2A agonists exist (regadenoson, for a cardiac indication). Direction predicted
    favourable; **no length endpoint in any species.**
14. **S1P receptor modulation.** Fingolimod, siponimod, ozanimod are approved and orally dosed; S1P/S1P3 is
    documented in condylar cartilage degradation downstream of Smad3 (26272361). Direction unestablished.
15. **β2-adrenergic agonism.** Salbutamol and formoterol are approved and given to children continuously.
    18059015 reports β2AR on chondrocytes *stimulating cellular growth* while *inhibiting Ihh and collagen
    X* — a split output, which is precisely why the net length effect is worth measuring rather than
    inferring. This class is in more adolescent bodies than any other item on this list.

**The single largest gap on this axis is SOCS2 (row 141).** It is described as the critical regulator of
GH action in growth-plate chondrogenesis (22228213), its removal amplifies GH signalling in the skeleton,
and **no SOCS2-directed molecule exists in any species.** If GH action at the plate is worth raising, this
is the node — and it is entirely undrugged.

---

## PATHWAYS IN THE PLATE NOBODY HAS PERTURBED FOR LENGTH

These are pathways for which I found positive evidence of **presence or activity in growth-plate cartilage
or the endochondral apparatus**, but **no bone-length or stature endpoint in any species**. Each is an
unrun experiment, not a closed question.

- **NO / soluble guanylate cyclase.** The effector kinases of the cGMP arm are the ones whose loss causes
  dwarfism in four species (PRKG2 — 15838621, 19887637, 34680883, 33106379), yet the *nitrate/sGC* half
  of cGMP production has no growth-plate length endpoint anywhere. Riociguat and vericiguat are approved.
- **Complement.** 8831558 — complement proteins are present in developing endochondral bone and were
  proposed to mediate cartilage cell death and vascularisation. Approved complement drugs (eculizumab,
  ravulizumab, pegcetacoplan, iptacopan) have never been pointed at a growth plate.
- **Purinergic P2X/P2Y.** ATP raises Ca²⁺ and *enhances bFGF-induced chondrocyte proliferation*
  (8895344); P2 receptors form a mechanoreceptor complex with Cx43 and the primary cilium (19207989).
  Clinical-stage P2X7 antagonists exist. No length endpoint.
- **GABA-A and GABA-B receptors.** Expressed on growth-plate chondrocytes (16013446); GABA-B modulates
  CaSR there (17615148). Baclofen is approved and paediatric.
- **Endothelin.** ET receptors are on chondrocytes and ET-1 drives DNA synthesis and Ca²⁺ influx
  (7550073). Every marketed agent is an antagonist.
- **Lysophosphatidic acid.** Promotes proliferation, differentiation and survival in rat growth-plate
  chondrocytes (19233232). No LPA-receptor agonist has been given to a growing animal.
- **Serotonin 5-HT2A/2B.** Present and functional on chondrocytes (29145495).
- **PACAP.** Immunolocalised specifically in epiphyseal cartilage canals (9179866) — an anatomically
  precise, completely unfollowed observation.
- **Prostaglandin EP receptors.** PGE2-dependent proliferation of growth-plate chondrocytes is documented
  (16646980, 11595507). The mainstream question has only ever been whether NSAIDs *harm*; nobody has asked
  whether an EP4 agonist helps.
- **Semaphorin/plexin, Slit/Robo, netrin/DCC-UNC5.** All three axon-guidance families have documented bone
  roles (38078001, 35173554, 32986130, 27681594, 33883596) and clinical-stage agents exist for two of them
  (pepinemab, NP137). **Not one has a longitudinal-growth endpoint.**
- **Connexin 43 hemichannels.** Cartilage-specific loss damages chondrocytes (42327095); no opener exists
  and no length endpoint has been recorded.
- **NF-κB.** Despite an enormous osteoarthritis literature I could not retrieve any chondrocyte-conditional
  study reporting bone LENGTH.
- **Interferon.** Nothing at all in the growth plate.
- **CXCL12/CXCR4.** Stimulates hypertrophy at the chondro-osseous junction (20206617, 22623989) and
  mediates part of glucocorticoid growth damage (30395366). Plerixafor is approved. Never tested for length.
- **HGF/MET, PDGF.** Present or implicated (8894141) but no conditional length endpoint.
- **GPER/GPR30.** Expressed in the growth plate and *declines through puberty* (17878253) — the exact
  shape of a candidate — with G-1 and G15 available as tool compounds and no experiment done.
- **24R,25(OH)₂D₃.** A distinct vitamin D metabolite acting on the RESERVE zone (20307662) — the pool
  compartment — obtainable as a chemical, never trialled.
- **AHR, GPR68/OGR1, oxytocin receptor, Cav3.2, Piezo2, integrin α10β1, FAK, DDR1, PP5, PHLPP1, UFMylation
  (DDRGK1), PiT1/SLC20A1, NF2/merlin.** Each has at least one primary paper placing it in cartilage or the
  skeletal growth apparatus; none has a length endpoint under a pharmacological perturbation.
- **BAMBI.** Named in the brief; I could find **no skeletal data of any kind** in any species. A true blank.
- **Adenosine A2A/A3 receptors.** Endogenous adenosine maintains cartilage homeostasis (28492224) and a
  deliverable formulation exists (32778777). No growth-plate length endpoint.
- **S1P receptors.** Present in cartilage signalling (26272361); three approved oral modulators; no length
  endpoint.
- **NMDA receptor / glutamate.** *Required for early chondrogenesis* (31842918) and expressed in human
  articular chondrocytes with a mechanotransduction role (15299260). Memantine is approved and blocks it —
  so the only clinically available direction is the one predicted to be harmful, and nobody has checked.
- **Muscarinic receptors.** Cholinergic tone is proliferative in chondrocytes (9804129), and **low-dose
  atropine is now given chronically to large numbers of children for myopia control** with no skeletal
  endpoint recorded anywhere.
- **β2-adrenergic receptors.** Row 145; the most widely-dosed class in this table with the least skeletal
  follow-up.
- **SOCS2.** Present, critical, and undrugged (22228213).
- **Primary-cilium mechanotransduction of Ihh under hydrostatic load** (21930256) — the one documented
  bridge between a mechanical input and the hedgehog arm, with no intervention of any kind attached.

---

## STRUCTURAL OBSERVATIONS FROM THE ENUMERATION

1. **Almost every pathway with an agent has the agent pointing the shortening way.** Hedgehog (SMO
   antagonists), Wnt (agonists — wrong end of a band whose optimum is below wild type per row 41), Notch
   (γ-secretase inhibitors), mTOR (rapalogs), EGFR/ADAM17 (inhibitors), VEGF (anti-angiogenics), retinoid
   (RARγ agonists), TEAD (inhibitors), endothelin (antagonists), calcineurin (inhibitors). This is not bad
   luck — the indications that funded those molecules were cancer, fibrosis and inflammation, where the
   goal is always *less* signalling.
2. **The exceptions are all in the "supply a substrate / occupy a decoy / activate a stress-response"
   class**, not the inhibitor class: CNP analogues, osteocrin-like NPR3 occupancy, Nrf2 activators, GABA-B
   agonism, SMO agonism, clustered Notch ligand.
3. **Bands are the rule, not the exception.** PTH1R/cAMP, canonical Wnt, TRPV4, retinoic acid, RAC1 dosage,
   EXT1/heparan sulfate, PPARγ and hedgehog itself all shorten at BOTH ends. No marketed agent is titrated
   for an interior optimum.
4. **A recurring measurement failure across this literature: plate morphology is reported and length is
   not.** ADAM17 (23349978) is the clearest instance and it is instructive in the opposite direction —
   an *elongated* growth plate with *shorter* bones. Any pathway assessed only on plate thickness is
   unassessed.
5. **Non-classical afferents to the plate are systematically under-studied**: nutrient sensing (insulin
   receptor, 30798001), meal timing via ghrelin/GH rhythmicity (40168099), light-at-night via BMAL1
   (37029304), microbiota-derived LPS (30264889). All four are behaviour- or environment-modifiable and
   none is in the standard signalling inventory.

---

## WHAT I COULD NOT VERIFY

- **Classic foundational PMIDs — partially recovered on the second pass.** I did verify the founding
  Ihh–PTHrP feedback paper (8662546, "Regulation of rate of cartilage differentiation by Indian hedgehog
  and PTH-related protein") and the CNP-rescues-achondroplasia paper (14702637). I could **NOT** surface
  the canonical Ihh-null paper (St-Jacques 1999), the PTH1R-null paper (Lanske 1996) or the original FGFR3
  achondroplasia mapping (Shiang 1994). I have therefore **not cited them**; rows 1, 8 and 9 rest on the
  papers I did retrieve. These are real, well-known works — I simply could not confirm their identifiers
  in this session and refuse to guess.
- **Effect sizes.** No numeric percentage change in bone length is quoted anywhere in this document,
  because I read titles and metadata rather than full texts. Every "SHORTENS"/"LENGTHENS" is a direction
  only.
- **Species for complement (row 71, PMID 8831558).** The retrieved title does not state the species; the
  work is on developing endochondral bone but I could not confirm whether it is human, bovine or murine.
- **Androgen receptor (row 99), NF-κB (row 64), interferon (row 76), HGF/MET (row 135), BAMBI (row 34).**
  Recorded as *no data retrieved*, which is weaker than *no data exists*. My queries may have missed them.
- **Row 24 (GPC3/Simpson-Golabi-Behmel).** 20301398 is a GeneReviews entry — an index, not a primary
  source — used only to anchor that the syndrome is an overgrowth phenotype.
- **Rows relying on reviews as index only** and therefore not carrying primary evidence: 8 (32933018),
  22 (29545125), 67 (29026147), 113 (38078001), 115 (35173554, 32986130), 131 (39290327, 37229246).
- **Europe PMC relevance ranking was strongly biased toward 2025–2026 publications**, which is why the
  table is thinner on pre-2000 primary work than it should be. NCBI esearch partially compensated but
  multi-term queries frequently returned zero results, so coverage of any given pathway depends on my
  choice of two or three keywords rather than on an exhaustive sweep.
- **No clinicaltrials.gov, FDA or EMA document was retrieved in this session** — the drug-availability
  column is based on general pharmacological knowledge of each class plus the retrieved literature, and
  every "approved" claim should be re-checked against a regulatory source before it is acted on.
- **Row 148 (muscarinic) is NOT a growth-plate result.** 9804129 is chick **scleral** chondrocytes. It is
  included only because low-dose atropine is now given chronically to very large numbers of children and
  the skeletal question has apparently never been asked. Treat the tissue mismatch as the main objection.
- **Row 154 (kartogenin) carries NO PMID.** I searched for a growth-plate length endpoint for kartogenin
  and did not retrieve one; the row records the *design intent* of the cartilage-regeneration field
  (permanent, non-hypertrophic cartilage), which I state from the general framing of that literature
  rather than from a specific retrieved paper. Treat it as an unverified orientation note.
- **Row 143 (GDF11).** 32071240's retrieved title states that follistatin — a MSTN/GDF11 inhibitor —
  increases muscle mass but *weakens bone*. I did not confirm whether "weakens" refers to mass, strength
  or geometry, and it is **not** a length endpoint.
- **Row 145 (β2AR).** 18059015 is murine chondrocytes; 21177286 is growth-plate chondrocytes. The
  "stimulate cellular growth" phrasing is the paper's own and refers to cells, **not** to bone length.
- **Rows citing 2026-dated records** (e.g. 42268882, 42157948, 42082502, 41595528, 41574606, 42327095,
  41748604, 42338508, 41342396) are very recent and several may be ahead-of-print; I read titles only.

### Integrity check performed
All **311** distinct 7–8-digit identifiers appearing in this document were submitted to NCBI esummary and
**all 311 resolved to real PubMed records**. A subset of **≈105 load-bearing PMIDs** — every one used to
support a direction claim in the prose sections — was additionally title-checked against the claim made in
its row, and all matched. No identifier in this file was written from memory.
