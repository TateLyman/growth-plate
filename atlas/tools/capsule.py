import json, re, collections
SP = "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad"
dos = json.load(open(SP + "/dossier2.json"))

# ---- species: prefer the atlas's own species word already present, else dossier
SPEC_ORDER = ["human", "mouse", "rat", "rabbit", "chick", "bovine", "pig", "sheep", "zebrafish"]


def species_of(d):
    sp = d.get("species") or {}
    if not sp:
        return []
    mx = max(sp.values())
    keep = [s for s in SPEC_ORDER if sp.get(s, 0) >= max(3, 0.25 * mx)]
    return keep[:3]


# ---- stage
def stage_from(d, spec):
    """Return (literal_phrase, vocab_words[]) determined from source, or (None,None)."""
    lits, vocab = [], []
    toks = d.get("age_tokens") or []
    E = sorted({float(t[1:]) for t in toks if t.startswith("E")})
    P = sorted({int(t[1:]) for t in toks if t.startswith("P") and t[1:].isdigit()})
    if E:
        lits.append("E%g-E%g" % (E[0], E[-1]) if len(E) > 1 else "E%g" % E[0])
        vocab.append("fetal")
    if P:
        lits.append("P%d-P%d" % (P[0], P[-1]) if len(P) > 1 else "P%d" % P[0])
        if P[0] <= 7:
            vocab.append("neonatal")
        if any(8 <= x <= 28 for x in P):
            vocab.append("juvenile")
        if any(x > 28 for x in P):
            vocab.append("adult")
    raws = d.get("age_num_raw") or []
    human = "human" in spec
    wk, mo, yr, dy = [], [], [], []
    for s in raws:
        m = re.match(r"(\d+(?:\.\d+)?)", s.strip())
        if not m:
            continue
        v = float(m.group(1))
        u = s.lower()
        (dy if "day" in u else wk if "week" in u else mo if "month" in u else yr).append(v)
    if raws:
        lits.append("; ".join(sorted(set(raws))[:4]))
    if not human:
        # rodent mapping
        if dy:
            if min(dy) <= 7:
                vocab.append("neonatal")
            if any(8 <= x <= 28 for x in dy):
                vocab.append("juvenile")
            if any(x > 28 for x in dy):
                vocab.append("adult")
        if wk:
            if min(wk) <= 3:
                vocab.append("juvenile")
            if any(4 <= x <= 7 for x in wk):
                vocab.append("peripubertal")
            if any(x >= 8 for x in wk):
                vocab.append("adult")
        if mo or yr:
            vocab.append("adult")
    else:
        if yr:
            if min(yr) < 2:
                vocab.append("infant")
            if any(2 <= x < 10 for x in yr):
                vocab.append("childhood")
            if any(10 <= x < 18 for x in yr):
                vocab.append("pubertal")
            if any(x >= 18 for x in yr):
                vocab.append("adult")
        if mo:
            vocab.append("infant" if min(mo) < 24 else "childhood")
        if wk and not yr and not mo:
            vocab.append("infant")
    for m in (d.get("age_mean") or []):
        v, u = float(m[0]), m[1].lower()
        lits.append("mean age %g %s" % (v, u))
        if u.startswith("year"):
            vocab.append("infant" if v < 2 else "childhood" if v < 10 else "pubertal" if v < 18 else "adult")
        else:
            vocab.append("infant")
    aw = d.get("age_words") or {}
    mxw = max(aw.values()) if aw else 0
    for k, n in aw.items():
        if n >= max(2, 0.2 * mxw):
            vocab.append({"fetal": "fetal", "neonatal": "neonatal", "child": "childhood",
                          "pubertal": "pubertal", "adult": "adult"}[k])
    # de-dup preserving order
    seen, vv = set(), []
    for v in vocab:
        if v not in seen:
            seen.add(v); vv.append(v)
    return ("; ".join(lits) if lits else None), vv


ZTXT = {"resting": "resting zone", "proliferative": "proliferative zone",
        "prehypertrophic": "prehypertrophic zone", "hypertrophic": "hypertrophic zone",
        "perichondrium": "perichondrium"}

caps = {}
for rid, d in dos.items():
    spec = species_of(d)
    lit, vocab = stage_from(d, spec)
    z = d.get("zone") or {}
    zmax = max(z.values()) if z else 0
    zones = [k for k, v in z.items() if v >= 3 and v >= 0.15 * zmax]
    caps[rid] = {"species": spec, "sex": d["sex"], "stage_lit": lit, "stage_vocab": vocab,
                 "zones": zones, "zone_counts": z, "src": d["src"], "type": d.get("type"),
                 "title": d["title"], "one_line": d["one_line"]}
json.dump(caps, open(SP + "/capsules.json", "w"), indent=0)
print("caps", len(caps))
print("with species", sum(1 for c in caps.values() if c["species"]))
print("with sex", sum(1 for c in caps.values() if c["sex"]))
print("with stage vocab", sum(1 for c in caps.values() if c["stage_vocab"]))
print("with zones", sum(1 for c in caps.values() if c["zones"]))
