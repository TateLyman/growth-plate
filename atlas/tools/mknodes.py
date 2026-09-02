import os, yaml, sys
D = "/home/user/growth-plate/atlas/nodes/L3_signaling_networks"

class LS(str): pass
def _rep(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.add_representer(LS, _rep)

def w(n):
    n.setdefault("layer","L3"); n.setdefault("stub",False)
    n.setdefault("last_verified","2026-08-05")
    if "summary" in n: n["summary"]=LS(n["summary"].strip()+"\n")
    order=["id","name","aliases","type","layer","stub","summary","quantitative","localization",
           "human_evidence","human_evidence_note","species_basis","translation_risk",
           "translation_risk_reason","confidence","key_refs","open_questions","contradicts",
           "pending_source","last_verified"]
    o={k:n[k] for k in order if k in n}
    for k in n:
        if k not in o: o[k]=n[k]
    p=os.path.join(D,n["id"]+".yaml")
    with open(p,"w") as f:
        yaml.dump(o,f,sort_keys=False,default_flow_style=False,width=100,allow_unicode=True)
    print("wrote",p)

def kr(ref_id, pmid, fa, yr, typ, finding, doi=None):
    d={"ref_id":ref_id,"pmid":str(pmid),"first_author":fa,"year":yr,"type":typ,"one_line_finding":finding}
    if doi: d["doi"]=doi
    return d
