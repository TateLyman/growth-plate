# EXACT DOWNLOAD LIST — the on-treatment bone age under an FGFR inhibitor

Compiled round 226, 2026-08-10. Everything below was checked by this atlas first; each item says **what
it should contain**, **why it is needed**, and **whether it will actually answer the question**. Items are
ordered by expected yield.

---

## 1. ASCO 2023 abstract 10007 — the only report of APEC1621B that exists

- **Citation:** *Erdafitinib in patients with FGFR-altered tumors: Results from the NCI-COG Pediatric MATCH
  trial arm B (APEC1621B).* J Clin Oncol 2023;**41**(16_suppl):**10007**
- **DOI:** `10.1200/JCO.2023.41.16_suppl.10007`
- **URL:** https://ascopubs.org/doi/10.1200/JCO.2023.41.16_suppl.10007
- **Why I can't get it:** ASCO returns **HTTP 403** to this session.
- **What to look for:** any sentence containing *growth plate*, *physis*, *physeal*, *tibial radiograph*,
  *bone age*, *growth*, *height*, *scoliosis*. Also the **poster/slide deck** if ASCO has it — meeting
  posters often carry a safety table the abstract omits.
- **Honest expectation: LOW-TO-MODERATE.** A 300-word oncology abstract reports response rate and toxicity.
  It may list growth-plate changes as an adverse event; it will almost certainly not give a bone age.
  Worth one minute because it is the only published APEC1621B output in existence.

## 2. The APEC1621B full manuscript — if it now exists

- **Search:** PubMed / Europe PMC for `APEC1621B`, or `erdafitinib AND "Pediatric MATCH"`
- **Status as of 2026-08-10:** **no full paper exists.** A 33-result Europe PMC sweep returned only the
  abstract, reviews, and case reports.
- **What to look for if one has appeared since:** the **supplementary appendix**. In COG papers the
  protocol-mandated safety imaging is reported there, not in the main text.
- **Honest expectation: HIGH if it exists, and it may not.** Worth re-checking periodically rather than now.

## 3. NCTN Data Archive — request the APEC1621B dataset ★ THE ONE THAT ACTUALLY HAS THE ANSWER

- **URL:** https://nctn-data-archive.nci.nih.gov/
- **What to request:** study **APEC1621B / NCT03210714**, the imaging and case-report-form data
- **What it should contain, and this is why it is item ★:** protocol §8.2 mandates a plain AP radiograph of
  a single **proximal tibial growth plate in ALL patients BEFORE the first dose**, then — in patients with
  an open plate — repeats of the **same** plate **prior to cycles 2 and 5 and every 6 months**. §8.3, headed
  **"Bone Age/Knee MRI"**, requires that **all tibial radiographs and knee MRIs be submitted for review**.
  **Twenty evaluable patients, median age 15, at erdafitinib 4.7 mg/m²/day capped at 8 mg — this
  programme's own dose.**
- **How it works:** free, requires an account and a short data-use proposal; NCTN releases deposited trial
  data after primary publication. Turnaround is weeks, not days.
- **Honest expectation: HIGHEST OF ANYTHING ON THIS LIST — with two real caveats.** (a) The films are
  **tibial**, and a conventional bone age is read from a **hand and wrist**, so a formal Greulich-Pyle
  reading may never have been performed even though the section is headed "Bone Age". (b) The protocol
  **exempts patients whose tibial plate is already closed at baseline**, and at a median age of 15 that
  could be a large fraction of the twenty. **Even so, baseline-plus-serial physeal width in adolescents at
  8 mg would answer the round-224 question — preserved reserve or arrested remodelling — which the bone age
  alone would not.**

## 4. The BALVERSA label and the FDA review for NDA 212018 — the five paediatric growth cases

- **Label:** https://www.accessdata.fda.gov/drugsatfda_docs/label/ — search **BALVERSA**, take the most
  recent label revision
- **Review:** Drugs@FDA, **NDA 212018**, the Multi-disciplinary Review (this atlas has cited it before via
  CORR-047, so parts are already held)
- **What to look for:** the wording under **Warnings** and **8.4 Pediatric Use** for *accelerated growth*
  and any description of the **five paediatric cases** — specifically whether any bone age, growth velocity
  or physeal imaging is described, and what the ages and doses were.
- **Honest expectation: MODERATE for context, LOW for a bone age.** Labels describe events, not
  measurements. But the five-case series is the origin of this atlas's claim that "accelerated growth" is
  labelled, and I have never read the primary wording.

## 5. PROPEL2 / PROPEL3 clinical study reports or supplementary appendices

- **Papers:** *Oral Infigratinib Therapy in Children with Achondroplasia*, NEJM (PMID **39555818**);
  the phase 3, NEJM (PMID **42370681**, doi 10.1056/NEJMoa2604565)
- **What to look for:** the **supplementary appendix** of either, searched for *bone age*, *skeletal
  maturation*, *Greulich*. The conference deck this atlas holds asserts "no accelerated progression of bone
  age" — I need to know whether a number sits behind that sentence.
- **Why this matters even though it is infigratinib and not erdafitinib:** it is the same drug class in
  children with **intact gonadal function**, and it is the claim round 225 found has **no registered
  endpoint** behind it. If the supplement has numbers, the FGFR class gets its first real bone-age rate.
- **Honest expectation: MODERATE.** Bone age was not a registered outcome in either trial, so if it appears
  it will be as safety narrative — but NEJM supplements routinely carry exactly that.

---

## What I have already exhausted, so you don't repeat it

| checked | result |
|---|---|
| ClinicalTrials.gov registry, 5 trials (NCT04265651, NCT05145010, NCT04035811, NCT06164951, NCT03210714) | **no bone-age or skeletal-maturation outcome registered in any of them** |
| NCT03210714 posted results | adverse events only — scoliosis 1/20 serious, hyperphosphataemia 14/20; nothing on growth |
| APEC1621B protocol PDF (107 pp) | **read in full** — this is where §8.2 and §8.3 were found |
| Europe PMC, 33 results for APEC1621B / erdafitinib + Pediatric MATCH | no full paper |
| `erdachild2024` full text | bone age 14.0 at CA 16.2, **no baseline**, authors state assessments were not performed before or during therapy |
| `raimann2024` full text | physeal widening without apparent bone maturation; **no numeric bone ages** |
| `brizini2024` full text | proximal femoral physeal widening, **no bone age obtained** |
| FDA reviews for navepegritide NDA 219164 | **not posted** — every review filename pattern returns 404 |
| EMA EPAR for navepegritide | **does not exist yet** — MAA submitted October 2025, CHMP review ongoing |
| Voxzogo CHMP report | **has the answer for the CNP arm** — Greulich-Pyle, randomised, 1.02 (SD 0.83) vs placebo 1.14 (SD 0.82) |

## The one-line summary of where this stands

**The on-treatment bone age under an FGFR inhibitor has never been published by anyone.** The films that
would give it were taken by protocol, with a baseline, in twenty adolescents at 8 mg — and left in the COG
database. **Item 3 is the request that would get them.** Everything else on this list is worth a few
minutes; item 3 is worth an account and a proposal.
