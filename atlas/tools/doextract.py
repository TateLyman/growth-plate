import json, tbifetch
B="https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90728001-GCST90729000"
ACC=["GCST90728584","GCST90728586","GCST90728587"]
W=150000
g=json.load(open("gene_coords_b38.json"))
for acc in ACC:
    names,lin,_=tbifetch.read_tbi(acc+".tbi")
    url=f"{B}/{acc}/harmonised/{acc}.h.tsv.gz"
    n=0
    with open(acc+".region.tsv","w") as out:
        for gene in sorted(g):
            c=g[gene]["chr"]; beg=max(1,g[gene]["start"]-W); end=g[gene]["end"]+W
            rows=tbifetch.region(url,lin,c,beg,end,span=3_000_000)
            last=int(rows[-1].split('\t')[1]) if rows else -1
            flag="OK " if last>=end-20000 else "SHORT"
            print(f"  {acc} {gene:8s} {c}:{beg}-{end}  n={len(rows):5d} last={last} {flag}",flush=True)
            for r in rows: out.write(gene+"\t"+r+"\n")
            n+=len(rows)
    print(f"{acc}: {n} rows",flush=True)
