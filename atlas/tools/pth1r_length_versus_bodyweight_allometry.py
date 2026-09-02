#!/usr/bin/env python3
"""
Is the female-only femoral length gain under teriparatide a PLATE effect or a
BODY-SIZE effect? Test it against isometric allometry.

THE SETUP
---------
Round 195 established that every femoral length increase in the NDA 21-318
package is female and co-occurs with a body-weight increase, while every
intact-male arm is null and loses weight. Two studies report BOTH quantities
per dose in the same females, which makes the question testable without new
data.

IF THE LENGTH GAIN IS NOTHING BUT BODY SIZE, then for geometrically similar
animals mass scales with the cube of a linear dimension, so

    delta_length / length  ~=  (1/3) * delta_mass / mass

i.e. a 10% heavier rat is about 3.2% longer-boned. Deviation ABOVE that line is
the part a systemic size effect cannot explain and is the candidate plate effect.

Rat long-bone allometry is not exactly isometric, so the 1/3 exponent is a
reference line and not a law. A sensitivity band of 0.25 to 0.40 is run
alongside it.

ALL INPUTS ARE AUTHOR-STATED, transcribed from fda_forteo_pharmreview_2002.
"""

STUDIES = {
    "26-week rat toxicity study, females": {
        # dose label -> (body weight % change, femur length % change)
        "low":  (7.0, 2.0),
        "mid":  (10.0, 3.0),
        "high": (10.0, 4.0),
        "note": "femur length reported as 1.02x, 1.03x, 1.04x; BW +7/+10/+10%. "
                "Males in the same study: BW -3.8%, length change not seen.",
    },
    "first carcinogenicity study, females (2 y)": {
        "low":  (4.5, None),
        "mid":  (9.0, None),
        "high": (10.4, 6.0),
        "note": "only the high-dose length is stated (up to 6%); BW +4.5/+9.0/"
                "+10.4% after 1 year. Length is by CALIPER in animals whose "
                "femoral width rose 33%.",
    },
}

EXPONENTS = [0.25, 1.0 / 3.0, 0.40]


def main():
    print("=" * 78)
    print("FEMORAL LENGTH GAIN VERSUS BODY-WEIGHT GAIN, FEMALE RATS")
    print("=" * 78)
    print("\nReference line: d(length)/length = k * d(mass)/mass, k = 1/3 for")
    print("isometric scaling. Sensitivity k = 0.25 and 0.40 alongside.\n")

    for study, d in STUDIES.items():
        print(f"--- {study} ---")
        print(f"    {d['note']}\n")
        hdr = (f"    {'dose':>5} {'dBW%':>7} {'dLen%':>7} "
               + " ".join(f"{'k=%.2f pred' % k:>13}" for k in EXPONENTS)
               + f" {'excess @1/3':>13}")
        print(hdr)
        for dose in ("low", "mid", "high"):
            bw, ln = d[dose]
            preds = [k * bw for k in EXPONENTS]
            if ln is None:
                print(f"    {dose:>5} {bw:>7.1f} {'n/r':>7} "
                      + " ".join(f"{p:>13.2f}" for p in preds)
                      + f" {'-':>13}")
                continue
            excess = ln - (bw / 3.0)
            print(f"    {dose:>5} {bw:>7.1f} {ln:>7.1f} "
                  + " ".join(f"{p:>13.2f}" for p in preds)
                  + f" {excess:>+13.2f}")
        print()

    print("[1] READING")
    print("    26-week study. Isometric scaling predicts +2.3%, +3.3%, +3.3%")
    print("    length from the observed weight gains. Observed: +2.0%, +3.0%,")
    print("    +4.0%. Two of three doses fall BELOW the isometric line and the")
    print("    third exceeds it by 0.7 percentage points. There is no residual")
    print("    length effect left over once body size is accounted for.")
    print()
    print("    Two-year study. Isometric predicts +3.5% from +10.4% BW;")
    print("    observed +6% by caliper, an excess of +2.5 points. But that")
    print("    measurement is the one whose femoral WIDTH rose 33%, and the")
    print("    regulator's own reading of it is 'effect of LY mainly on")
    print("    periosteal expansion'. The excess is the size of the artefact")
    print("    the method cannot exclude.")

    print("\n[2] WHAT THIS DOES AND DOES NOT SETTLE")
    print("    It does NOT prove the length gain is only body size - allometry")
    print("    is a reference line, the exponent is not measured in these")
    print("    animals, and body weight and femur length could both be")
    print("    downstream of one plate effect.")
    print("    It DOES remove the reason to think otherwise. The female length")
    print("    gains are the size that the concurrent weight gains predict; the")
    print("    males, who lost weight, gained no length; and the one arm that")
    print("    exceeds the line is the one measured by a method that counts")
    print("    periosteal bone as length.")

    print("\n[3] THE DISCRIMINATING EXPERIMENT, WHICH NOBODY HAS RUN")
    print("    Dose intact males and females at matched exposure with a")
    print("    PAIR-FED control arm, so body-weight trajectory is equalised")
    print("    across drug and vehicle. Measure femur length by microCT and")
    print("    growth plate height and cells per column in the same animals.")
    print("    If the female length gain survives pair-feeding, it is a plate")
    print("    effect. If it disappears, the entire femoral-length literature")
    print("    for this drug class is a body-weight readout.")
    print("=" * 78)


if __name__ == "__main__":
    main()
