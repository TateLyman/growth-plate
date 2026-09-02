# Round 44 — most of that experiment was already run, by Janssen, for the FDA. And the drug is the cheapest part.

You asked me to check whether the experiment can be solved and to price it. **It was substantially run
already, in two species, and the documents are public.** I pulled the FDA label and the 264-page
Multi-disciplinary Review for NDA 212018.

## What was already done

**BALVERSA label, Juvenile Animal Toxicity Data:**

> In 4- and 13-week repeat-dose toxicology studies in **rats and dogs**, toxicities in bone and teeth were
> observed **at an exposure less than the human exposure (AUC) at the maximum recommended human dose**.
> **Chondroid dysplasia/metaplasia** were reported in **multiple bones in both species.**

**Label, Pediatric Use:**

> In a study of BALVERSA that included pediatric patients ages 6 to <18 years… **epiphysiolysis and bone
> fractures occurred.** In the postmarket setting… **slipped capital femoral epiphysis and accelerated
> linear growth** have been reported.

The FDA reviewer adds that the chondroid dysplasia **"may be especially relevant for a pediatric
population."**

**So the cartilage effect is on-target, dose-dependent, and present in rat, dog and human — and in humans
it appears at the standard clinical dose.** There is a dose-response with a clean no-effect level: the
trachea table runs **0, 0, 4m/1f, 6m/6f, 5m/5f** across five dose groups.

## And the exposure margins change the experiment I proposed

| | AUC (ng·h/mL) |
|---|---|
| rat, **highest** dose tested (32 mg/kg) | 1,910 |
| dog, **highest** dose tested (1.5 mg/kg) | 1,300 |
| **human, clinical 8 mg** | **29,268** |

**Human clinical exposure is ~15× the rat maximum and ~22× the dog maximum. Rats died at 0.003× human
clinical AUC.**

**A rodent cannot be dosed to human-equivalent exposure at all.** So the experiment I sketched last round
— "span two orders of magnitude below oncology-equivalent exposure" — is not runnable as stated, and I
should have known that before proposing it.

**The runnable version is narrower and better posed:** *does growth benefit appear below the
chondroid-dysplasia no-effect level?* The tox tables give that level, so the doses are already chosen.

## Pricing it

| line | estimate |
|---|---|
| **erdafitinib** (5 doses, n=10, 28 d, 150 g rats → ~0.65 g, buy 1 g) | **$2,000–4,000** |
| weanling Sprague-Dawley rats, 60 | $2,400–3,600 |
| per-diem housing, ~30 cages × 35 d | ~$1,300 |
| histology (physeal thickness, terminal cell height, RZ count) | ~$3,000 |
| µCT / radiographic bone length, 60 specimens | ~$4,500 |
| physeal mechanical testing | ~$2,000 |
| labour (0.25 FTE technician, 4 months) | $15,000–25,000 |
| **direct total** | **≈ $30,000–45,000** |
| with typical 55 % institutional indirects | **≈ $50,000–70,000** |

**Your "1 billion grams" framing is inverted: drug supply is the cheapest line item in the whole study.**
About one gram of erdafitinib runs the entire dose-response — roughly $2–4k of a $50–70k experiment. The
expensive parts are animals, imaging and labour, and they'd be identical for any FGFR inhibitor.

**Which means the accessibility argument doesn't favour erdafitinib the way it seemed to.** If drug cost
is 5 % of the study, then *obtaining* the compound was never the bottleneck — and TYRA-300/dabogratinib
being trial-only matters for **treating a person**, not for **running the experiment.** For the
experiment, an FGFR3-selective tool compound is purchasable too.

## Where this leaves it — honestly

**Against erdafitinib, and this is now regulatory-grade rather than inferred:** bone toxicity in two
species at exposures *below* human clinical, epiphysiolysis and fractures in an actual paediatric study,
and a label carrying SCFE and accelerated growth under Pediatric Use.

**But it does not close the specific question you raised**, because nobody measured *growth* in those tox
studies — they measured toxicity. **Whether a sub-toxic dose produces useful growth is still unknown**, and
it is exactly what the $50–70k study would answer.

**The one thing I'd change about my own recommendation:** run the dose-response with **both** erdafitinib
and an FGFR3-selective tool compound in the same experiment. The marginal cost is one more drug (~$2–4k)
and one more set of groups, and the growth-to-toxicity ratio between them **isolates the FGFR1+FGFR4
contribution directly** — settling `g_l3_local_fgfr1_sign_in_growth_plate` and
`g_l12_fgfr3_blockade_dose_response` in the same run.

Validator: 645 nodes, 1249 edges, 323 gaps, 1158 refs — 0 errors, 0 warnings.
