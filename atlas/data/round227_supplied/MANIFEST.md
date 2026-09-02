# Round 227 — the ASCO abstract, the wrong label revision, and what chasing it found

| file | source | what it settled |
|---|---|---|
| `asco2023_apec1621b_abstract_10007.txt` | Lee A, Chou AJ, … Parsons DW. *Erdafitinib in patients with FGFR-altered tumors: Results from the NCI-COG Pediatric MATCH trial arm B (APEC1621B).* J Clin Oncol 2023;41(16_suppl):10007 | **Confirms round 226 from the primary source.** Reports the tumour endpoint, hyperphosphataemia, nail changes, grade 1 vision changes, one grade 3 spinal cord compression and one grade 4 intracranial haemorrhage — and **not one word about the growth plate**, in a trial whose protocol mandates baseline and serial tibial physeal radiographs in every patient with central submission. 20 evaluable, median age 15, 4.7 mg/m²/day capped at 8 mg. |
| `balversa_label_s010_oct2024.txt` | BALVERSA prescribing information, revision s010, revised 10/2024 | **The wrong revision — and that is what produced the round.** §8.4 Pediatric Use is animal toxicology only; **no growth language of any kind**. |
| `balversa_label_current_nov2025_section84.txt` | Current label, DailyMed setid `2a8aa5c0-6c92-4566-8c45-e8f4d1fc20ee`, published 17 Nov 2025 | **Has it.** "Skeletal adverse reactions have occurred in pediatric patients… in a study of BALVERSA that included pediatric patients ages 6 to <18 years with FGFR-positive advanced solid tumors, **epiphysiolysis and bone fractures occurred**. In the postmarket setting and in literature reports, cases of **slipped capital femoral epiphysis and accelerated linear growth**… have been reported." |

## What the label sentence led to

It names a study. That study is **RAGNAR, NCT04083976**, which **has posted results** containing a cohort
labelled **"Pediatric Cohort," n = 11**:

| event | paediatric n=11 | broad panel n=217 | CCA n=35 | exploratory n=53 |
|---|---|---|---|---|
| **Tibia fracture** (serious) | **2** | 2 | 0 | 0 |
| **Epiphysiolysis** (serious) | **1** | 1 | 0 | 0 |
| Scoliosis | 1 | 1 | 0 | 0 |
| Foot / upper-limb / wrist / unspecified fracture | 1 each | — | — | — |
| Pain in extremity | **5** | — | — | — |
| Hyperphosphataemia | 7 | — | — | — |
| **Hyperparathyroidism** | **2** | — | — | — |

The atlas had cited RAGNAR before — for an ocular toxicity rate — **without ever opening its paediatric
arm.**

## Retrieval notes

The current label came from the DailyMed v2 API (`/services/v2/spls/{setid}.xml`) and the RAGNAR results
from the ClinicalTrials.gov v2 API. Both are free and scriptable; neither needed a manual download. Worth
remembering — the atlas has twice now been slowed by treating a regulatory document as something that must
be supplied.
