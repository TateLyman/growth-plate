# F-R050 — Three of my own claims corrected, and the ablation strategy inverts

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** All three primaries read at source. **The sulfatase case survives and gets much stronger on the
numbers — but the specific reason I gave for it was wrong.** The fulvestrant problem is confirmed in cells,
not just in vitro. **And that confirmation inverts the architecture: ligand ablation is primary, and the
SERD is an adjunct with a liability that bites precisely when you need it most.** A fourth correction:
my GPER1 advice was contested and I did not know it.

---

## 1. van der Eerden 2002, at source — the numbers, and correction #1

### What I said, and what the paper says

**F-R049, my words:** *"The plate turns up exactly the enzymes that make oestradiol, exactly when it
closes"* — naming aromatase, 17β-HSD1 **and STS**.

**That is true for two of the three and false for STS.** I took it from the abstract, which lumps the
mRNA data. The activity measurements say otherwise:

| enzyme | 1 wk | 7 wk (sexual maturation) | regulation |
|---|---|---|---|
| **aromatase** (attomol/µg DNA) | F **59.0 ± 18.1**, M **46.0 ± 11.4** | F **665 ± 143**, M **718 ± 82.6** | **↑ 11–15×, P < 0.001** |
| **type I 17β-HSD** (attomol/µg DNA) | **absent** | F **89.8 ± 14.4** (P<0.001), M **80.2 ± 43.1** (P<0.01) | **absent → present** |
| **STS** (**picomol**/µg DNA) | F **0.44 ± 0.17**, M **0.19 ± 0.03** | F ~0.11–0.31, M **0.26 ± 0.03** | ***"no apparent age-related regulation"*** |

**Correction: STS activity in the growth plate is constitutive. It is not upregulated at puberty.**
Aromatase and 17β-HSD1 are.

### But look at the units — and the case gets far stronger than the one I made

**Aromatase is reported in attomoles. STS is reported in picomoles. Per microgram of the same DNA.**

```
1 pmol = 10⁶ attomol

STS at 7 wk (male)      = 0.26 pmol/µg DNA  = 260,000 attomol/µg DNA
Aromatase at 7 wk (male) =                        718 attomol/µg DNA

                                    ratio ≈ 360×
```

Across the range: **265× to 660×.** And the STS assay ran for **15 minutes** against an aromatase
incubation run **overnight** — so on a per-unit-time basis the gap is larger still, not smaller.

**Caveats, stated because the comparison is not clean:** the two assays use different substrates at
different concentrations (STS at 20 µM E1S; aromatase corrected against exemestane, which gave a maximum
of 72% inhibition and was taken as the specific fraction), and cross-assay comparison of Vmax-like numbers
is imperfect. **But three orders of magnitude is not an assay artefact, and it independently reproduces
Muir's finding in bone, in the growth plate itself, at a larger ratio.**

> ### The revised claim, which is stronger and better supported: STS is a constitutively open, very high-capacity gate. What puberty adds is aromatase, 17β-HSD1, and circulating substrate. The gate was always open.

**And that promotes 17β-HSD1.** It is **absent at 1 week and present at 7** — the one enzyme in the chain
whose appearance coincides with closure, and it is the potency step, converting weak E1 to E2. **On this
data HSD17B1 inhibition is not a third-line refinement; it is the pubertally-regulated node.**

**One more detail from the in situs:** at 7 weeks *"STS mRNA expression extended into the **early
proliferating zone**"* — the only enzyme to spread its territory at maturation. All the others stay in
late-proliferating and hypertrophic cells.

---

## 2. Muir 2004, at source — the kinetics change the arithmetic in a way that helps

Human femoral head, 15 women and 12 men, plus 17 osteoblast strains:

| measurement | value |
|---|---|
| STA, bone fragments (0.05 µM E1S) | **0.75 ± 0.18 pmol/100 mg bone/h** |
| **Km of bone sulfatase** | **5.2 µM (fragments); 5.9 ± 1.6 µM (osteoblasts)** |
| Vmax | 44 pmol/100 mg/h; **853 ± 296 pmol/mg protein/h** |
| STA, osteoblasts, women vs men | 1.04 ± 0.14 vs 1.29 ± 0.41 — **no sex difference** |
| **estrone sulfamate (EMATE) IC₅₀** | **~0.3 nM** |
| **STA vs dexamethasone-stimulated aromatase** | ***"STA exceeded that of dexamethasone-stimulated AA by 2 orders of magnitude"*** |
| aromatase without dexamethasone | ***"very low to undetectable"*** |

### The kinetics: the enzyme runs far below saturation, and that is good news

**Km ≈ 5.2–5.9 µM. Physiological E1S is ~0.005 µM** — the concentration Muir deliberately used as *"within
the normal range found in human adults."*

**So the plate's sulfatase operates at roughly 0.1% of Km, deep in the linear regime.** Local oestrogen
formation is therefore **directly proportional to E1S concentration**, with no saturation buffering.

**Which means aromatase inhibition does more than I credited it with in F-R047 and F-R048:**

```
letrozole reduces tissue E1S by 90.1%  →  local sulfatase-derived oestrogen falls ~90.1%
```

**But it also means the residual is exactly proportional, and the baseline is enormous:**

| | relative local oestrogen production |
|---|---|
| baseline | sulfatase **~100**, aromatase **~1** |
| **letrozole alone** | sulfatase **~10** (90% E1S reduction), aromatase **~0.01** → **~10** |
| **letrozole + irosustat** (98–99% STS block) | sulfatase **~0.1–0.2** → **~0.2** |

> ### After a maximal aromatase inhibitor, the residual sulfatase route is still roughly ten times larger than the aromatase route ever was. Adding an STS inhibitor takes ~90% suppression to ~99.8%.
>
> **Against Nilsson's threshold — 11 ± 2 pg/mL of oestradiol measurably suppressed resting-zone
> self-renewal — that is the difference between a few pg/mL of residual and a few hundredths.**

### And two things in Muir that belong in the interaction table

**(a) Glucocorticoid induces aromatase in bone.** *"AA was very low to undetectable in the absence of
dexamethasone but was **stimulated markedly by dexamethasone**, whereas STA remained unaffected."*

> **Abiraterone mandates prednisone. Prednisone induces the aromatase you are trying to block, in the
> tissue you are trying to protect.** This is a real, direct, previously unnoticed conflict inside the
> stack. It argues for the minimum glucocorticoid abiraterone tolerates — or for a CYP17 lyase-selective
> inhibitor (seviteronel, orteronel) that needs less.

**(b) There may be more than one sulfatase.** *"The Eadie-Scatchard plot… indicated **nonlinear rather than
linear kinetics, which might suggest the presence of more than one sulfatase isozyme in bone**."*
**Irosustat targets STS. If a second isozyme carries part of the flux, coverage is incomplete.** New hole.

**(c) EMATE is more potent than irosustat by orders of magnitude (IC₅₀ 0.3 nM) — and unusable**, because
oestrone sulfamate is itself oestrogenic on hydrolysis. That is precisely why the non-steroidal coumarin
irosustat exists.

---

## 3. Van Den Bemd 1999 at source, plus the cellular confirmation — correction #2, and it holds

### What the paper actually is

**A limited-proteolysis (trypsin) assay on in-vitro-synthesised receptor.** Not a cellular degradation
experiment. The authors say so:

> *"Whether the increased protease resistance of ERβ can also be observed in cells and tissues in terms of
> an increased receptor stability **needs to be examined**."*

**So F-R049's flat statement — "fulvestrant stabilises ERβ" — was stronger than that single paper
supports.** What it shows:

| | ICI 164,384 / ICI 182,780 |
|---|---|
| **ERα** | *"did not result in increased protection of distinct fragments, but rather led to a **slightly enhanced degradation** of the receptor"* |
| **ERβ** | *"induced a conformational change of ERβ resulting in a **stabilization**… increased protection of a similar 30 kDa fragment **as seen with E2**"*, plus *"a marked protective effect on an additional 32 kDa fragment"* |
| co-incubation with E2 | *"the E2 effect on ER conformation **can be overruled by the ICI compounds**"* |

ERβ is also intrinsically more protease-resistant than ERα — not from cleavage-site count (~60 in each,
~20 in each LBD) but from conformation.

### And the cellular experiment exists — the claim survives

Fulvestrant **increased ERβ expression at both mRNA and protein level in MCF-7 cells**, by immunoblot and
ELISA (*Oncotarget*: *"Fulvestrant… synergizes with tamoxifen in ERα positive breast cancer by
**up-regulation of ERβ**"*).

> ### Two independent lines — conformational stabilisation in vitro and mRNA plus protein upregulation in cells — say fulvestrant degrades ERα and raises ERβ.

**It still antagonises ERβ functionally** (the co-incubation shows it displaces E2 at both receptors). The
problem is not failure to block; it is that the arm depends on continuous complete occupancy of a receptor
pool **the drug itself enlarges**, on monthly dosing with a trough.

### And ERβ is genuinely present in the human growth plate

**Nilsson O, Chrysis D, … Sävendahl L, *"Localization of estrogen receptors-α and -β and androgen receptor
in the human growth plate at different pubertal stages"*, J Endocrinol 2003;177(2):319** — proximal tibial
growth plate biopsies taken at epiphyseal surgery, **16 boys and 8 girls, Tanner stages 1–5**:

> **Both ERα- and ERβ-positive chondrocytes were present throughout pubertal development, at greater
> frequency in the resting and proliferative zones than in the hypertrophic zone.**

**So the escape route is anatomically real in humans, in the compartment that matters** — though the
authors note *"any functional role of ERβ has not yet been defined in the human growth plate."* The
functional proof is Chagin's: **ERα⁻/⁻ mice all fused via ERβ at 18 months; only the double knockout stayed
open.**

---

## 4. The architecture inverts — and this is the real finding of the round

F-R047 made the receptor arm **"Layer 0 — the only complete solution"**, on the reasoning that chasing five
ligand sources is a losing game while destroying the receptor makes all of them irrelevant.

**That reasoning fails on §3, and the failure has a specific shape:**

> **Fulvestrant's ERβ liability only matters when ligand is still present. But if ligand were fully
> ablated, you would not need the SERD. So the SERD's risk is largest in exactly the scenario that
> justifies using it.**

**And the human existence proof was a ligand deficiency all along.** Rochira's four men are
**CYP19A1**-deficient — **aromatase deficiency, with completely intact ERα and ERβ** — and they reached
183.5–193.0 cm with bone ages of 14.8–15.5 and open radial epiphyses. *"Epiphyseal fusion never takes place
in men with estrogen deficiency or estrogen resistance."*

> ### The endpoint has been demonstrated in humans by removing the ligand while leaving both receptors intact. Ligand ablation is primary. The SERD is an adjunct that carries a liability the ligand route does not.

**Revised ordering of the ablation arms:**

| tier | arm | rationale |
|---|---|---|
| **1** | **aromatase inhibition** — letrozole 2.5 mg/day (98.9% plasma / 90.1% tissue E1S) or exemestane 25 mg/day (irreversible) | drops **both** the aromatase route and, because E1S derives from E1, **90% of the sulfatase substrate** |
| **1** | **STS inhibition** — irosustat, 98–99% enzyme block | takes the residual sulfatase route from ~10 to ~0.2 on the §2 scale. **Cannot be pulsed — E1S and DHEA-S rise behind the block** |
| **1** | **CYP17 inhibition** — abiraterone + minimum prednisone, or a lyase-selective agent | removes adrenal and gonadal substrate. **Note §2(a): the mandatory glucocorticoid induces bone aromatase** |
| **2** | **HSD17B1 inhibition** | the potency step, and **the enzyme that appears at puberty** (§1). Clinical-stage compounds exist |
| **2** | ligand hygiene — statin for 27-HC; no soy, flax, hops | sources no enzyme inhibitor touches |
| **3** | **SERD** | **demoted.** Adds ERα destruction but **upregulates ERβ**, and its benefit is conditional on the failure of tiers 1–2 |

**If a SERD is used anyway,** the two candidates worth checking are a **PROTAC** — vepdegestrant (approved
May 2026), ERD-3111, AC699 — since a PROTAC *degrades* what it engages rather than stabilising it, and the
ERα/ERβ ligand-binding domains are ~59% identical; and **palazestrant (OP-1250)**, a *"complete oestrogen
receptor antagonist"* blocking **both AF1 and AF2**, which matters because Börjesson showed the closure
pathway *"does not require ERα AF-1."* **Neither has been tested against ERβ that I can find.**

---

## 5. Correction #3 — my GPER1 advice was contested and I did not say so

F-R047, F-R048 and F-R049 all state: *"Do not block GPER1 — it is growth-promoting."* I based that on a
2021 chondrocyte-specific knockout showing decreased proliferative-zone thickness and shorter tibiae.

**The Sävendahl/Chagin/Ohlsson group ran the direct pharmacological test and found the opposite sign on
the knockout:**

**Iravani M, Lagerquist M, Karimian E, Chagin AS, Ohlsson C, Sävendahl L, *"Effects of the selective GPER1
agonist G1 on bone growth"*, Endocr Connect 2019;8(9):1302 (PMID 31434056):**

- mouse **and human** growth plate chondrocytes express GPER1
- ***"ablation of this receptor INCREASED bone length in mice"***
- **G1, ex vivo on metatarsals at multiple concentrations for 14 days: no effect.** G1 in vivo in
  ovariectomised mice: **no effect on tibia or femur**
- conclusion: *"E2 primarily modulates bone growth via ESR1"*

| | direction |
|---|---|
| **Iravani 2019 — global GPER1 ablation** | **bone length increased** |
| 2021 — chondrocyte-specific GPER1 knockout | PZ thickness and tibia length **decreased** |
| **G1 agonist, ex vivo and in vivo** | **no effect at all** |

**Correction: the sign of GPER1 on bone growth is contested between a global and a conditional knockout,
and GPER1 *activation* does nothing.** My instruction not to block it was stated with more confidence than
the literature supports. **Practically it changes little — G1's null means GPER1 agonism is not a free arm
either, and F-R047's claim that fulvestrant's GPER agonism is "the right sign by accident" is
unsupported** — but it was overstated and it is now corrected.

---

## 6. Holes, updated

| # | hole | status |
|---|---|---|
| **1** | ~~Is STS in the growth plate?~~ | **CLOSED. Present, active, constitutive, and ~265–660× aromatase activity in the same tissue** |
| **2** | ~~Does fulvestrant cover ERβ?~~ | **CLOSED, negatively. It upregulates ERβ — two independent lines.** Hence §4 |
| **3 NEW** | **A second sulfatase isozyme in bone** (Muir's nonlinear Eadie-Scatchard). Irosustat targets STS; a second isozyme would leave uncovered flux | open |
| **4 NEW** | **Prednisone induces bone aromatase** (Muir), and abiraterone mandates prednisone | open — argues for lyase-selective CYP17 inhibition |
| **5** | The erdafitinib dose giving 6–9 cm/yr instead of 19 | open, unmeasured anywhere |
| **6** | Everything in the pool section; Hedgehog has no molecule | open |
| **7** | Nobody has taken this combination | permanent |
| **8** | The mechanical ceiling — 3 of 7 hips | permanent |

---

## 7. Papers I still cannot get

**Tier 1:**

1. **NCT04265651** — *"FGFR TKIs investigated at lower doses to improve linear bone growth"* in
   achondroplasia. **Still the single most valuable missing item**, because it is the only study that could
   contain the dose in hole 5.
2. **APEC1621B / NCT03210714** — paediatric erdafitinib growth velocity **by dose**, whole cohort.
3. **Any characterisation of the second bone sulfatase isozyme** implied by Muir's Eadie-Scatchard
   nonlinearity — or any paper measuring what fraction of bone E1S hydrolysis irosustat actually blocks.
   *(Hole 3)*
4. **Whether any PROTAC ER degrader (vepdegestrant / ARV-471, ERD-3111, AC699) engages and degrades ERβ**,
   and **palazestrant (OP-1250) data against ERβ / AF2.** If one degrades ERβ, §4's demotion reverses.

**Tier 2:**

5. **Nilsson O et al., J Endocrinol 2003;177(2):319** — the human growth-plate ERα/ERβ/AR localisation
   paper. I have it through a summary; I want the **percent receptor-positive cells by zone and Tanner
   stage**, because that is the only quantitative human map of where the closure receptors actually sit.
6. **Histochem Cell Biol 2011 (PMID 22057437)** — *"Gender- and region-specific variations of ERα and ERβ
   expression in the growth plate of **spine and limb** during development and adulthood."* Directly bears
   on whether the axial plates carry the same receptors.
7. **HSD17B1 inhibitor clinical data** — FOR-6219 or equivalent, any phase 1/2 with steroid endpoints.
   §1 promotes this enzyme from third-line to the pubertally-regulated node.
8. **Weise M et al., PNAS 2001;98:6871**; **Muruganandan, Nat Commun 2022;13:2515** full text.
