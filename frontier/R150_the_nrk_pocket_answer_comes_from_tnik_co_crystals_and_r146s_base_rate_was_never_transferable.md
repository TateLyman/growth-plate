# F-R150 — **NO EXPERIMENT NEEDED FOR THIS PART. NRK HAS ZERO STRUCTURES BUT TNIK HAS FOUR INHIBITOR CO-CRYSTALS, AND THEY ANSWER THE QUESTION: NRK PRESERVES EVERY POSITION WHERE THE LIGAND IS TIGHT AND DIFFERS ONLY WHERE THERE IS ROOM. TWO CORRECTIONS TO MYSELF — R146's 68–94% BASE RATE WAS NEVER TRANSFERABLE, AND R147's SEVEN DIFFERENCES MOSTLY AREN'T WHERE THE LIGAND IS.**

**You said you can't run an experiment. Understood — so I stopped asking for one and derived what I
could from public structures instead. Here is how far that gets, honestly, including the part it
cannot reach.**

---

## => PART 1 — WHAT THE PATENT ACTUALLY CONTAINS, INCLUDING WHAT IT DOESN'T

**Your numbers were exactly right.** I read the figure image rather than trusting the OCR (which had
misread CC-1804 as 5.32) and confirm **FIG. 1F, sheet 14**:

| kinase | hit count | CC-1804 | CC-1817 | CC-1294 |
|---|---|---|---|---|
| ⭐ **NRK** | 2 | **1.51** | **2.85** | 1.09 |

⚠ **One correction to how the row above it reads:** the neighbouring entry is **NIM1K**, a separate
kinase — **not MINK1.** I checked.

### ⛔ AND THE STRUCTURAL PROBLEM WITH THIS PANEL: THE DRUGGED TRIO ISN'T IN IT

I went through the full 595-entity list. **MAP4K4, TNIK and MINK1 are all ABSENT** — FIG. 1E jumps
straight from **MAP4K3 → MAP4K5**. So the comparison I wanted (NRK vs the three kinases it is supposed
to resemble, same assay, same day) **cannot be made inside this patent.**

**What can be made is the next-best thing** — NRK against the four MAP4Ks that *are* present:

| kinase | CC-1804 | CC-1817 | CC-1294 | **sum** | rank |
|---|---|---|---|---|---|
| MAP4K2 | 7.03 | 10.89 | 1.97 | **19.89** | 1 |
| MAP4K3 | 6.84 | 3.45 | 1.58 | **11.87** | 2 |
| MAP4K1 | 3.94 | 2.07 | 2.58 | **8.59** | 3 |
| MAP4K5 | 2.82 | 1.74 | 1.18 | **5.74** | 4 |
| ⛔ **NRK** | 1.51 | 2.85 | 1.09 | ⛔ **5.45** | ⛔ **5 of 5 — last** |

> ⛔ **NRK is the weakest binder of the five.** That is the first hard number in this programme pushing
> the NRK estimate **DOWN**, and I am reporting it as such.

⚠ **Caveat, stated properly:** NanoBRET fold-change across *different* kinase fusions is confounded by
fusion geometry, expression level and donor–acceptor distance. Promega's own framing treats it as a
hit-call, not an affinity. **So this is suggestive, not quantitative.** It is enough to say NRK is not a
strong binder of this chemotype; it is not enough to put a number on it.

---

## => PART 2 — ⭐⭐⭐ THE MOVE THAT ACTUALLY WORKS: **USE TNIK's CO-CRYSTALS**

NRK has **zero PDB structures** (I queried RCSB by accession Q7Z2Y5 — nothing; it is Tdark all the way
down). **TNIK has twelve, and four of them have an ATP-site inhibitor bound:**

| PDB | ligand | what it is |
|---|---|---|
| ⭐ **5D7A** | 58C | ⭐ **NCB-0846 — already in my seven-compound panel** |
| 6RA7 | JWK | "compound 9", **1.2 Å** |
| 5AX9 | 4KT | TNIK inhibitor |
| 8ZML | A1D8H | ⭐ 2025, *"Bis-imidazolecarboxamide… **selective** TNIK inhibitors for **idiopathic pulmonary fibrosis**"* |

**The insight R147 missed:** an ATP-competitive inhibitor does not care about "pocket identity." It
cares about **the residues it actually touches.** So I took every residue within 4.5 Å of each ligand's
heavy atoms, kept the **23 positions contacted in ≥2 of the 4 complexes**, and mapped them into NRK
through the alignment. **Numbering validated: 29/29 contact residues match UniProt Q9UKE5 at their index.**

```
core contact set (TNIK numbering):
V31 G32 N33 G34 V39 A52 K54 E69 A83 M105 E106 F107 C108 G109 A110 G111 S112 D115 Q157 N158 L160 V170 D171
```

---

## => ⛔⛔ CORRECTION 1 — **R146's 68–94% BASE RATE WAS MEASURED ON KINASES WITH IDENTICAL POCKETS, AND WAS NEVER TRANSFERABLE TO NRK**

| TNIK vs | contact positions identical | R146 measured carry-over |
|---|---|---|
| **MAP4K4** | ⭐ **23/23 — 100%** | 89% |
| **MINK1** | ⭐ **23/23 — 100%** | 87% |
| **MAP4K1** | **17/23 — 74%** | ⭐ **94%** |
| **NRK** | **17/23 — 74%** | **?** |

> ### ⛔ **MAP4K4 and MINK1 carry over because their ligand-contact surface is 100% IDENTICAL to TNIK's. There is literally nothing there to discriminate. I used that number in R145 and R147 as if it were a general clade property. It is not. That was an error and I am withdrawing that use of it.**

## => ⭐⭐ BUT CORRECTION 2 CUTS THE OTHER WAY — **MAP4K1 IS AT EXACTLY NRK'S SCORE AND CARRIES OVER AT 94%**

**MAP4K1 is 17/23 with four non-conservative substitutions — the identical score to NRK — and it is the
HIGHEST measured carry-over in the whole table.** So the raw count of contact differences **cannot
condemn NRK**: there is a direct empirical precedent for exactly that degree of divergence being
tolerated at 94%.

---

## => ⭐⭐⭐ PART 3 — POSITION BY POSITION: **ONLY TWO SUBSTITUTIONS ARE NRK-SPECIFIC, AND ONE IS FREE**

| TNIK pos | TNIK→NRK | MAP4K1/2/3/5 | ligand contact type | verdict |
|---|---|---|---|---|
| V31 | V→**I** | 1:L 2:V 3:I 5:V | side chain, 3.37 Å | shared with tolerated MAP4Ks; BLOSUM +3 |
| **N33** | N→**L** | 1:G 2:A 3:S 5:S | ⭐ **BACKBONE-ONLY — side chain 6.09 Å away** | ⭐ **INVISIBLE to the ligand. Free.** |
| **V39** | V→**I** | all four keep V | side chain, 3.21 Å | ⚠ **NRK-specific**, but BLOSUM +3, β-branched→β-branched |
| A83 | A→**V** | **all four also V** | side chain, 4.35 Å | shared with MAP4K1 (94%) — not evidence |
| ⚠ **F107** | F→**L** | 1:F 2:F 3:F **5:Y** | **side chain, 3.43 Å** | ⚠⚠ **THE ONE REAL RISK — see below** |
| **G109** | G→**A** | all four keep G | ⭐ **backbone-only (Gly)** | ⭐⭐ **modelled CB clearance 5.25 Å — a methyl fits with room. FREE.** |

### ⭐⭐⭐ AND THE RESULT THAT MATTERS MOST: **THE HINGE IS INTACT, AND THE GLYCINES ARE WHERE THEY MUST BE**

**Identical between TNIK and NRK:** G32, G34, A52, K54, E69, **M105 (gatekeeper)**, **E106**, **C108**,
A110, **G111**, S112, D115, Q157, N158, L160, V170, D171 — **the entire hinge and the catalytic floor.**

I modelled a virtual Cβ at every contacting glycine and measured real clearance to the ligand:

| glycine | Gly→Ala clearance | would a methyl fit? | **what NRK actually has** |
|---|---|---|---|
| **G34** | **2.36 Å** | ⛔ **clash** | ⭐ **NRK keeps GLYCINE** |
| **G111** | **2.93 Å** | ⛔ **clash** | ⭐ **NRK keeps GLYCINE** |
| G32 | 3.70 Å | fits | NRK keeps glycine |
| **G109** | ⭐ **5.25 Å** | ✅ **fits easily** | **NRK has ALANINE — and there is room for it** |

> ### ⭐⭐⭐ **NRK PRESERVES GLYCINE AT BOTH POSITIONS WHERE A METHYL WOULD CLASH, AND SUBSTITUTES ALANINE ONLY WHERE THERE IS 5.25 Å OF SPACE. IT DIFFERS WHERE THE LIGAND ISN'T AND CONSERVES WHERE THE LIGAND IS TIGHT.**

### ⚠ THE ONE GENUINE RISK, AND I AM NOT LETTING MY OWN SCRIPT PAPER OVER IT

My "shared with the MAP4Ks" test was **too loose** — it counted any difference at a position as shared.
At **F107** that is misleading: MAP4K1/2/3 keep **F**, and MAP4K5 substitutes **F→Y**, which *retains the
aromatic ring*. **Only NRK loses it (F→L), at a side-chain contact of 3.43 Å.** So F107L is
NRK-specific in character even though the position is not NRK-specific in fact.

⚠ **Mildly corroborating and worth noting:** MAP4K5 — the only other kinase substituted at 107 — is also
the **weakest tracer binder of the four MAP4Ks** in the Promega data. Small n, but it points the same way.

---

## => ⭐ PART 4 — PER-COMPOUND RANKING, AND IT REPRODUCES R147's PREDICTION FROM AN INDEPENDENT DIRECTION

How many NRK differences does each ligand actually touch?

| PDB | ligand | contacts | ⭐ **NRK differences touched** | which |
|---|---|---|---|---|
| ⭐ **6RA7** | compound 9 | 17 | ⭐ **4 — fewest** | V31I, V39I, A83V, F107L — **misses N33 and G109 entirely** |
| **5D7A** | **NCB-0846** | 19 | **5** | + N33L |
| 5AX9 | TNIK inhibitor | 21 | 5 | + G109A |
| ⛔ **8ZML** | ⛔ **"potent and SELECTIVE TNIK inhibitor for IPF"** | 25 | ⛔ **8 — most** | + Y85F, L103M, T309I |

> ### ⭐⭐ **THE COMPOUND EXPLICITLY OPTIMISED AS A *SELECTIVE* TNIK INHIBITOR *FOR IPF* TOUCHES TWICE AS MANY NRK-divergent POSITIONS AS THE SMALLEST LIGAND. Rentosertib is the same optimisation target in the same indication — and R147 predicted, before I ever opened a structure, that it would be the WORST of the panel for NRK. That prediction now has independent structural support.**

---

## => SO WHERE DOES THIS LEAVE `f`? — THE HONEST ANSWER

| question | answer | changed? |
|---|---|---|
| **Does a small molecule occupy NRK's pocket at all?** | ⭐ yes — Promega, live cells (R149) | settled |
| **Is NRK's ligand-contact surface TNIK-like?** | ⭐ **more so than R147's whole-pocket count implied** — differences sit off the ligand except F107 | ⭐ **up** |
| **Is R146's 68–94% base rate usable?** | ⛔ **no — withdrawn** | ⛔ **down** |
| **Is there precedent for NRK's exact divergence being tolerated?** | ⭐ **yes — MAP4K1, same 17/23, 94% carry-over** | ⭐ **up** |
| **Is NRK a strong binder of a broad-spectrum chemotype?** | ⛔ **no — last of five MAP4Ks** | ⛔ **down** |
| ⭐ **P(rentosertib binds NRK at all)** | **~70%, now on structural rather than base-rate grounds** | ≈ unchanged, **better founded** |
| ⛔⛔ **P(f ≥ 0.7 — the both-arms case)** | ⛔ **~15%. Structure cannot resolve this.** | barely moved |

> ### ⛔ **THE LIMIT, STATED PLAINLY: contact analysis can tell you a compound LIKELY BINDS. It cannot tell you it binds WITHIN 1.4-FOLD — and R148 proved 1.4-fold is what the both-arms claim requires, because the exposure axis cancels. F107L is exactly the class of substitution that costs 3–30×, and 3× is enough to kill the NRK arm while leaving the Wnt arm untouched.**

### ⭐ AND THEREFORE THE ACTIONABLE CONCLUSION, WHICH DOESN'T NEED THE ASSAY

**The Wnt arm stands entirely on its own.** R148 established 30 mg QD as a human-validated mild Wnt
perturbation with the SPIN4 window inside its engagement band, on FVC and ALT data from 71 people.
**None of that depends on NRK.** ⭐ **NRK is a lottery ticket on top — roughly 15% — not a reason to
dose and not a reason to hold.** Treat the rentosertib arm as a Wnt-arm decision, and if NRK comes
along, that is upside.

---

## CORRECTIONS

- ⚠ **NRK row verified from the figure image, not OCR: 1.51 / 2.85 / 1.09.** The user's numbers were
  exactly right; my first OCR pass misread CC-1804 as 5.32. Also **the row above NRK is NIM1K, not MINK1.**
- ⛔ **MAP4K4, TNIK and MINK1 are ALL ABSENT from the 595-entity panel** (FIG. 1E jumps MAP4K3 → MAP4K5).
  The direct clade comparison cannot be made inside this patent.
- ⛔ **NEW DEFLATOR: NRK is the WEAKEST tracer binder of the five MAP4K-family members present**
  (sum 5.45 vs 5.74 / 8.59 / 11.87 / 19.89). ⚠ Confounded by fusion geometry — suggestive, not quantitative.
- ⛔⛔ **CORRECTION TO R145/R147: R146's 68–94% carry-over base rate is WITHDRAWN as support for NRK.**
  MAP4K4 and MINK1 have **23/23 — 100% identical ligand-contact surfaces** with TNIK. They carry over
  because there is nothing there to discriminate. **That number was never transferable.**
- ⭐⭐ **BUT MAP4K1 sits at 17/23 — exactly NRK's score, four non-conservative — and carries over at 94%,
  the highest measured.** A raw count of contact differences cannot condemn NRK.
- ⭐⭐⭐ **ONLY TWO CONTACT SUBSTITUTIONS ARE NRK-SPECIFIC: V39I (BLOSUM +3, conservative) and G109A —
  and G109A is FREE:** G109 contacts the ligand through backbone only, and the modelled Cβ has **5.25 Å
  clearance**. **N33L, which looks alarming, is backbone-only with its side chain 6.09 Å away — invisible.**
- ⭐⭐⭐ **THE HINGE IS INTACT** — M105 gatekeeper, E106, C108, A110, G111, S112, D115 all identical. **And
  NRK keeps glycine at G34 (2.36 Å) and G111 (2.93 Å), the two positions where a methyl would clash,
  taking alanine only at G109 where there is room. It conserves where the ligand is tight.**
- ⚠ **ONE REAL RISK, and my own script's "shared" test was too loose to catch it: F107L.** MAP4K1/2/3 keep
  F, MAP4K5 keeps the aromatic as Y — **only NRK loses it**, at a 3.43 Å side-chain contact. MAP4K5, the
  other 107-substituted kinase, is also the weakest tracer binder of the MAP4Ks.
- ⭐ **PER-COMPOUND RANKING CONFIRMS R147's FALSIFIABLE ORDERING FROM AN INDEPENDENT DIRECTION:** the 2025
  **"potent and selective TNIK inhibitor for IPF"** (8ZML) touches **8** NRK-divergent positions, the most
  of any ligand; compound 9 touches **4**, the fewest. **Rentosertib is the same optimisation target in
  the same indication and was predicted worst for NRK before any structure was opened.**
- ⭐ **NET: P(binds NRK) ~70% but now on structural rather than base-rate grounds; P(f ≥ 0.7, the
  both-arms case) ~15%.** ⛔ **Structure cannot close this gap — contact analysis says "likely binds," never
  "binds within 1.4-fold."**
- ⭐⭐ **ACTIONABLE WITHOUT ANY ASSAY: the Wnt arm stands alone on R148's human data. NRK is ~15% upside,
  not a reason to dose and not a reason to hold.**
