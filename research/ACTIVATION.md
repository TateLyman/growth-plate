# Activating the boundary: the least-complex route — revision 2

How to switch on a longitudinal growth interface in an adult, in situ. Third document in the series, after [THEORY.md](THEORY.md) (mechanics) and [COMPOUNDS.md](COMPOUNDS.md) (pharmacology). Built from 109 full texts read in full, notes in [notes/](notes/).

**Revision 2** follows a round of reading aimed specifically at strengthening, confirming and raising the ceiling of revision 1. It changes the emphasis, the molecular chain, the anatomical target and the arithmetic. §1 is the changelog; revision 1's core claim — that the apparatus exists and is held shut rather than absent — survives and is now much better supported.

---

## 0. The answer in one paragraph

**Longitudinal growth rate in a postnatal mammal is set almost entirely by how large hypertrophic chondrocytes get, not by how many there are.** Four growth plates in one rat, at one moment, elongating at rates differing 3–7×, produce **the same ~10,500 new chondrocytes per day each**; what differs is hypertrophic cell volume, which ranges **4,000 → 20,000 µm³** and correlates with elongation rate at **r = 0.70**, while cell production correlates at r = 0.35, non-significantly ([18404738](notes/18404738.md)). Across an eight-fold range of growth rate, **cellular enlargement contributes 59% of axial growth, matrix synthesis 32% and proliferation 9%**, and accelerated growth is "almost exclusively" enlargement ([32852849](notes/32852849.md)). That enlargement is an **osmotic pump with named parts**: IGF-1 licenses its final phase, **NKCC1 (SLC12A2)** traffics to the plasma membrane immediately before the cell swells, **AE3 (SLC4A3)** rises 14-fold alongside it, and blocking NKCC1 with bumetanide removes **35% of longitudinal growth while leaving hypertrophic cell number unchanged to three significant figures** ([20200963](notes/20200963.md), [23485973](notes/23485973.md)). **Adult articular deep-zone chondrocytes are stuck at roughly 1,750 µm³ — they have finished true hypertrophy and never begun swelling, leaving phases 2 and 3 entirely unused** (§4). One pathway — **ERK** — simultaneously sets progenitor proliferation in the groove of Ranvier, Ihh/PTHrP output, cell size, hypertrophic-zone depth and the gate to terminal conversion, and it has existing drugs on both sides ([25003010](notes/25003010.md), [24875294](notes/24875294.md)). And the thing being overcome is not exhaustion but **active restraint**: the perichondrium is a maintained anti-chondrogenic border made of heparan sulfate, and the fastest-elongating mammalian bone known gets that way partly by **releasing brakes** — 10.6× more retinoic-acid-sequestering Crabp1, 9.3× less of the RA-induced inhibitor Gdf10 ([23821404](notes/23821404.md), [34793695](notes/34793695.md)). **Two sections were added after the above was written and both change its scope.** §17 finds that the programme which builds skeleton outside a physis is the circumferential cartilaginous callus, and that it involutes unless apposed to a partner tissue. **§18 finds the layer above all of it: positional identity — what sets how much skeleton the body thinks it should have. It is a heparan-sulfate code in connective-tissue matrix, it is present in mammals, it closes around postnatal day 9 in mouse, retinoic acid is the only known compound that rewrites it heritably, and a 7-day exposure to the CYP26 inhibitor talarozole — a drug that has been through human Phase II — made axolotl limbs build an entire extra proximal segment, dose-dependently. Its effector is *Shox*, whose loss leaves proximal chondrocytes arrested as reserve cartilage for life and whose haploinsufficiency is a cause of human short stature.** On the evidence here the post-closure problem has two locks, not one: no responsive template, and no positional instruction.

**And the gate on that actuator is the thing I had missed** (§3b): hypertrophic cell size is set by **local free IGF availability**, which is set by **IGFBP abundance** — *Igfbp3* and *Igfbp5* are **direct H3K27me3 targets** whose derepression shrinks hypertrophic cells, and whose exogenous addition shrinks them just as much, while high IGF-1 overrides the whole thing ([27897169](notes/27897169.md)) — and by **IGFBP proteolysis**, carried out by **PAPP-A and PAPP-A2 and inhibited by stanniocalcin-2**, where **partial loss of *STC2* adds +1.9 cm to adult human height, the largest effect of any of 83 rare coding variants on stature**, with the effect strengthening postnatally and the overexpression phenotype being specifically **axial** ([29280739](notes/29280739.md)).

**So the revised answer: do not try to make more cells, and do not try to build a plate. Release the brake on an existing border, let the resident progenitors of the perichondrial rim form the interface where the gradient already points along the bone's axis, drive the volume actuator through phases 2 and 3 by opening the IGF gate locally, and cycle ERK to convert the bottom of the stack to bone.** The best site for it is probably the **vertebral endplate**, not the knee (§13.2–13.3c), and the honest price of the IGF gate is that it is a validated tumour-promoting axis whose loss makes mice long-lived (§3b).

**But every gene named above works through an open physis. §17 is the post-closure answer, and it is a different kind of thing: not a growth gene but a regeneration programme.** Every mammal, humans included, launches an endochondral elongation programme from the periosteum within hours of a bone injury — a **circumferential cartilaginous callus** — and then shuts it down, because the callus **involutes unless it is apposed to a partner tissue**. Deer escape that and regrow a metre of endochondral bone at **2 cm/day, annually, as adults**, from 3.3 million periosteal stem cells, released by **testosterone falling below ~0.5 ng/ml**. The partner is **substitutable by BMP2 applied before the callus involutes, which restored the entire length of a bone in a mammal** — and rhBMP-2 is licensed. What humans lack is not the cells or the capacity but a partner, and the block appears to be a **physical barrier of interposed connective tissue and muscle** ([37490254](notes/37490254.md)).

---

## 1. What changed in revision 2

| Revision 1 said | Revision 2 says | Why |
|---|---|---|
| G = n × h_max, both terms suppressed, both need fixing | **h_max is the term.** *n* is near-invariant across plates differing 3–7× in rate | [18404738](notes/18404738.md): ~10,500 cells/day in all four plates; volume r = 0.70, production r = 0.35 ns. [32852849](notes/32852849.md): 59/32/9 partition |
| The proliferation wall of [COMPOUNDS.md](COMPOUNDS.md) §2 is the central obstacle | **It is real but strategically mis-weighted.** Proliferation is ~9% of axial growth; those compounds were judged against the wrong variable | same, plus [20200963](notes/20200963.md) |
| *h_max* is "halved" in adult articular cartilage | **It is at ~12.5% of terminal volume — the phase-1/phase-2 boundary. Phases 2 and 3 are unused** | §4, from [28438606](notes/28438606.md) × [23485973](notes/23485973.md) |
| The actuator is "the volume set-point", mechanism unstated | **Named end to end: IGF-1 → NKCC1/AE3 membrane trafficking and phosphorylation → osmolyte import → water → directed expansion in confining matrix channels** | [20200963](notes/20200963.md), [23485973](notes/23485973.md) |
| Five stages, each with its own lever | **One dial (ERK) moves four of them; cycling it *is* the ratchet** | [25003010](notes/25003010.md), [24875294](notes/24875294.md) |
| Target the articular interior (tidemark, deep zone) | **Target the perichondrial rim / groove of Ranvier.** It is perfused, progenitor-rich, proliferative, migratory onto the articular surface, and the specificity controls say the interior does nothing | [25003010](notes/25003010.md), [25164565](notes/25164565.md), [28438606](notes/28438606.md) |
| Polarity is "already correct" at an articular surface — asserted | **Polarity is set by the direction and territory of the Ihh/BMP gradient.** Exostoses grow at 90° because the leak is lateral; at an axial border the gradient is axial | [23821404](notes/23821404.md), [25003010](notes/25003010.md), [24875294](notes/24875294.md) |
| The apparatus is "frozen" | **It is actively braked.** Two independent literatures: an HS anti-chondrogenic border, and de-repression of latent growth potential | [23821404](notes/23821404.md), [34793695](notes/34793695.md) |
| No human evidence of adult longitudinal growth from such an interface | **Two human proofs**: exostoses keep growing after plates close (no new ones form); and aromatase/ERα-deficient men grew into their fourth decade with radiographically open plates at 190–204 cm | [23821404](notes/23821404.md), [24485503](notes/24485503.md) |
| Arithmetic over 4 articular surfaces per leg | **Add the axial skeleton: ~48 vertebral endplates, the last structures to close, contributing 100 mm of T5–L5 length in adolescence** | [34362001](notes/34362001.md), 16778695 |
| The actuator's *regulated step* was "NKCC1 trafficking and phosphorylation", mechanism of licensing unstated | **§3b: the gate is local free IGF availability, set by IGFBP abundance (direct H3K27me3/PRC2 targets) and IGFBP proteolysis (PAPP-A/PAPP-A2, inhibited by STC1/STC2). Partial loss of STC2 = +1.9 cm of adult human height, the largest rare-coding-variant effect known** | [27897169](notes/27897169.md), [29280739](notes/29280739.md), [24572990](notes/24572990.md) |
| T3 and dasatinib were marginal leads | **Both were already raising free local IGF in adult human tissue** — T3 raises *PAPPA* 2.7–3.4× in 60–76-year-old cartilage; dasatinib raises *IGF1* and lowers *IGFBP1/3*. Neither paper measured cell volume | [38664820](notes/38664820.md), [39402753](notes/39402753.md) |
| — | **The epigenetic lever points the opposite way from the obvious one.** PRC2 loss costs length in chondrocytes and adds appositional width in osteoblasts; the Weaver mouse has normal bone length. So EZH2 inhibitors are wrong-signed, and **KDM6 inhibition is the untested correctly-signed lever** | [37425751](notes/37425751.md), [27897169](notes/27897169.md) |
| Every lever was a growth gene or pathway | **§17: all of them work only through an open physis. The post-closure programme is epimorphic regeneration — the periosteal circumferential cartilaginous callus, which humans already form and then involute for want of a partner tissue. Antler: 2 cm/day in adults; BMP2 substitutes for the partner and restored a bone's entire length; androgen withdrawal below ~0.5 ng/ml releases it** | [37490254](notes/37490254.md) |
| The "boundary" was this document's organising device | **It is the general rule for mammalian skeletal growth outside a physis** — six systems, one architecture, single domains always involute | §17.1 |
| — | **New dead end: looking for an animal whose endochondral plates never stop.** Zebrafish grow indeterminately for life and still arrest their endochondral zones; intramembranous is what stays active | [32852849](notes/32852849.md) |

---

## 2. The term that matters

Three independent lines, one conclusion.

**Within one animal, at one moment.** Four rat growth plates — proximal and distal radial, proximal and distal tibial — elongate at rates differing by **3–7×**. Hypertrophic cell volume ranges from **~4,000 µm³** (slow proximal radius, days 24–28) to **~20,000 µm³** (fast proximal tibia, days 7–13), correlating with elongation rate at **r = 0.70 (0.01 > p > 0.001)**. **Cells produced per day: ~10,500 ± 1,500 in all four plates**, with cells lost per day "relatively constant" and production correlating with velocity at only **r = 0.35, not significant** ([18404738](notes/18404738.md)).

**Partitioned.** In rat proximal tibia: **cellular enlargement 59%, matrix synthesis 32%, proliferation 9%** of axial growth, and "periodic accelerated growth almost exclusively involves cellular enlargement." Every natural case of one bone outgrowing its homologue — rat tibia vs radius, **bat wing metacarpals**, **jerboa metatarsals** — runs on "dramatic cellular enlargement in the HZ" ([32852849](notes/32852849.md)).

**Pharmacologically dissociated.** Bumetanide in rat metatarsal rudiment culture: longitudinal growth down **~35%**; late hypertrophic zone **204 → 151 µm (p = .015)**, HZ fraction **33.8% → 22.7% (p = .008)**; total plate height unchanged; and **hypertrophic cell number 193 ± 11.3 vs 192 ± 13.6 (p = .937)** with identical cell densities ([20200963](notes/20200963.md)).

**The consequence for the compound literature.** [COMPOUNDS.md](COMPOUNDS.md) §2 catalogued six agents that raise matrix while leaving chondrocyte number flat or lower — T3, dasatinib, OSK, kartogenin, Yoda1, sprifermin — and treated that as the fatal obstacle. It is not fatal; it is beside the point. **Postnatally, cell number is not what separates a plate growing at 400 µm/day from one growing at 50 µm/day.** The relevant question to have asked of each of those agents was what it did to hypertrophic cell volume, and none of those papers measured it.

---

## 3. The actuator, named end to end

| Step | Component | Evidence |
|---|---|---|
| Volume target | PZ ~1,000 µm³ → HZ ~15,000 µm³ (15×); terminal mouse tibia ~14,000 fl; jerboa metatarsal **~23,000 fl (40× initial)**, cell height +58% vs mouse | [20200963](notes/20200963.md), [23485973](notes/23485973.md) |
| Phase 1 | ~600 → 2,000 fl, **true hypertrophy** at constant dry density 0.183 pg/fl | [23485973](notes/23485973.md) |
| Phase 2 | ~2,000 → 8,000 fl, **swelling** — fluid uptake dilutes dry mass to ~0.07 pg/fl | [23485973](notes/23485973.md) |
| Phase 3 | >8,000 → ~14,000 fl, **IGF-1-dependent**. *Igf1*-null: same hypertrophic cell *number*, cells 30% shorter, never exceed ~7,000 fl | [23485973](notes/23485973.md) |
| Driving force | Not falling extracellular osmolarity (would need plasma at ~20 mOsmol) and not macromolecule catabolism; organic osmolytes supply only **~9%**. **Active inorganic osmolyte import** | [20200963](notes/20200963.md) |
| Transporter 1 | **NKCC1 / SLC12A2.** Translocates from a perinuclear pool to the plasma membrane **immediately preceding** the volume increase; mRNA up 2–3×. Blocking it costs 35% of growth | [20200963](notes/20200963.md) |
| Transporter 2 | **AE3 / SLC4A3**, the only other transporter of 161 screened to change: **~14-fold up PZ→HZ**. DIDS + bumetanide together block **~80%** of lengthening — the same share enlargement contributes | [20200963](notes/20200963.md) |
| Regulated step | **Not transcription — membrane trafficking and phosphorylation.** Named by the authors as the open question | [20200963](notes/20200963.md) |
| Geometry | Expansion is directed by **laterally restricting matrix channels**; swelling persists at 424 mOsm, so it is intrinsic and regulated | [23485973](notes/23485973.md) |
| Column order | **Primary cilia** organise chondrocytes into columns; that polarity is **lost in human osteochondroma cells** | [23821404](notes/23821404.md) |
| Timing | Cells triple in height in ~12 h, then sit ~12 h before turnover (~24 h hypertrophic lifespan) | [23485973](notes/23485973.md) |
| Upstream of volume | **Rho-family GTPase signalling sets hypertrophic zone size**; up in jerboa with RhoGDI suppressed; disruption shortens limb bones | [34793695](notes/34793695.md) |
| Systemic brake | **Glucocorticoids**, possibly by suppressing local chondrocyte IGF-1 — the proposed cause of the perinatal arrest in all four rat plates | [18404738](notes/18404738.md) |
| Anti-lever | **Loop diuretics.** Furosemide shortened rat tibiae in vivo at normal electrolytes; bumetanide is the tool that defined the mechanism | [20200963](notes/20200963.md) |

**Every step has a name. Two have existing drugs pointing the wrong way (loop diuretics, corticosteroids), one has a licensed ligand pointing the right way (IGF-1 and its binding-protein regulation), and the regulated step — NKCC1 trafficking and phosphorylation — is the class of target small molecules reach well and that nobody in this literature has tried to push.**

---

## 3b. The gate on the actuator — the mechanism I had missed

Revision 2 named the actuator (§3) but not what opens it. **It is local free IGF availability at the hypertrophic chondrocyte, and it has exactly two controls: how much IGF-binding protein is present, and how fast that binding protein is cleaved.** Both are named, both have human genetic validation, and both have drugs — pointing the wrong way.

**Control 1 — IGFBP abundance, under direct epigenetic repression.** In chondrocyte-specific *Ezh1/Ezh2* loss ([27897169](notes/27897169.md)):
- Terminal hypertrophic cell size fell. **Neither *Igf1* nor *Igf2*, nor *Igf1r* nor *Igf2r*, changed.** (*Igf2*, not *Igf1*, is the predominant ligand in the hypertrophic zone.)
- **Only *Igfbp3* and *Igfbp5* rose, specifically in the hypertrophic zone, and ChIP put H3K27me3 directly on both promoters in wild-type chondrocytes and nowhere on *Ihh* or *ColX*.**
- The EZH1/2 inhibitor **UNC1999** raised the IGFBPs and markedly shrank hypertrophic cells in monolayer, pellet and fetal metatarsal culture.
- **Exogenous IGFBP3 or IGFBP5 alone shrank hypertrophic cells as much as UNC1999, with no additive effect.** And **high IGF-1 completely overrode UNC1999** — equal cell size with IGF-1 alone or IGF-1 + UNC1999. The mechanism is pure ligand sequestration.
- **IGF-1 did not significantly affect proliferation.** A fifth independent dissociation of *h_max* from *n*.
- IGF-1 alone **significantly increased bone growth** in fetal metatarsal culture.

**Control 2 — IGFBP proteolysis, with the largest rare-variant effect on human height sitting on it** ([29280739](notes/29280739.md)):
- **PAPP-A** cleaves IGFBP-4 **at the cell surface and only when IGF is already bound** — a substrate-gated, autocrine/paracrine *local* amplifier ([24572990](notes/24572990.md)). **PAPP-A2** cleaves **IGFBP-3 and IGFBP-5** — the two the hypertrophic zone uses.
- **STC2** covalently binds and inactivates both; **STC1** inhibits PAPP-A.
- **Of 83 rare and low-frequency coding variants associated with adult human height, the largest effect was in *STC2*: p.Arg44Leu gives +1.9 cm (P = 5.7×10⁻¹⁵) and p.Met86Ile +0.9 cm**, both with demonstrated partial loss of PAPP-A binding and of PAPP-A inhibition.
- The mirror: ***PAPPA2* loss of function gives −2.8 to −3.8 SD height with *elevated* total IGF-1, IGFBP-3, IGFBP-5 and ALS but low free IGF-1**, and no pubertal growth spurt. rhIGF-1 took height velocity from **3.7 → 7.6** and **3.0 → 6.2 cm/year**.
- **Mice: *Stc2* KO born 15% heavier, with the growth-promoting effect "persisted or became more apparent in post-natal growth"; *Pappa* KO and hSTC1/hSTC2 transgenics 30–40% lighter; and hSTC1/hSTC2 transgenics showed "severe impairment in post-natal, linear *axial* skeletal growth."**
- *PAPPA*, *PAPPA2*, *STC2* and *IGFBP4* are all in genome-wide-significant height loci.

**Why this is the answer rather than one more lever.** It is the gate on the term that carries 59% of axial growth and ~100% of growth modulation (§2). It is **local** — a surface protease releasing ligand where it sits, which is precisely the property every systemic idea in [COMPOUNDS.md](COMPOUNDS.md) lacks and which acromegaly's mandible-only phenotype indicts. It has **human genetic validation at ~2 cm per allele**. Its effect **strengthens postnatally**. And in the one explicitly axial observation in the corpus, the overexpression phenotype is **axial**.

**And it explains two compound leads I under-rated, because I was scoring them against cell number.**
- **T3 raises *PAPPA* 2.7–3.4-fold in adult human articular cartilage explants from 60–76-year-olds** ([38664820](notes/38664820.md)).
- **Dasatinib raises *IGF1* while lowering *IGFBP1* and *IGFBP3* in adult human chondrocytes** ([39402753](notes/39402753.md)).
**Both were already moving this exact node in adult human tissue. Neither paper measured hypertrophic cell volume, which is the endpoint that would have shown whether it mattered.**

**The correctly-signed epigenetic lever is the opposite of the obvious one.** Weaver syndrome (EZH2 partial loss) is a human overgrowth disorder, which invites reaching for an EZH2 inhibitor. **Do not.** In chondrocytes, EZH1/2 loss *derepresses* IGFBP3/5 and *shrinks* hypertrophic cells; and the Weaver mouse has **normal femur, tibia and body length**, with its phenotype being raised cortical area and **periosteal/endosteal mineral apposition** — appositional width, not length — reversed by the KDM6A/6B inhibitor **GSK-J4** ([37425751](notes/37425751.md)). Two lineages, opposite signs, one mark: **PRC2 loss costs length in chondrocytes and adds width in osteoblasts.**
> **Prediction, mine, untested: KDM6A/6B inhibition (GSK-J4 class) should deepen H3K27me3 at *Igfbp3/5*, lower IGFBP abundance, raise local free IGF and therefore increase hypertrophic cell volume.** The mirror-image arm of an experiment already run in the other direction. §14.7.

**The dangers, since they were asked for directly.**
- **PAPP-A is a validated oncology target *for inhibition*.** An anti-PAPP-A exosite antibody (Ki 135 pM) suppresses xenograft growth ([24572990](notes/24572990.md)). Raising PAPP-A activity means deliberately doing what that drug exists to prevent.
- ***Pappa*-null mice are long-lived with reduced age-related pathology** (20351075, 36542300 — abstract-only here). **The growth direction and the longevity direction are opposite on the same gene.**
- **Intracranial hypertension**: one of four rhIGF-1-treated PAPP-A2-deficient patients required discontinuation for severe headaches; resolved on withdrawal.
- **hSTC2 overexpression caused 26–34% neonatal mortality in mice** — the axis is not benignly tunable in either direction.
- **Insulin resistance, pre-diabetes and hypoglycaemia risk**; IGF-1 signals through insulin and hybrid receptors.
- **STC1 also governs calcium and phosphate metabolism.**
- And the standing objection: **the human +1.9 cm is a lifelong developmental effect in people whose plates were open. Nothing shows this axis does anything after closure.**

---

## 4. Where the headroom is, exactly

Two papers that do not cite each other, multiplied together.

- Decker: **adult articular deep-zone chondrocytes are under 50% the diameter of metaphyseal growth-plate hypertrophic cells** (and ~60% of secondary-ossification-centre hypertrophic cells). Diameter scales as the cube root of volume, so **<12.5% of the volume** ([28438606](notes/28438606.md)).
- Cooper: a terminal metaphyseal hypertrophic cell is **~14,000 fl**, and **phase 1 ends at ~2,000 fl** ([23485973](notes/23485973.md)).

12.5% of 14,000 fl ≈ **1,750 fl.**

**So the adult articular deep-zone chondrocyte sits essentially at the phase-1/phase-2 boundary. It has completed true hypertrophy and never started to swell.** For comparison, the *slowest* rat growth plate's hypertrophic cells reach 4,000 µm³ ([18404738](notes/18404738.md)) — more than twice the adult articular value.

That is a far more specific statement than revision 1's "halved set-point," and it names the targets: **phase 2 (osmotic swelling: NKCC1, AE3) and phase 3 (IGF-1-dependent).** Both are unused. The 8-fold volume rise those same cells perform between P14 and P28 ([28438606](notes/28438606.md)) shows the machinery is not absent.

**Caveat, stated plainly: this is an inference from two independent measurements in different species, and no one has shown that an adult deep-zone chondrocyte can be made to enter phase 2.** It is the single most important thing to test (§14.1).

---

## 5. The dial: ERK

One pathway moves four things at once. Assembled from two papers; neither proposes it.

| ERK | Effect | Source |
|---|---|---|
| **Low** | Groove-of-Ranvier **Ctsk+ progenitors proliferate excessively and turn chondrogenic** → raises *n* | [25003010](notes/25003010.md) |
| **Low** | ***Ihh* up 6-fold and PTHrP up** → sustains proliferation, inhibits differentiation, and is the anti-exhaustion signal | [25003010](notes/25003010.md), [24875294](notes/24875294.md) |
| **Low** | Cells held at early-hypertrophic; **COLX zone expands from ~3 to >10 cells per column; cell size increases** → raises *h_max* | [24875294](notes/24875294.md) |
| **Low** | Late-hypertrophic programme off: matrix degradation, apoptosis, angiogenesis, osteoclastogenesis all suppressed → **conversion blocked** | [24875294](notes/24875294.md) |
| **High** | Terminal differentiation, matrix degradation, vascular invasion, replacement by bone → **conversion proceeds** | [24875294](notes/24875294.md) |

Mechanism: SHP2 → RAS/ERK; **ERK represses IHH/PTHrP**; the normal circuit is **perichondrial FGF18 → FGFR3 → ERK → suppresses IHH**, and IHH then induces PTHrP in the periarticular perichondrium, with IHH/PTHrP feeding back to sustain proliferation and block differentiation. IHH additionally **couples chondrogenesis to perichondrial osteogenesis** at the bony collar — so one signal licenses both the cartilage expansion and the bone that follows it ([25003010](notes/25003010.md)).

**Agents exist on both sides.** Down: approved **MEK1/2 inhibitors**, and allosteric **SHP2 inhibitors**. Up: **FGF-18 / sprifermin**, the one compound with a randomised controlled trial showing thickening of adult human cartilage ([26138203](notes/26138203.md)).

**So the ratchet of revision 1 is one pathway cycled, not five interventions.** Low-ERK phase: expand the progenitor pool, raise Ihh/PTHrP against exhaustion, let cells swell, hold conversion. High-ERK phase: convert.

**And the failure mode is named: sustained low ERK in these cells is metachondromatosis** — enchondromas, osteochondromas, skeletal deformation, avascular necrosis of the femoral epiphysis, chondrosarcoma. The build phase of this scheme is a cartilage tumour that must be converted on schedule. The conversion phase is what distinguishes a growth plate from a neoplasm.

---

## 6. The target: the rim, not the interior

Revision 1 aimed at the articular interior — the deep zone and the tidemark. **The evidence says aim at the perichondrial rim.**

**Six independent markers, one compartment.** Ctsk+ chondroid progenitors (CD44+ CD90+ Stro-1+ CD166+) in the groove of Ranvier ([25003010](notes/25003010.md)); CD90+/CD105+/STRO-1+/Jagged1+/BMPR1a+ CD45− mesenchymal progenitors in the same groove ([25164565](notes/25164565.md)); Gli1+ periosteal stem cells ([35844802](notes/35844802.md)); Scx+ and Tppp3+ tendon/ligament progenitors ([38672135](notes/38672135.md)); Fsp1+ fibroblasts at bone–ligament attachments ([24875294](notes/24875294.md)); and the groove as the lateral-expansion source for articular cartilage ([28438606](notes/28438606.md)).

**Five reasons the rim beats the interior.**
1. **Specificity control.** Deleting *Ptpn11* in Col2a1+ proliferating or Col10a1+ hypertrophic chondrocytes produced **no osteochondromas over 6 months**; deleting it in Ctsk+ groove cells produced lesions at hip, knee and ankle by **12 weeks** ([25003010](notes/25003010.md)).
2. **The interior is unresponsive.** "Adjacent articular chondrocytes stay passive" on injury; the responders are synovial Prg4-lineage CD44+/P75+ cells (70% proliferate) and the groove ([28438606](notes/28438606.md)).
3. **The rim is perfused; the interior is not.** The groove and ring of LaCroix carry **mature α-SMA-stabilised vessels, better vascularised than the ossification centre itself**, and the surrounding perichondrium and periosteum are "highly vascularized" ([25164565](notes/25164565.md)). **A systemically delivered agent reaches the groove and does not reach the interior of articular cartilage.** This is decisive for anything that is not an intra-articular injection.
4. **It already feeds the articular surface.** Groove progenitors migrate into the epiphysis and **onto the surface of the articular cartilage**; Ctsk+ cells are present in healthy adult articular cartilage and **increase during adult OA**, in clusters of proliferating chondrocytes ([25164565](notes/25164565.md), [25003010](notes/25003010.md)).
5. **It is required for longitudinal growth and it has a wall.** Salter-Harris type IV fractures confined to the groove cause **severe growth disturbance**; the ring of LaCroix "keeps the cells from oozing out under axial loading" ([25164565](notes/25164565.md)). A niche that is functionally necessary and mechanically contained.

The brakes and accelerators are there too: Crabp1 is a perichondrium marker; Shox2 appears in jerboa metatarsal **proliferative zone and perichondrium**; Mab21L2 sits in resting zone, proliferative zone and perichondrium; and the HoxB9/HoxB13/Pax1/Prrx1 patterns made those authors suspect the **surrounding perichondrium and connective tissues** drive the phenotype ([34793695](notes/34793695.md)).

---

## 7. Polarity is set by the gradient's direction

Revision 1 asserted that an articular surface has the right polarity. **Revision 2 can say why, and it is a rule rather than an assertion.**

- **Exostoses are properly zoned ectopic growth plates whose "main axis of elongation is at about 90° angle compared to that of the adjacent native growth plate."** They form beside, never within, the plate, and protrude into perichondrium ([23821404](notes/23821404.md)). Confirmed independently: COLX+ columns in SHP2-null lateral outgrowths run perpendicular to the native axis ([24875294](notes/24875294.md)); zebrafish *ext2*-mutant cells grow out from the cartilage edge perpendicular to wild-type cells.
- **Why: heparan-sulfate deficiency lets Ihh and BMP leak sideways into the perichondrium, so the new morphogen gradient runs radially outward and the new plate aligns to it.** Stated outright in the other literature too: "**any change in the strength or territory of FGF and IHH signaling can influence the polarization of physeal chondroid cells, allowing them to grow in the wrong direction or location**" ([25003010](notes/25003010.md)).
- **The design consequence.** An exostosis is a lateral lesion because it forms at a lateral border. **At an articular or metaphyseal border the geometry is already axial** — subchondral bone on one side, joint space on the other — so a broadened BMP/Ihh gradient emanating from the subchondral plate runs **along the bone's long axis**. Put the same perturbation at an axial border and the expected product is an axially oriented interface, not a lump.
- **And the order-preserving requirement: primary cilia build the columns, and they are lost in human osteochondroma cells** ([23821404](notes/23821404.md)). Columns are what make growth longitudinal rather than isotropic ([31787777](notes/31787777.md)). **An exostosis has the right axis and degraded columnar order — which may be exactly why it makes a mass instead of a shaft.** Preserving ciliary function while de-restricting the gradient is a specific, testable requirement that nothing in the corpus has tried. ((−)-Epicatechin is reported to rescue primary-cilium defects, [42650460](notes/42650460.md).)
- **One sharpening from the fast-growing bone.** The jerboa metatarsal shows **increased** heparan, chondroitin and dermatan sulfate synthesis ([34793695](notes/34793695.md)), the opposite of the HS deficiency that makes exostoses. **For ordered longitudinal growth you want the gradient steep and correctly oriented, not simply de-restricted.**

---

## 8. De-repression, not supply

Two literatures that do not cite each other reach the same conclusion.

**The border is actively maintained.** Ext1 and heparan sulfate are "critical regulators of the perichondrium phenotype — allowing it to act as an **anti-chondrogenic border** around the growth plate — and are also essential to **restrain and contain cartilage growth**." **Surfen**, a small-molecule HS antagonist, dose-dependently turns limb mesenchyme chondrogenic, raises aggrecan, COL2, Runx2 and Sox9, **raises pSmad1/5/8 before nodules form**, and makes the cells more sensitive to **endogenous and exogenous BMP2 — all abolished by Noggin**. In vivo, perichondrial *Ext1* deletion (or Surfen on limb explants) turns perichondrial cells nuclear-pSmad1/5/8-positive and is followed by **ectopic cartilage within the perichondrium** ([23821404](notes/23821404.md)). HS loss is a dose-graded rheostat: 100% → nothing, ~50% → occasional rib lesions, ~25% → **half the animals form properly zoned exostoses beside long-bone plates**.

**The fast bone got fast partly by releasing brakes.** In jerboa metatarsals versus mouse ([34793695](notes/34793695.md)):
- **Crabp1 10.6× higher (padj 1.5E-92)** — the most significant gene in the dataset, a perichondrium marker, which **sequesters retinoic acid** and blocks its anti-proliferative effect.
- **Gdf10/Bmp3b 9.3× lower (padj 1.3E-83)** — an inhibitory TGF-β ligand in the proliferative zone, itself **upregulated by RA or an RARγ agonist**.
- **Mab21L2 16.8× lower in metatarsals (padj 1.8E-26) while 3.9× higher in radius/ulna** — a BMP4/Smad1 inhibitor, **also low in elongated fetal bat wing digits**, whose misexpression shortens the chicken humerus by 1.9% (p = 0.0221) and whose human gain-of-function mutations shorten the proximal limb.
- **And the pharmacology: "exogenous RA inhibits skeletal elongation in juvenile rats, and pharmacological inhibition of RA signaling accelerates rat metatarsal elongation in vitro."**

**That confirms the RARγ mirror hypothesis of [COMPOUNDS.md](COMPOUNDS.md) Node E.** I had noted that palovarotene (RARγ agonist) ablates plates and shortens tibiae 13–19% ([30226468](notes/30226468.md)), that retinoids close human plates early, and that nobody had tried the reverse. **It has been tried, it works in vitro, and the natural experiment agrees.** Retinoic acid is an endogenous brake on longitudinal growth. (The primary — almost certainly De Luca 2000, PMID 10614657 — is Tier 00 of [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md) and I have not read it. Given how much weight this now carries, that is the most important gap in revision 2.)

**And one accelerator with a measured number.** *Prrx1-Cre;Rosa-LSL-Shox2* mice (2–2.5× Shox2): indistinguishable at birth, then **+23.6% metacarpal and +9.1% metatarsal length by eight weeks** ([34793695](notes/34793695.md)). A single transcription factor, one order of magnitude of overexpression, ~10–24% of bone length, accruing postnatally. Human *SHOX* loss causes the short stature of Turner and Langer syndromes.

---

## 9. Two human proofs

**9.1 An organised ectopic growth plate keeps running in an adult.** An exostosis is "a growth plate-like cartilaginous cap overlaying a bony base" with, in the EXT1/EXT2 form, "relatively normal growth plate architecture" and a narrow COLX zone at the base of the cap ([24875294](notes/24875294.md)). And:

> **"Although no new exostoses form after puberty when the growth plates close, existing exostoses can continue to grow and cause further pain and complications, leading to a surgical rate of 67% in adults."** ([23821404](notes/23821404.md))

**Initiation requires a juvenile context; propagation does not.** That is the same split garetosmab showed pharmacologically — new heterotopic lesions 40.9% → 0%, existing ones untouched ([37770652](notes/37770652.md)). **It is the strongest human evidence for the central claim of this document: the interface is the hard part, and once it exists it runs in an adult.**

**9.2 A native plate stays functional into the fourth decade without ERα signalling.** Two men with homozygous CYP19A1 (aromatase) mutations, first evaluated at **24 and 38 years, at 204 cm and 190 cm**, with **"linear growth continued into adulthood"**, severely retarded bone ages, and **"lack of epiphyseal fusion… detected by x-ray films in the knees and pelvis."** One man with a homozygous ESR1 mutation presents identically ([24485503](notes/24485503.md)).

**This says the closure clock is estrogen-paced, not division-counted.** My corpus attributes plate senescence to progenitor exhaustion ([39563452](notes/39563452.md), [19098525](notes/19098525.md)); these men were still growing at 38. Their pools had not exhausted on any intrinsic schedule. **Exhaustion is gated by ERα signalling, not an inevitable countdown** — which is a materially better premise for *n* being recoverable.

**Both proofs are about plates that never closed, or lesions already established.** Neither shows a closed human plate reopening. That remains unobserved.

---

## 10. The revised chain

**Stage 1 — release the border.** Lower the barrier to the endogenous Ihh/BMP gradient at an **axial** border so perichondrial/groove progenitors are licensed to form cartilage. Known inputs: HS antagonism (Surfen, heparanase, Ext reduction); RA-pathway antagonism; low ERK; Mab21L2/Gdf10 reduction. Mechanical input: at an articulation, periosteal Sox9+Runx2+ progenitors stay cartilage **only while movement continues** — paralysis or stretch-channel blockade turns them to bone ([21600197](notes/21600197.md)) — and sliding shear physically activates latent synovial TGF-β ([22858668](notes/22858668.md)), supplying the permanent-cartilage fate fork of [37126720](notes/37126720.md) for free. **Keep the gradient steep and axial, and keep primary cilia intact, or the product is a lump.**

**Stage 2 — expand the pool.** Low ERK makes Ctsk+ groove progenitors proliferate and turn chondrogenic, with **Ihh up 6-fold and PTHrP up** — proliferation sustained, differentiation inhibited, exhaustion opposed ([25003010](notes/25003010.md)). Mechanically, cyclic articulating shear roughly **doubles the Prg4+ surface pool in adult mice in a month** via FFSS → PGE2/PTHrP/ATP → CREB ([24449269](notes/24449269.md)). *Note this stage matters much less than revision 1 implied — it is the 9% term.*

**Stage 3 — drive the volume actuator. This is the main event.** Move cells from the phase-1/phase-2 boundary through phase 2 (NKCC1/AE3-driven osmotic swelling) and phase 3 (IGF-1-dependent). Available inputs: **local free IGF-1** (raised endogenously by dasatinib's suppression of IGFBP1/3, [39402753](notes/39402753.md); deliverable as a **cartilage-targeting scFv–IGF-1 fusion** that already exists, [37483459](notes/37483459.md)); **subchondral bone turnover during offloading, which releases TGF-β, BMP and IGF stored in the bone matrix** ([21565898](notes/21565898.md)); **low ERK**, which expands the COLX zone >3-fold and increases cell size ([24875294](notes/24875294.md)); **Rho-GTPase signalling**, which sets hypertrophic zone size ([34793695](notes/34793695.md)); and **T3** as the terminal-maturation licence in adult human tissue ([38664820](notes/38664820.md)). **Avoid loop diuretics and corticosteroids.** The regulated step — NKCC1 membrane trafficking and phosphorylation — is unexploited.

**Stage 4 — convert, on schedule.** Raise ERK (FGF-18/sprifermin) to drive terminal differentiation; **Piezo1 → YAP/β-catenin → BMP2 + VEGFA** from the resident cell, with **Sirt1 opening Piezo1 even when its force-transduction residues are mutated** ([35844802](notes/35844802.md), [40999873](notes/40999873.md)). The front's own trigger is enzymatic: **VEGF is stored in the cartilage ECM and released by MMP-2/9/13**, and heparanase does the analogous job for HS-bound factors and is naturally enriched at the chondro-osseous junction ([25164565](notes/25164565.md), [23821404](notes/23821404.md)). **New vessels arrive by sprouting from the bone collar, not from circulating progenitors** — so the front must abut perfused bone.

**Stage 5 — shield, and cycle.** Hypertrophic chondrocytes die by **YAP–p73–caspase-3 at ~0.023 MPa** without shielding and tolerate 25× more with it ([33063669](notes/33063669.md)); death tracks **principal compressive stress, not hydrostatic**. The adult solution is measured: **knee joint distraction — contact stress removed, fluid oscillation preserved — took affected-compartment cartilage from 2.4 → 3.0 mm in a year in adult humans**, against typical OA loss of ≤0.2 mm/year ([21565898](notes/21565898.md)). Cycle because the stages want opposite states and because **static stimuli adapt away** ([31787777](notes/31787777.md)), and because the Wilsman group's own hypothesis for why four plates diverge is **differential compressive, tensile and strain loading, accentuated by gravity once the animal walks** ([18404738](notes/18404738.md)) — mechanics acting on the volume term.

---

## 11. Minimum viable version, revised

> **Three inputs.**
> **(1) Release the brake at an axial border.** One de-repression input, delivered to the perichondrial rim — which is perfused and therefore reachable. RA-pathway antagonism is the best-supported; HS antagonism (Surfen) is the only one with a small molecule shown to turn perichondrium chondrogenic; low ERK does both this and (2) and (3).
> **(2) Drive the volume actuator.** The 59% term. Local IGF-1 availability plus whatever raises NKCC1/AE3 membrane activity. This is the step with the most headroom (§4) and the least prior art.
> **(3) Cycle, phased against unloading.** One physical variable that supplies shielding, latent TGF-β activation, the stress-type gradient, progenitor recruitment, subchondral factor release, and the anti-adaptation requirement — and that the kinetics literature independently proposes as the natural setter of differential cell volume.

Revision 1 said two inputs and put the mechanical one first. **Revision 2 keeps the mechanical input but demotes it from "six of seven jobs" to "the enabling envelope," and promotes the volume actuator to the central intervention.** The reason is §2: mechanics on an existing apparatus buys about +5% growth per 0.1 MPa ([23009361](notes/23009361.md)), whereas the volume term spans a 5-fold measured range.

**Where input (2) now points.** Revision 2's §3b replaces "whatever raises NKCC1/AE3 membrane activity" with something specific: **raise local free IGF at the hypertrophic cell, by lowering IGFBP3/5 abundance or by raising IGFBP proteolysis.** The named handles are **PAPP-A2 activity**, **STC2 inhibition** (a secreted target, the most tractable class), **the H3K27me3 mark on *Igfbp3/5*** (and therefore KDM6 inhibition, §14.7), and the two agents already shown to move this node in adult human tissue — **T3** (*PAPPA* up 2.7–3.4×) and **dasatinib** (*IGF1* up, *IGFBP1/3* down). It also makes the preferred site the **vertebral endplate** rather than the knee, for the reasons in §13.3b.

**One addition worth its complexity, unchanged from revision 1:** a single marrow-access or margin event at the start. The de novo literature says a signal without an injury does not initiate ([28629737](notes/28629737.md)), and in a primed adult the sufficient injury was **a 5 mm shallow skin cut** ([28645539](notes/28645539.md)).

---

## 12. The coupling condition, with a dial

Unchanged in substance, improved in control. **Length accrues only if addition ≥ conversion.**

| | Result | Documented as |
|---|---|---|
| addition **>** conversion | cartilage thickens, **no length** | palovarotene (tibia **13–19% shorter**, [30226468](notes/30226468.md)); chondrocyte Piezo1 cKO (**wider plate**, ossification blocked, [40999873](notes/40999873.md)); systemic anti-VEGF (**hypertrophic zone expanded**, shortening worse, [37483459](notes/37483459.md)); PKD inhibition; IGF-I + marrow cells on PLGA (**a large dense mass of hypertrophic chondrocytes**, no angular correction, [26309783](notes/26309783.md)); **sustained low ERK = metachondromatosis** ([25003010](notes/25003010.md)); **HS deficiency = hereditary multiple exostoses** ([23821404](notes/23821404.md)) |
| addition **<** conversion | cartilage thins, **this is osteoarthritis** | T3's signature overlaps **37 GWAS OA risk genes** ([38664820](notes/38664820.md)) |
| addition **≈** conversion | **constant thickness, bone end advances, segment lengthens** | a growth plate |

**What revision 2 adds is that both rates now hang off one upstream regulator.** ERK sets addition (low) and conversion (high), and **IHH couples chondrogenesis to perichondrial osteogenesis** ([25003010](notes/25003010.md)). A shared upstream regulator is what makes matched rates achievable rather than a knife-edge. It also means an open-loop push in either direction lands in one of the two failure rows — which is why a list of compounds is the wrong shape of answer.

---

## 13. Magnitude, revised

**13.1 The appendicular arithmetic (unchanged).** Four axial articular surfaces per leg — femoral head, distal femur, proximal tibia, distal tibia — whose juvenile physes together contribute roughly **1.8 cm/year per leg** at full throughput. At 25% restored: ~0.45 cm/leg/year. At 50%: ~0.9 cm.

**13.2 The axial skeleton, which revision 1 omitted.** From T5 to L5, **spinal length rises from ~250 mm to ~350 mm between ages 7.5 and 20 — 100 mm, almost all of it vertebral.** At 7.5 years the vertebral contribution is **~17 mm/year** against ~8 mm/year discal, and **discal height growth is effectively zero after age 12** (16778695, abstract only — Tier 0c). That is 17 vertebrae, **34 endplates**, each running at ~1 mm/year per vertebra at peak. The whole spine is ~24 vertebrae and **~48 endplate growth surfaces on the stature axis**, against 4 per leg.
Extrapolated to the full spine, ~24 mm/year at juvenile throughput — **comparable to both legs combined.** At 25% restored: ~6 mm/year from the spine alone.

**13.3 And the spine closes last.** Cervical vertebral body growth continues to **19–20 in males, 17–18 in females** (30945292, abstract only); ring apophyses reach 98% fusion only at 21, with several years of level-to-level heterogeneity ([34362001](notes/34362001.md)); and "**the spine continues to grow longer than the lower extremities… after the lower limb's growth has ceased**" (Sanders 2020, cited in [34362001](notes/34362001.md)). **If recency of closure predicts reactivability, the vertebral endplates are the best target in the adult skeleton, and they are also the most numerous.** This is the single clearest way to raise the ceiling, and it was absent from revision 1.

**13.3b Why the spine is structurally the right site, not just the most numerous.** Hypertrophic chondrocytes **tolerate hydrostatic stress and die under principal compressive and deviatoric stress at ~0.023 MPa without shielding**, tolerating 25× more once shielded ([33063669](notes/33063669.md)); and the single measured adult-human cartilage-thickening intervention works by **removing contact stress while preserving fluid-pressure oscillation** ([21565898](notes/21565898.md)). **The vertebral endplate is the only growth cartilage in the body that faces a hydrostatically pressurised, diurnally cycling fluid chamber — the nucleus pulposus — instead of an articulating contact surface.** If that is right, the spine supplies Stage 4's shielding and Stage 5's cycling anatomically, free, at up to 48 surfaces, where a knee needs an external fixator to approximate it. **Caveat: this rests on intradiscal pressure and vertebral endplate anatomy papers I have not read** (18590419, 4095820, 21213210; 15296209 came back abstract-only), and it is the most important untested structural claim in revision 2.

**13.3c And the axial bias of the IGF gate.** hSTC1 and hSTC2 transgenic mice showed "**severe impairment in post-natal, linear *axial* skeletal growth**" ([29280739](notes/29280739.md)) — the one explicitly axial statement about the §3b gate in the corpus. Its primary (their ref 24) is unread and is now a priority.

**13.3d The seductive axial dead end, flagged so it is not chased twice.** **Brachyury (TBXT)+ notochordal-lineage cells persist in the adult human nucleus pulposus** at every age and degeneration grade, with a CA12+Gal3+T+CD24+ subpopulation identifiable by flow cytometry ([28473691](notes/28473691.md)) — and Brachyury is the master regulator of **posterior axial elongation**. Raising *TBXT* dose produces **benign notochordal cell tumours in adult vertebrae, which progress to chordoma** (40323130, abstract only). **So the adult axial skeleton does retain a proliferation-competent elongation-programme lineage — and its output is an intraosseous mass, not a longer vertebra.** The tailbud neuromesodermal progenitor pool that Brachyury actually elongates does not exist after embryogenesis. Note the pattern this completes, though: **heparan-sulfate dose → exostosis → chondrosarcoma; ERK-low in groove progenitors → enchondroma/osteochondroma → chondrosarcoma; TBXT dose → BNCT → chordoma.** Three lineages, three nodes, one shape: adult proliferative competence is retained, dose-gated by a single node, and its uncontrolled form is a tumour.

**13.4 Combined, at 25% restored throughput: ~0.9 cm/year from both legs plus ~0.6 cm/year from the spine ≈ 1.5 cm/year.** At 50%: ~3 cm/year.

**13.5 What the numbers rest on, and what could break them.** The 59/32/9 partition is cited, not read (8982136, Tier 00). The spine partition is an abstract. The adult tidemark advance rate is still unread (Tier 0). The §4 headroom calculation multiplies two measurements from different species. **No one has measured bone length under any agent named in this document.** And the independent brake on all of it: endochondral growth-zone arrest is conserved in mammals, birds and even an indeterminately-growing teleost ([32852849](notes/32852849.md)) — this is working against something deep.

**13.6 A separate, additive axis.** Adults lose standing height to disc narrowing, which is intrinsic and independent of body composition ([36719517](notes/36719517.md)), and non-surgical decompression increases disc height in elderly humans (their ref 17, unread). **That is reversible fluid and matrix content, not growth** — different mechanism, different ceiling, different durability — but it is the only existing non-surgical adult height-changing intervention in the corpus, and it stacks rather than competes.

---

## 14. The decisive experiments

**14.1 Can an adult deep-zone chondrocyte enter phase 2?** The load-bearing assumption of §4. Adult human or large-animal osteochondral explants; measure chondrocyte volume by confocal/diffraction phase microscopy at baseline and after (a) raising local free IGF-1, (b) MEK inhibition, (c) both, with and without osmotic challenge. **Kill criterion: no volume increase beyond ~2,000 fl under any condition.** If that fails, §4 is wrong, the headroom is not there, and the rest of this document loses its principal mechanism.

**14.2 Does the ERK cycle produce length rather than a lump?** Mature rabbit or sheep (**not** rat or mouse, which never fuse). Arms: sham; sustained low ERK; sustained high ERK; **cycled**. Endpoints: segment length against the contralateral limb; tidemark position by sequential fluorochrome labelling; hypertrophic cell volume; COLX zone depth; Prg4+ and Ctsk+ cell counts; and osteophyte/OA/lesion scoring. **Kill criteria:** sustained-low arm produces a mass (expected — it is the metachondromatosis prediction); cycled arm produces a mass too → the scheme is an osteochondroma generator; no tidemark advance in any arm → no conversion lever exists.

**14.3 Is the rim really the responsive compartment in an adult?** Deliver the same de-repression input to (a) the groove of Ranvier and (b) the articular interior, and compare. **Prediction from [25003010](notes/25003010.md) and [28438606](notes/28438606.md): only the rim responds.** If the interior responds equally, the §6 redirection is wrong and the pharmacokinetic argument loses its force.

**14.4 Does an axial border give an axial plate?** The §7 rule. Place the same HS-antagonist or low-ERK perturbation at a lateral metaphyseal border versus an axial (subchondral/metaphyseal end-on) border and measure the orientation of the resulting columns. **Kill criterion: both produce 90° lateral outgrowths** → polarity is not gradient-set and the whole de-repression route produces only exostoses.

**14.5 Does RA antagonism lengthen bone in vivo?** Read 10614657 first. Then: RARγ antagonist or inverse agonist in growing and in mature animals, with bone length as the primary endpoint and plate histology, closure timing and chondrocyte volume as secondaries. **This is the cheapest high-value experiment in the document** — the agents exist, the in-vitro result exists, and nobody has run the in-vivo length measurement.

**14.6 The axial site.** Everything in 14.1–14.5 at a **vertebral endplate** rather than a limb, given §13.2–13.3. Nobody in this corpus has looked at the adult vertebral endplate as a growth target.

**14.7 Does KDM6 inhibition enlarge hypertrophic chondrocytes?** The mirror of an arm already run. [27897169](notes/27897169.md) applied the EZH1/2 inhibitor UNC1999 to fetal metatarsal culture and got raised *Igfbp3/5* and **shrunken** hypertrophic cells. Run **GSK-J4** (or a selective KDM6B inhibitor) in the same system, with hypertrophic cell size and metatarsal elongation as primary endpoints and *Igfbp3/5* and H3K27me3 ChIP as mechanism. **Prediction: deeper H3K27me3 at *Igfbp3/5* → less IGFBP → more free IGF → larger hypertrophic cells → faster elongation. Kill criterion: no increase in cell size or elongation.** Cheap, fast, and it tests §3b's whole logic in one experiment. Watch the confound that GSK-J4 also suppresses osteoblast apposition ([37425751](notes/37425751.md)).

**14.8 Does the §3b gate exist in adult tissue, and does it have an axial bias?** Measure **PAPP-A, PAPP-A2, STC1, STC2, IGFBP3, IGFBP5 and H3K27me3 at the *IGFBP3/5* promoters** in adult human articular cartilage deep zone and in adult human vertebral endplate cartilage, side by side. **Nobody has done this.** Then: STC2 neutralisation or PAPP-A2 supplementation on adult osteochondral and vertebral-endplate explants, with hypertrophic cell volume as the endpoint. **Kill criterion: the gate's components are absent from adult tissue, or free IGF cannot be raised locally.** If the axial tissue shows more STC2 or more IGFBP than the appendicular, that would independently support §13.3c.

**14.9 Is the vertebral endplate's stress state what §13.3b assumes?** Read the intradiscal-pressure and endplate primaries first. Then measure, in a large animal, what fraction of axial load arrives at the endplate cartilage as interstitial fluid pressure versus matrix compression, across the diurnal cycle. **Kill criterion: the endplate sees principal compressive stress comparable to an articular surface** → the anatomical-shielding argument for the spine collapses and the site advantage reduces to surface count.

**14.10 Is the adult human proximodistal positional code graded or binary?** **The single highest-value experiment in the project**, and it needs no new tissue. [16895450](notes/16895450.md) established that adult human fibroblasts retain a cell-autonomous proximodistal record — but found it **binary** (autopod vs rest), with no stylopod/zeugopod signature and no gradient, on 2006 cDNA arrays with 6–7 samples per limb. Length is generated by **intercalation across a positional gap** (§18.6), which requires intervening values to exist. Repeat the proximodistal comparison with **scRNA-seq and ATAC across many evenly spaced levels of one adult human limb**, powered for a gradient, and score the 337-gene signature, the HOX code and HS sulfotransferases level by level. **Kill criterion: no gradient at adequate power, and the finer code absent from other cell types too** → the adult human limb has one positional boundary, there is almost nothing to intercalate, and §18 does not transfer to an adult limb as stated. **Converse: a graded code exists** → positional disparity can be installed between real neighbouring values, and §18 becomes the project's primary route.

**14.10b Does the positional record exist in the tissues this project targets, and does it still exist in matrix?** Two parts. (i) Score the **337-gene positional signature, the HOX code and HOXA13 protein in adult human cartilage, perichondrial groove, periosteum and vertebral endplate** — public datasets may answer this before any tissue is collected. (ii) Repeat [27499874](notes/27499874.md) with **adult** mouse limb-skin ECM donors, anterior vs posterior, ± heparin lyase III; that study stopped at PN9. **Kill criterion: the target tissues carry no positional signature** → the positional layer exists in skin fibroblasts and nowhere useful.

**14.11 Does CYP26 inhibition do anything in a mammal's skeleton?** Three tiers, cheapest first. (i) Is **CYP26B1** expressed in adult human articular cartilage, vertebral endplate and perichondrial groove? If CYP26B1 is actively clearing RA in adult growth-competent cartilage, that is a standing repression with a Phase-II drug already pointed at it. (ii) Talarozole or liarozole on adult human osteochondral and endplate explants — endpoints **MEIS1, SHOX, COL10A1, and hypertrophic cell volume**, with the palovarotene sign conflict (§18.7) explicitly tested by running an RARγ agonist arm in parallel. (iii) Only then, an intact adult animal. **Kill criterion: CYP26B1 is absent from adult cartilage, or raising RA moves SHOX in the wrong direction** → §18 does not transfer out of the blastema and should be recorded as an amphibian mechanism.

**Positive control throughout:** the **adult mandibular condyle**, which runs this apparatus, never fuses, and is mechanically reactivatable in adult primates ([THEORY.md](THEORY.md) §2, §7).

---

## 15. Honest tensions and unknowns

**New in revision 2.**
- **§4's headroom is an inference across species.** Decker's diameters are mouse articular cartilage; Cooper's volumes are mouse and jerboa growth plate. The cube-root conversion and the 1,750 fl figure are mine. **No adult deep-zone chondrocyte has been shown to swell.**
- **The ERK dial is assembled by me from two papers.** Neither [25003010](notes/25003010.md) nor [24875294](notes/24875294.md) proposes cycling it, both are genetic loss-of-function in juvenile mice, neither measured bone length, and the "cell size increases" observation appears in text and a supplementary legend without a quantified volume.
- **The RA result I am leaning on hardest is unread** (10614657, Tier 00) and reaches me through a 2022 review's citation.
- **The 59/32/9 partition is unread** (8982136, Tier 00) and reaches me through two papers that cite it.
- **MEK inhibitors are oncology drugs** with rash, retinopathy, reduced ejection fraction and cardiomyopathy. SHP2 inhibitors likewise. Nothing in this corpus used either for growth.
- **Sustained low ERK is metachondromatosis; HS deficiency is hereditary multiple exostoses** (67% adult surgery rate, 2–5% chondrosarcoma at a mean age of 35). **The build phase of this scheme is, mechanistically, a benign cartilage tumour.** That is not a risk I can argue away; it is the same molecular state.
- **Exostoses lose columnar polarity**, which is the property longitudinal growth requires — and HME patients are *shorter*, with limb-length inequality and angular deformity. **The natural experiment produces mass and deformity, not height.**
- **Endochondral arrest is conserved across mammals, birds and an indeterminately-growing fish.** Zebrafish endochondral zones shut down completely in adults — hypertrophic chondrocytes vanish, no bone deposited at the fronts — while intramembranous growth continues ([32852849](notes/32852849.md)). Arrest is not a mammalian estrogen quirk even though estrogen triggers it in humans.
- **Transdifferentiation conflict.** [25164565](notes/25164565.md) states flatly that there is no evidence of one-step chondrocyte-to-osteocyte transdifferentiation in vivo; [37126720](notes/37126720.md) shows Ku80+ human bone arising from Ku80+ human cartilage. Unresolved, and it bears on whether the bone at the front comes from the cartilage or from invading osteoprogenitors.
- **Rho sign tension.** Rho GTPase signalling is up in the fast jerboa metatarsal and "regulates the size of the hypertrophic chondrocyte zone" ([34793695](notes/34793695.md)), but RhoA/ROCK is reported to promote proliferation and *reduce* hypertrophy ([31787777](notes/31787777.md)). Unresolved.
- **Spine arithmetic rests on an abstract** (16778695) and on a claim cited at second hand (Sanders 2020).
- **Shox2 and the jerboa phenotype are developmental**, driven from limb-bud stages. Nothing shows a postnatal or adult induction works, and genetic Shox2 misexpression *shortens* proximal elements.
- **Crabp1 and Gdf10 knockouts had no detected phenotype** (bone lengths not precisely measured). The de-repression circuit is assembled, not demonstrated.
- **NKCC1-null mice reach normal adult size.** The system is redundant, which is consistent with bumetanide capturing only 35% and needing DIDS to reach 80%.

- **§3b's human validation is developmental, not post-closure.** +1.9 cm from an *STC2* variant accrued over a childhood with open plates. **No evidence exists that manipulating IGF bioavailability after epiphyseal closure does anything at all.** This is the same objection that applies to aromatase deficiency, and it applies with full force here.
- **The growth direction and the longevity direction are opposite on PAPP-A.** *Pappa*-null mice are long-lived with less age-related pathology. Raising PAPP-A activity is raising a validated tumour-promoting axis that the oncology field is actively trying to block, with a sub-nanomolar antibody already built to do so.
- **The KDM6 prediction (§14.7) is mine**, chained from two papers in different cell types and systems. It has not been tested, and GSK-J4 is a promiscuous tool compound.
- **The Weaver mouse has no longitudinal phenotype at all** — normal femur, tibia and body length. So the human overgrowth syndromes (*EZH2*, *EED*, *SUZ12*, *NSD1*, *SETD2*, *DNMT3A*) remain unexplained mechanistically for *height*, and 37450557, the review of that whole class, came back abstract-only.
- **The "severe impairment in post-natal, linear axial skeletal growth" claim is one sentence citing one unread reference.** §13.3c rests on it.
- **§13.3b's hydrostatic-shielding argument rests entirely on unread primaries.** It is the most important untested structural claim in this revision.
- **For 40323130 I read only the abstract**; nothing in §13.3d from it should be weighted more heavily than that.
- **IGF-2, not IGF-1, is the predominant hypertrophic-zone ligand** ([27897169](notes/27897169.md)). The entire GH/IGF-1 literature, and my own §3 and Stage 3, may be naming the wrong ligand.

- **§17's load-bearing claim is unread.** "BMP2 restored the entire length of P2" reaches me through a review citing Yu 2010/2012 and Dawson 2017. P2 is a mouse middle phalanx; the claim is **restoring an amputated segment, not lengthening a normal bone**; and I have not read the primaries. They are Tier 000.
- **The rat two-step regeneration result is unpublished** (one histology figure, no measurements).
- **Every mammalian CCC in this literature follows an amputation or a fracture.** Nothing provokes one without breaking bone. Bioelectrical stimulation of intact periosteum is the only non-destructive candidate and it was one step of an unpublished procedure.
- **Antlers have no joints, no muscle and no load**, are cast and regrown rather than lengthened, and run on a cell population expressing Oct4/Nanog/SOX2/TERT that expands 3.3 million cells into 15 kg in 70 days. The literature does not discuss neoplasia.
- **Androgen withdrawal in a human adult lowers estrogen too**, and the aromatase-deficient men who kept growing were severely osteoporotic. The deer result cannot be read across without accounting for that.
- **The antler's interactive substance is unknown**, stated twice. It is the single most valuable unknown in §17.
- **The sclerostin/Wnt thread is abstract-level only** (27742500, 3351908, 11836356), and the sclerosteosis phenotype is dominated by appositional thickening, skull and mandible — the same appositional-not-longitudinal pattern as the Weaver mouse.
- **PI3K is a programme one can switch off, not on.** The activating direction is a mosaic mutation in a major human oncogene, and "reduced hemihypertrophy" is a pathological overgrowth shrinking toward normal, not evidence anything can exceed normal.

**Carried over from revision 1.**
- **The adult tidemark advance rate is unknown to me** (five papers, Tier 0).
- **"Unweighting accelerates tidemark advancement" is a title, not a reading** (9101369).
- **The poroelastic shield is assumed** (10710186, 14614932, both unread).
- **Piezo1 has opposite signs in the two contexts I chain together** — blocking stretch channels at an articulation turns secondary cartilage to bone ([21600197](notes/21600197.md)); blocking Piezo1 in a callus or plate blocks ossification ([40999873](notes/40999873.md)). My resolution is a hypothesis I constructed.
- **The mechanics contradiction is unresolved**: [37483459](notes/37483459.md) says hydrostatic pressure drives ossification and dynamic compression drives growth; [19540500](notes/19540500.md) and [23009361](notes/23009361.md) say the opposite.
- **Kozhemyakina vs Decker** treated as measuring different terms of the same equation — parsimonious, not established.
- **T3's transcriptional signature in adult human cartilage overlaps 37 OA risk genes.**
- **No one has measured bone length under any agent named in this document.**

**On scope.** This describes a mechanism and the experiments that would test it. It is not a protocol and contains no doses, schedules, combinations or sourcing, for the reasons in [COMPOUNDS.md](COMPOUNDS.md) §8. The specific point worth repeating is §12: an open-loop push on either rate lands in a documented failure mode — a joint full of osteophytes, osteoarthritis, or a cartilage tumour syndrome — and all three have been produced in animals by the agents named above.

---

## 16. The chain, condensed

```
  G = n × h_max          n ≈ invariant (~10,500 cells/day across plates differing 3-7× in rate)
                         h_max = 59% of growth, ~100% of growth MODULATION, 5-fold measured range

  PERICHONDRIAL RIM / GROOVE OF RANVIER   ← STAGE 1  release the border
  Ctsk+ CD44/CD90/Stro-1/CD166 progenitors           HS antagonism (Surfen) · RA antagonism
  CD105+ STRO-1+ Jagged1+ BMPR1a+                    low ERK · ↓Gdf10 · ↓Mab21L2
  PERFUSED (α-SMA-stabilised vessels)                keep gradient STEEP and AXIAL
  walled by the ring of LaCroix                      keep primary cilia intact (columns)
          │
          │  migrates onto the articular surface; Ctsk+ cells rise in adult OA
          ▼
  PROGENITOR POOL                          ← STAGE 2  expand  (the 9% term)
  low ERK → Ihh ×6, PTHrP ↑ → proliferate, hold undifferentiated, resist exhaustion
  cyclic articular shear → FFSS → CREB → Prg4 (doubles the adult pool in a month)
          │
          ▼
  VOLUME ACTUATOR                          ← STAGE 3  THE MAIN EVENT
  phase 1  600→2,000 fl   true hypertrophy
  ────────────────────────────────────────  adult articular deep zone sits HERE (~1,750 fl)
  phase 2  2,000→8,000 fl  SWELLING   ← NKCC1 (membrane trafficking) + AE3   [UNUSED]
  phase 3  8,000→14,000 fl            ← IGF-dependent (IGF-2 is the HZ ligand) [UNUSED]
  jerboa metatarsal reaches 23,000 fl (40× initial)
  directed by laterally restricting matrix channels
  ✗ loop diuretics  ✗ corticosteroids

      ↑ THE GATE (§3b) — what opens phase 3
      local FREE IGF  =  f( IGFBP abundance , IGFBP proteolysis )
                             │                    │
        H3K27me3 directly on │                    │ PAPP-A  → IGFBP-4
        Igfbp3 / Igfbp5      │                    │ PAPP-A2 → IGFBP-3/5
        (PRC2 writes it;     │                    │     ⊣ inhibited by STC1/STC2
         KDM6A/6B erase it)  │                    │
        EZH2 inhibitors = WRONG SIGN              STC2 partial LOF = +1.9 cm in humans
        KDM6 inhibition = predicted right sign    Stc2-KO mice heavier, effect grows postnatally
        (§14.7, untested)                         hSTC1/2 overexpression → impaired postnatal
                                                  linear AXIAL growth
        already moving in adult human tissue: T3 → PAPPA ×2.7-3.4
                                              dasatinib → IGF1 up, IGFBP1/3 down
        price: PAPP-A is an oncology target for INHIBITION; Pappa-null mice are long-lived
          │
          ▼
  ─── CONVERSION FRONT ───────────────────  ← STAGE 4  convert, on schedule
  high ERK (FGF-18) → terminal differentiation
  Piezo1 → YAP/β-catenin → BMP2 + VEGFA   (Sirt1 opens it without force)
  MMP-2/9/13 release matrix-bound VEGF · heparanase releases HS-bound factors
  vessels sprout from the bone collar — the front must abut perfused bone
          │
          ▼
  BONE ADVANCES  →  segment lengthens

  THROUGHOUT:  STAGE 5  shield (contact stress off, fluid oscillation on — the KJD
                        mechanism, 2.4→3.0 mm in adult humans in a year) and CYCLE,
                        because the stages want opposite states, static stimuli adapt
                        away, and differential load is the proposed natural setter of
                        differential cell volume

  COUPLING:   addition ≈ conversion → lengthens
              addition > conversion → osteophyte, enchondroma, exostosis
              addition < conversion → osteoarthritis
              both rates now hang off ONE upstream regulator (ERK), and IHH couples
              chondrogenesis to perichondrial osteogenesis

  HUMAN PROOF: existing exostoses keep growing after the plates close; no new ones form
               aromatase/ERα-deficient men grew into their 4th decade, 190-204 cm,
               with radiographically open knee and pelvic plates
```

```
  AND THE POST-CLOSURE PROGRAMME (§17) — a different architecture entirely

  bone injury  →  PERIOSTEUM divides within 8-24 h  →  CIRCUMFERENTIAL
                                                        CARTILAGINOUS CALLUS
                                                               │
                                          ┌────────────────────┴────────────────────┐
                                     has a PARTNER                          NO partner
                                          │                                        │
                      antler: fused velvet skin  (2 cm/day, >1 m)          INVOLUTES
                      fracture: the opposite CCC (BMP, gap-distance tuned)  (every human
                      digit tip: the nail organ (Wnt)                        amputation
                      stump + BMP2 before involution → ENTIRE BONE LENGTH    stump)
                                          │
                                      BLASTEMA  →  elongation

  release switch: testosterone < 0.5 ng/ml      barrier: interposed loose connective
  (castration starts it in 2 weeks;             tissue + muscle between periosteum
   exogenous T blocks it ~permanently)          and skin — remove it and length returns
```

**Revision 2 in one line: the growth apparatus is held shut by active brakes rather than spent; the rate-setting variable is hypertrophic cell volume and it is almost entirely unused in adult cartilage; the gate on it is local free IGF availability, controlled by an H3K27me3 mark on two binding-protein genes and by a surface protease whose inhibitor costs two centimetres of human height; the addressable compartment is the perfused perichondrial rim rather than the avascular interior; polarity is set by the direction of the morphogen gradient; the best site is probably a vertebral endplate; and one pathway — ERK — moves nearly all of the rest. And after closure specifically, the thing to pull is not a growth gene at all but the periosteal regeneration programme every mammal already runs and then aborts for want of a partner tissue (§17).**

---

## 17. Programs, not genes — the post-closure answer

Every "height gene" in this corpus works through an open physis: *FGFR3*, *NPR2*/CNP, *SHOX*/*SHOX2*, *STC2*/*PAPPA2*, *EZH2*, aromatase. All of them. The question of what works **after** closure is a different question, and it has a different answer: **not a growth gene, but a regeneration programme.**

### 17.1 The circumferential cartilaginous callus — the universal mammalian elongation programme

**Every mammal, including humans, launches an endochondral elongation programme from the periosteum within hours of a bone injury, and then shuts it down.**

- Periosteal cell division is detectable within **~8 hours** of a fracture and peaks at **~24 hours**, forming a **circumferential cartilaginous callus (CCC)** ([37490254](notes/37490254.md)).
- **This happens at every mammalian digit, limb and long-bone stump, including regeneration-incompetent ones, and it is "virtually independent of environmental factors."**
- **And it is short-lived. Without an interactive partner tissue the CCC involutes and the stump returns to its original form.**

| System | Partner | Substance | Outcome |
|---|---|---|---|
| **Deer antler** | enveloping velvet skin, **fused** to the pedicle periosteum | **unknown** | full regeneration, **up to 2 cm/day, >1 m, 15 kg from 3.3 million cells in 70 days** |
| **Fracture** | the opposite CCC | **BMP** | bridging callus, union |
| **Digit tip** | the nail organ | **Wnt** | tip restored |
| **Limb/digit stump** | **none** | — | **CCC forms, then involutes** |

**The human experiment that settles it.** One patient: a tibial fracture on one side, an amputation at approximately the same level on the other. **At six weeks both sides had formed CCCs. The fracture side had begun a bridging callus toward its partner; the amputation-stump CCC "was apparently inert even though it could be regarded as one side of a fracture."** Same person, same time, same periosteum. One had a partner. One did not.

**And this is the general rule the whole document has been circling.** Six systems, one architecture — in every case a single domain alone stalls or involutes, and juxtaposition sustains growth:
- chondro-spheroid + osteo-spheroid → a growth plate at the interface, in neither alone ([40118845](notes/40118845.md))
- perichondrium + de-restricted Ihh/BMP gradient → an organised ectopic plate ([23821404](notes/23821404.md))
- articular cartilage + calcified cartilage at the tidemark ([25603997](notes/25603997.md))
- CCC + opposite CCC → bridging callus
- CCC + nail organ → digit tip
- CCC + fused skin → an antler
**"The boundary" is not a device of this document. It is how mammalian skeletal growth works outside a physis.**

### 17.2 What humans are missing is a partner, not a capacity

**Stage 1 is intact in humans. Stage 2 is blocked, and the block is anatomical.**
- In a rat stump, "throughout the entire course of wound healing… the distal periosteum/CCC and the enveloping skin are separated by **multiple layers of muscle and loose connective tissue**." Goss argued this interposed layer — "the pad", "the dermal barrier" — is **the cause, not the consequence**, of regeneration failure, physically blocking inductive communication.
- In the deer pedicle, the periosteum and the skin are **almost fused over the distal third — the antler-regeneration region — and only loosely associated over the proximal two-thirds, the non-regeneration region.** An impermeable membrane inserted at the **fused** distal third did **not** prevent regeneration (a skin-less antler grew under a scab); inserted at the **loose** proximal region it **abolished** regeneration although CCCs still formed.
- **This is the soft-tissue version of the perichondrium's anti-chondrogenic heparan-sulfate border (§8).** Two literatures, two tissues, one conclusion: **the adult mammal maintains a barrier that blocks inductive communication, and growth resumes when the barrier is removed.**
- **And removing it works.** A two-step rat procedure — **(1) bioelectrical stimulation to the distal periosteum immediately after amputation** to enhance the CCC, then **(2) surgical removal of the interposing connective tissue and muscle, holding periosteum and skin tightly together** — induced blastema formation and **partial stump regeneration in which "the length of the regenerates was significantly longer than their width."** (Reported as unpublished, one figure.)

### 17.3 The partner is substitutable by an approved compound

> **"In the regeneration-incompetent digit/limb stump, the blastema can be induced by topical application of BMP2 to the CCC *before its involution*, and this induced blastema has the potential to regenerate the entire length of P2."**

**BMP2 substituted for the missing partner and restored the full length of a bone in a mammal** (cited to Yu 2010/2012 and Dawson 2017). It restored bone length **but not the joint or the distal P3 element**. The mechanism was **not more signal but longer signal** — BMP "enhanced the endogenous response by **extending the period of BMP2 signalling**." Periosteal-derived BMP2 is likewise required for the bridging callus after fracture.

**rhBMP-2 is a licensed human product.** This is the first thing in the entire project that is simultaneously **(a) post-closure, (b) about length, (c) in a mammal, and (d) deliverable with an existing clinical agent.**

**The qualifiers are real and I am not going to bury them.** P2 is a mouse middle phalanx — a millimetre-scale bone. "Restoring the entire length of P2" after amputation means **replacing a removed segment, not making a bone longer than it was.** It is regeneration, not augmentation. **I have not read the primaries** (Yu 2010/2012, Dawson 2017), and they carry the whole claim; they are now Tier 000 of [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md). And BMP2 in soft tissue is the heterotopic-ossification mechanism ([28629737](notes/28629737.md), [28645539](notes/28645539.md)) — in a primed adult, a 5 mm skin cut was a sufficient trigger.

### 17.4 The release switch is androgen withdrawal, at a threshold

The antler cycle is not triggered by injury. **Casting and regeneration are not causally related** — new antlers grow even when the old ones are screwed in place, and autumn trauma triggers nothing.

- **"Antler regeneration is strictly under control of androgen hormones… triggered by the *low* threshold level of circulating androgen."**
- **Castration at any point in the hard-antler phase → antlers cast within two weeks and regeneration begins immediately. Exogenous testosterone inhibits both casting and regeneration "relatively permanently."**
- The threshold given is **< 0.5 ng/ml testosterone**: wounding "potentiates" the periosteum, and **the fall in androgen "releases the brake."**

**That is the sixth independent instance of the de-repression frame** — after heparan sulfate / perichondrium, Crabp1-Gdf10 / retinoic acid, ERK / SHP2, PRC2 / IGFBP, and STC2 / PAPP-A. And **every clinically relevant androgen lever is an approved drug class** (GnRH agonists and antagonists, AR antagonists).

**Read it against the human aromatase data and the two point the same way.** In deer, lowering androgen *releases* the periosteal growth programme. In humans, estrogen — aromatised from androgen — is what closes plates, and men who cannot make or sense it were **still growing at 38, at 190–204 cm, with radiographically open knee and pelvic plates** ([24485503](notes/24485503.md)). **Lowering androgen signalling lowers both.** The cost is also the same in both: hypogonadism means bone loss, muscle loss and metabolic change, and the osteoporosis of the aromatase-deficient men was severe.

### 17.5 The cells, and why deer get away with it

Three antler stem cell populations: **antlerogenic periosteum** (first pedicle), **pedicle periosteum** (annual regeneration), and **reserve mesenchyme cells** — an apical undifferentiated pool feeding the growth zone, i.e. **the antler's resting zone, positioned at a free end and fed by periosteum rather than enclosed between two ossification centres.**

Pedicle periosteum cells express **CD73, CD90 and CD105** — *the same markers as the groove-of-Ranvier progenitors* ([25164565](notes/25164565.md)) and the Ctsk+ chondroid progenitors ([25003010](notes/25003010.md)) — **and also Oct4, Nanog, SOX2, TERT and nucleostemin.** "An intermediate cell type between adult and embryonic stem cells." **Position is set by where the periosteum is**: total removal abrogates regeneration, removing only the distal third gives an antler growing from the cut end of the residual periosteum, away from the natural site.

**And the programme is transferable as a reagent.** Antler stem cell injection or **topical conditioned medium** heals wounds in rats; **cell-free** preparations repair bone defects in rabbits; and **extracellular vesicles from antler blastema progenitor cells, given intravenously to aged mice and rhesus macaques, raised femoral BMD, improved physical and cognitive function, and reduced epigenetic age by >3 months in mice and >2 years in macaques** (40660003, abstract only — recorded in [37490254](notes/37490254.md)). That is BMD and ageing, not length — but it establishes that the programme's outputs survive isolation, injection and a species jump into a primate.

**Why this cannot simply be copied.** Deer have a dedicated permanent pedicle, a dedicated stem cell population with partial embryonic character, velvet skin physically fused to the periosteum, and a seasonal hormonal cycle built around all of it. **Antlers have no joints, no muscles, bear no load, and are cast and regrown rather than lengthened.** And a cell population expressing Oct4/Nanog/SOX2/TERT that goes from 3.3 million cells to 15 kg in 70 days is, in any other context, a description of tumour risk — which the literature does not discuss.

### 17.6 Two further programmes worth naming

- **PI3K–AKT.** *PIK3CA* gain-of-function causes **progressive postnatal segmental overgrowth** including skeletal overgrowth and hemihypertrophy. **BYL719 (alpelisib, now licensed as Vijoice) improved symptoms in all 19 PROS patients treated, reducing hemihypertrophy and attenuating scoliosis, without substantial side effects** ([29899452](notes/29899452.md)). So PI3K–AKT is a **drug-controlled, postnatal, progressive skeletal overgrowth programme**, demonstrated bidirectionally in humans — one direction by a mosaic oncogenic mutation, the other by an approved inhibitor. It also connects to the corpus: *Acvr1*^R206H drives heterotopic ossification partly through PI3K/mTOR, and mTOR and PI3K inhibitors reduce HO ([38672135](notes/38672135.md)).
- **Sclerostin / Wnt.** *SOST* loss of function (sclerosteosis, van Buchem disease) causes **progressive skeletal overgrowth continuing through adult life**, with tall stature reported, mandibular overgrowth and increased head circumference. Sclerostin is the secreted Wnt inhibitor made by **osteocytes — the mechanosensing cell — and loading suppresses it**. **Romosozumab is an approved anti-sclerostin antibody.** This connects to the corpus at three points: postnatal β-catenin ablation produces exostosis-like masses off the growth plate and in periosteum, HME osteochondroma cartilage is β-catenin-negative ([23821404](notes/23821404.md)); **DKK1 inhibition with WAY262611 increased condylar cartilage volume** ([42650460](notes/42650460.md)); and Wnt/β-catenin is enriched and activated in the fast-elongating jerboa metatarsal ([34793695](notes/34793695.md)). **The honest caution: the sclerosteosis phenotype is dominated by appositional thickening, skull and mandible — the same appositional-not-longitudinal pattern as the Weaver mouse (§3b) — and I have read only abstracts here** (27742500, 3351908, 11836356 all came back abstract-only or stubs).

### 17.7 What this changes

Revision 2 said: release the brake on an existing border, let the perichondrial rim form the interface, drive the volume actuator, cycle ERK. **§17 says the border and the rim are not the only option, and may not be the best one.** The alternative programme is:

> **Provoke a CCC from periosteum at a chosen site; give it a partner before it involutes; and keep the androgen brake off.**

Its advantages over everything else in this document are that **Stage 1 already works in humans**, that the deficiency is a **physical barrier** rather than a missing capacity, that the partner is **substitutable by a licensed agent**, that the **timing window is defined** (before involution), that **position is set by where the periosteum is**, and that the **output is length** — "significantly longer than their width" in the one experiment that produced it.

Its disadvantage is that **every instance of it in a mammal began with an amputation or a fracture.** The CCC is a response to bone injury. Nothing in this literature provokes one without breaking something — which is why **bioelectrical stimulation of intact periosteum** (§17.2) and the search for a non-destructive CCC trigger remain open questions. §18 adds the layer this section was missing: a programme that builds skeleton still needs to be told *how much* to build.

---

## 18. Goal changers — positional identity as the lever

§17 asked what *programme* builds skeleton outside a physis. This section asks a different and larger question: **what sets how much skeleton the body thinks it should have?** Growth-rate genes answer "how fast"; this answers "how much" — and it is the only axis in the project where a compound has been shown to make an animal build an *additional skeletal segment*.

### 18.1 The thing that exists: positional identity

Loose connective-tissue cells carry a stable record of where in the body they are. In salamanders this is the substrate of regeneration: confront cells of different positional value and they proliferate and intercalate the missing pattern between them. Three results make this relevant rather than exotic.

**(a) It is a chemical property of matrix, not a cell state.** Decellularized axolotl limb skin ECM carries it. Anterior ECM grafted into an anterior wound **abolished blastema formation in 8/8**; posterior ECM into the same wound induced jointed, tapered phalanx-like elements in 30%. Heparin lyase III lifted the anterior block completely. An **artificial matrix of nothing but Sigma type-I collagen and Sigma porcine heparan sulfate** induced complex jointed skeletal patterns in **8/19 (42%)** of blastemas at 5 mg/ml HS — and in **0/6** with collagen alone, **0/5** at 10 mg/ml ([27499874](notes/27499874.md)). The code is the sulfation pattern of heparan sulfate, written by NDST1/2, HS6ST1, HS2ST1, HS3ST1/2/3a and erased by SULF1/2.

**(b) It exists in mammals.** Mouse hindlimb skin ECM, grafted into an axolotl wound, induced skeletal elements position-specifically and HS-dependently: **PN3–4 posterior 37%, PN5–7 posterior 60%, anterior 0–18%**, abolished by heparin lyase III. The axolotl cells built *Alizarin-Red-positive calcified* elements rather than their native cartilage — the mammalian matrix imposed the mammalian fate ([27499874](notes/27499874.md)).

**(c) It can be rewritten by a compound, permanently.** Retinoic acid applied to an axolotl blastema reprograms positional memory, and the reprogramming is **heritable through a second regeneration**: RA-induced ectopic structures, re-amputated, regenerated — 94% to the same pattern, 6% to a *more* complex one — and skin grafted from them induced new structures in fresh wounds. Shh and FGF-8 supply a positional *cue* that produces structures which **fail both tests** ([31026439](notes/31026439.md)). RA is, as of this literature, the only molecule that stably rewrites the record.

### 18.2 The result that matters most

A **7-day exposure to a CYP26 inhibitor, dissolved in water, scored 120 days later, made distally amputated axolotl limbs regenerate an entire extra proximal limb segment, dose-dependently** ([40494878](notes/40494878.md)):

| Talarozole | Distally amputated limbs |
|---|---|
| 0.1 µM | **92.3% duplicated a zeugopod** (61.2% whole, 30.1% partial) |
| 1 µM | **100% duplicated a stylopod** (66.7% full, 33.3% partial) |
| 5 µM | 92.3% failed to regenerate |

The mechanism is degradation, not supply: RARs, RALDHs and RA synthesis are not graded along the proximodistal axis — **CYP26B1** is, and it sets local RA. Inhibiting it raised RA reporter signal, erased the HOXA13 reporter, and shifted the distal transcriptome toward the proximal one. Co-treatment with a RALDH inhibitor or a pan-RAR antagonist abolished the gain, so the effect runs through RA and RAR.

**Talarozole (R115866) has been through human Phase II.** This is the only place in the whole project where a drug that has been in people changed the amount of skeleton an animal built.

### 18.3 SHOX — where this touches human height

The RA-responsive effector is **Shox**, downstream of Meis1, mutually exclusive with Hoxa13, restricted to the proximal mesenchyme ([40494878](notes/40494878.md)).

- *Shox* crispants and *Shox*−/− axolotls: **shortened stylopod and zeugopod, autopod unaffected.**
- Their proximal chondrocytes **"failed to proliferate, appearing to remain as reserve cartilage through adulthood"** and never calcified — while digit chondrocytes in the same animals ossified normally.
- Shox is **dispensable for regeneration** and does not set positional identity (Meis1 and Hoxa13 are unchanged in its absence). It *executes* a positional instruction.
- In humans, *SHOX* haploinsufficiency is the cause of **Léri-Weill dyschondrosteosis, the short stature of Turner syndrome, and a measurable fraction of idiopathic short stature.**

Two things follow, and they are the reason this section exists.

**First, SHOX is a permission signal for reserve cartilage to enter the growth programme — and §4 of this document argues that is exactly where adult cartilage is stuck.** Adult articular deep-zone chondrocytes sit at ~1,750 fl, having finished true hypertrophy and never begun swelling. The *Shox*-null phenotype is the same arrest, described independently, in a different animal, by authors not thinking about adults: cartilage that stays reserve cartilage for life. The gate I inferred from cell volumes has a candidate name, and the name is RA-responsive.

**Second, it is proximally biased.** Shox governs stylopod and zeugopod and not autopod; proximal and distal endochondral ossification run on separate transcriptional programmes. A height strategy wants precisely that bias — long bones and, if it extends axially, vertebrae — rather than acromegaly's hands, feet and jaw. This is the first lever in the project with a *built-in* anatomical selectivity pointing the right way.

### 18.4 The architecture: competence, then goal

Across four papers the same two-step structure appears, and neither step works alone.

| | Step 1 — competence | Step 2 — goal |
|---|---|---|
| Axolotl ALM | FGF-2 + FGF-8 + BMP-2 (replaces the nerve) | RA → complete limb, 52% ([31026439](notes/31026439.md)) |
| Positional ECM | nerve-deviated blastema | HS sulfation state ([27499874](notes/27499874.md)) |
| Reindeer velvet | CRABP1+ fibroblast ground state | threshold of network activity ([36493752](notes/36493752.md)) |
| CYP26 inhibition | amputation blastema | talarozole dose ([40494878](notes/40494878.md)) |

**Mature tissue is refractory to step 2.** RA changed Alx4 and Shh in blastemas and left mature limb tissue untouched at both timepoints. Positional rewriting requires an already-activated cell. The gate on the goal changer is competence — which is the same conclusion §17 reached from the callus literature and the reindeer paper reached from fibroblast ground states.

### 18.5 CRABP1 — three literatures, one gene

| Source | Finding |
|---|---|
| Reindeer velvet vs back skin | **CRABP1** the top marker of the regeneration-competent fibroblast; **82% of fetal human** vs **10% of adult human** fibroblasts; absent from adult human interfollicular dermis ([36493752](notes/36493752.md)) |
| Axolotl regenerative vs flank wounds | **crabp1** significantly higher in regenerating wounds, and **nerve-dependent** (Monaghan 2012, via [31026439](notes/31026439.md)) |
| Fastest-elongating mammalian bone | **10.6× more Crabp1**, 9.3× less of the RA-induced inhibitor **Gdf10** ([23821404](notes/23821404.md)) |

CRABP1 is a cytosolic retinoic-acid binding protein — it controls how RA reaches the nucleus. Three unrelated literatures, examining regenerative skin, regenerative limbs and fast bone elongation, independently converge on the same RA-handling gene as the marker of the competent state. That is the strongest unforced convergence in the project, and it says the competence step and the goal step are not two systems but one.

### 18.6 The length-generating rule is intercalation, not proximalization — a correction

I framed §18.1–18.3 as "proximalize and gain length." That is wrong as stated, and [35241664](notes/35241664.md) is what corrects it.

**Tig1/Rarres1** is the conserved cell-surface determinant of proximal identity: RA-inducible, graded proximally in the mature limb, membrane-bound, **57% identical to human TIG1**, self-amplifying, and antibody-neutralisable. Overexpressed in cells already specified distal, it upregulates Prod1 and Meis1 and shuts down Hoxa13 and eleven of its targets. It is a genuine positional reprogrammer. And **overexpressing it shortened the regenerated limb** (p = 0.0014) — fused digits, malformed carpals, lower arm and hand significantly shorter, upper arm unchanged.

Not a contradiction with §18.2; the same rule at two timepoints:

| Manipulation | Timing | Result |
|---|---|---|
| RA, talarozole | early distal blastema | field believes it is proximal → **intercalates a whole extra segment**, more length |
| Tig1, Prod1 | from mid-bud, while distal elements are being built | suppresses the distal growth programme (Fgf8, Lhx2, Bmp2/7) → **those elements fail**, less length |

**Length comes from intercalation across a positional gap, not from the proximal value itself.** Apposed cells of disparate positional value proliferate and generate the intervening values; that is the only length-generating rule in this literature. Two further facts point the same way: Tig1 and Prod1 are both **anti-proliferative**, and the proximal-most late blastema proliferates least — so stable proximal identity may be intrinsically growth-suppressing. Uniform proximalization of a whole field creates no gap and should do nothing or worse.

**So the target is not "raise the positional value." It is "install a positional disparity inside a competent field and let the tissue fill it."** That is a different and more specific proposition than §18.3 implied, and it is what the ALM does surgically (graft opposite-axis tissue) and what RA does pharmacologically (rewrite a subpopulation, creating a gap against its neighbours).

### 18.6b The complete rule: growth = positional disparity × permission

[17975060](notes/17975060.md) supplies the missing half. **nAG**, a secreted Anterior Gradient protein, is the **ligand for Prod 1** — the positional determinant is also the growth receptor. nAG appears in distal nerve-sheath Schwann cells at day 5 and wound-epidermis glands after day 10, and **denervation abolishes both**. Electroporating nAG into a **denervated** newt stump rescued regeneration to digit stage in **half the animals, versus 0 of the vector controls**, without restoring innervation — a single protein substituting for the nerve. On blastemal cells (70% surface-Prod 1+) it drove S-phase entry **8.3 ± 3.3-fold** across 8 experiments.

The authors state the division of labour: "PD identity is manifested by the quantitative gradation of Prod 1, and **nAG has no role in specifying that identity but acts through Prod 1 to promote cell division**." And the condition: "Blastemal growth is stimulated in experimental confrontations of cells differing in positional identity … and **this is always dependent on the presence of the nerve**."

**Growth = positional disparity × permission signal. Neither alone.** Permission into a positionally uniform field gives proliferation without pattern — the ALM's "bump." Disparity without permission gives nothing. This sharpens §18.4: the two steps are not merely sequential; **the permission ligand signals through the positional determinant itself.**

**A named mammalian candidate pair.** Human **AGR2** (secreted, the AG-family counterpart of nAG) complexes with **LYPD3/C4.4A** — a GPI-anchored protein with two Ly6/uPAR-type domains, the same superfamily as Prod 1. The authors' inference: "functional interactions between AG proteins and this class of small Cys-rich protein domains may be conserved." Both are real, well-characterised human genes; AGR2 is secreted and LYPD3 has antibodies against it. **This is the project's first named, molecularly specific mammalian candidate for "permission to build a structure."** It is an inference from domain relatedness, not a demonstrated mammalian function — and Prod 1 itself is salamander-specific, which is why [35241664](notes/35241664.md)'s conserved, membrane-bound **TIG1/RARRES1** matters more as the positional side.

Also relevant: **Prod 1 is expressed by dermal fibroblasts and is retinoic-acid inducible.** The positional *receptor* level is RA-tunable, which puts the CYP26 route (§18.2) upstream of both halves of the rule.

### 18.7 Does the mammal have the substrate? Yes, with one hard limit

[16895450](notes/16895450.md) — 47 primary fibroblast populations from **43 anatomic sites across the adult human body**, every culture passaged five or more times in identical medium to strip the environment away.

**What survives in adult humans:**
- Positional identity is cell-autonomous and stable in culture; **anatomic origin beat donor identity** — cells grouped with the same site from other people rather than with their own donor.
- **337 positional-identifier genes clustered 47/47 samples into clusters composed purely of anatomic neighbours** (p = 0.00017; 7 SD from random), and correctly placed 10/10 samples from an independent panel including three untrained sites.
- A proximal–distal signature in both limbs (upper 7/7 distal, p < 0.01; lower 3/3 vs 3/3, p < 0.025), with a boundary at the **embryonic autopod**, and a **98-gene "distal" signature shared between hand, foot and foreskin** — spatially distant tissues with no shared local interactions.
- **HOXA13 protein present in foot fibroblasts and foreskin, absent from thigh fibroblasts**, with ~one third of foreskin dermal fibroblasts nuclear-HoxA13+ in vivo. **This is the exact boundary talarozole moves** — the gene whose reporter it erased, the gene mutually exclusive with *Shox* — demonstrably present and position-specific in adult human tissue.
- **HS3ST3B1** (a heparan sulfate 3-O-sulfotransferase) and **GPC6** (an HSPG) are among the 337. The amphibian work says HS sulfation *is* the positional code ([27499874](notes/27499874.md)); adult human fibroblasts vary an HS sulfotransferase with position. Unforced convergence.
- Maintenance is chromatin-based (HOX loci differentially modified site-specifically).

So **lock 2 is better described as a reading-and-writing problem than an erasure.** The matrix-borne HS code dies by mouse PN9; the record inside adult human cells does not.

**The hard limit:** the adult human proximodistal code, as measured, is **binary — autopod vs everything else.** Explicit multiclass search found **no stylopod/zeugopod signature** in either limb, and **"we also did not find genes that were expressed in fibroblasts according to a gradient along the limbs."** Intercalation needs intervening values to generate. A graded axolotl limb has a continuum; an adult human limb, on this evidence, has one boundary.

This is the most serious constraint in §18 and it comes from the best mammalian data available. The authors offer three readings and decline to choose: **underpowered** (their words: the result "does not rule out the possibility there may be finer segmentation or a gradient," and the proximodistal comparisons rest on 6–7 samples per limb on 2006 cDNA arrays); **wrong cell type** (the finer code may sit elsewhere or need heterotypic interaction); or **genuinely sparse in adulthood**. The third reading would be close to fatal for this route in humans. **Settling which is true is now the single highest-value experiment in the project** (§14.10).

### 18.7b Two closures, and a chromatin tension

Growth-plate fusion is not the first lock. There are at least two, on different schedules:

1. **No responsive template** — the cell-volume actuator has no substrate (§3, §4).
2. **No positional instruction being acted on** — the matrix-borne code is gone (mouse PN9), the cellular record persists but is binary and quiescent (§18.7).

Everything in COMPOUNDS.md and §§2–16 addresses lock 1. A compound that opens the actuator in tissue acting on no positional instruction should produce thickness, nodules and disorganised mass — which is what the failures in this literature produce, and what the ALM's bulbous masses were.

**And the two locks may share a keeper.** Positional identity is maintained by chromatin at HOX loci; §3b's IGF gate is maintained by PRC2/H3K27me3 at *IGFBP3/5*. **This is a tension, not a win.** PRC2 loss derepresses IGFBP3/5 and *shrinks* hypertrophic cells — the sign error I corrected in COMPOUNDS.md. A PRC2 inhibitor would be correctly signed for releasing positional identity and wrongly signed for the volume gate. Any epigenetic approach has to discriminate between these two loci rather than act globally.

### 18.8 Honest placement

This is the most promising *mechanism* the project has found and it is further from a human intervention than anything in §§2–16, because its entire evidentiary base sits in a blastema. It belongs here as the answer to "what sets the goal," not as a route anyone can take. The compound that matters — talarozole — has human safety data and no skeletal indication, no cartilage pharmacokinetics, and an axolotl-only efficacy record. I am not writing a regimen (§8 of [COMPOUNDS.md](COMPOUNDS.md) still holds and holds for this section specifically).

---

*Built from 109 full texts read in full, notes in [notes/](notes/). Untested. The newest and least-settled section is §18. The two most load-bearing unread papers are 8982136 (the 59/32/9 partition) and 10614657 (RA inhibition accelerating elongation), both Tier 00 of [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md).*
