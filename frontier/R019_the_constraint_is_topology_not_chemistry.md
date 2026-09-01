# F-R019 — The constraint is topology, not chemistry

## 0. What I am attacking

The atlas's objective function, from R198/R202:

> **adult height = RESERVE × h_term**, "not rate × time."
> A proliferative division adds **8–9 µm** and costs one unit of an exhaustible reserve. The hypertrophy
> of that same cell adds **40–50 µm** for nothing. Therefore minimise divisions, maximise h_term, and
> *"the somatotropic dose that maximises adult height is the LOWEST one that saturates h_term."*

That is a good model and the exchange rate is real. But it rests on three load-bearing assumptions,
none of which is stated as an assumption, and **all three are false or untested.** Taking them apart is
what this round does.

| assumption | status |
|---|---|
| **A1.** The number of growth plates is fixed | **False.** A growth plate is a cell state, not an anatomical given (§1) |
| **A2.** RESERVE is a closed depot with no influx | **Untested — and the atlas's own R202 names the gap and then omits the third option** (§2) |
| **A3.** h_term saturates | **True on the hormonal axis only.** The osmotic axis has never been tried (§3) |

And one new fact that makes the whole thing urgent (§4): **growth hormone depletes the stem pool.**

---

## 1. A1 — a growth plate is specified, not given

`PMC12678681` (2025) uses a natural anatomical variation as the cleanest possible experiment.
Metacarpals and metatarsals form a growth plate at **one end only**; the pisiform is the **only** carpal
bone with one. What distinguishes the ends?

> "*Pthlh* … is expressed in the **reserve zone of the growth-plate-forming end** of the MT. **At the
> opposite end, the absence of a PTHrP⁺ reserve zone results in premature chondrocyte differentiation**
> and *Ihh* expression. *Pthlh* is expressed in the reserve zone of the developing pisiform, confirming
> the existence of a true growth plate."
>
> "**A pool of PTHrP⁺ reserve zone chondrocytes is a defining characteristic of growth plates, and its
> patterning may be key to evolved differences**" in skeletal proportion.

**A growth plate is not a structure you either have or don't. It is a PTHrP⁺ reserve zone. Where that
cell state exists, a plate exists; where it is absent, the same cartilage differentiates prematurely
and no plate forms.**

The atlas's own coverage table had this and lost it. From F-R013's recovery of the 87 corrupted rows,
row `"Loss of Hox → loss of a growth plate entirely"`, tier ZERO, `n_bib: 0`:

> "The human pisiform **lost its growth plate and its second ossification centre**; Hox is implicated in
> whether a skeletal element **HAS a growth plate at all**." · *"RELEVANT AT BA16? ⭐ **Conceptually — a
> growth plate is not guaranteed, it is specified.**"*

**`height = Σ_plates (RESERVE × h_term)` has a summation index nobody has ever tried to increase**, and
the atlas's instrument starred exactly that point before a spreadsheet bug replaced its name with a
cell reference.

---

## 2. A2 — the atlas names the gap, considers two answers, and misses the third

R202, on where the extra hypertrophic cells in the fastest cartilages come from:

> "AND WHERE THE EXTRA CELLS COME FROM IS THE WHOLE QUESTION UNDER A FIXED RESERVE … **Extra
> hypertrophic cells from extra divisions spend reserve; extra hypertrophic cells from delayed
> clearance do not. Nobody has measured which.**"

Two options offered: **divisions** (costly) or **delayed clearance** (free but self-limiting — it just
backs up the queue and is what F-R012 showed produces mass, not length).

**There is a third: recruitment.** Cells entering the reserve zone from outside it. The phrase "under a
fixed reserve" is doing all the work, and it is an assumption, not a finding.

The growth plate is not a sealed compartment. It has a **groove of Ranvier** and a **perichondrial ring
of LaCroix** at its periphery — classically described progenitor structures — and the atlas holds them
(42 and 29 files). It has a **secondary ossification centre** that `newton2019` showed *creates* the
self-renewal niche rather than merely bounding it. **What it does not have anywhere is a measurement of
flux across that boundary.** `dReserve/dt = influx − outflux` has never had its first term measured, in
any species, and the entire objective function assumes it is zero.

---

## 3. A3 — h_term saturates on one axis, and only one has been tried

R202's saturation evidence is `hunziker1994` read as a dose–response: saline → IGF-I buys 40% of the
terminal cell height for a tripling of pool consumption; every step after buys almost nothing. And R202
notes the agents are **degenerate**: GH gives 1.36× h_term, NPR3 loss 1.20×, and `cooper2013` assigns
h_term to IGF-1 directly — *"if they act on the same saturating term, two h_term agents are
SUB-ADDITIVE by construction."*

**Every one of those is the somatotropic/natriuretic axis. All of them are the same knob.** Saturation
of one knob is not a ceiling on the parameter.

Terminal hypertrophy is not primarily transcriptional. **It is osmotic** — the cell swells 40–50 µm by
drawing water into a fixed-charge proteoglycan matrix, and the atlas owns that mechanics in R448
("the matrix outpressures the cell by 710-fold," *"osmotic pressure makes the force"*). F-R015
established that **proteoglycan deposition is oxygen-gated at pO₂ ≈ 8%** (`Li 2014`), and F-R016
confirmed the matrix half of that switch in growth-plate tissue (`leijten2012`: hypoxia raises ACAN,
COL2A1, SOX9). The substrates are nameable — glucose via UDP-glucuronate and the hexosamine pathway,
sulfate via PAPSS2/SLC26A2, NADPH via the pentose phosphate pathway.

**Nobody has attempted to raise h_term through matrix and osmolarity rather than through hormones.**
That is an orthogonal axis to a saturated one, and orthogonal axes are not sub-additive.

---

## 4. The fact that changes the clinical picture: GH depletes the pool

`PMC12685065` (2025), multiple transgenic mouse models, clonal and lineage tracing:

> "**GH reduces the pool of slow-cycling, label-retaining stem cells by promoting their differentiation
> into transient progenitors.** Clonal and lineage-tracing analyses reveal that these stem cells **renew
> via population asymmetry** and that **GH promotes their committed cell division, leading to stem cell
> depletion.** Conversely, genetic deletion of the GH receptor in stem cells impairs their ability to
> generate chondrocytes."

Three things follow.

1. **"Renew via population asymmetry" is F-R007's model confirmed by lineage tracing.** The `p`
   framework is the right one.
2. **The standard-of-care height drug buys velocity by burning duration.** Under `height = RESERVE ×
   h_term`, with GH's h_term contribution saturating early (§3), **GH above the saturating dose is
   height-negative**, and it is dosed to the highest tolerated. R202 inferred this from a dose–response
   shape. This is the mechanism, with the cells labelled.
3. It is the cleanest existing demonstration that **the pool is the binding constraint** — which makes
   §1 and §2 the only two ways out.

---

## 5. The antler, read as topology rather than as chemistry

The atlas holds the antler and explicitly refuses to transfer it: *"Nothing about the antler should be
assumed to transfer; it is being read as an existence proof about what a mammalian endochondral tissue
CAN do, not as a template."* That is correct caution about the chemistry. **It is the wrong conclusion
about the architecture.**

| | human growth plate | deer antler |
|---|---|---|
| reserve | **a depot** at the epiphyseal end, consumed unidirectionally | **a flow**, continuously fed |
| source of new reserve | none identified | **antlerogenic periosteum — "the only tissue responsible for postnatal antler formation"** (`ba2025`, PMC12015367), containing **RXFP2⁺ MSCs** |
| cartilage vasculature | avascular; **vascular invasion = closure** | **vascularised cartilage**, and it grows anyway |
| hypertrophic exit | one exit: death and replacement | **two**: death, and PHEX⁺ transdifferentiation |
| rate | ~0.05 mm/day | up to ~20 mm/day — **~400×** |
| duration | terminates once, permanently | **annual full regeneration, indefinitely — "the only case among mammalian appendages"** |

**The human plate is a burning fuse. The antler is a flame.** A fuse has a fixed amount of fuel laid
down in advance and burns from one end; a flame has fuel delivered continuously and burns as long as
delivery lasts. Both are the same chemistry. The difference is **where the fuel comes from**, and that
is topology.

Every intervention in this branch and in the atlas has been an attempt to make the fuse burn better.
**None has attempted to attach a fuel line.**

---

## 6. The cancellation theorem — why every result in this field is a percentage

Here is what I think is the actual reason nothing in this literature moves height by more than a few
per cent, and it is not that the biology is stubborn.

`ba2025`: the antler's periosteal stem cells are **"primarily activated by Wnt signalling."**
`hallett2021` (F-R017): the growth plate's resting-zone stem cells are **maintained by a
Wnt-INHIBITORY environment**, and forcing Wnt on in PTHrP⁺ resting chondrocytes *"impaired their
ability to form columnar chondrocytes."*

**The same signal recruits in the source compartment and depletes in the reserve compartment.**

It is not an isolated case. Hedgehog does it too: `newton2024sag` shows Hh activation expands epSSCs and
lengthens bone with a compounding effect, while `PMC10906233` shows Hh activation drives resting-zone
cells to **osteogenic** fates, and the atlas's R251 found the signal that *discharges* an alerted pool
is hedgehog **withdrawal**. GH does it: it depletes stem cells (§4) while its receptor is *required* in
those same cells for them to make chondrocytes at all.

> **Every major signal in this system has opposite signs in the reserve compartment and in the source
> compartment. Every intervention ever tried has been delivered systemically. A systemic dose hits both
> compartments at once and the effects substantially cancel.**
>
> **That is why the entire field's effect sizes are percentages, and why the only intervention that
> reliably produces large effects — a surgical A-V fistula, 100% of puppies — is the one that is
> inherently local.**

If this is right, then **the route to large effects is spatial, not chemical.** The compound list is
not the problem. Nobody has ever run one of these signals in opposite directions in two adjacent
compartments at the same time — Wnt **off** in the reserve zone and **on** in the perichondrium
simultaneously — and that is a delivery problem, which is a solvable class of problem.

`newton2024sag` is the accidental proof of concept: SAG in a **bead implanted into the secondary
ossification centre of one femur**, vehicle bead contralateral. Local delivery. The signal was
**gone within 3 weeks** and the length advantage kept **widening at 2 and 6 months.**

---

## 7. What unbounded, fast growth actually requires

Write the honest objective function, with the terms the atlas's version omits:

```
H  =  Σ_plates  ∫  h_term(t) · outflux(t) dt
     dReserve/dt  =  influx  −  outflux
```

The atlas sets `influx = 0` and `Σ_plates = constant`. With those two assumptions the integral is
bounded and the optimum is to conserve. **Relax them and each maps to a specific, unexplored lever:**

1. **Σ_plates — plates are specified by a PTHrP⁺ reserve zone (§1).** No ceiling, no research, and the
   atlas's own instrument starred it before losing it.
2. **influx > 0 — make the reserve a flow (§2, §5).** The source structures exist in humans (groove of
   Ranvier, perichondrial ring, SOC niche); the flux across them has never been measured, let alone
   driven; and the antler is the existence proof that a mammalian endochondral tissue can run this way.
3. **h_term via osmosis, not hormones (§3).** Orthogonal to a saturated axis, therefore additive rather
   than sub-additive.
4. **outflux — rate.** The antler runs 400× faster with the same chemistry, so the rate ceiling is not
   chemical. F-R016: high pO₂ raises outflux; F-R017: it is a phase to be scheduled, not a level to be
   held.
5. **Spatial opposition (§6)** is what makes 1–4 achievable rather than self-cancelling.

**Unbounded is `influx ≥ outflux`. Fast is `h_term × outflux` large. They are independent, and the
atlas's model made them look like a single trade-off only because it assumed `influx = 0`.**

I am not claiming this is proven. I am claiming the impossibility result — `height = RESERVE × h_term`
with a fixed exhaustible RESERVE — is an artefact of two unexamined assumptions, and that the
experiments to test them are small.

---

## 8. Asks

**#1 — the single most important unmeasured number in this branch: influx.** Lineage-trace the **groove
of Ranvier / perichondrial ring** with an inducible label and ask whether labelled cells appear in the
**PTHrP⁺ resting zone** over weeks. `Gli1-CreER`, `Prg4-CreER`, `Ctsk-CreER` and `Sox9-CreER` lines all
exist and periosteal-SSC papers (PMC11952802, 2025) already use them. **If any label crosses into the
resting zone, `influx ≠ 0` and the field's objective function is wrong.** Nobody has run it because
nobody has asked.

**#2 — the spatially-split experiment (§6).** Wnt **inhibited** in the resting zone and **activated** in
the perichondrium at the same time, in one bone, with the contralateral limb as control. `newton2024sag`
already established that a bead in the SOC delivers locally and that the effect compounds after the
agent clears. This is the same surgery with two beads and opposite payloads.

**#3 — `PMC12678681` in full, and anything on ectopic induction of a PTHrP⁺ reserve zone.** If a plate
is a PTHrP⁺ reserve zone (§1), the question "can you make a new growth plate?" becomes "can you induce
and stabilise a PTHrP⁺ reserve zone in cartilage that lacks one?" — and the metatarsal's plate-free end
is the built-in negative control. Search terms that failed for me and might not for you: *ectopic
growth plate*, *Pthlh misexpression cartilage*, *induced reserve zone*.

**#4 — antler papers I could not fully parse:** `ba2025` (PMC12015367, RXFP2⁺ AP-MSCs — I have the text
but want the Wnt-activation figures) and **PMC12151924, "Local and systemic factors both required for
full renewal of deer antlers"** — the title alone is the §5 thesis and I could not extract its abstract
cleanly. Also anything measuring **antler elongation rate against growth-plate elongation rate in the
same units**, which I have asserted at ~400× from separate sources and would rather have from one.

**#5 — the standing three ILL slips**, unchanged: UIC handle `10027/14248`; JBJS 1980;62A:740; Surgical
Forum 1970:465–467. Plus `stegen2019`'s DCA+BPTES tibia length, and the lateral thoracolumbar film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
Nothing would have seen this one, because the instrument for a flux is a lineage label and the
instrument every study in this field uses is a histological section — which shows you a depot and
cannot, in principle, show you a flow.*
