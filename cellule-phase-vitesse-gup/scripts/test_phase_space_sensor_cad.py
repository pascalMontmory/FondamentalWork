#!/usr/bin/env python3
from __future__ import annotations

import math

from phase_space_gas_common import (
    SPECIES,
    atom_interferometer_acceleration_noise,
    cloud_radius_after_time,
    degeneracy_parameter,
    gaussian_cubic_survival_fraction,
    velocity_sigma_1d,
)
from phase_space_sensor_cad import SCENARIOS, best_rows, evaluate_design_space


def assert_close(value: float, expected: float, rel: float = 1.0e-12) -> None:
    if not math.isclose(value, expected, rel_tol=rel, abs_tol=0.0):
        raise AssertionError(f"{value} != {expected}")


def test_basic_phase_space_monotonicity() -> None:
    rb = SPECIES["Rb87"]
    eta_cold = degeneracy_parameter(1.0e18, rb.mass_kg, 1.0e-8)
    eta_warm = degeneracy_parameter(1.0e18, rb.mass_kg, 1.0e-6)
    if eta_cold <= eta_warm:
        raise AssertionError("phase-space density must increase when temperature falls")

    sigma_cold = velocity_sigma_1d(rb.mass_kg, 1.0e-8)
    sigma_warm = velocity_sigma_1d(rb.mass_kg, 1.0e-6)
    if sigma_cold >= sigma_warm:
        raise AssertionError("thermal velocity dispersion must increase with temperature")


def test_cloud_and_detection_limits() -> None:
    radius_short = cloud_radius_after_time(1.0e-3, 1.0e-3, 0.1)
    radius_long = cloud_radius_after_time(1.0e-3, 1.0e-3, 1.0)
    if radius_short >= radius_long:
        raise AssertionError("cloud radius must increase with free-expansion time")

    survival_wide = gaussian_cubic_survival_fraction(1.0e-3, 10.0e-3)
    survival_narrow = gaussian_cubic_survival_fraction(10.0e-3, 1.0e-3)
    if not (0.99 < survival_wide <= 1.0):
        raise AssertionError("wide aperture should detect nearly all atoms")
    if not (0.0 <= survival_narrow < survival_wide):
        raise AssertionError("narrow aperture should detect fewer atoms")


def test_shot_noise_scaling() -> None:
    k_eff = 1.0e7
    noise_short = atom_interferometer_acceleration_noise(k_eff, 0.1, 1.0e6)
    noise_long = atom_interferometer_acceleration_noise(k_eff, 1.0, 1.0e6)
    assert_close(noise_short / noise_long, 100.0)

    noise_few = atom_interferometer_acceleration_noise(k_eff, 1.0, 1.0e4)
    noise_many = atom_interferometer_acceleration_noise(k_eff, 1.0, 1.0e6)
    assert_close(noise_few / noise_many, 10.0)


def test_design_space_has_one_best_row_per_scenario() -> None:
    rows = evaluate_design_space()
    best = best_rows(rows)
    if len(best) != len(SCENARIOS):
        raise AssertionError("missing best design rows")
    for row in best:
        score = float(row["utility_score"])
        if not (0.0 <= score <= 1.0):
            raise AssertionError("utility score must be bounded")


if __name__ == "__main__":
    test_basic_phase_space_monotonicity()
    test_cloud_and_detection_limits()
    test_shot_noise_scaling()
    test_design_space_has_one_best_row_per_scenario()
    print("phase-space sensor CAD tests passed")
