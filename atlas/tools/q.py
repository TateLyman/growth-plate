#!/usr/bin/env python3
"""Query harness for the falsification run. Follows QUERY.md load order."""
import json, sys, re, os
from collections import defaultdict

Q = '/home/user/growth-plate/query'
D = json.load(open(Q + '/derived.json'))
G = json.load(open(Q + '/graph.json'))
NODES = G['nodes'] if isinstance(G['nodes'], dict) else {n['id']: n for n in G['nodes']}
for _k, _v in NODES.items(): _v.setdefault('id', _k)
EDGES = G['edges']
ALIAS = D['alias_to_id']
REACH = D['reachability']
OUT = defaultdict(list); IN = defaultdict(list)
for e in EDGES:
    OUT[e['source']].append(e); IN[e['target']].append(e)


def resolve(term):
    t = term.lower().strip()
    if t in ALIAS: return [ALIAS[t]]
    hits = set()
    for k, v in ALIAS.items():
        if t in k: hits.add(v)
    for nid, n in NODES.items():
        if t in nid.lower() or t in n['name'].lower(): hits.add(nid)
    return sorted(hits)


def grep(term):
    t = term.lower()
    out = []
    for nid, n in NODES.items():
        blob = (n['name'] + ' ' + (n.get('summary') or '') + ' ' + ' '.join(n.get('aliases') or [])).lower()
        if t in blob: out.append(nid)
    return out


def show(nid, full=False):
    n = NODES.get(nid)
    if not n: return '!! no node ' + nid
    s = n.get('summary') or ''
    if not full: s = s[:700]
    return ("[%s] %s | layer=%s type=%s stub=%s\n  conf=%s human_ev=%s species=%s transl_risk=%s\n  refs=%s\n  SUMMARY: %s\n" % (
        nid, n['name'], n['layer'], n['type'], n.get('stub'), n.get('confidence'),
        n.get('human_evidence'), n.get('species_basis'), n.get('translation_risk'),
        n.get('key_refs'), s))


def edges_of(nid):
    L = []
    for e in OUT.get(nid, []):
        L.append("  OUT %s -%s(%s)-> %s  usable=%s  ctx=%s" % (
            e['edge_id'], e['relation'], e['sign'], e['target'], e['traversal_usable'], (e.get('context') or '')[:70]))
    for e in IN.get(nid, []):
        L.append("  IN  %s %s -%s(%s)->  usable=%s  ctx=%s" % (
            e['edge_id'], e['source'], e['relation'], e['sign'], e['traversal_usable'], (e.get('context') or '')[:70]))
    return '\n'.join(L) or '  (no edges)'


def reach(nid):
    r = REACH.get(nid)
    if r is None: return 'REACH: KEY ABSENT (stub or nonexistent)'
    if not r: return 'REACH: EMPTY DICT (terminal / all outbound sign-exempt)'
    return 'REACH(%d): %s' % (len(r), json.dumps(r)[:900])


if __name__ == '__main__':
    mode = sys.argv[1]
    for term in sys.argv[2:]:
        if mode == 'r':
            print(term, '->', resolve(term))
        elif mode == 'g':
            print(term, '->', grep(term))
        elif mode == 'n':
            print(show(term, full=True)); print(edges_of(term)); print(reach(term))
        elif mode == 's':
            print(show(term))
        elif mode == 'e':
            print(term); print(edges_of(term))
