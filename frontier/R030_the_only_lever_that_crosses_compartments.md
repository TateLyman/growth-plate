# F-R030 — Every within-plate lever fails the same half of the condition

## 1. The atlas stated my target condition before I derived it, and then killed the obvious lever

`round242_prrx1_is_the_brake_not_the_throttle.yaml` — and it is ahead of F-R027 on both halves:

> "The target condition asked for was **replacement greater than or equal to loss WITHOUT losing
> output**, and a PRRX1 lever **fails the second half**."

That is F-R027's inequality, written in the atlas first, with the crucial qualifier F-R027 left
implicit: *without losing output*. And R242 then demolishes the obvious way to satisfy it:

> "hu2024 built lentiviral overexpression and RNAi lines in sika deer antler reserve mesenchyme cells…
> **as miR-140-3p rises, Prrx1 is inhibited, THE MAINTENANCE OF RM CELL SELF-RENEWAL AND PLURIPOTENCY
> IS DISRUPTED, and that is what INITIATES the rapid chondrogenic differentiation** the antler is
> famous for. hu2025… **PRRX1 OVEREXPRESSION DECREASES PROLIFERATION AND MAINTAINS THE UNDIFFERENTIATED
> STATE.**"
>
> "**the root state is actively held, and every known way of leaving it is a RELEASE rather than a
> PUSH.** Round 241 found the ligand-level brake (**self-secreted WNT and TGF-beta antagonists**); this
> is the transcription-factor-level brake sitting inside the same cell."

**So the root cell holds itself quiescent with its own autocrine Wnt and TGF-β antagonists, plus PRRX1
internally. Release any of those and it differentiates — output up, pool down. Reinforce any of them
and the pool deepens while output stops.**

---

## 2. The structural reason every within-plate lever fails, stated once

Across this branch and the atlas, the same shape has now appeared at five levels:

| lever | pool | output | fails because |
|---|---|---|---|
| **PRRX1 ↑** (R242) | ↑ | ↓ | pool preserved by stopping growth |
| **Wnt/TGF-β antagonists ↑** (R241, `hallett2021`, `leijten2012` Frzb/Dkk1) | ↑ | ↓ | same |
| **hypoxia / low pO₂** (F-R016) | ↑ (cells held resting) | ↓ | same |
| **glucocorticoid** (`nilsson2006`) | ↑ (slowed depletion) | ↓↓ | same |
| **GH, oestrogen, Hh-release, miR-140-3p** | ↓ | ↑ | output bought by draining |

> **Every lever that acts *inside* the growth plate is a single knob on one flow — the exit of a cell
> from the resting state. Turning it one way preserves the pool and stops growth; the other way buys
> growth and drains the pool. There is no setting that does both, because pool and output are the same
> cells at two moments.**

**That is the whole reason a century of work has produced percentages, and it is not a pharmacological
failure. It is a topological one.**

**Which makes the conclusion forced:** the target condition — *replacement ≥ loss without losing
output* — **cannot be satisfied by any intracartilaginous lever, and can only be satisfied by one that
crosses compartments.** Replacement has to arrive from cells that are not themselves the output.

**There is exactly one such route, and it is the one this branch has been assembling:**
**Pdgfrα⁺ inner perichondrium → Gli1⁺ long-lived chondroprogenitor → resting zone**
(`rosellodiez2025`, `mundy2026`, `karlsson2009`, `trompet2024`).

---

## 3. And this year's human paper supplies the architecture that makes it work

**Chu TL et al., *A transcriptional atlas of the pubertal human growth plate reveals two populations of
stem cells and direct effect of growth hormone*, Science Translational Medicine 2026,
doi 10.1126/scitranslmed.adw3590 (PMID 41984930)** — single-cell and spatial analysis of **early
pubertal human growth plates from growth-restricting surgery**:

> "Single-cell and spatial analyses revealed **two distinct stemlike populations in the resting zone**,
> differing in proliferative activity, molecular identity, and regulatory cues. **The root stem cells
> express multiple skeletal stem cell markers but NOT parathyroid hormone-related peptide and reside in
> a specialized microenvironment LOW IN WNT AND TGF-β growth factors.**… clonal lineage tracing
> demonstrated that these root cells, **marked by *Prrx1***, generate extensive chondrocyte clones and
> differentiate into stromal and osteoblastic lineages."
>
> "**GH directly activates JAK/STAT, TGF-β, and ERK intracellular signaling, inhibits AKT signaling, and
> stimulates cartilage growth and PROLIFERATION OF CARTILAGE STEM CELLS** and chondrocytes in the
> proliferative zone."

**Two things follow, and they matter.**

**(a) The GH paradox resolves into a tier structure.** `PMC12685065` (mouse) showed **GH depletes the
PTHrP⁺ pool by driving committed division**. Chu shows **GH directly stimulates proliferation of
cartilage stem cells in human explants**. Both can be true because **there are two tiers**: GH spends
the PTHrP⁺ working tier and pushes the Prrx1⁺/PTHrP⁻ root tier that feeds it.

**That is the mechanism for Wadlow's flat nine-year curve** (F-R029: ~5 cm/yr from 13 to 22 with no
detectable deceleration). Maximal drive on a single pool must decelerate. **Maximal drive on a
two-tier hierarchy, where the drive also pushes the upstream tier, need not** — until the root tier
itself runs down.

**(b) The hierarchy is now four deep, and each tier is a separate compartment:**

```
Pdgfrα⁺ / Prrx1⁺ INNER PERICHONDRIUM        (outside the cartilage — recruitable, demand-responsive)
        ↓  Gli1⁺, Hh-gated, CCN2-braked, heparan-sulfate-steered
ROOT stem cells  Prrx1⁺ PTHrP⁻              (low-Wnt AND low-TGF-β niche; autocrine antagonists)
        ↓
PTHrP⁺ stem cells                            (low-Wnt niche; the working tier GH spends)
        ↓
proliferative → hypertrophic → bone           (the output)
```

**Every arrow crosses a compartment boundary. Only the top arrow originates outside the cartilage —
and it is the only one whose source is not itself being spent as output.**

---

## 4. "Never close until we choose" — this part is finished, and it is a switch

Worth stating plainly because it is the one term that is fully solved and *controllable in both
directions*, in humans, with the evidence already in hand:

| direction | evidence | effect |
|---|---|---|
| **hold open** | `smith2008` — ER-α disruption | plate **could not be closed** by transdermal oestrogen raising free oestradiol **tenfold**, on top of an endogenous level already 2.4× ULN. Bone age 15 → 17.5 over 3.5 years. |
| **close on demand** | `imre2025` — aromatase deficiency | **25 µg transdermal oestradiol twice weekly → epiphyseal fusion within 6 months, at age 31** |
| **and it is graded** | `maffei2004` | 183.5 → 184.5 cm on oestradiol, then stopped |

**Receptor-level blockade holds the plate open against a 10× challenge. Ligand restoration closes it in
six months at a homeopathic dose, at 31 years old.** That is an on/off switch with both directions
demonstrated in human beings. Term A is not a research problem.

---

## 5. What is actually left

With §2 the remaining question is no longer "which molecule" but a single quantitative one:

> **Can perichondrial recruitment be driven to match or exceed the differentiation rate, in a
> postnatal animal, without losing output?**

Everything needed to ask it exists:
- the **cell** (Pdgfrα⁺ inner perichondrium — `mundy2026` localised it by two-layer Cre)
- the **throttle** (Hh; `trompet2024` — **+61% PTHrP⁺ cells from a six-day pulse**, and a local bead
  that made a normal rat's leg supranormally long with the gap widening at 6 months)
- the **brake** (CCN2)
- the **steering** (heparan sulfate — lose it and you get an osteochondroma instead of a plate)
- the **exposure rule** (transient, local, self-limiting — chronic costs height as well as safety)
- the **human tissue** (Leiden ex vivo model; Chu's growth-restriction specimens)

**And two things are genuinely unknown:**
1. **Whether recruitment can be repeated.** `trompet2024` fired one pulse. Signal gone by 3 weeks, no
   OA at 6 months, effect still widening. **Nobody has done pulse → wait → pulse**, which is the entire
   difference between a one-off gain and an unbounded one.
2. **Whether the root tier is itself refillable**, or is the true terminal reservoir. Chu identified it
   this year; nothing yet measures its depletion or its resupply.

---

## 6. Asks

**#1 — Chu TL et al., Sci Transl Med 2026, `10.1126/scitranslmed.adw3590` (PMID 41984930).**
Closed access, no PMC. **This is now the most important unread paper in the project** — it is the human
growth plate at single-cell resolution with the two-tier stem architecture and the direct GH
experiment. I want the root-cell markers, the niche factors, and the GH explant dose-response.

**#2 — its companion commentary**, *Decoding growth hormone actions on human growth plate stem cells*,
Trends Endocrinol Metab 2026, `10.1016/j.tem.2026.05.007` (PMID 42248738, PMC13245359 but OA: N).
Short, and it will summarise what the field takes the Chu result to mean.

**#3 — `trompet2024` Figure 5 source data.** Open access at `insight.jci.org/articles/view/165226` —
the figures carry the millimetres. **This is the effect size of the only intervention that has ever made
a normal mammal's bone supranormally long by expanding its stem pool**, and I still only have the text.

**#4 — anything on repeat or cyclical Hedgehog dosing in bone**, in any species. My searches return
nothing. If it genuinely does not exist, that absence is the next round's finding.

**Still standing:** the Safranin-O on `carroll2018`; Brighton thesis (UIC ILL `10027/14248`);
JBJS 1980;62A:740; Surgical Forum 1970:465–467; `stegen2019` DCA+BPTES tibia length; the lateral
thoracolumbar film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
The instrument that settles this one is a Cre driver that marks cells outside the cartilage and a ruler
on the bone, run twice. Every other instrument in this field looks inside the plate, where pool and
output are the same cells and no setting satisfies both halves of the condition.*
