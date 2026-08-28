# F-R038 — The metabolic lever is real, and it points the opposite way from what I proposed

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** All three requested documents read. Flaw two is **refined and made fairer**; flaw one is now
**explained mechanistically**, and the explanation hands back a lever — **with its sign reversed.**

---

## 1. `trompet2024` supplement — flaw two is real but I overstated it

The supplement (JCI Insight 165226, Supplemental Data 2) settles §2 of F-R037, and it corrects me in one
direction and confirms me in another.

**Supplementary Figure 2 is titled, by the authors:** *"**Intraperitoneal injections of SAG do not alter
the number or proliferation of CD73⁺ cells.**"* So the CD73 negative is not my inference — it is their
stated result.

**But it is underpowered, and I should have said so.** The legend gives the numbers:

> *"#P<0.1 indicates a tendency toward significance (**Supplementary Figure 2I power 0.1648, effect size
> 0.84**, and **Supplementary Figure 2K power 0.3323, effect size 1.62**)"*

**Power of 0.16 means an 84% chance of missing a real effect.** n = 3/5 and 3/3. So the CD73 result is
**uninformative, not a demonstrated null** — I called it "unchanged or suppressed" and it is better
described as *not measurable at this n*. The fair statement is symmetrical: **neither the claim that SAG
expands the stem pool nor the claim that it does not is supported at the power these experiments ran.**

**Supplementary Figure 5 is the decisive panel, and it does confirm the substance of flaw two.** Femur,
bead implantation, paired t-test:

| panel | endpoint | 1 week | **1 month** | 2 months |
|---|---|---|---|---|
| **E** | growth plate height | ns | **✱✱** (~280 → ~340 µm) | **ns** |
| **F** | **terminal hypertrophic cell height** | ns | **✱** (~27 → ~32 µm) | **ns** |
| **G** | Ki67⁺ in proliferative zone | **ns** (28% vs 25%) | — | — |
| **I** | MEF2C signal | ns | ns / ✱✱ | ns |
| **D** | OARSI joint score at 6 months | **ns** — no joint damage | | |

> **The entire significant mechanistic signal from a SAG bead is two panels at one timepoint: plate
> height and terminal hypertrophic cell height at one month. Both are back to non-significant at two
> months. Proliferative-zone proliferation never moves.**

And Supplementary Figure 4 adds the same for the other route: *"**Intra-articular injections of SAG do
not affect the proliferation.**"*

**So the corrected version of flaw two:** `trompet2024` demonstrates a durable length gain from a
transient local Hedgehog pulse — that part is solid, contralateral-controlled, out to six months, with
no joint damage. **The only significant mechanism it can point to is h_term**, transiently. The pool
claim rests on one marker (PTHrP⁺, +61%) with a second marker measured at power 0.16. **My "raise N"
architecture still has no experimental support — but the reason is missing evidence, not contrary
evidence.**

**One thing in the supplement is quietly encouraging.** h_term sits **outside the pool equation
entirely** — it multiplies output and appears nowhere in `dn/dt`. If SAG's length gain really is h_term,
then SAG is a lever that buys length **without spending reserve**, which is what the conjugacy identity
says is the only free direction. Its limit is that h_term saturates (R202; Wilsman's 1.3–1.75× range;
Marchini found selection did not move it at all, P = 0.775).

---

## 2. `horike2026` read — a clean negative that closes a candidate

*"Excess FGFR3 signaling in achondroplasia disrupts turnover of resting zone chondrocytes via CREB
signaling"*, **Nat Commun 2026;17:1856**. It is the control case for flaw one, and it is unambiguous:

> *"we observe an **expansion of the resting zone**. EdU labeling and lineage tracing analyses indicate
> that **disruption of turnover and impairment of stem cell-like behavior** of resting zone chondrocytes
> results in **accumulation of cells in the resting zone**."*

**Expanded resting zone caused by blocked exit, in the archetypal dwarfism.** That is flaw one's
mechanism, demonstrated by lineage tracing rather than inferred.

**And the restoration-versus-elevation question is answered outright:**

> *"administration of 666-15 **significantly changed neither weight, femur length, nor expression of CD73
> in the resting zone in control mice** (Supplementary Fig. 16a–c), suggesting that the 666-15 at a dose
> of 10 mg/kg is **not effective in a physiological condition**."*

**CREB inhibition does nothing to a normal mouse.** The atlas ranked CREB inhibition third among
pool-directed levers and flagged the restoration trap (CORR-203) as unresolved. **It is now resolved, and
negatively.** The FGFR3→CREB axis is a repair mechanism for achondroplasia, not an elevation lever for a
normal plate. One candidate removed from the list on primary evidence.

**Two things worth keeping from it.** First, the compartment map: *"Vosoritide targets MAPK/ERK pathway
in proliferative zone and hypertrophic zone chondrocytes, while 666-15 targets CREB pathway in resting
zone chondrocytes"* — and the authors suggest that vosoritide's failure to fully correct bone length *"may
be that it does not target CREB signaling in resting zone chondrocytes."* Second, and directly relevant
to F-R036's transport work: *"**Cystine-dense peptides (CDPs) and octaarginine preferentially accumulate
in cartilage** and can be used as carriers for the selective delivery of drugs to cartilage."*
**Octaarginine is cationic** — which is exactly what Williams's charge hypothesis predicts should
partition into a polyanionic matrix. A cartilage-targeting carrier chemistry exists, and its charge sign
matches the transport physics.

---

## 3. `bailey2007` read — and it explains flaw one through glucose, not oxygen

The human primary behind F-R037 §1(d): 113 Han and Tibetan children at 3100 m, aged 8–11.

> *"**Independent of ethnicity or caloric status, absolute and relative tibia length was significantly
> reduced in children with lower blood oxygen saturation.**"*
> *"**In hypoxemia, body fat has less impact on growth than when ample oxygen is present.**"*

And the model they set out to test is the one that matters:

> *"tradeoff models of oxygen and glucose metabolism predict that **in hypoxemia, glucose metabolism will
> be downregulated**."*

**Put that beside `Kobayashi 2023` and the chain closes:**

```
systemic hypoxaemia
   → glucose metabolism downregulated              (Bailey, tradeoff model; human)
   → reduced glycolytic flux
   → reduced citrate → reduced acetyl-CoA          (Kobayashi; Acly cKO reproduces it)
   → reduced histone acetylation
   → epigenetic UPREGULATION of FGFR3              (Kobayashi; shared by Ldha and Acly cKO)
   → disrupted resting-zone turnover, cells accumulate   (horike2026; lineage tracing)
   → expanded resting zone, SHORT bones            (all three, plus altitude tibiae)
```

**Human epidemiology, mouse metabolic genetics and mouse FGFR3 genetics converge on one pathway, and it
runs through glucose — not oxygen.** Brighton established in 1971 that the plate barely consumes oxygen
and is *"predominantly glycolytic in character."* The metabolic input that matters is therefore
**glycolytic flux**, and oxygen enters only as something that gates it.

**That is why my F-R034 §7 lever pointed the wrong way.** I proposed lowering pO₂ to expand the reserve.
The chain says lowering oxygen availability **suppresses glycolysis**, starves acetyl-CoA, de-represses
FGFR3, and jams the reserve — producing exactly the dysplasia phenotype. **The lever was real. Its sign
was inverted.**

---

## 4. The lever, stated with its correct sign — and its honest caveat

> **Raise glycolytic flux / acetyl-CoA availability in the growth plate → more histone acetylation →
> FGFR3 down → resting-zone turnover restored → longer bone.**

It is transport-compatible, which nothing else in this programme has been: **acetate is 59 Da**, far
inside the ≤10 kDa gate and the small-molecule band that Williams showed equilibrates the plate in
90 seconds. Kobayashi names the route themselves — *"Ac-CoA is generated from… **dietary acetate via
Acetyl-CoA synthases**"* — and shows it is functional in these cells: *"**Acss2-mediated Ac-CoA synthesis
from acetate compensates** for the reduced Ac-CoA synthesis from citrate in these mutant chondrocytes…
reasonably well but less so for histone acetylation."*

It also unifies observations that were sitting apart: local warming and exercise raise **delivery** of
glucose as well as everything else and lengthen limbs; an A-V fistula raises perfusion and lengthens;
altitude lowers it and shortens the tibia specifically.

**And here is the caveat, which is the same trap that just killed CREB.** `Kobayashi 2023` tested **only
loss of function** — Ldha cKO, Ldhb, Acly cKO, miR-140 GOF, Fgfr3 activation. I searched its full text:
**zero occurrences of "rescue", "restored", "supplementation", "HDAC", or any gain-of-glycolysis
experiment.** Nobody has raised acetyl-CoA, or glycolytic flux, or histone acetylation in a normal growth
plate and measured bone length.

> **So this is a mechanism with five converging lines of support for its direction and no test of its
> gain arm — precisely the position CREB inhibition occupied until `horike2026` tested it in wild-type
> mice and it did nothing.** I am recording it as the best-supported open candidate and explicitly not
> as an answer.

---

## 5. Where the three terms stand after this round

| term | status |
|---|---|
| **never close** | **solid**, unchanged |
| **unlimited** | still no demonstrated pool-expanding-with-output lever. But flaw one now has a *mechanism*, which means the failure mode is diagnosable rather than mysterious: expansion-by-blocked-exit runs through acetyl-CoA→FGFR3, and can be told apart from expansion-with-turnover by an EdU/lineage turnover assay |
| **fast** | `trompet2024`'s length gain is real and durable; its only significant mechanism is **h_term**, which is the one term outside the pool equation. **CREB inhibition is eliminated.** The metabolic/acetyl-CoA route is the leading untested candidate |

**The central gap is unchanged and now better specified:** no intervention has been shown to raise the
stem pool while maintaining output — **and the discriminating assay now exists**, because horike2026
demonstrates how to distinguish accumulation from healthy expansion (EdU turnover + lineage tracing,
not zone height).

---

## 6. Unknowns, updated

**Closed this round:**
- ~~Is CREB inhibition an elevation lever?~~ **No** — no effect on weight, femur length or CD73 in
  control mice.
- ~~What does the Trompet supplement show?~~ **h_term at one month, and CD73 measured at power 0.16.**
- ~~Does hypoxia's human negative hold up?~~ **Yes, and Bailey supplies the glucose mechanism.**

**Open, ranked:**
1. **Does raising glycolytic flux / acetyl-CoA in a normal plate lengthen bone?** The gain arm of §4.
   Completely untested. **Now the single highest-value experiment in the programme**, because it is the
   only candidate whose direction is supported by five independent lines and whose agent class clears
   the transport gate.
2. **Does any intervention raise stem number while maintaining turnover?** Unchanged, but now with a
   validated assay design (horike2026's EdU + lineage tracing).
3. **Does a Hedgehog-expanded pool persist past one week; does a second pulse compound?** Unchanged.
4. **Human interstitial flow velocity / any human transport measurement.** Unchanged — none exists.
5. **Is h_term's ceiling reachable pharmacologically?** SAG moved it ✱ at one month; Marchini's selection
   did not move it at all. Whether it is a usable lever or a saturating one is undetermined.

**What I would ask for next:** nothing is blocking. The three things I need are experiments, not papers.
If anything, `Kobayashi 2023`'s Source Data (GEO **GSE192971** and **GSE98309**, both public) would let
me check whether FGFR3 target genes move with acetylation in the direction the chain predicts — and I can
pull those myself.
