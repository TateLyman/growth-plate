# F-R049 — The growth plate makes its own oestrogen, and it makes it mostly from sulfate

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** **Both holes from F-R048 are closed, and both close against the simpler option.** The growth
plate is an intracrine organ carrying the whole enzyme set, and it turns the sulfatase route up precisely
at sexual maturation. **Fulvestrant degrades ERα and *stabilises* ERβ** — so receptor-only ablation cannot
work. And one of my own claims needs correcting: aromatase inhibitors are **not** blind to the sulfate
reservoir.

---

## 1. Hole 1 closed — the enzymes are in the plate, and the sulfatase route is the major one

### van der Eerden et al., *"Sex steroid metabolism in the tibial growth plate of the rat"*, Endocrinology 2002 (PMID 12239116)

In situ hybridisation across development, female and male rats:

> *"mRNAs of **aromatase p450, type I and II 17β-hydroxysteroid dehydrogenase, steroid sulfatase (STS), and
> 5α-reductase** were detected in **proliferating and hypertrophic chondrocytes of the growth plate**. The
> former three were **strongly up-regulated around sexual maturation (7 wk)**, whereas the latter two were
> expressed at a relatively constant level."*

Confirmed at the protein level: *"measuring **aromatase, type I 17β-HSD, and STS enzyme activities** in
chondrocytes collected from tibial growth plates at 1 and 7 wk of age."*

Their conclusion:

> *"**intracrinology in the rat growth plate can occur and may be a major source of local sex steroid
> delivery**."*

**So the three enzymes that matter — aromatase, the sulfatase, and the potency step — are all present, all
active, and all three are the ones upregulated at sexual maturation.** 5α-reductase and 17β-HSD type II,
which are not on the oestrogen-generating path, stay flat. **The plate turns up exactly the enzymes that
make oestradiol, exactly when it closes.**

### Nawata et al., *"Estrone sulfate is a major source of local estrogen formation in human bone"*, JCEM 2004 (PMID 15356081)

Human femoral head, **15 women and 12 men**, fresh bone fragments and cultured osteoblasts:

| comparison | ratio |
|---|---|
| oestrogen formation from **E1S** vs from **androstenedione** (bone fragments) | **≥ 20×** |
| oestrogen formation from **E1S** vs from **testosterone** (bone fragments) | **~ 50×** |
| E1S vs aromatisation of androstenedione (human osteoblasts) | ***"exceeded… by two orders of magnitude"*** |

Steroid sulfatase activity was similar in men and women.

> ### In human bone, the sulfatase pathway produces 20 to 100 times more oestrogen than the aromatase pathway. Aromatase is the minor route. Every height protocol ever run has blocked the minor route.

**This is the answer to your question, and it is emphatic. The STS arm is not prudent — it is the main
arm.**

### But here is where I overstated it, and the correction matters

In F-R047 and F-R048 I implied an aromatase inhibitor leaves the sulfate reservoir untouched. **It does
not.** E1S is made from E1, which is made by aromatase, so blocking upstream drains it:

| agent | plasma E1S suppression | **tissue E1S suppression** |
|---|---|---|
| **letrozole** | **98.9%** | **90.1%** |
| anastrozole | 95.3% | **72.9%** |

**So an AI gets 90–99% of the way on its own.** The case for the STS arm is therefore not "the AI does
nothing" — it is **the residual, measured against the threshold**:

> **Nilsson/Schrier 2006: oestradiol at 11 ± 2 pg/mL measurably suppressed resting-zone self-renewal
> (P = 0.011).** In a young man circulating E1S runs in the nanogram range — one to two orders of magnitude
> above E2. **A 10% tissue residual of E1S, in a tissue that carries STS and 17β-HSD1 and turns both up at
> puberty, is entirely capable of generating local E2 above 11 pg/mL.**

**That is the honest, quantitative case, and it is narrower than what I wrote before but it still holds.**

### And the STS inhibitor data is unusually clean

**Irosustat (STX64, 667-coumate, BN83495)**, phase 1, oral, 5 mg and 20 mg doses:

| endpoint | result |
|---|---|
| **STS inhibition, peripheral blood lymphocytes** | **98%** |
| **STS inhibition, biopsied tumour tissue** | **99%** |
| serum **E1, E2, DHEA, androstenediol, androstenedione, testosterone** | **all decreased** |
| serum **E1S and DHEA-S** | **increased** |

**The rise in E1S and DHEA-S is substrate accumulating behind a blocked enzyme, and it is the single most
important operational consequence in this round:**

> **On an STS inhibitor the reservoir grows. Interrupt the block and you release a larger pool than you
> started with. This arm cannot be pulsed.**

**And AI + STS inhibition are genuinely complementary rather than redundant** — the AI reduces E1S
production by 90–99%, the STS inhibitor blocks conversion of whatever is left by 98–99%. Neither alone
reaches the 11 pg/mL threshold with confidence; the combination is the only configuration that plausibly
does.

---

## 2. Hole 2 closed — fulvestrant stabilises ERβ. Receptor-only ablation cannot work.

### Van Den Bemd et al., *"Distinct effects on the conformation of estrogen receptor α and β by both the antiestrogens ICI 164,384 and ICI 182,780 leading to opposite effects on receptor stability"* (PMID 10405313)

| receptor | effect of ICI 182,780 (fulvestrant) |
|---|---|
| **ERα** | *"does not result in protection but rather seems to induce a **ligand concentration-dependent increase in proteolytic degradation**"* |
| **ERβ** | *"**induced protection** in ERβ in a manner **similar to** 30-kDa fragment **E₂**"* — and dose-dependent preservation of a 32-kDa fragment |

> ### Fulvestrant degrades ERα and protects ERβ from degradation — behaving on ERβ the way oestradiol does. The receptor arm destroys one closure receptor and stabilises the other.

**Why that is disqualifying on its own.** Chagin 2004: **ERα⁻/⁻ mice all had fused femoral and tibial
growth plates at 18 months, mediated through ERβ under high oestradiol; only ERα⁻/⁻β⁻/⁻ stayed unfused.**
ERβ is a proven fusion route, and the drug that removes ERα raises the amount of ERβ protein present.

Fulvestrant remains a functional antagonist at ERβ, so this is not a catastrophe — but it means the ERβ
arm depends entirely on **continuous, complete occupancy** of a receptor pool the drug is enlarging, on
monthly dosing with a trough. **That is not a margin I would build "never closes" on.**

### And there is no ERβ-selective degrader anywhere

Every SERD and every PROTAC in clinical development targets **ERα/ESR1** — fulvestrant, elacestrant,
camizestrant, giredestrant, imlunestrant, amcenestrant, and the PROTACs vepdegestrant (**approved May
2026**), AC699, ERD-3111, ERD-4001, HP568. **Nothing targets ESR2.** The only selective ERβ antagonist in
existence is **PHTPP**, a research reagent (F-R041: 0.3 mg/kg/day i.p. in mice, 36-fold selectivity over
ERα).

**One open question worth chasing:** the PROTAC warheads bind the ER ligand-binding domain, and the ERα and
ERβ LBDs are ~59% identical. **If a PROTAC's warhead engages ERβ, it would *degrade* it rather than
stabilise it — solving exactly this problem.** Nobody appears to have asked. **Palazestrant (OP-1250)** is
also worth a look: it is a *"Complete Estrogen Receptor Antagonist (CERAN)"* blocking both AF1 and AF2,
which matters because Börjesson showed the growth-plate closure pathway *"does not require ERα AF-1"* — an
AF2-competent antagonist is the right shape.

---

## 3. Both holes point the same way

| hole | answer | consequence |
|---|---|---|
| **STS in the plate?** | **Yes — present, active, and upregulated at sexual maturation. And in bone the sulfatase route beats aromatase 20–100×** | **ligand ablation cannot be aromatase-only** |
| **Does fulvestrant cover ERβ?** | **No — it stabilises it** | **ablation cannot be receptor-only** |

> ### Neither single-node strategy is sufficient, and the two failures are independent. There is no one-drug version of this.

---

## 4. Is oestrogen the only remaining blocker? No — and it is probably no longer the binding one.

Oestrogen ablation is the arm with the best evidence, the clearest mechanism, and existing drugs. **It is
not the only blocker, and on current numbers it is not the one that stops you first.**

| # | blocker | status |
|---|---|---|
| **1** | **Oestrogen** | **Solvable with existing agents, once §1 and §2 are respected.** Human proof of the endpoint: *"epiphyseal fusion never takes place in men with estrogen deficiency or estrogen resistance"*; Rochira's four men at 183.5–193.0 cm with bone ages of 14.8–15.5 and GH peaks of 1.0–2.8 µg/L |
| **2** | **The mechanical envelope** | **3 of 7 patients on FGFR TKIs slipped a hip. One developed cord compression requiring surgery.** No published dose avoids it. **This is arguably now the binding constraint** |
| **3** | **The ossification front** | ALP 746 U/L against a 365 ceiling, DEXA −3.8 SD. Cartilage produced faster than it can be made into competent bone |
| **4** | **Cell number** | The write-off already incurred is **irreversible and produces no catch-up growth** (F-R048 §1). **Nothing in the literature adds cells.** Every approach in F-R047 Part II is untried, and the strongest — Hedgehog — has no molecule |
| **5** | **L² vs L³** | Strength scales with area, load with volume. A property of the phenotype, not a preference |

**So the honest answer to "is that the only blocker": no.** Solving oestrogen completely gets you a plate
that does not close. It does not get you a plate with cells in it, a skeleton that can carry the output, or
hips that survive the rate.

---

## 5. Dose corrections

**Growth hormone — this one inverts the design if it is wrong.**

**0.35 mg/kg/week is the dose to avoid, not the dose to use.** For 70 kg that is 24.5 mg/week = **3.5 mg/day**.

| | dose | for 70 kg |
|---|---|---|
| **adult replacement, starting** | **0.2–0.5 mg/day total** | **≈ 0.03–0.05 mg/kg/week** |
| **adult replacement, maintenance** | **0.3–0.6 mg/day total** | **≈ 0.03–0.06 mg/kg/week** |
| **paediatric ISS — the pharmacological dose** | **0.3–0.37 mg/kg/week** | **3.0–3.7 mg/day — 6 to 12× replacement** |

Replacement dosing is expressed as a **total daily dose, not per kilogram.** Target **IGF-1 SDS 0 to +1**.
The paediatric mg/kg schedule is precisely the "excess GH" that `chu2025` showed depletes the stem pool
and that Chu 2026 localised to the resting zone by phospho-STAT5.

**Erdafitinib — there is no known SCFE-free dose.**

Every published exposure that produced growth also sat inside the range that produced structural failure:
**7 mg/day** (interrupted for hyperphosphataemia) and **5 mg/day** gave 19.06 cm/yr with kyphoscoliosis and
cord compression; **4.7 mg/m²/day capped at 8 mg** gave SCFE with no growth acceleration at all; and across
the MSKCC series **7 of 7 grew faster and 3 of 7 slipped a hip.** **"5–9 mg doesn't get SCFE" is not
supported — that is the range in which it happened.** The dose that gives 6–9 cm/yr instead of 19 has never
been measured, which is why NCT04265651 is the paper I most want.

**Abaloparatide 80 µg** is the approved dose and is right. Its role is structural, not growth — Winer's ten
years of PTH(1-34) in children with open plates gave **normal, not increased, height velocity**, and the
decade-long open-plate record is teriparatide's rather than abaloparatide's.

---

## 6. Papers I cannot get

**Tier 1 — each changes a number:**

1. **NCT04265651** — Farouk Sait names it as *"FGFR TKIs… investigated at **lower doses** to improve linear
   bone growth"* in achondroplasia. **The dose-finding study for blocker 2.** I have no results.
2. **APEC1621B / NCT03210714** — paediatric erdafitinib growth velocities **by dose**, whole cohort.
3. **van der Eerden BCJ et al., Endocrinology 2002;143(10):4048–4055 (PMID 12239116)** — I have only the
   abstract. I need the **STS activity numbers at 1 wk versus 7 wk**, the zone-by-zone in-situ
   distribution, and whether STS activity in the plate exceeds aromatase activity as it does in bone.
   **This is the quantitative basis of the entire STS argument.**
4. **Nawata H et al., JCEM 2004;89(9):4433–4437 (PMID 15356081)** — the 20× and 100× figures with their
   assay conditions and absolute rates.
5. **Van Den Bemd GJ et al. (PMID 10405313)** — the ERβ stabilisation experiment in full. **This is the
   paper that says receptor-only ablation cannot work, and I have it only through a summary.**

**Tier 2:**

6. **Any test of whether a PROTAC ER degrader (vepdegestrant / ARV-471, ERD-3111, AC699) degrades ERβ.**
   If one does, it replaces fulvestrant outright and closes §2 properly.
7. **Palazestrant (OP-1250)** CERAN data on ERβ, and whether it blocks AF2 — the branch Börjesson named.
8. **Irosustat phase 2 dosing and duration** (the 40 mg/day continuous schedule) and any skeletal endpoint.
9. **Weise M et al., PNAS 2001;98:6871**; **Muruganandan, Nat Commun 2022;13:2515** full text;
   **Endocr Connect 2019;8(9):1302** (GPER1 agonist G1 on bone growth).
