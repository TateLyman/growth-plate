# Activating the boundary: the least-complex route — revision 2

How to switch on a longitudinal growth interface in an adult, in situ. Third document in the series, after [THEORY.md](THEORY.md) (mechanics) and [COMPOUNDS.md](COMPOUNDS.md) (pharmacology). Built from 94 full texts read in full, notes in [notes/](notes/).

**Revision 2** follows a round of reading aimed specifically at strengthening, confirming and raising the ceiling of revision 1. It changes the emphasis, the molecular chain, the anatomical target and the arithmetic. §1 is the changelog; revision 1's core claim — that the apparatus exists and is held shut rather than absent — survives and is now much better supported.

---

## 0. The answer in one paragraph

**Longitudinal growth rate in a postnatal mammal is set almost entirely by how large hypertrophic chondrocytes get, not by how many there are.** Four growth plates in one rat, at one moment, elongating at rates differing 3–7×, produce **the same ~10,500 new chondrocytes per day each**; what differs is hypertrophic cell volume, which ranges **4,000 → 20,000 µm³** and correlates with elongation rate at **r = 0.70**, while cell production correlates at r = 0.35, non-significantly ([18404738](notes/18404738.md)). Across an eight-fold range of growth rate, **cellular enlargement contributes 59% of axial growth, matrix synthesis 32% and proliferation 9%**, and accelerated growth is "almost exclusively" enlargement ([32852849](notes/32852849.md)). That enlargement is an **osmotic pump with named parts**: IGF-1 licenses its final phase, **NKCC1 (SLC12A2)** traffics to the plasma membrane immediately before the cell swells, **AE3 (SLC4A3)** rises 14-fold alongside it, and blocking NKCC1 with bumetanide removes **35% of longitudinal growth while leaving hypertrophic cell number unchanged to three significant figures** ([20200963](notes/20200963.md), [23485973](notes/23485973.md)). **Adult articular deep-zone chondrocytes are stuck at roughly 1,750 µm³ — they have finished true hypertrophy and never begun swelling, leaving phases 2 and 3 entirely unused** (§4). One pathway — **ERK** — simultaneously sets progenitor proliferation in the groove of Ranvier, Ihh/PTHrP output, cell size, hypertrophic-zone depth and the gate to terminal conversion, and it has existing drugs on both sides ([25003010](notes/25003010.md), [24875294](notes/24875294.md)). And the thing being overcome is not exhaustion but **active restraint**: the perichondrium is a maintained anti-chondrogenic border made of heparan sulfate, and the fastest-elongating mammalian bone known gets that way partly by **releasing brakes** — 10.6× more retinoic-acid-sequestering Crabp1, 9.3× less of the RA-induced inhibitor Gdf10 ([23821404](notes/23821404.md), [34793695](notes/34793695.md)).

**So the revised answer: do not try to make more cells, and do not try to build a plate. Release the brake on an existing border, let the resident progenitors of the perichondrial rim form the interface where the gradient already points along the bone's axis, and then drive the volume actuator through phases 2 and 3 while cycling ERK to convert the bottom of the stack to bone.**

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
  phase 3  8,000→14,000 fl            ← IGF-1-dependent                      [UNUSED]
  jerboa metatarsal reaches 23,000 fl (40× initial)
  directed by laterally restricting matrix channels
  ✗ loop diuretics  ✗ corticosteroids
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

**Revision 2 in one line: the growth apparatus is held shut by active brakes rather than spent, the rate-setting variable is hypertrophic cell volume and it is almost entirely unused in adult cartilage, the addressable compartment is the perfused perichondrial rim rather than the avascular interior, polarity is set by the direction of the morphogen gradient, and one pathway — ERK — moves nearly all of it.**

---

*Built from 94 full texts read in full, notes in [notes/](notes/). Untested. The two most load-bearing unread papers are 8982136 (the 59/32/9 partition) and 10614657 (RA inhibition accelerating elongation), both Tier 00 of [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md).*
