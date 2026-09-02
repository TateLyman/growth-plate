# R115 — the redundancy gap is closed with data: erda and the CNP arm are ~98% independent,
# CNP induces its own clearance receptor, and the only term left standing is N

**Target for this round (operator):** 180.3 cm → 195.6 cm (5'11" → 6'5") at bone age 16.
Chosen deliberately: the near-closure population because young plates are easy, and a height
delta above the observed ceiling. Base stack is **erdafitinib + anastrozole** and is NOT to be
replaced — only added to.

---

## 0. The framework this round runs on (R360 + arm3, read together for the first time)

R360 already holds the identity for the fixed-budget regime:

> **adult height from a fixed pool = N × A × h_term**, and the rate–yield law **A ∝ throughput^−0.150**

and states that **anastrozole is precisely what moves the subject from the deadline regime into the
fixed-budget regime**, where "throughput is worth nothing and yield is everything." Its closing line:
**nothing in the stack raises A.**

`arm3_pool_ceiling_is_imposed_not_intrinsic` states its own target as: *"decouple the program's
progression from growth output — run the counter slowly while the plate keeps producing. Nothing
does this."*

**These are the same target in two vocabularies, and the atlas has never connected them.** The counter
tracks resting-zone divisions (nilsson2005: methylation loss is a property of slow RZ replication in
its niche, not of division per se). So A and h_term are *counter-free*: raising them buys length per
stem cell spent, which is exactly "the plate keeps producing while the counter runs slowly."

This is not speculative — it is already demonstrated once. dauber2026: vosoritide, velocity +4.0 SD,
**bone-age-to-chronological-age ratio unmoved**. Length without counter advance.

---

## 1. PTH1R — the atlas's own best A candidate — stays dead

`the_yield_candidate_intermittent_pth1r_agonism` ranked intermittent PTH1R agonism first for yield on
good grounds (abaloparatide is a PTHrP(1-34) analogue; PTHrP-Ihh sets proliferative column length;
column length *is* amplification; ogawa2002 raised growth rate in a normal animal).

R194 killed it and the kill holds: FDA NDA 21-318 terminal table, femur length **35 / 35 / 35 / 35 /
35 / 35 / 35 / 35 mm** across eight arms at 26 months, including continuous dosing from 2 months.
Every other row in that table is starred somewhere. Rate effect on an unchanged total — GH's class.

---

## 2. THE REDUNDANCY GAP, CLOSED WITH DATA

`is_the_cnp_arm_redundant_with_fgfr3_blockade` defines the gap: *"does raising CNP signalling add bone
length on top of near-complete FGFR blockade, in a pathway-intact animal? … **NOBODY HAS RUN IT IN ANY
SPECIES**."* R114 guessed redundant. **That guess was wrong.**

Two GEO series, **both on GPL1261**, so this is probe-level with no annotation step:

- **GSE4481** — CD1 mouse E15.5 tibiae, 3 biological replicates, BSA vs CNP, dissected into
  **R/P (resting+proliferative), H (hypertrophic), M (mineralised)**
- **GSE145821** — *Fgfr3^Y367C/+* vs control littermate, femoral head, 7/14/21/28 d, n=3 per cell.
  Contrast taken as **WT − mutant**, i.e. the direction FGFR3 blockade moves the tissue.

18,183 expressed probes.

### Positive controls first (without these the result is meaningless)

| | wk1 | wk2 | wk3 | wk4 |
|---|---|---|---|---|
| **FGFR3 axis vs itself** | — | +0.466 | +0.181 | +0.216 |
| wk3 vs wk4 | | | | **+0.861** |

Mean within-axis \|r\| for the FGFR3-blockade axis = **0.461**. It is a strongly reproducible axis.
CNP axis within-itself (across zones) = 0.170 — weaker, as expected when the three zones are
different tissues.

### The cross-correlation

| CNP zone | wk1 | wk2 | wk3 | wk4 |
|---|---|---|---|---|
| R/P | +0.060 | −0.058 | −0.155 | −0.146 |
| H | +0.092 | +0.059 | +0.102 | +0.031 |
| M | +0.129 | +0.144 | +0.095 | +0.086 |

**Max \|r\| = 0.155. Shared variance ≤ 2.4%.**

The FGFR3 axis correlates with *itself* at 0.46–0.86. If CNP were acting through FGFR3's
transcriptional output it would appear at that magnitude. It appears at a third of it.

**→ The CNP arm is not inside erdafitinib. The two are additive.** By the same criterion this file
used for oestrogen × FGFR3 (r=+0.127, ~1.6% shared → additive), this is an additive pair.
The operator was right and R114 is retracted.

---

## 3. WHAT EACH AGENT ACTUALLY COVERS, MEASURED

Marker-panel z-scores against the genome-wide distribution, and the per-gene table:

| gene | FGFR3-blockade wk3 | wk4 | CNP R/P | CNP H |
|---|---|---|---|---|
| Col10a1 | +2.39 | **+3.10** | −0.52 | −0.20 |
| Col2a1 | +0.98 | **+2.36** | −0.24 | −0.14 |
| Sp7 | +0.74 | **+2.20** | −0.27 | −0.90 |
| Alpl | +0.89 | **+1.82** | −0.20 | −0.95 |
| Mest | +1.68 | **+3.44** | −0.23 | −1.14 |
| Mki67 | −0.84 | **−0.87** | +0.38 | −0.18 |
| Mmp9 | −0.01 | −0.11 | −0.57 | **−1.73** |
| **Npr3** | +0.33 | +0.25 | −0.20 | **+2.58** |

**Erdafitinib's direction is h_term + matrix, and it is NOT a proliferation agent.** Col10a1 +3.10
and Col2a1 +2.36 with Sp7 +2.20 and Alpl +1.82, while Mki67 goes **down** (−0.87). Those are the two
largest terms in Wilsman's closed partition (59% hypertrophy + 32% matrix in a fast plate; 44% + 49%
in a slow one — and a subject at bone age 16 has slow plates, where matrix is the larger term).

**The CNP arm suppresses hypertrophic commitment in R/P and the closure/vascular program in H**
(h_term panel −4.25 in R/P; closure/vascular −4.78 in H; Mmp9 −1.73). Delaying commitment = longer
residence in the proliferative compartment = **A**.

### CORRECTION made inside this round
An earlier panel score read "FGFR3 blockade raises N" at +2.47/+2.54. That was inflated by the
**Fgfr3 probe itself**, which is circular in an *Fgfr3*-mutant contrast. Dropping it and Sox9 the
panel still reads +2.30, but gene-level the signal is **mixed and unresolved**: Grem1 +1.45 up,
**Foxa2 −1.46 down**, Nt5e −0.33 down, and **Pthlh has no working probe on this array**. The h_term
result is robust across genes; the N result is not. **Erda's evidence is for h_term and matrix, not N.**

---

## 4. ⭐ CNP INDUCES ITS OWN CLEARANCE RECEPTOR — MEASURED, AND IT NAMES AGENT 4

**Npr3 +2.58 (log2, ≈6-fold) in the hypertrophic zone under CNP.** Zone-specific: −0.20 in R/P, +0.17 in M.

A CNP analogue **self-limits**: it drives up the receptor that internalises and degrades it, in the
exact zone where its non-redundant cAMP/PKA arm acts. This is the measured mechanism for why
**kanai2017's CNP × OSTN double transgenic gains additional bone length over elevated CNP alone —
the only demonstrated additivity on bone length for any pair of agents in this atlas.**

Osteocrin occupies NPR3 without agonising it (smith2022 uses it as an antagonist tool compound;
it reverses cANF(4-23)-induced cAMP fall exactly as M372049 does). It removes the brake this round
just measured.

---

## 5. THE HUMAN GENETICS ON THIS AXIS ARE THE STRONGEST "EXCEEDS NORMAL" EVIDENCE IN THE FILE

- **NPR3 biallelic LOF:** height **+3.03, +3.43, +4.41, +4.76 SDS**; height velocity **+6.17 SD**
  (8.9 cm/yr) — boudin2018
- **Lauffer 2022 proband:** 172.1 cm at 10 → **195.6 cm at 13.5** → **205.1 cm at 14.7**. +33 cm in
  4.7 yr. Midparental target range −0.8 to +2.4 SDS; reached **+3.93**, above his own genetic target.
  **Bone age equal to calendar age at 13.**
- **NPR2 heterozygous GOF:** epiphyseal chondrodysplasia Miura type — tall stature, arachnodactyly,
  macrodactyly of the halluces, from excess cGMP
- **Npr3-null mouse:** three independent alleles, all skeletal overgrowth (PNAS 1999)
- **OSTN-Tg mouse:** dose-dependent skeletal overgrowth, abolished in CNP-null or NPR-C-null backgrounds

**Bone-age-neutral + supranormal velocity + final height above midparental target = YIELD, not rate.**
This is the property GH and PTH1R both fail.

### And the one instance of N being CREATED in a human
NPR3-LOF patients carry **extra epiphyses**: a pseudoepiphysis at the base of MC2, an extra epiphysis
at the distal 1st metatarsal, and at the distal ends of proximal phalanges 2–5. New ossification
centres at the **normally non-growing end** of tubular bones. The proposed mechanism is **incomplete
elimination of PTHrP from epiphyseal chondrocytes** — and PTHrP⁺ cells are exactly the resting-zone
stem cells measured at 0.72% for n₀ in R112. A separate case report is titled *"Complete
Pseudoepiphyses With Associated **Enhanced Growth** in Hands and Feet."*

**boudin2018 notes these extra epiphyses have never been reported in the mouse models.** The human
phenotype exceeds the mouse — which inverts the usual translation risk on this arm.

---

## 6. THE ARITHMETIC FOR THE TARGET, AND WHERE IT BREAKS

Bayley–Pinneau, male, skeletal age 16.0 = 98.8% of adult height → **2.19 cm remaining** at 180.3 cm.
Target needs **+15.3 cm**.

| | k on (A × h_term) | result |
|---|---|---|
| **required** | **6.99×** | 195.6 cm |
| CNP analogue alone (meta, +1.24 cm/52wk) | 1.25× | 183.0 cm |
| NPR3-LOF human velocity (8.9 vs ~5.5) | 1.62× | 183.8 cm |
| LB-100 + BMN-111 (ex vivo growth ratio) | 2.06× | 184.8 cm |
| optimistic full stack, log-additive | 2.60× | **186.0 cm** (6'1.2") |

At SA 16.5 the required k is 9.34×; at SA 17.0 it is 12.04×.

**Nothing in the corpus reaches k ≈ 7 on a fixed N.** The stack gets roughly a third of the way.
The whole remaining gap is **N** — and A and h_term are *multiplicative* on N, so every high-value
lever is worth zero when N is spent. This is visible in the drug's own clinical record: vosoritide's
effect **collapses in older children**, "no apparent differences between vosoritide and placebo" in
the oldest group. That is not a failure of the axis. It is N going to zero underneath it.

---

## 7. THE STACK (adding to the base, replacing nothing)

1. **Erdafitinib** — h_term + matrix (the two largest Wilsman terms) + the closure arm. Base. Keep.
2. **Anastrozole** — moves the subject into the fixed-budget regime where yield is everything;
   defers the terminal event. Base. Keep.
3. **CNP-axis agent** (vosoritide / navepegritide) — **proven this round to be ≤2.4% redundant with
   erda**; supplies A and the closure/vascular brake; bone-age-sparing.
4. **NPR3 decoy, osteocrin-class** — removes the **Npr3 +2.58** self-limiting feedback measured in §4;
   the only demonstrated additive pair on bone length in the file (kanai2017).
5. *(watchlist)* **LB-100** — PP2A/PPP inhibitor, sustains NPR2 phosphorylation against FGF-driven
   dephosphorylation. 1.30× alone, 1.78× BMN-111 alone, **2.06× combined** — but ex vivo E16.5 femur
   culture only, no in vivo, and the combination is sub-multiplicative (1.30 × 1.78 = 2.31 expected).

**Cardiovascular ceiling on arms 3–4:** NPR3 also clears ANP/BNP, and the boudin2018 patients had
aortic dilatation and joint hypermobility. The atlas notes **not one** osteocrin study measured an
aortic dimension. That is the dose-limiting endpoint and it is unmeasured.

---

## 8. WHAT THIS ROUND LEAVES

**N is now the only term in the identity with no agent, and it is the entire remaining gap to the
target.** Every other term is covered, and covered additively.

The single lead: **NPR3 loss creates new growth plates in humans via retained PTHrP⁺ cells, and does
not do so in mice.** That is the only documented instance of N being created rather than transplanted,
it sits on the axis this stack is already on, and nobody has asked whether it can be induced
pharmacologically rather than genetically.

That is the next round.

---
### Corrections carried by this round
- **R114 retracted** — "vosoritide is redundant with FGFR3i" is refuted at ≤2.4% shared variance.
- **In-round correction** — the "erda raises N" panel reading was circular via the Fgfr3 probe;
  erda's evidence is h_term + matrix, and N is unresolved on this data.
- **k.py error** — an earlier stack multiplier was computed without erdafitinib in it.
