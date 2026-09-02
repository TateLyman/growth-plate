#!/usr/bin/env python3
"""
R406 - THE COMPARTMENT QUESTION FOR THE TWO SUPPLY CANDIDATES, DONE R323's WAY.

R318 placed the SCUBE3 height allele at about 104 percent LEG and recorded it as a real
cost, because the residual at bone age 16 is trunk-dominant. R323 then showed that R318's
whole method was compromised: it selected variants from the sitting-height-RATIO scan,
which is selection ON THE OUTCOME and guarantees extreme compartment values. The fix is to
take each gene's STANDING-HEIGHT lead variant instead, then read the same SNP out of the
sitting-height and leg-length scans and see where the height actually goes.

R323 ran that correction on 22 genes. SCUBE3 was not among them, and CLEC11A had never
been asked at all. This runs it for both, on regions streamed from the GWAS Catalog
harmonised summary statistics for the three ABSOLUTE traits in one cohort of 451,921:

  GCST90728584  standing height   (inverse-normalised)
  GCST90728586  sitting height    (inverse-normalised)
  GCST90728587  leg length        (inverse-normalised)

Every effect is aligned to the HEIGHT-INCREASING allele, so a positive sitting-height beta
means the allele puts height into the trunk. Units are inverse-normalised SD, NOT
centimetres, and a compartment coordinate is a ranking criterion, not a predicted effect.
"""
import os, sys

SP = ('/tmp/claude-0/-home-user-growth-plate/'
      'ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad')
FILES = {'std': 'GCST90728584', 'sit': 'GCST90728586', 'leg': 'GCST90728587'}


def load(acc):
    """gene -> {variant_id: (chrom, pos, ea, oa, beta, se, p)}"""
    out = {}
    path = os.path.join(SP, acc + '.region.tsv')
    with open(path) as fh:
        for line in fh:
            f = line.rstrip('\n').split('\t')
            if len(f) < 10:
                continue
            gene, chrom, pos, ea, oa, beta, se, eaf, p, vid = f[:10]
            try:
                beta, se, p = float(beta), float(se), float(p)
            except ValueError:
                continue
            out.setdefault(gene, {})[vid] = (chrom, int(pos), ea, oa, beta, se, p)
    return out


tables = {k: load(v) for k, v in FILES.items()}

print('=' * 96)
print('R406  COMPARTMENT OF THE TWO SUPPLY CANDIDATES, ON STANDING-HEIGHT LEAD VARIANTS')
print('      GWAS Catalog harmonised sumstats, 451,921 Europeans, three absolute traits')
print('=' * 96)

for gene in sorted(tables['std']):
    std = tables['std'][gene]
    # the region's standing-height lead
    lead_id, lead = min(std.items(), key=lambda kv: kv[1][6])
    chrom, pos, ea, oa, b_std, se_std, p_std = lead

    # align to the HEIGHT-INCREASING allele
    flip = -1.0 if b_std < 0 else 1.0
    inc_allele = oa if b_std < 0 else ea

    row = {'std': (b_std * flip, se_std, p_std)}
    ok = True
    for trait in ('sit', 'leg'):
        rec = tables[trait].get(gene, {}).get(lead_id)
        if rec is None:
            ok = False
            break
        c2, p2, ea2, oa2, b2, se2, pv2 = rec
        # harmonised files share allele orientation; assert it rather than assume
        if (ea2, oa2) != (ea, oa):
            print(f'  !! {gene}: allele orientation differs for {lead_id} '
                  f'({ea}/{oa} vs {ea2}/{oa2}) - skipped')
            ok = False
            break
        row[trait] = (b2 * flip, se2, pv2)
    if not ok:
        continue

    sit, leg = row['sit'][0], row['leg'][0]
    total = sit + leg
    pct_trunk = 100.0 * sit / total if total else float('nan')

    print(f'\n{gene}   chr{chrom}:{pos}  lead {lead_id}')
    print(f'  height-increasing allele: {inc_allele}')
    print(f"  {'trait':<18}{'beta (aligned)':>16}{'se':>12}{'P':>12}")
    for t, label in (('std', 'standing height'), ('sit', 'SITTING height'),
                     ('leg', 'leg length')):
        b, se, p = row[t]
        print(f'  {label:<18}{b:>16.6f}{se:>12.6f}{p:>12.2e}')
    verdict = ('TRUNK-dominant' if pct_trunk >= 60 else
               'LIMB-dominant' if pct_trunk <= 40 else 'BOTH')
    print(f'  --> {pct_trunk:.1f}% of the height gain is TRUNK   [{verdict}]')

print("""
================================================================================================
READING RULES
  · These are COMMON-VARIANT lead-allele effects in inverse-normalised SD, not centimetres,
    and not the coding-burden effects (SCUBE3 -6.71 cm, CLEC11A -0.74 cm) that put these two
    genes on the list. A regulatory lead variant and a loss-of-function allele need not
    allocate height the same way.
  · The window is +/-150 kb, so the lead is the region's, not necessarily the gene's.
  · A compartment coordinate is a RANKING criterion for additions, not a predicted effect,
    and R327's exception applies: it only selects against a lever that is window-bounded.
""")
