#!/usr/bin/env python3
"""
F-R016 - recover the numbers from brighton1969/1971 via the OA citing literature.

Legitimate route: papers that CITE Brighton frequently restate his figures. Harvest
every open-access citing work, pull its full text where available (PMC / OA PDF /
landing page), and grep for quantitative restatements of the oxygen results.
"""
import json, re, sys, time, urllib.request, urllib.parse

UA = {'User-Agent': 'Mozilla/5.0 (research; mailto:hello@tateprograms.com)'}
MAIL = 'mailto=hello@tateprograms.com'

def get(u, t=45, tries=4, raw=False):
    for i in range(tries):
        try:
            d = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read()
            return d if raw else d.decode('utf8', 'replace')
        except Exception as e:
            c = getattr(e, 'code', None)
            if c in (429, 500, 502, 503, 504):
                time.sleep(3 * (i + 1)); continue
            return 'ERR %s' % e
    return 'ERR ratelimited'

SEEDS = {  # openalex work ids for the Brighton papers
    'brighton1969_invitro_O2': 'pmid:4186275',
    'brighton1971_zonemap':    'pmid:5580029',
    'brighton1972_avfistula':  'pmid:5133323',
    'brighton1980_diffusion':  'doi:10.2106/00004623-198062050-00007',
    'brighton1983_gpshuttle':  'doi:10.2106/00004623-198365050-00012',
}

# phrases that would indicate a quantitative restatement
PAT = re.compile(
    r'(21\s*(?:per\s*cent|%)[^.]{0,120}oxygen|oxygen[^.]{0,120}21\s*(?:per\s*cent|%)'
    r'|5\s*(?:per\s*cent|%)\s*oxygen|metaphyseal bone formation'
    r'|Brighton[^.]{0,200}(?:oxygen|tension|mm\s*Hg|glycerol|diffusion)'
    r'|glycerol[- ]phosphate shuttle'
    r'|(?:\d{1,3}(?:\.\d)?)\s*mm\s*Hg[^.]{0,80}(?:plate|hypertroph|prolifer|column)'
    r'|(?:hypertroph\w+|prolifer\w+)[^.]{0,80}\d{1,3}(?:\.\d)?\s*mm\s*Hg)',
    re.I)

def resolve(seed):
    d = get('https://api.openalex.org/works/%s?%s' % (seed, MAIL))
    try: return json.loads(d)
    except Exception: return None

def citing(oid, cap=200):
    out, cur = [], '*'
    while len(out) < cap:
        u = ('https://api.openalex.org/works?filter=cites:%s&per-page=100&cursor=%s&%s'
             % (oid, urllib.parse.quote(cur), MAIL))
        r = get(u)
        try: d = json.loads(r)
        except Exception: break
        out += d.get('results', [])
        cur = (d.get('meta') or {}).get('next_cursor')
        if not cur: break
    return out

def fulltext(w):
    """Try PMC first (clean XML), then any OA pdf/landing page."""
    ids = w.get('ids', {})
    pmcid = ids.get('pmcid')
    if pmcid:
        pmc = pmcid.split('/')[-1]
        x = get('https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML' % pmc, t=60)
        if x and not x.startswith('ERR') and len(x) > 2000:
            return re.sub('<[^>]+>', ' ', x), 'epmc:%s' % pmc
    loc = w.get('best_oa_location') or {}
    for u in (loc.get('pdf_url'), loc.get('landing_page_url')):
        if not u: continue
        b = get(u, t=60, raw=True)
        if isinstance(b, bytes) and b[:4] == b'%PDF':
            open('/tmp/_cite.pdf', 'wb').write(b)
            try:
                import pypdf
                r = pypdf.PdfReader('/tmp/_cite.pdf')
                return ' '.join((p.extract_text() or '') for p in r.pages), u
            except Exception:
                pass
        elif isinstance(b, bytes):
            return re.sub('<[^>]+>', ' ', b.decode('utf8', 'replace')), u
    return None, None

if __name__ == '__main__':
    hits = []
    for name, seed in SEEDS.items():
        w = resolve(seed)
        if not w:
            print('!! could not resolve', name, seed); continue
        oid = w['id'].split('/')[-1]
        cits = citing(oid)
        oa = [c for c in cits if (c.get('open_access') or {}).get('is_oa')]
        print('\n### %-26s %s  cited_by=%-4s  OA citing=%s'
              % (name, oid, w.get('cited_by_count'), len(oa)))
        sys.stdout.flush()
        for c in oa:
            txt, src = fulltext(c)
            if not txt: continue
            found = PAT.findall(txt)
            if found:
                title = (c.get('title') or '')[:70]
                print('  HIT %s %s | %s' % (c.get('publication_year'), title, src))
                for f in dict.fromkeys(found):
                    s = re.sub(r'\s+', ' ', f).strip()
                    if 25 < len(s) < 400:
                        print('       >', s[:320])
                        hits.append({'seed': name, 'citing': c.get('id'),
                                     'year': c.get('publication_year'),
                                     'title': c.get('title'), 'src': src, 'quote': s})
            sys.stdout.flush()
    json.dump(hits, open('cite_hits.json', 'w'), indent=1)
    print('\n=== %d quantitative restatements captured -> cite_hits.json' % len(hits))
