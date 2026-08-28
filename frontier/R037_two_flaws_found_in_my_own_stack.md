# F-R037 — I checked the three "does not exist" claims. Two of my own load-bearing claims broke instead.

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** The three unknowns are confirmed genuinely unmeasured. But hunting them found **two flaws in
my own stack**, one of which is in the single experiment the whole "raise N" architecture rests on.

---

## 0. Why this round exists

Tate's instruction was not to accept my own "these experiments don't exist" and to find every flaw before
the stack is built on. Both halves paid off, and the second half paid more.

---

## 1. FLAW ONE — "hypoxia is the `a − b` lever" is a pool-without-flux trap

F-R034 §7 proposed tissue pO₂ as a renewal lever, on the strength of `leijten2012`: hypoxia expands the
resting zone and induces GREM1/FRZB/DKK1, the same antagonist set that defines the human root niche.
**Four independent lines say an expanded resting zone is not the same as more growth, and can be its
opposite.**

**(a) Leijten's own length endpoint.** In the same experiment, hypoxia expanded the resting zone **and
produced a SHORTER tibia.** I quoted the zone result and let the length result sit in a table. An
expanded reserve with reduced output is a **traffic jam**, not a charged battery.

**(b) `Kobayashi et al. 2023`** (PMC9882305) — fetched in full this round, and it is worse for me than
the abstract suggested. **Four independent genetic routes all produce the same thing:**

| perturbation | resting zone | bone |
|---|---|---|
| **miR-140-5p gain-of-function** (the mouse model of human **SEDN**, a spondyloepiphyseal dysplasia) | *"expansion of the resting zone… and an **increase in resting chondrocytes**"* | short |
| **Ldha cKO** (± Ldhb) | expanded | *"significant growth defects"*, **reduced number AND size of hypertrophic chondrocytes** |
| **Acly cKO** | expanded | same phenotype, *"without inducing energy deficiency"* |
| **Fgfr3 activating mutation** | *"causes an expansion of resting zone chondrocytes"* | **achondroplasia — short-limb dwarfism** |

All four converge on **FGFR3 upregulation**, via reduced acetyl-CoA → reduced histone acetylation. And
the miR-140 mutant reaches it through **reduced Hif1a** — the *opposite* direction from the hypoxia story
I was telling.

> **An increased number of resting-zone chondrocytes is a signature of skeletal dysplasia, not of tall
> stature.** SEDN, achondroplasia, LDH-deficiency and Acly-deficiency all have **more resting cells and
> shorter bones**.

**(c) `horike2026`, already in the atlas.** The FGFR3-achondroplasia knock-in shows an **expanded resting
zone from disrupted turnover and impaired stem-cell-like behaviour, with cells accumulating in the
resting zone instead of entering columns** — expanded RZ, short bones.

**(d) The human experiment, which I had not looked for.** High-altitude child growth: *"independent of
ethnicity or caloric status, absolute and relative **tibia length was significantly reduced in children
with lower blood oxygen saturation**"*, with the consensus that most of the altitude stature deficit is
socioeconomic but **~1–2 cm of adult stature is attributable to hypoxia itself**. Chronic systemic
hypoxia in humans **costs** height, and it costs it specifically in the tibia.

**And the sign flips back the other way when you look at delivery rather than tension.** Serrat: local
warming lengthens the treated limb; exercise lengthens limbs locally. Brighton: an A-V fistula
(hyperperfusion) lengthened 100% of puppies. Altitude: less oxygen delivery, shorter tibia. **All four
say the same thing — more delivery, longer limb — and none of them says low tissue pO₂ is good.**

> **Verdict: hypoxia is demoted from "the `a − b` lever" to a pool-without-flux trap** — the same failure
> mode the atlas already catalogued for PRRX1 (*"replacement ≥ loss WITHOUT losing output, and a PRRX1
> lever fails the second half"*) and for mTORC1 (*"pool without flux"*). F-R034 §7 is withdrawn as a
> lever and retained only as a description of how pO₂ shifts the reserve/hypertrophy balance.

One thing survives and should not be lost: the **GREM1/FRZB/DKK1/SFRP5 convergence** across `leijten2012`,
`chu2026`, `trompet2024` and atlas R241 is still four independent lines describing the same niche state.
What is withdrawn is hypoxia as the way to *reach* it.

**A calibration note.** The 2025 review of growth-plate skeletal stem cells and their niche
(PMC12525321, 67k characters) contains **zero occurrences of "oxygen" or "hypoxia."** So the oxygen→stem
link is not contradicted by the stem-cell field — it is **absent from it**. Unexamined, not refuted; but
after (a)–(d), the burden of proof has moved.

---

## 2. FLAW TWO — and it is in the load-bearing experiment

Everything in my "fast must be bought in N" architecture rests on `trompet2024` being the demonstration
that **expanding the stem pool produces length**. The 2025 review calls it exactly that: *"the first
direct evidence that increasing the number of gpSSCs translates into enhanced linear bone growth in
vivo."* **Read against the paper's own text, it does not establish that.**

From the primary, verbatim:

> *"**neither the number nor proliferative activity of cells expressing CD73 was affected by treatment
> with SAG at both time points tested**… the number of Tomato⁺CD73⁺ cells was elevated by treatment on
> P10–P16 and **tended to be suppressed on P30–P36**."*
> *"The CD73⁺ and Tomato⁺ populations of cells did not overlap entirely… with an **overlap of 40%–50%**
> in control bones, suggesting that the PTHrP⁺ and CD73⁺ cell populations may not be identical."*
> *"a large proportion (**28.2% ± 6.8%**, n = 7) of mCherry⁺ cells were CD73⁻."*

**So the famous +61% is marker-specific.** A second, 40–50%-overlapping stem marker shows **no change**,
and **trends downward in P30–P36 — the exact post-SOC window where the length effect is obtained.** This
is the atlas's denominator problem (*"every yield in this programme is computed against a marker rather
than a cell type"*) landing on the one experiment I built on.

**Three more of the paper's own negatives, which I had not carried:**

> *"proliferation in the **columnar zone of flat chondrocytes was not affected** by SAG treatment at
> either age."* → **no amplification (A) increase.**
> *"the **orientation of stem cell division (dyads)… is not affected** by Hh signaling, suggesting that
> Hh pathway stimulates **both symmetric and asymmetric division**."* → no shift toward renewal.
> *"only [population asymmetry] increases the number of stem cells. **Although the mode of epSSC renewal
> remains to be elucidated**…"* → the authors decline to claim the pool grew.

**And the mechanism they do offer for the length gain is not pool at all.** On the bead experiment, the
growth increase was *"**probably due to an elevation in the height of the terminal hypertrophic
chondrocytes**."*

> **`trompet2024` solidly demonstrates that a local Hedgehog pulse lengthens a bone against a
> contralateral control, out to six months. It does not demonstrate that it does so by expanding the stem
> pool — and its authors attribute the length gain to terminal hypertrophic cell height (h_term).**

That reverses the polarity of the whole edifice. My F-R032/F-R033 argument was that **fast must be bought
in N, not λ**, because the conjugacy identity prices λ and not N. **There is now no experiment showing
that buying it in N works.** The one candidate lengthens bone by a term that sits *outside* the pool
equation entirely.

---

## 3. The three unknowns: confirmed unmeasured

Searched properly, not asserted:

1. **Does raising `a − b` preserve stem NUMBER in a postnatal plate with intact influx?** No such study.
   The nearest are Vhl-deletion (HIF stabilisation) work — *"significantly reduced chondrocyte
   proliferation rate, increased extracellular matrix, and presence of atypical large cells within the
   resting zone"* — which is embryonic, reports no stem-cell counts, and points the wrong way anyway.
   **Still open, and now more important, because it is the measurement that would distinguish a charged
   pool from a traffic jam.**
2. **Does a Hedgehog-expanded pool persist past one week?** **No.** Trompet counted Pthlh⁺ at one week
   (a *tendency*, `#`) and the +61% at two days post-dose in a separate systemic experiment. Nothing later.
3. **Does a second pulse add a second increment?** **No such experiment exists**, in any species, for any
   pool-expanding agent.

**And the review confirms the field agrees on the scarcity:** across every marker-defined population —
PTHrP, CD73, Axin2, FoxA2, ApoE — Trompet is named as the *only* intervention linking pool number to
bone length.

---

## 4. What the round adds that is positive

**(a) The resting zone is a laterally shared resource, not a per-column stack.** *"Individual clones in
the resting zone **expand radially, feeding into multiple proliferative columns**."* This refines
F-R033 §0: `N` per column is drawn from a lateral neighbourhood, so the pool is larger than a strict
vertical stack — without reviving the plate-area error, since elongation rate is still per-column
production × h_term.

**(b) The niche has a birthday.** CD73 appears *de novo* in the resting zone at **P28**, and the clonal
mode switches at **~P30** from short polyclonal columns to long monoclonal ones. **The stem niche is
established after SOC formation** — which is why Trompet's window works and why early dosing does not.

**(c) A tension worth recording.** PTHrP⁺ cells are described as maintained in a **Wnt-inhibitory**
niche, while **Axin2⁺** cells require β-catenin — *"loss of β-catenin resulted in impaired expansion of
these cells."* Two resting-zone populations with **opposite Wnt requirements**. Any Wnt-directed lever
will help one and harm the other, and nobody has reconciled them.

---

## 5. Where the goal actually stands, with the flaws removed

| term | status |
|---|---|
| **never close** | **solid.** Human, both directions, receptor-level durable |
| **unlimited** | **no demonstrated lever.** Every candidate that expands the pool does so by blocking exit — hypoxia, LDH ablation, FGFR3, PRRX1, mTORC1 — and all produce short bones or no length gain. Hedgehog lengthens but is not shown to expand the pool |
| **fast** | **three levers that demonstrably lengthen bone**: Hedgehog beads (mechanism uncertain, authors say h_term), local heat/exercise (delivery; window-limited; one human negative), GH (spends the pool). **None is established as pool-expanding** |

**And the discriminator is exactly the identity.** Longshanks LS2 also had an expanded resting zone
(**+56%**) — and got **longer** bones, because its **proliferative zone expanded +37% and cells per column
+32% at the same time**. The dysplasias expand the reserve while output falls; Longshanks expanded the
reserve while output rose. `chu2026`'s fig. S2L fits: human tall-stature and normal-height children
**both** show a *"prominently enlarged resting zone"*, so reserve size alone does not separate them.
**Pool size is not the variable. Pool size with maintained discharge is.**

**The central gap, stated more sharply than before:**

> **There is no demonstrated intervention, in any species, that increases the growth-plate stem pool while
> maintaining output.** Every agent that raises the pool does it by blocking the exit; every agent that
> raises output does it by spending the pool. The conjugacy identity says these are the same event seen
> from two sides — and the empirical record now contains no counterexample.

That is not a reason to stop. It is the precise statement of what has to be broken, and it is a
*sharper* target than "find a stronger accelerator." But I am not going to name agents against an
architecture whose keystone experiment I have just had to downgrade.

---

## 6. What would settle it — and what I would ask for

**The one measurement that decides everything above** is the same in all three unknowns, and it is a
single experiment: **give a pool-expanding stimulus to a postnatal plate with an intact niche, then count
stem cells by TWO independent markers at 1 week, 1 month and 6 months, alongside a length endpoint and a
column-output endpoint.** Trompet did four of those five things, at one time point, with one marker.

**Papers I would still like, in order:**

1. **`trompet2024` Supplemental Figures 2 and 5** — the CD73 panels (2B–2J), the division-orientation
   panel (2M), and **5E/5F**, the terminal hypertrophic cell height data on which the authors' own
   explanation of the length gain rests. The main text is open; I have not seen the supplement, and §2
   turns entirely on it.
2. **`horike2026`** — still unread here. It is the cleanest published case of *expanded resting zone
   with short bones*, and it names CREB plus a rescue compound (666-15). It is the control case for
   flaw one.
3. **~~`Kobayashi 2023` full text~~ — fetched this round.** Nothing further needed.
4. **Bailey 2007, *"Tradeoffs between oxygen and energy in tibial growth at high altitude"*** (*Am J Hum
   Biol*) — the human hypoxia-versus-tibia-length primary behind §1(d). Likely paywalled.

**Corrections carried:** F-R034 §7 withdrawn as a lever. F-R032 §3, F-R033 and F-R036's reliance on
`trompet2024` as a pool→length demonstration is downgraded to "lengthens by an unestablished mechanism."
The GREM1/FRZB/DKK1/SFRP5 niche convergence stands; hypoxia as the route to it does not.
