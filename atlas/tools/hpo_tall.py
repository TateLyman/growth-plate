"""Every human gene in which variation is annotated to cause TALL STATURE or
OVERGROWTH, straight from the Human Phenotype Ontology.  This is the human-genetics
counterpart of the drug screen: not 'what raises a pathway' but 'what, in a person,
has ever made a person taller'."""
import re, collections, csv, json

# --- parse hp.obo into a child->parents map so we can take full descendant sets ----
terms, cur = {}, None
for line in open("hpo/hp.obo", encoding="utf-8"):
    line = line.rstrip("\n")
    if line == "[Term]": cur = {"id": None, "name": None, "is_a": [], "obsolete": False}
    elif line.startswith("id: HP:") and cur is not None: cur["id"] = line[4:]
    elif line.startswith("name: ") and cur is not None: cur["name"] = line[6:]
    elif line.startswith("is_a: ") and cur is not None: cur["is_a"].append(line[6:].split(" ! ")[0])
    elif line.startswith("is_obsolete: true") and cur is not None: cur["obsolete"] = True
    elif line == "" and cur and cur["id"]:
        terms[cur["id"]] = cur; cur = None
if cur and cur.get("id"): terms[cur["id"]] = cur
children = collections.defaultdict(list)
for t in terms.values():
    for p in t["is_a"]: children[p].append(t["id"])
def descendants(root):
    out, stack = {root}, [root]
    while stack:
        n = stack.pop()
        for c in children.get(n, []):
            if c not in out: out.add(c); stack.append(c)
    return out

ROOTS = {"HP:0000098": "Tall stature",
         "HP:0001548": "Overgrowth",
         "HP:0001519": "Disproportionate tall stature",
         "HP:0003502": "Advanced ossification / accelerated skeletal maturation"}
for r in list(ROOTS):
    if r not in terms: print(f"  NOTE {r} absent from this hp.obo release"); ROOTS.pop(r)

sets = {r: descendants(r) for r in ROOTS}
allterms = set().union(*sets.values())
print(f"{len(ROOTS)} roots -> {len(allterms)} HPO terms in the tall/overgrowth cone")
for r, n in ROOTS.items(): print(f"   {r} {n:<50} {len(sets[r])} terms")

# --- gene annotations ------------------------------------------------------------
rows = collections.defaultdict(lambda: collections.defaultdict(set))
hdr = None
with open("hpo/phenotype_to_genes.txt", encoding="utf-8") as f:
    for line in f:
        if line.startswith("#"): continue
        p = line.rstrip("\n").split("\t")
        if hdr is None and p[0] == "hpo_id": hdr = p; continue
        if hdr is None: hdr = ["hpo_id","hpo_name","ncbi_gene_id","gene_symbol","disease_id"]
        d = dict(zip(hdr, p))
        hid = d.get("hpo_id")
        if hid in allterms:
            rows[d.get("gene_symbol")][hid].add(d.get("disease_id",""))
print(f"\n{len(rows)} distinct genes annotated anywhere in the tall/overgrowth cone")

# rank: how many distinct tall-stature terms, and is the gene annotated to TALL STATURE itself
tall = sets.get("HP:0000098", set())
recs = []
for g, hm in rows.items():
    if not g: continue
    dis = set().union(*hm.values())
    recs.append(dict(gene=g, n_terms=len(hm), n_diseases=len(dis),
                     core_tall=bool(set(hm) & tall),
                     terms=sorted(terms[h]["name"] for h in hm if h in terms)[:6],
                     diseases=sorted(x for x in dis if x)[:5]))
recs.sort(key=lambda r: (-r["core_tall"], -r["n_terms"], r["gene"]))
core = [r for r in recs if r["core_tall"]]
print(f"{len(core)} genes annotated under TALL STATURE (HP:0000098) specifically\n")
with open("hpo_tall_genes.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["gene","core_tall","n_terms","n_diseases","terms","diseases"])
    for r in recs:
        w.writerow([r["gene"], r["core_tall"], r["n_terms"], r["n_diseases"],
                    "; ".join(r["terms"]), "; ".join(r["diseases"])])
print("TOP 40 by breadth of tall/overgrowth annotation:")
for r in recs[:40]:
    print(f"  {r['gene']:<12} terms={r['n_terms']:<3} dis={r['n_diseases']:<3} "
          f"{'CORE-TALL' if r['core_tall'] else '         '}  {'; '.join(r['terms'][:3])[:88]}")
json.dump(recs, open("hpo_tall_genes.json","w"), indent=1)
