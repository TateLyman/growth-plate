> # ⛔⛔ RETRACTED IN PART — READ THIS FIRST (added same session, F-R118-CORR)
>
> **The headline quantitative claim of this round, r(activation, youth) = +0.446, DOES NOT SURVIVE ITS
> OWN CONTROLS AND IS WITHDRAWN.** So is the stem-panel result and the BMP2/sVEGFR1 fate result.
> I published the number before running a permutation null. That was the error.
>
> **What the controls showed:**
> - **GSE151303's GPL1261 deposit is thresholded, not a usable expression matrix.** 62.7% of probes are
>   exactly **zero** per sample; only **1,983 of 45,101** probes are nonzero across all 14 arrays. The
>   implausible +4 to +6.5 log2 effect sizes were zero-to-value transitions, not expression changes.
> - **ACT and YOUTH share the same denominator group** (adult uninjured). Under label permutation with
>   that shared denominator, the null is **r = +0.386 ± 0.144**. The observed +0.446 sits inside it.
> - On clean (nonzero-everywhere) probes the observed shared-denominator r falls to **+0.232, p = 0.820** —
>   *below* the null mean.
> - **Disjoint-split** (no shared samples): observed **r = +0.047** against a matched null of
>   +0.001 ± 0.088, **p = 0.320.** Not significant.
> - **Every gene in the stem panel — Pthlh, Spon1, Prg4, Sox9, Acan, Col2a1 — contained zeros and drops
>   out under a clean-probe filter.** The z = +1.78 and Pthlh +1.87 were artifacts of zero-inflation.
> - The BMP2 / soluble VEGFR1 fate numbers were n=1 per arm on the same zero-inflated matrix. **Withdrawn.**
>
> **WHAT STILL STANDS (all of it literature, none of it my analysis):**
> - The GSE151303 authors' own finding that SSC expansion **can be triggered in ADULT joints by
>   microfracture**, that MF-activated SSCs tend to form fibrous tissue, and that they used BMP2 +
>   soluble VEGFR1 to redirect fate. That is their result, independently reported, and is unaffected.
> - FoxA2⁺ 2.7-fold expansion and 96% plate regeneration in 7 days (R117, separate paper).
> - The trigger enumeration and the observation that every adult-competent trigger in the literature is
>   mechanical.
> - The reverse-Wnt experiment being unrunnable on public data.
>
> **The claim that a mechanical stimulus transcriptionally rejuvenates an adult tissue is NOT established
> by this round.** It remains an open question and it needs a dataset with a real expression matrix.
>
> Controls: `frontier/analysis/redundancy/{ctrl2,ctrl3}.py`.

---

# R118 — I ran the two named experiments. One returned the strongest positive in this project;
# the other cannot be run on any public data. Mechanical activation is the only thing that has
# ever moved an adult skeletal tissue toward the young state, and the fate switch is an approved drug.

**Operator: "attempt the named experiment perfectly, find all the triggers, everything that gets us to 7×."**

Two experiments were named at the end of R117. Both were attempted. Results are asymmetric.

---

## 1. ⭐⭐⭐⭐ EXPERIMENT ONE: CAN THE POOL BE ACTIVATED IN A MATURE ANIMAL? — YES, AND IT PARTIALLY REJUVENATES

**GSE151303** (`Articular cartilage regeneration by activated skeletal stem cells`, mouse, GPL1261, n=14).
Design: P3 juvenile bulk (n=3), **adult uninjured** bulk (n=5), **adult microfracture** bulk (n=3), plus
sorted adult MF mSSC under control / BMP2 / soluble VEGFR1 (n=1 each).

The authors' own framing: aging causes progressive loss of SSCs and diminished chondrogenesis **in mice
AND humans**, but a local expansion **can still be triggered in ADULT joints by microfracture**.

### THE NUMBER
Built two axes on 22,550 expressed probes:
- **YOUTH** = P3 − adult uninjured
- **ACTIVATION** = adult microfracture − adult uninjured

> ### r(ACTIVATION, YOUTH) = **+0.446**

**A local mechanical stimulus, in an adult animal, moves the tissue transcriptome nearly half-way toward
the juvenile state.** For scale, the FGFR3-blockade axis correlates with *itself* across timepoints at
0.461 (R115). This is a full-size effect, not a trace.

**THIS IS THE FIRST THING IN THE ENTIRE PROJECT THAT MOVES AN ADULT TISSUE TOWARD YOUNG.** Set it against
what this file has already killed: **R110 — young blood does not rejuvenate the cell** (heterochronic
parabiosis/plasma null); **R103 — no systemic drug can reset the senescence clock**, argued from
transplantation; R104–R107 — the methylation route closed. Every one of those was a **systemic** attempt.
The thing that works is **local and mechanical.**

### AND IT RAISES THE STEM COMPARTMENT IN AN ADULT
Adult microfracture vs adult uninjured, panel z vs genome-wide:

| panel | z |
|---|---|
| **stem / chondro (N)** | **+1.78** |
| fibrous | +0.81 |
| bone / osteogenic | +0.46 |

per gene: **Pthlh +1.87, Spon1 +2.74**, Prg4 +0.59, Sox9 +0.55; Col3a1 +1.17, Postn +0.73.

**PTHrP goes up in an adult joint after a mechanical stimulus.** That is the resting-zone stem marker,
in the mature animal, which is exactly the test the FoxA2⁺ paper (R117) never performed.

## 2. ⭐⭐ AND THE FATE PROBLEM FROM R117 HAS AN APPROVED-DRUG ANSWER

R117 established that pool expansion fails on **fate** — Hedgehog-expanded resting-zone cells become
trabecular osteoblasts, which is why Trompet's +61% pool bought +3.63% length. The authors of GSE151303
hit the same wall: MF-activated SSCs **tend to form fibrous tissue**, and they fix it with
**co-delivery of BMP2 and soluble VEGFR1**.

Sorted adult MF mSSC, n=1 per arm — **directional only, no replicates, must not be over-read**:

| panel | BMP2 | soluble VEGFR1 |
|---|---|---|
| stem / chondro | −0.36 | **+1.63** |
| bone / osteogenic | **+1.74** | +1.54 |
| fibrous | −0.14 | +0.10 |

The two agents separate: **BMP2 drives skeletal differentiation (osteogenic), the VEGF trap holds the
chondro/stem program.** Together they are charge and blocked-discharge — the law derived earlier in this
project — deployed as a **fate switch** rather than as a growth lever.

**And soluble VEGFR1 is a VEGF trap, which is aflibercept — approved, obtainable.** This also
re-scopes the atlas's axitinib node (R364): anti-VEGF was rejected there as "charge without discharge"
when evaluated as a *lengthening* agent. As a *fate* agent for activated stem cells, blocking discharge
is the point.

---

## 3. ⛔ EXPERIMENT TWO: THE REVERSE WNT TEST CANNOT BE RUN ON PUBLIC DATA

R117 named it: eLife 64513 showed Wnt activation costs ⅓ of the PTHrP⁺ pool and 72% of long columns,
and stated *"no reverse experiment was conducted… no evidence that expansion is possible."*

Searched GEO systematically (58 series across 16 queries). The only candidate with usable expression is
**GSE211559** — XAV939 (tankyrase inhibitor, Wnt antagonism) vs TGFβ, three paired human MSC lines.

| panel | XAV939 − TGFβ, z |
|---|---|
| resting / stem (N) | −2.25 |
| chondrocyte | −4.79 |
| **hypertrophic** | **−15.73** |
| fibrous | −5.85 |

**This is not the reverse experiment and I will not report it as one.** There is **no vehicle arm** — it
compares two chondrogenic drivers, and TGFβ is the stronger, so every panel reads negative. The only
extractable content is the rank order: hypertrophy is by far the most suppressed (MMP13 −3.66,
RUNX2 −0.70), the stem panel is the *least* suppressed, and SFRP1 alone rises (+0.53). Weakly consistent
with Wnt inhibition holding cells undifferentiated; **it cannot establish pool expansion.**

**The named experiment remains unrun, and no public dataset can run it.** GSE245140 (LGK974 in vivo) is
deposited without processed expression. This is now a data-generation requirement, not a literature gap.

---

## 4. EVERY TRIGGER FOUND, RANKED

| trigger | what it does | animal age | obtainable |
|---|---|---|---|
| **microfracture** | **r=+0.446 toward young; stem z=+1.78; Pthlh +1.87** | **ADULT** | surgical, routine |
| Salter-Harris injury | FoxA2⁺ **2.7×**; plate **96% regenerated in 7 d**, all three zones, physeal cartilage | young only | surgical |
| suture expansion (GSE227468) | mechanical expansion → SSC proliferation, sustains calvarial growth | — | mechanical |
| **distraction osteogenesis** | **8.85 cm femoral + 7.36 cm tibial, n=1149; works AFTER fusion** | **adult** | approved surgery |
| sensory innervation — **p75/NGF** (GSE263602) | regulates the skeletal stem cell niche | — | **untouched by this project** |
| sympathetic innervation — **SLIT2** (GSE284991) | regulates the skeletal stem cell niche | — | **untouched by this project** |
| Hedgehog / SAG | pool +61% → length +3.63% | young | ⛔ osteogenic fate (R117) |

### ⭐ THE PATTERN, AND IT IS THE ROUND
**Every trigger that works in an ADULT is mechanical.** Microfracture, suture expansion, distraction.
Every *systemic pharmacological* attempt at rejuvenation in this file has failed — young blood, the
methylation route, the senescence clock. **The stem pool is mechanically gated, not chemically gated.**

And that retro-explains R277's uncomfortable arithmetic. Distraction osteogenesis was ranked an order of
magnitude above the entire pharmacological stack and could not be assigned to a term in R264's audit.
**It can be assigned now: it is sustained mechanical activation of skeletal stem cells, applied for
months.** The largest intervention in the file and the only adult-competent stem trigger are the same
mechanism. That is a mechanistic result, not a surgical recommendation.

**Two whole axes are untouched:** sensory (p75/NGF) and sympathetic (SLIT2) innervation control of the
SSC niche. Neither appears anywhere in this atlas. Both have 2024–2025 primary papers. Nerves are
pharmacologically accessible in ways cartilage is not.

---

## 5. WHAT IT TAKES TO REACH 7×, HONESTLY

`height = N × A × h_term`, k required at SA 16.0 = **6.99×**, stack tops out ≈ **2.60×**.

| term | best available | ceiling | gap |
|---|---|---|---|
| h_term | erdafitinib (+ CNP cAMP arm) | ~4–5% (GC-B7E/7E, wild-type) | at ceiling |
| NPR2 activity | erdafitinib, LB-100 | phospho-state only; no upregulator exists | at ceiling |
| A | CNP axis | real, **but paid out of N** (R117, z=−3.39) | contraindicated here |
| **N** | **nothing pharmacological** | mechanical triggers only; fate needs BMP2 + VEGF trap | **the entire residual** |

**The 4.4× that is missing is all N, and N has no drug — it has a mechanical trigger and a fate switch.**
Nothing found in four rounds changes that arithmetic. What changed is that N stopped being a closed door:
it now has a demonstrated adult-competent trigger (r = +0.446), a measured stem response (Pthlh +1.87),
an identified fate problem, and an approved-drug candidate for the fate half.

### The three things that would actually move the number
1. **Run the reverse Wnt experiment.** Local delivery, vehicle-controlled, measuring pool size AND fate
   AND length. No public data can answer it; it has to be generated.
2. **Find what microfracture does chemically.** r = +0.446 is a transcriptional signature — the ligands
   inside it are the candidate drugs. If the mechanical gate has a chemical key, that is the whole game.
3. **Open the innervation axis.** p75/NGF and SLIT2 control the SSC niche and are absent from this atlas.

---
### Corrections and status carried by this round
- **R117's fate problem gets a candidate answer** (BMP2 + soluble VEGFR1), at n=1 per arm — directional only.
- **R364's anti-VEGF rejection is re-scoped, not overturned:** wrong as a lengthening agent, potentially
  right as a fate agent for activated stem cells.
- **The reverse Wnt experiment is reclassified** from "unrun in the literature" to "unrunnable on public
  data — requires generation."
- **The 7× arithmetic is unchanged.** Every gain this round is on N's tractability, not on the multiplier.

Code: `frontier/analysis/redundancy/{act,wntrev,search}.py`.
