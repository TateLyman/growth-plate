# F-R027 — The absolute statement: recruit at least as fast as you grow

This round assembles nothing new from outside. It runs the census as promised, reads one paper the
atlas had already resolved better than I would have, and finds that **the complete answer is forced by
material already in hand.**

---

## 1. Why `herrmann2002`'s man stopped at 24 — the atlas answered this and I had not read it

`rz_depletion_causes_fusion.yaml` arbitrates the two readings of growth-plate senescence and resolves
them, including the case that has been driving this branch:

> "**Depletion is therefore SUFFICIENT TO STOP GROWTH and NOT SUFFICIENT TO FUSE A PLATE**; fusion
> additionally requires the oestrogen signal that converts an exhausted plate to bone."

and, resolving the paradox in `nilsson2006` (PMID 16614378 — oestrogen accelerates senescence yet
*slows* resting-zone proliferation):

> "It can, **once RENEWAL and EXIT are separated: oestrogen slows resting-zone proliferation — that is,
> SELF-RENEWAL — without delaying, and possibly while accelerating, DIFFERENTIATION OUT of the resting
> zone. The pool drains because the OUTFLOW is unchanged while the INFLOW falls.**"

with `nilsson2014` supplying the decisive experiment: oestrogen accelerated resting-zone loss in
ovariectomised rabbits, **the loss persisted five weeks after treatment stopped**, and transient
exposure **permanently** hastened fusion.

**So `herrmann2002`'s man stopped at 24 because his resting zone drained.** He had no oestrogen, so
nothing was suppressing his inflow — and he drained anyway, because self-renewal alone does not keep
up. His plate was still there three years later at bone age 16 because **there was no oestrogen signal
to convert an exhausted plate into bone.**

**That is the whole phenotype, explained:** open, cell-poor, nonossifying, producing nothing — which is
exactly `carroll2018`'s histology (*"nonossifying hyaline cartilage with admixed fibroconnective
tissue"*) and exactly what a 27-year-old's hand X-ray at bone age 16 shows.

---

## 2. What that does to the goal

Write the resting-zone balance:

```
d(RZ)/dt  =  self-renewal_inflow  +  recruitment_inflow  −  differentiation_outflow
dH/dt     ∝  differentiation_outflow  ×  λ  ×  h_term
```

**Three facts, each independently established, make the answer forced:**

**(i) Growth *is* outflow.** Every centimetre is a resting-zone cell leaving the resting zone. You
cannot grow fast without draining fast. This is not a trade-off to be engineered around — it is an
identity.

**(ii) Self-renewal cannot cover outflow.** F-R007 computed the renewal fraction across 36 parameter
combinations: `p = 0.392–0.493`, **every one below the 0.500 required for a steady pool.**
`PMC12685065` confirmed the mechanism by lineage tracing — these cells *"renew via population
asymmetry"* — and showed **GH depletes the pool by driving committed division.**

**(iii) Oestrogen blockade does not stop the draining.** It removes the *conversion* step, not the
*consumption* step. `smith2008`, `maffei2004`, `herrmann2002` all drained on schedule; they simply
ended up with an open empty plate instead of a fused one.

**Therefore every strategy that has ever been tried fails for the same structural reason:**

| strategy | inflow | outflow | result |
|---|---|---|---|
| **GH / IGF-1** | unchanged | ↑ | drains faster — `PMC12685065`: GH *depletes* the stem pool. **Velocity bought with duration.** |
| **oestrogen blockade alone** | unchanged | unchanged | still drains; you get an **open, empty, nonossifying plate at 1 cm/yr** (F-R025) |
| **glucocorticoid / growth inhibition** | ↓ | ↓↓ | conserves the pool by not growing. **Duration bought with velocity** (`nilsson2006`: dexamethasone slowed RZ depletion) |
| **oestrogen itself** | ↓ | unchanged | *"the pool drains because the outflow is unchanged while the inflow falls"* — the fastest drain of all |

**Nobody has ever raised inflow.** Every intervention in the history of this field moves outflow, or
moves inflow *downward*. That is the single sentence explanation of why a century of work has produced
percentages.

---

## 3. The absolute statement

> **Unbounded, fast, non-closing growth requires the perichondrial recruitment rate to equal or exceed
> the differentiation rate, with oestrogen-receptor signalling blocked so that a transient shortfall
> does not become irreversible bony conversion.**
>
> - **Speed** is set by `differentiation_outflow × λ × h_term`.
> - **Sustainability** is set by whether `recruitment_inflow ≥ differentiation_outflow`.
> - **Oestrogen blockade** is what makes a shortfall *recoverable* rather than terminal.
>
> **Fast and unbounded are not in tension. They are coupled by one inequality: you must recruit at
> least as fast as you grow.**

And **recruitment is the only inflow that escapes the trade**, because — F-R018's arithmetic and
F-R020's genetics — **a recruited Pdgfrα⁺ stromal cell arrives with its own unspent division counter.**
Self-renewal buys pool at the cost of the clock; recruitment adds pool *and* clock.

### Every term now has a name

| term | mechanism | status |
|---|---|---|
| **oestrogen blockade** | **receptor-level** — `smith2008` survived a deliberate 10× oestradiol challenge; ligand-level closes on ligand restoration (`maffei2004`) | **confirmed in humans** |
| **recruitment inflow** | **Pdgfrα⁺ inner perichondrium → Gli1⁺ LLCP**, demand-responsive, required for normal bone length | `rosellodiez2025`, `mundy2026` |
| — its **throttle** | Hedgehog: **PTCH1⁺ groove of Ranvier** → GLI1 | `karlsson2009`, `trompet2024` |
| — its **brake** | **CCN2** — falls when cartilage is challenged, and exogenous CCN2 suppresses Gli1 and Ki67 | `rosellodiez2025` |
| — its **steering** | **heparan sulfate** shapes the Ihh gradient; lose it (EXT1) and the cell makes a lump instead of entering the plate | `mundy2026` |
| — its **exposure rule** | **transient, local, self-limiting** — every pool-expanding lever is a tumour suppressor, and chronic activation *costs height* (HME carriers are short) | F-R022; the atlas's `the_stack_in_a_normal_human` |
| **differentiation outflow / speed** | `P_swell × f_axial × Φ` — pO₂ **< 8%** for proteoglycan; **radial confinement** to vector it; cyclic loading for convection | F-R015, F-R023, `serrat2010` |
| **not the answer** | GH/IGF-1 (supranormal → 0.3 cm/yr), androgen (27 months supraphysiological → bone age frozen) | F-R025 |

---

## 4. The census, run

The atlas's round-86 census is in `the_human_ceiling_has_never_been_observed.yaml`, and its result is
already stated in a form I cannot improve:

> "**NOT ONE has a reported final height**" reached without intervention · *"all seven had unfused or
> [incompletely fused epiphyses]"* at their pre-oestrogen heights · and, of the cases that do report a
> number, it is *"the height at which a **clinician deliberately stopped them**."*

**The velocity extraction I promised cannot be done, and the reason is the finding.** There is no
distribution of final heights in oestrogen-null humans because **no oestrogen-null human has been
allowed to reach one.** The literature records the height at which each was stopped. `maffei2004`'s
5-year untreated series (177 → 183.5 cm) and `imre2025`'s 6-year interval (+5 cm) are the only
substantial untreated growth intervals in the entire corpus, and they are the two numbers F-R025
already used.

**The human ceiling has never been observed. Not "is unknown" — has never been permitted to occur.**

---

## 5. What is genuinely still open

I want to be exact about what this framework does *not* have, because everything above is now
structurally complete and the gaps are specific:

1. **Recruitment has never been shown to exceed the set point.** `rosellodiez2025`'s influx *restored*
   normal length after a challenge — homeostatic. **Nothing shows it can push a bone past normal.**
   This is the single load-bearing untested assumption in §3.
2. **Recruitment has never been demonstrated postnatally**, let alone near skeletal maturity. The
   genetics are fetal/perinatal.
3. **The 8% switch has never been measured in an adult physis.** It is the leading explanation for the
   1 cm/yr and it rests on articular chondrocytes in pellet culture (`Li 2014`) plus Brighton's 1971
   zone map.
4. **The radial-confinement lever (F-R023) has never been tested in either direction constructively.**
   Only the destructive half exists (`rodriguez1985`).
5. **No one has combined any two of these arms in the same animal.**

---

## 6. Asks

**#1 — the decisive experiment, stated as one sentence:** in a growing animal with a contralateral
control, apply a **transient local Hedgehog pulse at the groove of Ranvier** (the `trompet2024`
geometry, moved from the SOC to the perichondrium) in an **unchallenged** limb, and measure whether
final bone length **exceeds** the control. That single result separates *homeostatic robustness* from
*unbounded growth*, and it is the assumption everything in §3 rests on.

**#2 — `nilsson2014`** (the ovariectomised-rabbit oestrogen washout study the atlas cites for permanent
RZ loss). I have it only through the atlas's summary and I want the resting-zone cell counts, because
they are the only direct measurement of inflow-versus-outflow in any species.

**#3 — one Safranin-O on `carroll2018`'s specimen** (Brooke Army Medical Center). Tests the 8% switch
in human tissue on material already cut. Still the cheapest decisive item in the project.

**#4 — `imre2025`** (PMID **40048086**) and contact with **Akçay/Yavuz, Marmara University** — a living,
identified 31-year-old with every long-bone physis open and 5 cm in six years, who has not yet been
stopped.

**Still standing:** Brighton thesis (UIC ILL, handle `10027/14248`); JBJS 1980;62A:740; Surgical Forum
1970:465–467; `stegen2019` DCA+BPTES tibia length; the lateral thoracolumbar film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
The instrument for this round was a sentence in the atlas's own node file separating renewal from exit,
written before I started. The whole of F-R019 through F-R026 was an elaborate route to a balance
equation the graph already contained — with one term added that it did not: recruitment from outside
the cartilage, which is the only inflow that does not spend the clock, and the only one nobody has
ever tried to raise.*
