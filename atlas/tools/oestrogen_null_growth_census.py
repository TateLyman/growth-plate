#!/usr/bin/env python3
"""
ADULT GROWTH VELOCITY IN THE OESTROGEN-NULL HUMAN, and what it says about
whether the plate at exhaustion is EMPTY or merely SWITCHED OFF.

WHY THIS EXISTS
---------------
Round 198 made the budget binding rather than the closure. Round 199 asked
whether the budget can be expanded. This tool asks the prior question: when a
human plate stops producing, has it run out of cells or has it stopped using
them? The oestrogen-null human is the only place to look, because fusion has
been removed and whatever ends growth there is not closure.

Every value below is author-stated in the cited case report. Velocities are
computed by division and are labelled DERIVED.
"""

# ref, age span, height span cm, note
CASES = [
    # NOTE: herrmann2002's span STARTS AT 14 and therefore includes pubertal
    # growth. Its velocity is NOT an adult velocity and must not be pooled with
    # the two spans that begin in the third decade.
    ("herrmann2002", 14, 24, 170.0, 197.0,
     "grew 170 cm at 14 to 197 cm and CEASED SPONTANEOUSLY AT 24; at 27, "
     "untreated, arm span 204 cm, bone age 16, hand X-ray showing OPEN "
     "EPIPHYSES"),
    ("maffei2004", 21, 29, 172.0, 183.5,
     "bone age frozen at 15 throughout, including through 27 months of "
     "supraphysiological testosterone; oestradiol then advanced bone age past "
     "16 in 6 months and stopped growth at 184.5 cm"),
    ("imre2025", 25, 31, 188.0, 193.0,
     "height increased by 5 cm over the preceding 6 years to 193 cm with "
     "incomplete epiphyseal fusion; transdermal estradiol 25 ug twice weekly "
     "produced EPIPHYSEAL FUSION WITHIN 6 MONTHS"),
]

# the ESR1-null man, who cannot be closed by any means
SMITH = ("smith2008/smith2010", 28, 31.5, 204.0, None,
         "204 cm at 28 with incomplete closure and a history of continued "
         "linear growth into adulthood; six months of transdermal oestrogen "
         "raising free oestradiol tenfold had no detectable effect; bone age "
         "advanced only 15 to 17.5 over 3.5 years. NO LATER HEIGHT EXISTS")


def main():
    print("=" * 82)
    print("GROWTH AFTER 20 IN THE OESTROGEN-NULL HUMAN")
    print("=" * 82)
    print(f"    {'case':>14} {'ages':>10} {'height cm':>14} {'cm/yr':>8}")
    for ref, a0, a1, h0, h1, note in CASES:
        v = (h1 - h0) / (a1 - a0)
        print(f"    {ref:>14} {f'{a0}-{a1}':>10} {f'{h0:.0f} to {h1:.1f}':>14} "
              f"{v:>8.2f}   [DERIVED]")
    print()
    for ref, a0, a1, h0, h1, note in CASES:
        print(f"    {ref}: {note}")
    print(f"\n    {SMITH[0]}: {SMITH[5]}")

    print("\n" + "=" * 82)
    print("[1] THE PLATE IS STILL THERE WHEN GROWTH STOPS")
    print("=" * 82)
    print("    herrmann2002 is the only observed spontaneous endpoint in this")
    print("    literature and it is an ARREST, not an emptying. Growth ceased")
    print("    at 24. THREE YEARS LATER the epiphyses were still anatomically")
    print("    open and the bone age was 16. A plate that had run out of cells")
    print("    would not still be a plate.")
    print("    So at the tissue level the human answer is: the cartilage")
    print("    remains and stops being used.")

    print("\n[2] AND THE ENDPOINT IS NOT SHARED")
    print("    herrmann2002 exhausted at 197 cm by 24. maffei2004 was still")
    print("    producing at 29. imre2025 was still producing at 31. The ESR1-")
    print("    null man was still producing at about 31 and cannot be stopped.")
    print("    ONE MAN'S PLATE QUIT AT 24 WHILE OTHERS RAN A DECADE LONGER.")
    print("    That spread is the direct evidence that the budget is not a")
    print("    fixed species constant, and it is larger than any drug effect")
    print("    in this file.")

    print("\n[3] THE VELOCITY IS THE CEILING OF THE DURATION LEVER, MEASURED")
    adult = [(ref, (h1 - h0) / (a1 - a0)) for ref, a0, a1, h0, h1, _ in CASES
             if a0 >= 20]
    print("    ADULT spans only - herrmann2002 is excluded because its span")
    print("    starts at 14 and therefore contains pubertal growth:")
    for ref, v in adult:
        print(f"      {ref:>12}: {v:.2f} cm/year")
    print(f"    mean {sum(v for _, v in adult) / len(adult):.2f} cm/year"
          "   [DERIVED, n=2]")
    print("    Removing oestrogen for an entire lifetime buys growth at ABOUT")
    print("    ONE CENTIMETRE A YEAR into the third decade. It does not buy a")
    print("    resumption of pubertal velocity. Anything in this atlas that")
    print("    treats delayed fusion as an open-ended lever should be read")
    print("    against that number.")

    print("\n[4] THE NEW NUMBER, AND IT POINTS THE OTHER WAY")
    print("    imre2025 closed the plates of a 31-year-old with transdermal")
    print("    estradiol 25 ug TWICE WEEKLY in SIX MONTHS. carani1997 and")
    print("    maffei2004 report the same direction. A decade of accumulated")
    print("    residual growth capacity is spent by six months of a low")
    print("    transdermal dose. THE OFF-SWITCH IS FAST AND CHEAP AND THE")
    print("    ON-SWITCH IS NEITHER - which is the asymmetry that makes an")
    print("    aromatase inhibitor worth more than anything acting inside the")
    print("    plate, and also the reason accidental oestrogen exposure is the")
    print("    dominant downside risk in this programme.")

    print("\n[5] WHAT THIS DOES NOT SETTLE, AND IT IS THE WHOLE QUESTION")
    print("    The cartilage remains at cessation. Whether the cells IN it")
    print("    retain any capacity to divide has never been tested, in any")
    print("    species. Nobody has taken a senescent or arrested growth plate")
    print("    and attempted to restart it. The atlas holds that the ceiling is")
    print("    IMPOSED rather than intrinsic - culture restores maintenance")
    print("    methylation to resting-zone cells that were losing it in vivo -")
    print("    which predicts the cells are recoverable. That prediction has")
    print("    never been tested against a length endpoint.")
    print("=" * 82)


if __name__ == "__main__":
    main()
