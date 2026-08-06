#!/usr/bin/env python3
"""
rubin_decompose.py - split the growth plate's "cell height" into the two things it is.

WHY THIS EXISTS
---------------
Every quantity called terminal chondrocyte HEIGHT in this literature is AXIAL EXTENT: how
much length the cell occupies along the proximal-distal axis. That is not a property of the
cell alone. It is

    axial extent  =  intrinsic cell length  x  how well the cell is aligned with the axis

rubin2021 says so itself. Its Supplementary Fig. 4A caption states that the cell bounding
box height "is influenced by cell orientation", beside an illustration of three cells that
yield the same h: a wide flat one, a tall narrow one, and a TILTED elongated one.
cruzorive1986 section 10.5 names the identical confound for hunziker1989's 2D stereological
estimators, in 1986. Cell VOLUME has no such confound in either study.

So the recurring result "volume predicts bone growth better than height" is reported from a
comparison between an orientation-free variable and an orientation-confounded one. That does
not make it wrong. It makes it untested: nobody has asked whether the height metric fails
because cells are not elongating, or because they are elongating and rotating at the same
time. Those have different targets - cell volume regulation and pericellular compliance for
the first, column alignment (integrin beta1, cytoskeletal tension, chondrocyte rotation) for
the second. See atlas gap g_l1arch_017 and contradiction C-L1-08.

WHAT THIS SCRIPT DOES, AND ON WHAT
----------------------------------
rubin2021's 3D MAPs sample deposit (Figshare 10.6084/m9.figshare.14903052.v1) contains, per
segmented cell, everything needed to do the split:

    G/cel/PC_range        extent along each principal axis   <- orientation-FREE lengths
    G/cel/PCA_coeff       the principal axis directions      <- the orientation itself
    G/cel/ellipsoid_radii, ellipsoid_evecs                   <- the fitted ellipsoid
    G/cel/volume, surface_area, sphericity, centroids

The published predictor comparison used the bounding-box height and neither of the first two.

WHAT IT CANNOT DO - READ THIS BEFORE QUOTING ANY NUMBER FROM IT
---------------------------------------------------------------
The deposit is ONE growth plate: distal ulna, sample DU_S84_m3_wt, 21 tiles. There is no
proximal tibia and no distal tibia in it. So this script CANNOT run the three-plate predictor
comparison that produced rubin2021's conclusion, and it cannot say whether the DU-vs-PT
hypertrophic height difference is size or alignment. That needs the other two plates from the
corresponding author.

What it CAN answer is the prior question, which nobody has asked either: WITHIN one plate,
along the differentiation axis, does the cell's alignment with the growth axis change enough
to matter? If alignment is flat from resting zone to hypertrophic zone, the confound is real
but immaterial and the field's height metric is fine. If alignment changes substantially, the
confound bites, and every "cell height" number in this literature is part elongation and part
rotation in an unknown ratio.

VALIDATION GUARD
----------------
Before reporting anything the script reconstructs rubin2021's own published DU profile - mean
cell bounding box height along the P-D axis, Supplementary Fig. 4A, which rises from about
9 um in the resting and proliferative zones to a peak near 26 um in the hypertrophic zone. If
the reconstruction does not reproduce that curve, the registration is wrong and the script
REFUSES to report the decomposition rather than reporting a decomposition of noise.

Usage:
  python3 atlas/tools/rubin_decompose.py --dir <extracted Nuclei_and_Cells_DU_S84_m3_wt>
"""
from __future__ import annotations
import argparse, csv, glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "query", "rubin_decompose")

# rubin2021 Supplementary Fig. 4A, distal ulna trace, read off the published panel.
# These are the guard rails, not measurements - hence the deliberately loose windows.
EXPECT_RZPZ_UM = (6.0, 13.0)     # plateau over roughly the first half of the axis
EXPECT_HZ_PEAK_UM = (20.0, 32.0)  # peak in the hypertrophic zone, published value ~26
MIN_CELLS = 2000


def _canon(raw_axes, from_h5):
    """Return principal axes as (n, 3, 3) with axes[i, k, :] the k-th unit axis of cell i.

    MATLAB stores pca() coefficients with the axes as COLUMNS. scipy.io hands the matrix back
    unchanged, so an axis is a column; h5py hands back the transpose, so an axis is a row.
    Getting this backwards silently rotates every cell and the validation guard is the only
    thing that would catch it - so it is done once, here, and nowhere else.
    """
    import numpy as np
    A = np.asarray(raw_axes, float)
    return A if from_h5 else np.transpose(A, (0, 2, 1))


def load_tile(path):
    """Per-cell arrays from one 3D MAPs (Characteristics).mat tile.

    The deposit mixes MATLAB v5 and v7.3 files in the same directory - 15 of the 21 tiles are
    v5 and open only with scipy, 6 are v7.3 (HDF5) and open only with h5py. Reading the
    directory with either library alone silently drops two thirds of the sample.
    """
    import numpy as np
    with open(path, "rb") as fh:
        is_h5 = b"MATLAB 7.3" in fh.read(64)

    if is_h5:
        import h5py
        with h5py.File(path, "r") as f:
            if "G/cel" not in f:
                return None
            g = f["G/cel"]
            n = g["volume"].shape[1]
            if n == 0:
                return None
            out = {"volume": np.asarray(g["volume"][0, :], float),
                   "surface_area": np.asarray(g["surface_area"][0, :], float),
                   "sphericity": np.asarray(g["sphericity"][0, :], float),
                   "pc_range": np.asarray(g["PC_range"][:, :], float),
                   "centroid": np.asarray(g["centroids"][:, :], float),
                   "ell_radii": np.asarray(g["ellipsoid_radii"][:, :], float)}
            for key, dst in (("PCA_coeff", "pca_axes"), ("ellipsoid_evecs", "ell_axes")):
                refs = g[key]
                M = np.empty((n, 3, 3), float)
                for i in range(n):
                    M[i] = np.asarray(f[refs[0, i]])
                out[dst] = _canon(M, True)
        return out

    import scipy.io as sio
    m = sio.loadmat(path, struct_as_record=False, squeeze_me=True)
    if "G" not in m or not hasattr(m["G"], "cel"):
        return None
    c = m["G"].cel
    n = np.asarray(c.volume).size
    if n == 0:
        return None
    stack = lambda seq: np.stack([np.asarray(x, float) for x in np.atleast_1d(seq)])
    return {"volume": np.asarray(c.volume, float).ravel(),
            "surface_area": np.asarray(c.surface_area, float).ravel(),
            "sphericity": np.asarray(c.sphericity, float).ravel(),
            "pc_range": np.asarray(c.PC_range, float).reshape(n, 3).T,
            "centroid": np.asarray(c.centroids, float).reshape(n, 3).T,
            "ell_radii": np.asarray(c.ellipsoid_radii, float).reshape(n, 3).T,
            "pca_axes": _canon(stack(c.PCA_coeff), False),
            "ell_axes": _canon(stack(c.ellipsoid_evecs), False)}


def tile_origins(xlsx):
    """{'POS1': (x, y, z_start), ...} in um, from the deposit's Tile_coordinates.xlsx.

    Cell centroids are LOCAL to each 900x900 px tile (0-175 um in x and y). Without these
    offsets every tile's cells pile up at the same coordinates and the P-D profile is a
    scramble of 21 stacks laid on top of one another.
    """
    import re, zipfile, xml.etree.ElementTree as ET
    NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    z = zipfile.ZipFile(xlsx)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        r = ET.fromstring(z.read("xl/sharedStrings.xml"))
        shared = ["".join(t.text or "" for t in si.iter() if t.tag.endswith("}t"))
                  for si in r if si.tag.endswith("}si")]
    sheet = [n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml", n)][0]
    out = {}
    for row in ET.fromstring(z.read(sheet)).iter(f"{NS}row"):
        vals = []
        for cell in row:
            v = cell.find(f"{NS}v")
            val = v.text if v is not None else ""
            if cell.get("t") == "s" and val != "":
                val = shared[int(val)]
            vals.append(val)
        if len(vals) >= 4 and isinstance(vals[0], str) and "POS" in vals[0].upper():
            try:
                out[vals[0].upper().split("_")[-1]] = tuple(float(x) for x in vals[1:4])
            except ValueError:
                continue
    return out


def axis_from_alignment(R, convention):
    """The proximal-distal direction expressed in raw tile coordinates.

    The registration matrix maps raw coordinates into the frame where P-D is the global z.
    Which of R's row 3 / column 3 is the P-D direction depends on whether MATLAB applied it
    as R*v or v*R, and the .dat file does not say. Both are tried and the one that produces
    a monotone volume gradient - the defining property of the differentiation axis - is kept.
    """
    import numpy as np
    return np.asarray(R[2, :] if convention == "row" else R[:, 2], float)


def main():
    import numpy as np
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="directory of c_n_pos*.mat tiles")
    ap.add_argument("--align", default=None, help="Alignment_matrix.dat (default: in --dir)")
    ap.add_argument("--bins", type=int, default=40)
    a = ap.parse_args()

    align_path = a.align or os.path.join(a.dir, "Alignment_matrix.dat")
    R = np.array([[float(x) for x in line.split()]
                  for line in open(align_path) if line.strip()])
    assert R.shape == (3, 3), f"alignment matrix is {R.shape}, expected 3x3"

    tiles = sorted(glob.glob(os.path.join(a.dir, "*Characteristics*.mat")))
    if not tiles:
        print(f"no (Characteristics).mat tiles under {a.dir}", file=sys.stderr)
        return 2
    print(f"{len(tiles)} tiles")

    origins = tile_origins(os.path.join(a.dir, "Tile_coordinates.xlsx"))
    print(f"{len(origins)} tile origins")

    cells = []
    for t in tiles:
        base = os.path.basename(t)
        d = load_tile(t)
        if d is None:
            print(f"  {base}: no cells, skipped")
            continue
        key = "POS" + str(int("".join(ch for ch in base.split("(")[0] if ch.isdigit())))
        if key not in origins:
            print(f"  {base}: NO TILE ORIGIN for {key} - skipped rather than mis-placed")
            continue
        d["centroid"] = d["centroid"] + np.asarray(origins[key], float)[:, None]
        d["tile"] = base
        cells.append(d)
        print(f"  {base}: {len(d['volume'])} cells at {origins[key]}")

    vol = np.concatenate([d["volume"] for d in cells])
    sa = np.concatenate([d["surface_area"] for d in cells])
    sph = np.concatenate([d["sphericity"] for d in cells])
    pcr = np.concatenate([d["pc_range"] for d in cells], axis=1)          # (3, N)
    cen = np.concatenate([d["centroid"] for d in cells], axis=1)          # (3, N)
    erad = np.concatenate([d["ell_radii"] for d in cells], axis=1)        # (3, N)
    pax = np.concatenate([d["pca_axes"] for d in cells], axis=0)          # (N, 3, 3)
    eax = np.concatenate([d["ell_axes"] for d in cells], axis=0)          # (N, 3, 3)
    N = vol.size
    print(f"\n{N} cells total")
    if N < MIN_CELLS:
        print(f"REFUSING: {N} cells is below the {MIN_CELLS} needed for a zone profile.")
        return 1

    # ---- pick the P-D axis convention by the monotone volume gradient ----------------
    best = None
    for conv in ("row", "col"):
        z = axis_from_alignment(R, conv)
        pos = z @ cen
        q = (pos - pos.min()) / max(np.ptp(pos), 1e-9)
        lo = vol[q < 0.25].mean()
        hi = vol[q > 0.75].mean()
        print(f"  convention {conv}: mean volume first quartile {lo:8.1f} um^3, "
              f"last {hi:8.1f} um^3, ratio {hi/max(lo,1e-9):5.2f}")
        r = max(hi / max(lo, 1e-9), lo / max(hi, 1e-9))
        if best is None or r > best[0]:
            best = (r, conv, z, pos, hi > lo)
    _, conv, zaxis, pos, increasing = best
    if not increasing:                  # orient so that position 1 is the hypertrophic end
        zaxis = -zaxis
        pos = -pos
    q = (pos - pos.min()) / max(np.ptp(pos), 1e-9)
    print(f"  -> using convention '{conv}', P-D axis {np.round(zaxis, 4)}")

    # ---- the three quantities ---------------------------------------------------------
    # 1. axial extent: rubin2021's metric. Bounding box of the fitted ellipsoid along P-D.
    #    For an ellipsoid with semi-axes a_i along unit vectors u_i, its support along z is
    #    sqrt(sum_i a_i^2 (u_i.z)^2), so the box height is twice that.
    uz_e = np.einsum("nij,j->ni", eax, zaxis)          # (N,3) components of ellipsoid axes
    axial = 2.0 * np.sqrt((erad.T ** 2 * uz_e ** 2).sum(axis=1))
    # 2. intrinsic length: the cell's extent along its OWN long axis. No orientation in it.
    L1 = pcr[0, :]
    # 3. alignment: |cos| between the long axis and P-D.
    uz_p = np.einsum("nij,j->ni", pax, zaxis)
    align = np.abs(uz_p[:, 0])

    # ---- VALIDATION GUARD: reproduce the published DU profile before reporting ---------
    edges = np.linspace(0, 1, a.bins + 1)
    idx = np.clip(np.digitize(q, edges) - 1, 0, a.bins - 1)

    def prof(v):
        return np.array([v[idx == b].mean() if (idx == b).sum() >= 20 else np.nan
                         for b in range(a.bins)])

    p_axial = prof(axial)
    first_half = np.nanmean(p_axial[: a.bins // 2])
    peak = np.nanmax(p_axial[a.bins // 2:])
    print(f"\nreconstruction check against rubin2021 Supplementary Fig. 4A (distal ulna):")
    print(f"  mean bounding-box height over the first half of the axis : {first_half:6.2f} um "
          f"(published trace sits near 9-10)")
    print(f"  peak bounding-box height in the second half              : {peak:6.2f} um "
          f"(published peak near 26)")
    ok = (EXPECT_RZPZ_UM[0] <= first_half <= EXPECT_RZPZ_UM[1]
          and EXPECT_HZ_PEAK_UM[0] <= peak <= EXPECT_HZ_PEAK_UM[1])
    if not ok:
        print(f"\n{'='*74}\nREFUSING TO REPORT THE DECOMPOSITION.\n\nThe reconstructed profile "
              f"does not reproduce rubin2021's own published curve for this\nsample, so the "
              f"registration or the axis convention is wrong and any split of\nthis profile "
              f"would be a split of noise. Expected roughly {EXPECT_RZPZ_UM} um across the\n"
              f"first half and a peak in {EXPECT_HZ_PEAK_UM} um; got {first_half:.2f} and "
              f"{peak:.2f}.\n{'='*74}")
        return 1
    print("  -> reproduced. Proceeding.")

    # ---- the decomposition -------------------------------------------------------------
    p_L1, p_al, p_vol, p_sph = prof(L1), prof(align), prof(vol), prof(sph)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "du_profile.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["bin", "pd_position", "n_cells", "axial_extent_um",
                    "intrinsic_long_axis_um", "alignment_abs_cos", "volume_um3", "sphericity"])
        for b in range(a.bins):
            w.writerow([b, round((edges[b] + edges[b + 1]) / 2, 4), int((idx == b).sum()),
                        *[None if np.isnan(x) else round(float(x), 4)
                          for x in (p_axial[b], p_L1[b], p_al[b], p_vol[b], p_sph[b])]])

    lo = slice(0, a.bins // 4)                       # resting / early proliferative
    hz = int(np.nanargmax(p_axial))                  # the hypertrophic peak bin
    f_axial = p_axial[hz] / np.nanmean(p_axial[lo])
    f_L1 = p_L1[hz] / np.nanmean(p_L1[lo])
    f_al = p_al[hz] / np.nanmean(p_al[lo])
    f_vol = p_vol[hz] / np.nanmean(p_vol[lo])

    print(f"\n{'quantity':34s} {'first quarter':>14s} {'HZ peak':>10s} {'fold':>7s}")
    for nm, p, f in (("axial extent (their metric), um", p_axial, f_axial),
                     ("intrinsic long axis, um", p_L1, f_L1),
                     ("alignment with P-D, |cos|", p_al, f_al),
                     ("volume, um^3", p_vol, f_vol)):
        print(f"  {nm:32s} {np.nanmean(p[lo]):14.3f} {p[hz]:10.3f} {f:7.3f}")

    # ---- exact counterfactual decomposition -------------------------------------------
    # axial extent = 2*sqrt(sum_i a_i^2 (u_i.z)^2) is NOT the product L1*|cos| except for a
    # needle, so the log-shares of those two factors do not partition anything. The clean
    # split is a swap: give the hypertrophic cells the resting zone's ORIENTATIONS while
    # keeping their own SHAPES, and vice versa. Orientations are drawn with replacement from
    # the other zone's pool, so the swap is a distribution swap, not a pairing.
    # Zone windows with a CELL-COUNT FLOOR, not a threshold on the peak. The peak bin holds
    # only 24 cells; a swap between orientation DISTRIBUTIONS estimated from 24 cells is not
    # a measurement. The HZ window therefore grows downward from the peak bin until it holds
    # at least MIN_ZONE_CELLS, and the resulting window is printed so the reader can see how
    # much of the profile it covers.
    MIN_ZONE_CELLS = 300
    rz_m = idx < a.bins // 4
    b_hi = hz
    b_lo = hz
    while True:
        hz_m = (idx >= b_lo) & (idx <= b_hi)
        if hz_m.sum() >= MIN_ZONE_CELLS or b_lo <= a.bins // 2:
            break
        b_lo -= 1
    print(f"\n  zone windows: RZ = bins 0-{a.bins//4-1} ({int(rz_m.sum())} cells, "
          f"P-D 0.00-{(a.bins//4)/a.bins:.2f}); HZ = bins {b_lo}-{b_hi} "
          f"({int(hz_m.sum())} cells, P-D {b_lo/a.bins:.2f}-{(b_hi+1)/a.bins:.2f})")
    print(f"  mean alignment |cos| : RZ {align[rz_m].mean():.3f}  HZ {align[hz_m].mean():.3f}"
          f"   (0.500 is the value for uniformly random axes in 3D)")

    def ext(radii, axes):
        uz = np.einsum("nij,j->ni", axes, zaxis)
        return 2.0 * np.sqrt((radii ** 2 * uz ** 2).sum(axis=1))

    rng = np.random.default_rng(0)
    r_rz, r_hz = erad.T[rz_m], erad.T[hz_m]
    a_rz, a_hz = eax[rz_m], eax[hz_m]
    draw = lambda pool, n: pool[rng.integers(0, len(pool), n)]
    base = ext(r_rz, a_rz).mean()
    shape_only = ext(r_hz, draw(a_rz, hz_m.sum())).mean()   # HZ shapes, RZ orientations
    orient_only = ext(r_rz, draw(a_hz, rz_m.sum())).mean()  # RZ shapes, HZ orientations
    both = ext(r_hz, a_hz).mean()
    print(f"\n  COUNTERFACTUAL SWAP  (n_RZ={int(rz_m.sum())}, n_HZ={int(hz_m.sum())})")
    print(f"    resting zone, as observed                      {base:8.3f} um")
    print(f"    HZ cell shapes wearing RESTING orientations    {shape_only:8.3f} um   "
          f"x{shape_only/base:5.3f}   <- elongation alone")
    print(f"    resting shapes wearing HYPERTROPHIC orients    {orient_only:8.3f} um   "
          f"x{orient_only/base:5.3f}   <- realignment alone")
    print(f"    hypertrophic zone, as observed                 {both:8.3f} um   "
          f"x{both/base:5.3f}")
    inter = (both / base) / ((shape_only / base) * (orient_only / base))
    print(f"    interaction                                                x{inter:5.3f}")
    sh_pct = 100 * np.log(shape_only / base) / np.log(both / base)
    or_pct = 100 * np.log(orient_only / base) / np.log(both / base)
    print(f"\n    share of the log rise from ELONGATION   {sh_pct:6.1f} %")
    print(f"    share from REALIGNMENT                 {or_pct:6.1f} %")
    print(f"    share from their interaction           {100-sh_pct-or_pct:6.1f} %")

    # ---- is the enlargement isotropic? -------------------------------------------------
    # If the cell scales by the same factor on all three axes, then volume^(1/3) and the long
    # axis rise by the same factor, height and volume carry the same information, and the only
    # thing separating them as predictors is which is measured better. If the axial direction
    # is favoured, they carry different information and the distinction is real.
    p_L = [prof(pcr[k, :]) for k in range(3)]
    f_L = [p_L[k][hz] / np.nanmean(p_L[k][lo]) for k in range(3)]
    print(f"\n  ISOTROPY CHECK, first quarter -> HZ peak bin")
    for k in range(3):
        print(f"    principal axis {k+1} length fold        x{f_L[k]:5.3f}   "
              f"({np.nanmean(p_L[k][lo]):6.2f} -> {p_L[k][hz]:6.2f} um)")
    print(f"    cube root of the volume fold        x{f_vol ** (1/3):5.3f}")
    print(f"    sphericity                          {np.nanmean(p_sph[lo]):6.3f} -> "
          f"{p_sph[hz]:6.3f}")

    json.dump({
        "sample": os.path.basename(os.path.normpath(a.dir)),
        "n_cells": int(N), "bins": a.bins, "pd_axis_convention": conv,
        "pd_axis_in_raw_coords": [round(float(x), 6) for x in zaxis],
        "validation": {"first_half_axial_um": round(float(first_half), 3),
                       "hz_peak_axial_um": round(float(peak), 3),
                       "expected_first_half": list(EXPECT_RZPZ_UM),
                       "expected_peak": list(EXPECT_HZ_PEAK_UM),
                       "reproduced_published_profile": True},
        "fold_first_quarter_to_hz_peak": {
            "axial_extent": round(float(f_axial), 4),
            "intrinsic_long_axis": round(float(f_L1), 4),
            "alignment": round(float(f_al), 4),
            "volume": round(float(f_vol), 4)},
        "counterfactual_swap": {
            "n_rz": int(rz_m.sum()), "n_hz": int(hz_m.sum()),
            "rz_observed_um": round(float(base), 3),
            "hz_shapes_with_rz_orientations_um": round(float(shape_only), 3),
            "rz_shapes_with_hz_orientations_um": round(float(orient_only), 3),
            "hz_observed_um": round(float(both), 3),
            "fold_elongation_alone": round(float(shape_only / base), 4),
            "fold_realignment_alone": round(float(orient_only / base), 4),
            "fold_observed": round(float(both / base), 4),
            "fold_interaction": round(float(inter), 4),
            "log_share_elongation_pct": round(float(sh_pct), 2),
            "log_share_realignment_pct": round(float(or_pct), 2),
            "log_share_interaction_pct": round(float(100 - sh_pct - or_pct), 2)},
        "CAVEAT_ALIGNMENT": "|cos(PC1, P-D)| is entangled with cell shape CLASS: in an oblate "
                            "(disc-shaped) cell the long axis is necessarily in the plane of "
                            "the plate, so a low value is partly definitional rather than a "
                            "statement about rotation. The counterfactual swap above does not "
                            "have this problem - it exchanges whole orientation frames between "
                            "zones while holding each cell's own radii fixed.",
        "axis_length_folds": [round(float(x), 4) for x in f_L],
        "cube_root_volume_fold": round(float(f_vol ** (1 / 3)), 4),
        "SCOPE": "ONE growth plate - distal ulna DU_S84_m3_wt, the only sample in the "
                 "rubin2021 Figshare deposit. This is a WITHIN-plate decomposition along the "
                 "differentiation axis. It is NOT the three-plate predictor comparison that "
                 "produced rubin2021's conclusion, and it cannot say whether the DU-vs-PT "
                 "hypertrophic height difference is size or alignment. That needs the "
                 "proximal and distal tibia samples.",
        "WARNING": "A within-plate RZ-to-HZ contrast is a DIFFERENTIATION axis. hunziker1989's "
                   "comparison is the same zone at two growth rates, and rubin2021's is between "
                   "plates. Neither is this. What this establishes is only whether the "
                   "orientation confound in the height metric is large enough to matter.",
    }, open(os.path.join(OUT, "du_decomposition.json"), "w"), indent=1)
    print(f"\nwrote {OUT}/du_profile.csv and du_decomposition.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
