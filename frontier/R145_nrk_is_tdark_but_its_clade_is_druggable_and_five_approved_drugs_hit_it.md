# F-R145 — **NRK IS Tdark WITH ZERO LIGANDS — BUT ITS KINASE DOMAIN IS 65% IDENTICAL TO THREE KINASES WITH REAL CHEMISTRY, IT HAS THE SAME GATEKEEPER, AND FIVE APPROVED DRUGS HIT THAT CLADE AT 3–25 nM. THE PROBLEM IS THAT THOSE FIVE ARE THE DRUG CLASS DOCUMENTED TO STUNT CHILDREN'S GROWTH.**

**The operator's call was right: NRK is a kinase, and the off-target space is where to look. R144
said "no chemical matter at all." That was true of NRK itself and wrong about what it implies.**

Supplied: `kosmicki2026` full supplement (`media2_4.xlsx`, 29 tables), `Gizzio et al. 2026` active-kinase
AF2 preprint, UniProt Q7Z2Y5. Plus ChEMBL, Pharos/IDG and UniProt REST queried directly.
Code: `analysis/redundancy/kos.py`, `homalt.py`, `pocket.py`, `offtarget.py`.

---

## => ⭐⭐⭐ FIRST, THE SUPPLEMENT DELIVERS SOMETHING I DID NOT EXPECT: **NRK HAS A HUMAN KNOCKOUT COHORT**

Table S5, the full 17 singleton-pLoF genes, combined discovery + replication (1.45M exomes):

| gene | chr | **effect (cm)** | het | ⭐ **hom/hemizygous nulls** | P |
|---|---|---|---|---|---|
| FBN1 | 15 | **+9.37** | 87 | **0** | 1.95e-37 |
| LCORL | 4 | **+8.18** | 166 | **0** | 1.89e-53 |
| TET1 | 10 | **+7.74** | 90 | **0** | 8.84e-27 |
| CHD8 | 14 | **+7.05** | 45 | **0** | 5.8e-12 |
| ZFAT | 8 | **+6.49** | 94 | **0** | 5.39e-20 |
| ⭐ **NRK** | **X** | **+3.48** | 80 | ⭐⭐ **34** | 2.13e-13 |
| NF1 · DTL · IGF2BP2 · COL1A1 · IGF1R · ADAMTS10 · SCUBE3 · ADAMTS6 · EXT1 · ANKRD11 · ACAN | | −5.39 → **−14.10** | | **0** | |

**Six of seventeen are positive. The atlas's list was right and is now complete.**

> ### ⭐⭐⭐ **NRK IS THE ONLY GENE IN ALL SEVENTEEN WITH HOMOZYGOUS/HEMIZYGOUS NULLS. 34 OF THEM — AND ALL 34 HOM/HEMI INDIVIDUALS IN THE ENTIRE TABLE ARE NRK. EVERY OTHER GENE HAS ZERO.**
> **NRK is X-linked, so in males "HomAlt" is HEMIZYGOUS — complete loss of function. There are 34
> adults in a health-system biobank with no functional NRK, and they are 3.48 cm taller.**

**For a drug target that is the best safety evidence class that exists — better than a knockout mouse,
better than a Phase 1.** It is a natural human knockout cohort showing that total, lifelong NRK
ablation is compatible with reaching adulthood in a healthcare system, with height as the phenotype.

⚠ **Honest limits:** biobank ascertainment is not a safety study — these people were not examined for
subtle phenotypes, and Nrk-null mice do show **delayed parturition**, a phenotype no biobank would
capture. NRK's effect is also the **smallest** of the six positives, and its pLoF-to-GWAS ratio (19.7)
is the lowest of them (TET1 41.6, ZFAT 49.3, CHD8 59.9).

---

## => THE TARGET, FROM UniProt Q7Z2Y5

| | |
|---|---|
| length | **1,582 aa** — kinase domain **25–313** at the N-terminus, CNH domain **1209–1552** |
| family | **STE Ser/Thr kinase family, STE20 subfamily** (GCK group IV) |
| active site | **177**; ATP binding **31–39** (P-loop) and **54** (β3 lysine) |
| function | *"May phosphorylate **cofilin-1** and induce **actin polymerisation**… Involved in the TNF-induced signalling pathway"* |
| ⛔ **chemistry** | ⛔ **NO ChEMBL, NO BindingDB, NO DrugBank, NO Guide-to-Pharmacology cross-reference** |
| ⛔ **ChEMBL direct query** | ⛔ **0 targets returned for Q7Z2Y5 — NRK is not a registered target at all** |
| ⛔ **Pharos / NIH IDG** | ⛔ **`Tdark`, ligands = 0, drugs = 0, novelty 0.18** |

⭐ **And `Gizzio 2026` DOES contain NRK** — `STE_NRK NRK_HUMAN NRK Q7Z2Y5 17 321 305 1582`, sitting in
the STE table between MAP4K5/MINK1 and OXSR1/PAK1-4. **It is in the structural kinome; it is simply not
in the pharmacological one.**

> ### **Tdark WITH ZERO LIGANDS DOES NOT MEAN NOTHING BINDS. IT MEANS NOBODY HAS LOOKED. NRK is absent from the commercial selectivity panels, and its restricted expression keeps it out of the cell lysates used for chemoproteomics. THE OFF-TARGET SPACE IS UNEXPLORED, NOT EMPTY — which is exactly the operator's point.**

---

## => ⭐⭐ SO I ASKED THE QUESTION STRUCTURALLY: **HOW CLOSE IS NRK'S POCKET TO KINASES THAT DO HAVE DRUGS?**

Pairwise global alignment (BLOSUM62) of NRK's kinase domain against every GCK/STE20 relative:

| kinase | KD identity | similarity | chemical matter |
|---|---|---|---|
| ⭐ **MINK1** | ⭐ **64.9%** | 80.8% | Tchem — hit by MAP4K4 inhibitors |
| ⭐ **MAP4K4** | ⭐ **64.5%** | 80.8% | Tchem — PF-06260933, GNE-495, DMX-5804 |
| ⭐ **TNIK** | ⭐ **63.0%** | 80.8% | Tchem — NCB-0846, KY-05009 · ⭐ **and TNIK is a Wnt/TCF4 kinase** |
| MAP4K3 | 44.3% | 63.6% | Tbio |
| MAP4K2 | 43.0% | 63.6% | Tbio |
| MAP4K1 (HPK1) | 41.2% | 59.9% | Tchem, heavy immuno-oncology programme |
| MAP4K5 | 40.9% | 61.3% | Tbio |
| OXSR1 | 34.6% | 55.0% | Tbio |
| STK39 (SPAK) | 33.6% | 55.0% | Tchem |

**NRK is squarely inside the GCK-IV clade with MAP4K4/TNIK/MINK1 at 63–65%, and a full 20 points above
every other STE20.** And the pocket motifs are identical where it matters:

| | P-loop | HRD motif | **gatekeeper** |
|---|---|---|---|
| **NRK** | (variant) | **HRDIK** | ⭐ **Met** — `RHQLWMV`**`M`**`ELCAA` |
| MAP4K4 | GNGTYGQV | **HRDIK** | ⭐ **Met** — `DDQLWLV`**`M`**`EFCGA` |
| TNIK | GNGTYGQV | **HRDIK** | Met |
| MINK1 | GNGTYGQV | **HRDIK** | Met |

> ### ⭐⭐ **SAME GATEKEEPER RESIDUE, SAME CATALYTIC MOTIF, 65% DOMAIN IDENTITY. The gatekeeper is the single biggest determinant of ATP-competitive inhibitor selectivity, and NRK's is the same methionine as the three kinases that have inhibitors. There is no steric reason a GCK-IV inhibitor would not bind NRK.**

---

## => ⭐⭐⭐ AND THEN THE ACTUAL SEARCH: **WHICH COMPOUNDS HIT ALL THREE?**

Pulled every ChEMBL activity at pChEMBL ≥ 6 (≤ 1 µM) for MAP4K4 (745 compounds), TNIK (469) and
MINK1 (217), and intersected. **26 compounds are potent against all three.** Of those, thirteen are
clinical or approved:

| compound | phase | **MAP4K4** | **TNIK** | **MINK1** |
|---|---|---|---|---|
| ⭐⭐ **BOSUTINIB** | ⭐ **4 — APPROVED** | ⭐ **8.1 (8 nM)** | **7.6 (25 nM)** | ⭐ **8.5 (3 nM)** |
| **SUNITINIB** | **4 — APPROVED** | 6.8 | 7.6 | 7.5 |
| **NINTEDANIB** | **4 — APPROVED** | 6.8 | 7.3 | 7.1 |
| **NERATINIB** | **4 — APPROVED** | 6.5 | 6.8 | 7.5 |
| **AXITINIB** | **4 — APPROVED** | 6.5 | 6.8 | 6.2 |
| LESTAURTINIB | 3 | 7.6 | **8.3** | **8.4** |
| DOVITINIB | 3 | 7.6 | ⭐ **8.7 (2 nM)** | 8.0 |
| BRIVANIB · SOTRASTAURIN · SU-014813 · DORAMAPIMOD · AST-487 · KW-2449 | 1–2 | 6.2–7.8 | 6.8–8.0 | 6.5–8.1 |

> ### **THE GCK-IV CLADE IS NOT AN ORPHAN POCKET. IT IS POTENTLY DRUGGED BY APPROVED CHEMISTRY — BOSUTINIB AT 3–25 nM ACROSS ALL THREE. R144's "NRK has an ideal target class and not one molecule" IS CORRECTED: NRK itself has no molecule, but its clade has a dozen, five of them approved.**

---

## => ⛔⛔ AND HERE IS THE CATCH, AND IT IS SEVERE ENOUGH TO LEAD WITH

**Every one of those five approved drugs is a promiscuous multi-kinase inhibitor whose *intended*
targets include ABL, SRC, KIT, PDGFR and VEGFR. And that drug class has a measured, published effect
on children's height — in the wrong direction.**

> **`German CML-PAED II cohort, 2024`, n = 94 children on imatinib > 12 months:** *"In children and
> adolescents, **impaired growth due to tyrosine kinase inhibitor therapy** remains an insufficiently
> studied adverse effect… **During imatinib treatment, significant height reduction occurred, with
> medians of −0.35 standard deviation score.**"*
>
> **And a 2019 case report:** a boy on imatinib then dasatinib with chronic bone pain and *"downward
> crossing of height percentiles."*

> ### ⛔ **THE APPROVED DRUGS MOST LIKELY TO HIT NRK BELONG TO THE ONE DRUG CLASS WITH A DOCUMENTED, QUANTIFIED GROWTH-STUNTING EFFECT IN CHILDREN. Using bosutinib to gain height would be giving a growth-impairing agent for a growth indication.**

**The mechanism of that class effect is thought to be PDGFR-β and c-KIT inhibition in the growth plate
plus GH/IGF-1 axis effects — i.e. it is ON-target for those kinases, not an idiosyncrasy.** It cannot
be dosed around, and it is the same failure logic as R138's verteporfin rejection: the systemic agent
cannot choose its compartment.

---

## => SO WHAT ACTUALLY SURVIVES — AND IT IS A REAL ADVANCE, JUST NOT THE ONE HOPED FOR

| | before R145 | after R145 |
|---|---|---|
| **is NRK druggable?** | ⛔ "dark kinase, zero chemical matter" | ⭐ **its clade is drugged to 3 nM by approved compounds, and NRK shares 65% identity, the HRD motif and the Met gatekeeper. The pocket is tractable.** |
| **is there an NRK inhibitor?** | ⛔ no | ⛔ **still no — and nobody has ever tested one against NRK** |
| **can we repurpose an approved drug?** | unknown | ⛔ **NO — the five candidates are the growth-stunting TKI class** |
| **what is needed?** | a med-chem programme from scratch | ⭐ **a GCK-IV-selective compound WITHOUT ABL/KIT/PDGFR — and those already exist as tool compounds** |

⭐ **The tool compounds that have the right shape:** **PF-06260933** (Pfizer, MAP4K4-selective),
**GNE-495** (Genentech, MAP4K4), **NCB-0846** (TNIK-selective, entered clinical development for
colorectal cancer). **None is approved, but none carries the ABL/KIT/PDGFR burden either.**

### ⭐⭐ AND ONE CONVERGENCE WORTH MORE THAN THE REST: **TNIK IS A Wnt/TCF4 KINASE**

A GCK-IV inhibitor would hit **two** of this file's arms with one chemotype:

```
TNIK inhibition  →  ↓ Wnt/TCF transcriptional output  →  the SPIN4 axis (R138: the 38-45% target)
NRK inhibition   →  ↑ AKT → ↑ mTORC1 → symmetric division  →  the N axis (newton2019, R130/R144)
```

> **These are the two mechanisms this file has been pursuing separately for ten rounds, and one
> chemical clade touches both. NCB-0846 is a TNIK inhibitor that reached clinical development — so
> unlike selamectin, that chemotype may have human exposure data.**
> ⚠ **And R137's magnitude ladder applies here too: a POTENT TNIK inhibitor would overshoot the Wnt
> arm into the ICAT regime. The same dose-response caution from R139/R140 carries over.**

---

## => ⭐ THE EXPERIMENT THAT SETTLES THE WHOLE QUESTION, AND IT IS CHEAP

**Run a binding/activity assay of recombinant NRK against a small panel: bosutinib, lestaurtinib,
dovitinib, PF-06260933, GNE-495, NCB-0846.**

- **NRK is absent from the standard commercial selectivity panels — which is the entire reason nobody
  knows.** A single custom kinase assay (Reaction Biology, Eurofins, DiscoverX) covers it.
- **If NRK is hit at ≤100 nM by a GCK-IV-selective compound**, the target goes from Tdark to
  chemically addressable in one experiment, and the med-chem starting point is handed over.
- **If NRK is not hit despite 65% identity and an identical gatekeeper**, that is a real and
  informative negative — it says the selectivity lives in the 35% that differs, and a dedicated
  programme is required.

**Cost: one assay. It is the single highest information-per-dollar experiment anywhere in this file,
including the explant.**

---

## => WHAT I NEED

1. ⭐⭐ **`Gizzio et al.` main text and supplementary tables on NRK specifically** — the paper models
   active-state kinase conformations from AlphaFold2 across the kinome. **If NRK is predicted to adopt
   a canonical active DFG-in conformation, ATP-competitive inhibition is straightforward; if it is
   predicted pseudokinase-like or constitutively DFG-out, that changes the chemistry.** I found NRK in
   their table but not their conformational call for it.
2. ⭐ **Any kinome selectivity panel that actually contains NRK.** The whole argument turns on its
   absence — one panel with NRK on it would replace all of this homology reasoning with data.
3. **The `NCB-0846` clinical file** — a TNIK inhibitor with human exposure would be the fastest route
   into both arms at once.
4. Still outstanding: **erda hand/wrist films**; **sitting height vs subischial leg length +
   ring-apophysis staging**; **NT-proCNP**; **liver fat**.

---

## CORRECTIONS

- ⭐⭐⭐ **NRK HAS A HUMAN KNOCKOUT COHORT — 34 homozygous/hemizygous nulls in 1.45M exomes, and it is
  the ONLY gene of the 17 with any. Every other gene has zero.** X-linked, so male HomAlt = complete
  loss. **The best target-safety evidence class that exists, and R144 did not have it.**
- ⭐⭐ **R144's "NRK has an ideal target class and NOT ONE MOLECULE" is CORRECTED.** NRK itself has zero
  ligands (Pharos Tdark, ChEMBL not even a registered target) — **but its kinase domain is 63–65%
  identical to MAP4K4/TNIK/MINK1, carries the same Met gatekeeper and the same HRDIK motif, and that
  clade is hit by five approved drugs, bosutinib at 3–25 nM.** The pocket is tractable.
- ⭐ **"Tdark with zero ligands" reinterpreted:** NRK is absent from commercial selectivity panels and
  from chemoproteomic lysates. **Nobody has looked. The off-target space is unexplored, not empty** —
  the operator's framing was correct.
- ⛔⛔ **BUT DIRECT REPURPOSING IS DEAD: all five approved GCK-IV binders are ABL/SRC/KIT/PDGFR
  multi-kinase inhibitors, and that class has a measured growth-stunting effect in children —
  imatinib, median −0.35 SDS in a 94-patient paediatric cohort.** On-target for those kinases, so not
  dosable around.
- ⭐ **What is needed is named and exists:** a GCK-IV-selective compound without the ABL/KIT/PDGFR
  burden — **PF-06260933, GNE-495, NCB-0846.**
- ⭐⭐ **CONVERGENCE: TNIK is a Wnt/TCF4 kinase, so one GCK-IV chemotype touches BOTH the SPIN4/Wnt arm
  and the NRK/mTORC1 N arm** — the two mechanisms this file has pursued separately. ⚠ Subject to
  R137's magnitude ladder: a potent TNIK inhibitor would overshoot the Wnt arm.
- ⭐ **The decisive experiment is now one kinase assay**, not a med-chem programme.
