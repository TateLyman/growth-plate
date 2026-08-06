# DRAFT — Vivli / CSDR data request for KIGS (and NCGS)

**Status:** ready to submit except for the two fields I cannot supply — a named lead researcher
with an institutional affiliation, and a statistician of record. Everything else is written.

**Where to submit.**
- KIGS is a **Pfizer** dataset. Pfizer shares through **Vivli** — https://vivli.org — "Request
  Data". Pfizer's listing includes post-marketing studies; if KIGS does not appear in the study
  catalogue, Vivli accepts a *"data not listed"* enquiry, which routes to the sponsor.
- NCGS is a **Genentech/Roche** dataset. Roche shares through **Vivli** and historically through
  **CSDR** (https://clinicalstudydatarequest.com).
- Both require: lead researcher with institutional affiliation, a statistician, a research
  proposal, a publication plan, conflict-of-interest declaration, and signature of a Data Use
  Agreement. Analysis is performed inside the platform's secure environment; raw data are not
  exported.

> **Verify before submitting.** The routing above is from the sponsors' public data-sharing
> policies and I have not confirmed KIGS is currently listed in Vivli's catalogue. Check the
> catalogue first; if absent, use the enquiry route rather than assuming refusal.

---

## Title

Does cumulative growth hormone exposure shorten the remaining growth period? A test of the
stem-cell-depletion hypothesis in the KIGS cohort.

## Research question

In children treated with recombinant human growth hormone, is higher **cumulative** GH exposure
associated with **earlier attainment of near-adult height** at the **same or lower** final
height — after adjustment for baseline height deficit, age at start, diagnosis and bone-age
delay?

## Background and rationale

Chu et al. (PNAS 2025;122:e2512316122) show in mouse that GH shifts growth-plate stem cells from
self-renewing toward lineage-restricted division, reducing the slow-cycling label-retaining pool
and the PTHrP+ population, and that the effect is cell-autonomous (GHR conditional knockout
impairs clone formation). Independently, growth-plate senescence is division-dependent rather
than time-dependent, which makes growth velocity and growth duration draw on one finite budget.

If that mechanism transfers to humans, GH does not simply add height — it **trades duration for
velocity**. The published KIGS aggregates are consistent with that shape but cannot test it:

| Idiopathic GHD, prepubertal at start | Europe | USA |
|---|---|---|
| median dose | 0.21 mg/kg/wk | 0.30 mg/kg/wk (+43%) |
| baseline height SDS / age | −3.01 / 7.51 y | −2.99 / 7.4 y |
| Δ height SDS, year 1 | +0.69 | +0.75 |
| Δ height SDS, near-adult height | **+1.97** | **+1.96** |

(Maghnie et al., JCEM 2022;107:3287, Supplemental Table 11.)

A 43% higher dose buys more in year 1 and nothing at the end; and across all six
diagnosis × region cells the first year delivers 35–41% of the lifetime gain. **Both patterns
are equally consistent with catch-up growth toward a genetically set target and no depletion at
all.** They cannot be separated in aggregate, and the confound is visible in the same table:
2,642/8,597 European children reach near-adult height (31%) against 213/2,239 American (9.5%),
so the endpoint medians describe differently selected survivors. Individual participant data
resolves this; nothing else does.

## Objectives

1. **Primary.** Estimate the association between cumulative GH exposure (mg/kg, integrated over
   treatment) and *age at attainment of near-adult height*, adjusting for diagnosis, sex,
   baseline height SDS, baseline bone-age delay, age at start, and mid-parental height where
   recorded.
2. **Secondary.** Estimate the association between cumulative exposure and *total height SDS
   gain*, and test whether the two associations have opposite signs — the depletion signature.
3. **Secondary.** Estimate *bone-age advance per centimetre of height gained*, by exposure
   tertile. This is the most direct registry proxy for spending duration to buy velocity.
4. **Falsification.** Under catch-up-to-target, exposure should show **no** association with
   timing once baseline deficit is controlled. That is the null this study can reject or fail to
   reject, and it is prespecified.

## Analysis plan (outline; final version with the statistician of record)

- **Cohort:** patients with a recorded near-adult height, ≥2 years prepubertal treatment, in the
  diagnostic groups with adequate n (IGHD, ISS, Turner, SGA). Analyses stratified by diagnosis;
  no pooling across diagnoses in the primary.
- **Exposure:** cumulative mg/kg, and separately mean weekly dose and treatment duration, since
  the hypothesis concerns cumulative committed divisions rather than intensity alone.
- **Outcomes:** age at near-adult height; Δ height SDS start→near-adult height; Δ bone age per
  Δ height.
- **Models:** multivariable linear regression for each outcome; sensitivity analyses with
  time-to-event models for age at attainment, censoring those lost to follow-up.
- **The central threat, handled explicitly:** *differential attrition and confounding by
  indication.* Children given more GH differ systematically from those given less. Planned
  mitigations — inverse-probability-of-follow-up weighting using baseline covariates; restriction
  to countries/eras with uniform stopping rules; a negative-control exposure (dose in the final
  year, which cannot affect earlier trajectory); and a within-country analysis to remove
  health-system effects. **If these do not adequately separate exposure from indication, the
  study will report that the question is not answerable in these data**, which is a legitimate
  and publishable result.
- **Multiplicity:** two primary comparisons, prespecified; secondaries reported as exploratory.

## Variables requested

Per participant: diagnosis; sex; date/age at treatment start and stop; height and height SDS at
each visit with visit dates; bone age assessments with dates and method; GH dose at each
interval; pubertal stage where recorded; near-adult height and the criterion by which it was
defined; birth weight/length and gestational age; mid-parental height; country.

## Publication plan

Results published regardless of direction, in a peer-reviewed paediatric endocrinology or bone
journal, with the analysis plan registered before data access. Code deposited publicly. A plain
null will be reported as prominently as a positive finding — the hypothesis under test predicts
an association that would be an argument for *changing* GH dosing schedules, so a null is
directly useful to clinicians and must not be left in a drawer.

## Conflicts of interest

None. No funding from any manufacturer of growth hormone or of any growth-promoting agent. No
commercial interest in the outcome.

## Fields I cannot complete

- **Lead researcher** — name, degree, institution, ORCID, CV.
- **Statistician** — name and affiliation.
- **Institutional email** — most platforms will not accept a personal domain.

These are the barrier. A paediatric endocrinologist, a bone biologist, or a biostatistician at
any university with a data-sharing office can supply all three; the proposal above is written to
be handed to one of them largely intact.
