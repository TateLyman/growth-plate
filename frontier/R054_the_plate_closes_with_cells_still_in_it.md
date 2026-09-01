# F-R054 — Systemic Hedgehog does nothing, local Hedgehog works, and the plate closes with capable cells still in it

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** Figure 4H answers my own Tier 1 question and the answer is negative. **But I asked the wrong
question, and `trompet2024` — which has been in this branch since F-R038 — already answered the right
one.** Reconciling the two gives Hedgehog a fifth counter-move and a clear design rule. **And Kindblom
2002 supplies the missing human measurement that turns this from "the plate runs out" into something
different and more tractable.**

---

## 0. A correction I owe before anything else

F-R053 asked, as Tier 1 item 2: *"Any experiment giving a Smoothened agonist to a wild-type mammal and
measuring bone length, at any dose, any duration."*

**`trompet2024` is that experiment. It has been in this branch since F-R038, I have its supplement, and I
have cited its numbers in four separate rounds.** Asking for it was not a gap in the literature; it was a
gap in my own bookkeeping. **The synthesis in §2 is the one I should have written last round.**

---

## 1. Figure 4H — systemic SAG does nothing to a normal animal

The panel resolves it cleanly. In **Figure 4H (body length at P30)** and **4I (body weight at P30)**, the
comparison **Ihh^fl/fl versus SAG+Ihh^fl/fl is marked NS.** The wild-type and wild-type-plus-SAG curves in
panel F run together across P7 → 4 weeks; every ### significance marker sits between the Ihh-cko groups.

| comparison | result |
|---|---|
| Ihh^cko vs Ihh^fl/fl | *** P < 0.0001 (dysplastic) |
| SAG + Ihh^cko vs Ihh^cko | *** P < 0.0001 (rescued) |
| SAG + Ihh^cko vs Ihh^fl/fl | **NS — full rescue to normal** |
| **SAG + Ihh^fl/fl vs Ihh^fl/fl** | **NS — no effect on a normal animal** |

> ### Systemic SAG at 20 mg/g every other day for three weeks made Ihh-deficient mice normal and made normal mice nothing. That is the restoration-versus-elevation trap, and Hedgehog falls into it exactly as CREB inhibition did (666-15: no effect on weight, femur length or CD73 in control mice).

**F-R053 §4a upgraded the Hedgehog arm on this paper. That upgrade is withdrawn for the systemic route.**

---

## 2. But the local route is positive in wild-type — and the two together give the design rule

**`trompet2024` (Trompet D et al., *"Stimulation of skeletal stem cells in the growth plate promotes
linear bone growth"*, JCI Insight, 165226):** SAG-loaded beads implanted locally into **rat femurs**,
**contralateral limb as internal control**, in **normal animals**:

- **sustained increase in femoral *and* tibial length on the treated side**
- durable to **six months**
- **OARSI joint score at 6 months: ns — no joint damage**
- PTHrP-mCherry⁺ cells **+61%**

| route | animal | result |
|---|---|---|
| **systemic SAG, 20 mg/g q2d × 3 wk** | **wild-type mouse** | **NS (Fig 4H)** |
| **local SAG bead** | **wild-type rat** | **durable femoral and tibial length gain, 6 months, contralateral-controlled** |

> ### Local Hedgehog agonism elevates growth in a normal animal. Systemic Hedgehog agonism does not. That is not a contradiction — it is the design rule, and there is a mechanism for it.

### Why systemic fails: Hedgehog carries its own brake, and it is transcriptional

**PTCH1, PTCH2 and HHIP1 are all Hedgehog target genes and all are negative regulators of the pathway.**
Activating Hh *transcriptionally induces its own antagonists* — *"the Hedgehog pathway initiates a
negative-feedback mechanism that includes downregulation of Gas1, Cdon and Boc, and **upregulation of
Ptch1, Ptch2 and Hhip1**."* PTCH1 acts catalytically on SMO, so **more PTCH1 means more inhibition of the
very receptor SAG is agonising.**

Sustained systemic exposure therefore drives the brake up alongside the accelerator. A bead delivering a
high local concentration into an avascular tissue, or a transient pulse, can outrun it.

> **This is the fifth instance of F-R052's pattern. Block aromatase → receptors and STS rise. Block the
> sulfatase → substrate accumulates. Block the receptor → ERβ rises. Now: *activate* Hedgehog → PTCH1,
> PTCH2 and HHIP1 rise. Every node in this system has a counter-move, and the counter-move is
> transcriptional in every case.**

**And the design rule that follows is the one the nanoparticle paper is built for:** F-R053 §4b's
CT-CM-NPs — PLGA loaded with **purmorphamine**, chondrocyte-membrane-coated, **WYRGRL**-targeted, given
**intravenously** — is precisely a systemic route that produces a *local* exposure. **The delivery platform
is not a convenience. On this evidence it is the difference between the arm working and not working.**

---

## 3. Kindblom 2002 — the shutdown signal, measured in humans

**Kindblom JM, Nilsson O, Hurme T, Ohlsson C, Sävendahl L, J Endocrinol 2002;174(2):R1–R6.** Human growth
plate biopsies from epiphyseal surgery, across pubertal stages, immunohistochemistry:

> **Ihh and PTHrP are expressed mainly in early hypertrophic chondrocytes, and the levels of expression of
> both are HIGHER in early puberty than later.**

**The maintenance loop declines through human puberty.** Set against the rest:

| finding | source |
|---|---|
| **Ihh and PTHrP decline through human puberty** | **Kindblom 2002 — human tissue** |
| periosteal stem cells maintain resting-zone stem cells **via Ihh**; PSC-specific *Ihh* deletion impairs RZSC maintenance | Nat Commun 2022 |
| post-SOC Hedgehog antagonism (vismodegib) reduces clone size and causes **premature fusion** | Chagin group |
| local Hedgehog agonism in a normal animal gives durable length gain | `trompet2024` |

> **The signal that maintains the resting-zone stem cells is measured, in human tissue, to fall during
> exactly the window in which the plate closes.**

---

## 4. The reframe — and it changes what the problem is

Three findings that only make sense together:

1. **Weise:** fusion is triggered when the proliferation rate approaches zero. Fusion is abrupt — plates
   are *"either completely fused… or completely unfused."*
2. **Chu 2026, human:** *"a notable feature of human pubertal growth plates is the **large RZ, which
   comprises nearly half of the structure**. This challenges the long-standing hypothesis that growth
   ceases because of the exhaustion of chondroprogenitors."*
3. **Nilsson 2005:** resting-zone chondrocytes from fetal, 4-week and 16-week rabbits underwent
   **13.1 / 14.6 / 14.3 population doublings, P = 0.36** — *"previous proliferation in vivo had no effect
   on subsequent proliferation in vitro"* — and maintenance methylases were **upregulated** on removal
   from the tissue.

> ### The plate closes with cells still in it that are still capable of dividing and have stopped dividing. That is a regulatory shutdown, not a resource exhaustion — and a regulatory shutdown is in principle reversible.

**This is the single most consequential reframe in the programme**, because "add more cells" and "restart
the cells that are there" are different problems with different solutions, and the second is far more
tractable.

**The qualification it needs, and I am not going to skip it.** Nilsson/Schrier 2006 measured **resting-zone
chondrocytes per mm of growth plate and found a significant decline with age (P < 0.001** in the overall,
epiphyseal and reserve resting zones). **So the resting zone becomes thick but sparse: half the plate by
height, fewer cells per unit area.** Depletion is real. What Chu and Nilsson 2005 establish is that
depletion is **not complete** at the moment of closure and that the survivors are **not damaged**.

> **So it is both. Cells are lost, and the survivors are switched off. Weise's "proliferation reaches
> zero" is the second one, not the first.**

---

## 5. How infinite growth would work, stated as a chain with its primary attached

| # | link | evidence | status |
|---|---|---|---|
| 1 | Fusion is triggered by proliferative arrest, not by ossification | Weise 2001 | **established** |
| 2 | Senescence counts replications, not time | Gafni 2001 | **established** |
| 3 | Suppressing replication banks capacity and delays fusion **88% → 14%** | Gafni 2001 | **established** |
| 4 | Oestrogen accelerates the count, irreversibly and non-apoptotically | Nilsson 2014, Weise 2001 | **established** |
| 5 | At closure, the resting zone is still half the plate and its cells retain full replicative capacity | Chu 2026, Nilsson 2005 | **established** |
| 6 | The maintenance signal (Ihh/PTHrP) **declines through human puberty** | **Kindblom 2002** | **established** |
| 7 | Restoring that signal **locally** elevates growth in a normal animal | `trompet2024` | **established** |
| 8 | Restoring it **systemically** does not, because Hh induces PTCH1/PTCH2/HHIP1 | **Li 2021 Fig 4H** + feedback literature | **established** |
| 9 | A systemic route producing local exposure exists | CT-CM-NPs (WYRGRL, chondrocyte-membrane-coated, IV) | **demonstrated in a dysplasia model** |
| 10 | A long-term stem tier exists that self-renews through three serial transplants and rebuilds the plate at no cost to growth | FoxA2, Nat Commun 2022 | **established** |
| 11 | **Does maintaining the signal indefinitely prevent arrest, or only postpone it?** | — | **UNRESOLVED** |

**The answer to "how do we grow infinitely", as far as the evidence supports it:**

> **Remove the accelerator (oestrogen, links 3–4), spend the count slowly (link 3), take output from the
> free multipliers rather than from λ, and sustain the maintenance signal locally in the plate (links 6–9)
> so the cells that are still there — and they are still there, and still capable — do not switch off.**

**Every link but one has a primary behind it. Link 11 is the whole remaining question, and it is now much
sharper than "does the pool run out": it is whether Ihh/PTHrP restoration can hold proliferation above
zero indefinitely, or whether something downstream arrests anyway.**

---

## 6. Every flaw in the above

1. **`trompet2024`'s own mechanism panel is weak.** Its only significant mechanistic signals were plate
   height and terminal hypertrophic cell height **at one month, both back to ns at two months**, with
   Ki67 in the proliferative zone never moving and CD73 measured at **power 0.1648 and 0.3323**. The
   length gain is durable and real; the "stem cell stimulation" mechanism is not well demonstrated **in
   its own data.**
2. **Kindblom is descriptive.** Ihh and PTHrP fall during puberty. Nobody has restored them in a human and
   measured growth.
3. **Weise's vehicle rabbits still fused at the distal tibia with E2 below 5 pg/ml.** If the oestrogen-
   independent trigger is the Ihh decline, links 6–9 address it. **If it is something else, nothing in
   this chain addresses it, and I cannot presently tell which.**
4. **One bead in one femur is not the same problem as every plate in the body simultaneously and for
   years.** The nanoparticle platform is the proposed answer and it has been run once, in a dysplasia
   model, as a short study.
5. **Chronic Hedgehog activation is oncogenic** — medulloblastoma and basal cell carcinoma are Hh-driven,
   and Li 2021 additionally reports intestinal smooth-muscle thickening with *"the possibility of bowel
   obstruction."* Stated as a fact about chronic dosing feasibility, not as a risk opinion.
6. **The resting zone does deplete** (Nilsson 2006, P < 0.001). §4's reframe softens the exhaustion model;
   it does not abolish it.
7. **No agent in this chain has ever been given to a human for this purpose**, and the two that carry the
   Hedgehog arm — SAG and purmorphamine — are research reagents with no human exposure at all.

---

## 7. What I need — every item aimed at link 11

**Tier 1:**

1. **Kindblom JM et al., J Endocrinol 2002;174(2):R1–R6** in full. I have only the summary. **I need the
   quantification of the Ihh and PTHrP decline by Tanner stage** — if the fall is steep and late, it is
   the shutdown signal; if it is gradual from early childhood, it is a correlate. **This is the human
   measurement link 6 rests on and I have it second-hand.**

2. **Any experiment maintaining Hedgehog activation in a growth plate for longer than the ~6 months of
   `trompet2024`**, at any dose, by any route, with plate patency as an endpoint. **Link 11 in one
   sentence: does sustained Hh keep a plate open, or does the plate arrest anyway?**

3. **Ye S-H et al. (CT-CM-NPs, growth-plate-targeting nanoparticles) — the biodistribution and efficacy
   figures.** Specifically: growth-plate accumulation versus untargeted particles, absolute body-length
   gain, dosing interval, and duration. I have the methods in full and none of the effect sizes.

4. **Anything measuring PTCH1, PTCH2 or HHIP1 induction in growth-plate cartilage under sustained
   Smoothened agonism.** §2's explanation for the systemic null is inferred from developmental-biology
   feedback literature, **not measured in a growth plate.** If the brake is not induced there, my
   explanation is wrong and the systemic null needs a different one.

**Tier 2:**

5. **Any long-term complete oestrogen ablation in a species whose plates fuse**, followed to maturity —
   unchanged from F-R053, and flaw 3 makes it more important, not less.
6. **The longest untreated follow-up of a human with aromatase deficiency or ER resistance.**
7. **Whether repeated physeal micro-injury produces sustained FoxA2⁺ expansion** rather than the
   single-injury 7-day course.
