import sys, yaml, glob, os, textwrap
names = sys.argv[1:]
files = {}
for p in glob.glob('/home/user/growth-plate/atlas/nodes/*/*.yaml'):
    files[os.path.basename(p)[:-5]] = p
for n in names:
    p = files.get(n)
    if not p:
        print(f"### {n}: NOT FOUND"); continue
    d = yaml.safe_load(open(p))
    print(f"### {n} [{d.get('layer')}] conf={d.get('confidence')} he={d.get('human_evidence')} sp={d.get('species_basis')}")
    s = (d.get('summary') or '').replace('\n',' ')
    print(textwrap.fill(s, 150, initial_indent='  S: ', subsequent_indent='     '))
    for q in d.get('quantitative') or []:
        print(f"   - {q.get('parameter')} = {q.get('value')} {q.get('unit')} | {q.get('conditions')} | sp={q.get('species')} | ±{q.get('uncertainty')} | <{q.get('source_ref')}>")
    print()
