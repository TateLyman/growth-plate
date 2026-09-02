# Round 37 — all four checks run, and the first one kills my own argument

## 1. β-klotho in growth plate — **the FGFR4 case collapses**

I flagged this as the cheapest check that could kill the FGFR4 argument, and asked you for it. Then I
ran it myself against data the atlas already held — GSE288028, four fresh human growth plate biopsies:

| gene | donor1 | donor2 | donor3 | donor4 | ≥1% |
|---|---|---|---|---|---|
| **KLB** (β-klotho, obligate co-receptor) | 0.77 | 2.23 | 0.20 | 0.26 | **1/4** |
| **FGF19** (ligand) | 0.00 | 0.01 | 0.00 | 0.00 | **0/4** |
| FGFR4 | 4.97 | 3.71 | 24.78 | 6.01 | 4/4 |
| *COL2A1 (control)* | 88 | 91 | 100 | 52 | 4/4 |

**The ligand is absent and the obligate co-receptor is essentially absent.** FGF19 is an *endocrine* FGF
made in the ileum, so the route is closed from both ends — circulating FGF19 cannot signal without KLB in
the target tissue. **The mechanism I imported last round is not operating in a human growth plate.**

**What survives:** FGFR4 *is* expressed in all four donors, reaching 24.78 % in donor3 — the most
hypertrophic-rich sample — so it sits in hypertrophic chondrocytes and could signal through **paracrine**
FGFs, which don't need KLB (FGF2 is present 4/4). That's a weaker and different claim than the one I made.
No FGFR4 loss-of-function skeletal phenotype exists to settle it; I searched and found none.

Logged as **CORR-041**, with the pattern named: CORR-040 and CORR-041 are **the same defect twice, in
opposite directions** — reasoning about a tissue from a pathway's general biology instead of measuring the
tissue, when the measurement was one command away against data already on disk.

## 2. The same check produced something I had assumed away

**FGFR1 is the most widely detected FGFR in human growth plate — 23–43 % of cells, 4/4 — above FGFR3 in
three of four donors.**

Every argument I've made for or against a pan-FGFR agent treated FGFR1 blockade as a purely *systemic*
liability via FGF23/phosphate. **It is also a local action on the target tissue, and the atlas holds no
direction for it.** New gap `g_l3_local_fgfr1_sign_in_growth_plate`.

The reason this matters more than a caveat: FGFR1 is reported in **hypertrophic** chondrocytes while
FGFR3 sits proliferative. **If FGFR1 restrains terminal differentiation, blocking it would enlarge or
prolong the terminal cell — moving FGFR1 from the liability column into the h_term column** and inverting
the whole assessment of pan-FGFR agents. That is testable and nobody has done it.

## 3. Drug penetration — confirmed as a real barrier, stated by the field

`ctcmnp2026`, verbatim: the **avascular and alymphatic** nature of growth plate cartilage **"severely
limits drug delivery and accumulation."** So the question I raised is a recognised problem, not a
hypothetical, and no growth-plate concentration has been measured for any of these drugs.

## 4. **The recruiter may exist — and it also solves delivery**

Same paper. **CT-CM-NPs** — nanoparticles coated with primary chondrocyte membranes plus the collagen-II
binding peptide **WYRGRL** — delivered the **Hedgehog agonist purmorphamine** to growth plate cartilage
in vivo, restored ciliogenesis, and **increased bone and body length**.

**Why this is the recruiter candidate:** `qu2025`'s reservoir is **GLI1+**, and GLI1 is the Hedgehog
transcriptional effector. Purmorphamine is a Smoothened agonist. And the human check supports translation
— **GLI1 3.0–8.1 %, PTCH1 11–84 %, PDGFRA 12–41 %, all 4/4 donors.** The pathway *and* the reservoir
markers are present in human tissue, not a mouse construct.

**The conflict, unresolved and recorded.** `orikasa2024` deleted *Ptch1* in PTHrP+ resting chondrocytes —
constitutive Hedgehog activation in exactly that compartment — and got hyperplasia with **no significant
bone length change**, plus descendants converting to trabecular osteoblasts. Constitutive genetic
activation in resting cells did *not* lengthen bone; transient pharmacological activation delivered to
whole cartilage did. The reconciling variables — transient vs constitutive, whole-plate vs
PTHrP-restricted, disease model vs wild-type — are exactly what nobody has separated.

Also: this is a **disease model** where Hedgehog and ciliogenesis are impaired at baseline. Restoring a
deficit is not pushing a normal plate above normal. And no resting-zone counts were made, so whether the
length came from recruiting the reservoir is not established.

## Where this leaves the stack

- **Arm 2 (amplification):** the FGFR4 bonus is withdrawn. Erdafitinib's advantage narrows to FGFR3
  potency plus the phosphate-titration biomarker. **The local FGFR1 sign is now the open question that
  decides pan- vs selective.**
- **Arm 3 (pool):** upgraded from "no recruiter exists" to **"a candidate exists, with a delivery vehicle,
  and a direct contradiction in the atlas."**
- **Delivery:** the barrier is real and named; a targeting chemistry now exists that could carry a CNP
  analogue as readily as a Hedgehog agonist.

## What would settle the two live questions

1. **Chondrocyte-specific Fgfr1 deletion**, postnatally induced — long bone length, zone heights, and
   **terminal hypertrophic cell height**. Or the cheaper version: FGFR3-selective vs pan-FGFR at matched
   FGFR3 occupancy in one wild-type strain; any difference in terminal cell height isolates FGFR1+FGFR4.
2. **A Hedgehog agonist in a WILD-TYPE animal** with resting-zone cell counts, to separate
   deficit-correction from reservoir recruitment.

Validator: 643 nodes, 1247 edges, 321 gaps, 1150 refs — 0 errors, 0 warnings.
