"""NRK is Tdark with 0 ligands. But its kinase domain is 63-65% identical to
MAP4K4/TNIK/MINK1, with the same Met gatekeeper and the same HRD motif.
So: what compounds hit that clade, and are any of them APPROVED drugs?
If an approved drug binds all three GCK-IV members potently, NRK is the most
likely untested member of the same set."""
import urllib.request, json, collections, time

CHEMBL = {"MAP4K4": "CHEMBL4899", "TNIK": "CHEMBL5330", "MINK1": "CHEMBL5591"}

def get(url):
    for _ in range(3):
        try:
            return json.load(urllib.request.urlopen(url, timeout=90))
        except Exception as e:
            time.sleep(2)
    return None

# resolve target IDs from accession to be safe
ACC = {"MAP4K4": "O95819", "TNIK": "Q9UKE5", "MINK1": "Q8N4C8", "MAP4K1": "Q92918"}
tids = {}
for sym, acc in ACC.items():
    d = get("https://www.ebi.ac.uk/chembl/api/data/target.json?target_components__accession=%s&limit=5" % acc)
    if d and d['targets']:
        for t in d['targets']:
            if t['target_type'] == 'SINGLE PROTEIN':
                tids[sym] = t['target_chembl_id']; break
    print("%-8s %s -> %s" % (sym, acc, tids.get(sym)))

print()
print("Pulling potent activities (pChEMBL >= 6, i.e. <= 1 uM) per target ...")
binders = {}
for sym, tid in tids.items():
    mols = {}
    off = 0
    while True:
        d = get("https://www.ebi.ac.uk/chembl/api/data/activity.json"
                "?target_chembl_id=%s&pchembl_value__gte=6&limit=1000&offset=%d" % (tid, off))
        if not d: break
        for a in d['activities']:
            m = a.get('molecule_chembl_id')
            try: p = float(a.get('pchembl_value'))
            except (TypeError, ValueError): continue
            if m and (m not in mols or p > mols[m]): mols[m] = p
        if not d['page_meta'].get('next'): break
        off += 1000
        if off > 4000: break
    binders[sym] = mols
    print("  %-8s %d distinct potent compounds" % (sym, len(mols)))

core = ['MAP4K4', 'TNIK', 'MINK1']
core = [c for c in core if c in binders]
shared = set(binders[core[0]])
for c in core[1:]: shared &= set(binders[c])
print()
print("Compounds potent (<=1 uM) against ALL of %s: %d" % ("+".join(core), len(shared)))

print()
print("Which of those are APPROVED DRUGS (max_phase 4) or clinical (>=1)?")
print("%-16s %-28s %5s  %s" % ("ChEMBL ID", "name", "phase", "  ".join("%-7s" % c for c in core)))
print("-" * 86)
rows = []
for i, m in enumerate(sorted(shared)):
    d = get("https://www.ebi.ac.uk/chembl/api/data/molecule/%s.json" % m)
    if not d: continue
    ph = d.get('max_phase')
    name = d.get('pref_name') or ''
    try: phf = float(ph)
    except (TypeError, ValueError): phf = 0.0
    if phf >= 1:
        rows.append((phf, m, name, [binders[c].get(m) for c in core]))
    if i > 400: break
rows.sort(reverse=True)
for phf, m, name, ps in rows:
    print("%-16s %-28s %5.1f  %s" % (m, name[:28], phf,
          "  ".join("%-7s" % ("%.1f" % p if p else "-") for p in ps)))
print()
print("(pChEMBL 6 = 1 uM, 7 = 100 nM, 8 = 10 nM, 9 = 1 nM)")
