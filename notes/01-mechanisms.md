# Layer 3–4: The Controllers and the Feedback Loop

Running mechanism notes. Every claim is tagged to a paper actually read (full text `[FT]`
or abstract-only `[AB]` — flagged honestly, because the distinction matters).

**Scope note:** this is a mechanistic and clinical-evidence synthesis of published
literature. It is not a protocol and contains no dosing guidance. Doses appear only
as factual descriptions of what published studies administered. Several agents
discussed (MK-677/ibutamoren, GHRP-2/6, hexarelin, CJC-1295) are not approved for
growth indications in any jurisdiction and have no pediatric safety data.

---

## 1. The architecture, stated precisely

GH release from the somatotroph is governed by **three** inputs, not two:

| Input | Receptor | G-protein | Effect |
|---|---|---|---|
| GHRH | GHRH-R (class B GPCR) | Gs → cAMP → PKA → CREB | secretion **+** transcription (trophic) |
| Somatostatin (SRIF) | SSTR2 / SSTR5 (also SSTR3) | Gi/o → ↓cAMP, K⁺ hyperpolarization | tonic **brake** |
| Ghrelin / GHS | GHSR-1a | Gq/11 → PLC → IP₃/DAG → Ca²⁺, PKC | secretion; **functionally opposes the brake** |

The decomposition that makes the whole comparison tractable
(Bermann 1994 `[FT]`, citing Plotsky & Vale 1985; Tannenbaum 1989; Frohman 1990):

- **Pulse frequency** ≈ driven by phasic GHRH release.
- **Pulse amplitude** ≈ set by prevailing somatostatin tone at the time of the GHRH pulse.
- **Interpulse / basal GH** ≈ set by tonic somatostatin.

A GH pulse is therefore not "GHRH fires." It is **GHRH fires while the brake is off.**
Vance 1985 `[FT]` states the conclusion directly: GH pulses result from GHRH secretion
*associated with a diminution or withdrawal of somatostatin secretion.*

This is the single most important structural fact in the GH-vs-GHS comparison, because
the two drug classes act on different terms of that product.

---

## 2. Vance et al. 1985 — continuous GHRH does not clamp GH, and reveals a finite pool

Vance ML, Kaiser DL, Evans WS, Furlanetto R, Vale W, Rivier J, Thorner MO.
*J Clin Invest* 1985;75:1584–90. PMID **2860126**. DOI 10.1172/JCI111864. `[FT]`

Design: 6 healthy men, 24 h continuous IV hGRF(1-40) at 2 ng/kg/min vs vehicle, then a
supramaximal GHRH bolus (3.3 µg/kg) at 23.5 h. Plus one patient with an ectopic
GHRH-secreting tumor.

Findings:

1. **Pulsatility survived continuous GHRH.** GH remained pulsatile throughout the
   infusion, and in the ectopic-GHRH patient GH was pulsatile despite *continuously*
   elevated GHRH. Since the releasing signal was constant, the pulses must come from
   something else oscillating → **intermittent somatostatin secretion**. This is the
   foundational inference for the whole brake model.
2. Continuous GHRH *augmented* naturally occurring pulses rather than flattening them —
   explicitly contrasted with GnRH→gonadotropin, where continuous exposure downregulates.
3. **GH output during infusion: 1576 ± 284 vs 634 ± 151 µg** (p = 0.042) — a 2.5× increase.
4. **But the bolus response afterward was halved: 386 ± 125 vs 877 ± 170 µg** (p = 0.015).
5. **And total GH over the whole 25.5 h was not different: 1952 ± 383 vs 1504 ± 260 µg
   (p = 0.36).**

Point 5 is the one almost always missed. Sustained GHRH drive front-loaded GH release but
did **not** increase total integrated output once the reserve was probed. That is direct
human evidence of a **finite releasable pool with rate-limited refill.**

> **Therefore: "pool depletion" is a real, measured phenomenon — and the 1985 experiment
> demonstrates it for a *secretagogue*, not for exogenous GH.** This inverts the premise
> the comparison usually starts from and must be carried through the whole analysis.

---

## 3. Bermann et al. 1994 — IGF-1 feedback runs through the somatostatin brake

Bermann M, Jaffe CA, Tsai W, DeMott-Friberg R, Barkan AL.
*J Clin Invest* 1994;94:138–145. PMID **7913710**. DOI 10.1172/JCI117114. `[FT]`

Design: 6 normal **fed** men, 48 h rhIGF-I infusion (10–15 µg/kg/h), GH sampled q10min
for 24 h, plus GHRH (0.33 µg/kg) and TRH (50 µg) challenges on and off infusion.
IGF-1 rose 163.5 ± 9.3 → 452.0 ± 20.9 µg/L (~2.8×).

| Parameter | Saline | rhIGF-I | Suppression |
|---|---|---|---|
| Mean 24-h GH (µg/L) | 1.69 ± 0.47 | 0.29 ± 0.12 | **85 ± 3 %** |
| Pulsatile AUC | 2368 ± 651 | 365 ± 169 | **87 ± 2 %** |
| Mean pulse amplitude (µg/L) | 4.92 ± 1.01 | 1.12 ± 0.39 | **77 ± 4 %** |
| Maximal pulse amplitude (µg/L) | 21.50 ± 4.23 | 3.54 ± 1.57 | **85 ± 4 %** |
| Pulse frequency (/24 h) | 7.8 ± 0.9 | 4.7 ± 0.6 | p = 0.006 *(see note)* |
| **Non-pulsatile AUC** | 60.4 ± 29.4 | 47.0 ± 13.5 | **ns (p = 0.64)** |
| Nadir GH | 0.05 | 0.045 | ns |
| **GH response to exogenous GHRH** | 14.85 ± 5.22 | 2.34 ± 0.79 | **81 ± 5 %** |
| TSH response to TRH | 4.68 ± 0.46 | 3.33 ± 0.68 | 44 ± 9 % |

Mechanistic reasoning, which is unusually clean:

- The frequency drop is **an artifact**. Authors show that once amplitude falls 80%, small
  pulses sink below assay noise; correcting for the detection floor, the frequency
  difference vanishes (p = 0.15). So IGF-1 did **not** silence the GHRH pulse generator.
- The locus is identified by an elegant orthogonal probe: **TSH**. IGF-1 has no direct
  pituitary effect on TSH *in vitro*, but somatostatin suppresses TSH. TRH-stimulated TSH
  fell 44 ± 9%. Compare Williams 1988, where exogenous somatostatin infusion suppressed
  TRH→TSH by 43 ± 5% and GHRH→GH by 78 ± 5% — numbers the authors call "remarkably
  similar" to their own 44% and 81%.
- Conclusion: a rise in **hypothalamic somatostatin** fully accounts for the effect.
  No direct pituitary action need be invoked.

### The two consequences that decide the GH-vs-GHS question

**(a) Exogenous GH does not destroy the somatotroph; it raises IGF-1, which raises the
brake.** The suppression is a *functional*, hypothalamically-mediated, ligand-dependent
state — the pathway is intact and a somatostatin-independent stimulus should still reach
it. This is a reversibility claim and must be tested against withdrawal/retest data
(→ `02-withdrawal.md`).

**(b) High IGF-1 costs a GHRH-class secretagogue ~81 % of its efficacy.** The brake is
*upstream of and dominant over* GHRH signalling. Any intervention that raises IGF-1 —
including exogenous GH, and including a *successful* secretagogue — degrades GHRH-class
drive. **GHRH analogs are therefore self-limiting by construction.**

This generates the central falsifiable prediction of the whole review:

> **If a GHS acts by removing the somatostatin brake rather than by pushing GHRH, it
> should retain efficacy in a high-somatostatin state where a GHRH analog fails.**
> Mechanism predicts the two GHS classes are *not* interchangeable.

---

## 4. Testing that prediction

### Iranmanesh, Bowers & Veldhuis 2004 — the closest head-to-head
*J Clin Endocrinol Metab* 2004;89:4581–7. PMID **15356066**. DOI 10.1210/jc.2004-0205. `[AB]`

10 healthy men, 8 randomized separate-day sessions. Octreotide (SSTR-2/-5 agonist,
1 µg/kg sc) then bolus saline / GHRH / GHRP-2 / both.

| Condition | GH burst mass, no octreotide | with octreotide | Suppression |
|---|---|---|---|
| Saline (endogenous) | 2.7 ± 0.65 | 0.55 ± 0.11 | **~80 %** (p = 0.013) |
| GHRP-2 | 28 ± 3.2 | 18 ± 2.0 | **~36 %** (p = 0.045) |
| GHRH | — | — | burst mass only, p = 0.047 *(numbers in full text)* |
| GHRH + GHRP-2 | — | — | burst mass only, p = 0.047 |

Under a somatostatin clamp that removes ~80 % of endogenous GH secretion, **GHRP-2 keeps
~64 % of its drive and still produces ~33× the suppressed baseline.** The prediction in §3
survives its first test. Octreotide also reduced GHRP-2 pulse frequency (3.3→2.0) and
regularity, but affected *only* burst mass for GHRH — a qualitative, secretagogue-selective
difference.

⚠️ **The within-study GHRH-vs-GHRP-2 suppression percentages are the single most valuable
unretrieved number in this review.** → top of the pull-list.

### Veldhuis et al. 2006 — ghrelin is partly brake-independent
*J Clin Endocrinol Metab* 2006;91:2441–6. PMID **16537682**. DOI 10.1210/jc.2005-2718. `[AB]`

9 healthy postmenopausal women, randomized double-blind crossover; ghrelin bolus after
saline / L-arginine (presumed somatostatin withdrawal) / human CRH. Pulsatile GH rose
2.7 ± 1.0 → 20 ± 5.0 µg/L·3h with ghrelin. Authors conclude ghrelin activates pathways
**both dependent on and independent of somatostatinergic restraint**, and that its action
**resists inhibition by CRH** (a stress-like inhibitory signal). Consistent with §3.

### Rigamonti et al. 2001 — but the GHS pool depletes *within a session*
*Eur J Endocrinol* 2001;145:635–42. PMID **11720883**. DOI 10.1530/eje.0.1450635. `[AB]`

5 dogs; three consecutive boli of saline / GHRH / GHRP (EP92632) / both, at the end of
somatostatin-infusion-withdrawal cycles or during saline.

- GHRP alone produced a **larger** GH rise than GHRH alone.
- Somatostatin withdrawal **strikingly enhanced** the GHRP response → confirms the brake
  gates GHS output too.
- **Tachyphylaxis, explicitly:** the 2nd GHRP bolus gave a *smaller* peak, with only
  *partial* restoration by the 3rd. GHRH+GHRP showed "progressive reduction" across
  the 2nd and 3rd boli.
- Repeated somatostatin-withdrawal cycles, by contrast, gave **uniform** GH responses —
  which the authors read as mimicking the physiological pulse generator.

> **This is the counterweight to §2 and must not be softened.** Pharmacological GHS drive
> depletes a releasable pool within hours; endogenous brake-cycling does not. Any claim
> that GHS are "physiological" has to survive this result.

---

## 5. Where §2–4 leave the comparison

Established so far:

1. A GH pulse = GHRH drive × (brake off). Two different drug classes, two different terms.
2. A finite, rate-limited releasable GH pool exists and is demonstrable in humans —
   shown for a **secretagogue** (Vance 1985), and intrasession for **GHS** (Rigamonti 2001).
3. Exogenous GH suppresses the axis **functionally via hypothalamic somatostatin**, through
   IGF-1 — not by destroying somatotrophs. Reversibility is a separate empirical question.
4. Raised IGF-1 costs GHRH-class drive ~81 % of its efficacy → GHRH analogs are
   self-limiting.
5. GHRP-class drive is substantially **brake-resistant** (~36 % vs ~80 % suppression),
   so the two GHS classes must be analysed separately. "GHS" as one category is an error.

Open and load-bearing:

- **Does suppression reverse fully after exogenous GH stops?** (→ `02-withdrawal.md`)
- **Does the pool/somatotroph change structurally, or only functionally?**
  Note the contrast case: chronic GHRH excess causes somatotroph **hyperplasia**, which
  would mean a GHRH analog *grows* the pool rather than depleting it.
- **Does any of this reach the growth plate?** Level A (axis) ≠ Level B (plate). Pulse
  waveform only matters if the plate reads waveform. (→ `03-growth-plate.md`)
- **Does GHS tachyphylaxis compound over weeks-to-months**, as the acute dog data imply?
  (→ MK-677/LUM-201 long-term human data.)

---

## Corpus status

Full texts retrieved and read: PMID 2860126, 7913710 (+ 15286801, 11413165, 24606125 on disk).
Abstract-only, full text requested: 15356066, 16537682, 11720883, 12208658, 18073313,
15613434, 19088159, 11452249.
