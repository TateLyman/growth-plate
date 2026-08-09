# OPEN THREADS — exactly where we are

Last updated: **2026-08-09, after round 171.** Repo: 694 nodes, 364 gaps, 1380 refs, validator errors none.

This file exists so a side pivot does not lose the main line. Anything listed OPEN here is unfinished
work with a defined next step, not a closed question.

---

## THREAD A — the NPR2 compound (MAIN LINE, OPEN, furthest advanced)

**Where we got to.** The arm was reframed at round 155 (CORR-169, SD-008): NPR2 has **three separable
control points**, not one, and the atlas had spent rounds 152–154 optimising the hardest.

- **A — ligand supply.** Vosoritide / navepegritide. In the stack. *See THREAD D for sourcing.*
- **B — receptor phosphorylation state.** Strongest genetic proof on the axis (`wagner2021`, +4.3–8.8%
  femur on a **wild-type FGFR3** background — our subject condition). **Cannot be de-risked**: both the
  kinase and the phosphatase are unidentified, and `egbert2024`/`egbert2025` show the identity has
  *resisted* phosphoproteomics plus combinatorial knock-in mice. **SD-008 forbids planning around the
  enzyme being identified.** Best compound remains a neutral phosphate-masked fostriecin prodrug
  (does not exist; `the_best_phosphatase_compound`).
- **C — phosphorylation-independent allosteric gain.** The live one.

**Current state of C — two allosteric sites on GC-B, opposite faces of the membrane:**

| | MCUF-42 / compound 1 (`ma2024`) | compound 20 (`andresen2023`) |
|---|---|---|
| site | **extracellular**, K_D 710 nM | **intracellular** KHD, GC-A Thr640 / GC-B Ile624 |
| mechanism | raises CNP **affinity** (6.4× potency shift, **no Eₘₐₓ change**) | raises **efficacy** (+30% Eₘₐₓ) |
| phospho-dependence | untested | **independent** (+183% on GC-A 7E) |
| exists at wild-type GC-B? | **yes** | **no** — GC-B data are from the I624T mutant |

**ROUND 161 — compound 1 CONFIRMED best in the screen, and confirmed NOT a therapy.** Re-ranked all 253
selective actives: **208 distinct scaffolds** (singleton-dominated = HTS noise), **40% PAINS/BRENK-flagged**,
and all seven compounds scoring above compound 1 are **scaffold singletons** (one is **diazinon**). Compound
1 is the highest-activity compound with real SAR support (4-member scaffold + 3-member sister). Best
clean-and-supported alternative: 65.1%. **But compound 1 is itself BRENK-flagged for the thioamide — and
`ma2024` shows the thioamide is REQUIRED (amide -> complete loss). The alert IS the pharmacophore.** Plus
`robinson2011`: Go6976 is a catalytic-site *inhibitor*, so there is **no chemical starting point for an
intracellular GC-B activator**.

**VERDICT — add to the therapeutic stack: NOTHING. Add as research probes: `CID 647514` + `CID 3588620`.**

**The named compound (round 157).** `CID 647514` = **compound 1**, CAS **332862-27-8** — MCUF-42 with a
piperazine for its piperidine. EC₅₀ 0.74 µM, **Eₘₐₓ 112%** (vs MCUF-42's 0.80 µM / 86%), no GC-A activity
to 67 µM, HTS 96.67% @10 µM. **14 vendors.** MCUF-42 itself has **zero** vendors.
Charge probe: `CID 3588620`, the N-methylpiperazine analogue, 50.37% @10 µM, 7 vendors.

**OPEN — next steps, in order:**
1. **One potentiometric titration** of CID 647514 and CID 3588620 (`g_l12_pka_and_cartilage_uptake_of_the_gcb_pam_series`).
   Decides whether the cationic/Donnan argument applies to this series at all. Cheapest
   decision-relevant experiment on the whole axis. *CORR-173: compound 1 is probably NOT cationic —
   cyanoethyl + thioamide suppress the amine.*
2. Cartilage explant uptake, neutral vs cationic member — ratio of tissue to bath.
3. Spatial distribution (concentrated-throughout vs bound-at-surface — the `hakim2025` failure mode for
   lipophilic cations; this chemotype is XLogP ≈ 3.8).
4. ~~Counter-screen the `andresen2023` series at wild-type GC-B~~ — **DONE, ALREADY, AND NEGATIVE
   (CORR-174).** andresen2023 reported it: *"Neither of the compounds modulated the potency of CNP or
   increased the maximum level of CNP-mediated cGMP production."* All ~100 analogues were made and
   screened **against GC-A**. Every GC-B number for this chemotype comes from the **I624T point mutant**.
   The site transfers; **no molecule does.** Remaining open: whether new chemistry can be built against
   Ile624 — a synthesis programme, not a screen.

**Unresolved objection, not waved away:** the plate is a CNP **consumer**, not producer, so a systemic
potentiator raises vascular signalling at least as much as plate signalling. The cationic route is the
only proposed escape and it is unmeasured.

**Round 159 — A vs B settled: they MULTIPLY, and B gates A.** Three kinetic handles, three arms, no
overlap: ligand moves **Vmax** (>10×, `robinson2012`), KHD phosphorylation **gates** whether Vmax can move
(`yoder2012`; 6E only ~20% of WT), KHD allostery moves **Km** and is **phosphorylation-independent**
(`edmund2019`). MCUF-42 is a pure **potency**-shifter with no Eₘₐₓ change, and `robinson2017` says
dephosphorylation is **not surmountable by ligand** — so a potency-shifter **cannot rescue a
dephosphorylated receptor**. Synergy, not additivity. Corollary: the PAM is worth **more** in a
normal-FGFR3 subject than in achondroplasia — opposite to how every trial is powered.

**New interaction found: `prickett2021` — exogenous CNP agonism SUPPRESSES endogenous CNP production**
in humans (−4.2 to −5.0 pmol/L NTproCNP at 4 h from day 183, p=0.003–0.015; replicated in
hypochondroplasia by `kanakatti2026`). A PAM has **no intrinsic activity** — it multiplies endogenous
ligand, which this loop shrinks. **So the PAM needs a feedback-immune exogenous analogue underneath it.**
Inverts the round-156 framing: the peptide isn't displaced by the small molecule, it's what makes it work.

**`g_l12_does_the_gcb_pam_potentiate_vosoritide` — DOWNGRADED to confirmatory (round 160). Probably YES,
on two independent grounds without an experiment.** *Structural:* vosoritide is Pro-Gly + the 37 C-terminal
residues of CNP-53 and **retains the intact CNP-22 binding ring** — it differs from native CNP only by an
N-terminal protease-resistance extension, and the ring is what engages the ECD where MCUF-42 acts.
*Cross-ligand:* PAMs here are not ligand-specific — MCUF-651 potentiates **ANP, BNP and endogenous human
plasma pools** at GC-A. Residual risk: the N-terminal extension could obstruct a cleft-adjacent modulator.

**Rivals checked, none displaces either arm:** BMN 333 = better control point A, not a third arm;
KK8398 = infigratinib under a Kyowa Kirin code, already in the stack; activating antibodies (`liu2026`,
XX16 works in vivo) are **dead on delivery at ~150 kDa** against a farnum2006 curve that is undetectable
by 40 kDa.

---

## THREAD B — the phosphatase arm (**CLOSED** 2026-08-09, five independent lines; mechanism retained)

Fostriecin has the right enzyme selectivity (PP2A 1.4 nM vs **PP5 60 µM measured**, `swingle2009`) and the
wrong charge (dianion, partition 0.21). Candidate is a neutral phosphate-masked prodrug (~4.3× gain,
CORR-167). **Does not exist**; no fostriecin prodrug has ever been made. Not cheap to make — the
`jiang2025` nine-step route needs an **engineered enzyme** for its key C–H oxidation.

**Round 159 verdict: KEEP the control point, but "keep" here means the mechanism, NOT a drug.** It is not
redundant with Thread A — different kinetic handle — but it has no compound, no identified enzyme, and
SD-008 bars planning on identification. Its incremental value in a stack that already contains an FGFR
inhibitor is bounded by the **1.42× tonic, FGF-independent** component.

**OPEN:** `g_l12_fostriecin_pp4_versus_pp2a_attribution` — re-run the `swingle2009` ten-analogue panel
**with a PP4 column**. `theobald2013` shows PP4C knockdown alone reproduces fostriecin's cellular phenotype
while PP2AC knockdown does not, so the dose ceiling and the intended effect may sit on different enzymes.

**ROUND 164 — the arm stays closed, but it now has a named bench probe.**
`the_best_purchasable_phosphatase_probe_and_its_delivery`. **Cantharidin, 100 µM, intact tibia** — the
compound and concentration the effect was measured with (`shuhaibar2017`: FGF inhibition 51% → a
non-significant 14%; tonic effect **1.42×, p=0.0018**). **10 µM fails** (`robinson2017`, monolayer).
CID 5944, MW 196, **91 vendors**.

**Delivery finding:** cantharidin and norcantharidin are **neutral anhydrides that hydrolyse to dianions** —
they are *self-masking prodrugs*. Computed partition: anhydride **1.00**, hydrolysed diacid **0.22**. The
charge-masking strategy designed for fostriecin across rounds 153–157 is already built into the cheapest
probe on the list. Caveat: depends on hydrolysis half-life vs penetration time, neither of which we have.

**Three probes, three questions, none interchangeable:** cantharidin (validated readout, no selectivity) ·
LB-100 (human phase 1, 45 vendors, partition 1.00, no selectivity) · fostriecin (only PP5-sparing agent,
43,000×, but partition 0.21 and unstable).

**No human dose is specified and the reason is pharmacological:** cantharidin is a vesicant with a
documented lethal dose in the low milligrams, accepted only topically; okadaic acid is the diarrhetic
shellfish poison; calyculin A is acutely toxic. Systemic therapeutic index ≈ zero.

**ROUND 163 — EXHAUSTIVELY CHECKED AND CLOSED. Five independent lines, all empty.**
1. **ChEMBL** — 39 phosphatase targets, 1,801 molecules: 16 at PP2A catalytic, **1** at PP4, **0 both**.
2. **PubChem BioAssay** (independently curated) — PPP4C: 18 assays, **one compound ever tested**;
   PPP2CA: 32 assays, 70 compounds; **intersection zero**.
3. **Literature 2023–2026** — no PP2A inhibitor with PP4 selectivity data, no new selective chemotype.
4. **The fostriecin series itself** — no PP4 number for any analogue, anywhere.
5. **The B56 route, and this is the one that shuts it.** PP2A substrate selectivity is set by the B
   subunit, so a B56-groove-directed agent was the only selective route that *doesn't* require knowing
   the catalytic enzyme. Scanning NPR2 with the authoritative **ELM DOC_PP2A_B56_1** regex: 4 matches vs
   ~1.5 expected by chance, **all in ordered regions** (pLDDT 74.6–93.3), **none within 40 residues** of a
   phosphosite (nearest 75) — while the phosphosite cluster **S513–T529 is disordered at pLDDT 36**. SLiMs
   work in disordered segments; a match buried at pLDDT 90 is not a docking site.

*Bonus:* UniProt annotates exactly the seven sites S513/T516/S518/S522/S523/S526/T529 — **Ser-489 is not
among them**, independently corroborating `otto2022` and CORR-170.

**ROUND 161 — REMOVED AS A COMPOUND ARM. Four independent blockers.** (1) enzyme unidentified and has
resisted direct attack (SD-008); (2) no compound exists and none is cheaply makeable; (3) **PP2A-versus-PP4
selectivity has never been measured for any compound** — across all 39 human Ser/Thr phosphatase targets in
ChEMBL, 1,801 molecules carry a value, **16** have a PP2A catalytic number, **1** has a PP4 number
(fostriecin), and **0 have both**; (4) prize bounded at **1.42×** tonic where an FGFR inhibitor is already
present, against systemic pan-PPP liability with hepatic DLT. **Nothing to add. Mechanism retained**
(`wagner2021`, +4.3–8.8% femur on wild-type FGFR3).

**CORR-175 corrects the cost claim — it is NOT one plate.** ChEMBL target `CHEMBL5465552` (PP4 catalytic
subunit) holds **exactly one activity record in the entire database**: fostriecin, 3.0 nM. Not one
analogue, not one other chemotype. **PP4 has no chemical probe and no counter-screen series in public
medicinal chemistry** — the assay has to be built before the panel can be run. The compounds exist; the
assay does not.

---

## THREAD E — THE NEXT AXIS (**OPEN, new 2026-08-09**) — non-endochondral, and a re-check on closure timing

`the_next_axis_after_the_cnp_axis_died`. **h_term is no longer "closest to solved"** — after rounds
152–164 it is the most thoroughly explored and the emptiest arm in the atlas. That entry in
`the_arms_reordered_for_late_bone_age` is corrected; the rest of that ranking stands.

**The structural argument that picks the next axis.** Pool, amplification and h_term are **rate terms and
all require an open plate** — which is exactly what bone age 16+ is taking away, and exactly what every
CNP access route gates on. **Non-endochondral height uses no growth plate**, so bone age does not reduce
its availability. It is the only term with that property.

**And nobody here has ever looked for a compound on it.** The term appears in exactly **four nodes, all
indexes**; the biology has real L6 coverage (`diurnal_stature_variation`, `bed_rest_growth_human`,
`gravity_posture_spinal_loading`) and **zero L12 pharmacology nodes**. The intervertebral-disc
regenerative literature — aggrecan/proteoglycan synthesis, GDF5 and BMP agents — has never been read here.
`acan_gene` already sits on both sides of the divide.

**FIRST MOVE, and it costs no experiment** (`g_l12_what_fraction_of_non_endochondral_height_is_durable`):
read the diurnal/bed-rest/microgravity literature for the **recovery curve, not the peak**. If it's all
reversible, the term scores zero durable centimetres and we go to site instead. If a durable fraction
exists, size it, then read the disc literature for compounds.

**ROUND 166 — FOUND ONE. `resveratrol_delays_fusion_the_untouched_compound`.** Resveratrol appeared in
**zero nodes and zero references** across 690 nodes. `karimian2013` — oral 200 mg/kg/day in rabbit —
**delayed fusion at three physes** (distal tibia, distal femur, proximal tibia) and **improved final
length**, with **VEGF and laminin suppression** proposed as the mechanism. Endpoints almost nothing else
in this atlas has, and from **the same laboratory whose `chagin2007`/`karimian2008` killed tamoxifen**.
Mechanistically it is a *different control point* from aromatase inhibition — blocking the vascular
invasion fusion requires, not the hormonal clock — so stackable in principle.

**ROUND 167 — FULL TEXT READ. The dose objection is WITHDRAWN (CORR-177) and the stack analysis is done.**

*Dose resolves favourably.* Human Cmax across 0.3 mg–5 g = **0.3–2.4 µM**; ex vivo **active 0.3 µM**;
**inhibitory 10 and 50 µM — 4–20× above the top of the human range.** The achievable window sits in the
stimulatory band and *cannot reach* the inhibitory band. My BSA scaling to "4.5 g/day" compared the wrong
quantity. Real caveat: conjugates exceed parent by up to **20.3× AUC**, so free drug at a chondrocyte is
unknown.

*It does NOT do what killed tamoxifen.* Apoptosis 0.2% on RES = 0.2% control (E2 1.1%). Resting zone
**more than doubled** (0.26 vs 0.11 mm²). Opposite sign from tamoxifen on the exact liability.

*Fusion data is the strongest part.* Distal tibia at 4 wk: **57% unfused on RES (8/14) vs 6% control
(1/17)**, 0% on E2, p<0.05. Proximal tibia at 10 wk — **the last plate to fuse and the one that sets final
length** — **0% fused on RES vs 50% fused control**, p<0.05.

*Magnitudes are small and inconsistent:* ovary-intact tibia **+1.9%** (p<0.05) but femur p=0.1 ns; OVX
femur **+1.5%** (p<0.05) but tibia no difference. The significant bone **swaps between arms**.

**STACK VERDICT — collides with two of four arms:**
- **GH — ANTAGONISED, in humans.** `brown2010`: 40 volunteers, 0.5–5 g × 29 d, **IGF-I and IGFBP-3 fell in
  ALL volunteers, p<0.04**, most marked at 2.5 g. Rabbit showed no change; **human data govern.** Magnitude
  not in the abstract — that decides nuisance vs disqualifying.
- **ERDAFITINIB — PK risk, serious.** Erdafitinib is cleared **39% CYP2C9 + 20% CYP3A4 = 59%** through
  enzymes resveratrol inhibits, against a paediatric record of 5/5 permanent discontinuation, 3 surgeries.
  Plus a smaller PD conflict: RES **cuts BrdU incorporation** while erdafitinib works by relieving FGFR3's
  brake *on proliferation*.
- **ANASTROZOLE — probably clean, weaker test than it looks (CORR-179).** Uterus weight unaffected — but
  `nilsson2003_raloxifene` shows raloxifene **passes that same test while being a full plate agonist.**
  What saves it is the fusion direction itself. Residual risk is **redundancy** if the mechanism is ERα
  antagonism.
- **VOSORITIDE — CNP direction still unresolved**, plus a new overlap question: RES raises hypertrophic
  cell number and terminal size, which is the term CNP serves.

**And every animal is FEMALE** — the same lab ran its tamoxifen work in male rats, so this was a choice.
No male resveratrol growth-plate data exists anywhere.

**RALOXIFENE CLOSED** (`nilsson2003_raloxifene`): an oestrogen **agonist** at the rabbit plate — hastens
fusion. Wrong direction.

**Five reasons to doubt it, all recorded:** SD-006 applies to half the histology (zone thickness ≠ growth;
final length and fusion timing are what carry it) · **the dose scales to ~4.5 g/day in a human**, above
supplement range and into GI toxicity · **biphasic in vitro** — stimulates at 0.3 µM, *inhibits* at 10–50 µM
· resveratrol is a canonical frequent-hitter chemotype · the fusion-delay arm is ovariectomised.

**And an unresolved CNP interaction that must be settled before combining anything:** `prickett2023`
(125-subject RCT) shows plasma NTproCNP **falls** after resveratrol. The obvious reading — that it
antagonises the CNP arm — is **unsafe**, because `prickett2021` established NTproCNP falls when pathway
output *rises*. Direction unassigned. → `g_l12_resveratrol_human_dose_and_cnp_direction`.

**GPER1 checked and CLOSED.** `kang2020` eliminated ERα vs ERβ but never covered GPER1, a third membrane
receptor. `iravani2019` tested the selective agonist G1 on the endpoint that matters: **no effect on mouse
metatarsal growth at any concentration ex vivo, none on tibia/femur in vivo** — while oestradiol behaved
as expected. `chou2021`/`chou2025` report the *opposite* knockout direction, but measure zone thicknesses
rather than length, and their profile is a **trade** (proliferation up, hypertrophy down). Length was
measured once and did not move.

**SECOND, on the highest-ranked arm.** Closure timing is #1 and only *partially* exploited. Anastrozole
removes **ligand**; `smith1994`'s 204 cm is **receptor** disruption — a different control point.
`tamoxifen_at_the_growth_plate` killed the obvious compound (resting-zone apoptosis, no catch-up, at
paediatric exposures) — **but that same node records the effect is NOT simple ER antagonism** (neither
oestradiol nor IGF-I rescued it). If the killing is a tamoxifen off-target rather than a class effect,
**pure antagonists and SERDs were never tested.** Checkable, and it sits on the largest arm.

---

## THREAD F — the duration arm (**AT ITS CEILING** 2026-08-09) — every alternative route closed

`the_vegf_control_point_is_the_wrong_lever`. The task was to replace resveratrol with a cleaner molecule at
the same control point. **I tested the control point first and it does not survive — so there is no cleaner
molecule to find.**

**`gerber1999` is decisive, and `karimian2013` cites it in support of its own mechanism.** Systemic VEGF
blockade (Flt-(1-3)-IgG) in 24-day-old mice: vessel invasion almost completely suppressed → **impaired
trabecular bone formation**, expanded hypertrophic zone, decreased chondroclast recruitment and terminal
chondrocyte resorption. Proliferation and maturation normal — **only resorption inhibited.** And the
sentence that settles it: **"Cessation of the anti-VEGF treatment was followed by capillary invasion,
restoration of bone growth."** Growth was restored *on stopping* — so it was impaired *during*. **Blocking
VEGF converts growth into cartilage accumulation.** It is a resorption brake, not a growth lever.

**This re-reads `karimian2013` against itself.** Every histological feature that paper offers as evidence
of benefit — wider plate, taller hypertrophic zone, more hypertrophic chondrocytes, suppressed VEGF — is
what `gerber1999` produces *while impairing bone formation*. SD-006 already forbade reading zone thickness
as growth; Gerber supplies the specific reason. The caliper length gain is still real; the mechanism
offered for it is the failure signature.

**And the logic inverts:** if resveratrol works by *partial* VEGF suppression, the window is bounded
**above** by the Gerber phenotype — so a **more potent, cleaner VEGF inhibitor would be worse, not better.**

**Senolytics closed in the same breath, before costing anything.** `growth_plate_senescence` states plate
senescence is **not** cellular senescence in the p16/SASP sense — it's a division-dependent decline. There
is no p16-high SASP population to clear. Dasatinib+quercetin, navitoclax, fisetin: inapplicable by target
definition.

**THE DURATION ARM IS AT ITS CEILING WITH ANASTROZOLE.** Oestrogen removal is the only validated lever.
Receptor route dead twice (`chagin2007` tamoxifen kills the resting zone; `nilsson2003_raloxifene` is a
plate *agonist* that hastens fusion). Vascular route closed by `gerber1999`. Senescence route closed by
definition.

### ROUND 169 — the receptor route re-checked exhaustively at the user's direction. SAME VERDICT, MUCH STRONGER BASIS.

`the_receptor_level_oestrogen_sweep`. Round 168 closed the receptor route on **two compound-specific
failures**, which left every untested compound as a live possibility. It is now closed on a **class
mechanism plus a human trial**, and the mechanism predicts the failure of compounds nobody has tested.

**CORR-181 first — my working claim was wrong.** "No pure antagonist or SERD has ever been tested at a
growth plate" is **false**. Fulvestrant, under its research code **ICI 182,780**, has been at a growth
plate at least four times since 1998. I searched marketed names in titles; this literature uses the
compound code in abstracts. Second instance of the CORR-171 failure mode — depth on one paper mistaken
for coverage of a field. Countermeasure: **search the research code as well as the marketed name.**

**In wild-type animals a pure antagonist does nothing to longitudinal growth — three times, two species,
both sexes.** `sibonga1998` (rat, female, growing; **complete uterine antagonism in the same animals**
proves engagement; no effect on tibial growth rate) · `turner2000` (rat, **male**; no effect, while
**orchiectomy in the same experiment did** reduce growth) · `movrareskrtic2014` (mouse, OVX; **no effect
in wild-type** on plate height). The only positive, `gunther1999`, is a **rescue** of exogenous-E2-
accelerated maturation back to control — not a gain below it.

**THE MECHANISM, AND IT GENERALISES TO THE WHOLE CLASS.** `movrareskrtic2014`: ICI acts at the plate
**only once AF-2 is disabled**, and then as an *inverse agonist* — the authors infer plate ERα is
**constitutively active without ligand**. `brjesson2012`: closure runs on ERα functions that **do not
require AF-1**, and **AF-1 opposes closure** (AF-1 deletion → hyperactive receptor → plates CLOSED).
**Every drug in this class is an AF-2 agent, aimed at a function that does not need AF-2.**

**THE HUMAN TRIAL EXISTS AND ITS HEIGHT ENDPOINT IS NULL.** `sims2012` / NCT00278915, on the **FDA label**
— 30 girls, mean age 5.9 y, McCune-Albright, **fulvestrant 4 mg/kg IM monthly × 12 months**, prospective
multicentre. Bone age advancement **1.99 → 1.06** (mean change −0.93, 95% CI −1.43 to −0.43, **p=0.0007**),
progressive. No serious treatment-related AEs. Uterine/ovarian volumes unchanged = **no partial agonism**,
the thing tamoxifen and raloxifene both failed. **BUT: predicted adult height 163.0 → 163.5 cm** (FDA: *no
clinically meaningful change*) because **growth velocity Z fell alongside** (−1.14, 95% CI −2.67 to 0.38,
p=0.135, point estimate negative). **The clock slowed and the growth slowed with it.**

**AND THE COMPARTMENT WAS WRONG.** `brjesson2010` — cartilage-specific ERα-null mice grew **normally**
through sexual maturation; the tall phenotype of *total* ERα loss ran through the **GH/IGF-1 axis**. A
plate-directed antioestrogen aims at a compartment that is not carrying the pubertal effect; systemic
ligand removal (anastrozole) acts on the one that is.

**Fulvestrant is the one compound that stacks cleanly, and it does not matter.** FDA label: **no known
drug-drug interactions**, no CYP1A2/2C9/2C19/2D6/3A4 inhibition, PK unchanged by rifampin/ketoconazole —
it clears the *exact* CYP2C9/3A4 objection that disqualified resveratrol. GH arm direction is favourable
(oestrogen *suppresses* hepatic IGF-I: `gibney2005`, `wolthers2001`), though IGF-I has never been measured
under fulvestrant (graded **E**). `mehta2012`/`mehta2019` show anastrozole+fulvestrant is **non-redundant
in humans** — but in breast cancer, and **non-redundant plus zero is still zero**.

**Rest of the class: zero plate studies for six oral SERDs, the ERα PROTAC vepdegestrant, the covalent
SERCA class, and six further SERMs** — and all are AF-2 agents, so the mechanism predicts the same null.
`basu2026`: giredestrant and camizestrant cause **on-target ERα-mediated bradycardia**; fulvestrant does
not. Potency is not buying safety either.

**Cost of the genetic version, recorded:** `smith2008` spine aBMD Z **−3.85** and falling, **while bone age
still advanced** 15→17.5 y; `feigerlova2025` lumbar Z **−3.9 → −5.6**, unresponsive to oestrogen *and*
tamoxifen. FDA label: paediatric BMD under fulvestrant **unstudied**.

**TWO GAPS OPENED, NEITHER A LEVER:**
1. `g_l12_does_fulvestrant_degrade_eralpha_in_growth_plate_chondrocytes` — **nobody has ever measured ERα
   protein in plate cartilage under a degrader.** Uterus degraded + plate intact ⇒ the class failed on
   *delivery* and the arm reopens as a formulation problem. Both degraded + no growth change ⇒ permanent.
2. `g_l12_final_height_of_the_sims2012_extension_cohort` — **24 of 29 girls entered an extension with
   yearly data collection in 2012; nothing was ever published.** They have now reached adult height. Only
   existing route to a final-height endpoint for a pure ER antagonist in humans. A retrieval, not an
   experiment.

**CORR-180 also raised:** `brjesson2012`'s bibliography one-line finding stated the **opposite** of the
paper's conclusion. Confined to the index string — the node `estrogen_receptor_alpha` had it right and
graded it D. Corrected in place, prior string preserved under `finding_corrected_from`.

### ROUND 171 — CORR-182. THE ROUND-170 HEADLINE WAS WRONG. The user caught it, and the atlas already held the answer.

**My claim:** *"slowing the bone-age clock through the oestrogen axis does not convert into adult height."*
**The objection:** height = velocity × duration; all three of my sources tested an oestrogen agent
**alone**, where velocity falls as the clock slows. A stack with independent accelerators does not.
**Correct — and `duration_velocity_combination` said so at grade B on 2026-08-06, three days before I
contradicted it.**

- `mauras2008` — **placebo-controlled**, anastrozole added to GH: **linear growth COMPARABLE** between
  arms while bone age advanced +2.5 vs +4.1 y at 3 y (p<0.0001) → **PAH +6.7 vs +1.0 cm**. The mechanism
  as an experiment: hold velocity, slow the clock, height appears.
- `mauras2016` — randomised three-arm, near-final height, n=71 at BA 15.3: **AI +18.2, GH +20.6, AI/GH
  +22.5 cm** (p=0.01) vs +13.0 expected. SDS −1.4 / −1.4 / **−1.0** (p=0.06, borderline).
- `nct01248416` — PAH change: AI +0.5, GH +4.9, **combination +7.4 cm**.
- `tanriverdi2023` — **true adult height +3.3 cm** (173.1 vs 169.8, p=0.044), but only at ≥2 y exposure.

**TWO reasons my claim was unsound, not one.** (1) **Monotherapy** — `geffner2024` even says AIs "appear
to have an additive effect" added to GH, a sentence I quoted in round 170 and didn't follow. (2) **The
endpoint** — two of my three were **predicted**-height nulls, and `nearfinal2026` shows PAH **ranked two
drugs backwards**: at 1 y anastrozole +4.2 > letrozole +1.4 (p=0.03); at near-final height **letrozole
+4.2 > anastrozole +0.8 (p=0.013)**. A PAH null is weak evidence about attained height.

**Procedural countermeasure (this is the real lesson):** rounds 169–170 searched the literature hard and
never grepped the atlas's own nodes for the claim being graded. **Before grading claim X, grep nodes for
X — not just refs for evidence.**

**WHAT SURVIVES, AND IT IS THE PART THAT MATTERS FOR THIS CASE.**
- **Duration agents are NOT one class.** `nct00355030` — GnRHa + GH **fails** on true adult height (−1.8
  vs −1.9 SDS, n=91) because the analogue removes the **pubertal spurt** along with the fusion signal.
  Anastrozole is the right duration agent *precisely because it preserves the spurt.* Do not substitute.
- **The prize is bounded and measured.** `nearfinal2026`, 72 males with **advanced bone age** to near-final
  height: **overall median gain +1.2 cm** (IQR −1.9 to +4.2). Best subgroup (letrozole) +4.2 cm.
  Independently predicting more gain: **earlier pubertal stage (p=0.012)**, longer treatment (p=0.005),
  **concurrent GH (p=0.022)**. Optimising everything identified reaches single digits, against ~25 cm for
  the genetic nulls.
- **Starting late is a measured penalty, not a hypothesised one** — and it is the one gradient that speaks
  directly to bone age 16.

**RECEPTOR ARM DOES NOT REOPEN.** Tested explicitly. An AI has a real duration effect that monotherapy
trials hid behind a falling velocity term. A pure antagonist has **no measured longitudinal-growth effect
in any wild-type animal** — there is no duration term for GH to multiply, and the `sims2012` bone-age
effect is cancellation of a *pathological* excess specific to MAS, which anastrozole already covers.

**NEW GAP — the operative unknown for this case:**
`g_l12_does_the_ai_gh_combination_still_work_above_bone_age_15`. **Every dataset stops just below the
band.** `mauras2016` *ended* at BA 15.3; `cui2025` uses BA ≥13 as a floor with **no upper stratum**;
nobody reports **starting** above 15. Answerable by **re-stratifying data that already exists** by bone
age at start rather than pubertal stage — the radiographs and heights are in all three cohorts.

**Also fixed:** `duration_velocity_combination` was a grade-B node with **no claim_grades** — six added,
including the two X-grades above (PAH unreliable; duration agents not interchangeable). Round-169 and
round-170 nodes amended so neither carries the withdrawn claim.

---

### ROUND 170 — both round-169 gaps checked, one new control point found and closed, and the answer to the whole oestrogen/closure area

`the_intracrine_oestrogen_control_point`.

**GAP 1 — ERα protein under a degrader: CONFIRMED EMPTY, stays open.** Abstract-level search for a
degradation/receptor-protein measurement in cartilage or chondrocytes returns **four papers, none
relevant**. Nobody has measured ERα protein in growth-plate cartilage under fulvestrant in any species.
The round-169 closure rests on an inference that has never been checked.

**GAP 2 — the `sims2012` extension: PARTIALLY CLOSED, and it sharpened the null.** Registry
(`nct00278915_results_2024`, retrieved 2026-08-09): status **COMPLETED**, primary completion 2009-12-08,
**overall study completion 2023-07-20** — the extension ran a further **fourteen years** — and the posted
results carry **one period only** (30 started, 29 completed) with **no extension outcome**. Record last
updated 2024-03-05; only derived reference is sims2012. Contact route exists (AstraZeneca CSIC).
**And the 12-month PAH null is now precise: +0.5 cm, SD 4.10, n = 17 → 95% CI ≈ −1.6 to +2.6 cm.** It
excluded gains **above ~2.6 cm** and nothing smaller. Not evidence of zero; evidence of not-large.
Tractability raised to 4.

**NEW CONTROL POINT, GENUINELY UNTOUCHED.** Anastrozole blocks **aromatase**. It does not block the
**sulfatase** route: STS liberates oestrone from **oestrone sulfate** — the largest, longest-lived
circulating oestrogen pool — and 17β-HSD I makes oestradiol, **bypassing aromatase entirely**. This is the
canonical AI-resistance mechanism in breast cancer. **And the plate runs the whole pathway**:
`vandereerden2002` found aromatase, 17β-HSD I and II, **steroid sulfatase** and 5α-reductase mRNA in rat
physeal chondrocytes, **three confirmed by direct enzyme activity**, and aromatase/17β-HSD/**STS strongly
up-regulated at sexual maturation**. `sylvia2002`: chondrocytes **release** oestradiol, most in the
**resting zone**. `oz2001`: aromatase protein in the **human** plate. Before this round, *steroid
sulfatase*, *oestrone sulfate* and *intracrine* appeared in **zero** growth-plate nodes.
**A human drug exists** — irosustat (STX64), 40 mg/day oral, and `palmieri2017` (IRIS) is literally the
add-it-on-top-of-an-AI trial, which met its endpoint.

**IT CLOSES ANYWAY, THREE LINES.** (1) The human knockout — **X-linked ichthyosis** — is reviewed across
1960–2025 with endocrine and cardiac involvement catalogued and **no stature, bone-age or epiphyseal
finding** (`fryze2026`). (2) Irosustat's dose-limiting grade 3/4 toxicity is **dry skin, 28%** — it
reproduces the ichthyosis. (3) **The atlas already held the decisive line**: `zegarra2024`, letrozole vs
anastrozole, 79 boys, 3 years — **threefold deeper suppression, slower bone age, NO difference in
predicted adult height**, +1.3 cm combined, **year-1 gain gone by year 3**. A second parallel blockade has
no headroom.

**THE ANSWER TO THE WHOLE AREA — three human tests, three control points, one result.**
- **ligand synthesis** → `varimo2019`, **the only randomised double-blind PLACEBO-CONTROLLED AI trial
  followed to ADULT height**: letrozole **164.8 ± 4.0** vs placebo **163.7 ± 3.7 cm, p = 0.49**, and
  **neither arm beat its own baseline prediction**. *The atlas did not hold this paper.*
- **suppression depth** → `zegarra2024`, above.
- **receptor** → `sims2012`, bone age **halved**, predicted height **unchanged**.

**SLOWING THE BONE-AGE CLOCK THROUGH THE OESTROGEN AXIS DOES NOT CONVERT INTO ADULT HEIGHT.** The axis is
at its ceiling because **blockade depth is not the rate-limiting variable** — not because a better blocker
is missing. That is why round 169 found nothing, and why the sulfatase route would have found nothing.

**THE BOUNDARY, AND IT DESCRIBES THIS CASE.** Every null is **early puberty** — `varimo2019` stopped at
bone age 10.2–10.8, `zegarra2024` required bone age <14, `sims2012` mean age 5.9. **None tests bone age
16.** The one attained-height dataset in the late band points the other way: **`cui2025`, anastrozole +
rhGH, highest target-height-adjusted adult height SDS (0.81) of three matched regimens at bone age ≥13** —
which is the regimen already running. So the ceiling claim is an extrapolation into an untested band, and
it **endorses the current stack rather than changing it**. Graded **E** in the node, deliberately.

**Also recorded from `geffner2024` (index only):** `zegarra2024` carried **significant decreases in
whole-body and lumbar bone density** from baseline to 2 years in **both** arms, plus biconcave vertebrae,
spondylolysis, irregular endplates, 3 scoliosis, 6 fractures. Counterweight: `varimo2019` found vertebral
deformity **no more frequent on drug** (29% vs 22%, p=0.20) and the deformities **resolved** on follow-up.
Relevant to spine reserve.

**NEW GAP:** `g_l12_does_the_human_growth_plate_express_steroid_sulfatase` — no human physeal STS
measurement exists, and **every trial on this axis measured plasma oestradiol, never cartilage**. Two
cheap reads: IHC/RNA-seq on archival epiphysiodesis tissue; oestrone sulfate on stored samples from
children already on an AI. A methodological finding if positive, not a new lever.

---

## THREAD C — NPR3 / clearance arm (CLOSED, do not reopen without new evidence)

Not added to the stack. NPR-C is bifunctional with opposite signs (SD-007); M372049 has the wrong sign at
the receptor; no pharmacological NPR3 ligand has a bone endpoint in any species; NPR-B counter-screen
exists nowhere.

---

## THREAD D — sourcing vosoritide / navepegritide (**CLOSED** 2026-08-09)

See `atlas/data/round158_cnp_analogue_sourcing/README.md`. Summary of state:

- **Voxzogo (vosoritide, BioMarin)** — US list ~**$320k/yr**, net ~$240k after rebates; ~$1,139/vial US;
  CA$950/vial submitted (CA$346,988/yr). No generic or biosimilar before **~2030–2031** (8 patents,
  orphan exclusivity; one Paragraph IV challenge, eligible since 19 Nov 2025).
- **Yuviwel (navepegritide, Ascendis)** — FDA approved **27 Feb 2026** (accelerated), US launch Q2 2026,
  **orphan drug exclusivity granted April 2026** (→ ~2033). WAC **$38,325 per 4 injections** ≈
  **$498k/yr** — *more expensive than vosoritide*. EU decision expected Q4 2026.
- **Both labels require achondroplasia AND open epiphyses.** Our case is bone age 16+ and non-achondroplasia
  → off-label on two axes. Every legitimate route runs through a prescriber.
- **Cheapest legitimate route identified: clinical trial.** `NCT06382155` — BioMarin Phase 2 vosoritide in
  **idiopathic short stature**, **RECRUITING** as of May 2026, with open-label extension "until near-final
  adult height." Free drug plus monitoring. Eligibility (age, open plates, treatment-naïve) not yet
  checked against this case — **OPEN**.

**CLOSED — and price was never the binding constraint.** Full 31-trial landscape scanned.
`NCT06382155` (vosoritide in idiopathic short stature) is **age 3–11, Tanner Stage I, treatment-naïve** —
ineligible three ways over. The only two recruiting studies in the adolescent band both gate on
**genetically confirmed achondroplasia plus an open, actively growing plate**: `NCT06732895` (Ascendis,
navepegritide 12–17; excludes AGV < 1.5 cm/yr or radiological growth-plate closure) and `NCT07441876`
(BioMarin, BMN 333 vs vosoritide, 2–17; requires ACH and open epiphyses).

**Every route — label, trial, assistance programme — gates on diagnosis and growth-plate status, none on
money.** For a non-achondroplastic subject at bone age 16+ there is no legitimate access route at any
price. Do not reopen this as a pricing exercise.

**Two carried consequences:** (1) two sponsors with the deepest CNP datasets in existence both decline to
enrol a closing plate — convergent with `hakata2024` and `serrat2013`, and evidence about whether this
axis is worth pursuing in this case at all, not just about supply; (2) this raises the relative value of
THREAD A, the one route not gated by another organisation's inclusion criteria.

Unlicensed / RUO peptide sourcing was deliberately not investigated; reason recorded in the round-158
README so the omission is not mistaken for an oversight.

---

## STANDING CONSTRAINTS (carried, not re-litigated)

Never invent a citation, author, year or number. Species on every claim. Reviews are an index, not a
source. Identifiers looked up, never recalled. No manufacturing edges to hit a density target. Re-analysis
results graded as strictly as anyone else's. See `atlas/audit/standing_decisions.yaml` SD-001…SD-008.
