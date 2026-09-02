# F-R032 — Output is conjugate to the pool, one cell for one cell, and that is an identity

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** the three-term problem reduces to a single inequality; two atlas rounds were each half right

---

## 0. What is new in this round

Two documents that this programme had never read:

1. **`chu2026` supplement — read for the first time.** `Sci. Transl. Med.` 18, eadw3590 (2026),
   DOI `10.1126/scitranslmed.adw3590`. Figures **S1–S10**, **Table S1**, and the full Methods. The atlas
   named this document, in `round240`'s own words, *"PAYWALLED, figures never read here, and **the
   highest-value unobtained document**."* Tate supplied it. It corrects the atlas's record of what the
   paper shows.

2. **`chu2025` full text — PNAS, PMID 41289405, PMC12685065, DOI `10.1073/pnas.2512316122`,
   2 December 2025.** Open access via Europe PMC. The atlas held its abstract at round 240; the results
   section carries the measurement that closes the argument.

Together they let me state the answer to *fast + unbounded + non-closing* as a single inequality, and to
show that **`round240` and `round247` were each half right and each stopped one line early.**

---

## 1. The identity

`round247` wrote down two lines of algebra this programme had never written, and they are correct. Under
population asymmetry, a stem division has three outcomes — symmetric renewal (2 stem, 0 committed),
symmetric loss (0 stem, 2 committed), asymmetric (1 each). If symmetric renewal and symmetric loss are
**equally probable at `r`**, then

```
E[Δstem]      = r(+1) + r(−1) + (1−2r)(0) = 0
E[committed]  = r(0)  + r(2)  + (1−2r)(1) = 1      ← for every r
```

`r` cancels. `round247` concluded: *"THE SELF-RENEWAL FRACTION IS A DISPERSION PARAMETER, NOT A
PRODUCTION PARAMETER… the fraction is not in the equation."* Height was rewritten as
`∫ λ·N·A·h_term dt`, and the finite term was named **N**.

**That is right, and it is right only because the premise imposed neutrality.** Setting
P(renewal) = P(loss) = `r` *is* the definition of neutral drift. It is the assumption, not a result.

**And the whole point of `chu2025` is that GH breaks that equality.** Verbatim:

> *"GH reduces the pool of slow-cycling, label-retaining stem cells **by promoting their differentiation
> into transient progenitors**."*
> *"…that **GH promotes their committed cell division, leading to stem cell depletion**."*

So let symmetric renewal have probability `a` and symmetric loss `b`, with `a ≠ b`. Then:

```
E[Δstem]      = a − b
E[committed]  = 2b + (1 − a − b) = 1 + (b − a) = 1 − E[Δstem]
```

**`E[committed] + E[Δstem] = 1`, exactly, for all `a`, `b`.**

This is a conservation identity, not an empirical finding. It says:

> **Every committed cell produced above the neutral rate of one-per-stem-division is subtracted, one for
> one, from the stem pool.** Output above neutral is not *paid for by* pool loss. Output above neutral
> **is** pool loss, in the same cells, counted twice.

The atlas has been calling this "the exchange rate" and pricing it empirically since R198. **It has no
exchange rate. It is 1:1 and it is arithmetic.** No agent, no niche, no species will ever get a better
price, because there is no price — there is an accounting identity.

`round247` was therefore right that `r` cancels and **wrong to conclude that the fraction is not in the
equation**. The *neutral* parameter `r` cancels. The **asymmetry `a − b` does not cancel; it is the pool
derivative, and it is conjugate to output one-for-one.**

`round240` named "the self-renewal fraction" as the controllable variable and was right about *which
quantity matters* and wrong about *which fraction* — it is not `r`, the dispersion, but `a − b`, the
imbalance.

---

## 2. What that does to the objective function

`round247`'s `Height = ∫ λ·N·A·h_term dt` holds **N as a parameter**. N is a state variable. Restoring
its dynamics:

```
dH/dt  =  λ · N · A · h_term
dN/dt  =  λ · N · (a − b)  +  influx
```

Three regimes, and every one of them is occupied by a real intervention:

| regime | N(t) | H(t) | occupied by |
|---|---|---|---|
| `a < b`, influx 0 | decays exponentially | **saturates** at `N₀·A·h_term / (b−a)` | **pharmacological GH; oestrogen; puberty** |
| `a = b`, influx 0 | constant | linear in t — unbounded only if the plate stays open | the neutral plate `chu2025` measured, 1–6 months |
| `a > b` **or** influx > 0 | grows | **superlinear — unbounded and accelerating** | **nothing in clinical use.** Nearest: `trompet2024` |

**The bounded regime is where all of medicine sits.** That is the formal reason the field returns
percentages, and it is a stronger statement than F-R019's cancellation theorem: cancellation was a claim
about compartments having opposite signs, which is contingent. This is conservation, which is not.

**The solution condition for all three terms at once:**

> ### `influx ≥ λ·N·(b − a)`, with ER signalling blocked, and λ·N large.

Held with equality, the pool is stationary at any velocity — **fast and non-closing**. Held with strict
inequality, the pool grows and velocity rises with it — **fast, non-closing, and unbounded.** Term A
(never close) is the ER clause; F-R028/R029 established it is solved in humans at the receptor level and
is a knife edge at the ligand level.

Note what the inequality demands. The right-hand side **scales with the drive**. Every velocity lever
raises `λ` *and* drives `a − b` negative, so it inflates the RHS twice over. **Influx cannot be a
pre-treatment. It must be co-dosed and titrated proportionally to the drive.** That is a control-theory
statement and it is the thing nobody has done: `trompet2024` fired one Hedgehog pulse and stopped; the
entire GH literature raises `λ` with no influx term at all.

---

## 3. The escape: λ is conjugate to the pool, N is not

Output is `λ·N·A·h_term`. The identity in §1 prices `λ`, because `λ` is the *stem division rate* and the
identity is per stem division. **It does not price `N`.**

> **Doubling `λ` doubles output and doubles the rate at which the pool is spent.
> Doubling `N` doubles output and spends nothing extra per unit output.**

A plate with 10× the stem number at unchanged `λ` grows ten times as fast and pays exactly the same 1:1
rate on each division it makes. **"Fast" must be bought in N, not in λ.** Every drug the field has
targets λ. That single substitution is the answer to Term C, and it survives the identity because the
identity is denominated per division and N is a count of dividers.

**Three independent confirmations that λ-levers do not produce height, all in this round's documents:**

**(a) Cell-cycle acceleration in the transit-amplifying zone gives nothing at steady state.** `chu2026`
fig. **S10T**: GH raises the S+G2M fraction of **GP3** (the proliferating cluster) from **~14% to ~45%,
χ², p < 0.0001** — a 3.2× acceleration. Fig. **S10V**: the KEGG signature is *DNA replication, cell
cycle, homologous recombination, cellular senescence*. Pure replication program.

And fig. **S8C**: **explant length after two months of that, P = 0.1827, n = 5 paired patients.**

The reason is in the algebra. `A` is a **count** — the number of amplification divisions a committed
daughter undergoes before exit — not a rate. Accelerating the execution of a fixed count changes *when*
cells emerge, not *how many* per stem division. At steady state, output = `λ·N·A` regardless of how fast
the A divisions are run. **Tripling proliferative-zone cycling cannot raise height. It produces a
transient and then nothing.** That kills the entire class of cell-cycle levers, and `chu2026` measured
it and did not draw the conclusion.

**(b) GH depletes the pool without dividing it faster — and the SI Appendix measures the transfer
directly.** `chu2025`, PTHrP-mCherry reporter, GH 5 mg/kg/d i.p. P28→P38, n = 6/group: PTHrP⁺ stem cells
**reduced, P < 0.0001**. Independently, **CD73⁺ cells 283 → 220 per mm of growth plate, P < 0.001,
n = 7 vs 6** (fig. S5F) — a 22% pool reduction in ten days. p-STAT5 co-localises with both mCherry and
CD73 (S5G, H), so the signal is received in the stem cells themselves.

And the rate term does not move: **Ki67⁺/mCherry⁺ = 22.2% → 19.3%, n.s.** (fig. S5C), with the main text
adding *"**EdU incorporation in mCherry+ cells was unchanged** between vehicle and GH-treated groups…
high doses of GH reduce the number of stem cells in the growth plate, and **this effect is not
attributable to altered proliferative activity**."*

**Then fig. S6 stratifies the clones, and it is the identity read off a graph.** Femoral plate,
PTHrP-CreERT2:R26R-tdTomato, n = 5/group, vehicle → GH:

| clonal outcome | vehicle | GH | change | statistic |
|---|---|---|---|---|
| **singlets** (labelled cell retained, not recruited) | 47.4% | 37.6% | **−9.8 pp** | **p < 0.01** |
| **dyads** (one division) | 38.7% | 40.4% | +1.7 pp | **n.s.** |
| **long columns** (recruited, ran the amplification series) | 7.4% | 16.1% | **+8.7 pp** | **p < 0.001** |

**GH converts retained stem cells into committed columns, −9.8 against +8.7, with the intermediate class
untouched.** That is `a` down and `b` up with `1 − a − b` conserved — probability mass moved from the
pure-renewal outcome to the pure-commitment outcome, leaving the asymmetric outcome alone. And the
asymmetric outcome is precisely the one the identity says is fate-neutral (one committed, zero net stem
change). **The class the arithmetic predicts should not move is the only class that did not move.**

The pool falls by **conversion, not by exhaustion through division**: `λ_stem` flat, `a − b` negative.
This is the identity operating in isolation with the rate term held still, and the exchange is visible as
a near-exact one-for-one transfer between two clonal classes.

**(c) It is the same arithmetic as oestrogen, from the opposite side.** The atlas's
`rz_depletion_causes_fusion.yaml` records oestrogen draining the pool because *"the OUTFLOW is unchanged
while the INFLOW falls."* GH drains it because the outflow rises while the inflow is unchanged.
`nilsson2014` (via `round247`): oestrogen's effects on **growth rate, proliferation rate and hypertrophic
cell size are reversible** on withdrawal; its effect on **resting-zone chondrocyte number is not**, and
*"did not appear to be due to apoptosis"* — the cells left by commitment.

**Oestrogen and GH are the same lever with opposite handles.** Both drive `a − b` < 0. Both are, in the
end, closure agents. **Fusion is not a separate program: fusion is `a < b` integrated to N = 0.** Terms A
and C are not two problems. They are one variable.

---

## 4. `chu2026`'s figures correct the atlas's record of `chu2026`

`round240` recorded, from the abstract alone:

> *"chu2026 reports GH acting directly on human growth plate explants… and **STIMULATING PROLIFERATION OF
> BOTH CARTILAGE STEM CELLS AND PROLIFERATIVE-ZONE CHONDROCYTES**."*

**The first half of that is not supported by the paper's own quantification.** Every stem-compartment
endpoint in the supplement is null, and every one of them trends the wrong way:

| endpoint | figure | vehicle → GH | statistic |
|---|---|---|---|
| **GP2** (PTHrP⁺ working stem tier) S+G2M | S10T | 22.5% → 23% | no change |
| **GP3** (proliferating) S+G2M | S10T | 14% → 45% | **χ², p < 0.0001** |
| RZ **CYTL1⁺** cells, 24 h | S9C | 26% → 15% | **n.s.** (trends down) |
| RZ **RAMP3⁺** cells, 24 h | S9F | 21% → 22% | **n.s.** |
| RZ **SOX9⁺** nuclei, 2 mo | S8Q | 85% → 63% | **P = 0.79** (trends down) |
| PZ SOX9⁺ / HZ SOX9⁺, 2 mo | S8Q | — | P = 0.99 / P = 0.65 |
| Cyclin D1⁺, plate-wide, 24 h | S9L | 15% → 33% | **P = 0.0101** |
| MEF2C⁺, 24 h | S9O | — | **n.s.** |
| LARS2⁺, 2 mo, by zone | S8S | up | P = 0.13 / 0.09 / **0.04** |
| **explant length SOC→PS, 2 mo** | **S8C** | **1254 → 1520 µm** | **P = 0.1827, n = 5 paired** |

Read the structure, not the individual rows. **Every readout quantified *specifically in the resting
zone* is null. The one proliferative readout that is positive (Cyclin D1, P = 0.0101) is quantified
plate-wide.** That is the same dissociation as the main text's zone-split EdU — **PZ P = 0.013, RZ
P = 0.79** — and the same as `chu2025`'s mouse result. Three independent readouts, two species, one
conclusion: **GH acts on the transit-amplifying compartment and not on the stem compartment.**

Two further marks of the same retreat. The **bioRxiv preprint** (2025.03.14.642964) is titled *"…reveals
**direct stimulation of cartilage stem cells** by growth hormone."* The published title is *"…reveals two
populations of stem cells and **direct effect** of growth hormone."* And the companion PNAS paper, from
the same first author and the same lab, states the opposite outright — and **reverses the lab's own 1992
result**, with the original author still on the byline:

> *"Based on the earlier experiments showing that GH increases the number of LRCs (22), we were expecting
> that GH would promote the number and activity of cartilaginous stem cells. **Unexpectedly, GH treatment
> led to a decrease** in stem cell number as well as in the number of LRCs."*

Reference 22 is **Ohlsson, Nilsson, Isaksson & Lindahl, *"Growth hormone induces multiplication of the
slowly cycling germinal cells of the rat tibial growth plate."*** **Ohlsson is a co-author of the 2025
paper that overturns it.** That is a genuine self-correction by the field, and the atlas's "counterweight
that must be carried" at round 240 — the abstract-level claim that `chu2026` showed human stem-cell
stimulation — **can now be set down.** The human data agrees with the mouse data. The counterweight was
an artefact of reading an abstract.

**What the atlas got right and should keep:** the round-240 claim *"pharmacological growth hormone
depletes the growth plate stem cell pool"* (grade C) is now supported in **human tissue** as well as
mouse, and should rise. Its stated uncertainty — *"the direction is DOSE- AND CONTEXT-DEPENDENT"* — is
confirmed by the authors in terms worth recording verbatim, because a sign that flips with dose is a
control variable:

> *"it is plausible that GH augments both stem cell number and activity **under physiological
> conditions** but causes stem cell depletion **under pharmacological exposure**."*

---

## 5. Two things the supplement contains that nobody has used

**(a) Resting-zone height does not distinguish tall children from normal-height children.** Fig. **S2L**,
*"Archived Samples (resting zone height)"*: two children with **idiopathic tall stature** (#29, #28)
beside four **normal-height** children having leg-length correction (#20, #22, #17, #11). The legend:
*"**both showing a prominently enlarged resting zone**."* The authors ran it as a control against a
tall-stature sampling artefact. Read as an experiment, it says: **RZ height is not what makes a tall
child tall.**

That is a direct hit on `RESERVE × h_term`. Either RZ height is a poor proxy for N, or N is not what sets
human height. It is unquantified, n = 2 vs 4, and both groups are mid-puberty with growth remaining — so
it is a **lead, not a result**. But it is the only human tall-versus-normal growth-plate histology
comparison I have found, and it points the same way as §3(a): **static compartment sizes do not predict
human height; rates and durations do.**

**(b) The pool is a zero-sum compartment over the window measured.** `chu2025`, Col2-CreERT2:R26R-Confetti
pulsed at 1 month, 6-month chase: clone sizes normalised at each time point *"followed an **exponential
distribution** (Fig. 4F and G), consistent with **neutral stem cell competition**."*
*"This pattern is characteristic of **stochastic drift in a zero-sum system**, commonly modeled as a
Markov process."*

Exponential clonal scaling is the signature of neutral drift in a **fixed-size** compartment. Over
1–6 months of mouse age, the stem compartment behaved as though it had a **fixed number of slots** — a
cell enters only as another leaves. If that is the cap, then **N is limited by niche slots, not by cell
behaviour, and no cell-intrinsic lever can raise it.** You would have to build slots.

That is a hypothesis with a sharp and testable consequence — **slot count should scale with the plate's
cross-sectional area** — which connects Term C to F-R023's pressure vessel and to the groove of Ranvier's
latitudinal role, and would say that widening a plate raises N without touching `a`, `b`, or `λ`. **I am
recording it as a hypothesis and not more.** Exponential scaling over a window in which the mouse plate
is already ceasing to expand is consistent with a fixed compartment but does not prove a hard cap.

---

## 6. The lead I will not overstate

`chu2025`'s discussion names a mechanism for `a − b` itself:

> *"The **planar cell polarity (PCP)** pathway is one of the most important regulators of **symmetric vs.
> asymmetric stem cell division**."*

If PCP sets the division plane, and the renewal-versus-commitment outcome is a matter of spindle
orientation relative to the niche, then **PCP is a handle on `a − b` that is physically separate from the
cell-cycle machinery that sets `λ`** — Cyclin D1, STAT5. That separation is the whole game: **the
coupling between `λ` and `a − b` is regulatory, not thermodynamic, and a regulatory coupling can be
broken.** They even stained γ-tubulin.

**But the citation does not support the claim, and I checked rather than assuming.** The paper `chu2025`
cites is **Li, Li, Junge & Bronner, *eLife* 2017;6:e23279 (PMID 28994649, PMC5634781)** — chick limb
cartilage, PCP enabling a post-division **pivot** that stacks sister cells into a column via N-cadherin.
I pulled the full text and counted: **"self-renewal" appears 0 times**; "fate" once, in the introduction,
describing *Drosophila* spermatogenesis as a general illustration; and every occurrence of "stem" and
"asymmetric" is in that same introductory framing or in the reference list. **Vangl2 appears 18 times.**

**The paper contains no stem-cell fate data at all.** It is about column architecture and division
orientation. PCP-as-`a−b`-lever is a hypothesis Chu floats in a discussion, supported by a citation about
a different thing. I am flagging it because it is the most promising unworked lead in the round, and
flagging equally that **it is currently unsupported.** (I made exactly this error in F-R022 with
`fenichel2006`; this time I read the citation before repeating it.)

What survives the check is narrower and still useful: PCP demonstrably controls **division orientation
and the pivot that builds a column** in cartilage. Whether orientation relative to the niche *is* the
renewal/commitment decision in the resting zone is unmeasured — and it is a well-posed experiment, since
`chu2025` already has the clonal stratification (singlets / dyads / long columns, fig. S6) that would
read the answer out.

The atlas is not blank here — 26 files mention planar cell polarity, 34 Vangl, 51 Wnt5a — but
`oriented cell division` appears in 9 and `division plane` in 8, and I have not yet read whether any
node connects PCP to the renewal fraction rather than to column architecture. **That is the next read.**

---

## 7. The platform, stated exactly, because it is now the bottleneck

`chu2026` Methods, verbatim — the human growth plate maintained **two months** in a 6-well dish:

> Cylindrical biopsies from epiphysiodesis, sectioned **perpendicular to the longitudinal axis into 1–2 mm
> slices** in HBSS. *"To obtain slices containing the secondary ossification centre (SOC), the growth
> plate, and the primary spongiosa… slices with POC or SOC only were **excluded**."*
> Medium: **DMEM/F12 (no phenol red), gentamycin 20 µg/ml, 0.2% BSA, β-glycerophosphate 1 mM, ascorbic
> acid 5 µg/ml, 2% FBS.** 37 °C, 5% CO₂. **Medium replaced every 2–3 days, 3 ml per well.**
> Long-term: **± 40 ng/ml recombinant human GH (Norditropin) for 2 months.**
> Short-term: **± 40 ng/ml GH for 24 h.**
> Cohort: **ten patients aged 11–14**, both sexes, **Tanner B1–B4 / G2–G4**, proximal tibia + distal
> femur, Karolinska ethics permit **97-214**. (Table S1.)

Three observations that matter more than the protocol.

**(i) The preparation has no influx source.** A cylindrical core taken through the centre of the plate
under X-ray guidance does not contain the peripheral groove of Ranvier. **The explant is the reserve
compartment with the perichondrial source surgically removed** — `influx = 0` by construction. Under §2
that puts it permanently in the bounded regime. It is the right rig for measuring the identity and the
wrong rig for escaping it.

**(ii) The culture itself halves the cycling fraction.** Fig. **S10K**: native **14.2%** in S+G2M →
**8.4%** after 24 h in culture, **p < 0.0001**. The rig runs at ~60% of in vivo drive before any drug is
added.

**(iii) It is normoxic.** 5% CO₂ in a standard incubator is ~18.6% O₂ at the medium surface. Brighton's
zone map puts the proliferative zone at **6.0–7.0%** and the hypertrophic at **2.1–2.2%**. The explant
runs the proliferative zone at ~3× and the hypertrophic at ~9× their native pO₂, and above the ~8%
proteoglycan/collagen switch (`li2014`, F-R015). **Every result in this paper was obtained in a plate
held on the wrong side of that switch** — and F-R016 says normoxia trades duration for velocity. This is
directly testable in the rig as published, by changing one incubator setting.

**And the one measurement, absent, that would have decided the paper.** Fig. S8C is a paired test on
**absolute** plate height at two months with **no day-zero baseline** — yet the design had spare slices
from each biopsy, explicitly allocated *"for either immediate analysis… or for explant culture."* A t = 0
slice from the same patient would have converted a total dominated by inter-patient baseline (730 →
1930 µm across five donors) into an **increment**, which is what the experiment was asking about. Means
were 1254 → 1520 µm, +21%, with 3 of 5 pairs up, 1 flat, 1 down.

> **The highest-value missing measurement in the field's best human platform is a day-zero plate height,
> and it costs nothing.**

I am not claiming the null means GH does nothing to human plate length. I am claiming the experiment as
designed **cannot detect the effect it was built to test**, and that a 3.2× acceleration of proliferative
cycling failing to produce a detectable two-month length change at n = 5 puts a **low ceiling** on what
λ-levers buy — which is what §3(a) predicts on independent grounds.

---

## 8. Where the three terms stand

| term | status | what holds it |
|---|---|---|
| **A — never close** | **solved, both directions, in humans** | receptor-level ER disruption survived a 10× oestradiol challenge (`smith2008`); 25 µg transdermal E2 twice weekly fused a 31-year-old in 6 months (`imre2025`). Durable at the receptor, knife-edge at the ligand |
| **B — cells remain / unbounded** | **mechanism identified, condition stated** | `influx ≥ λ·N·(b−a)`. Influx is real, demand-responsive, with a named throttle (Hh/PTCH1/Gli1), brake (CCN2), steering (heparan sulfate) and source (Pdgfrα⁺ inner perichondrium). **Never co-dosed with a drive lever. Never fired twice.** |
| **C — fast** | **rerouted, not solved** | must be bought in **N**, not `λ` — the identity prices λ at 1:1 and does not price N. `trompet2024` is the only intervention that raised N (+61% PTHrP⁺) and `λ` together with a durable contralateral length gain. Whether N has a niche-slot cap (§5b) is undetermined |

**What changed this round:** Term C stops being "find a stronger accelerator." Every accelerator is
priced by the identity, and the price is total. Term C becomes *"raise the number of dividers"* — which
is the same lever as Term B. **Terms B and C collapse into one, and Term A is the clause that keeps a
transient shortfall from becoming permanent.** One inequality, three terms.

---

## 9. Asks — ranked by what they would settle

1. **`trompet2024`'s second pulse.** Still the single decisive unperformed experiment, and it is now
   sharper: the identity says a one-off N gain pays out linearly and stops, while a repeated N gain
   compounds. **Does SAG dosed a second time add a second +61%, or does the plate return to a slot
   count?** §5(b) predicts the latter and I want it falsified. Related and newly relevant: the reported
   **age dependence** of systemic SAG — early postnatal suppressed, late promoted — needs its primary
   source pinned.
2. **~~`chu2025` SI Appendix~~ — obtained and read this round.** Europe PMC supplementary bundle for
   PMC12685065. It supplied fig. S5C/S5F and, unexpectedly, **fig. S6** — the clonal stratification that
   turned §3(b) from a quotation into a measurement. Nothing further needed from it. Also in the bundle
   and unread: **Movies S1–S2**, light-sheet renderings of whole cleared tibiae (control vs GHR cKO
   PTHrP), the source of the 31 ± 8 vs 15 ± 4 columns-per-tibia count.
3. **`horike2026`** — the FGFR3-ACH knock-in with **CREB** as effector and **666-15** restoring bone
   length. Round 240 flagged it as the one druggable node downstream of FGFR3, and it reports
   **randomised clonal stack angles** — which is the PCP/division-orientation phenotype of §6, in a
   mammal, with a rescue compound. This is where the `a − b` lead and the atlas's existing FGFR arm meet.
4. **~~Li, Li, Junge & Bronner, *eLife* 2017~~ — obtained and read this round.** Chain closed in §6:
   the citation does not support the claim it is attached to.
5. Standing, unchanged: Brighton thesis (UIC INDIGO `10027/14248`, restricted); **JBJS 1980;62A:740**
   (Stambough & Brighton, zonal diffusion); **Surgical Forum 1970:465–467** (PMID 5383117);
   `stegen2019` DCA+BPTES tibia length.

---

## 10. Corrections carried

- **To `round247`:** the neutral parameter `r` cancels; the asymmetry `a − b` does not, and it is the pool
  derivative. `Height = ∫λ·N·A·h_term` is correct but holds a state variable as a parameter.
- **To `round240`:** the controllable variable is not "the self-renewal fraction" as dispersion but the
  renewal/loss **imbalance**; and the counterweight it carried from `chu2026`'s abstract — human stem-cell
  stimulation by GH — **is not in `chu2026`'s data** (§4).
- **To this branch, F-R019:** the cancellation theorem is superseded on its own subject. Compartments
  having opposite signs is contingent; **output being conjugate to the pool is an identity.** F-R019's
  conclusion survives; its status improves from mechanism to arithmetic.
- **To this branch, F-R029/R031:** I wrote that GH "fails the second half of the condition." Correct, and
  understated. GH does not merely fail to replenish the pool — **it is the agent that spends it**, and in
  humans as well as mice.
- **Not corrected, and I want it on the record as unexplained:** Wadlow's flat ~5 cm/yr from 13 to 22 with
  no deceleration. Under §2 a pituitary giant sits in the `a < b` regime and should decelerate. He did
  not. F-R031 withdrew my mechanism for it; nothing this round supplies a new one.
