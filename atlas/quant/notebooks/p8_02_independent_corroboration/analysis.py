#!/usr/bin/env python3
"""
P8-02 — do the four P8-01 negatives survive independent donors and platforms?

Executes PREREGISTRATION.md exactly. Read that first.

Inputs are fetched live from GEO, not vendored:
  GSE22855  Illumina HumanWG-6 v3   (GPL6884)  2 growth-plate arrays
  GSE32398  Affymetrix              (GPL9828)  5 growth-plate arrays
  GSE18338  Agilent                 (GPL9324)  6 arrays, ONE donor across puberty

Usage:
  python3 analysis.py --fetch
  python3 analysis.py
"""
import os, sys, re, json, csv, gzip, argparse, urllib.request, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "_data")
RES = os.path.join(HERE, "results")

SERIES = {
    "GSE22855": {"platform": "GPL6884", "family": "Illumina HumanWG-6 v3",
                 "gp_match": r"growth plate"},
    "GSE32398": {"platform": "GPL9828", "family": "Affymetrix GPL9828",
                 "gp_match": r"growth plate"},
    "GSE18338": {"platform": "GPL9324", "family": "Agilent GPL9324",
                 "gp_match": r"growth plate|epiphyseal"},
}
# GSE18338 is ONE donor across six arrays (PREREGISTRATION 3).
DONORS = {"GSE22855": 2, "GSE32398": 5, "GSE18338": 1}

OR_RE = re.compile(r"OR\d+[A-Z]\d*[A-Z]?$")
NULL_PCTILE = 0.95
MIN_OR_PROBES = 20                      # PREREGISTRATION 4.1 fallback rule

GATE = ["COL2A1", "ACAN"]               # 4.2 - a dataset must pass this to testify
SECONDARY = ["COL10A1", "SOX9", "IHH"]

CLAIMS = {
    "N1_NPPC": {
        "negative": ["NPPC"],
        "controls": ["NPR2", "NPR3"]},
    "N2_cGMP_PDE": {
        "negative": ["PDE1A", "PDE1B", "PDE1C", "PDE2A", "PDE3A", "PDE3B",
                     "PDE5A", "PDE9A", "PDE10A", "PDE11A"],
        "controls": ["PDE4A", "PDE4B", "PDE4C"]},
    "N3_local_estrogen": {
        "negative": ["CYP19A1", "ESR2"],
        "controls": ["ESR1"]},
    "N4_TH_transport": {
        "negative": ["SLC16A2", "SLC16A10", "SLCO1C1"],
        "controls": ["THRA", "THRB", "DIO2", "SLC7A5"]},
}
ALIASES = {"SLCO1C1": {"SLCO1C1", "SLC21A14", "OATP1C1"},
           "ACAN": {"ACAN", "AGC1", "CSPG1"},
           "NPPC": {"NPPC", "CNP"},
           "PDE5A": {"PDE5A", "PDE5"},
           "SLC16A2": {"SLC16A2", "MCT8", "XPCT"}}


def fetch():
    os.makedirs(DATA, exist_ok=True)
    for gse, meta in SERIES.items():
        p = os.path.join(DATA, f"{gse}.txt")
        if not os.path.exists(p):
            n = gse[:-3] + "nnn"
            url = (f"https://ftp.ncbi.nlm.nih.gov/geo/series/{n}/{gse}/matrix/"
                   f"{gse}_series_matrix.txt.gz")
            print("fetching", gse, "...")
            raw = p + ".gz"
            urllib.request.urlretrieve(url, raw)
            with gzip.open(raw) as f, open(p, "wb") as o:
                o.write(f.read())
            os.remove(raw)
        gpl = meta["platform"]
        pp = os.path.join(DATA, f"{gpl}.json")
        if not os.path.exists(pp):
            print("fetching platform", gpl, "...")
            tmp = os.path.join(DATA, gpl + ".txt")
            urllib.request.urlretrieve(
                "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?"
                f"acc={gpl}&targ=self&form=text&view=data", tmp)
            m = {}
            with open(tmp, errors="replace") as f:
                for line in f:
                    if line.startswith("!platform_table_begin"):
                        break
                hdr = next(f).rstrip("\n").split("\t")
                # platforms name the symbol column differently
                # Prefer a real symbol column; fall back to an Entrez id column and
                # resolve it through the GPL570 symbol<->Entrez table (below).
                # GPL9828 carries only ENTREZ_GENE_ID; GPL9324 carries ORF + EntrezID.
                pref = ["gene symbol", "symbol", "orf", "gene_symbol", "genesymbol",
                        "ilmn_gene", "gene", "genename"]
                low = [c.strip().lower() for c in hdr]
                cand = [hdr[low.index(x)] for x in pref if x in low]
                i_id = 0
                i_sym = hdr.index(cand[0]) if cand else None
                ez = [c for c in hdr
                      if c.strip().lower() in ("entrez_gene_id", "entrezid",
                                               "entrez_gene", "gene_id")]
                i_ez = hdr.index(ez[0]) if ez else None
                for line in f:
                    if line.startswith("!platform_table_end"):
                        break
                    p2 = line.rstrip("\n").split("\t")
                    if i_sym is not None and len(p2) > i_sym and p2[i_sym].strip():
                        m[p2[i_id]] = p2[i_sym]
                    elif i_ez is not None and len(p2) > i_ez and p2[i_ez].strip():
                        m[p2[i_id]] = "ENTREZ:" + p2[i_ez].split("///")[0].strip()
            json.dump({"header": hdr, "map": m}, open(pp, "w"))
            os.remove(tmp)
            if any(str(v).startswith("ENTREZ:") for v in m.values()):
                e2s = entrez_to_symbol()
                m = {k: (e2s.get(v[7:], v) if str(v).startswith("ENTREZ:") else v)
                     for k, v in m.items()}
                json.dump({"header": hdr, "map": m, "resolved_via": "GPL570"},
                          open(pp, "w"))
                print(f"  {gpl}: Entrez ids resolved to symbols via GPL570")
            print(f"  {gpl}: {len(m)} probes, symbol column "
                  f"{cand[0] if cand else 'NOT FOUND'}")
    print("inputs ready")


def entrez_to_symbol():
    """GPL570 carries BOTH Gene Symbol and ENTREZ_GENE_ID, so it is a symbol<->Entrez
    table this project has already validated. Platforms annotated only with Entrez ids
    (GPL9828) are resolved through it rather than through a hand-typed mapping."""
    cache = os.path.join(DATA, "entrez2symbol.json")
    if os.path.exists(cache):
        return json.load(open(cache))
    print("  building Entrez->symbol map from GPL570 (about 80 MB, deleted after) ...")
    tmp = os.path.join(DATA, "gpl570.txt")
    urllib.request.urlretrieve(
        "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?"
        "acc=GPL570&targ=self&form=text&view=data", tmp)
    out = {}
    with open(tmp, errors="replace") as f:
        for line in f:
            if line.startswith("!platform_table_begin"):
                break
        hdr = next(f).rstrip("\n").split("\t")
        i_s, i_e = hdr.index("Gene Symbol"), hdr.index("ENTREZ_GENE_ID")
        for line in f:
            if line.startswith("!platform_table_end"):
                break
            p = line.rstrip("\n").split("\t")
            if len(p) > max(i_s, i_e):
                for e in str(p[i_e]).split("///"):
                    e = e.strip()
                    if e and p[i_s].strip():
                        out.setdefault(e, p[i_s].split("///")[0].strip())
    os.remove(tmp)
    json.dump(out, open(cache, "w"))
    print(f"  {len(out)} Entrez ids mapped")
    return out


def load_series(gse):
    p = os.path.join(DATA, f"{gse}.txt")
    f = open(p, errors="replace")
    titles = srcs = chars = None
    for line in f:
        if line.startswith("!Sample_title"):
            titles = line.rstrip("\n").replace('"', "").split("\t")[1:]
        elif line.startswith("!Sample_source_name_ch1"):
            srcs = line.rstrip("\n").replace('"', "").split("\t")[1:]
        elif line.startswith("!Sample_characteristics_ch1") and chars is None:
            chars = line.rstrip("\n").replace('"', "").split("\t")[1:]
        elif line.startswith("!series_matrix_table_begin"):
            break
    hdr = next(f).rstrip("\n").replace('"', "").split("\t")
    X = {}
    for line in f:
        if line.startswith("!series_matrix_table_end"):
            break
        p2 = line.rstrip("\n").replace('"', "").split("\t")
        vals = []
        for v in p2[1:]:
            try:
                vals.append(float(v))
            except ValueError:
                vals.append(None)
        X[p2[0]] = vals
    lab = [f"{a} | {b}" for a, b in zip(titles or [], srcs or [])]
    return hdr[1:], lab, X


def sym_index(pmap, wanted):
    want = {}
    for s in wanted:
        for a in ALIASES.get(s, {s}):
            want[a.upper()] = s
    out = {s: [] for s in wanted}
    for probe, raw in pmap.items():
        for tok in re.split(r"[/;,|]+", str(raw or "")):
            tok = tok.strip().upper()
            if tok in want:
                out[want[tok]].append(probe)
                break
    return {k: sorted(set(v)) for k, v in out.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    a = ap.parse_args()
    if a.fetch:
        return fetch()
    os.makedirs(RES, exist_ok=True)

    all_genes = sorted({g for c in CLAIMS.values()
                        for g in c["negative"] + c["controls"]} |
                       set(GATE) | set(SECONDARY))
    per_dataset, rows = {}, []

    for gse, meta in SERIES.items():
        pmap = json.load(open(os.path.join(DATA, meta["platform"] + ".json")))["map"]
        gsms, labels, X = load_series(gse)
        gp = [i for i, l in enumerate(labels)
              if re.search(meta["gp_match"], l, re.I)]
        # background
        orp = [p for p, s in pmap.items() if OR_RE.fullmatch(str(s or "")) and p in X]
        info = {"platform": meta["family"], "arrays_total": len(gsms),
                "growth_plate_arrays": len(gp),
                "growth_plate_labels": [labels[i] for i in gp],
                "donors": DONORS[gse], "or_probes": len(orp)}
        if len(orp) < MIN_OR_PROBES:
            info["status"] = "DROPPED_no_estimable_background"
            info["note"] = (f"only {len(orp)} olfactory-receptor probes on "
                            f"{meta['platform']}; the empirical null is not estimable "
                            f"and PREREGISTRATION 4.1 forbids substituting an arbitrary "
                            f"percentile cut")
            per_dataset[gse] = info
            print(f"{gse}: DROPPED - {len(orp)} OR probes")
            continue
        thr = {}
        for i in gp:
            v = sorted(x for p in orp if (x := X[p][i]) is not None)
            thr[i] = v[int(NULL_PCTILE * len(v))] if v else None
        info["thresholds"] = {labels[i]: round(thr[i], 2) for i in gp if thr[i]}

        idx = sym_index(pmap, all_genes)

        def detect(gene):
            probes = [p for p in idx.get(gene, []) if p in X]
            if not probes:
                return "NO_PROBE", 0, []
            hits = []
            for i in gp:
                if thr[i] is None:
                    continue
                best = max((X[p][i] for p in probes if X[p][i] is not None),
                           default=None)
                hits.append(bool(best is not None and best > thr[i]))
            n_det = sum(hits)
            verdict = ("DETECTED" if n_det > len(hits) / 2 else "NOT_DETECTED")
            return verdict, n_det, probes

        gate_ok = True
        for g in GATE:
            v, n, _ = detect(g)
            info.setdefault("gate", {})[g] = f"{v} ({n}/{len(gp)})"
            if v != "DETECTED":
                gate_ok = False
        info["status"] = "USED" if gate_ok else "DROPPED_failed_tissue_gate"
        for g in SECONDARY:
            v, n, _ = detect(g)
            info.setdefault("secondary", {})[g] = f"{v} ({n}/{len(gp)})"

        for g in all_genes:
            v, n, probes = detect(g)
            rows.append({"dataset": gse, "platform": meta["family"], "gene": g,
                         "verdict": v, "arrays_detected": n,
                         "arrays_total": len(gp), "n_probes": len(probes),
                         "dataset_status": info["status"]})
        per_dataset[gse] = info
        print(f"{gse}: {info['status']}  gp arrays {len(gp)}  OR probes {len(orp)}  "
              f"gate {info.get('gate')}")

    with open(os.path.join(RES, "detection_by_dataset.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

    # ---- claim-level verdicts, PREREGISTRATION 4.4 ---------------------------
    used = [g for g, i in per_dataset.items() if i["status"] == "USED"]
    verdicts = {}
    for cname, c in CLAIMS.items():
        ctrl_ok = {}
        for g in used:
            vs = [r for r in rows if r["dataset"] == g and r["gene"] in c["controls"]]
            avail = [r for r in vs if r["verdict"] != "NO_PROBE"]
            ctrl_ok[g] = bool(avail) and any(r["verdict"] == "DETECTED" for r in avail)
        per_gene = {}
        for neg in c["negative"]:
            calls = {}
            for g in used:
                if not ctrl_ok[g]:
                    calls[g] = "INCONCLUSIVE_controls_failed"; continue
                r = next(r for r in rows if r["dataset"] == g and r["gene"] == neg)
                calls[g] = r["verdict"]
            live = [v for v in calls.values() if v in ("DETECTED", "NOT_DETECTED")]
            if not live:
                verdict = "INCONCLUSIVE"
            elif "DETECTED" in live:
                verdict = ("REFUTED" if all(v == "DETECTED" for v in live)
                           else "PARTIALLY_CORROBORATED")
            else:
                verdict = "CORROBORATED"
            per_gene[neg] = {"verdict": verdict, "by_dataset": calls}
        vs = [v["verdict"] for v in per_gene.values()]
        claim_v = ("REFUTED" if "REFUTED" in vs else
                   "PARTIALLY_CORROBORATED" if "PARTIALLY_CORROBORATED" in vs else
                   "CORROBORATED" if all(v == "CORROBORATED" for v in vs) else
                   "MIXED")
        verdicts[cname] = {"claim_verdict": claim_v,
                           "controls_held": ctrl_ok, "genes": per_gene}

    json.dump({"datasets": per_dataset, "claims": verdicts},
              open(os.path.join(RES, "verdicts.json"), "w"), indent=1)

    print("\n===== CLAIM VERDICTS =====")
    for k, v in verdicts.items():
        print(f"\n{k}: {v['claim_verdict']}   controls held: {v['controls_held']}")
        for g, d in v["genes"].items():
            print(f"   {g:10s} {d['verdict']:26s} {d['by_dataset']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
