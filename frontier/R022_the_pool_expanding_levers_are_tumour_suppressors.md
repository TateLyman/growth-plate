# F-R022 — Three corrections, one new positive, and the ceiling the atlas named before I did

## 0. Corrections first

**(a) I sent you the wrong DOI, and that is why you got the wrong paper.** In F-R021 I gave
`10.1007/BF02554932` for the ring-excision study. **That DOI is `caraceni1985` — bromocriptine and
forearm bone mineral content in hyperprolactinaemia, Calcif Tissue Int 1985;37:687–689.** The paper I
actually wanted is ten pages earlier in the same issue:

> **Rodriguez JI, Delgado E, Paniagua R. *Changes in young rat radius following excision of the
> perichondrial ring.* Calcif Tissue Int 1985;37:677–683.
> PMID 3937595 · DOI 10.1007/bf025549**30** (not …32).**

**(b) And its abstract, which I have now read, refutes the claim I built §2 of F-R021 on.**

> "The distal growth plate of the radius was exposed in young rats and the perichondrial ring and
> fibrous covers were removed at the exposed surface… The most relevant changes were **an enlargement
> of the growth plate at the exposed surface that grew in an abnormal direction**, proliferation of
> bone trabeculae at the level of the excised perichondrial ring, and **bending of the bone**. No
> regeneration of the perichondrial ring occurred. These changes support both **the role of the
> perichondrial ring in the MECHANICAL CONSTRAINT of the growth plate**, and the induction of bone
> formation by the hypertrophic cartilage at the level of the absent perichondrial ring."

**Excision did not arrest growth. It produced a plate that grew in the wrong direction, and a bent
bone.** The authors read the ring as a **mechanical corset**, not a cell source.

F-R021 quoted `fenichel2006`'s statement that *"operative removal of the ring of LaCroix causes growth
arrest and short stature"* and treated it as the loss-of-function leg of the argument. **That statement
is not supported by the literature it points at** — and F-R021 already noted `fenichel2006`'s citation
keying is unreliable (the sentence is keyed to an FGF9 paper). **I should have discounted it then
rather than passing it through. The loss-of-function leg of the influx argument is withdrawn.**

What survives from F-R021 is the positive evidence, which is untouched by this: `karlsson2009`'s
label-retaining gradient enriched at the rim, `fenichel2006`'s labelled cells crossing the physis, and
`rosellodiez2025`'s genetics. The ring being a mechanical constraint and the groove being a cell source
are not mutually exclusive — they are different structures, and Rodriguez removed the *ring*.

**(c) A labelling error of mine.** I have been calling the SAG-bead paper `newton2024sag`. Its first
author is **Trompet D**, and the atlas already indexes it correctly as **`trompet2024`**. I will use
that from here.

---

## 1. The new positive: the groove makes cartilage engines

Searching for Rodriguez surfaced the same group's companion paper, which nobody in this branch or the
atlas has:

> **Rodriguez JI et al. *Radiation-induced osteochondroma-like lesion in young rat radius.* Clin Orthop
> Relat Res 1985;(201):251–258. PMID 4064411 · DOI 10.1097/00003086-198512000-00038.**
>
> "the external surface of the distal growth plate of the radius… was exposed to a single low dose of
> radiation (150 r), **focused on the perichondrial groove**. This **induced the formation of a
> chondrocyte nest at the proximal external edge of the growth plate** (5–9 days after irradiation).
> With advancing longitudinal growth of the bone, the chondrocyte nest occupied a diaphyseal position.
> At 9–11 days **the chondrocyte nest underwent endochondral ossification.**"

**A single focal insult to the groove of Ranvier generated a new nest of chondrocytes that ran its own
endochondral programme outside the plate.** That is the groove behaving as a chondrogenic source — and
it is the classical origin story of **osteochondroma**, which is a piece of physeal cartilage that
relocates and keeps growing under its own cartilage cap until skeletal maturity.

`chondrocyte nest` returns **0 files** in the atlas; PMID 4064411 returns 0.

---

## 2. The convergence — and the atlas nominated this cell first

`atlas/nodes/L12_pharmacology_as_mechanistic_probe/the_stack_in_a_normal_human.yaml`:

> "**mundy2026 localises the osteochondroma progenitor to the PDGFRalpha-positive INNER PERICHONDRIUM,
> the population this atlas nominated for recruitment.**"

Put that against F-R020's finding and the same cell appears three times from three directions:

| line | cell | what it does |
|---|---|---|
| `rosellodiez2025` (Nat Commun) | **Pdgfra⁺ cells outside the cartilage** | become Gli1⁺ long-lived chondroprogenitors and **enter the plate**; required for normal bone length |
| `mundy2026` (via the atlas) | **PDGFRα⁺ inner perichondrium** | is the **osteochondroma progenitor** |
| Rodriguez 1985b | the perichondrial groove | irradiated → **chondrocyte nest → endochondral ossification** |

**One population. Recruited into the plate, it restores growth. Released without control, it builds an
ectopic cartilage engine.** F-R019 asked "can a new growth plate be specified?" — this is the cell that
does it, and the pathological version has a name.

---

## 3. The ceiling, and the atlas named it before I did

I have been arguing across F-R019 to F-R021 that the problem is delivery. The atlas states something
deeper and I did not have it:

> "**THE REAL BLOCKER IN ARM 3, NAMED — EVERY KNOWN POOL-EXPANDING LEVER IS A TUMOUR SUPPRESSOR.**
> PTCH1 loss gives Gorlin syndrome — basal cell carcinomas and medulloblastoma. TSC1 and TSC2 loss
> gives tuberous sclerosis. And a human tall-stature cohort supplies the mTORC1 counterpart directly:
> kim2025, 37 patients above the 97.7th height percentile… pathogenic variants in FBN1, **PTEN**,
> NSD1, SUZ12, CDH8 and **DEPDC5** — both negative regulators of mTORC1 whose loss hyperactivates it,
> and **both are tumour suppressors**."
>
> "**AN EXPANDABLE SELF-RENEWING PROGENITOR POOL IS WHAT A TUMOUR IS.** The organism holds the pool in
> check with tumour suppressors, and arm 3 proposes to release exactly those brakes. **That is why no
> pharmacological pool recruiter exists: not because nobody has looked, but because the obvious
> molecules are the ones oncology spends its effort BLOCKING** — vismodegib against SMO, rapalogues
> against mTORC1."

**That is the real ceiling on the influx arm, and it is not a missing compound.** Every gene whose loss
expands a skeletal progenitor pool is a gene whose loss causes cancer, because they are the same
property described twice.

### The dose–response this implies, which is the actual answer

Three points on one axis — Hedgehog/pool expansion — at three exposures:

| exposure | outcome | height |
|---|---|---|
| **chronic, germline, global** — PTCH1 loss (Gorlin), EXT1/EXT2 loss (hereditary multiple exostoses) | tumours; exostoses that **disrupt** the plate | **HME patients are typically SHORT** |
| **chronic, systemic, pharmacological** | oncogenic risk, and F-R019's cancellation — the same agent depletes the resting zone while recruiting outside it | net small or negative |
| **transient, local, self-limiting** — `trompet2024`'s bead | *"signal gone by 3 weeks while the length divergence kept widening to 6 months, with no osteoarthritis"* | **positive, and compounding** |

The atlas reaches the same shape independently:

> "IT IS NOT, HOWEVER, A DEAD END, AND THE SHAPE OF THE SOLUTION IS ALREADY VISIBLE IN trompet2024:
> **TRANSIENT, LOCAL, SELF-LIMITING ACTIVATION.** … **a pulse rather than a chronic state, delivered
> into one anatomical compartment.**"

**Two routes, arrived at separately — the atlas from tumour-suppressor genetics, this branch from the
cancellation theorem — converge on the identical prescription.** That convergence is worth more than
either argument alone, and I am not going to dress it up as my finding: **the atlas had the deeper
version first.** What F-R019–F-R021 add is *why* the pulse must also be spatially split (opposite signs
in adjacent compartments), and *where* the valve is (PTCH1⁺ groove of Ranvier).

**And osteochondroma bounds the risk quantitatively.** It is the uncontrolled version of exactly this
intervention, it is common enough to be well characterised, and its carriers end up **short**. That
tells you the failure mode of over-driving this axis is not merely oncological — **it costs height
directly**, because an ectopic cartilage engine competes with and distorts the plate it grew out of.
The therapeutic window is real but it is narrow, and it is a window in *dose × duration × location*,
not in molecule choice.

---

## 4. Where the theory stands

```
H = Σ_plates ∫ h_term·outflux dt        dReserve/dt = influx − outflux
```

| term | status | knob | constraint |
|---|---|---|---|
| **influx** | proven ≠ 0, necessary (F-R020); source cell = **PDGFRα⁺ inner perichondrium**, triple-confirmed (§2) | Hedgehog (PTCH1→GLI1); CCN2 brake | **every knob is a tumour suppressor** (§3) — so: pulse, local, self-limiting |
| **outflux** | proven, phase-schedulable | pO₂, Wnt, GH (depletes pool) | systemic possible |
| **h_term** | hormonal axis saturated; osmotic axis untried | proteoglycan, sulfate, pO₂ | none identified |
| **Σ_plates** | a plate = a PTHrP⁺ reserve zone; the groove can build an ectopic engine (§1) | — | ectopic engines are osteochondromas and cost height |
| **clock** | counts RZ divisions | bypassed by influx | — |

**The single sentence:** *unbounded growth requires influx ≥ outflux; influx is real and its source cell
is identified; every lever on it is a tumour suppressor; and the only exposure profile that has ever
produced a compounding length gain without a tumour is a transient, local pulse into one compartment —
which `trompet2024` has already demonstrated once, in a rat, with a contralateral control.*

---

## 5. Asks — and an honest word about what is gettable

You have been carrying this and I want to be straight about the remaining list, because some of it is
not worth your time.

**Genuinely worth chasing:**
1. **Rodriguez 1985a — PMID 3937595, DOI `10.1007/bf02554930`, Calcif Tissue Int 1985;37:677–683.**
   You already reached 37:687–689 from the same issue, so this is the same paywall you already got
   through. **I want the figures: did the bone end up SHORTER, or only bent?** The abstract says
   "abnormal direction" and "bending" but never says short, and that distinction decides whether the
   ring matters for length at all.
2. ~~`mundy2026`~~ — **already yours.** I listed this as an ask, then greped: the atlas's bibliography
   has it as **Mundy C et al., Bone 2026, DOI `10.1016/j.bone.2026.117913`**, `access_route:
   user-supplied PDF (HHS author manuscript), 2026-08-07`, `full_text_read: 2026-08-07`. **You already
   got it and the atlas has already read it.** It is on disk in this repository. Nothing to fetch — but
   it is the direct characterisation of the influx source cell, and F-R020's `rosellodiez2025` (which
   the atlas does *not* hold) is its missing counterpart. **Reading the two against each other is a
   round in itself, and needs no new papers.**
3. **`trompet2024` followed to skeletal maturity** — PMC11063944, open access, but they stopped at
   6 months with the advantage still widening. Worth one email to Dana Trompet / the Chagin lab asking
   whether a longer cohort exists.

**Probably not worth your time any more:** Shapiro 1977 (JBJS 59:703–723) — its content is the
"latitudinal" claim, which the atlas already holds and already grades as untested; and Long &
Linsenmayer 1998 — Development's archive 403'd every route I tried, and its finding is upstream
regulation rather than a length endpoint.

**Still standing, unchanged:** UIC handle `10027/14248` (Brighton thesis, ILL/ProQuest);
**JBJS 1980;62A:740**; **Surgical Forum 1970:465–467**; `stegen2019`'s DCA+BPTES tibia length — and I
checked the 80-page manuscript you just sent: **it is the same author manuscript, the Source Data are
not in it**, so that number still has to come from Nature's Source Data files or from Geert Carmeliet
directly.

**And the one that is not a paper:** the lateral thoracolumbar spine film. Every trunk conclusion in
this branch and in the atlas is a population prior until it exists, and your residual is trunk-dominant.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
This round the instrument was a citation, I passed one through without checking where it pointed, and
it pointed at nothing. The correction cost one abstract lookup and it should have happened a round
earlier.*
