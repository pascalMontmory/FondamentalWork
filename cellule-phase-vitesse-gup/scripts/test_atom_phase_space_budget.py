#!/usr/bin/env python3
from __future__ import annotations

import math

from compare_atom_phase_space_budget import (
    ATOM_OPTIONS,
    effective_volume,
    evaluate_atom_budget,
    phase_space_atom_cap,
)
from phase_space_gas_common import SPECIES, gup_beta_p2_from_velocity


def test_phase_space_cap_scales_with_volume() -> None:
    lambda_th = 1.0e-6
    small = phase_space_atom_cap(0.3, 1.0e-9, lambda_th)
    large = phase_space_atom_cap(0.3, 8.0e-9, lambda_th)
    if not math.isclose(large / small, 8.0):
        raise AssertionError("phase-space atom cap must scale with effective volume")


def test_effective_volume_is_aperture_limited() -> None:
    aperture = 1.0e-2
    wide_cloud = effective_volume(2.0e-2, aperture)
    aperture_volume = 4.0 * math.pi * aperture**3 / 3.0
    if not math.isclose(wide_cloud, aperture_volume):
        raise AssertionError("effective volume should be aperture-limited")


def test_best_atom_budget_row_is_physical() -> None:
    row = evaluate_atom_budget(
        atom=ATOM_OPTIONS[0],
        temperature_k=1.0e-7,
        interrogation_s=0.5,
        eta_max=0.3,
        initial_atoms_cap=1.0e7,
        initial_radius_m=1.0e-3,
        aperture_radius_m=12.0e-3,
        beta0_for_gup_bound=1.0e26,
    )
    if float(row["detected_atoms_budget"]) > 1.0e7:
        raise AssertionError("detected atom budget must not exceed technical cap")
    if float(row["sensitivity_fom_s2_sqrt_atoms"]) <= 0.0:
        raise AssertionError("sensitivity figure of merit must be positive")
    if float(row["gup_beta_p2_beta0_bound"]) >= 1.0e-20:
        raise AssertionError("GUP correction should be negligible for cold atoms")


def test_gup_velocity_scaling() -> None:
    rb = SPECIES["Rb87"]
    slow = gup_beta_p2_from_velocity(1.0, rb.mass_kg, 1.0)
    fast = gup_beta_p2_from_velocity(1.0, rb.mass_kg, 10.0)
    if not math.isclose(fast / slow, 100.0):
        raise AssertionError("GUP epsilon must scale as velocity squared")


if __name__ == "__main__":
    test_phase_space_cap_scales_with_volume()
    test_effective_volume_is_aperture_limited()
    test_best_atom_budget_row_is_physical()
    test_gup_velocity_scaling()
    print("atom phase-space budget tests passed")