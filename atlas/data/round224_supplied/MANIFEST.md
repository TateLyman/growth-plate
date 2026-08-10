# Round 224 — the bone-age hunt

| file | source | ref_id |
|---|---|---|
| `demuynck2024_jbmr_zjae051.txt` | Demuynck B, Flipo J, Kaci N, Dambkowski C, Paull M, Muslimova E, Shah BP, Legeai-Mallet L. "Low-dose infigratinib increases bone growth and corrects growth plate abnormalities in an achondroplasia mouse model." *J Bone Miner Res* 2024, doi 10.1093/jbmr/zjae051 | `demuynck2024` |

## What it settled

- **L4-L6 lumbar segment +18.4 %** at infigratinib 0.5 mg/kg/day (vs 4.5 % at 0.2 mg/kg/day, 6.4 % at
  1 mg/kg every 3 days) — the largest axial number in the FGFR file. IVD area and outer annulus fibrosus
  area also improved at 0.5 mg/kg/day.
- **Hypertrophic cells SWELL** — "quantitative measurements of the hypertrophy area of the growth plate
  (mm²) showing a significant swelling of hypertrophic cells exclusively for daily infigratinib 0.5 and
  1 mg/kg every 3 days." Plus enlargement of the secondary ossification centre and a larger Col X area.
- **This corrects round 223's unverified note** that the paper showed *fewer* hypertrophic cells. Cell
  number is **not reported at all**. And the measure is an **area**, which CORR-190 forbids reading as a
  length — the decomposition is still not closed.

## The bone ages, found by search rather than supplied

The assignment was to find bone ages for the FGFR arm. Both sources were already in the bibliography:

- **`erdaseries2025`** (correctly **Raimann A** et al., *Horm Res Paediatr* 2024;98(6):753–757 — see
  CORR-227) — serial **wrist imaging**: *"atypical physeal widening without apparent progression of bone
  maturation"*, profound metaphyseal sclerosis at onset, **normalisation of bone mineralisation after
  treatment halt**. No numeric bone ages.
- **`erdachild2024`** — bone age **14.0 at chronological age 16.2**, >2 SD below mean, **no baseline**, so
  no rate.

**And the confound:** all three children were sex-steroid deficient (hypogonadotropic hypogonadism with
undetectable testosterone; prepubertal Tanner 1 with oestradiol <5 pg/mL; pre-pubescent with pre-pubertal
testosterone). Sex steroids drive skeletal maturation — so absent bone-age progression is what their
endocrine state predicts on its own.

## Corrections this round produced

- **CORR-226** — round 217's human curve splices patient 1's dose with patient 2's velocity; the upper
  anchor was already unassignable under CORR-062. The human exponent is **unidentifiable**, not merely
  artefactual.
- **CORR-227** — `erdaseries2025` first author is **Raimann A**, not Hartmann G. Second wrong-first-author
  defect after CORR-216, and the back-catalogue sweep that rule implied was never run.
- **CORR-228** — round 223 graded X an absence claim refuted by a paper cited in its own `key_refs`.
