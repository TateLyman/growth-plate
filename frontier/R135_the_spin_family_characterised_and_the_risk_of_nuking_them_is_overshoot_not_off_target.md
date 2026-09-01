# R135 — the SPIN family characterised gene by gene, with human growth-plate expression
# measured. **"Nuke them all" is not obviously wrong — SPIN1 inhibition points the SAME
# direction as SPIN4 inhibition on Wnt.** The real risk is **overshoot**, not off-target,
# and this file already has the experiment that shows what overshoot looks like.

**Operator: the cancer point is weak — characterise each SPIN and see if we can nuke them.**
Agreed on the first part: 5/19 vs 0/17 at P = 0.047, n small, female heterozygotes null, and human SPIN4
expression *elevated* in cancers rather than reduced. **That is a signal to watch, not a finding. I
over-weighted it.**

---

## 1. THE FAMILY, MEASURED IN THE TISSUE THAT MATTERS

Human growth plate, LCM zone-resolved (GSE9160). Array 25th/50th/75th percentiles = 60.8 / 196.9 / 539.8;
calibrators NPPC ≤ 19.8 (absent), PTHLH 308.6 (present).

| gene | Reserve | Prolif | PreHyp | Hyper | Perich | call |
|---|---|---|---|---|---|---|
| **SPIN1** | **1430.6** | 1129.0 | 1325.3 | 1173.9 | 1410.3 | **dominant, uniform across all zones** |
| **SPIN3** | 608.4 | 323.3 | 290.8 | 330.7 | 324.8 | expressed, RZ-enriched |
| **SPIN2A** | 300.4 | 41.6 | 76.9 | 135.8 | 96.9 | expressed, **7× RZ-enriched** |
| **SPIN4** | 90.9 | **267.8** | 193.2 | 153.6 | 195.3 | expressed, **PZ-enriched, lowest of the family** |
| SPIN2B | — | — | — | — | — | **no probe on array** |

**Two things fall out immediately:**
1. **SPIN1 is the dominant family member in the growth plate — 5–15× SPIN4 — and uniform across every
   zone.** Any pan-SPIN agent delivered locally is functionally a *SPIN1* agent there. **The "local delivery
   makes it SPIN4-selective" idea from R133 is dead.**
2. **SPIN4 is PZ-enriched and LOWEST in the resting zone** — which fits Lui 2023 exactly. Her primary
   growth-plate finding was **increased proliferation rate in the PZ** with no change in zone height, and
   the resting-zone increase followed downstream from decreased Wnt. **The gene acts where it is expressed.**

---

## 2. WHAT EACH ONE DOES

| gene | function | evidence quality |
|---|---|---|
| **SPIN1** | **Transcriptional COACTIVATOR.** Reads H3K4me3 + H3R8me2a via three Tudor domains. Coactivates rRNA genes, MAZ targets, and ⭐ **Wnt/TCF4 target genes.** Overexpression transforms NIH3T3 (soft agar, nude mice); elevated in many cancers; **active oncology target** | **well characterised** |
| **SPIN4** | Histone reader; **PROMOTES canonical Wnt**; inhibits proliferation; **negatively regulates resting-zone progenitor number**. LOF → human X-linked overgrowth (+4.5–5 SDS), mouse +5.06% length | **well characterised (Lui 2023/2026)** |
| **SPIN2A / SPIN2B / SPIN3** | Three Tudor domains + IDRs; methylated-histone-binding molecular adaptors; annotated for transcription regulation, chromatin organisation, and ⭐ **gamete generation**. **All five family members bind SPIN·DOC**, which *attenuates* SPIN1 coactivator activity | **largely uncharacterised** |

⚠ GeneCards lists SPIN3 against X-linked deafness 4 and X-linked severe congenital neutropenia. **These are
very likely positional locus associations rather than causal, and I am flagging them as unverified rather
than treating them as SPIN3 LOF phenotypes.**

---

## 3. ⭐⭐⭐ THE REFRAME — SPIN1 INHIBITION POINTS THE **SAME WAY** AS SPIN4 INHIBITION

**SPIN1 coactivates Wnt/TCF4 target genes. SPIN4 promotes canonical Wnt. Inhibiting either LOWERS Wnt output
in chondrocytes — which is precisely the mechanism by which SPIN4 loss increases resting-zone progenitors
and lengthens bone.**

> **My objection in R133–R134 was that VinSpinIn hits SPIN1 hardest and SPIN4 weakest. On the Wnt axis that
> may not be a defect at all. SPIN1 is 5–15× more abundant in the plate and is a direct Wnt/TCF4
> coactivator — so a pan-SPIN agent would deliver a LARGER chondrocyte Wnt reduction than a SPIN4-selective
> one would. The operator's instinct is mechanistically defensible and my framing was wrong.**

---

## 4. ⛔ BUT THE RISK IS **OVERSHOOT**, AND THIS FILE ALREADY HAS THAT EXPERIMENT

The Wnt-lowering dose–response in cartilage is **non-monotonic**, and both ends are measured:

| intervention | degree of chondrocyte Wnt reduction | result |
|---|---|---|
| **Spin4 loss** | **partial, cell-intrinsic, one reader** | ⭐ **RZ progenitors ↑, tibia length ↑ to 18 months, h_term untouched** |
| **Col2a1-ICAT** | chondrocyte-wide β-catenin blockade | ⛔ **SHORTENS bone** |
| PORCN inhibition | organism-wide ligand blockade | ⛔ reduces PZ; impairs trabecular + cortical bone mass |

**And R134's dosage law, which generalises across this whole gene class:** heterozygous **partial** loss of
NSD1 (Sotos) and EZH2 (Weaver) **increases** growth in humans, while homozygous **complete** loss of Nsd1 or
Ezh1/Ezh2 **impairs** it in mice.

> **PARTIAL LOSS GROWS. COMPLETE LOSS SHORTENS. Removing SPIN1's coactivator function — at 1430 units of
> expression, uniformly across every zone — is far more likely to be the ICAT case than the Spin4 case.
> "Nuking them all" risks landing on the wrong side of a non-monotonic curve, and the wrong side is SHORTER.**

**That is the real objection. It is not off-target toxicity and it is not SPIN1 essentiality — both of which
I raised and both of which were weaker than this.**

### The named, specifiable risks that remain
1. **Overshoot into the ICAT regime** — bone shortening. The dominant risk.
2. **Gamete generation** — the shared annotation across SPIN2A/2B/3. A pan-family agent has a plausible
   reproductive effect, and this is specifiable rather than hand-waving.
3. **VinSpinIn's unattributed toxicity**, present in the inactive control, unresolved "despite significant
   effort" (R134).
4. On-target neoplasia — **downgraded to a watch item**, per the operator.

---

## 5. SO CAN WE NUKE THEM?

**The mechanism says maybe. The dose–response says be careful. The molecule says not this one.**

- ✅ **Direction is right:** SPIN1 and SPIN4 inhibition both lower chondrocyte Wnt, which is the validated
  growth-promoting direction
- ⚠️ **Magnitude is the whole question:** the curve is non-monotonic and the overshoot end is measured and
  shortens bone
- ⛔ **VinSpinIn is still the wrong tool** — not on selectivity direction any more, but on **ΔTm 6.53 for
  SPIN4 (weakest of four)**, an unattributed toxicity shared with its inactive control, **no PK, and no in
  vivo administration on record**

**What the analysis actually argues for is a LOW-DOSE, PARTIAL pan-SPIN engagement — deliberately
sub-saturating — which is the opposite of "nuking."** The therapeutic object is a *partial* Wnt-output
reduction, and the family is a legitimate way to get it. **The floor and the ceiling both matter, and
nobody has mapped either in cartilage.**

### The experiment that would settle it, and it is small
**Dose-ranging VinSpinIn (or A366) in fetal tibial explant culture or the E16.5 femur system this file
already uses (hakata2024 / shuhaibar2021), with bone length as the endpoint.** A non-monotonic curve would
show directly, the readout is length rather than a marker, and it costs one experiment. **No SPIN compound
has ever been given to a growing bone in any system.**

---
### Corrections carried by this round
- **The neoplasia objection is DOWNGRADED to a watch item** — one small study at P = 0.047, null in females,
  with human expression pointing the other way. The operator was right that I over-weighted it.
- **My R133/R134 selectivity objection is REVERSED in direction:** SPIN1-dominance is not obviously a defect,
  because SPIN1 coactivates Wnt/TCF4 and inhibiting it lowers Wnt — the same direction as SPIN4 loss.
- **The real risk is named: OVERSHOOT into the Col2a1-ICAT regime**, on a non-monotonic dose–response where
  the far end shortens bone.
- **Family expression in human growth plate measured for the first time here:** SPIN1 dominant and uniform,
  SPIN4 lowest and PZ-enriched, SPIN2A/SPIN3 RZ-enriched, SPIN2B absent from the array.
- **"Nuke them" is re-specified as "partially engage them"** — and the decisive experiment is a dose-ranging
  explant with a length endpoint, which has never been done for any SPIN compound.
