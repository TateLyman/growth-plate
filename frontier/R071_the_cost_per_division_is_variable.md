# F-R071 — The cells are not exhausted, the cost per division is variable, and OSK may push the wrong way

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** Theoretical analysis. All three F-R070 requests exhausted by search; two abstracts obtained that
change the framework in opposite directions.

**Three findings, and I found the third by reading carefully rather than by wanting it.**

1. **Growth-plate chondrocytes are not intrinsically exhausted.** Cells from old animals divide as well in
   culture as cells from young ones. **The limit is not Hayflick, not telomeres, not cell-intrinsic. It is
   in vivo and epigenetic.**
2. **The cost per division is variable, and oestrogen raises it.** This is a genuine escape from the
   conservation law I stated in F-R066 — and it comes from the branch's own core literature.
3. **The OSK route has a direction problem I did not anticipate**, and it is specific enough to be
   disqualifying if it holds.

---

## 1. The cells are fine — the limit is not in them

**Nilsson O, Mitchum RD, Schrier L, Ferns SP, Barnes KM, Troendle JF, Baron J. "Growth plate senescence is
associated with loss of DNA methylation." *J Endocrinol* 2005;186(1):241–9. PMID 16002553.**

> **"we found that the number of population doublings of rabbit resting zone chondrocytes in culture **did
> not depend on the age of the animal** from which the cells were harvested, suggesting that the mechanisms
> limiting replicative capacity of growth plate chondrocytes **in vivo are distinct from those in vitro**."**

> ### Take resting-zone chondrocytes out of an old rabbit and they divide as many times as cells from a young one. **The senescent plate is not made of exhausted cells.** Whatever limits growth is imposed *in vivo* and is not carried by the cell as a hard, intrinsic counter. **The Hayflick/telomere model of growth-plate senescence is excluded by direct experiment**, and F-R067's framing — a counter each cell carries — needs this qualification.

**And the epigenetic finding, with its specificity:**

- **DNA methylation decreased with age in resting-zone chondrocytes in vivo**
- The loss occurred **specifically with the slow proliferation of RZ chondrocytes in vivo**
- **NOT** with rapid proliferation of PZ chondrocytes (methylation unchanged from resting zone to
  hypertrophic zone), **NOT** in vitro, **NOT** in the liver

**Baron's own conclusion, verbatim:**

> **"loss of DNA methylation might be a **fundamental biological mechanism that limits longitudinal bone
> growth in mammals, thereby determining the overall adult size of the organism**."**

**That is the branch's thesis, written in 2005 by the group that defined growth-plate senescence.**

---

## 2. The escape hatch: cost per division is not fixed

**Schrier L, Ferns SP, Barnes KM, Emons JA, Newman EI, Nilsson O, Baron J. "Depletion of resting zone
chondrocytes during growth plate senescence." *J Endocrinol* 2006;189(1):27–36. PMID 16614378.**

**Confirmed, directly measured:** RZ chondrocyte proliferation rate falls with age; **RZ chondrocyte number
per area of growth plate falls with age**; **dexamethasone decreased RZ proliferation and slowed the
numerical depletion** — banking, measured at the cell-count level.

**But the result that matters most is the one they could not explain:**

> **"Estrogen is known to accelerate growth plate senescence. However, we found that estradiol cypionate
> treatment **slowed** resting zone chondrocyte proliferation… We speculate that estrogen might accelerate
> senescence by a **proliferation-independent mechanism, or by increasing the loss of proliferative capacity
> per cell cycle**."**

**Oestrogen slows resting-zone division and yet accelerates senescence.** A pure division-counter cannot
produce that.

> ### F-R066 stated a conservation law: *every centimetre grown advances the programme by a fixed amount.* **That is wrong, and this is the correction.** The advance per division is **not a constant** — oestrogen raises it. The law is really
>
> ```
> clock advance  =  Σ over divisions of ( cost per division )
> ```
>
> **and `cost per division` is a modulated variable, not a physical constant.** That is the first genuine escape from the conservation law the branch has had, and it was in Baron's 2006 discussion the whole time.

**Two consequences that change the stack's rationale:**

1. **The anti-oestrogen arm gets a much better reason than "it delays fusion."** It **lowers the cost of
   every division you spend.** Under this reading, oestrogen removal does not merely postpone the endpoint —
   it makes each unit of growth cheaper in capacity. **That is qualitatively different and much more
   valuable.**
2. **It joins CXXC5 (F-R067).** Oestrogen → CXXC5 → Wnt shutdown across all three zones. **A per-cycle cost
   term is exactly what a transcriptional brake applied every cycle would look like.**

---

## 3. The problem I did not anticipate: OSK may push the wrong way

**This is the hole this round found, and it is specific.**

| | direction |
|---|---|
| **Growth-plate senescence** (Nilsson 2005, in vivo, global) | **methylation is LOST** |
| **OSK in chondrocytes** (F-R069) | **DNMTs down, TET2 up** — i.e. **drives DEmethylation**, TET2 confirmed pivotal by siRNA |

> ### If growth-plate senescence **is** loss of DNA methylation, then an intervention whose demonstrated mechanism is **removing** methylation is pushing in the same direction as senescence, not against it.

**The reconciliation that may save it, stated as a possibility rather than an answer.** Ageing is
conventionally **global hypomethylation plus focal hypermethylation at CpG islands and PRC2 targets**. The
2005 paper measured **global** methylation with 2005 methods; the Horvath/Petkovich clocks and the PRC2
convergence result (F-R070) are **site-specific** and driven largely by focal **gains**. **Both can be true
at once, and OSK could be correcting the focal component while the global component moves independently.**

**But that is a hypothesis, and the measurement that would settle it does not exist.** Nobody has run a
site-specific methylation clock on growth-plate tissue. **Until that is done, the OSK route rests on an
unexamined assumption about which methylation compartment matters.**

**And there is a cleaner reading available that F-R070 already supports:** if the relevant lesion is at
**bivalent/PRC2-target promoters** (where Lui's H3K4me3 loss occurs and where partial reprogramming
demonstrably acts), then the global hypomethylation Nilsson measured may be a **correlate rather than the
mechanism**. **The H3K4me3 evidence is more specific than the global methylation evidence, and it points
the right way.** I am flagging the tension rather than resolving it, because it is not resolvable from what
is published.

---

## 4. Delivery — exhausted, and the gap is confirmed and sharpened

**AAV does reach the growth plate — but only by the route that does not help us.**

**AAV8-CNP works:** AAV8 vectors expressing **C-type natriuretic peptide** stimulate bone growth via NPR-B;
in achondroplasia mice, growth plates showed increased chondrocytes with partial normalisation and **both
proliferative and hypertrophic zone heights increased.**

> ### But CNP is a **secreted** factor. The vector transduces liver or muscle and the protein circulates to the plate. **It never has to transduce a growth-plate chondrocyte.** **OSK is a cell-autonomous transcription factor — it must be inside the target cell.** So the entire successful AAV-skeletal literature routes around exactly the problem we have.

**Confirmed by exhaustion:** every AAV-cartilage tropism study is **intra-articular and articular**
(AAV2 best in arthritic chondrocytes; AAV2/5/6/6.2 substantial; AAV6 aggravates degeneration; AAV7/8/9
strongly transduce liver even after intra-articular injection). **No serotype has been characterised for
direct transduction of growth-plate resting-zone chondrocytes**, and the resting zone sits behind the
secondary ossification centre, fed by epiphyseal vessels rather than exposed to the joint space.

---

## 5. Where the programme stands

| line | status |
|---|---|
| never close | **solved in humans** — ESR1-null / aromatase-null, epiphyses open at 28–31 |
| fast | **solved** — Mauras +22.5 vs +13.0; TYRA-300 wild-type +8.2% femur; KY19382 both zones |
| the cells are intrinsically capable | **PROVEN** — donor age does not affect population doublings in culture |
| the limit is epigenetic and in vivo | **Baron's own stated hypothesis** |
| cost per division is modulable | **PROVEN in the favourable direction** — oestrogen raises it; removing oestrogen lowers it |
| banking is real | **measured at cell-count level** — dexamethasone slowed RZ depletion |
| the clock is reversible in cartilage | **measured**, but on a methylation compartment whose relevance to the plate is **unverified** |
| OSK reaches the resting zone | **no — no serotype characterised, and the working skeletal AAV route uses secreted factors** |
| reversal extends longitudinal growth | **never attempted** |

**The single most important upgrade this round:** *the cells are not the problem.* Everything that limits
growth is imposed on capable cells by a reversible-in-principle in vivo state, **and one of its terms — the
per-division cost — is already known to be lowered by an agent in the stack.**

---

## 6. What I would still want, and it is now two specific documents

Both are closed at the publisher (Bioscientifica, 403; no PMC, no repository copy — verified). **I have the
full abstracts; the figures and methods are what would matter.**

1. **Nilsson O et al., *J Endocrinol* 2005;186(1):241–9 (PMID 16002553)** — specifically **which methylation
   assay** was used (global vs site-specific) and **the magnitude and time course** of the methylation loss
   by zone. This decides §3: if it is a global assay, the tension with OSK largely dissolves; if it is
   site-specific and shows loss at CpG islands, the OSK route has a real problem.
2. **Schrier L et al., *J Endocrinol* 2006;189(1):27–36 (PMID 16614378)** — the **age-by-age resting-zone
   cell counts**, and the **oestradiol arm's numbers**. The per-cycle cost argument in §2 is the most
   valuable inference in this round and it currently rests on one sentence of a discussion.

*Everything else I asked for in F-R070 is now resolved by search: the cyclic-versus-constitutive question
(continuous OSKM kills in ~4 days; cyclic 2-on/5-off ran 35 weeks safely at single copy, but 8 cycles at
two copies caused teratomas in liver, kidney and pancreas — and cyclic OSKM does drive proliferation of
beta cells and satellite cells, so it works in dividing compartments), the clock reagents (Petkovich
PMC5578459, Stubbs PMC5389178, both open), and the AAV landscape.*
