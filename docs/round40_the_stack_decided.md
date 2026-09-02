# Round 40 — your papers decided it. Two of them were the experiments I said didn't exist.

I could fetch **5 of your 8** free: Karolak 2015 (PMC4383864), Shuhaibar 2021 (PMC8262325), Shuhaibar
2017 (PMC5745078), Krejci 2010 (PMC2898326), Gori 2009 (PMC2670346). Two of them settle the question.

## 1. Karolak 2015 — the FGFR1 experiment I twice said did not exist, and it goes against erdafitinib

Chondrocyte-restricted (Col2a1-Cre) *Fgfr1* deletion:

> Fgfr1<sup>Col2cKO</sup> mice had **reduced stature (by P4), body weight (by P9) and tibial length (P18)**
> compared with WT littermates, **despite the increased size of their hypertrophic zone**

**Local FGFR1 blockade in cartilage shortens bones.** Erdafitinib engages FGFR1 *most* potently of all
(1.20 nM, below FGFR3 at 3.00), so its net effect is **the FGFR3 benefit minus an FGFR1 cost** that a
selective agent doesn't pay.

That converts the argument for a selective agent from a dosing inconvenience into a mechanism — and it's
the only one of five consecutive erdafitinib-related corrections that rests on a **genetic experiment
with a length endpoint** rather than on inference from expression or potency.

## 2. And it corrects me on something more important than erdafitinib

`jacob2006` said Fgfr1 deletion *delays hypertrophic maturation*. I read that as an **h_term action, so
pro-growth**, and built on it for two rounds. Karolak shows the same enlarged zone **and measures the
bone: it's shorter.**

**The zone got bigger and the bone got shorter.** That's a units confusion I should have caught: growth
rate is *cells produced per unit time × terminal cell height*; **zone height is a standing stock** that
rises when clearance slows. A zone can thicken while elongation falls. This atlas had already written
that caveat onto the h_term node and then failed to apply it to the next result. Logged as **CORR-044**.

## 3. Shuhaibar 2021 — the additivity answer, and it's the productive direction

LB-100 (blocks the phosphatase that dephosphorylates NPR2) + BMN-111 (vosoritide), cultured
*Fgfr3*<sup>Y367C/+</sup> femurs:

| | growth ratio vs untreated |
|---|---|
| LB-100 alone | 1.30 |
| **LB-100 + BMN-111** | **2.06** |
| | **+16 % elongation over BMN-111 alone** |
| bone + cartilage area | 1.93 vs 1.51 — **+27 %** |
| **hypertrophic CELL area** | **+32 % over BMN-111 alone, ≈ wild-type** |

**Cell size up 32 % *and* length up 16 %, together, in one preparation.** That is the first direct support
this atlas has for the h_term thesis in the productive direction — and it sits exactly opposite Karolak:
**cell enlargement raises length; zone enlargement lowers it.** The distinction is now load-bearing, and
the thesis should only ever have been about the first.

## 4. This forces a correction to my own stacking rule — and it's a better rule

I said: **stack across terms, never within one**, based on sacubitril (not additive with CNP) and
tadalafil (raised cGMP 37–52 %, no length gain). **Both of those add cGMP.**

LB-100 does something different — it keeps **NPR2 phosphorylated so the receptor can still respond**. That
is a control point *upstream* of cGMP production, not a second source of it.

> **Corrected rule: never at the same control point.** cGMP concentration saturates once a CNP analogue is
> aboard. Receptor *responsiveness* does not.

That's more useful than the old rule, and it opens a combination the old rule would have forbidden.

## Does this decide the stack? Yes, for two of four arms.

- **Arm 1 (h_term):** CNP analogue **+ an NPR2-phosphatase inhibitor.** Additive, quantified, and it works
  by restoring receptor responsiveness rather than adding cGMP. Shuhaibar 2017 is the mechanistic bridge —
  FGF18 dephosphorylates NPR2 and that's what LB-100 opposes.
- **Arm 2 (amplification): FGFR3-selective, decisively — not erdafitinib.** FGFR1 blockade shortens bones;
  erdafitinib leads with FGFR1.
- **Arm 3 (pool):** unchanged — Hedgehog agonist candidate, unresolved conflict with `orikasa2024`.
- **Arm 4 (duration):** unchanged.

**One caution on arm 1:** LB-100 is a broad PP2A-family phosphatase inhibitor with its own oncology safety
profile, and the experiment is embryonic femur culture in an achondroplasia model where NPR2 is
*pathologically* dephosphorylated — so it corrects a deficit rather than pushing a normal plate. The
right target is the specific phosphatase, not PP2A wholesale.

## What I could not get, and what I'd still want

**Couldn't fetch (paywalled):** Cinque 2015 *Nature* (FGF18→FGFR4/autophagy — the FGFR4 counter-sign, and
still the only candidate FGFR4 loss-of-function skeletal phenotype) and Delucchi 2019 *JBMR*.

**Please send: Cinque 2015 (PMID 26595272).** It is the one paper that would settle FGFR4's sign, which is
now the last open receptor question — FGFR3 pro-growth to inhibit, FGFR1 anti-growth to inhibit, FGFR4
unknown. If FGFR4 is growth-*supportive*, then inhibiting it is a second cost, and the case for a
narrowly FGFR3-selective agent becomes complete.

Validator: 644 nodes, 1248 edges, 321 gaps, 1154 refs — 0 errors, 0 warnings.
