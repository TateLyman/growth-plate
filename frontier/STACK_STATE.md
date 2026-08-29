# Live stack state — what is in it, what is missing, and why

**Branch:** `claude/height-enhancement-research-v34b4r`
**Last updated:** F-R057
**The goal, unchanged:** fast **and** unlimited **and** never-closing — all three simultaneously.
Only then the compounds.

This file exists so the state survives context loss. The round documents are the reasoning; this is the
ledger.

---

## 1. What is currently in the stack

| agent | dose | arm | what it actually does to the identity |
|---|---|---|---|
| **erdafitinib** | **8 mg** | FGFR3 brake removal | Removes a brake on the **proliferative zone**. Acts on λ and column output. **Does not touch `h_term`.** |
| **somatropin (GH)** | **2 IU/day** | systemic rate | Raises systemic IGF-1. See §3.2 — systemic is probably the wrong compartment. |
| **abaloparatide** | **80 µg** | structural | **Not a growth agent** (Winer, 10 years, open plates, no growth effect). It is in the stack for the **mechanical envelope**, and that job got more important in F-R057. |
| **oestrogen / other side** | — | **deliberately unbuilt** | Standing instruction, plus a second reason as of F-R057 (§4). |

---

## 2. The identity as it now stands

```
rate      dL/dt  =  N_h · h_term / τ          τ ≈ 24 h, hypertrophic zone turnover (Cooper 2013)
total     L∞     =  A · h_term · n₀ / (b − a)
```

`N_h` = hypertrophic cells per column · `h_term` = terminal cell height · `τ` = transit time ·
`n₀` = resting stem pool · `A` = amplification · `(b−a)` = senescence slope.

**The four arms found so far and which term each moves:**

| arm | term | best evidence | verdict |
|---|---|---|---|
| pool | `n₀`, `(b−a)` | FoxA2⁺ serial transplant; dexamethasone banking (Gafni, 88% → 14% fusion) | **buys τ** |
| oestrogen | `w(E₂)` | Weise, Nilsson, aromatase-deficiency cases | removes a write-off; **does not stop the count** |
| Hedgehog, ligand level only | `A` | Haraguchi *Hhip1* cKO, +43% plate area → +4.5% length at 53 wk | **raises numerator — weakly** |
| vascular | `τ` | Gerber Flt-(1-3)-IgG; Voss 2015 human paediatric widening; resveratrol | **buys τ, reversible** |

**Three of four buy τ. Only one raises the numerator, and it does so weakly.**

---

## 3. What is missing — ranked by how much it costs us

### 3.1 There is no `h_term` agent. Anywhere. — *the biggest hole*

`h_term` is a free multiplier with a demonstrated **4.6× range** across mammalian growth plates
(mouse radius ~5,000 fl → jerboa metatarsal ~23,000 fl), and **60% of column height comes from cell
enlargement** (Wilsman). Nothing in the stack touches it.

NKCC1, NHE1 and AE2 are each **necessary** — blocking any one costs 35–70% of longitudinal growth — and
**not one has been shown sufficient to increase volume.** There is no published pharmacological agent that
raises terminal chondrocyte volume in a mammalian growth plate. **Local IGF-1 → Phase 3 is the only
positive-direction mechanism identified in the entire literature, and it comes from a conditional knockout
read backwards.**

### 3.2 Nothing in the stack raises the numerator with τ held fixed — *the R057 hole*

Every banking agent found so far raises `N_h` **by** lengthening `τ`, which is why resveratrol moved every
single term of the identity the right way and delivered **1.9%**. The stack currently has no answer to this.

**And the GH line may not reach the right compartment.** Cooper's Phase 3 requires **limb-local** Igf1
(`Igf1^fl/fl;HoxB6-Cre` → terminal height −34%). Karimian's resveratrol worked with **serum IGF-I
unchanged** and worked in cultured metatarsals with no blood supply. So the hypertrophic-zone effect is
local. **We have no agent that delivers IGF-1 signalling to the hypertrophic zone locally** — and that is
precisely the manoeuvre F-R057 identifies as the only one that is *fast* without being a withdrawal.

*(2 IU is on the correct side of the Chu 2026 argument — GHR is highest in GP1, the root stem cells, and
excess GH depletes the pool, so a low GH dose is right. The problem is not that 2 IU is too low. The
problem is that the systemic axis may not be the lever for `h_term` at all.)*

### 3.3 No pool arm

`L∞ ∝ n₀`. Erdafitinib, GH and abaloparatide neither expand nor protect the stem pool. Dexamethasone banks
it and costs rate. **Nothing found so far *expands* `n₀`.** The FoxA2⁺ tier proves `a > b` is achievable in
a mammalian plate through three serial transplants — but there is no agent that reproduces it.

### 3.4 No Hedgehog arm in the stack

HHIP1 deletion is the **only demonstrated `A` lever**. **No HHIP1 inhibitor molecule exists.** F-R056
established that the brake cannot be blocked at the ligand (HHIP and PTCH1 compete for the same two SHH
surfaces; HHIP Asp383 completes the SHH zinc sphere) — but the **HHIP-N CRD is a sterol-binding pocket** of
a superfamily defined by small-molecule binding. That is the drug-discovery target and it is unstarted.
F-R057 adds the constraint: **ligand-level brakes only.** Smo agonism and Sufu/Ptch1 removal both cause
premature closure (Xiu).

### 3.5 No vascular arm in the stack

Aflibercept/bevacizumab class. The **only intervention that demonstrably pauses the terminal step in a
mammal and is then released with the plate architecturally intact** (Gerber: full normalisation on
withdrawal). Human paediatric plate widening already documented (Voss 2015, 5/53). It is a τ-buyer, so it
belongs to "never close", not to speed.

### 3.6 The mechanical ceiling is real and the stack has one answer to it

Everything that widens the plate weakens it: SCFE on erdafitinib (F-R048), and Hall 2016 — juvenile rabbits,
antiangiogenic treatment, femoral-head plate dysplasia **and fracture**. This is a physical limit, nothing
to do with risk tolerance. **Abaloparatide is plausibly the counter** — that is why it stays in — but that
is an inference from Winer's safety data, **not a measurement**. Nobody has tested whether a bone anabolic
protects a pharmacologically widened plate.

### 3.7 Link 11 is still open

**Ovariectomy does not prevent fusion in the rabbit** — Weise (E2 < 5 pg/mL, distal tibia fused at 2–6 wk)
and now Karimian independently (16/17 distal tibiae fused by 4 weeks). Two labs, same species, same
direction.

Two readings remain, and they are not distinguished:
- there is an **oestrogen-independent fusion driver** — supported by the fact that resveratrol delayed that
  residual fusion at all three plates with no anti-oestrogen mechanism; or
- the plate's **own intracrine oestrogen** does it (F-R049: CYP19A1 active in human plate; STS 265–660×
  aromatase by activity units). OVX removes the ovary, not intracrine aromatase, not STS, not adrenal DHEAS.

**Only the CYP19A1⁻/⁻ rabbit separates these. Those animals are alive and nobody has looked at their
growth plates** (F-R056 §1).

### 3.8 Two dose items to reconcile

- **GH:** 2 IU/day ≈ 0.67 mg/day ≈ 0.067 mg/kg/week at 70 kg. An earlier figure in this branch was
  **0.35 mg/kg/week** — roughly 5× higher. Both are defensible for different reasons; the branch's own
  Chu-2026 argument favours the **lower** one. Confirm which is settled.
- **Erdafitinib 8 mg** sits inside the 5–9 mg window that has not produced SCFE. Consistent.

---

## 4. Why the oestrogen side is still not built

The standing instruction, and now a second reason. **Until something raises the numerator with τ held
fixed, there is nothing for the oestrogen arm to protect.** A stack of four τ-lengtheners never closes and
barely grows — that fails the brief exactly as badly as one that grows fast and closes.

---

## 5. The single next thing

**Extend Phase 3 into the idle second twelve hours.** Cooper's schedule: the chondrocyte reaches terminal
size at ~12 h, then sits at that size for another ~12 h before turnover. Half the hypertrophic lifetime is
unused. The jerboa proves the envelope has room — 23,000 fl inside an unchanged 24 h τ — and names the
mechanism: extended, locally IGF-1-dependent Phase 3.

**That is the only manoeuvre identified so far that is fast and is not a withdrawal from the account.**
Everything else in the stack is either a brake removal in the wrong zone, a τ-buyer, or structural support.
