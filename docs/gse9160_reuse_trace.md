# Has the GSE9160 dissection failure reached the published record?

**Short answer: once, in a supplementary figure, with a significance test on n = 2 —
and the two other apparent uses turn out to be one clean reuse and one typo.**

This note exists because the P8-01 re-analysis
(`atlas/quant/notebooks/p8_01_gse9160_human_zonal/`) found that the two donors in
GSE9160 are not of equal quality: donor 1's laser capture resolves the zonal axis and
donor 2's largely does not. COL10A1 — which defines the hypertrophic zone — sits at
**0.6 %** of its hypertrophic level in donor 1's resting-zone sample and at **15–36 %**
in donor 2's. Genome-wide, 9.6 % of donor 1's detected probe sets vary more than
five-fold across zones against **1.0 %** of donor 2's.

If that is right, then **any zonal conclusion drawn from this series by pooling the two
donors is diluted by an amount nobody has reported.** So: has anyone done that?

The finding is reported here regardless of which way it fell, and it fell mostly the
reassuring way.

---

## 1. GEO's own citation field: the deposit has never been linked to a paper

Queried directly rather than inferred from a search returning nothing:

> **Citation missing** — *"Has this study been published? Please login to update or
> notify GEO."*
> — `https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE9160`, retrieved 2026-08-05

Submitted **25 September 2007**; last updated **25 March 2019**; contributors Mougey EB,
Olney RC, Soteropoulos P (Nemours Children's Clinic). **Eighteen years, no linked
publication.**

That matters for a reason beyond bibliography. The dissection-quality problem was never
available to peer review, because there was no manuscript to review. A reader
encountering this series meets a methods description consisting of four sentences in a
GEO record, and nothing else.

## 2. Every apparent downstream use, adjudicated

Europe PMC full-text search for the accession returns **three** records. Each was read.

### 2.1 Murray *et al.* 2018 — **CLEAN**

*Transcriptomics and machine learning predict diagnosis and severity of growth hormone
deficiency* · PMID 29618660 · PMC5928867

Their methods, in their words:

> *"Human gene expression data from growth plate–derived RNA was available for two
> subjects (1 male, 1 female)… **an expression barcode was defined for each growth plate
> zone for each patient**."*

**Donors kept separate throughout.** They used frozen RMA and a per-array absolute
expression barcode — a presence/absence call per array — rather than a pooled zonal
comparison. This is precisely the analysis class that the P8-01 diagnostic shows is
**robust** to the donor-2 problem: detection is unaffected (donor 2's arrays are the more
sensitive, and account for 87 % of all one-donor calls genome-wide), while zonal
*contrast* is what degrades. Their conclusions are not touched by this.

### 2.2 Choi *et al.* 2019 — **POOLED, with a significance test at n = 2**

*CXXC5 mediates growth plate senescence and is a target for enhancement of longitudinal
bone growth* · PMID 30971423 · PMC6458850

Figure S2A legend, verbatim:

> *"Analyses of the relative mRNA expression of CXXC5 and CXXC4 in growth plates during
> the pubertal period from microarray data (GEO: GSE9160) (**mean ± SEM, n = 2**; t test,
> \*P < 0.05 and \*\*P < 0.005)"*

This is the contaminated pattern: the two donors averaged, a standard error computed
across them, and a t test run — on a pair in which one member's compartments are
substantially mixed. A p-value from n = 2 is fragile in any case; here one of the two
observations carries a hypertrophic marker at a third of its hypertrophic level in the
resting-zone sample.

**Three things must be said in the paper's favour, and they are not concessions:**

1. **It is a supplementary figure.** The paper's core evidence is rat GSE16981 (n = 5)
   plus functional work in cells and mice. Figure S2 is a cross-species check on whether
   the human ortholog behaves similarly.
2. **Nothing here says the CXXC5 conclusion is wrong.** It says one supporting panel is
   weaker than its p-values suggest.
3. **Nobody could have known.** There is no publication describing GSE9160 and therefore
   no methods section in which the dissection variability could have been reported.

There is also a small factual slip worth recording because it shows how far the
accession has drifted from its origin: Choi 2019's Data-availability statement lists
GSE9160 among the accessions under which *their own* profiling results "were deposited".
GSE9160 was deposited in 2007 by a different group at a different institution.

### 2.3 Chen *et al.* 2021 — **NOT A USE. It is a typo.**

*Weighted miRNA co-expression network… in thoracic aortic aneurysm* · PMID 34164170 ·
PMC8182548

The paper's Methods consistently name **GSE9106** — a *plasma* mRNA dataset used as a
validation set in a thoracic-aortic-aneurysm study. In two sentences of the Results the
accession is written **GSE9160** instead:

> *"For GSE26155 and GSE9160, a total of 1,965 and 2,368 DEGs were screened"*
> *"These overlapping genes were validated using the DEGs of GSE9160"*

A human growth-plate dataset has no role in an aortic-aneurysm analysis, and the
Methods, the data-availability statement and the discussion all say GSE9106. **This is a
transposed digit, and it inflates the apparent reuse count of GSE9160 by 33 %.**

It is recorded because the atlas has now been bitten by exactly this class of error
twice in its own tree — a PMID transposition that pointed a citation at an autism
genetics paper, and a two-digit slip in `pth1r_receptor` — and both were caught only by
cross-checking an identifier against the record it claims to name. The same defect
exists in the published literature and nothing catches it there.

## 3. Result

| use | donors | verdict |
|---|---|---|
| Murray 2018 | **separate**, per-patient barcode | clean, and unaffected by the P8-01 finding |
| Choi 2019 Fig S2A | **pooled**, mean ± SEM, t test | contaminated — supplementary panel, not the paper's core |
| Chen 2021 | — | **not a use**; typo for GSE9106 |
| — | | GEO citation field: **missing**, 18 years on |

**One contaminated pooled zonal conclusion exists in the published record**, in a
supplementary figure of a paper whose main argument rests elsewhere. That is a much
smaller footprint than the finding might have implied, and reporting the small number is
the point of having looked.

## 4. What this trace cannot see

- **Europe PMC full-text search only reaches indexed full text.** A paywalled paper that
  used the accession without it appearing in an indexed abstract or open full text would
  not be found. The three hits are a floor, not a census.
- **Uses that do not name the accession** — "a published human growth plate microarray
  dataset" — are invisible to a string search.
- **The reverse typo.** If Chen 2021 can write GSE9160 for GSE9106, another paper can
  write GSE9106 for GSE9160. Not searched for.
- **This note does not re-analyse anyone's data.** Choi 2019's Figure S2A is flagged as
  resting on a pooled n = 2; whether re-doing it per donor changes the conclusion is a
  question for its authors, who have the raw analysis and we do not.

## 5. Why this is worth having as a standalone note

The combination is what is unusual: **a dataset with no publication, a measurable quality
asymmetry between its only two donors, and downstream reuse that has no methods section
to warn it.** The asymmetry is not hidden — it is visible to anyone who plots COL10A1 by
zone per donor, which takes about ten minutes — and in eighteen years it appears not to
have been written down.

Method, data and code for the underlying finding:
`atlas/quant/notebooks/p8_01_gse9160_human_zonal/` (`donor_separation.py`,
`RESULTS.md` §3). The whole chain reproduces from a cold fetch of the live GEO records.
