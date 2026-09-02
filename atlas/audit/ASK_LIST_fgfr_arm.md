# WHAT IS NEEDED TO CLOSE THE FGFR ARM

Compiled round 233, 2026-08-11. **Every item below was checked against `atlas/tools/holdings.py --have`
before being written down**, and the file passes `--check-asks`. Nothing here is already on disk.

The FGFR arm has **96 open gaps** touching it. Most are peripheral or are answerable by me. This file lists
only the ones where **the atlas is genuinely blocked and a human can unblock it**, in order of what each
would change.

---

## TIER 1 — these change a decision in the stack

### 1. PROPEL 2 supplementary appendix — hyperphosphataemia **by dose cohort**
- **Paper:** *Oral Infigratinib Therapy in Children with Achondroplasia*, NEJM, **PMID 39555818**
- **What I need:** the **supplementary appendix**, specifically the adverse-event table **broken out by the
  five dose cohorts** (0.016 → 0.25 mg/kg), and any serum-phosphate summary.
- **Why it decides something.** Rounds 231–233 established the phosphate arm is FGFR1 and only FGFR1, and
  that erdafitinib's dose is titrated *toward* a phosphate target. Infigratinib is FGFR1-3 — it covers
  FGFR1 — yet at 0.25 mg/kg it produced growth in children **and no phosphate signal has ever been
  reported**. If hyperphosphataemia really is absent across that dose range while growth velocity rises,
  then **the growth arm and the phosphate arm separate by DOSE within a single FGFR1-covering molecule**,
  and the whole "switch to an FGFR3-selective agent" recommendation is replaced by a simpler one: use a
  lower dose of an agent that already has paediatric data. That is the single largest possible change to
  the FGFR arm and it turns on one table.
- **Also useful from the same file:** whether bone age appears anywhere.

### 2. PROPEL 3 supplementary appendix
- **Paper:** the phase 3, NEJM, **PMID 42370681**, doi 10.1056/NEJMoa2604565
- **What I need:** supplementary appendix — adverse events including phosphate, and any skeletal-maturation
  or bone-age content.
- **Why:** same logic as item 1 at scale, in a randomised trial. The conference deck this atlas holds
  asserts "no accelerated progression of bone age"; round 225 found no registered endpoint behind that
  sentence. **If a number sits behind it, the FGFR class gets its first real bone-age datum.**

### 3. The MSKCC tibial physeal radiographs — `farouk2021` / `farouk2023`, subject 3
- **What it is:** `farouk2021` Methods state plain radiographs of tibial growth plates were taken **every
  8–12 weeks in all five children**. For subject 3 that spans the **40 months** in which his height went
  from the 83rd centile to above the 99.9th (CORR-239).
- **Why it is the most valuable unpublished dataset in this field.** The surviving open question after
  rounds 229–230 is **proportionality**: is the physeal widening proportionate to the length gained, or in
  excess of it? The atlas's own gap record calls this "the cheap version that needs no new procedure."
  **Both halves already exist for the best-characterised patient in the literature and neither is published.**
- **How it would actually be obtained:** this is not a download. It is a request to the corresponding
  author (Karajannis, MSKCC) or a re-analysis published by that group. **I am flagging it as the highest-value
  target, not asking you to email anyone** — say the word if you want me to draft what the request would need
  to specify.

---

## TIER 2 — these close a named gap but do not move a decision

### 4. A serial sex-steroid panel under an FGFR inhibitor
- **Gap:** `g_l12_does_fgfr_inhibition_raise_testosterone_in_humans_and_shorten_the_window`
- **Why:** `kot2026` reports **elevated serum testosterone in treated male mice of both genotypes**. If that
  translated, it accelerates fusion and attacks duration — the only lever rounds 228–229 left standing — and
  it interacts with the anastrozole already in this stack. Human genetics points the other way (FGFR1 loss
  of function is Kallmann syndrome), so the direction is genuinely open.
- **What would answer it:** any paediatric FGFR-inhibitor series reporting **serial testosterone, LH, FSH or
  Tanner staging** in a child with an intact axis. **Nothing published contains this.** It is probably in
  clinical records at MSKCC and Vienna and nowhere else.

### 5. An HFTC cohort with height SDS
- **Gap:** the height leg of `g_l12_does_phosphate_control_subtract_from_fgfr_tki_growth_or_only_from_the_mechanical_failure`
- **Why:** `ramnitz2016` measured heights (it computed height-adjusted BMD Z-scores) and reported no stature
  abnormality, which passes CORR-233's admissibility test — but it is still a silence, not a measurement.
  **A height SDS distribution for any genotyped HFTC cohort would convert it.**
- **Honest expectation: it may not exist.** I have not found one.

---

## WHAT I DO **NOT** NEED, AND WHY — so nothing is requested twice

| | |
|---|---|
| ASCO abstract 10007 | **held** since round 227, read in full round 231. Requested in error at round 230 — CORR-238 |
| `farouk2021` (Debio1347 parent study) | **supplied and read** round 231; subject 3's dose is 80 mg/1.73 m² × BSA daily |
| PROPEL 2 schedule of assessments | **supplied** round 231 — no bone-age line item |
| BALVERSA label + FDA five-case series | **held**; label mined round 233, series read round 228 |
| SURF301 / TYRA-300 protocol | **held** since round 215, mined round 233 |
| APEC1621B protocol | **held** since round 226 |
| NCTN Data Archive | **struck** — APEC1621B is not deposited (CORR-232) |
| A bone age under an FGFR inhibitor | **does not exist**, closed by exhaustion across five routes (round 228) and confirmed at three levels of the record (round 231) |

---

## THE 83-REF BACKLOG, WHICH NEEDS NOTHING FROM YOU

`holdings.py --unread` lists **83 bibliography references whose full text is recoverable through NCBI eutils
and has never been read**, 20 of which this atlas had wrongly recorded as inaccessible (CORR-234). That is a
reading backlog, not an access problem, and it is mine to work through.
