# F-R055 — Remove the brake, do not push the accelerator

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** All four Tier 1 items from F-R054 answered, and together they make one mechanism. **Deleting the
Hedgehog feedback inhibitor HHIP1 in a normal mouse limb produces progressive long-bone overgrowth with
the growth plate still expanded at fifty-three weeks, at unchanged body weight.** That is the elevation
experiment systemic SAG failed, it is sustained an order of magnitude longer than anything else in this
programme, and it inverts the design rule for the entire Hedgehog arm.

---

## 1. Kindblom 2002, in full — the human decline is real and it is regressed against Tanner stage

**Kindblom JM, Nilsson O, Hurme T, Ohlsson C, Sävendahl L, J Endocrinol 2002;174:R1–R6.** Ten human
growth-plate biopsies from epiphyseal surgery, all pubertal, immunohistochemistry with peptide-preadsorbed
negative controls, sections from different pubertal stages **mounted on the same slide under the same
solutions** to remove batch effects, quantified by image analysis as percent positive cells.

- **Ihh and PTHrP localise mainly to early hypertrophic chondrocytes** in all ten patients
- **Early puberty (Tanner B1–2/G1–2): both highly expressed. Late puberty (B4–5/G4–5): both consistently
  expressed in a lower percentage of cells**
- **Linear regression: a significant negative correlation between Tanner pubertal stage and the expression
  levels of both Ihh and PTHrP**
- No sex difference

**Limitations, stated plainly: n = 10, all within puberty (so the curve before puberty is unobserved), and
the readout is percent-positive cells by IHC, not absolute ligand concentration.**

> **The maintenance loop declines across human puberty. Link 6 of F-R054 is confirmed at source.**

---

## 2. The brake is induced in cartilage — measured, which is what I asked for

**Ye S-H et al. (CT-CM-NPs), on chondrocytes treated with the Smoothened agonist purmorphamine:**

> *"key Hedgehog target genes, including **Ptch1, Gli1, and Hhip, were significantly upregulated**."*

**That is F-R054 Tier 1 item 4 answered directly, in the right tissue.** My explanation for the systemic
null was inferred from developmental-biology feedback literature; it is now measured in chondrocytes.
**Agonising Smoothened raises Gli1 and both of its own antagonists at the same time.**

**The delivery data, for completeness:** DiR-labelled CT-CM-NPs accumulate in the growth plate on confocal
imaging of hard-tissue cryosections, peak at ~24 h with gradual clearance, with **reduced lung and spleen
uptake** and unavoidable liver uptake. Dosing was **1 mg/kg intravenously every two days for five weeks**
from 3 weeks of age. In Fgfr3^V376D/+ mice, CT-CM-NPs-PM **restored body length to 8.94 cm, not
significantly different from wild-type littermates.** The authors themselves note residual off-target
organ accumulation as a limitation.

---

## 3. Haraguchi 2025 — deleting the brake works where pushing the accelerator does not

**Haraguchi R, Kitazawa R, Yanagihara Y, Imai Y, Kitazawa S, *"Dissecting Hhip1 Function In Vivo Using a
Conditional Knockout Mouse Model"*, Acta Histochem Cytochem 2025;58(6):187–198.**

A CRISPR-generated *Hhip1* floxed allele (exon 2, frameshift on excision, abolishing the Hh ligand-binding
domain), because **global *Hhip1* knockout is perinatally lethal from respiratory defects.**

**Global null neonates:** increased body size and significantly greater body weight; *"a pronounced
expansion of the femoral growth plate"* with **the overall height of the epiphyseal cartilage significantly
increased and notable widening of both the proliferative and hypertrophic zones**; Gli1 markedly
upregulated.

**And then the experiment that matters — Prx1-Cre; Hhip1^flox/flox, limb-specific, in an otherwise normal
mouse:**

| endpoint | 10 weeks | **53 weeks** |
|---|---|---|
| **femur length** | **significantly increased** | **significantly increased** |
| growth plate | **visibly expanded** | **visibly expanded** |
| Toluidine blue-positive area | **significantly increased** | **significantly increased** |
| **body weight** | **not significantly different** | **not significantly different** |
| Gli1 | **sustained upregulation** | |

The authors' own reading: Hhip1 has a role *"not only [in] growth plate architecture during development,
but also **maintaining its integrity and regulating Hedgehog signaling dynamics throughout postnatal
skeletal maturation**"*, and the abstract describes **"progressive growth plate expansion and long bone
overgrowth."**

> ### Removing one Hedgehog brake in a normal limb gives longer femurs and an expanded growth plate at fifty-three weeks, with body weight unchanged — so it is skeletal, not somatic. It is progressive rather than front-loading, and it is sustained roughly ten times longer than any positive result previously in this branch.

**And the other brake points the same way.** Conditional *Ptch1* deletion in PTHrP⁺ resting-zone cells
causes clonal expansion into *"patched roses"* — the second Hh antagonist, deleted in the stem compartment,
also expands it. **Two independent brakes, two independent removals, both expand the plate.**

---

## 4. Four papers, one mechanism — and the rule inverts

| step | evidence |
|---|---|
| Smoothened agonism in chondrocytes upregulates **Gli1 *and* Ptch1 *and* Hhip** together | **Ye et al.** |
| So systemic SAG does nothing to a normal animal | **Li 2021, Fig 4H: NS** |
| But a local bead, at high local concentration or as a transient pulse, outruns the feedback | **`trompet2024`: durable femoral and tibial gain in normal rats, 6 months, contralateral-controlled** |
| And **deleting** the brake gives sustained, progressive elevation | **Haraguchi 2025: 53 weeks** |

> ### The design rule for the Hedgehog arm is not "agonise Smoothened." It is "remove the feedback inhibitor." Pushing the accelerator raises the brake with it; taking the brake off does not raise the accelerator's antagonist.

**This is the sixth instance of F-R052's counter-move pattern and the first time the pattern has suggested
its own solution.** Every node in this system answers a push with a transcriptional counter-move — but a
counter-move can itself be the target.

---

## 5. Human validation, and druggability — the best-shaped target in the programme

**Human genetics: *HHIP* is an established adult-height GWAS locus** (rs6845999 among others), from the
first generation of height GWAS onward. **The caveat is honest: individual common variants at height loci
contribute on the order of ±0.2 cm**, so this establishes that HHIP dosage moves human stature in the
expected direction — not that blocking it moves it far.

**Druggability, and this is where it gets unusually favourable:**

| property | consequence |
|---|---|
| **HHIP is the only reported *secreted* inhibitor of Hedgehog signalling** | it acts in the extracellular space, on the ligand |
| binds SHH, IHH and DHH with **high nanomolar affinity** | a single target covers all three ligands |
| **HHIP-N has structural homology to cysteine-rich domains, and a potential small-molecule ligand-binding pocket has been outlined** (Nat Commun 2021) | a small molecule is structurally plausible, not just an antibody |
| acts by engaging the **cholesterol moiety** on Hh ligands, preventing it binding PTCH1 | a defined interaction to disrupt |
| extracellular and secreted | **the transport problem does not arise.** F-R036's gate is about entry into an avascular matrix; a small molecule equilibrates across the plate in ~90 seconds, and an extracellular target needs no cell entry at all |

**No therapeutic HHIP inhibitor exists.** Research antibodies do (Proteintech 11654-1-AP is the one
Haraguchi used for immunoblot). **This is a target with human genetic support, a genetic proof of concept
sustained to 53 weeks, a structurally defined pocket, and no molecule — which is a very different position
from "no mechanism."**

---

## 6. Where link 11 stands

F-R054's link 11 was: *does maintaining the signal indefinitely prevent arrest, or only postpone it?*

**Haraguchi is now the longest-running Hedgehog elevation with a growth-plate endpoint that exists —
53 weeks, plate still expanded, femur still longer, effect described as progressive.** That is the best
evidence available and it points the right way.

**It is not proof, for three specific reasons:**

1. **Mouse growth plates do not fuse.** "Plate still expanded at 53 weeks" is a comparison against
   wild-type, not a demonstration of non-fusion.
2. **Prx1-Cre deletes from the limb bud.** This is a developmental *and* postnatal manipulation. **Nobody
   has deleted Hhip1 in an adult plate.** Whether removing the brake restarts an arrested plate, as
   opposed to preventing arrest from the beginning, is completely unknown — and it is the difference
   between a treatment and a genotype.
3. The femur-length effect sizes are in figures I have only as text references (Fig 6b, 6d, 6i).

---

## 7. Every flaw in this round

1. **Kindblom is n = 10, entirely within puberty, and semiquantitative.** The regression is significant;
   the curve outside puberty is unobserved.
2. **Haraguchi's phenotype is congenital-lineage, not adult-onset** — §6 point 2, and it is the single
   biggest limitation.
3. **HHIP has essential non-skeletal functions.** Global knockout is perinatally lethal from lung defects;
   Hhip1-null lungs show *"a marked reduction in alveolar air space and expansion of the alveolar septa."*
   **Systemic HHIP blockade is not obviously survivable, and the demonstrated skeletal effect is from a
   limb-restricted deletion.**
4. **Chronic Hedgehog pathway elevation is oncogenic** — medulloblastoma and basal cell carcinoma are
   Hh-driven, Li 2021 reports intestinal smooth-muscle thickening, and eLife 2019 reports that *"activation
   of hedgehog signaling in mesenchymal stem cells induces cartilage and bone tumor formation via
   Wnt/β-catenin."* Stated as a constraint on chronic dosing feasibility.
5. **`trompet2024`'s own mechanism panel remains weak** — significant only at one month for plate height
   and h_term, ns at two, CD73 at power 0.16. Its durable length gain is solid; its mechanism is not.
6. **No HHIP inhibitor exists at any stage of development.**
7. **The transport advantage assumes HHIP acts extracellularly within the plate.** Haraguchi's deletion is
   in the Prx1 lineage, which includes perichondrium and periosteum — so the relevant HHIP may be
   peri-skeletal rather than intra-plate. **Which compartment matters is not established.**

---

## 8. What I need next

**Tier 1:**

1. **Haraguchi 2025, Figures 6b, 6d and 6i — the femur length values at 10 and 53 weeks and the Toluidine
   blue area quantification.** I have the significance statements and none of the magnitudes. **This is
   the effect size of the best-shaped arm in the programme.**

2. **Any inducible or adult-onset deletion or blockade of Hhip1, Ptch1 or Ptch2 in cartilage**, with bone
   length as an endpoint. **§6 point 2 is the crux: does removing the brake in an already-mature plate do
   anything?** If nobody has done it, that is the experiment, and knowing that it has not been done is
   itself worth establishing.

3. **Bishop B / Kim et al., *"Hedgehog-Interacting Protein is a multimodal antagonist of Hedgehog
   signalling"*, Nat Commun 2021;12:7171.** The structural paper that outlines the HHIP-N pocket. **I need
   the pocket description and whether any compound has been screened against it.**

4. **Any long-term complete oestrogen ablation in a species whose growth plates actually fuse** — carried
   forward from F-R053 and F-R054 and still the cleanest test of whether oestrogen removal prevents or
   merely postpones fusion. Weise's own vehicle group (distal tibia fusing at E2 < 5 pg/ml) is why this
   matters.

**Tier 2:**

5. **Ptch1 conditional deletion in the growth plate — the primary**, with bone length and long-term plate
   patency, not just the "patched roses" clonal description.
6. **Whether HHIP expression in the human growth plate changes with pubertal stage**, as Ihh and PTHrP do.
   **If HHIP rises while Ihh falls, the brake and the accelerator move in opposite directions during
   closure and that is the whole mechanism of fusion.** I could not find this measured and it is the most
   valuable single unmeasured thing I can currently name.
7. The longest untreated follow-up of a human with aromatase deficiency or ER resistance.
