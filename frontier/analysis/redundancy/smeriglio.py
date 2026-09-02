"""GSE105122 - Smeriglio's own Tet1 KO cartilage RNA-seq (WT n=3 vs Tet1 KO n=3).

This is the dataset behind R159's ACAN CONFLICT: Smeriglio 2020 reported that TET1
loss stops SOX9 binding at Col2a1 and Acan, and ACAN pLoF is the most
height-NEGATIVE gene in the kosmicki table (-14.1 cm/allele). R159 called it "the
sharpest new hole" but never quantified it. Here it is quantified.

Counts use retired UCSC mm10 knownGene 'uc' transcript IDs; mapped to symbols via
kg10ToKg11 coordinates intersected with mm10 refGene.
"""
import gzip, io, os, re, math, statistics as st, urllib.request

D = '/home/user/gp_data'
SM = os.path.join(D, 'smer')

# ---- 1. uc ID -> coordinates ----
loc = {}
with gzip.open('/tmp/kg10ToKg11.gz', 'rt') as f:
    for line in f:
        p = line.rstrip('\n').split('\t')
        if len(p) >= 4 and p[0].startswith('uc'):
            loc[p[0]] = (p[1], int(p[2]), int(p[3]))
print('uc IDs with coordinates:', len(loc))

# ---- 2. mm10 refGene -> symbol intervals ----
rg = os.path.join(D, 'refGene_mm10.txt.gz')
if not os.path.exists(rg):
    urllib.request.urlretrieve(
        'https://hgdownload.soe.ucsc.edu/goldenPath/mm10/database/refGene.txt.gz', rg)
by_chr = {}
with gzip.open(rg, 'rt') as f:
    for line in f:
        p = line.rstrip('\n').split('\t')
        if len(p) < 13:
            continue
        chrom, s, e, sym = p[2], int(p[4]), int(p[5]), p[12]
        by_chr.setdefault(chrom, []).append((s, e, sym))
for c in by_chr:
    by_chr[c].sort()
print('refGene chroms:', len(by_chr))


def sym_for(uc):
    if uc not in loc:
        return None
    c, s, e = loc[uc]
    best, bestov = None, 0
    for (gs, ge, sym) in by_chr.get(c, []):
        if ge < s:
            continue
        if gs > e:
            break
        ov = min(e, ge) - max(s, gs)
        if ov > bestov:
            best, bestov = sym, ov
    return best


# ---- 3. load counts ----
FILES = {
    'WT': ['GSM2819565_WT_1_AGTCAA_counts.txt.gz', 'GSM2819566_WT_2_AGTTCC_counts.txt.gz',
           'GSM2819567_WT_3_ATGTCA_counts.txt.gz'],
    'KO': ['GSM2819568_KO_1_CCGTCC_counts.txt.gz', 'GSM2819569_KO_2_GTGAAA_counts.txt.gz',
           'GSM2819570_KO_3_GTCCGC_counts.txt.gz'],
}
counts = {}
order = []
for grp, fs in FILES.items():
    for fn in fs:
        col = {}
        with gzip.open(os.path.join(SM, fn), 'rt') as f:
            next(f)
            for line in f:
                a = line.rstrip('\n').split('\t')
                if len(a) >= 2:
                    try:
                        col[a[0]] = int(float(a[1]))
                    except ValueError:
                        pass
        counts[fn] = col
        order.append((grp, fn))
ids = sorted(set().union(*[set(v) for v in counts.values()]))
print('transcripts:', len(ids), '| libraries:', len(order))

# map transcripts -> gene, summing counts per gene
tx2g = {}
for uc in ids:
    s = sym_for(uc)
    if s:
        tx2g[uc] = s
print('transcripts mapped to a symbol:', len(tx2g))

genes = {}
for grp, fn in order:
    tot = sum(counts[fn].values())
    for uc, c in counts[fn].items():
        g = tx2g.get(uc)
        if g:
            genes.setdefault(g, {}).setdefault(fn, 0)
            genes[g][fn] += c
libsize = {fn: sum(counts[fn].values()) for _, fn in order}
print('genes:', len(genes), '| library sizes:', {k.split("_")[1]: v for k, v in libsize.items()})


def cpm(g, fn):
    return genes.get(g, {}).get(fn, 0) / libsize[fn] * 1e6


def welch(a, b):
    if len(a) < 2 or len(b) < 2:
        return float('nan')
    va, vb = st.variance(a), st.variance(b)
    se = math.sqrt(va / len(a) + vb / len(b))
    if se == 0:
        return float('nan')
    t = (st.mean(a) - st.mean(b)) / se
    return t


WT = [fn for g, fn in order if g == 'WT']
KO = [fn for g, fn in order if g == 'KO']

PANEL = [
    ('Tet1', 'the target - KO check'),
    ('Tet2', 'paralogue'), ('Tet3', 'paralogue'),
    ('Acan', '*** ACAN CONFLICT: pLoF = -14.1 cm/allele, most height-negative gene ***'),
    ('Col2a1', 'the other SOX9 target Smeriglio names'),
    ('Sox9', 'master chondrogenic TF'),
    ('Col10a1', 'hypertrophy'), ('Ihh', 'growth driver'), ('Pthlh', 'resting zone'),
    ('Col9a1', 'cartilage ECM'), ('Col11a1', 'cartilage ECM'),
    ('Fgfr3', 'growth brake'), ('Npr2', 'CNP receptor'), ('Nppc', 'CNP'),
    ('Mki67', 'proliferation'), ('Igf1', 'growth'),
    ('Ccnd1', 'cell cycle'), ('Sox5', 'SOX trio'), ('Sox6', 'SOX trio'),
]

print('\n' + '=' * 94)
print('Tet1 KO vs WT  -  Smeriglio cartilage RNA-seq, n=3 vs n=3')
print('=' * 94)
print('%-9s %10s %10s %9s %8s %7s  %s' % ('gene', 'WT CPM', 'KO CPM', 'log2FC', 'x-fold', 't', 'note'))
for g, note in PANEL:
    if g not in genes:
        print('%-9s %10s %10s %9s %8s %7s  %s' % (g, '-', '-', '-', '-', '-', note + '  [NOT DETECTED]'))
        continue
    w = [cpm(g, f) for f in WT]
    k = [cpm(g, f) for f in KO]
    mw, mk = st.mean(w), st.mean(k)
    lfc = math.log2((mk + 0.5) / (mw + 0.5))
    t = welch(k, w)
    print('%-9s %10.1f %10.1f %+9.2f %8.2f %7.2f  %s'
          % (g, mw, mk, lfc, 2 ** lfc, t if t == t else float('nan'), note))

print("""
INTERPRETATION KEY
  Acan log2FC is the ACAN conflict, quantified for the first time in this file.
  A -14.1 cm/allele gene falling hard in a Tet1 NULL is the worst case; a small
  or absent change means R159's "sharpest hole" is quantitatively minor.
  Remember the KO is 0% gene dosage - our target is ~50%, one rung down R137's
  magnitude ladder.""")
