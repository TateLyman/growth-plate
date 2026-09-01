# R134 — both operator challenges answered from the primary sources. **The off-targets are
# NOT specified — by anyone.** VinSpinIn engages **SPIN4 the WEAKEST of the whole family**.
# The SPIN1-lethality argument was wrong and is withdrawn. And the real objection is neither
# of mine: **it is ON-target neoplasia, measured, P=0.047.**

---

## 1. ⭐ "SPECIFY THE OFF-TARGET EFFECTS" — I CANNOT, AND NEITHER CAN ANYONE

That is the answer, and it is the finding. From the Chemical Probes Portal entry for VinSpinIn:

- **No off-target proteins are named. No IC50s. No affinities. No concentration. No cell type.**
- Selectivity was assessed **only against the four SPIN subfamily members** (ITC and DSF)
- The reviewer states: *"both the active and inactive compounds displayed toxicity, **implying off-target
  effects**"* — and that **"toxicity issues relating to this series" persist "despite significant effort"**
- Recommended cellular working range: **0.5–3 µM**
- **No statement regarding in vivo use exists on the entry at all**

> **An unattributed toxicity that survived a medicinal-chemistry campaign and is present in the purpose-built
> INACTIVE control is worse than a named off-target, not better. You cannot design around a liability nobody
> has identified, and you cannot dose-separate it from the on-target effect because the inactive twin has it too.**

## 2. ⭐⭐ AND THE SELECTIVITY DATA IS WORSE THAN "SPIN1-FIRST" — SPIN4 IS **LAST**

Thermal shift (ΔTm) across the family, from the probe's own characterisation:

| target | ΔTm | other |
|---|---|---|
| **SPIN3** | **14.12** | — |
| **SPIN1** | **13.17** | Kd 9.9 nM; IC50 33 nM; **cellular EC50 270 nM** |
| **SPIN2B** | **10.47** | — |
| **SPIN4** | **6.53** | ⛔ **the LOWEST engagement of the four** |

> **VinSpinIn binds SPIN4 the most weakly of every family member it touches. The cellular EC50 (270 nM) is
> measured against SPIN1. To reach meaningful SPIN4 occupancy you must first saturate SPIN3, SPIN1 and
> SPIN2B — while carrying an unidentified toxicity.**

**This is a much sharper objection than the one I gave, and it is the correct one:** not "SPIN1 is
essential," but **"this molecule cannot deliver SPIN4 engagement as its dominant pharmacology, by its own
selectivity data."**

## 3. ⛔ MY SPIN1-LETHALITY ARGUMENT WAS WRONG AND IS WITHDRAWN

The operator is right. **Germline Spin1-null lethality is a developmental phenotype and does not establish
that acute SPIN1 inhibition in an adolescent is harmful** — I made exactly this germline-versus-acute
distinction for SPIN4 one round earlier and failed to apply it to SPIN1. **And SPIN1 inhibitors are being
developed as oncology therapeutics**, which presupposes acute inhibition is tolerable in humans.

**The question that actually mattered was whether SPIN1 inhibition affects longitudinal growth. I asserted
"essential" instead of answering it — and I still cannot answer it: no data on SPIN1 and the growth plate
exists that I can find.** Recorded as unknown, not as an objection.

---

## 4. ⭐⭐⭐ THE REAL OBJECTION IS ON-TARGET, AND IT IS MEASURED

**Lui JC, Hannula I, Rama-Krishnan A, Dong L, Baron J.** *Effects of Spin4 ablation in aging mice*, bioRxiv,
8 Feb 2026 — **the safety study, 18-month endpoint.**

### The growth result confirms the target
| | Spin4^Y/− | WT | P |
|---|---|---|---|
| **body length, males** | **10.80 cm** | **10.28 cm** | **0.002** (**+5.06%**) |
| body weight | 46.39 g | 42.71 g | 0.06 (NS) |
| **lean mass, fat mass, body composition** | — | — | **no significant effect** |
| **bone mineral density and content** | — | — | **no difference** |
| females (het) | 10.31 | 10.01 | 0.128 (NS) |

**+5% body length sustained to 18 months, with no adiposity penalty and no bone-density penalty.** That is a
clean phenotype.

### And then the cancer result
| | tumours | |
|---|---|---|
| **WT males** | **0 / 17** | |
| **Spin4^Y/− males** | **5 / 19** | **P = 0.047**, two-sided Fisher |
| WT females | 3 / 15 | |
| Spin4^+/− females | 3 / 23 | P = 0.66 (NS) |

Male tumours included histiocytic sarcoma and mesenteric lymphoma (common in aged C57BL/6) **plus two
bronchiolo-alveolar carcinomas and one cranial osteoma, which the authors flag as NOT common.**

> **This is an ON-TARGET risk. It cannot be engineered away with better selectivity, a cleaner molecule, or
> an oligonucleotide — it is what losing SPIN4 does.** And it is the class signature: Beckwith-Wiedemann,
> Sotos, Weaver and Tatton-Brown-Rahman all carry raised malignancy risk.

### ⚖️ But the honest counterweights, which the authors themselves raise
1. **n = 19 vs 17, five events versus zero, P = 0.047 — right at the boundary.** One event either way moves it.
2. ⭐ **The human expression data contradicts the simple model.** The authors predicted SPIN4 would be
   *downregulated* in cancers. **Instead SPIN4 expression is ELEVATED in many human cancers (P = 0.0008)** —
   as are EZH2 (P < 0.0001) and DNMT3A (P = 0.0057). They state this was *"contrary to our prediction."*
   **A gene whose expression is UP in tumours is a poor fit for a tumour suppressor whose loss causes them.**
3. **Female heterozygotes showed no increase at all** (P = 0.66).

**Net: a real, statistically significant, on-target neoplasia signal in hemizygous males, from a small study
at the edge of significance, with human expression data pointing the other way.** That is not
disqualifying and it is not dismissible. **It is the actual thing to weigh — and it is a far better
objection than either argument I gave in R133.**

---

## 5. THE MECHANISM, FROM Lui 2023 — AND IT IS EXACTLY THE TERM WE WANT

| zone | finding in Spin4-KO |
|---|---|
| **resting zone** | ⭐ **significant INCREASE in zone height**; increased number of progenitor chondrocytes |
| **proliferative zone** | **no change** in zone height, cells per column, or cell height — **but INCREASED proliferation rate (EdU)** |
| **hypertrophic zone** | **no change** in zone height, cells per column, or **terminal hypertrophic cell height** |
| mechanism | **decreased canonical Wnt signalling in growth plate chondrocytes**, offered as the explanation for the increased resting-zone number |

**SPIN4 loss raises N and the proliferation rate, and leaves h_term completely untouched.** That is a pure
N-and-flux intervention with no borrowing from terminal cell size — the cleanest term profile of anything in
this file.

Also: **ablation of Tudor-like domain 3 ALONE was sufficient to promote growth in vivo and impair histone
binding.** That names the exact sub-domain a selective agent would need to target.

### ⚠ And a dosage warning that generalises across the whole class
From the same paper: in humans, **heterozygous partial** loss of NSD1 (Sotos) and EZH2 (Weaver) **increases**
growth — while in mice, **homozygous complete** loss of Nsd1 or Ezh1/Ezh2 **IMPAIRS** growth.

> **Partial loss grows. Complete loss shortens.** This file already found that for PRC2 (R113) and it
> generalises. **Any SPIN4 knockdown would have a therapeutic window with a floor as well as a ceiling** —
> too much is not more growth, it is less.

---
### Corrections carried by this round
- **"Specify the off-targets" — they are unspecified by anyone.** The toxicity is unattributed, survived a
  med-chem campaign, and is present in the inactive control.
- **The selectivity objection is sharpened and corrected: SPIN4 is VinSpinIn's WEAKEST family target
  (ΔTm 6.53 vs 13–14).** Not merely SPIN1-first — SPIN4-last.
- **My SPIN1-lethality argument is WITHDRAWN** as a germline-versus-acute error, the same one I had just
  warned about for SPIN4. Whether SPIN1 inhibition affects growth is recorded as **unknown**.
- **The real objection is ON-target neoplasia**: 5/19 vs 0/17 in males, P = 0.047, with uncommon tumour
  types — counterweighted by small n and by SPIN4 being *elevated*, not reduced, in human cancers.
- **Target profile confirmed as ideal:** +5.06% length to 18 months, RZ height up, proliferation up,
  **h_term untouched**, no BMD or adiposity penalty.
- **New constraint: partial knockdown only.** Complete loss of this gene class impairs growth.
