# OPEN THREADS — exactly where we are

Last updated: **2026-08-09, after round 157.** Repo: 686 nodes, 357 gaps, 1340 refs, validator errors none.

This file exists so a side pivot does not lose the main line. Anything listed OPEN here is unfinished
work with a defined next step, not a closed question.

---

## THREAD A — the NPR2 compound (MAIN LINE, OPEN, furthest advanced)

**Where we got to.** The arm was reframed at round 155 (CORR-169, SD-008): NPR2 has **three separable
control points**, not one, and the atlas had spent rounds 152–154 optimising the hardest.

- **A — ligand supply.** Vosoritide / navepegritide. In the stack. *See THREAD D for sourcing.*
- **B — receptor phosphorylation state.** Strongest genetic proof on the axis (`wagner2021`, +4.3–8.8%
  femur on a **wild-type FGFR3** background — our subject condition). **Cannot be de-risked**: both the
  kinase and the phosphatase are unidentified, and `egbert2024`/`egbert2025` show the identity has
  *resisted* phosphoproteomics plus combinatorial knock-in mice. **SD-008 forbids planning around the
  enzyme being identified.** Best compound remains a neutral phosphate-masked fostriecin prodrug
  (does not exist; `the_best_phosphatase_compound`).
- **C — phosphorylation-independent allosteric gain.** The live one.

**Current state of C — two allosteric sites on GC-B, opposite faces of the membrane:**

| | MCUF-42 / compound 1 (`ma2024`) | compound 20 (`andresen2023`) |
|---|---|---|
| site | **extracellular**, K_D 710 nM | **intracellular** KHD, GC-A Thr640 / GC-B Ile624 |
| mechanism | raises CNP **affinity** (6.4× potency shift, **no Eₘₐₓ change**) | raises **efficacy** (+30% Eₘₐₓ) |
| phospho-dependence | untested | **independent** (+183% on GC-A 7E) |
| exists at wild-type GC-B? | **yes** | **no** — GC-B data are from the I624T mutant |

**The named compound (round 157).** `CID 647514` = **compound 1**, CAS **332862-27-8** — MCUF-42 with a
piperazine for its piperidine. EC₅₀ 0.74 µM, **Eₘₐₓ 112%** (vs MCUF-42's 0.80 µM / 86%), no GC-A activity
to 67 µM, HTS 96.67% @10 µM. **14 vendors.** MCUF-42 itself has **zero** vendors.
Charge probe: `CID 3588620`, the N-methylpiperazine analogue, 50.37% @10 µM, 7 vendors.

**OPEN — next steps, in order:**
1. **One potentiometric titration** of CID 647514 and CID 3588620 (`g_l12_pka_and_cartilage_uptake_of_the_gcb_pam_series`).
   Decides whether the cationic/Donnan argument applies to this series at all. Cheapest
   decision-relevant experiment on the whole axis. *CORR-173: compound 1 is probably NOT cationic —
   cyanoethyl + thioamide suppress the amine.*
2. Cartilage explant uptake, neutral vs cationic member — ratio of tissue to bath.
3. Spatial distribution (concentrated-throughout vs bound-at-surface — the `hakim2025` failure mode for
   lipophilic cations; this chemotype is XLogP ≈ 3.8).
4. Counter-screen the `andresen2023` series at **wild-type** GC-B (`g_l12_gcb_selective_allosteric_enhancer_does_not_exist`).

**Unresolved objection, not waved away:** the plate is a CNP **consumer**, not producer, so a systemic
potentiator raises vascular signalling at least as much as plate signalling. The cationic route is the
only proposed escape and it is unmeasured.

---

## THREAD B — the phosphatase arm (OPEN but HELD)

Fostriecin has the right enzyme selectivity (PP2A 1.4 nM vs **PP5 60 µM measured**, `swingle2009`) and the
wrong charge (dianion, partition 0.21). Candidate is a neutral phosphate-masked prodrug (~4.3× gain,
CORR-167). **Does not exist**; no fostriecin prodrug has ever been made. Not cheap to make — the
`jiang2025` nine-step route needs an **engineered enzyme** for its key C–H oxidation.

**OPEN:** `g_l12_fostriecin_pp4_versus_pp2a_attribution` — re-run the existing `swingle2009` ten-analogue
panel **with a PP4 column**. `theobald2013` shows PP4C knockdown alone reproduces fostriecin's cellular
phenotype while PP2AC knockdown does not, so the dose ceiling and the intended effect may sit on
different enzymes. Compounds already exist; assay already established. **One plate.**

---

## THREAD C — NPR3 / clearance arm (CLOSED, do not reopen without new evidence)

Not added to the stack. NPR-C is bifunctional with opposite signs (SD-007); M372049 has the wrong sign at
the receptor; no pharmacological NPR3 ligand has a bone endpoint in any species; NPR-B counter-screen
exists nowhere.

---

## THREAD D — sourcing vosoritide / navepegritide (OPEN — side pivot, 2026-08-09)

See `atlas/data/round158_cnp_analogue_sourcing/README.md`. Summary of state:

- **Voxzogo (vosoritide, BioMarin)** — US list ~**$320k/yr**, net ~$240k after rebates; ~$1,139/vial US;
  CA$950/vial submitted (CA$346,988/yr). No generic or biosimilar before **~2030–2031** (8 patents,
  orphan exclusivity; one Paragraph IV challenge, eligible since 19 Nov 2025).
- **Yuviwel (navepegritide, Ascendis)** — FDA approved **27 Feb 2026** (accelerated), US launch Q2 2026,
  **orphan drug exclusivity granted April 2026** (→ ~2033). WAC **$38,325 per 4 injections** ≈
  **$498k/yr** — *more expensive than vosoritide*. EU decision expected Q4 2026.
- **Both labels require achondroplasia AND open epiphyses.** Our case is bone age 16+ and non-achondroplasia
  → off-label on two axes. Every legitimate route runs through a prescriber.
- **Cheapest legitimate route identified: clinical trial.** `NCT06382155` — BioMarin Phase 2 vosoritide in
  **idiopathic short stature**, **RECRUITING** as of May 2026, with open-label extension "until near-final
  adult height." Free drug plus monitoring. Eligibility (age, open plates, treatment-naïve) not yet
  checked against this case — **OPEN**.

**OPEN next steps:** check NCT06382155 eligibility in detail; check EU/Japan reimbursed prices once
Yuviwel EU decision lands Q4 2026; re-check biosimilar timing after the Paragraph IV challenge resolves.

---

## STANDING CONSTRAINTS (carried, not re-litigated)

Never invent a citation, author, year or number. Species on every claim. Reviews are an index, not a
source. Identifiers looked up, never recalled. No manufacturing edges to hit a density target. Re-analysis
results graded as strictly as anyone else's. See `atlas/audit/standing_decisions.yaml` SD-001…SD-008.
