import re, sys
OLD_MISSING = """  what_is_missing: (1) ANY HUMAN OBSERVATION. No human growth plate tissue has been examined for GLI1+ or PDGFRA+
    progenitors outside the cartilage. (2) WHETHER THE RESERVOIR PERSISTS POSTNATALLY IN HUMANS, since the mouse
    demonstration is fetal. (3) WHETHER IT IS STILL PRESENT NEAR FUSION - the age at which it would matter most
    is the age at which it is least likely to remain.
"""
NEW_MISSING = """  what_is_missing: 'PARTLY ANSWERED 2026-08-06 BY THIS ATLAS''S OWN RE-ANALYSIS, AND THE ANSWER SPLITS THE QUESTION
    IN TWO. (1) A HUMAN STROMAL POPULATION EXISTS - GSE288028, four directly processed libraries, 27,620 cells,
    harmony-corrected, per-library ambient reference: cluster 0, 1,374 cells in three donors, COL1A1 573x enriched
    over chondrocytes, PRRX1 13x, PDGFRA-positive in 78%, COL2A1 at its own donors'' ambient floor. (2) IT IS
    HEDGEHOG-NEGATIVE. GLI1 0.30, PTCH1 0.08, HHIP 0.03, GLI2 0.22 relative to chondrocytes. Every direct target
    is DEPLETED, and GLI1 is the marker by which the mouse reserve is identified, traced and recruited. STILL
    MISSING: (a) POSITION - dissociated scRNA-seq infers "outside the cartilage" from transcriptome, and no image
    places these cells relative to the plate; (b) WHETHER THE POPULATION IS RECRUITABLE, since qu2025 recruits it
    by cartilage DAMAGE and no human sample can be taken under that condition, so a Hedgehog-off-at-rest population
    is not thereby shown to be Hedgehog-unresponsive; (c) THE CONSTITUTION WINDOW - the biopsies are 12-14 y and
    Tanner 2-4, and the mouse reserve is constituted at about 3 postnatal weeks, so the human equivalent of that
    window is unsampled; (d) DONOR3, the most cartilage-rich library, is EXCLUDED because it holds 9 immune cells
    and its ambient floor cannot be measured (CORR-021); (e) INDEPENDENT REPLICATION in a second human cohort.'
"""
OLD_DISC_TAIL = """  ASKING WHETHER GLI1 AND PDGFRA MARK A POPULATION ADJACENT TO THE HUMAN RESTING ZONE IS A RE-ANALYSIS
    OF PUBLISHED DATA AND COSTS NOTHING. A positive answer justifies everything downstream; a negative answer closes
    the most promising route in this atlas, cheaply.
"""
NEW_DISC_TAIL = """  THE RE-ANALYSIS HAS NOW BEEN RUN AND THE CHEAP ROUTE IS SPENT. It took
    three instruments, four guard failures and two corrections (CORR-018 through CORR-021) to get a readable answer,
    and the spatial data proved too shallow for Hedgehog components - PTCH1 45 and GLI1 60 pooled counts across 14
    sections. THE REMAINING EXPERIMENT IS NO LONGER FREE AND IS NOW SPECIFIC: (1) a targeted in-situ panel - Xenium
    or RNAscope - for GLI1, PTCH1, PDGFRA, COL1A1 and COL2A1 on an INTACT human growth plate section, which supplies
    the position that dissociation destroys and the depth that RRST lacks; (2) chu2026''s explant, which survives two
    months, INJURED and then assayed for GLI1 induction, because the mouse result is about recruitment on damage and
    nothing observed at rest can test it; (3) a younger human cohort, to sample the window in which the reserve would
    be constituted rather than the pubertal window in which it would already be spent.
"""
p="atlas/gaps/gaps.yaml"; s=open(p).read()
for f,(o,n) in {"gaps.yaml":(OLD_MISSING,NEW_MISSING)}.items(): pass
for path in ("atlas/gaps/gaps.yaml","atlas/gaps/shards/l2stem.gaps.yaml"):
    s=open(path).read(); before=s
    assert OLD_MISSING in s, f"missing block not found in {path}"
    assert OLD_DISC_TAIL in s, f"disc block not found in {path}"
    s=s.replace(OLD_MISSING,NEW_MISSING).replace(OLD_DISC_TAIL,NEW_DISC_TAIL)
    open(path,"w").write(s); print("patched",path)
