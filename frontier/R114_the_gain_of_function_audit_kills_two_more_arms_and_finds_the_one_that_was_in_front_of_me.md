# F-R114 — I audited every arm against its own gain-of-function experiment. Two more died. And the best-evidenced obtainable arm in the file turned out to be one I had been calling a "flag."

You said check all of it. I did the one check I had never applied systematically: **for every candidate,
find the experiment where the pathway was pushed in the direction we want, in an animal, with bone
length measured.** It kills most of the file and it settles the stack.

---

## 1. The systematic sweep that started it

I scored **22 druggable axes in the pool compartment** (GSE113982 resting zone, P2/P3 → P28), each
against its own zone's background:

| axis | RESTING zone | proliferative | RZ-specific |
|---|---|---|---|
| **imprinted network** | **−2.92** | −1.07 | **−1.85** |
| **hypoxia / HIF** | **−0.80** | +0.35 | **−1.16** |
| GH / IGF | −0.53 | −0.53 | 0.00 |
| Notch, cilium, mTOR, FGF, AMPK, Hippo, PTHrP, thyroid, BMP, retinoic acid, Wnt, TGF-β, CNP, autophagy, senescence, Hedgehog | −0.52 … +0.44 | | **all ≤ \|0.43\|** |

**Only two axes move in the pool: the imprinted network, and hypoxia.** Everything else — including
several I have spent whole rounds on — is flat.

---

## 2. Hypoxia looked like a new arm for about an hour

Clean HIF core set (collagen hydroxylases removed, because P4HA1/P4HA2/PLOD2 are height genes for
collagen reasons and were inflating the score):

| | HIF program | z |
|---|---|---|
| **mouse tibia vs phalanx, PZ** | +0.12 | **+2.82** |
| mouse tibia vs phalanx, HZ | +0.12 | +2.21 |
| **rat tibia vs phalanx, PZ** | +0.15 | **+3.70** |
| rat tibia vs phalanx, HZ | +0.15 | +3.40 |
| Longshanks vs control | +0.14 | +2.28 |
| Dnmt1-flox vs cKO | +0.34 | +2.07 |
| **MOUSE RESTING ZONE, P2/P3 vs P28** | **+0.81** | **+4.50** |
| *proliferative zone, same contrast* | *−0.11* | *−0.16* |
| *hypertrophic zone* | *+0.02* | *+0.85* |
| HUMAN growth plate, pre- vs late-puberty | +0.27 | +1.81 |

**Six of seven length systems positive, pool-specific with age, and roxadustat / daprodustat /
vadadustat are approved oral HIF stabilisers.** Better on length than the imprinted network, which was
null in the proliferative zone.

**Two things killed it.**

1. **No human genetic support.** 68 height associations vs 89 ± 168 in a matched null, **p = 0.41**.
   Every other arm in this file that survived has GWAS behind it.
2. **The gain-of-function experiment exists and it is strongly negative.**
   `Pfander D, Kobayashi T, … Schipani E. Deletion of Vhlh in chondrocytes reduces cell proliferation
   and increases matrix deposition during growth plate development. Development 2004;131:2497.`
   **Vhl cKO stabilises HIF1α in chondrocytes — exactly what a PHD inhibitor does — and the mice
   "grow slower than control littermates and develop a severe dwarfism," with reduced chondrocyte
   proliferation and atypical large cells in the resting zone.**

**HIF-PHD inhibitors are wrongly signed. Arm closed the same day it opened.**

---

## 3. The audit, and the pattern it exposes

| arm | pathway pushed the way we want | length outcome | verdict |
|---|---|---|---|
| **Hedgehog, partial/het dose** | PTCH1⁺/⁻ human; SAG bead in the SOC | **taller** (+0.8 to +3.8 SD; femur, tibia, leg longer at 1, 2, 6 months) | **SURVIVES** |
| Hedgehog, full/sustained | Sufu-cKO; full Ptch1 loss | **shorter** (−3.7 mm at P120); Gorlin | fails at full dose |
| **oestrogen blockade** | aromatase / ERα deficiency, human | **taller**, 204 cm, epiphyses open at 28 | **SURVIVES** |
| **CNP / NPR2** | see §4 | **taller** | **SURVIVES** |
| proteoglycan sulfation | PAPSS2, SLC26A2, CHSY1 loss | shorter | loss-of-function only; no GOF exists |
| DNA methylation | Dnmt1^ΔPrx1 | shorter (<half length) | loss-of-function only |
| **chromatin de-repression** | Ezh1⁻/⁻;Col2-Cre Ezh2^fl/fl | **shorter** — and it raised the imprinted network at z=+7.5 | **FAILS** (F-R113) |
| **HIF / hypoxia** | Vhl cKO in chondrocytes | **severe dwarfism** | **FAILS** (§2) |
| GH / IGF-1 | somatropin, human growth plate | null on the axis (r=+0.029), pool-negative | fails |
| injury / regeneration | remote fracture (GSE3298) | plate network unchanged | doesn't reach the plate |
| FGFR3 inhibition | erdafitinib, infigratinib | achondroplasia rescue | rescue only, never above normal |

> **Every candidate in this file except three has an expression correlate pointing the right way and a
> gain-of-function experiment pointing the wrong way.** The growth plate counter-regulates hard —
> F-R094's rescue law, now generalised. **The arms that survive are the ones where a human dose-response
> exists in both directions**, not the ones with the best transcriptome story.

---

## 4. And the arm that survives everything is one I have been under-rating for four rounds

**CNP / NPR2. I called it a "flag" in F-R108, "promoted" it in F-R109 on expression grounds, and never
once ran the gain-of-function test.** Here it is:

| evidence | |
|---|---|
| human **loss** of function | **acromesomelic dysplasia, Maroteaux type — severe short stature** |
| **human gain of function** | **epiphyseal chondrodysplasia, Miura type (OMIM 615923) — TALL STATURE and overgrowth**, autosomal dominant, from excess cGMP (V883M, R655C, A488P) |
| **human CNP overexpression** | balanced t(2;7) translocation overexpressing *NPPC* → **overgrowth and bone anomalies** |
| **mouse GOF in a NORMAL animal** | **SAP-CNP-Tg mice, ~2× wild-type plasma CNP → skeletal OVERGROWTH.** Also Col2a1-driven cartilage overexpression → overgrowth |
| stem-compartment expression | **NPR2 enriched in the resting zone, 5+/1− of 8 datasets** (F-R108) |
| behaviour with age | **NPR2 *rises* +1.05 in the ageing resting zone** (F-R111) — the target gets more abundant exactly when we need it |
| human common variation | **NPR2 + PRKG1 carry 40 genome-wide height associations** (F-R109) |
| mechanism | cGMP/PKG inhibits the **MAPK arm of FGFR3** and increases matrix synthesis and hypertrophic size — i.e. it acts on **v**, the one axis that survived F-R108's controls |
| **obtainable** | **vosoritide — approved, daily subcutaneous, established paediatric dosing** |

### ⇒ This is the third experiment in the entire file that exceeds normal, and it is the cleanest

F-R094's rescue law has held nearly everywhere: every agent rescues a deficit, nothing beats a healthy
control. The exceptions were Trompet's SAG bead and the glucosamine composition shift (which had no
length endpoint).

**SAP-CNP-Tg is a wild-type mouse, systemically, at two times normal plasma CNP, with skeletal
overgrowth.** No deficit, no rescue, systemic route, length endpoint.

> **And it is systemic. F-R110 posed the fork — accept local intra-epiphyseal delivery, or stay systemic
> and accept the deadline arm only. CNP is the third option: a systemic agent with a human bidirectional
> dose-response and an approved drug. The fork is not as sharp as I put it to you.**

### ⇒ One correction to the stack that follows immediately

**Vosoritide and erdafitinib are the same node.** CNP's mechanism is inhibition of the MAPK arm of FGF
signalling; erdafitinib inhibits FGFR3 upstream of it. **They are redundant, not additive**, and
vosoritide is the one with the human gain-of-function genetics and the approved paediatric label.
**Erdafitinib should come out in favour of vosoritide**, not sit alongside it.

---

## 5. Two corrections to my own last two rounds

**(a) The deadline arm's value is set by *when you start*, not by how completely you block.**
I was about to argue that the gap between aromatase *deficiency* (+3 SD, 204 cm) and aromatase
*inhibitor trials* (+3.8 cm) is dose and duration. **The trials say otherwise:** in the 3-year
randomised comparison, **letrozole produced greater hormonal suppression than anastrozole and no
greater height**, and PAH gain was "minimal" after years 2–3. **More complete blockade does not buy more
height.** What separates +3.8 cm from +20 cm is that the genetic cases had **zero lifetime oestrogen
exposure** — which is exactly Nilsson 2014's irreversible structural advancement, from the other
direction. **The arm is front-loaded, and starting late caps it. That was already in the ledger from
F-R104 and the trial data now confirms it independently.**

**(b) The imprinted network is mostly an age variable, not a length variable.** Scored properly against
matched nulls:

| | imprinted network | z |
|---|---|---|
| mouse tibia PZ, **young vs old** | +0.27 | **+9.27** |
| rat tibia PZ, young vs old | +0.25 | +6.53 |
| mouse tibia vs phalanx PZ, **long vs short at same age** | +0.04 | **+1.08 — null** |
| rat tibia vs phalanx PZ | +0.07 | +1.00 — null |
| mouse/rat tibia vs phalanx, HZ | +0.16 / +0.14 | +3.83 / +3.11 |
| Longshanks vs control | +0.32 | +4.47 |
| Dnmt1 flox vs cKO | +0.14 | +0.85 — null |
| Fgfr3 WT vs GOF | −0.02 | −0.13 — null |

**It tracks age 4–9× more strongly than it tracks length at fixed age, and it is null in the
proliferative zone of the cleanest length contrast that exists.** Combined with F-R113's Ezh2 result —
network up, bone shorter — **I am downgrading the imprinted network from "the counter" to "the largest
measured correlate of pool ageing, of unproven causal status."** F-R111's measurement stands; its
interpretation was too strong.

---

## 6. The stack, final form

| arm | what it buys | evidence | obtainable |
|---|---|---|---|
| **1. vosoritide (CNP/NPR2)** | **rate and v; human GOF = tall** | bidirectional human dose-response; **exceeds normal in a normal animal at 2× plasma**; target rises in the ageing pool | **YES — approved, systemic, paediatric** |
| **2. aromatase inhibition** | **the deadline; ~+3 SD ceiling alone** | human genetic proof (204 cm, epiphyses open at 28) | **YES — approved. Value is front-loaded; start as early as possible** |
| **3. Hedgehog at partial dose** | setpoint / pool; **orthogonal to 1 and 2, therefore additive** | PTCH1 human dose-response; SAG bead durable to 6 months | **only locally** — no clean systemic agonist |
| *out* | **erdafitinib** — same node as vosoritide, weaker evidence | | |
| *out* | somatropin, mecasermin, EZH2i, HDACi, BETi, HIF-PHD inhibitors, pirfenidone, calcium AKG | each fails its own gain-of-function test | |
| **the counter** | **still nothing** | every mechanism proposed for it fails GOF | — |

**The obtainable programme is: vosoritide + aromatase inhibition started early, which are systemic,
approved, act on different axes (rate and deadline), and have never been combined in any trial or any
animal. Plus partial Hedgehog agonism if local delivery is acceptable, which is orthogonal to both.**

---

## 7. Where infinity actually stands

**`infinite = never-closing × non-senescing`** (F-R113).

- **never-closing: solved**, human-proven, approved drug, ceiling ~+3 SD alone, front-loaded in time.
- **non-senescing: not solved, and now I can say why it is hard rather than just that it is.** The
  counter is division-based, cell-intrinsic (transplantation; parabiosis), oestrogen-independent
  (castrated rats, z = −6.7 to −7.9), Hedgehog-orthogonal, unreachable by remote injury — and **every
  molecular mechanism proposed for it, mine included, has now been pushed in the right direction in an
  animal and made bones shorter.**

**That is not "we haven't found the agent." It is "the four best-supported mechanisms have each been
tested and each failed."** Infinite is not reachable on current biology. **The maximum obtainable stack
is rate + deadline + setpoint, and its ceiling is set by capacity, which nothing yet moves.**

## 8. The one thing I would still ask for

**Any experiment in which vosoritide, CNP, or any NPR2 agonist was given to a normal (non-dysplastic)
growing animal with a final-length endpoint.** SAP-CNP-Tg is transgenic overexpression from birth;
vosoritide is a drug given for a few years. **The gap between those two is the whole question of what
the arm is worth**, and I could not find a normal-animal drug experiment in 5,591 series or in the
literature I can reach.

---

*Two arms opened and closed in this round, both by the same test. The one that survived was sitting in
the file since F-R108 wearing the word "flag." The lesson I am writing into the ledger: **do not promote
an arm until its gain-of-function experiment has been found and read.** Applied retrospectively, that
rule would have saved about six rounds.*
