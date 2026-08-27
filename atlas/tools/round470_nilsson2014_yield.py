"""R470: compute the YIELD - output per resting-zone cell spent - from nilsson2014
Figures 2G/2H (denominator, resting zone cells per mm GP width) and Figure 3B/3C/3D
(numerator, proximal tibial growth rate and BrdU proliferation rate).

Gap g_l2_raise_the_yield_per_progenitor named this exact computation as its
discriminating step and recorded the obstacle as MECHANICAL - both figures are raster
images. Both were rendered at 760-900 dpi from the operator-supplied scan on 2026-08-27
and read off by eye.

EVERY INPUT IS value_unverified: axis-calibrated visual reads of a printed figure, not
source data. The paper reports no numeric table.

THREE STRUCTURAL CAVEATS, stated because they bound what the quotient means:
 1. Resting zone is a STANDING STOCK in cells per mm of plate width. Its fall between
    timepoints understates gross consumption, because self-renewal replaces some of what
    leaves. Every yield below is therefore an UPPER BOUND, and the ratio between arms is
    more robust than any absolute value.
 2. Units. cells/mm-of-plate-width is a linear density and growth rate is a length, so
    the quotient is not a clean per-cell figure. Only the BETWEEN-ARM RATIO in one bone
    is interpretable.
 3. NOT THE SAME ANIMALS. Growth rate came from a dedicated pinned subset followed by
    serial radiography (10 vehicle + 10 estradiol); the histology came from separate
    animals killed at 11, 16 and 21 weeks (n = 8-10 per group per timepoint). This is
    weaker than lui2018, where both terms are per-animal.
"""

# ---- Figure 2G/2H: resting zone chondrocytes per mm growth plate width, at 11/16/21 wk
RZ = {
    ('PT', 'vehicle'):   [35.3, 26.2, 17.5],
    ('PT', 'estradiol'): [35.3, 21.3, 14.3],
    ('DR', 'vehicle'):   [36.8, 28.5, 23.5],
    ('DR', 'estradiol'): [36.8, 21.3, 15.2],
}

# ---- Figure 3B: proximal tibial growth rate, mm per 2.5 weeks, plotted at interval
#      midpoints 12.25 / 14.75 / 17.25 / 19.75 wk. Only the PROXIMAL TIBIA was measured.
GR_PT = {
    'vehicle':   [4.65, 3.25, 2.30, 1.55],
    'estradiol': [4.15, 3.00, 2.05, 1.45],
}

# ---- Figure 3C/3D: proliferation, BrdU-labelled cells per column, at 11/16/21 wk
PROLIF = {
    ('PT', 'vehicle'):   [7.60, 4.30, 2.20],
    ('PT', 'estradiol'): [7.50, 2.70, 1.95],
    ('DR', 'vehicle'):   [7.20, 5.40, 1.90],
    ('DR', 'estradiol'): [7.20, 2.70, 1.35],
}

INTERVALS = [('11-16 wk (ON TREATMENT)', 0, 1, (0, 2)),
             ('16-21 wk (WASHOUT)',      1, 2, (2, 4))]

out = {'inputs_are_figure_reads': True, 'value_unverified': True, 'results': []}
print('=' * 78)
print('YIELD A -- micrometres of proximal tibial growth per resting-zone cell lost')
print('=' * 78)
for label, i0, i1, (g0, g1) in INTERVALS:
    row = {'interval': label, 'metric': 'growth_rate_per_RZ_cell_lost', 'bone': 'PT'}
    for arm in ('vehicle', 'estradiol'):
        grown_mm = sum(GR_PT[arm][g0:g1])
        rz_lost = RZ[('PT', arm)][i0] - RZ[('PT', arm)][i1]
        row[arm] = round(grown_mm * 1000.0 / rz_lost, 1)
        row[arm + '_grown_mm'] = round(grown_mm, 2)
        row[arm + '_rz_lost'] = round(rz_lost, 2)
    row['ratio_est_over_veh'] = round(row['estradiol'] / row['vehicle'], 3)
    out['results'].append(row)
    print(f"{label:26s} vehicle {row['vehicle']:7.1f}   estradiol {row['estradiol']:7.1f}"
          f"   ratio {row['ratio_est_over_veh']:.2f}")

print()
print('=' * 78)
print('YIELD B -- mean BrdU-labelled cells per column, per resting-zone cell lost')
print('=' * 78)
for bone in ('PT', 'DR'):
    for label, i0, i1, _ in INTERVALS:
        row = {'interval': label, 'metric': 'proliferation_per_RZ_cell_lost', 'bone': bone}
        for arm in ('vehicle', 'estradiol'):
            mean_prolif = (PROLIF[(bone, arm)][i0] + PROLIF[(bone, arm)][i1]) / 2.0
            rz_lost = RZ[(bone, arm)][i0] - RZ[(bone, arm)][i1]
            row[arm] = round(mean_prolif / rz_lost, 4)
        row['ratio_est_over_veh'] = round(row['estradiol'] / row['vehicle'], 3)
        out['results'].append(row)
        print(f"{bone}  {label:26s} vehicle {row['vehicle']:7.4f}   estradiol {row['estradiol']:7.4f}"
              f"   ratio {row['ratio_est_over_veh']:.2f}")

import json
json.dump(out, open('atlas/data/round470/nilsson2014_yield.json', 'w'), indent=1)
print('\nwritten atlas/data/round470/nilsson2014_yield.json')
