# F-R031 — Trompet's Figure 5 read, and two corrections to F-R030

You supplied the figure I had been asking for and the paper I called the most important unread one in
the project. Both change things.

---

## 1. `trompet2024` Figure 5 — the kinetics, and they are the pulse model exactly

Reading the panels directly:

**(B–E) Length, paired DMSO-contralateral vs SAG, every animal:**

| | femur | tibia | whole leg |
|---|---|---|---|
| 1 month | ***** (P<0.05) | NS | ****** (P<0.001) |
| 2 months | ****** (P<0.01) | ****** (P<0.01) | ****** (P<0.01) |
| **6 months** | ******* (P<0.001) | ******* (P<0.001) | ******** (P<0.0001) |

**Every paired line rises, in all three panels, at 6 months.** The significance *deepens* with time —
P<0.05 → P<0.01 → P<0.001 for femur, and to P<0.0001 for whole leg. And panel E is the photograph: two
femurs against a ruler, visibly different.

**(G–H) Growth *rate*, calcein–xylenol double label:** significant only at **1 month for femur** and
**2 months for tibia**; **NS at 1 week and NS at 2 months for femur.**

**(J–K) Ki67⁺ cells in the top 50 µm of the growth plate — the resting zone:**

| | 1 week | 1 month | 2 months |
|---|---|---|---|
| femur | **≈4.5% → ≈13%, P<0.01** | NS | NS |
| tibia | **≈8% → ≈19%, P<0.01** | NS | NS |

**(M) Pthlh⁺ cells in the top 50 µm at 1 week: ≈20% → ≈29%.**

### What that sequence says

> **The resting-zone proliferative response is a ONE-WEEK EVENT — roughly a threefold Ki67 spike — and
> it is over by one month. The PTHrP⁺ stem fraction rises ~20% → ~29% in that same week. The SAG signal
> itself is gone by three weeks. And the length gap keeps widening for six months, with the P value
> falling the whole time.**

**A single week of stem-cell proliferation buys at least six months of divergent growth.** That is not
a drug effect being sustained — the drug is long gone. It is **a larger pool, created once, paying out
continuously.** The transient rate differences in G–H are the visible edge of an effect too small to
resolve at any single timepoint but large enough to accumulate into a photograph.

**This is the strongest evidence in the entire project for the pulse architecture**, and it makes the
untested question sharp rather than vague: **the pool was expanded once. Nobody has expanded it
twice.**

---

## 2. Correction to F-R030: GH does **not** push the root tier

F-R030 explained Wadlow's flat nine-year curve by proposing that GH pushes the Prrx1⁺ root tier while
spending the PTHrP⁺ working tier. **`chu2026`'s own quantification refutes that.**

Human growth-plate explants, **7 vehicle and 6 GH donors**, two months in culture, EdU⁺ cells counted
separately in RZ and PZ (Fig. 5L):

> "cell proliferation was significantly (**P = 0.013**) increased in the **PZ** after GH exposure"
> — and the resting-zone comparison in the same panel is **P = 0.79.**

**GH raised proliferation in the proliferative zone and did nothing measurable in the resting zone.**
The abstract's phrasing ("proliferation of cartilage stem cells and chondrocytes in the proliferative
zone") is looser than the data.

**So GH agrees with `PMC12685065` after all: it is a working-tier drug.** It amplifies output
downstream of the stem compartment and does not replenish it.

**Two consequences.**

**(a) F-R030's central argument gets stronger, not weaker.** GH is the largest output driver known, and
it does not touch the stem compartment. **Every within-plate lever fails the second half of the
condition, GH included.** The compartment-crossing route is more clearly the only one.

**(b) I no longer have an explanation for Wadlow's flat curve, and I am not going to invent one.**
The candidates are: his root pool was simply large enough that nine years did not exhaust it; something
recruited that GH does not do directly; or the serial heights, which I assembled from secondary
sources, are not reliable enough to support the inference. **F-R029's observation stands as an
observation; F-R030's mechanism for it is withdrawn.**

---

## 3. Correction to F-R030: the hierarchy conflated two compartments

F-R030 drew a four-tier stack with perichondrium at the top feeding Chu's root cells. **`chu2026`
explicitly excludes perichondrium from its dataset:**

> "Although surgical exclusion of perichondrial cells cannot be fully guaranteed, **gene expression
> analysis for periostin (POSTN) confirmed their absence in our dataset.**"

**Chu's GP1 root population is intracartilaginous.** It is upstream of PTHrP⁺ — velocyto trajectory
analysis puts **GP1 as "the root population" and GP5 as "the terminal end point"** — but it is inside
the plate. The Prrx1 marker is shared with limb-bud and perichondrial mesenchyme, which is what misled
me.

**Corrected structure:**

```
Pdgfrα⁺ INNER PERICHONDRIUM  (outside; rosellodiez2025, mundy2026)
        ⇣  ← this arrow is demonstrated in fetal mouse and UNMEASURED IN HUMANS,
           because chu2026 excluded the compartment by design
GP1  root, Prrx1⁺ PTHrP⁻      (inside the cartilage; low WNT, low TGF-β)
        ↓
GP2  PTHrP⁺                    (the working tier GH spends)
        ↓
GP3 → GP4 → GP5 → bone         (output)
```

**The one arrow that matters most is the one no human dataset has looked for.**

---

## 4. What `chu2026` gives that nothing else does

**(a) The root niche has human markers.** GP1/GP2 are defined by **SFRP5** (a secreted WNT antagonist)
and **APOE**; the niche is *"low in WNT and TGF-β growth factors"*, with **DKK1, GREM1, FGF2, KLF4**
appearing in the regulatory set. SFRP5⁺ cells localise to the RZ while cyclin D1 does not.
**This is the atlas's R241 "self-secreted WNT and TGF-β antagonists" with the human gene names on it**,
and it is the same niche `hallett2021` and `leijten2012` (Frzb/Dkk1) found from two other directions.

**(b) The human organ-culture platform, characterised.** Biopsied human growth plate cut into
**1-mm slices**, maintained **two months**:

> "human growth plate cartilage **retained its structural integrity and biological activity, as
> evidenced by preserved histology and PROTEOGLYCAN ABUNDANCE assessed by SAFRANIN O staining**."

**That is the Safranin-O I have been asking for across four rounds — on human growth plate, at two
months, and it stays proteoglycan-rich.**

**(c) And a result that speaks directly to this branch's oxygen arc:**

> "This persistence of cartilage viability is consistent with its **avascular nature, which allows
> diffusion-based nutrient supply** in vivo. In contrast, **bone did not expand ex vivo**… indicating
> that **vascularization is dispensable for chondrogenesis but essential for ossification.**"

**Cartilage grows on diffusion alone; bone does not.** F-R013–F-R016 built a transport-limitation
argument that has to be read against this: at 1 mm, diffusion suffices for two months. It does not
refute transport limitation in an intact epiphysis with a far longer path, but it does mean **the
cartilage engine is not intrinsically vessel-dependent**, and the limiting step in ossification is.

**(d) The honest limitation on GH.** *"GH treatment caused a measurable expansion of growth plate
cartilage, although **not all patient samples responded**… This variability may reflect known
interindividual differences in GH responsiveness among children."*

---

## 5. Where the three terms stand

| term | status |
|---|---|
| **never close** | **Solved and controllable both ways in humans** — receptor-level blockade survived a 10× challenge; 25 µg twice weekly closed a 31-year-old in 6 months. |
| **constant** | **The pulse architecture is now demonstrated**: one week of RZ proliferation → six months of divergent length, in a normal animal with a contralateral control. |
| **fast** | **Not endocrine at the stem level.** GH raises PZ output (P=0.013) and not RZ (P=0.79). The remaining levers are the local ones — pO₂/proteoglycan, confinement, convection — plus recruitment. |

**The single unanswered question is unchanged and now sharper: the pool has been expanded once, by a
one-week pulse, with a six-month payout. Nobody has fired a second pulse, and nobody has measured
whether the human root tier can be resupplied from outside the cartilage.**

---

## 6. Asks

**#1 — `chu2026`'s supplementary figures S8A–C.** The GH explant response per donor — *"not all patient
samples responded"* — and the Safranin-O quantification. **The non-responders are as informative as the
responders**, and if the supplement carries donor age or bone age, it may show that the response tracks
plate state rather than GH dose. You have the main text; the supplement is a separate file on the
Science site.

**#2 — `chu2026` reference 43**, the human growth plate organ-culture method paper. Chu cites it as
*"our previously established organ culture model"* — that is the protocol paper for the platform every
remaining experiment in this project would use. It is almost certainly Sävendahl's group at Karolinska.

**#3 — anything on repeat or cyclical Hedgehog dosing in bone**, still returning nothing in my
searches. If it does not exist, that absence is itself the next finding, and the experiment is one
bead replaced at three months.

**Still standing:** Brighton thesis (UIC ILL `10027/14248`); JBJS 1980;62A:740; Surgical Forum
1970:465–467; `stegen2019` DCA+BPTES tibia length; the lateral thoracolumbar film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
Two instruments arrived this round and both corrected me. A Ki67 count at one week showed the pool
expansion is a single event, not a sustained state. An EdU count separated by zone showed the largest
growth drug in medicine does not touch the compartment that matters. I had a mechanism for Wadlow's
curve for exactly one round.*
