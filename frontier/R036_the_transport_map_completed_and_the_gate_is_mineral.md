# F-R036 — The transport map completed: the gate is mineral, the decision band is the most permeable place in the plate

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** Both blocked papers obtained, plus the size-gate primary. Two of my own claims corrected.
The delivery problem is now solved as a **design constraint**, and it favours us.

---

## 0. What arrived

- **Stambaugh & Brighton 1980**, *JBJS* 62A:740–749 — the paper I could not obtain by any route.
- **Williams, Zipfel, Tinsley & Farnum**, *"Solute Transport in Growth Plate Cartilage: In Vitro and In
  Vivo"*, *Biophysical Journal* 93(3):1039–1050 — the size-gate primary I asked for, and (I now realise)
  **the source of the atlas's entire Péclet/Damköhler analysis** in
  `the_plate_is_advection_fed_not_diffusion_limited`.
- **Brighton & Schaffzin 1970**, *Calc. Tiss. Res.* 6:151–161 — the oxygen-toxicity mechanism.

All three read in full. Tables recovered from page images where OCR failed.

---

## 1. Two corrections I owe before anything else

**(a) It is INULIN, not insulin.** F-R035 reported, from Serrat 2014's text, that Stambaugh & Brighton
measured *"radioactively labeled **insulin**."* The primary says **³H-inulin** (~5 kDa polysaccharide)
and **¹⁴C-sucrose** (342 Da). Serrat's sentence carries the error; I propagated it. The temperature claim
itself checks out: reserve-zone D goes **2.02 → 5.57 ×10⁻⁶ cm²/s from 4°C to 22°C = 2.76×**, which is
Serrat's *"over twofold."*

**(b) "Molecules >10 kDa are essentially size excluded" is too strong, and the block may not be size.**
That was Serrat's paraphrase of Williams; the primary is more precise and more useful:

> *"Compared quantitatively to the amount of FL entering the region, **3 kDa and 10 kDa dextrans only
> enter the growth plate at 62 and 15%**, respectively."*
> *"…tracers of **10,000 MW and less saturate the full growth plate region (~300 µm across) within 5
> min**."*
> *"…the **FL and 10k-FL diffusion coefficients were measured to be at most twofold different** in the ex
> vivo experiments, so we suspect that **the transport block may be a charge effect**."*

So: 10 kDa is not excluded — it enters at **15%** of a small tracer's level and still saturates the plate
in five minutes. And because their dextrans were anionic and the ex vivo diffusivities differ only ~2×,
**the metaphyseal block is plausibly electrostatic rather than steric.** F-R035 §4's table is directionally
right and its hard-wall framing is wrong.

---

## 2. Stambaugh & Brighton 1980 — the answer is mineral

**Table I — diffusion coefficients (×10⁻⁶ cm²/s), rabbit growth plate:**

| zone | ³H-inulin 4°C | ³H-inulin **22°C** | **Q₁₀** | ¹⁴C-sucrose 4°C |
|---|---|---|---|---|
| hyaline cartilage | 1.89 ± 0.26 | 4.06 ± 0.63 | 1.64 | 2.76 ± 0.49 |
| **small-size cells (reserve)** | **2.02 ± 0.29** | **5.57 ± 0.95** | **1.97** | 2.39 ± 0.27 |
| middle cell columns | 1.51 ± 0.16 | 2.44 ± 0.18 | 1.34 | 1.66 ± 0.13 |
| **hypertrophic cells** | **0.62 ± 0.09** | **1.11 ± 0.23** | 1.43 | 0.99 ± 0.15 |

The hypertrophic value is **41% of the middle cell columns and 31% of the reserve zone** (p < 0.001).
At 22°C the reserve:hypertrophic ratio is **5.0×**. And a detail that matters: raising temperature from
4→22°C significantly raised D **in every zone except the hypertrophic one**, where there was no
significant change. **Warmth opens the top of the plate and does not open the calcified front.**

**Table II — why.** Across hyaline → reserve → columns → hypertrophic: **% matrix falls 88.9 → 55.0**
(so there is *less* matrix where diffusion is *worst*), while **ash as % of dry matter rises 3.1 → 6.3 →
9.8 → 24.4** — *"the hypertrophic zone showed an **eightfold increase in ash**."* Regression across every
measured parameter — matrix volume, hexosamine, hydroxyproline, water, dry matter, ash — found **ash
content the single best correlate of diffusion.**

**Table III — the causal test, and it is reversible.** Rat, ³H-inulin at 4°C:

| | hyaline cartilage | **hypertrophic** | **ash (% dry matter), hypertrophic** |
|---|---|---|---|
| normal rat | 1.55 ± 0.15 | **0.71 ± 0.15** | **23.4** |
| **rachitic rat** | 3.77 ± 0.88 | **4.65 ± 0.95** | **11.1** |
| healed rachitic | 4.20 ± 0.85 | **1.27 ± 0.17** | **20.4** |

> **Demineralise the front and it opens 6.5×. Re-mineralise it and it closes again.** In the rachitic
> plate the gradient *inverts* — the hypertrophic zone becomes **more** permeable than hyaline cartilage.

That is a clean, bidirectional, causal demonstration that **the growth plate's transport barrier is
provisional calcification**, not thickness, not matrix density, not cell size.

---

## 3. Williams et al. — the map, and the band that matters

**Three vascular sources**: epiphyseal, metaphyseal, and the **subperichondrial plexus**. And the routes
have different destinations:

- **Entering from the two chondro-osseous junctions** → *"become distributed throughout the growth
  plate"*; fluorescein equilibrates across ~300 µm in **90 seconds**.
- **Entering from the perichondrium** → stays put: at 5 min the 10 kDa tracer *"remains relatively
  concentrated adjacent to the subperichondrial plexus from which it originated"*, enriched in **the
  proliferative and early hypertrophic zones**.

**The permissive band.** *"the matrix in the proliferative and early hypertrophic zones is **at least
two-to-fivefold as permissive** as that at the two COJs."* Both junctions are barriers; the **midplane is
the open door** — corroborated independently by a dark band on gadolinium-enhanced T1 MRI of piglet hips.

That reconciles Williams with Stambaugh & Brighton: S&B's "hypertrophic" wafer includes the calcified
front; Williams resolves *early* hypertrophic (permissive) from the COJ (blocked). **The barrier is the
calcified front specifically, not the hypertrophic zone as a compartment.**

**And the midplane is not just any band.** It is *"the transition at which chondrocytes commit to
hypertrophy"*, and it is where perichondrium-derived **BMP2, FGF18 and PTHrP** concentrate.

> **The place where the commitment decision is made is the most transport-accessible place in the plate.**

**A mechanism for commitment that nobody has framed as a lever.** Williams:

> *"After secretion of more and more matrix and after swelling and thus reducing the available
> extracellular volume for diffusion, **hypertrophic chondrocytes can no longer communicate as freely
> with the perichondrium**, where many of the signaling molecules originate. **This self-constructed
> environment may then partially define their development toward hypertrophy**."*

**Commitment is partly a transport event.** A cell that begins to swell cuts itself off from the
perichondrial anti-hypertrophic signals that were restraining it, which drives it further into
hypertrophy. That is a **positive feedback loop mediated by geometry rather than by signalling** — and it
predicts that maintaining transport access at the midplane opposes commitment, i.e. raises `a − b`, by
physical means.

**Two more corrections to my geometry, from the same paper.** *"no indication of a proposed unidirectional
entrance to the growth plate sourced by the epiphyseal vasculature… transport patterns are generally
symmetric from both the E and M vasculatures."* **My one-sided slab is dead for the third and final time.**
And: *"The overall **centrifugal flow pattern** is characteristic of a **resting limb only**; limb
stresses and movement are ex[pected to alter it]."* — **the advective field is load-dependent**, which
ties this directly to the atlas's loading layer and to Serrat's exercise result.

**Also recovered, and directly on this branch's influx arc:** EXT1 mutation → loss of heparan sulfate on
ECM proteoglycans → *"dramatically decreases the interaction of Ihh with the ECM, **increasing the range
of Ihh signaling** within the growth plate and causing an **extended proliferative zone** due to excessive
activation of PTHrP."* **Heparan sulfate is a tunable range-setter for Hedgehog, and reducing it extends
the proliferative zone** — which is exactly the term Longshanks selection moved. (Human EXT1 carriers are
short, so the systemic phenotype is net-negative; the local mechanism is not.)

---

## 4. Brighton & Schaffzin 1970 — the ceiling has a mechanism, and it is blockable

At **90% oxygen**, explants showed:

- **no reduction in the length of the cartilage component** — high O₂ does not stop cartilage production
- progressive **loss of acid mucopolysaccharide stainability** (proteoglycan)
- **narrowing and eventual loss of the zone of hypertrophic cells**
- acellular PAS-positive debris at the bone–cartilage junction
- **marked reduction in length of the bone component**
- **"EACA and chloroquine partially reversed these effects"** — ε-aminocaproic acid (a protease inhibitor)
  and chloroquine (a lysosomal membrane stabiliser)

> **Oxygen toxicity in the plate is lysosomal and proteolytic, it attacks hypertrophy and ossification
> rather than cartilage production, and it is pharmacologically blockable.**

That completes the oxygen axis at both ends: within 2.5–21% pO₂ sets reserve-versus-hypertrophy
(`leijten2012`, via GREM1/FRZB/DKK1); above ~21% it destroys the hypertrophic zone by lysosomal enzyme
release. And it explains Brighton 1969's two-endpoint split — cartilage growth maximal at **21%**,
metaphyseal bone formation maximal at **5%** — as production versus ossification, not one curve.

---

## 5. What this does to the programme

**Delivery is now a solved design constraint, and the news is good.** The two compartments this
programme needs to reach are the two most accessible ones in the tissue:

| target | transport status |
|---|---|
| **reserve zone** (GP1/stem pool, where `a` is set) | **most permeable zone measured** — 5.57 at 22°C — and **most temperature-responsive**, Q₁₀ 1.97 |
| **midplane** (where commitment happens, where `b` is set) | **2–5× more permissive than either junction**; the concentration point for perichondrial signals |
| metaphyseal COJ (discharge) | **the barrier** — 8× ash, D at 31% of reserve, temperature-insensitive, reversible with mineral |

**And it filters agent classes before any of them are named.** Relative to a 332 Da tracer: **3 kDa gets
62%, 10 kDa gets 15%**, and anionic species are further penalised.

| lever | carrier size | reaches the plate? |
|---|---|---|
| pO₂ / HIF stabilisation | gas or small molecule | **yes** |
| Hedgehog agonism (SAG class) | ~0.5 kDa | **yes** |
| oestrogen-receptor blockade | small molecule | **yes** |
| CNP analogue class | ~4 kDa | partial (~50–60%) |
| **IGF-1** | 7.6 kDa | partial (~15–30%) |
| **GREM1 / FRZB / DKK1 / SFRP5 as proteins** | 20–40 kDa | **no — must be induced in situ, not delivered** |
| **growth hormone** | **22 kDa** | **largely excluded in vivo** |

**The pattern is striking and it was not designed: every small-molecule lever in this programme reaches
its target, and every protein lever does not.** The WNT-antagonist set that F-R034 identified as the
`a − b` effector cannot be given as protein — which is precisely why an *inducer* of it (hypoxia/HIF,
or Hedgehog's Wnt-inhibitory environment) is the right shape of intervention.

**And the GH reconciliation strengthens.** F-R035 predicted `chu2026`'s **P = 0.1827** from the size
gate. The numbers now support it quantitatively: GH at 22 kDa sits beyond the 10 kDa point where entry is
already down to 15%, while the explant — 1–2 mm slices bathed in medium — has no barrier at all. **The
direct GH-on-plate effect may be substantially an explant artefact of bypassing the transport block**, and
the experiment that tests it is a size-matched tracer study, not another explant.

---

## 6. The unknowns that remain — complete list

**Tier 1 — still decide the method:**

1. **Does raising `a − b` preserve stem NUMBER in a postnatal plate with intact influx?** `leijten2012`
   used fetal explants with no influx and measured resting-zone **height**, never stem-cell **number**.
   This is the single most important untested step in the current architecture.
2. **Does a Hedgehog-expanded pool persist past one week?** (`trompet2024` counted once, at day 2
   post-dose and at 1 week.) Unchanged from F-R033.
3. **Does a second pulse add a second increment?** Unchanged.
4. **What is the human interstitial flow velocity `v`?** The atlas flags it: Da = kL/v, and v ≈ 2.5 µm/s
   is mouse. A human plate is thicker and slower; if `v` is tenfold lower, Da rises to 0.15–1.85 and the
   transport question reopens for humans specifically. **All transport data in §2–3 are rabbit, rat and
   mouse. There is none in human.**
5. **Is the λ ↔ (a − b) coupling breakable?** Still no agent shown to raise the cycling rate without
   driving commitment.

**Tier 2 — decide how to operate it:**

6. **No sensor for stem number in a living human.** Unchanged, and still the practical blocker on any
   titration scheme.
7. **The pO₂ dose-response between 2.5% and 21%** — I have 2.5/21 (Leijten) and 5/21/90 (Brighton), not
   the shape between. Threshold or gradient is undetermined.
8. **Charge versus size in the metaphyseal block** — Williams could not separate them (no neutral
   dextrans). Decides whether a charge-modified agent bypasses the gate.
9. **Does loading change the advective field favourably?** Williams: the centrifugal pattern is
   *"characteristic of a resting limb only."* Untested, and it connects a solved-looking transport map to
   the atlas's loading layer.

**Tier 3 — decide whether it holds:**

10. **Does ossification keep pace at high velocity?** (`chu2026`: vascularisation dispensable for
    chondrogenesis, essential for ossification.)
11. **The human temperature negative** — Ring & Lee 1958, 40°C at the knee in four children, no effect —
    against a consistent mouse literature. Unresolved.
12. **Species translation of everything clonal.** All mouse.
13. **Is there a permissive midplane in the human plate?** Never measured.

---

## 7. Two things I chased myself rather than ask for

**(a) Serrat 2017 (PMC5792102) — obtained on retry.** *"Imaging IGF-I uptake in growth plate cartilage
using in vivo multiphoton microscopy."* It settles the one endogenous protein lever that sits inside the
gate:

- **Fluorescently labelled IGF-I (7.6 kDa native, 8.2 kDa labelled) is readily taken up**, reaching
  **peak values in the growth plate within ~90 min** after a single IP injection (~6 µg/g).
- It is **bioactive** — over **fourfold** greater p-Akt (Thr308) in treated metatarsals.
- **In the plate it localises to chondrocytes, not matrix** — *"resembles round chondrocytes, suggesting
  receptor-mediated localization."*
- **In the perichondrium it is diffuse and punctate**, which the authors attribute to **IGFBP
  entrapment**: *"IGF-binding proteins (IGFBPs) are **up to 50-fold higher in the perichondrium**
  compared with growth plate."*

**That last point is a delivery bottleneck specific to IGF-1, and it is quantified and modulable.** The
perichondrium is a binding-protein sink standing between the vasculature and the plate; the atlas
separately holds `schneiderman1995`, which measures IGF-I partitioning **an order of magnitude better
free than ternary-complexed**. So for the one protein lever that fits through the size gate, the
rate-limiting step may be **binding-protein displacement at the perichondrium**, not the cartilage
matrix at all.

**(b) Human growth-plate solute transport — searched for, and it does not exist.** Every transport
measurement in §2–3 is rabbit, rat, mouse or pig. The nearest human-adjacent data are gadolinium-enhanced
paediatric MRI studies, which are qualitative imaging rather than transport coefficients, and the
permissive-midplane MRI corroboration is **piglet**. **There is no measured diffusion coefficient, flow
velocity, or size cut-off for any human growth plate at any age.** Unknowns #4 and #13 both turn on this,
and recording the absence is the finding: *the entire delivery argument for a human intervention is
extrapolated from small mammals whose plates are thinner and faster.*

**The experiments that would close Tier 1 do not exist as papers.** They are: a pO₂ or HIF manipulation
in a postnatal plate with stem-cell *counts* as the endpoint; a Hedgehog pulse with pool counts at 1, 2
and 6 months; and a second pulse. Those are the three that decide whether fast, unlimited and non-closing
can be had together, and no amount of retrieval will produce them.
