#!/usr/bin/env python3
"""
R480 - v(d) = v(c) + v(m) CLOSES TO 0.04% ON WILSMAN 1996's OWN MEASURED NUMBERS,
AND THE PAPER CONTAINS A SECOND, INDEPENDENT MEASUREMENT OF v(m) IN THE SAME FOUR
PLATES AS BREUR 1997.

PROVENANCE. Every value below is transcribed from the atlas's own local full text
of Wilsman NJ, Farnum CE, Leiferman EM, Fry M, Barreto C, "Differential growth by
growth plates as a function of multiple parameters of chondrocytic kinetics",
J Orthop Res 1996;14:927-936 (acquire/papers/txt/wilsman1996.txt). Tables 4, 5 and
6 plus the Results text. NOT re-derived, NOT inferred, NOT from a secondary source.

  Table 6   matrix per cell, V[m]hypertrophic (um^3)
  Table 4   N_lost (chondrocytes lost per day at the chondro-osseous junction),
            V_T turned over (mm^3/day), and mean hypertrophic cellular volume
  text      "Mean cellular volumes ranged from 14,997 um^3 in the proximal tibia
            to 4,135 um^3 in the proximal radius"

WHY THIS IS NOT CIRCULAR. round480_vd_decomposition.py noted honestly that once
flux is DEFINED as rate/v_d the identity is closed by construction. Here it is not:
v(c) is a stereological mean cell volume, v(m) is computed from the hypertrophic
volume fraction, and v(d) is the total turned-over volume divided by the cells lost.
Three separately measured quantities. Their agreement is a real check.

WHAT IS NEW. The atlas has carried Wilsman's 9/32/59 and 7/49/44 source
decomposition since R470 and has never extracted Table 6, which gives MATRIX VOLUME
PER CELL directly for all four plates. That makes Wilsman an independent second
measurement of v(m) against Breur 1997 in the same four rat growth plates.

Output: atlas/data/round480/wilsman_vd_closure.json
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "round480")

# Wilsman 1996, transcribed from the local full text.
W = {
    # plate: (matrix per cell um^3 [T6], N_lost per day [T4], V_T turned over mm^3/day [T6],
    #         mean hypertrophic cell volume um^3 [T4/text], elongation rate um/day [T2])
    "proximal_tibia":  (6900, 14200, 0.311, 14997, 396),
    "distal_radius":   (5970, 11450, 0.211, None, None),
    "distal_tibia":    (5780,  7520, 0.108, None, None),
    "proximal_radius": (4090,  4500, 0.037,  4135,  47),
}

# Breur GJ 1997 Calcif Tissue Int 61:418-425, day 21, as tabulated in CLAUDE.md R470.
BREUR_D21 = {
    "proximal_tibia":  {"v_m": 8950, "v_c": 17040},
    "distal_radius":   {"v_m": 6380, "v_c": 12860},
    "distal_tibia":    {"v_m": 7860, "v_c": 11900},
    "proximal_radius": {"v_m": 4650, "v_c":  4420},
}

UM3_PER_MM3 = 1e9


def main():
    rows = []
    for plate, (v_m, n_lost, vt_mm3, v_c_meas, rate) in W.items():
        v_d = vt_mm3 * UM3_PER_MM3 / n_lost          # measured: total volume / cells lost
        v_c_implied = v_d - v_m                       # what the identity requires
        row = {
            "plate": plate,
            "elongation_rate_um_day": rate,
            "n_lost_per_day": n_lost,
            "vt_turned_over_mm3_day": vt_mm3,
            "v_m_matrix_per_cell_um3_measured": v_m,
            "v_d_domain_um3_measured": round(v_d, 1),
            "v_c_implied_by_identity_um3": round(v_c_implied, 1),
            "v_c_stereologically_measured_um3": v_c_meas,
            "matrix_fraction_of_domain": round(v_m / v_d, 4),
        }
        if v_c_meas is not None:
            row["identity_residual_pct"] = round(
                100 * abs((v_c_meas + v_m) - v_d) / v_d, 4)
        rows.append(row)

    rows.sort(key=lambda r: -r["v_d_domain_um3_measured"])

    fast = next(r for r in rows if r["plate"] == "proximal_tibia")
    slow = next(r for r in rows if r["plate"] == "proximal_radius")

    rate_ratio = fast["elongation_rate_um_day"] / slow["elongation_rate_um_day"]
    vd_ratio = fast["v_d_domain_um3_measured"] / slow["v_d_domain_um3_measured"]
    flux_ratio = rate_ratio / vd_ratio

    # cross-paper agreement on both terms
    cross = []
    for plate in W:
        w_vm = W[plate][0]
        w_vd = W[plate][2] * UM3_PER_MM3 / W[plate][1]
        w_vc = w_vd - w_vm
        b = BREUR_D21[plate]
        cross.append({
            "plate": plate,
            "v_m_wilsman": w_vm,
            "v_m_breur_d21": b["v_m"],
            "v_m_pct_apart": round(100 * abs(w_vm - b["v_m"]) / ((w_vm + b["v_m"]) / 2), 1),
            "v_c_wilsman": round(w_vc, 0),
            "v_c_breur_d21": b["v_c"],
            "v_c_pct_apart": round(100 * abs(w_vc - b["v_c"]) / ((w_vc + b["v_c"]) / 2), 1),
        })

    w_vm_range = max(W[p][0] for p in W) / min(W[p][0] for p in W)
    w_vc_range = (max(r["v_c_implied_by_identity_um3"] for r in rows)
                  / min(r["v_c_implied_by_identity_um3"] for r in rows))
    b_vm_range = max(b["v_m"] for b in BREUR_D21.values()) / min(b["v_m"] for b in BREUR_D21.values())
    b_vc_range = max(b["v_c"] for b in BREUR_D21.values()) / min(b["v_c"] for b in BREUR_D21.values())

    out = {
        "note": __doc__.strip(),
        "per_plate": rows,
        "identity_closure": {
            "claim": "v(d) = v(c) + v(m) with all three terms separately measured",
            "proximal_tibia": "14997 + 6900 = 21897 against a measured 21901 um^3",
            "proximal_radius": "4135 + 4090 = 8225 against a measured 8222 um^3",
            "max_residual_pct": max(r["identity_residual_pct"] for r in rows
                                    if "identity_residual_pct" in r),
            "why_not_circular": (
                "v(c) is a stereological mean cell volume, v(m) is computed from the "
                "hypertrophic volume fraction, and v(d) is total turned-over volume "
                "divided by cells lost. Three independent measurements."
            ),
        },
        "growth_identity": {
            "rate_ratio_fast_over_slow": round(rate_ratio, 3),
            "v_d_ratio": round(vd_ratio, 3),
            "implied_flux_ratio": round(flux_ratio, 3),
            "comment": "reproduces the frontier branch's 3.16 x 2.67 = 8.42 against 8.43 measured",
        },
        "cross_paper_agreement": cross,
        "between_site_ranges": {
            "v_c_range_wilsman": round(w_vc_range, 2),
            "v_m_range_wilsman": round(w_vm_range, 2),
            "v_c_range_breur": round(b_vc_range, 2),
            "v_m_range_breur": round(b_vm_range, 2),
            "reading": (
                "Two independent papers on the same four rat growth plates agree that "
                "terminal CELL volume varies about twice as much between sites as MATRIX "
                "per cell does. The organism modulates the cell more than the matrix."
            ),
        },
        "the_headline": (
            "In the slowest plate v(c) = 4135 and v(m) = 4090 um^3, a ratio of 1.011. "
            "THE TERMINAL CHONDROCYTIC DOMAIN OF THE SLOWEST RAT GROWTH PLATE IS HALF "
            "CELL AND HALF MATRIX TO ONE PER CENT. And the matrix fraction rises "
            "monotonically as the plate slows: 31.5 / 32.4 / 40.2 / 49.7 per cent."
        ),
    }

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "wilsman_vd_closure.json"), "w") as fh:
        json.dump(out, fh, indent=1)

    print(f"{'plate':18s} {'rate':>5s} {'v_c':>8s} {'v_m':>7s} {'v_d':>8s} {'matrix%':>8s} {'resid%':>7s}")
    for r in rows:
        vc = r["v_c_stereologically_measured_um3"] or r["v_c_implied_by_identity_um3"]
        star = "" if r["v_c_stereologically_measured_um3"] else " (implied)"
        print(f"{r['plate']:18s} {str(r['elongation_rate_um_day'] or '-'):>5s} "
              f"{vc:8.0f} {r['v_m_matrix_per_cell_um3_measured']:7d} "
              f"{r['v_d_domain_um3_measured']:8.0f} "
              f"{100*r['matrix_fraction_of_domain']:7.1f}% "
              f"{r.get('identity_residual_pct', float('nan')):7.3f}{star}")
    print()
    print(f"rate {rate_ratio:.2f}x = v_d {vd_ratio:.2f}x  x  flux {flux_ratio:.2f}x")
    print()
    print("cross-paper agreement on the two terms (Wilsman 1996 vs Breur 1997 D21):")
    for c in cross:
        print(f"  {c['plate']:18s} v_m {c['v_m_wilsman']:5d} vs {c['v_m_breur_d21']:5d} "
              f"({c['v_m_pct_apart']:4.1f}% apart)   v_c {c['v_c_wilsman']:6.0f} vs "
              f"{c['v_c_breur_d21']:6d} ({c['v_c_pct_apart']:4.1f}% apart)")
    print()
    print(f"between-site range   v_c {w_vc_range:.2f}x (Wilsman) / {b_vc_range:.2f}x (Breur)")
    print(f"                     v_m {w_vm_range:.2f}x (Wilsman) / {b_vm_range:.2f}x (Breur)")


if __name__ == "__main__":
    main()
