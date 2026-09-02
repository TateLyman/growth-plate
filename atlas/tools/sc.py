import subprocess, json, sys
nodes = sys.argv[1:]
out = {}
for n in nodes:
    try:
        r = subprocess.run(['python3', '/home/user/growth-plate/atlas/tools/structural_confidence.py', '--node', n],
                           capture_output=True, text=True, timeout=120)
        d = json.loads(r.stdout)
        out[n] = d['structural_confidence']
    except Exception as e:
        out[n] = None
for k, v in out.items():
    print('%-45s %s' % (k, v))
