# DOMAIN 09 — MECHANICS AND PHYSICAL INTERVENTIONS: COMPLETE INVENTORY (R436)

Built ENTIRELY from external search (Europe PMC REST API, NCBI eutils efetch, WebSearch/WebFetch).
No atlas file was read except the two briefs. Every PMID was returned by a live query and, except where
noted, its abstract was retrieved and read. Anything not verified is marked `UNVERIFIED`.

Conventions:
- **"LENGTH endpoint"** = a caliper / radiographic / fluorochrome measurement of BONE or BODY length.
  Growth-plate height, BMD, BMC, mineral apposition rate and bone-formation rate are **NOT** length endpoints
  and are labelled as proxies. This distinction does most of the work in this domain: dozens of modalities
  have a bone-*mass* literature and no length endpoint at all.
- Species is given for every animal claim.
- `OBSCURE? yes` = rarely or never discussed in the mainstream growth/auxology literature.

---

## MAIN TABLE

| # | MODALITY | DOSE PARAMETERS | EFFECT ON LENGTH | EVIDENCE (species + PMID) | HUMAN DATA? | OBSCURE? |
|---|---|---|---|---|---|---|
| 1 | **Sustained axial COMPRESSION across a growth plate (Hueter–Volkmann)** | ~0.1–0.2 MPa, external fixator, 8 d, continuous | **NEGATIVE, linear, no dead band.** Growth-rate sensitivity **17.1%/0.1 MPa** (range 9.2–23.9); vertebra 15.0 vs proximal tibia 18.6 | rat, rabbit, calf; caudal vertebra + proximal tibia; fluorochrome interlabel length **PMID 16705695** | Inferred only (scoliosis, Blount, brace) | no |
| 2 | **Sustained DISTRACTION (tension) across a growth plate** | same rig, tensile stress up to ~0.1 MPa | **POSITIVE and on the same line as compression** — distraction accelerates growth; sensitivity is the mirror of row 1 | rat/rabbit/calf **PMID 16705695**; rabbit 1 kg distraction **PMID 2312573** | No direct normal-child data | no |
| 3 | **DUTY CYCLE of sustained compression (24 h vs 12 h)** | 0.1 MPa, 24/24 h vs 12/24 h day vs 12/24 h night, 8 d | Full-time loading suppressed growth MORE than intermittent: vertebra 82% (full) vs 93% (day) vs 90% (night) of control; tibia 70% vs 84% vs 86% | rat **PMID 15607892** | No | no |
| 4 | **Time-of-day of loading (day vs night)** | 12 h day vs 12 h night at 0.1 MPa | **No day/night difference** — the loading clock does not matter, only the hours | rat **PMID 15607892** | No | **yes** |
| 5 | **DYNAMIC/cyclic compression at an elevated MEAN stress** | mean 0.2 MPa, ±0.06 MPa at 1.0 Hz; ±0.2 MPa at 0.1 Hz; ±0.14 MPa at 1.0 Hz; 15 d implanted device | Growth rate REDUCED vs sham at both usable settings, **with growth-plate height, hypertrophic cell height and proliferative count all UNCHANGED**. Combined high magnitude + high frequency destroyed the tissue (inflammation) | rat caudal vertebra **PMID 24902946** | No | no |
| 6 | **INTERMITTENT cyclic loading returning to zero (physiological strain)** | cyclical "biologically relevant" strain, 4 wk, one tibia loaded, contralateral internal control | ⭐ **POSITIVE. Loaded tibiae significantly LONGER than unloaded**; plate height and area greater; PTHrP up in the loaded plate in FEMALES | mouse tibia **PMID 39090666** (McGarry 2024) | No | no |
| 7 | ⭐ **LATERAL / TRANSVERSE joint loading ("knee loading")** | **0.5 N, 5-min bouts/day**, piezoelectric loader across the knee, contralateral control | ⭐⭐ **POSITIVE AND THE LARGEST IN THE DOMAIN. Femur +2.3% vs contralateral / +3.5% vs age-matched; tibia +2.3% / +3.7%; all P<0.001.** Proximal tibial plate height **+19.5%**, plate cross-sectional area **+30.7%**; hypertrophic zone chondrocyte NUMBER and CELL HEIGHT both up | mouse (C57BL/6, ~8 wk) **PMID 19890688** | **NO — never tested in a human** | **yes** |
| 8 | ⭐ **LATERAL joint loading at the ELBOW (forelimb replication)** | 0.5 N class dynamic load, **5-min bouts/day × 10 d** | **POSITIVE: humerus +1.2%; ulna +1.7% vs contralateral, +3.4% vs age-matched.** c-fos/egr1/atf3 rose not only at the elbow but at the **wrist and shoulder of the loaded limb** | mouse **PMID 21748461** | No | **yes** |
| 9 | **Loading FREQUENCY for the lateral-joint modality** | 0.5 N at **5, 10, 15 Hz**, 3 min/day | Frequency-dependent bone FORMATION (proxy, not length). Establishes the effective band is 5–20 Hz | mouse tibia/femur **PMID 17968490** | No | **yes** |
| 10 | **Intramedullary pressure as the mediator of lateral joint loading** | knee loading, IM pressure measured directly | Knee loading **dynamically alters intramedullary pressure**; drilling holes that vent the medullary cavity modulates the response | mouse **PMID 17070127**, **PMID 17344109** | No | **yes** |
| 11 | **Load-driven interstitial fluid flow / molecular transport (FRAP in lacunocanalicular network)** | knee loading, 376 Da tracer | Loading drives molecular transport — the proposed non-strain mechanism for rows 7–8 | mouse femur **PMID 17029032** | No | **yes** |
| 12 | ⭐ **LOCAL LIMB HEATING (unilateral, targeted)** | **40 °C, 40 min/day**, one side; contralateral side ~30 °C; 1–2 wk; weanling mice | ⭐ **POSITIVE: tibia ~+1%, femur ~+1.4% after ONE WEEK (both P<0.001); tibial elongation RATE +6%.** Up to **+1.5%** in the 2-week protocol. Functional: loaded-side weight bearing +20% | mouse **PMID 29915560**; **PMID 25639189** | **No** | **yes** |
| 13 | **Ambient (whole-body) TEMPERATURE during growth** | chronic housing at ~16 °C vs 25 °C from weaning | Warm-reared limbs permanently LONGER; effect is on the extremities (Allen's rule), acts by directly modulating cartilage growth, not only by selection | mouse **PMID 19047632**; review/index **PMID 24715562**; window **PMID 23956063** | No (ecological correlation only) | no |
| 14 | ⭐ **VOLUNTARY WHEEL RUNNING (chronic, high-volume) as a SOLUTE-DELIVERY intervention** | 11 days free wheel access, 16 °C or 25 °C housing | ⭐ **POSITIVE: ALL runners had significantly longer limbs regardless of temperature.** **TAIL length responded only to temperature** — the internal control proving the effect is LOCAL to loaded limb bones, not systemic endocrine. Multiphoton imaging showed **enhanced solute delivery to the tibial growth plate measured AT REST under anaesthesia** = a lasting vascular adaptation | mouse **PMID 20930127** | **No** | **yes** |
| 15 | **Temperature-dependent solute transport into growth-plate cartilage** | in vivo multiphoton, tracer size series | Temperature alters solute delivery to the plate; provides the quantitative method | mouse **PMID 19372302** | No | **yes** |
| 16 | **PERIOSTEAL STRIPPING (circumferential, mid-diaphyseal)** | full diaphyseal strip, single operation | **POSITIVE BUT TRANSIENT: femur only 1.5% longer at 4 weeks (P<0.001), NOT maintained**; diaphyseal diameter progressively NARROWER at every timepoint | rat, n=70+70 **PMID 2071281** | see rows 18–19 | no |
| 17 | **PERIOSTEAL DIVISION — site dependence** | proximal release vs distal release vs full diaphyseal strip | **PROXIMAL (adjacent to the target physis) division was the most effective** of the three | rat tibia **PMID 3680349**; chondrocyte kinetics **PMID 3654353** | — | **yes** |
| 18 | **PERIOSTEAL DIVISION combined with compression or distraction** | 1 kg compression or distraction ± circumferential periosteal division + 1 cm strip, 6 wk | Periosteal division **enhanced growth at the ADJACENT plate and INHIBITED it distally**; it **amplified distraction and blunted compression**. Authors conclude the mechanism is at least partly MECHANICAL (release of a periosteal tether) | rabbit **PMID 2312573** | — | **yes** |
| 19 | **PARTIAL / hemicircumferential periosteal division** | longitudinal vs hemicircumferential incision | Hemicircumferential incision → 1–2 mm overgrowth **plus 5–10° valgus and an S-shaped deformity**; direction of the cut determines the deformity → supports the mechanical (not humoral) theory | rabbit **PMID 3180580** | — | **yes** |
| 20 | **PERIOSTEAL STRIPPING — HUMAN, post-polio limb shortening** | long lower-limb bones, 30 children, 5-year follow-up | **Relative length increase in the majority**, but the response was **haphazard and unpredictable**; recommended only for minor discrepancy | **HUMAN, n=30 children, PMID 1194317** | **YES** | **yes** |
| 21 | **PERIOSTEAL STRIPPING + DIVISION (PSPD) — HUMAN, modern controlled series** | PSPD at implant removal; 10 treated vs 6 declining controls; mean follow-up 4.3 y | **ΔLLD −13.9 mm vs −3.2 mm in controls (significant).** Age was the significant predictor; **cut-off 9.6 years** — >10 mm correction unlikely above ~10 y of age | **HUMAN, n=16, PMID 39502984** (Perthes LLD) | **YES** | **yes** |
| 22 | **Periosteal stripping — earlier large-animal work** | — | Title claims stimulation of longitudinal growth | dog + monkey **PMID 14083143** (1963, no abstract in PubMed — direction UNVERIFIED); rat **PMID 7586829**; beagle distal ulna **PMID NA (1987, EPMC record, no PMID)** | — | **yes** |
| 23 | **VIBRATION — whole-body / low-magnitude high-frequency (LMHF), animal** | 50 Hz, 0.5 g, 15 min/day, 5 d/wk, 5 or 10 wk, from 5 wk of age | **NO length effect reported.** Cortical BMC and cortical area rose at 5 wk; "bone size" was measured but only cortical geometry reported. A bone-MASS result | rat tibia **PMID 36384427** | see rows 24–25 | no |
| 24 | ⭐ **VIBRATION — the ONLY registered HUMAN trial with a BONE-LENGTH primary outcome** | **LivMD platform, 30 Hz, 0.4 g vs 1.0 g, 15 min, 3×/wk × 10 wk**; shorter leg on the plate, longer leg on a static block; 4 mo pre / 3 mo treat / 6 mo post; laser+ultrasound leg length monthly | **UNKNOWN — trial status UNKNOWN, n=40 planned, NO RESULTS POSTED** | **HUMAN, children 6–12 y with leg-length discrepancy. NCT03666975, University College London** | **YES (registered, unreported)** | **yes** |
| 25 | **VIBRATION — 1980 dog experiment** | mechanical vibration to a growing dog limb | **Title says "Attempt to…" — no abstract in PubMed, direction UNVERIFIED** | dog **PMID 7421329** (Med Biol Eng Comput 1980) | No | **yes** |
| 26 | **Low-intensity vibration in a paediatric disease population** | 0.4 g, 30 Hz, 10 min/day, 14 months | Trabecular tibial BMD preserved/raised; **no length endpoint** | **HUMAN, boys with Duchenne MD** (randomised, placebo-controlled) — see WebSearch source below | Yes (bone mass only) | no |
| 27 | **THERAPEUTIC ULTRASOUND applied over an open physis** | 0.5 W/cm² (therapeutic) vs 2.2 W/cm² (~45× dose), 20 min/day × 6 wk, over the knee | **HIGH dose = pathological: epiphyseal flattening, tibial plateau wedging, disordered proliferative zone, lateral physis height 1084 µm vs 500 (therapeutic) vs 531 (contralateral).** Therapeutic dose no adverse effect short-term | rabbit, 6 wk old **PMID 12919875** | No | no |
| 28 | **THERAPEUTIC ULTRASOUND — systematic review of physeal effects** | 8 animal studies | High dose → necrosis + growth inhibition; **LOW dose → transient STIMULATORY effect on growth, thicker hypertrophic zone, thicker whole plate**. No human growth disturbance reported; review recommends avoiding the physis | INDEX (review) **PMID 34958326** | No | **yes** |
| 29 | ⭐ **RADIAL EXTRACORPOREAL SHOCKWAVE (rESWT) directly on the growth plate** | single application; low 500 imp/5 Hz/90 mJ, mid 500/5 Hz/120 mJ, **high 500 imp/10 Hz/180 mJ**; 14 d culture | ⭐ **POSITIVE LENGTH ENDPOINT: high-dose bone length 4.46 ± 0.75 mm vs control 3.50 ± 0.38 mm, p=0.01**; proliferative chondrocyte number up. Explicitly avascular/ex vivo, so the effect is LOCAL and not systemic-GF-dependent | **fetal rat metatarsal organ culture** (Sävendahl lab) **PMID 31794485**; commentary **PMID 32011380** | No | **yes** |
| 30 | **PULSED ELECTROMAGNETIC FIELD (PEMF) during limb lengthening — HUMAN, double-blind** | active vs inactive coil, 13 patients (mean age ~12–13 y), Villarubbias lengthening | **NO effect on the rate or amount of regenerate bone.** DID prevent disuse bone LOSS distal to the gap (BMD −10% vs −33% at 2 mo). **No length endpoint** | **HUMAN, n=13 children/adolescents, PMID 8805989** | **YES (regenerate, not stature)** | no |
| 31 | **PEMF during limb lengthening — animal** | 1 h/day low-amplitude, rabbit tibial distraction 0.25 mm ×2/day × 21 d | Regenerate maturation endpoints; no stature endpoint | rabbit **PMID 12826946**, **PMID 16419963**; high-slew-rate variant **PMID 34872332** | Clinical series **PMID 16305082** | no |
| 32 | ⭐ **DIRECT CURRENT applied to the epiphyseal plate** | **5 µA constant DC**, implanted subcutaneous stimulator, 2 wk, contralateral dummy electrodes | **Plate height 1.0 ± 0.4 mm vs 0.6 ± 0.2 mm control (significant); mineral apposition rate 4.6 vs 3.0 µm/day.** Authors: epiphyseal cartilage growth is ACCELERATED by DC. **No bone-length endpoint** | rabbit proximal tibia **PMID 1918270** (Japanese) | No | **yes** |
| 33 | **Non-invasive AC electrical stimulation of the epiphyseal plate — PATENT** | 2.5–15 V p-p at 20–100 kHz, surface electrodes | Claimed physeal stimulation. **PATENT, not a study — no data** | patent record, EPMC 1984, no PMID | No | **yes** |
| 34 | **LOW-LEVEL LASER THERAPY over the femoral physis** | GaAlAs 830 nm, 40 mW, 10 J/cm², one point, daily up to 21 d | **NEGATIVE: percentage femoral longitudinal length LOWER in the irradiated group at day 21.** Calcified cartilage zone and angiogenesis increased (i.e. accelerated closure direction) | rat **PMID 22378365** | No | **yes** |
| 35 | **LOW-LEVEL LASER THERAPY, 670 nm, dose series** | 4, 8 and 16 J/cm², right tibia, contralateral control, followed to 14 wk | **NULL on limb length and on all plate histology at every dose** | rat **PMID 22654576** | No | **yes** |
| 36 | **HYPERBARIC OXYGEN during distraction osteogenesis** | 2.5 ATA, 2 h/day; also tested against accelerated (2 mm/day) distraction | Improves regenerate BMD/torsional strength and mitigates smoking; **HBO permitted an ACCELERATED distraction rate in mandible**. **No physis, no stature endpoint** | rabbit **PMID 9555841**, **PMID 10528613**; muscle **PMID 18040699**; accelerated rate **PMID 19200793** | No | no |
| 37 | **SPACEFLIGHT / true microgravity — animal longitudinal growth rate** | 4–14 day flights (PSE 1/3/4, PARE 3, COSMOS 2044) | **Skeletal unloading generally did NOT change longitudinal growth rate**, regardless of age, strain, sex, duration or method — one exception, −34% in slow-growing ovariectomised rats hindlimb-elevated 8 d. Col2 mRNA −33%, aggrecan −53% after 11-d flight | rat **PMID 11033449**; plate histomorphometry **PMID 1526950** | No | no |
| 38 | **HINDLIMB UNLOADING (tail suspension) — the ground analogue** | 5–21 d suspension | Longitudinal growth rate largely unaffected (row 37); tail-suspended controls did **not** differ from other controls on plate histomorphometry. Bone MASS falls | rat **PMID 11033449**, **PMID 1526950**, **PMID 11907715** | No | no |
| 39 | **Axial tibial loading superimposed on hindlimb unloading** | ~800 µε target strain, in vivo axial loading of one tibia in suspended rats | Discordant response of composition vs mechanical properties; **no length endpoint** | rat **PMID 29855437** | No | no |
| 40 | **HUMAN spinal elongation in microgravity / dry immersion** | days–months of axial unloading | **Spinal elongation is a recognised effect of microgravity** and is accompanied by back pain and raised post-flight disc herniation risk. It is DISC water/geometry, not physeal growth | **HUMAN astronauts** — reviews (INDEX) **PMID 29403389**, **PMID 28962911**; dry immersion **PMID 36311233** | **YES** | no |
| 41 | **DIURNAL stature variation (disc creep and rehydration)** | 24 h cycle; static shoulder loads 2.5–40 kg; repetitive lifting | **Mean circadian variation 19.3 mm = 1.1% of stature; 54% of the loss in the FIRST HOUR after rising; ~70% regained in the first half of the night.** Shrinkage rises NON-linearly with load; **repetitive lifting shrinks more than the equivalent static load**; Fowler's position recovers faster than standing | **HUMAN, n=8 adults, PMID 4002039**; ankylosing spondylitis **PMID 23915708**; heel-pad artefact **PMID 15676749** | **YES** | no |
| 42 | **Diurnal stature loss in CHILDREN + the "stretched" measurement technique** | measured 0900/1100/1300/1500, stretched vs unstretched | Loss 0.31 cm (0900→1100) and 0.20 cm (1100→1300), **no further loss after ~6 h up**. **Stretching did NOT reduce diurnal loss** but added 0.28 cm to the recorded height. Afternoon appointments recommended | **HUMAN, 53 children, PMID 9389235** | **YES** | **yes** |
| 43 | **SLEEP DEPRIVATION and the stature rhythm** | one night of deprivation | **Decreased stature and blunted the 24-h rhythm** in young and middle-aged men; regained on the first recovery night. The rhythm is driven by RECUMBENCY, not an endogenous clock | **HUMAN, PMID 4076396** | **YES** | **yes** |
| 44 | ⭐ **SWIMMING (non-weight-bearing exercise) in growing animals** | 35 °C water, 1 h/day, 5 d/wk, **20 weeks**, from 5 wk of age; ± 1% body-weight lead load | ⭐ **POSITIVE LENGTH ENDPOINT: humerus bone LENGTH +2.8%** (with bone weight +19%, volume +11%, cortical area +16%, BMD +7%), **irrespective of added load** | rat, n=40 **PMID 2804453** | No | **yes** |
| 45 | **SWIMMING — growth-plate histomorphometry** | 1 h/day, 5 d/wk × 12 wk, 12-wk-old rats | Increased column cell number and proliferative cell number in the plate, femur > humerus | rat **PMID 7547437** | No | **yes** |
| 46 | **TREADMILL running in young growing rats** | 25 m/min, 1 h/day, 5 d/wk, 7 or 11 wk | Femoral LENGTH was measured. Bone-mass endpoints reported; length effect not the headline (**direction UNVERIFIED from abstract**) | rat **PMID 14691683** | No | no |
| 47 | **BIPEDAL walking / standing imposed on a quadruped (loading history)** | treadmill-harness, 12 wk, 5 conditions: fully-loaded biped walk, partially loaded, standing, quadrupedal, control | **Percentage change in tibia and femur length differed for fully-loaded bipedal walking and bipedal standing; NO absolute length differences** — authors conclude loading moderates growth VELOCITY not final length | rat **PMID 30730948** | No | **yes** |
| 48 | ⭐ **HIGH-IMPACT JUMPING in short-stature children (controlled trial)** | **3 sessions/wk, 50 min/session, 24 weeks**, progressive jumping | ⭐ **HEIGHT GAIN 4.200 cm vs 2.478 cm in controls, p=0.001**; femoral-neck BMD Z +1.075. ⚠ Mediation analysis internally incoherent (indirect effect via BMD **NEGATIVE**, β=−0.442, no direct effect) | **HUMAN, 47 prepubertal children 8–11 y, PMID 41233903** (non-randomised; ChiCTR2500095544) | **YES** | no |
| 49 | **Same jumping trial, endocrine arm** | as row 48 | IGF-1 and IGF-1/IGFBP-3 molar ratio ROSE, **IGFBP-3 FELL, serum GH UNCHANGED** — i.e. an IGF-BIOAVAILABILITY effect, not a somatotroph effect | **HUMAN, PMID 40597964** (same registration; group sizes differ between the two reports) | **YES** | no |
| 50 | **JUMPING in normal children — bone endpoints only** | 100 jumps/day 3×/wk (Fuchs) ; 25 jumps/day from 45 cm box 5 d/wk × 12 wk (Gunter) | Hip and spine BMC gains; height used as a COVARIATE. **No analysed height endpoint** | **HUMAN, randomised, PMID 11149479, PMID 14555256** | **YES (height measured, unanalysed)** | no |
| 51 | ⭐ **GYMNASTICS — the human natural experiment, and it splits by discipline** | ≥ years of elite training from early childhood | **Elite male artistic gymnasts: final height SDS BELOW genetic target; final height correlated NEGATIVELY with training intensity (r=−0.252, p=0.022).** Elite female ARTISTIC gymnasts also below target; elite female RHYTHMIC gymnasts **EXCEEDED** target height | **HUMAN, n=86 males PMID 22768655; n=215 RG + 113 AG PMID 22450345** | **YES** | no |
| 52 | **Compressive repetitive loading through a SMALL joint (gymnast wrist)** | weight-bearing on the upper limb during growth | **Distal radial physeal injury with acquired POSITIVE ULNAR VARIANCE** — an internally controlled human demonstration that repetitive compression through a small joint arrests a physis | **HUMAN, PMID 16493174** | **YES** | no |
| 53 | **Detraining after impact exercise** | treadmill running or jump training then detraining, 90 male Wistar rats | Trabecular microarchitecture endpoints; persistence after detraining. **No length endpoint** | rat **PMID 42204782** | No | no |
| 54 | ⭐ **FEMORAL FRACTURE OVERGROWTH (the injury/hyperaemia lever)** | diaphyseal fracture in a growing child | ⭐ **HUMAN LENGTH GAIN WITHOUT ANY DRUG: mean femoral overgrowth 10.5 ± 7.3 mm after internal fixation** (ESIN 9.9 vs MIPO 11.2 mm, ns); greater in length-UNSTABLE fractures (12.3 vs 9.2 mm, p=0.048). Separately, overgrowth avg **1.17 cm in the first 18 months** in 77.4% of children; greater with proximal-third fractures and age <8 y | **HUMAN, n=87 PMID 31567782; n=62 PMID 11989577; also PMID 26201394, 9917716, 6952854, 40785768** | **YES** | no (as a complication) / **yes as a lever** |
| 55 | ⭐ **SURGICALLY INDUCED ARTERIOVENOUS FISTULA to lengthen a limb** | AV fistula created in the shorter leg | Four human papers 1961–1974 on the effect on leg length, incl. **10-year observations** — **direction and magnitude UNVERIFIED (no abstracts in PubMed for any of them)** | **HUMAN, PMID 13789389 (1961), PMID 5888999 (1963), PMID 14119083 (1964), PMID 4822516 (1974)** | **YES** | **yes** |
| 56 | **EXPERIMENTAL VENOUS LIGATION (venous stasis) and bone growth** | ligation of limb veins | Bone growth and blood flow measured together — **direction UNVERIFIED, no abstract** | rabbit/rat **PMID 5547971** (J Anat 1971) | No | **yes** |
| 57 | **TEMPERATURE and bone growth in the CHICK (early comparative work)** | — | Companion to the Serrat/Allen's-rule line; **no abstract, UNVERIFIED** | chick **PMID 4116029** (J Anat 1972) | No | **yes** |
| 58 | **HEMIEPIPHYSIODESIS / GUIDED GROWTH (tension-band plate, "8-plate", staples, transphyseal screw)** | eccentric compression across one half of a physis until correction | **The clinical proof that Hueter–Volkmann is exploitable in humans.** ~0.7°/month correction rate in the femur; tension-band plating ≈ stapling on treatment time (randomised) | **HUMAN, PMID 20130322, 17414005, 23485073 (RCT), 36461004** | **YES** | no |
| 59 | **REBOUND after temporary hemiepiphysiodesis** | implant removal after correction | Rebound growth is common and its risk factors are age, correction rate and residual growth; rabbit model quantifies incidence and chronology | **HUMAN, PMID 35142715, 35395849, 32732797, 33422021, 37799311**; rabbit **PMID 26033070** | **YES** | no |
| 60 | ⭐ **VERTEBRAL BODY TETHERING (anterior spinal growth modulation)** | flexible tether under tension across the convexity | **Measured DIFFERENTIAL SEGMENTAL GROWTH of vertebrae in vivo — 51 patients, 764 vertebrae**; concave-side vertebral growth magnitude is the primary determinant of response; maintained at 4 years across 888 peri-apical vertebrae | **HUMAN, PMID 35064912, 38634997, 38834863, 32618924** | **YES** | no |
| 61 | **GROWING RODS / magnetically controlled growing rods (axial distraction of the spine)** | repeated lengthenings; frequency varied | **Frequency of lengthening affects the height achieved** (dual growing rod series). Direct human axial distraction with a length endpoint (T1–S1) | **HUMAN, PMID 18427320, 16138066, 23060057** | **YES** | no |
| 62 | ⭐ **HALO-GRAVITY TRACTION (sustained axial spinal traction in children)** | halo + progressive weights, weeks to months, preoperative | Substantial radiographic correction of severe deformity and improved pulmonary function. **Height/T1–S1 gain is real but is deformity correction, not physeal growth** | **HUMAN, PMID 27927320, 35577210 (meta-analysis), 21954764** | **YES** | no |
| 63 | **CHONDRODIATASIS (slow symmetric distraction THROUGH an open physis)** | ~0.25 mm ×4/day or less, dynamic axial fixator, physis still open | **Length gains up to 36% (LLD) and 64.5% (achondroplasia) of segment length**, 170 segments in 75 children. ⛔ Mechanism is NOT stimulation of the plate — thymidine labelling, sulfate labelling and microcirculation all UNCHANGED in rabbit. ⛔ **Premature physeal closure with LOSS of gained length in 5/5 femora <13 y** | **HUMAN, PMID 3733829, 2924455, 11961457, 1590047**; rabbit mechanism **PMID 1552021** | **YES** | **yes** |
| 64 | **Ilizarov DISTRACTION RATE and RHYTHM (the classic parameter study)** | rates 0.5 / 1.0 / 2.0 mm per day × frequencies **1, 4 or 60 steps per day**; open osteotomy vs closed osteoclasis | Osteogenesis quality depends on BOTH rate and frequency; higher subdivision of the same daily rate is better. Companion paper: fixation stability and **periosteal/medullary preservation** matter | dog tibia **PMID 2912628** (Part II) and **PMID 2910611** (Part I); clinical **PMID 2403497** | Clinical | no |
| 65 | **Supraphysiological distraction rate + drug rescue** | 10 mm lengthening at above-standard rate ± intermittent teriparatide, rabbit tibia, n=24 | Feasibility of raising the rate without losing regenerate quality — the rate limiter is regenerate biology, not the bone | rabbit **PMID 40657227** | No | **yes** |
| 66 | **DISTRACTION EPIPHYSIOLYSIS (rapid physeal separation, distinct from chondrodiatasis)** | high-rate distraction that fractures through the hypertrophic zone | A lengthening method with defined experimental, morphological and clinical series; forces monitored continuously | rabbit + **HUMAN, PMID 7471563 (I, experimental), 7009012 (II, morphology), 7471565 (III, clinical), 1561874, 3392584** | **YES** | **yes** |
| 67 | **DIRECT CURRENT during distraction epiphysiolysis** | **20 µA**, cathode in the elongation zone, 3 wk | **NULL — no effect on bone formation in the elongated zone** | rabbit **PMID 2388116** | No | **yes** |
| 68 | **Electromagnetic stimulation after distraction epiphysiolysis** | PEMF | Bone growth and remodelling after distraction epiphysiolysis (**direction UNVERIFIED**) | rabbit **PMID 2019066** | No | **yes** |
| 69 | ⭐ **DENERVATION / PARALYSIS (removal of muscle force) — the negative control for all of the above** | unilateral sciatic nerve transection at P8 | ⭐ **Tibiae significantly SHORTER at 8 and 14 wk; growth-plate columns FEWER and SHORTER; collagen fibre and actin cytoskeleton organisation disrupted** — establishes that ordinary muscle force is REQUIRED for normal column formation and full length | mouse **PMID 28539407** | No (analogue: CP, spina bifida) | no |
| 70 | **Fetal immobilisation / absent skeletal muscle** | Splotch-delayed mouse, no skeletal muscle | Reduced mineralisation, altered tuberosity, **decreased chondrocyte density, size and elongation** in the growth plate | mouse embryo **PMID 33454374** | No | no |
| 71 | **Botulinum toxin muscle paralysis and bone growth** | masseter injection in developing rats | Reduced mandibular bone growth; a chemical route to the same mechanical lesion as row 69 | rat **PMID 29588910**; facial **PMID 17433895** | Used clinically in CP | **yes** |
| 72 | **LOADING FREQUENCY on isolated growth-plate chondrocytes (in vitro)** | intermittent TENSILE stress at varied frequency; rib growth-plate chondrocytes, proliferating (d4) and matrix-forming (d11) | **DNA synthesis up at 30 and 150 cycles/min (0.5 and 2.5 Hz); collagen and proteoglycan synthesis rose WITH frequency.** A dose-response in the frequency dimension that has never been taken in vivo | rat **PMID 18278554** | No | **yes** |
| 73 | **HIGH-MAGNITUDE loading on human growth-plate chondrocytes** | physiological vs near-detrimental vs detrimental loads, 2 h | MMP expression rose at high loads — proposed mechanism for paediatric overuse physeal injury | **HUMAN growth-plate chondrocytes, PMID 23539713** | Ex vivo human | **yes** |
| 74 | ⭐ **Precisely controlled loading of intact HUMAN growth-plate biopsies** | microloading device on biopsies taken at epiphysiodesis, RNA-seq 24 h later | The only genomic read-out of mechanical loading in **human** growth-plate cartilage. Pilot study | **HUMAN tissue, PMID 39655393** | Ex vivo human | **yes** |
| 75 | **HYDROSTATIC PRESSURE on growth-plate cartilage** | physiological vs injurious HP, ex vivo explants, RNA-seq; and 1–10 MPa 1 Hz in chondrocytes | Physiological HP is chondroprotective/chondroinductive; injurious HP is degradative. **HP prevents chondrocyte differentiation via heterochromatin remodelling** — i.e. it holds cells in the chondrocyte state | mouse growth-plate + articular explants **PMID 38144567**; **PMID 33310912**; human chondrocytes **PMID 12507587** | No length endpoint | **yes** |
| 76 | **Coupled hydrostatic-pressure + THERMAL stimulus** | HP with a transient temperature rise 32.5→38.7 °C | HSP70-mediated; the combined stimulus is more chondroinductive than either alone. **Links the mechanical and thermal arms (rows 12–15) at the cell level** | chondrocytes **PMID 38679285** | No | **yes** |
| 77 | **TORSIONAL SHEAR of the growth plate** | torsional loading, 140 samples, 3 plates, 5 pigs | Microstructural and mechanical properties under torsion; torsion is associated with physeal FRACTURE, not growth gain | pig **PMID 40834615** | No | **yes** |
| 78 | **Trans-physeal mineralised BRIDGES as mechanical "base isolation"** | native anatomy | Proposes that physeal bridges exist to minimise epiphyseal SHEAR — a structural constraint on how much shear a plate can be given | preprint/record, **PMID NA (2026 EPMC record, no PMID) — UNVERIFIED** | No | **yes** |
| 79 | **REST INSERTION between load cycles** | 10-s rest inserted between cycles; and loading duration × rest insertion factorial | **Rest insertion combined with high-frequency loading ENHANCES osteogenesis**; cortical response saturates quickly without it. **Bone-formation endpoints only — never tested on a growth plate** | mouse tibia **PMID 14707150**, **PMID 28076363** | No | **yes** |
| 80 | **LOADING FREQUENCY for cortical bone formation (adult)** | 1–10 Hz at matched strain, rat ulna | Frequency modulates bone-formation rate. Establishes the frequency-response shape in the bone (not cartilage) compartment | rat **PMID 11341337** | No | no |
| 81 | **LIPUS on the MANDIBULAR CONDYLE (a secondary growth cartilage)** | 20 min/day × 20 or 28 days, unilateral or bilateral | 20 min > 10 min; stimulates chondrogenesis AND osteogenesis and enhances endochondral bone formation; gross condylar dimension change non-significant. **A dose-response exists for LIPUS on a growth cartilage** | rat **PMID 19705932**, **PMID 34527791** (erratum **PMID 38163011**) | No | **yes** |
| 82 | **LIPUS during distraction osteogenesis (consolidation)** | standard LIPUS protocol during/after distraction | Enhances callus consolidation (regenerate endpoint). Combined with BMP-2 in rats | **HUMAN tibia lengthening-over-nail (PMC6419405, PMID UNVERIFIED)**; rat **PMID 35594008** | Yes (regenerate) | no |
| 83 | **INVERSION THERAPY / inversion tables** | 30–60° tilt, minutes | **NO peer-reviewed height endpoint exists.** The indexed literature is renal-calculus clearance, lumbar disc symptoms, EMG relaxation and **cervical cord injury from falls**. Commercial height claims rest on transient disc rehydration (row 41) | **HUMAN, PMID 22263648, 34776613, 27190459; harm PMID 33922070** | Yes (not for height) | **yes** |
| 84 | **CHIROPRACTIC "vibration traction" / spinal decompression for DISC HEIGHT** | multimodal rehabilitation + vibration traction, retrospective case series | Radiographic disc-height increase claimed; uncontrolled case series | **HUMAN, PMID 19646376** | Yes (very weak) | **yes** |
| 85 | ⭐ **YOGA / intensive asana practice in growing girls** | habitual intensive practice, cross-sectional, n=757 | **NEGATIVE: mean stature and LEG LENGTH significantly LOWER in the yoga group at ages 10–12**; authors attribute it to greater skeletal stress. Cross-sectional, selection-confounded | **HUMAN, n=757 girls 4–15 y, PMID 35255268** | **YES** | **yes** |
| 86 | **MASSAGE / tactile-kinaesthetic stimulation in preterm infants** | 15 min × 3/day, moderate pressure, days–weeks | Robust weight-gain effect (multiple RCTs + meta-analyses); **effect on LENGTH is inconsistently reported and usually not the primary outcome.** Exercise (passive limb flexion-extension) works through a different mechanism from stroking | **HUMAN preterm infants, PMID 37224588 (meta), 32379694 (meta), 32666281, 24480603, 23062248, 15106151 (Cochrane)** | **YES** | no |
| 87 | **Kangaroo mother care vs massage** | skin-to-skin vs massage | Compared head-to-head on weight and length of stay | **HUMAN, PMID 24976830** | **YES** | no |
| 88 | **Plantar vibration during disuse** | plantar vibration in tail-suspended rats | Bone and deep-fascia endpoints; no length | rat **PMID 29875702** | No | **yes** |
| 89 | **Whole-body vibration + IGF-I after botulinum paralysis** | WBV plus IGF-I | Bone degeneration endpoints; no length | mouse **PMID 24292598** | No | **yes** |
| 90 | **STATIC MAGNETIC FIELD on bone/cartilage** | 180 mT to 1–2 T | Bone formation orientation, chondrogenic differentiation of MSCs, OA cartilage repair. **No growth-plate or length endpoint in any species found** | rat/in vitro **PMID 12369785, 24506272, 36721767, 20953437** | No | **yes** |
| 91 | **PIEZO1 / primary cilium as the transducer of compressive stress at the physis** | compressive loading, AIS models | PIEZO1–primary cilium axis mediates compressive-stress-induced growth-plate degeneration and ossification; PIEZO1–GPX4/ferroptosis in vertebral plate dysplasia | mouse/human AIS **PMID 41194970**, **PMID 40714837** | Human tissue | no |
| 92 | **Primary cilium transduces HYDROSTATIC loading of Ihh signalling** | hydrostatic loading of growth-plate chondrocytes | Cilia modulate Ihh signal transduction in response to hydrostatic load — a mechanical→morphogen link at the plate | **PMID 21930256** | No | **yes** |
| 93 | **SUSTAINED TENSILE DISTRACTION of vertebrae + disc (growing-rod analogue)** | sustained tension, mouse tail model | In vivo mechanobiology of vertebral and disc growth under sustained tension | mouse **PMID 40179155** | Analogue of human growing rods | **yes** |
| 94 | **FOOT PROGRESSION ANGLE / gait modification as a non-invasive growth-plate load lever** | altered foot progression angle, musculoskeletal + FE modelling | Changes hip contact forces and **femoral growth-plate mechanics** in children — a zero-cost, zero-device way to change physeal loading. **Modelling only, no growth endpoint** | **HUMAN modelling, PMID 42131502** | Modelling | **yes** |
| 95 | **Bipedal/quadruped joint-load ontogeny and cam morphology** | altered hip loading during growth | Growth plate reorients to minimise shear; altered hip loading predicts cam deformity — proof that habitual load direction shapes physeal ORIENTATION | **HUMAN/FE, PMID 31712938, 42324072** | Modelling | no |
| 96 | ⭐⭐ **RECUMBENCY as the permissive state for elongation (implanted microtransducers)** | continuous sampling every 167 s for 21–25 days, immature lambs, free-ranging | ⭐ **AT LEAST 90% OF BONE ELONGATION OCCURS DURING RECUMBENCY AND ALMOST NONE DURING STANDING OR LOCOMOTION.** The single most decision-relevant mechanical fact in the domain: growth is mechanically GATED by unloading, in real time | lamb **PMID 15502578** | No (hypothesised for children; the "growing pains" link) | **yes** |
| 97 | ⭐ **PERIOSTEAL RESECTION measured in REAL TIME with microtransducers** | proximal tibial periosteal resection, 5 lambs, 10 µm resolution, up to 7 wk | ⭐ **Growth velocity increased in EVERY lamb at EVERY timepoint, immediately and sustained.** Mechanism identified: **AXIAL ELONGATION OF THE HYPERTROPHIC CHONDROCYTE**, not proliferation, not swelling magnitude, not matrix. Authors propose it as an adjunct to counteract the growth INHIBITION of distraction osteogenesis | lamb **PMID 19098649** | See rows 20–21 | **yes** |
| 98 | **PERIOSTEAL RESECTION combined with guided growth** | modular plate ± periosteal resection, 16 lambs | Adding periosteal resection made the guided-growth construct significantly more efficient (2.5°/mm faster deformation) — i.e. **the two mechanical levers, growth retardation and growth acceleration, are ADDITIVE** | lamb **PMID 27159337** | No | **yes** |
| 99 | **MICROWAVE THERMAL ABLATION of the physis (minimally invasive epiphysiodesis)** | 65 W, 90–270 s, antenna adjacent to the proximal tibial plate | Thermal destruction of the plate to ARREST growth — the deliberate opposite direction, and proof that a percutaneous thermal device can reach and change a physis | pig, in vivo **PMID 38471002** | No | **yes** |
| 100 | **Guided growth of the PROXIMAL FEMUR** | screw/plate constructs, lamb pilot | Extends growth modulation beyond the knee | lamb **PMID 20864854**; construct comparison **PMID 22327457**; fatigue failure **PMID 26523701** | **YES (clinical technique)** | no |
| 101 | **Asymmetric physeal loading as a Blount-disease model** | asymmetrical loading of the lamb plate | Mechanical behaviour of the physis under asymmetric load; the experimental basis of the clinical deformity | lamb **PMID 17585254**; MMP12 after asymmetric loading, rat tail **PMID 25224255** | Analogue | no |
| 102 | **PREOPERATIVE COTREL DYNAMIC TRACTION for scoliosis** | longitudinal traction ± exercises ± casting | Historical randomised pilot and several series; correction endpoints only. **No stature endpoint** | **HUMAN, PMID 350002 (randomised pilot), 863946, 7180401, 7319770** | **YES** | **yes** |
| 103 | **Skull-tongs femoral traction vs Cotrel traction** | axial skeletal traction | Head-to-head for rigid severe scoliosis; correction endpoints | **HUMAN, PMID 33664953** | **YES** | **yes** |
| 104 | **Dynamic (spring-loaded) growth rod** | continuous rather than staged distraction | A device explicitly designed to allow continuous spinal growth modulation rather than intermittent surgical distraction | animal/bench **PMID 39801572** | Not yet | **yes** |
| 105 | **Computational / FE models of physeal growth modulation** | sustained load models; tension-band plate FE; foot-progression FE | Predict proliferative/hypertrophic zone response and validate against the Stokes dose-response. **Models, not experiments** | **PMID 23009361, 37415789, 8262991, 42131502** | Modelling | no |
| 106 | **Chondron curvature / strain distribution under compression** | compressive loading of intact physis | Maps the strain field the chondrocytes actually experience — the missing link between applied MPa and cell response | **PMID 29783204** | No | **yes** |
| 107 | **ESWT for proximal humeral epiphysiolysis in gymnasts** | ESWT applied to an injured physis | Rapid bone repair and pain relief in 1 of 2 cases; the other developed humeral SHORTENING | **HUMAN case reports, PMID 38883126** | **YES (n=2)** | **yes** |
| 108 | **Ultrasound (SMI) monitoring of children undergoing limb lengthening** | diagnostic, not therapeutic | Completed registry study — imaging, not an intervention | **HUMAN, NCT07026188** | Yes | **yes** |
| 109 | ⭐ **IDENTICAL cyclic load, TWO different bones, OPPOSITE length results** | **0.4 N at 0.77 Hz, 30 s bouts**, ex vivo culture, portable loading device | ⭐ **Fetal rat METATARSAL: loaded bones grew LESS than controls (p<0.05). Fetal rat FEMUR: same regimen, loaded bones grew SIGNIFICANTLY MORE (p<0.001).** The clearest evidence in the domain that the sign of the mechanical response is BONE-SPECIFIC, not universal | rat, ex vivo **PMID 37314663** (Sävendahl lab) | No | **yes** |
| 110 | **Endurance exercise and physeal vs articular cartilage in a large animal** | graded treadmill running, 17 weeks, 14 miniature pigs | Exercised humeral **PHYSEAL cartilage was THICKER** while articular cartilage was thinner; physeal response larger than articular; humerus responded more than femur. **No length endpoint** | miniature pig **PMID 22496283** | No | **yes** |
| 111 | **Aquatic treadmill / partial weight-bearing water immersion** | water depth sets percentage weight bearing | Establishes a graded, non-invasive way to set limb load in a human without a device — never used with a growth endpoint | **HUMAN, PMID 36196338, 25091034** | Yes (biomechanics only) | **yes** |
| 112 | **HEEL-PAD / soft-tissue compression as a confound on any stature measurement** | standing, equilibrium at ~82 s | Heel-pad compression alone contributes to measured stature; must be standardised in any height-intervention trial | **HUMAN, PMID 15676749** | **YES** | **yes** |
| 113 | ⭐ **EMBRYO MOVEMENT as a determinant of LIMB PROPORTIONS** | incubation temperature → motility; pharmacological immobilisation of chick embryos | **Altered movement changes limb PROPORTIONS and regulates chondrocyte proliferation in ONLY SPECIFIC growth plates** — selectivity determined by intrinsic **mTOR pathway activity in each individual plate**. A mechanism for why the same load gives opposite answers in different bones (row 109) | crocodile + chick **PMID 28165010** | No | **yes** |
| 114 | **"Chondral modelling theory" as the general framework** | habitual joint load | Predicts cartilage responds to habitual load; tested across joints in one animal and only partially supported | miniature pig **PMID 22496283**; growth-plate mechanobiology survey (INDEX) **PMID 19540500** | — | no |
| 115 | **Vertebral WEDGING: growth vs remodelling partition** | imposed 30° angulation + 0.1 or 0.2 MPa, three ages of rat | Wedging is partly asymmetric growth (Hueter–Volkmann) and partly diaphyseal remodelling (Wolff) — the two mechanical laws act simultaneously | rat **PMID 27927317**, **PMID 20543392** | Human modelling **PMID 17653775** | no |
| 116 | **Vertebral vs DISC contribution to spinal height growth** | stereoradiographs, ages 7.5–20 y | **Vertebral height growth PREDOMINATES over intervertebral disc height growth** in adolescents — bounds how much of trunk height any disc-directed mechanical intervention can reach | **HUMAN, PMID 16778695** | **YES** | **yes** |
| 117 | **Spinal curvature as a stature confound** | 407 radiographs, Cobb angle vs spinal length | Curvature makes measured stature underestimate spinal length; must be corrected before any height claim in a scoliotic subject | **HUMAN, PMID 18809998** | **YES** | **yes** |

---
## MODALITIES WITH A POSITIVE LENGTH ENDPOINT IN A NORMAL GROWING ANIMAL

This is the short list that matters. "Normal" excludes deficiency, dysplasia and injury models; "length"
excludes plate height, BMD, BMC and mineral apposition rate. Ranked by strength.

**1. LATERAL (transverse) JOINT LOADING — the largest effect in the domain, and it is nearly unreplicated.**
`PMID 19890688` (mouse, ~8 wk): 0.5 N, 5-min bouts/day across the knee →
**femur +2.3% vs contralateral / +3.5% vs age-matched; tibia +2.3% / +3.7%, all P<0.001**, with plate height
+19.5%, plate area +30.7%, and hypertrophic chondrocyte NUMBER and CELL HEIGHT both up (i.e. both the
amplification and the terminal-cell-size terms move). Replicated at the ELBOW by the same group
(`PMID 21748461`, humerus +1.2%, ulna +1.7–3.4%) with the transcriptional response propagating to the
**wrist and shoulder of the loaded limb**. The proposed mechanism is not strain but **intramedullary
pressure and load-driven interstitial fluid flow** (`PMID 17070127`, `PMID 17344109`, `PMID 17029032`).
⛔ NCBI elink returns **only 12 citing papers**, essentially all from the originating lab or adjacent;
**no independent group has reproduced the length endpoint, and it has never been done in a larger animal.**
⛔ The one registered human test of a related idea (row 24) has no results.

**2. LOCAL LIMB HEATING.** `PMID 29915560`, `PMID 25639189` (weanling mice): 40 °C for 40 min/day to one
side → tibia ~+1%, femur ~+1.4% after **one week** (P<0.001 both), elongation rate +6%, up to +1.5% over
two weeks, with a measurable functional consequence (+20% weight bearing on the treated side). Contralateral
internal control. The mechanism is solute delivery to an avascular tissue (`PMID 19372302`).

**3. CHRONIC VOLUNTARY WHEEL RUNNING.** `PMID 20930127`: **all runners had significantly longer limbs
regardless of housing temperature**, while **tail length responded only to temperature** — the internal
control that makes this a LOCAL effect and not a systemic endocrine one. Multiphoton imaging showed enhanced
growth-plate solute delivery **measured at rest under anaesthesia**, i.e. a lasting vascular adaptation
rather than a transient during exercise. This is the only modality here that plausibly multiplies the
delivery of every systemically administered agent as well as acting on its own.

**4. INTERMITTENT CYCLIC AXIAL LOADING THAT RETURNS TO ZERO.** `PMID 39090666` (mouse tibia, 4 wk, one limb
loaded): loaded tibiae significantly longer, plate height and area greater, PTHrP raised in the loaded plate
in females. Distinguish this sharply from rows 1–5: cyclic loading about an ELEVATED MEAN stress reduces
growth (`PMID 24902946`), whereas cyclic loading returning to zero increases it.

**5. SWIMMING (non-weight-bearing).** `PMID 2804453` (rat, 20 weeks, 1 h/day): humeral **bone length +2.8%**,
independent of an added 1% body-weight load, with bone weight +19%, cortical area +16%. Corroborated
histologically by increased column cell number and proliferative cell number (`PMID 7547437`).
Non-weight-bearing exercise raising bone length is a genuinely surprising result that has been ignored.

**6. PERIOSTEAL RESECTION / DIVISION.** `PMID 19098649` (lamb, real-time microtransducers, 10 µm resolution):
growth velocity increased **in every animal at every timepoint, immediately and sustained**, and the
mechanism is **axial elongation of the hypertrophic chondrocyte**, not proliferation. `PMID 3680349` shows
the effect is site-dependent (proximal division near the target physis is best). `PMID 2312573` shows it
amplifies distraction and blunts compression, i.e. it acts as a mechanical tether release. ⚠ `PMID 2071281`
found the rat effect (+1.5% femur) was **not maintained**; the lamb data say otherwise; the human data
(rows 20–21) say the response is real but haphazard and age-limited.

**7. RADIAL EXTRACORPOREAL SHOCKWAVE.** `PMID 31794485`: **4.46 ± 0.75 mm vs 3.50 ± 0.38 mm, p=0.01** at
500 impulses / 10 Hz / 180 mJ, in fetal rat metatarsal culture — explicitly avascular and systemic-GF-free,
so the action is local to the plate. ⚠ Fetal, ex vivo, one time point, and the same laboratory's portable
loader (`PMID 37314663`) shows that fetal metatarsals can respond to mechanics in the OPPOSITE direction
from fetal femurs.

**8. DIRECT CURRENT at the physis.** `PMID 1918270`: 5 µA for 2 weeks raised plate height 0.6→1.0 mm and
mineral apposition rate 3.0→4.6 µm/day in rabbit. **A proxy, not a length endpoint** — listed because the
dose is trivially small, the device is implantable and nobody has followed it up in 35 years.

**Negative or null in normal growing animals, recorded so they are not re-proposed:** low-level laser at
830 nm (femoral length LOWER, `PMID 22378365`) and at 670 nm across a 4× dose range (null, `PMID 22654576`);
whole-body vibration in growing rats (no length effect reported, `PMID 36384427`); direct current during
distraction epiphysiolysis (null, `PMID 2388116`); hindlimb unloading and spaceflight (longitudinal growth
rate largely UNAFFECTED, `PMID 11033449`); static magnetic fields (no length endpoint in any species).

---

## MODALITIES WITH A HUMAN HEIGHT ENDPOINT OF ANY QUALITY

**Positive, with a real length/height number:**
- **Periosteal stripping ± division.** `PMID 1194317` — 30 children, 5-year follow-up, relative length gain
  in the majority but "haphazard". `PMID 39502984` — 10 treated vs 6 controls, **ΔLLD −13.9 mm vs −3.2 mm**,
  with a hard age cut-off at **9.6 years**. This is the only *non-distraction* surgical growth stimulus with
  a controlled human comparison.
- **Femoral fracture overgrowth.** `PMID 31567782` — **10.5 ± 7.3 mm** mean femoral overgrowth in 87
  children; `PMID 11989577` — 1.17 cm in the first 18 months in 77.4% of 62 children, greater with
  proximal-third fractures and age <8 y. A human length gain produced by injury-driven hyperaemia, with no
  drug and no device.
- **High-impact jumping in short-stature children.** `PMID 41233903` — **height gain 4.200 vs 2.478 cm over
  24 weeks, p=0.001** (3×/wk, 50 min). ⚠ Non-randomised, single centre, and its own mediation analysis is
  internally incoherent (the indirect path via femoral-neck BMD is NEGATIVE with no direct effect); the
  companion report `PMID 40597964` gives different group sizes for the same registration (ChiCTR2500095544).
  Treat as hypothesis-generating.
- **Chondrodiatasis / distraction through an open physis.** `PMID 3733829`, `PMID 2924455` — up to 36% (LLD)
  and 64.5% (achondroplasia) of segment length across 170 segments in 75 children. ⛔ But `PMID 1590047`:
  premature physeal closure with **loss of the gained length in 5/5** femora under 13 years, and the rabbit
  mechanism study (`PMID 1552021`) shows the plate is NOT being stimulated — proliferation, matrix synthesis
  and microcirculation were all unchanged. The length comes from mechanical separation, and it is paid for.
- **Vertebral body tethering.** `PMID 35064912` — measured differential segmental growth across 51 patients
  and 764 vertebrae; `PMID 38634997` — maintained at 4 years across 888 peri-apical vertebrae. This is the
  cleanest human demonstration that Hueter–Volkmann growth modulation is exploitable and reversible.
- **Guided growth / hemiepiphysiodesis** (`PMID 20130322`, `PMID 23485073` RCT) and its **rebound**
  (`PMID 35142715`, `PMID 26033070`) — the negative direction, with a well-characterised dose-response.
- **Growing rods**: the **frequency of lengthening** affects the T1–S1 height achieved (`PMID 18427320`).
- **Halo-gravity traction** (`PMID 35577210` meta-analysis): substantial spinal-length/correction gains, but
  it is deformity correction, not physeal growth.

**Negative or null in humans:**
- **Elite artistic gymnastics**: final height SDS below genetic target in males, and **negatively correlated
  with training intensity** (r=−0.252, p=0.022, `PMID 22768655`); same direction in female artistic gymnasts,
  while female RHYTHMIC gymnasts EXCEEDED target height (`PMID 22450345`) — a within-sport dissociation that
  points at modality and energy availability rather than loading per se.
- **Gymnast wrist**: repetitive compression through a small joint produces distal radial physeal injury with
  acquired positive ulnar variance (`PMID 16493174`) — an internally controlled human arrest.
- **Intensive yoga**: stature and LEG LENGTH significantly lower at 10–12 y in 380 practising girls vs 377
  controls (`PMID 35255268`). Cross-sectional and selection-confounded, but it is the only height endpoint
  the stretching-modality literature has.
- **PEMF during limb lengthening** (`PMID 8805989`, double-blind): no effect on regenerate quantity or rate;
  it only prevented adjacent disuse bone loss.
- **Inversion tables / hanging / stretching devices**: **no peer-reviewed height endpoint exists at all.**
  The indexed inversion-therapy literature is renal-stone clearance, lumbar disc symptoms and cervical cord
  injury from falls (`PMID 33922070`). The commercial claims rest entirely on transient disc rehydration.
- **The "stretched" measurement technique** adds 0.28 cm to the recorded height and does NOT reduce diurnal
  loss (`PMID 9389235`) — a measurement artefact masquerading as a lever.

**Human measurement facts that bound every claim above:** diurnal stature variation is **19.3 mm = 1.1% of
stature, 54% lost in the first hour after rising** (`PMID 4002039`); most of the loss in children is over by
~6 h after rising, so afternoon measurement is preferable (`PMID 9389235`); one night of sleep deprivation
lowers stature and blunts the rhythm (`PMID 4076396`); heel-pad compression is a separate confound
(`PMID 15676749`); and spinal curvature makes stature underestimate spinal length (`PMID 18809998`).
**Any trial reporting a height effect smaller than ~2 cm without a fixed measurement time is uninterpretable.**

**Registered but unreported:** `NCT03666975` (UCL) — the only human trial anywhere with **bone length as the
primary outcome under a physical modality**: LivMD platform, 30 Hz, 0.4 g vs 1.0 g, 15 min, 3×/wk × 10 wk,
n=40 planned, triple-masked, 4 months pre / 3 months treatment / 6 months post. Status UNKNOWN, no results.

---

## THE PARAMETER SPACE NOBODY HAS EXPLORED

The domain has an unusual shape: the **magnitude** axis of axial compression is mapped to a coefficient
(17.1% growth-rate change per 0.1 MPa, `PMID 16705695`), and essentially **nothing else is mapped at all.**

**1. LOADING AXIS. This is the largest hole and it is not subtle.**
Axial compression at 4–17 N for tens of minutes a day SHORTENS bone. Transverse load at **0.5 N for 5 minutes
a day LENGTHENS it by 2–4%** — a ~30× smaller force, a ~10× shorter exposure, and the opposite sign. Yet the
entire clinical and exercise literature (walking, running, jumping, gymnastics, weight-bearing, bracing,
guided growth, distraction) is AXIAL. **No human activity, device or trial has ever delivered a transverse
oscillatory load across a growing knee**, and only one laboratory has done it in any species. Everything
downstream — dose, duration, age window, larger animals, humans — is unexplored because the axis is.

**2. FREQUENCY. Three disconnected fragments, no curve.**
- In vitro, tensile loading of growth-plate chondrocytes: DNA synthesis rose at **30 and 150 cycles/min
  (0.5 and 2.5 Hz)** and matrix synthesis rose WITH frequency (`PMID 18278554`).
- In vivo, lateral joint loading: bone FORMATION was frequency-dependent across **5, 10 and 15 Hz**
  (`PMID 17968490`) — but that experiment measured bone formation, **not length**. The length paper
  (`PMID 19890688`) reports a single condition.
- In cortical bone, frequency modulates formation rate across 1–10 Hz (`PMID 11341337`).
**Nobody has ever produced a frequency-vs-BONE-LENGTH curve in any species.** The two candidate optima
(~0.5–2.5 Hz from cartilage cells vs 5–20 Hz from the joint-loading device) differ by an order of magnitude
and have never been tested against each other on a length endpoint.

**3. DUTY CYCLE. Mapped for the harmful direction only.**
`PMID 15607892` gives the one clean duty-cycle experiment: halving sustained compression from 24 h to 12 h
recovered 11 points of vertebral growth and 14–16 points of tibial growth, **with no difference between day
and night loading**. That is the duty cycle of a *suppressive* load. **The duty cycle of a stimulatory load
has never been varied** — the lengthening protocols are all "5 minutes a day, daily", chosen and never
optimised. Is 5 min/day the plateau, the peak, or the left-hand limb? Unknown. Would 2 × 5 min beat 1 × 10?
Unknown. Is daily necessary, or does alternate-day work? Unknown.

**4. REST INSERTION. Proven in bone, never attempted in cartilage.**
Inserting short rests between load cycles substantially enhances the osteogenic response and defeats the
rapid saturation of the cortical response (`PMID 14707150`, `PMID 28076363`). A targeted query for rest
insertion or rest-inserted loading **with a growth-plate or longitudinal-growth endpoint returns nothing in
any species.** Given that the mechanism proposed for lateral joint loading is fluid flow and solute
transport — exactly the mechanism rest insertion is thought to exploit in bone — this is the single
cheapest untried parameter in the domain.

**5. INTERMITTENCY vs MEAN STRESS — a distinction the field keeps conflating.**
`PMID 24902946` shows cyclic loading about an ELEVATED mean (0.2 MPa ± 0.06–0.2 MPa) still reduces growth,
and that raising magnitude and frequency TOGETHER destroys the tissue. `PMID 39090666` shows cyclic loading
that RETURNS TO ZERO increases length. So the governing variable is plausibly **mean stress**, with waveform
setting tissue damage — but the two have never been factorially crossed with a length endpoint.

**6. THE SIGN IS BONE-SPECIFIC AND NOBODY KNOWS WHY.**
`PMID 37314663`: identical 0.4 N at 0.77 Hz for 30 s made fetal rat **metatarsals grow LESS (p<0.05)** and
fetal rat **femurs grow MORE (p<0.001)**. `PMID 28165010` supplies a candidate explanation — movement
regulates chondrocyte proliferation in only SPECIFIC plates, and the selectivity tracks **intrinsic mTOR
activity per plate**. **No study has mapped mechanical sensitivity across plates within one animal**, so
there is no way to predict which of a human's plates would respond, or in which direction.

**7. AGE / MATURITY WINDOW.** Every positive length result is in a weanling-to-young animal (3–8 weeks
mouse, 5 weeks rat, lambs, fetal explants). The heating window has been partly characterised
(`PMID 23956063`), and the human periosteal data give a hard cut-off (`PMID 39502984`, 9.6 years). For the
lateral-loading, swimming, ESWT and rest-insertion arms **there is no age-response data at all**, and no
experiment in a near-mature animal.

**8. COMBINATION.** Heat, exercise and loading act through overlapping transport mechanisms
(`PMID 20930127`, `PMID 19372302`, `PMID 38679285` couples hydrostatic pressure with a thermal stimulus at
the cell level). **No experiment has combined local heating with mechanical loading**, and none has combined
periosteal release with a stimulatory load (the only combination ever tested is periosteal resection plus a
GROWTH-RETARDING construct, `PMID 27159337`, where the two were additive).

**9. LARGER ANIMALS AND HUMANS.** For the lateral-loading axis there is nothing above the mouse. For
vibration there is one abandoned human trial. For heating there is nothing above the mouse. **The entire
positive half of this domain sits on rodent and lamb data from four laboratories.**

**10. WHAT IS NOT A GAP.** Do not re-derive these: low-level laser (tested at 3 doses, null or negative);
whole-body vibration in growing rats (no length effect); spaceflight/hindlimb unloading (longitudinal growth
rate unaffected — unloading does not lengthen); static magnetic fields (no length endpoint anywhere);
therapeutic ultrasound at high dose (frankly damaging to the physis, `PMID 12919875`); inversion and hanging
(no evidence of any quality); PEMF on regenerate bone (human double-blind null).

---

## WHAT I COULD NOT VERIFY

- **`PMID 7421329`** (Elson & Watts, *Med Biol Eng Comput* 1980, "Attempt to stimulate longitudinal growth in
  the dog by mechanical vibration"). **No abstract in PubMed or Europe PMC.** The title implies an attempt;
  the RESULT AND ITS DIRECTION ARE UNVERIFIED. This is potentially the earliest vibration-for-height
  experiment and it should be obtained in full text.
- **The four arteriovenous-fistula-for-leg-length papers** (`PMID 13789389` 1961 Mayo, 10-year observations;
  `PMID 5888999` 1963; `PMID 14119083` 1964; `PMID 4822516` 1974). **None has an abstract.** Direction and
  magnitude UNVERIFIED. Given that femoral fracture overgrowth (row 54) is real and hyperaemia-driven, this
  historical human series is the most interesting unverified item in the enumeration.
- **`PMID 5547971`** (venous ligation and bone growth, *J Anat* 1971) and **`PMID 4116029`** (temperature and
  bone growth in the chick, *J Anat* 1972) — no abstracts; both are PMC-available and were not fetched.
- **`PMID 14083143`** (1963, periosteal stripping in dogs and monkeys) — no abstract; direction inferred from
  the title only.
- **`PMID 14691683`** (treadmill running, young growing rats) — femoral length was measured but the
  direction is not stated in the abstract.
- **The 2026 Europe PMC record on trans-physeal growth-plate bridges** (row 78) has **no PMID** and appears to
  be a preprint; treated as unverified.
- **A 1987 EPMC record on periosteal stripping and the beagle distal ulna** has no PMID and no abstract.
- **`PMC6419405`** (LIPUS enhancing callus consolidation in human tibial lengthening-over-nail) — found via
  WebSearch, **PMID not resolved**; cited as PMC only.
- **Row 26** (low-intensity vibration in Duchenne boys, 0.4 g / 30 Hz / 10 min/day / 14 months) comes from a
  WebSearch snippet of a PMC article; **I did not resolve its PMID** and the numbers are quoted at one remove.
- **`NCT03666975`** has **no posted results** and its status is UNKNOWN; whether it was completed, abandoned
  or published elsewhere could not be determined.
- **Citation counts** used to argue non-replication came from Europe PMC's `citedByCount` field and NCBI
  `elink` (12 citing articles for `PMID 19890688`); these undercount preprints and non-indexed work.
- I did **not** access: the full texts of any paywalled article (all extraction is from abstracts and, where
  stated, the ClinicalTrials.gov API record); the FDA/EMA device literature for vibration platforms or bone
  growth stimulators; any non-English primary source beyond its English abstract (`PMID 1918270` is Japanese).
- **Commercial height-increase devices**: no peer-reviewed evaluation of any specific marketed inversion
  table, hanging bar or "grow taller" device was found. The claim that none exists is an absence-of-evidence
  statement from Europe PMC and general web search, not a verified negative.

**Sources consulted outside Europe PMC / NCBI:**
[ClinicalTrials.gov NCT03666975](https://clinicaltrials.gov/study/NCT03666975) ·
[CenterWatch listing for NCT03666975](https://www.centerwatch.com/clinical-trials/listings/NCT03666975/can-we-promote-bone-lengthening-with-vibration-therapy) ·
[LIPUS and mandibular condylar growth (PMC8433121)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8433121/) ·
[Low-intensity vibration in Duchenne muscular dystrophy (PMC9664527)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9664527/) ·
[LIPUS callus consolidation in tibial lengthening (PMC6419405)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6419405/) ·
[Effects of therapeutic ultrasound on growth plates (PubMed 34958326)](https://pubmed.ncbi.nlm.nih.gov/34958326/) ·
commercial-device claims checked against non-scientific consumer sources
([LiveLifeTaller](https://www.livelifetaller.com/does-hanging-make-you-taller/),
[Supplement Choices](https://supplementchoices.com/do-inversion-tables-make-you-taller/)) — cited only to
establish what is being SOLD, never as evidence.
