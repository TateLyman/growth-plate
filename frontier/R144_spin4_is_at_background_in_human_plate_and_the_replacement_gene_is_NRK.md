# F-R144 — **SPIN4 IS AT BACKGROUND IN THE HUMAN GROWTH PLATE. R143's SECOND LEG IS WITHDRAWN. AND THE REPLACEMENT GENE IS **NRK** — SAME FUNCTIONAL CLASS, BETTER HUMAN EVIDENCE, A KINASE INSTEAD OF A READER, AND NO DRUG.**

The EPAR is a dead end — a veterinary EMA document with no human data, and the PDF the fetch returned
was a one-page stub. **R142's finding stands: there is no human selamectin data.** Moving to the
operator's second instruction.

**But the atlas section I opened to start that search contained something that forces a correction
first.**

---

## => ⛔⛔ THE CORRECTION: **SPIN4 IS NOT DETECTED IN THE HUMAN GROWTH PLATE, AND I HAVE BEEN QUOTING NOISE SINCE R135**

The atlas recorded it at R292 — *"TWO HUMAN NEGATIVES, grade D, recorded because they are
inconvenient. **SPIN4** (R281's 'cleanest pool lever') = **0/10 arrays**."* **I never checked it, and
I built three rounds of zonal argument on top of the numbers.**

I verified it myself rather than taking the atlas's word (`analysis/redundancy/detect2.py`). Background
= 60th percentile of all 54,675 probes per array, which puts thresholds at **210–385** — and the
controls behave correctly under it:

| control | detected | behaviour |
|---|---|---|
| COL2A1 | **10/10** | 44,607–104,438 everywhere ✅ |
| ACAN | **10/10** (3 probes) | high everywhere ✅ |
| COL10A1 | 8–10/10 | **72,039 in HZ → 426 in PZ** ✅ correct zonal switch |
| IHH | 4–8/10 | **20,856 in HZ → 141 in PZ** ✅ correct |

**Against that:**

| gene | probe | values across 10 arrays | **detected** |
|---|---|---|---|
| ⛔ **SPIN4** | 228654_at (only probe) | 166 178 353 36 186 141 209 183 146 205 | ⛔ **1 / 10** |

> ### **SPIN4 SITS AT BACKGROUND ON THE ONLY ZONE-RESOLVED HUMAN GROWTH-PLATE TRANSCRIPTOME. Every SPIN4 number I quoted from GSE9160 in R135, R138 and R143 is noise.**

### WHAT THAT INVALIDATES, PRECISELY

| claim | status |
|---|---|
| ⛔ **R143 TERM B2** — "SPIN4 anti-correlates with Wnt output across zones, r = −0.28" | ⛔ **WITHDRAWN.** Noise correlated against noise — **and the Wnt panel is at background too:** SP5 **0/10**, LGR5 **1/10**, AXIN2 detected on only **1 of 4** probes, NKD1 marginal. |
| ⛔ **R138** — "mouse Spin4 is RZ-highest, human SPIN4 is PZ-enriched and RZ-lowest: an open species conflict" | ⛔ **THERE WAS NO CONFLICT.** I was reading a below-background probe as a zonal pattern. **Withdrawn, and it was a cleaner error than "unresolved."** |
| ⛔ **R135's SPIN-family zonal table** | ⛔ SPIN4, SPIN2A, SPIN3 all at background. ✅ **SPIN1 survives** — probe 222431_at is **10/10** at 1,595–3,910, so "SPIN1 is abundant and uniform across zones" stands. |
| ✅ **R143 TERM B1** — drug-signature concordance, SPIN4 52.1% vs AXIN2 69.5%, n=466 | ✅ **UNTOUCHED.** RummaGEO is a completely different data source. **B1 alone carries the loop-gain conclusion, and the conclusion stands: g = 0.016–0.042, amplification 1.02×.** |
| ✅ **R138's Wnt-ANTAGONIST half** | ✅ **STANDS.** SFRP5 6,043 · FRZB 5,048 · DKK3 5,504 · SFRP1 1,533 — all far above a 210–385 threshold. **The resting zone really is the plate's antagonist reservoir.** ⚠ The Wnt-*output* half now rests on AXIN2 alone. |

⚠ **This is NOT a refutation of SPIN4.** The same platform reads **NPPC** — vosoritide's own ligand —
below background while detecting NPR2 and NPR3; it is insensitive to low-abundance regulatory
transcripts. **The human SPIN4 phenotype (+4.5–5 SDS, segregating in three relatives) is unaffected.**
**What is gone is my claim to have measured SPIN4 in human cartilage.**

---

## => ⭐⭐⭐ THE REPLACEMENT: **`kosmicki2026`'s 17 GENES — AND THE ENDPOINT IS WHY THEY MATTER**

**826,066 discovery exomes, 98% of 207 genes replicated in 624,567 more. Singleton pLoF in 17 genes
moves adult height a mean 8.92 cm/allele — ~52× the average common variant.** Our whole stack is 1–3 cm.

> ### ⭐⭐ **AND HERE IS THE STRUCTURAL POINT THIS ARM HAS NEVER USED: THE ENDPOINT IS *ADULT* HEIGHT.**
> **R138 spent a whole round establishing that SPIN4 is the only member of the epigenetic overgrowth
> class that is BONE-AGE-NEUTRAL — every writer (NSD1, EZH2, EED, SUZ12, DNMT3A) advances bone age and
> lands at NORMAL adult height. `kosmicki2026`'s β is measured on FINAL height. So every positive-β
> gene in that table is BONE-AGE-SURVIVABLE BY CONSTRUCTION — the gain persisted to adulthood or it
> would not be in the table.**
> **That is a pre-filtered list of seventeen levers with exactly the property R138 identified as
> decisive, at a mean 8.92 cm/allele, and this arm went looking in the syndrome literature instead.**

| gene | β cm/allele | carriers | class | baggage |
|---|---|---|---|---|
| FBN1 | +11.14 | 40 | ECM/TGF-β | ⛔ Marfan (aorta) |
| **CHD8** | **+10.22** | 21 | ⭐ **chromatin, Wnt** | ⛔ **ASD + ID + macrocephaly** |
| LCORL | +9.99 | 71 | TF | ⛔ downgraded R285 — Lcorl-null mice born *smaller* |
| ⭐ **TET1** | ⭐ **+8.32** | 42 | ⭐ **ENZYME** | ⭐ **none** |
| ZFAT | +7.86 | 41 | TF | ⚠ thyroid autoimmunity, nothing skeletal in any species |
| ⭐⭐ **NRK** | **+3.79** | **56** | ⭐⭐ **KINASE** | ⭐ **none** |

**CHD8 is mechanistically the closest thing to SPIN4 in the table — chromatin regulator acting on Wnt,
+10.22 cm — and it is unusable. Autism, intellectual disability and macrocephaly are not a side
effect; they are the syndrome.**

---

## => ⭐⭐⭐ THE ANSWER: **NRK**, AND THE PARALLEL TO SPIN4 IS ALMOST POINT-FOR-POINT

| | **SPIN4** | ⭐ **NRK** |
|---|---|---|
| chromosome | **X-linked** | ⭐ **X-linked** — a male subject is hemizygous, one allele to move |
| knockout mice | **viable**, larger | ⭐ **viable** (phenotype is delayed delivery, a placental-maternal signalling effect) |
| cellular function | *"inhibits cell proliferation"* | ⭐ *"**plays a role in preventing placental HYPERPLASIA**"* |
| loss produces | **hyperplasia, not hypertrophy** | ⭐ **hyperplasia** |
| human LOF evidence | +4.5–5 SDS, **one family, 3 relatives** | ⭐ **+3.79 cm/allele, 56 carriers, 1.45M exomes** |
| druggable class | ⛔ **Tudor reader — the hardest class in the genome** | ⭐⭐ **KINASE — the easiest** |
| therapeutic direction | inhibition | ⭐ **inhibition** (pLoF is the beneficial allele) |
| **human growth plate** | ⛔ **1/10 probe-array cells — at background** | ⭐⭐ **10/10, values 557–9,980** |

**NRK in GSE9160, probe 227971_at:**

| | Reserve | Prolif | PreHyp | Hyper | Perich |
|---|---|---|---|---|---|
| donor 1 | 1,050 | **8,062** | **9,980** | **9,289** | 3,556 |
| donor 2 | 2,444 | **4,297** | 1,771 | 1,448 | 557 |

> **Detected on every array of both donors, against a 210–385 threshold. One of only three genes —
> with ACAN and COL2A1 — present in all five compartments of both children. NRK has better human
> growth-plate evidence than SPIN4 has ever had.**

### ⭐⭐ AND THE MECHANISM IS A ROUTE TO N THAT IS **INDEPENDENT OF WNT**

> *"Placental mammals acquired functional sequences in NRK for regulating the **CK2–PTEN–AKT pathway**
> and placental cell proliferation."*

**NRK ⊣ (via CK2) PTEN ⊣ AKT → mTORC1.** And **`newton2019` (R130) has mTORC1 activation expanding the
stem pool via SYMMETRIC DIVISION** — the exact N mechanism this file has been chasing.

> ### **NRK INHIBITION → ↑AKT → ↑mTORC1 → SYMMETRIC DIVISION → N. Every link is published. The chain has never been assembled, and never in cartilage.**
> ⭐ **AND IT IS ORTHOGONAL TO WNT, so it is potentially ADDITIVE to a Wnt-lowering agent rather than
> competing for the same narrow shelf that R137's magnitude ladder describes.**
> ⭐ **It also inverts R136's metformin problem in our favour:** metformin *inhibits* mTORC1 and
> therefore opposes the pool arm; **NRK inhibition activates it.**

### ⛔ AND THE TWO THINGS THAT ARE WRONG WITH IT, STATED FIRST-CLASS

1. ⛔⛔ **THERE IS NO NRK INHIBITOR. NONE.** I searched for a chemical probe, tool compound or
   selective inhibitor and the query returned **zero results**. NRK is a GCK group-IV STE20 kinase and
   an **understudied ("dark") kinase**. **This is the exact opposite of selamectin's problem: SPIN4 had
   a bad drug for an undruggable target; NRK has an ideal target class and no chemical matter at all.**
2. ⛔ **NO SKELETAL PERTURBATION OF NRK EXISTS IN ANY SPECIES.** The atlas already recorded this
   (`g_l8_nrk_has_no_skeletal_experiment_in_any_species`) and it is still true. The direction comes
   entirely from human pLoF genetics.
3. ⚠ **The zonal profile does not obviously say "N".** NRK is **lowest in the resting zone** (1,050)
   and highest in proliferative/prehypertrophic (8,062/9,980) in donor 1 — a transit-amplifying
   profile, not a stem-compartment one. **If it acts where it is expressed, inhibiting it raises PZ
   proliferation, and R138 established that raising throughput SPENDS BONE AGE.**
   > ⭐ **The counter is the endpoint itself: +3.79 cm is measured on ADULT height in 56 carriers. If
   > the gain were being paid for in bone age it would not be there at maturity.** The human data
   > answers the bone-age question directly, which is the same argument R138 used for SPIN4.
   > ⚠ **And I am flagging the profile rather than reading a direction from it — that is the error I
   > have now made three times (AR in R126, TGF-β in R130, and nearly with verteporfin in R137).**

---

## => THE SECOND CANDIDATE: **TET1** — BIGGER EFFECT, A REAL DRUG CLASS, WORSE SPECIFICITY

| | |
|---|---|
| β | ⭐ **+8.32 cm/allele, 42 carriers** — more than double NRK's |
| class | ⭐ **enzyme** (Fe(II)/2-OG dioxygenase, DNA demethylase) — druggable in principle |
| baggage | ⭐ **none** |
| human growth plate | ⭐ **7/10 probe-array cells** (228906_at, 210–753) — present, modest |
| ⭐ **class logic** | **`Lui 2023`'s own introduction:** *"no overgrowth syndrome has been ascribed to a gene that acts primarily as epigenetic **erasers**… or **readers**."* **SPIN4 became the first reader. TET1 would be the first eraser** — and both sit outside the bone-age-spending writer class |
| ⛔ **the drug problem** | **Bobcat339 is the only TET tool compound in use, it is a pan-TET inhibitor (TET1/2/3), and its selectivity has been contested.** TET1/2/3 are functionally redundant. **A pan-TET inhibitor is the ICAT-equivalent mistake — total blockade of a family where only partial single-member loss is wanted** |
| ⚠ | atlas R287: TET1's bone literature is *"ageing/BMSC only"* — nothing in growth plate |

⚠ **And an unresolved paradox worth naming:** DNMT3A **writes** methylation and its loss causes
overgrowth (Tatton-Brown-Rahman, with advanced bone age). TET1 **erases** methylation and its loss also
causes overgrowth (+8.32 cm, bone-age-survivable). **Opposite enzymes, same direction of effect —
structurally identical to the SPIN4/CXXC5 Wnt paradox R137 resolved as a magnitude law rather than a
direction law.** Unexplained, and it should be explained before TET1 is taken seriously.

---

## => THE HONEST RANKING FOR "A DIFFERENT GENE IN THE SPIN4 REALM WE CAN DRUG"

| | target quality | human evidence | druggability | verdict |
|---|---|---|---|---|
| ⭐⭐ **NRK** | ⭐ anti-proliferative, X-linked, viable KO, **CK2-PTEN-AKT→mTORC1 = an N route independent of Wnt** | ⭐ **+3.79 cm, 56 carriers, 1.45M exomes; 10/10 in human plate** | ⛔ **kinase — ideal class, ZERO chemical matter** | ⭐ **best target, no drug** |
| ⭐ **TET1** | ⭐ eraser class, outside the BA-spending writers | ⭐ **+8.32 cm, 42 carriers**; 7/10 in human plate | ⚠ **pan-TET only, contested selectivity, family redundancy** | ⚠ **bigger effect, worse tool** |
| **CHD8** | ⭐⭐ **chromatin + Wnt — the closest mechanistic match to SPIN4** | ⭐ **+10.22 cm** | — | ⛔ **ASD + ID + macrocephaly — unusable** |
| **SPIN4** | ⭐ the validated mechanism | ⭐ human family + mouse; ⛔ **not detectable in human plate** | ⛔ reader; **selamectin is the tool and has no human data** | ⚠ **still the lead, on mechanism** |

> ### **NRK AND SPIN4 HAVE OPPOSITE PROBLEMS. SPIN4 has a validated mechanism, a measured 38% Wnt contribution, a proven phenotype — and its best tool is a veterinary drug no human has taken. NRK has 1.45M-exome human genetics, the best growth-plate expression of any candidate, an ideal druggable class, and NOT ONE MOLECULE.**
> **Neither is finishable today. But NRK's gap is a medicinal-chemistry programme against a defined
> kinase, and SPIN4's gap is a Phase 0 study of an existing molecule. The second is much cheaper.**

---

## => WHAT I WOULD DO NEXT, IN ORDER

1. ⭐ **Run the explant with selamectin anyway.** It is still the only experiment that converts six
   rounds of preparation into a sign, and R142's design is unchanged.
2. ⭐⭐ **Get the full `kosmicki2026` 17-gene table.** I have six. **Eleven are unnamed here, and the
   atlas records that "the 11 NEGATIVE-beta genes were never searched in the ELEVATION direction"
   (CORR-303).** A pre-filtered, bone-age-survivable, 1.45M-exome list is the best hunting ground this
   file has and it has been used in one direction only.
3. **Check whether any approved kinase inhibitor hits NRK off-target.** NRK is a GCK-IV STE20 kinase;
   its neighbours (MAP4K4, TNIK, MINK1) have inhibitors, and **TNIK inhibitors are themselves Wnt/TCF4
   agents** — cross-reactivity is plausible and cheaply checked against public kinome panels.
4. **Explain the DNMT3A/TET1 paradox** before TET1 advances.

---

## => WHAT I NEED

1. ⭐⭐ **The full `kosmicki2026` table — all 17 genes with β, carriers and class**, and ideally the
   207. **This is the highest-value document remaining and it outranks anything further on selamectin.**
2. ⭐ **Any kinome selectivity panel that includes NRK** (DiscoverX/KINOMEscan, Eurofins) — would tell
   us in one lookup whether an existing drug already hits it.
3. Still outstanding: **erda hand/wrist films**; **sitting height vs subischial leg length +
   ring-apophysis staging**; **NT-proCNP**; **liver fat**.

---

## CORRECTIONS

- ⛔⛔ **SPIN4 IS AT BACKGROUND IN GSE9160 — 1/10 probe-array cells against a threshold where COL2A1
  and ACAN read 10/10.** The atlas recorded this at R292 and I never checked it. **Every SPIN4 number
  I quoted from that dataset in R135, R138 and R143 is noise.**
- ⛔ **R143's TERM B2 IS WITHDRAWN** — and doubly so, because the Wnt panel it was correlated against
  is also at background (SP5 **0/10**, LGR5 1/10, AXIN2 on 1 of 4 probes). ✅ **R143's conclusion
  survives on Term B1 alone**, which is independent RummaGEO data with its own positive control.
- ⛔ **R138's "mouse-vs-human SPIN4 zonal conflict" IS WITHDRAWN — there was no conflict**, only a
  below-background probe read as a pattern.
- ⛔ **R135's SPIN-family zonal table is invalid** except SPIN1 (10/10, 1,595–3,910), which stands.
- ✅ **R138's Wnt-antagonist finding STANDS** — SFRP5, FRZB, DKK3, SFRP1 are all far above threshold.
- ⭐⭐ **STRUCTURAL: `kosmicki2026`'s endpoint is ADULT height, so all 17 genes are BONE-AGE-SURVIVABLE
  BY CONSTRUCTION** — the exact property R138 spent a round establishing for SPIN4 alone.
- ⭐⭐ **NRK NOMINATED as the replacement gene** — X-linked, viable KO, anti-proliferative
  ("prevents hyperplasia"), **+3.79 cm/allele in 1.45M exomes**, **10/10 in human growth plate**,
  **kinase**, and a **CK2-PTEN-AKT→mTORC1 route to N that is independent of Wnt** and therefore
  potentially additive. ⛔ **No inhibitor exists and no skeletal perturbation exists in any species.**
- ⭐ **TET1 nominated second** — +8.32 cm, enzyme, first "eraser" counterpart to SPIN4's "reader";
  ⛔ only a contested pan-TET tool compound, and an unexplained DNMT3A/TET1 direction paradox.
- ⛔ **The Stronghold EPAR is a dead end** — veterinary document, no human data, and the fetched PDF
  was a one-page stub.
