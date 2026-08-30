# R116 — NPR3 does not make vosoritide irrelevant, because the limit at bone age 16 is
# neither ligand nor clearance: it is RECEPTOR. Which makes erdafitinib an NPR2 agent,
# and leaves exactly two terms missing — both of them stock, not signalling.

**Operator's question:** *"if we can push NPR3 how we want, vosoritide becomes irrelevant. or am I wrong."*

**Answer: wrong, but for a reason that reframes the whole axis and that vindicates keeping erdafitinib
as the base.** Three independent lines say clearance blockade is multiplicative on substrate, and then
the data says the real ceiling is neither.

---

## 1. THE PLATE MAKES NO CNP — SO CLEARANCE BLOCKADE CANNOT CREATE LIGAND

`the_plate_consumes_cnp_it_does_not_make_it` — GSE9160, laser-capture microdissected, zone-resolved,
HUMAN distal femoral growth plate, two normal children (F 11y10m, M 13y3m), five compartments
including perichondrium:

- **NPPC never exceeds 19.8 in any compartment of either donor** (ten values, 4.4–19.8)
- calibrators chosen before extraction: **PTHLH 308.6, GDF5 603.8**, each with clear zonal peaks
- assay is reading real plate: COL2A1 >100,000, ACAN ~59,000, COL10A1 433 → 72,039 reserve→hypertrophic
- and the plate carries **NPR2 1262, NPR3 979, MME (neprilysin) 1062**

**Replicated independently in this round, in rat:** GSE16981 proliferative zone, Nppc sits at array floor
(3.30–3.91 log2) at every age while Npr2 runs 9.5–10.3 and Prkg2 11.4–11.7.

The plate is a **consumer**, carrying the receptor and **two** independent degradation routes at
transcript levels comparable to the receptor itself.

## 2. AND THE ATLAS ALREADY HAD THE EXPERIMENT THAT PROVES THE DEPENDENCE

- **kanai2017** — osteocrin's skeletal overgrowth is **abolished in CNP-depleted backgrounds**. NPR3
  blockade requires endogenous ligand to work.
- **hakata2024** — sacubitril (neprilysin inhibitor, approved, already given to children) gives
  **dose-dependent skeletal overgrowth in WILD-TYPE mice**, abolished by cartilage-specific NPR-B
  knockout. But it worked **only at 3–4 weeks of age, the window when endogenous CNP and neprilysin
  expression were highest.** The node's own rule: *"an agent that raises a peptide the tissue is not
  making will do nothing."* Magnitude is small and must be quoted as such: **103% and 102% of vehicle
  naso-anal length**, i.e. 2–3%.
- **Human substrate curve:** NT-proCNP is high in infancy, low in early childhood, rises through puberty,
  **peaks at 14.1 y in boys — coincident with peak height velocity — then falls to low adult levels**,
  and correlates directly with height velocity (olney2012, pediatr res 2005). **Bone age 16 is on the
  declining limb, ~2 years past peak.**

**→ NT-proCNP is the first biomarker in this stack that can be measured in an individual to decide,
in advance, whether a clearance-blockade arm will do anything at all.**

---

## 3. ⭐⭐⭐ BUT THE REAL LIMIT IS NEITHER LIGAND NOR CLEARANCE — IT IS RECEPTOR

GSE16981, rat proliferative zone, 3 / 6 / 9 / 12 wk, n=5 per timepoint, GPL1355:

| gene | 3wk | 6wk | 9wk | 12wk | slope/log2age | r |
|---|---|---|---|---|---|---|
| **Npr2** (signalling receptor) | 10.25 | 9.80 | 9.53 | 9.57 | −0.370 | **−0.964** |
| Npr3 (clearance receptor) | 7.36 | 5.88 | 6.35 | 7.01 | −0.232 | −0.305 |
| Mme (neprilysin) | 6.10 | 6.48 | 6.14 | 6.74 | +0.222 | +0.641 |
| Nppc (ligand) | 3.91 | 3.60 | 3.30 | 3.76 | — | *at floor* |
| Ihh | 12.34 | 11.95 | 11.43 | 11.18 | −0.592 | −0.983 |
| Mki67 | 11.64 | 11.60 | 11.55 | 11.69 | +0.002 | +0.028 |

**The ageing plate LOSES THE RECEPTOR. It does not gain clearance.** Npr3 does not rise (r = −0.305);
Mme rises only modestly. Npr2 falls monotonically at **r = −0.964**, second only to Ihh in the whole panel.

**This is the mechanism behind a fact R115 could only report empirically** — that vosoritide's effect
collapses in older children, "no apparent differences between vosoritide and placebo" in the oldest group.
It is not that the drug stops working. It is that there is progressively less receptor for it to work on.

**Both of the operator's CNP strategies are receptor-limited at the target age.** Supplying more ligand
gives more molecules for receptors that are disappearing. Blocking clearance protects ligand for the
same missing receptors. **Neither creates receptor, and NPR3 blockade therefore cannot substitute for
ligand supply — the two are multiplicative on a third term that is falling underneath both.**

### Zonal structure — and it targets the NPR3 decoy precisely
| | RZ | PZ | HZ |
|---|---|---|---|
| Npr2 | 11.08 | 11.03 | 11.19 |
| **Npr3** | 4.94 | 6.55 | **8.80** |
| Mme | 7.68 | 6.64 | 8.38 |

Receptor is **flat** across zones; clearance is **~14-fold concentrated in the hypertrophic zone** —
which is exactly where R115 measured CNP inducing its own Npr3 (+2.58 log2, H zone only), and exactly
where the non-redundant cAMP/PKA arm acts on h_term. **The NPR3 decoy is precisely targeted. It is
just not a substitute for ligand.**

---

## 4. ⭐⭐ WHICH MAKES ERDAFITINIB AN NPR2 AGENT — A MECHANISM THIS PROJECT NEVER ATTRIBUTED TO IT

There is **no known route to transcriptionally upregulate NPR2** anywhere in the literature. The receptor
term is controllable only through **phosphorylation state**:

- **FGF inhibits bone growth BY dephosphorylating NPR2**, via a PPP-family phosphatase (eLife 31343).
  CNP activation of NPR2 *requires* the receptor be phosphorylated on multiple serines and threonines.
- **Therefore blocking FGFR3 preserves NPR2 phosphorylation.** Erdafitinib is not only an FGFR blocker —
  it is an agent on the one CNP-axis term that still has headroom at bone age 16.
- **LB-100** (PP2A/PPP inhibitor) hits the same term by the other route — blocking the phosphatase
  directly rather than the kinase cascade upstream. 1.30× alone, 1.78× BMN-111 alone, **2.06× combined**
  (ex vivo E16.5 femur only; sub-multiplicative — 1.30 × 1.78 = 2.31 expected).

### The ceiling on this term is now a number
**GC-B7E/7E** — all seven phospho-serines/threonines mutated to glutamate to constitutively mimic
phosphorylation, so the receptor **cannot be inactivated by dephosphorylation**. In **genetically normal
mice**, not a dysplasia model:

- **naso-anal length +4.1% (M), +5.3% (F)**
- **femur +4.3% (M), +5.0% (F)**
- explicitly **longer than normal controls**, not merely restored to baseline

**That is a fourth "exceeds normal" entry, it is germline and lifelong, and it caps the phospho-state
term at ~4–5% of final length when maximally engaged from conception.** Caveat the authors state:
it failed to rescue midface hypoplasia, so phospho-state is not sufficient across all bone types.

**→ The operator's instinct that erdafitinib is the key agent is now supported by a mechanism nobody
in this file had identified. It is the base for a better reason than the one it was chosen for.**

---

## 5. THE COMPLETE CNP-AXIS ARCHITECTURE — FOUR NON-OVERLAPPING CONTROL POINTS

| point | agent | obtainable | evidence in WILD-TYPE | limit at BA16 |
|---|---|---|---|---|
| **receptor activity** | **erdafitinib** | yes, approved | BGJ398 +19.6% over WT; TYRA-300 | **the term that survives** |
| receptor activity | LB-100 | clinical-stage (oncology) | 1.30× alone ex vivo | ex vivo only, no in vivo |
| **ligand supply** | vosoritide / navepegritide | yes, approved | SAP-CNP-Tg exceeds normal | substrate declining post-14.1y |
| clearance — receptor | osteocrin-class NPR3 decoy | research-grade only | OSTN-Tg dose-dependent overgrowth | needs substrate; ANP/BNP → hypotension |
| clearance — enzyme | **sacubitril** | **yes, approved, paediatric use** | **+2–3% naso-anal, WT mice, dose-dependent** | window-dependent (hakata2024) |

**Genetic ceiling of the whole axis, human:** NPR3 biallelic LOF **+3.03 / +3.43 / +4.41 / +4.76 SDS**,
velocity **+6.17 SD**, bone-age neutral, above midparental target. NPR2 GOF = Miura overgrowth.
**These people had complete loss from conception, through childhood, when circulating CNP is high.**
That is why their numbers do not transfer to a near-closure subject.

**CV ceiling, unmeasured:** NPR3 also clears ANP/BNP; boudin2018 patients had aortic dilatation and joint
hypermobility; **not one osteocrin study measured an aortic dimension.**

---

## 6. WHAT IS MISSING FOR 6'5", STATED EXACTLY

`height = N × A × h_term`, and every agent above is a **signalling** agent. Two terms are missing and
**both are stock problems, not signalling problems**:

1. **N — the resting-zone stem pool.** No agent anywhere. A and h_term are multiplicative on it, so
   every high-value lever is worth zero once it is spent. Only documented creation of N in a human:
   **NPR3-LOF extra epiphyses** (pseudoepiphysis at MC2 base, distal MT1, distal proximal phalanges 2–5)
   via **incomplete elimination of PTHrP⁺ cells** — the same cells measured at 0.72% for n₀ in R112 —
   and **absent from every mouse model**, so the human phenotype exceeds the mouse.
2. **NPR2 receptor density.** Falls at **r = −0.964** with age. **No transcriptional upregulator exists
   in the literature.** Only phospho-state is controllable, and that term caps at ~4–5%.

**THE UNIFYING STATEMENT OF THIS ROUND: every remaining gap is a stock problem, and every agent we
have is a signalling agent.** That is why k ≈ 7× is unreachable and the stack tops out near 2.6×.
Signalling agents multiply a stock; they do not create one.

---

## 7. WHAT THIS ROUND CHANGES IN THE STACK

Nothing is removed. Two additions are now justified on measured grounds, and one is downgraded:

- **erdafitinib** — promoted from "FGFR blocker" to **the NPR2-activity agent**, the one CNP-axis term
  with headroom at BA 16. Base.
- **anastrozole** — unchanged. Fixed-budget regime. Base.
- **vosoritide / navepegritide** — **NOT redundant with an NPR3 decoy** (it supplies what the plate
  cannot make) and **not redundant with erda** (R115, ≤2.4% shared variance). Keep. But expect its
  value to scale with measured NT-proCNP.
- **sacubitril** — **new, and the most obtainable addition in the file**: approved, paediatric use,
  dose-dependent overgrowth in wild-type mice, clean NPR-B epistasis. Blocks the *other* half of
  clearance (MME 1062 vs NPR3 979 in human plate), which no other agent in the stack touches.
- **LB-100** — watchlist. Right term, ex vivo only.
- **NPR3 decoy** — right target, right zone, but research-grade and substrate-dependent.

---

### Corrections carried by this round
- **The operator's NPR3-replaces-vosoritide hypothesis is refuted** on three independent lines
  (no NPPC in plate; osteocrin abolished in CNP-null; sacubitril window-dependent) — and then
  superseded, because the binding constraint is neither.
- **R115's "N is the only term left" is amended.** There are **two** stock terms missing: N *and*
  NPR2 receptor density.

Code: `frontier/analysis/redundancy/clear.py`.
