#!/usr/bin/env python3
"""Is there a HEDGEHOG-RESPONSIVE, PDGFRA+/COL1A1+ population adjacent to the human
resting zone but outside the cartilage?

THIS IS A NEW ANALYSIS, NOT A RETUNE OF THE TWO THAT FAILED.
  reservoir_screen.py   (dissociated scRNA-seq) failed its THY1 guard twice. Dead.
  spatial_reservoir.py  (Visium HD) failed its GLI1/PTCH1 coherence guard, and the
                        diagnostic showed why: GLI1 had 21 counts in the entire
                        section, in 6 of 2787 cells. Dead.

WHAT CHANGES AND WHY, DECLARED BEFORE ANY RESULT IS SEEN:
  (a) DATA. 14 standard Visium sections instead of one bin2cell-segmented Visium HD
      section. Visium spots carry orders of magnitude more counts than segmented
      cells, which is the specific failure of the previous attempt.
  (b) MARKER. GLI1 alone is not measurable in this tissue. The mouse paper uses Gli1
      as a lineage-tracing HANDLE for Hedgehog-responsive cells, not because Gli1
      itself matters. The human-tissue equivalent of "Hedgehog-responsive" is a
      COMPOSITE of direct pathway targets - PTCH1, GLI1, HHIP, PTCH2 - pooled to
      raise detectability. Substituting a composite for an undetectable single gene
      is a change of instrument, not a change of hypothesis, and it is declared here.

PRE-REGISTERED GUARDS:
  G1 DETECTION FLOOR. Every gene entering a score must have >= 100 counts pooled
     across all sections. Genes below that are EXCLUDED and the exclusion reported.
     If fewer than 2 Hedgehog targets survive, the analysis does not run.
  G2 ZONE VALIDITY. COL10A1 must be highest in the hypertrophic annotation and
     COL2A1 must be lower in the non-cartilage annotation than in every cartilage
     annotation.
  G3 PATHWAY COHERENCE. PTCH1 and HHIP are independent direct Hedgehog targets.
     Their per-spot values must correlate positively across all spots (Spearman
     rho > 0, p < 0.01). This replaces the GLI1/PTCH1 check that failed, and it is
     stronger because both genes are detectable.
  G4 NEGATIVE CONTROL. A set of genes with no expected spatial structure
     (housekeeping: ACTB, GAPDH, RPL13A) must NOT differ more than 2-fold between
     the resting-zone-adjacent band and the far band.
"""
import sys, os, glob, json
import numpy as np, pandas as pd
from scipy.io import mmread
from scipy.stats import spearmanr

HH   = ["PTCH1","GLI1","HHIP","PTCH2"]
STROMA=["PDGFRA","COL1A1","PRRX1","PDGFRB"]
CART = ["COL2A1","ACAN","COL10A1","SFRP5"]
NEG  = ["ACTB","GAPDH","RPL13A"]
MIN_COUNTS = 100

def main(expdir):
    metas=sorted(glob.glob(os.path.join(expdir,"*.meta.csv")))
    if not metas: print(f"no exports in {expdir}",file=sys.stderr); return 1
    print(f"{len(metas)} sections exported\n")
    pooled={}; sections=[]
    for m in metas:
        nm=m[:-len(".meta.csv")]
        try:
            md=pd.read_csv(m,index_col=0)
            genes=pd.read_csv(nm+".genes.csv")["x"].values
            M=mmread(nm+".counts.mtx").tocsr()
        except Exception as e:
            print(f"  skip {os.path.basename(nm)}: {e}"); continue
        sections.append(dict(name=os.path.basename(nm),meta=md,genes=genes,M=M))
        gi={g:i for i,g in enumerate(genes)}
        for g in HH+STROMA+CART+NEG:
            if g in gi: pooled[g]=pooled.get(g,0)+int(M[gi[g],:].sum())
        print(f"  {os.path.basename(nm):<22} {M.shape[1]:>6} spots  {int(M.sum()):>10} counts  "
              f"meta: {list(md.columns)[:6]}")
    print("\nDETECTION FLOOR - pooled counts across all sections")
    for g in HH+STROMA+CART+NEG:
        c=pooled.get(g,0)
        print(f"  {g:<9} {c:>9} {'PASS' if c>=MIN_COUNTS else 'EXCLUDED (below floor)'}")
    hh_ok=[g for g in HH if pooled.get(g,0)>=MIN_COUNTS]
    if len(hh_ok)<2:
        print(f"\nG1 FAILED: only {len(hh_ok)} Hedgehog target(s) above the floor -> {hh_ok}")
        print("REFUSING TO REPORT."); return 1
    print(f"\nG1 PASS: Hedgehog score will use {hh_ok}")
    json.dump({"pooled_counts":pooled,"hh_used":hh_ok,
               "sections":[s["name"] for s in sections]},
              open("/home/user/growth-plate/query/visium_detection_floor.json","w"),indent=1)
    print("\nSections and per-spot annotations above determine the next step; the zone,\n"
          "coherence and negative-control guards run once the annotation column is known.")
    return 0

if __name__=="__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else "visium_export"))
