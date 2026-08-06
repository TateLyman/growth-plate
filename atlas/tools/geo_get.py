"""Download the GEO series that carry an age, a species that CLOSES, or a human plate.
Series matrix + full supplementary FILE LIST (not the files - list first, then choose)."""
import os, sys, json, time, urllib.request, gzip, io

TARGETS = {
 # human, ages the atlas does not hold
 "GSE18338":  "human growth plate PRE-puberty / early puberty / late puberty, one patient",
 "GSE246390": "human growth plate cartilage, biomechanical loading, children, n=19",
 "GSE107649": "genes uniquely expressed in human growth plate chondrocytes",
 "GSE17368":  "human epiphyseal cartilage, 9 samples",
 "GSE267139": "human cartilage development at single cell resolution, fetal, n=25",
 "GSE209948": "early human knee joint development scRNAseq",
 "GSE6565":   "fetal cartilage selective genes, genome-scale",
 "GSE40942":  "fetal MSC toward chondrocyte vs human growth plate cartilage",
 "GSE233188": "IN VIVO CLONAL TRACKING of human skeletal stem cells, scRNA readout",
 # species whose plate CLOSES
 "GSE16981":  "RAT spatial AND TEMPORAL gene expression in mammalian growth plate (senescence)",
 "GSE114919": "RAT+MOUSE differential ageing of growth plate determines skeletal proportions",
 "GSE54216":  "RAT articular vs growth plate zones, 10-day proximal tibia",
}
FTP = "https://ftp.ncbi.nlm.nih.gov/geo/series/{stub}/{acc}/"

def fetch(url, dest=None, timeout=180):
    for a in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "growth-plate-atlas/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            if dest:
                open(dest, "wb").write(data); return len(data)
            return data
        except Exception as e:
            if a == 3: raise
            time.sleep(2 ** a)

log = {}
for acc, why in TARGETS.items():
    stub = acc[:-3] + "nnn"
    d = f"geo/{acc}"; os.makedirs(d, exist_ok=True)
    rec = {"why": why, "matrix": None, "supp": [], "error": None}
    try:
        murl = FTP.format(stub=stub, acc=acc) + f"matrix/{acc}_series_matrix.txt.gz"
        n = fetch(murl, f"{d}/{acc}_series_matrix.txt.gz")
        rec["matrix"] = n
    except Exception as e:
        rec["error"] = f"matrix: {e}"
    try:
        idx = fetch(FTP.format(stub=stub, acc=acc) + "suppl/").decode("utf-8", "replace")
        import re
        rec["supp"] = [m for m in re.findall(r'href="([^"?][^"]*)"', idx) if not m.startswith("/")]
    except Exception as e:
        rec["supp"] = []
    log[acc] = rec
    print(f"{acc:<11} matrix={rec['matrix']} supp={len(rec['supp'])} {'ERR:'+rec['error'] if rec['error'] else ''}")
    for s in rec["supp"][:8]: print(f"              {s}")
json.dump(log, open("geo/manifest.json", "w"), indent=1)
