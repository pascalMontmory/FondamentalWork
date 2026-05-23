#!/usr/bin/env python3
from __future__ import annotations

import math

import numpy as np

from simulate_sensor_noise_budget import (
    acceleration_transfer_squared,
    isolation_transfer_asd,
    k_effective,
    sigma_phi_photon_detection,
    sigma_phi_quantum_projection,
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
    unisolated = sigma_phi_vibration(0.1, k_eff, "typical_lab", "constant", 1.0)
    isolated = sigma_phi_vibration(0.1, k_eff, "typical_lab", "constant", 0.01)
    if not math.isclose(isolated / unisolated, 0.01, rel_tol=1.0e-3):
        raise AssertionError("vibration phase should scale linearly with ASD isolation")


def test_frequency_dependent_isolation_is_not_constant_40db() -> None:
    low, mid = isolation_transfer_asd(
        np.array([0.05, 5.0]), "portable_active", 1.0
    )
    if not low > mid:
        raise AssertionError("portable isolation should reject mid-band vibration more than low-frequency vibration")


def test_laser_phase_noise_positive() -> None:
    if sigma_phi_laser(0.1, "good_raman") <= 0.0:
        raise AssertionError("laser phase noise should be positive")


def test_quantum_projection_noise_has_contrast() -> None:
    value = sigma_phi_quantum_projection(1.0e6, contrast=0.5)
    if not math.isclose(value, 2.0e-3, rel_tol=1.0e-12):
        raise AssertionError("QPN should be 1/(C sqrt(N))")


def test_photon_noise_improves_with_more_photons() -> None:
    low = sigma_phi_photon_detection(1.0e5, 0.6, 20.0, 0.25, 10.0)
    high = sigma_phi_photon_detection(1.0e5, 0.6, 200.0, 0.25, 10.0)
    if not high < low:
        raise AssertionError("photon shot noise should improve with collected photons")


def test_total_phase_noise_exceeds_shot_noise() -> None:
    detected_atoms = 1.0e6
    total = total_phase_noise(
        detected_atoms=detected_atoms,
        contrast=0.6,
        phi_laser=1.0e-3,
        phi_vibration=2.0e-3,
        phi_thermal=5.0e-4,
        phi_photon=1.0e-3,
    )
    if total <= sigma_phi_quantum_projection(detected_atoms, 0.6):
        raise AssertionError("technical phase noise should increase total noise above shot noise")


if __name__ == "__main__":
    test_acceleration_transfer_low_frequency_limit()
    test_vibration_isolation_reduces_phase_linearly()
    test_frequency_dependent_isolation_is_not_constant_40db()
    test_laser_phase_noise_positive()
    test_quantum_projection_noise_has_contrast()
    test_photon_noise_improves_with_more_photons()
    test_total_phase_noise_exceeds_shot_noise()
    print("sensor noise budget tests passed")
