#!/usr/bin/env python3
"""R482 - Longshanks selected-vs-control, from the deposited histomorphometry.

>>> THE v(m) DECOMPOSITION THIS SCRIPT WAS WRITTEN TO DO CANNOT BE DONE ON THIS
>>> DATASET, AND THE FAILURE IS INFORMATIVE.  Column J/L gives a mean domain
>>> height per hypertrophic cell of 13.9 um while column M gives a mean
>>> hypertrophic cell height of 30.2 um.  A cell cannot be taller than the
>>> domain that contains it, so the two columns are not measured on the same
>>> population: J/L is a ZONE MEAN over all hypertrophic cells (which start
>>> small) while M is almost certainly the TERMINAL cell height.  Subtracting
>>> one from the other returns a nonsensical v(m) of -16 um.  The subtraction
>>> is left in the output, labelled INVALID, so the error is visible rather
>>> than silently removed.  What survives is the group contrast on each
>>> measured parameter, which is design-controlled and is the real result.

Source: Marchini & Rolian, Dryad doi:10.5061/dryad.0g1f2, sheet
'Histomorphometry Data'.  Two independent selected lines (LS1, LS2) plus
random-bred controls; ~20 generations of artificial selection on tibia length
relative to body mass.

The sheet reports, per animal:
    J  Mean Hypertrophic Zone Depth (um)
    L  # Hypertrophic Cells
    M  Mean hypertrophic cell height (um)

so the mean CELL-TO-CELL SPACING in the hypertrophic zone is J/L, which is the
domain height contributed per cell.  Subtracting the mean cell height M leaves
the MATRIX height contributed per cell.  This is the linear form of Wilsman's
v(d) = v(c) + v(m), and is the same decomposition Vanky 2000 performs via
cell-centre distance x matrix volume fraction.

NOTHING is imputed.  Animals missing any of the three fields are dropped and
the count is reported.
"""
import zipfile, re, html, math, statistics as st, itertools, os

XLSX = os.path.join(os.path.dirname(__file__), '..', '..',
                    'acquire', 'bundle4',
                    'Marchini+and+Rolian+-+Longshanks+Growth+Raw+Data 2.xlsx')

def load(sheet):
    z = zipfile.ZipFile(XLSX)
    ss = [html.unescape(s) for s in
          re.findall(r'<t[^>]*>(.*?)</t>', z.read('xl/sharedStrings.xml').decode('utf8'), re.S)]
    d = z.read(sheet).decode('utf8')
    out = []
    for rn, body in re.findall(r'<row[^>]*r="(\d+)"[^>]*>(.*?)</row>', d, re.S):
        rec = {}
        for col, attrs, v in re.findall(r'<c r="([A-Z]+)\d+"([^>]*)>(?:<v>(.*?)</v>)?', body):
            if v is None:
                continue
            rec[col] = ss[int(v)] if 't="s"' in attrs else v
        out.append((rn, rec))
    return out

def num(rec, col):
    try:
        return float(rec[col])
    except (KeyError, ValueError, TypeError):
        return None

def welch(a, b):
    """Welch t and two-sided p via a normal-tail fallback-free Student survival."""
    na, nb = len(a), len(b)
    ma, mb = st.mean(a), st.mean(b)
    va, vb = st.variance(a), st.variance(b)
    se = math.sqrt(va / na + vb / nb)
    t = (ma - mb) / se
    df = (va / na + vb / nb) ** 2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
    # two-sided p from the incomplete beta (regularised) - exact Student
    x = df / (df + t * t)
    p = betainc(df / 2.0, 0.5, x)
    return t, df, p

def betainc(a, b, x):
    """Regularised incomplete beta I_x(a,b) by continued fraction (NR 6.4)."""
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lbeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    front = math.exp(math.log(x) * a + math.log(1 - x) * b - lbeta) / a
    if x < (a + 1) / (a + b + 2):
        return front * _cf(a, b, x)
    else:
        return 1.0 - math.exp(math.log(1 - x) * b + math.log(x) * a - lbeta) / b * _cf(b, a, 1 - x)

def _cf(a, b, x, itmax=300, eps=1e-12):
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < 1e-30: d = 1e-30
    d = 1.0 / d
    h = d
    for m in range(1, itmax):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < 1e-30: d = 1e-30
        c = 1.0 + aa / c
        if abs(c) < 1e-30: c = 1e-30
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < 1e-30: d = 1e-30
        c = 1.0 + aa / c
        if abs(c) < 1e-30: c = 1e-30
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < eps:
            break
    return h

def main():
    rows = load('xl/worksheets/sheet2.xml')
    hdr = rows[0][1]
    print('COLUMNS:', {k: v for k, v in sorted(hdr.items())})
    print()

    recs, dropped = [], 0
    for rn, r in rows[1:]:
        line = (r.get('C') or '').strip()
        if line not in ('Ctrl', 'LS1', 'LS2'):
            dropped += 1
            continue
        hz, nh, ch = num(r, 'J'), num(r, 'L'), num(r, 'M')
        tib = num(r, 'E')
        if None in (hz, nh, ch) or nh == 0:
            dropped += 1
            continue
        v_d = hz / nh                 # domain height per cell, um
        v_c = ch                      # cell height, um
        v_m = v_d - v_c               # matrix height per cell, um
        recs.append(dict(id=r.get('A'), sex=r.get('B'), line=line,
                         mass=num(r, 'D'), tibia=tib,
                         gp_ct=num(r, 'F'), gp_hist=num(r, 'G'),
                         rz=num(r, 'H'), pz=num(r, 'I'), hz=hz,
                         n_prolif=num(r, 'K'), n_hyper=nh,
                         v_d=v_d, v_c=v_c, v_m=v_m,
                         frac_m=v_m / v_d if v_d else None))
    print(f'usable animals = {len(recs)}   dropped = {dropped}')
    print()

    def grp(name):
        return [r for r in recs if r['line'] == name]

    ctrl = grp('Ctrl')
    sel = grp('LS1') + grp('LS2')

    fields = [('tibia', 'tibia length (um)'),
              ('gp_hist', 'total GP height, histology (um)'),
              ('rz', 'resting zone depth (um)'),
              ('pz', 'proliferative zone depth (um)'),
              ('hz', 'hypertrophic zone depth (um)'),
              ('n_prolif', '# proliferative cells'),
              ('n_hyper', '# hypertrophic cells'),
              ('v_d', 'v(d)  domain height per cell (um)'),
              ('v_c', 'v(c)  hypertrophic CELL height (um)'),
              ('v_m', 'INVALID v(d)-v(c), see docstring'),
              ('mass', 'body mass (g)')]

    print('=' * 96)
    print('SELECTED (LS1+LS2) vs CONTROL   -- all animals, both sexes')
    print('=' * 96)
    print(f'{"parameter":40s} {"Ctrl":>18s} {"Selected":>18s} {"ratio":>7s} {"t":>7s} {"p":>9s}')
    for key, label in fields:
        a = [r[key] for r in ctrl if r[key] is not None]
        b = [r[key] for r in sel if r[key] is not None]
        if len(a) < 3 or len(b) < 3:
            continue
        t, df, p = welch(b, a)
        print(f'{label:40s} {st.mean(a):9.3f}+-{st.stdev(a):6.3f} '
              f'{st.mean(b):9.3f}+-{st.stdev(b):6.3f} '
              f'{st.mean(b)/st.mean(a):7.3f} {t:7.2f} {p:9.2e}')

    for ln in ('LS1', 'LS2'):
        print()
        print('-' * 96)
        print(f'{ln} vs Ctrl')
        print('-' * 96)
        g = grp(ln)
        for key, label in fields:
            if key == 'v_m':
                continue
            a = [r[key] for r in ctrl if r[key] is not None]
            b = [r[key] for r in g if r[key] is not None]
            if len(a) < 3 or len(b) < 3:
                continue
            t, df, p = welch(b, a)
            print(f'{label:40s} {st.mean(a):9.3f} {st.mean(b):9.3f} '
                  f'{st.mean(b)/st.mean(a):7.3f} {t:7.2f} {p:9.2e}')

    # sex-stratified, because Ctrl is 11M/5F and LS2 is 7M/10F
    print()
    print('=' * 96)
    print('SEX-STRATIFIED (the group sex ratios are unbalanced: Ctrl 11M/5F, LS1 8M/8F, LS2 7M/10F)')
    print('=' * 96)
    for sex in ('M', 'F'):
        a_all = [r for r in ctrl if r['sex'] == sex]
        b_all = [r for r in sel if r['sex'] == sex]
        print(f'\n  sex={sex}   n_ctrl={len(a_all)}  n_sel={len(b_all)}')
        for key, label in fields:
            if key == 'v_m':
                continue
            a = [r[key] for r in a_all if r[key] is not None]
            b = [r[key] for r in b_all if r[key] is not None]
            if len(a) < 3 or len(b) < 3:
                continue
            t, df, p = welch(b, a)
            print(f'    {label:38s} {st.mean(a):9.3f} {st.mean(b):9.3f} '
                  f'{st.mean(b)/st.mean(a):7.3f} {t:7.2f} {p:9.2e}')

    # within-animal check: does v_m track tibia length at all?
    print()
    print('=' * 96)
    print('CORRELATION WITH TIBIA LENGTH (all animals pooled, Pearson r)')
    print('=' * 96)
    def pearson(xs, ys):
        n = len(xs); mx, my = st.mean(xs), st.mean(ys)
        num_ = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        den = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
        r = num_ / den
        t = r * math.sqrt((n - 2) / (1 - r * r)) if abs(r) < 1 else float('inf')
        p = betainc((n - 2) / 2.0, 0.5, (n - 2) / ((n - 2) + t * t))
        return r, n, p
    pool = [r for r in recs if r['tibia'] is not None]
    for key, label in [('v_d', 'v(d) domain height/cell'),
                       ('v_c', 'v(c) cell height'),
                       ('n_hyper', '# hypertrophic cells'),
                       ('n_prolif', '# proliferative cells'),
                       ('hz', 'hypertrophic zone depth'),
                       ('gp_hist', 'total GP height'),
                       ('mass', 'body mass')]:
        xs = [r['tibia'] for r in pool if r[key] is not None]
        ys = [r[key] for r in pool if r[key] is not None]
        r_, n_, p_ = pearson(xs, ys)
        print(f'  tibia vs {label:32s} r={r_:+.3f}  n={n_}  p={p_:.2e}')

if __name__ == '__main__':
    main()
