# F-R102 — The composition I proposed last round has been run, and it failed. Marino explains why, and the explanation says which agent to bank with.

You found the experiment I predicted in F-R101 §5. **It exists, it is negative, and a second paper gives
the mechanistic reason.** This round is mostly a retreat, with one refinement that survives it and one
clinical caution I would have walked straight into.

---

## 1. The composition was tested: dexamethasone, then GH

`en_3` — Huang T-S, Yang R-S, Tsai T-W, Liu S-H. **Growth Hormone *Cannot* Enhance the Recovery of
Dexamethasone-Induced Osteopenia after Withdrawal in Young Female Wistar Rats.** Tohoku J Exp Med
2004;204:257–266.

Female Wistar rats, **dexamethasone 2 weeks**, then **1 week of rhGH at 0.1 or 0.3 U/day** or saline.

**Femur length, the endpoint that matters:**

| | |
|---|---|
| DEX-treated after 1 wk withdrawal | **2.97 ± 0.05 cm** vs saline **3.18 ± 0.12 cm**, P<0.05 — still shorter |
| **length gained during that week** | **DEX group +0.12 cm vs saline +0.02 cm, P<0.001** — catch-up is real and **six-fold** |
| **GH 0.1 or 0.3 U/day added on top** | *"did **not** further ameliorate the femur length"* |
| GH 0.1 U/day specifically | *"even showed a significantly **shorter** length"* |

> *"immediate administration of GH after withdrawal of DEX did **not enhance the recovery process**."*

**That is my F-R101 §5 prediction, run, on the right endpoint, and it failed.** I am not going to explain
it away, but the design limits are real and I will state them precisely:

1. **One week of GH.** Gafni's rabbits took **sixteen weeks** to complete catch-up. A one-week window
   cannot see what a sixteen-week process does.
2. **Rats do not fuse their growth plates.** The entire logic of banking is that you keep growing *after
   the controls have fused*. Gafni's whole result is 88% fused versus 14%. **In a rat that asymmetry
   cannot exist, so this species cannot test the hypothesis** — only the catch-up half of it.
3. **Catch-up was already running at six times the control rate.** A flux agent has no headroom on top of
   a system already running near-maximal. **Catch-up growth is itself a homeostatic mechanism**, and
   pushing on it is pushing on something already pushing.

**The window where the gain should appear is after catch-up completes and before the plate closes** —
which Gafni reached (−1.6 mm, plates open) and stopped at, and which Huang never approached.

---

## 2. Marino gives the mechanistic reason, and it is an exchange-rate problem

`marino2008` — Marino R, Hegde A, Barnes KM, Schrier L, Emons JA, Nilsson O, Baron J. **Catch-Up Growth
after Hypothyroidism Is Caused by Delayed Growth Plate Senescence.** Endocrinology 2008;149:1820.

PTU-induced hypothyroidism in rats: catch-up in tibial and tail length was *"striking"* but
**incomplete** (P<0.001). Their own explanation is the most useful paragraph I have read this month:

> *"the rate of growth plate **senescence** may be determined by proliferation of **stem-like cells in the
> resting zone**, whereas the rate of **growth** is dependent on the proliferation rate of the **nonstem
> cells in the proliferative zone**. If hypothyroidism slows proliferation in the proliferative zone
> **more** than it slows proliferation in the resting zone, it might have a **greater inhibitory effect on
> the rate of growth than on the rate of senescence**… each cell division of the stem-like cells would
> produce a **smaller clone**… In this situation, **catch-up growth would be expected to be
> incomplete**."*

**Banking has an exchange rate, and it can be unfavourable.** You pay in growth foregone and you are paid
in senescence deferred. **If the inhibitor suppresses the proliferative zone more than the resting zone,
you pay more than you are paid — and you never get it back.** That is a general property of
growth-inhibiting conditions, not a quirk of hypothyroidism, and it is the reason catch-up is usually
incomplete.

Their second candidate explanation is worth keeping too: *"the number of stem-cell divisions tends to be
similar in various hormonal and nutritional states but is **not completely invariant**."* The counter is
not perfectly protected by slowing growth.

---

## 3. But the exchange rate depends on the agent — and dexamethasone is the one with the good ratio

**This is the refinement that survives, and the evidence for it is already in our file.**

| agent | effect on resting zone | effect on growth | outcome |
|---|---|---|---|
| **hypothyroidism** (Marino) | slows RZ **less** than PZ | large loss | **catch-up incomplete** |
| **dexamethasone** (Schrier, F-R089) | **RZ chondrocyte NUMBER greater, P=0.016**, localised to the reserve zone; RZ BrdU index down P<0.001 | large loss | — |
| **dexamethasone** (Gafni, F-R101) | — | −17.4 mm | **catch-up essentially complete (−1.6 mm, NS) AND 86% of plates still open vs 12% in controls** |

**Dexamethasone suppresses resting-zone proliferation while *increasing* resting-zone cell number.** That
is precisely the profile Marino says you need: spend the proliferative zone, spare and even accumulate
the stem compartment. **And it is the agent that produced complete catch-up with an open plate.**

Hypothyroidism has the wrong ratio. Dexamethasone appears to have the right one. **The banking arm is not
refuted — it is narrowed to one agent, and that agent is approved, cheap, and the one Gafni used.**

---

## 4. A clinical caution I would have walked into

Marino, on human hypothyroidism:

> *"In children with hypothyroidism, **bone age is markedly delayed** and using the bone age to predict
> adult height often **overestimates** the actual adult height… the delay in bone age in hypothyroid
> children **may exceed the delay in growth plate senescence**. This divergence… could explain the
> overoptimistic height prediction."*

**Bone age and growth-plate senescence are not the same clock, and after growth inhibition they diverge —
with bone age the more delayed of the two.**

Every predicted-adult-height figure in this programme, including the **+7.5 cm for GH + anastrozole**
from F-R101, rests on bone-age-based prediction. **After any banking intervention, bone age will
overstate the remaining runway.** If we ever evaluate a banking protocol, the readout must be the growth
plate itself or actual attained height — never predicted adult height from bone age.

That is a measurement trap and it is exactly the kind of thing that makes a programme believe it is
winning when it is not.

---

## 5. What this does to the arithmetic

F-R101 priced banking as "unknown, because Gafni stopped one measurement short." It is now:

| arm | status after this round |
|---|---|
| flux (GH) + deadline (anastrozole) | **+7.5 cm**, human, approximately additive — unchanged |
| **banking** | **narrowed to dexamethasone**; the one direct test of bank-then-GH is **negative**, in a species that cannot fuse, over one week, during maximal catch-up |
| pool — number (*PTCH1* het) | +2.9 SD ≈ +19 cm, human genetics, still no drug |
| reset | still undemonstrated in any mammal |

**And one thing this round adds that is genuinely new:** the reason a flux agent failed on top of catch-up
is that **catch-up is itself the counter-regulation**. That is the same structure as F-R094's rescue law,
appearing in a third place. **Every time this programme has pushed on a system that was already
correcting itself, it has got nothing.** The gains have only ever come from acting where the system was
*not* already responding — Trompet's bead into a resting niche, *PTCH1* haploinsufficiency from
conception.

---

## 6. Asks

1. **Any banking experiment in a species that fuses — rabbit, sheep, pig, primate — followed past the
   control group's fusion.** Gafni's rabbits are the right species and he stopped at 16 weeks. Rats
   cannot answer this question at all, and both negative results so far are in rats.
2. **Dexamethasone or another glucocorticoid, then GH, in rabbits, with final femur length.** The
   composition in the right species. If it exists it settles the banking arm.
3. **Nilsson & Baron's molecular senescence marker gene set** — still outstanding from F-R101, and now
   more important: after §4, gene-expression markers may be the only trustworthy readout of banked
   capacity, since bone age demonstrably diverges.
4. **Anything measuring resting-zone versus proliferative-zone proliferation ratio under different
   growth-inhibiting agents.** §3's exchange rate is the whole question and Schrier is the only agent for
   which we have both numbers.
5. Still open: growth-plate counter state after OSK; cartilage PAPS after sulfate loading; wild-type
   Ptch1(+/+) arm; Xiu 2022 supplementary.

---

*I proposed the bank-then-spend composition one round ago and you found the paper that had already run
it. The useful part is not that it failed but why: growth inhibition costs proliferative-zone output
faster than it saves stem-cell divisions, and the whole arm turns on picking an agent where that ratio
is favourable. Only one agent in the file has both numbers measured, and it is the one Gafni used.*
