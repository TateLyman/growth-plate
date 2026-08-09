import json, math
from rdkit import Chem
from rdkit import RDLogger; RDLogger.DisableLog('rdApp.*')

# Basic centres protonated at pH 7.4: aliphatic amines (not amide/sulfonamide/aniline/nitrile/
# nitro/aromatic-ring N), plus amidines and guanidines. Pyridine-type N (pKa ~5) excluded.
BASIC = [
 Chem.MolFromSmarts('[NX3;H2,H1,H0;!$(N[C,S]=[O,S,N]);!$(N[SX4](=O)=O);!$(Nc);!$(N[CX3]=[CX3]);!$(N#*);!$(N=*);!$([N+]);!$(N[NX3]);!$(NO);R0]'),
 Chem.MolFromSmarts('[NX3;H2,H1,H0;!$(N[C,S]=[O,S,N]);!$(N[SX4](=O)=O);!$(Nc);!$(N#*);!$(N=*);!$([N+]);!$(NO);R;!$([n])]'),
 Chem.MolFromSmarts('[NX3][CX3]=[NX2;!$(N[C,S]=O)]'),          # amidine
 Chem.MolFromSmarts('[NX3][CX3](=[NX2])[NX3]'),                 # guanidine
]
ACID = [
 Chem.MolFromSmarts('[CX3](=O)[OX2H1]'),                        # carboxylic acid
 Chem.MolFromSmarts('c1nnn[nH]1'), Chem.MolFromSmarts('c1nn[nH]n1'),   # tetrazole
 Chem.MolFromSmarts('[SX4](=O)(=O)[OX2H1]'),                    # sulfonic acid
 Chem.MolFromSmarts('[CX3](=O)[NX3H1][SX4](=O)(=O)'),           # acylsulfonamide
 Chem.MolFromSmarts('[PX4](=O)([OX2H1])'),                      # phosphate/phosphonate
]
def centres(m,pats):
    s=set()
    for p in pats:
        if p is None: continue
        for match in m.GetSubstructMatches(p):
            s.add(match[0])
    return s

def net_charge(smi):
    m=Chem.MolFromSmiles(smi)
    if m is None: return None,None,None
    b=len(centres(m,BASIC)); a=len(centres(m,ACID))
    return b-a+Chem.GetFormalCharge(m), b, a

def size_term(mw):
    A=[(332,1.00),(3000,0.60),(10000,0.10),(40000,0.01)]
    if mw<=A[0][0]: return 1.00
    for (m1,p1),(m2,p2) in zip(A,A[1:]):
        if mw<=m2:
            f=(math.log(mw)-math.log(m1))/(math.log(m2)-math.log(m1)); return p1+f*(p2-p1)
    return 0.01
def donnan_ratio(cF,c0=0.15):
    return ((-cF+math.sqrt(cF**2+4*c0**2))/2.0)/c0
def partition(mw,z):
    s=size_term(mw)
    if z==0: return s
    los,his=donnan_ratio(0.35),donnan_ratio(0.19)
    d=((los**abs(z))+(his**abs(z)))/2 if z<0 else (((1/los)**z)+((1/his)**z))/2
    return s*d
