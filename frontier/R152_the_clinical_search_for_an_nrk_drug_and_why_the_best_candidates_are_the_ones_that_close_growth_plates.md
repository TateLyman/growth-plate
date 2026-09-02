# F-R152 — **THE CLINICAL SEARCH, RUN PROPERLY: NRK IS PHARMACOLOGICALLY ISOLATED (ITS HINGE BLOCK IS UNIQUE IN 435 HUMAN KINASES), AND THE DRUGS MOST LIKELY TO CATCH IT ARE THE ONES DOCUMENTED TO *CLOSE GROWTH PLATES*. ONE CANDIDATE SURVIVES THE FILTER: SOTRASTAURIN. AND I HAD TO CORRECT MY OWN OPTIMISM TWICE MID-ANALYSIS.**

**Direct answer: yes, there are clinical drugs that could plausibly hit NRK — but the ranking is
governed by a trap. Promiscuity is what would catch NRK (R151), and promiscuity in the clinic means
PDGFR/KIT, and PDGFR/KIT inhibition is what closes growth plates. The two properties are not
independent. Exactly one clinical molecule breaks the link.**

---

## => STEP 1 — **NRK IS PHARMACOLOGICALLY ISOLATED. THERE IS NO PROXY TARGET.**

I mapped R150's 23-position ligand-contact frame into **all 480 human protein kinases** (UniProt,
PROSITE PS50011; 435 aligned cleanly) and ranked by similarity **to NRK**:

| rank | kinase | %id to NRK | |
|---|---|---|---|
| 1 | **NRK** | 100% | — |
| 2 | MYO3A | **73.9%** | |
| 3–5 | **TNIK · MINK1 · MAP4K4** | **73.9%** | ⛔ the three R151 showed a selective drug discriminates against |
| 6 | TAOK1 | 71.4% | |
| 7 | CDK5 | 70.0% | |
| 8–11 | MYO3B · STK3 · MAP4K3 · PAK2 | 69.6% | |

> ⛔ **NOTHING in the human kinome exceeds 73.9%.** And on the **gatekeeper+hinge block alone** — the
> region that dominates ATP-competitive recognition — **NRK's `MELCAAGS` is UNIQUE. Not one other human
> kinase carries it.** (TNIK/MINK1/MAP4K4 = `MEFCGAGS`; STK3/STK4 = `MEYCGAGS`.)

**Consequence: there is no "drug this neighbour and you'll catch NRK" shortcut.** The proxy strategy
that works for most dark kinases does not exist here.

---

## => STEP 2 — SO THE FILTER HAS TO BE **PROMISCUITY**, AND THAT IS WHERE THE TRAP IS

R151's lesson: rentosertib lost 3.7× on a paralog with a **100% identical contact surface**. Selectivity
in an optimised molecule does not live in the contact residues. **Therefore only a promiscuous compound
can catch a kinase nobody designed for.**

I pulled every ChEMBL compound active ≤1 µM on 19 NRK pocket-neighbours (TNIK, MINK1, MAP4K1–5, TAOK1/2,
CDK5, PAK1/2, STK3/4, CSNK1D/E, SLK, ULK1, PTK2, STK39), intersected with **all 16,784 clinical-phase
molecules in ChEMBL**, and scored each against the growth-plate liability set (**PDGFRA/PDGFRB/KIT**).

| drug | phase | #proxies hit | ⛔ **PDGFR/KIT (nM)** |
|---|---|---|---|
| SUNITINIB | 4 | **15** | ⛔ KIT 0, PDGFRA 1, PDGFRB 0 |
| LESTAURTINIB | 3 | **15** | ⛔ KIT 7, PDGFRB 28 |
| NINTEDANIB | 4 | 13 | ⛔ KIT 3, PDGFRA 2, PDGFRB 2 |
| BOSUTINIB | 4 | 12 | ⛔ KIT 32, PDGFRB 200 |
| ⭐ **NERATINIB** | **4** | **12** | ⭐ **none ≤1 µM** |
| DOVITINIB | 3 | 11 | ⛔ KIT 1, PDGFRB 1 |
| MIDOSTAURIN | 4 | 6 | ⛔ KIT 8 |
| DASATINIB | 4 | 6 | ⛔ KIT 1, PDGFRA 0 |
| ⭐ **SOTRASTAURIN** | 2 | 6 | ⭐ **none ≤1 µM** |

> ### ⛔⛔ **THE TOP OF THE LIST IS THE IMATINIB CLASS, AND THAT CLASS IS DISQUALIFIED ON MECHANISM, NOT ON TOLERABILITY.**

**Verified, and worse than R145 had recorded** (`PMC11290534`, Germany-wide **CML-PAED II**, NCT00445822):

> *"During imatinib treatment, significant height reduction occurred, with medians of **−0.35 SDS at 12
> months and −0.76 SDS at 24 months**… **37%** experienced growth stunting below −0.5 SD… only **18%**
> were unaffected."*

And the mechanism paper it cites: ⛔⛔ **`Vandyke et al., Leukemia 2009` — "Imatinib mesylate causes
growth plate CLOSURE in vivo."** Nilotinib carries its own pediatric growth-retardation update
(PMID 34309636).

> ### ⛔⛔⛔ **FOR A PROGRAMME WHOSE ENTIRE PURPOSE IS TO HOLD THE PLATE OPEN AT BONE AGE 16, A DRUG CLASS THAT CLOSES IT IS CATEGORICALLY OUT. This is not a side effect to dose around — it is the exact inverse of the objective.**

---

## => STEP 3 — ⚠⚠ **TWO CORRECTIONS I HAD TO MAKE TO MY OWN ANALYSIS**

### ⚠ Correction A — the aggregation was biased optimistic
My pipeline took `min()` across all reported values per target. That silently reports the single most
potent measurement ever published. **Checking provenance changed the picture materially.** Where both
exist, the **recombinant kinase-domain panel** and **Kinobeads** (native protein, cell lysate — the more
physiological assay) disagree by up to **200-fold**:

| drug | target | recombinant Kd | **Kinobeads Kd** |
|---|---|---|---|
| neratinib | MAP4K3 | 7.7 nM | ⛔ **1753 nM** |
| neratinib | TNIK | 140 nM | ⛔ **30,000 nM (not detected)** |
| lestaurtinib | TNIK | 5.4 nM | ⛔ **30,000 nM** |
| bosutinib | MAP4K4 | 8.2 nM | ⛔ **30,000 nM** |

### ⚠ Correction B — **neratinib is not clade-promiscuous, and I nearly reported that it was**
It looked like the answer: approved, 12 proxies, PDGFR/KIT-clean, and *"MAP4K5 at 1 nM"*. But its own
targets are **EGFR median 2.5 nM, HER2 median 29 nM**, and by Kinobeads only **MAP4K5 (13 nM)** is
genuinely engaged — TNIK and MAP4K1 are not detected at 30 µM. **It is an EGFR drug with one real clade
off-target, not a clade inhibitor.** ⭐ Withdrawn as the headline.

---

## => ⭐ STEP 4 — THE HONEST RANKING, ON KINOBEADS WHERE AVAILABLE

| drug | primary target | **clade engagement** | PDGFR/KIT | verdict |
|---|---|---|---|---|
| **BOSUTINIB** | ABL1 1 nM, SRC 3.6 | ⭐ **MAP4K5 16, TNIK 23, MAP4K3 58** — within ~20× of its own target | ⛔ **KIT 32, PDGFRB 200** | ⭐ **most likely to catch NRK** ⛔ **disqualified — closes plates** |
| **LESTAURTINIB** | FLT3 3.0 | MINK1 41, MAP4K4 91 | ⛔ **KIT 7, PDGFRB 28** | ⛔ disqualified |
| ⭐ **SOTRASTAURIN** | PKCθ 1.0 nM | ⭐ **TNIK 38, MINK1 41** (~40× off primary) | ⭐ **clean** | ⭐⭐ **THE ONLY SURVIVOR** |
| NERATINIB | EGFR 2.5 nM | MAP4K5 13 only | ⭐ clean | ⚠ not clade-promiscuous |
| DEFACTINIB | FAK 0.2 nM | ⛔ **TNIK/STK24/STK26 all 30,000 nM** | clean | ⛔ **flatly inactive** |
| PF-562271 | FAK 0.6 nM | STK26 12, MINK1 631 | unmeasured | ⚠ phase 1, discontinued |

### ⭐⭐ SOTRASTAURIN (AEB071) — WHY IT IS THE ONE

| | |
|---|---|
| ⭐ **not an oncology drug** | Novartis; developed for **psoriasis and transplant rejection** — so the acceptable-risk profile is a chronic non-malignant one, unlike every other entry |
| ⭐ **clade engagement by Kinobeads** | **TNIK 38 nM, MINK1 41 nM** — native protein, cell lysate |
| ⭐ **PDGFR/KIT** | **no activity ≤1 µM** — escapes the growth-plate-closure mechanism entirely |
| ⭐ **oral, phase 2, human PK exists** | |
| ⛔ **discontinued** | efficacy, not safety, but obtainability is unresolved |
| ⛔ **primary target is PKCθ/PKCβ at ~1 nM** | broad PKC inhibition is immunosuppressive by design — that is what it was *for* |
| ⛔ **~40× off-target ratio** | to engage the clade you saturate PKC |
| ⛔ **never measured against NRK** | as with everything else |

---

## => ⛔ AND THE THEORETICAL ESCAPE HATCH, REPORTED HONESTLY AS HAVING NO MOLECULE

R151's kill is **equilibrium** math — Hill n=1, exposure cancels, engagement set by affinity ratio.
**That does not apply to an irreversible covalent inhibitor**, where occupancy accumulates with time
against protein resynthesis rather than tracking Kd. A weak covalent target can still reach high
occupancy. ⭐ **And NRK conserves Cys108** (verified in R150's design-spec check).

⛔ **But it goes nowhere, for two measured reasons:**
1. **85 of 435 human kinases (19.5%) carry that same cysteine** — AAK1, BRAF, FLT3, KDR, PLK1–3, TBK1,
   IKBKB, NEK1–9, ULK1/2, STK11, CHEK1… **no selectivity whatsoever.**
2. ⛔ **Every approved covalent kinase drug targets a DIFFERENT cysteine** — EGFR Cys797 / BTK Cys481
   sit at **gatekeeper+7**; TNIK/NRK Cys108 is at **gatekeeper+3**. TNIK and NRK have **Ser112** at the
   neratinib/afatinib position. **So the approved covalent drugs bind this clade reversibly, and the
   covalent advantage does not apply.** No literature exists on covalent Cys108 chemistry for MAP4K4 or
   TNIK — I searched.

---

## CORRECTIONS

- ⭐⭐ **NRK IS PHARMACOLOGICALLY ISOLATED — MEASURED ACROSS THE WHOLE KINOME.** Of 435 aligned human
  kinases, **none exceeds 73.9%** contact-set identity, and **NRK's gatekeeper+hinge block `MELCAAGS` is
  UNIQUE — no other human kinase has it.** There is no proxy-target shortcut.
- ⛔⛔ **THE TRAP: the drugs most likely to catch NRK are the ones documented to CLOSE growth plates.**
  Promiscuity is what would catch it (R151) and promiscuity in the clinic means PDGFR/KIT.
  **CML-PAED II: −0.35 SDS at 12 months, −0.76 SDS at 24 months, 37% stunted below −0.5 SD, only 18%
  unaffected. Vandyke 2009: "Imatinib mesylate causes growth plate closure in vivo."** ⛔ **Categorically
  disqualifying for a programme trying to hold the plate open — the inverse of the objective, not a
  tolerability question.** (Upgrades R145, which had only the 12-month figure and no mechanism.)
- ⚠⚠ **SELF-CORRECTION A — my aggregation was biased optimistic.** Taking `min()` across published
  values reports the single most potent measurement ever made. **Recombinant panels and Kinobeads
  disagree by up to 200×** (neratinib/TNIK: 140 nM vs 30,000 nM). All conclusions re-derived on
  Kinobeads where available.
- ⚠⚠ **SELF-CORRECTION B — NERATINIB WITHDRAWN AS THE ANSWER.** It looked ideal (approved, 12 proxies,
  PDGFR/KIT-clean, "MAP4K5 1 nM") but its own targets are EGFR 2.5 nM / HER2 29 nM and by Kinobeads only
  MAP4K5 (13 nM) is real — **TNIK and MAP4K1 undetected at 30 µM. An EGFR drug with one clade
  off-target, not a clade inhibitor.**
- ⛔ **THE FAK LEAD IS DEAD.** PTK2 shares NRK's `MEL` hinge, but **defactinib is flatly inactive on the
  clade (TNIK/STK24/STK26 all 30,000 nM)** and PF-562271 reaches MINK1 only at 631 nM vs FAK 0.6 nM —
  **1000× off**, and it is a discontinued phase 1.
- ⭐ **BOSUTINIB is the compound most likely to actually engage NRK** — MAP4K5 16, TNIK 23, MAP4K3 58 nM
  by Kinobeads, within ~20× of its own primary target. ⛔ **And it is disqualified: KIT 32 nM,
  PDGFRB 200 nM.**
- ⭐⭐ **SOTRASTAURIN (AEB071) IS THE ONLY CLINICAL MOLECULE THAT SURVIVES THE FILTER** — TNIK 38 nM,
  MINK1 41 nM by Kinobeads, **no PDGFR/KIT ≤1 µM**, oral, phase 2, and **non-oncology** (psoriasis and
  transplant, so a chronic-dosing risk profile). ⛔ Discontinued for efficacy; primary target is PKCθ at
  ~1 nM so clade engagement costs full PKC blockade; **and it has never been measured against NRK.**
- ⛔ **THE COVALENT ESCAPE HATCH IS REAL IN PRINCIPLE AND EMPTY IN PRACTICE.** Covalent kinetics break
  R151's equilibrium ceiling, and NRK conserves Cys108 — but **85/435 kinases share that cysteine (no
  selectivity)** and **every approved covalent kinase drug targets gatekeeper+7 (EGFR C797 / BTK C481),
  whereas Cys108 is gatekeeper+3; TNIK and NRK carry Ser112 at the covalent position.** No Cys108
  chemistry exists in the literature.
- ⛔ **NOTHING HAS EVER BEEN MEASURED AGAINST NRK.** ChEMBL 0 · BindingDB 0 · PDB 0 · absent from
  Eurofins KinaseProfiler (430) and KINOMEscan · the only molecules ever shown to occupy it remain
  Promega's broad-spectrum tracers (R149), and it was the **weakest of five MAP4Ks** there.
