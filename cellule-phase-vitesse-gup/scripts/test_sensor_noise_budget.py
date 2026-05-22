#!/usr/bin/env python3
from __future__ import annotations

import math

import numpy as np

from simulate_sensor_noise_budget import (
    acceleration_transfer_squared,
    k_effective,
    sigma_phi_laser,
    sigma_phi_vibration,
    total_phase_noise,
)


def test_acceleration_transfer_low_frequency_limit() -> None:
    ti = 0.2
    h2 = acceleration_transfer_squared(np.array([1.0e-6]), ti)[0]
    expected = ti**4
    if not math.isclose(h2, expected, rel_tol=1.0e-4):
        raise AssertionError("acceleration transfer should approach T_i^4 at low frequency")


def test_vibration_isolation_reduces_phase_linearly() -> None:
    k_eff = k_effective(780.241e-9)
    unisolated = sigma_phi_vibration(0.1, k_eff, "typical_lab", 1.0)
    isolated = sigma_phi_vibration(0.1, k_eff, "typical_lab", 0.01)
    if not math.isclose(isolated / unisolated, 0.01, rel_tol=1.0e-3):
        raise AssertionError("vibration phase should scale linearly with ASD isolation")


def test_laser_phase_noise_positive() -> None:
    if sigma_phi_laser(0.1, "good_raman") <= 0.0:
        raise AssertionError("laser phase noise should be positive")


def test_total_phase_noise_exceeds_shot_noise() -> None:
    detected_atoms = 1.0e6
    total = total_phase_noise(
        detected_atoms=detected_atoms,
        contrast=0.6,
        phi_laser=1.0e-3,
        phi_vibration=2.0e-3,
        phi_thermal=5.0e-4,
    )
    if total <= 1.0 / math.sqrt(detected_atoms):
        raise AssertionError("technical phase noise should increase total noise above shot noise")


if __name__ == "__main__":
    test_acceleration_transfer_low_frequency_limit()
    test_vibration_isolation_reduces_phase_linearly()
    test_laser_phase_noise_positive()
    test_total_phase_noise_exceeds_shot_noise()
    print("sensor noise budget tests passed")
