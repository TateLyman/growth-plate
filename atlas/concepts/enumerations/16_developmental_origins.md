# DOMAIN 16 — DEVELOPMENTAL ORIGINS AND LIMB PATTERNING — COMPLETE INVENTORY (R436)

**Method.** Every row below was reached by EXTERNAL search only — Europe PMC REST (`/search`,
`resultType=core`) and NCBI eutils `efetch` for abstracts. No file in `/home/user/growth-plate` was read
except the two briefs. Where I could only see a title (not the abstract), the row says so. Where I could
not verify a number, the cell says `UNVERIFIED`. Reviews are used as an INDEX and are labelled as such.

**The governing question, applied to every row.** A developmental gene earns a place in this atlas only if
it is **still doing work in an OPEN POSTNATAL GROWTH PLATE**. Embryonic necessity does not transfer. The
column `DOES IT STILL ACT POSTNATALLY?` is therefore answered per row with one of:
- **YES-DIRECT** — a postnatal/juvenile perturbation or postnatal expression+function experiment exists
- **YES-EXPR** — postnatally expressed in plate/perichondrium, function postnatally not tested
- **PROBABLY-NO** — evidence it is an embryonic-only requirement
- **NO-ARCHITECTURE** — it acted once, set a starting condition, and is gone; it still constrains adult
  length through the geometry it left behind
- **UNKNOWN** — nobody has looked (under the atlas's own rule this is a GAP, not a disqualification)

---

## TABLE

| # | EVENT/GENE | WHAT IT SETS | DOES IT STILL ACT POSTNATALLY? | EVIDENCE (species + PMID) | RELEVANT AT BA16? | OBSCURE? |
|---|---|---|---|---|---|---|
| **A. AXIS, LIMB FIELD, LIMB BUD INITIATION** |
| 1 | Lateral plate mesoderm (somatic layer) | The entire source cell pool for limb skeleton; limb bud cell number at initiation | NO-ARCHITECTURE | Classic embryology; no single PMID cited here — UNVERIFIED as a discrete citable experiment | No — but it fixes the founding progenitor number | no |
| 2 | Retinoic acid / RALDH2 (ALDH1A2) | Limb field induction; permissive for Tbx5; later a proximalising signal | PROBABLY-NO for initiation; RA signalling is separately active postnatally (CYP26/RARγ) | mouse, PMID 15069081 (Raldh2 required early for limb bud initiation, then AER); mouse, PMID 26212321 (RA→Tbx5 coherent feed-forward) | Indirect only | no |
| 3 | **TBX5** | Forelimb bud initiation; forelimb identity; Holt-Oram syndrome in humans | PROBABLY-NO (initiation-stage requirement) | mouse, PMID 12490567 (Tbx5 essential for forelimb bud initiation *after* limb-field patterning); mouse/chick PMID 12399308, 12736216 (Tbx5→Wnt2b/Fgf10) | No | no |
| 4 | **TBX4** | Hindlimb bud initiation and outgrowth; NOT hindlimb identity | Hindlimb-enhancer alleles set *bone size regionally* — see #5 | mouse PMID 12736212 (Tbx4 loss blocks hindlimb dev); PMID 17164415 (**not** required for identity or post-bud outgrowth) | No | no |
| 5 | **Tbx4 hindlimb enhancer elements (HLEA/HLEB)** | **Region-specific control of BONE SIZE** — a *cis*-element that scales an element rather than specifying it | NO-ARCHITECTURE, but it is a direct demonstration that enhancer dose sets skeletal element size | mouse/vertebrate, PMID 18579682 ("Dual hindlimb control elements in the Tbx4 gene and region-specific control of bone size") | No, but conceptually load-bearing | **YES** |
| 6 | **PITX1** | Hindlimb identity; sets hindlimb-characteristic morphology and *targeted growth control* | UNKNOWN postnatally | mouse PMID 10049363, 10073939 (Pitx1 upstream of Tbx4); PMID 22071103 (Pitx1 shapes hindlimb morphology **via targeted growth control**); PMID 16989801 (muscle/tendon/bone morphology) | Unlikely direct | no |
| 7 | **PITX1 human alleles — Liebenberg syndrome** | *Upper* limb transformed toward *lower* limb character by a deletion upstream of PITX1 | NO-ARCHITECTURE | human, PMID 23587911; also PMID 18950742 (asymmetric lower-limb malformation), PMID 22258522 (mirror-image polydactyly) | No | **YES** |
| 8 | WNT2B / WNT8C | Upstream/parallel to FGF10 in limb bud induction | PROBABLY-NO | chick/mouse PMID 12399308 (Tbx5 interacts with Wnt2b and Fgf10); AER re-induction by wnt-2b + fgf-10 PMID 20347761 | No | no |
| 9 | **FGF10** | Mesenchymal signal that induces and maintains the AER; limb bud outgrowth | UNKNOWN in plate; FGF10 is a known postnatal FGFR2b ligand elsewhere | chick PMID 20347761; mouse (Fgf10-null limbless) — canonical, PMID UNVERIFIED here | No | no |
| 10 | **AER / FGF4, FGF8, FGF9, FGF17** | Distal outgrowth; number of progenitors that survive to be allocated to each segment | NO-ARCHITECTURE for the AER itself; FGF/FGFR signalling is emphatically postnatal (FGFR3) | chick PMID 8221896 (FGF-4 replaces the AER); mouse PMID 15328019 (Fgf4+Fgf8); review-as-index PMID 12152071 | AER no; the FGFR axis yes (different node) | no |
| 11 | AER removal / limb truncation experiments | Demonstrates that the *time* the AER is present sets how many PD segments form | NO-ARCHITECTURE | chick, classical (Saunders); PMID UNVERIFIED | No | no |
| 12 | WNT3 (human) / Wnt3a (mouse) — AER induction | Tetra-amelia in humans when WNT3 is lost | NO-ARCHITECTURE | human tetra-amelia — gene WNT3; specific PMID UNVERIFIED in this round | No | no |
| 13 | SP8 / SP6 (AER transcription factors) | AER integrity; downstream of WNT/FGF | UNKNOWN | mouse; specific PMID UNVERIFIED in this round | No | **YES** |
| 14 | **GREM1 (Gremlin) ↔ BMP** | Maintains the SHH–FGF positive-feedback loop; sets duration of bud outgrowth | UNKNOWN in plate | chick/mouse PMID 10619030 (Meis2 proximal + Gremlin distal BMP antagonism maintain Shh/FGF loop) | No | no |
| 15 | BMP2/BMP4 in AER/ectoderm | AER induction, DV patterning, interdigital death — **not** limb outgrowth per se | BMP signalling is postnatally active in the plate | mouse PMID 19210962 (Bmp2/Bmp4 in AER required for DV patterning and ICD **but not limb outgrowth**); chick PMID 11714672 | BMP axis yes, this arm no | no |
| **B. ZONE OF POLARISING ACTIVITY, ANTEROPOSTERIOR AXIS** |
| 16 | **SHH (ZPA)** | Digit number and identity; posterior expansion of the bud; indirectly total progenitor number via the SHH–GREM1–FGF loop | Hedgehog signalling is emphatically postnatal in the plate — but that is **IHH**, not limb-bud SHH | mouse/chick, canonical; ETV4/5 restrict Shh posteriorly PMID 19386268 | ZPA-SHH no; the Hh axis yes | no |
| 17 | **ZRS / MFCS1 (SHH limb enhancer, ~1 Mb away, in LMBR1 intron 5)** | A single distant enhancer that controls where and how much SHH the limb bud makes; a textbook example of a non-coding element setting skeletal pattern | NO-ARCHITECTURE | human, PMID 18463159 (ZRS variant deregulates SHH expression, triphalangeal thumb); PMID 18178630 (ZRS microduplication → TPT-PS); PMID 22495965 (13 bp insertion → PPD + TPT); PMID 24456159 (microduplications → Haas-type polysyndactyly / Laurin-Sandrow); PMID 31395945 | No | no |
| 18 | **pre-ZRS** | A *second*, separate cis-element upstream of the ZRS; point mutation → triphalangeal thumb-polysyndactyly | NO-ARCHITECTURE | human, PMID 29543231 | No | **YES** |
| 19 | **ZRS affinity-optimising variants** | Shows the enhancer is tuned to SUB-optimal binding affinity on purpose; raising affinity breaks the limb | NO-ARCHITECTURE, but a general principle for any enhancer-dose lever | mouse/human, PMC-indexed 2022 preprint "Affinity-optimizing variants within the ZRS enhancer disrupt limb development" — PMID UNVERIFIED (PMC record only) | No | **YES** |
| 20 | **ZRS → Werner mesomelia** | A ZRS point change can shorten the *zeugopod* (mesomelic limb shortening), i.e. an AP enhancer producing a LENGTH phenotype | NO-ARCHITECTURE | human, PMID 24478176 | No — but it is a rare case of an AP element moving segment LENGTH | **YES** |
| 21 | **GLI3 / GLI3-repressor** | Anterior identity; digit number; the SHH-independent default state | GLI3R is the node CLAUDE-level hedgehog work runs through; postnatal plate role UNKNOWN separately | human, PMID 28224613 (review-as-index, GLI3-related polydactyly); variant-position→phenotype PMID 32591344 | Indirect | no |
| 22 | **HAND2** | Establishes limb-bud posterior polarity upstream of Shh | PROBABLY-NO | mouse, PMID 20386744; PMID 25453830 (HAND2 target network compartmentalises early bud) | No | no |
| 23 | **TBX3** | Sets the posterior boundary of anterior genes with HAND2 at limb-bud onset; human TBX3 = ulnar-mammary syndrome (limb reduction) | UNKNOWN | PMID 38828908 | No | **YES** |
| 24 | **ETV4 / ETV5 (PEA3 family)** | FGF-dependent posterior restriction of SHH; promotes bud outgrowth | UNKNOWN | mouse, PMID 19386268; preaxial polydactyly ETV/TWIST1/HAND2 PMID 20826535 | No | **YES** |
| 25 | ISL1 | Establishes the posterior HINDLIMB field upstream of Hand2-Shh | PROBABLY-NO | mouse, PMID 22438573 | No | **YES** |
| **C. PROXIMODISTAL PATTERNING — the axis that actually sets segment LENGTH** |
| 26 | **Progress-zone model vs early-specification / two-signal model** | Whether PD identity is timed inside a distal zone or specified early by opposing signals. **Directly relevant: it determines whether segment length is set by residence time or by allocation.** | NO-ARCHITECTURE | chick, PMID 12152081 (re-examination — the classic challenge to the progress zone); PMID 19553938 (re-evaluation of X-irradiation phocomelia); evolutionary two-step model PMID 15108812 | No, but it frames "is length set by a clock or a count?" | no |
| 27 | **MEIS1 / MEIS2 (+PBX1)** | Proximal (stylopod) identity; ectopic Meis proximalises and abolishes distal structures | UNKNOWN in plate | chick/mouse, PMID 10586884, 10619030, 19247936; RING1/PcG restricts Meis2 PMID 26674308 | Unlikely | no |
| 28 | **CYP26B1** | Degrades RA distally; sets the proximal RA gradient. Loss → **meromelia** (limb truncation) in mouse | **YES-DIRECT elsewhere in this atlas's own genetics** (CYP26B1 is a human height gene); postnatal plate role of the PD arm UNKNOWN | mouse, PMID 15030763 | Possibly — as a retinoid-clearance node, not as a PD node | no |
| 29 | HOX9/HOX10 paralogues | Stylopod (humerus/femur) formation | UNKNOWN | mouse; specific PMID UNVERIFIED this round | No | no |
| 30 | **HOXA11 / HOXD11** | Zeugopod (radius-ulna, tibia-fibula) formation — **and, separately, an early step of CHONDROCYTE DIFFERENTIATION upstream of Runx2 and Shox2** | **YES-DIRECT (lineage): Hox11-expressing cells are self-renewing skeletal stem cells that make osteoblasts, chondrocytes and adipocytes THROUGHOUT LIFE** | mouse, PMID 14668414 (multiple roles in zeugopod); mouse, PMID 22916278 (Hoxa11/Hoxd11 arrest chondrocyte differentiation *before* the round→columnar transition; upstream of Runx2 and Shox2); mouse, PMID 31320650 (Hoxa11-CreERT2 lineage = lifelong MSC, upstream of LepR-Cre and Osx-CreER); PMID 27939685 (regionally restricted Hox function in ADULT marrow MSCs) | ⭐ **YES — this is the single strongest "developmental gene still working postnatally" row in the domain** | **YES** |
| 31 | **Hox11 and postnatal ARTICULAR cartilage zonation** | Hox11 marks developing zeugopod synovial joints and is coupled to POSTNATAL articular cartilage morphogenesis into functional zones | **YES-DIRECT** | mouse, PMID 34010606 | Yes (articular, adjacent compartment) | **YES** |
| 32 | **HOXA13 / HOXD13** | Autopod. HOXA13 also drives *Aldh1a2* to permit interdigital cell death | HOXD13: **YES-EXPR/DIRECT in the postnatal-relevant plate** — controls cell POLARITY in the metacarpal growth plate and perichondrium with WNT5A | mouse, PMID 24161848 (spdh Hoxd13 mutant metacarpal growth plates lose linear cell orientation; metacarpals transformed to carpal-like, lacking cortical bone and perichondrium); PMID 23553814 (HOXA13→Aldh1a2) | Yes for the polarity mechanism | **YES** |
| 33 | **Loss of Hox → loss of a growth plate entirely** | The human pisiform lost its growth plate and its second ossification centre; Hox is implicated in whether a skeletal element HAS a growth plate at all | NO-ARCHITECTURE | comparative human/ape, PMID 25279687; PMID 27507801 (Hox, pisiform/calcaneus growth plates and the zeugopod/autopod boundary) | ⭐ Conceptually — a growth plate is not guaranteed, it is specified | **YES** |
| 34 | **SHOX2** | Proximal limb; required for chondrocyte proliferation and maturation in the proximal skeleton; targets include **NPPB and ACAN** | UNKNOWN postnatally, but its targets are the atlas's own nodes | mouse, PMID 17481601; PMID 23038774 (progression through chondrogenesis); PMID 24421874 (**NPPB and ACAN are SHOX2 transcriptional targets**); PMID 24347445 (Tbx4–Shox2 interaction); PMID 25217052 (Shox2×Hox genetic interaction in regional growth) | ⭐ Yes — NPPB/ACAN are live nodes | **YES** |
| 35 | **SHOX (human, pseudoautosomal PAR1)** | Human-specific; haploinsufficiency = Léri-Weill dyschondrosteosis, Madelung deformity, Turner short stature, ~2-15% of idiopathic short stature; **duplication reported with TALL stature** | **YES-DIRECT — GH therapy in SHOX deficiency is randomised-trial supported** | human, PMID 27194967 (review-as-index); PMID 38572386 (randomised phase 3 GH in Japanese SHOX-deficient children); PMID 31093387 (SHOX duplication + tall stature); PMID 34811950 (CNVs OUTSIDE the enhancer region also cause LWD/short stature) | ⭐⭐ **YES — SHOX has no mouse orthologue, so mouse work systematically misses it** | no (SHOX) / **YES** (the enhancer CNVs) |
| **D. DORSOVENTRAL PATTERNING** |
| 36 | **WNT7A** | Dorsal ectoderm signal; also feeds back on SHH. Human loss → Fuhrmann and Al-Awadi/Raas-Rothschild limb-reduction syndromes | UNKNOWN in plate | human/mouse; WNT7A/WNT7B–GPR124–RECK module PMID 35552394 | No | no |
| 37 | **LMX1B** | Dorsalisation; human = **nail-patella syndrome** (patellar hypoplasia, iliac horns, nephropathy) | UNKNOWN in plate | human, PMID 34545091 (limb-specific Lmx1b auto-regulatory modules with NPS pathogenicity); PMID 37899549 (enhancer deletion → mild NPS) | No | no |
| 38 | **EN1** | Ventral ectoderm; restricts Wnt7a dorsally | UNKNOWN | mouse, PMID 41986232 / preprint (temporal loss of En1 gives distinct phenotypes) | No | **YES** |
| 39 | **MAENLI lncRNA (limb-specific EN1 regulator)** | A non-coding RNA whose deletion produces limb malformation by de-regulating EN1 — a *trans*-acting non-coding layer on a patterning gene | NO-ARCHITECTURE | human/mouse, PMID 33568816 | No | **YES** |
| 40 | **WNT7A/WNT7B–GPR124–RECK module** | An adhesion-GPCR co-receptor system required for the WNT7 arm of limb development | UNKNOWN | mouse, PMID 35552394 | No | **YES** |
| **E. MESENCHYMAL CONDENSATION, DIGIT SELF-ORGANISATION, JOINT SPECIFICATION** |
| 41 | **Mesenchymal condensation** | The moment the future skeleton is drawn — condensation NUMBER, POSITION and SIZE. The condensation is the physical antecedent of every later "anlage size" question | NO-ARCHITECTURE | chick, PMID 37281641 (precartilage condensation in skeletal pattern formation); Frzb-1 in condensation PMID 10610022 | No, but it is the origin of the ceiling | no |
| 42 | **SOX9** | Master chondrogenic TF; marks and is required for condensation; human haploinsufficiency = campomelic dysplasia | **YES-DIRECT** — SOX9 is continuously required in postnatal cartilage | mouse, PMID 7704017, 9119111 (expression during chondrogenesis), PMID 8702178 (campomelic dysplasia), PMID 12837698 (dimerisation required for chondrogenesis) | Yes | no |
| 43 | **BMP–SMAD4 in condensation, SOX9-independently** | Precartilaginous condensation requires BMP-Smad4 **independent of Sox9** — i.e. condensation and differentiation are separable steps | UNKNOWN | mouse, PMID 25641697 | No | **YES** |
| 44 | **N-cadherin (CDH2)** | Cell–cell adhesion that physically makes the condensation; TGF-β3 blocks condensation by shedding N-cadherin | UNKNOWN in plate | chick/mouse in vitro, PMID 12397616, 17573353 (Rac1→N-cadherin→condensation), 20401699 | No | **YES** |
| 45 | NCAM1 | Adhesion molecule of the condensation, alongside N-cadherin | UNKNOWN | in vitro; specific PMID UNVERIFIED this round | No | **YES** |
| 46 | **Hox genes set the WAVELENGTH of a Turing-type digit-patterning mechanism** | Digit NUMBER and spacing arise from a self-organising periodic system; distal Hox tunes its wavelength | NO-ARCHITECTURE | mouse, PMID 23239739; the network identified as **BMP–SOX9–WNT** modulated by morphogen gradients, PMID 25082703 | No — but it separates "how many elements" from "how big each is" | **YES** |
| 47 | **Joint interzone specification** | Where a continuous cartilage rod is INTERRUPTED — i.e. how many separate growth plates a ray will have and where | NO-ARCHITECTURE for the initial event | human, PMID 7525525 (hyaluronan/CD44 in human synovial cavitation) | No | no |
| 48 | **GDF5** | Interzone marker; joint formation; also the classic *brachydactyly* gene. Joint development involves a **continuous influx of Gdf5-positive cells** — i.e. the interzone is a recruiting population, not a fixed one | **YES-EXPR/DIRECT** — Gdf5 expression is regulated in joint remodelling and repair postnatally | mouse, PMID 27292641 (continuous influx of Gdf5+ cells); PMID 31932746 (Gdf5 regulation in remodelling/repair/OA); human BDC PMID 33872773, 25820810; BDA2 PMID 16014698; PMID 16127465 (activating vs deactivating mutations → symphalangism vs BDA2); PMID 16829522 (processing restricts GDF5 action to joint surfaces) | Yes | no |
| 49 | **GDF5 regulatory landscape** | Complex *cis*-regulation at GDF5 shapes JOINT MORPHOLOGY and OA risk — the same locus tunes shape and disease | YES (adult OA risk) | human/mouse, PMID 40356240 | Partly | **YES** |
| 50 | **WNT9A** | Required for joint integrity and regulates Ihh during chondrogenesis — a joint gene that feeds the plate's own Ihh node | YES-EXPR | mouse, PMID 16818445 | Possibly | **YES** |
| 51 | **ERG (transcription factor)** | Joint/articular cartilage formation during limb and spine skeletogenesis; **articular cartilage endurance requires Erg postnatally** | **YES-DIRECT** | mouse, PMID 17336282 (joint/articular formation); PMID 26097038 (articular cartilage endurance and resistance to OA require Erg) | Yes (articular compartment) | **YES** |
| 52 | **NOG (noggin)** | BMP antagonist; loss → **proximal symphalangism** and multiple-synostoses (joints fail to form) | YES-EXPR (BMP antagonism continues) | human, PMID 21538686 (review-as-index, NOG-related symphalangism spectrum); PMID 24735539 (heparin-binding-site mutation) | Partly | no |
| 53 | **FGF9** | A point mutation impedes joint interzone formation → multiple synostoses syndrome | UNKNOWN | mouse/human, PMID 28169396 | No | **YES** |
| 54 | **Interdigital programmed cell death (BMP-driven, ROS-mediated)** | Digit separation; removes the interdigital mesenchyme. HOXA13→ALDH1A2 permits it | NO-ARCHITECTURE | mouse/chick, PMID 26826495 (BMPs are direct triggers), PMID 25617432 (vascular patterning→ROS), PMID 23553814 (HOXA13→Aldh1a2), PMID 31204171 (environmental oxygen and the evolution of ICD) | No | no |
| **F. CARTILAGE ANLAGE → GROWTH PLATE → OSSIFICATION CENTRES** |
| 55 | **Transition from anlage to a zonally-organised growth plate** | The moment "a cartilage rod" becomes "a machine with a resting/proliferative/hypertrophic axis" | — | Covered piecewise; no single citable event-defining paper found this round — **GAP** | — | **YES** |
| 56 | **Primary ossification centre (POC)** | Diaphyseal ossification; establishes the metaphysis and the chondro-osseous junction | NO-ARCHITECTURE | canonical; searched `TITLE:("primary ossification" AND centre...)` → **0 hits**, so no clean citable POC-formation paper was reachable by title search this round | No | no |
| 57 | **Secondary ossification centre (SOC) — formation** | Splits one cartilage mass into GROWTH PLATE + ARTICULAR CARTILAGE; creates the epiphysis; is what bone age measures | NO-ARCHITECTURE (formation) but it defines the postnatal machine | mouse, PMID 30681752 (periarticular mesenchymal progenitors initiate and contribute to SOC); review-as-index PMID 33091640 | Formation no; consequences yes | no |
| 58 | ⭐ **SOC — mechanical function** | The SOC **REDUCES MECHANICAL STRESS WITHIN THE GROWTH PLATE**; it appears evolutionarily in amniotes (land-conquering) and its development correlates with mechanical load across whales/bats/jerboa | **YES-DIRECT (protective, ongoing)** | mouse + comparative + FE modelling, PMID 33063669 ("Secondary ossification center induces and protects growth plate structure") | ⭐ **YES** | **YES** |
| 59 | ⭐ **SOC and the ONSET of stem-cell self-renewal** | Before the SOC, clones are transient and the progenitor pool DEPLETES; coinciding with SOC formation, chondroprogenitors acquire SELF-RENEWAL and columns become monoclonal | **YES-DIRECT** | mouse, PMID 30814736 ("A radical switch in clonality reveals a stem cell niche in the epiphyseal growth plate") | ⭐⭐ **YES — this is the single most decision-relevant developmental fact in the domain** | no |
| 60 | **SOC vs direct epiphyseal mineralisation (proximal femoral head)** | Not all epiphyses use an osteoblast-rich SOC; the mouse proximal femur head mineralises chondrocytes directly. Thyroid hormone acts on both by DIFFERENT pathways | **YES-DIRECT (postnatal)** | mouse, PMID 35098920 | Yes | **YES** |
| 61 | **IGF-I receptor in Osterix+ cells** | IGF-I signalling in OSX+ cells regulates **SOC formation, growth-plate maturation and metaphyseal formation** during POSTNATAL bone development | **YES-DIRECT (postnatal)** | mouse, PMID 26011431 | Yes | **YES** |
| 62 | **Cartilage canals** | Vascular canals that precede and permit the SOC; they arise in relation to the perichondrium | YES (until SOC completes) | rat, PMID 1950417 (cartilage canal–perichondrium relationship, proximal tibial epiphysis); PMID 15103736 (VEGF and SOC microcirculation, rat humeral head) | Yes while epiphysis vascularises | **YES** |
| 63 | **RBP4 (retinol-binding protein 4) in developing long bones** | Locally expressed in chondrocytes; proposed local role in SOC formation | UNKNOWN | mouse, PMID 23224267 | Unlikely | **YES** |
| 64 | **Perichondrium / periosteum** | Circumferential (appositional) growth; a restraint compartment on longitudinal growth; source of SOC progenitors | **YES-DIRECT** | mouse PMID 30681752 (periarticular progenitors → SOC) | Yes | no |
| 65 | **Groove of Ranvier (perichondrial ossification groove)** | Latitudinal growth of the plate; source of the "bone bark"; a progenitor reservoir at the plate periphery | **YES-DIRECT (postnatal)** | rabbit, PMID 71299 (three cell groups incl. progenitors for bone-bark osteoblasts); PMID 8242950 (Col II mRNA in groove inner layer → cells originate in the growth plate); review-as-index PMID 9531398; rat postnatal Col VI/NG2 PMID 27498042 | Yes | **YES** |
| 66 | **Borderline chondrocytes** | Chondrocytes at the plate periphery, perpendicular to the columns, that behave as **transient mesenchymal precursor cells** feeding the metaphyseal marrow | **YES-DIRECT (postnatal lineage tracing)** | mouse, PMID 30888720; commentary PMID 31329317; earlier concept PMID 9707341 | Yes | **YES** |
| 67 | **Chondrocyte-to-osteoblast transdifferentiation** | Hypertrophic chondrocytes are not all destined to die — a fraction becomes osteoblasts and marrow stroma | **YES-DIRECT (postnatal)** | mouse, PMID 28874841 (epiphyseal bone formation via **thyroid-hormone-regulated** chondrocyte→osteoblast transdifferentiation, postnatal d7-10); review-as-index PMID 29928541; in-vitro assay PMID 34529238; KDM6A/Wnt PMID 42212366 | Yes | no |
| 68 | ⭐ **Resting zone as a stem-cell niche (PTHrP+)** | Skeletal stem cells FORM among PTHrP+ chondrocytes in the resting zone of the **POSTNATAL** growth plate | **YES-DIRECT** | mouse, PMID 30401834 | ⭐ **YES** | no |
| 69 | **Resting zone is maintained in a WNT-INHIBITORY environment** | The niche's defining molecular state | **YES-DIRECT** | mouse, PMID 34309509 | Yes | **YES** |
| 70 | **ApoE as a pan-marker of resting-zone chondrocytes** | A new marker for the whole resting zone (not a subset) | YES-EXPR | mouse, PMID 40025030 | Yes | **YES** |
| 71 | **FoxA2+ long-term stem cell population** | A distinct long-term stem population necessary for growth-plate cartilage REGENERATION after injury | **YES-DIRECT** | mouse, PMID 35523895 | Yes | **YES** |
| 72 | ⭐ **Differential growth-plate SENESCENCE sets skeletal proportions** | Small bones (metacarpals, phalanges) senesce EARLIER than large bones (femur, tibia); differential aging — not differential starting size — contributes to the 20-fold femur:phalanx length disparity | **YES-DIRECT — it is a postnatal programme** | mouse + rat, PMID 30036371 | ⭐⭐ **YES** | no |
| 73 | ⭐ **Hypertrophic chondrocyte volume enlargement has THREE phases; the THIRD sets elongation rate differences and is IGF-dependent** | The largest contribution to element length, and to length DIFFERENCES between elements | **YES-DIRECT** | mouse/mammal, PMID 23485973 (Cooper et al., quantitative phase microscopy) | ⭐⭐ **YES** | no |
| **G. FETAL GROWTH AND ITS DETERMINANTS** |
| 74 | **IGF2 (paternally expressed, imprinted 11p15)** | The dominant fetal growth factor; loss → Silver-Russell, gain → Beckwith-Wiedemann | **PROBABLY-NO as the *fetal* driver** — the postnatal switch to GH/IGF-1 is the canonical transition. But IGF2 is measurably expressed in postnatal cartilage | human, PMID 31803239, 28489339, 36268036 (de novo paternal IGF2 variants → SRS); mouse, PMID 28910276 (IGF2 stimulates fetal growth **sex- and organ-dependently**) | Indirectly | no |
| 75 | **H19/IGF2 ICR1 and its OCT4/SOX2 binding sites** | The imprinting switch. Point mutations in the OCT-binding motif alone cause BWS | NO for the plate | human, PMID 21863054, 24299031, 32012256, 24916376; complete biallelic insulation → fetal growth retardation + perinatal lethality (mouse) PMID 20838620 | No | no |
| 76 | **Placental-specific Igf2 (P0 transcript)** | Separates *placental supply* from *fetal demand*: deleting the placental-only transcript restricts fetal growth | NO | mouse, PMID 23099110 (placental-specific Igf2 KO × eNOS-deficient = FGR model); PMID 34963058 (Igf2-Igf2r axis matches placental microvasculature to fetal growth) | No | **YES** |
| 77 | **Prenatal correction of IGF2 rescues growth in BWS and SRS mouse models** | Proof the fetal growth setpoint is pharmacologically movable *in utero* | NO (window is prenatal) | mouse, PMID 33567274 | No — the window is closed | **YES** |
| 78 | **CDKN1C (p57Kip2), imprinted** | The BWS overgrowth gene on the maternal allele; a cell-cycle brake on fetal growth | UNKNOWN in plate | human, PMID 26077438; mouse, PMID 21729874 | No | no |
| 79 | **ZNF597 — a HUMAN-SPECIFIC imprinted gene** | Loss of imprinting → prenatal growth retardation and SRS-overlapping features. Human-specific imprinting means mouse cannot model it | UNKNOWN | human, PMID 32576657 | No | **YES** |
| 80 | **HMGA2–PLAG1–IGF2 axis** | An oncogenic module that is also the fetal-growth module; genetic disruption → fetal growth restriction. HMGA2 variants → idiopathic short stature; Hmga2-null mice show **allometric growth retardation** | **YES-EXPR (HMGA2 is a top human height GWAS locus)** | human/mouse, PMID 28796236 (disruption → FGR); human PMID 26536448 (HMGA2 variation ↔ ISS); mouse PMID 34878116; PLAG1 KO growth retardation PMID 15606491; PLAG1-related SRS PMID 37165482 | ⭐ Yes | no |
| 81 | **PLAG1 in cattle stature** | A single locus explaining a large fraction of bovine stature; the same gene appears in human SRS. Livestock genetics as an under-used external instrument | — | cattle, PMID 21516082, 22607022, 29215042 (a PLAG1 mutation contributed to stature RECOVERY in modern cattle) | Conceptually | **YES** |
| 82 | ⭐ **Maternal (uterine) constraint** | An epigenetic/physiological ceiling imposed by the mother that is INDEPENDENT of fetal genotype — the reason a foal from a pony dam is pony-sized at birth | NO (prenatal only), and it is the reason birth size under-predicts genetic potential | human, PMID 5893722 (Ounsted 1965), PMID 15691778, PMID 18276629 (commentary: maternal constraint is a pre-eminent regulator of fetal growth); rhesus, PMID 10655322 (intergenerational mother–daughter link); mouse/rat, PMID 1500836 (raising maternal IGF-I **removes** maternal constraint); sheep, PMID 9623486, 29157356 | No — but it explains why SGA≠small genotype | **YES** |
| 83 | **Maternal height — Mendelian randomisation** | MR analysis of maternal height on birth size AND gestational age at birth: separates genetic transmission from intrauterine effect | NO | human, PMID 26284790 | No | no |
| 84 | **Gestational age itself** | Independent contributor to adult size; the birth-length→adult-height relationship is STRONGEST at 39-41 weeks and considerably WEAKER in preterm births | NO | human, 348,706 Norwegian male births linked to conscription at 18 y, PMID 15703531 | No | **YES** |
| 85 | ⭐ **Birth length → adult height** | Birth LENGTH predicts adult HEIGHT far better than birth weight predicts adult weight (R ≈ 7-9% vs <0.1% in the Norwegian cohort). Length and weight at birth contribute **independently** | NO | human, PMID 15703531 | No — but it bounds how much of adult height is set before birth | no |
| 86 | ⭐ **Adult-height GWAS alleles act on birth length AND increasingly through childhood** | The 180-SNP adult-height allelic score raises birth length by ~0.026 cm/allele (P=1e-15) and its per-month effect GROWS with each consecutive growth period (0.015 SD at 3 mo-1 y → 0.028 SD at 3-10 y). By age 10 the top vs bottom decile differ by 4.7 cm | **YES — the same alleles keep acting postnatally** | human, ALSPAC n=7,768, PMID 21757498 | ⭐ **YES — direct evidence that "developmental" height genetics is not spent at birth** | no |
| 87 | **Preterm birth and adult height** | Preterm birth associated with lower adult height (women); very-preterm vs VLBW growth patterns differ | NO | human, PMID 27941067, 27998884, 28422945 | No | no |
| 88 | **SGA without catch-up → GH is licensed** | ~10% of SGA children fail to catch up; GH raises adult height in RCTs | **YES-DIRECT (therapeutic)** | human RCTs, PMID 12679443, 12915640; long-term PMID 31427155, 34906341 | Yes if he were SGA | no |
| 89 | ⭐ **Catch-up growth = DELAYED GROWTH-PLATE SENESCENCE, not a systemic servo** | The classical "sizostat" is largely wrong: growth-plate chondrocytes have a FINITE proliferative capacity that is spent by dividing, so growth suppression *conserves* it and the plate resumes from where it left off | **YES-DIRECT — this is a postnatal growth-plate programme** | rabbit, PMID 11641457; rat/mouse review-as-index PMID 21865751; hypothyroid model PMID 18174286; glucocorticoid PMID 7925098; nutrition PMID 18924581, 18201948; human test PMID 16356444; framework PMID 15723267 | ⭐⭐ **YES — and it is the same "divisions not time" clock that governs closure** | no |
| 90 | **Catch-up growth has a COST/limit — leptin raises aromatase in the plate** | Leptin stimulates aromatase locally in the growth plate, **limiting catch-up growth efficiency** — a local oestrogen brake on catch-up | **YES-DIRECT** | rat/mouse, PMID 29615477 | ⭐ Yes — a local oestrogen source distinct from gonadal | **YES** |
| 91 | **Catch-up growth after IUGR accelerates SENESCENCE in other organs** | Kidneys of low-birth-weight rats show accelerated senescence after catch-up — catch-up is not free | — | rat, PMID 19828676 | No (cost, not lever) | **YES** |
| 92 | **ICP (infancy–childhood–puberty) model** | Partitions postnatal growth into three additive, differently-regulated phases; the infancy phase is nutrition-driven and the childhood phase GH-driven | **YES (descriptive framework)** | human, PMID 2683573, 9560027 | Yes as a framework | no |
| 93 | **Postnatal growth canalisation** | The tendency to return to a percentile track. Mechanistically it appears to be #89 rather than a central set-point | YES | see #89 | Yes | no |
| **H. INFORMATIVE FAILURES — congenital limb defects that name the machinery** |
| 94 | **Thalidomide → CRBN → SALL4 degradation** | The mechanism of the most famous human limb teratogen: thalidomide converts cereblon into a degrader of SALL4 (and others) | NO (embryonic window) | human cells/zebrafish/rabbit, PMID 30067223, 30190590, 32071327; commentary PMID 30597765; species-specificity PMID 34249098 | No — **but it is the cleanest proof that a small molecule can delete a limb-patterning TF** | no |
| 95 | **SALL4** | Duane-radial ray / Okihiro syndrome; also restricts glycolytic metabolism in limb buds; Sall4-Gli3 in early progenitors | UNKNOWN | human, PMID 12395297, 16086360; mouse, PMID 25848055, 37301463 (Sall4 restricts glycolysis in limb buds) | No | **YES** |
| 96 | **ESCO2 → Roberts / SC phocomelia** | Sister-chromatid cohesion failure produces **phocomelia** — proximal limb reduction. A "housekeeping" gene producing a limb-length phenotype | NO | human, PMID 15821733, 16380922; also a thalidomide-susceptibility candidate PMID 31388035 | No | no |
| 97 | **RBM8A (exon-junction complex) → TAR syndrome** | Radial aplasia from a compound low-frequency regulatory SNP + a rare null; a **non-coding regulatory dose** disease | UNKNOWN; a 2026 preprint reports RBM8A is critical for embryonic bone development and Hedgehog signalling (PMID UNVERIFIED, preprint only) | human, PMID 22366785, 32227665 | No | **YES** |
| 98 | **TBX5 → Holt-Oram** | Heart-hand syndrome; radial ray defects | PROBABLY-NO | human, PMID 30552424 (78 patients with TBX5 variants) | No | no |
| 99 | **TBX3 → ulnar-mammary syndrome** | Posterior (ulnar) limb reduction | UNKNOWN | human; TBX3/TBX5 duplication overlap phenotype PMID 33930582 | No | no |
| 100 | **Brachydactyly type A1 — IHH** | The FIRST human trait shown to follow Mendelian inheritance; middle phalanges shortened. IHH mutations impair Hh transduction at multiple levels | **YES — IHH is the growth plate's own hedgehog ligand** | human, PMID 12384778, 12525541; mechanism PMID 21537345, 20024692, 30651074; a case with short stature responding to 4 y of GH PMID 38840672 | ⭐ **YES** | no |
| 101 | **Brachydactyly A2 — BMPR1B / GDF5 / BMP2 duplication** | A BMP-pathway dose disease; a **duplication DOWNSTREAM of BMP2** (a regulatory element) also causes it | UNKNOWN | human, PMID 16014698 (GDF5 receptor-binding site), PMID 24710560, 29129813 (BMP2 downstream duplication), PMID 33486847 (BMPR1B) | No | **YES** (the BMP2 regulatory duplication) |
| 102 | **Brachydactyly B — ROR2** | Distal phalanges/nails absent; ROR2 is the WNT5A receptor — links to #32's HOXD13/WNT5A polarity mechanism | UNKNOWN | human, PMID 23238279, 18365018 | No | no |
| 103 | **Brachydactyly C — GDF5** | Most variable brachydactyly; also Grebe chondrodysplasia when biallelic — **a dose series from digit shortening to severe limb shortening** | YES (see #48) | human, PMID 33872773 (frameshift → Grebe + BDC+ in one family), PMID 25820810 | Partly | no |
| 104 | **Brachydactyly D/E — HOXD13** | HOXD13 nonsense → isolated BDE; other HOXD13 alleles → synpolydactyly (see #106) | YES (see #32) | human, PMID 22233338, 32789964 | Partly | no |
| 105 | ⭐ **Brachydactyly E — PTHLH** | Deletions and point mutations of **PTHLH** (PTHrP) cause BDE **with short stature**; a PTHLH DUPLICATION causes osteochondroplasia with combined BDE/A1, disturbed bone maturation and **rhizomelia** | **YES-DIRECT — PTHrP is the resting-zone stem-cell marker and half of the Ihh-PTHrP loop** | human, PMID 20170896 (deletion + point mutations), PMID 28211986, PMID 25801215; duplication PMID 26733284 | ⭐⭐ **YES — a human dose-response on PTHrP in both directions** | **YES** (the duplication) |
| 106 | **Synpolydactyly — HOXD13 polyalanine expansion** | A repeat-length dose disease; homozygotes get **metacarpal-to-carpal transformation** (an element loses its long-bone identity entirely) | YES (see #32) | human, PMID 26581570 (homozygous missense → metacarpal→carpal transformation), PMID 37427568 (38 new + 49 published families), PMID 22373878 (G11A interferes with Gli3R) | Partly | no |
| 107 | **Symphalangism — NOG, GDF5, FGF9** | Joints fail to form; the phalanges fuse. Same genes as brachydactyly, opposite functional direction (activating vs inactivating) | YES for the pathways | human, PMID 16127465 (activating→symphalangism, deactivating→BDA2 in ONE gene), PMID 21538686, PMID 28169396 (FGF9), PMID 29371961 (GDF5 L373R knock-in mouse) | Partly | no |
| 108 | **Split-hand/foot malformation — TP63, DLX5/DLX6, WNT10B, 10q24 duplications, SOX3 SV** | Failure of the central AER; a large fraction of cases are **non-coding structural variants**, not coding mutations | UNKNOWN | human, PMID 37776184 (DLX5, HOXD13, BTRC microduplication), PMID 38058757 (WNT10B), PMID 37216008 (complex SV near SOX3) | No | no |
| 109 | **X-irradiation phocomelia re-evaluated** | The classic evidence for the progress-zone model was re-examined and the interpretation changed — a caution about inferring mechanism from a truncation | NO | chick/mouse, PMID 19553938 | No | **YES** |
| **I. THE ANLAGE→PLATE TRANSITION, MECHANICS, AND GENES THAT DO BOTH JOBS** |
| 110 | ⭐ **Column formation is LARGELY ABSENT in the EMBRYONIC growth plate** | Confetti multicolour clonal analysis: most embryonic chondrocyte pairs do NOT show the stacked pattern of column formation — embryonic clones are elongated but form CLUSTERS oriented PERPENDICULAR to the growth direction. Postnatal plates show complex columns plus disorganised clusters at the outer edge | **This is the transition itself.** The authors conclude the mechanisms of PRE- and POSTNATAL bone growth DIVERGE | mouse, PMID 39269144 (eLife 2024) | ⭐⭐ **YES — it is the direct evidence that embryonic and postnatal elongation are different machines, which is the strongest argument that embryonic patterning results should NOT be assumed to transfer** | **YES** |
| 111 | **Fetal movement is REQUIRED for joint cavitation and normal bone shape** | Immobilisation in ovo differentially regulates GDF-5 and FGF-2/4; restrained fetal movement disrupts hip joint development | NO (prenatal), but the mechanical principle continues | chick, PMID 16425226; rat, PMID 12196711; mouse, PMID 41388826 (maternal exercise rescues fetal-akinesia-impaired joint and bone development) | No | **YES** |
| 112 | **FGFR3** | Patterning-adjacent AND growth: expressed in the limb bud and the postnatal plate; achondroplasia is a postnatal-progressive disorder | **YES-DIRECT** (the whole vosoritide/infigratinib field) | human/mouse — canonical; achondroplasia resting-zone turnover via CREB PMID 41748604 | ⭐ Yes | no |
| 113 | **IHH** | Does BOTH jobs: brachydactyly A1 (a PATTERNING/proportion phenotype) and the Ihh-PTHrP loop (a GROWTH-RATE mechanism) | **YES-DIRECT** | human PMID 12384778; mouse — canonical | ⭐ Yes | no |
| 114 | **PTHLH (PTHrP)** | Does BOTH: brachydactyly E with short stature (human dose-response, both directions) AND the resting-zone stem-cell marker | **YES-DIRECT** | human PMID 20170896, 26733284; mouse PMID 30401834 | ⭐ Yes | no |
| 115 | **HOXD13** | Does BOTH: digit identity/number (synpolydactyly) AND growth-plate CELL POLARITY with WNT5A | **YES** | mouse PMID 24161848; human PMID 37427568 | ⭐ Yes | **YES** |
| 116 | **SHOX** | Does BOTH: a patterning-type mesomelic phenotype (Madelung, LWD) AND a quantitative stature effect responsive to GH | **YES-DIRECT** | human PMID 27194967, 38572386 | ⭐ Yes | no |
| 117 | **GDF5** | Does BOTH: joint number/position AND digit element length (brachydactyly C → Grebe dose series) | YES | human PMID 33872773 | Yes | no |
| 118 | **Chondroinduction vs proliferation in nodule growth** | In limb-bud culture, cartilage-nodule growth is BOTH recruitment of new cells into the nodule AND proliferation within it — so "condensation size" is not fixed at t=0 | NO-ARCHITECTURE | mouse, PMID 23447083 | No | **YES** |
| 119 | **Resting-zone chondrocytes do NOT shorten telomeres with age** | The growth-plate clock is not a telomere clock | **YES-DIRECT (a negative)** | mouse, PMID 15795509 | Yes (it constrains what the clock can be) | **YES** |
| 120 | **Depletion of resting-zone chondrocytes during growth-plate senescence** | The physical substrate of the finite-capacity model | **YES-DIRECT** | rabbit, PMID 16614378 | ⭐ Yes | no |

---

## PROSE 1 — DEVELOPMENTAL GENES THAT ARE STILL EXPRESSED **AND STILL FUNCTIONAL** IN A POSTNATAL GROWTH PLATE

The brief's framing is the right one and most of the limb-patterning literature fails it. Of the ~120 rows
above, the great majority are **NO-ARCHITECTURE**: TBX5, TBX4, FGF10, the AER, the ZPA, MEIS, WNT7A, LMX1B,
EN1 and the interdigital death programme all act, finish, and leave. The honest list of developmental genes
with *demonstrated postnatal work in the plate or its immediate niche* is short. It is:

**1. HOXA11/HOXD11 — the strongest entry, and it is a LINEAGE result, not an expression result.**
`Hoxa11-CreERT2` lineage tracing shows Hox11-marked cells give rise to osteoblasts, chondrocytes and
adipocytes **throughout the life of the animal** and persist as MSCs; they sit **upstream** of the
LepR-Cre and Osx-CreER progenitor populations that the postnatal bone field normally treats as the root
(mouse, PMID 31320650). Regionally restricted Hox function is retained in **adult** marrow MSCs
(PMID 27939685). Separately, Hoxa11/Hoxd11 control an early step of chondrocyte differentiation —
specifically the transition from round to columnar cells — upstream of Runx2 and Shox2 (mouse, PMID
22916278). So the classic "positional" TF is not a positional relic; it is a marker and regulator of the
cells that make bone for life. **This is the single most important row in the domain and it is obscure in
the growth literature.**

**2. HOXD13 — postnatal-relevant cell POLARITY.** In the *spdh* (synpolydactyly) mouse the metacarpal
growth plate loses the linear orientation of its cells and shows random polarity, acting with WNT5A;
the metacarpals are transformed toward carpal-like bones lacking a perichondrium (mouse, PMID 24161848).
That is a growth-plate architecture phenotype produced by a digit-identity gene.

**3. SHOX / SHOX2.** SHOX has **no mouse orthologue**, which is why mouse-derived limb patterning
systematically misses it and why it is disproportionately important for human stature. SHOX
haploinsufficiency is a recognised, GH-responsive cause of short stature with randomised-trial support
(PMID 38572386), and duplication has been reported with tall stature (PMID 31093387). Its paralogue
SHOX2 is required for proximal chondrocyte proliferation and maturation and transcriptionally targets
**NPPB and ACAN** (mouse, PMID 17481601, 23038774, 24421874) — two nodes this atlas already works.

**4. IHH and PTHLH — the two genes that are simultaneously patterning genes and growth genes.** IHH gives
brachydactyly type A1 in humans (the first Mendelian trait ever described) and is the growth plate's own
hedgehog ligand. PTHLH gives brachydactyly E **with short stature** on loss (PMID 20170896, 28211986) and
osteochondroplasia with rhizomelia and disturbed bone maturation on **duplication** (PMID 26733284) — a
human dose-response in BOTH directions on the gene that marks resting-zone skeletal stem cells (PMID
30401834). No other node in this domain has that.

**5. SOX9, GDF5, ERG, WNT9A.** SOX9 is required continuously. GDF5 is not a one-off interzone marker —
joints are built by a *continuous influx* of Gdf5+ cells (PMID 27292641) and Gdf5 expression is
re-regulated in postnatal remodelling and repair (PMID 31932746). ERG is required for **postnatal**
articular cartilage endurance (PMID 26097038). WNT9A regulates Ihh during chondrogenesis (PMID 16818445).

**6. The niche genes that only exist postnatally.** PTHrP+ resting-zone skeletal stem cells **form
postnatally** (PMID 30401834); the resting zone is held in a **Wnt-inhibitory** state (PMID 34309509);
ApoE marks the whole resting zone (PMID 40025030); a FoxA2+ long-term stem population drives regeneration
after injury (PMID 35523895); borderline chondrocytes act as transient mesenchymal precursors (PMID
30888720); chondrocyte→osteoblast transdifferentiation is thyroid-hormone-regulated and postnatal
(PMID 28874841). None of these is a "developmental origins" gene in the classical sense — they are the
machinery that *replaces* the embryonic programme.

**And the decisive negative, which should govern how the rest of this domain is used.** Confetti clonal
analysis in mouse shows that **columns barely form in the embryonic growth plate**: most embryonic
chondrocyte pairs do not stack, embryonic clones form *clusters oriented perpendicular to the growth
direction*, and only postnatal plates show true complex columns (mouse, PMID 39269144, eLife 2024). The
authors' own conclusion is that pre- and postnatal bone growth use **divergent mechanisms**. Combined with
the clonality switch at the SOC (PMID 30814736), the correct default assumption is: **an embryonic limb
result does not transfer to an open postnatal plate unless someone has specifically shown that it does.**
Under this atlas's own CORR-299 rule the germline-from-conception objection is not automatic — but the
burden of proof sits on the transfer, and for most limb-patterning genes nobody has discharged it.

---

## PROSE 2 — WHAT SETS THE SIZE OF THE INITIAL CARTILAGE ANLAGE, AND WHETHER THAT CONSTRAINS ADULT LENGTH

**The short answer, and it is more favourable than expected: the initial anlage does NOT appear to be the
binding constraint on adult length. The postnatal programme dominates.**

*What sets the anlage.* Four inputs, in order of how well they are evidenced:
1. **Condensation number, position and spacing** are set by a self-organising periodic (Turing-type)
   system whose **wavelength is tuned by distal Hox genes** and whose molecular identity is a
   **BMP–SOX9–WNT** network modulated by morphogen gradients (mouse, PMID 23239739, 25082703). This sets
   *how many* elements and *where*, and it is separable from *how big*.
2. **Duration and geometry of AER-driven outgrowth**, i.e. how many progenitors are produced and allocated
   before the AER regresses (chick, PMID 8221896; mouse, PMID 15328019). Whether allocation is by residence
   time (progress zone) or by early specification is genuinely unsettled — PMID 12152081 challenged the
   progress zone and PMID 19553938 re-evaluated the X-irradiation phocomelia evidence that supported it.
3. **Condensation is not a fixed cell count at t=0.** In limb-bud culture, nodule growth is *both*
   recruitment of surrounding cells into the nodule (chondroinduction) *and* proliferation within it
   (mouse, PMID 23447083). So "anlage size" is itself dynamic.
4. **Regional, enhancer-level scaling.** The cleanest demonstration that a *cis*-element can set element
   size rather than element identity is the pair of **Tbx4 hindlimb enhancers**, described explicitly as
   giving "region-specific control of bone size" (PMID 18579682). PITX1 is described as shaping hindlimb
   morphology via **targeted growth control** (PMID 22071103). These are proofs of principle that skeletal
   size is enhancer-tunable.

*Does it constrain adult length?* Two independent lines say the constraint is weak and the postnatal
programme is where the length actually comes from.

- **Cooper et al. (mouse/mammal, PMID 23485973):** the largest single contribution to element length, and
  to the *differences in length between elements*, is the increase in hypertrophic chondrocyte volume.
  Quantitative phase microscopy resolves three phases of enlargement, and it is the **duration of the
  third phase** (proportional dry-mass increase at low density, locally IGF-dependent) that varies most
  between rapidly and slowly elongating growth plates. Element proportions are therefore set by a
  *postnatal, local, IGF-modulated* parameter — not by starting size.
- **Lui et al. (mouse/rat, PMID 30036371):** the ~20-fold human femur:phalanx length difference is
  attributed to **differential growth-plate senescence** — small bones exhaust their proliferative,
  hypertrophic and cellular reserves *earlier* than large bones. Again a postnatal programme.

Put together with the finite-proliferative-capacity model (PMID 15723267, 11641457, 16614378) and the
observation that resting-zone chondrocytes do **not** shorten telomeres with age (PMID 15795509), the
picture is: **adult length is set by how many divisions the postnatal resting-zone pool has left and how
much each hypertrophic cell swells — not by how big the cartilage rod was at birth.**

*The human epidemiology agrees and quantifies it.* In 348,706 Norwegian males linked from birth records to
conscription at 18, birth **length** explains only about 7–9% of the variance in adult height (and birth
weight explains <0.1% of adult weight); length and weight at birth contribute independently; and the
association is strongest at 39–41 weeks and much weaker in preterm births (PMID 15703531). Meanwhile the
adult-height allelic score raises birth length by only ~0.026 cm per allele but its per-month effect
**grows with every subsequent growth period**, reaching 0.028 SD/month at 3–10 years, with a 4.7 cm gap
between the top and bottom deciles by age 10 (ALSPAC n=7,768, PMID 21757498). **The same alleles that
"should" be developmental do most of their work after birth.**

*Two important caveats that run the other way.*
- **A growth plate is not guaranteed.** The human pisiform lost its growth plate and its second
  ossification centre, and Hox is implicated in whether an element has a plate at all (PMID 25279687,
  27507801). Homozygous HOXD13 mutation transforms metacarpals into carpal-like elements (PMID 26581570).
  So patterning can remove the *machine*, which is a hard ceiling that no postnatal lever can lift.
- **Maternal/uterine constraint** means birth size systematically under-reports genotype (human, PMID
  5893722, 15691778, 18276629; rhesus, PMID 10655322; and the direct demonstration that raising maternal
  IGF-I *removes* maternal constraint in rodents, PMID 1500836). A small newborn is therefore weak
  evidence of a small ceiling — which is exactly why SGA children who do not catch up respond to GH
  (PMID 12679443, 12915640).

---

## PROSE 3 — THE SECONDARY OSSIFICATION CENTRE AS A CONTROL POINT

The SOC is the most under-rated structure in this domain and it is a control point in **four** distinct
senses.

**(1) It creates the postnatal growth plate as a separate organ.** Growth plate and articular cartilage
begin as one anatomical entity and are separated into two structures by the SOC (mouse + comparative,
PMID 33063669). Before that separation there is no "growth plate" in the sense this atlas uses the word.

**(2) It switches the plate from a DEPLETING pool to a SELF-RENEWING one — and this is the load-bearing
fact.** Clonal analysis shows a "radical switch in clonality": fetal/neonatal chondroprogenitors are
transient and the pool depletes; **coinciding with SOC formation**, progenitors acquire self-renewal, and
columns become monoclonal and persist for months (mouse, PMID 30814736). Independently, the resting zone
of the **postnatal** plate is where PTHrP+ skeletal stem cells form (PMID 30401834). Two labs, two
methods, one conclusion: **the stem-cell niche is a POST-SOC phenomenon.** Everything this atlas cares
about — pool size, pool preservation, whether a lever adds to N — is downstream of an event that happens
after birth. That is a strong argument that pool-directed thinking is aimed at the right window, and it
also explains why pre-SOC and post-SOC perturbations of the same pathway can have opposite signs.

**(3) It is mechanical.** The SOC appears evolutionarily in **amniotes** — animals that conquered land —
and across mammals with specialised extremities (whales, bats, jerboa) its development correlates with the
extent of mechanical load. Mathematical modelling shows the SOC **reduces mechanical stress within the
growth plate**, and functional experiments in the same paper support induction and protection of plate
structure (PMID 33063669; review-as-index PMID 33091640). So the SOC is a stress shield, not merely an
ossification event — which makes it directly relevant to any mechanical-loading argument, and it predicts
that plates with an immature or abnormal SOC are more vulnerable to load.

**(4) It is what bone age actually measures.** Bone-age scoring is in large part the assessment of SOC
appearance, size and fusion (PMID 33091640 states this framing explicitly; chronology in human pelvis and
proximal femur by CT, PMID 27442214). The instrument the atlas uses to time the window is an instrument
pointed at this structure.

**What acts on it, postnatally.** Three hormonal/local handles are documented:
- **IGF-I signalling in Osterix+ cells** regulates SOC formation, growth-plate maturation and metaphyseal
  formation during postnatal bone development (mouse, PMID 26011431).
- **Thyroid hormone** drives epiphyseal bone formation by chondrocyte→osteoblast transdifferentiation
  postnatally (mouse, PMID 28874841) — and, importantly, TH acts through **different pathways** at the
  distal femur SOC versus the directly-mineralising proximal femoral head (mouse, PMID 35098920). The same
  hormone, two epiphyses, two mechanisms.
- **Periarticular mesenchymal progenitors** initiate and contribute to the SOC (mouse, PMID 30681752), and
  **cartilage canals** carrying VEGF-associated microvasculature precede it (rat, PMID 1950417, 15103736).

**The honest limits.** No intervention has ever been aimed at the SOC to change adult height in any
species. Whether accelerating or delaying SOC maturation changes final length is, as far as this external
search can tell, **unmeasured** — and at bone age 16 the SOCs are long formed, so the only live reading of
this section is the *consequence*: the self-renewing niche exists, it is post-SOC, and it is the compartment
worth protecting.

---

## WHAT I COULD NOT VERIFY

Recorded honestly, as instructed.

1. **FGF10-null limbless mouse** — universally cited, but a `TITLE:(Fgf10 AND limb...)` query returned
   **0 hits** and I did not locate the primary PMID. Marked UNVERIFIED in row 9.
2. **Classic AER-removal / Saunders truncation experiments** — no PMID (pre-indexing era). Row 11.
3. **WNT3 tetra-amelia** — a title-level hit exists (PMID 14872406, "Homozygous WNT3 mutation causes
   tetra-amelia in a large consanguineous family") but I did not read the abstract; the row is written
   conservatively.
4. **SP8/SP6 in the AER** and **NCAM1 in condensation** — real, textbook, but I could not retrieve a
   specific primary PMID within this round. Rows 13 and 45.
5. **HOX9/HOX10 and the stylopod** — no primary PMID retrieved. Row 29.
6. **Primary ossification centre formation** — `TITLE:("primary ossification" AND (center OR centre) AND
   (formation OR Runx2 OR vascular))` returned **0 hits**. There is no clean title-searchable
   POC-formation primary in Europe PMC by that phrasing; row 56 says so rather than inventing one.
7. **The anlage→growth-plate transition as a named event** — no single paper defines it. The best proxy
   found is PMID 39269144 (columns barely form embryonically). Recorded as a GAP in row 55.
8. **Heterospecific limb-bud transplantation showing donor-intrinsic size control** (the classic
   amphibian and chick-quail grafts) — I could not retrieve a citable PMID; targeted queries returned only
   PMID 7227645 (supernumerary structures from graft position/orientation, chick) and PMID 3704002
   (canine heterotopic growth-plate transplant), neither of which tests intrinsic size. **This is a real
   gap and it is the experiment that would most directly answer PROSE 2.**
9. **ZRS affinity-optimising variants** — I saw only a PMC record (2022) with no PMID in the search
   result. Row 19 says PMID UNVERIFIED.
10. **RBM8A and Hedgehog signalling in embryonic bone** — 2026 preprint only, no PMID. Row 97.
11. **Numbers I deliberately did not state**: I have not asserted any effect size for SHOX prevalence in
    ISS, any catch-up-growth percentage, any SOC appearance age, or any heritability partition of birth
    weight, because I did not read those abstracts in full.
12. **Not attempted**: clinicaltrials.gov and regulatory documents were not queried for this domain —
    there is no drug aimed at limb patterning, so the yield would have been zero, but I am recording that
    I did not look.
13. **Rows marked UNKNOWN are genuine gaps, not nulls.** For most limb-patterning genes (MEIS1/2, WNT7A,
    LMX1B, EN1, ETV4/5, HAND2, SALL4, GLI3) nobody has asked whether they are expressed or functional in a
    postnatal growth plate. Under this atlas's own rule a missing endpoint is a gap. The cheapest way to
    close most of them at once is a single zone-resolved expression query against a postnatal human growth
    plate dataset — which is a lookup, not a round.
