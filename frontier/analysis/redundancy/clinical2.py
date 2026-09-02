"""Inverted and cached: build the FULL set of ChEMBL molecules that ever reached a
clinical phase, then intersect with everything active on NRK's pocket neighbours.
Score each clinical drug by breadth across the proxies and by its PDGFR/KIT liability
(the imatinib-class -0.35 SDS height decrement in children)."""
import json, os, urllib.request, time

BASE = 'https://www.ebi.ac.uk/chembl/api/data'
def get(url):
    for _ in range(5):
        try:
            with urllib.request.urlopen(url, timeout=120) as r: return json.load(r)
        except Exception: time.sleep(3)
    return None

PROXY = {'TNIK':'CHEMBL4527','MINK1':'CHEMBL5518','MAP4K4':'CHEMBL6166','MAP4K3':'CHEMBL5432',
         'MAP4K1':'CHEMBL5749','MAP4K5':'CHEMBL4852','TAOK1':'CHEMBL5261','TAOK2':'CHEMBL1075195',
         'CDK5':'CHEMBL4036','PAK2':'CHEMBL4487','PAK1':'CHEMBL4600','STK3':'CHEMBL4708',
         'STK4':'CHEMBL4598','CSNK1D':'CHEMBL2828','CSNK1E':'CHEMBL4937','SLK':'CHEMBL4202',
         'ULK1':'CHEMBL6006','PTK2':None,'STK39':'CHEMBL1163108'}
LIAB = {'PDGFRA':'CHEMBL2007','PDGFRB':'CHEMBL1913','KIT':'CHEMBL1936'}
# PTK2/FAK -- NRK's closest hinge match outside the clade
d = get('%s/target.json?target_components__accession=Q05397&limit=20' % BASE)
for t in (d['targets'] if d else []):
    if t['target_type'] == 'SINGLE PROTEIN': PROXY['PTK2'] = t['target_chembl_id']; break

def actives(tid, cutoff=1000.0):
    out = {}; off = 0
    while True:
        u = ('%s/activity.json?target_chembl_id=%s&standard_type__in=IC50,Ki,Kd&standard_units=nM'
             '&limit=1000&offset=%d' % (BASE, tid, off))
        d = get(u)
        if not d or not d.get('activities'): break
        for a in d['activities']:
            v, c = a.get('standard_value'), a.get('molecule_chembl_id')
            if v is None or c is None: continue
            try: v = float(v)
            except: continue
            if v <= cutoff: out[c] = min(out.get(c, 9e9), v)
        off += 1000
        if off >= (d['page_meta']['total_count'] or 0) or off > 15000: break
    return out

CACHE = 'act_cache.json'
ACT = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
for k, t in list(PROXY.items()) + list(LIAB.items()):
    if k in ACT or not t: continue
    ACT[k] = actives(t); print("  %-8s %5d" % (k, len(ACT[k]))); json.dump(ACT, open(CACHE,'w'))

# every molecule that reached a clinical phase
DCACHE = 'drug_cache.json'
if os.path.exists(DCACHE):
    DRUG = json.load(open(DCACHE))
else:
    DRUG = {}; off = 0
    while True:
        d = get('%s/molecule.json?max_phase__gte=1&limit=1000&offset=%d'
                '&only=molecule_chembl_id,pref_name,max_phase' % (BASE, off))
        if not d or not d.get('molecules'): break
        for m in d['molecules']:
            DRUG[m['molecule_chembl_id']] = [m.get('pref_name'), m.get('max_phase')]
        off += 1000
        print("   drugs %d / %d" % (off, d['page_meta']['total_count'] or 0))
        if off >= (d['page_meta']['total_count'] or 0): break
    json.dump(DRUG, open(DCACHE,'w'))
print("clinical-phase molecules in ChEMBL: %d" % len(DRUG))

rows = []
for c, (nm, ph) in DRUG.items():
    hits = {k: ACT[k][c] for k in PROXY if k in ACT and c in ACT[k]}
    if not hits: continue
    lia = {k: ACT[k][c] for k in LIAB if k in ACT and c in ACT[k]}
    try: ph = float(ph) if ph is not None else 0.0
    except: ph = 0.0
    rows.append((len(hits), ph, nm or c, c, hits, lia))
rows.sort(key=lambda r: (-r[0], -r[1]))

print()
print("=" * 122)
print("CLINICAL-PHASE DRUGS ACTIVE (<=1 uM) ON NRK's ATP-POCKET NEIGHBOURS")
print("=" * 122)
print("%-24s %-6s %-5s %-40s %s" % ("drug", "phase", "#prox", "proxies (nM)", "PDGFR/KIT (nM)"))
print("-" * 122)
for n, ph, nm, c, hits, lia in rows[:40]:
    hs = ", ".join("%s %.0f" % (k, v) for k, v in sorted(hits.items(), key=lambda x: x[1]))
    lt = ", ".join("%s %.0f" % (k, v) for k, v in sorted(lia.items())) or "*** CLEAN ***"
    print("%-24s %-6.1f %-5d %-40s %s" % (str(nm)[:24], ph, n, hs[:40], lt))

print()
print("=" * 122)
print("THE ONLY SUBSET THAT COULD WORK: hits >=2 NRK proxies AND no PDGFR/KIT activity <=1 uM")
print("=" * 122)
for n, ph, nm, c, hits, lia in rows:
    if n >= 2 and not lia:
        print("  %-26s phase %-4.1f  %s" % (str(nm)[:26], ph,
              ", ".join("%s %.0f nM" % (k, v) for k, v in sorted(hits.items(), key=lambda x: x[1]))))
