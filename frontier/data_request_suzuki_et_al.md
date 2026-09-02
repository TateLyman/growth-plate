# Data request — Suzuki et al., HH methylation array

> ## ⛔ DO NOT SEND — SUPERSEDED BY F-R077 (2026-08-29)
>
> **The question this letter was written to answer has been answered on public data.** ArrayExpress
> **E-MTAB-13950** (Palumbo 2024) contains EPIC arrays on 19 girls with central precocious puberty whose
> **bone age is advanced 1.69 ± 1.00 years** and 14 age-matched pre-pubertal controls. I computed the
> Horvath 2013 and Horvath skin-&-blood clocks on it directly. **The difference was −0.016 years,
> 95% CI −0.649 to +0.616, p = 0.959**, with a positive control at p ≈ 7×10⁻⁵ — tight enough to **exclude**
> the bone-age advance rather than merely fail to find it.
>
> **A blood methylome that does not move for a 1.7-year bone-age advance in 19 children will not resolve
> delayed fusion in nine adults.** Sending this letter would be asking two researchers for their time in
> order to reproduce a negative at lower power. **The file is kept for the reasoning, not for use.**
> See `R077_i_ran_the_clock_myself_and_it_is_chronologically_paced.md`.

---

**To:** Dr Maki Fukami and Dr Keiko Matsubara
Department of Molecular Endocrinology, National Research Institute for Child Health and Development, Tokyo
*(corresponding authors; addresses on the paper)*

**Subject:** Data request — raw methylation array data, Suzuki et al., DNA methylation in hypogonadotropic hypogonadism

---

Dear Dr Fukami and Dr Matsubara,

I read your recent paper on genome-wide DNA methylation profiles in patients with hypogonadotropic
hypogonadism with great interest, and I am writing to ask about the data-availability statement, which
notes that data can be made available on request.

I am interested in a question your analysis was not designed to address. As I understand your methods, you
excluded probes known to show aging-related methylation changes (citing Horvath 2013) before the
differential-methylation analysis — which is entirely appropriate for detecting an epi-signature, since
those probes would otherwise add age-driven noise. My interest is in precisely those probes.

Specifically, I would like to compute DNA methylation age (Horvath 2013 and/or the Horvath skin-and-blood
clock) for your nine patients and twelve controls, and compare epigenetic age acceleration between the
groups. The motivating hypothesis is that the epigenetic clock in childhood may be paced by somatic growth
rather than by chronological time — a possibility raised by Lui and Baron's finding that transient growth
inhibition delays the postnatal gene-expression program, and consistent with the logarithmic age
transformation the Horvath clock requires below age 20. Hypogonadotropic hypogonadism, with its delayed or
absent pubertal growth and prolonged epiphyseal opening, is an unusually informative natural experiment
for this question, and to my knowledge no methylation-age analysis has been reported in this population.

If you were willing, what would be most useful is:

1. **The raw IDAT files**, or alternatively the β-value matrix **prior to** the exclusion of aging-related
   and sex-biased probes, for the nine patients and twelve control individuals analysed on the EPIC array.
2. **Chronological age at sampling** for each of those twenty-one individuals.
3. **Androgen (or other sex-steroid) treatment status and duration at the time of sampling**, if recorded.

Items 2 and 3 matter as much as the array data. If the patients were sampled before or early in the age
range at which fusion normally occurs, or were already receiving androgen replacement, then their skeletal
trajectory would not yet have diverged from controls and the analysis would be uninformative — so those
two facts largely determine whether this is worth either of our time. If it would be simpler, I would be
glad to receive the ages and treatment status first, and only trouble you for the array data if they look
promising.

I would of course be happy to discuss authorship or acknowledgement as you think appropriate, to share any
analysis code and results with you before any wider use, and to comply with whatever conditions your ethics
approval places on secondary use of the data. I am equally happy to work with de-identified data under any
data-transfer agreement you would prefer.

Thank you for considering this, and for making the data available in principle — it is much appreciated.

With best regards,

[name]
[affiliation, if any]
[contact]

---

## Notes for Tate (not part of the email)

- **Send it plainly as yourself.** Do not claim an institutional affiliation you do not have — it is
  unnecessary and would poison the request if it came out. Independent researchers do get data; a clear,
  specific, technically literate request is what earns it.
- **The ask is deliberately staged.** Ages and treatment status first, array data second. That is genuinely
  the right order scientifically, and it also makes the request cheap for them to answer, which makes a
  reply much more likely.
- **What the answer would mean.** If HH patients show *lower* epigenetic age acceleration than age-matched
  controls, the clock is tracking growth rather than time, and F-R066's pacing law is confirmed in the
  population that matters. If their acceleration is normal, the clock is time-paced and the pacing law is
  substantially weakened — which would be worth knowing just as much.
- **Expect the ages to be the problem.** This is a paediatric institute; the controls were "eight boys and
  four adults." If all nine patients are under ~16 the test is underpowered, because their plates would
  still be open in the normal course of events too.
