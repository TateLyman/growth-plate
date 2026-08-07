import json, sys, re
G = json.load(open('/home/user/growth-plate/query/gaps.json'))
gaps = G['gaps']
if isinstance(gaps, dict): gaps = list(gaps.values())
pat = re.compile('|'.join(sys.argv[1:]), re.I)
for g in gaps:
    blob = json.dumps(g)
    if pat.search(blob):
        print('*', g.get('gap_id'), '|', g.get('layer'), '|', g.get('type'))
        print('   Q:', (g.get('question') or '')[:230])
        print('   MISSING:', (g.get('what_is_missing') or '')[:200])
