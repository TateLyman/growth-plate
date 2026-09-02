import os, yaml, textwrap
DIR='/home/user/growth-plate/atlas/nodes/L13_methods_and_data'
class Blk(str): pass
def _blk(dumper,data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.SafeDumper.add_representer(Blk,_blk)
def w(n):
    n.setdefault('layer','L13'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    if 'summary' in n:
        n['summary']=Blk(textwrap.fill(' '.join(n['summary'].split()),92)+'\n')
    p=os.path.join(DIR,n['id']+'.yaml')
    with open(p,'w') as f:
        yaml.safe_dump(n,f,sort_keys=False,default_flow_style=False,width=95,allow_unicode=True)
    return p
