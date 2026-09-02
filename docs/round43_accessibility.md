# Round 43 — the accessibility argument is right, and it has one hole that decides it

## Where you're right, and I'll say it plainly

**Erdafitinib is approved, obtainable, has an established dose, and is the only FGFR inhibitor with a
demonstrated large human growth effect.** 19.06 cm/yr. Nothing else in the class has that.

| agent | status |
|---|---|
| **erdafitinib** | **approved**, dose established (8 mg, up-titrated on phosphate) |
| **dabogratinib (TYRA-300)** | first-in-human **phase I/II** (SURF301) — in humans, but trial-only |
| infigratinib | dosed 0.25 mg/kg/day in achondroplasia; regulatory path troubled |

So on obtainability you're correct, and the "magical world where we acquire TYRA" framing is fair — it
isn't acquirable.

## The hole

**You said erdafitinib doesn't *need* to be dosed recklessly high. But the 19.06 cm/yr *was* full oncology
dosing in a child — and that exposure caused kyphoscoliosis with spinal cord compression requiring
surgery.**

**There is no data on erdafitinib at a lower dose for growth, in any species.** The entire curve below
oncology dosing is blank.

So accessibility buys access to **precisely the exposure that is known to be dangerous**, and says nothing
about any exposure that might be safe.

## And the pharmacology makes dose-reduction the wrong strategy *for this molecule specifically*

Dose reduction is the standard way to make an oncology drug tolerable. It's the strategy erdafitinib is
least suited to:

> **FGFR1 IC50 1.20 nM < FGFR3 3.00 nM.** The FGFR1:FGFR3 occupancy ratio is **worst at low doses.**

So lowering the dose doesn't give you a smaller share of the benefit — **it gives you a larger share of
the cost**, since FGFR1 blockade shortens bones (`karolak2015`).

**Infigratinib is the exact opposite case, and this is the comparison that matters:** at 0.25 mg/kg it
demonstrably produces growth with **no clinical evidence of FGFR1 or FGFR2 inhibition**. Its low-dose
window is favourable *and measured*. **That is the one thing erdafitinib lacks — not potency, not
availability, but a characterised safe dose.**

## And the price argument inverts

The expensive intervention isn't the unobtainable selective agent. **It's the cord decompression, the
spinal fusion, and the permanent neurological risk that the accessible one produced in three of five
children.**

## So: does erdafitinib stay in the stack?

**Conditionally, and the condition is a single missing experiment** — new gap
`g_l12_erdafitinib_low_dose_growth`, tractability 5:

> **Is there a low dose of erdafitinib at which FGFR3 relief produces growth without physeal failure?**

**The experiment needs no new molecule and nobody has run it.** Erdafitinib across five doses spanning two
orders of magnitude below oncology-equivalent exposure, in **wild-type growing mice**, measuring bone
length, physeal thickness, terminal hypertrophic cell height, resting zone count, **and capital femoral
physeal integrity** at each dose.

**The shape of the curve is the whole answer:**

- **Growth appears below the threshold for physeal widening** → a window exists, and the accessible drug
  becomes usable. Your position is vindicated.
- **Growth and widening rise together with no separation at any dose** → harm is inseparable from benefit
  for this molecule, and the accessibility advantage is worth nothing.

Run the same curve for an FGFR3-selective agent in parallel and the difference in growth-to-widening ratio
**isolates the FGFR1+FGFR4 contribution** — settling two other open gaps at the same time.

## Honest summary of where we are

I withdrew the mechanistic case against erdafitinib last round and I'm not reinstating it. What's left is
narrower and harder to dismiss: **the only characterised erdafitinib exposure is the harmful one, and the
obvious remedy — dose down — is the one manoeuvre its receptor ordering punishes.** That is a real,
specific, testable objection rather than a preference for the drug I can't get.

Validator: 645 nodes, 1249 edges, 323 gaps, 1156 refs — 0 errors, 0 warnings.
