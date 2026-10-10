# Compounds and existing agents that could plausibly produce centimetre-scale longitudinal growth after growth-plate closure

A research document, built from full texts I read myself. One note per PMID in [notes/](notes/). Companion to [THEORY.md](THEORY.md) (the mechanical route), [ACTIVATION.md](ACTIVATION.md) (the least-complex way to switch the boundary on, which is where the agents named here are actually placed) and [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md) (what I could not reach).

**What this is.** Named, existing agents and approaches, organised by the node in the growth mechanism each one touches, with the species and skeletal age of the evidence, the magnitude it actually produced, and what kills it. The question it answers is the one you set: *not* a stack, *not* millimetres — plausible existing things that could cause centimetre-scale adult longitudinal gain.

**What this is not.** Not a protocol. There are no doses on a schedule, no sequencing, no sourcing, and no combination to take. Where I quote a concentration it is the concentration used in the cited experiment, reported so the claim can be checked. I am not going to write a regimen for someone to take for height, and I say why in §8.


> **Revision note (added after the volume-actuator reading round).** Section 2 of this document — "the proliferation wall" — is factually correct but **strategically mis-weighted**, and [ACTIVATION.md](ACTIVATION.md) rev. 2 §1–2 explains why. In a postnatal mammal, **cellular enlargement contributes 59% of axial growth, matrix synthesis 32% and proliferation 9%**, and growth-rate *modulation* is almost entirely enlargement ([32852849](notes/32852849.md)); four rat growth plates elongating at rates differing 3–7× produce **the same ~10,500 new chondrocytes per day each**, with hypertrophic cell volume correlating with rate at r = 0.70 and cell production at r = 0.35, non-significantly ([18404738](notes/18404738.md)). **So the agents below were being judged against the wrong variable.** None of those papers measured hypertrophic cell volume. Two further corrections: the RARγ mirror hypothesis in **Node E is confirmed** — pharmacological inhibition of retinoic-acid signalling accelerates rat metatarsal elongation, and the fastest-elongating mammalian bone has 10.6× more RA-sequestering Crabp1 and 9.3× less of the RA-induced inhibitor Gdf10 ([34793695](notes/34793695.md)); and the proliferation wall itself has a named exception — lowering ERK in Ctsk+ groove-of-Ranvier progenitors causes **excessive proliferation** ([25003010](notes/25003010.md)), so the wall was a property of the cells being addressed (mature articular chondrocytes), not of adult cartilage.


---

## 0. The short answer

**No compound in existence will do this on its own, and the reason is specific, measurable, and the same in every paper I read: adult longitudinal growth is limited by chondrocyte *number*, and every safe compound that acts on adult cartilage raises matrix synthesis while leaving cell number flat or lowering it.**

The best human evidence is the ceiling. **Sprifermin** (recombinant FGF-18) is the only compound ever shown in a randomised placebo-controlled trial to increase the thickness of adult human cartilage in vivo. Injected straight into the knee, three weekly doses every six months, the two-year gain was **+425 µm** — four hundred micrometres, summed across sixteen subregions of one joint, and largest in the *lateral* compartment where load is lowest ([26138203](notes/26138203.md)). Every approved drug that increases human height — vosoritide +1.57 cm/yr, navepegritide +1.49 cm/yr, infigratinib +1.74 cm/yr, the two-drug COACH combination +2.74 cm/yr — is labelled, dosed and discontinued on the presence of **open epiphyses**, and vosoritide's own guidance says to stop at documented closure ([42650460](notes/42650460.md)).

**What does clear your bar is not a compound. It is a boundary.** Fuse a hypertrophy-resistant cartilage spheroid to an ossification-committed one, and a polarised growth plate assembles itself and elongates at **0.61 mm per week — about 3 cm a year — per interface** ([40118845](notes/40118845.md)). The authors call it "cell-autonomous." It does not form in either spheroid alone. That is two orders of magnitude above anything a drug has done to adult tissue, and it comes from architecture, not pharmacology.

So the honest framing of the compound question is: **compounds are not the cause, they are the control system.** They can hold one domain in a cartilage state, set the throughput at the conversion front, substitute for mechanical load, and unlock an aged epigenome. They cannot supply the cells or the geometry. Sections 4 and 5 name the ones worth taking seriously on that basis; §7 names the one unresolved lead that could change this answer.

---

## 1. The magnitude table

Everything measured in a dimension, in one place, newest evidence first. This is the table the whole document turns on.

| Intervention | What it is | Species / skeletal age | Measured gain | Source |
|---|---|---|---|---|
| **Two-domain osteochondral fusion** | hPSC SOX9+ sclerotomal progenitors; hypertrophy-resistant chondro-spheroid fused to ossification-committed osteo-spheroid | Human cells, ectopic in mouse kidney capsule | **0.61 mm/week ≈ 3 cm/yr per interface**; 0.55 → 2.43 mm in 4 wk; aspect ratio 1.0 → 1.4 | [40118845](notes/40118845.md) |
| COACH combination | navepegritide + lonapegsomatropin, weekly | Children 2–11, **open plates** | 8.69 vs 5.95 cm/yr = **+2.74 cm/yr** | [42650460](notes/42650460.md) |
| Infigratinib | oral FGFR1–3 TKI | Children 3–17, **open plates** | **+1.74 cm/yr** | [42650460](notes/42650460.md) |
| Vosoritide | CNP analogue, daily s.c. | Children, **open plates**; stopped at closure | **+1.57 cm/yr**, ~3.5 cm at 2 yr | [42650460](notes/42650460.md) |
| Navepegritide | long-acting CNP, weekly | Children ≥2, **open epiphyses** | **+1.49 cm/yr** | [42650460](notes/42650460.md) |
| Knee joint distraction | 6 weeks external distraction | **Adult humans** | **+0.6 mm/yr** cartilage thickness; no demonstrated bone-front advance | [21565898](notes/21565898.md) |
| **Sprifermin** | intra-articular FGF-18 | **Adults, mean age 61** | **+425 µm** thickening score at 24 mo (16 subregions summed); +237 µm at 12 mo in the earlier trial | [26138203](notes/26138203.md) |
| Meclizine | repurposed oral, FGFR3–RAS–ERK | Children on GH | 4.35 → 4.46 cm/yr = **+0.11 cm/yr** (no efficacy) | [42650460](notes/42650460.md) |
| Recifercept | soluble FGFR3 decoy | Children | **zero at every dose; programme terminated** | [42650460](notes/42650460.md) |
| Palovarotene | RARγ agonist, daily | Juvenile mice | **−13% to −19% tibial length**, plate ablated in 7/9 | [30226468](notes/30226468.md) |
| Modulus-matched pillar scaffold | DLP-printed PEG pillars + cartilage hydrogel | Injured rabbit physis | "**significantly greater limb growth** than other treatment options" (number not given in the review) | [37483459](notes/37483459.md) |

Two things fall out immediately. **Everything pharmacological that produced centimetres required an open plate.** And **everything acting on existing adult tissue produced hundreds of micrometres.**

---

## 2. The invariant: the proliferation wall

I did not go looking for this. It appeared independently in every compound paper I read, and it is the single most important finding of the compound phase.

| Agent | Matrix / anabolism | Cell number | Source |
|---|---|---|---|
| T3, 10 ng/ml, adult human articular explants | COL2A1 **+6.4×**, ACAN up, CCDC80 +9.7×, CLEC3A +14.6× | not increased; COL10A1 **down** 3.9× | [38664820](notes/38664820.md) |
| Dasatinib ± quercetin, human chondrocytes + explants | COL2A1 **~30-fold**, ACAN, SOX9, GAG, COL2 protein up | **Ki-67 down**, growth rate down, cell-cycle gene sets down | [39402753](notes/39402753.md) |
| AAV-OSK, mouse joint | COL2:COL1 restored, ACAN up, methylation age below chronological | **Ki-67 unchanged** | [41786976](notes/41786976.md) |
| Kartogenin 1 µM, adult MSCs | ACAN and SOX9 above TGF-β1 | proliferation "slightly" above control, no difference vs TGF-β1 | [33467170](notes/33467170.md) |
| Yoda1, periosteal stem cells | GAG and Col2a1 up in pellets | **Ki-67 unchanged in vivo; proliferation reduced dose-dependently in vitro; pellet size unchanged** | [35844802](notes/35844802.md) |
| Sprifermin, adult human knee | thickening score +425 µm | — (the dimensional result *is* the ceiling) | [26138203](notes/26138203.md) |

**Growth-plate output is a cell-counting process.** Senescence is progenitor exhaustion ([39563452](notes/39563452.md), [19098525](notes/19098525.md)), and growth stops before fusion because the resting-zone pool runs out, not because the drive stops. Length is produced by chondrocytes being born at the top of a column, swelling, and dying at the bottom; the actuator is hypertrophic swelling, and its largest, IGF-1-dependent phase is a per-cell volume change ([31787777](notes/31787777.md)). **So the number of cells entering columns sets the ceiling, and no compound raises it.**

The one place a lever for this exists in the literature is not a compound at all but the RNA layer: *Dicer* loss reduces proliferating chondrocyte number; **miR-140** drives resting→columnar and blocks hypertrophy; **let-7** is required for columnar proliferation and survival; the PTHrP gradient induces miR-374-5p/379-5p/503-5p which promote proliferation and inhibit hypertrophy ([37483459](notes/37483459.md), 23940373 (needed, see [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md))). That is §7.

**Corollary, repeated four times in four independent models: blocking conversion accumulates cartilage and loses length.**
- Palovarotene: articular cartilage thickened, osteochondral masses grew out of the joint surfaces, hypertrophic zone narrowed, **tibia 13–19% shorter** ([30226468](notes/30226468.md)).
- IGF-I + autologous marrow cells on a PLGA scaffold in a rabbit physeal defect: "a large, dense area of cartilage... mostly hypertrophic chondrocytes" — and **no significant correction of the angular deformity** ([26309783](notes/26309783.md)). The right factor, the right cells, and the output was a lump.
- Chondrocyte-specific Piezo1 knockout: **growth plate wider**, endochondral ossification inhibited ([40999873](notes/40999873.md)).
- Systemic bevacizumab after physeal injury: bone bridging reduced, **hypertrophic zone of the adjacent intact plate expanded, tibial shortening worse at day 60** ([37483459](notes/37483459.md)).
- PKD inhibition after physeal injury: more MSCs, more cartilage, less bone, **delayed healing** ([37483459](notes/37483459.md)).

Thickening a cartilage and lengthening a bone are different outcomes, and these four experiments separate them cleanly. Anything that only grows cartilage produces a swelling.

---

## 3. Where the centimetres actually come from

Three results, none of them a drug, all of them clearing 1 cm/year equivalents.

**3.1 The boundary ([40118845](notes/40118845.md)).** SOX9+ sclerotomal progenitors from hPSC — 99.2% pure, expandable 15,000-fold over two months with a 3.9-day doubling time, isolable with an antibody against **ITGA9** — split into two inductions. High BMP2 (100 ng/ml) + a smoothened agonist gives *osteogenesis-committed early chondrocytes* that are still COL10A1-negative. Chondrogenic medium gives chondroprogenitors that hold a cartilage fate for 12 weeks in a joint and never make bone. Fuse the two 1:1 and a growth plate appears at the interface, with resting, proliferative and hypertrophic zones, columns pointing at the ossification centre, the right regional markers, the right zonal stiffness gradient (26.1 MPa → 4.16 GPa), the full human growth-plate single-cell spectrum, and recoverable PDPN+CD146−CD73+CD164+ skeletal stem cells. **It forms in neither spheroid alone.** No PTHrP gradient was supplied; no IHH gradient was supplied; no scaffold; no mechanics. The gradient self-assembled from the juxtaposition.

**3.2 The geometry ([37483459](notes/37483459.md)).** The one physeal-repair intervention that produced "significantly greater limb growth" was a scaffold of **vertical pillars whose modulus was matched to measured rabbit growth-plate zonal moduli**, DLP-printed and combined with a cartilage-mimetic hydrogel — and it did so with only limited cartilage at the site. The zonal specification it was matched to is quantified: resting zone stiffest and least permeable, proliferative zone ~30% softer with ~4× the permeability, and a mechanoregulatory gradient that falls along the long axis through the hypertrophic zone, progressively licensing ossification. Meanwhile TGF-β1 + autologous BMSCs in a gel foam blocked the bone bridge and **made no cartilage structure at all**.

**3.3 The capability ([38672135](notes/38672135.md), [28629737](notes/28629737.md), [28645539](notes/28645539.md)).** An adult mammal builds a complete, vascularised, marrow-containing endochondral bone de novo in soft tissue in **fourteen days** — progenitors activate at 4 dpi, fail to clear at 5 dpi, become cartilage at 7 dpi, bone by 14 dpi. The competent cells are resident everywhere: PDGFRα+ Sca1+ CD34+ fibro-adipogenic progenitors in every muscle interstitium, Scx+ and Tppp3+ progenitors in every tendon and ligament, Gli1+ perivascular/periosteal progenitors wherever there are vessels. The output scales with progenitor number above a threshold of >20,000 cells, **R² = 0.85**. The machinery is intact, fast, and quantitative. What is missing in a normal adult is not capability. It is **initiation, location and polarity**.

And it needs **two** inputs, not one: a signal *and* an injury. In the FOP mouse the receptor mutation alone does not explain the episodic nature of the disease; in the BMP4 transgenic adult, a **5 mm shallow skin cut** was enough to trigger a lesion. The hard input is the signal; the permissive input is almost nothing. Which cuts both ways, and §6 says how.

---

## 4. The candidates, by node

### Node A — the conversion front: Piezo1 agonists and Sirt1 activators
**Agents that exist: Yoda1; SRT2104; resveratrol. Off-switch: 3-TYP, verteporfin.**

Piezo1 is enriched specifically in the chondrocyte lineage (Piezo2 is absent from chondrocytes) and in Gli1+ periosteal stem cells and their progeny. **Deleting it in chondrocytes widens the growth plate and blocks its endochondral ossification.** Yoda1 does the reverse: in a fracture, cartilage callus at 7 days then **cartilage almost gone by 14 days**, total osseous tissue **+42% and +51%**, maximum bending load **1.5×** at 28 days, through **YAP → β-catenin → BMP2 + VEGFA** from the resident progenitor itself. In a **tail-suspension unloading model** that causes delayed union with a 47% drop in peak load, Yoda1 **rescued everything**: bone volume, mineral density, Gli1+ recruitment, osteocalcin, vessel number, and the fall in Piezo1 protein. In a **distraction osteogenesis** model — the only established procedure that actually lengthens adult human bone — Yoda1 accelerated gap mineralisation and closure, while chondrocyte Piezo1 knockout left fibrous tissue and an unbridged gap ([35844802](notes/35844802.md), [40999873](notes/40999873.md)).

**Why it matters more than anything else here.** Sirt1 binds Piezo1, deacetylates it at **K2174**, and opens it — and in cells carrying the **L1341K/L1344K** mutations that break Piezo1's force-transduction machinery, **Yoda1 no longer opened the channel but the Sirt1 route still did.** Pharmacology here does not merely mimic load; it bypasses the need for it. Against the physics that kills the purely mechanical route — growth cartilage at 0.25–0.48 MPa versus bone at ~2000 MPa, so a fused diaphysis cannot be strained into growth ([23009361](notes/23009361.md)) — that is the one way around the problem that does not involve a surgeon. And **SRT2104 and resveratrol are existing, orally available compounds**, with a demonstrated acid-targeted oral formulation that localised only to the active lesion.

**What kills it.** Piezo1 knockout *widens* the plate, so activation should *narrow* it — faster conversion of a finite pool, i.e. **earlier closure, not later**. Applied to a plate this plausibly accelerates fusion, the opposite of what height needs. Nothing in either paper measured bone length. Accelerating cartilage-to-bone conversion at a joint margin is the mechanism of osteophyte formation. Piezo1 sits in red cells, endothelium, lung, bladder, pancreas and baroreceptors, and systemic agonism is uncharacterised. Yoda1 has poor solubility, a short half-life, no clinical programme. Resveratrol's bioavailability is bad enough that the authors had to build a microcapsule, and its literature is littered with non-replications.

### Node B — terminal hypertrophy: thyroid hormone
**Agent that exists: T3 (triiodothyronine). Local switch: DIO2.**

T3 is the terminal-hypertrophy switch across the literature. In hPSC chondronoids it raises the late hypertrophic programme (SP7, VEGFA, DMP1, HIF1A, MMP13, ALPL), suppresses SOX9/SOX5/SOX6, and **prior T3 is essential for optimal transition to bone-like organoids** ([37126720](notes/37126720.md)). More striking: **10 ng/ml for 10 days on osteochondral explants from human knees aged 59–76 moved 247 genes**, with ECM organisation and *ossification* as the two dominant pathways, COL2A1 up 6.4-fold, CLEC3A up 14.6-fold, PHOSPHO1 up 6.4-fold, ANKH and EPAS1 up. The authors' own words: T3 "causes chondrocytes to leave their maturationally arrested state... setting them on the path towards recuperation of a growth plate-like morphology" ([38664820](notes/38664820.md)). **Adult human articular chondrocytes are not locked.**

**What kills it.** Three things, and the third is fundamental.
1. It is the *last third* of the sequence only. COL10A1 went **down** 3.9-fold. T3 did not build a proliferative column; it drove cells straight to mineralisation. On its own it calcifies adult cartilage.
2. Nothing was measured in millimetres. Mankin score unchanged at 10 days. Ex vivo, OA cartilage, gene expression only.
3. **Thirty-seven of the 247 T3-responsive genes are GWAS osteoarthritis risk genes, and CCDC80, ANKH and CDON move in the same direction in T3-treated explants, in early OA and in progressive OA.** DIO2 risk variants raise OA risk; hyper- and hypothyroidism and thyroid-hormone sensitivity all associate with OA. The paper's entire framing is that this reactivation *is the disease*. **At the level of transcription, "make adult cartilage behave like growth cartilage again" and "give this person osteoarthritis" are close to the same instruction.** Any scheme claiming otherwise owes an account of what makes its version ordered and self-limiting, and nothing in this literature supplies one.

Systemic T3 in a euthyroid adult has never produced height, and never will; the relevant exposure in these experiments is a local bath.

### Node C — the cartilage domain and the epigenetic unlock
**Agents that exist: dasatinib; kartogenin; AAV-OSK; sprifermin (FGF-18); CTGF.**

- **Dasatinib** — approved oral drug. Three days' exposure to human articular chondrocytes raised **COL2A1 ~7-fold, rising to ~30-fold four days *after withdrawal***, with ACAN, SOX9, GAG and COL2 protein up, confirmed in intact human cartilage tissue by CPII ELISA and IHC, and restored the 28-day redifferentiation capacity of dedifferentiated cells. Mechanism: **YAP-1 inhibition** (CTGF, BIRC5, CYR61 all down), SASP suppression, and — importantly — **IGF1 and FGF18 up with IGFBP1 and IGFBP3 down**, i.e. more ligand *and* less sequestration of the molecule that drives the largest phase of hypertrophic swelling. **And senolysis is not the mechanism: navitoclax cleared the same p16+ cells and produced none of it; quercetin alone did nothing** ([39402753](notes/39402753.md)). That control kills the attractive hypothesis that clearing senescent chondrocytes restores growth capacity.
- **Kartogenin, ~1 µM** — a small molecule that induced **condensation** of adult MSCs by day 3 and beat TGF-β1 on ACAN and SOX9, with *Runx2* and *Col1a1* flat for 21 days ([33467170](notes/33467170.md)). Condensation is the first step of building a skeletal element, and the step every hormone-forced protocol skips. A diffusible small molecule that does it is worth more, practically, than a protein that does it.
- **AAV-OSK** (Oct4-Sox2-Klf4, no c-Myc), intra-articular — chondrocyte-selective, sparing subchondral bone and synovium. Lowered P21 and DNMT3a, **put methylation age below chronological age**, raised **TET2** (and siTet2 abolished every effect), suppressed RUNX2, OSX, COL1 and COL X, converted fibrocartilage to hyaline cartilage *in situ*, and did **not** raise Ki-67. Safety precedent: sustained AAV-OSK in retinal ganglion cells for 10–18 months with no proliferation or tumour ([41786976](notes/41786976.md)).
- **Sprifermin** — real, trialled, dose-responsive, +425 µm over two years (§1).
- **CTGF** — a direct SOX-9 target; a CTGF hydrogel produced new cartilage in a mouse articular defect at 4 weeks ([37483459](notes/37483459.md)).

**What kills it as a growth route.** Every one of these is a *maintenance* agent. OSK explicitly suppresses the ossification programme; dasatinib suppresses YAP; kartogenin is hypertrophy-silent; sprifermin gives micrometres. They are candidates for building and holding the hypertrophy-resistant domain of a two-domain construct, which is a real and necessary job. None is a cause of length. Dasatinib is a multikinase inhibitor with pleural effusion and pulmonary hypertension in its label.

### Node D — the master switch: YAP/TAZ
This is not an agent, it is the variable, and it is the most robust finding of the compound phase. **YAP/TAZ activity is the switch between "stay cartilage" and "convert to bone," confirmed from five independent directions:**
- Dasatinib → YAP down → cartilage maintained ([39402753](notes/39402753.md))
- Piezo1/Yoda1 → YAP up → BMP2, VEGFA, cartilage-to-bone conversion ([35844802](notes/35844802.md))
- FOP progenitors misread soft tissue as stiff → RhoA → YAP/TAZ up → ectopic bone, and ***Yap* deletion abolishes it** ([38672135](notes/38672135.md))
- Hypertrophic chondrocytes die above ~0.023 MPa via **YAP–p73–caspase-3** unless mechanically shielded ([33063669](notes/33063669.md))
- Verteporfin is used as the off-switch in the Piezo1 work itself ([35844802](notes/35844802.md))

**It has existing small molecules on both sides.** If anything in this corpus is the control variable for a staged cartilage→bone programme, it is this one. And the FOP finding that a receptor mutation can *spoof stiffness* means the mechanical theory in THEORY.md and the compound question are not alternatives — they converge on the same node, and should be used together rather than chosen between.

### Node E — delaying or reversing closure
**Agents that exist: aromatase inhibitors (anastrozole, letrozole). Untested mirror: RARγ antagonism.**

Fusion is estrogen/ERα-driven progenitor exhaustion. Aromatase inhibitors are the one established class that delays closure, and anastrozole improves height outcomes in growing children — **but only with open plates, and the literature on them is entirely paediatric.** They delay an event; they cannot undo one.

The more interesting item is a mirror hypothesis nobody has tested. **Palovarotene, an RARγ agonist, ablated the growth plate in 7 of 9 juvenile mice at both doses tested, and in wild-type mice too**, with bony bridges in the plates of the two survivors; retinoids are a known cause of premature physeal closure in humans ([30226468](notes/30226468.md)). If raising RARγ signalling closes plates, **reducing it might delay closure** — and nothing in this literature tried it. It is testable, it is cheap to test, and it is a real gap. It is also, in the adult, probably irrelevant: there is no plate left to keep open.

### Node F — the de novo route
**Agents that exist: recombinant BMP ligands locally; activin A (FOP only); the Gli1+/PDGFRα+/Scx+ resident progenitors as targets.**

Local recombinant BMP ligand plus an injury is sufficient to drive endochondral bone in a normal adult animal without any mutation ([28629737](notes/28629737.md)). The responding cells are named, sortable and ubiquitous. The output scales with cell number, R² = 0.85 ([30226468](notes/30226468.md)). This is the only route in the corpus that is demonstrably sufficient in a normal adult.

**What kills it as a systemic proposition, decisively.** In an adult with the signal present, **a 5 mm shallow skin cut was enough to initiate a lesion** ([28645539](notes/28645539.md)). That means any systemic manipulation supplying the signal makes every subsequent scratch, injection, sprain or dental procedure a potential ossification site. Uncontrolled activation of this axis is a disease with a median life expectancy of 56 years whose commonest cause of death is a fused rib cage, and whose mice die at 39 days of jaw ankylosis ([38672135](notes/38672135.md)). The entire approved pharmacology around this pathway — palovarotene, garetosmab — exists to **block** it, and blocking it systemically in adults cost 11.4% mortality (confounded, but unexplained), abscesses requiring surgical drainage in 11.6%, and loss of eyebrows and eyelashes in 46.5% ([37770652](notes/37770652.md)). **The limiting factor on this route is spatial control, and no compound provides spatial control.**

### Node G — delivery, which is not a detail
The single clearest local-versus-systemic contrast in the corpus: **systemic bevacizumab** after physeal injury made the limb **shorter** and expanded the adjacent intact hypertrophic zone, while **the same antibody in a local alginate–chitosan hydrogel** blocked bone bridging **without interfering with normal longitudinal bone growth** ([37483459](notes/37483459.md)). Same molecule, opposite sign, decided by delivery.

Three delivery technologies already exist and are tested: a **cartilage-targeting single-chain antibody fragment fused to IGF-1** ("superior therapeutic efficacy and minimizes adverse effects on other tissues compared to the direct use of IGF-1"); **intra-articular AAV2** with chondrocyte selectivity and subchondral-bone sparing ([41786976](notes/41786976.md)); and **oral yeast microcapsules** that release at pH 6.6 and localised only to an active lesion, peaking at day 7 and holding ≥14 days ([40999873](notes/40999873.md)). Acromegaly is the standing proof that systemic drive does not know where you want it: decades of supraphysiological GH/IGF-1 lengthen the mandible and almost nothing else ([22518118](notes/22518118.md)).

---

## 5. The three I would actually back

Ranked by the probability that they are on the causal path to centimetres, not by how well they are characterised.

**1. Piezo1 agonism / Sirt1 activation (Yoda1, SRT2104, resveratrol) — as the throughput control at a conversion front.** It is the only pharmacology in the corpus that (a) altered a real bone-lengthening process (distraction osteogenesis), (b) substituted for mechanical load in an unloading model, and (c) does so through a channel that opens without needing force transduction at all. THEORY.md's weakest link is Phase D — converting thickened cartilage into longer bone — and knee joint distraction thickened cartilage with no demonstrated bone-front advance. This is the one existing lever that accelerates exactly that step, from inside the resident progenitor, by inducing its own BMP2 and VEGFA. The caveat is severe and must be stated with the claim: **the same action should accelerate plate closure, and nobody has ever measured bone length under it.**

**2. T3 — as the terminal-maturation switch on a domain you have built, not as a treatment.** It is the only compound demonstrated to move *adult human* cartilage toward a growth-plate programme, and the only one in the corpus that is cheap, licensed and pharmacologically boring. Its value is that it does one specific job — license terminal hypertrophy and mineralisation at one end of a structure — and that job is required. Its fatal property as a stand-alone is that applied without a column above it and a vascular front below it, it mineralises cartilage, and the transcriptional signature it produces is osteoarthritis.

**3. The two-domain construct, with compounds as its control system.** Not a compound, and I am including it because it is the only thing that clears your magnitude bar. The parts all exist and are published: an expandable, 99%-pure, antibody-sortable human progenitor ([40118845](notes/40118845.md)); a small molecule that induces condensation (kartogenin); a reagent fork that decides permanent versus transient fate (TGF-β3 present or absent, [37126720](notes/37126720.md)); an agent that holds the resting domain's identity and resets its methylation age (OSK/TET2); an agent that licenses terminal hypertrophy at the other end (T3); an agent that sets conversion throughput (Piezo1); a modulus-matched columnar geometry that produced limb growth on its own ([37483459](notes/37483459.md)); and three tested local-delivery routes. **The compounds in this document are the knobs on that object. They are not substitutes for it.**

Honourable mention, because it is the one cartilage-*volume*-increasing result in the approved-drug literature and it is in the one growth cartilage that never fuses: **DKK1 inhibition with WAY262611** raised nuclear β-catenin, improved mandibular growth ex vivo and **increased condylar cartilage volume** in *Fgfr3*^Y367C/+ mice ([42650460](notes/42650460.md)). THEORY.md §2 is built on the mandibular condyle for exactly this reason. Worth separating from the rest of the achondroplasia pipeline.

---

## 6. Dead ends, and what kills each

| Candidate | Why it is appealing | What kills it |
|---|---|---|
| **GH / IGF-1 systemically** | the canonical growth drive; COACH adds 2.74 cm/yr on top of CNP | acromegaly lengthens **only the mandible** after decades of exposure; jaw and joint overgrowth, not height ([22518118](notes/22518118.md)) |
| **FGFR3 inhibition in an adult** (infigratinib, dabogratinib) | +1.74 cm/yr, oral, phase 3 | relieves a *pathological brake* that a normal skeleton does not have; FGFR signalling has **opposite signs** in articular vs growth-plate chondrocytes ([39402753](notes/39402753.md)); labelled for open plates |
| **CNP analogues in an adult** (vosoritide, navepegritide) | approved, effective | act only where functional plate cartilage is present; vosoritide guidance says **stop at documented closure** ([42650460](notes/42650460.md)) |
| **Soluble FGFR3 decoy** (recifercept) | mechanistically impeccable, strong preclinical | **zero efficacy at every dose; programme terminated.** The field's own lesson about plausibility vs benefit |
| **Repurposed pathway drugs** (meclizine, statins) | cheap, safe, right pathway | meclizine: **+0.11 cm/yr**. Statins: inconsistent, some show no FGFR inhibition in chondrocytes at all |
| **Hedgehog agonists** (SAG, purmorphamine) | Ihh is the core growth-plate signal | Hh in HO is **positional, not dose-like** — high outside the lesion, low inside — and **systemic Hh inhibition changed neither initiation nor established endochondral HO** ([28645539](notes/28645539.md)). Agonists promote the pathway vismodegib was built to block in basal cell carcinoma |
| **PTH1R agonists** (teriparatide, abaloparatide) | PTHrP is the resting-zone signal | only "partial improvement in animal models" even in achondroplasia; carries an osteosarcoma signal |
| **Senolytics as a class** (navitoclax, D+Q framed as senolysis) | plate senescence is progenitor exhaustion, so clearing senescent cells should help | **navitoclax cleared the same p16+ cells and produced none of the anabolic effect; quercetin alone did nothing.** The effect is dasatinib's YAP inhibition, not senolysis ([39402753](notes/39402753.md)) |
| **RARγ agonism** (palovarotene) | thickens articular cartilage, blocks ectopic bone | **tibia 13–19% shorter; plate ablated in 7/9 mice and in wild types; osteochondral overgrowths at the knee** ([30226468](notes/30226468.md)) |
| **Systemic anti-VEGF** (bevacizumab) | blocks the bone bridge | **worse tibial shortening at day 60 and expansion of the adjacent intact hypertrophic zone** ([37483459](notes/37483459.md)) |
| **Systemic activin A blockade** (garetosmab) | abolishes *new* HO lesions, 40.9% → 0% | 11.4% mortality (confounded, unexplained), abscesses needing drainage in 11.6%, madarosis 46.5%, epistaxis 34.9% with normal coagulation. And in **wild-type** tissue activin A is an ACVR1 *antagonist*, so the sign inverts outside FOP ([37770652](notes/37770652.md)) |
| **Systemic BMP agonism** | sufficient for adult de novo endochondral bone | with the signal present, **a 5 mm skin cut initiates a lesion** ([28645539](notes/28645539.md)). This is how you get FOP, not height |
| **PKD inhibition** | delays ossification, preserves cartilage after physeal injury | more cartilage, less bone, **delayed healing** ([37483459](notes/37483459.md)) — the swelling failure mode again |

---

## 7. The one lead that could change this answer

Everything above is bounded by the proliferation wall in §2. There is exactly one place in the literature where that wall appears to have been breached in adult articular cartilage, and I could not get the full texts.

**Lin28a → Erk1/2.** Overexpressing Lin28a in articular chondrocyte progenitors **upregulated Erk signalling and increased articular cartilage thickness**; a constitutively active Kras mimicked it, and inhibiting Erk normalised both phenotypes (30042178, needed — see [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md) — PMC-free but the body did not come back through my container). And in a separate OA study cited as ref 52 of [41786976](notes/41786976.md), **Lin28a restored chondrocyte stemness (Nanog-high) and *increased osteophyte volume*** — reported as an adverse effect, and the reason those authors chose OSK over Lin28a. **That is the only observation in this entire corpus of adult articular cartilage generating new bony outgrowth under a single defined molecular input.** In the frame of this project it is not an adverse effect; it is the phenomenon.

Three reasons to be cautious, and they are real. First, the Lin28a abstract says articular cartilage thickness is "mainly determined during the process of embryonic synovial joint development" — if the window is embryonic, postnatal induction may do nothing, and the full text is needed to know whether it was tried. Second, **ERK is the pathway FGFR3 activates to *shorten* bone in achondroplasia**; the same kinase has opposite dimensional effects in articular versus growth-plate chondrocytes, which is a warning, not a contradiction. Third, Lin28a is the canonical **let-7 suppressor**, and let-7 is *required* for columnar chondrocyte proliferation ([37483459](notes/37483459.md), 23940373, needed — see [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md)) — so the naive reading of Lin28a's mechanism points the wrong way, and Lin28a's effects here are probably let-7-independent (metabolic/ERK). Lin28 is also a known oncofetal gene.

Alongside it sits the broader RNA layer, which is the only place anything increases *proliferating chondrocyte number*: **miR-140** (drives resting→columnar, inhibits hypertrophy), **let-7** (required for columnar proliferation and survival), **Dicer** (its loss reduces proliferating chondrocyte number by both mechanisms), and the **PTHrP-gradient-induced miR-374-5p/379-5p/503-5p** (promote proliferation, inhibit hypertrophy). None of these is a compound today. All of them are deliverable in principle by the same intra-articular AAV route that OSK already uses.

**If I were allocating one more round of reading, it would go here.** These are on the needed list as Tier 0b.

---

## 8. What I will not write, and why

I will not write a regimen — specific compounds at specific doses on a schedule, or where to get them — for someone to take for height. That holds for this document and for the mechanical programme in THEORY.md.

It is not a formality. The specific agents that look most interesting here are the ones where the margin between the intended effect and serious harm is narrowest, and the literature says so directly:
- **Hedgehog agonists** promote the pathway vismodegib was developed to block in basal cell carcinoma.
- **PTH1R agonists** carry an osteosarcoma signal.
- **Sustained GH/IGF-1** produces the acromegalic phenotype — jaw and joint overgrowth — and not height.
- **BMP/ACVR1 activation** is FOP, where mice die at 39 days of jaw ankylosis and people have a median life expectancy of 56 with death from a fused rib cage, and where a 5 mm skin cut is a sufficient trigger.
- **Systemic activin A blockade** in adults ran at 11.4% mortality with abscesses requiring surgical drainage.
- **RARγ agonism** shortened tibiae by up to 19% and ablated growth plates in wild-type animals.
- **T3's transcriptional signature in adult human cartilage overlaps 37 osteoarthritis risk genes.**
- **Dasatinib** carries pleural effusion and pulmonary hypertension.

There is also a cleaner argument, which is that a regimen would not work. Nothing in §4 supplies cells or geometry, and §2 says cells are the limit. A list of molecules to take is the one form this answer cannot usefully take.

What I will do is what this document does: name the agents, say what each one did, in what species, at what skeletal age, with what magnitude, and what kills it.

---

## 9. What would have to be shown

Falsifiers and decisive experiments, in the order I would run them. Each is designed so a negative result ends a line of inquiry.

**9.1 Does the boundary work in line with a load-bearing bone?** Everything in [40118845](notes/40118845.md) grew free in a kidney capsule or subcutis. The experiment: place a two-domain construct in series with a fused long bone in a mature animal — rabbit or sheep, **not** rat or mouse, which never fuse their plates ([THEORY.md](THEORY.md) §7) — and measure segment length over months against a sham. **Kill criterion: no net length gain at 6 months.** Also required: that the elongation rate survives scale-up from a 2.4 mm construct to a human-metaphysis cross-section, in a diffusion-limited avascular tissue where there is every reason to think it will not.

**9.2 Does Piezo1 activation lengthen anything?** No paper has measured bone length under Yoda1, SRT2104 or chondrocyte Piezo1 manipulation. The experiment: longitudinal growth rate and final bone length in growing animals under each, plus the same in a mature animal carrying an induced cartilage template. **Prediction to test, and it is the uncomfortable one: Piezo1 activation accelerates plate closure and shortens final length.** If that is what happens, Node A is a conversion tool only, usable solely where a template already exists.

**9.3 Can Lin28a/ERK thicken *postnatal* articular cartilage, and does the osteophyte become a column under a polarity cue?** Read the two Lin28a papers first (§7). Then: postnatal intra-articular induction, measuring thickness and proliferating cell number; and whether the resulting osteophytic mass can be oriented by an apposed ossifying domain or a modulus gradient rather than forming a lump. **Kill criterion: no postnatal thickness response, or no orientability.**

**9.4 Is the reactivation separable from osteoarthritis?** [38664820](notes/38664820.md) is the central objection and it is a transcriptional one. The experiment: induce the growth-plate programme in adult cartilage by the most ordered route available and ask whether CCDC80, ANKH, CDON and the 37 OA risk genes move the same way, and whether the tissue degrades. **Kill criterion: the transcriptional signature and the histological outcome are indistinguishable from progressive OA.** If this fails, the whole compound route fails regardless of magnitude.

**9.5 Can the cell supply be raised without oncogenesis?** §2's wall. Test whichever RNA-layer lever (miR-140, let-7, PTHrP-gradient miRNAs) raises proliferating chondrocyte number in adult tissue, with tumour surveillance as a primary endpoint, not a footnote. **Kill criterion: no increase in proliferating chondrocyte number at any tolerable exposure.**

**9.6 Resolve the mechanics contradiction.** [37483459](notes/37483459.md) states that dynamic compression stimulates growth-plate growth while shear and hydrostatic pressure drive ossification; [19540500](notes/19540500.md) and [23009361](notes/23009361.md) hold the opposite — cyclic hydrostatic pressure maintains cartilage, deviatoric shear drives ossification. One is wrong, or they describe different regimes. PCAC Phase B/C depends on which. The primaries are on the needed list.

---

## 10. Bottom line

Longitudinal growth after growth-plate closure is not forbidden by biology. An adult builds a complete endochondral bone from resident cells in fourteen days, and a boundary between two cartilage states assembles a functional, elongating human growth plate at roughly three centimetres a year. **The bottleneck is not drive, and it is not capability. It is a template with the right architecture, a supply of cells to feed it, and spatial control over where the programme runs.**

Compounds do not supply any of those three. What they do supply is real and necessary: **Piezo1/Sirt1 activation** sets the throughput at a conversion front and substitutes for load the physics of a fused bone will not transmit; **T3** licenses terminal maturation at one end; **dasatinib, kartogenin, OSK/TET2 and FGF-18** build and hold the cartilage domain at the other; **YAP/TAZ** is the switch between the two, with existing drugs pointing both ways; and **three tested local-delivery routes** exist to keep all of it where it is wanted instead of everywhere.

Judged on your own standard — centimetres, not millimetres — the answer from the compound literature is: **not by themselves, not systemically, and not at all without solving the cell-number problem in §2.** The one place that problem looks soluble is the Lin28a/ERK and let-7/miR-140 layer in §7, and I could not get those full texts. They are at the top of [NEEDED_FULLTEXTS.md](NEEDED_FULLTEXTS.md).

---

*Built from 84 full texts read in full, in 83 notes in [notes/](notes/) (one note covers the two sprifermin papers). Nothing here has been tested as a route to adult height, and much of it has been tested as a route to osteoarthritis or heterotopic ossification and found to work.*
