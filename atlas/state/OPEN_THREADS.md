# OPEN THREADS — exactly where we are

Last updated: **2026-08-09, after round 180.** Repo: 704 nodes, 368 gaps, 1382 refs, validator errors none.

> **PRIMARY OBJECTIVE, set by the user 2026-08-09: YIELD.** See THREAD G. Everything else is
> subordinate until the amplification assay exists.

> **READ THIS BEFORE GRADING OR CLOSING ANY ARM (CORR-183).** Open
> `ledger_what_is_dead_what_is_settled_what_is_live` **first**; grep the *nodes* for the claim, not only
> the refs for the evidence; and state which **sub-lever** of the eight-term decomposition you are
> auditing. FIVE consecutive corrections (CORR-171, -181, -182, -183, -184) are the same failure: searching
> outward for evidence before reading inward for what is already held. Sub-rule from CORR-184: **a thin
> bibliography entry is not evidence a claim is unsourced — the numbers live in the nodes.**

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

---

## THREAD G — THE DURATION ARM, PROPERLY DECOMPOSED (**OPEN, saved 2026-08-09, three live sub-levers**)

**Saved deliberately so it is not lost again.** Rounds 169–171 audited the oestrogen axis and reported it
as a verdict on duration. It is one sub-lever of five (CORR-183).

**THE FRAME** — `fusion_is_proliferative_exhaustion`, grade B, `weise2001`: senescence is **spontaneous**;
fusion is what happens to a plate that has **run out**; oestrogen **accelerates every senescence parameter
and causes none of them**. **Duration = time to proliferative exhaustion.**

| # | sub-lever | status | next step |
|---|---|---|---|
| 1 | slow the oestrogen multiplier | **in stack** (anastrozole); closed 169–171, bounded | — |
| 2 | **raise the YIELD** | **OPEN — never attempted by anyone** | `g_l2_raise_the_yield_per_progenitor` |
| 3 | **add progenitors (POOL)** | **OPEN — 1 compound, 1 length endpoint** | `g_l2_larger_pool_with_intact_flux` |
| 4 | **stop spending the pool** | **OPEN — the stack may be the spender** | `g_l2_cycling_the_progenitor_pool` |
| 5 | **cycle the pool** | **OPEN — tractability 5, highest in atlas** | same gap; needs no drug |

**② YIELD.** `the_exchange_rate_between_growth_and_pool_depletion`, grade B — **height = pool × yield, and
nothing has ever targeted the yield.** `lui2018`: metacarpal (fuses 2–3 wk) **14 µm bone per RZ cell** vs
femur (never fuses) **146**, non-overlapping CIs *inside one animal*. `schrier2006` forces the term by
exclusion — oestrogen and dexamethasone **both lower** RZ proliferation yet move senescence in **opposite**
directions (dex *raises* RZ cell number P=0.016 by blocking differentiation out).

**③ POOL.** `trompet2024` — intra-articular SAG: RZ PTHrP⁺ cells 65.5→139.8/mm² (P=0.017), proliferation
and terminal cell size **unchanged**. Unilateral SAG beads: **+2.75% at 1 mo → +3.63% femur at 6 mo, 8/8,
P=0.00004 — the effect GREW.** Limits: bead moved pool + h_term + rate together; **short systemic SAG did
nothing** (femur P=0.247) → **local delivery only**.

**④ THE STACK MAY BE SPENDING THE POOL.** `chu2025` (PNAS) — GH shifts RZ stem-cell divisions to the
**committed** side and **depletes** the pool; authors propose **intermittent GH**. Graded **D**: dose was
~**100× therapeutic** and the **GHR knockout did not change bone length**. Human data = one 14-y-old
specimen showing the cells are *present*.

### ROUND 180 — **ROUTE 4 WORKED TO THE BOTTOM.** It closes as a lever and survives as the hazard bound on route 1.

`route4_fate_leakage_worked`. Ranked #1 of eight because it was the only route with **both** a positive
length endpoint and an existing compound. Worked properly, it does not hold.

**THE RANKING, for the record — nothing crossed off, just queued:**
**1** fate leakage · **2** self-renewal/SOC niche · **3** external recruitment · **4** transit time ·
**5** column density · **6** column entry · **7** terminal cell size · **8** attrition.

**FIRST JOB WAS A PROVENANCE FIX THE ATLAS HAD FLAGGED ITSELF.** `orikasa2024` was held via a
**summarisation step**, never read directly. Read from PMC:

> femur length equivalent at all time points **"except in earlier time points of P21, indicating that
> Hedgehog activation negatively affects the bone length only transiently."**

**Not a null — a transient decrement (CORR-186).** The summarisation dropped the direction, and the
direction is the point.

**AND THE LEAK IS SMALL, WHICH IS WHAT CLOSES THE ROUTE.** The premise was that progenitors lost to
osteoblast fate are recoverable value. `orikasa2024` states the baseline: descendants of PTHrP⁺ resting
chondrocytes normally contribute **"only a small number of osteoblasts and CAR cells"** to adult marrow.
**The conversion is created by Hedgehog activation, not revealed by it.** Little to plug.

**Two more things the summary had dropped, both against the route:**
- **The expansion self-resolves** — labelled cells rise P21→P36, **fall at P56/P70, no difference by P96.**
- **Removing Hedgehog does not shorten bone** — Smo cKO cut PTHrP⁺ column contribution significantly with
  **bone length and plate structure unchanged.** Other cells compensate. A pool you can cut for free isn't
  a pool worth plugging.

**AND THE ROUND-179 RECONCILIATION IS DOWNGRADED.** I proposed the Hedgehog lever has a *time-dependent
sign*. Reading both primaries, **the two manipulations differ in KIND, not just duration**: `trompet2024`
doubled resting-zone PTHrP⁺ cells with **proliferation and terminal cell size explicitly unchanged** — a
clean pool expansion; `orikasa2024` caused **loss of quiescence** and clonal derangement that obliterated
the resting–proliferative boundary, columns widening to 5–6 cells. Duration is now one candidate among
dose, cell-autonomy, delivery, species and genetic-vs-pharmacological. Graded **E**.

**WHAT IT LEAVES BEHIND IS WORTH MORE THAN THE LEVER.** Route 1 (SOC niche) is next-ranked, and **Hedgehog
is the only signal anyone has used to manipulate that niche.** So route 4 is not a separate lever — it is
**the hazard specification for route 1**: push Hh too hard or too long in these cells and the expanded pool
leaves the plate as trabecular osteoblasts, the plate distorts, and the bone gets **transiently shorter**.
`trompet2024` is the only protocol on record that appears to stay below that threshold.

**THE DECIDING MEASUREMENT WAS NEVER TAKEN, AND IT IS SMALL.** `trompet2024` **never lineage-traced its
SAG-treated animals.** Nobody knows whether the cells it added to the resting zone stayed chondrocytes or
followed the `orikasa2024` route into the marrow more slowly. **One trace on an existing protocol** decides
whether the atlas's only positive pool result is a real pool gain. Gap rewritten around exactly that.

**NEXT: ROUTE 1 — self-renewal / the SOC niche.** Its measured effect is 1.37× clone size within one bone,
its causal test (axitinib) exists, and route 4 has just told us what its main tool does when overdriven.

---

### ROUND 179 — **EIGHT ROUTES TO YIELD, NOT ONE.** I'd worked one branch of a flow system and then searched it for agents.

`every_mechanical_route_to_yield`. The user's objection was correct and it was a scoping error, not a search error.

**THE FLOW.** progenitor → [renew vs commit] → transit-amplifying cell → [N divisions] → [exit to
hypertrophy] → hypertrophic cell. **Yield = cells delivered per progenitor consumed**, so anything losing
cells between the ends, or spending a progenitor for nothing, lowers it.

| # | route | status |
|---|---|---|
| 1 | raise self-renewal fraction | **OPEN** — mTORC1 failed (pool w/o flux); **SOC niche = 1.37× within one bone, never pursued** |
| 2 | lengthen transit | the only one worked; PTHrP–Ihh, Jansen warning |
| 3 | cut attrition in transit | **CLOSES ON DIRECTION** |
| 4 | **cut FATE LEAKAGE to osteoblast** | **OPEN AND NEW** |
| 5 | cut failed column entry | real, **no lever** |
| 6 | column density | untouched |
| 7 | terminal cell size | small, IGF-owned, double-covered |
| 8 | external recruitment | changes the accounting; never costed |

**④ FATE LEAKAGE — the first genuinely new route, and it reframes our best pool result.** A progenitor
that becomes an osteoblast delivers **zero length**. `orikasa2024`: sustained Hedgehog in PTHrP⁺ resting
chondrocytes → "patched roses", wider columns, plate hyperplasia — **then the descendants migrate out of
the plate and become trabecular osteoblasts, with no significant bone length change.** The pool was
expanded and the expansion was spent on bone.

**And `trompet2024` used SAG — the same pathway — for +3.63% femur (8/8, P=0.00004).** The difference:
trompet's bead was **local and transient** (Gli1 signal gone by 3 weeks); orikasa's deletion is
**permanent**. **The Hedgehog lever may have a time-dependent sign — pulse expands and lengthens,
sustained converts to bone.** Graded **E**: the two differ in duration, reversibility, delivery *and*
genetic-vs-pharmacological all at once, so duration is one of four candidates. **Neither paper cites the
other for this.** New gap `g_l2_does_the_hedgehog_lever_have_a_time_dependent_sign` — one lineage-traced
duration-response would settle it and give our only positive pool intervention a **dosing rule**.

**③ ATTRITION CLOSES.** Mechanism real — `velentza2023`, venetoclax cuts viability and suppresses growth
in cells, metatarsals and mice, so survival is rate-limiting. But the one manipulation that *reduces*
chondrocyte death — `eaton2014` ASK1 KO — protects the **terminally differentiated** cell (which already
delivered its length) and **shortens the proliferative zone**. All available pharmacology points the wrong
way.

**⑤ COLUMN ENTRY is a distinct loss term with no lever.** `yuan2023` images it directly: joining a column
is an **active integrin-mediated rotation**; α-parvin loss → disorganised PZ, binucleation, cell death,
dilated RZ, dwarfism. A cell that fails to rotate wastes its progenitor's investment. Entirely
loss-of-function.

**AND THE ONE IDEA THAT COULD BREAK THE ROUND-178 CONSTRAINT.** That round found charging needs IGF/Akt
**low** and driving velocity needs it **high** — one switch. **The escape is zone selectivity.**
`oichi2023`: *Igf-1* transcript is **higher in the resting zone than the proliferative zone** — the RZ has
its own local source. `harboe2024`: **PAPP-A sets local IGF bioavailability in cartilage by cleaving
IGFBPs**. **Lower resting-zone IGF availability while maintaining systemic IGF and the pool charges while
velocity continues.** Nothing achieves that today, and `harboe2024` shows the *unselective* version is
harmful (global PAPP-A loss → shorter femora, disorganised columns, rescued by IGF-I). **Mechanism with no
agent — but the only route that dissolves the constraint instead of working around it.**

---

### ROUND 178 — **FOUND IT. The first yield-raising intervention on record — and it names the switch.**

`the_charge_discharge_switch`. Retargeting the screen from *agents* to *denominators* worked immediately.

**THE MEASUREMENT — stronger than either yield I'd computed.** `oichi2023`, mouse proximal tibia,
`Axin2CreERT2;R26R-ZsGreen` fate mapping through 7 days of dietary restriction then refeeding:

| | result |
|---|---|
| labelled **columns** (numerator) | **up** — adj. P=0.0043 (P41), **P<0.0001** (P48); absolute count higher at P48 (P=0.0461) |
| labelled **progenitors, top 50 µm** (denominator) | **unchanged at every timepoint** — P>0.9999 at P41 and P48 |

**Numerator up, denominator flat, both lineage-traced in the same animals.** `nilsson2014` and `lui2018`
divide separately-measured standing stocks; this counts progeny per progenitor directly.

**THE SWITCH, NAMED.** Restriction lowered circulating IGF-1, **growth-plate Igf-1**, and **resting-zone
p-Akt** together; refeeding restored all three; **rhIGF-1 reversed the p-Akt fall**; the IGF1R inhibitor
picropodophyllin lowered p-Akt⁺ cells in the top 50 µm (P=0.0435). Igf-1 transcript is **higher in resting
than proliferative zone** (P=0.0041) — local source, not just endocrine.
> **Low IGF-1/Akt CHARGES the pool and blocks differentiation. High IGF-1/Akt DISCHARGES it into columns.**
> The authors: exogenous IGF-1 *"stimulated differentiation of the pooled chondroprogenitors, **decreasing
> their numbers**."*

**THIRD INDEPENDENT LINE ON OUR OWN GH ARM — no shared method.** `chu2025` (GHR cKO + label retention) ·
`dauber2026` (clinical trajectory: same first-year SDS, GH then slows, CNP sustains) · `oichi2023`
(nutrient gating of Akt). **The GH/IGF-1 arm is the discharge signal.**

**⚠ THE HARD CONSTRAINT, and it limits the round-171 insight.** Charging needs IGF-1/Akt **LOW**. Driving
velocity needs it **HIGH**. **They are the same switch.** So the round-171 finding — that accelerators
rescue a duration lever whose monotherapy failed on velocity — **does NOT transfer to the yield arm.** You
cannot charge and drive simultaneously. Any strategy here is **forced to alternate**, not combine.

**THE HONEST LIMIT, AND IT IS DECISIVE.** **The cycle restored the deficit and did not exceed control** —
tibial deficit 0.02 mm (M) / 0.10 mm (F) at P62, both ns. **Yield rose; total length did not**, because the
charge phase cost growth. `gafni2001` sits in exactly the same place from glucocorticoid: 3-week senescence
delay, **14% vs 88% fused**, deficit 17.4 → 1.6 mm — **and it stopped with growth still running in the
treated arm.**

> **The question is no longer whether yield can be raised. It is whether a charge phase can be paid for.**
> Two experiments got to the edge of the answer and both stopped there.

**Also registered:** `hallett2021` — resting chondrocytes sit in a **Wnt-inhibitory** environment; Wnt
*activation* **impairs** column formation. So Wnt inhibition keeps cells resting = **pool conservation
without flux**, the Tsc1 failure mode. **Not** an amplification lever. Unresolved tension with `oichi2023`,
whose progenitors are marked by **Axin2 — a Wnt target gene**. Logged as a conflict, not smoothed over.

**`g_l2_cycling_the_progenitor_pool` upgraded to tractability 4 and partially answered.** What remains:
follow a cycle **to skeletal maturity** (gafni2001's design plus continued follow-up); **repeated** cycles
at matched intake (battery or loan?); and whether the charge phase can be paid for by any route other than
losing growth — which the shared switch makes hard.

---

### ROUND 177 — SCREEN RUN. **Dexamethasone does not compute — and the reason is structural.** The screen returned the HUMAN ANCHOR instead.

`the_yield_screen_first_pass` + `the_human_anchor_for_yield`.

**① THE HUMAN ANCHOR — the decomposition holds in man, at the same number.** `kember1976`, human distal
femur, Harpenden Growth Study radiographs + Institute of Orthopaedics histology:

| | birth–2y | 13–14y | fall |
|---|---|---|---|
| amplifying compartment (cells/column) | 49.6 | 25.3 | **1.96×** |
| terminal hypertrophic cell height (µm) | 34.4 | 31.3 | **1.10×** |

→ **88% of the log fall is compartment size.** Mouse (between-bone) **88%**. Rabbit (drug) **91%**.
**Three species, four contrast types, no shared data, same answer.**

**Terminal cell height is conserved across SPECIES too** — human 25–39 µm, mouse 18–33, rat 18–38, across
a **tenfold** difference in cycle time. Fourth independent line.

**② THE NUMBER THAT RESCALES EVERYTHING.** Human distal femur at 5–8y: 1.4 cm/yr = 38 µm/day ÷ 33 µm cell
= **1.2 new cells/column/day**, across ~24 proliferating cells → **cell cycle 20 DAYS. Rodent is 2.**
Round 174 independently computed mouse at **10.8 and 8.33** cells/column/day — Kember's tenfold factor,
recovered from different data fifty years later.
**A five-week rodent experiment spans ~17 proliferative cycles; five weeks in a human spans fewer than
two.** Every kinetic result this programme rests on was measured on the fast clock. Kember says it
himself for this exact tissue: *"it is unwise to extrapolate the findings in this tissue from mouse to
man"* — and names a structural reason: in man an **inert zone 0.5–1.2 mm** lies between the proliferating
cells and the epiphysial vessels, which rodents do not have.

**③ THE SCREEN'S NEGATIVE, WITH A PRECISE DIAGNOSIS.** A yield needs a **resting-zone CELL COUNT**. The
field reports **resting-zone HEIGHT**. `gafni2001` has growth rate + terminal cell size + zone heights and
**never counts a resting-zone cell**; `weise2001` measures six numerator terms and uses the resting zone
only as the landmark for cell position 1. The three datasets that *do* carry the denominator — `lui2018`,
`schrier2006`, `nilsson2014` — are the three already used. **And height cannot be substituted for count on
dexamethasone specifically**, because `schrier2006` shows it *raises* RZ cell number (P=0.016) without a
matching height change: the substitution fails hardest on the agent it was wanted for.
**This corrects round 176's optimism** — the numerator is common, the denominator is rare.

**④ METHOD VALIDATED, AND IT ISN'T MINE.** `gafni2001` names the round-174 construction explicitly:
*"proliferation rate … assessed by dividing the growth rate by the height of the terminal hypertrophic
cell **according to the method of Kember and Sissons**."* Standard since 1976. **What is novel is bolting a
resting-zone denominator onto it.**

**⑤ AND gafni2001 CONTAINS THE BEST DURATION RESULT IN THE ATLAS, TWO-THIRDS RUN.** Five weeks of
dexamethasone → senescent curves **right-shifted ~3 weeks** (P<0.001 GP and HZ height, P<0.005 PZ); at 16
weeks recovery **88% of control plates fused vs 14% treated**; femoral deficit **17.4 mm → 1.6 mm**.
**Growth was still running in the treated arm and finished in the controls when the study stopped.**
The sign of the final length difference is **unmeasured** — and it is the same question as
`g_l2_cycling_the_progenitor_pool`, far closer to answered than a feeding experiment would get.

**SCREEN CONTINUES WITH A SHARPER CRITERION: search for the DENOMINATOR, not the agent.** Any study with
resting-zone cell counts + a growth rate is computable whatever it was testing; any study with
resting-zone height is not, however relevant its drug.

---

### ROUND 176 — **THE FIRST YIELD UNDER A DRUG.** Schrier proposed it in 2006. It now has a number.

`the_first_yield_under_a_drug`. Both nilsson2014 figures supplied; `atlas/tools/nilsson2014_yield.py`.

**RABBIT PROXIMAL TIBIA, ON TREATMENT 11–16 wk:**

| | grown µm | RZ lost | **YIELD** | THC mean | cells made | **AMPLIF** |
|---|---|---|---|---|---|---|
| vehicle | 7,980 | 9.0 | **887** | 69.5 | 114.8 | 12.76 |
| oestradiol | 7,130 | 14.1 | **506** | 66.2 | 107.6 | 7.63 |
| **ratio** | 0.89 | **1.57** | **0.57** | 0.95 | 0.94 | **0.60** |

**Oestrogen spent 57% more pool to deliver 11% less bone.** Yield **0.57×**.

**The decomposition replicates across species AND across contrast type.** Amplification 0.598, terminal
cell size 0.953 → **91% of the log effect is amplification.** Round 174 got **88%** in *mouse* from a
*between-bone* contrast. Two species, two designs, no shared data. Same split.

**A second construction inside the same experiment agrees.** BrdU per column integrated ÷ RZ lost:
vehicle 3.32, oestradiol 1.82 → **0.55**, against **0.57** from the length route. They share only the
denominator — the numerators are calcein-derived growth × cell size vs BrdU incorporation. **Two per cent
apart.**

**THE LINE THAT CHANGES WHAT WE DO — the yield effect is REVERSIBLE; the pool loss is not.** Washout
16–21 wk, no drug in either arm: yield ratio **1.12** (length route) / 0.88 (BrdU route) — bracketing
unity. **The 43% deficit is gone.** But the RZ deficit created during treatment is still there at 21 wk.
**Oestrogen damages the denominator permanently and the exchange rate only while present.** That assigns
the yield term to nilsson's *reversible* half — which nobody had done, because nobody had computed it.

**THE BAR, NOW A NUMBER.** Vehicle yield fell **887 → 457** across the two intervals — **the untreated
yield halves every 5 weeks.** Against that decay, 5 weeks of oestrogen cost **4.2 weeks of extra yield
decay**: oestrogen roughly **doubles the decay rate**. Any candidate agent is measured against a baseline
falling by half every five weeks on its own.

**WHAT IT SAYS ABOUT THE STACK.** Anastrozole was carried as a *duration* agent, reframed round 173 as an
*exchange-rate* agent on bone age. Third reading, and the most direct: **removing oestrogen protects the
yield**, worth ~the doubling of decay rate avoided. **Not a new lever — the same lever scored on the right
axis for the first time.** Graded **E**: no aromatase inhibitor has ever had a yield computed under it.

**AND IT BOUNDS THE PRIZE.** Oestrogen removal restores the yield **to** baseline. **Nothing known raises
it above baseline.** The entire remaining prize is slowing a decay that runs at 1.94-fold per 5 weeks.

**THE SECOND DELIVERABLE — THE METHOD.** Any experiment reporting **three** things in the same animals —
longitudinal growth rate, terminal hypertrophic cell size, resting-zone cell count — **yields a yield.**
Many published papers report all three. The quantity went unmeasured for twenty years because nobody
divided.

**NEW GAP — `g_l2_yield_screen_of_the_published_literature`, tractability 4, NO NEW ANIMALS.** Priority
targets: **① dexamethasone** (`schrier2006` — the only agent known to move the exchange rate the *opposite*
way; if its yield computes, it is the first yield-RAISING intervention on record); ② any FGFR-inhibitor
study that counted resting-zone cells (settles kot2026); ③ CNP/GH studies with an RZ count (confirms from
data, not inference, that neither touches amplification); ④ thyroid hormone and `forcinito2011`.

---

### ROUND 175 — AMPLIFICATION IS **TRANSIT TIME**, not division rate. The target is named and the circuit is already in the atlas.

`amplification_is_transit_time`. Four full texts read (Newton, Mizuhashi, Cooper — user-supplied; nilsson
Fig 2 digitised from the supplied panel).

**AMPLIFICATION IS CLONE SIZE, AND NEWTON MEASURED IT.** Col2-creERT/Confetti tracing:
- clone size **7.8 ± 0.3** centrally vs **5.7 ± 0.1** laterally (P=0.0012) — **by distance from the
  secondary ossification centre**. Amplification differs **1.37× within one bone** by anatomy.
- **axitinib delaying SOC maturation REDUCED clone size** (P=0.0023) → the SOC is **causal**.

**THE MECHANISM OF ITS DECLINE — and it redefines the drug.** Newton, in their own words: the change
*"did not reflect changes in chondrocyte proliferation or growth rate"*; EdU + morphometry gave **fewer
flat cells but more labelled hypertrophic cells** at P30 vs P3, so flat cells *"do not exhibit increased
replication, but **move to the hypertrophic layer more rapidly** in older mice."*

> **Amplification = residence time in the proliferative compartment before hypertrophic commitment.**
> The lever is **NOT "proliferate faster"** — that is what every velocity agent does and what every assay
> in this literature measures. It is **"delay hypertrophic commitment without slowing proliferation."**
> The two are routinely conflated and are *opposite* in their effect on the pool.

**THE CIRCUIT WAS ALREADY HERE AT GRADE B AND NOBODY CONNECTED IT.** `pthrp_ihh_feedback_loop`, written
**2026-08-05**: PTHrP acts on PTH1R "to keep those cells cycling and **delay the switch to hypertrophy**";
the loop is "a negative feedback loop whose **geometry sets the length of the proliferative column**."
**Column length is amplification.** `mizuhashi2018` makes it bidirectional — the transit-amplifying
compartment *maintains* PTHrP⁺ stem-cell fate via forward PTHrP + reverse Ihh.

**COOPER RESOLVES THE APPARENT CONFLICT AND HANDS OVER h_term.** Its headline (volume dominates
differential elongation) is about **RATE** and about **VOLUME**. Jerboa metatarsal: **volume 2.9×** mouse
but **height only +58%** — volume includes radial expansion that adds no length. Axial height ratios are
modest in three datasets: **1.32× mouse, 1.45–1.75× rat, 1.58× jerboa/mouse.** And **IGF-1 owns it**:
Igf1-null mice have the **same number** of hypertrophic chondrocytes, each **30% shorter axially**, and the
between-bone height difference is **abolished**. → **h_term is covered TWICE (GH/IGF-1 + CNP);
amplification ZERO times.**

**RATE ≠ YIELD.** A subject with years of pool left should buy rate. **A subject with months of pool left
should buy yield.** That is the argument for the objective.

**TWO INTERVENTIONS, BOTH WITH NULLS THAT MUST TRAVEL:**
- **mTORC1 up (Tsc1 KO)** — clone size ↑ (P=0.0342), CD73 zone ↑ (P=0.0025), EdU⁺ stem cells 62.4±7.5 vs
  24.7±3.7 (P=0.014), symmetric division ↑ — **but "neither proliferation of chondroprogenitors nor their
  recruitment into the proliferative layer changed detectably"**, RZ became **disordered**, clusters had
  **no ColX or Ihh**. **Pool expansion without flux** — exactly what `g_l2_larger_pool_with_intact_flux`
  was written to catch. Opposite manipulation → fewer columns + **mild growth retardation**. Graded **X**.
- **Hedgehog** — vismodegib +2 doses **FUSED the plate at P37**. Hh is *required*. SAG raised niche
  proliferation but did **not** expand the CD73⁺ domain (P=0.3) — separates proliferation from identity,
  and bears on `trompet2024`.

**THE HUMAN WARNING, STATED BEFORE ANYONE PROPOSES THE DRUG.** The obvious handle is **PTH1R agonism** —
and constitutive PTH1R activation in humans is **Jansen metaphyseal chondrodysplasia, which is
SHORT-limbed**. Delayed commitment is **not monotonically good**; the loop has an optimum and Jansen sits
past it. Blomstrand (PTH1R loss) is lethal at the other end. **This is a titration problem, and nothing
has ever been titrated against amplification because amplification has never been the endpoint.**

**NILSSON FIG 2 DIGITISED** (`atlas/tools/nilsson2014_fig2.py`, read off by eye, value_unverified). A
structural amplification index (PZ cells/column ÷ RZ cells/mm) is **lower under oestrogen at every
post-baseline age in both bones** — tibia 0.954 then **0.847** of vehicle; radius 0.972 then 0.941. The
direction the paper asserts and never quantified. **Not the yield** — both terms are standing stocks.
**16–21 wk is a WASHOUT: the deficit persists with no drug in either arm.**

**STILL NEEDED FROM NILSSON: Figure 3 (BrdU proliferation rate).** That is the flux numerator. With it,
the first true yield-under-a-drug becomes computable.

---

### ROUND 174 — YIELD DECOMPOSED. It is **amplification**, not cell size, and nothing in the stack touches it.

`yield_is_amplification_not_cell_size`. **First round of the yield programme.**

**The test that had to be run first.** A length-yield is a *product*:
**µm bone per progenitor = (cells produced per progenitor) × (µm per cell)** = **AMPLIFICATION ×
TERMINAL CELL HEIGHT**. The atlas already has an arm on the second factor — the CNP axis, which
`nakao2015` puts on the hypertrophic zone. So if the 10× yield gap were mostly cell size, **yield would be
h_term renamed and there would be no new lever.**

**It is not.** Mouse, 2–3 wk, femur (never fuses) vs metacarpal (fuses at 2–3 wk):

| term | ratio |
|---|---|
| yield (length) | **10.4×** [6.1–17.3] |
| terminal cell height | **1.32×** [1.15–1.55] |
| **→ amplification** | **7.9×** |
| **log gap from cell size** | **12%** |
| **log gap from amplification** | **88%** |

Tibia vs metacarpal: **93% amplification.** **Rat independently replicates the cell-height half** —
femur/metacarpal **1.45, 1.46, 1.75, 1.47, 1.69** at 1/2/4/8/12 wk. **Terminal cell height is conserved to
within ~2× between bones whose fusion times differ by an order of magnitude, in two species.**

**And amplification fails FIRST.** Mouse cells/column/day: femur **10.80 → 10.60 → 8.33** at 1/2/3 wk;
metacarpal **6.58 → 3.35 → 1.02**, with its RZ falling **78.2 → 48.7 → 24.1**. Metacarpal terminal cell
height still holds at 23–25 µm until week 3 (then 15.9). **Cell size is a late casualty; amplification is
already gone.**

**THE TARGET, NAMED.** Height = **pool × amplification × terminal cell height**. Vosoritide works the
right-hand term (the 1.3× one). Anastrozole is an exchange-rate agent on bone age. GH *spends* the pool.
**The middle term — nearly 8× variable — has no agent in this stack and none in this atlas.**

**One candidate, graded E deliberately:** amplification should read out as **proliferative**-zone output,
and `kot2026` has infigratinib raising femur length *with PZ height* — that signature. **But raising
proliferation ≠ raising divisions per progenitor consumed**; an agent could do the first while spending
the pool faster. `kot2026` measures no resting-zone denominator. **First question of round 175.**

**CORR-185 — species error caught before it entered the atlas.** `lui2018`'s workbook holds **mouse and
rat**, and only `FigS3` names either. `FigS2` (the richest sheet — and therefore the tempting one) is
**rat**. My first run divided a **mouse** yield by a **rat** cell height. Corrected: 7.2× → **7.9×**, 16% →
**12%**. The conclusion survived — *that is luck, not method.* Rule: **establish species from the file
before reading a cell.** The contaminated run had also shown the metacarpal RZ *rising*, which would have
contradicted `rz_depletion_causes_fusion` on an artefact.

**NEW GAP — this is now the programme:**
`g_l2_what_sets_amplification_in_the_proliferative_column`. **The assay is the deliverable and it does not
exist.** Amplification needs both terms in the same animals: lineage-label RZ cells at t0
(`Pthrp-CreERT2` or H2B-GFP label retention), count labelled progeny reaching hypertrophy by t1. Run
untreated first — **nobody has the normal value or its age curve** — then across FGFR inhibition, PTH1R
agonism, and the two agents already known to move the exchange rate oppositely (oestrogen, dexamethasone).

**Candidate control nodes for the commitment step, none ever assessed as amplification levers:**
PTHrP–Ihh feedback loop · FGFR3 · HDAC4–MEF2C · mTORC1. All are studied as *proliferation* or *hypertrophy*
regulators — **different quantities**.

---

### ROUND 173 — THE EXCHANGE-RATE TABLE, BUILT (`bone_age_cost_per_centimetre`)

At bone age 16 the question is **not how to add years to the clock but how many centimetres to extract per
year the clock still runs.** `atlas/tools/bone_age_cost.py`:

| agent | cm per bone-age year | strength |
|---|---|---|
| **anastrozole on GH** | **1.64× (95% CI 1.37–1.91)** | **robust** — growth comparable, so the height term *cancels exactly* |
| **vosoritide** | 4.8 → 10.4 (**~2.15×**) | **direction only** — ±0.5 y reading error spans **1.31×–6.00×** |
| **growth hormone** | **not placeable** | pays in **progenitors**, which BA/CA cannot see |
| erdafitinib | uncomputed | 3 favourable observations, none pairing height with bone age in one comparison |

**The result:** the two placeable agents improve the exchange rate by **different routes** — anastrozole
lowers the denominator at constant numerator, vosoritide raises the numerator at constant denominator.
The atlas design rule (*stack across control points*) appearing as arithmetic. **Predicts they compose
rather than compete — and nobody has ever measured the exchange rate for two agents given together.**

**Converging signature on GH:** identical first-year SDS to vosoritide in the same three conditions
(GH 0.49/0.62/0.70 vs vosoritide 0.69) — then **GH slows in subsequent years and the CNP axis sustains.**
`chu2025` supplies the mechanism. Two independent lines, one conclusion.

**CORR-184 — my round-172 flag was false.** The `dauber2026` bone-age figure *is* sourced:
**BA/CA 0.94 ± 0.20 → 0.92 ± 0.17, P=0.22**, unchanged in every subgroup, held in
`terminal_cell_volume_is_the_undefended_term` — whose "weak null" caveat was better calibrated than my
flag. Fifth of the family. Sub-rule added: **a thin bibliography entry is not evidence a claim is
unsourced; the numbers live in the nodes.**

**NEXT ON THIS THREAD, in order:**
1. **Yield is the only never-attempted sub-lever** — and `schrier2006`'s dexamethasone result is the one
   demonstrated way to conserve the pool. Ask whether pool conservation is separable from its growth
   suppression *when accelerators are running*. Nobody has tested a pool-conserving agent on top of a
   velocity stack.
2. **Price the second currency.** Until progenitor cost has units, GH cannot be ranked and the table has a
   hole where the stack's largest agent should be.
3. **The SAG route is local-delivery-only** — which is a constraint, not a disqualification, and the atlas
   has never asked what a local intra-SOC delivery would look like in a human.

---

### ROUND 172 — DURATION BROKEN DOWN. It is five sub-levers, I audited one, and three of the other four are open.

`the_duration_term_broken_down`. **CORR-183, procedural, and the fourth of a family.**

**THE REFRAME, from the atlas's own keystone.** `fusion_is_proliferative_exhaustion` (grade B,
`weise2001`): senescence is **spontaneous** in vehicle-treated animals, fusion happens when proliferation
approaches zero, and **oestrogen accelerates every senescence parameter and causes none of them** — a rate
multiplier on a programme already running. So **duration = time to proliferative exhaustion**, not time to
oestrogen-driven closure. Rounds 169–171 audited the multiplier and reported a verdict on the clock.

**THE FIVE SUB-LEVERS:**

| # | sub-lever | status |
|---|---|---|
| 1 | slow the multiplier (oestrogen) | **in stack**; closed exhaustively 169–171, bounded |
| 2 | **raise the YIELD** | **OPEN — never attempted by anyone** |
| 3 | **add progenitors (POOL)** | **OPEN — one compound, one length endpoint** |
| 4 | **stop spending the pool** | **OPEN — and the stack may be the spender** |
| 5 | **cycle the pool** | **OPEN — tractability 5, highest in atlas** |

**2 — YIELD.** `the_exchange_rate_between_growth_and_pool_depletion`, grade B: **height = pool × yield per
cell spent, and nothing has ever targeted the yield.** Not hypothetical — `lui2018` per-animal data give
metacarpal (fuses at 2–3 wk) **14 µm of bone per RZ cell** vs femur (never fuses) **146**, non-overlapping
CIs *inside one animal*. Movable in principle: `schrier2006` — oestrogen and dexamethasone **both lower**
RZ proliferation yet move senescence in **opposite** directions (dex *raises* RZ cell number, P=0.016, by
blocking differentiation out). Both observables excluded by measurement → the residual is the yield.

**3 — POOL.** `trompet2024` — intra-articular SAG doubled RZ PTHrP+ cells (65.5→139.8/mm², P=0.017) with
proliferation and terminal cell size **unchanged**. Unilateral SAG beads in the femoral SOC: **+2.75% at 1
mo → +3.63% at 6 mo, 8/8 animals, P=0.00004. The effect GREW rather than washing out.** Honest limits,
already recorded: the bead moved pool + h_term + rate together, and **short systemic SAG did nothing**
(femur P=0.247) — this is a **local-delivery** lever.

**4 — THE STACK MAY BE SPENDING THE POOL.** `chu2025` (PNAS): GH shifts RZ stem-cell divisions toward the
**committed** side and **depletes** the pool, cell-autonomously via GHR; authors offer it as the
explanation for GH's declining long-term efficacy and propose **intermittent GH**. **Counterweights that
must travel with it, both already in the atlas:** dose was 5 mg/kg/day ≈ **100× human therapeutic**, and
the **GHR knockout did not change bone length** (tibia P=0.31, femur P=0.35). Graded **D, conflicting.**
Human component is **one** 14-y-old epiphysiodesis specimen showing PTHrP+ cells are *present* — and
`orikasa2026` calling them "GH-responsive in humans" **overstates its own primary source**.

**THE SYNTHESIS — the actual answer.** Duration and velocity are not independent. Every velocity agent has
a **bone-age cost per centimetre**, and *nobody has put the agents on one axis*. `mauras2008` is the clean
instance: anastrozole added to GH left **linear growth comparable** while bone age advanced **+2.5 vs +4.1
y** — it bought duration **without buying velocity**. `dauber2026` is the claimed CNP counterpart at +4.0
SD velocity with BA/CA reportedly unmoved.

**FLAG RAISED:** that `dauber2026` bone-age figure is **not in the abstract** and was **not verified from
full text**. It is the single most load-bearing unverified number in the stack — it is the only claimed
human bone-age-sparing velocity effect. Bibliography entry annotated accordingly.

**NEW GAP:** `g_l7_bone_age_cost_per_centimetre_across_the_stack`, tractability 4 — **not an experiment, a
table**, buildable from published data plus one full-text retrieval. If agents separate >2× on this ratio,
the stack is reweightable at late bone age from existing data. If they don't, bone-age cost is a property
of growth itself and only the progenitor routes remain.

---

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
