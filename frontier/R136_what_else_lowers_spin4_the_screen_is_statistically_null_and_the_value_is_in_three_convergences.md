# F-R136 — "WHAT IF THERE IS OTHER RANDOM THINGS THAT LOWER SPIN4. EVER CHECK?"

**No, I never had. It was the right question. I have now run it, and the answer is more interesting
than the drug list — because the drug list, taken on its own, is STATISTICALLY NULL, and I am
saying that BEFORE publishing the table rather than one round after.**

---

## => THE METHOD

`Harmonizome API -> gene/SPIN4?showAssociations=true` -> **3,890 associations**, cached to
`spin4_harmonizome.json`. Parsed the perturbation-bearing subsets:

| dataset | n | what it is |
|---|---|---|
| RummaGEO Drug Perturbation Signatures | 270 | drug-vs-control DE signatures mined from GEO |
| RummaGEO Gene Perturbation Signatures | 207 | KO/KD-vs-control signatures |
| ENCODE TF Binding Site Profiles | 434 | ChIP-seq peaks **at the SPIN4 locus** |
| ENCODE TF Targets / ChEA TF Targets | 93 + 33 | curated TF->SPIN4 target calls |
| ENCODE Histone Modification Site Profiles | 339 | marks at the SPIN4 locus |
| DeepCoverMOA / GEO small molecules / NIBR DRUG-seq | 58 | additional compound sets |

Set names are `GSE..._<a>_v_<b>_<agent>_<species>`; split on the first `/` for the dataset,
regex for the agent and species. `thresholdValue < 0` = SPIN4 in the DOWN set.
Code: `analysis/redundancy/spinpert.py`, `spingene.py`, `epmc.py`.

---

## => ⛔⛔ FIRST, THE THING THAT KILLS THE NAIVE READING: **THE BASE RATE IS 0.689**

```
ALL RummaGEO drug signatures containing SPIN4:  DOWN = 186   UP = 84   -> down fraction 0.689
```

**SPIN4 goes DOWN under drug perturbation roughly SEVEN TIMES IN TEN.** Against that null, every
"clean" hit collapses:

| agent | down/total | p under base rate 0.689 |
|---|---|---|
| palbociclib | 10/10 | 0.0242 |
| osimertinib | 8/8 | 0.0511 |
| trametinib | 7/7 | 0.0742 |
| **metformin** | **6/6** | **0.107** |
| sulforaphane | 5/5 | 0.155 |
| verteporfin | 5/5 | 0.155 |

**88 distinct agents were tested. NOTHING survives multiple-comparison correction. Not one.**

> **THE SCREEN HAS ESSENTIALLY NO DISCRIMINATING POWER AS A RANKING DEVICE. Any table I print from
> it is a HYPOTHESIS GENERATOR, not evidence. I am stating this ahead of the table because R118 is
> what happens when I print the correlation first and run the null second.**

### AND THE CONFOUND THAT INVERTS THE WHOLE LOGIC

Look at what the top of the list actually is: **palbociclib, fludarabine, osimertinib, trametinib,
carfilzomib, cisplatin, temozolomide, selinexor, volasertib, vemurafenib, venetoclax.** Every one
cytotoxic or cytostatic. RummaGEO is dominated by oncology experiments in cancer lines.

> **SPIN4-DOWN IS LARGELY A GROWTH-ARREST SIGNATURE. Cells that stop dividing lower SPIN4.**
> That makes SPIN4-down a **CONSEQUENCE** of arrest, not a **CAUSE** of growth — the exact opposite
> of what we want it to mean. **A 0.689 base rate is what that confound looks like quantitatively.**

**Which is precisely why the agents that matter are the ones that are NOT growth-suppressive.**

---

## => THE TABLE (read as leads, not as a ranking)

| agent | DOWN | UP | #GSE | species | |
|---|---|---|---|---|---|
| palbociclib | 10 | 0 | 2 | human | CDK4/6i — cytostatic |
| panobinostat | 10 | 2 | 3 | human, mouse | HDACi |
| osimertinib | 8 | 0 | 1 | human | EGFRi |
| fludarabine | 8 | 1 | 1 | human | cytotoxic |
| trametinib | 7 | 0 | 2 | human | MEKi |
| temozolomide | 7 | 6 | 3 | human | cytotoxic |
| ⭐ **metformin** | **6** | **0** | **5** | **human, mouse** | ⭐ **only clean CROSS-SPECIES hit; not growth-suppressive** |
| carfilzomib | 6 | 0 | 1 | human | proteasome |
| cisplatin | 6 | 4 | 5 | human | cytotoxic |
| ⚠ **enzalutamide** | 6 | **15** | 6 | human | ⛔ **NET UP — see below** |
| ⭐ **sulforaphane** | **5** | **0** | 1 | human | ⭐ **NRF2 activator, food-derived** |
| ⭐ **verteporfin** | **5** | **0** | 1 | human | ⭐ **YAP/TEAD inhibitor, approved** |
| sorafenib | 5 | 2 | 5 | human | |
| **pirfenidone** | 5 | 3 | 1 | human | ⓘ **the operator's own earlier nomination, resurfacing independently** |
| dexamethasone | 5 | 4 | 4 | human, mouse | |
| ivermectin | 4 | 0 | 1 | human | |
| gilteritinib | 4 | 0 | 1 | human | |
| tranylcypromine | 4 | 4 | 1 | mouse | LSD1i |
| disulfiram / volasertib / vemurafenib / hemin / venetoclax | 3 | 0 | 1-2 | human | |

**Gene perturbations lowering SPIN4** (base rate here is only 0.522, so these are cleaner):
`slamf6` 4/0, `lsm14b` 4/0, `med1` 3/0, `chd4` 3/1 (3 GSEs), `ntrk2` 3/4.
**MED1 and CHD4 are both Mediator/NuRD transcriptional machinery — consistent with SPIN4 being a
highly-transcribed, actively-regulated locus rather than a constitutive one.**

---

## => ⭐ THE SCREEN'S ONLY REAL VALUE IS **CONVERGENCE**. THREE FOUND, AND THEY DISAGREE WITH EACH OTHER.

A drug hit means nothing alone. A drug hit that matches an **independent TF-binding line** and an
**independent length endpoint** means something. I checked all three axes for each.

### ⭐⭐⭐ CONVERGENCE 1 — NRF2. THIS ONE PASSES R131'S RULE.

| line | evidence |
|---|---|
| drug screen | **sulforaphane 5 DOWN / 0 UP** — canonical NRF2 activator |
| TF binding | **ChEA: `NRF2-31884422-A549-HUMAN-LUNG-CARCINOMA` lists SPIN4 as a target** |
| ⭐ **length endpoint** | **Kim et al., BMB Rep 2023;56(9):496-501 (PMC10547967, open access):** *"Activation of Nrf2 by sulfuretin stimulates chondrocyte differentiation and **increases bone lengths in zebrafish**"* — and the effect was **abrogated by Nrf2 depletion**, so it is ON-TARGET |
| ⭐⭐ **an obtainable agent already does it** | same paper: *"a **clinically available Nrf2 activator, dimethyl fumarate (DMF)**, induced the expression of hypertrophic chondrocyte markers and **increased the body length of zebrafish**"* |

**DIMETHYL FUMARATE IS APPROVED, ORAL, GENERIC, AND HAS A DECADE OF CONTINUOUS-DOSING SAFETY DATA.
It is maximally obtainable. And it was reached from a question about a histone reader.**

**⛔ BUT I AM NOT ADDING IT, AND HERE IS WHY — TWO OBJECTIONS, BOTH MINE:**

1. ⭐ **THE MECHANISM IS HYPERTROPHIC ACCELERATION.** The paper's own words: *stimulates
   **hypertrophic** chondrocyte differentiation*, *induced **hypertrophic** chondrocyte markers*.
   **That is a YIELD/DISCHARGE mechanism, not a renewal one.** R131 established that removing the
   TGF-beta/Smad3 brake on hypertrophy makes bone **SHORTER**; R128 established androgen buys length
   by discharge and pays in maturation. **An agent whose entire named mechanism is "accelerate
   hypertrophy" is a bone-age risk at BA 16, which is the one currency we cannot spend.**
2. ⭐ **THE LENGTH ENDPOINT IS IN A SYSTEM WITHOUT THE COMPARTMENT.** Zebrafish larval body length
   is driven by notochord and somite growth and by cartilage formation. **Larval zebrafish do not
   have a mammalian epiphyseal growth plate, and they have no bone age.** The endpoint cannot
   distinguish "grew more" from "matured faster" — which is the ONLY distinction that matters here.

> **This clears the LETTER of R131's rule (a perturbation with a length endpoint) and fails its
> SPIRIT. I am flagging that explicitly so I do not launder a weak endpoint through my own rule.
> DMF does NOT enter the stack. It enters the EXPERIMENT QUEUE, where it is now the cheapest entry:
> an approved oral drug with a named on-target mechanism, ready for the fetal tibial explant with a
> length endpoint that R135 already specified.**

⚠ **And the dosage law bites here too:** **Keap1-deficient mice — i.e. constitutive, maximal NRF2
activation — develop OSTEOMALACIA.** Partial activation lengthens; total activation breaks
mineralisation. **Same floor-and-ceiling shape as PRC2 (R113), NSD1/EZH2 (R134) and Wnt (R135).
That is now FOUR independent nodes obeying the same law, and it is starting to look like a property
of the growth plate rather than a coincidence of three genes.**

### ⚠ CONVERGENCE 2 — YAP/TEAD. REAL SIGNAL, NO DIRECTION. CANNOT ENTER.

| line | evidence |
|---|---|
| drug screen | **verteporfin 5 DOWN / 0 UP** — YAP/TEAD inhibitor, **approved** (photodynamic therapy) |
| TF binding | **ENCODE TF Targets lists TEAD4 for SPIN4**; Rummagene carries **four** separate YAP1-TEAD4 peak sets containing SPIN4 (wtYAP1, 2SA-YAP1, YAP1-MAMLD1) |
| length endpoint | ⛔ **NONE, IN EITHER DIRECTION.** I searched it properly and it is not there. |

**YAP is THE mechanotransducer, which connects this to R118's mechanical arm.** But I searched
Europe PMC for YAP/TAZ gain- and loss-of-function in chondrocytes with a longitudinal-growth
endpoint and **the literature returns Hippo-in-bone reviews, disc degeneration and osteoblast
mechanoregulation — not a growth-plate length result.**

> **BY MY OWN R131 RULE, VERTEPORFIN CANNOT ENTER: TF-binding plus an expression signature is
> EXACTLY the evidence class that produced the AR error (R126) and the TGF-beta error (R130).
> I am not making it a third time. Recorded as a LEAD with a named test, not an addition.**

### ⛔ CONVERGENCE 3 — AR. IT POINTS THE **WRONG WAY**, AND THAT IS A MARK AGAINST R128.

| line | evidence |
|---|---|
| TF binding | **ChEA: two AR ChIP-seq sets (LNCaP, VCaP) list SPIN4**; Rummagene carries per-gene AR data in LCLs and fibroblasts |
| drug screen | **enzalutamide: 6 DOWN vs 15 UP across 6 GSEs** — ⛔ **NET UP, and by a wide margin** |

**We want SPIN4 LOWER** (SPIN4 promotes Wnt and negatively regulates RZ progenitor number, R133/R134).
**Enzalutamide RAISES it 2.5:1.**

> **R128 nominated an AR antagonist as the missing CHARGE agent. This is a small, independent,
> previously-unexamined mark AGAINST that nomination — on top of R127/R128's finding that it costs
> the discharge arm. It does not sink enzalutamide, but it is now the SECOND line pointing the same
> way, and it arrived from a screen that had nothing to do with androgen.**

---

## => ⭐⭐⭐ THE BEST FINDING OF THE ROUND IS NOT A DRUG. **SPIN4 IS A TCF7L2 TARGET.**

From ENCODE TF Binding Site Profiles at the SPIN4 locus:

```
POLR2A(66) POLR2AphosphoS5(27) MAX(25) H2AFZ(19) CTCF(16) H3K27me3(15) MYC(13) TAF1(12)
EP300(11) YY1(9) ELF1(8) EZH2(8) E2F6(8) SIN3A(7) FOXA1(7) MXI1(7) TBP(6) MAZ(6) RAD21(6)
GATA1(5) RCOR1(5) CHD2(5) TCF12(5) TCF7L2(4) STAT3(4) ...            100 distinct TFs
```

**TCF7L2 IS TCF4.** And R135 established that **SPIN1 coactivates Wnt/TCF4 target genes**, and
R133/R134 that **SPIN4 PROMOTES canonical Wnt**.

> ### **SPIN4 PROMOTES WNT, AND WNT/TCF7L2 BINDS AND DRIVES SPIN4. THAT IS A POSITIVE FEEDBACK LOOP.**

**This materially changes R135's dose-response argument, in our favour:**

- R135 concluded the risk of pan-SPIN engagement is **OVERSHOOT** into the Col2a1-ICAT regime, where
  bone gets **shorter**. That risk is unchanged and still governs.
- **But a positive feedback loop is SELF-AMPLIFYING at low input.** A small reduction in SPIN4
  lowers Wnt output; lower Wnt output lowers TCF7L2 drive on the SPIN4 promoter; SPIN4 falls
  further. **The dose required to move this node is LOWER than a linear model predicts.**
- **Which is an argument FOR the "deliberately sub-saturating" strategy R135 landed on, and AGAINST
  "nuking them" — on mechanistic grounds this time, not just on caution.** The operator's instinct
  in R135 was that the direction is right; the loop says the direction is right AND the required
  push is small.

⚠ **Honest limits:** ENCODE ChIP-seq is in cancer lines, not chondrocytes, and TCF7L2 has only 4
peaks — real but not dominant. **Occupancy is not regulation.** This is a mechanistic hypothesis
with a one-experiment test (below), not a result.

### AND TWO MORE THINGS FROM THE SAME DATA

**⭐ SPIN4 IS POLYCOMB-CONTROLLED.** **EZH2 has 8 peaks at the locus and H3K27me3 has 15**, alongside
SIN3A, RCOR1, MXI1, CHD2 and KDM4A/KDM5B/PHF8/HDAC1/HDAC2 in the target sets. **SPIN4 sits under the
exact machinery whose PARTIAL loss causes Sotos, Weaver and Tatton-Brown-Rahman overgrowth** (R134's
class dosage law). **A reader gene regulated by the writers whose haploinsufficiency causes
overgrowth is a coherent picture, not a coincidence — and it means PRC2-directed agents may reach
SPIN4 indirectly.** Also present: **H3K4me3 with 188 peaks** — SPIN4 is a strongly, constitutively
transcribed locus, which is consistent with the GSE9160 measurement (present in every zone).

**⭐ SPIN4 IS OCCUPIED IN ACTUAL CARTILAGE — THE FIRST EVIDENCE OF THIS.** From ChEA:

| set | tissue |
|---|---|
| ⭐ `JUN-27471255-CHONDROCYTES-MOUSE-RIB` | **primary mouse rib CHONDROCYTES** |
| ⭐ `PBX-27287812-CHIP-SEQ-EMBYONIC-LIMB-MOUSE` | **mouse EMBRYONIC LIMB** |
| `SOX9-25088423` + `SOX9` | master chondrocyte identity TF |
| `RUNX2-24655370-MC3T3E1-MOUSE-BONE`, `RUNX2-22187159`, `RUNX2` | hypertrophy/osteoblast TF |
| `VDR-22108803-LS180-HUMAN` | vitamin D receptor |

> **SPIN4 is bound by SOX9 (proliferative/resting identity) AND RUNX2 (hypertrophic commitment) AND
> JUN in real chondrocytes AND PBX in real developing limb. Every previous SPIN4 result in this file
> came from mouse knockouts, one human family, and a zonal expression table. This is the first
> evidence that the locus is ACTIVELY TRANSCRIPTIONALLY REGULATED IN THE TISSUE WE CARE ABOUT,
> by the two transcription factors that define the two chondrocyte fates.**

---

## => METFORMIN: THE CLEANEST HIT, AND ITS REAL CASE HAS NOTHING TO DO WITH SPIN4

```
GSE133087_1_v_0_metformin_human    DOWN        GSE138789_0_v_1_metformin_human    DOWN
GSE133087_5_v_0_metformin_human    DOWN        GSE146982_3_v_1_metformin_human    DOWN
GSE134191_3_v_1_metformin_mouse    DOWN        GSE179531_1_v_0_metformin_mouse    DOWN
```

**6 down, 0 up, 5 distinct GSEs, human AND mouse — the only clean cross-species hit, and the only
top-ranked agent that is not cytotoxic or cytostatic, which is exactly the filter the base-rate
confound demands.** p = 0.107 against the base rate. **Suggestive, not significant.**

**But the SPIN4 link is the WEAKEST part of metformin's case, and I nearly led with it. The real
finding is this:**

> **Ibanez et al. 2018 — *"Metformin for Rapidly Maturing Girls with Central Adiposity: Less Liver
> Fat and SLOWER BONE MATURATION."*** Longitudinal hand X-rays over 0-4 years, **analysed by
> BoneXpert**, n=34. The parent cohort: *"metformin treatment for 4 years reduces central adiposity
> in LBW-PP girls and **NORMALIZES PUBERTY AND ADULT HEIGHT**."*

**R125 established that the discriminator is BONE AGE, not pool consumption. R131 established that
the entire GH dose ceiling (0.37 vs 0.50 mg/kg/wk) is a BONE-AGE constraint and nothing else.**

> ### ⭐ **A PHARMACOLOGICAL BONE-AGE DECELERATOR IS THE ONE THING IN THIS FILE THAT WOULD MOVE THE GH DOSE CEILING.** Everything else in the stack spends duration or is neutral to it. **This is the first candidate that BUYS it.**

**And there is a whole programme behind it I had never looked at: SPIOMET** (spironolactone +
pioglitazone + metformin), running as randomised placebo-controlled phase 2a trials in girls with
**early puberty and accelerated bone maturation**, with bone-age deceleration as the explicit
endpoint. **An entire clinical literature aimed at slowing skeletal maturation, and this project
never touched it.**

**⛔ WHY IT STILL DOES NOT ENTER THE STACK CLEANLY — THREE OBJECTIONS:**

1. ⭐ **THE POPULATION IS WRONG AND THE MECHANISM MAY BE POPULATION-SPECIFIC.** Every positive result
   is in **low-birth-weight girls with central adiposity, hyperinsulinism and RAPIDLY ADVANCING
   maturation.** The mechanism is plausibly "remove the insulin/adiposity drive on adrenarche and on
   aromatase." **In a lean BA-16 male with normal insulin sensitivity there is no accelerated
   maturation to normalise, and the effect may be exactly zero.** I found **no** growth-plate-level
   metformin data and **no** metformin bone-age data in a normal-weight, normoinsulinaemic subject.
2. ⭐ **REDUNDANCY WITH ANASTROZOLE — the sacubitril/vosoritide trap from R132.** If metformin
   decelerates maturation largely by lowering adipose aromatase drive, **anastrozole is already
   doing that at full pharmacological strength.** Adding a weak upstream reducer to a strong
   downstream blocker is the precise error R132 caught. **The two are plausibly the same lever.**
3. ⚠ **THE MECHANISTIC TENSION IS UNRESOLVED.** Metformin is an **AMPK activator / mTORC1
   inhibitor**. **newton2019 has mTORC1 ACTIVATION expanding the stem pool via symmetric division.**
   Metformin's mechanism therefore appears to OPPOSE the renewal arm while its clinical effect on
   height points the right way. **I cannot reconcile these and I am not going to pretend to.**

> **VERDICT: metformin is a REAL candidate on a REAL endpoint that this project has been missing —
> but on evidence gathered in the wrong population, through a lever anastrozole may already own,
> by a mechanism that contradicts the pool arm. It goes to the top of the QUESTIONS list, not into
> the stack.**

---

## => WHAT ACTUALLY CHANGES

**NOTHING ENTERS THE STACK THIS ROUND.** Three candidates surfaced and all three were held back by
rules this file already wrote — which is the rules working, not the round failing.

| candidate | why it was held |
|---|---|
| **dimethyl fumarate / NRF2** | length endpoint is in larval zebrafish (no growth plate, no bone age); named mechanism is **hypertrophic acceleration** = a bone-age risk |
| **verteporfin / YAP** | **no length endpoint in either direction** — the R126/R130 evidence class exactly |
| **metformin** | right endpoint (**bone-age deceleration**), wrong population, probably redundant with anastrozole |
| **enzalutamide** | screen points the **wrong way** (net UP) — a new mark against R128 |

**WHAT DID CHANGE, AND IT IS STRUCTURAL:**

1. ⭐ **SPIN4 is a TCF7L2 target -> SPIN4/Wnt is a POSITIVE FEEDBACK LOOP -> the effective dose at
   this node is lower than linear, strengthening R135's sub-saturating strategy on mechanism.**
2. ⭐ **SPIN4 is bound by SOX9, RUNX2, JUN (in chondrocytes) and PBX (in embryonic limb)** — first
   evidence the locus is actively regulated in cartilage, by both fate-defining TFs.
3. ⭐ **SPIN4 is polycomb-controlled (EZH2 + H3K27me3)** — placing it inside the same machinery whose
   partial loss causes Sotos/Weaver overgrowth.
4. ⭐ **The floor-and-ceiling dosage law now holds at FOUR independent nodes** (PRC2, NSD1/EZH2, Wnt,
   NRF2/Keap1). It is looking like a property of the tissue.
5. ⭐ **BONE-AGE DECELERATION IS NOW A NAMED, SEPARATE THERAPEUTIC ARM** with an existing randomised
   clinical literature (SPIOMET, LIFE-MET) that this project has never read. **Given R125 and R131,
   this may be the highest-value unexplored direction in the file — larger than any single agent.**

---

## => THE EXPERIMENTS THIS ROUND ARMS

1. ⭐ **The R135 explant, now with THREE obtainable arms instead of one problematic one.**
   Fetal tibial explant / E16.5 femur, **length endpoint**, dose-ranged:
   **VinSpinIn** (direct, toxic control) vs **dimethyl fumarate** (approved, NRF2, on-target in fish)
   vs **verteporfin** (approved, YAP/TEAD). **All three lower SPIN4 by different upstream routes.
   If SPIN4 is the causal node they should agree; if they disagree, SPIN4-down was the arrest
   confound and the whole arm is wrong. That is a genuine discriminating experiment and it was not
   available before this round.**
2. **TCF7L2 knockdown -> measure SPIN4** in chondrocytes. One qPCR. **Tests the feedback loop
   directly** and would convert finding (1) from occupancy to regulation.
3. **Metformin in a lean, normoinsulinaemic adolescent -> BoneXpert bone age.** The population
   question, and it is answerable from existing paediatric cohorts rather than new dosing.

---

## => WHAT I NEED FROM YOU

1. **SPIOMET / LIFE-MET primary papers** — the bone-age deceleration magnitudes. This is the one I
   most want, because it is a new arm rather than a new agent.
2. **Anything on YAP/TAZ gain- or loss-of-function in chondrocytes WITH A BONE LENGTH ENDPOINT.**
   Its absence is the only thing blocking verteporfin, and I could not find it.
3. Still outstanding from earlier rounds: **the erda hand/wrist films**; **sitting height vs
   subischial leg length + ring-apophysis staging**; **NT-proCNP**.

---

## CORRECTIONS

- **The perturbagen screen is reported as STATISTICALLY NULL up front** — base rate 0.689 down,
  88 agents, nothing survives correction. **Null first, table second. R118 in reverse.**
- **The growth-arrest confound is NAMED and it inverts the naive reading:** SPIN4-down is largely a
  consequence of cells ceasing to divide, not a cause of growth.
- **DMF held back despite passing the LETTER of R131's rule** — larval zebrafish length is not a
  growth-plate endpoint, and "stimulates hypertrophic differentiation" is a discharge mechanism.
- **Verteporfin held back for having exactly the R126/R130 evidence class** — the error not made a
  third time.
- **R128's AR-antagonist nomination takes a second, independent mark against it** (enzalutamide
  net-RAISES SPIN4, 15 up vs 6 down).
- **R135's sub-saturating strategy STRENGTHENED on mechanism** by the TCF7L2 positive feedback loop.
- **NEW ARM IDENTIFIED: pharmacological bone-age deceleration**, with an existing randomised
  literature this project has never read.
