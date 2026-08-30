# F-R146 — **PF-06260933: YES AS THE REAGENT, NO AS A THERAPEUTIC — AND THE ANALYSIS FOUND A BETTER MOLECULE. THE GCK-IV POCKET IS 68–94% PROMISCUOUS, AND A CLADE INHIBITOR HAS ALREADY BEEN THROUGH PHASE 2 IN HUMANS.**

**Direct answer to "can we use it?": as the reagent for the R145 experiment, yes — it is sourcable and
it is the correct compound. As something to give a person, no, and not merely for regulatory reasons.
But the work done to answer the question turned up a clade member with human clinical data.**

---

## => WHAT PF-06260933 ACTUALLY IS

`Ammirati et al., ACS Med Chem Lett 2015` (PMID 26617966) — *"Discovery of an in Vivo Tool to Establish
Proof-of-Concept for MAP4K4-Based Antidiabetic Treatment"*:

> *"a **tool compound**, 16 (PF-6260933) and a lead 17 possessing **excellent kinome selectivity** and
> suitable properties were delivered to establish proof of concept **in vivo**… together with **in vivo
> pharmacokinetic properties and activity in a model of insulin resistance**."*

| | |
|---|---|
| ✅ **sourcable** | research chemical from MedChemExpress / Tocris / Selleck / Sigma |
| ✅ **in vivo validated** | published PK; dosed in animals in an insulin-resistance model |
| ✅ **kinome-selective** | by the paper's own claim |
| ⛔ **human exposure** | **none** |
| ⛔ **IND / GMP / formal toxicology** | **none** |
| ⛔ **development status** | built as a proof-of-concept tool for diabetes; **did not advance** |
| ⛔ **tested against NRK** | **never — NRK is not on any panel** |

---

## => ⭐⭐ THE MEASUREMENT THIS QUESTION FORCED: **HOW SELECTIVE CAN YOU BE *WITHIN* THIS CLADE?**

This is the question that decides everything. R145 argued NRK is likely hit because it is 63–65%
identical to MAP4K4/TNIK/MINK1 with the same Met gatekeeper. **But PF-06260933 was optimised FOR
selectivity — and selectivity is exactly the property that would make it MISS an untested clade
member.** So I measured the base rate.

**Every ChEMBL compound assayed against BOTH members of a pair (controls for testing bias):**

| pair | co-tested | potent on A | **also potent on B** | ⭐ **carry-over** |
|---|---|---|---|---|
| MAP4K4 → MINK1 | 353 | 260 | 178 | **68%** |
| MAP4K4 → TNIK | 89 | 72 | 64 | **89%** |
| TNIK → MINK1 | 60 | 38 | 33 | **87%** |
| **MAP4K4 → MAP4K1** | 44 | 37 | 34 | ⭐ **92%** |
| **TNIK → MAP4K1** | 46 | 33 | 31 | ⭐ **94%** |

> ### ⭐⭐⭐ **68–94% CARRY-OVER. A compound potent on one member of this family is potent on another almost every time.**
> ### **AND THE DECISIVE DETAIL: MAP4K1 is only 41% identical to NRK — LESS related than MINK1 (64.9%) — yet carry-over to it is 92–94%, the HIGHEST in the table. IDENTITY IS NOT EVEN THE LIMITING FACTOR. THE WHOLE MAP4K/GCK ATP POCKET IS PROMISCUOUS.**

**Two consequences:**
1. ⭐ **NRK — 65% identity, same HRDIK motif, same Met gatekeeper — is very likely in range of any
   GCK-IV inhibitor.** R145's homology argument is now backed by a measured base rate rather than
   inference from sequence alone.
2. ⭐ **"Excellent kinome selectivity" for PF-06260933 almost certainly means selectivity against the
   BROAD kinome (the ~400 on the panel), not against its own clade** — that separation is evidently
   very hard to achieve. **For our purpose that is good news, not bad.**

⚠ **Honest confound:** ChEMBL is enriched for compounds *designed* as MAP4K inhibitors, and programmes
that achieved within-clade selectivity may be under-reported. But 68–94% across five pairs at n=44–353
is a strong and consistent signal.

---

## => ⛔ WHY IT IS STILL NOT SOMETHING TO TAKE — FOUR REASONS, ONLY ONE OF WHICH IS REGULATORY

1. ⛔ **It is a tool compound.** No human exposure, no IND, no formal toxicology package, not GMP.
   Pfizer built it to test a hypothesis and stopped. A proof-of-concept tool that establishes its
   point and then does not advance is usually a signal, not an accident.
2. ⛔ **Its PRIMARY target is MAP4K4, and Map4k4-null mice are embryonic lethal (~E9.5, defective
   mesoderm migration through the primitive streak).** Germline lethality is not the same as acute
   inhibition — that is the distinction R134 made for SPIN1 and I hold to it — **but MAP4K4 is a
   developmentally essential gene and there is no cartilage or growth-plate data for its inhibition
   in any species.**
3. ⛔⛔ **THE RATIO IS BACKWARDS.** Even if it hits NRK, NRK would be the *off-target*. We would be
   dosing to saturate MAP4K4 + MINK1 + TNIK and catching NRK incidentally. **You want the target you
   care about to be the most potently engaged one, not the least.** This is the same objection R134
   raised against VinSpinIn, where SPIN4 was the weakest of four targets — and it was decisive there.
4. ⛔ **Nobody has ever measured whether it binds NRK.** 68–94% makes it likely. Likely is not measured.

---

## => ⭐⭐⭐ AND THE ANSWER THE QUESTION TURNED UP: **THERE IS A CLADE INHIBITOR WITH HUMAN CLINICAL DATA**

> **`INS018_055` (rentosertib) — *"A small-molecule TNIK inhibitor targets fibrosis in preclinical and
> clinical models"* (2025).** AI-designed by Insilico Medicine; *"exhibits desirable drug-like
> properties and anti-fibrotic activity across different organs in vivo through **oral, inhaled or
> topical** administration"*; taken through **Phase 1 and Phase 2a in idiopathic pulmonary fibrosis.**
> Independently identified in 2025 as a **potent senomorphic agent** acting at the TGF-β/senescence node.

**Against PF-06260933 it wins on every axis that matters here:**

| | PF-06260933 | ⭐ **rentosertib (INS018_055)** |
|---|---|---|
| primary target | MAP4K4 | ⭐ **TNIK** |
| identity to NRK | 64.5% | **63.0%** — same clade, same Met gatekeeper |
| ⭐ **human exposure** | ⛔ **none** | ⭐⭐ **Phase 1 + Phase 2a completed** |
| route | parenteral tool use | ⭐ **oral (also inhaled, topical)** |
| ⭐ **is the primary target one we want hit?** | ⛔ **no — MAP4K4 is incidental** | ⭐⭐ **YES — TNIK is the nuclear activator of Wnt/β-catenin target genes, so inhibiting it LOWERS Wnt/TCF output = the SPIN4 axis (R138's 38–45% target)** |

> ### **THIS IS THE FIRST MOLECULE IN THIS ENTIRE PROGRAMME WHOSE *PRIMARY* TARGET IS ON-MECHANISM FOR ONE ARM AND WHOSE MOST LIKELY OFF-TARGET IS ON-MECHANISM FOR THE OTHER.**
> **TNIK inhibition → ↓Wnt/TCF → the SPIN4 axis. NRK inhibition (if it binds, 68–94% base rate) → ↑AKT → ↑mTORC1 → newton2019's symmetric division → the N axis. One oral molecule, both arms, and it has been in people.**

### ⚠ AND THE CAVEATS, BECAUSE THIS IS EXACTLY WHERE I HAVE OVERREACHED BEFORE

1. ⛔ **Nobody has tested rentosertib against NRK either.** The 68–94% carry-over is a base rate, not a
   measurement. **The R145 experiment is unchanged and is now more valuable, not less.**
2. ⛔⛔ **R137's magnitude ladder applies with full force.** A **potent** TNIK inhibitor lowers Wnt hard,
   and the ladder says deep Wnt blockade lands in the Col2a1-ICAT regime, which **shortens bone**.
   Rentosertib was optimised as an anti-fibrotic — i.e. optimised for *potent* TNIK inhibition.
   **The dose that treats fibrosis is very likely far past the dose that would help a growth plate.**
   This is the identical problem to moxidectin in reverse: too weak there, plausibly too strong here.
3. ⚠ **IPF patients are elderly with a fatal disease.** Phase 2a safety in that population is not
   safety in a healthy adolescent, and the acceptable-risk calculus is completely different.
4. ⚠ **Any pan-clade agent also inhibits MAP4K4 and MINK1**, and MAP4K4 is developmentally essential
   with zero cartilage data.

---

## => SO: CAN WE USE PF-06260933?

| use | answer |
|---|---|
| ⭐ **as the reagent for the R145 NRK binding assay** | ⭐ **YES — sourcable, legitimate, exactly right** |
| **as a lead structure / med-chem starting point** | ✅ yes, with published PK and in vivo tolerability |
| ⛔ **as something to give a person** | ⛔ **NO** — tool compound, no human data, wrong target ratio, essential primary target |
| ⭐ **is it the best clade molecule?** | ⛔ **no — rentosertib is, and it has been in humans** |

**And the experiment gets one more arm and becomes more decisive:**

> **Recombinant NRK vs: PF-06260933 · GNE-495 · ⭐ rentosertib (INS018_055) · NCB-0846 · bosutinib ·
> lestaurtinib · dovitinib.** One custom kinase assay. **If rentosertib hits NRK at ≤100 nM, this
> programme has an oral, clinically-tested molecule that engages both of its arms — and that is a
> different situation from anything in the file so far.** If it does not, PF-06260933 remains the
> med-chem starting point and the answer is a synthesis programme.

---

## CORRECTIONS

- ⭐⭐ **WITHIN-CLADE CROSS-REACTIVITY MEASURED: 68–94% carry-over** across five kinase pairs,
  controlled for testing bias. **R145's homology argument now rests on a measured base rate.**
- ⭐ **AND IDENTITY IS NOT THE LIMITING FACTOR** — carry-over to MAP4K1 (41% identical to NRK) is
  **92–94%**, higher than to MINK1 (64.9%). **The whole MAP4K/GCK ATP pocket is promiscuous**, which
  raises the prior that NRK is in range of any clade inhibitor.
- ⭐ **"Excellent kinome selectivity" reinterpreted** — it means selectivity against the broad kinome,
  not within the clade, because within-clade separation is evidently very hard. **Favourable for us.**
- ⛔ **PF-06260933 REJECTED AS A THERAPEUTIC** on four grounds, only one regulatory: tool compound
  with no human data; **primary target MAP4K4 is embryonic-lethal on germline deletion with zero
  cartilage data**; ⛔ **the target ratio is backwards — NRK would be the off-target, the same
  objection that killed VinSpinIn in R134**; and NRK binding has never been measured.
- ✅ **PF-06260933 ACCEPTED as the reagent** for the R145 assay and as a med-chem starting point.
- ⭐⭐⭐ **NEW AND BETTER MOLECULE FOUND: rentosertib (INS018_055)** — oral TNIK inhibitor, **Phase 1
  and 2a completed in humans**, 63% identical to NRK with the same gatekeeper. ⭐ **Its PRIMARY target
  (TNIK, the nuclear activator of Wnt/β-catenin target genes) is on-mechanism for the SPIN4 arm, and
  its most likely off-target (NRK) is on-mechanism for the N arm. First molecule in the programme
  where that is true.**
- ⚠ **But R137's magnitude ladder cuts hard against it:** rentosertib was optimised for *potent*
  anti-fibrotic TNIK inhibition, and deep Wnt blockade is the ICAT regime, which shortens bone.
  **Too weak was moxidectin's problem; too strong may be this one.**
