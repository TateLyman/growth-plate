# F-R056 — The brake has a pocket, and the animal that settles the oestrogen question already exists

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** Five PDB structures downloaded and analysed directly from coordinates, plus eight papers.
**HHIP holds the SHH zinc with a single aspartate, HHIP and PTCH1 compete for the same two SHH surfaces —
so the brake cannot be blocked at the ligand — and the HHIP-N CRD is a sterol-binding pocket of a
superfamily defined by small-molecule binding.** And separately: **a CYP19A1-null rabbit line exists, is
viable to adulthood, and nobody has ever looked at its growth plates.**

---

## 1. The animal that settles the oestrogen question is already alive

F-R053 and F-R055 both asked for *"any long-term complete oestrogen ablation in a species whose growth
plates actually fuse."* It exists.

**Jolivet G, … Pailhoux E, Pannetier M, Endocrinology 2022;163(1):bqab210** — *"Fetal Estrogens Are Not
Involved in Sex Determination But Critical for Early Ovarian Differentiation in Rabbits"*:

> *"we produced **3 lines of TALEN genetically edited CYP19A1 knockout (KO) rabbits that were devoid of any
> estradiol production**."*

And the companion paper (**Dewaele A et al., Genes 2022;13:2070**) characterises **CRISPR/Cas9 CYP19A1⁻/⁻
males** — decreased fertility, hypo-spermatogenesis, reduced sperm motility. Both papers report the animals
are **viable into adulthood**; heterozygotes showed *"no metabolic or postural diseases until they were at
least 2 years old."*

**The rabbit is the species Weise, Gafni and Nilsson used. It fuses. And Weise's own vehicle group —
ovariectomised, E2 below 5 pg/ml — still fused the distal tibia at 2–6 weeks, which is the single result
that most threatens "never close."**

> ### A rabbit with zero oestradiol from conception, viable for years, is the exact experiment that decides whether oestrogen ablation prevents fusion or merely postpones it. The animals exist. Both papers are reproductive; neither reports a single skeletal measurement. I searched for a published skeletal phenotype of this line and found none.
>
> **Long-bone radiographs and growth-plate histology on animals that already exist would settle the
> question. No new model has to be made.**

Both papers even note that CYP19A1 has *"physiologically significant expression… in bones"* — and then
study the gonad.

---

## 2. The HHIP–SHH interaction, computed from the coordinates

I downloaded **3HO5, 7PGK, 7PGL, 7PGM and 7PGN** and analysed them directly rather than relying on the
papers' descriptions.

**3HO5 (HHIP–SHH, 3.01 Å):** chain H is SHH (residues 38–191); chains A and B are HHIP (residues 214–670).

**The interface is small — 21 SHH residues and 15 HHIP residues within 4.0 Å:**

| | residues |
|---|---|
| **SHH side** | Ala43, Tyr44, Lys87, Glu89, Arg123, Thr125, Glu126, His133, **His134**, Ser135, Glu136, **His140**, **Asp147**, Arg153, Arg155, Glu176, Ser177, Lys178, Ala179, His180, **His182** |
| **HHIP side** | Ala311, Ile312, Gly313, Pro314, Leu376, Asp377, Met379, Glu380, Glu381, Met382, **Asp383**, Gly384, Asp387, Thr418, Pro421 |

**The zinc coordination, measured:**

```
SHH Zn is held by:  His140 NE2  2.07 Å
                    Asp147 OD1  2.00 Å
                    His182 ND1  2.07 Å      ← SHH's own His-Asp-His triad
                    HHIP Asp383 OD2  2.17 Å ← the fourth ligand comes from HHIP
```

> ### HHIP completes the coordination sphere of the SHH zinc with a single aspartate. The entire metal-site half of this protein–protein interaction runs through Asp383.

The two SHH calcium ions sit in a separate acidic groove (Glu89, Glu90, Asp95, Thr125, Glu126, Asp129,
Asp131) — the canonical Ca-binding site.

**A one-residue, metal-mediated interface is, in the abstract, exactly what fragment-based zinc-chelator
chemistry is built for. But §3 says that route is closed.**

---

## 3. Why you cannot block HHIP by targeting SHH — and it is the paper's own conclusion

**Griffiths SC, Schwab RA, El Omari K, Bishop B, Iverson EJ, Malinauskas T, Dubey R, Qian M, Covey DF,
Gilbert RJC, Rohatgi R, Siebold C, Nat Commun 2021;12:7171:**

> *"**HHIP targets both the SHH metal-binding and lipid-modification sites recognised by PTCH1**, while
> potentially staying localized on the cell surface via HHIP-GAG interactions."*

**HHIP and PTCH1 compete for the same two surfaces on SHH.** So any molecule that occludes the SHH zinc
site or the SHH lipid site blocks PTCH1 engagement too — it would silence Hedgehog signalling, which is
the opposite of the objective. **This is confirmed independently: the 5E1 antibody binds the SHH
metal-binding site, overlapping with HHIP, and *inhibits* SHH activity in vivo.**

> **The brake must be blocked on the brake, not on the ligand. That single constraint eliminates the most
> obvious chemistry and points at exactly one place instead.**

---

## 4. The HHIP-N CRD — the actual target, and its class is defined by small-molecule binding

Griffiths' central structural finding:

- **HHIP-N has a bipartite fold: an N-terminal GAG-binding domain (GBD) plus a C-terminal Cysteine-Rich
  Domain (CRD)**, stabilised by six disulphides (C39–C78, C69–C112, C79–C115 among them)
- the CRD *"shows weak sequence homology to the **cysteine-rich domain (CRD) superfamily, typically
  involved in small molecule-binding**"*
- *"**the purified CRD binds to a mimic of the cholesteroylated HH C-terminus**"*
- *"**HHIP-N is required to convey full HHIP inhibitory function**, likely by interacting with the
  cholesterol moiety covalently linked to HH ligands, thereby **preventing this SHH-attached cholesterol
  from binding to the HH receptor PTCH1**"*

> ### The HHIP-N CRD is a sterol-binding pocket on the antagonist itself, it is necessary for full antagonism, and its structural superfamily is the one that binds small molecules. A ligand occupying that pocket disables HHIP's cholesterol capture without ever touching SHH — which is the only selectivity the objective permits.

**And the chemistry already has a starting point.** The mimic of the cholesteroylated HH C-terminus was
made by **Qian and Covey** — sterol chemists — as co-authors on this paper. **The tool compound for probing
this pocket exists.** The same CRD superfamily includes **Smoothened's own CRD, which binds cholesterol and
oxysterols**, so ligand chemistry for CRD sterol pockets is a developed field.

---

## 5. The GAG sites, mapped from the coordinates — and what they mean in cartilage

I computed the polysaccharide contacts in all three GAG-bound structures:

| structure | domain | **residues within 4.0 Å of the GAG** |
|---|---|---|
| **7PGK** (HHIP-N + sucrose octasulfate, 2.75 Å) | HHIP-N, res 36–184 | **Pro44, Pro45, Lys46, Arg47, Lys49, Arg81** |
| **7PGN** (HHIP-C + SOS, 2.40 Å) | HHIP-C, res 213–670 | **Lys277, Gly278, Gly279, Asp280, His349, Arg350, Lys351, Pro490, Arg514, His550, Lys569** |
| **7PGM** (HHIP-C + heparin, 2.70 Å) | HHIP-C | Gln273, Ile276, **Lys277**, Gly278, Gly279, Asp280, **Arg282, Arg350, Lys351, Lys569** |

**Two independent basic patches — one per domain — and 7PGM and 7PGN converge on the same HHIP-C site with
a different polysaccharide, so the site is real rather than a crystallisation artefact.**

**What Griffiths shows they do:** *"Heparin can bind to both HHIP-N and HHIP-C, thereby **inducing
clustering at the cell surface and generating a high-avidity platform for SHH sequestration and
inhibition**."* HHIP-C assembles into large HHIP–GAG oligomers.

> ### GAG binding is not incidental to HHIP. It is the avidity mechanism — how the brake is concentrated and held where it acts.

**And this lands directly on F-R036.** The growth-plate matrix is a dense polyanionic gel — that is the
finding that made cationic carriers like octaarginine and the WYRGRL conjugates work in the first place.
**A polyanionic matrix is precisely the platform these two basic patches are built to bind. The plate's own
aggrecan is plausibly what holds HHIP in place.**

**Which suggests a second intervention point, and a cruder one:** a soluble polyanion — heparin, sucrose
octasulfate itself, pentosan polysulfate — that saturates HHIP's GAG sites in solution should compete with
matrix HSPG and strip HHIP off its platform, collapsing the avidity. **This is speculative and the sign is
not established** — soluble GAG could in principle cluster HHIP rather than release it. **But it is
testable with reagents that already exist, and sucrose octasulfate is the active moiety of a marketed
drug.**

---

## 6. Two intervention points, ranked

| | target | rationale | status |
|---|---|---|---|
| **1** | **HHIP-N CRD sterol pocket** | necessary for full antagonism; binds the cholesteroylated HH C-terminus; **CRD superfamily is defined by small-molecule binding**; blocking it disables HHIP without touching SHH's PTCH1 interface | **no compound; a sterol-mimic tool exists (Qian/Covey); pocket structurally defined in 7PGL/7PGK** |
| **2** | **HHIP GAG sites** (HHIP-N K46/R47/K49/R81; HHIP-C K277/R350/K351/R514/K569) | GAG binding creates the clustering/avidity platform; the cartilage matrix is polyanionic | **reagents exist (heparin, SOS, pentosan polysulfate); direction of effect unproven** |
| **✗** | **the SHH zinc or lipid site** | **eliminated** — HHIP and PTCH1 compete for the same surfaces; 5E1 proves blocking there inhibits SHH | **closed** |

---

## 7. Flaws in all of the above

1. **§1 is an experiment that has not been done, not a result.** The rabbits exist; the skeletal phenotype
   is unknown, and it could as easily show fusion at the normal time as show non-fusion.
2. **3HO5 is 3.01 Å.** Side-chain positions at that resolution carry real uncertainty; the Asp383–Zn
   distance of 2.17 Å is consistent between the two HHIP copies (2.17 and 2.56 Å) but should not be
   over-read.
3. **The CRD sterol pocket has never been drugged**, and Griffiths demonstrate binding of a *mimic*, not a
   functional small-molecule inhibitor. *"Potential ligand-binding pocket"* is their language and it is
   the right level of confidence.
4. **The GAG-competition idea has an unknown sign** (§5) and I am not going to pretend otherwise.
5. **All the HHIP loss-of-function skeletal data is a limb-lineage congenital deletion** (F-R055). Nobody
   has removed the brake from an adult plate — still the crux.
6. **Chronic Hedgehog elevation is oncogenic.** The eLife 2019 paper in this bundle shows Hh activation in
   mesenchymal stem cells causes cartilage and bone tumours via Wnt/β-catenin; HHIP itself is a tumour
   suppressor in several tissues. A brake-removal strategy inherits all of that.
7. **HHIP's essential lung role** makes systemic blockade doubtful; the demonstrated skeletal benefit came
   from a limb-restricted deletion, so a cartilage-targeted delivery route (F-R053 §4b) is not optional
   here — it is the only version that could work.

---

## 8. What I want next

**Tier 1:**

1. **Long-bone radiographs and growth-plate histology from the CYP19A1⁻/⁻ rabbits** — Pannetier and
   Pailhoux, INRAE BREED, Jouy-en-Josas. **The animals exist and the measurement has never been made.**
   Failing tissue: any published photograph, radiograph or body-length measurement of an adult
   CYP19A1⁻/⁻ rabbit, from any of their papers or theses.

2. **Haraguchi 2025 Figures 6b, 6d, 6i** — the femur-length values at 10 and 53 weeks and the Toluidine
   blue area. Still outstanding from F-R055 and still the effect size of the best-shaped arm.

3. **Any inducible or adult-onset Hhip1, Ptch1 or Ptch2 deletion in cartilage with bone length as an
   endpoint.** The crux, unchanged.

4. ***"Resveratrol Treatment Delays Growth Plate Fusion and Improves Bone Growth in Female Rabbits"***
   (PMC3695926). I found this while searching §1. **A fusion-delaying intervention in the species that
   fuses, with fusion as the endpoint, is directly on the objective and I have not read it.**

**Tier 2:**

5. **Any screening campaign, fragment screen or compound series against the HHIP-N CRD**, or against any
   CRD sterol pocket outside Smoothened.
6. **Whether HHIP expression in the human growth plate changes across pubertal stage** — carried forward
   from F-R055 §8, and §4–5 make it more important: if HHIP rises while Ihh falls (Kindblom), the brake
   and the accelerator move in opposite directions during closure and that is the mechanism of fusion.
7. **Any experiment adding soluble heparin, sucrose octasulfate or pentosan polysulfate to a growth plate
   or a Hedgehog-responsive assay**, to settle the sign in §5.
