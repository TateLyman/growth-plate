# DOMAIN 19 — REGENERATIVE, GENETIC AND ADVANCED MODALITIES
## R436 full-concept-space enumeration (external search only; Europe PMC REST, NCBI eutils, WebSearch)

Compiled 2026-08-15. Every row carries species. Where a number, product or PMID could not be
verified from a primary record it is written `UNVERIFIED`. Reviews are used as an INDEX only and
are labelled as such.

**Scope note.** This domain is "everything that is not a small molecule". The organising question
throughout is not "does the modality exist" — most do — but **has it ever been shown to reach, or
act on, a GROWTH PLATE (physis) in vivo**, as opposed to articular cartilage, subchondral bone or
a joint space. Those are different tissues with different access routes, and the literature
conflates them constantly. Rows are marked accordingly.

---

## TABLE

| MODALITY | STATE OF THE ART | EVER APPLIED TO GROWTH PLATE? | DELIVERY ROUTE | OBTAINABLE? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| **Antisense oligonucleotide, PS/cEt gapmer (systemic)** | Ionis chemistry: full phosphorothioate backbone, 10-DNA gap flanked by three constrained-ethyl (cEt) nucleotides | **YES — the single clearest demonstration.** Human-COMP-specific ASOs reached **growth-plate** chondrocytes (shown by immunostaining against the ASO backbone), cut MT-COMP mRNA ~38% and endogenous mouse COMP ~60%, and largely reversed growth-plate chondrocyte pathology in a transgenic pseudoachondroplasia MOUSE. Authors explicitly note cartilage was "considered inaccessible" before this | **Subcutaneous, 60 mg/kg 3×/week for 3 weeks from postnatal day 7** | Research grade routine; GMP ASO manufacture is a mature industry (multiple approved ASOs) | 28162960 (mouse; erratum 42208536) | no |
| **ASO, splice-switching (e.g. exon skipping/inclusion)** | Approved in other tissues (nusinersen CNS, eteplirsen muscle) | **No growth-plate demonstration found.** No splice-switching ASO reported acting on a physis in any species | Intrathecal / systemic depending on tissue | GMP mature | UNVERIFIED for cartilage | yes |
| **ASO, steric-block (non-degrading, e.g. PMO)** | Morpholino chemistry; charge-neutral, so Donnan exclusion does not apply | **No** growth-plate demonstration found | Systemic | Research grade routine | UNVERIFIED for growth plate | yes |
| **ASO chemistry choice (PS backbone → protein binding → endocytosis)** | The mechanistic reason a polyanionic oligo can enter a fixed-negative-charge tissue at all: PS-ASOs are heavily protein-bound and taken up by endocytosis rather than free diffusion | Implicit in 28162960 | — | — | 28162960 (mouse) | **yes** |
| **siRNA, unconjugated** | Approved systemically only with hepatic targeting | Indirectly — siRNA reached growth-plate cartilage when carried in a cartilage-targeted exosome (below) | Needs a vehicle | Research grade routine | 38639394 (mouse/rat, engineered exosome) | no |
| **siRNA, GalNAc conjugate** | Standard-of-care hepatocyte delivery via ASGR1 | **No.** Wrong receptor — ASGR1 is a hepatocyte protein; nothing indicates growth-plate chondrocytes carry it | Subcutaneous | Approved products exist | UNVERIFIED for cartilage | no |
| **RNA aptamer (ligand trap)** | RBM-007, an anti-FGF2 RNA aptamer, given **subcutaneously**, restored defective skeletal growth in an achondroplasia MOUSE; also rescued iPSC-derived achondroplasia cartilage xenografts | **YES — bone growth endpoint in a mouse model** | Subcutaneous | Clinical-stage molecule (RBM-007, Ribomic); GMP oligo manufacture mature | 33952673 (mouse, rat chondrocytes, human iPSC xenograft) | no |
| **Soluble decoy receptor (recombinant protein trap)** | sFGFR3 / recifercept (PF-07256472): recombinant human soluble FGFR3 extracellular domain, subcutaneous, rescued achondroplasia in mice; taken into human phase 2; juvenile toxicity study run in cynomolgus monkeys | **YES — restored bone growth in mice; skull-base synchondroses imaged** | Subcutaneous | Was clinical-stage (Pfizer); phase 2 modelled against natural history | 24048522 (mouse), 33370388 (in vitro + in vivo), 35229060 (mouse skull base), 36367445 (monkey juvenile tox), 38685585 (human phase 2 modelling), 29652901 (mouse, obesity arm) | no |
| **Cartilage-targeted polymer nanoparticle, chondrocyte-membrane coated + WYRGRL** | CT-CM-NPs: PLGA core, primary-chondrocyte membrane coat, collagen-II-binding peptide WYRGRL; carried purmorphamine to growth-plate cartilage systemically in a hypochondroplasia mouse; increased bone AND body length | **YES — explicit growth-plate delivery with a LENGTH endpoint** | Systemic (tail vein) | Research grade only; membrane-coating is not a GMP-mature process | 42338508 (mouse, 2026) | no |
| **Engineered exosome / extracellular vesicle as a delivery vehicle to growth plate** | CT-Exo: cartilage-targeting engineered exosomes loaded with siRNA **and growth hormone**, aimed at growth-plate cartilage in idiopathic short stature | **YES — stated target is growth-plate cartilage** | Systemic | Research grade | 38639394 (2024) | no |
| **MSC-derived exosomes as a therapeutic (not a carrier)** | Single intra-articular injection of 100 µg human MSC exosomes after surgical growth-plate defect in rats promoted repair and **reduced limb-length discrepancy** | **YES — limb-length endpoint** | **Intra-articular** | Research grade; MSC-EV GMP is emerging | 35175995 (rat) | no |
| **Exosome-loaded ECM-mimetic hydrogel at a physeal defect** | Local implant combining EVs with an anti-inflammatory hydrogel to repair growth-plate injury | **YES (injury model)** | Surgical implantation into the physeal defect | Research grade | 34901536 (rat/rabbit — species UNVERIFIED) | no |
| **Cationic peptide carrier (CPC+14 class) on a protein** | Short arginine-rich, hydrophilic, net +14; drives full-thickness penetration of proteins into cartilage by Donnan partition; demonstrated for IGF-1 (7.6 kDa) and IL-1Ra (17 kDa) | **NOT on a growth plate** — every result is ARTICULAR cartilage reached by intra-articular injection | Intra-articular | Research grade; peptide fusion is GMP-compatible in principle | 35858920 (IGF-1, rat/bovine), 36739939 (IL-1Ra) | no |
| **Cationic protein carrier — avidin / multi-arm avidin** | Avidin (66 kDa, pI ~10) penetrates full-thickness cartilage and forms a bound depot; multi-arm avidin nanoconstructs deliver dexamethasone and kartogenin | **NOT on a growth plate** — articular only | Intra-articular | Avidin is a commodity protein | 24120044, 24753019, 26211608, 29205258, 31843642, 35491681 (rat/bovine) | no |
| **Charge-engineered biologic (cationic IL-1Ra, terminus chosen computationally)** | catIL-1RA: carrier at the C-terminus, chosen to preserve receptor binding; outperforms anakinra on joint retention | **No** — articular | Intra-articular | Research grade | 41453720 (rat, 2026) | no |
| **Collagen-II-binding peptide WYRGRL as a targeting ligand** | Now used on nanoparticles, liposomes, microspheres, EVs, hydrogels **and lentiviral envelopes** | **YES via CT-CM-NPs** (42338508); otherwise articular | Systemic or intra-articular | Peptide synthesis trivial | 42338508, 41614872, and ~30 further articular papers | no |
| **Collagen-hybridising peptide (CHP) targeting** | Binds DENATURED collagen; used to image and to deliver a therapeutic antibody in rheumatoid arthritis models | **No.** Wrong ligand for a healthy physis — CHP reports damage, not intact matrix | Systemic | Research grade | 42010292 (mouse, 2026), 39247402 | yes |
| **Lentivirus with a cartilage-targeting envelope** | LV envelope engineered with WYRGRL, carrying GALNS under CBh or COL2A1 promoters, given IV or intra-articularly to MPS IVA newborn mice; peptide-modified vector raised enzyme in non-liver tissues and lowered keratan sulfate | Aimed at **bone and cartilage**; growth-plate-specific readout UNVERIFIED | IV and intra-articular | Research grade; LV GMP mature (ex vivo products approved) | 41614872 (mouse, 2025) | **yes** |
| **AAV serotype selection for cartilage** | Head-to-head of 14 serotypes: only AAV2, 5, 6 and 6.2 substantially transduced human chondrocytes; AAV2 and AAV6.2 nominated as best for intra-articular cartilage | **No growth-plate arm** — articular cartilage and OA models | Intra-articular | AAV GMP mature | 34522160 (human cells, mouse OA, human explants) | no |
| **AAV, intra-articular, in vivo chondrocyte transduction** | Comparative 7-serotype study found AAV2 most efficient to mouse arthritic chondrocytes; self-complementary AAV in canine joints | **No** | Intra-articular | GMP mature | 33320893 (mouse), 36261499 (canine), 15183427 | no |
| **CRISPR/Cas9 germline enhancer deletion as a DOSAGE tool** | Deleting a −29 kb cartilage enhancer of mouse *Fgfr3* halved Fgfr3 in cartilage in otherwise WT mice **with no adverse phenotype**, and in achondroplastic mice normalised long-bone AND vertebral body growth, reduced foramen magnum stenosis and removed lethality; the element is conserved in humans | **YES — genetic, germline; long bone and vertebra endpoints** | Germline zygote editing (not a delivered therapy) | Not a product; a proof of concept | 39817451 (mouse, 2025) | no |
| **Somatic CRISPR nuclease delivered to a growth plate** | — | **NO REPORT FOUND IN ANY SPECIES.** SpCas9 ≈160 kDa, far beyond the measured physeal size cutoff | — | — | UNVERIFIED / none found | **yes** |

| **Base editing (ABE/CBE)** | Approved-adjacent in liver/HSC; corrects point mutations without a DSB | **No cartilage or growth-plate report found.** Achondroplasia is a single recurrent missense (G380R) and is the obvious substrate — no in vivo skeletal base-editing paper located | — | Research grade | UNVERIFIED / none found | **yes** |
| **Prime editing** | Search-and-replace editing, larger cargo than base editors | **No growth-plate report found** | — | Research grade | UNVERIFIED / none found | **yes** |
| **CRISPRa (dCas9-VP64/SAM) — RAISE a gene** | Injectable CRISPRa microspheres used in bone to activate A20 and rescue age-related osteogenic impairment; CRISPRa of *Tfeb* in osteoblast-lineage cells increased bone mass and strength (transgenic, not delivered) | **No growth-plate arm** | Local microsphere implant (bone); transgenic otherwise | Research grade | 41213207 (2026, bone), 40728889 (mouse, osteoblast lineage) | **yes** |
| **CRISPRi (dCas9-KRAB)** | Persistent transcriptional repression; requires continuous expression of a >160 kDa fusion | **No growth-plate report** | — | Research grade | UNVERIFIED for cartilage | yes |
| **Epigenome editing to RESTORE expression (dCas9-TET / demethylation)** | Epigenome editing restored *FBN1* expression by demethylating a CpG-island shore — in porcine fibroblasts | **No** (cells only) — but FBN1 is a height gene, so the precedent is directionally relevant | — | Research grade | 40129967 (porcine cells, 2025) | **yes** |
| **ASO that RAISES a protein — TANGO / poison-exon skipping** | Targeted Augmentation of Nuclear Gene Output: an ASO blocks a non-productive (poison) exon so more mRNA becomes productive; raises SCN1A protein and rescues Dravet mice; clinical-stage in that indication | **No skeletal application found** | Intrathecal in the published indication | GMP ASO manufacture mature | 32848094, 34843701 (mouse), 39946203, 36946385 | **yes** |
| **SINEUP antisense lncRNA — RAISES translation of a chosen mRNA** | Synthetic antisense lncRNA with a SINE B2 effector domain that increases translation of the sense target ~2-fold without changing mRNA level; demonstrated in vivo for GDNF in a Parkinson mouse | **No skeletal application found** | AAV or synthetic RNA | Research grade | 31495777 (mouse), 33012004, 35228902 | **yes** |
| **Enzyme replacement therapy, untargeted (elosulfase alfa etc.)** | Approved for MPS IVA; explicit consensus is that it has only a limited impact on bone growth and skeletal lesions | **Reaches bone poorly; skeletal/growth benefit limited** — an important negative for "can a 100+ kDa enzyme reach cartilage" | IV infusion | Approved products | 37373036 (statement of limitation), 25284089, 26331768, 42279040 | no |
| **Bone-targeted ERT (acidic oligopeptide / Asp-tagged protein)** | Deca-aspartate and related acidic oligopeptides direct proteins to hydroxyapatite; the approved example is **asfotase alfa** (TNSALP-Fc-deca-aspartate) for hypophosphatasia | Asfotase alfa acts on **mineralising** tissue and improves growth in children with HPP; whether it enters unmineralised physeal cartilage is UNVERIFIED | Subcutaneous | **Approved (asfotase alfa)** | 18537566, 27376160, 30558909, 30811537 (human) | no |
| **Bone-targeted LNP-mRNA (Asp8-conjugated)** | SA@LNP-D: Asp8-peptide-conjugated LNP redirected mRNA from liver to bone and expressed an **anti-sclerostin antibody** in bone in an OVX mouse | **No growth-plate arm** — but this is the clearest "make a biologic in situ" precedent in skeleton | Systemic | Research grade; LNP GMP mature | 42338194 (mouse, 2026) | **yes** |
| **LNP-mRNA to articular cartilage** | LNP-encapsulated recombinant human FGF18 mRNA delivered intra-articularly for OA | **No** — articular | Intra-articular | Research grade | 39363784 (mouse) | no |
| **Bone-targeted LYTAC (extracellular protein degrader)** | Dual-action LYTAC with bone-specific accumulation reported for bone disorders | **No growth-plate arm** | Systemic | Research grade | 41450662 (2025) | **yes** |
| **AAV expressing a SECRETED PEPTIDE (protein-raising gene therapy)** | AAV vector expressing C-type natriuretic peptide **induced bone growth and chondrocyte proliferation** in an MPS IVA mouse | **YES — bone growth endpoint, secreted-factor mechanism** | Systemic AAV (route as reported; UNVERIFIED here) | Research grade; AAV GMP mature | 37373036 (mouse, 2023) | **yes** |
| **Ex vivo lentiviral HSPC gene therapy (systemic enzyme supply)** | HSPC gene therapy for Hurler syndrome with an early **skeletal outcome** readout in humans | Skeletal outcomes measured in children; growth-plate-level effect UNVERIFIED | Autologous transplant | Clinical/approved-adjacent | 34788506, 38691622 (human) | no |
| **Allogeneic HSCT as a skeletal/growth intervention** | Systematic review of growth outcomes after HSCT in MPS; height after HSCT in MPS I/II analysed against dermatan sulfate | Growth is measured but skeletal disease persists; classic statement that HSCT does not correct dysostosis | IV transplant | Standard of care in MPS I | 40083105 (systematic review — INDEX), 39272740, 34408967 (human) | no |
| **Skeletal-stem-cell agonist depot implanted INTO the secondary ossification centre** | SAG-containing beads implanted into the rat femoral SOC of one leg made that leg significantly longer at 1, 2 and 6 months vs the vehicle-bead contralateral leg; transient intra-articular SAG also raised epSSC number | **YES — the cleanest local-depot demonstration with a LENGTH endpoint** | **Intraosseous (into the SOC)**, plus an intra-articular arm | SAG is research grade only (no GMP) | 38516888 (rat/mouse, 2024) | no |
| **Growth-plate organoids (in vitro)** | Layered-induction 3D culture system producing growth-plate organoids | In vitro model, not a therapy | — | Research grade | 41643409 (2026) | **yes** |
| **hPSC-derived skeletal assembloids** | Human pluripotent-stem-cell limb skeletal assembloids modelling human limb skeletal development | In vitro model | — | Research grade | preprint 2025 (PMID UNVERIFIED) | **yes** |
| **iPSC-derived cartilage xenograft as a disease model / test bed** | Achondroplasia-patient iPSC-derived cartilage xenografts used to test an aptamer | Test bed, not a therapy for a physis | Xenograft | Research grade | 33952673 (human iPSC in mouse) | yes |
| **iPSC-derived chondrocyte particles / sheets** | Plate-based self-aggregation to make chondrocyte particles from human iPSC chondroprogenitors; iPSC limb-bud mesenchyme chondrocyte sheets | **No growth-plate application** — aimed at articular repair | Surgical implantation | Research grade; clinical iPSC cartilage work is in articular indications | 39596131, 36829201 | no |
| **Autologous chondrocyte implantation into a physeal defect** | Autogenous cultured **growth-plate** chondrocyte transplantation in rabbit physeal injury; autogenous chondrocytes in rabbit growth-plate injury; perichondrium-derived chondrocytes in rabbit physeal defects | **YES — physeal defect models** | Open surgical implantation | Autologous cell products exist (articular ACI/MACI approved) | 25376625, 12143986, 16263608 (rabbit) | no |
| **Cultured chondrocyte allograft to replace a physis** | Early attempts to reconstruct a physis with cultured chondrocytes of varying developmental time **failed** to make a functional or structural physis | **YES — and it is a NEGATIVE** | Surgical | — | 8423511, 3611332 (rabbit) | **yes** |
| **Free / microvascular physeal allograft transfer** | Free physeal transplantation in rabbit; survival of microvascular physeal allografts after short-term immunosuppression | **YES** | Surgical, vascularised | Not a product | 6418748, 14960672 | yes |
| **Vascularised autograft physeal transfer (clinical)** | Vascularised proximal fibular epiphyseal transfer for radial longitudinal deficiency — a growing physis moved with its blood supply in children | **YES — human, and it grows** | Microsurgery | Surgical technique, no product | 25539323 (human) | no |
| **MSC transplantation for physeal bar** | Allogeneic and autogenous MSCs for physeal bone bridge in rabbits; allogeneic stem cells to prevent bone bridge in minipigs; MSC+chondrocyte composite scaffold in pigs; systematic review of MSCs in paediatric physeal growth arrest | **YES — bar prevention / repair models, and a human systematic review** | Surgical implantation into the defect | Autologous/allogeneic MSC products exist regionally | 18789143 (rabbit), 19093735 (pig), 22217406 (pig), 41141171 (systematic review — INDEX) | no |
| **Adipose stromal vascular fraction at a physeal defect** | SVF prevented bone-bridge formation after growth-plate injury in rat | **YES (injury model)** | Local implantation | Point-of-care devices exist | 33194176 (rat) | yes |
| **Synovial-MSC scaffold-free tissue-engineered construct** | In vitro-generated scaffold-free construct from rabbit synovial MSCs used to treat partial growth arrest | **YES (injury model)** | Surgical | Research grade | 22411340 (rabbit) | yes |
| **Autologous tissue-engineered composite for physeal injury** | Composite graft in rabbit growth-plate injuries | **YES (injury model)** | Surgical | Research grade | 17053322 (rabbit) | yes |
| **3D-bioprinted hydrogel/polymer scaffold with factor delivery for physeal repair** | Printed construct providing both growth-factor release and mechanical support at a growth-plate injury | **YES (injury model)** | Surgical implantation | Research grade | 37324424 | no |
| **Injectable hydrogel + bilayer microspheres (anti-angiogenic + pro-chondrogenic) for physeal repair** | Designed to inhibit angiogenesis (bar formation) while promoting cartilage | **YES (injury model)** | Injection into defect | Research grade | 37274168 | yes |
| **Classical interposition materials for bar resection (fat, silicone, bone cement/PMMA)** | Langenskiöld procedure and its descendants; free fat interposition; cement interposition; MRI follow-up of fat grafts | **YES — human standard of care for physeal bar**, though results are variable and a 2025 study found **acute fat autograft did NOT protect against bar formation** | Open surgery | Off-the-shelf materials | 10823590, 1516323, 11204797, 40403121 (negative, 2025), 41196964 (human cement) | no |
| **Fibrin sealant / autologous cartilage as interposition** | Fibrin interposition prevented growth arrest in one model; autologous cartilage + fibrin sealant possibly superior to fat in porcine physeal bridge prevention | **YES** | Surgical | Fibrin sealants are **approved** (Tisseel/Evicel) | 19918192, 33204354 (porcine) | no |
| **Recombinant growth factor at a physeal defect (rhOP-1/BMP-7)** | rhOP-1 tested on growth-plate repair in a sheep model | **YES** | Local implantation | Was a marketed device (OP-1); availability now limited (UNVERIFIED) | 15946820 (sheep) | yes |
| **Physeal distraction / chondrodiatasis (mechanical, not biological)** | Distraction across an intact physis to lengthen; long-term human results published; also used for joint-preserving tumour surgery; **risk of premature physeal closure after femoral chondrodiatasis is documented** | **YES — human, growth plate is the actual target tissue** | External fixator | Standard devices | 11961457, 1590047 (negative), 22203330 (human) | no |

| **CARTILAGE-HOMING ANTIBODY FRAGMENT (scFv anti-matrilin-3)** | Yeast-display-selected human scFv binding human and mouse matrilin-3 (a cartilage-restricted ECM protein); **injected IV in mice it specifically homed to cartilage**; explicit stated purpose was to couple chondrogenic factors to it | **YES — homing to growth-plate cartilage from the bloodstream** | **Intravenous** | Research grade; scFv GMP mature | 25690340 (mouse, 2015) | **yes** |
| **⭐ CARTILAGE-TARGETED IGF-1 FUSION PROTEIN (CaAb-IGF-1 / CV1574-1 / CV1623-1)** | scFv-anti-matrilin-3 fused to IGF-1. Subcutaneous injection raised **growth-plate height** in GH-deficient (lit) mice without raising kidney cortical cell proliferation; alternate-day dosing sufficient; CV1574-1 restored plate height under pegvisomant-induced GH resistance with **less hypoglycaemia** than IGF-1; **CV1623-1 (2026) significantly increased body weight, TAIL LENGTH and TIBIAL BONE LENGTH on alternate-day dosing.** Commercialised by Cavalry Biosciences ("precision IGF-1 medicines") | **YES — repeatedly, with a BONE-LENGTH endpoint, from a SYSTEMIC route** | **Subcutaneous** | Company-stage preclinical (the 2026 paper says trials "would be required"); antibody-fusion GMP is entirely routine | 30765323 (mouse, 2019), 39850478 (mouse, 2025), 41877483 (mouse, 2026) | no |
| **Anti-aggrecan Fab / F(ab')₂ — matrix-binding + downsizing** | Head-to-head in rat: control IgG 143 kDa < anti-aggrecan IgG 141 kDa < anti-aggrecan F(ab')₂ < **anti-aggrecan Fab** for cartilage concentration and penetration; matrix binding and size act synergistically | **No — articular**, but the design rule transfers | Intra-articular (systemic arm UNVERIFIED) | Chugai; research/preclinical | 40097892 (rat, 2025) | **yes** |
| **Antibody-size solute diffusion measurements in cartilage** | Direct measurement of how antibody size and mechanical loading affect diffusion through the articular surface | Articular | — | — | 28672295 | yes |
| **Anti-ADAMTS-5 nanobody (VHH), e.g. M6495** | ~15 kDa single-domain format protecting cartilage ex vivo; the smallest true antibody format | **No growth-plate report; no cartilage-delivery measurement located for a nanobody** | Systemic in the OA programme | Clinical-stage in OA (UNVERIFIED current status) | 32825512 (ex vivo human/bovine) | no |
| **Chondrocyte-homing peptide from phage display (non-viral vector targeting)** | A chondrocyte-homing peptide identified by phage display used to target non-viral vectors to cartilage in vivo | **No growth-plate arm** | Systemic/local | Research grade | 21624651 | **yes** |
| **Chondrocyte-affinity peptide (CAP) on PAMAM dendrimer** | CAP-modified PAMAM conjugate as a cartilage-targeting/retention nanoplatform | Articular | Intra-articular | Research grade | 29528264 | yes |
| **Cartilage-penetrating nanocarrier for a growth factor** | Nanocarriers improved delivery and efficacy of growth-factor treatment in OA | Articular | Intra-articular | Research grade | 30487252 | no |
| **Peptide-siRNA nanocomplex for cartilage** | Peptide–siRNA nanocomplex targeting NF-κB designed for efficient cartilage delivery | Articular | Intra-articular | Research grade | 30679644 | yes |
| **Tetrahedral framework nucleic acid (tFNA / DNA nanostructure) carriers** | Cartilage-penetrating framework nucleic acid nanoparticles; siRNA and miRNA delivery to chondrocytes; aptamer-modified variants | **No growth-plate report** | Intra-articular | Research grade | 40192172, 39330704, 39282962 | yes |
| **Engineered EVs carrying Cas9 / CRISPR machinery to chondrocytes** | Cas9 exosome vesicles for ASPN editing; CAP-LAMP2b EV–CRISPR hybrids targeting ADAMTS4; hybrid exosomes enabling chondrocyte-specific genomic editing | **No growth-plate report** — all OA | Intra-articular | Research grade | 41689014, 41097079, 35836795 | **yes** |
| **Bacteriophage-based particles displaying chondrocyte ligands** | Ligand-directed phage particles targeting human osteoarthritic chondrocytes | No | — | Research grade | 34960616 | **yes** |
| **Ultrasound-enhanced (sonoporation) transport into cartilage** | Ultrasound-enhanced molecular transport in articular cartilage studied directly; ultrasound-responsive gene-activated matrices exist for bone | **No growth-plate report** — and the physis lies deep to the epiphysis, so acoustic access differs | External ultrasound + systemic/local agent | Devices exist | 39145819, 28084018 | **yes** |
| **Microneedle patches for joint/skin-adjacent delivery** | Microneedles delivering nanoparticle payloads in arthritis models | **No** — cannot reach a physis (depth) | Transdermal | Research grade | 41840375, 41444549 | yes |
| **Gene-activated matrix (scaffold + nucleic acid) for skeletal repair** | Large literature in calvarial/long-bone defect repair; bioprinted gene-activated scaffolds for articular cartilage; AAV-loaded gene-activated matrices | **No growth-plate report found** | Implanted scaffold | Research grade; one clinical bone-substitute programme reported | 39649247, 42358449, 33614609 (INDEX) | yes |
| **AAV released from a fibrin scaffold (local depot for a vector)** | Bioactive AAV released from fibrin glue; fibrin concentration tunes release | No | Local implant | Fibrin approved; AAV GMP mature | 21449684 | yes |
| **Bisphosphonate / hydroxyapatite-binding drug conjugate** | Hydroxybisphosphonate-conjugated sitafloxacin studied for fracture healing **and skeletal growth** in mice; acidic-oligopeptide-tagged drugs as a general bone-targeting platform | Skeletal growth was an endpoint; **growth-plate cartilage is unmineralised, so a mineral-binding tag targets the metaphysis/primary spongiosa, not the plate itself** | Systemic | Bisphosphonate chemistry is commodity | 41783235 (mouse, 2026), 18663412, 27803481 | **yes** |
| **Recombinant peptide therapeutic reaching the growth plate (CNP analogue)** | **Vosoritide** — a 39-aa CNP analogue (~4 kDa), daily subcutaneous, APPROVED, raises height velocity in achondroplasia; extended in a phase 2 basket trial to RASopathies, **ACAN** and **NPR2** deficiency | **YES — approved human drug whose site of action is the growth plate** | Daily subcutaneous | **Approved (Voxzogo)** | 42026358 (meta-analysis — INDEX), 41967490 (basket trial) | no |
| **Peptide prodrug / carrier-linked long-acting peptide (TransCon)** | **Navepegritide (TransCon CNP)** — CNP transiently conjugated to a PEG carrier, released by pH/temperature-dependent linker cleavage; once-weekly; phase 2 ACcomplisH met height-velocity endpoint | **YES** | Weekly subcutaneous | Approved/approval-stage (UNVERIFIED current status) | 37823031 (human phase 2), 35481707 (human phase 1), 31235532 | no |
| **Protein half-life engineering (Fc fusion, CTP fusion, albumin binding, PEG prodrug) for GH** | Somatrogon (hGH-CTP fusion), lonapegsomatropin (TransCon hGH), somapacitan (albumin-binding) — all weekly | Acts via the GH/IGF-1 axis, not by entering the plate as a large protein | Weekly subcutaneous | **Approved** | 34272849, 35428884, 38333899 | no |
| **Recombinant IGF-1 and IGF-1/IGFBP-3 binary complex** | Mecasermin; mecasermin rinfabate (rhIGF-1 + rhIGFBP-3) — the complex form was an explicit attempt to change the pharmacokinetics of a growth factor | Systemic, acts on the plate indirectly | Subcutaneous | Approved (mecasermin); rinfabate status UNVERIFIED | see 30765323 discussion | no |
| **Guided growth / tension-band plating (hemiepiphysiodesis)** | The one routinely used clinical intervention that manipulates a physis mechanically and reversibly | **YES — human standard of care**, though it redirects rather than adds growth | Surgical implant | Approved devices | 32773655 and general orthopaedic literature | no |
| **Distraction osteogenesis (regenerate as engineered bone)** | Limb lengthening; regenerate quality is the rate-limiter; adjuncts studied include rhBMP, teriparatide, sclerostin antibody | Bypasses the growth plate entirely — works after fusion | Surgical + external/internal device | Approved devices | see domain on limb lengthening | no |
| **Bone marrow aspirate concentrate / PRP at a physeal or osteochondral site** | Widely used clinically in cartilage/OA; in physeal injury the evidence base is thin and inconsistent | Occasionally in physeal/osteochondrosis contexts | Local injection | Point-of-care | 41133728 (review — INDEX) | yes |
| **Decellularised cartilage/bone ECM scaffolds** | Standard scaffold class; prochondrogenic decellularised ECM from iPSC-derived chondrocytes | **No physis-specific product** | Implant | Research + some commercial ECM products | 37295627 | yes |
| **Hydrogel depot chemistries (fibrin, GelMA, alginate, agarose, HA)** | Fibrin sealant is FDA-approved and paediatric-labelled; GelMA/alginate/agarose are research materials; agarose beads are the classic morphogen depot in developmental biology | **YES for agarose beads and fibrin** (see SAG bead row; fibrin interposition row) | Implant/injection | Fibrin approved; others research grade | 38516888, 19918192 | no |
| **Microspheres / microcarriers as local depots** | Bilayer microspheres for physeal repair; PLGA microspheres for corticosteroid; injectable CRISPRa microspheres in bone | **YES (physeal repair microspheres)** | Local | Research grade | 37274168, 41213207, 42514970 | no |
| **Cell-membrane-coated nanoparticles** | Chondrocyte-membrane-coated PLGA is the coat used in CT-CM-NPs; the general class also uses RBC, platelet, macrophage and MSC membranes | **YES — via CT-CM-NPs** | Systemic | Research grade only | 42338508 | no |
| **Plant-derived / dietary extracellular vesicles** | Grape-skin-derived EVs engineered for cartilage targeting | No | Systemic/local | Research grade | 42387506 | **yes** |
| **Ribozymes** | Catalytic RNA; largely superseded by RNAi and ASOs | **No cartilage or growth-plate application found** | — | Research grade | UNVERIFIED / none found | yes |
| **Suppressor tRNA / nonsense readthrough** | Engineered tRNAs to read through PTCs; relevant in principle to nonsense alleles in ACAN, FGFR3-adjacent genes, COL2A1 | **No skeletal application found** | Systemic (LNP/AAV) | Research grade, several companies | UNVERIFIED for skeleton | **yes** |
| **De novo designed protein minibinders (Rosetta/AlphaFold)** | Now routine to design ~5–15 kDa high-affinity binders to a chosen surface; the size class that Farnum's data say CAN enter a growth plate | **No growth-plate application found in any species** | Systemic | Research grade; expression is trivial | UNVERIFIED / none found | **yes** |
| **Macrocyclic peptides (mRNA display / RaPID)** | 1–2 kDa constrained peptides with antibody-like affinity; small enough to partition freely by the Farnum criterion | **No growth-plate application found** | Systemic | Research grade | UNVERIFIED / none found | **yes** |
| **PROTAC / molecular glue (intracellular degradation)** | Requires target + E3 ligase + proteasome in the same cell; VHL/CRBN chemistry mature | **No growth-plate report found**; small-molecule PROTACs are ~0.7–1 kDa so size is not the obstacle | Oral/systemic | Approved-adjacent | UNVERIFIED for growth plate | yes |
| **AUTAC / ATTEC / autophagy-directed degraders** | Emerging degrader classes for aggregates and organelles | **No cartilage application found** | — | Research grade | UNVERIFIED | **yes** |
| **RIPTAC (regulated induced proximity targeting chimera)** | Very new; induces a cell-killing proximity in target-positive cells | Irrelevant direction for growth (kills cells) | — | Research grade | UNVERIFIED | **yes** |
| **Cell-penetrating peptide (TAT/RALA class) delivery to chondrocytes** | Used for transcription-factor delivery and for hTGFβ3 transfection into precartilaginous stem cells | **No growth-plate in vivo report** | Local | Research grade | 23757322, 33611769 | yes |
| **Magnetic nanoparticle targeting to a skeletal site** | Reported for cartilage imaging (USPIO) and MSC steering | **No growth-plate report** | Systemic + external magnet | Research grade | 37397872 | yes |
| **Rabbit/porcine standardised physeal-injury models (enabling infrastructure)** | Purpose-built models for evaluating regenerative approaches at a physis, incl. a rabbit model paper and a new rabbit method paper | — | — | — | 31552802, 35959744, 28830302 (review — INDEX) | yes |


### Delivery routes and access physics (same columns)

| MODALITY | STATE OF THE ART | EVER APPLIED TO GROWTH PLATE? | DELIVERY ROUTE | OBTAINABLE? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| **The three vascular routes into a physis (epiphyseal / metaphyseal / perichondrial ring)** | Multiphoton imaging of live mouse tibial physis showed tracers arrive from all three directions; for ≤10 kDa, epiphyseal and metaphyseal entry are equally permissive | **YES — this is the foundational measurement** | Intracardiac tracer injection (experimental) | — | 16342207 (mouse, 2006) | no |
| **Measured SIZE CUTOFF for entry into a growth plate** | Fluorescein (332 Da) and 3 and 10 kDa dextrans entered from all three directions; **40 kDa and larger dextrans did not enter within a detection limit of a few percent of vascular concentration** | **YES** | Systemic | — | 16342207 (mouse) | no |
| **…and the qualification of that cutoff** | A later study using the same technique **did quantify 40 and 70 kDa dextran entry** into murine tibial physes and their temperature dependence — so 40–70 kDa entry is small but non-zero, not absent | **YES** | Systemic | — | 24371019 (mouse, 2014) | **yes** |
| **A permissive mid-plate transport region** | Fluorescence photobleaching + in vivo multiphoton found a relatively permissive band at the growth-plate midplane (late proliferative/early hypertrophic), plus fluid flow from both chondro-osseous junctions | **YES** | — | — | 17496046 (mouse, 2007) | **yes** |
| **LOCAL LIMB HEATING as a delivery adjunct** | Raising hindlimb temperature 22→34 °C (a physiological human knee range) increased 10 kDa dextran entry into the physis **>150%**, 40 and 70 kDa by <50%; blood velocity +118%, vessel diameter +31% | **YES — a non-invasive delivery modality specific to the growth plate** | External warming + systemic agent | Free / trivially obtainable | 24371019 (mouse, 2014) | **yes** |
| **EXERCISE as a delivery adjunct** | Exercise mitigated cold-induced stunting of limb elongation in mice **by increasing solute delivery to the growth plate** | **YES** | Behavioural | Free | 20930127 (mouse, 2010) | **yes** |
| **Intra-articular route to a physis** | Transient intra-articular SAG raised epiphyseal skeletal stem cell number; MSC exosomes given intra-articularly repaired a physeal defect and cut limb-length discrepancy | **YES in juvenile rodents.** ⚠ Caveat: in an older animal or an adolescent human the epiphysis is largely ossified, so a joint injection is separated from the resting zone by bone | Intra-articular | Routine clinically | 38516888, 35175995 | no |
| **Intraosseous / intra-epiphyseal (into the SOC) route** | SAG beads implanted into the rat femoral secondary ossification centre; clinically, image-guided intraosseous subchondral injection ("subchondroplasty") of the human knee is an established procedure | **YES (rat, with a length endpoint)**; the human procedure exists but has never carried a growth-plate payload | Percutaneous, image-guided, intraosseous | Procedure routine; payloads are not | 38516888 (rat), 41950892 (human review — INDEX) | **yes** |
| **Systemic (SC/IV) route to a physis** | The route used by every demonstration that actually moved bone length — ASO (28162960), aptamer (33952673), sFGFR3 (24048522), CT-CM-NPs (42338508), CaAb-IGF-1 (30765323/41877483) | **YES** | SC or IV | — | as listed | no |
| **Donnan partition / fixed charge density as the design variable** | Cartilage FCD is strongly negative, so cationic solutes partition IN and anionic solutes are excluded; this is the whole basis of the avidin and CPC+14 carriers | **Measured in ARTICULAR cartilage; not measured for a human physis** | — | — | 24120044, 24753019 | no |
| **A CSF-equivalent bypass route** | Intrathecal dosing gives ASOs access to the CNS at low systemic exposure. **There is no anatomical equivalent for a growth plate** — no compartment that bathes all physes | **No — and this is a structural fact, not a gap** | — | — | none | **yes** |

### Additional genetic / protein-supply modalities

| MODALITY | STATE OF THE ART | EVER APPLIED TO GROWTH PLATE? | DELIVERY ROUTE | OBTAINABLE? | EVIDENCE (PMID) | OBSCURE? |
|---|---|---|---|---|---|---|
| **⭐ LIVER-DEPOT AAV making a large secreted ENZYME that reaches the physis** | AAV8 with a liver-specific promoter expressing human GALNS, single IV dose 5×10¹³ GC/kg in MPS IVA mice; plasma enzyme **4–19× wild-type** and sustained; storage reduced in articular cartilage, ligament, meniscus **and the growth-plate region** | **YES — functional evidence of a ~55 kDa (dimeric ~120 kDa) enzyme acting in the growth-plate region** | Single IV AAV; the *protein* arrives via plasma | AAV GMP mature | 32577432 (mouse, 2020) | **yes** |
| **AAV expressing tissue-nonspecific alkaline phosphatase (hypophosphatasia)** | High-level AAV-driven ALP ameliorated pathological bone structure in an HPP mouse | Skeletal; growth-plate-specific readout UNVERIFIED | Systemic AAV | Research grade | 32076747 (mouse) | yes |
| **AAV expressing full-length PTH** | Bioactive full-length parathyroid hormone delivered by AAV | Skeletal | Systemic AAV | Research grade | 35666091 | yes |
| **Lentiviral gene therapy with a skeletal readout (MPS VII)** | Skeletal response to lentivirally mediated gene therapy in MPS VII mice | Skeletal | Systemic/ex vivo | Research grade | 22525091 (mouse) | yes |
| **Gene therapy reversing GROWTH FAILURE as an endpoint (GSD Ia)** | Pathogenesis of growth failure and its partial reversal by gene therapy in murine and canine glycogen storage disease type Ia | **Growth failure endpoint, systemic metabolic mechanism** | Systemic vector | Research grade | 23623482 (mouse, dog) | **yes** |
| **AAV gene therapy for achondroplasia specifically** | Searched: the achondroplasia clinical pipeline in 2026 is peptides (vosoritide, navepegritide) and oral small molecules (infigratinib, TYRA-300) plus the RBM-007 aptamer. **No AAV or other gene-therapy programme for achondroplasia was found in clinical development** | **No** | — | — | none found (WebSearch, Aug 2026) | no |


---

## PROSE 1 — MODALITIES DEMONSTRATED TO REACH GROWTH-PLATE CARTILAGE IN VIVO, IN ANY SPECIES

This is the list the domain exists to produce. I have separated **direct physical demonstration that the
agent was in the plate** from **functional demonstration that something changed at the plate**, because
the literature routinely blurs them. Everything below is *growth plate*, not articular cartilage.

**A. Direct physical demonstration (the molecule was seen, or measured, inside a physis)**

1. **Small fluorescent tracers, by all three vascular routes.** `16342207` (mouse, 2006, Farnum/Williams,
   multiphoton through an intact perichondrium): fluorescein (332 Da) and 3 kDa and 10 kDa dextrans entered
   the proximal tibial physis from epiphyseal, metaphyseal **and** perichondrial-ring vessels; epiphyseal
   and metaphyseal entry were equally permissive. **40 kDa and larger did not enter within a detection
   limit of a few percent of vascular concentration.** This is the origin of the "size cutoff" idea.
2. **40 kDa and 70 kDa dextrans, at low but measurable levels.** `24371019` (mouse, 2014, Serrat) explicitly
   quantified 10, 40 and 70 kDa dextran accumulation in tibial physes and their temperature dependence.
   The honest statement is therefore *not* "nothing above 40 kDa enters" but "entry falls steeply with
   size and is a few percent or less of vascular concentration above ~40 kDa".
3. **A BIOACTIVE PROTEIN — fluorescently labelled IGF-1, 8.2 kDa.** `28798204` (mouse, 2017, Serrat & Ion):
   labelled IGF-I was readily taken up into proximal tibial growth plates of live mice and localised to
   chondrocytes, with bioactivity confirmed separately by Akt phosphorylation in metatarsal culture. The
   authors note the cellular fluorescence pattern was *completely distinct* from inert probes — i.e. this
   was receptor-mediated uptake, not passive filling.
4. **A PHOSPHOROTHIOATE/cEt GAPMER ASO.** `28162960` (transgenic MT-COMP mouse, 2017, Posey/Hecht with
   Ionis): **60 mg/kg subcutaneously, three times weekly for three weeks from postnatal day 7.** ASO was
   detected in **growth-plate** and articular chondrocytes by immunostaining against the ASO backbone;
   human MT-COMP mRNA fell ~38% and endogenous mouse COMP ~60%; growth-plate chondrocyte pathology,
   inflammation and cell death were largely reversed. **This is the single strongest demonstration in the
   whole domain: molecule visualised in the tissue, target engaged, phenotype rescued, systemic route.**
5. **A cartilage-homing antibody FRAGMENT.** `25690340` (mouse, 2015, Baron lab NIH): yeast-display scFv
   against matrilin-3, injected **intravenously**, "specifically homed to cartilage" by
   immunohistochemistry in mouse sections. This is the localisation evidence the later IGF-1 fusion
   proteins lean on.
6. **A polymer nanoparticle.** `42338508` (mouse, 2026): chondrocyte-membrane-coated PLGA bearing WYRGRL
   (CT-CM-NPs) "effectively delivered … Purmorphamine to the growth plate cartilage" from a systemic route
   in a hypochondroplasia model, with body and bone length as the endpoint.

**B. Functional demonstration (bone length or growth-plate architecture moved, route systemic or local)**

7. **RNA aptamer, subcutaneous** — RBM-007 restored defective skeletal growth in achondroplasia mice
   (`33952673`).
8. **Recombinant soluble decoy receptor, subcutaneous** — sFGFR3/recifercept rescued achondroplasia
   symptoms and restored bone growth in mice (`24048522`), with a monkey juvenile toxicity study
   (`36367445`) and a human phase 2 (`38685585`).
9. **Cartilage-targeted IGF-1 antibody fusion, subcutaneous** — increased growth-plate height in *lit* mice
   (`30765323`), restored plate height under pegvisomant-induced GH resistance (`39850478`), and in 2026
   increased **tibial bone length and tail length** on alternate-day dosing (`41877483`).
10. **Intraosseous morphogen depot** — SAG-loaded beads implanted into the rat femoral secondary
    ossification centre made that leg significantly longer than the vehicle-bead contralateral leg at 1, 2
    and 6 months (`38516888`). Same paper: transient **intra-articular** SAG raised epiphyseal skeletal
    stem cell number.
11. **MSC exosomes, intra-articular** — promoted growth-plate repair and reduced limb-length discrepancy
    after a surgical physeal defect in rats (`35175995`).
12. **Engineered cartilage-targeting exosomes carrying siRNA + growth hormone** — aimed explicitly at
    growth-plate cartilage in idiopathic short stature (`38639394`).
13. **A large secreted ENZYME produced by a liver depot** — AAV8-GALNS gave 4–19× wild-type plasma enzyme
    and reduced substrate storage **in the growth-plate region** in MPS IVA mice (`32577432`).
14. **AAV expressing a secreted PEPTIDE** — AAV-CNP induced bone growth and chondrocyte proliferation in
    MPS IVA mice (`37373036`).
15. **Approved peptides** — vosoritide (~4 kDa CNP analogue, daily SC) and navepegritide (TransCon CNP,
    weekly SC) both act at the growth plate in children, which is the only *human* entry on this list
    besides physeal surgery.
16. **Cells and matrices placed surgically into a physeal defect** — autologous growth-plate chondrocytes
    (`25376625`), perichondrium-derived chondrocytes (`16263608`), MSCs (`18789143`, `19093735`), adipose
    SVF (`33194176`), synovial-MSC constructs (`22411340`), 3D-bioprinted scaffolds (`37324424`), fat and
    fibrin interposition (`10823590`, `19918192`), rhOP-1 (`15946820`). These reach a physis by being put
    there; none is a systemic delivery result.
17. **Non-invasive physiological adjuncts** — local limb heating (`24371019`) and exercise (`20930127`)
    both increased solute delivery to the growth plate in mice, and the exercise effect was tied to limb
    elongation. These are the only "delivery modalities" on the list that cost nothing.

**C. What has NOT been shown to reach a growth plate** (searched, not assumed): any viral vector delivered
locally to a physis; any CRISPR nuclease, base editor or prime editor in any species; any nanobody or
minibinder; any full IgG; any PROTAC; any splice-switching or steric-block ASO; any GalNAc conjugate;
any LNP-mRNA; any aptamer other than by systemic action; any microneedle or ultrasound-assisted delivery.

---

## PROSE 2 — WHAT THE LARGEST SUCCESSFULLY DELIVERED MOLECULE WAS, AND HOW

Three defensible answers, depending on what "delivered" is allowed to mean. They should be quoted
separately because they support different design decisions.

**(a) Largest molecule directly MEASURED inside a growth plate: a 70 kDa dextran.**
`24371019` (mouse, in vivo multiphoton) quantified 10, 40 and 70 kDa dextran accumulation in tibial
physes. Entry at 40 and 70 kDa is small — Farnum's earlier work put 40 kDa below a detection limit of a
few percent of vascular concentration (`16342207`) — but it is not zero and it is temperature-sensitive.
**How: passively, from the subperichondrial plexus and the two chondro-osseous junctions.**

**(b) Largest BIOACTIVE PROTEIN construct shown to act at a growth plate from a systemic route:
CV1574-1 / CV1623-1, a three-part fusion of IGF-1 + a MONOMERIC antibody Fc + an anti-matrilin-3 scFv.**
Confirmed format from the open-access text of `39850478`. No molecular weight is stated in that paper;
by composition it is of the order of ~55–65 kDa (IGF-1 7.6 kDa + monomeric Fc + scFv ~27 kDa) —
**that arithmetic is mine and the figure is UNVERIFIED.** Doses used were 12 mg/kg SC in one-week-old
pups, 1.5 mg/kg SC in adults, 5.25 mg/kg SC once daily for efficacy. **How: subcutaneous injection plus
an ECM-binding targeting arm** — the scFv binds matrilin-3, a cartilage-restricted matrix protein, which
both concentrates the drug in cartilage and (per `39850478`) prolongs AKT signalling in a
matrilin-3-dependent way. Important honesty: the 2019 paper did **not** image the fusion protein in the
plate; localisation rests on the earlier free-scFv homing result (`25690340`).

**(c) Largest protein with FUNCTIONAL evidence in the growth-plate region: GALNS, a lysosomal sulfatase
(~55 kDa monomer, active as a larger oligomer).** `32577432`: a single IV AAV8 dose with a liver-specific
promoter produced **4–19× wild-type plasma enzyme, sustained for 12 weeks**, and reduced stored substrate
in the growth-plate region as well as articular cartilage, ligament and meniscus. **How: not by making
the protein more penetrant, but by making the plasma concentration enormous and continuous.** The authors
say so explicitly — continuous high circulating enzyme increases penetration into bone. That is a
different engineering lever from targeting, and it is the one the ERT field partly failed at:
conventional intermittent elosulfase alfa infusion has only limited impact on bone growth (`37373036`).

**The design rule that falls out.** Three independent handles raise physeal exposure: (i) **be small** —
below ~10 kDa transport is essentially free; (ii) **bind the matrix** — `40097892` showed in articular
cartilage that aggrecan binding and downsizing act *synergistically*, with anti-aggrecan Fab ≫ F(ab')₂ ≫
IgG, and the matrilin-3 scFv is the physeal version of the same trick; (iii) **hold the plasma level high
for a long time** — the AAV liver-depot result. A fourth, cheap and almost unexploited: **raise local
blood flow** (heating, exercise), which bought >150% more 10 kDa entry in mice.

---

## PROSE 3 — MODALITIES THAT WOULD LET YOU RAISE A PROTEIN RATHER THAN BLOCK ONE

This matters because a screen that ranks genes by "loss shortens" returns load-bearing genes, and the
needed direction is elevation — the direction the small-molecule pharmacopoeia does not serve. There are
seven mechanistically distinct ways to raise a protein, and they differ enormously in how mature they are.

1. **Supply the recombinant protein, with a cartilage-targeting arm bolted on.** Fully demonstrated at a
   growth plate with a bone-length endpoint: CV1623-1 (`41877483`). The generalisable component is the
   **anti-matrilin-3 scFv** (`25690340`) — it is a reusable address, and its authors said so at the time.
   Any secreted or matricellular protein whose loss shortens (the SCUBE3/CHAD/SMOC1/osteolectin class) is
   in principle fusable to it. Manufacturing path: standard mammalian expression, entirely GMP-routine.
2. **Supply a soluble decoy that raises the FREE concentration of an endogenous ligand.** sFGFR3 works the
   other way (it removes FGF), but the same architecture inverted — a decoy for a *clearance receptor* or
   an inhibitor — raises the free ligand without adding any. This is what the NPR3-occupant idea is, and
   the aptamer `33952673` and recifercept `24048522` are the two proofs that ligand-trap proteins reach
   the plate from a subcutaneous injection.
3. **Make the protein in situ from mRNA.** `42338194` conjugated **Asp8** (hydroxyapatite-binding) to an
   LNP and got an anti-sclerostin antibody expressed **in bone** in mice. No growth-plate version exists.
   Note the caveat that a mineral-binding tag targets mineralised tissue, i.e. the metaphysis, not the
   unmineralised physeal cartilage — so Asp8 is the wrong address for the plate even though it is the
   right idea.
4. **Make the protein in situ from DNA.** AAV expressing a secreted peptide already produced **bone
   growth** in a mouse (`37373036`, AAV-CNP), and AAV liver depots raise plasma enzyme 4–19× wild type
   (`32577432`). For a *secreted* target this is the highest-leverage route in the domain, because the
   producing cell does not have to be a chondrocyte. For a cell-autonomous intracellular target it is
   useless, because no AAV serotype has been shown to transduce a growth plate (the tropism work
   `34522160`, `33320893` is all intra-articular and articular).
5. **Raise output of the endogenous gene — transcriptionally.** CRISPRa (dCas9-VP64/SAM) has been
   delivered locally in bone by injectable microspheres (`41213207`) and used transgenically to raise bone
   mass (`40728889`). Epigenome editing has restored expression of a *height gene* — `40129967` demethylated
   a CpG-island shore to restore **FBN1** — but in porcine fibroblasts, not cartilage. The unsolved part is
   delivery: a dCas9 fusion is >160 kDa and must persist, which is the worst possible profile for a physis.
6. **Raise output of the endogenous gene — post-transcriptionally, with an OLIGO.** This is the most
   under-appreciated set and the one that fits the tissue best, because the ASO chemistry class is the
   *only* macromolecule with proven growth-plate access (`28162960`):
   - **TANGO / poison-exon-skipping ASOs** convert non-productive transcript into productive transcript
     and raise protein without touching the promoter (`32848094`, `34843701`). Proven in vivo in brain;
     never tried on a skeletal gene.
   - **SINEUP antisense lncRNAs** raise translation of a chosen mRNA ~2-fold without changing mRNA level,
     demonstrated in vivo for GDNF (`31495777`).
   - **uORF- or miRNA-site-blocking steric ASOs** (same chemistry, different site) — no skeletal example.
   These are the only "raise a protein" modalities that inherit an existing growth-plate delivery proof.
7. **Remove the endogenous brake instead of adding the protein.** Two forms, both proven at a physis:
   knock down an inhibitor with a gapmer ASO (`28162960` did exactly this, just for a toxic gain-of-function
   protein), or **delete a repressive/dosage regulatory element**. `39817451` is the cleanest example in
   the whole domain — deleting a −29 kb cartilage enhancer of *Fgfr3* halved the gene in cartilage only,
   with no adverse phenotype in wild-type mice, and rescued long-bone **and vertebral body** growth in the
   achondroplasia model. Enhancer editing as a *dosage dial* is directly transferable to raising a gene
   (delete a silencer, or add/de-repress an enhancer), and the element is conserved in humans.

**Ranked by what could actually be attempted.** (1) is the only one already demonstrated at a growth plate
with a length endpoint and a company behind it. (6) is the cheapest to try because the chemistry already
gets in. (4) is the highest ceiling for secreted targets. (3) and (5) are blocked on delivery. (7) is the
best genetics and the worst deliverability. Nothing in (2)–(7) has ever been given to a human growth plate.

---

## WHAT I COULD NOT VERIFY

- **Molecular weights.** No paper I could reach states a kDa figure for CV1574-1/CV1623-1, for the
  anti-matrilin-3 scFv, or for the CT-CM-NPs payload. The ~55–65 kDa estimate in PROSE 2 is my arithmetic
  from the stated composition and is **UNVERIFIED**.
- **CT-CM-NP dose, particle size and biodistribution quantification** (`42338508`) — I read the abstract
  only; the full text was not retrieved.
- **Species and model for `34901536`** (exosome-loaded hydrogel for growth-plate injury) — abstract only;
  species recorded as UNVERIFIED.
- **Whether asfotase alfa's deca-aspartate tag delivers it into unmineralised physeal cartilage**, as
  opposed to the mineralisation front. The growth benefit in children with HPP is well documented; the
  physeal-cartilage localisation is not something I could verify.
- **Current clinical status** of recifercept, RBM-007, M6495 and navepegritide. I have their published
  trial reports but did not confirm 2026 development status for each; treat all as UNVERIFIED.
- **Cavalry Biosciences' development stage.** The company website exists and describes "precision IGF-1
  medicines", and the 2026 paper states that preclinical studies and clinical trials "would be required" —
  which I read as pre-IND. No registered trial was found.
- **Whether any AAV gene therapy for a skeletal dysplasia is in clinical development.** A WebSearch of the
  achondroplasia pipeline (August 2026) returned only peptides, small molecules and the RBM-007 aptamer.
  Absence in a search is weaker than a registry query; I did not exhaustively enumerate clinicaltrials.gov.
- **clinicaltrials.gov systematically.** My one API query returned poorly matched results; the human
  cell-therapy question is instead answered by `41141171`, a 2025 systematic review which concludes that
  after screening, **no human studies of stem cells for physeal growth arrest remained** — i.e. the entire
  cell-therapy arm of this domain is animal-only.
- **Ribozymes, suppressor tRNAs, de novo minibinders, macrocyclic peptides, AUTAC/ATTEC and RIPTAC** —
  I searched each against cartilage/growth plate and found nothing. Those rows are marked as no-report
  rather than as verified negatives; a null Europe PMC query is not proof of absence.
- **Whether the intra-articular route reaches the resting zone in an older/adolescent subject.** Every
  positive intra-articular result (`38516888`, `35175995`) is in a juvenile rodent whose epiphysis is
  still largely cartilaginous. I could find no measurement of intra-articular access to a physis in a
  skeletally mature-ing large animal or human.
