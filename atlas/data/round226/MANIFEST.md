# Round 226 — the exhaustive bone-age sweep

| file | source |
|---|---|
| `apec1621b_protocol.txt` | Text of the APEC1621B protocol and SAP (107 pp), version 28 Oct 2022, downloaded 2026-08-10 from `https://cdn.clinicaltrials.gov/large-docs/14/NCT03210714/Prot_SAP_000.pdf` |

## The two passages that locate the data

**§8.2 Monitoring for Specific Toxicities — Growth Plate Toxicity.** *"Patients will have a plain AP
radiograph of a single proximal tibial growth plate obtained prior to the first dose of protocol therapy…
If patients are found to have an open tibial growth plate, then repeat plain AP radiographs of the same
tibial growth plate will be obtained prior to cycles 2, 5 and every 6 months thereafter. Patients with
evidence of growth plate thickening or other changes should have a knee MRI performed to further assess
the degree of physeal pathology and undergo more frequent x-ray follow up at least every 3 cycles."*

**§8.3 Radiology Studies — Bone Age/Knee MRI.** *"All tibial radiographs and knee MRIs (if obtained) should
be submitted for review."*

**Cohort:** 20 evaluable patients, median age 15 years, enrolled June 2018 – July 2022, erdafitinib
**4.7 mg/m²/day capped at 8 mg** — this programme's own dose.

**Published output:** ASCO 2023 abstract only (JCO 41(16_suppl):10007). No full paper exists. The
ClinicalTrials.gov results posting gives adverse events — scoliosis 1/20 serious, hyperphosphataemia
14/20 — and nothing about growth.

## The registry sweep

Queried against the ClinicalTrials.gov v2 API on 2026-08-10. **None of these registers a bone-age or
skeletal-maturation outcome measure of any kind:**

| trial | population | results posted |
|---|---|---|
| NCT04265651 PROPEL2 | ages 3–11 | no |
| NCT05145010 extension | ages 3–18 | no |
| NCT04035811 natural history | ages 2.5–17 | no |
| NCT06164951 PROPEL3 | ages 3–17 | no |
| NCT03210714 Pediatric MATCH arm B | ages 1–21 | **yes** |

See `atlas/audit/ASK_LIST_bone_age.md` for the exact retrieval instructions.
