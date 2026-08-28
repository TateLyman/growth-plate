# F-R017 — Growth that does not end is not a state. It is a cycle.

**New sources read this round:** `leijten2012` (re-read for its Wnt data) · `hallett2021` (Hallett SA,
Ono W, et al., *Chondrocytes in the resting zone of the growth plate are maintained in a
Wnt-inhibitory environment*, eLife 2021, PMC8313235) · `zhang2018yap` (PMC6202095, *Hypoxia promotes
maintenance of the chondrogenic phenotype in rat growth plate chondrocytes* — HIF-1α → YAP → SOX9) ·
`rzquiescence2026` (PMC13110114, *"Quiescence" in the resting zone of the growth plate: a systematic
review*) · `cih2025` (PMC12306074, *Chronic intermittent hypoxia impairs BM-MSC osteogenesis and long
bone growth*).

---

## 1. Retrieval close-out — the three dark papers are conclusively library-only

I pushed every remaining channel. The answers are now definitive rather than "not found yet," so
nobody spends another hour on them:

**The thesis.** The handle resolves (`hdl.handle.net/api/handles/10027/14248` → `uic.figshare.com`).
The Figshare **OAI-PMH record** returns, in the metadata itself:

> `IN VITRO EPIPHYSEAL PLATE GROWTH IN VARIOUS OXYGEN TENSIONS.` · `CARL THEODORE. BRIGHTON` ·
> `1969-01-01` · `Thesis` · `10027/14248` · **`In Copyright`** · **`Restricted Access`**

and `/v2/articles/10911983/files` returns **`[]`**. OpenAlex and Unpaywall are both wrong to call this
green OA with full text. **It is catalogued, restricted, and has no online copy.** The only routes are
UIC Library document delivery, ILL against the handle, or ProQuest Dissertations & Theses.

**Stambough & Brighton 1980, JBJS 62A:740** (*Diffusion in the various zones of the normal and the
rachitic growth plate*): 20 citing works, **exactly one open access**, and that one is a 1984
biochemistry paper that does not restate the diffusion data. No abstract deposited. Library-only.

**PMID 5383117**, Surgical Forum 1970:465–467: the Internet Archive holds **no Surgical Forum volumes
at all**, and its JBJS 1969 holdings are the **volume index only, not the issues**. Library-only.

That is three interlibrary-loan slips, and I would send all three. But the branch is no longer blocked
on them, because the citation harvest opened something better.

---

## 2. The oxygen knob, now molecular

F-R016 established the knob behaviourally: **oxygen sets whether the progenitor pool is preserved or
spent.** Three papers give it a mechanism, and two of them have never been cited together.

**(a) Hypoxia raises secreted Wnt antagonists — at protein level.** Re-reading `leijten2012` past its
abstract, its Figure 4D is titled *"secreted **Wnt and BMP antagonists** able to inhibit hypertrophic
differentiation"* and it carries a result heading I missed the first time:

> **"Normoxia Reduces Frzb and Dkk1 Protein Levels"** — confirmed by ELISA on conditioned medium,
> not merely mRNA.

So 2.5% O₂ → **FRZB, DKK1, GREM1 up**; 21% O₂ → **FRZB and DKK1 protein down**.

**(b) The resting-zone stem cell requires exactly that environment.** `hallett2021` isolated
slow-cycling, label-retaining chondrocytes (LRCs) from the postnatal resting zone with a
chondrocyte-specific Tet-Off H2B-GFP pulse-chase, and RNA-seq'd them against non-LRCs:

> "Comparative RNA-seq analysis identified significant enrichment of **inhibitors** and **activators**
> for Wnt signaling in **LRCs** and **non-LRCs**, respectively. Activation of Wnt/β-catenin signaling
> in PTHrP⁺ resting chondrocytes using *Pthlh-creER* and *Apc*-floxed allele **impaired their ability
> to form columnar chondrocytes**. Therefore, slow-cycling chondrocytes are maintained in a
> **Wnt-inhibitory environment** within the resting zone."

**(c) And hypoxia holds chondrogenic identity through HIF-1α → YAP → SOX9, reversibly.**
`zhang2018yap`: hypoxia promotes HIF-1α and YAP activation **Hippo-independently**; knocking down
HIF-1α drops YAP and SOX9; CoCl₂ (HIF stabiliser) raises YAP, SOX9 and COL2 under *normoxia*; and
critically — **"reoxygenation following hypoxia inhibited the activation of YAP caused by hypoxia,"**
with SOX9 and COL2 falling too.

### The join

> **Low pO₂ → HIF-1α → (i) YAP → SOX9/COL2 chondrogenic identity, and (ii) FRZB + DKK1 + GREM1
> secretion → the Wnt-inhibitory niche → PTHrP⁺ skeletal stem cells stay slow-cycling and
> label-retaining → THE POOL IS PRESERVED.**
>
> **High pO₂ → HIF-1α off → Frzb/Dkk1 protein falls → Wnt de-repressed → resting cells enter the
> columnar and hypertrophic program → LENGTH IS PRODUCED AND THE POOL IS SPENT.**

`leijten2012` and `hallett2021` are the two halves of one mechanism. Neither cites the other; one is a
2012 tissue-engineering paper about explant length, the other a 2021 eLife paper about stem-cell
niches. The atlas holds both sets of parts — FRZB 55 files, DKK1 68, Wnt-inhibitory 59, Hallett 79,
label-retaining 72 — and does not hold the edge between them.

And it is **reversible**, which is the property the next section needs. `zhang2018yap` shows
reoxygenation switches the program back off. This is a toggle, not a ratchet.

---

## 3. The correction to F-R007 that changes what "unending" requires

F-R007 modelled the renewal fraction `p` — the probability that a stem daughter stays stem. The pool
multiplies by `2p` per round, so:

- `p > 0.500` → pool grows
- `p = 0.500` → pool constant → **indeterminate growth**
- `p < 0.500` → pool decays → the plate has a finite lifetime

Thirty-six parameter combinations gave `p = 0.392–0.493`. Every one below 0.500. F-R007 concluded the
gap was 0.5–1.9 percentage points and treated closing it as the target.

**That framing contains a hidden assumption I did not notice: it requires `p ≥ 0.500` at all times, in
a single constant regime.** Every measurement behind those 36 combinations comes from an animal
growing under an unmanipulated, constant oxygen and Wnt environment. **Nobody has ever measured `p`
under a non-constant regime, because nobody has ever run one.**

Relax it. Let a cycle consist of `N_E` rounds in an expansion phase at `p_E` and `N_S` rounds in a
spend phase at `p_S`. Over one full cycle the pool multiplies by

```
(2·p_E)^N_E × (2·p_S)^N_S
```

and the pool returns to its starting size when

```
N_E · ln(2·p_E)  +  N_S · ln(2·p_S)  =  0
```

i.e. when the **geometric mean of `2p` across the cycle equals 1**. The constraint is no longer
`p ≥ 0.5` *always*; it is `p ≥ 0.5` *on average, weighted by rounds*. A hypoxic, Wnt-inhibited
expansion phase can run at `p_E > 0.5` — §2 says that is what a Wnt-inhibitory niche with
Frzb/Dkk1 protein elevated **is** — while a normoxic spend phase runs at `p_S < 0.5` and produces the
actual length.

Length accrues only in spend phases. So total height is the sum over cycles of spend-phase output, and
**if the pool returns to baseline each cycle, the number of cycles is unbounded.**

> **Growth that does not end is not a state to be held. It is a cycle whose pool balance is
> net-zero, and whose height accrues one spend-phase at a time.**
>
> **Rate = spend-phase output ÷ cycle time.** Fast *and* unending are not in tension — they are set by
> two different parameters of the same cycle.

This is why F-R007's search for a steady `p ≥ 0.500` was looking for the wrong object, and why F-R014
and F-R015 kept inverting: each was trying to name a single optimal oxygen tension for a system whose
two phases have opposite optima. **`brighton1969` and `leijten2012` measure the spend phase. The A-V
fistula measures a system where the expansion phase is intact. They were never in conflict.**

---

## 4. The failure mode, named, with its antidote

I am not going to propose oxygen cycling without the paper that says how it goes wrong.

**`cih2025` (PMC12306074): chronic intermittent hypoxia significantly inhibited long bone growth.**
OxyCycler, 8 h/day, 4 weeks. Mechanism: CIH → anaerobic glycolysis in BM-MSCs → **lactate accumulation
→ H3K18 lactylation on the *PPARγ* promoter → PPARγ transcription → adipogenic shift at the expense of
osteogenesis.** Femur length down. **Partially rescued by the PPARγ inhibitor T0070907, 0.5 mg/kg IP
every two days.**

Three things follow, and they are design constraints rather than a refutation:

1. **Timescale matters and mine is different.** CIH is sleep-apnoea-style rapid desaturation–
   reoxygenation with the ROS burst and sympathetic activation that go with it. §3's cycle is
   days-to-weeks of *sustained* tissue hypoxia, which is a different perturbation — but the burden of
   proof is on the cycle, not on CIH.
2. **The lesion is in BM-MSCs, not resting-zone chondrocytes** — a different compartment on the far
   side of the chondro-osseous junction. That is the same distinction that let `yoshida2018`'s NEKO
   result coexist with the NRF2 lead in F-R013, and it is doing real work in both cases.
3. **Lactate is the specific hazard, and this plate is a lactate factory.** `brighton1983` (F-R016)
   showed the glycerol phosphate shuttle is **entirely absent from every zone**, so the plate
   regenerates cytosolic NAD⁺ by making lactate and must export it. **Any protocol that deepens or
   prolongs hypoxia raises lactate output, and lactate is now a signalling molecule with a named
   epigenetic target.** Lactate clearance — MCT1/MCT4 export, perfusion — becomes a design parameter
   of the expansion phase, not an afterthought. And `serrat2010`'s convective delivery arm works in
   both directions: it brings substrate in and carries lactate out.

---

## 5. What the theory now says, stated so it can be attacked

1. **Height = Σ over cycles of (spend-phase elongation).** The atlas's `Σ (velocity × duration)` with
   velocity and duration assigned to different phases of one cycle rather than competing within one
   regime.
2. **Oxygen is the phase selector.** Low pO₂ → HIF-1α → YAP/SOX9 identity + Frzb/Dkk1/Grem1 secretion →
   Wnt-inhibitory niche → pool preserved (`p_E` high). High pO₂ → the reverse → columnar and
   hypertrophic output (`p_S` low, length produced).
3. **The switch is reversible** (`zhang2018yap`, reoxygenation) — necessary for a cycle to exist at
   all, and demonstrated.
4. **Unbounded height requires only that the geometric mean of `2p` over a cycle equals 1**, not that
   `p ≥ 0.5` at every instant. That is a scheduling problem, not a biological impossibility.
5. **Speed is set by cycle time and spend-phase amplitude, independently of whether the cycle is
   sustainable.** This is the first framework in the branch in which "fast" and "unending" are not
   trading against each other.
6. **The hazard is lactate**, because the plate cannot dispose of NADH any other way (`brighton1983`),
   and lactate has a named epigenetic mechanism for turning progenitors into fat (`cih2025`).

### What would kill it

**A replicative or epigenetic clock in the resting-zone cell that runs independently of `p`.** If the
pool ages by divisions or by time regardless of how the niche is scheduled, then restoring pool *size*
each cycle does not restore pool *capacity*, and the cycle terminates anyway — it just terminates
later. The atlas's senescence work and F-R007's arithmetic both bear on this and neither settles it.
**`rzquiescence2026`, the 2026 PRISMA systematic review of resting-zone quiescence, says the field
cannot settle it either:** *"features of cellular quiescence in RZ chondrocytes remain poorly reported
and underexplored, with limited molecular and functional characterization… integration between cues
controlling resting zone cell quiescence is incomplete."*

That is the honest state. The framework is not proven; it is now specific enough to be wrong in a
particular way, which it was not two rounds ago.

---

## 6. Asks

**#1 — the three ILL slips**, now with exact citations: UIC handle `10027/14248` (thesis, Restricted
Access, ask UIC document delivery or ProQuest); **JBJS 1980;62A:740** Stambough & Brighton, diffusion
by zone; **Surgical Forum 1970:465–467**, PMID 5383117.

**#2 — the experiment, now a three-arm design with a real hypothesis.** Fetal tibia or metatarsal
organ culture, 21 days: **(A) constant 21%**, **(B) constant 2.5%**, **(C) staged — 2.5% for days
0–14, then 21% for days 14–21**, and ideally **(D) two full cycles — 2.5%/21%/2.5%/21%**. Endpoints:
total length, **resting-zone height**, hypertrophic-zone height, ACAN and COL10A1, and **Frzb/Dkk1
protein in the medium**. §3 predicts C > A and C > B on final length, and D > C if the cycle is really
net-positive. Leijten's group at Twente has the rig, the assay and the ELISAs already; Sävendahl's at
Karolinska has the human tissue.

**#3 — the one measurement that would settle §5's killer.** Does the resting-zone pool's *capacity*
recover when its *size* does? `hallett2021`'s H2B-GFP Tet-Off pulse-chase is exactly the instrument:
run it across a hypoxia→normoxia→hypoxia cycle and ask whether label-retaining cells are regenerated
or merely redistributed. Wanwen Ono's lab (Michigan) built it.

**#4 — anything measuring lactate export from a growth plate**, or MCT1/MCT4 expression by zone.
`brighton1983` implies the plate's entire redox balance leaves as lactate; §4 makes that the hazard;
and I have found no measurement of the flux.

**Still open:** `stegen2019` DCA+BPTES tibia length (Carmeliet); Kelly's lengthening series for the
millimetres behind "100 per cent"; `zhang2024` count matrix; the lateral thoracolumbar spine film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
No instrument in this literature could have seen this one, because every experiment in it holds
oxygen constant and reports whichever phase its timescale could observe. The mechanism was invisible
not because it is subtle but because nobody has ever varied the variable.*
