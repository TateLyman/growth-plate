# Round 38 — I gated the data and it corrected me twice; and the atlas already held the answer I asked you for

## The check that should have been first

`delezoide1998` — held in this atlas — reports that in human embryo-fetal long bones **FGFR1 and FGFR2
are restricted to perichondrium and periosteum**, with only FGFR3 in growth plate chondrocytes. A growth
plate needle biopsy contains perichondrium, periosteum and marrow. **So my headline last round —
"FGFR1 is the most abundant FGFR in human growth plate" — might have been counting contaminating cells.**

Gated on COL2A1⁺ACAN⁺ (chondrocyte fraction 41.6 / 25.0 / 99.5 / 23.0 %):

| gene | **chondrocyte-gated** | non-chondrocyte |
|---|---|---|
| **FGFR1** | **49.6 / 29.5 / 36.5 / 67.1 %** | 32.5 / 21.1 / 29.6 / 36.3 % |
| **FGFR4** | **11.5 / 12.7 / 24.9 / 25.0 %** | **0.29 / 0.71 / 0.00 / 0.34 %** |
| FGFR3 | 46.6 / 22.3 / 91.7 / 70.5 % | — |
| KLB | 1.00 / 2.50 / 0.20 / 0.00 % | 0.61 / 2.14 / 0.00 / 0.34 % |

**The FGFR1 finding survives** — higher inside the gate than outside, in all four donors. `delezoide1998`
is embryo-fetal ISH; this is adolescent tissue. Both are carried.

**But the gate reversed part of my last conclusion.** **FGFR4 is essentially chondrocyte-exclusive —
35- to 80-fold enriched inside the gate.** That makes it a *more* specifically cartilage receptor than
FGFR1 or FGFR3.

So I over-called it: **"the FGFR4 case collapses" conflated a target with a mechanism.** The target is
real and better localised than I said. Only the FGF19/KLB mechanism is dead — KLB stays absent even among
chondrocytes, so FGFR4 in human cartilage must signal via **paracrine** FGFs, which need no klotho.
Logged as **CORR-042**.

## And the atlas already held the answer I asked you for

Last round I opened a gap asking **the sign of local FGFR1 inhibition**, and proposed that if FGFR1
restrains terminal differentiation, blocking it would be an h_term action.

`jacob2006`, in this bibliography as `primary_abstract_only` the entire time:

> **"Fgfr1 deletion in the osteo-chondrogenic lineage delays hypertrophic chondrocyte maturation"**

**That is the direction I predicted.** If it translates, **FGFR1 inhibition is pro-h_term, and erdafitinib
is the most potent FGFR1 inhibitor available (1.20 nM) — making its supposed main liability a third
therapeutic action.** Your instinct on erdafitinib keeps surviving contact with the data.

**Four things stand against it, and they are not small:**

1. `jacob2006` is abstract-only, the deletion is **whole osteo-chondrogenic lineage** not
   chondrocyte-restricted, and **no bone length or terminal cell height is reported.** Delayed maturation
   is not a longer bone — it could equally be a disorganised plate.
2. `wu2012`'s FGF21→FGFR1 growth-inhibition mechanism **requires β-klotho**, which I now measure as
   absent from human chondrocytes while `wu2012` finds it present in mouse. **The FGF21 route may be
   mouse-specific**, so blocking it in humans may buy nothing.
3. FGF23→FGFR1→**α-klotho** in kidney is what causes the hyperphosphatemia. **The liability is on the
   same receptor as any benefit** — inseparable pharmacologically, separable only by delivery.
4. The **plate widening** seen under erdafitinib is exactly what delayed hypertrophic maturation looks
   like — and it is also what precedes the mechanical failure. **The mechanism and the toxicity may be
   the same event.**

## A species divergence worth carrying

`wu2012`: FGF21 + FGFR1 + **β-klotho** expressed in *mouse* growth plate chondrocytes, FGF21 blocking GH
action directly at the plate. This atlas: **KLB absent from human growth plate chondrocytes, gated.**

If that holds, the entire endocrine-FGF arm (FGF19, FGF21) is **functional in mouse cartilage and closed
in human cartilage** — which would make a class of mouse growth-plate results untranslatable, and is
worth knowing independently of any drug.

## What I could not find, having searched properly

- **No chondrocyte-restricted *Fgfr1* deletion with a bone-length endpoint.** `jacob2006` is the closest
  and it is lineage-wide with no length reported.
- **No *Fgfr4* loss-of-function skeletal phenotype**, in any species.
- **No growth-plate drug concentration** for any FGFR inhibitor or CNP analogue.
- **No Hedgehog agonist in a wild-type animal with resting-zone counts** — `ctcmnp2026` is a disease
  model, `orikasa2024` is constitutive and genetic and got no length.

These four are genuine absences, not gaps in my searching. Each is one experiment.

## Tooling

`atlas/tools/fgfr_axis_expression.py` now **gates on chondrocytes by default**, with `--ungated` as the
opt-out, and prints why: an ungated number was reported here as a finding before anyone checked whether
it was contamination. It also warns that a COL2A1/ACAN gate **excludes resting-zone cells**, which have
the lowest mRNA content of any zone — so gated fractions are biased toward proliferative and hypertrophic
cells.

Validator: 643 nodes, 1247 edges, 321 gaps, 1150 refs — 0 errors, 0 warnings.
