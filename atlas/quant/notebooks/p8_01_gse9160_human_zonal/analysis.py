#!/usr/bin/env python3
"""
P8-01 - re-analysis of GSE9160, the only public zone-resolved transcriptome of a
human growth plate.

Executes PREREGISTRATION.md exactly. Read that file first; every rule applied here
was fixed before any gene of interest was looked up.

Inputs are fetched from the live GEO record, not vendored, so the analysis is
reproducible from this file alone:
  - GSE9160 series matrix (10 arrays: 5 compartments x 2 donors)
  - GPL570 platform table, for probe set -> gene symbol

Usage:
  python3 analysis.py --fetch       # download inputs into ./_data (about 80 MB, deleted after parse)
  python3 analysis.py               # run, writing results/
"""
import os, sys, json, re, csv, gzip, argparse, urllib.request, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "_data")
RES = os.path.join(HERE, "results")

SERIES_URL = ("https://ftp.ncbi.nlm.nih.gov/geo/series/GSE9nnn/GSE9160/matrix/"
              "GSE9160_series_matrix.txt.gz")
PLATFORM_URL = ("https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?"
                "acc=GPL570&targ=self&form=text&view=data")

# Sample order in the series matrix, from the GEO record's own Sample_title line.
# Donor 1 = Caucasian female 11y10m; donor 2 = Caucasian male 13y3m.
SAMPLES = [
    ("GSM231426", 1, "HZ"), ("GSM231427", 1, "PHZ"), ("GSM231428", 1, "PZ"),
    ("GSM231429", 1, "RZ"), ("GSM231430", 1, "PC"),
    ("GSM231431", 2, "HZ"), ("GSM231432", 2, "PHZ"), ("GSM231433", 2, "PZ"),
    ("GSM231434", 2, "RZ"), ("GSM231435", 2, "PC"),
]
# The zonal axis. Perichondrium is a separate compartment and is deliberately not
# a point on it (PREREGISTRATION 3.2).
AXIS = ["RZ", "PZ", "PHZ", "HZ"]
ADJACENT = {(AXIS[i], AXIS[j]) for i in range(4) for j in range(4) if abs(i - j) <= 1}

# Authors' own present-calls, from the GEO record. The preregistered positive
# control for the background rule (PREREGISTRATION 3.1).
AUTHOR_PRESENT = {1: 12193, 2: 18454}

OR_NULL_RE = re.compile(r"OR\d+[A-Z]\d*[A-Z]?$")
NULL_PCTILE = 0.95

# ---------------------------------------------------------------- locked gene list
# PREREGISTRATION section 4. Fixed before execution. Do not extend this list; a gene
# added after seeing results is post hoc and must be recorded as such in RESULTS.md.
GROUP_A = {
    "g_l3core_006": ["PDE1A", "PDE1B", "PDE1C", "PDE2A", "PDE3A", "PDE3B",
                     "PDE4A", "PDE4B", "PDE4C", "PDE4D", "PDE5A", "PDE7A",
                     "PDE7B", "PDE8A", "PDE8B", "PDE9A", "PDE10A", "PDE11A"],
    "g_l4endo_003": ["NR3C1", "NR3C2", "HSD11B1", "HSD11B2"],
    "g_l4endo_009": ["IGFBP1", "IGFBP2", "IGFBP3", "IGFBP4", "IGFBP5", "IGFBP6",
                     "IGFBP7", "IGF1", "IGF2", "IGF1R", "IGF2R", "PAPPA",
                     "PAPPA2", "STC1", "STC2"],
    "g_l3rest_007": ["SOST", "DKK1", "DKK2", "SFRP1", "SFRP2", "SFRP4", "FRZB",
                     "WIF1", "LRP5", "LRP6"],
    "g_l3rest_009": ["NOTCH1", "NOTCH2", "NOTCH3", "NOTCH4", "JAG1", "JAG2",
                     "DLL1", "DLL3", "DLL4", "HES1", "HES5", "HEY1", "HEY2",
                     "RBPJ", "PSEN1"],
    "g_l6mech_007": ["PIEZO1", "PIEZO2", "TRPV4"],
    "g_l11path_023": ["SLC16A2", "SLC16A10", "SLCO1C1", "SLC7A5", "SLC7A8",
                      "DIO1", "DIO2", "DIO3", "THRA", "THRB"],
}
# SFRP3 is FRZB; the platform annotates it as FRZB, so that is the symbol queried.

GROUP_B = {
    "PRKG1_vs_PRKG2": ["PRKG1", "PRKG2"],
    "ANKH_vs_ENPP1": ["ANKH", "ENPP1", "ENPP2", "ENPP3", "ALPL", "PHOSPHO1"],
    "IGF1R_vs_INSR": ["IGF1R", "INSR", "IRS1", "IRS2"],
    "FGFR_family": ["FGFR1", "FGFR2", "FGFR3", "FGFR4", "FGF2", "FGF9", "FGF18"],
    "NPR_family": ["NPR1", "NPR2", "NPR3", "NPPB", "NPPC"],
    "steroid_receptors": ["ESR1", "ESR2", "GPER1", "AR", "CYP19A1"],
    "PTH_IHH_axis": ["PTH1R", "PTH2R", "PTHLH", "IHH", "GLI1", "GLI2", "GLI3",
                     "PTCH1", "SMO"],
    "SOX_trio": ["SOX5", "SOX6", "SOX9"],
}
# GPER1 was called GPR30 when this platform was designed; both symbols are accepted.
SYMBOL_ALIASES = {"GPER1": {"GPER1", "GPER", "GPR30", "CMKRL2"},
                  "ANKH": {"ANKH", "ANK"},
                  "PHOSPHO1": {"PHOSPHO1"},
                  "FRZB": {"FRZB", "SFRP3"},
                  "SLCO1C1": {"SLCO1C1", "SLC21A14", "OATP1C1"},
                  "PIEZO1": {"PIEZO1", "FAM38A"},
                  "PIEZO2": {"PIEZO2", "FAM38B"}}


def fetch():
    os.makedirs(DATA, exist_ok=True)
    sm = os.path.join(DATA, "GSE9160_series_matrix.txt")
    if not os.path.exists(sm):
        print("fetching series matrix ...")
        raw = os.path.join(DATA, "sm.gz")
        urllib.request.urlretrieve(SERIES_URL, raw)
        with gzip.open(raw) as f, open(sm, "wb") as o:
            o.write(f.read())
        os.remove(raw)
    p2g = os.path.join(DATA, "probe2gene.json")
    if not os.path.exists(p2g):
        print("fetching GPL570 platform table (about 80 MB) ...")
        tmp = os.path.join(DATA, "gpl570.txt")
        urllib.request.urlretrieve(PLATFORM_URL, tmp)
        m = {}
        with open(tmp, errors="replace") as f:
            for line in f:
                if line.startswith("!platform_table_begin"):
                    break
            hdr = next(f).rstrip("\n").split("\t")
            i_id, i_sym = hdr.index("ID"), hdr.index("Gene Symbol")
            for line in f:
                if line.startswith("!platform_table_end"):
                    break
                p = line.rstrip("\n").split("\t")
                if len(p) > i_sym:
                    m[p[i_id]] = p[i_sym]
        json.dump(m, open(p2g, "w"))
        os.remove(tmp)          # 80 MB is not committed and not kept
    print("inputs ready in", DATA)


def load():
    sm = os.path.join(DATA, "GSE9160_series_matrix.txt")
    p2g = os.path.join(DATA, "probe2gene.json")
    if not (os.path.exists(sm) and os.path.exists(p2g)):
        sys.exit("inputs missing - run: python3 analysis.py --fetch")
    probe2gene = json.load(open(p2g))
    f = open(sm, errors="replace")
    for line in f:
        if line.startswith("!series_matrix_table_begin"):
            break
    hdr = next(f).rstrip("\n").replace('"', "").split("\t")
    order = [hdr.index(g) - 1 for g, _, _ in SAMPLES]
    X = {}
    for line in f:
        if line.startswith("!series_matrix_table_end"):
            break
        p = line.rstrip("\n").replace('"', "").split("\t")
        try:
            vals = [float(x) for x in p[1:]]
        except ValueError:
            continue
        X[p[0]] = [vals[i] for i in order]      # reordered to SAMPLES
    return X, probe2gene


def background(X, probe2gene):
    """Per-array background from olfactory-receptor probe sets. PREREG 3.1."""
    null_probes = [p for p, s in probe2gene.items()
                   if OR_NULL_RE.fullmatch(s or "") and p in X]
    thr = []
    for i in range(len(SAMPLES)):
        v = sorted(X[p][i] for p in null_probes)
        thr.append(v[int(NULL_PCTILE * len(v))])
    return null_probes, thr


def sym_index(probe2gene, wanted):
    """symbol -> [probe sets], honouring the alias table."""
    want = {}
    for s in wanted:
        for a in SYMBOL_ALIASES.get(s, {s}):
            want[a.upper()] = s
    out = {s: [] for s in wanted}
    for p, raw in probe2gene.items():
        for tok in str(raw or "").replace("///", "/").split("/"):
            tok = tok.strip().upper()
            if tok in want:
                out[want[tok]].append(p)
                break
    return {k: sorted(set(v)) for k, v in out.items()}


def profile(X, probe, donor):
    """rel(zone) for one probe set in one donor. PREREG 3.2."""
    idx = {z: i for i, (_, d, z) in enumerate(SAMPLES) if d == donor}
    vals = {z: X[probe][idx[z]] for z in idx}
    mean = statistics.fmean(vals.values())
    return vals, {z: (v / mean if mean else 0.0) for z, v in vals.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    a = ap.parse_args()
    if a.fetch:
        return fetch()
    os.makedirs(RES, exist_ok=True)
    X, probe2gene = load()
    null_probes, thr = background(X, probe2gene)

    # ---- preregistered positive control on the background rule ----------------
    ctrl_rows, above = [], {1: [], 2: []}
    for i, (gsm, donor, zone) in enumerate(SAMPLES):
        n = sum(1 for p in X if X[p][i] > thr[i])
        above[donor].append(n)
        ctrl_rows.append({"gsm": gsm, "donor": donor, "compartment": zone,
                          "or_null_p95": round(thr[i], 1),
                          "probesets_above_background": n,
                          "fraction_of_array": round(n / len(X), 4)})
    control = {
        "authors_present_calls": AUTHOR_PRESENT,
        "or_null_probesets": len(null_probes),
        "donor1_range": [min(above[1]), max(above[1])],
        "donor2_range": [min(above[2]), max(above[2])],
        "donor1_median": int(statistics.median(above[1])),
        "donor2_median": int(statistics.median(above[2])),
    }
    d1, d2 = control["donor1_median"], control["donor2_median"]
    control["reproduces_donor_asymmetry"] = bool(
        (d2 > d1) == (AUTHOR_PRESENT[2] > AUTHOR_PRESENT[1]))
    control["donor1_ratio_to_authors"] = round(d1 / AUTHOR_PRESENT[1], 2)
    control["donor2_ratio_to_authors"] = round(d2 / AUTHOR_PRESENT[2], 2)
    control["verdict"] = ("PASS" if control["reproduces_donor_asymmetry"]
                          and 0.5 <= control["donor1_ratio_to_authors"] <= 2.0
                          and 0.5 <= control["donor2_ratio_to_authors"] <= 2.0
                          else "FAIL - background rule abandoned, see RESULTS.md")
    json.dump(control, open(os.path.join(RES, "background_control.json"), "w"),
              indent=1)
    with open(os.path.join(RES, "array_background.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(ctrl_rows[0]))
        w.writeheader()
        w.writerows(ctrl_rows)
    print("background control:", control["verdict"],
          f"(donor1 {d1} vs authors {AUTHOR_PRESENT[1]}; "
          f"donor2 {d2} vs authors {AUTHOR_PRESENT[2]})")

    # ---- the locked gene list --------------------------------------------------
    groups = [("A:" + k, v) for k, v in GROUP_A.items()] + \
             [("B:" + k, v) for k, v in GROUP_B.items()]
    wanted = sorted({g for _, gs in groups for g in gs})
    idx = sym_index(probe2gene, wanted)

    rows, missing = [], []
    for gname, genes in groups:
        for g in genes:
            probes = idx.get(g) or []
            if not probes:
                missing.append((gname, g))
                continue
            for p in probes:
                if p not in X:
                    continue
                rec = {"group": gname, "gene": g, "probe_set": p}
                det_any = {}
                for donor in (1, 2):
                    vals, rel = profile(X, p, donor)
                    for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]:
                        i = [k for k, (_, d, zz) in enumerate(SAMPLES)
                             if d == donor and zz == z][0]
                        rec[f"d{donor}_{z}"] = round(vals[z], 1)
                        rec[f"d{donor}_{z}_rel"] = round(rel[z], 3)
                        det = vals[z] > thr[i]
                        rec[f"d{donor}_{z}_det"] = int(det)
                        det_any.setdefault(z, []).append(det)
                    axis_rel = {z: rel[z] for z in AXIS}
                    rec[f"d{donor}_max_zone"] = max(axis_rel, key=axis_rel.get)
                    rec[f"d{donor}_fold_range"] = round(
                        max(axis_rel.values()) / max(1e-9, min(axis_rel.values())), 2)
                m1, m2 = rec["d1_max_zone"], rec["d2_max_zone"]
                rec["concordant_max_zone"] = int((m1, m2) in ADJACENT)
                rec["same_max_zone"] = int(m1 == m2)
                # detection verdict per compartment: both donors required
                for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]:
                    both = det_any[z]
                    rec[f"{z}_verdict"] = ("detected" if all(both)
                                           else "one_donor_only" if any(both)
                                           else "not_detected")
                rec["detected_any_compartment"] = int(any(
                    rec[f"{z}_verdict"] == "detected"
                    for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]))
                rows.append(rec)

    fields = list(rows[0].keys())
    with open(os.path.join(RES, "zonal_profiles.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # ---- gene-level roll-up ----------------------------------------------------
    genes = {}
    for r in rows:
        k = (r["group"], r["gene"])
        genes.setdefault(k, []).append(r)
    summary = []
    for (grp, g), rs in sorted(genes.items()):
        det = [r for r in rs if r["detected_any_compartment"]]
        best = max(rs, key=lambda r: max(r[f"d{d}_{z}"] for d in (1, 2)
                                         for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]))
        summary.append({
            "group": grp, "gene": g, "n_probe_sets": len(rs),
            "n_probe_sets_detected": len(det),
            "gene_detected": int(bool(det)),
            "compartments_detected": ";".join(
                z for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]
                if any(r[f"{z}_verdict"] == "detected" for r in rs)) or "none",
            "one_donor_only": ";".join(
                z for z in ["RZ", "PZ", "PHZ", "HZ", "PC"]
                if not any(r[f"{z}_verdict"] == "detected" for r in rs)
                and any(r[f"{z}_verdict"] == "one_donor_only" for r in rs)) or "",
            "representative_probe": best["probe_set"],
            "d1_max_zone": best["d1_max_zone"], "d2_max_zone": best["d2_max_zone"],
            "concordant": best["concordant_max_zone"],
            "d1_fold_range": best["d1_fold_range"],
            "d2_fold_range": best["d2_fold_range"],
            "probe_sets_disagree_on_detection": int(
                0 < len(det) < len(rs)),
        })
    with open(os.path.join(RES, "gene_summary.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary[0]))
        w.writeheader()
        w.writerows(summary)

    with open(os.path.join(RES, "not_on_platform.txt"), "w") as fh:
        for grp, g in missing:
            fh.write(f"{grp}\t{g}\n")

    print(f"probe sets analysed : {len(rows)}")
    print(f"genes in locked list: {len(wanted)}  "
          f"detected: {sum(s['gene_detected'] for s in summary)}  "
          f"not on platform: {len(missing)}")
    print("results/ written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
