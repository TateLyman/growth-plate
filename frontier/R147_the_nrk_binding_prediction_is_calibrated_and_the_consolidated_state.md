# F-R147 — **THE NRK PREDICTION, CALIBRATED AGAINST MEASURED CROSS-REACTIVITY: NRK'S POCKET IS 77.4% IDENTICAL TO THE DRUGGED TRIO — *MORE* THAN MAP4K1, WHICH CARRIES OVER 92–94%. BEST ESTIMATE ~70%, WITH ONE REAL DEFLATOR: ALL SEVEN DIFFERENCES ARE NRK-UNIQUE.**

**And a bug I caught and killed before reporting it.**

---

## => ⛔ FIRST, THE BUG — BECAUSE THE FIRST ANSWER WAS WRONG

My initial attempt located the catalytic motifs by regex **independently in each sequence** and then
compared them **by string index**. It produced "16 of 18 pocket positions differ, 0/16 conservative" —
which would have killed the whole arm.

**It was an artefact.** NRK's motifs are canonical but *variant*:

| motif | MAP4K4 | **NRK** | why the regex missed it |
|---|---|---|---|
| glycine-rich loop | `GNGTYG**QV**` | `GLGTYG**RI**` | pattern required `...V`; NRK has **I** |
| β3 lysine | `LA**AIK**V` | `FTA**VK**V` | pattern required `xxIK`; NRK has **AVK** |

**One conservative substitution each.** With both anchors missing, the pocket set collapsed to the
HRD/DFG block only — and the comparison lined **NRK's catalytic loop up against everyone else's
P-loop.** Garbage in, garbage out.

> **Fixed by defining the pocket ONCE in a reference kinase with inhibitor co-crystals (MAP4K4) and
> mapping those positions into every other kinase THROUGH A PAIRWISE ALIGNMENT.** Code:
> `analysis/redundancy/predict2.py` (the broken `predict.py` is retained so the error is visible).

---

## => ⭐ STEP 1 — THE ATP POCKET, 31 POSITIONS, ALL ON THE SAME REFERENCE COLUMNS

P-loop (8) + β2 floor (2) + β3 Ala/Lys (2) + αC region (2) + gatekeeper−2…hinge+5 (8) + catalytic
loop (5) + DFG−1…DFG+2 (4).

```
MAP4K4   GNGTYGQVGHAKNKWLVMEFCGHRDIGVDFG
TNIK     GNGTYGQVGHAKNKWLVMEFCGHRDIGVDFG
MINK1    GNGTYGQVGHAKNKWLVMEFCGHRDIGVDFG
NRK      GLGTYGRIGHTKNKWMVMELCAHRDIGVDFG      <- 7 differences
MAP4K1   GGGTYGEVADVKIKWICMEFCGHRDIGADFG
MAP4K2   GAGTYGDVADAKTEWICMEFCGHRDIGADFG
MAP4K3   GSGTYGDVANAKIKWICMEFCGHRDIGADFG
MAP4K5   GSGTYGDVANAKFEWICMEYCGHRDIGADFG
OXSR1    GSGATAVVACVKQQWLVMKLLSHRDVAADFG
STK39    -----AALPQVKQQWLVMKLLSHRDLAADFG
```

⭐ **The catalytic core is invariant across NRK and the drugged trio: `HRDIGVDFG` — identical.**
MAP4K1/2/3/5 differ even there (`HRDIGADFG`), and they still cross-react 92–94%.

---

## => ⭐⭐⭐ STEP 2 — CALIBRATION AGAINST **MEASURED** CROSS-REACTIVITY (R146)

The five pairs whose carry-over I measured empirically from ChEMBL, now with their pocket identity:

| pair | **pocket identity** | pocket similarity | **MEASURED carry-over** |
|---|---|---|---|
| MAP4K4 / MINK1 | **100.0%** | 100.0% | **68%** (n=260) |
| TNIK / MINK1 | **100.0%** | 100.0% | **87%** (n=38) |
| MAP4K4 / TNIK | **100.0%** | 100.0% | **89%** (n=72) |
| ⭐ **MAP4K4 / MAP4K1** | ⭐ **71.0%** | 77.4% | ⭐ **92%** (n=37) |
| ⭐ **TNIK / MAP4K1** | ⭐ **71.0%** | 77.4% | ⭐ **94%** (n=33) |

> ### **THE LOWEST POCKET IDENTITY IN THE CALIBRATION SET IS 71.0% — AND IT CARRIES OVER 92–94% OF THE TIME. Across the whole 71–100% range carry-over is uniformly 68–94%, with NO evidence that lower identity reduces it. If anything the relationship is inverted, which says identity is not the rate-limiting variable in this range.**

---

## => ⭐⭐⭐ STEP 3 — WHERE NRK SITS

| NRK vs | **pocket identity** | pocket similarity | |
|---|---|---|---|
| ⭐ **TNIK** | ⭐ **77.4%** | **87.1%** | **ABOVE the 71% calibration floor** |
| ⭐ **MINK1** | ⭐ **77.4%** | **87.1%** | **ABOVE the floor** |
| ⭐ **MAP4K4** | ⭐ **77.4%** | **87.1%** | **ABOVE the floor** |
| MAP4K3 | 61.3% | 71.0% | below |
| MAP4K1 | 61.3% | 67.7% | below |
| MAP4K5 / MAP4K2 | 58.1% | 67.7–71.0% | below |
| STK39 / OXSR1 | 41.9–42.3% | 61.3–65.4% | below |

> ### ⭐⭐ **NRK'S POCKET IS *MORE* SIMILAR TO THE THREE DRUGGED KINASES (77.4%) THAN MAP4K1 IS (71.0%) — AND MAP4K1 IS CROSS-INHIBITED 92–94% OF THE TIME.**
> **This is an INTERPOLATION INSIDE the calibrated range, not an extrapolation beyond it. That is as
> close to validation as sequence can get without an assay.**

### AND THE GATEKEEPER IS CONFIRMED — WITH A CORRECTION TO R145

```
MAP4K4   ... Q L W L V M E F C G A ...      hinge = E-F-C  ->  gatekeeper = M
NRK      ... Q L W M V M E L C A G ...      hinge = E-L-C  ->  gatekeeper = M
```

| | MAP4K4 | NRK |
|---|---|---|
| gatekeeper residue | **Met** | ⭐ **Met — identical** |
| **protein number** | ⚠ **105** | **129** |

⚠ **R145 said "Met104." It is Met105 — off by one, corrected.** NRK's is Met129 (its kinase domain
carries a ~24-residue insertion relative to MAP4K4). **The substance of R145's claim stands and is now
verified rather than recalled: the gatekeeper Met is conserved, as are the flanking V (gk−1), E (gk+1)
and C (gk+3). Only gk+2 differs (F→L), the most solvent-exposed and most tolerant position in the hinge.**

---

## => ⛔ STEP 4 — THE HONEST DEFLATOR: **ALL SEVEN DIFFERENCES ARE NRK-UNIQUE**

```
TNIK/MAP4K4/MINK1   GNGTYGQVGHAKNKWLVMEFCGHRDIGVDFG
NRK                 GLGTYGRIGHTKNKWMVMELCAHRDIGVDFG
                     ^    ^^  ^    ^   ^ ^
```

**N→L@2 · Q→R@7 · V→I@8 · A→T@11 · L→M@16 · F→L@20 · G→A@22.  3 of 7 conservative.**

**Checked against the whole family — every one of the seven is a residue no other member has:**

| pos | element | trio | MAP4K1/2/3/5 | **NRK** | |
|---|---|---|---|---|---|
| 2 | P-loop | N | G/A/S | **L** | unique |
| ⭐ **7** | **P-loop** | **Q** | **E/D (acidic)** | ⭐ **R (basic)** | ⭐ **CHARGE REVERSAL vs half the family** |
| 8 | P-loop | V | V | **I** | unique, ultra-conservative |
| 11 | β3/αC | A | V/A/N | **T** | unique |
| 16 | gk−1 | L | I | **M** | unique |
| 20 | hinge gk+2 | F | F/Y | **L** | unique |
| 22 | hinge gk+4 | G | G | **A** | unique |

> ### ⛔ **NRK IS THE FAMILY OUTLIER. Seven pocket positions that no other GCK member carries — and the calibration set contains NO example of an outlier like that. A compound series optimised against MAP4K4/TNIK/MINK1 could systematically miss NRK at exactly these positions, and the calibration cannot see that failure mode because it never occurred in the pairs I measured.**
> ⭐ **The single most consequential one is Q7R: the glycine-rich loop caps the ATP site, and NRK puts an ARGININE where the trio has glutamine and MAP4K1/2/3/5 have aspartate or glutamate. That is a full charge reversal relative to half the family, in the loop that closes over an inhibitor. If NRK is missed, that is where.**
> **Three of the seven sit in the P-loop and three in the gatekeeper/hinge block — precisely the two
> regions med-chemists exploit to build selectivity.**

---

## => THE ANSWER, WITH A NUMBER AND ITS ERROR BARS

| | |
|---|---|
| **family base rate of cross-reactivity** | **68–94%** (measured, five pairs, testing-bias controlled) |
| **NRK's pocket identity to the drugged trio** | **77.4%**, above the 71% floor that still yields 92–94% |
| **catalytic core** | `HRDIGVDFG` **identical** to the trio |
| **gatekeeper** | **Met, conserved**, with conserved V/E/C flanks |
| ⛔ **deflator** | **7 NRK-unique pocket residues, 3 in the P-loop and 3 in the hinge block, including a charge reversal at Q7R** |
| ⭐ **BEST ESTIMATE** | ⭐ **~70% that a pan-GCK-IV inhibitor engages NRK at comparable potency** |

**Read that as: more likely than not, and by a clear margin — but not a result. The 30% is not noise;
it is concentrated in seven specific residues that the calibration set could not test.**

⚠ **What this cannot do:** kinase selectivity genuinely can turn on one residue. The ChEMBL carry-over
base rate is also enriched for compounds *designed* as pan-family inhibitors, which inflates it.
**One assay replaces all of this.**

---

## => ⭐ AND IT SHARPENS THE EXPERIMENT INTO A DISCRIMINATING ONE

The panel is no longer "see if anything binds." **The seven positions predict *which* compounds fail:**

| arm | what it tests |
|---|---|
| **rentosertib (INS018_055)** | ⭐ the one with human Phase 1/2a data — the outcome that matters most |
| **PF-06260933, GNE-495** | MAP4K4-optimised: **most likely to be defeated by Q7R and the hinge block** |
| **NCB-0846** | TNIK-optimised |
| **bosutinib, lestaurtinib, dovitinib** | promiscuous scaffolds — ⭐ **least shaped by the trio's pocket, so MOST likely to tolerate NRK's seven differences** |

> ⭐ **PREDICTION ON THE RECORD, BEFORE THE ASSAY: the promiscuous scaffolds (bosutinib class) are more
> likely to hit NRK than the selective GCK-IV tool compounds are, because selectivity optimisation
> shapes a molecule to the trio's pocket and NRK is the outlier. If that ordering comes back inverted,
> this whole homology model is wrong.**

---

## => THE SIDING — WHERE EVERYTHING ACTUALLY STANDS

**IN THE STACK, on real endpoints:** erdafitinib · anastrozole ≥2 yr · GH **0.24–0.37 mg/kg/wk** ·
CNP analogue · axial decompression (not a drug).

| arm | state |
|---|---|
| ⭐ **SPIN4 / Wnt** — the mechanism | ⭐ **VALIDATED.** Supplies **38%** of chondrocyte Wnt output (Lui Fig 6C); loss → **reduced recruitment**, RZ expansion, **h_term untouched**, **+5.06%** length, **bone-age neutral** — the only member of its class that is |
| ⛔ selamectin | ⭐ right potency (0.103 µM), dose converges at **0.15 mg/kg**, **90× margin in P-gp-null animals**, all seven safety studies clean — ⛔ **no human has ever taken it** |
| ⛔ moxidectin | ⛔ **DEAD systemically** — 3.5–7% vs a 38–45% target, and the feedback rescue measured at **1.02×** |
| ⛔ verteporfin | ⛔ **REFUTED** — N-negative in the Prrx1+ root compartment |
| ⭐ **NRK** — the new target | ⭐ **+3.48 cm/allele, 1.45M exomes, and the ONLY gene of the 17 with human nulls (34 of them)**; ⛔ Tdark, zero ligands |
| ⭐ **NRK druggability** | ⭐ **this round: 77.4% pocket identity, conserved Met gatekeeper, ~70% prior** — ⛔ never assayed |
| ⚠ rentosertib | ⭐ oral, **Phase 1+2a in humans**, primary target on-mechanism (TNIK→↓Wnt) — ⚠ **optimised for POTENT Wnt blockade = the ICAT regime that shortens bone** |
| ⭐ metformin | ⭐ **ΔBA/ΔCA 1.16→0.96, height per bone-age year +32%** — the only agent that *relaxes* the GH ceiling; ⚠ wrong population, possible anastrozole redundancy |
| ⛔ TET1 | +7.74 cm, enzyme class — ⛔ only a contested pan-TET tool compound |

**THE THREE EXPERIMENTS, IN COST ORDER:**
1. ⭐ **One kinase assay** — NRK vs the 7-compound panel. *Cheapest, most decisive, and now makes a falsifiable ordering prediction.*
2. **The explant** — selamectin 0.02/0.07/0.2/0.6 µM, bryostatin control, endpoint **bone length** + Axin2 + Sfrp5⁺ RZ count + h_term.
3. **Spin4 × Cxxc5 double** — tests R139's orthogonality claim, required before any Wnt agent joins a stack containing an AI.

**STILL OUTSTANDING FROM THE OPERATOR:** erda hand/wrist films · sitting height vs subischial leg
length + ring-apophysis staging · NT-proCNP · **liver fat** (decides the metformin arm).

---

## CORRECTIONS

- ⛔ **A BUG WAS CAUGHT AND KILLED BEFORE REPORTING.** Motif-by-regex + compare-by-index misaligned
  NRK's catalytic loop against the others' P-loop and produced a false "16/18 differ, 0 conservative."
  **NRK's motifs are canonical but variant** (`GLGTYG**RI**`, `TA**VK**`), which broke the patterns.
  Rebuilt alignment-based; the broken script is kept so the error stays visible.
- ⭐⭐ **CALIBRATED PREDICTION:** pocket identity **77.4%** to MAP4K4/TNIK/MINK1, **above the 71% floor
  at which MAP4K1 still carries over 92–94%.** Interpolation inside the measured range.
- ⭐ **Catalytic core `HRDIGVDFG` is IDENTICAL** between NRK and the drugged trio; MAP4K1/2/3/5 differ
  even there and still cross-react.
- ⚠ **R145's "Met104" CORRECTED to Met105** (MAP4K4); NRK's gatekeeper is **Met129**. **The substance —
  a conserved Met gatekeeper with conserved V/E/C flanks — is now verified rather than recalled.**
- ⛔ **HONEST DEFLATOR ADDED: all seven pocket differences are NRK-UNIQUE within the family**, 3 in the
  P-loop and 3 in the hinge block, **including a charge reversal (Q→R) in the glycine-rich loop.** The
  calibration set contains no outlier like this and cannot see that failure mode.
- ⭐ **BEST ESTIMATE ~70%**, with the residual risk concentrated in seven named residues rather than
  spread as noise.
- ⭐ **A FALSIFIABLE ORDERING PUT ON THE RECORD:** promiscuous scaffolds should hit NRK *more* readily
  than the selective GCK-IV tool compounds. **Inverted result falsifies the model.**
