"""WHICH CLINICAL KINASE DRUGS COULD PLAUSIBLY HIT NRK?

R151's lesson decides the search strategy. Rentosertib failed on NRK not because of
contact residues (MINK1 is 23/23 identical and it STILL lost 3.7x) but because it is
SELECTIVE. So a selective drug for anything will miss NRK. Only a PROMISCUOUS drug
can catch it.

So: pull every ChEMBL compound with a clinical development phase that is active on
NRK's nearest ATP-pocket neighbours, and score by how many of them each compound hits.

THEN apply the constraint that actually matters here: the German CML-PAED II study
measured a -0.35 SDS height decrement in children on TKIs, an effect attributed to
PDGFRA/PDGFRB/KIT inhibition in the growth plate. A drug that is promiscuous ENOUGH
to catch NRK but SPARES PDGFR/KIT is the only thing that can work.
"""
import json, urllib.request, time

BASE = 'https://www.ebi.ac.uk/chembl/api/data'
def get(url):
    for _ in range(4):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return json.load(r)
        except Exception:
            time.sleep(2)
    return None

# NRK's nearest ATP-contact neighbours (kinome.py) + the clade
PROXY = {'TNIK':'Q9UKE5','MINK1':'Q8N4C8','MAP4K4':'O95819','MAP4K3':'Q8IVH8',
         'MAP4K1':'Q92918','MAP4K5':'Q9Y4K4','TAOK1':'Q7L7X3','TAOK2':'Q9UL54',
         'CDK5':'Q00535','PAK2':'Q13177','PAK1':'Q13153','STK3':'Q13188',
         'STK4':'Q13043','CSNK1D':'P48730','CSNK1E':'P49674','STK39':'Q9UEW8',
         'OXSR1':'O95747','SLK':'Q9H2G2','ULK1':'O75385'}
# the growth-plate liability targets (imatinib-class height decrement)
LIAB = {'PDGFRA':'P16234','PDGFRB':'P09619','KIT':'P10721'}

def tid(acc):
    d = get('%s/target.json?target_components__accession=%s&limit=20' % (BASE, acc))
    if not d: return None
    for t in d['targets']:
        if t['target_type'] == 'SINGLE PROTEIN': return t['target_chembl_id']
    return d['targets'][0]['target_chembl_id'] if d['targets'] else None

TID = {}
for k, a in list(PROXY.items()) + list(LIAB.items()):
    TID[k] = tid(a)
print("resolved targets:")
for k in TID: print("   %-8s %-14s %s" % (k, TID[k] or 'NONE', PROXY.get(k, LIAB.get(k))))

def actives(t, cutoff_nM=1000):
    """clinical-phase compounds active on target t below cutoff"""
    out = {}
    if not t: return out
    off = 0
    while True:
        u = ('%s/activity.json?target_chembl_id=%s&standard_type__in=IC50,Ki,Kd,EC50'
             '&standard_units=nM&limit=1000&offset=%d' % (BASE, t, off))
        d = get(u)
        if not d or not d.get('activities'): break
        for a in d['activities']:
            v = a.get('standard_value')
            c = a.get('molecule_chembl_id')
            if v is None or c is None: continue
            try: v = float(v)
            except: continue
            if v <= cutoff_nM:
                out[c] = min(out.get(c, 9e9), v)
        off += 1000
        if off >= (d['page_meta']['total_count'] or 0) or off > 12000: break
    return out

print()
print("pulling activities (<=1 uM) ...")
ACT = {}
for k, t in TID.items():
    ACT[k] = actives(t)
    print("   %-8s %5d compounds" % (k, len(ACT[k])))

# which compounds are clinical?
allc = set()
for k in PROXY:
    allc |= set(ACT.get(k, {}))
print("\nunique compounds active on >=1 NRK-proxy: %d" % len(allc))

# score promiscuity across proxies, then fetch phase for the top ones
score = {}
for c in allc:
    hits = [k for k in PROXY if c in ACT.get(k, {})]
    score[c] = hits
cands = sorted(allc, key=lambda c: -len(score[c]))[:400]

print("fetching development phase for top %d ..." % len(cands))
INFO = {}
for i in range(0, len(cands), 40):
    ids = ';'.join(cands[i:i+40])
    d = get('%s/molecule.json?molecule_chembl_id__in=%s&limit=40' % (BASE, ids))
    if not d: continue
    for m in d['molecules']:
        INFO[m['molecule_chembl_id']] = (m.get('pref_name'), m.get('max_phase'))

rows = []
for c in cands:
    nm, ph = INFO.get(c, (None, None))
    try: ph = float(ph) if ph is not None else 0.0
    except: ph = 0.0
    if ph < 1 or not nm: continue
    hits = score[c]
    lia = {k: ACT[k][c] for k in LIAB if c in ACT.get(k, {})}
    rows.append((len(hits), ph, nm, c, hits, lia))
rows.sort(key=lambda r: (-r[0], -r[1]))

print()
print("=" * 116)
print("CLINICAL-PHASE COMPOUNDS RANKED BY HOW MANY OF NRK's POCKET NEIGHBOURS THEY HIT (<=1 uM)")
print("=" * 116)
print("%-26s %-6s %-6s %-34s %s" % ("drug", "phase", "#prox", "proxies hit", "PDGFR/KIT liability (nM)"))
print("-" * 116)
for n, ph, nm, c, hits, lia in rows[:35]:
    lt = ", ".join("%s %.0f" % (k, v) for k, v in sorted(lia.items())) or "*** none measured <=1uM ***"
    print("%-26s %-6.1f %-6d %-34s %s" % (nm[:26], ph, n, ",".join(sorted(hits))[:34], lt))

print()
print("=" * 116)
print("THE SUBSET THAT MATTERS: promiscuous across NRK proxies AND clean on PDGFR/KIT")
print("=" * 116)
clean = [r for r in rows if not r[5] and r[0] >= 3]
if not clean:
    print("  NONE at >=3 proxies.")
    clean = [r for r in rows if not r[5] and r[0] >= 2]
    print("  relaxing to >=2 proxies:")
for n, ph, nm, c, hits, lia in clean[:25]:
    print("  %-28s phase %-4.1f  hits %d: %s" % (nm[:28], ph, n, ", ".join(sorted(hits))))
