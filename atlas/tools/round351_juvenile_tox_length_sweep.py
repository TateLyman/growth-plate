#!/usr/bin/env python3
"""
ROUND 351. THE JUVENILE-TOXICITY LENGTH SWEEP - CORR-350 EXECUTED.

R350 found the bone-length endpoint R348 declared absent "in any species" sitting inside an FDA
NONCLINICAL review: serial left-ulna length in Han Wistar rats dosed PND 7 to PND 62. ICH S11
juvenile toxicity studies routinely record serial LIMB LENGTH, body weight, sexual maturation and
skeletal histopathology in animals dosed through the ENTIRE growth period - which is precisely the
experiment this atlas repeatedly declares does not exist. These documents are free, public, and
invisible to PubMed and Europe PMC.

RETRIEVAL NOTE (this is why every previous attempt failed): accessdata.fda.gov serves default
clients an Akamai abuse page that presents as a 404. A browser User-Agent plus a Drugs@FDA Referer
gets the real file. And the review TOC year is NOT the approval year - Pradaxa was approved June
2021 and its reviews are filed under 2022 - so the year must be read from the openFDA
application_docs URL rather than guessed.
"""
import json, re, sys, time, urllib.request, urllib.parse, os

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
REF = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm"

def _get(url, binary=False, timeout=90):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Referer": REF,
        "Accept": "text/html,application/xhtml+xml,application/pdf,*/*",
        "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = r.read()
    return d if binary else d.decode("utf-8", "replace")

def review_years(appno):
    """Return candidate review-doc base URLs from openFDA application_docs."""
    u = ('https://api.fda.gov/drug/drugsfda.json?search=application_number:"%s"&limit=1'
         % appno)
    try:
        d = json.loads(_get(u))
    except Exception as e:
        return [], f"openFDA error: {e}"
    out = []
    for res in d.get("results", []):
        for s in res.get("submissions", []):
            for doc in (s.get("application_docs") or []):
                url = doc.get("url", "")
                m = re.search(r"/drugsatfda_docs/nda/(\d{4})/([A-Za-z0-9]+)(TOC\.html|\.pdf)", url)
                if m:
                    out.append((m.group(1), m.group(2).replace("TOC", "")))
    # dedupe preserving order
    seen, ded = set(), []
    for y, b in out:
        if (y, b) not in seen:
            seen.add((y, b)); ded.append((y, b))
    return ded, None

def fetch_pharmr(appno, outdir):
    cands, err = review_years(appno)
    if err:
        return None, err
    tried = []
    for year, base in cands:
        for suffix in ("PharmR", "MultidisciplineR", "IntegratedR", "SumR"):
            url = f"https://www.accessdata.fda.gov/drugsatfda_docs/nda/{year}/{base}{suffix}.pdf"
            tried.append(url)
            try:
                blob = _get(url, binary=True)
            except Exception:
                continue
            if blob[:4] == b"%PDF" and len(blob) > 50_000:
                path = os.path.join(outdir, f"{appno}_{base}{suffix}.pdf")
                open(path, "wb").write(blob)
                return path, url
            time.sleep(0.4)
    return None, "no review PDF found; tried %d URLs" % len(tried)

# The terms that matter. A juvenile tox study that measured a LENGTH will use one of these.
LENGTH_TERMS = [r"ulna length", r"limb measurement", r"femur length", r"femoral length",
                r"tibia length", r"tibial length", r"body length", r"crown[- ]rump",
                r"bone length", r"long bone"]
PLATE_TERMS  = [r"growth plate", r"physis", r"physeal", r"epiphys", r"hypertroph",
                r"chondrocyt", r"ossif", r"cartilage"]
CONTEXT_TERMS = [r"juvenile", r"neonatal tox", r"sexual maturation", r"body weight gain"]

def scan(pdf_path):
    from pypdf import PdfReader
    r = PdfReader(pdf_path)
    pages = [(p.extract_text() or "") for p in r.pages]
    t = "\n".join(pages)
    hits = {}
    for label, terms in (("LENGTH", LENGTH_TERMS), ("PLATE", PLATE_TERMS), ("CONTEXT", CONTEXT_TERMS)):
        hits[label] = {}
        for term in terms:
            n = len(re.findall(term, t, re.I))
            if n:
                hits[label][term] = n
    return t, hits, len(pages)

def excerpts(t, terms, before=500, after=1100, limit=3):
    out = []
    for term in terms:
        for i, m in enumerate(re.finditer(term, t, re.I)):
            if i >= limit:
                break
            s = max(0, m.start() - before); e = min(len(t), m.end() + after)
            out.append((term, re.sub(r"\s+", " ", t[s:e])))
    return out

if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(outdir, exist_ok=True)
    for appno in sys.argv[2:]:
        print(f"\n{'='*80}\n## {appno}")
        path, info = fetch_pharmr(appno, outdir)
        if not path:
            print("  NOT RETRIEVED:", info); continue
        print("  got:", path, "|", info)
        t, hits, npages = scan(path)
        print(f"  {npages} pages, {len(t)} chars")
        for k, v in hits.items():
            print(f"  {k}: {v}")
