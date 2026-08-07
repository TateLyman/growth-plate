import json, re, sys, yaml
SP = "/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad"
F = "/home/user/growth-plate/atlas/edges/edges.yaml"
new = json.load(open(SP + "/newctx.json"))
KEYS = {"edge_id", "source", "target", "relation", "sign", "magnitude", "context",
        "evidence_tier", "refs", "confidence", "gap_id", "notes", "superseded_by",
        "traversal_usable", "timescale", "sign_basis", "termination_reason",
        "relation_note", "quantitative", "mechanism"}
lines = open(F).read().split("\n")
out, i, cur, nrep = [], 0, None, 0
while i < len(lines):
    l = lines[i]
    m = re.match(r"- edge_id: (\S+)", l)
    if m:
        cur = m.group(1)
    if l.startswith("  context:") and cur in new:
        j = i + 1
        while j < len(lines):
            nx = lines[j]
            mm = re.match(r"  ([a-z_]+):", nx)
            if (mm and mm.group(1) in KEYS) or nx.startswith("- edge_id:"):
                break
            j += 1
        blob = yaml.safe_dump({"context": new[cur]}, default_flow_style=False,
                              width=110, allow_unicode=True, sort_keys=False)
        for bl in blob.rstrip("\n").split("\n"):
            out.append("  " + bl)
        nrep += 1
        i = j
        continue
    out.append(l)
    i += 1
open(F, "w").write("\n".join(out))
print("rewrote context on", nrep, "edges")
