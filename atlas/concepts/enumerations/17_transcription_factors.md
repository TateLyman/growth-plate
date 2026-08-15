# DOMAIN 17 — TRANSCRIPTION FACTORS AND THE GENE-REGULATORY NETWORK OF THE CHONDROCYTE
## R436 full-concept-space enumeration

**Method.** Enumerated by external search only (Europe PMC REST API, NCBI eutils efetch, WebSearch/
WebFetch). No file in `/home/user/growth-plate` was read other than the two briefs, so nothing here is
derived from the atlas's own prior conclusions. Species is stated in every row. PMIDs were returned by a
live query and, where a specific number or direction is quoted, the abstract was retrieved and read.
Where I could not verify, the cell says `UNVERIFIED` — see the final section.

**Reading the HEIGHT DIRECTION column.**
- **POSITIVE regulator** = the factor's presence/activity promotes longitudinal growth; losing it SHORTENS.
- **NEGATIVE regulator / BRAKE** = losing it LENGTHENS. These are the rows the project wants.
- **BAND** = both directions shorten (an interior optimum). These are traps, and there are many.
- **JAM** = loss expands the plate but the bone is shorter (charge without discharge).

---

## TABLE

| # | FACTOR / ELEMENT | ROLE | HEIGHT DIRECTION | HUMAN PHENOTYPE | MODULATABLE? HOW | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|---|
| 1 | **SOX9** | Master chondrocyte TF; HMG-box; binds paired CATTGT motifs; drives COL2A1, ACAN, COL9A1, COL11A2 | POSITIVE (required). Haploinsufficiency shortens; but SOX9 also *blocks* the hypertrophic exit, so over-expression is a JAM | Campomelic dysplasia (heterozygous LoF or upstream translocation) — bowed limbs, short stature, often lethal. Milder acampomelic form from breakpoints far upstream | ✗ No direct chemical. HMG-box is a minor-groove DNA binder with no pocket. Indirect only (FGF→MAPK raises Sox9; PKA phosphorylation; SUMO/ubiquitin). CRISPRa is the realistic route | 10319868 (mouse); 8001137 (human); 9121483 (enhancer); 11371614 (het mouse); 22421045 (hypertrophic block); 27128146 (review/index) | no |
| 2 | **SOX5 / SOX6 (L-SOX5, SOX6)** | Obligate SOX9 partners; no transactivation domain of their own; secure SOX9 occupancy at far-upstream enhancers | POSITIVE (required); double null = severe generalised chondrodysplasia in mouse | SOX5 haploinsufficiency = **Lamb–Shaffer syndrome** (neurodevelopmental; skeletal features variable). SOX6 human skeletal phenotype UNVERIFIED | ✗ None. Same HMG-box problem. Their value is as the SOX9-cofactor axis for a CRISPRa/enhancer approach | 18559420 (ACAN far-upstream enhancer, mouse); 26150426 (super-enhancers); 31578471 (SOX5 human) | no |
| 3 | **SOXC trio — SOX4 / SOX11 / SOX12** | Distinct from the SOX trio; act in perichondrium/pre-cartilage, promote non-canonical WNT | POSITIVE — SOXC induce growth-plate FORMATION in mouse embryos | SOX11 de novo variants = Coffin–Siris-like with growth restriction; SOX4 variants = neurodevelopmental disorder | ✗ None direct | 25761772 (mouse); 30661772, 34205270 (human); 31288943 ("SOXopathies" index) | **yes** |
| 4 | **RUNX2 (CBFA1)** | Drives chondrocyte hypertrophy (Col10a1, Mmp13, Vegfa, Ihh) and osteoblast commitment | BAND. Loss delays hypertrophy → shorter; excess accelerates hypertrophy → spends the plate. Perichondrial RUNX2 *inhibits* proliferation and hypertrophy | Cleidocranial dysplasia (haploinsufficiency) — **short stature is part of the phenotype**, clavicular aplasia, delayed fontanelle closure | ⚠ Partial. RUNX2 acts through **CBFB**, and the CBFβ interface is the only drugged node in the family (AI-10-49 class, built for CBFβ-SMMHC in inv(16) AML). Not selective for RUNX2 | 11857736 (human); 17050674 (perichondrial Runx2 inhibits, mouse); 23150948, 35628587 (index); 29958106, 27542261 (CBFβ chemistry) | no |
| 5 | **RUNX3** | Redundant with RUNX2 for hypertrophy; Runx2/Runx3 double null blocks hypertrophy almost completely | POSITIVE for hypertrophy (= h_term); redundancy means single knockout is uninformative | No isolated human skeletal phenotype recorded | ✗ Same CBFβ dependence as RUNX2 | 25715393, 27771362 (index) | **yes** |
| 6 | **RUNX1** | Earliest of the three; required for chondrogenic commitment / mesenchymal condensation | POSITIVE (early). Largely pre-natal | Familial platelet disorder with AML predisposition; no clear stature phenotype | ⚠ RUNX1 inhibitors exist as tool compounds in oncology; none skeletal | 28790107, 37697370 (oncology chemistry) | **yes** |
| 7 | **CBFB** | Obligate non-DNA-binding heterodimerisation partner for all three RUNX proteins; stabilises RUNX on DNA | POSITIVE (required) — removing CBFB removes all RUNX output at once | Human CBFB skeletal phenotype UNVERIFIED (CBFB is a leukaemia fusion partner) | ⭐ **The single best-drugged node in the RUNX arm.** Protein–protein interface, small-molecule tractable, clinical-stage chemistry exists in AML | 29958106; 33821975; 27542261 | **yes** |
| 8 | **SP7 / OSTERIX** | Zinc-finger, downstream of RUNX2; osteoblast commitment; also expressed in hypertrophic chondrocytes | POSITIVE for ossification. Loss = no bone; but the direction for LENGTH specifically is the discharge step | Recessive **osteogenesis imperfecta** from a frameshift; broader SP7-related bone fragility with short stature | ⚠ Cys2His2 zinc finger — the ONE TF class where degrader chemistry now exists (see row 78) | 20579626 (human); 23225263 (index) | no |
| 9 | **MEF2C** | Drives the hypertrophic program; the direct transcriptional output of the HDAC4/5 switch | POSITIVE for hypertrophy → for h_term, the largest term in longitudinal growth | MEF2C haploinsufficiency syndrome — neurodevelopmental; stature effect UNVERIFIED | ⚠ Only indirectly, via HDAC4/5 (class IIa HDAC inhibitors are pan-class and would de-repress MEF2C). No MEF2C-selective agent | 23284041, 26378079 (index) | no |
| 10 | **MEF2D** | Redundant partner of MEF2C in cartilage | POSITIVE (redundant) | None recorded | ✗ None | 25715393 (index) | **yes** |
| 11 | **HDAC4 (and HDAC5)** | Class IIa; not a TF but a MEF2 **co-repressor**; the PKA→SIK→HDAC4 phosphorelay controls its nuclear export | NEGATIVE regulator of hypertrophy — Hdac4-null mice ossify prematurely. But **Prx1-Cre Hdac4 deletion shortens limbs and closes the plate early**, so it is a BAND with no accessible interior | 2q37 deletion (brachydactyly–mental retardation) involves HDAC4 | ⚠ Class IIa HDAC inhibitors exist (TMP269, tool-grade); marketed HDAC inhibitors are pan-class and **givinostat is taken chronically by growing boys** | 26378079 (index) | no |
| 12 | **GLI1** | Hedgehog output; itself a Hh target so it reports pathway state | POSITIVE readout, largely non-essential (Gli1-null mice are viable) | None | ⚠ GANT61 and glabrescione B are GLI tool inhibitors (wrong direction for growth); no activator | 30754706, 34298625 (index) | no |
| 13 | **GLI2** | Principal Hh **activator** after SMO; full-length GLI2A | POSITIVE for Ihh output | GLI2 LoF = holoprosencephaly / pituitary anomalies with short stature (hypopituitarism route, not a plate route) | ✗ No activator. Upstream SMO agonists are the only handle | 34298625 (index) | no |
| 14 | **GLI3** | The **repressor**: proteolytically processed to GLI3R by PKA/GSK3/CK1 + βTrCP; the brake on Hh output | NEGATIVE — more GLI3R = less Hh output. Reducing GLI3R should raise Ihh output | Greig cephalopolysyndactyly, Pallister–Hall — polydactyly, not primarily stature | ⭐ **Uniquely tractable in principle: GLI3 processing is an enzymatic, PKA-dependent step, not a DNA-binding step.** Anything lowering PKA at the cilium shifts GLI3A:GLI3R. No selective agent exists | 30754706; 27713395 (5'Hoxd–Gli3 antagonism, mouse) | **yes** |
| 15 | **SUFU** | Intracellular Hh brake; sequesters GLI | NEGATIVE nominally — but chondrocyte Sufu loss **shortens** bone and destroys zonal order (the intracellular-brake trap) | Sufu LoF = medulloblastoma predisposition, Gorlin-like | ✗ No agent; and the direction is wrong in vivo | 34298625 (index) | no |
| 16 | **SMAD1 / SMAD5 (/SMAD8)** | BMP-receptor Smads | POSITIVE — Smad1/5 double deletion in chondrocytes blocks endochondral bone formation | No isolated human stature phenotype for SMAD1/5 | ✗ None direct; upstream ALK2/3 inhibitors exist (wrong direction) | 19224984 (mouse) | no |
| 17 | **SMAD2 / SMAD3** | TGF-β receptor Smads | Context-dependent. Smad3 loss → degenerative joint disease with altered hypertrophy | Somatic **SMAD3-activating** variants cause melorheostosis (focal hyperostosis) | ⚠ ALK5 inhibitors (galunisertib, vactosertib) act upstream; no Smad-selective agent | 32232430 (human somatic) | no |
| 18 | **SMAD4** | Common mediator for both arms | BAND with a striking human anchor: **SMAD4 gain-of-function = Myhre syndrome, SHORT stature with stiff joints and fibrosis** | Myhre syndrome (recurrent Ile500/Arg496 substitutions that stabilise SMAD4) | ⚠ The Myhre mechanism is **impaired SMAD4 ubiquitination/degradation** — i.e. a degradation-rate disease, which is exactly the axis a molecular glue acts on. Nothing built | 27302097, 24398790 (human) | no |
| 19 | **SMAD6 / SMAD7** | Inhibitory Smads; feedback brakes on BMP (SMAD6) and TGF-β (SMAD7) | NEGATIVE regulators of BMP/TGF-β output → in principle removing them raises signalling | SMAD6 LoF = craniosynostosis and radioulnar synostosis; SMAD7 stature phenotype UNVERIFIED | ✗ None | 30976276 (index) | **yes** |
| 20 | **β-catenin (CTNNB1) + TCF/LEF** | Canonical Wnt transcriptional output; TCF7L2/LEF1 provide DNA binding, β-catenin the activation domain | BAND with an interior optimum reportedly **below** wild type in cartilage; total ligand blockade exhausts the plate | CTNNB1 LoF = neurodevelopmental disorder; no clean stature direction | ⭐ Best-drugged node in this whole domain: **tankyrase inhibitors** (Axin stabilisers — basroparib/STP1002 class, human phase 1), **CBP/β-catenin antagonist PRI-724**, PORCN inhibitors upstream (wrong half) | 15132997 (Sox9–β-catenin, mouse); 38987555 (index) | no |
| 21 | **NFATC2 (NFATp)** | Calcineurin-dependent; a **repressor of chondrogenesis** in extra-articular tissue | NEGATIVE (repressor) — Nfatc2-null mice develop ectopic cartilage. Whether it restrains LENGTH is unknown | None recorded | ⚠ Calcineurin inhibitors (ciclosporin, tacrolimus) block all NFAT — non-selective, and tacrolimus/FKBP12 is separately a maturation-accelerating liability | 10620601 (mouse) | **yes** |
| 22 | **NFATC1 / NFAT5 (TonEBP)** | NFATC1 in osteoclasts; NFAT5 is the osmotic-stress TF that drives organic-osmolyte transporters | NFAT5 is the transcriptional arm of chondrocyte volume regulation → touches h_term | None recorded for stature | ✗ No NFAT5 activator exists | 32186512 (Piezo1–NFAT–YAP, mouse) | **yes** |
| 23 | **NF-κB (RELA, NFKB1, RELB)** | Inflammatory transcriptional output; suppresses growth-plate output in chronic inflammation | NEGATIVE in the inflamed state; direction in a healthy plate unclear | Chronic inflammatory short stature (IBD, JIA) is partly NF-κB-mediated | ⭐ **NF-κB decoy oligonucleotide has been dosed in humans**; upstream IL-1/IL-6/TNF blockade is approved and paediatrically dosed | 22719020 (STAT3 decoy, human first-in-human — the modality precedent) | no |
| 24 | **CREB1** | cAMP/PKA transcriptional output | Reported to expand the resting zone while **shortening** bone (a JAM). Lowering CREB is one described mechanism of FGFR3 inhibition | None isolated | ⚠ 666-15 is a CREB inhibitor tool compound; reported null in wild type | 32422296 (index) | no |
| 25 | **ATF4** | Osteoblast TF; also required for chondrocyte Ihh expression; downstream of RSK2 | POSITIVE | **Coffin–Lowry syndrome** (RSK2/RPS6KA3 LoF) — short stature; ATF4 is the effector | ✗ No direct agent | 17485283, 27002737 (index); 24418675 (BMP2→ATF4, chondrocyte) | **yes** |
| 26 | **CREB3L2 / BBF2H7** | ER-membrane-tethered TF, cleaved by S1P/S2P; drives **SEC23A** and the COPII machinery that exports procollagen II | POSITIVE and mechanistically specific: it sets the **secretory capacity** for type II collagen | **MBTPS1 (site-1 protease) deficiency causes human skeletal dysplasia** via this pathway | ⚠ S1P/S2P are proteases — enzymatically druggable in principle, but every existing agent inhibits (wrong direction) | 19767744 (mouse); 28500182; 24711445 (Sox9→BBF2H7); 30046013 (human MBTPS1) | **yes** |
| 27 | **XBP1 / ATF6** | UPR TFs; XBP1s drives the chondrocyte secretory program | POSITIVE (capacity) | ATF6 LoF = achromatopsia (eye, not bone) | ✗ None in the raising direction | 27002737 (index); 34737845 | **yes** |
| 28 | **HIF1A** | Survival TF of the avascular plate interior; drives glycolysis and VEGF | POSITIVE (required for chondrocyte survival in the hypoxic core) | HIF1A stature phenotype UNVERIFIED | ⚠ HIF-PHIs (roxadustat, daprodustat) stabilise HIF — approved, oral. Their skeletal literature is bone MASS, not length | 37794190 (chondrocyte hypoxia, mouse) | no |
| 29 | **EPAS1 / HIF2A** | Second HIF; catabolic in cartilage — drives MMP13, COL10A1 | Reported to **drive hypertrophy and catabolism**; direction for length contested | EPAS1 GoF = erythrocytosis/paraganglioma; no stature | ⭐ **HIF2A has a real, approved small-molecule inhibitor — BELZUTIFAN (PT2977)** binding an internal PAS-B cavity. This is the proof that a bHLH-PAS TF is druggable | 24914685 (HIF-2α catabolic, mouse/human) | no |
| 30 | **ARNT / HIF1B** | Obligate dimerisation partner for HIF1A and EPAS1 (and AHR) | Required | None | ⚠ The belzutifan site is at the HIF2A–ARNT interface — so the interface itself is the drugged surface | 24914685 | **yes** |
| 31 | **STAT5B** | The GH-receptor transcriptional output; drives IGF1, IGFALS, SOCS2 | POSITIVE — the canonical GH→IGF-1 axis | **STAT5B deficiency = severe GH insensitivity with short stature** and immunodeficiency; dominant-negative forms also described | ⚠ JAK inhibitors act upstream (wrong direction, and growth-suppressive). No STAT5 activator | 22520845; 31514194; 24825400 (index) | no |
| 32 | **STAT3** | IL-6/gp130 output; also required for skeletal development | POSITIVE — STAT3 is critical for skeletal development and bone homeostasis | STAT3 LoF = hyper-IgE (Job) syndrome, with skeletal features; GoF = early-onset autoimmunity with **growth failure** | ⭐⭐ **The best-precedented TF modality in this whole table: (a) SD-36, a potent selective STAT3 PROTAC degrader with complete tumour regression in mice; (b) a STAT3 DECOY OLIGONUCLEOTIDE already dosed in a first-in-human trial.** Both point the wrong way for growth, but they prove the modality | 34824272 (mouse skeletal); 31715132 (SD-36 degrader); 22719020 (human decoy trial) | no |
| 33 | **STAT1** | The FGFR3 growth-arrest arm in chondrocytes | NEGATIVE — STAT1 mediates FGF-induced chondrocyte growth arrest | STAT1 GoF = chronic mucocutaneous candidiasis; STAT1 LoF = mycobacterial disease | ⚠ Only via upstream FGFR/JAK inhibition | 12821644 (FGF→chondrocyte arrest network, mouse) | no |
| 34 | **SHOX / SHOX2** | Pseudoautosomal homeobox; SHOX is dosage-sensitive and expressed in the mid-portion of the limb; SHOX2 acts upstream of RUNX2 in the stylopod | POSITIVE, strongly dosage-dependent. **SHOX haploinsufficiency is one of the commonest single-gene causes of short stature** | Léri–Weill dyschondrosteosis (het), Langer mesomelic dysplasia (biallelic), Turner-syndrome short stature, and a slice of "idiopathic" short stature | ⭐ **SHOX is a dosage problem with an ENHANCER solution: the downstream and upstream PAR1 enhancers are deleted in many patients, so the therapeutic object is an enhancer, not a protein.** No agent exists | 9590292, 9590293 (human); 16537395, 27287812 (Shox2 mouse) | no |
| 35 | **NKX3-2 / BAPX1** | Sclerotome TF; **represses RUNX2** and thereby delays hypertrophy | NEGATIVE regulator of hypertrophy → nominally a way to lengthen the proliferative phase. But biallelic human loss is a dysplasia, so it is a BAND | **Spondylo-megaepiphyseal-metaphyseal dysplasia** (homozygous inactivating variants) | ✗ None. ⭐ But its chondrogenic enhancer was mapped and deleted in mouse (row 71) | 20004766 (human); 26363466 (PI3K→Nkx3.2, mouse); 38844479 (enhancer) | **yes** |
| 36 | **TRPS1** | Atypical **GATA-type repressor**; represses the osteocalcin promoter and uncouples chondrocyte differentiation from perichondrial mineralisation | NEGATIVE at the mineralisation step; human loss gives short stature, so net POSITIVE for length | **Tricho-rhino-phalangeal syndrome I/III** — short stature, cone-shaped epiphyses, brachydactyly. Type III (missense in the GATA finger) is the severe short-stature form | ✗ None. GATA zinc finger; theoretically in the degradable-ZnF class | 10615131, 11112658 (human); 18424451 (mouse mechanism); 12446778 (GATA domain) | no |
| 37 | **ZBTB16 / PLZF** | BTB-zinc finger; skeletal patterning; Hox5 partner restricting Shh in the limb | Loss = limb patterning defects (mouse *luxoid*) | Human biallelic ZBTB16 skeletal phenotype UNVERIFIED | ⭐⭐ **PLZF is a THALIDOMIDE/CEREBLON NEOSUBSTRATE — 5-hydroxythalidomide degrades PLZF and this is proposed as the teratogenic mechanism.** i.e. an already-marketed drug class degrades this TF in humans. Direction is almost certainly harmful, but it is a *proven human TF degradation event in the skeleton* | 33470442 (cereblon neosubstrate); 24218595 (Hox5–Plzf, mouse); 20338044 (allele separating functions) | **yes** |
| 38 | **NFIX** | Nuclear factor I family | ⭐ **BIDIRECTIONAL BY DOSAGE, and the tall direction is the LOSS direction.** Haploinsufficiency → overgrowth/tall stature; duplication → short stature | **Malan syndrome** (NFIX haploinsufficiency): Sotos-like OVERGROWTH, tall stature, macrocephaly. **Marshall–Smith syndrome**: NFIX variants escaping NMD (dominant-negative), accelerated bone maturation. **19p13 microduplication encompassing NFIX: SHORT stature** | ✗ No agent. But the dosage curve is documented in both directions in humans, which almost nothing else here is | 20673863 (allelic mechanism); 25118028, 29897170 (Malan); 29184170 (duplication → short) | **yes** |
| 39 | **NFIB / NFIA / NFIC** | Same family | NFIB haploinsufficiency = macrocephaly + ID; NFIC is tooth-root; NFIA is brain/urinary | See left | ✗ None | 30388402 (NFIB human); 25156673 (index) | **yes** |
| 40 | **CHD8** | Chromatin remodeller acting as a transcriptional regulator; Wnt-adjacent | ⭐ **LOSS ASSOCIATES WITH OVERGROWTH AND TALL STATURE** in humans; among the largest positive height effects in exome burden work | Truncating CHD8 variants: autism, macrocephaly, **increased height/overgrowth**, GI problems | ✗ No agent. Large ATPase; a helicase/ATPase pocket exists in principle | 31001818, 36182950 (human phenotype series); 26733790 (index) | no |
| 41 | **LCORL** (and neighbour **NCAPG**) | Putative transcription factor at a locus that is one of the strongest body-size signals in ANY mammal | Convergent across humans, cattle, horses, sheep, dogs, pigs. Direction in humans: loss associates with TALLER | No named Mendelian syndrome | ✗ No agent. ⚠ Caution: LCORL and NCAPG sit in one linkage block and the causal gene is contested in every species | 22615965 (horse); 26260584 (livestock index); 23418579 (LCORL expression–size); 21998595, 33713608 (human height GWAS) | no |
| 42 | **ZFAT** | Zinc-finger and AT-hook domain; reaches height GWAS/exome burden lists | Reported LOSS→TALLER direction in exome burden work | Thyroid autoimmunity association; no stature syndrome | ✗ No agent. Cys2His2 ZnF, so nominally in the degradable class | 28146470 (rare coding variants alter height, human) | **yes** |
| 43 | **ZNF518A** | KRAB-adjacent zinc finger; appears in height burden lists | Reported LOSS→TALLER; effect size UNVERIFIED here | None known | ✗ None | UNVERIFIED — I could not retrieve a primary that states the ZNF518A height effect. 28146470 is the general precedent | **yes** |
| 44 | **SCMH1** | Polycomb-associated (Sex comb on midleg homolog 1); appears in height burden lists | Reported LOSS→TALLER; UNVERIFIED | None known | ✗ None | UNVERIFIED | **yes** |
| 45 | **HMG20B (BRAF35)** | LSD1/CoREST complex subunit — a chromatin-adjacent "TF" | Reported LOSS→TALLER; UNVERIFIED | None known | ⭐ Indirect: it sits in the **LSD1/KDM1A–CoREST** complex, and LSD1 inhibitors (bomedemstat, iadademstat) are oral and in phase 2/3 | UNVERIFIED for the height effect; the complex membership is well established | **yes** |
| 46 | **HMGA2** | Architectural HMG protein; the classical "let-7 target" body-size gene | POSITIVE — the 12q14 microdeletion syndrome including HMGA2 gives short stature; Hmga2 mouse mutants are pygmy | 12q14 deletion short stature; HMGA2 also within Silver–Russell differential diagnosis panels | ⚠ Only indirectly, through **let-7 microRNA**: lowering let-7 raises HMGA2. Oncogenic direction | 31963852 (index); 32546215 (Silver–Russell panel, human) | no |
| 47 | **TWIST1 / TWIST2** | bHLH; antagonises RUNX2 by binding its DNA-binding domain; also thresholds limb development | NEGATIVE regulator of osteoblast differentiation; TWIST1 dose sets multiple limb functions | **Saethre–Chotzen syndrome** (TWIST1 haploinsufficiency); TWIST2 → Setleis/focal facial dermal dysplasia and ablepharon-macrostomia | ✗ None. bHLH dimer interface is a protein–protein target in principle | 11585922 (Twist–Runx2, mouse); 20732316 (Twist1 thresholds, mouse); 30976276 (human index) | no |
| 48 | **PRRX1 / PRRX2** | Paired-related homeobox; the canonical limb-mesenchyme driver (Prx1-Cre is the standard limb driver) | Positive for limb mesenchyme; Prrx1/2 double null = severe limb and craniofacial defects | **PRRX1 variants cause craniosynostosis** with incomplete penetrance; agnathia–otocephaly in biallelic cases | ✗ None | 37154149 (human); 32629173 (Prx1 lineage index) | **yes** |
| 49 | **MSX1 / MSX2** | Homeobox; MSX2 drives canonical Wnt anabolism; both suppress heterotopic bone in neural crest | MSX2 GoF = Boston-type craniosynostosis; MSX2 LoF = parietal foramina | Both directions are human, and both are cranial, not long-bone | ✗ None | 18487199 (Msx2–Wnt, mouse); 20398647 (mouse); 30976276 (index) | no |
| 50 | **DLX5 / DLX6** | Distal-less homeobox; **DLX5 promotes COL10A1 and chondrocyte hypertrophy** | POSITIVE for hypertrophy → h_term | Split-hand/foot malformation type 1 (SHFM1) from deletion of a DLX5/6 **enhancer**, not the gene | ✗ No agent; ⭐ the human lesion is again an ENHANCER deletion | 12000792 (mouse); 37492739 (DLX5→Col10a1); 19707792 (human enhancer deletion) | **yes** |
| 51 | **PAX1 / PAX9** | Sclerotome specification, vertebral bodies and intervertebral discs — the AXIAL compartment | Positive for axial skeleton; PAX1 loss → *undulated* mouse, vertebral defects | PAX1 biallelic → otofaciocervical syndrome type 2 (with thymic aplasia); PAX9 → tooth agenesis | ✗ None. ⚠ Notable as one of the few TFs specific to the compartment that is trunk rather than limb | 30902259, 36393845, 38473380 (index) | **yes** |
| 52 | **HOXD13 / posterior HOXD cluster** | 5' HOX; posterior prevalence; antagonises GLI3 in the interdigit | Patterning rather than length; polydactyly/synpolydactyly | **Synpolydactyly** from polyalanine expansion in HOXD13; brachydactyly types from HOXD13 missense | ✗ No agent. ⭐ But the HOXD cluster is the textbook TAD/regulatory-archipelago locus, so the *element* is targetable in principle | 19075394 (mouse); 27713395 (5'Hoxd–Gli3, mouse); 22448207 (human index) | no |
| 53 | **HOXA11 / HOXD11 (Hox11 paralogues)** | Zeugopod (radius/ulna, tibia/fibula) identity; act **upstream of RUNX2 and SHOX2** in chondrocyte differentiation | POSITIVE and REGIONAL — Hox11 marks regional skeletal stem cells for life | HOXA11 LoF = radioulnar synostosis with amegakaryocytic thrombocytopenia | ✗ None. ⭐ Value is conceptual: Hox11⁺ regional stem cells persist postnatally and are region-specific, so any pool lever is regional | 22916278 (Hoxa11/Hoxd11→Runx2/Shox2, mouse); 31320650 (Hox11 stem cells, mouse); 28470721 (mouse) | **yes** |
| 54 | **MEIS1 / MEIS2 / PBX1 / PBX2 (TALE)** | HOX cofactors; PBX1/2 govern axial skeleton by controlling Polycomb and Hox in mesoderm and Pax1/Pax9 in sclerotome | POSITIVE for proximal (stylopod) identity | PBX1 LoF = CAKUT with skeletal features; MEIS2 LoF = cleft palate/cardiac/ID | ✗ None. ⚠ MEIS–PBX–HOX is a ternary protein–protein interface, which is the class stapled peptides attack | 18691704 (Pbx1/Pbx2 axial, mouse); 37414772 (PBX1/2→HAND2, mouse); 21416555 (index) | **yes** |
| 55 | **TBX2 / TBX3** | T-box; TBX3 establishes posterior boundary in the limb bud with HAND2 | TBX3 haploinsufficiency = **ulnar–mammary syndrome** (limb reduction, short stature reported) | See left | ⚠ T-box DNA-binding domain has recently been discussed as a targeted-therapy surface; nothing skeletal | 31669645, 38965548 (index); 38828908 (mouse) | no |
| 56 | **TBX4 / TBX5** | Hindlimb (TBX4) and forelimb (TBX5) identity | Patterning, not length. Tbx4 explains proximal limb defect origins | TBX5 → Holt–Oram; TBX4 → small patella syndrome and childhood pulmonary hypertension | ⚠ Note: the human height locus at chr17 spans TBX2/TBX4 and is reported as a strong sitting-height-ratio (proportion) signal | 34423345 (Tbx4 mouse); 25294936 (index) | no |
| 57 | **TBX15** | T-box; sets regional (dorsal/ventral, adipose depot) identity; promoter-adjacent hypermethylation modulates it | **TBX15 LoF = Cousin syndrome** (craniofacial dysmorphism, short stature) | See left | ⚠ Its expression is set by promoter DNA methylation — nominally an epigenetic-editing target | 36547252 (methylation, human) | **yes** |
| 58 | **PITX1** | Hindlimb identity | PITX1 haploinsufficiency = **Liebenberg syndrome** (arm takes on leg character) when a *PITX1 enhancer* is captured by a structural variant | See left; also clubfoot | ✗ None. ⭐ One of the cleanest human demonstrations that moving an ENHANCER, not the gene, changes limb morphology | 30262816 (3D chromatin, mouse); 30499775 (Pitx1 enhancer, vertebrates); 33844046 (index) | **yes** |
| 59 | **SIX1 / SIX2 + EYA1** | SIX–EYA is a TF plus a **phosphatase** cofactor | Limb tendon/muscle and placode; skeletal length role weak | EYA1 → branchio-oto-renal; SIX1 → BOR/DFNA | ⭐ Mechanistically special: **EYA is a protein tyrosine phosphatase, i.e. an enzyme**, so the SIX–EYA transcriptional output has an enzymatic handle where the TF itself does not | 22971774 (index); 34490256 (index) | **yes** |
| 60 | **ZEB1 / ZEB2** | EMT zinc-finger E-box factors | ZEB2 haploinsufficiency = Mowat–Wilson; growth restriction is part of it. Chondrocyte-specific role UNVERIFIED | Mowat–Wilson (ZEB2) | ✗ None | 40011185 (EMT-TF index) | **yes** |
| 61 | **SNAI1 / SNAI2 (Slug)** | E-box repressors; **bind YAP/TAZ** and thereby control skeletal stem-cell self-renewal vs differentiation | Snail/Slug–YAP/TAZ binding controls skeletal stem-cell self-renewal — i.e. this is a POOL lever | SNAI2 biallelic loss = Waardenburg type 2D (pigmentary, no stature) | ✗ None direct; ⚠ the YAP/TAZ half has TEAD chemistry (row 63) | 27479603 (mouse/human, Nature) | **yes** |
| 62 | **ID1 / ID2 / ID3 / ID4** | HLH proteins lacking a DNA-binding basic region — **dominant-negative sequestrators of bHLH factors**; canonical BMP transcriptional output | ID1 is the standard BMP readout in cartilage; direction for length not isolated | No stature syndrome | ⚠ ID1/ID3 have tool-grade peptide/small-molecule inhibitors in oncology (AGX51 class); nothing skeletal | 27252362 (index); 12821644 (FGF→chondrocyte network, mouse) | **yes** |
| 63 | **YAP1 / WWTR1(TAZ) → TEAD1-4** | Hippo transcriptional output; TEAD provides DNA binding, YAP/TAZ the activation domain | Complicated and mostly a GUARDRAIL: forcing YAP in cartilage gives chondrodysplasia, while cartilage-specific Yap/Taz double loss does not increase growth. YAP is reported a **negative** regulator of MSC chondrogenesis | No clean human stature phenotype | ⭐⭐ **The single best chemical matter in this domain.** TEAD has a **lipid (palmitate) pocket** that is genuinely druggable: VT3989, IK-930, IAG933 are clinical-stage; **TEAD PROTAC degraders have been published**; verteporfin is approved (for photodynamic therapy) and disrupts YAP–TEAD | 29401582 (Yap/Taz promote bone dev, mouse); 26025096 (YAP negative for chondrogenesis); 38746898 (TEAD PROTACs); 38538573, 41347094 (clinical TEAD index) | no |
| 64 | **MYC / MYCN / MAX / MNT** | bHLH-LZ proliferation drivers; MAX is the obligate partner, MNT the antagonist | Proliferation; c-MYC in MSCs raises proliferation at the cost of differentiation | MYCN GoF = Feingold-like; **MYCN LoF = Feingold syndrome, short stature and brachydactyly** | ⚠ MYC has been attacked with Omomyc (a dominant-negative MYC **mini-protein**, OMO-103, which reached first-in-human) — the proof that a bHLH-LZ TF can be drugged by a protein | 30836996 (c-MYC in MSC, human); 31614829 (index) | no |
| 65 | **RB1 + E2F family** | Cell-cycle gatekeeper for the proliferative zone | **Loss of pRB and p107 disrupts cartilage development and promotes enchondroma** — so removing the brake does not lengthen, it deranges | Retinoblastoma; osteosarcoma | ⚠ CDK4/6 inhibitors (palbociclib etc., approved) act on this axis and are **growth-plate toxic in juvenile animals** — a contraindication, not a lever | 23146901 (mouse); 11159908 (index) | **yes** |
| 66 | **TP53 / TP63 / TP73** | p53 restrains proliferation; TP63 is limb/AER | TP63 → EEC/split-hand-foot (limb, not length) | TP63 limb syndromes; Li–Fraumeni for TP53 | ⭐ p53 is the most-drugged TF of all (MDM2 inhibitors, reactivators) — all in the anti-growth direction | 36216888, 38729160 (index) | **yes** |
| 67 | **ESRRA / ESRRG** | Orphan nuclear receptors | ERRα **directly regulates sox9** in zebrafish cartilage | None | ⭐ Nuclear receptors have ligand pockets: **GSK5182** is an ERRγ inverse agonist with cartilage data | 26657540 (zebrafish); 33261216 (GSK5182); 33446092 (index) | **yes** |
| 68 | **ESR1 / ESR2 (ER)** | Nuclear receptor; ERα drives epiphyseal fusion | ⭐ **NEGATIVE for the growth PERIOD — the human ERα-null man and aromatase-deficient men remain unfused and keep growing into their 20s–30s** | ERα LoF: tall, unfused epiphyses, osteopenia. ERβ has no male skeletal phenotype | ⭐⭐ **The best-drugged TF in the whole domain and the only one already used against height: aromatase inhibitors (ligand removal), SERMs, SERDs (fulvestrant, elacestrant), and now VEPDEGESTRANT, an approved ERα PROTAC DEGRADER** — a TF actually removed as protein in humans | 28539434 (index, human) | no |
| 69 | **AR (androgen receptor)** | Nuclear receptor; male growth-zone chondrocytes convert testosterone to DHT locally | POSITIVE for male pubertal growth; complete AIS gives adult height intermediate between male and female norms | Androgen insensitivity syndrome | ⭐⭐ Fully drugged both ways: agonists, antagonists (enzalutamide), **and an approved AR degrader class in development**; plus 5α-reductase inhibitors upstream | 27807202, 25202834 (index) | no |
| 70 | **NR3C1 (glucocorticoid receptor)** | Nuclear receptor; the strongest pharmacological suppressor of longitudinal growth in clinical use | NEGATIVE — glucocorticoid excess is grade-A growth suppression, and glucocorticoid **deficiency (familial glucocorticoid deficiency) gives tall stature in childhood** | Cushing (short), FGD (tall as a child) | ⭐ Fully drugged: mifepristone, relacorilant; and the cortisol-lowering enzymes (metyrapone, osilodrostat). ⚠ Every cortisol-lowering agent raises ACTH by feedback | 30321335 (index) | no |
| 71 | **VDR** | Nuclear receptor | Required for normal growth-plate resorption; VDR in chondrocytes drives osteoclastogenesis and regulates FGF23 | Hereditary vitamin-D-resistant rickets (VDR LoF) — rickets with short stature | ⭐ Fully drugged (calcitriol, paricalcitol, and non-calcaemic VDR agonists) | 17099775 (mouse); 18694980 (index) | no |
| 72 | **THRA / THRB** | Nuclear receptors for T3; T3 is the classical INDUCER of chondrocyte hypertrophy | POSITIVE for hypertrophy = h_term; but T3 also **advances bone age**, so it is a period/rate trade | **THRA resistance = short stature, skeletal dysplasia, delayed bone age**; THRB resistance = advanced bone maturation in mouse models | ⭐ Fully drugged: levothyroxine, liothyronine, and **THRB-selective agonists (resmetirom, approved 2024)** — the first tissue-selective nuclear-receptor agonist relevant here | 24914936 (Thra mouse); 22442145 (Thrb mouse); 34069457 (human THRA2); 26862888, 29407442 (index) | no |
| 73 | **RARA / RARB / RARG + RXR** | Retinoid nuclear receptors; RARG is the cartilage-dominant subtype; unliganded RAR is a co-repressor-bound REPRESSOR | BAND with a grade-A human harm on one side: **retinoid excess (isotretinoin, palovarotene) causes PREMATURE EPIPHYSEAL CLOSURE**. Unliganded RARγ appears permissive | Retinoid embryopathy; palovarotene physeal closure in children | ⭐⭐ **Fully drugged in both directions AND already delivered LOCALLY to a growth plate: RARγ-agonist-loaded nanoparticles implanted beside the mouse proximal tibial growth plate caused involution and closure of THAT plate and shortened THAT tibia versus the contralateral control, while RARα and RARβ agonists did nothing.** Systemic dosing closed plates everywhere. Agonists (palovarotene/Sohonos, tretinoin), antagonists (CD2665, RARγ-selective 7C class), and CYP26 inhibitors (talarozole) all exist | **39883086** (mouse, local NP, J Bone Miner Res 2025); 39677926 (palovarotene index); 32151018 (CYP26 index) | no |
| 74 | **PPARG** | Adipogenic nuclear receptor; competes with the chondro/osteogenic program in mesenchymal progenitors | Fate-competition rather than a direct length term | PPARG LoF = familial partial lipodystrophy | ⭐ Fully drugged (TZDs, approved). ⚠ TZDs shift MSC fate to adipose — likely a cost | 23589826 (index) | no |
| 75 | **NR1D1/2 (REV-ERB), RORA/B/C, BMAL1/CLOCK** | The circadian transcriptional loop; BMAL1 controls the **secretory pathway timing for collagen** | Circadian control of collagen homeostasis is real; a length term is UNVERIFIED | None for stature | ⭐ Fully drugged: REV-ERB ligands (SR9009 class, tool-grade), RORγt inverse agonists (clinical-stage) | 31907414 (collagen circadian, mouse); 27253997 (human cartilage BMAL1) | **yes** |
| 76 | **NR4A1/2/3 (NUR77/NURR1/NOR1)** | Immediate-early orphan nuclear receptors, mechanically and cAMP-inducible | Direction in growth plate UNVERIFIED | None | ⭐ Ligandable orphan receptors with published agonists/antagonists | 23589826, 35935773, 36110555 (index) | **yes** |
| 77 | **KLF2 / KLF4 / KLF15** | Krüppel-like zinc fingers; KLF15 is a glucocorticoid-induced catabolic TF in muscle | Direction in cartilage UNVERIFIED. KLF15 is a candidate mediator of glucocorticoid growth suppression | None isolated | ⚠ Cys2His2 ZnF class — degradable in principle (row 89) | UNVERIFIED for growth plate | **yes** |
| 78 | **EGR1 / EGR2** | Immediate-early zinc fingers; mechanotransduction output | UNVERIFIED for length | EGR2 → Charcot-Marie-Tooth (nerve) | ⚠ ZnF class | UNVERIFIED | **yes** |
| 79 | **AP-1 (FOS/FOSB/FOSL1-2 × JUN/JUNB/JUND)** | bZIP dimers; the immediate-early output of mechanical load, FGF and inflammation; converge on MMP13 | Mostly catabolic/inflammatory in cartilage; a length direction is not isolated | FOSL1-related? UNVERIFIED. Fos transgenics give osteosarcoma | ⭐ Real chemistry exists: **small-molecule AP-1 inhibitors (T-5224 and related) reached clinical study**; AP-1 decoy oligonucleotides are also published | 24831826 (AP-1 small-molecule inhibitors, index) | no |
| 80 | **SRF + MRTF-A/B (MKL1/2)** | Actin-sensing transcriptional module; MRTF-A regulates the contractile/dedifferentiated chondrocyte phenotype | Cytoskeletal-state readout; length direction UNVERIFIED | None | ⭐ CCG-1423/CCG-203971 class MRTF/SRF inhibitors exist (tool-grade, in vivo-capable) | 27751947 (chondrocyte MRTF-A); 33807043 (index) | **yes** |
| 81 | **IRF family (IRF1, IRF8)** | Interferon-response TFs; part of inflammatory growth suppression | NEGATIVE in the inflamed state | Various immunodeficiencies | ⚠ Only upstream (JAK inhibitors) | 30671054 (index) | **yes** |
| 82 | **TFAP2A / TFAP2B** | AP-2 family, neural crest | Craniofacial rather than long-bone | TFAP2A → branchio-oculo-facial; TFAP2B → Char syndrome | ✗ None | 32666711 (index) | **yes** |
| 83 | **GATA family (GATA3, GATA6) + TRPS1 as an atypical GATA** | GATA3 → HDR syndrome; GATA6 → pancreatic agenesis/cardiac | Stature effects secondary (hypoparathyroidism in HDR affects mineral, not the plate directly) | HDR (hypoparathyroidism, deafness, renal) | ✗ None | 10615131 (TRPS1 GATA context) | **yes** |
| 84 | **ELF3 / ESE-1 (ETS)** | ETS-family **repressor of COL2A1** in human chondrocytes; IL-1 inducible | ⭐ NEGATIVE — a direct repressor of the plate's most abundant transcript | None | ✗ None | 18044710 (human chondrocytes) | **yes** |
| 85 | **ERG (ETS)** | Required for articular cartilage endurance and resistance to osteoarthritic change | Articular rather than physeal | None | ⚠ ETS inhibitors exist in oncology (YK-4-279 class) | 26097038 (mouse) | **yes** |
| 86 | **ETV4 / ETV5 (PEA3 ETS)** | FGF transcriptional output; opposing ETS functions define Shh spatial expression in the limb | Patterning; length direction UNVERIFIED | None isolated | ⚠ Same ETS chemistry | 22340503 (mouse/chick) | **yes** |
| 87 | **SALL4** | Zinc finger; limb and heart development | Haploinsufficiency = radial-ray reduction | **Okihiro / Duane-radial-ray, acro-renal-ocular** — SALL4 haploinsufficiency | ⭐⭐ **SALL4 IS A THALIDOMIDE-INDUCED CEREBLON NEOSUBSTRATE.** Thalidomide degrades SALL4 and this is a leading explanation of its limb teratogenicity. A marketed drug degrades a skeletal TF in humans | 30067223 (SALL4 degradation); 12843316, 15342710 (human genetics) | no |
| 88 | **ZBTB16/PLZF — degradation route** *(see also row 37)* | | | | **5-hydroxythalidomide + cereblon → PLZF degradation → teratogenicity** | 33470442 | **yes** |
| 89 | **The Cys2His2 zinc-finger proteome as a drug class** | Not a single factor — the structural class that includes SP7, TRPS1, ZFAT, ZNF518A, KLF, EGR, GLI, SNAI, ZEB | n/a | n/a | ⭐⭐ **This is the answer to "TFs are undruggable". Systematic work now maps which C2H2 zinc fingers are degradable by cereblon-recruiting molecular glues, and defines the sequence/structure properties that predict degradability.** Most growth-plate TFs above are C2H2 | 40845806 (2025, druggable zinc-finger proteome); 39218923 (multi-neosubstrate glues); 40835825 (unbiased CRBN neosubstrate map) | **yes** |
| 90 | **ZFHX4** | Zinc-finger homeobox; described as the transcriptional **platform for Osterix/SP7** in endochondral ossification | POSITIVE | ZFHX4 haploinsufficiency (8q21 deletion) — ptosis/8q21.11 deletion syndrome; stature UNVERIFIED | ✗ None | 34732852 (mouse) | **yes** |
| 91 | **FOXA1 / FOXA2 / FOXA3** | Pioneer forkhead factors; **crucial regulators of the hypertrophic chondrocyte program**; act in a phasic SOX9–GLI–FOXA network that times the differentiation transitions | POSITIVE for hypertrophy = h_term | No isolated stature phenotype | ✗ None. ⭐ Conceptually important: FOXA are PIONEER factors, so they open chromatin others cannot — a different class of intervention point | 22595668 (mouse); 29659575 (SOX9–GLI–FOXA network) | **yes** |
| 92 | **FOXO1 / FOXO3 / FOXO4** | Forkhead; PI3K/AKT-inhibited; autophagy and oxidative-stress resistance in chondrocytes; drive PRG4 | Protective/homeostatic; a LENGTH direction is not isolated. Note the axis is the same one NRK/PTEN/AKT sits on | FOXO3 longevity association; no stature syndrome | ⭐ Chemistry exists at both ends: AS1842856 (FOXO1 inhibitor) and PI3K/AKT inhibitors upstream (approved, but growth-suppressive) | 29444976 (mouse); 25186470 (human chondrocytes); 31973091 (index) | no |
| 93 | **FOXC1 / FOXC2** | Forkhead; somitogenesis and sclerotome; Foxc1/2 double mutants lose axial patterning | Axial/patterning | FOXC1 → Axenfeld–Rieger (eye); FOXC2 → lymphoedema-distichiasis | ✗ None | 11562355 (mouse); 32788657 (index) | **yes** |
| 94 | **FOXN3, FOXP1/2, FOXL2** | Other forkheads reaching skeletal/GWAS lists | UNVERIFIED | FOXP1 → ID/speech; FOXL2 → BPES | ✗ None | UNVERIFIED for growth plate | **yes** |
| — | **REGULATORY DNA — the elements themselves** | | | | | | |
| 95 | **Fgfr3 −29E enhancer** | Cartilage-specific enhancer 29 kb upstream of mouse Fgfr3; a transgenic reporter under it matches Fgfr3's own cartilage domain | ⭐⭐ **The cleanest proof in this domain that an ENHANCER is the right unit.** CRISPR deletion in otherwise WT mice **halved Fgfr3 in cartilage with no adverse phenotype**; in an achondroplasia model it largely normalised **long-bone AND VERTEBRAL BODY growth**, reduced spinal-canal and foramen-magnum stenosis, and removed lethality | n/a (mouse); **the element is stated to be highly conserved in humans** | ⭐ Somatic enhancer editing; the authors explicitly frame it as a path to genetic therapy for achondroplasia | **39817451** (mouse, J Clin Invest 2025) | no |
| 96 | **Hhip chondrogenic enhancers (CE2/CE3-type)** | Limb-enriched chondrogenic enhancers at the Hhip locus, identified in a genome-wide chondrocyte enhancer map and deleted by CRISPR | Deletion lowers Hhip **in limb** with little change in trunk — i.e. a compartment-selective dosage handle on a secreted hedgehog antagonist | n/a (mouse) | ⭐ Enhancer deletion; conceptually the only route to a **limb- vs trunk-selective** dosage change | **38844479** (mouse, Nat Commun 2024) | **yes** |
| 97 | **Nkx3-2 and Col2a1 chondrogenic enhancers** | Same study: targeted deletions at Fgfr3, Col2a1, Hhip and Nkx3-2 loci each confirmed regulation of the cognate gene | Dosage handles on four cartilage genes | n/a (mouse) | ⭐ Same enhancer-editing route | 38844479; 36377467 (a distinct Nkx3.2 jaw-joint element) | **yes** |
| 98 | **The chondrocyte enhancer atlas itself** | 780 chondrocyte-specific genes and **2,704 putative chondrocyte enhancers** from Col2a1-sensor-sorted fetal mouse chondrocytes (RNA-seq + ATAC-seq + H3K27ac ChIP-seq). **74% pan-chondrogenic, 18% limb-restricted, 8% trunk-restricted** | ⭐ Height-associated variants overlapping these enhancers explain height differences BETTER than variants over non-chondrogenic enhancers | Human height GWAS interpretation | The resource *is* the target list for any enhancer-directed approach | **38844479** | no |
| 99 | **Human skeletal-development functional genomics (element-specific vs global)** | Epigenomic + transcriptomic maps from chondrocytes sampled from **different growth plates across developing human skeletons**, then intersected with height GWAS | ⭐ Separates **skeletal-element-specific** from **global-acting** height variants and concludes regulatory **pleiotropy** dominates height variation | Human, directly | The resource that would let a lever be aimed at a compartment | **39549696** (human, Cell 2025) | no |
| 100 | **SOX9 upstream regulatory domain (up to ~1.5 Mb)** | A very long-range enhancer archipelago; translocation breakpoints hundreds of kb to >1 Mb upstream cause disease without touching the coding sequence | Dosage: reduced SOX9 → campomelic/acampomelic dysplasia; specific subsets give Pierre Robin only | **Acampomelic campomelic dysplasia and Pierre Robin sequence from breakpoints/deletions in distinct upstream regulatory territories** — the element determines which tissue is affected | ⭐ Tissue-selective SOX9 dosage is achievable *only* through these elements, never through the protein | 23648064, 24934569, 32991838 (human); 28085555, 36417512 (3D folding) | no |
| 101 | **ACAN far-upstream enhancer + promoter** | SOX9 binding at a far-upstream aggrecan enhancer requires SOX5/SOX6 to be secured; SOX9 also enhances the ACAN promoter/enhancer directly | The transcriptional control point for the plate's dominant proteoglycan; ACAN loss-of-function is one of the largest human height effects | ACAN haploinsufficiency = short stature with advanced bone age (a common "idiopathic" short-stature cause) | ⭐ ACAN cannot be supplied as a protein, so the ONLY elevation route is transcriptional — CRISPRa at this enhancer is the concrete proposal | 18559420 (mouse); 10753864 (SOX9→ACAN promoter) | no |
| 102 | **IHH enhancer cluster** | A multipartite enhancer cluster whose **composition and dosage** control Ihh expression; human copy-number changes at the locus cause disease | ⭐ Dosage-graded morphogen control by element copy number | **IHH-locus duplications cause syndactyly and craniosynostosis**; a large duplication mimics acrocallosal syndrome | ⭐ The only demonstrated way to titrate a hedgehog ligand by DNA | 28846100 (mouse); 21167467, 22234151 (human CNV) | **yes** |
| 103 | **ZRS (SHH limb enhancer, ~1 Mb into LMBR1)** | The textbook long-range limb enhancer | Point mutations → preaxial polydactyly; duplications → triphalangeal thumb-polysyndactyly and Haas syndactyly; **a specific ZRS variant causes Werner MESOMELIC syndrome (a limb-SHORTENING phenotype)** | Multiple, all human, all non-coding | ⭐ The proof that single-base changes in one enhancer produce a graded allelic series of limb phenotypes | 19847792, 18417549 (human); 27402708, 32169219 (function) | no |
| 104 | **CTCF sites at the SHH locus** | Boundary elements | ⭐ **Deleting CTCF sites in the SHH locus rewires enhancer–promoter contacts and causes ACHEIROPODIA (absence of hands and feet) in humans** | Acheiropodia | ⭐ Demonstrates that the *insulator*, not the enhancer and not the gene, can be the causal element in a limb-size phenotype | 33863876 (human/mouse) | **yes** |
| 105 | **PITX1 pelvic/hindlimb enhancer (Pen-type)** | A hindlimb enhancer whose capture by a structural variant converts arm toward leg | Limb identity by element hijacking | **Liebenberg syndrome** | ⭐ Same lesson: move an element, change a limb | 30262816, 30499775 (mouse/vertebrates); 25315429 (human boundary deletions) | **yes** |
| 106 | **DLX5/DLX6 enhancer (SHFM1 region)** | Deletion of an enhancer near DLX5/6 causes limb and craniofacial disease without disrupting the genes | Element-level dosage | Split-hand/foot malformation 1, hearing loss | ⭐ Same class | 19707792 (human) | **yes** |
| 107 | **SHOX PAR1 enhancers (up- and downstream)** | SHOX's enhancers lie in the pseudoautosomal region; deletions of the downstream enhancer region alone cause disease | ⭐ **A large share of SHOX-related short stature is caused by ENHANCER deletion with an intact SHOX gene** | Léri–Weill dyschondrosteosis and idiopathic short stature | ⭐⭐ **The single most clinically common enhancer lesion in human short stature.** The therapeutic object here is unambiguously an element | 9590292, 9590293 (human); 39389973 (Shox2 gene desert, mouse) | no |
| 108 | **BMP2 downstream regulatory element** | A conserved element downstream of BMP2; duplications alter digit length | Element dosage → digit length | **Brachydactyly type A2** | ⭐ Same class | 19327734 (human) | **yes** |
| 109 | **Chondrocyte super-enhancers** | SOX9 with SOX5/SOX6 act genome-wide **through super-enhancers**, and the trio's targets are enriched at these clusters | The super-enhancer is the functional unit for the SOX trio, not the individual site | n/a | ⭐ Super-enhancers are the class most sensitive to BET and CDK7/12 inhibition — a real (if blunt and antiproliferative) chemical handle on a TF program | 26150426 (mouse/human) | no |
| 110 | **Knee-chondrocyte regulatory landscape under selection** | Human knee chondrocyte cis-regulatory map showing evolutionary selection and constraint, tied to osteoarthritis risk | Establishes that human knee chondrocyte regulation is under recent selection — the same elements that set joint shape set height risk | Human | Resource | 32220312 (human) | **yes** |
| 111 | **Pediatric bone-accrual and bone-size GWAS loci** | Longitudinal paediatric bone accrual GWAS; bone-size GWAS with 12 loci overlapping height/BMD/OA | Provides growth-trajectory (not just endpoint) genetic anchors | Human | Resource | 33397451, 31053729 (human) | **yes** |
| 123 | **RARγ-agonist nanoparticle depot (a TF drug delivered to ONE growth plate)** | Not a factor — a demonstration that a nuclear-receptor ligand can be aimed at a single physis | Direction demonstrated is SHORTENING and DIRECTIONAL: one-sided implantation tilted the epiphysis and angulated the tibia. **The mirror experiment — a local RARγ ANTAGONIST depot to lengthen — is stated by that group as an unrealised possibility and has never been done** | n/a (mouse) | ⭐⭐ The route problem and the TF-selectivity problem are solved simultaneously: a local depot gives compartment selectivity that no systemic TF drug can, and RARγ is one of the few growth-plate TFs with a real ligand pocket | **39883086** (mouse) | **yes** |
| — | **MODALITIES — the "can a TF be modulated at all" row set** | | | | | | |
| 112 | **PROTAC / heterobifunctional degrader** | Recruits an E3 (CRBN or VHL) to any protein with a ligandable surface — the TF does not need a *functional* pocket, only a *bindable* one | n/a | n/a | ⭐⭐ **VEPDEGESTRANT (Veppanu) was FDA-approved 1 May 2026 — the first approved PROTAC, and its target is a TRANSCRIPTION FACTOR (ERα).** Also: SD-36 (STAT3 degrader, complete tumour regression in mice); published TEAD PROTACs | 39072356 (VERITAC-2 phase 3); 40702893 (NDA); 38819400 (preclinical); 31715132 (STAT3 SD-36); 38746898 (TEAD) | no |
| 113 | **Molecular glue / cereblon neosubstrate** | Reshapes the CRBN surface so a zinc finger becomes a substrate; needs NO pre-existing ligandable pocket | n/a | n/a | ⭐⭐ **The two skeletal-relevant human examples are both teratology: thalidomide degrades SALL4 (limb reduction) and 5-hydroxythalidomide degrades PLZF/ZBTB16.** These are proofs that marketed drugs already degrade skeletal TFs in humans — in the harmful direction | 30067223 (SALL4); 33470442 (PLZF); 35856839 (index) | no |
| 114 | **Systematic zinc-finger degradability mapping** | Defines which C2H2 zinc fingers can be degraded and what predicts it | n/a | n/a | ⭐⭐ **This is the reason "TFs are undruggable" is now false for the C2H2 class**, which covers SP7, TRPS1, GLI1-3, SNAI1/2, ZEB1/2, KLF, EGR, ZFAT, ZNF518A | 40845806; 40835825; 39218923 | **yes** |
| 115 | **Transcription-factor DECOY oligonucleotide** | Double-stranded DNA carrying the TF's binding site; titrates the factor away from the genome. Sequence-programmable, so it works for factors with no pocket at all | n/a | n/a | ⭐ **A STAT3 decoy ODN completed a FIRST-IN-HUMAN intratumoral trial**; NF-κB and AP-1 decoys are published. Delivery to avascular cartilage is the unsolved half | 22719020 (human trial) | no |
| 116 | **Antisense oligonucleotide, including UPREGULATING ASOs (TANGO)** | Splice-switching ASOs that block non-productive alternative splicing **raise** protein output from the healthy allele — the one oligonucleotide modality that goes UP | n/a | n/a | ⭐⭐ **Directly applicable to every haploinsufficiency in this table (SHOX, SOX9, RUNX2, NFIX-duplication reversal, ACAN).** The chemistry is approved-class (PS/MOE gapmers, 2'-MOE splice switchers) | 32647108 (TANGO); 38182878, 37253858, 37884512 (index) | no |
| 117 | **CRISPRa / dCas9 transcriptional activation at a promoter or enhancer** | Raises expression from the intact allele without editing the sequence | n/a | n/a | ⭐⭐ **The decisive precedent exists in vivo: CRISPR-mediated activation of a PROMOTER OR ENHANCER RESCUED OBESITY CAUSED BY HAPLOINSUFFICIENCY in mice (Sim1/Mc4r).** That is exactly the SHOX and SOX9 problem | 30545847 (mouse, Science); 33020616, 36902207 (index) | no |
| 118 | **Somatic ENHANCER deletion (CRISPR)** | Removes a tissue-restricted enhancer to halve a gene's expression in ONE tissue only | n/a | n/a | ⭐⭐ Demonstrated at Fgfr3 (−29E) with a large skeletal benefit and **no adverse phenotype in wild-type mice** — the cleanest tissue-selective dosage tool in this domain. ⛔ Irreversible, and no somatic editing of a growth plate has been reported in any species | 39817451; 38844479 | no |
| 119 | **BET / CDK7 / CDK12-13 inhibition (super-enhancer collapse)** | Blunt: removes the coactivator machinery that super-enhancers depend on | n/a | n/a | ⭐ Real approved/clinical-stage chemistry, but broadly antiproliferative — a contraindication near an open plate rather than a lever | 26150426 (chondrocyte super-enhancers) | **yes** |
| 120 | **Dominant-negative mini-protein (the Omomyc precedent)** | An engineered bHLH-LZ that dimerises with the target and poisons its DNA binding | n/a | n/a | ⭐ **OMO-103 (Omomyc) completed a phase 1 trial in solid tumours** — a *protein* drug against a TF everyone called undruggable. The route generalises to any obligate-dimer TF: MYC/MAX, TWIST, ID, bZIP AP-1, HIF/ARNT | 38321218 (human phase 1); 34942444 (index) | no |
| 121 | **Nuclear-receptor ligand pocket** | The one TF superfamily built to be drugged | n/a | n/a | ⭐⭐ ER, AR, GR, VDR, THR, RAR/RXR, PPAR, REV-ERB, ROR, ERR are all ligandable, and **four of them (ER, AR, GR, THR) are the levers already used clinically against growth or stature** | 23589826 (index) | no |
| 122 | **PAS-domain internal cavity (the HIF-2α precedent)** | An "undruggable" bHLH-PAS TF turned out to have a buried cavity that a small molecule fills, breaking dimerisation with ARNT | n/a | n/a | ⭐⭐ **BELZUTIFAN is an APPROVED HIF-2α inhibitor.** It is the proof that non-nuclear-receptor TFs can have real orthosteric pockets — and it is the closest structural analogue in medicine to what an anti-SOX9 or anti-RUNX2 agent would have to be | 33945366 (MK-6482/belzutifan in VHL) | no |

**Row count: 123. Marked OBSCURE = 64. Not obscure = 59.**

---

## TRANSCRIPTION FACTORS WHOSE LOSS LENGTHENS

This is the shortest and most important section, and the honest headline is that the list is **thin, and
almost every member is a band rather than an arrow.** Endochondral growth is built out of factors that are
*required*, and the base rate for "knock this TF out and the animal is longer" is very low. What follows is
everything I could find with real evidence, ranked by how directly the human data support the direction.

**Tier 1 — human loss-of-function gives documented TALL stature or overgrowth**

1. **NFIX** *(row 38)* — the best row in the domain and probably the most under-used TF in the whole height
   literature. **Haploinsufficiency causes Malan syndrome: Sotos-like overgrowth with tall stature and
   macrocephaly.** The opposite dosage change is also human: **19p13 microduplications encompassing NFIX
   cause SHORT stature.** So the dose–height curve is documented in humans in *both* directions on one gene,
   which is true of essentially nothing else here. A third allelic class (variants escaping nonsense-mediated
   decay, i.e. dominant-negative) gives Marshall–Smith syndrome with accelerated bone maturation — so NFIX
   also separates *height* from *bone age*, which is the exact separation this project needs.
   PMIDs 20673863, 25118028, 29897170, 29184170.
2. **CHD8** *(row 40)* — truncating variants give macrocephaly and increased height/overgrowth in large
   clinical series. Chromatin-adjacent rather than a classical TF; carries severe neurodevelopmental
   baggage, so it is a target-validation datum, not a proposal. PMIDs 31001818, 36182950.
3. **ESR1 / the oestrogen receptor** *(row 68)* — the largest and best-documented "loss lengthens" effect in
   human skeletal biology: an ERα-null man, and men with aromatase deficiency, keep growing with unfused
   epiphyses into their twenties and thirties. This one is already exploited pharmacologically, and it is
   the proof of principle that removing a transcription factor's function adds adult height in humans.
4. **NR3C1 / the glucocorticoid axis** *(row 70)* — familial glucocorticoid deficiency presents with tall
   stature in childhood. ⛔ But the honest counterweight is that reported adult heights in MC2R-deficient
   cohorts end **below** target because of early puberty, so this is a childhood-height effect that does not
   bank. A cautionary member, not a candidate.

**Tier 2 — mechanistically a brake in cartilage, direction supported in animals, human height data absent**

5. **GLI3** *(row 14)* — the hedgehog repressor. Uniquely attractive because the brake is created by a
   *proteolytic processing step* (PKA→GSK3→CK1→βTrCP), not by DNA binding, so it is the one TF in this table
   whose activity could in principle be lowered by an enzyme inhibitor. Nobody has tried.
6. **NKX3-2/BAPX1** *(row 35)* — represses RUNX2 and delays hypertrophy, i.e. prolongs the proliferative
   phase. ⛔ Biallelic human loss is a dysplasia, so it is a band.
7. **ELF3/ESE-1** *(row 84)* — a direct ETS repressor of COL2A1 in human chondrocytes. Obscure, clean
   direction, no length endpoint anywhere.
8. **NFATC2** *(row 21)* — a genuine repressor of chondrogenesis; its null develops ectopic cartilage.
   Whether it restrains *length* has never been asked.
9. **SMAD6 / SMAD7** *(row 19)* — the inhibitory Smads; removing them raises BMP/TGF-β output.
10. **TWIST1** *(row 47)* — antagonises RUNX2 by occupying its DNA-binding domain. ⛔ But human
    haploinsufficiency (Saethre–Chotzen) is craniosynostosis, not tall stature.
11. **HDAC4** *(row 11)* — the MEF2 co-repressor; Hdac4-null mice ossify prematurely (so it is a brake on
    hypertrophy), yet limb-restricted deletion **shortens** limbs and closes the plate early. A band with
    both ends bad.

**Tier 3 — height-GWAS/exome burden signals in the "loss is taller" direction, mechanism unknown**

12. **LCORL/NCAPG** *(row 41)*, **ZFAT** *(42)*, **ZNF518A** *(43)*, **SCMH1** *(44)*, **HMG20B** *(45)*.
    These are the statistically strongest members and the biologically emptiest. ⛔ I could verify the
    general result that rare coding variants alter adult height with effects up to ~2 cm per allele
    (PMID 28146470), but I could **not** externally verify per-gene effect sizes for ZNF518A, SCMH1 or
    HMG20B, and they are marked UNVERIFIED. LCORL is additionally confounded: it sits in one linkage block
    with NCAPG and the causal gene is contested in every species examined.

**What is NOT on this list, and why that matters.** SOX9, SOX5/6, RUNX2, RUNX3, CBFB, MEF2C, SP7, GLI2,
SMAD1/5, STAT5B, SHOX, TRPS1, ATF4, CREB3L2, FOXA1-3, HIF1A, DLX5, HOXA11/D11, ZFHX4 — all POSITIVE. The
growth plate's transcriptional network is overwhelmingly built from required components, which is the
network-level reason the "inhibit something" reflex keeps failing in this tissue. **The productive
direction for most of this domain is RAISING a factor, and raising is what the pharmacopoeia does not do —
which is precisely why the oligonucleotide and CRISPRa rows (116, 117) matter more here than any inhibitor.**

---

## ANY TF IN THIS LIST WITH A REAL CHEMICAL OR OLIGONUCLEOTIDE HANDLE

**"Transcription factors are undruggable" is now false, and it stopped being true in a specific, datable
way.** Five distinct routes have each produced an agent that reached humans. Ranked by how real they are:

**A. Nuclear receptors — a ligand pocket by design (row 121).** Not news, but it is the reason four of the
levers already used against or for stature are TFs: **ER** (aromatase inhibitors remove the ligand; SERMs
and SERDs block or degrade the receptor), **AR**, **GR** (mifepristone, relacorilant), **VDR**, and **THR**
— where **resmetirom** is a marketed *isoform-selective* nuclear-receptor agonist, i.e. proof that the
selectivity problem is solvable within this family. RAR/RXR, PPAR, REV-ERB/ROR, ERR (GSK5182) and NR4A all
carry pockets too. If a growth-plate TF has a ligand-binding domain, it is already drugged.

**B. Targeted degradation — and this is the one that changed the field (rows 112–114).**
- ⭐⭐ **VEPDEGESTRANT (Veppanu) was approved by the FDA on 1 May 2026 as the first PROTAC, and its target is
  a transcription factor.** A TF is now removed as *protein*, orally, in routine human medicine.
- **SD-36**, a selective STAT3 degrader, produced complete tumour regression in mice — a TF with no ligand
  pocket, degraded because a bindable surface was enough (PMID 31715132).
- **TEAD PROTAC degraders are published** (PMID 38746898), on top of clinical-stage TEAD pocket inhibitors.
- ⭐⭐ And the two most skeletally relevant examples are *already human drugs doing this by accident*:
  **thalidomide degrades SALL4** (PMID 30067223) and **5-hydroxythalidomide degrades PLZF/ZBTB16**
  (PMID 33470442) via cereblon — the proposed mechanism of thalidomide limb teratogenicity. **A marketed
  drug already degrades skeletal transcription factors in humans. The direction is harmful; the capability
  is proven.**
- ⭐⭐ **Most of the growth-plate TF network is Cys2His2 zinc-finger — SP7, TRPS1, GLI1-3, SNAI1/2, ZEB1/2,
  KLF, EGR, ZFAT, ZNF518A** — and systematic work now maps which C2H2 fingers are degradable by
  cereblon glues and what predicts degradability (PMIDs 40845806, 40835825, 39218923). **That is the
  single most important generalisable fact in this domain.**

**C. Real orthosteric pockets in non-nuclear-receptor TFs.**
- ⭐⭐ **BELZUTIFAN**, an approved HIF-2α inhibitor, fills a buried cavity in a bHLH-PAS domain and breaks
  the HIF-2α/ARNT dimer. This is the structural template for what an anti-SOX9 or anti-RUNX2 agent would
  have to be, and it says such a thing is not impossible — it is a search problem.
- ⭐ **TEAD** has a lipid (palmitate) pocket; **VT3989, IK-930, IAG933** are clinical-stage. TEAD is the
  best-drugged node in the growth-plate network by a wide margin (row 63).
- ⭐ **CBFB** — the obligate RUNX partner — is a protein–protein interface with real chemistry from the
  inv(16) AML programme (AI-10-49 class). It is the only drugged node in the entire RUNX arm (row 7).
- ⭐ **β-catenin/TCF** is attacked from three sides at once: tankyrase inhibitors (Axin stabilisers, human
  phase 1), the CBP/β-catenin antagonist PRI-724, and PORCN inhibitors upstream (row 20).
- ⭐ **AP-1** has genuine small-molecule inhibitors that reached clinical study (T-5224 class, PMID 24831826).
- ⭐ **MRTF/SRF** has the CCG-1423/CCG-203971 series (row 80). **ID1/ID3** and **ETS** have tool compounds.

**D. Protein-based dominant negatives (row 120).** ⭐ **OMO-103 (Omomyc) completed a phase 1 trial**
(PMID 38321218) — an engineered mini-protein that poisons MYC dimerisation. The principle generalises to
every obligate-dimer TF in this table: **MYC/MAX, TWIST1/E-protein, ID/bHLH, AP-1 bZIP, HIF/ARNT, RUNX/CBFB,
SOX9/SOX5-6, YAP/TEAD.** Almost the entire growth-plate network is built from obligate heterodimers, which
is a structural argument that this modality fits this tissue unusually well.

**D2. Local delivery, which solves TF selectivity by geometry rather than by chemistry (row 123).**
⭐⭐ `PMID 39883086` — **RARγ-agonist-loaded nanoparticles implanted beside the proximal tibial growth plate
of juvenile mice closed THAT plate and shortened THAT tibia against the contralateral control**, and
one-sided implantation angulated the bone; RARα and RARβ agonists did nothing, and systemic dosing closed
plates everywhere. **This is the only experiment I found in which a transcription-factor drug was aimed at a
single growth plate and produced a compartment-specific skeletal result.** The direction demonstrated is
shortening (it was built as an alternative to epiphysiodesis for limb-length discrepancy), so **the mirror
experiment — a local RARγ ANTAGONIST depot — is the obvious unrun one.** It also shows that the two problems
this domain keeps hitting, "no selectivity" and "cannot reach avascular cartilage", can be attacked together
by putting the depot in the bone rather than in the bloodstream.

**E. Oligonucleotides — and this is the only class that goes UP (rows 115–117).**
- ⭐ **Decoy ODN:** a **STAT3 decoy oligonucleotide has been dosed in a first-in-human trial**
  (PMID 22719020). Sequence-programmable, so it works against factors with no pocket at all — but it only
  goes DOWN, and delivery into avascular cartilage is unsolved.
- ⭐⭐ **Upregulating ASOs (TANGO):** splice-switching oligos that block non-productive alternative splicing
  and thereby **raise** protein output from the healthy allele (PMID 32647108; also RNA-based translation
  activators, PMID 37884512). **This is the only pharmacological modality in the entire domain that points
  in the direction most growth-plate TFs need.** Directly relevant to SHOX, SOX9, RUNX2 and ACAN
  haploinsufficiency.
- ⭐⭐ **CRISPRa:** **activation of a promoter or an enhancer rescued a haploinsufficiency phenotype in vivo
  in mice** (PMID 30545847). That is the decisive precedent for treating a dosage disease by turning the
  remaining allele up instead of replacing the gene.

**The honest summary.** Of the TFs that actually set longitudinal growth, the ones with real chemical matter
are mostly the ones we do not want to touch (ER, GR, TEAD, β-catenin, p53, RB/CDK4-6, BET), and the ones we
would want to move (SOX9, SHOX, ACAN's transcription, RUNX2 dosage, CBFB, GLI3 processing) have none. **The
gap is not modality — five modalities now work in humans. The gap is that no programme has ever been pointed
at a growth-plate transcription factor.**

---

## REGULATORY ELEMENTS THAT COULD BE TARGETED INSTEAD OF THE GENE

This is where the domain pays off, because **the regulatory-DNA layer solves the two problems the protein
layer cannot: TISSUE SELECTIVITY and PARTIAL DOSAGE.** A systemic drug hits a TF in every cell that
expresses it and at whatever occupancy the PK allows. An enhancer is, by construction, active in one tissue
and often one compartment, and deleting or activating it produces a *graded* change.

**1. The decisive experiment already exists, and it is the Fgfr3 −29E enhancer (row 95).**
`PMID 39817451` — a cartilage-specific enhancer 29 kb upstream of mouse Fgfr3. CRISPR deletion **in
otherwise wild-type mice halved Fgfr3 in that cartilage domain with no adverse phenotype**; in an
achondroplasia model the same deletion largely normalised **long-bone and vertebral-body growth**, reduced
spinal-canal and foramen-magnum stenosis, improved craniofacial defects, and removed lethality. The element
is stated to be highly conserved in humans. **This is a clean, tissue-restricted, ~50% dosage change on a
growth-plate gene achieved by deleting non-coding DNA — exactly the shape of intervention the protein layer
has never delivered.** Note also that it reached the **vertebral bodies**, which most limb-directed agents do not.

**2. Compartment selectivity is real at the element level (rows 96–98).**
`PMID 38844479` maps **2,704 chondrocyte enhancers** and finds **74% pan-chondrogenic, 18% LIMB-restricted,
8% TRUNK-restricted** — and shows that height-associated variants overlapping chondrocyte enhancers explain
height better than variants over non-chondrogenic enhancers. It then deletes enhancers at **Fgfr3, Col2a1,
Hhip and Nkx3-2** and confirms each regulates its gene. **The Hhip enhancer deletion lowered Hhip in limb and
not trunk.** ⭐ **Nothing in pharmacology can do that. If a lever must reach the trunk and not the limb (or
vice versa), the enhancer is the only object that carries the address.** `PMID 39549696` does the human
version, separating skeletal-element-specific from global-acting height variants across growth plates
sampled from different bones.

**3. The single most common human enhancer lesion in short stature is already known: SHOX (row 107).** A
large share of SHOX-related short stature — Léri–Weill dyschondrosteosis and a slice of "idiopathic" short
stature — is caused by **deletion of PAR1 enhancers with an intact SHOX coding sequence**. The therapeutic
object for those patients is unambiguously an element, and the matching modality (CRISPRa at a promoter or
enhancer, PMID 30545847) has an in vivo haploinsufficiency rescue behind it.

**4. Elements, not genes, are the causal unit across the whole limb-skeletal disease catalogue.** The
pattern repeats so consistently that it should be treated as the default rather than the exception:
- **SOX9 upstream regulatory domain** (row 100) — breakpoints up to >1 Mb away; *which* territory is hit
  decides whether the patient has acampomelic campomelic dysplasia or isolated Pierre Robin sequence.
- **ZRS** at SHH (row 103) — single-base changes give preaxial polydactyly; duplications give triphalangeal
  thumb-polysyndactyly; and one specific variant gives **Werner mesomelic syndrome, a limb-shortening
  phenotype**. A graded allelic series in one enhancer.
- **CTCF sites at SHH** (row 104) — deleting the *insulator* rewires enhancer–promoter contacts and causes
  **acheiropodia**. The boundary, not the enhancer, can be the causal element.
- **IHH enhancer cluster** (row 102) — expression is set by the **composition and copy number** of a
  multipartite cluster; human duplications cause syndactyly and craniosynostosis. This is morphogen dosage
  titrated by DNA.
- **PITX1** (row 105), **DLX5/6** (row 106), **BMP2 downstream element** (row 108) — enhancer deletion,
  capture or duplication changes limb identity or digit length with the coding sequence untouched.

**5. ACAN is the case where the element is the ONLY route (row 101).** Aggrecan carries one of the largest
human height effects and **cannot be supplied as a protein**. Blocking its degradation is the
denosumab/aggrecanase trap. That leaves transcription — SOX9 acting with SOX5/SOX6 at a far-upstream ACAN
enhancer (PMID 18559420) and at the promoter (PMID 10753864). **CRISPRa at the ACAN enhancer is the only
concrete proposal in this domain for raising the plate's dominant proteoglycan.**

**6. The blunt version exists too, and it is a contraindication rather than a lever.** Chondrocyte
super-enhancers (row 109, PMID 26150426) are the class most sensitive to BET and CDK7/12/13 inhibition —
real, approved-or-clinical chemistry that would collapse the SOX-trio program non-selectively and is broadly
antiproliferative. Near an open growth plate that is a hazard to avoid, not an approach.

**What is missing, stated plainly.** No somatic enhancer editing of a growth plate has been reported in any
species; the Fgfr3 −29E result is germline. Enhancer deletion is irreversible, which is a hard objection for
a non-disease indication and for any axis with an interior optimum. And CRISPRa/ASO/decoy delivery into
avascular cartilage is unsolved for every one of them.

---

## WHAT I COULD NOT VERIFY

Listed so nothing here is mistaken for a checked fact.

1. **Per-gene height effect sizes for ZNF518A, SCMH1 and HMG20B.** I could not retrieve a primary source
   externally that states their height burden effects. Rows 43–45 are marked UNVERIFIED. What I *could*
   verify is the general result that rare and low-frequency coding variants alter adult height with effects
   up to about 2 cm per allele (PMID 28146470). The 1.45M-exome-scale burden analysis those genes are
   usually quoted from did not surface in my searches and I have not read it.
2. **ZFAT's height direction.** The gene appears in height-GWAS-adjacent literature (PMID 28146470 context),
   but I did not find a primary stating the sign and magnitude of its effect. Treated as UNVERIFIED.
3. **SOX6 human skeletal phenotype**, **SMAD7 stature phenotype**, **ZFHX4 stature**, **KLF15/EGR1 direction
   in cartilage**, **FOXN3/FOXP1/FOXL2 growth-plate roles**, **NR4A direction in the growth plate**, and
   **RARG-specific chondrocyte direction** — all searched, none returned a primary I would quote. Marked
   UNVERIFIED in their rows.
4. **A single-cell MULTIOME (paired RNA+ATAC) atlas of the human growth plate.** My targeted query returned
   only conference abstracts. A multi-omic atlas of human early skeletal development appeared as a
   no-PMID record in one result list. **I could not confirm that a published paired single-cell
   multiome of the postnatal human growth plate exists**, and I have recorded it as a gap rather than
   asserting either way. `PMID 39549696` (bulk-resolved human chondrocyte epigenomics across skeletal
   elements) and `PMID 38844479` (mouse chondrocyte enhancer atlas) are the two real resources I verified.
5. **Hi-C / TAD structure specifically in growth-plate chondrocytes.** I found TAD and CTCF work at
   *skeletal loci* (SHH, SOX9, HoxD, Pitx1) and a review of the emerging skeletal regulatory landscape
   (PMID 27814929), but no chondrocyte-specific Hi-C dataset. Recorded as a gap.
6. **Whether the Hhip elements deleted in PMID 38844479 are the same elements as the "CE2/CE3" naming used
   in the brief.** The paper deletes enhancers at the Hhip locus and reports a limb-selective reduction; I
   have described that result and have NOT asserted the CE2/CE3 label maps onto it.
7. **Exact regulatory-element nomenclature and coordinates** for the SHOX PAR1 enhancers and the SOX9
   upstream territories. The existence and disease relevance of both is well sourced; the specific element
   names and distances are not quoted.
8. **Belzutifan's precise binding-site description.** The approval and target are verified (PMID 33945366 and
   FDA/regulatory sources); my structural description ("buried PAS-B cavity disrupting the HIF-2α/ARNT
   dimer") is the standard account but I did not read the structural primary.
9. **Class IIa HDAC / Hdac4 limb-conditional length numbers.** I have stated the direction qualitatively; I
   did not retrieve a primary with the length measurements, so no numbers are given.
10. **Paywalled full texts.** Everything above is from abstracts and open-access records via Europe PMC and
    NCBI efetch. Where a claim needed a figure or a supplementary table, I did not make the claim.
