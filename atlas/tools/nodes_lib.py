import yaml, os
DIR="/home/user/growth-plate/atlas/nodes/L1_growth_plate_architecture"
TODAY="2026-08-05"

def Q(parameter,value,unit,conditions,species,source_ref,uncertainty="not reported",unverified=False):
    d=dict(parameter=parameter,value=str(value),unit=unit,conditions=conditions,
           species=species,source_ref=source_ref,uncertainty=uncertainty)
    if unverified: d["value_unverified"]=True
    return d

def R(ref_id,pmid,first_author,year,rtype,finding,doi=None):
    d=dict(ref_id=ref_id,pmid=str(pmid),first_author=first_author,year=year,type=rtype,
           one_line_finding=finding)
    if doi: d["doi"]=doi
    return d

def write(node):
    node.setdefault("stub",False)
    node.setdefault("layer","L1")
    node.setdefault("last_verified",TODAY)
    order=["id","name","aliases","type","layer","stub","summary","quantitative","localization",
           "human_evidence","human_evidence_note","species_basis","translation_risk",
           "translation_risk_reason","confidence","key_refs","open_questions","contradicts",
           "pending_source","last_verified"]
    out={k:node[k] for k in order if k in node and node[k] not in (None,[],"")}
    p=os.path.join(DIR,node["id"]+".yaml")
    with open(p,"w") as f:
        yaml.safe_dump(out,f,sort_keys=False,default_flow_style=False,width=100,allow_unicode=True)
    return p
