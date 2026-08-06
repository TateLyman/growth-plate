"""Do the human tall-stature genes concentrate in one ZONE of the human growth plate?

Data on disk only.  Gene sets from HPO (every gene in which human variation is
annotated to cause tall or short stature).  Expression from chu2026's deposited
single-cell data, already reduced by this atlas to % of cells expressing, per zone,
per donor.

GUARDS, stated before the answer is seen:
  P1  COL10A1 must be maximal in the hypertrophic zone.
  P2  COL2A1 must be detected in >50% of cells in every zone.
  P3  MKI67 must be higher in proliferative than in hypertrophic.
If any positive control fails the zone labels are not trustworthy and NOTHING is reported.
A null result is a result; do not tune the gene set or the normalisation to move it.
"""
import csv, json, math, collections, sys
import numpy as np

# ---------- expression ------------------------------------------------------------
rows = list(csv.reader(open("/home/user/growth-plate/query/human_growth_plate_expression.byzone.csv")))
hdr, rows = rows[0], rows[1:]
cols = hdr[1:]
# donor3 was excluded from the neprilysin analysis for an untrustworthy zone assignment
# (83-98% COL10A1+ in EVERY zone).  donor4 has 13-62 cells per zone.  Both dropped, and
# the drop is declared, not silent.
DROP = ("donor3", "donor4")
keep_idx = [i for i, c in enumerate(cols) if not c.endswith(DROP)]
cols_k = [cols[i] for i in keep_idx]
zones = ["GP1_2_stem", "GP3_proliferative", "GP4_prehypertrophic", "GP5_hypertrophic"]
zidx = {z: [j for j, c in enumerate(cols_k) if c.startswith(z + "__")] for z in zones}
print("donors dropped:", ", ".join(DROP))
print("columns used:", ", ".join(cols_k))

genes, X = [], []
for r in rows:
    genes.append(r[0])
    X.append([float(r[1:][i]) for i in keep_idx])
X = np.asarray(X)                      # genes x columns, % of cells expressing
G = {g: i for i, g in enumerate(genes)}

# per-donor-column standardisation: a zone/donor with a deeper library detects more of
# EVERYTHING, so compare each gene against its own column's distribution.
Xr = np.apply_along_axis(lambda v: (np.argsort(np.argsort(v)) + 0.5) / len(v), 0, X)
Z = np.column_stack([Xr[:, zidx[z]].mean(1) for z in zones])     # genes x 4 zones

def show(g):
    """mean % of cells expressing, PER ZONE - X has one column per (zone, donor),
    so the per-zone value must be averaged over that zone's donor columns.  An
    earlier version zipped the 8 columns against the 4 zone names and silently
    truncated, which mislabelled proliferative columns as hypertrophic."""
    i = G.get(g)
    if i is None: return None
    return {z: round(float(np.mean(X[i, zidx[z]])), 2) for z in zones}

# ---------- positive controls -----------------------------------------------------
ok, notes = True, []
c10, c2, ki = show("COL10A1"), show("COL2A1"), show("MKI67")
for nm, v in (("COL10A1", c10), ("COL2A1", c2), ("MKI67", ki)):
    print(f"  {nm}: {v}")
if not c10 or max(c10, key=c10.get) != "GP5_hypertrophic":
    ok = False; notes.append("P1 FAILED: COL10A1 not maximal in hypertrophic zone")
if not c2 or min(c2.values()) <= 50:
    ok = False; notes.append(f"P2 FAILED: COL2A1 min across zones = {min(c2.values()) if c2 else None}")
if not ki or ki["GP3_proliferative"] <= ki["GP5_hypertrophic"]:
    ok = False; notes.append("P3 FAILED: MKI67 not higher in proliferative than hypertrophic")
if not ok:
    print("\n".join(notes)); print("REFUSING TO REPORT THE ENRICHMENT."); sys.exit(1)
print("positive controls PASS\n")

# ---------- gene sets -------------------------------------------------------------
def hpo_genes(root_ids):
    import re
    terms, cur = {}, None
    for line in open("hpo/hp.obo", encoding="utf-8"):
        line = line.rstrip("\n")
        if line == "[Term]": cur = {"id": None, "is_a": []}
        elif line.startswith("id: HP:") and cur is not None: cur["id"] = line[4:]
        elif line.startswith("is_a: ") and cur is not None: cur["is_a"].append(line[6:].split(" ! ")[0])
        elif line == "" and cur and cur["id"]: terms[cur["id"]] = cur; cur = None
    ch = collections.defaultdict(list)
    for t in terms.values():
        for p in t["is_a"]: ch[p].append(t["id"])
    want = set()
    for r in root_ids:
        st = [r]; want.add(r)
        while st:
            n = st.pop()
            for c in ch.get(n, []):
                if c not in want: want.add(c); st.append(c)
    out = set()
    hdr = None
    for line in open("hpo/phenotype_to_genes.txt", encoding="utf-8"):
        if line.startswith("#"): continue
        p = line.rstrip("\n").split("\t")
        if hdr is None and p[0] == "hpo_id": hdr = p; continue
        d = dict(zip(hdr, p))
        if d["hpo_id"] in want: out.add(d["gene_symbol"])
    return out

TALL  = hpo_genes(["HP:0000098"])
SHORT = hpo_genes(["HP:0004322"])
BOTH  = TALL & SHORT
print(f"HPO tall stature: {len(TALL)} genes; short stature: {len(SHORT)}; in both: {len(BOTH)}")

def in_data(s): return sorted(g for g in s if g in G)
sets = {"tall_only": in_data(TALL - SHORT), "short_only": in_data(SHORT - TALL),
        "tall_and_short": in_data(BOTH)}
for k, v in sets.items(): print(f"  {k}: {len(v)} present in the expression matrix")

# ---------- expression-matched background -----------------------------------------
mean_expr = X.mean(1)
order = np.argsort(mean_expr)
rank_of = np.empty(len(genes), int); rank_of[order] = np.arange(len(genes))
rng = np.random.default_rng(20260806)
def matched_null(idx, n=2000):
    """resample genes with the same overall detection rank, so 'expressed at all'
    cannot masquerade as 'zone specific'."""
    out = []
    for _ in range(n):
        pick = []
        for i in idx:
            lo, hi = max(0, rank_of[i] - 250), min(len(genes) - 1, rank_of[i] + 250)
            pick.append(order[rng.integers(lo, hi + 1)])
        out.append(Z[pick].mean(0))
    return np.asarray(out)

print(f"\n{'set':<16} " + " ".join(f"{z.split('_',1)[1][:12]:>13}" for z in zones))
res = {}
for k, gl in sets.items():
    idx = [G[g] for g in gl]
    obs = Z[idx].mean(0)
    null = matched_null(idx)
    p = [(np.sum(null[:, j] >= obs[j]) + 1) / (len(null) + 1) for j in range(4)]
    p_lo = [(np.sum(null[:, j] <= obs[j]) + 1) / (len(null) + 1) for j in range(4)]
    res[k] = dict(n=len(gl), obs=obs.tolist(), null_mean=null.mean(0).tolist(),
                  p_high=p, p_low=p_lo)
    print(f"{k:<16} " + " ".join(f"{obs[j]:.3f}({null.mean(0)[j]:.3f})" for j in range(4)))
    print(f"{'':<16} " + " ".join(f"  p+={p[j]:.4f}   " for j in range(4)))

# ---------- which zone is each tall gene's maximum? -------------------------------
print("\nzone of maximum standardised expression, tall-stature genes:")
mx = collections.Counter(zones[int(np.argmax(Z[G[g]]))] for g in sets["tall_only"])
mxs = collections.Counter(zones[int(np.argmax(Z[G[g]]))] for g in sets["short_only"])
for z in zones:
    print(f"  {z:<22} tall {mx[z]:>3}/{len(sets['tall_only'])}   short {mxs[z]:>3}/{len(sets['short_only'])}")
json.dump({"result": res, "tall_argmax": dict(mx), "short_argmax": dict(mxs),
           "sets": {k: v for k, v in sets.items()}},
          open("zone_enrich.json", "w"), indent=1)
