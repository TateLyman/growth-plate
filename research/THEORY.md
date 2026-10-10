# Longitudinal bone growth after growth-plate fusion: a mechanical theory

**Status:** a hypothesis built from full texts I read myself (notes in [`notes/`](notes/), one file per PMID — 66 at the time this document was written, 84 across the project). It has **not** been tested. Every claim below is tagged with the PMID it rests on. Where I go beyond the data, I say so.

**Companion document:** [`COMPOUNDS.md`](COMPOUNDS.md) covers the pharmacological route — which existing agents touch which node, what each produced, and what kills each. Read together, the two documents converge rather than compete: the compound literature's central switch (YAP/TAZ) is a mechanotransduction node, FOP progenitors reach it by *misreading tissue stiffness*, and Sirt1 activation opens Piezo1 even when its force-transduction residues are mutated. That last result matters for this document specifically: it is a way to deliver the mechanical signal where the stiffness contrast of a fused diaphysis (§0.1) will not transmit it.

---

## 0. Short answer

1. **Through the fused physis: no.** No non-surgical method lengthens a fused limb bone through its former growth plate, and the physics says none can. Fused bone has ~2000 MPa stiffness; growth cartilage has ~0.3–0.5 MPa ([23009361](notes/23009361.md)). Any load you can apply gives µε strains in bone, whereas growth modulation needs ~10% strains in cartilage ([19540500](notes/19540500.md)).
   - Hormones don't do it either. Acromegaly lengthens only the mandible after closure, not limb bones ([22518118](notes/22518118.md)).
   - **The missing ingredient is a living, progenitor-fed cartilage template, not a growth signal.**
2. **Adult endochondral lengthening does exist in humans**, at bone ends that keep a progenitor-capped cartilage:
   - The mandibular condyle keeps growing in adults: acromegaly ([22518118](notes/22518118.md)); condylar hyperplasia biopsies at age 28–36 still show elongation fronts ([39584870](notes/39584870.md)); a 30-year-old regrew condyle with a repositioning splint ([19619334](notes/19619334.md)).
   - Mechanically repositioning adult animal condyles reactivates them ([15574348](notes/15574348.md), [34527791](notes/34527791.md), [35515998](notes/35515998.md), [39563452](notes/39563452.md)).
3. **Every limb bone end also carries a never-fused, ontogenetically "growth-plate-like" cartilage: the articular cartilage.**
   - In juveniles it grows the epiphysis appositionally. Superficial progenitors feed cells downward until they pass the tidemark into calcified cartilage, which is replaced by bone ([25521919](notes/25521919.md), [25068449](notes/25068449.md), [25603997](notes/25603997.md)).
   - In adults this engine idles, but it is not dead. In 48-year-old humans, 2 months of contact-free knee distraction with oscillating fluid pressure **regrew ~0.6 mm of cartilage in a year** ([21565898](notes/21565898.md)).
4. **My proposal (novel):** reactivate the articular cartilage as an adult appositional growth front, i.e. make limb joints behave like the mandibular condyle. Use a **phase-cycled, non-invasive mechanical program**, with one phase for each bottleneck:
   - recruit surface progenitors;
   - keep them young;
   - open a protected output window;
   - convert the gain to bone at the tidemark;
   - ratchet the set-point so the response doesn't adapt away.

   I call it **Phase-Cycled Articular Condylization (PCAC)**.
5. **Realistic magnitude, if it works at all:** millimetres per year, not centimetres. The evidence does not yet show any of this produces *bone length* in a fused limb. It shows that each component step is mechanically controllable in adult tissue.

---

## 1. What the full texts establish (the constraints the theory must satisfy)

| # | Constraint | Evidence |
|---|---|---|
| C1 | Growth after fusion cannot come from the old physis. It is bone; there is nothing compliant to strain or distract. | [23009361](notes/23009361.md), [9246990](notes/9246990.md), [3213455](notes/3213455.md) |
| C2 | Growth needs a **young progenitor supply**. An old, open plate gives little: a decade of extra open plate adds ~3 cm ([31770102](notes/31770102.md)). Senescence is use-dependent: an unused plate "banks" capacity ([42022344](notes/42022344.md)). Growth rate follows donor age ([40478277](notes/40478277.md)). | as cited |
| C3 | A cartilage layer alone is not growth. Active-looking but non-growing growth cartilage exists (aged monkey vertebrae, [29750005](notes/29750005.md)). **Net length = cartilage production rate**; ossification only consumes it. | [29750005](notes/29750005.md), [34141832](notes/34141832.md) |
| C4 | The length actuator is **hypertrophic cell swelling inside laterally confining matrix** (three phases; phase 3 needs IGF-1). Articular cartilage also thickens mainly by cell-volume increase and stacking. | [23485973](notes/23485973.md), [28438606](notes/28438606.md), [19540500](notes/19540500.md) |
| C5 | **Hypertrophic cells are the most mechanically fragile cells.** They have ~25% of the stiffness of columnar cells and die (YAP–p73–caspase) under compressive and octahedral stress at ~0.02 MPa unless shielded. Hydrostatic stress is tolerated. The SOC evolved to shield them; archosaurs instead sequester them in bony pockets. | [33063669](notes/33063669.md) |
| C6 | Progenitors need a **niche**: PTHrP source, balanced Hh, Wnt/BMP-low pocket, mechanical shielding. A transient boost to a functioning niche gives durable length gains. | [30401834](notes/30401834.md), [35523895](notes/35523895.md), [38516888](notes/38516888.md), [42552306](notes/42552306.md), [31830758](notes/31830758.md), [35851381](notes/35851381.md) |
| C7 | **A surface-fed, appositional growth cartilage works without a physis.** The condyle is fed by a superficial PTHrP layer over a periosteum-contiguous RUNX2+ progenitor layer. It escapes the estrogen/ERα depletion clock that fuses primary plates. | [38058151](notes/38058151.md), [28643917](notes/28643917.md) |
| C8 | **Mechanical switches exist in adult tissue.** Compression+shear makes adult human MSCs chondrogenic without growth factors. Joint sliding physically activates synovial latent TGF-β. Fluid shear induces PTHrP/PGE2/ATP → CREB → Prg4 at the surface; running doubles Prg4+ surface cells. Friction (no lubricin) makes adult articular surfaces chondrogenic and endochondral for 12 months. | [22048899](notes/22048899.md), [22858668](notes/22858668.md), [27445107](notes/27445107.md), [24449269](notes/24449269.md), [25603997](notes/25603997.md), [26945615](notes/26945615.md) |
| C9 | **Stress type decides fate** (Carter rule). Cyclic hydrostatic pressure keeps cartilage and keeps progenitors quiescent and Sox9-high (reversible within ~3 h). Shear, octahedral or static stress drives ossification, and bridges start at shear-rich peripheries. Injurious pressure (≥20–50 MPa) degrades cartilage. | [33310912](notes/33310912.md), [31056740](notes/31056740.md), [29417047](notes/29417047.md), [38144567](notes/38144567.md) |
| C10 | **Tension and unloading increase output; compression suppresses it**, linearly with no threshold (~17%/0.1 MPa). About 90% of lengthening happens in recumbency. Dynamic tension is most anabolic. Safe physeal tension is <~0.15 MPa. | [19540500](notes/19540500.md), [23009361](notes/23009361.md), [31787777](notes/31787777.md), [9246990](notes/9246990.md) |
| C11 | **Adult human cartilage regrows when contact stress is removed and fluid-pressure oscillation is kept** (KJD: +0.6 mm in 1 year, progressive after frame removal). | [21565898](notes/21565898.md) |
| C12 | **Responses adapt away.** Condylar reactivation peaks at ~3 weeks and returns to baseline by 60 days despite the appliance. Static tension effects fade. Condylar hyperplasia stops at mechanical equilibrium. **Stepwise or renewed stimuli sustain them.** | [15574348](notes/15574348.md), [31787777](notes/31787777.md), [42187771](notes/42187771.md), [39563452](notes/39563452.md), [34527791](notes/34527791.md) |
| C13 | **Adult progenitor reservoirs at the bone end:** synovial Prg4+ CD44+ P75+ cells (massive injury response); groove of Ranvier / perichondrial ring; periosteal stem cells (CD200+, present in humans, switch to endochondral under injury and motion). Adult articular chondrocytes themselves are passive. | [28438606](notes/28438606.md), [30250253](notes/30250253.md), [36309308](notes/36309308.md), [3213455](notes/3213455.md) |
| C14 | **The periosteum is a tether:** releasing it raises growth ~25% even without blood supply. The soft-tissue envelope compresses any growth front. | [532591](notes/532591.md) |
| C15 | **What doesn't work post-fusion:** systemic GH/IGF ([22518118](notes/22518118.md)); lateral joint loading (widens cortex via marrow hydraulics, [16984642](notes/16984642.md), [17968490](notes/17968490.md), [17344109](notes/17344109.md)); venous stasis ([1146509](notes/1146509.md)); LIPUS alone, a weak gain on existing cartilage ([35515998](notes/35515998.md)); ESWT, shown only in open plates ([40038756](notes/40038756.md)). | as cited |

---

## 2. The central insight

There is a perfect natural model of what we want: **the mandibular condyle**.
- It is a bone end covered by a cartilage that never fuses.
- Its growth front is fed from the surface, not from a buried plate.
- It keeps lengthening the jaw in adult humans when stimulated, by GH excess or by mechanical repositioning.

Every **limb joint surface has the same topology**. Articular cartilage sits on a calcified layer (tidemark) on subchondral bone, perpendicular to the long axis at the knee, ankle and hip. In juveniles this tissue *was* an appositional growth cartilage ([25603997](notes/25603997.md): clones from surface progenitors end up below the tidemark).

The limb articular surface differs from the condyle in four specific, mechanically addressable ways:

| Condyle (grows in adults) | Adult limb articular cartilage (idle) | Mechanical lever |
|---|---|---|
| Active proliferative progenitor layer, periosteum-contiguous | Surface progenitors quiescent; adult chondrocytes passive | Articulating shear + compression → TGF-β activation, Sox9, Prg4/PTHrP (C8) |
| Surface PTHrP gradient prevents exhaustion | Weak | Fluid shear → PTHrP (C8); intermittent load → PTHrP ([39090666](notes/39090666.md)) |
| Hypertrophic layer that isn't crushed | Deep zone under direct compressive load, so hypertrophy would be lethal (C5) | Schedule hypertrophy into unloaded/traction windows |
| Mechanical drive with stepwise renewal | Steady-state loading (adapted) | Ratchet: renew the stimulus every 2–3 weeks (C12) |

---

## 3. The mechanism: Phase-Cycled Articular Condylization (PCAC)

A repeating daily/weekly mechanical program applied to a target joint (knee first: it holds two growth fronts in series, distal femur and proximal tibia). Everything is external and non-surgical. The hardware is repurposed from existing devices.

### Phase A: Activate the surface (recruitment)
- **Input:** articulating sliding under moderate compression. Example: continuous-passive-motion with an applied axial load, or a sliding ergometer; ~1 h sessions; physiological contact stresses.
- **Why:**
  - Compression+shear is the only mechanical regime shown to make adult human MSCs chondrogenic without exogenous factors (Sox9/Col2/Acan up, Col10/ALP not; [22048899](notes/22048899.md)).
  - Sliding shear physically activates the synovial latent TGF-β reservoir, dose-dependent on shear rate × time and protease-independent ([22858668](notes/22858668.md), [27445107](notes/27445107.md)).
  - Fluid shear at the surface induces PTHrP, PGE2 and ATP → CREB → the Prg4/progenitor program ([24449269](notes/24449269.md)). Running expands Prg4+ cells where load is highest ([25603997](notes/25603997.md)).
  - Raised friction makes the surface chondrogenic and endochondral ([26945615](notes/26945615.md)).
  - At articulations, periosteal Sox9+/Runx2+ progenitors stay cartilage only while movement continues. Paralysis or blocking stretch-activated channels turns that cartilage into bone ([21600197](notes/21600197.md)). Motion is the switch that holds the joint-margin tissue in a cartilage state.
- **Targets:** surface progenitors, synovial Prg4+ CD44+ P75+ cells, groove of Ranvier, periosteal stem cells at the margin (C13).
- **Dose limits:**
  - Active TGF-β above ~1–10 ng/mL is osteophytic ([22858668](notes/22858668.md), [23339896](notes/23339896.md)), so sessions are capped.
  - Avoid COX-2 inhibitors, which blunt the response by ~35% ([24449269](notes/24449269.md)).

### Phase B: Keep the progenitors young (niche maintenance)
- **Input:** fast cyclic axial compression (~0.5–1 Hz) in the physiological band. At these rates most of the load is carried by interstitial fluid pressure, so cells see **cyclic hydrostatic pressure** (~1–5 MPa) rather than deformation.
- **Why:**
  - Cyclic HP puts progenitors into a reversible quiescent, Sox9-high, anti-hypertrophic state through H3K9me3 loss ([33310912](notes/33310912.md)).
  - HP in the 0.1–10 MPa band is chondrogenic ([31056740](notes/31056740.md)).
  - Intermittent physiological loading induces PTHrP ([39090666](notes/39090666.md)).
  - This guards against the cell-counting exhaustion that ends normal growth (C2).
- **Limit:** stay well below injurious HP (≥20–50 MPa; [38144567](notes/38144567.md)).

### Phase C: Output window (protected expansion)
- **Input:** prolonged contact-free axial unloading of the joint, with gentle traction and small oscillations. It is scheduled into recumbency, e.g. a night-time joint-traction device.
- **Why:**
  - Removing compressive and octahedral stress is the only way to let deep cells swell (hypertrophy) without killing them ([33063669](notes/33063669.md)). Cell swelling is the actuator ([23485973](notes/23485973.md), [28438606](notes/28438606.md)).
  - Releasing HP lets the progenitors maintained in Phase B exit quiescence within ~3 h and divide ([33310912](notes/33310912.md)).
  - Tension raises hypertrophic output; dynamic tension is the most anabolic ([19540500](notes/19540500.md), [23009361](notes/23009361.md), [31787777](notes/31787777.md)). Natural growth happens ~90% in recumbency ([19540500](notes/19540500.md)).
  - Human proof that this regime is anabolic in adult cartilage: KJD ([21565898](notes/21565898.md)).
- **Limits:** keep tissue tension low (physeal separation risk above ~0.15 MPa, [9246990](notes/9246990.md)). Keep small axial oscillations so fluid pumping (nutrition) continues, as KJD's springs did.

### Phase D: Convert the gain to bone (front advance)
- **Input:** ordinary weight-bearing and slow loading. Under sustained or slow loading, interstitial fluid support decays and the solid matrix carries deviatoric strain at depth. This is the stress type that favours ossification (C9).
- **Why:**
  - Loading activates BMP–Smad1/5/8 and alkalinises the front (Pi/PPi up, ALP up), accelerating calcification of hypertrophic cartilage ([34141832](notes/34141832.md)).
  - KJD showed subchondral resorption then normalisation, i.e. an active bone-turnover coupling step under the cartilage ([21565898](notes/21565898.md)).
  - **This is the step that turns thicker cartilage into longer bone.** Length gained = tidemark/subchondral advance while cartilage thickness is held constant (C3).

### Ratchet (against adaptation)
- Every ~2–3 weeks, change the parameters (load, sliding amplitude, traction set-point, frequency) and step the traction set-point up slightly.
- **Why:**
  - Single mechanical changes give a ~3-week response that decays ([15574348](notes/15574348.md)). Stepwise renewal sustains output ([39563452](notes/39563452.md), [34527791](notes/34527791.md)).
  - Growth driven by mechanical demand stops at equilibrium ([42187771](notes/42187771.md)).
  - The soft-tissue and periosteal envelope is a tether that compresses the front ([532591](notes/532591.md)). Slow progressive traction lengthens that envelope so the joint can accommodate thicker cartilage and advancing bone instead of loading it back into compression.

### Why the result is length, not osteophytes or thicker cartilage only
- **Direction.** Knee, ankle and hip articular fronts face along the limb axis. Endochondral replacement at their base adds length, exactly as juvenile epiphyseal growth did ([25521919](notes/25521919.md), [25603997](notes/25603997.md)).
  - Osteophytes are radial because they arise at margins, driven by instability and excess TGF-β ([23339896](notes/23339896.md)). PCAC keeps the joint stable, doses TGF-β, and targets the central loaded plateau, where Prg4+ progenitor expansion is greatest ([25603997](notes/25603997.md)).
- **Protection without an SOC.** Archosaurs grow without SOCs by sequestering hypertrophic cells between bony protrusions ([33063669](notes/33063669.md)). The adult osteochondral interface is already interdigitated (calcified-cartilage pegs). Combined with unloaded output windows, that may suffice. **This is speculative.**
- **Two fronts in series per joint.** Both articular surfaces see the same program, so congruity is preserved and the gains add.

---

## 4. What is new here (and what is repurposed)

New, as far as the 66 papers I read show:
1. **Treating adult limb articular cartilage as a dormant appositional growth plate**, and the joint as the place to make length after fusion, modelled on the adult condyle.
2. **Stress-type gating by loading rate**. The same joint load is delivered either fast (fluid-supported → hydrostatic → progenitor-preserving) or slow (matrix-supported → deviatoric → ossifying). That spatially and temporally selects which zone responds. This rests on biphasic cartilage mechanics; I have not yet read the primary papers that quantify it (Soltz & Ateshian 2000; Park & Ateshian 2003; see needed list).
3. **Duty-cycling between a progenitor-maintenance state (cyclic HP) and an output state (unloaded/tension)**, exploiting the ~3 h reversibility of HP-induced quiescence ([33310912](notes/33310912.md)).
4. **Shear as a self-dosed, drug-free TGF-β/PTHrP release system** for chondrogenic recruitment ([22858668](notes/22858668.md), [24449269](notes/24449269.md)).
5. **A ratchet** to defeat the mechanical adaptation that otherwise ends every response.

Repurposed hardware (allowed):
- **Phase A:** CPM machines with axial loading.
- **Phase B:** cyclic axial loaders or the human joint-loading devices already built ([27690057](notes/27690057.md), [30405872](notes/30405872.md)).
- **Phase C:** joint/axial traction devices.
- **Optional amplifiers:** LIPUS (a +20% gain on an existing endochondral front, [35515998](notes/35515998.md)); low-energy focused ESWT (SOX9/BMP up in cartilage, [40038756](notes/40038756.md)).
- KJD's mechanical principle, made non-invasive.

---

## 5. Expected magnitude (illustrative arithmetic, not a prediction)

- Adult appositional articular growth is near zero at baseline. Mouse clones labelled at 1 month never reach the tidemark by 18 months ([25603997](notes/25603997.md)).
- The best adult human cartilage gain under mechanical offloading is ~0.6 mm/year, and that is *repair* in OA ([21565898](notes/21565898.md)).
- Adult (120-day) rat condyle endochondral bone growth is ~13 µm/day, raised ~20% by LIPUS ([35515998](notes/35515998.md)).
- If PCAC could sustain a front advance of 0.1–0.5 mm/year per articular surface:
  - knee (2 surfaces) + ankle (2) + hip (≈1 effective) ≈ 5 surfaces in series per leg → roughly **0.5–2.5 mm/year of leg length**;
  - only if cartilage thickness is maintained at the same time.
- Centimetres would need condyle-like rates (hyperplasia-level), which no limb data support.
- The spine (vertebral cartilaginous end-plates, ~46 surfaces) would multiply this, but I have not read human end-plate full texts. Aged monkey vertebral plates show "active-looking" cartilage without growth ([29750005](notes/29750005.md)), so this is unsupported for now.

---

## 6. Risks and how the theory could fail

- **It may just be OA.** OA is articular cartilage regaining hypertrophy, tidemark advance and thinning ([29619368](notes/29619368.md), [38144567](notes/38144567.md)).
  - Distinguishing criterion: **cartilage thickness must stay constant or rise while the tidemark advances**, with Col II synthesis up and MMP-13 not.
  - Kill criteria: loss of cartilage thickness, fibrillation (OARSI score), osteophytes, subchondral sclerosis, pain.
- **Osteophytes from excess TGF-β** ([23339896](notes/23339896.md)). Cap shear dose.
- **Hypertrophic cell death** if hypertrophy occurs under load ([33063669](notes/33063669.md)).
- **No conversion step.** KJD thickened cartilage but did not show bone advance. Phase D is the least-supported phase.
- **Joint incongruity** if the two surfaces advance unequally.
- **Non-invasive traction may not achieve KJD-like contact-free unloading.** Skin and soft tissue absorb force. I have no full text quantifying joint separation under external traction.
- **Human magnitude may be clinically trivial** (sub-mm/year).

---

## 7. How to test it (cheapest first)

1. **Ex vivo, adult osteochondral explants** (skeletally mature bovine/porcine/human surgical waste) in a multi-axial bioreactor (ball-on-plate like [22048899](notes/22048899.md), plus a traction mode). Run the A→B→C→D cycle vs each phase alone.
   - Readouts: sequential fluorochrome labels measuring the tidemark/calcification front advance (as in [34141832](notes/34141832.md)); cartilage thickness; Sox9/Prg4/PTHrP at the surface; Col10 in the deep zone; YAP–p73/TUNEL; MMP-13.
2. **Skeletally mature animals with true fusion** (rabbit after closure, sheep, dog; *not* rats or mice, which don't fuse, [40478277](notes/40478277.md)). Non-invasive knee devices; arms = control, each phase alone, full cycle, and full cycle without ratchet.
   - Readouts: fluorochrome tidemark advance, high-resolution CT bone length, MRI cartilage thickness, 99mTc-MDP SPECT uptake at the joint as an activity marker ([37415579](notes/37415579.md)), OARSI histology.
3. **Positive control:** adult condyle, where mechanical reactivation is known to work. Does adding Phases B/C and the ratchet beat stepwise advancement alone?
4. **Falsifiers:**
   - The full cycle gives no tidemark advance beyond control at constant cartilage thickness in mature animals.
   - Any advance comes only with OA signs.
   - Advance stops within ~4 weeks despite the ratchet.

---

## 8. Papers I need (to firm up or kill the weak links)

See [`NEEDED_FULLTEXTS.md`](NEEDED_FULLTEXTS.md), section **Tier 0**. They cover:
- adult tidemark advance rates in humans and its mechanical control;
- biphasic fluid load support vs loading rate (the stress-type gating claim);
- non-invasive joint traction mechanics;
- KJD follow-ups and histology;
- the condyle stepwise-advancement and Ihh-mechanotransduction primaries;
- Noonan's recumbency data;
- human vertebral end-plate ageing.
