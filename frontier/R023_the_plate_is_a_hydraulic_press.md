# F-R023 — The plate is a hydraulic press, and nobody has worked the cylinder

**Source read in full:** `rodriguez1985` (Rodríguez JI, Delgado E, Paniagua R. *Changes in Young Rat
Radius Following Excision of the Perichondrial Ring.* Calcif Tissue Int 1985;37:677–683, PMID 3937595).
Archived at `frontier/screens/the_vector/`.

**Noted:** you have said risk is irrelevant. That is your call and I will not re-litigate it. One
factual point survives it and belongs in the record because it is about *efficacy*, not safety: on the
Hedgehog arm, chronic activation produces **less** height, not merely more risk — carriers of
hereditary multiple exostoses are typically **short** (F-R022 §3). The argument for a pulse over
saturation on that one arm is an efficacy argument and stands regardless of risk tolerance. Everything
else below is unaffected.

---

## 1. The answer to "shorter, or only bent?" is "neither, and here is something better"

`rodriguez1985` measured **no bone lengths at all.** It is a pure histomorphology study — 7 pages,
serial sections, no calipers. So the question F-R022 asked cannot be answered from it, and the
loss-of-function leg stays withdrawn.

But it reports something in **every single operated radius**, and states it as a specific law:

> "in both conditions (epiphyseal or metaphyseal injury) **there was a lengthening of the hypertrophic
> cartilage at the external edge of the growth plate, subjacent to the removed perichondrial ring.
> This feature seems to be a SPECIFIC RESPONSE of the growth plate to the excision of the perichondrial
> ring.**"

> "When the perichondrial ring was removed without injuring the epiphysis, **the lengthened hypertrophic
> cartilage PROTRUDED forming an ARC.**"

> "The **absence** of such a cartilaginous protrusion when the epiphysis is partially injured might be
> due to the development of an **osseous bridge from the epiphysis, which would constrain the growth
> plate and impede the protrusion of cartilage.**"

**Cut the ring, and the hypertrophic zone expands at that spot and bulges outward. Leave a bony bridge,
and it does not.** The tissue expands wherever the confinement is removed, and is held wherever it is
not. That is not a signalling result. It is a statement about **where a pressure is allowed to go.**

---

## 2. What that does to R448

The atlas's `round448_the_matrix_outpressures_the_cell_by_710_fold.yaml` computes the central number:

> the chondrocyte's own turgor is about **400 Pa**; the matrix swelling pressure at cartilage
> fixed-charge density is about **0.28 MPa**. **"THE MATRIX OUT-PRESSURES THE CELL BY 710-FOLD."**
> Conclusion: *"h_term is a matrix-yield problem… R296 searched for osmolytes and agonists to raise the
> DRIVE"* — and that was the wrong arm.

R448 is right that raising the drive is the wrong arm. **But its own number says why, and it is not
"matrix-yield."** 0.28 MPa is roughly **2.8 atmospheres**, generated continuously, in a tissue whose
job is to get longer. **The drive is not scarce. It is enormous, and it is isotropic.**

An isotropic pressure in a confined space does not choose a direction — **the confinement chooses for
it.** Rodriguez cut one wall of the cylinder and the pressure went out through the hole, in an arc, in
every animal.

> **The growth plate is a hydraulic press. The proteoglycan matrix is the working fluid, the
> perichondrial ring and the surrounding cortical bone are the cylinder walls, and longitudinal
> elongation is what happens because that is the only direction left open.**

This reframes the objective function's `h_term` term. It is not `h_term(hormones)` and it is not
`h_term(osmolytes)`. It is:

```
longitudinal output  ∝  (swelling pressure generated)  ×  (fraction of it vectored axially)
```

**and the second factor is architectural.** R448 searched the first factor and found it saturated.
**Nobody has searched the second.** `radial constraint`, `hoop stress` and `circumferential constraint`
each return **0 files** across the entire atlas.

### And the field already knows the vector law under another name

- **Hueter–Volkmann** (61 files here): sustained **compression slows**, **tension accelerates**
  longitudinal growth. That is the axial component of exactly this statement, and every
  growth-modulation device ever built runs on it.
- **Distraction osteogenesis** (47 files): pure longitudinal tension lengthens a human limb **with no
  growth plate at all** — up to 14.5 cm per person (F-R001, PMID 40101878). That is the vector arm run
  at maximum, in adults, in the clinic, today.
- **`rodriguez1985`**: cut the radial wall and the pressure escapes radially.

Three literatures, one law, and the atlas holds all three without joining them: **the plate's output is
a pressure with a direction imposed on it, and both terms are separately manipulable.**

---

## 3. Why this matters more than anything else in the branch

**The vector term is the only lever found in twenty-three rounds that is not gated by a tumour
suppressor.**

F-R022 established the ceiling: every pool-expanding molecule — PTCH1, TSC1/2, PTEN, DEPDC5 — is a
tumour suppressor, *"because an expandable self-renewing progenitor pool is what a tumour is."* That
ceiling is real and it constrains the influx arm no matter how the risk is weighed, because chronic
release of those brakes **costs height** as well as safety.

**Confinement geometry has no such ceiling.** A stiffer cylinder wall is not an oncogene. It cannot
expand a progenitor pool, cannot transform a cell, and has no systemic exposure at all. It is the one
axis where you can push arbitrarily hard and the only failure modes are mechanical — deformity,
bending, and the exact protrusion Rodriguez photographed when the wall was removed rather than added.

---

## 4. The combination

Elongation rate and duration are set by different terms, so write both:

```
dH/dt  =  P_swell  ×  f_axial  ×  Φ_throughput
duration =  ∫ until  influx < outflux
```

Five levers, on **four independent axes**, only one of which touches the tumour-suppressor ceiling:

| # | axis | lever | evidence in this branch | ceiling? |
|---|---|---|---|---|
| 1 | **P_swell** — generate the pressure | hold plate pO₂ **< 8%** → proteoglycan program → fixed charge; flood GAG substrate: glucose (UDP-glucuronate, hexosamine), **sulfate → PAPS (PAPSS2/SLC26A2)**, NADPH via PPP | F-R015 (Li 2014 threshold; Brighton's zone map puts the whole plate below 8%); F-R016 (`leijten2012`: hypoxia ↑ ACAN/COL2A1/SOX9) | none |
| 2 | **f_axial** — vector it | **maximise radial confinement; apply axial tension, never compression** | **`rodriguez1985` (§1)**; Hueter–Volkmann; distraction osteogenesis | **none** |
| 3 | **Φ** — supply and throughput | cyclic loading for convective delivery; scheduled normoxic spend phases | Serrat (**1.5× solute delivery**, four bones longer, local not endocrine); McGarry (loaded tibiae longer, plate taller); Zhang 2024 human (30 s load → AQP9↑, tight junctions↑) | none |
| 4 | **influx** — feed the pool | **transient, local Hh pulse at the groove of Ranvier** + local CCN2 release | `trompet2024` (signal gone by 3 wk, divergence widening at 6 mo); `rosellodiez2025` (Pdgfra⁺→Gli1⁺ recruitment, necessary); `karlsson2009` (**PTCH1⁺ groove**) | **yes — pulse, do not saturate** |
| 5 | **scheduling** | alternate **hypoxic pool-preserving** and **normoxic spend** phases rather than holding one state | F-R016/F-R017 (`leijten2012`: hypoxia holds cells resting, normoxia releases them; `zhang2018yap` shows the switch is **reversible**) | none |

**Axes 1 and 2 multiply.** Pressure with nowhere to go is a bulge; a perfect cylinder with no pressure
is a splint. Every intervention in the literature has worked one of them and left the other at
baseline — which is a second, mechanical reason the field's effect sizes are percentages, alongside
F-R019's cancellation theorem.

**Axis 2 is also the only one that works when the pool is nearly spent**, because it does not consume
anything. For a subject at bone age 16+ with `n` low, the ordering is: **2 → 1 → 3 → 5 → 4**, which is
the exact reverse of where this branch spent its first fifteen rounds.

---

## 5. The experiment that tests the new claim, and it is cheap

`rodriguez1985` did the destructive half in 1985: remove confinement → the plate bulges sideways. **The
constructive half has never been done.**

- **Model:** growing rat or rabbit, **contralateral limb as internal control** — the geometry
  `trompet2024` validated.
- **Intervention:** a **circumferential band** — a compliant sleeve or cerclage placed around the
  perichondrial ring of one proximal tibia, adding radial confinement **without** compressing axially.
  The critical design constraint is that it must not become a tether: it has to grip radially and slide
  axially, or it becomes an epiphysiodesis and does the opposite.
- **Endpoints:** **bone length** (the thing nobody measured in 1985), **growth-plate width**,
  hypertrophic zone height, and terminal chondrocyte height in the axis of elongation (CORR-189's
  measurement).
- **Prediction:** if §2 is right, the banded limb is **longer** and **narrower**; the unbanded control
  is shorter and wider. If the plate is not confinement-directed, nothing changes and this whole axis
  dies in one experiment.

This is orthopaedic hardware, not pharmacology. The field builds growth-modulation devices routinely —
tension-band plates, guided-growth systems, the Luque trolley — and every one of them is designed to
apply **axial** force. **Nobody has built one that applies radial force**, because nobody has framed
the plate as a pressure vessel.

---

## 6. Asks

**#1 — anyone who has banded, sleeved or circumferentially constrained a growth plate and measured
length.** My searches return only axial devices. Terms that failed for me: *circumferential
constraint growth plate*, *perichondrial cerclage*, *radial confinement physis*, *hoop stress growth
plate*. If this exists anywhere it is in orthopaedic engineering, not biology.

**#2 — `mundy2026` against `rosellodiez2025`.** Both are on disk already (`mundy2026` is in the atlas
as a user-supplied PDF, full text read; `rosellodiez2025` is in
`frontier/screens/influx/`). They characterise the same PDGFRα⁺ inner-perichondrial cell from two
directions and neither cites the other. **This is a full round that needs no new papers**, and I will
run it next unless you want something else first.

**#3 — the finite-element or biomechanical literature on physeal stress distribution.** If anyone has
modelled the growth plate as a pressure vessel, the ratio of hoop to axial stress is already computed
and would tell us how much of the 0.28 MPa is currently being wasted radially. That number would size
this entire axis before anyone builds anything.

**Still standing:** Brighton thesis (UIC ILL, handle `10027/14248`); **JBJS 1980;62A:740**;
**Surgical Forum 1970:465–467**; `stegen2019` DCA+BPTES tibia length (Nature Source Data or Carmeliet
directly — confirmed *not* in the author manuscript you sent). And the lateral thoracolumbar film,
which under §4 now matters more, not less: the vector argument is about geometry, and the trunk's
geometry is the one thing here that has never been looked at.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
The instrument was a scalpel in 1985 and the observation is in every operated animal — the cartilage
came out through the hole. Everyone read that as "the ring provides mechanical constraint" and filed
it under stability. It is also a measurement of how much pressure the plate has spare, and which way
it goes when you let it.*
