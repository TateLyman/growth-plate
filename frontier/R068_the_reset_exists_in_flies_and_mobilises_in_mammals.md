# F-R068 — The reset exists in flies, and the mammalian analogue mobilises instead of resetting

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** Theoretical analysis. Nine documents read including the Nature peer-review file, the CXXC5
peer-review file, a completed Phase 1 record, and a patent.

**Four results, and one of them requires me to downgrade F-R067.**

1. **The reset is real and named** — in *Drosophila*: a **retrograde Delta→Notch signal from the
   differentiated daughter back to the stem cell resets the chromatin division counter.**
2. **F-R067 overstated the counter.** A *Nature* reviewer argued the division-counter interpretation may be
   **fatally flawed**. I presented it as established; it is contested.
3. **The mammalian structural analogue exists and is Hedgehog, not Notch** — and **it mobilises the pool
   rather than resetting it.** That is a genuine negative and it retroactively explains three prior
   failures.
4. **The CXXC5 arm survives with a mechanistic caveat from its own peer review, and its drug class has
   cleared a Phase 1 in humans.**

---

## 1. The reset, specified

From the *Nature* rebuttal file, the revised Results section is titled **"Transient Notch activation
maintains 8 divisions of epigenetic memory."**

> *"Adult ISCs engage in **bidirectional Notch signaling**: they send Delta to EBs to promote EC
> differentiation, **or they receive Delta from EMCs/EEPs to maintain stemness and reset the division
> counter**."*

**And it is confirmed by loss of function**, added during revision: knocking down Delta specifically in the
differentiated daughters (prosV1-Gal4 > Dl RNAi) produced *"clusters of Pros⁺ EECs and showed a
**significant reduction in Dl⁺ ISC numbers**"* — i.e. removing the retrograde signal **drained the stem
pool**.

> ### This is the only demonstrated mechanism by which any cell un-counts its divisions: **the differentiated daughter signals back to its parent and clears the parent's epigenetic memory.** Renewal capacity is not intrinsic to the stem cell — it is **conferred by its own progeny.**

---

## 2. Correction — F-R067 leaned on a contested claim

F-R067 stated flatly that self-renewal advances the counter and does not reset it, treating the ISC paper
as settled. **The peer-review file shows a reviewer was not convinced, on a substantive methodological
ground I should have anticipated:**

> *"the assumption that the size and composition of each clone is determined **only** by the mitosis of a
> **single** ISC is just wrong. Intestinal stem cells from flies to humans undergo **neutral competition**,
> whereby they may divide asymmetrically, differentiate symmetrically or self-renew symmetrically…
> **I have only found one way out of thinking that this is not a fatal flaw**."*

The reviewer notes symmetric division occurs ~20% of the time, and that clones were pooled across 3–15
days without time as a variable.

**What survives, and what I should have said:**

| claim | status |
|---|---|
| TrxG active marks (H3K4me3, H3K36me3) decline and PcG marks accumulate across successive divisions | **well supported** |
| Transient Notch resets the epigenetic state | **supported, with loss-of-function** |
| Cells count *precisely eight* divisions | **contested** — lineage-history confound |
| This is a senescence clock | **not claimed by the authors** — it is a fate-ratio cycle **with a reset**, in an invertebrate |

**Lui 2010 remains the better evidence for our case and it stands on its own:** H3K4me3 declining
monotonically with age at 11 growth-promoting promoters, across three mammalian organs, **paced by growth
rather than age.** The fly paper is corroborating architecture, not the mammalian proof. **F-R067's
conservation law is downgraded from "measured" to "strongly indicated."**

---

## 3. The mammalian analogue is Hedgehog — and it spends the pool

**The architecture transfers.** The mammalian growth plate has exactly the same retrograde topology:

> *"**Ihh functions as a reverse signal from terminally differentiated chondrocytes** in the prehypertrophic
> zone… while **increasing PTHrP expression in the resting zone**."*

Differentiated daughter → signals back → maintains the stem compartment. **Same shape as Delta→Notch.**

**But when it is tested experimentally, it does not reset. It mobilises.**

**Hedgehog activation confined to PTHrP⁺ resting-zone chondrocytes** (Ptch1 deletion, *Pthrp-creER*;
[PMC10906233](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10906233/)):

| observation | |
|---|---|
| **"patched roses"** | concentric, clonally expanded PTHrP⁺ populations in the resting zone |
| columns | **significantly wider**, **growth-plate hyperplasia** |
| proliferation | quiescent RZ cells became **highly proliferative, in equal proportion to the proliferating zone** |
| **fate** | *"drives resting zone chondrocytes into **transit-amplifying states**… and eventually **converts these cells into osteoblasts**"* — descendants **migrate away from the growth plate** |
| compartment specificity | **Col2a1-creER did NOT produce patched roses** — *"Hedgehog activation needs to be specifically confined to the resting zone"* |

> ### Hedgehog activation in the niche expands the clone and then **exports it**. The cells leave the plate and become trabecular bone. **That is pool spending dressed as pool expansion**, and it is the mammalian answer to whether the retrograde signal resets: **it does not.**

**This retroactively explains three things the branch had filed separately:**

1. **Why systemic SAG did nothing in wild-type** (F-R053/R054) — systemic Hedgehog is not RZ-confined, and
   the paper shows non-confined activation produces no clonal expansion at all.
2. **Why Haraguchi's *Hhip1* cKO gave only +4.5% over 53 weeks** — amplitude bought by drawing down the
   pool, which is why the gain accrues slowly and the plate-area decline stayed parallel (F-R057).
3. **The KY19382 niche-drain risk I flagged in F-R067** now has a named precedent: Wnt/Hh activation in the
   resting zone pushes stem cells into transit-amplifying fates and out of the niche.

---

## 4. The CXXC5 arm — what its own peer review says, and where the class is

**The mechanistic caveat, from the referees:** reviewer 3 was *"not convinced"* that KY19382's action runs
through the **CXXC5–DVL** interaction as opposed to its **GSK3β** inhibition. Since GSK3β inhibition alone
activates Wnt, **the CXXC5-specific attribution is weaker than the paper presents.** The remaining
criticisms were presentational — figure layer identification, scatter plots over bar graphs.

**This does not touch the in vivo result** — tibiae were longer, both zones expanded, TRAP⁺ resorption rose
— but it matters for compound selection: **a cleaner CXXC5–DVL binder without GSK3β activity would be the
better tool, and F-R067 asked for exactly that.**

**Where the class is in humans:** **CKR-051** (CK Regeon) completed **NCT05833906** — Phase 1, **52 healthy
male subjects**, single and multiple ascending dose, **completed January 2024**. **But it is transdermal**,
and the primary endpoints are skin-irritation scores. **This is the dermatological indication** (the same
CXXC5–DVL chemistry was developed for hair loss and wound healing). **So the class has human safety data
and no systemic skeletal programme.**

---

## 4b. The mammalian reset exists after all — and it has been done in chondrocytes

I named partial reprogramming as the lead in §6 and then found it rather than asking. **It exists, it is in
cartilage, and it has human-cell data.**

**"Local delivery of OSK factors enables partial cellular reprogramming to mitigate osteoarthritis and
cartilage fibrosis," *Exp Mol Med* ([PMID 41786976](https://pubmed.ncbi.nlm.nih.gov/41786976/)).**

Partial reprogramming with **OCT4/SOX2/KLF4 (OSK)** is the one intervention class known to **reset the
epigenetic clock in a mammal** — *"reverses DNA damage, upregulates DNA repair pathways, and resets the
epigenetic clock."* Applied to chondrocytes by **AAV**:

| finding | why it matters here |
|---|---|
| *"Chondrocytes expressing OSK **retained chondrocyte-specific markers with no increase in stemness-associated genes**"* | partial, not dedifferentiation — identity preserved |
| *"**counteracted the upregulation of osteogenic genes** during OG differentiation"* | **directly opposes the chondrocyte-to-osteoblast export** that §3 shows drains the pool under Hedgehog activation |
| AAV-OSK preserved chondrocyte vitality under inflammation; improved cartilage integrity, reduced subchondral bone thickening | in vivo efficacy in a mammal |
| *"aged chondrocytes from **osteoarthritic human donors** showed a **partial reversal of gene expression and cellular physiology to a more youthful state**"* | **human chondrocytes, reversed** |
| delivery is **local, by AAV** | solves the compartment-specificity problem §3 identified — Hedgehog only worked when confined to the resting zone |

> ### This is the first candidate in the entire branch for the one thing "infinite" requires: **clearing accumulated epigenetic division memory in a mammalian chondrocyte.** It is the mechanism the fly achieves with retrograde Notch, reached by a different route, in the right tissue, with human cells.

**What it is not, stated plainly.** These are **articular** chondrocytes in an **osteoarthritis** model, not
growth-plate chondrocytes. **No one has shown extended longitudinal growth, or applied OSK to a physis.**
The effect on the **H3K4me3 growth-gene set specifically** (Lui's 11 promoters) is unmeasured. And
intra-articular AAV is not the same delivery problem as reaching a resting zone. **The direction and the
tissue are right; the experiment is not done.**

---

## 5. The gap list — patched and unpatched

**Patched this round:**

- **How any cell un-counts divisions** → retrograde ligand from the differentiated daughter (Delta→Notch,
  fly). Named, with loss-of-function.
- **Whether the mammalian plate has that topology** → yes, Ihh→PTHrP.
- **Whether Hedgehog is the reset** → **no.** It mobilises and exports.
- **Why systemic Hedgehog agonism failed** → compartment specificity; it must be RZ-confined.
- **KY19382's mechanistic attribution** → contested between CXXC5–DVL and GSK3β.
- **Human safety for the CXXC5–DVL class** → Phase 1 complete, transdermal.

**Unpatched, and now precisely located:**

1. **A reset candidate now exists (partial reprogramming, §4b) but has never been applied to a growth
   plate.** The barrier is no longer "nothing resets an epigenetic clock in a mammal" — OSK does, in
   chondrocytes, with human-cell data. **The barrier is that nobody has pointed it at a physis and measured
   longitudinal growth.**
2. **KDM5 inhibition on skeletal growth — still untested** (standing from F-R067). This attacks the counter
   directly rather than seeking a reset, and remains the highest-value available experiment.
3. **Whether the growth-plate counter can be reset at all**, or only paused. Everything demonstrated in
   mammals is a pause: tryptophan restriction, dexamethasone banking, oestrogen removal.
4. **A CXXC5–DVL binder without GSK3β activity.**

---

## 6. What I need

1. **The OSK chondrocyte paper in full** (*Exp Mol Med*, PMID 41786976) — I have the abstract-level
   findings. I want the **AAV serotype and dose**, the **duration of OSK induction**, whether **epigenetic
   age was measured directly**, and any **growth-plate or physeal observation**.
2. **Any application of partial reprogramming to a growth plate or to longitudinal bone growth.** If it does
   not exist, it is now the defining experiment of this programme.
2. **Any KDM5 inhibitor study touching cartilage, chondrocytes or bone growth.**
3. **CK Regeon's systemic/oral programme**, if one exists — the patent WO2020079570A1 is in hand; anything
   later covering systemic administration or a skeletal indication.
4. **The *Nature* ISC paper's main text figures** — I have the peer-review file and the supplementary
   tables; the main figures showing the H3K4me3/H3K36me3 decline per division would let me judge the
   contested counter claim myself rather than relying on the referee exchange.
