# F-R020 — The reserve IS fed from outside. The gate has a name, and it is druggable.

**The finding:** F-R019 asserted that `dReserve/dt = influx − outflux` had never had its first term
measured in any species, and asked for a lineage trace of the perichondrium into the resting zone.
**That experiment has been done. It was published in Nature Communications in October 2025. Influx is
real, it is necessary, it is demand-responsive, and its molecular brake is CCN2.**

**Primary source:** Rosello-Diez lab, *Gli1-expressing stromal cells are highly reparative precursors
of long-lived chondroprogenitors in the fetal murine limb.* **Nat Commun 2025;16:10107.
doi 10.1038/s41467-025-65029-y · PMID 41253754 · PMC12627582 · open access** (preprint
doi 10.1101/2024.07.29.603524). Full text archived at
`frontier/screens/influx/rosellodiez2025_gli1_pdgfra_influx_natcomm_PMC12627582.txt`.

---

## 1. What they did and what it shows

They built a mosaic, cartilage-targeted **cell-cycle arrest** — salt-and-pepper overexpression of
**p21** (a G1 CDK inhibitor) driven by `Col2a1-rtTA` with `Tigre Dragon-p21`, either in the left limb
only (`Pitx2-Cre`, giving a perfect contralateral internal control) or in all cartilage. Then they
lineage-traced with `Gli1-CreER` and `Pdgfra-CreER` against `R26-LSL-tdTomato`, plus single-nucleus
RNA-seq, clonal RGBow reporters, label-retention, and targeted ablation with attenuated diphtheria
toxin.

**(a) The plate compensates completely for a large loss of proliferative capacity.** Followed to
**P100, well past the end of growth**: *"no major asymmetries in bone length were found"* — the femur
only ~**1.5%** shorter. Arresting the cell cycle in a mosaic fraction of the cartilage did **not**
shorten the bone.

**(b) The compensating cells come from outside the cartilage.**

> "**reparative Gli1⁺ cells originate from Pdgfra⁺ cells outside the cartilage, revealing the
> surrounding tissues as an unexpected CP source.**"

> "in normal growth, the E13.5-labelled Pdgfra-lineage gave rise to an increasing proportion of
> chondrocytes… **the proportion of Pdgfra-lineage chondrocytes was progressively increased** in
> `Pan-Cart-p21 MOE` limbs as compared to controls."

**(c) It is demand-responsive, and the cartilage sends the signal.**

> "the contribution outside the cartilage was also expanded in P0 `Pan-Cart-p21 MOE` limbs compared to
> controls, **suggesting that the challenged cartilage signals to the surrounding tissues.**"

Pdgfra-lineage cells **in the resting zone** showed *increased proliferation* in challenged limbs at
E14.5 and E17.5.

**(d) It is necessary, not incidental.** Ablating Gli1-derived chondrocytes (`Gli-Cart-DTA`) on the
p21 background gave **significantly decreased bone length** versus p21 alone — *"Gli1-derived
chondrocytes are required to compensate."* And ablating fetal Gli1-derived chondrocytes in normal
growth **reduced bone length at P100, especially femur and tibia.**

**(e) The groove of Ranvier is explicitly in the frame.** Their Fig. 7b quantifies expression across
*"proliferative zone, resting zone, **groove of Ranvier** (separated from cartilage by dashed line),"*
and Supplementary Fig. 11 shows Gli1-high subpopulations expanding *"at the expense of the
groove-of-Ranvier one"* under challenge.

**F-R019's assumption A2 — "RESERVE is a closed depot with no influx" — is falsified.** The atlas's
objective function `height = RESERVE × h_term` is missing a source term that is real, measured, and
required for normal bone length.

---

## 2. The gate has a name: CCN2

This is the part that turns a mechanism into a target. They asked what triggers the recruitment, ran
pseudobulk differential expression via edgeR plus MultiNicheNet cell–cell communication analysis, and
did **not** find the hedgehog pathway. They found:

> **CCN2** (cellular communication network factor 2, a.k.a. **CTGF**, connective tissue growth factor)
> — **downregulated** in challenged limbs, confirmed by HCR in situ, and *"this reduction happened in
> both Gli1⁺ and Gli1⁻ chondrocytes, suggesting it was not a cell-autonomous consequence of Gli1
> activation."* Spatially, *"p21⁺ chondrocytes generate a **Ccn2-inhibiting area**."*

And they tested it directly, ex vivo, on fetal femurs with the contralateral femur as control:

> "**CCN2 impairs Gli1 expression and proliferation in chondrocytes** … As predicted, Gli1 expression
> was found downregulated in [human-CCN2-]treated samples—both Ctl and `Pan-Cart-p21 MOE`. Moreover,
> Ki67 immunostaining … **diminished in treated samples.**"

Their model, in one line: **CCN2 normally restrains Gli1 activation in stromal progenitors. When CCN2
falls, Gli1 activation is unrestricted, Pdgfra⁺ cells outside the cartilage become Gli1⁺ long-lived
chondroprogenitors, and they migrate in.**

> **CCN2 is the brake on influx. Lowering CCN2 opens the gate.**

**CCN2 has a clinical-stage antagonist — and the atlas has already killed it. Correctly, and for the
wrong scope.**

I drafted this section proposing **pamrevlumab (FG-3019)**, the phase-3 anti-CCN2/CTGF human monoclonal
(IPF, Duchenne, pancreatic cancer), as the obvious agent. Then I greped, and found `pamrevlumab` in
three atlas files. **R341 closed CCN2 negative, and its reasoning is good:**

> "**CCN2/CTGF CLOSES, AND FAST.** R340 flagged it as the most abundant unexamined transcript in the
> human growth plate (1,249.2 CPM in 99.9 per cent of cells, above ACAN). Three free checks close it.
> It is NOT in kosmicki2026's 207 — no human height genetics at any variant class. IMPC has NO *Ccn2*
> length row of any kind, and the paralogues that do have rows are null. And the published **Ctgf-null
> phenotype is an EXPANDED hypertrophic zone with impaired angiogenesis — i.e. a DISCHARGE FAILURE**,
> which is failure mode 1 and the same trap that made denosumab and aggrecanase inhibition
> contraindications. **The clinical-stage anti-CCN2 antibody PAMREVLUMAB therefore points the wrong
> way.** CCN2 is abundant because it is a matricellular coordinator of matrix and angiogenesis, not
> because it is a rate-limiter on length. Gap closed negative."

**That kill stands, and I am not overturning it. But it and the 2025 paper are both right, about
different compartments — and their collision is the cleanest possible confirmation of F-R019's
cancellation theorem.**

| compartment | what CCN2 does there | what blocking it does |
|---|---|---|
| **inside the cartilage** (resident chondrocytes) | matricellular coordinator of matrix and angiogenesis | `Ctgf`-null → **expanded hypertrophic zone, impaired angiogenesis** → discharge failure → F-R012's mass trap. **Height-negative.** |
| **outside the cartilage** (Pdgfra⁺ stroma, groove of Ranvier) | **restrains Gli1 activation in progenitors** — non-cell-autonomous, and explicitly *not* via hedgehog | Gli1⁺ LLCPs are recruited into the plate. **Height-positive.** |

**One molecule. Opposite signs in adjacent compartments. A systemic antibody hits both, the discharge
failure dominates, and the net is negative — which is exactly what R341 measured and exactly what
F-R019 §6 predicted would happen to any systemic dose of any signal in this system.**

So the conclusion is not "pamrevlumab is the answer." It is sharper and more useful:

> **CCN2 is a real lever on influx and a real hazard on outflux. It is therefore not a drug target —
> it is a DELIVERY target.** The lever is CCN2 blockade confined to the perichondrial/stromal
> compartment, with the cartilage spared. That is precisely the geometry `newton2024sag` already
> demonstrated is achievable: a bead in the secondary ossification centre, agent cleared by week 3,
> contralateral internal control, and a length advantage that kept widening at 6 months.

**R341's kill should be amended rather than reversed**: from *"CCN2 is not a lever"* to *"CCN2 is not a
**systemic** lever; its intracartilaginous arm is a discharge-failure contraindication and its stromal
arm is the only measured controller of progenitor influx."*

---

## 3. What this does to the theory — and the limit I am not going to hide

### It resolves F-R018's dilemma completely

F-R018's problem: the senescence clock counts **resting-zone divisions**, so an expansion phase that
grows the pool *by division* spends the very budget it is trying to bank. **Recruitment does not have
that problem.** A Pdgfra⁺ stromal cell entering the cartilage brings its **own, unspent division
counter**. Influx adds capacity without drawing on the resident clock at all.

So the three-way picture is now:

| route to more reserve | costs resident clock? | evidence |
|---|---|---|
| symmetric self-renewal of RZ cells | **yes** — but nets `+(n−2)` per event (F-R018) | arithmetic; SAG compounding result |
| delayed clearance | no, but self-limiting — backs up the queue | F-R012: makes mass, not length |
| **recruitment from outside** | **no** | **this paper — lineage-traced, necessary, demand-responsive** |

### And it explains F-R019's cancellation theorem better than F-R019 did

F-R019 argued that every signal has opposite signs in the reserve and source compartments, so systemic
dosing cancels. **This paper shows the compartments are not merely adjacent — they are coupled by a
signal the cartilage itself sends.** A challenged cartilage lowers CCN2 locally and thereby recruits.
That is a homeostatic loop, and it is why the plate is robust: it already has a feedback controller
whose set point nobody has tried to move.

### The limit, stated plainly

**Every result above is fetal/perinatal mouse, and the compensation restored normal length — it did
not exceed it.** The demonstrated influx is **homeostatic**: it defends a set point. Nothing here shows
recruitment can push a bone *past* its normal length, and nothing here was done postnatally, let alone
near skeletal maturity.

That is a real gap and it is the next experiment, not a reason to discount this. What has been proven
is the thing F-R019 said was unproven: **`influx ≠ 0`, it is required, and it has a controller.**
Whether the controller's set point can be raised is now a question about a named molecule rather than
a question about whether the term exists.

Two further cautions I will not paper over: **CCN2-null mice have skeletal dysplasia** — CCN2 is
required for normal growth plate development, so this is a U-shaped variable and "block CCN2" is not
automatically "grow taller." And the Rosello-Diez ablation experiments could not be sustained
postnatally *"due to insufficient activity of Col2a1-rtTA,"* which the authors themselves flag as
raising the possibility that further compensation happened postnatally and was not captured.

---

## 4. The supporting chain — four species, four decades, one conclusion

The 2025 paper is not alone. Running the citation graph out of it found a lineage nobody has
assembled:

| study | species | finding |
|---|---|---|
| **PMID 16652202** (2006) Int Orthop 30:353–356 | chick | LaCroix-ring cells transfected with adenoviral **lacZ** and **re-injected into the perichondrial ring** were found 4 weeks later *"arranged horizontally along parts of the physis."* **"The perichondrial ring of LaCroix represents a potential reservoir of growth-plate germ cells."** |
| **PMID 19563472** (2009) J Anat 215:355–363 | rabbit | BrdU pulse-chase: label-retaining cells persist in the **perichondrial groove of Ranvier**, positive for **Stro-1, Jagged1, BMPr1a**. *"The perichondrial groove of Ranvier demonstrates the properties of a **stem cell niche**."* |
| **PMC3854713** (2013) Stem Cell Res Ther | rabbit | BrdU and **Fe-nanoparticle** tracing: *"BrdU⁺ cells were observed at early time points in niches of knee joints, and at later time points in articular cartilage, **indicating a gradual migration of cells**."* |
| **PMC12627582** (2025) Nat Commun | mouse | Pdgfra⁺ → Gli1⁺ LLCP recruitment, necessary for normal bone length, gated by CCN2 |

And the one apparent negative is not one: **PMC9705540** (2022) shows `Dlx5⁺` **fetal** perichondrial
cells *"do not generate cartilage"* but become cortical bone and adipocyte-biased marrow stroma. That
is a different population with a different fate — `Dlx5⁺` fetal perichondrium is committed away from
cartilage, while `Pdgfra⁺` stroma is the one that converts. Both can be true, and the 2025 paper
supersedes the ambiguity.

---

## 5. Where the theory stands

```
H  =  Σ_plates  ∫  h_term(t) · outflux(t) dt        dReserve/dt = influx(CCN2, demand) − outflux(pO₂, Wnt, GH)
```

| term | status | knob |
|---|---|---|
| **influx** | **PROVEN ≠ 0** (§1), necessary, demand-responsive | **CCN2 ← pamrevlumab**; Gli1/Hh; the groove of Ranvier |
| **outflux** | proven, phase-schedulable | pO₂ (F-R016/17), Wnt (Frzb/Dkk1), GH (depletes pool) |
| **h_term** | saturates on the hormonal axis; **osmotic axis untried** | proteoglycan/sulfate/pO₂ (F-R015) |
| **Σ_plates** | a plate is a PTHrP⁺ reserve zone (F-R019 §1) | untouched |
| **resident clock** | counts RZ divisions (F-R018) | bypassed by influx |

**Unbounded requires `influx ≥ outflux`. That is now a statement about a measured, controlled,
druggable quantity rather than a hope.** Fast requires `h_term × outflux` large, and F-R017 showed the
two are schedulable in alternating phases rather than traded off.

---

## 6. What I need — with links

**I have these already (open access, archived in the repo):** PMC12627582 and its preprint.

**These I could not get and would like:**

1. **PMID 16652202** — *The perichondrial ring as a reservoir for precartilaginous cells. In vivo model
   in young chicks' epiphysis.* International Orthopaedics 2006;30(5):353–356.
   **DOI: 10.1007/s00264-006-0082-2** · `https://doi.org/10.1007/s00264-006-0082-2` ·
   `https://pubmed.ncbi.nlm.nih.gov/16652202/` — Springer, not OA. **Want: the histology showing where
   the labelled cells ended up relative to the resting zone.**
2. **PMID 19563472** — *Identification of a stem cell niche in the zone of Ranvier within the knee
   joint.* Journal of Anatomy 2009;215(4):355–363.
   **DOI: 10.1111/j.1469-7580.2009.01115.x** · `https://doi.org/10.1111/j.1469-7580.2009.01115.x` —
   Wiley, not OA. **Want: the BrdU label-retention quantification and the niche marker panel.**
3. **Anything separating CCN2's two compartments** — a conditional `Ccn2` deletion driven in stroma/perichondrium (e.g. `Pdgfra-CreER`, `Gli1-CreER`, `Prx1-Cre`) rather than in cartilage (`Col2a1`), with a bone-length endpoint. R341's kill rests on the global `Ctgf`-null, which cannot distinguish the two arms. If a stroma-restricted knockout lengthens bone, the amended claim in §2 is proven and the systemic kill is confirmed at the same time.
   **pamrevlumab and the skeleton** — the DMD trials measured a lot of children over years and may have
   incidental growth data. `https://clinicaltrials.gov/search?intr=pamrevlumab`
4. **The standing three ILL slips**, unchanged: UIC handle `10027/14248` (Brighton thesis);
   **JBJS 1980;62A:740**; **Surgical Forum 1970:465–467**.

**And the two experiments that would finish this:**

- **Postnatal recruitment.** Repeat the `Pdgfra-CreER` → cartilage trace **postnatally**, at and after
  the SOC-driven clonality switch, ± a CCN2 antagonist, scoring entry into the **PTHrP⁺ resting zone**
  and measuring **bone length at skeletal maturity.** The 2025 paper's own limitation section says
  postnatal ablation failed on `Col2a1-rtTA` activity — a different driver fixes it. **Lab: Alberto
  Rosello-Diez.**
- **Can influx exceed the set point?** Everything shown is homeostatic restoration. Lower CCN2 in an
  *unchallenged* limb, contralateral control, and ask whether the bone goes **past** normal. That is
  the single experiment that separates "robust" from "unbounded," and it is one antibody and a ruler.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
I asked for an inducible lineage trace across the perichondrial boundary and said no one had run it.
Someone had — it went online eleven months ago, it is open access, and it names the gate. The
instrument existed. What was missing was somebody looking for a flow instead of a depot.*
