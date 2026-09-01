"""How hard is it to be selective WITHIN the GCK-IV clade?

This is the question that decides whether PF-06260933 (optimised FOR selectivity)
would hit NRK. If compounds potent on MAP4K4 almost always also hit MINK1/TNIK
(63-65% identity, same gatekeeper -- the same relationship NRK has), then clade
cross-reactivity is the rule and NRK is likely in range. If med-chem routinely
separates them, then a selective compound will likely spare NRK too.

Controls for testing bias by using only compounds ASSAYED against both targets.
"""
import urllib.request, json, time

ACC = {"MAP4K4": "O95819", "TNIK": "Q9UKE5", "MINK1": "Q8N4C8", "MAP4K1": "Q92918"}

def get(u):
    for _ in range(3):
        try: return json.load(urllib.request.urlopen(u, timeout=90))
        except Exception: time.sleep(2)
    return None

tids = {}
for sym, acc in ACC.items():
    d = get("https://www.ebi.ac.uk/chembl/api/data/target.json?target_components__accession=%s&limit=5" % acc)
    for t in (d['targets'] if d else []):
        if t['target_type'] == 'SINGLE PROTEIN':
            tids[sym] = t['target_chembl_id']; break

# pull ALL activities with a pchembl value (not just potent ones)
allact = {}
for sym, tid in tids.items():
    mols = {}
    off = 0
    while True:
        d = get("https://www.ebi.ac.uk/chembl/api/data/activity.json"
                "?target_chembl_id=%s&pchembl_value__isnull=false&limit=1000&offset=%d" % (tid, off))
        if not d: break
        for a in d['activities']:
            m = a.get('molecule_chembl_id')
            try: p = float(a.get('pchembl_value'))
            except (TypeError, ValueError): continue
            if m and (m not in mols or p > mols[m]): mols[m] = p
        if not d['page_meta'].get('next'): break
        off += 1000
        if off > 6000: break
    allact[sym] = mols
    print("%-8s %-14s %d compounds with a measured pChEMBL" % (sym, tids[sym], len(mols)))

print()
print("CROSS-REACTIVITY WITHIN THE CLADE, among compounds ASSAYED AGAINST BOTH")
print("(controls for testing bias: only pairs where both measurements exist)")
print()
print("%-22s %8s %10s %12s %10s" % ("pair", "co-tested", "potent on A", "also potent B", "carry-over"))
print("-" * 70)
pairs = [("MAP4K4", "MINK1"), ("MAP4K4", "TNIK"), ("TNIK", "MINK1"),
         ("MAP4K4", "MAP4K1"), ("TNIK", "MAP4K1")]
for a, b in pairs:
    if a not in allact or b not in allact: continue
    both = set(allact[a]) & set(allact[b])
    pa = [m for m in both if allact[a][m] >= 6]
    pab = [m for m in pa if allact[b][m] >= 6]
    if not pa: continue
    print("%-22s %8d %10d %12d %9.0f%%" % ("%s -> %s" % (a, b), len(both), len(pa), len(pab),
                                           100.0 * len(pab) / len(pa)))

print()
print("For reference, kinase-domain identity to NRK:")
print("  MINK1 64.9%   MAP4K4 64.5%   TNIK 63.0%   |   MAP4K1 41.2%")
print()
print("READ: if carry-over within the 63-65% group is HIGH, clade cross-reactivity")
print("is the rule and NRK is plausibly in range of any GCK-IV inhibitor.")
print("If med-chem routinely separates them, a SELECTIVE compound will likely spare NRK.")
