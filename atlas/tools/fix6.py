p = '/home/user/growth-plate/atlas/tools/overgrowth_screen.py'
s = open(p).read()

# The old API returned a numeric phase; this one returns a string like APPROVAL or PHASE_III.
# Rank them explicitly rather than sorting strings, which would put PHASE_I above APPROVAL.
s = s.replace('''CONTROL_ENSEMBL = "ENSG00000137869"          # CYP19A1''',
'''STAGE_RANK = {"APPROVAL": 5, "PHASE_IV": 5, "PHASE_III": 4, "PHASE_II": 3, "PHASE_I": 2,
              "EARLY_PHASE_I": 1, "PRECLINICAL": 0, None: -1, "": -1}


def stage_rank(v):
    """Order clinical stages. Sorting the raw strings would rank PHASE_I above APPROVAL."""
    return STAGE_RANK.get((v or "").upper(), 0)


CONTROL_ENSEMBL = "ENSG00000137869"          # CYP19A1''', 1)

s = s.replace('''        top = sorted(uniq, key=lambda d: -(d[2] or 0))[:4]''',
              '''        top = sorted(uniq, key=lambda d: -stage_rank(d[2]))[:4]''', 1)

s = s.replace('''            "max_phase": (max([d[2] or 0 for d in uniq], default="")
                          if drugs is not None else ""),''',
              '''            "max_phase": (max((d[2] for d in uniq), key=stage_rank, default="")
                          if drugs is not None else ""),''', 1)

s = s.replace('''        print(f"  {r['gene']:10s} {r['best_assoc_score']:6.3f} {r['gp_donors_detected']:>3} "
              f"{r['n_known_drugs']:5d} {str(r['max_phase']):>3}  {r['top_terms'][:70]}")''',
              '''        print(f"  {r['gene']:10s} {r['best_assoc_score']:6.3f} {r['gp_donors_detected']:>3} "
              f"{r['n_known_drugs']:5d} {str(r['max_phase'])[:9]:>9}  {r['top_terms'][:62]}")''', 1)

s = s.replace('''    print(f"  {'gene':10s} {'assoc':>6s} {'GP':>3s} {'drugs':>5s} {'ph':>3s}  terms")''',
              '''    print(f"  {'gene':10s} {'assoc':>6s} {'GP':>3s} {'drugs':>5s} {'stage':>9s}  terms")''', 1)

open(p, 'w').write(s)
print('patched')
