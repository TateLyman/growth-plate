#!/usr/bin/env python3
"""
flow_model.py - PARAMETER-FLOW CONSISTENCY MODEL for the Human Growth System Atlas
==================================================================================

WHAT THIS IS
------------
This is NOT a mechanistic ODE model of the growth plate. The atlas's own parameter
record does not support one: 1264 of ~1350 recorded quantitative rows rest on a single
source, human growth plate pO2 has never been measured, and the single most important
human kinetic constant (proliferative cell cycle time) is a DERIVED quantity, not an
observation.

What this IS: an auditable arithmetic chain that carries measured parameters, with their
provenance and reliability class, along the critical path

    proliferative-zone cell cycle time  ->  column production rate [cells/day]
      -> terminal hypertrophic cell length increment [um/cell]
      -> hypertrophic + matrix + division partition -> total elongation [um/day]
      -> mineralisation / chondro-osseous removal steady state (closure check)
      -> mechanical modulation
      -> um/day -> cm/yr
      -> site share -> bone velocity -> stature velocity

and STOPS, LOUDLY, at every step where the conversion factor the arithmetic needs has
never been measured. It names the missing parameter and the atlas gap that records it.

A model that runs end-to-end by quietly inventing a factor is worse than one that stops.

MODES
-----
  strict       (default) Raise MissingParameter at the first unmeasured factor.
  closure      Run the chain BACKWARDS from a measured organism/site target to solve for
               the value the missing factor MUST take. Invents nothing; produces a
               falsifiable prediction and states what would measure it.
  sensitivity  Monte Carlo with DECLARED spans for the unmeasured factors. Every declared
               span is stamped DECLARED_SPAN in the output and justified by the atlas row
               it is bracketed from. Ranks parameters by how much output uncertainty each
               would remove IF MEASURED (freeze-one-input variance reduction).

USAGE
-----
  python3 flow_model.py --site human_distal_femur --age 8 --sex male
  python3 flow_model.py --site human_distal_femur --age 8 --sex male --mode closure
  python3 flow_model.py --all
  python3 flow_model.py --mode sensitivity --n 40000
  python3 flow_model.py --consistency          # run against organism_targets.csv
  python3 flow_model.py --selftest             # unit-conversion assertions only

Author: Phase 6 quantitative closure. No number in this file is invented; every numeric
input is pulled from atlas/quant/parameters.csv by param_id at run time.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Callable, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
QUANT = os.path.abspath(os.path.join(HERE, ".."))
ATLAS = os.path.abspath(os.path.join(QUANT, ".."))
PARAM_CSV = os.path.join(QUANT, "parameters.csv")
TARGET_CSV = os.path.join(QUANT, "organism_targets.csv")
GAPS_YAML = os.path.join(ATLAS, "gaps", "gaps.yaml")

# =============================================================================
# 1. UNITS.  Every conversion in this model is declared here, exactly once, and
#    asserted.  Nothing downstream is allowed to convert units inline.
# =============================================================================

HOURS_PER_DAY = 24.0
DAYS_PER_YEAR = 365.25          # tropical year; the 0.07% difference from 365 is below
                                # every uncertainty in this model but is stated anyway
UM_PER_CM = 10_000.0
FL_PER_UM3 = 1.0                # 1 femtolitre == 1 cubic micrometre, exactly
MPA_PER_KPA = 1e-3


def hours_to_days(h: float) -> float:
    assert h > 0, f"cell cycle time must be positive, got {h} h"
    d = h / HOURS_PER_DAY
    assert abs(d * HOURS_PER_DAY - h) < 1e-9, "hours<->days round trip failed"
    return d


def days_to_hours(d: float) -> float:
    assert d > 0
    return d * HOURS_PER_DAY


def um_per_day_to_cm_per_yr(u: float) -> float:
    """um/day -> cm/yr.  x * 365.25 / 10000."""
    cm = u * DAYS_PER_YEAR / UM_PER_CM
    # round trip
    assert abs(cm_per_yr_to_um_per_day(cm) - u) < 1e-9, "um/day<->cm/yr round trip failed"
    return cm


def cm_per_yr_to_um_per_day(c: float) -> float:
    return c * UM_PER_CM / DAYS_PER_YEAR


def fl_to_um3(v: float) -> float:
    """Femtolitres to cubic micrometres.  1 fl = 1e-15 L = 1e-18 m^3 = 1 um^3."""
    assert v > 0
    return v * FL_PER_UM3


def percent_to_fraction(p: float) -> float:
    assert 0.0 <= p <= 100.0, f"percent out of range: {p}"
    return p / 100.0


def kpa_to_mpa(k: float) -> float:
    return k * MPA_PER_KPA


def _selftest_units() -> None:
    """Assertions on the unit layer, plus one cross-check against the atlas itself."""
    assert abs(hours_to_days(30.9) - 1.2875) < 1e-9
    assert abs(days_to_hours(20.0) - 480.0) < 1e-9
    assert abs(um_per_day_to_cm_per_yr(38.0) - 1.38795) < 1e-5
    assert abs(cm_per_yr_to_um_per_day(1.4) - 38.33) < 0.01
    assert fl_to_um3(14000.0) == 14000.0
    assert abs(percent_to_fraction(59.0) - 0.59) < 1e-12
    assert abs(kpa_to_mpa(380.0) - 0.380) < 1e-12
    # ATLAS CROSS-CHECK: kember1976 records BOTH 1.4 cm/year (p_456dd2428e) and 38 um/day
    # (p_1c34689beb) for the same plate.  If our conversion is right the two rows must agree.
    reg = registry()
    a = reg.get("p_456dd2428e").num          # 1.4  cm/year
    b = reg.get("p_1c34689beb").num          # 38   um/day
    pred = um_per_day_to_cm_per_yr(b)  # 1.388 cm/yr
    rel = abs(pred - a) / a
    assert rel < 0.02, (f"atlas rows p_456dd2428e/p_1c34689beb disagree by {rel:.1%} - either the "
                        f"conversion or one of the rows is wrong")
    return rel


# =============================================================================
# 2. PARAMETER REGISTRY.  Every input is fetched by param_id from parameters.csv
#    and carries source_ref, spread and reliability_class.
# =============================================================================

# Reliability classification reproduced EXACTLY from atlas/tools/compile_query.py
# (Phase 2e policy).  single_source_point_no_uncertainty is the RISK class.
_SPREAD_RE = re.compile(
    r"\brange\b|\bspread\b|varies|disagree|conflict|order of magnitude|"
    r"method-dependent|depend\w* on (method|technique)|differs? (between|across)|"
    r"inconsisten", re.I)
_RANGE_VAL = re.compile(r"\d\s*[-–]\s*\d")


def _norm_param(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def _first_number(v) -> Optional[float]:
    m = re.search(r"[-+]?\d*\.?\d+", str(v).replace(",", ""))
    return float(m.group()) if m else None


@dataclass
class Param:
    param_id: str
    layer: str
    parameter: str
    raw_value: str
    num: Optional[float]
    lo: Optional[float]
    hi: Optional[float]
    unit: str
    conditions: str
    species: str
    site: str
    age: str
    sex: str
    source_ref: str
    uncertainty: str
    notes: str
    reliability_class: str

    @property
    def risk(self) -> bool:
        return self.reliability_class == "single_source_point_no_uncertainty"

    def cite(self) -> str:
        flag = "  [!RISK single_source_point_no_uncertainty]" if self.risk else ""
        return (f"{self.param_id} {self.parameter} = {self.raw_value} {self.unit} "
                f"({self.species}; {self.source_ref}; {self.reliability_class}){flag}")

    def span(self) -> tuple[float, float]:
        """Recorded spread if the row has one, else the point value twice."""
        if self.lo is not None and self.hi is not None and self.hi > self.lo:
            return self.lo, self.hi
        # a stated range inside the uncertainty text, e.g. "range 9.2-23.9%/0.1 MPa"
        m = re.search(r"(\d+\.?\d*)\s*[-–]\s*(\d+\.?\d*)", self.uncertainty or "")
        if m:
            a, b = float(m.group(1)), float(m.group(2))
            if b > a:
                return a, b
        if self.num is None:
            raise MissingParameter(self.parameter, None,
                                   f"row {self.param_id} carries no numeric value "
                                   f"(raw value: {self.raw_value!r})", None)
        return self.num, self.num


class _Registry:
    def __init__(self, path: str = PARAM_CSV):
        self.rows: dict[str, Param] = {}
        self.class_counts: Counter = Counter()
        raw = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
        byname = defaultdict(list)
        for r in raw:
            byname[_norm_param(r["parameter"])].append(r)
        multi = {k for k, v in byname.items()
                 if len({str(x["source_ref"]) for x in v}) > 1}
        for r in raw:
            txt = " ".join(str(r.get(f) or "") for f in ("uncertainty", "conditions", "notes"))
            if str(r.get("superseded_model") or "").strip().lower() in ("true", "1", "yes"):
                c = "superseded"
            elif str(r.get("value_unverified") or "").strip().lower() in ("true", "1", "yes"):
                c = "unverified"
            elif _norm_param(r["parameter"]) in multi:
                c = "multi_source"
            elif _RANGE_VAL.search(str(r["value"])):
                c = "range_value"
            elif _SPREAD_RE.search(txt):
                c = "spread_documented"
            elif str(r.get("uncertainty") or "").strip() not in ("", "not reported", "none", "-"):
                c = "single_source_with_uncertainty"
            else:
                c = "single_source_point_no_uncertainty"
            self.class_counts[c] += 1
            lo = _first_number(r["value_min"]) if str(r["value_min"]).strip() else None
            hi = _first_number(r["value_max"]) if str(r["value_max"]).strip() else None
            self.rows[r["param_id"]] = Param(
                param_id=r["param_id"], layer=r["layer"], parameter=r["parameter"],
                raw_value=r["value"], num=_first_number(r["value"]), lo=lo, hi=hi,
                unit=r["unit"], conditions=r["conditions"], species=r["species"],
                site=r["site"], age=r["age"], sex=r["sex"], source_ref=r["source_ref"],
                uncertainty=r["uncertainty"], notes=r["notes"], reliability_class=c)

    def get(self, pid: str) -> Param:
        if pid not in self.rows:
            raise KeyError(f"param_id {pid} is not in {PARAM_CSV}")
        return self.rows[pid]


_REG: Optional[_Registry] = None


def registry() -> _Registry:
    global _REG
    if _REG is None:
        _REG = _Registry()
    return _REG


# =============================================================================
# 3. THE FAILURE MECHANISM.  A required factor that has never been measured must
#    stop the chain and name itself.  It must NEVER be defaulted.
# =============================================================================

class MissingParameter(Exception):
    def __init__(self, name: str, unit: Optional[str], why: str,
                 gap_id: Optional[str], nearest: str = "", step: str = ""):
        self.name, self.unit, self.why = name, unit, why
        self.gap_id, self.nearest, self.step = gap_id, nearest, step
        super().__init__(self.render())

    def render(self) -> str:
        L = ["", "=" * 78,
             "MODEL HALTED - REQUIRED CONVERSION FACTOR HAS NEVER BEEN MEASURED",
             "=" * 78,
             f"  step            : {self.step}",
             f"  missing factor  : {self.name}" + (f"  [{self.unit}]" if self.unit else ""),
             f"  why it is needed: {self.why}"]
        if self.gap_id:
            L.append(f"  atlas gap       : {self.gap_id}")
        if self.nearest:
            L.append(f"  nearest evidence: {self.nearest}")
        L += ["  NOT SUBSTITUTED. No default was used. The chain stops here.", "=" * 78]
        return "\n".join(L)


# The unmeasured factors this chain needs, each bound to its gap register entry.
MISSING = {
    "h_term_um": dict(
        name="terminal hypertrophic chondrocyte HEIGHT along the growth axis",
        unit="um/cell",
        why=("cells/day must be multiplied by the axial length each terminal cell "
             "contributes to convert a cell flux into a length flux. The atlas records "
             "terminal hypertrophic VOLUME (mouse, cooper2013: 5000-23000 fl) and a "
             "4-fold rat height INCREASE (hunziker1987, p_9137beb338) but no absolute axial "
             "height in um for any species, and no transverse cross-sectional area with "
             "which volume could be converted to height."),
        gap_id="g_l1arch_009",
        nearest="breur1991, cooper2013, thurston1985"),
    "A_x_um2": dict(
        name="hypertrophic chondrocyte transverse cross-sectional area",
        unit="um^2",
        why=("the only route from the recorded volumes (fl) to an axial height. Not "
             "recorded for any species in parameters.csv."),
        gap_id="g_l1arch_009",
        nearest="cooper2013"),
    "f_hyp_human": dict(
        name="human elongation partition (division / matrix / hypertrophy)",
        unit="fraction",
        why=("hypertrophic length increment must be divided by the hypertrophic share "
             "to recover TOTAL elongation. Only rat values exist: 9/32/59 % in the fast "
             "proximal tibia and 44 % hypertrophy / 49 % matrix in the slow proximal "
             "radius (wilsman1996, p_677f954703-p_30bbb4b516). Substituting the rat partition for a "
             "human plate is a species transfer, not a measurement."),
        gap_id="g_l1arch_001",
        nearest="wilsman1996, hunziker1989, breur1991, byers2000"),
    "sigma_physis_MPa": dict(
        name="in vivo compressive stress across a human physis",
        unit="MPa",
        why=("the Stokes growth-stress coefficient (17.1 %/0.1 MPa, p_e8cec37611) is a "
             "sensitivity, not a growth rate. Applying it needs the stress. "
             "p_15641b1682 records the human value explicitly as NOT MEASURED - FE model "
             "output only."),
        gap_id="g_l6mech_003",
        nearest="hucke2023, rodrguez2025, stokes2006"),
    "k_stress_human": dict(
        name="human physeal growth-rate sensitivity to sustained stress",
        unit="% per 0.1 MPa",
        why=("the 17.1 %/0.1 MPa coefficient is pooled rat/rabbit/calf (stokes2006). "
             "No human experiment applying a known stress and measuring the growth "
             "response exists."),
        gap_id="g_l6mech_001",
        nearest="stokes2006, tolk2026, hucke2023"),
    "E_zone_ratio": dict(
        name="zonal stiffness ratio of the human growth plate (which zone is stiffest)",
        unit="dimensionless",
        why=("needed to distribute a plate-level stress onto the growth-controlling "
             "zone. The recorded values span three orders of magnitude (rabbit "
             "380-690 kPa, p_1f7d5385aa; human sharp-tip AFM 130.7 and 416.2 MPa, p_d7e6e017fa/7) "
             "AND THE GRADIENT DIRECTION DISAGREES: xie2025 makes the hypertrophic zone "
             "3.2x STIFFER than resting, sergerie2009 makes proliferative+hypertrophic "
             "0.33-0.5x SOFTER than reserve. The sign of the stress concentration is "
             "unknown."),
        gap_id="g_l5matrix_008",
        nearest="sergerie2009, eckstein2022, radhakrishnan2004, xie2025, williams2001"),
    "v_vertebral_per_plate": dict(
        name="per-plate vertebral growth rate",
        unit="mm/yr",
        why=("stature velocity is the sum over lower limb + spine + skull base. The "
             "human vertebral column carries >130 growth plates (p_0296c00c3e) and the "
             "per-plate rate is recorded as NOT REPORTED (p_d83b4b691e, dimeglio2020). "
             "Without it no plate-level model can be summed to stature."),
        gap_id="g_l1arch_011",
        nearest="dimeglio2020, pritchett1992"),
    "v_tibia_absolute": dict(
        name="absolute human tibial elongation rate",
        unit="cm/yr",
        why=("the atlas records the proximal tibial SHARE of tibial growth (57 %, "
             "p_9325eb32b4) but no absolute tibial cm/yr, so the tibial term of the stature "
             "sum cannot be formed from measured rows."),
        gap_id="g_l1arch_011",
        nearest="pritchett1992"),
    "T_c_human_measured": dict(
        name="measured human proliferative-zone cell cycle time",
        unit="days",
        why=("the 20-day human figure (p_61f79e4fdb, kember1976) is explicitly a DERIVED "
             "quantity - derived from column count and growth rate, i.e. from the very "
             "output this chain is trying to predict. Using it makes the human chain "
             "circular. The measured rat value is 30.9 h (p_206d079d10), a ~16-fold gap."),
        gap_id="g_l1arch_002",
        nearest="kember1976, thurston1985, wilsman1996a"),
    "N_p_column": dict(
        name="cells per proliferative column for this species/site",
        unit="cells",
        why=("cell production per column = cells per proliferative column / cell cycle "
             "time. parameters.csv records a cells-per-column value only for human "
             "(24 cells, p_18c99a7ad2, kember1976, distal femur). No rodent or other-species "
             "column count is recorded, and no site- or age-resolved human value exists, "
             "so production cannot be formed for this site."),
        gap_id="g_l1arch_012",
        nearest="kember1976, hunziker1987, wilsman1996a"),
    "pO2_human_zonal": dict(
        name="human growth plate zonal oxygen tension",
        unit="mmHg",
        why=("recorded as NOT MEASURED (p_13aaeefc45). Any metabolic or matrix-synthesis "
             "sub-model requires it; this chain therefore treats matrix synthesis as a "
             "partition share rather than a rate, which is a structural limitation, not "
             "a solved problem."),
        gap_id="g_l1arch_007",
        nearest="brighton1971, zhang2023_2, schipani2001"),
}


def fail(key: str, step: str) -> None:
    m = MISSING[key]
    raise MissingParameter(m["name"], m["unit"], m["why"], m["gap_id"],
                           m["nearest"], step)


# =============================================================================
# 4. DECLARED SPANS.  Used ONLY in --mode sensitivity, which must be asked for
#    explicitly.  Each is a hypothesis interval, stamped as such, justified by
#    the atlas row it is bracketed from.  None of these is a measurement.
# =============================================================================

@dataclass
class DeclaredSpan:
    key: str
    lo: float
    hi: float
    unit: str
    status: str          # MEASURED_SPREAD | DECLARED_SPAN (unmeasured)
    basis: str
    gap_id: Optional[str] = None

    @property
    def log_range(self) -> float:
        return math.log(self.hi / self.lo) if self.lo > 0 else float("nan")


def declared_spans() -> dict[str, DeclaredSpan]:
    r = registry()
    S: dict[str, DeclaredSpan] = {}

    # --- measured spreads, taken straight off the recorded rows -------------
    lo, hi = r.get("p_206d079d10").num, r.get("p_69f9e770de").num           # 30.9 - 76.3 h, rat
    S["T_c_rat_h"] = DeclaredSpan("T_c_rat_h", lo, hi, "h", "MEASURED_SPREAD",
        "wilsman1996a p_206d079d10/p_69f9e770de: 2.5-fold spread across four plates of one 28-day rat")

    S["f_hyp"] = DeclaredSpan("f_hyp", percent_to_fraction(r.get("p_03591cde3d").num),
        percent_to_fraction(r.get("p_53c796311c").num), "fraction", "MEASURED_SPREAD",
        "wilsman1996 p_03591cde3d/p_53c796311c: 44 % (slow proximal radius) to 59 % (fast proximal "
        "tibia). The human value is a gap.", "g_l1arch_001")

    klo, khi = r.get("p_e8cec37611").span()                            # 9.2 - 23.9 %/0.1 MPa
    S["k_stress"] = DeclaredSpan("k_stress", klo, khi, "%/0.1MPa", "MEASURED_SPREAD",
        "stokes2006 p_e8cec37611: pooled 17.1, across-plate range 9.2-23.9. Animal only.",
        "g_l6mech_001")

    S["site_share"] = DeclaredSpan("site_share", 0.55, 0.90, "fraction", "MEASURED_SPREAD",
        "pritchett1992 p_8a1d1c6c9c uncertainty text: distal femoral share 55-90 % by age and sex")

    # --- declared spans for factors that have never been measured -----------
    # Terminal hypertrophic axial height. Bracketed from the recorded mammalian volume
    # range (cooper2013 p_be99ba5726 5000 fl slow plate .. p_89512304c6 23000 fl jerboa) under a
    # transverse diameter of 20-40 um. The diameter itself is unrecorded, which is why
    # this is a DECLARED_SPAN and not a measurement.
    v_lo = fl_to_um3(r.get("p_be99ba5726").num)      # 5000 um^3
    v_hi = fl_to_um3(r.get("p_89512304c6").num)      # 23000 um^3
    d_lo, d_hi = 20.0, 40.0                    # DECLARED, not measured
    h_lo = v_lo / (math.pi * (d_hi / 2) ** 2)
    h_hi = v_hi / (math.pi * (d_lo / 2) ** 2)
    S["h_term_um"] = DeclaredSpan("h_term_um", h_lo, h_hi, "um/cell", "DECLARED_SPAN",
        f"UNMEASURED. Bracketed from recorded terminal volumes {v_lo:.0f}-{v_hi:.0f} um^3 "
        f"(cooper2013 p_be99ba5726/p_89512304c6) under a DECLARED transverse diameter of "
        f"{d_lo:.0f}-{d_hi:.0f} um. No human value; no cross-sectional area recorded for "
        f"any species.", "g_l1arch_009")

    S["T_c_human_d"] = DeclaredSpan("T_c_human_d", hours_to_days(r.get("p_206d079d10").num),
        r.get("p_61f79e4fdb").num, "days", "DECLARED_SPAN",
        f"UNMEASURED IN HUMAN. Bracketed by the measured rat fast-plate value "
        f"({r.get('p_206d079d10').num} h = {hours_to_days(r.get('p_206d079d10').num):.2f} d, p_206d079d10) "
        f"and the DERIVED human figure (20 d, p_61f79e4fdb). ~16-fold. The human end of this "
        f"span is itself derived from the growth rate, so it cannot independently "
        f"predict it.", "g_l1arch_002")

    S["N_p_cells"] = DeclaredSpan("N_p_cells", 12.0, 36.0, "cells", "DECLARED_SPAN",
        "kember1976 p_18c99a7ad2 records 24 cells/proliferative column with uncertainty "
        "'single-study value' - no dispersion, no age or site resolution. byers2000 "
        "(p_e0ba1f702a) records only that proliferative zone height DECREASES with age, "
        "direction only. Span declared at +/-50 % to represent the unrecorded "
        "dispersion.", "g_l1arch_012")

    S["sigma_MPa"] = DeclaredSpan("sigma_MPa", 0.005, 0.20, "MPa", "DECLARED_SPAN",
        "UNMEASURED IN HUMAN (p_15641b1682 'not measured'). Bracketed by the applied stress "
        "range of the animal experiments that define the coefficient "
        "(0.02-0.2 MPa, p_dea1787acd), extended downward because a physiological human "
        "physeal stress may lie below the apparatus-driven animal range.",
        "g_l6mech_003")

    S["E_zone_ratio"] = DeclaredSpan("E_zone_ratio", 0.33, 3.18, "dimensionless",
        "DECLARED_SPAN",
        f"DIRECTION DISPUTED. Lower bound 0.33 = porcine transverse stiffness of "
        f"PZ+HZ relative to reserve (sergerie2009 p_1fbf4533c0, HZ SOFTER). Upper bound 3.18 = "
        f"human sharp-tip AFM HZ/RZ = {r.get('p_d1d4284224').num}/{r.get('p_d7e6e017fa').num} MPa "
        f"(xie2025, HZ STIFFER). Absolute moduli across the record span 380 kPa "
        f"(rabbit p_1f7d5385aa) to 416 MPa (human p_d1d4284224), ~1100-fold.", "g_l5matrix_008")

    return S


# =============================================================================
# 5. SITES.  A named site binds the chain to specific parameter rows.
# =============================================================================

@dataclass
class Site:
    key: str
    label: str
    species: str
    # kinetics
    p_cells_per_column: Optional[str] = None
    p_cycle_time: Optional[str] = None
    p_cycle_time_unit: str = ""
    p_production_direct: Optional[str] = None      # cells/day/column measured directly
    # partition
    p_f_hyp: Optional[str] = None
    p_f_matrix: Optional[str] = None
    p_f_div: Optional[str] = None
    # observed outputs, for the consistency check
    p_rate_um_day: Optional[str] = None
    p_rate_cm_yr: Optional[str] = None
    p_share_of_bone: Optional[str] = None
    p_plate_production: Optional[str] = None       # cells/day/plate
    bone: str = ""
    age_note: str = ""
    sex: str = "both"


SITES: dict[str, Site] = {
    "human_distal_femur": Site(
        key="human_distal_femur", label="human distal femur", species="human",
        p_cells_per_column="p_18c99a7ad2", p_cycle_time="p_61f79e4fdb", p_cycle_time_unit="days",
        p_rate_um_day="p_1c34689beb", p_rate_cm_yr="p_456dd2428e", p_share_of_bone="p_8a1d1c6c9c",
        bone="femur", age_note="kember1976 ages 5-8 y; pritchett1992 age 7 to maturity"),
    "human_distal_femur_pritchett": Site(
        key="human_distal_femur_pritchett", label="human distal femur (pritchett1992)",
        species="human", p_cells_per_column="p_18c99a7ad2", p_cycle_time="p_61f79e4fdb",
        p_cycle_time_unit="days", p_rate_cm_yr="p_75b3d4fa3b", p_share_of_bone="p_8a1d1c6c9c",
        bone="femur", age_note="age 7 to skeletal maturity"),
    "human_proximal_tibia": Site(
        key="human_proximal_tibia", label="human proximal tibia", species="human",
        p_cells_per_column="p_18c99a7ad2", p_cycle_time="p_61f79e4fdb", p_cycle_time_unit="days",
        p_share_of_bone="p_9325eb32b4", bone="tibia", age_note="age 7 to maturity"),
    "human_distal_radius_female": Site(
        key="human_distal_radius_female", label="human distal radius (girls)",
        species="human", p_cells_per_column="p_18c99a7ad2", p_cycle_time="p_61f79e4fdb",
        p_cycle_time_unit="days", p_rate_cm_yr="p_b4773ea198", p_share_of_bone="p_c00ef87c0d",
        bone="radius", sex="female", age_note="age 7 to skeletal maturity"),
    "human_distal_radius_male": Site(
        key="human_distal_radius_male", label="human distal radius (boys)",
        species="human", p_cells_per_column="p_18c99a7ad2", p_cycle_time="p_61f79e4fdb",
        p_cycle_time_unit="days", p_rate_cm_yr="p_2bf6656756", p_share_of_bone="p_c00ef87c0d",
        bone="radius", sex="male", age_note="age 7 to skeletal maturity"),
    "human_proximal_humerus_male": Site(
        key="human_proximal_humerus_male", label="human proximal humerus (boys)",
        species="human", p_cells_per_column="p_18c99a7ad2", p_cycle_time="p_61f79e4fdb",
        p_cycle_time_unit="days", p_rate_cm_yr="p_de3fd37974", p_share_of_bone="p_d2af0e126c",
        bone="humerus", sex="male", age_note="age 7 to skeletal maturity"),
    "rat_proximal_tibia": Site(
        key="rat_proximal_tibia", label="rat proximal tibia (fast plate)", species="rat",
        p_cycle_time="p_206d079d10", p_cycle_time_unit="h", p_production_direct="p_ac972fbc3f",
        p_f_hyp="p_53c796311c", p_f_matrix="p_def18e2a21", p_f_div="p_677f954703",
        p_rate_um_day="p_48944d62f2",
        p_plate_production="p_dca0355e09", bone="tibia", age_note="28-day-old Long-Evans rat"),
    "rat_proximal_radius": Site(
        key="rat_proximal_radius", label="rat proximal radius (slow plate)", species="rat",
        p_cycle_time="p_69f9e770de", p_cycle_time_unit="h",
        p_f_hyp="p_03591cde3d", p_f_matrix="p_30bbb4b516",
        p_plate_production="p_84a65d40e1", bone="radius", age_note="28-day-old Long-Evans rat"),
}


# =============================================================================
# 6. THE CHAIN
# =============================================================================

@dataclass
class Step:
    n: int
    name: str
    detail: str
    value: Optional[float] = None
    unit: str = ""
    provenance: list = field(default_factory=list)
    status: str = "ok"      # ok | assumption | halt | derived


class Chain:
    def __init__(self, site: Site, age: Optional[float], sex: str, mode: str,
                 verbose: bool = True):
        self.site, self.age, self.sex, self.mode = site, age, sex, mode
        self.verbose = verbose
        self.steps: list[Step] = []
        self.reg = registry()
        self.risk_flags: list[str] = []
        self.halted_at: Optional[str] = None
        self.halt_exc: Optional[MissingParameter] = None
        self.results: dict = {}

    # -- plumbing ---------------------------------------------------------
    # EXPECT table: what each parameter id is SUPPOSED to be. A regex on the parameter
    # name and, where it matters, the unit. Added 2026-08-06 after the id drift described
    # in the banner at the top of this file: the model read a COMP patient count as
    # cells-per-column and kept going. A fetch that does not match its expectation now
    # halts instead of returning a number.
    EXPECT = {
        "p_0296c00c3e": (r"number.{0,18}?growth.{0,18}?plates.{0,18}?human", 'growth plates'),
        "p_03591cde3d": (r"contribution.{0,18}?hypertrophic.{0,18}?cell.{0,18}?enlargement", '% of elongation'),
        "p_13aaeefc45": (r"measured.{0,18}?oxygen.{0,18}?tension.{0,18}?human", 'mmHg'),
        "p_15641b1682": (r"vivo.{0,18}?human.{0,18}?physeal.{0,18}?stress", 'MPa'),
        "p_18c99a7ad2": (r"cells.{0,18}?proliferative.{0,18}?column", 'cells'),
        "p_1c34689beb": (r"mean.{0,18}?distal.{0,18}?femoral.{0,18}?growth", 'um/day'),
        "p_1f7d5385aa": (r"Hertz.{0,18}?reduced.{0,18}?modulus.{0,18}?growth", 'kPa'),
        "p_1fbf4533c0": (r"Transverse.{0,18}?stiffness.{0,18}?proliferative.{0,18}?hypertrophic", None),
        "p_206d079d10": (r"total.{0,18}?cell.{0,18}?cycle.{0,18}?time", 'h'),
        "p_2bf6656756": (r"radial.{0,18}?growth.{0,18}?rate.{0,18}?boys", 'cm/year'),
        "p_30bbb4b516": (r"contribution.{0,18}?matrix.{0,18}?synthesis.{0,18}?elongation", '% of elongation'),
        "p_456dd2428e": (r"mean.{0,18}?distal.{0,18}?femoral.{0,18}?growth", 'cm/year'),
        "p_48944d62f2": (r"range.{0,18}?elongation.{0,18}?rates.{0,18}?across", 'um/24 h'),
        "p_53c796311c": (r"contribution.{0,18}?hypertrophic.{0,18}?cell.{0,18}?enlargement", '% of elongation'),
        "p_61f79e4fdb": (r"derived.{0,18}?mean.{0,18}?proliferative.{0,18}?cell", 'days'),
        "p_677f954703": (r"contribution.{0,18}?cell.{0,18}?division.{0,18}?elongation", '% of elongation'),
        "p_69f9e770de": (r"total.{0,18}?cell.{0,18}?cycle.{0,18}?time", 'h'),
        "p_75b3d4fa3b": (r"distal.{0,18}?femoral.{0,18}?contribution.{0,18}?femoral", 'cm/year'),
        "p_84a65d40e1": (r"chondrocytes.{0,18}?produced.{0,18}?growth.{0,18}?plate", 'cells/day'),
        "p_89512304c6": (r"final.{0,18}?volume.{0,18}?jerboa.{0,18}?distal", 'fl'),
        "p_8a1d1c6c9c": (r"distal.{0,18}?femoral.{0,18}?share.{0,18}?femoral", '% of femoral length'),
        "p_9137beb338": (r"mean.{0,18}?cell.{0,18}?height.{0,18}?increase", 'fold'),
        "p_9325eb32b4": (r"proximal.{0,18}?tibial.{0,18}?share.{0,18}?tibial", '% of tibial length'),
        "p_ac972fbc3f": (r"cells.{0,18}?lost.{0,18}?column", 'cells/day'),
        "p_b4773ea198": (r"radial.{0,18}?growth.{0,18}?rate.{0,18}?girls", 'cm/year'),
        "p_be99ba5726": (r"final.{0,18}?volume.{0,18}?slow.{0,18}?plate", 'fl'),
        "p_c00ef87c0d": (r"distal.{0,18}?radial.{0,18}?share.{0,18}?radial", '% of radial length'),
        "p_c8b35c61f3": (r"Axial.{0,18}?stiffness.{0,18}?proliferative.{0,18}?hypertrophic", None),
        "p_ceb7164801": (r"mean.{0,18}?annual.{0,18}?height.{0,18}?velocity", 'cm/yr'),
        "p_d1d4284224": (r"Elastic.{0,18}?modulus.{0,18}?hypertrophic.{0,18}?zone", 'MPa'),
        "p_d2af0e126c": (r"proximal.{0,18}?humeral.{0,18}?share.{0,18}?humeral", '% of humeral length'),
        "p_d7e6e017fa": (r"Elastic.{0,18}?modulus.{0,18}?resting.{0,18}?zone", 'MPa'),
        "p_d83b4b691e": (r"plate.{0,18}?vertebral.{0,18}?growth.{0,18}?rate", 'mm/year'),
        "p_dca0355e09": (r"chondrocytes.{0,18}?produced.{0,18}?growth.{0,18}?plate", 'cells/day'),
        "p_de3fd37974": (r"humeral.{0,18}?growth.{0,18}?rate.{0,18}?boys", 'cm/year'),
        "p_dea1787acd": (r"applied.{0,18}?stress.{0,18}?range.{0,18}?animal", 'MPa'),
        "p_def18e2a21": (r"contribution.{0,18}?matrix.{0,18}?synthesis.{0,18}?elongation", '% of elongation'),
        "p_e0ba1f702a": (r"direction.{0,18}?proliferative.{0,18}?zone.{0,18}?height", 'qualitative'),
        "p_e8cec37611": (r"growth.{0,18}?rate.{0,18}?sensitivity.{0,18}?sustained", None),
        "p_ebe9a640c0": (r"final.{0,18}?volume.{0,18}?fast.{0,18}?plate", 'fl'),
    }

    def _p(self, pid: str) -> Param:
        p = self.reg.get(pid)
        exp = self.EXPECT.get(pid)
        if exp:
            pat, unit = (exp if isinstance(exp, tuple) else (exp, None))
            if not re.search(pat, str(p.parameter or ""), re.I) or (
                    unit and unit.lower() not in str(p.unit or "").lower()):
                raise SystemExit(
                    "\n" + "=" * 78 +
                    "\nPARAMETER IDENTITY CHECK FAILED - MODEL HALTED\n" + "=" * 78 +
                    f"\n  id        : {pid}\n  expected  : /{pat}/"
                    + (f"  unit containing '{unit}'" if unit else "") +
                    f"\n  got       : '{p.parameter}'  [{p.raw_value} {p.unit}]"
                    f"  ref={p.source_ref}"
                    "\n\n  The row this model asked for is not the row it received. Do NOT"
                    "\n  interpret any number printed above this line. Re-resolve the id"
                    "\n  against parameters.csv by CONTENT, never by position.\n" + "=" * 78)
        if p.risk:
            self.risk_flags.append(p.param_id)
        return p

    def _emit(self, s: Step) -> None:
        self.steps.append(s)
        if not self.verbose:
            return
        head = f"  [{s.n}] {s.name}"
        mark = {"ok": "", "assumption": "   <-- STRUCTURAL ASSUMPTION",
                "derived": "   <-- DERIVED, NOT MEASURED", "halt": "   <-- HALT"}[s.status]
        print(head + mark)
        print(f"        {s.detail}")
        if s.value is not None:
            print(f"        => {s.value:,.6g} {s.unit}")
        for pr in s.provenance:
            print(f"          . {pr}")

    # -- steps ------------------------------------------------------------
    def step1_production(self) -> float:
        """Proliferative kinetics -> new cells per column per day."""
        s = self.site
        if s.p_production_direct:
            p = self._p(s.p_production_direct)
            rate = p.num
            prov = [p.cite()]
            detail = "cell production per column measured directly at the vascular front"
            # cross-check against the cycle time if one exists for this site
            if s.p_cycle_time:
                pc = self._p(s.p_cycle_time)
                tc_d = hours_to_days(pc.num) if s.p_cycle_time_unit == "h" else pc.num
                implied_np = rate * tc_d
                prov.append(pc.cite())
                prov.append(f"CROSS-CHECK: {rate} cells/day x {tc_d:.4f} d cycle "
                            f"=> {implied_np:.1f} proliferative cells/column implied. "
                            f"parameters.csv holds NO cells-per-column row for "
                            f"{s.species}, so this cannot be tested. NEW GAP.")
            self._emit(Step(1, "PROLIFERATIVE OUTPUT", detail, rate,
                            "cells/day/column", prov))
            self.results["T_c_days"] = (hours_to_days(self._p(s.p_cycle_time).num)
                                        if s.p_cycle_time and s.p_cycle_time_unit == "h"
                                        else (self._p(s.p_cycle_time).num
                                              if s.p_cycle_time else None))
            return rate

        if not s.p_cells_per_column:
            prov = [self._p(s.p_cycle_time).cite()] if s.p_cycle_time else []
            prov.append(self._p("p_18c99a7ad2").cite() +
                        "  <- the ONLY cells-per-column row in the atlas, and it is "
                        "human distal femur")
            self._emit(Step(1, "PROLIFERATIVE OUTPUT",
                            "cells per proliferative column / cell cycle time",
                            None, "", prov, "halt"))
            fail("N_p_column", "step 1: proliferative output")
        pn = self._p(s.p_cells_per_column)
        pc = self._p(s.p_cycle_time)
        tc_d = hours_to_days(pc.num) if s.p_cycle_time_unit == "h" else pc.num
        assert tc_d > 0
        rate = pn.num / tc_d
        status = "ok"
        prov = [pn.cite(), pc.cite(),
                f"N_p / T_c = {pn.num} cells / {tc_d:g} days"]
        if "derived" in (pc.uncertainty or "").lower():
            status = "derived"
            prov.append("CIRCULARITY WARNING: this cycle time was itself derived from "
                        "column count and growth rate (kember1976). Any elongation rate "
                        "computed from it is not an independent prediction of the "
                        "elongation rate. See gap g_l1arch_002.")
            self.results["circular"] = True
        self._emit(Step(1, "PROLIFERATIVE OUTPUT",
                        "cells per proliferative column / cell cycle time", rate,
                        "cells/day/column", prov, status))
        self.results["T_c_days"] = tc_d
        return rate

    def step2_length_per_cell(self, prod: float) -> float:
        """cells/day -> um/day of hypertrophic column length. Needs h_term."""
        self._emit(Step(2, "HYPERTROPHIC VOLUME EXPANSION -> AXIAL LENGTH",
                        "cells/day x terminal hypertrophic cell height (um/cell) "
                        "= um/day of hypertrophic length", None, "", [
                            self._p("p_ebe9a640c0").cite(),
                            self._p("p_be99ba5726").cite(),
                            self._p("p_9137beb338").cite(),
                            "volume (fl == um^3) cannot become an axial height without a "
                            "transverse cross-sectional area, which is unrecorded."],
                        "halt"))
        fail("h_term_um", "step 2: hypertrophic volume expansion -> axial length")
        return 0.0  # unreachable

    def step3_partition(self, hyp_um_day: float) -> float:
        s = self.site
        if s.species == "human" or s.p_f_hyp is None:
            self._emit(Step(3, "MATRIX SYNTHESIS + DIVISION -> TOTAL ELONGATION",
                            "total elongation = hypertrophic increment / hypertrophic "
                            "share of the elongation budget", None, "", [
                                self._p("p_53c796311c").cite(),
                                self._p("p_03591cde3d").cite(),
                                self._p("p_def18e2a21").cite(),
                                self._p("p_30bbb4b516").cite(),
                                self._p("p_677f954703").cite()], "halt"))
            fail("f_hyp_human", "step 3: elongation partition")
        pf = self._p(s.p_f_hyp)
        f = percent_to_fraction(pf.num)
        tot = hyp_um_day / f
        self._emit(Step(3, "MATRIX SYNTHESIS + DIVISION -> TOTAL ELONGATION",
                        f"total = hypertrophic / {f:.2f}", tot, "um/day", [pf.cite()]))
        return tot

    def step4_mineralisation(self, prod: float, tot_um_day: float) -> None:
        """Mineralisation / chondro-osseous removal. This step is an IDENTITY under
        steady state, not an independent measurement, and says so."""
        s = self.site
        prov = []
        if s.p_production_direct:
            prov.append(self._p(s.p_production_direct).cite())
        if s.p_plate_production:
            pp = self._p(s.p_plate_production)
            prov.append(pp.cite())
            if s.p_production_direct:
                cols = pp.num / self._p(s.p_production_direct).num
                prov.append(f"CROSS-SOURCE CHECK: {pp.num:g} cells/day/plate "
                            f"(wilsman1996) / {self._p(s.p_production_direct).num:g} "
                            f"cells/day/column (hunziker1987) => {cols:.0f} columns per "
                            f"plate. parameters.csv records NO columns-per-plate or "
                            f"column-density row for any species, so this cross-source "
                            f"prediction cannot be tested. NEW GAP.")
                self.results["implied_columns_per_plate"] = cols
        prov.append("STEADY STATE IDENTITY (not a measured factor): cells removed at the "
                    "chondro-osseous junction == cells produced. No measurement in any "
                    "species records net axial length lost to mineral shrinkage or "
                    "resorption at the junction, so the model asserts 1:1 conversion of "
                    "calcified cartilage length to primary spongiosa length.")
        prov.append(self._p("p_13aaeefc45").cite() +
                    "  -> matrix synthesis cannot be modelled as a RATE (gap "
                    "g_l1arch_007); it enters only as a partition share.")
        self._emit(Step(4, "MATRIX MINERALISATION / CHONDRO-OSSEOUS REMOVAL",
                        "steady-state closure check", None, "", prov, "assumption"))

    def step5_mechanics(self, tot_um_day: float) -> float:
        self._emit(Step(5, "MECHANICAL MODULATION",
                        "elongation x (1 - k * sigma), k = growth-rate sensitivity to "
                        "sustained stress, sigma = in vivo physeal stress", None, "", [
                            self._p("p_e8cec37611").cite(),
                            self._p("p_15641b1682").cite(),
                            self._p("p_d7e6e017fa").cite(),
                            self._p("p_d1d4284224").cite(),
                            self._p("p_1f7d5385aa").cite(),
                            self._p("p_c8b35c61f3").cite(),
                            self._p("p_1fbf4533c0").cite(),
                            "the zonal modulus record spans 380 kPa to 416 MPa and the "
                            "GRADIENT DIRECTION disagrees between species, so the model "
                            "cannot even determine which zone carries the peak stress."],
                        "halt"))
        fail("sigma_physis_MPa", "step 5: mechanical modulation")
        return 0.0

    def step6_units(self, um_day: float) -> float:
        cm_yr = um_per_day_to_cm_per_yr(um_day)
        self._emit(Step(6, "UNIT CONVERSION um/day -> cm/yr",
                        f"x {DAYS_PER_YEAR} d/yr / {UM_PER_CM:,.0f} um/cm", cm_yr,
                        "cm/yr", ["exact conversion, asserted in _selftest_units()"]))
        return cm_yr

    def step7_stature(self, cm_yr_site: float) -> float:
        s = self.site
        prov = []
        if s.p_share_of_bone:
            ps = self._p(s.p_share_of_bone)
            share = percent_to_fraction(ps.num)
            bone_v = cm_yr_site / share
            prov += [ps.cite(), f"{s.bone} velocity = site / {share:.2f} = "
                                f"{bone_v:.3f} cm/yr"]
        prov += [self._p("p_0296c00c3e").cite(), self._p("p_d83b4b691e").cite()]
        self._emit(Step(7, "SITE -> STATURE",
                        "stature velocity = femur + tibia + foot + spine + skull base",
                        None, "", prov, "halt"))
        fail("v_vertebral_per_plate", "step 7: summation of plates to stature")
        return 0.0

    # -- driver -----------------------------------------------------------
    def run(self) -> dict:
        s = self.site
        if self.verbose:
            print()
            print("#" * 78)
            print(f"# FLOW MODEL  site={s.key}  age={self.age}  sex={self.sex}  "
                  f"mode={self.mode}")
            print(f"# {s.label}  ({s.species})   {s.age_note}")
            print("#" * 78)
        try:
            prod = self.step1_production()
            self.results["production_cells_per_day"] = prod
            hyp = self.step2_length_per_cell(prod)
            tot = self.step3_partition(hyp)
            self.step4_mineralisation(prod, tot)
            tot = self.step5_mechanics(tot)
            cm = self.step6_units(tot)
            self.step7_stature(cm)
            self.results["completed"] = True
        except MissingParameter as e:
            self.halted_at = e.step
            self.halt_exc = e
            self.results["completed"] = False
            if self.verbose:
                print(e.render())
        if self.verbose and self.risk_flags:
            print(f"  RISK-CLASS ROWS USED (single_source_point_no_uncertainty): "
                  f"{', '.join(sorted(set(self.risk_flags)))}")
        return self.results


# =============================================================================
# 7. CLOSURE MODE.  Run the chain backwards from a measured rate to solve for the
#    missing factor.  Invents nothing; produces a falsifiable prediction.
# =============================================================================

def closure(site_key: str, verbose: bool = True) -> dict:
    reg = registry()
    s = SITES[site_key]
    out = {"site": site_key}
    if verbose:
        print()
        print("#" * 78)
        print(f"# CLOSURE MODE  {s.label}")
        print("# The forward chain halts for want of terminal hypertrophic cell height.")
        print("# Run it BACKWARDS from the measured elongation rate to solve for the")
        print("# value that factor MUST take. This is a prediction, not a measurement.")
        print("#" * 78)

    # measured elongation rate for this site
    if s.p_rate_um_day:
        p = reg.get(s.p_rate_um_day)
        lo, hi = p.span()
        v_um_day = p.num
        src = p.cite()
        if hi > lo:
            out["v_um_day_range"] = (lo, hi)
            src += (f"  RANGE ROW: {lo:g}-{hi:g} um/day is the spread across the FOUR "
                    f"plates wilsman1996a compared; the atlas does not resolve the "
                    f"per-plate value, so closure yields an interval, not a point.")
    elif s.p_rate_cm_yr:
        p = reg.get(s.p_rate_cm_yr)
        v_um_day = cm_per_yr_to_um_per_day(p.num)
        src = p.cite() + f"  -> {v_um_day:.2f} um/day"
    else:
        if verbose:
            print(f"  no measured elongation rate recorded for {s.key}; closure "
                  f"impossible. This is itself a gap.")
        return out
    out["v_um_day"] = v_um_day

    ch = Chain(s, None, "both", "closure", verbose=False)
    prod = ch.step1_production()
    out["production_cells_per_day"] = prod
    out["circular"] = ch.results.get("circular", False)

    total_per_cell = v_um_day / prod
    out["required_total_length_per_cell_um"] = total_per_cell
    if "v_um_day_range" in out:
        out["required_total_length_per_cell_um_range"] = (
            out["v_um_day_range"][0] / prod, out["v_um_day_range"][1] / prod)

    lo_f = percent_to_fraction(reg.get("p_03591cde3d").num)     # 0.44 slow rat plate
    hi_f = percent_to_fraction(reg.get("p_53c796311c").num)     # 0.59 fast rat plate
    out["required_h_term_um_range"] = (total_per_cell * lo_f, total_per_cell * hi_f)

    if verbose:
        print(f"  measured elongation      : {v_um_day:,.2f} um/day")
        print(f"    {src}")
        print(f"  chain production rate    : {prod:,.4f} cells/day/column")
        print(f"  => REQUIRED total axial length contributed per cell cycle:")
        if "required_total_length_per_cell_um_range" in out:
            r = out["required_total_length_per_cell_um_range"]
            print(f"       {r[0]:,.2f} - {r[1]:,.2f} um/cell (interval, per-plate rate "
                  f"unresolved in the atlas)")
            hlo, hhi = r[0] * lo_f, r[1] * hi_f
            out["required_h_term_um_range"] = (hlo, hhi)
        else:
            print(f"       {total_per_cell:,.2f} um/cell")
        print(f"  => of which HYPERTROPHIC cell height, under the rat partition "
              f"(44-59 %):")
        print(f"       {out['required_h_term_um_range'][0]:,.2f} - "
              f"{out['required_h_term_um_range'][1]:,.2f} um/cell")
        # implied geometry from the recorded volumes
        for pid in ("p_be99ba5726", "p_ebe9a640c0", "p_89512304c6"):
            vol = fl_to_um3(reg.get(pid).num)
            h = out["required_h_term_um_range"][1]
            d = math.sqrt(4.0 * vol / (math.pi * h))
            print(f"       if terminal volume were {vol:,.0f} um^3 ({reg.get(pid).source_ref}, "
                  f"{reg.get(pid).species}) the cell would be {d:,.1f} um wide")
        if out["circular"]:
            print()
            print("  *** THIS CLOSURE IS CIRCULAR FOR HUMAN SITES. The production rate")
            print("      used the kember1976 20-day cycle time, which kember1976 itself")
            print("      derived from this same growth rate and column count. The human")
            print("      chain therefore contains NO independent information: it")
            print("      reproduces the target by construction. The recovered cell height")
            print("      is nevertheless a real, testable prediction, because it is a")
            print("      quantity kember1976 assumed and never measured (gap g_l1arch_009).")
    return out


# =============================================================================
# 8. CONSISTENCY CHECK AGAINST organism_targets.csv
# =============================================================================

def _targets() -> list[dict]:
    return list(csv.DictReader(open(TARGET_CSV, newline="", encoding="utf-8")))


def consistency(verbose: bool = True) -> dict:
    reg = registry()
    T = _targets()
    res: dict = {}
    if verbose:
        print()
        print("#" * 78)
        print("# CONSISTENCY CHECK against atlas/quant/organism_targets.csv")
        print("#" * 78)

    # ---- A. arithmetic self-consistency of the atlas -----------------------
    rel = _selftest_units()
    res["A_kember_internal_rel_residual"] = rel
    if verbose:
        print(f"\nA. UNIT/ARITHMETIC SELF-CONSISTENCY")
        print(f"   kember1976 records 1.4 cm/yr (p_456dd2428e) and 38 um/day (p_1c34689beb).")
        print(f"   38 um/day x 365.25 / 10000 = "
              f"{um_per_day_to_cm_per_yr(38.0):.4f} cm/yr")
        print(f"   residual vs 1.4 cm/yr = "
              f"{um_per_day_to_cm_per_yr(38.0) - 1.4:+.4f} cm/yr ({rel:.2%})")
        print(f"   PASS - but this tests arithmetic only, not biology: both rows are")
        print(f"   the same measurement in two units from one source.")

    # ---- B. does the human kinetic chain contain independent information? ---
    c = closure("human_distal_femur", verbose=False)
    res["B_required_h_term_um"] = c["required_h_term_um_range"]
    res["B_total_per_cell_um"] = c["required_total_length_per_cell_um"]
    res["B_circular"] = c["circular"]
    if verbose:
        print(f"\nB. INDEPENDENCE OF THE HUMAN CHAIN")
        print(f"   human distal femur: 24 cells/column (p_18c99a7ad2) / 20 d cycle (p_61f79e4fdb)")
        print(f"   = {c['production_cells_per_day']:.3f} cells/day/column.")
        print(f"   Required length per cell to reach 38 um/day: "
              f"{c['required_total_length_per_cell_um']:.2f} um.")
        print(f"   RESIDUAL = 0 BY CONSTRUCTION. The 20-day cycle time is derived from")
        print(f"   the growth rate it is being used to predict (p_61f79e4fdb uncertainty field")
        print(f"   reads 'derived quantity, not measured'). The human chain is an")
        print(f"   identity, not a test. Residual source: model structure (3), not")
        print(f"   parameter error.")

    # ---- C. species cross-check: is the human chain compatible with rat? ----
    rat = SITES["rat_proximal_tibia"]
    prod_rat = reg.get(rat.p_production_direct).num              # 8 cells/day
    rat_lo, rat_hi = reg.get("p_48944d62f2").span()                    # 50-400 um/24h
    rat_per_cell = (rat_lo / prod_rat, rat_hi / prod_rat)
    res["C_rat_length_per_cell_um"] = rat_per_cell
    human_per_cell = c["required_total_length_per_cell_um"]
    inside = rat_per_cell[0] <= human_per_cell <= rat_per_cell[1]
    res["C_human_inside_rat_range"] = inside
    if verbose:
        print(f"\nC. SPECIES CROSS-CHECK (the only non-circular test available)")
        print(f"   rat proximal tibia: {prod_rat:g} cells/day/column (hunziker1987 "
              f"p_ac972fbc3f)")
        print(f"   rat elongation across four plates: {rat_lo:g}-{rat_hi:g} um/day "
              f"(wilsman1996a p_48944d62f2)")
        print(f"   => rat requires {rat_per_cell[0]:.2f}-{rat_per_cell[1]:.2f} um of "
              f"axial length per cell")
        print(f"   human requires {human_per_cell:.2f} um per cell")
        print(f"   human value lies INSIDE the rat range: {inside}")
        print(f"   The ~16-fold human/rat cell cycle gap (20 d vs 30.9 h) is absorbed")
        print(f"   almost entirely by the production rate ("
              f"{prod_rat / c['production_cells_per_day']:.1f}-fold) and NOT by the")
        print(f"   length contributed per cell. That is a substantive, falsifiable")
        print(f"   prediction: human terminal hypertrophic cells should be of ORDINARY")
        print(f"   mammalian size, and the human plate should be slow because it cycles")
        print(f"   slowly, not because its cells are small.")

    # ---- D. cross-source check inside the rat data --------------------------
    plate = reg.get("p_dca0355e09").num                                # 16400 cells/day/plate
    cols = plate / prod_rat
    res["D_implied_columns_per_plate"] = cols
    if verbose:
        print(f"\nD. CROSS-SOURCE CHECK WITHIN THE RAT (wilsman1996 vs hunziker1987)")
        print(f"   {plate:,.0f} cells/day/plate (p_dca0355e09) / {prod_rat:g} "
              f"cells/day/column (p_ac972fbc3f)")
        print(f"   => {cols:,.0f} columns in a rat proximal tibial growth plate.")
        print(f"   parameters.csv contains NO columns-per-plate or column-density row")
        print(f"   for any species. This is a testable prediction that the atlas cannot")
        print(f"   currently test. NEW QUANTITATIVE GAP.")

    # ---- E. the organism target: can the plate model be summed to stature? --
    fem_site = reg.get("p_75b3d4fa3b").num                             # 1.3 cm/yr distal femur
    share = percent_to_fraction(reg.get("p_8a1d1c6c9c").num)           # 0.70
    fem_bone = fem_site / share
    res["E_femur_cm_yr"] = fem_bone

    tgt_phv_m = float([t for t in T if t["target_id"] == "t001"][0]["value"])   # 9.61
    tgt_phv_f = float([t for t in T if t["target_id"] == "t003"][0]["value"])   # 8.32
    tgt_child = reg.get("p_ceb7164801").num                            # 6.10 cm/yr, 8-11 y
    res["E_targets"] = {"PHV_male_t001": tgt_phv_m, "PHV_female_t003": tgt_phv_f,
                        "childhood_8_11y_dalskov2016": tgt_child}

    accounted = fem_bone
    residuals = {k: v - accounted for k, v in res["E_targets"].items()}
    res["E_residual_cm_yr"] = residuals
    res["E_fraction_unaccounted"] = {k: (v - accounted) / v
                                     for k, v in res["E_targets"].items()}

    sitar = float([t for t in T if t["target_id"] == "t028"][0]["value"])       # 0.79 cm
    res["E_sitar_floor_cm"] = sitar

    if verbose:
        print(f"\nE. RESIDUAL AGAINST THE ORGANISM TARGET")
        print(f"   Stature velocity = femur + tibia + foot + spine + skull base "
              f"(one side).")
        print(f"   The atlas supplies exactly ONE of those terms from measured rows:")
        print(f"     distal femur {fem_site:g} cm/yr (p_75b3d4fa3b, pritchett1992)")
        print(f"     / {share:.2f} distal share (p_8a1d1c6c9c) = femur {fem_bone:.2f} cm/yr")
        print(f"   tibia: NO absolute rate recorded (only the 57 % share, p_9325eb32b4)")
        print(f"   spine: per-plate rate recorded as NOT REPORTED (p_d83b4b691e), across "
              f">130 plates (p_0296c00c3e)")
        print(f"   foot / skull base: no rows at all")
        print()
        for k, v in res["E_targets"].items():
            print(f"   target {k:<28} = {v:5.2f} cm/yr   accounted "
                  f"{accounted:4.2f}   RESIDUAL {residuals[k]:+5.2f} cm/yr "
                  f"({res['E_fraction_unaccounted'][k]:.0%} unaccounted)")
        print()
        print(f"   Age-matched comparison is the fair one: the pritchett rates are means")
        print(f"   over ages 7 to maturity, so dalskov2016's 6.10 cm/yr for 8-11 year")
        print(f"   olds is the right target, giving a residual of "
              f"{residuals['childhood_8_11y_dalskov2016']:+.2f} cm/yr "
              f"({res['E_fraction_unaccounted']['childhood_8_11y_dalskov2016']:.0%}).")
        print(f"   ACCURACY CEILING. SITAR fits the same kind of serial height data with")
        print(f"   a residual SD of {sitar} cm IN HEIGHT (t028, cole2010). Integrating the")
        print(f"   parameter-flow shortfall over a single year gives "
              f"{residuals['childhood_8_11y_dalskov2016']:.2f} cm of height")
        print(f"   unaccounted for after twelve months - "
              f"{residuals['childhood_8_11y_dalskov2016'] / sitar:.0f}x the SITAR floor,")
        print(f"   and it grows linearly with the length of the prediction window.")
        print(f"   A model that knows nothing about chondrocytes describes these children")
        print(f"   {residuals['childhood_8_11y_dalskov2016'] / sitar:.0f} times more "
              f"accurately than the mechanism-derived chain.")

    # ---- F. what the model CAN reproduce -----------------------------------
    checks = []
    for key in ("human_distal_radius_female", "human_distal_radius_male",
                "human_proximal_humerus_male", "human_distal_femur",
                "human_distal_femur_pritchett"):
        s = SITES[key]
        if not (s.p_rate_cm_yr or s.p_rate_um_day):
            continue
        cc = closure(key, verbose=False)
        checks.append((key, cc["required_total_length_per_cell_um"]))
    res["F_required_length_per_cell_by_site"] = dict(checks)
    if verbose:
        print(f"\nF. SITE-TO-SITE COHERENCE")
        print(f"   The same human kinetic constants (24 cells/column, 20 d) applied to")
        print(f"   every site with a recorded rate require these per-cell lengths:")
        for k, v in checks:
            print(f"     {k:<34} {v:6.2f} um/cell")
        vals = [v for _, v in checks]
        print(f"   spread {min(vals):.2f}-{max(vals):.2f} um "
              f"({max(vals) / min(vals):.2f}-fold).")
        print(f"   Since the kinetic constants are held fixed across sites (the atlas")
        print(f"   has only one human value for each), ALL site-to-site variation is")
        print(f"   forced onto the one factor that has never been measured. The model")
        print(f"   cannot distinguish 'human plates differ in cell size' from 'human")
        print(f"   plates differ in cycle time' - gap g_l1arch_010.")

    return res


# =============================================================================
# 9. SENSITIVITY.  Freeze-one-input variance reduction: how much output
#    uncertainty would MEASURING each parameter remove?
# =============================================================================

def _sample(sp: DeclaredSpan, u: float) -> float:
    """Log-uniform sample from a declared span given u in [0,1)."""
    if sp.lo <= 0:
        return sp.lo + u * (sp.hi - sp.lo)
    return math.exp(math.log(sp.lo) + u * (math.log(sp.hi) - math.log(sp.lo)))


def _forward(x: dict) -> float:
    """The chain, evaluated with an explicit dict of inputs. cm/yr, one plate.

    elongation = (N_p / T_c) * h_term / f_hyp * (1 - k*sigma*E_ratio) -> cm/yr
    Every factor here is either a recorded row or a DECLARED_SPAN stamped in
    declared_spans(). Nothing is defaulted.
    """
    prod = x["N_p_cells"] / x["T_c_human_d"]                 # cells/day/column
    hyp = prod * x["h_term_um"]                              # um/day hypertrophic
    tot = hyp / x["f_hyp"]                                   # um/day total
    # mechanical modulation: k is %/0.1 MPa, sigma in MPa, E_zone_ratio concentrates
    # (or relieves) the stress on the growth-controlling zone.
    frac_loss = (x["k_stress"] / 100.0) * (x["sigma_MPa"] / 0.1) * x["E_zone_ratio"]
    mech = 1.0 - frac_loss
    if mech <= 0.0:
        # The Stokes linear law has been driven past the point where it predicts zero
        # or negative elongation. Linearity was demonstrated only over roughly
        # -0.2 to +0.1 MPa (p01026); beyond that the functional form is unknown
        # (gap g_l6mech_002). Do not clip silently - signal it.
        return float("nan")
    return um_per_day_to_cm_per_yr(tot * mech)


SENS_KEYS = ["T_c_human_d", "h_term_um", "N_p_cells", "f_hyp",
             "k_stress", "sigma_MPa", "E_zone_ratio"]


def sensitivity(n: int = 40000, seed: int = 20260805, verbose: bool = True,
                scenario: str = "recorded_spreads") -> dict:
    S = declared_spans()
    if scenario == "human_ignorance":
        # The rat partition spread (44-59 %) understates human ignorance: no human
        # partition exists at all. Widen f_hyp to the interval a human measurement
        # could plausibly fall in, and stamp it as DECLARED.
        S["f_hyp"] = DeclaredSpan("f_hyp", 0.20, 0.80, "fraction", "DECLARED_SPAN",
            "SCENARIO human_ignorance: no human partition has ever been measured "
            "(gap g_l1arch_001). The rat spread 44-59 % (p_53c796311c/p_03591cde3d) describes "
            "variation between two RAT plates, not the human value. Span declared "
            "0.20-0.80 to represent genuine human ignorance.", "g_l1arch_001")
    elif scenario != "recorded_spreads":
        raise ValueError(f"unknown scenario {scenario}")
    rng = random.Random(seed)
    # common random numbers so freeze-one comparisons are paired
    U = [[rng.random() for _ in SENS_KEYS] for _ in range(n)]

    def run(freeze: Optional[str]) -> list[float]:
        out = []
        for row in U:
            x = {}
            for i, k in enumerate(SENS_KEYS):
                sp = S[k]
                x[k] = _sample(sp, 0.5) if k == freeze else _sample(sp, row[i])
            out.append(_forward(x))
        return out

    base = run(None)
    n_nan = sum(1 for v in base if v != v)
    logs = [math.log(v) for v in base if v == v and v > 0]
    mu = sum(logs) / len(logs)
    var0 = sum((v - mu) ** 2 for v in logs) / (len(logs) - 1)

    contrib = {}
    for k in SENS_KEYS:
        fz = [math.log(v) for v in run(k) if v == v and v > 0]
        m = sum(fz) / len(fz)
        var = sum((v - m) ** 2 for v in fz) / (len(fz) - 1)
        contrib[k] = max(0.0, (var0 - var) / var0)

    tot = sum(contrib.values()) or 1.0
    norm = {k: v / tot for k, v in contrib.items()}
    ranked = sorted(norm.items(), key=lambda kv: -kv[1])

    base_sorted = sorted(v for v in base if v == v)
    q = lambda p: base_sorted[min(len(base_sorted) - 1, int(p * len(base_sorted)))]
    res = {"n": n, "n_out_of_domain": n_nan, "median_cm_yr": q(0.5),
           "p05": q(0.05), "p95": q(0.95),
           "fold_90pct": q(0.95) / q(0.05) if q(0.05) > 0 else float("inf"),
           "contribution": norm, "ranked": ranked, "spans": S,
           "var_log": var0}

    if verbose:
        print()
        print("#" * 78)
        print("# SENSITIVITY - human distal femur, forward chain")
        print("# EVERY unmeasured factor below is a DECLARED_SPAN, not a measurement.")
        print("# The model does NOT run in this mode by default; it must be asked for.")
        print("#" * 78)
        print()
        print("  DECLARED INPUT SPANS")
        for k in SENS_KEYS:
            sp = S[k]
            tag = "MEASURED " if sp.status == "MEASURED_SPREAD" else "*DECLARED"
            gid = f"  gap:{sp.gap_id}" if sp.gap_id else ""
            print(f"   [{tag}] {k:<14} {sp.lo:>9.4g} - {sp.hi:<9.4g} {sp.unit:<12}"
                  f"({sp.hi / sp.lo:.1f}x){gid}")
            for line in _wrap(sp.basis, 66):
                print(f"                {line}")
        print()
        print(f"  OUTPUT: predicted distal femoral elongation, n={n:,} log-uniform draws")
        print(f"    median {res['median_cm_yr']:.2f} cm/yr   "
              f"90 % interval {res['p05']:.3f} - {res['p95']:.2f} cm/yr   "
              f"({res['fold_90pct']:.0f}-fold)")
        print(f"    {n_nan:,} of {n:,} draws ({n_nan / n:.1%}) drove the Stokes linear "
              f"stress-growth law to zero or negative elongation - outside the "
              f"-0.2 to +0.1 MPa interval over which linearity was actually "
              f"demonstrated (p01026). Those draws are reported, not clipped; the "
              f"functional form beyond that range is gap g_l6mech_002.")
        print(f"    measured value 1.3-1.4 cm/yr (p_456dd2428e/p_75b3d4fa3b) lies "
              f"{'INSIDE' if res['p05'] <= 1.35 <= res['p95'] else 'OUTSIDE'} that "
              f"interval - which tells us almost nothing, because the interval spans "
              f"{res['fold_90pct']:.0f}-fold.")
        print()
        print("  UNCERTAINTY CONTRIBUTION (share of Var[log output] removed if the")
        print("  parameter were MEASURED and pinned; freeze-one, common random numbers)")
        for k, v in ranked:
            sp = S[k]
            bar = "#" * int(round(v * 50))
            tag = "MEASURED" if sp.status == "MEASURED_SPREAD" else "UNMEASURED"
            print(f"    {v * 100:5.1f}%  {k:<14} {tag:<11} {bar}")
        unmeas = sum(v for k, v in norm.items()
                     if S[k].status != "MEASURED_SPREAD")
        print(f"\n    {unmeas:.0%} of the output uncertainty is carried by parameters "
              f"that have NEVER BEEN MEASURED.")
        res["unmeasured_share"] = unmeas

        # --- robustness: is the ranking an artefact of the span widths? -----
        print()
        print("  ROBUSTNESS - elasticity vs span width")
        print("  In a multiplicative chain every kinetic input has |d ln Y / d ln X| = 1")
        print("  by construction, so no input is structurally more powerful than another.")
        print("  The ranking above is therefore ENTIRELY a statement about how wide the")
        print("  current ignorance of each input is - which is exactly the right basis")
        print("  for an experimental agenda, but means the ranking must be reread")
        print("  whenever a span changes. Elasticities and span widths:")
        med = {k: _sample(S[k], 0.5) for k in SENS_KEYS}
        y0 = _forward(med)
        for k, share in ranked:
            x = dict(med)
            x[k] = med[k] * 1.01
            y1 = _forward(x)
            el = (math.log(y1 / y0) / math.log(1.01)) if (y1 == y1 and y0 == y0) else float("nan")
            print(f"    {k:<14} elasticity {el:+.2f}   span {S[k].hi / S[k].lo:5.1f}x   "
                  f"ln-range^2 {S[k].log_range ** 2:6.2f}   contribution {share:.0%}")
        res["elasticity_note"] = ("multiplicative chain: unit elasticity; ranking is "
                                  "driven by span width, i.e. by current ignorance")
    else:
        res["unmeasured_share"] = sum(v for k, v in norm.items()
                                      if S[k].status != "MEASURED_SPREAD")
    return res


def _wrap(s: str, w: int) -> list[str]:
    words, lines, cur = s.split(), [], ""
    for wd in words:
        if len(cur) + len(wd) + 1 > w:
            lines.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    if cur:
        lines.append(cur)
    return lines


# =============================================================================
# 10. GAP CROSS-REFERENCE
# =============================================================================

SENS_TO_GAP = {
    "T_c_human_d": "g_l1arch_002",
    "h_term_um": "g_l1arch_009",
    "N_p_cells": "g_l1arch_012",
    "f_hyp": "g_l1arch_001",
    "k_stress": "g_l6mech_001",
    "sigma_MPa": "g_l6mech_003",
    "E_zone_ratio": "g_l5matrix_008",
}


def load_gaps() -> dict:
    try:
        import yaml
    except ImportError:
        return {}
    with open(GAPS_YAML, encoding="utf-8") as fh:
        return {g["gap_id"]: g for g in yaml.safe_load(fh)["gaps"]}


def agenda(n: int = 40000, verbose: bool = True,
           scenario: str = "recorded_spreads") -> list[dict]:
    s = sensitivity(n=n, verbose=False, scenario=scenario)
    G = load_gaps()
    rows = []
    for k, share in s["ranked"]:
        gid = SENS_TO_GAP[k]
        g = G.get(gid, {})
        rows.append({
            "param": k, "share": share, "gap_id": gid,
            "status": s["spans"][k].status,
            "tractability": g.get("tractability"),
            "type": g.get("type"),
            "question": g.get("question", ""),
            "experiment": g.get("discriminating_experiment", ""),
            "what_is_missing": g.get("what_is_missing", ""),
            "nearest": g.get("nearest_evidence", []),
        })
    if verbose:
        print()
        print("#" * 78)
        print("# EXPERIMENTAL AGENDA - uncertainty contribution x gap register")
        print("#" * 78)
        for i, r in enumerate(rows, 1):
            print(f"\n{i}. {r['param']}   {r['share']:.0%} of output uncertainty   "
                  f"[{r['status']}]")
            print(f"   gap {r['gap_id']}  type={r['type']}  tractability="
                  f"{r['tractability']}/5")
            for line in _wrap(r["question"], 72):
                print(f"   Q: {line}" if line == _wrap(r["question"], 72)[0]
                      else f"      {line}")
    return rows


# =============================================================================
# 11. CLI
# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default="human_distal_femur", choices=sorted(SITES))
    ap.add_argument("--age", type=float, default=None,
                    help="age in years (recorded rows are not age-resolved; see report)")
    ap.add_argument("--sex", default="male", choices=["male", "female", "both"])
    ap.add_argument("--mode", default="strict",
                    choices=["strict", "closure", "sensitivity"])
    ap.add_argument("--all", action="store_true", help="run every site in strict mode")
    ap.add_argument("--consistency", action="store_true")
    ap.add_argument("--agenda", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--n", type=int, default=40000)
    ap.add_argument("--scenario", default="recorded_spreads",
                    choices=["recorded_spreads", "human_ignorance"],
                    help="span set for --mode sensitivity / --agenda")
    a = ap.parse_args()

    reg = registry()
    print(f"parameters.csv: {len(reg.rows)} rows")
    print("reliability classes: " + ", ".join(
        f"{k}={v}" for k, v in reg.class_counts.most_common()))
    risk = reg.class_counts["single_source_point_no_uncertainty"]
    print(f"RISK CLASS single_source_point_no_uncertainty: {risk} rows "
          f"({risk / len(reg.rows):.0%})")

    if a.selftest:
        rel = _selftest_units()
        print(f"\nunit self-test PASSED; atlas cross-check residual {rel:.2%}")
        return 0

    if a.consistency:
        consistency()
        return 0
    if a.agenda:
        agenda(n=a.n, scenario=a.scenario)
        return 0

    if a.all:
        halts = Counter()
        for k in sorted(SITES):
            ch = Chain(SITES[k], a.age, a.sex, "strict")
            ch.run()
            halts[ch.halted_at or "COMPLETED"] += 1
        print("\n" + "=" * 78)
        print("SUMMARY - where the chain halts")
        for k, v in halts.most_common():
            print(f"  {v} site(s): {k}")
        print("=" * 78)
        return 0

    if a.mode == "closure":
        closure(a.site)
        return 0
    if a.mode == "sensitivity":
        sensitivity(n=a.n, scenario=a.scenario)
        agenda(n=a.n, verbose=False, scenario=a.scenario)
        return 0

    ch = Chain(SITES[a.site], a.age, a.sex, a.mode)
    ch.run()
    return 0 if ch.results.get("completed") else 3


if __name__ == "__main__":
    sys.exit(main())
