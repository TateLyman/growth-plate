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
| **erdafitinib** | **8 mg** | **three jobs, not one (F-R060)** | (1) flux — PZ **+25%** in Fgfr3 cKO; (2) **terminal cell volume** — *"significant swelling of hypertrophic cells"* (infigratinib, JBMR 2024), HZ **+45%**; (3) **the closure step** — lowers **ERK1/2**, the same node phosphate→VEGFR2→caspase-9 uses to kill the terminal chondrocyte. **Works in wild-type: TYRA-300 femur +8.2%, tibia +6.4% in 4 wk; and the FDA tox package shows growth-plate thickening in NORMAL rats (≥1 mg/kg) and dogs (3 mg/kg).** **But see F-R061: at oncology doses it raises serum phosphate, which drives the very death signal it otherwise suppresses. The 8 mg label dose is titrated INTO phosphate 5.5–7.0 mg/dL.** |
| **somatropin (GH)** | **2 IU/day** | **AKT support for erdafitinib** | **Not a rate agent.** FGFR3 blockade alone is **apoptotic**; IGF-1 via sustained AKT rescues it. That is the job. Separately, 2 IU sits on the **physiological** side of the GH stem-pool sign flip (§3.8). **And a third candidate role as of F-R059:** GH **normalises terminal chondrocyte volume** in uremic rat via proposed Nkcc1 + Igf1 — the only half of the identity nothing else touches. One study, deficit-normalisation not supranormal gain; carried as a hypothesis. |
| **abaloparatide** | **80 µg** | structural — now with a mechanism | **Not a growth agent** (Winer, 10 years, open plates, no growth effect). For the **mechanical envelope** — and F-R060 gives the reason: *Fgfr3*-null mice show **increased femur length with decreased BMD**, and aromatase loss gives **increased osteoid and low phosphate**. **SCFE is the mechanical shadow of the effect we want, not an incidental toxicity.** |
| **serum phosphate** | **held at LOW-normal** | **sign reversed in F-R061** | F-R060 predicted oestrogen ablation would *lower* it and cause rickets. **Backwards for humans:** oestrogen ablation **raises** phosphate (Uemura TmP/GFR +28.5% on GnRH-a; Zhang NHANES n=7,005, 3.83 vs 3.98 mg/dL, P<0.001; rat NaPi-IIa mechanism). **And erdafitinib raises it on-target (89% of patients).** Both stack arms push phosphate UP, and **phosphate is the executioner's ligand.** Requirement: **binders to a normal target, not the oncology target of 7.0.** |
| **oestrogen / other side** | — | **deliberately unbuilt** | Standing instruction, plus a second reason as of F-R057 (§4). |

---

## 2. The identity as it now stands — measured, not modelled (F-R058)

```
dL/dt  =  flux  ×  v(d)_terminal
          │         │
          │         └─ terminal chondrocytic domain volume = v(c) cell + v(m) matrix per cell
          └─ N_lost per day; gated by cell-cycle time and proliferative-zone height
```

Derived independently by **Wilsman 1996** from two separately-measured equations; confirmed empirically by
**Breur 1997** (`R² = 0.992`, exactly these two variables plus their interaction). **Verified on Wilsman's
own data: flux × domain = 8.42× against a measured growth ratio of 8.43×.**

**The human, anchored for the first time (F-R059).** `v(c)` measured stereologically in a human distal
tibial physis at closure — **5,900 µm³** (White 2008, RHT fixation, Wilsman's lab, same method as all animal
data; n=1 and chemotherapy-exposed, so plausibly depressed). Distal tibia peak rate 5 mm/yr = 13.7 µm/day.

| plate | rate µm/day | v(c) µm³ | flux cells/mm²/day |
|---|---|---|---|
| rat proximal tibia | 396 | 14,997 | 12,830 |
| rat proximal radius (slowest) | 47 | 4,135 | 4,340 |
| **HUMAN distal tibia, peak** | **13.7** | **5,900** | **≈1,300** |

> **The human runs at ~1/3 the cell flux of the slowest rat growth plate, at a comparable cell volume.
> Poor on both factors.** Humans are tall by *lasting*, not by growing fast — low flux **is** the mechanism
> of long duration, which is Gafni's banking result read forward.
>
> **Hence: raising flux is a withdrawal; raising `v(d)` is not.** Every extra division spends the account
> "never close" depends on; every extra µm³ of domain volume converts the *same* division into more length.
> **`v(d)` is the only lever that is fast and not a withdrawal.**

**Measured headroom in terminal cell volume, all wild-type mammals:** rat proximal tibia 14,997 (**2.5×**),
rabbit distal radius 18,000 (**3.1×**), jerboa metatarsal 23,000 (**3.9×**), **bat manus 40,300 µm³
(6.8×)** — the bat carrying 1,300 µm³ cells in its own foot, a **31× range in one animal under one
endocrine environment.** At constant flux the distal tibia alone would run **10 mm/yr at 2×, 34 mm/yr at
6.8×**, against 5 mm/yr now.

**The decomposition of the natural range, fastest rat plate against slowest:**

| factor | contribution | in the stack? |
|---|---|---|
| **flux** (N_lost/day) | **3.16×** | erdafitinib, via cell-cycle time |
| ↳ cell-cycle time | 2.47× (30.9 → 76.3 h) | erdafitinib |
| ↳ proliferative-zone height | 3.19× (43 → 137 µm) | **nothing** |
| ↳ growth fraction | **saturated, 0.89–0.99** | **closed — no headroom exists** |
| **terminal domain volume** | **2.67×** (human headroom **6.8×**) | **nothing — GH a candidate** |
| ↳ cell volume `v(c)` | 3.63× | **nothing** |
| ↳ **pericellular/territorial** matrix | +61% P→H; **the capillary invasion route** | **nothing** |
| ↳ interterritorial matrix | +26% P→H; calcifying structural template | **nothing** |
| conversion efficiency per unit volume | ~2× loss, rabbit 5 → 8 wk | **nothing** |

**Both factors are of comparable size and they multiply.** This kills both extreme positions the branch has
held: *"λ is worthless"* (F-R044 — wrong, flux is the larger factor) and *"h_term is the free multiplier"*
(F-R043 onward — overstated; it is one of two, and cannot act alone).

**Retracted:** F-R057's `dL/dt = N_h · h_term / τ`. Whole-plate transit time is **not** constant — 1.56 →
3.85 days in the rat, a 2.46× range varying inversely with growth rate. Cooper's "~24 h" is a narrower,
hypertrophic-zone-only claim inherited from bat/mouse forelimb work I still do not have. The form above
needs no τ assumption.

**The four arms and which term each moves:**

| arm | term | best evidence | verdict |
|---|---|---|---|
| pool | flux, `(b−a)` | FoxA2⁺ serial transplant; dexamethasone banking (Gafni, 88% → 14% fusion) | banks |
| oestrogen | `w(E₂)` | Weise, Nilsson, aromatase-deficiency cases | removes a write-off; does not stop the count |
| Hedgehog, ligand level only | flux/amplitude | Haraguchi *Hhip1* cKO, +43% plate area → +4.5% length at 53 wk | weak |
| vascular | transit | Gerber Flt-(1-3)-IgG; Voss 2015 human paediatric widening; resveratrol | banks, reversible |

---

## 2b. The terminal step, named (F-R060)

```
serum phosphate → VEGFR2 (on the hypertrophic chondrocyte, not the endothelium)
                → Raf/MEK/ERK1/2 → caspase-9 → apoptosis → vascular invasion → junction advances
```

Sabbagh/Demay *PNAS* 2005 (low phosphate blocks the apoptosis; that expansion **is** rickets);
Yadav/Demay *iScience* 2023 (a screen for blockers of phosphate-induced ERK1/2 **identified VEGFR2**;
chondrocyte-specific VEGFR2 depletion → more hypertrophic cells, less apoptosis, impaired invasion).

**This unifies four arms previously treated as separate — oestrogen, vascular, mechanical envelope, and
transit time — and it retires "the vascular arm" as a description. Vascular invasion is downstream of a
cell-autonomous suicide signal, and the signal is phosphate.**

**And it supplies a renal route from oestrogen to closure** (Ikedo 2024): adipose aromatase → E2 → renal
NaPi2a/2c → serum phosphate → the axis above. **Nothing to do with ERα on a chondrocyte.**

**Design rule: block the death signal at VEGFR2, not by lowering phosphate.** Lowering phosphate achieves
the same plate effect and gives rickets; blocking the receptor spares the mineral.

**Human validation, and it contradicts F-R057.** Voss 2015 patient 5, pazopanib ×10 cycles: MRI-confirmed
**expansion of the hypertrophic chondrocyte layer**, fully reversible on stopping — and ***"no disruption in
longitudinal growth… gaining approximately 6 cm while on study."*** **The terminal step slowed while flux
and volume carried on.** F-R057's "VEGF blockade is a pure banking agent that costs rate" was drawn from
Gerber's ligand trap (which abolishes VEGF-A entirely); a receptor-level partial blockade behaves
differently.

---

## 2c. The counter-move inside erdafitinib (F-R061)

| via | terminal apoptosis | for us |
|---|---|---|
| FGFR3 → **ERK1/2 ↓** | suppressed | **delays closure — wanted** |
| FGF23 resistance → **phosphate ↑** → VEGFR2 → **ERK1/2 ↑** → caspase-9 | promoted | **accelerates closure — against us** |

**The same drug hits the same kinase with opposite signs.** Invisible until F-R060 named the executioner.

**They separate by ~10× in dose:**

| effect | normal rat | normal dog | ACH children |
|---|---|---|---|
| growth-plate thickening | **≥1 mg/kg** | 3 mg/kg | — |
| growth effect | — | — | **0.25 mg/kg → +3.38 cm/yr** |
| hyperphosphatemia | **10 mg/kg only** | — | **0 events at 0.25 mg/kg** |
| fracture + bone loss | — | **3 mg/kg** | — |

*"Hyperphosphatemia does not occur at the low doses of infigratinib that show activity in vivo."*
**Past the threshold you stop buying plate effect and start buying phosphate, which works against you.**
This is why F-R046's "threshold, not gradient" plateau at 0.25 mg/kg exists.

**Open decision (F-R061 §4.3):** all low-dose growth data is **infigratinib**; the stack specifies
**erdafitinib 8 mg**, an oncology dose with no growth-plate dose–response and a deliberate phosphate target
of 5.5–7.0 mg/dL. **No published mapping between the two exists and I will not guess one.** Either dose the
FGFR3 arm low with phosphate held at low-normal, or substitute infigratinib at the PROPEL 2 dose, which is
the only agent with a paediatric growth-plate dose–response behind it.

---

## 3. What is missing — ranked by how much it costs us

### 3.1 Terminal domain volume — **partly addressed after all** (corrected F-R060)

`v(d)` carries **2.67×** of the natural range and **6.8× measured human headroom**. F-R058 and F-R059 both
said nothing in the stack touches it and that **no agent raises terminal chondrocyte volume in a mammal**.
**Both were wrong, and the counter-example was the first drug in the stack:** FGFR3 inhibition produces
*"significant swelling of hypertrophic cells"* with HZ **+45%** against PZ +25%. **The volume lever is
occupied by erdafitinib.** What remains genuinely untouched:

**Cell volume `v(c)` — occupied, and now confirmed in wild-type (F-R061).** The published literature has
histology only in FGFR3 gain-of-function models (where TYRA-300's authors call the endpoint *"more similar
to a wild-type growth plate"* — normalisation). **The FDA infigratinib tox package supplies the wild-type
answer: dose-dependent growth-plate thickening in normal rats from 1 mg/kg and normal dogs at 3 mg/kg.**
Per-cell volume in wild-type is still inferred rather than measured (HZC-count-in-fixed-ROI is the ACH-model
proxy). NKCC1/NHE1/AE2 remain necessary-but-not-
sufficient; GH→Nkcc1 remains a one-study hypothesis.

**Matrix per cell `v(m)`.** **32–49% of daily elongation** — larger than cellular enlargement in slow plates
— and this branch has **never once addressed it.** Breur: matrix volume per cell is essentially
age-invariant and *"may be predetermined"*; its regulators were *"largely unknown"* as of 1997. Whether
that changed is an open question I have not yet answered.

### 3.2 And volume is what senescence and closure actually take

Across Breur's four plates from 21 to 35 days, elongation fell 12.5–39.5% and **cell volume fell 18.7–41.3%
while flux fell only 7.7–16.6% — and rose 7.4% in the proximal radius.** Kuhn gives the same dissociation
*inside one bone under identical systemic hormones*: at 12 weeks the rabbit **proximal radius is "almost
fused" at v(c) = 2,590 µm³** while the **distal radius is still growing at 290 µm/day at v(c) = 11,770 µm³**.
The two plates with no significant volume decline are exactly the two still open at 12 weeks.

> **Corrected in F-R059.** This holds *between* plates, not *within* one. In the human specimen caught
> mid-closure, cell volume was **statistically uniform across all nine regions** while bridging bone was
> **46% in one region and ~0 elsewhere**. **Closure initiates focally in a plate whose cells are all the
> same size — local volume collapse is not the local trigger.** Between-plate volume remains a valid
> correlate of remaining capacity.

**And the species split (F-R059).** In the *rat* 21→35 d, volume carried the decline and flux barely moved.
In the *human rib* birth→13.5 y, **cell size is preserved (lacunar diameter unchanged, ns) while cell number
collapses** — PZ height to 34%, HZ to 26%, matrix fraction rising 60→82.5% and 25→40%. **The human
age-related slowdown is flux-limited.** Which is exactly why volume is the compartment to push: the flux the
human is losing is the thing we must not spend.

**A second, independent senescence mechanism** (Kuhn): the **conversion efficiency per unit cell volume**
degrades with age — the 5-week rabbit slope is ~2× the 8- and 12-week slope (p < 0.01), and no
volume-to-rate relationship exists at all at 2–3 weeks. Restoring `v(c)` in an old plate buys about half
what it buys in a young one.

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

- **GH: resolved, not merely "confirm which."** The two figures sit on opposite sides of a **sign flip the
  authors state explicitly** — *"GH augments both stem cell number and activity **under physiological
  conditions** but causes stem cell depletion **under pharmacological exposure**"* (F-R032). 2 IU/day
  (≈0.067 mg/kg/wk at 70 kg) is physiological; **0.35 mg/kg/wk is ~5× higher and lands in the depleting
  range.** The low dose is not a compromise — it is the side where GH adds to the pool while still
  supplying the AKT tone erdafitinib requires.
- **Erdafitinib 8 mg** sits inside the 5–9 mg window that has not produced SCFE. Consistent.

---

## 4. Why the oestrogen side is still not built

The standing instruction, and now a third reason. §3.2 says what closure looks like mechanically — a
**local collapse of terminal cell volume**. **Until something defends `v(c)`, there is nothing for an
anti-oestrogen arm to preserve.**

---

## 5. The single next thing

**Raise terminal chondrocytic domain volume.** It is half the identity, it carries **6.8× measured headroom
in the human** against a wild-type mammalian ceiling, and — uniquely among the levers — **it buys speed
without spending the division count that closure draws on.**

**The one experiment that would settle it, and that appears never to have been done:** has anything ever
raised terminal hypertrophic chondrocyte volume **above normal in a healthy mammalian growth plate**?
Searched (F-R059 §7): only deficit-normalisation (GH in uremia, via proposed Nkcc1/Igf1) and
loss-of-function (bumetanide −35%, EIPA/DIDS −60–70%, Igf1 cKO −34% height). Three independent lines —
GH→Nkcc1, CNP→hypertrophy, IGF-1→Phase 3 — converge on the lever from different directions and **none has
been pushed past normal.** Both candidate molecules (**GH, vosoritide**) are already in or adjacent to the
stack.

**The highest-value mechanistic question:** what sets the **bat manus at 40,300 µm³ and the bat pes at
1,300 µm³ in the same animal**? Whatever it is, it is local, endocrine-independent, and has a 31× dynamic
range.

Flux is not neglected — erdafitinib works there — but flux is capped (**growth fraction already saturated
at 0.89–0.99**) and, more importantly, **spending it is the thing that closes the plate.**
