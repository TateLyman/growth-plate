# Round 42 — you were right; the ledger was weighted wrong, and I overruled a measurement with a prediction

You said it doesn't line up with the evidence. It doesn't, and the error is structural and mine.

## What I did wrong

**1. I weighted three receptors as equals while holding a magnitude for none of them.**

| lesion | adult human stature effect |
|---|---|
| **FGFR3 gain** (achondroplasia) | **≈ −45 to −50 cm** |
| **FGFR3 partial loss** (CATSHL) | **≈ +20 cm (+2.8 SD)** |
| FGFR1 chondrocyte deletion | mouse only; "reduced tibial length", **no magnitude** |
| FGFR4 germline null | mouse only; **no bone length reported at all** |

**FGFR3 spans ~65 cm of adult human height between its two directions. Neither FGFR1 nor FGFR4 has any
reported human stature phenotype.** FGFR3 isn't one of three brakes — **it is the brake.** A pan-inhibitor's
net is dominated by FGFR3 relief, which is exactly what the child showed.

**2. The ledger came from germline and developmental deletions and I applied it to postnatal partial
pharmacology.** `karolak2015` is Col2a1-Cre from embryonic cartilage; `cinque2015` is germline. Both ask
*"is this receptor required to **build** a growth plate?"* Erdafitinib asks *"what if I partially inhibit
in an already-built adolescent plate?"* **Different questions.**

**3. And the deepest one: a mechanistic ledger contradicted a direct human measurement, and I sided with
the ledger.** The net effect *was measured* — 19.06 cm/yr, with "accelerated growth" added to the US label
off a five-case series. **When a ledger assembled from three mouse knockouts disagrees with an observed
outcome, the ledger is what's wrong.** Logged as CORR-046.

## So what *is* unique to erdafitinib? Probably not selectivity — **exposure**

| | dose | velocity |
|---|---|---|
| infigratinib (achondroplasia) | **0.25 mg/kg/day** (~5 mg for a 20 kg child) vs 125 mg oncology | +1.74 cm/yr |
| erdafitinib (the children) | **full oncology dosing**, titrated up against phosphate | **19.06 cm/yr** |

**An elevenfold velocity gap across the same axis** — and the selective agents are dosed roughly an order
of magnitude below their own oncology exposures, for safety in a disease population.

**If that's the explanation, the 19 cm/yr is evidence about the dose-response of FGFR3 blockade, not about
erdafitinib.** And the implication runs opposite to the drug choice: **the selective agents' +1.74 cm/yr
is a floor set by regulatory caution, not a ceiling set by biology.**

A second candidate I could **not** verify: a long terminal half-life giving *continuous* rather than
intermittent FGFR3 coverage. If FGFR3 restraint recovers between doses, continuous blockade could differ
qualitatively. **I could not confirm the half-life from any source I retrieved — recorded as unverified,
not asserted.**

## What still stands, and what it now rests on

- **CORR-043 stands.** The IC50 ordering is arithmetic: FGFR1 (1.20) engages before FGFR3 (3.00), so
  phosphate is the entry ticket, not a guardrail.
- **The safety record stands.** Five of five paediatric cases permanently discontinued, three surgical.
- **But the reason to prefer a selective agent has changed** — from *"its net mechanism is unfavourable"*
  to *"it carries two receptors with no upside and an unquantified downside, at a molecule you can't dose
  down without losing FGFR3 first."* **Safety and margin, not net mechanism.**

## The question this actually opens — and it's better than the one I was answering

New gap `g_l12_fgfr3_blockade_dose_response`, tractability 5:

> **Is +1.74 cm/yr a biological ceiling or a regulatory floor?**

**The pivotal unknown, and it decides the whole arm:** the five erdafitinib toxicities cannot be
attributed between FGFR3 blockade *itself* and the FGFR1/FGFR4 blockade that came with it. **If the
slipped epiphyses and kyphoscoliosis track the *growth* rather than the off-target receptors, then dose
escalation of a selective agent buys nothing in safety — and the ceiling on this entire arm is mechanical,
not pharmacological.**

**The experiment is cheap and needs no new molecule:** an FGFR3-selective agent in **wild-type** growing
mice, dose range from achondroplasia-equivalent up to maximum tolerated, measuring bone length, physeal
thickness, terminal hypertrophic cell height, **and the mechanical integrity of the capital femoral physis
and vertebral bodies together.**

- Growth keeps rising while physeal mechanics hold → **the selective agents are badly under-dosed and the
  FGFR arm has a large unexploited range.**
- Physeal failure appears at whatever dose produces large growth, regardless of selectivity → **the
  toxicity is the growth, the erdafitinib cases weren't off-target, and this arm has a mechanical
  ceiling.**

Either answer is decisive.

Validator: 645 nodes, 1249 edges, 322 gaps, 1155 refs — 0 errors, 0 warnings.
