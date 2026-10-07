# Paywalled full texts to pull

Ordered by how much the answer changes if we get them. I can read any format —
PDF, or pasted text. Drop files anywhere in the repo or paste inline.

Status key: ⬜ needed · ✅ received

---

## Tier 1 — these decide the core argument

| | PMID | DOI | Citation | Why it is load-bearing |
|---|---|---|---|---|
| ⬜ | **15356066** | 10.1210/jc.2004-0205 | Iranmanesh, Bowers, Veldhuis. *JCEM* 2004;89:4581–7. "Activation of SSTR-2/-5 suppresses the mass, frequency, and irregularity of GHRP-2-stimulated GH secretion in men" | **Highest value in the whole review.** Abstract gives GHRP-2 suppression (~36%) but withholds the GHRH numbers. This is the only within-study head-to-head of how much somatostatin blunts GHRH-class vs GHRP-class drive. The entire "GHS classes are not interchangeable" claim rests on it. |
| ⬜ | **11452249** | 10.1210/jcem.86.7.7649 | Codner et al. / Merck. *JCEM* 2001. "Oral ibutamoren mesylate ... on the GH–IGF-I axis in growth-hormone-deficient children" | The earliest pediatric MK-677 data. Growth velocity + whether IGF-1 response sustained or attenuated in *children*. |
| ⬜ | **16537682** | 10.1210/jc.2005-2718 | Veldhuis et al. *JCEM* 2006;91:2441–6. "Ghrelin potentiates GH secretion driven by putative somatostatin withdrawal and resists inhibition by CRH" | Quantifies how much of ghrelin's action is brake-independent. Abstract is truncated mid-sentence at the key result. |
| ⬜ | **11720883** | 10.1530/eje.0.1450635 | Rigamonti et al. *Eur J Endocrinol* 2001;145:635–42. "GH rebound rise following somatostatin infusion withdrawal ... GHRH and a GHRP" | Only source with explicit within-session GHS tachyphylaxis *and* a GHRH comparator. Need the magnitude of the 2nd/3rd-bolus falloff. |

## Tier 2 — needed for the pool/reversibility question

| | PMID | DOI | Citation | Why |
|---|---|---|---|---|
| ⬜ | **12208658** | — | Rigamonti et al. *J Endocrinol* 2002. "GH and cortisol rebound rise during and following a somatostatin infusion ... GHRP" | Second tachyphylaxis dataset + the cortisol off-target of GHRP-class agents. |
| ⬜ | **22109886** | 10.1210/en.2011-1788 | *Endocrinology* 2012. "Homologous and heterologous in vitro regulation of pituitary receptors for somatostatin, GHRH, and ghrelin in a nonhuman primate" | Direct receptor-level desensitization/cross-regulation data — the mechanism of tachyphylaxis. Primate. |
| ⬜ | **18073313** | 10.1210/jc.2007-1388 | Paulo et al. *JCEM* 2008;93:819–24. "Gonadal status and BMI jointly determine GHRH/GHRP synergy in healthy men" | Quantifies GHRH+GHRP **synergy** and how adiposity/sex steroids modulate it. Bears on "GHS + something". |
| ⬜ | **15613434** | 10.1210/jc.2004-1838 | Veldhuis et al. *JCEM* 2005. "Determinants of dual secretagogue drive of burst-like GH secretion ... selective estradiol clamp" | Estradiol × secretagogue interaction — directly relevant to the aromatase-inhibitor adjunct question. |
| ⬜ | **19088159** | 10.1210/jc.2008-1534 | *JCEM* 2009. "Aromatase and 5α-reductase inhibition during an exogenous testosterone clamp unveils selective sex steroid modulation of somatostatin and GH secretion" | The cleanest human evidence on whether blocking aromatase changes **somatostatin tone**. Central to "GHS + aromatase inhibitor". |

## Tier 3 — queued, not yet searched out

Will be filled in as I work through Layers 0–2 and 5–6 (growth-plate biology, the
senescence clock, adult-height outcome trials, and the adjunct literature:
GnRH analogs, aromatase inhibitors, rhIGF-1, vosoritide).

---

## Notes on retrieval

Automated pipeline (`scratchpad/bin/lit.py`) already recovers full text where any
open-access route exists — Europe PMC JATS XML, NCBI efetch, and OpenAlex-resolved
publisher PDFs. Everything listed above has been confirmed to have **no** open route,
so these genuinely need your access. Items marked `[FT]` in the notes were retrieved
and read in full; `[AB]` means abstract-only and is labelled as such everywhere it is used.
