# OPEN THREADS — exactly where we are

Last updated: **2026-08-09, after round 161.** Repo: 688 nodes, 358 gaps, 1347 refs, validator errors none.

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

**ROUND 161 — compound 1 CONFIRMED best in the screen, and confirmed NOT a therapy.** Re-ranked all 253
selective actives: **208 distinct scaffolds** (singleton-dominated = HTS noise), **40% PAINS/BRENK-flagged**,
and all seven compounds scoring above compound 1 are **scaffold singletons** (one is **diazinon**). Compound
1 is the highest-activity compound with real SAR support (4-member scaffold + 3-member sister). Best
clean-and-supported alternative: 65.1%. **But compound 1 is itself BRENK-flagged for the thioamide — and
`ma2024` shows the thioamide is REQUIRED (amide -> complete loss). The alert IS the pharmacophore.** Plus
`robinson2011`: Go6976 is a catalytic-site *inhibitor*, so there is **no chemical starting point for an
intracellular GC-B activator**.

**VERDICT — add to the therapeutic stack: NOTHING. Add as research probes: `CID 647514` + `CID 3588620`.**

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
4. ~~Counter-screen the `andresen2023` series at wild-type GC-B~~ — **DONE, ALREADY, AND NEGATIVE
   (CORR-174).** andresen2023 reported it: *"Neither of the compounds modulated the potency of CNP or
   increased the maximum level of CNP-mediated cGMP production."* All ~100 analogues were made and
   screened **against GC-A**. Every GC-B number for this chemotype comes from the **I624T point mutant**.
   The site transfers; **no molecule does.** Remaining open: whether new chemistry can be built against
   Ile624 — a synthesis programme, not a screen.

**Unresolved objection, not waved away:** the plate is a CNP **consumer**, not producer, so a systemic
potentiator raises vascular signalling at least as much as plate signalling. The cationic route is the
only proposed escape and it is unmeasured.

**Round 159 — A vs B settled: they MULTIPLY, and B gates A.** Three kinetic handles, three arms, no
overlap: ligand moves **Vmax** (>10×, `robinson2012`), KHD phosphorylation **gates** whether Vmax can move
(`yoder2012`; 6E only ~20% of WT), KHD allostery moves **Km** and is **phosphorylation-independent**
(`edmund2019`). MCUF-42 is a pure **potency**-shifter with no Eₘₐₓ change, and `robinson2017` says
dephosphorylation is **not surmountable by ligand** — so a potency-shifter **cannot rescue a
dephosphorylated receptor**. Synergy, not additivity. Corollary: the PAM is worth **more** in a
normal-FGFR3 subject than in achondroplasia — opposite to how every trial is powered.

**New interaction found: `prickett2021` — exogenous CNP agonism SUPPRESSES endogenous CNP production**
in humans (−4.2 to −5.0 pmol/L NTproCNP at 4 h from day 183, p=0.003–0.015; replicated in
hypochondroplasia by `kanakatti2026`). A PAM has **no intrinsic activity** — it multiplies endogenous
ligand, which this loop shrinks. **So the PAM needs a feedback-immune exogenous analogue underneath it.**
Inverts the round-156 framing: the peptide isn't displaced by the small molecule, it's what makes it work.

**`g_l12_does_the_gcb_pam_potentiate_vosoritide` — DOWNGRADED to confirmatory (round 160). Probably YES,
on two independent grounds without an experiment.** *Structural:* vosoritide is Pro-Gly + the 37 C-terminal
residues of CNP-53 and **retains the intact CNP-22 binding ring** — it differs from native CNP only by an
N-terminal protease-resistance extension, and the ring is what engages the ECD where MCUF-42 acts.
*Cross-ligand:* PAMs here are not ligand-specific — MCUF-651 potentiates **ANP, BNP and endogenous human
plasma pools** at GC-A. Residual risk: the N-terminal extension could obstruct a cleft-adjacent modulator.

**Rivals checked, none displaces either arm:** BMN 333 = better control point A, not a third arm;
KK8398 = infigratinib under a Kyowa Kirin code, already in the stack; activating antibodies (`liu2026`,
XX16 works in vivo) are **dead on delivery at ~150 kDa** against a farnum2006 curve that is undetectable
by 40 kDa.

---

## THREAD B — the phosphatase arm (**CLOSED as a compound arm** 2026-08-09; mechanism retained)

Fostriecin has the right enzyme selectivity (PP2A 1.4 nM vs **PP5 60 µM measured**, `swingle2009`) and the
wrong charge (dianion, partition 0.21). Candidate is a neutral phosphate-masked prodrug (~4.3× gain,
CORR-167). **Does not exist**; no fostriecin prodrug has ever been made. Not cheap to make — the
`jiang2025` nine-step route needs an **engineered enzyme** for its key C–H oxidation.

**Round 159 verdict: KEEP the control point, but "keep" here means the mechanism, NOT a drug.** It is not
redundant with Thread A — different kinetic handle — but it has no compound, no identified enzyme, and
SD-008 bars planning on identification. Its incremental value in a stack that already contains an FGFR
inhibitor is bounded by the **1.42× tonic, FGF-independent** component.

**OPEN:** `g_l12_fostriecin_pp4_versus_pp2a_attribution` — re-run the `swingle2009` ten-analogue panel
**with a PP4 column**. `theobald2013` shows PP4C knockdown alone reproduces fostriecin's cellular phenotype
while PP2AC knockdown does not, so the dose ceiling and the intended effect may sit on different enzymes.

**ROUND 161 — REMOVED AS A COMPOUND ARM. Four independent blockers.** (1) enzyme unidentified and has
resisted direct attack (SD-008); (2) no compound exists and none is cheaply makeable; (3) **PP2A-versus-PP4
selectivity has never been measured for any compound** — across all 39 human Ser/Thr phosphatase targets in
ChEMBL, 1,801 molecules carry a value, **16** have a PP2A catalytic number, **1** has a PP4 number
(fostriecin), and **0 have both**; (4) prize bounded at **1.42×** tonic where an FGFR inhibitor is already
present, against systemic pan-PPP liability with hepatic DLT. **Nothing to add. Mechanism retained**
(`wagner2021`, +4.3–8.8% femur on wild-type FGFR3).

**CORR-175 corrects the cost claim — it is NOT one plate.** ChEMBL target `CHEMBL5465552` (PP4 catalytic
subunit) holds **exactly one activity record in the entire database**: fostriecin, 3.0 nM. Not one
analogue, not one other chemotype. **PP4 has no chemical probe and no counter-screen series in public
medicinal chemistry** — the assay has to be built before the panel can be run. The compounds exist; the
assay does not.

---

## THREAD C — NPR3 / clearance arm (CLOSED, do not reopen without new evidence)

Not added to the stack. NPR-C is bifunctional with opposite signs (SD-007); M372049 has the wrong sign at
the receptor; no pharmacological NPR3 ligand has a bone endpoint in any species; NPR-B counter-screen
exists nowhere.

---

## THREAD D — sourcing vosoritide / navepegritide (**CLOSED** 2026-08-09)

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

**CLOSED — and price was never the binding constraint.** Full 31-trial landscape scanned.
`NCT06382155` (vosoritide in idiopathic short stature) is **age 3–11, Tanner Stage I, treatment-naïve** —
ineligible three ways over. The only two recruiting studies in the adolescent band both gate on
**genetically confirmed achondroplasia plus an open, actively growing plate**: `NCT06732895` (Ascendis,
navepegritide 12–17; excludes AGV < 1.5 cm/yr or radiological growth-plate closure) and `NCT07441876`
(BioMarin, BMN 333 vs vosoritide, 2–17; requires ACH and open epiphyses).

**Every route — label, trial, assistance programme — gates on diagnosis and growth-plate status, none on
money.** For a non-achondroplastic subject at bone age 16+ there is no legitimate access route at any
price. Do not reopen this as a pricing exercise.

**Two carried consequences:** (1) two sponsors with the deepest CNP datasets in existence both decline to
enrol a closing plate — convergent with `hakata2024` and `serrat2013`, and evidence about whether this
axis is worth pursuing in this case at all, not just about supply; (2) this raises the relative value of
THREAD A, the one route not gated by another organisation's inclusion criteria.

Unlicensed / RUO peptide sourcing was deliberately not investigated; reason recorded in the round-158
README so the omission is not mistaken for an oversight.

---

## STANDING CONSTRAINTS (carried, not re-litigated)

Never invent a citation, author, year or number. Species on every claim. Reviews are an index, not a
source. Identifiers looked up, never recalled. No manufacturing edges to hit a density target. Re-analysis
results graded as strictly as anyone else's. See `atlas/audit/standing_decisions.yaml` SD-001…SD-008.
