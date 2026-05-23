#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from phase_space_gas_common import SPECIES


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
DATA = REPORTS / "data"
FIGURES = REPORTS / "figures"
MICROGAL = 1.0e-8


@dataclass(frozen=True)
class NoiseCase:
    name: str
    seismic_model: str
    isolation_model: str
    isolation_factor: float
    laser_model: str
    contrast: float
    detected_atoms: float
    source_prep_time_s: float
    detection_time_s: float
    dead_time_s: float
    photons_per_atom: float
    detection_efficiency: float
    photon_excess_noise_factor: float
    detection_method: str
    atom: str
    laser_wavelength_m: float
    room_temperature_k: float
    room_temperature_noise_k: float
    thermal_mech_phase_rad_at_0p1s: float
    magnetic_noise_model: str
    magnetic_sensitivity_hz_per_t: float
    benchmark_microgal_sqrt_hz: float | None = None
    benchmark_label: str = ""


NOISE_CASES = (
    NoiseCase(
        name="typical_lab_no_isolation",
        seismic_model="typical_lab",
        isolation_model="none",
        isolation_factor=1.0,
        laser_model="good_raman",
        contrast=0.55,
        detected_atoms=1.0e6,
        source_prep_time_s=0.90,
        detection_time_s=0.10,
        dead_time_s=0.10,
        photons_per_atom=80.0,
        detection_efficiency=0.25,
        photon_excess_noise_factor=15.0,
        detection_method="fluorescence_2d",
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=1.0e-3,
        magnetic_noise_model="portable_shielded",
        magnetic_sensitivity_hz_per_t=1.0e4,
    ),
    NoiseCase(
        name="typical_lab_constant_40db",
        seismic_model="typical_lab",
        isolation_model="constant",
        isolation_factor=0.01,
        laser_model="good_raman",
        contrast=0.55,
        detected_atoms=1.0e6,
        source_prep_time_s=0.90,
        detection_time_s=0.10,
        dead_time_s=0.10,
        photons_per_atom=80.0,
        detection_efficiency=0.25,
        photon_excess_noise_factor=15.0,
        detection_method="fluorescence_2d",
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=1.0e-3,
        magnetic_noise_model="portable_shielded",
        magnetic_sensitivity_hz_per_t=1.0e4,
    ),
    NoiseCase(
        name="typical_lab_active_portable",
        seismic_model="typical_lab",
        isolation_model="portable_active",
        isolation_factor=1.0,
        laser_model="good_raman",
        contrast=0.55,
        detected_atoms=1.0e6,
        source_prep_time_s=0.90,
        detection_time_s=0.10,
        dead_time_s=0.10,
        photons_per_atom=80.0,
        detection_efficiency=0.25,
        photon_excess_noise_factor=15.0,
        detection_method="fluorescence_2d",
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=1.0e-3,
        magnetic_noise_model="portable_shielded",
        magnetic_sensitivity_hz_per_t=1.0e4,
    ),
    NoiseCase(
        name="sr88_nominal_typical_lab_active",
        seismic_model="typical_lab",
        isolation_model="portable_active",
        isolation_factor=1.0,
        laser_model="good_raman",
        contrast=0.60,
        detected_atoms=8.0e5,
        source_prep_time_s=0.85,
        detection_time_s=0.10,
        dead_time_s=0.10,
        photons_per_atom=120.0,
        detection_efficiency=0.30,
        photon_excess_noise_factor=12.0,
        detection_method="fluorescence_high_na_proxy",
        atom="Sr88",
        laser_wavelength_m=689.449e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=7.0e-4,
        magnetic_noise_model="portable_shielded",
        magnetic_sensitivity_hz_per_t=1.0e3,
    ),
    NoiseCase(
        name="nim_like_active_105ms",
        seismic_model="typical_lab",
        isolation_model="cs_avi_like",
        isolation_factor=1.0,
        laser_model="good_raman",
        contrast=0.45,
        detected_atoms=1.5e5,
        source_prep_time_s=0.68,
        detection_time_s=0.08,
        dead_time_s=0.03,
        photons_per_atom=60.0,
        detection_efficiency=0.25,
        photon_excess_noise_factor=20.0,
        detection_method="fluorescence_transportable_proxy",
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=1.0e-3,
        magnetic_noise_model="portable_shielded",
        magnetic_sensitivity_hz_per_t=1.0e4,
        benchmark_microgal_sqrt_hz=20.5,
        benchmark_label="NIM transportable atomic gravimeter lab benchmark",
    ),
    NoiseCase(
        name="muquans_like_quiet_site",
        seismic_model="quiet_site",
        isolation_model="feedforward_compensation",
        isolation_factor=1.0,
        laser_model="good_raman",
        contrast=0.35,
        detected_atoms=1.0e5,
        source_prep_time_s=0.30,
        detection_time_s=0.08,
        dead_time_s=0.02,
        photons_per_atom=50.0,
        detection_efficiency=0.25,
        photon_excess_noise_factor=20.0,
        detection_method="fluorescence_transportable_proxy",
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=1.2e-3,
        magnetic_noise_model="portable_shielded",
        magnetic_sensitivity_hz_per_t=1.0e4,
        benchmark_microgal_sqrt_hz=50.0,
        benchmark_label="Muquans/Exail AQG quiet-site datasheet",
    ),
)


def k_effective(laser_wavelength_m: float, pulse_order: int = 1) -> float:
    return pulse_order * 4.0 * math.pi / laser_wavelength_m


def experimental_cycle_time(case: NoiseCase, interrogation_s: float) -> float:
    return (
        case.source_prep_time_s
        + 2.0 * interrogation_s
        + case.detection_time_s
        + case.dead_time_s
    )


def frequency_grid() -> np.ndarray:
    return np.logspace(-2, 2, 2500)


def log_interp_asd(
    f_hz: np.ndarray, points: tuple[tuple[float, float], ...]
) -> np.ndarray:
    xp = np.log10(np.array([point[0] for point in points], dtype=float))
    yp = np.log10(np.array([point[1] for point in points], dtype=float))
    return 10.0 ** np.interp(np.log10(f_hz), xp, yp)


def seismic_accel_asd(f_hz: np.ndarray, model: str) -> np.ndarray:
    """Acceleration ASD in m/s^2/sqrt(Hz), approximate design envelopes."""
    envelopes = {
        "quiet_site": (
            (0.01, 3.0e-10),
            (0.10, 1.0e-9),
            (1.00, 3.0e-8),
            (10.0, 1.0e-7),
            (100.0, 3.0e-7),
        ),
        "typical_lab": (
            (0.01, 2.0e-8),
            (0.10, 5.0e-8),
            (1.00, 3.0e-7),
            (10.0, 3.0e-7),
            (100.0, 1.0e-6),
        ),
        "urban": (
            (0.01, 3.0e-7),
            (0.10, 1.0e-6),
            (1.00, 1.0e-5),
            (10.0, 1.0e-4),
            (100.0, 3.0e-4),
        ),
    }
    if model not in envelopes:
        raise ValueError(f"unknown seismic model: {model}")
    return log_interp_asd(f_hz, envelopes[model])


def isolation_transfer_asd(f_hz: np.ndarray, model: str, scalar: float) -> np.ndarray:
    """Amplitude transfer from ground acceleration ASD to retroreflector ASD."""
    if model == "none":
        return np.ones_like(f_hz) * scalar
    if model == "constant":
        return np.ones_like(f_hz) * scalar
    if model == "portable_active":
        points = (
            (0.01, 1.40),
            (0.05, 1.20),
            (0.10, 1.00),
            (0.20, 0.60),
            (0.50, 0.20),
            (1.00, 0.08),
            (5.00, 0.03),
            (30.0, 0.04),
            (100.0, 0.15),
        )
    elif model == "cs_avi_like":
        points = (
            (0.01, 0.80),
            (0.05, 0.45),
            (0.10, 0.30),
            (0.20, 0.18),
            (0.50, 0.08),
            (1.00, 0.035),
            (5.00, 0.020),
            (30.0, 0.035),
            (100.0, 0.12),
        )
    elif model == "feedforward_compensation":
        points = (
            (0.01, 1.00),
            (0.05, 0.80),
            (0.10, 0.55),
            (0.20, 0.35),
            (0.50, 0.16),
            (1.00, 0.08),
            (5.00, 0.05),
            (30.0, 0.06),
            (100.0, 0.20),
        )
    else:
        raise ValueError(f"unknown isolation model: {model}")
    return log_interp_asd(f_hz, points) * scalar


def magnetic_noise_asd_t_per_sqrt_hz(f_hz: np.ndarray, model: str) -> np.ndarray:
    """Magnetic field ASD proxy in tesla/sqrt(Hz)."""
    envelopes = {
        "low_noise_shielded": (
            (0.01, 3.0e-12),
            (0.10, 2.0e-12),
            (1.00, 1.0e-12),
            (10.0, 1.5e-12),
            (100.0, 4.0e-12),
        ),
        "portable_shielded": (
            (0.01, 5.0e-11),
            (0.10, 3.0e-11),
            (1.00, 1.5e-11),
            (10.0, 2.0e-11),
            (100.0, 8.0e-11),
        ),
        "unshielded_lab": (
            (0.01, 5.0e-10),
            (0.10, 2.0e-10),
            (1.00, 1.0e-10),
            (10.0, 2.0e-10),
            (100.0, 8.0e-10),
        ),
    }
    if model not in envelopes:
        raise ValueError(f"unknown magnetic noise model: {model}")
    return log_interp_asd(f_hz, envelopes[model])


def laser_phase_psd(f_hz: np.ndarray, model: str) -> np.ndarray:
    """Raman relative phase PSD in rad^2/Hz, intentionally simple envelopes."""
    if model == "excellent_raman":
        white = 3.0e-8
        flicker = 3.0e-8
    elif model == "good_raman":
        white = 1.0e-7
        flicker = 1.0e-7
    elif model == "noisy_raman":
        white = 1.0e-6
        flicker = 3.0e-6
    else:
        raise ValueError(f"unknown laser model: {model}")
    return white + flicker / np.maximum(f_hz, 1.0e-3)


def laser_phase_transfer_squared(f_hz: np.ndarray, interrogation_s: float) -> np.ndarray:
    return 16.0 * np.sin(math.pi * f_hz * interrogation_s) ** 4


def acceleration_transfer_squared(f_hz: np.ndarray, interrogation_s: float) -> np.ndarray:
    omega = 2.0 * math.pi * f_hz
    response = 4.0 * np.sin(math.pi * f_hz * interrogation_s) ** 2 / omega**2
    return response**2


def frequency_noise_transfer_squared(f_hz: np.ndarray, interrogation_s: float) -> np.ndarray:
    tau = 2.0 * interrogation_s
    response = np.empty_like(f_hz)
    small = f_hz < 1.0e-9
    response[small] = tau**2
    response[~small] = (np.sin(math.pi * f_hz[~small] * tau) / (math.pi * f_hz[~small])) ** 2
    return response


def integrate_grid(y: np.ndarray, x: np.ndarray) -> float:
    return float(np.trapz(y, x))


def sigma_phi_laser(interrogation_s: float, laser_model: str) -> float:
    f_hz = frequency_grid()
    integrand = laser_phase_transfer_squared(f_hz, interrogation_s) * laser_phase_psd(
        f_hz, laser_model
    )
    return math.sqrt(max(0.0, integrate_grid(integrand, f_hz)))


def sigma_phi_vibration(
    interrogation_s: float,
    k_eff_m_inv: float,
    seismic_model: str,
    isolation_model: str,
    isolation_factor: float,
) -> float:
    f_hz = frequency_grid()
    accel_asd = (
        seismic_accel_asd(f_hz, seismic_model)
        * isolation_transfer_asd(f_hz, isolation_model, isolation_factor)
    )
    accel_psd = accel_asd**2
    displacement_variance = integrate_grid(
        acceleration_transfer_squared(f_hz, interrogation_s) * accel_psd, f_hz
    )
    return k_eff_m_inv * math.sqrt(max(0.0, displacement_variance))


def bbr_shift_hz_at_300(atom: str) -> float:
    """Order-of-magnitude BBR shift proxy at 300 K for relevant clock states."""
    return {
        "Rb87": 8.6e-5,
        "Cs133": 1.7e-2,
        "Sr88": 2.0,
        "Yb174": 1.3,
    }.get(atom, 1.0e-4)


def sigma_phi_thermal(
    interrogation_s: float,
    atom: str,
    room_temperature_k: float,
    room_temperature_noise_k: float,
    mechanical_phase_rad_at_0p1s: float,
) -> float:
    shift_300 = bbr_shift_hz_at_300(atom)
    fractional_temperature_noise = 4.0 * room_temperature_noise_k / room_temperature_k
    dnu_hz = shift_300 * (room_temperature_k / 300.0) ** 4 * fractional_temperature_noise
    tau = 2.0 * interrogation_s
    phi_bbr = 2.0 * math.pi * abs(dnu_hz) * tau
    phi_mech = mechanical_phase_rad_at_0p1s * (interrogation_s / 0.1)
    return math.sqrt(phi_bbr**2 + phi_mech**2)


def sigma_phi_johnson(
    interrogation_s: float,
    magnetic_noise_model: str,
    magnetic_sensitivity_hz_per_t: float,
) -> float:
    f_hz = frequency_grid()
    b_asd = magnetic_noise_asd_t_per_sqrt_hz(f_hz, magnetic_noise_model)
    frequency_psd = (magnetic_sensitivity_hz_per_t * b_asd) ** 2
    phase_variance = (2.0 * math.pi) ** 2 * integrate_grid(
        frequency_noise_transfer_squared(f_hz, interrogation_s) * frequency_psd,
        f_hz,
    )
    return math.sqrt(max(0.0, phase_variance))


def sigma_phi_quantum_projection(detected_atoms: float, contrast: float) -> float:
    if detected_atoms <= 0.0 or contrast <= 0.0:
        return math.inf
    return 1.0 / (contrast * math.sqrt(detected_atoms))


def sigma_phi_photon_detection(
    detected_atoms: float,
    contrast: float,
    photons_per_atom: float,
    detection_efficiency: float,
    excess_noise_factor: float,
) -> float:
    if (
        detected_atoms <= 0.0
        or contrast <= 0.0
        or photons_per_atom <= 0.0
        or detection_efficiency <= 0.0
    ):
        return math.inf
    detected_photons = photons_per_atom * detected_atoms * detection_efficiency
    population_noise = excess_noise_factor / math.sqrt(detected_photons)
    return population_noise / contrast


def phase_variance_components(
    detected_atoms: float,
    contrast: float,
    phi_laser: float,
    phi_vibration: float,
    phi_thermal: float,
    phi_johnson: float,
    phi_photon: float,
) -> dict[str, float]:
    if detected_atoms <= 0.0 or contrast <= 0.0:
        return {
            "qpn": math.inf,
            "photon": math.inf,
            "laser": math.inf,
            "vibration": math.inf,
            "thermal": math.inf,
            "johnson": math.inf,
        }
    return {
        "qpn": sigma_phi_quantum_projection(detected_atoms, contrast) ** 2,
        "photon": phi_photon**2,
        "laser": (phi_laser / contrast) ** 2,
        "vibration": (phi_vibration / contrast) ** 2,
        "thermal": (phi_thermal / contrast) ** 2,
        "johnson": (phi_johnson / contrast) ** 2,
    }


def total_phase_noise_from_components(components: dict[str, float]) -> float:
    return math.sqrt(sum(components.values()))


def total_phase_noise(
    detected_atoms: float,
    contrast: float,
    phi_laser: float,
    phi_vibration: float,
    phi_thermal: float,
    phi_johnson: float = 0.0,
    phi_photon: float = 0.0,
) -> float:
    return total_phase_noise_from_components(
        phase_variance_components(
            detected_atoms,
            contrast,
            phi_laser,
            phi_vibration,
            phi_thermal,
            phi_johnson,
            phi_photon,
        )
    )


def dominant_component(components: dict[str, float]) -> str:
    return max(components, key=components.get)


def evaluate_noise_case(case: NoiseCase, interrogation_s: float) -> dict[str, float | str]:
    k_eff = k_effective(case.laser_wavelength_m)
    cycle_time_s = experimental_cycle_time(case, interrogation_s)
    phi_laser = sigma_phi_laser(interrogation_s, case.laser_model)
    phi_vib = sigma_phi_vibration(
        interrogation_s,
        k_eff,
        case.seismic_model,
        case.isolation_model,
        case.isolation_factor,
    )
    phi_therm = sigma_phi_thermal(
        interrogation_s,
        case.atom,
        case.room_temperature_k,
        case.room_temperature_noise_k,
        case.thermal_mech_phase_rad_at_0p1s,
    )
    phi_johnson = sigma_phi_johnson(
        interrogation_s,
        case.magnetic_noise_model,
        case.magnetic_sensitivity_hz_per_t,
    )
    phi_photon = sigma_phi_photon_detection(
        case.detected_atoms,
        case.contrast,
        case.photons_per_atom,
        case.detection_efficiency,
        case.photon_excess_noise_factor,
    )
    components = phase_variance_components(
        case.detected_atoms,
        case.contrast,
        phi_laser,
        phi_vib,
        phi_therm,
        phi_johnson,
        phi_photon,
    )
    phi_total = total_phase_noise_from_components(components)
    component_total = sum(components.values())
    accel_asd = phi_total * math.sqrt(cycle_time_s) / (k_eff * interrogation_s**2)
    species = SPECIES[case.atom]
    row: dict[str, float | str] = {
        "case": case.name,
        "atom": case.atom,
        "mass_kg": species.mass_kg,
        "interrogation_time_s": interrogation_s,
        "cycle_time_s": cycle_time_s,
        "source_prep_time_s": case.source_prep_time_s,
        "detection_time_s": case.detection_time_s,
        "dead_time_s": case.dead_time_s,
        "photons_per_atom": case.photons_per_atom,
        "detection_efficiency": case.detection_efficiency,
        "photon_excess_noise_factor": case.photon_excess_noise_factor,
        "detection_method": case.detection_method,
        "detected_atoms": case.detected_atoms,
        "contrast": case.contrast,
        "k_eff_m_inv": k_eff,
        "seismic_model": case.seismic_model,
        "isolation_model": case.isolation_model,
        "isolation_factor": case.isolation_factor,
        "laser_model": case.laser_model,
        "magnetic_noise_model": case.magnetic_noise_model,
        "magnetic_sensitivity_hz_per_t": case.magnetic_sensitivity_hz_per_t,
        "sigma_phi_qpn_rad": sigma_phi_quantum_projection(
            case.detected_atoms, case.contrast
        ),
        "sigma_phi_photon_rad": phi_photon,
        "sigma_phi_laser_rad": phi_laser,
        "sigma_phi_vibration_rad": phi_vib,
        "sigma_phi_thermal_rad": phi_therm,
        "sigma_phi_johnson_rad": phi_johnson,
        "sigma_phi_total_rad": phi_total,
        "accel_noise_m_s2_sqrt_hz": accel_asd,
        "accel_noise_microgal_sqrt_hz": accel_asd / MICROGAL,
        "dominant_noise": dominant_component(components),
    }
    for name, value in components.items():
        row[f"variance_fraction_{name}"] = value / component_total if component_total else math.nan
    return row


def evaluate_grid() -> list[dict[str, float | str]]:
    interrogation_times = np.logspace(math.log10(0.02), math.log10(1.0), 90)
    rows: list[dict[str, float | str]] = []
    for case in NOISE_CASES:
        for interrogation_s in interrogation_times:
            rows.append(evaluate_noise_case(case, float(interrogation_s)))
    return rows


def closest_row(
    rows: list[dict[str, float | str]], case_name: str, interrogation_s: float
) -> dict[str, float | str]:
    subset = [row for row in rows if row["case"] == case_name]
    if not subset:
        raise ValueError(f"case not found: {case_name}")
    return min(
        subset,
        key=lambda row: abs(float(row["interrogation_time_s"]) - interrogation_s),
    )


def sample_rows(rows: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    samples = []
    targets = (0.05, 0.10, 0.25, 0.50, 1.00)
    for case in NOISE_CASES:
        for target in targets:
            samples.append(closest_row(rows, case.name, target))
    return samples


def benchmark_rows(rows: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    output = []
    for case in NOISE_CASES:
        if case.benchmark_microgal_sqrt_hz is None:
            continue
        target_t = 0.105 if "nim" in case.name else 0.100
        row = dict(closest_row(rows, case.name, target_t))
        simulated = float(row["accel_noise_microgal_sqrt_hz"])
        target = case.benchmark_microgal_sqrt_hz
        row["benchmark_microgal_sqrt_hz"] = target
        row["benchmark_label"] = case.benchmark_label
        row["model_to_benchmark_ratio"] = simulated / target
        output.append(row)
    return output


def nominal_contribution_row(rows: list[dict[str, float | str]]) -> dict[str, float | str]:
    return closest_row(rows, "sr88_nominal_typical_lab_active", 0.100)


def write_outputs(rows: list[dict[str, float | str]]) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    with (DATA / "sensor_noise_budget.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    nominal = nominal_contribution_row(rows)
    summary = {
        "model_status": "engineering_noise_budget_proxy",
        "warning": (
            "This is not a calibrated instrument model. Laser PSD, seismic PSD, "
            "thermal phase, Johnson-Nyquist magnetic noise and isolation transfer "
            "functions are explicit envelope inputs."
        ),
        "formulae": [
            "sigma_phi_laser^2 = integral |H_phi(f)|^2 S_phi(f) df",
            "|H_phi(f)|^2 ~= 16 sin^4(pi f T_i)",
            "sigma_phi_vib^2 = k_eff^2 integral |H_a(f)|^2 S_a(f) df",
            "|H_a(f)|^2 ~= [4 sin^2(pi f T_i)/(2 pi f)^2]^2",
            "sigma_phi_JN^2 = (2 pi)^2 integral |H_nu(f)|^2 (dnu/dB)^2 S_B(f) df",
            "sigma_phi_QPN = 1/(C sqrt(N_at))",
            "sigma_phi_photon = F_excess/(C sqrt(N_ph_per_atom N_at eta_det))",
            "sigma_phi_total^2 = phi_QPN^2 + phi_photon^2 + (phi_laser/C)^2 + (phi_vib/C)^2 + (phi_thermal/C)^2 + (phi_JN/C)^2",
            "T_cycle = T_prep + 2 T_i + T_detection + T_dead",
            "delta a_sqrtHz = sigma_phi_total sqrt(T_cycle)/(k_eff T_i^2)",
        ],
        "cases": [asdict(case) for case in NOISE_CASES],
        "nominal_contribution_row": nominal,
        "benchmarks": benchmark_rows(rows),
        "sample_rows": sample_rows(rows),
    }
    (REPORTS / "sensor_noise_budget_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    lines = [
        "# Sensor technical noise budget",
        "",
        "This report extends the phase-space CAD proxy with first-order technical",
        "noise envelopes for a three-pulse cold-atom gravimeter.",
        "",
        "The model is useful for ranking assumptions, not for certifying an",
        "instrument. The PSDs and coefficients are explicit inputs that must be",
        "replaced by measured laser, seismometer, magnetometer and thermal data for",
        "a real design.",
        "",
        "## Model status",
        "",
        "| block | status | comment |",
        "|---|---|---|",
        "| quantum projection noise | standard quantum limit | `1/(C sqrt(N_at))` |",
        "| photon shot noise | detection proxy | Poisson photon count with detection efficiency and excess imaging noise |",
        "| laser phase noise | envelope PSD | replace by measured Raman relative phase PSD |",
        "| seismic vibration | envelope PSD + isolation transfer | constant `-40 dB` is kept only as an optimistic bound |",
        "| thermal drift | proxy | BBR plus mechanical thermal phase; not a calibrated Allan model |",
        "| Johnson-Nyquist magnetic noise | proxy | magnetic ASD times explicit `dnu/dB` sensitivity |",
        "| duty cycle | explicit | `T_cycle = T_prep + 2 T_i + T_detection + T_dead` |",
        "",
        "## Equations",
        "",
        "```text",
        "sigma_phi_laser^2 = integral |H_phi(f)|^2 S_phi(f) df",
        "|H_phi(f)|^2 ~= 16 sin^4(pi f T_i)",
        "sigma_phi_vib^2 = k_eff^2 integral |H_a(f)|^2 S_a(f) df",
        "|H_a(f)|^2 ~= [4 sin^2(pi f T_i)/(2 pi f)^2]^2",
        "sigma_phi_JN^2 = (2 pi)^2 integral |H_nu(f)|^2 (dnu/dB)^2 S_B(f) df",
        "sigma_phi_QPN = 1/(C sqrt(N_at))",
        "sigma_phi_photon = F_excess/(C sqrt(N_ph_per_atom N_at eta_det))",
        "sigma_phi_total^2 = phi_QPN^2 + phi_photon^2 + (phi_laser/C)^2 + (phi_vib/C)^2 + (phi_thermal/C)^2 + (phi_JN/C)^2",
        "T_cycle = T_prep + 2 T_i + T_detection + T_dead",
        "delta a_sqrtHz = sigma_phi_total sqrt(T_cycle)/(k_eff T_i^2)",
        "```",
        "",
        "## Nominal contribution budget",
        "",
        "Nominal case: `sr88_nominal_typical_lab_active`, closest point to `T_i = 100 ms`.",
        "",
        "| contribution | variance fraction [%] | phase term [rad] |",
        "|---|---:|---:|",
    ]
    for name, phase_key in (
        ("qpn", "sigma_phi_qpn_rad"),
        ("photon", "sigma_phi_photon_rad"),
        ("laser", "sigma_phi_laser_rad"),
        ("vibration", "sigma_phi_vibration_rad"),
        ("thermal", "sigma_phi_thermal_rad"),
        ("johnson", "sigma_phi_johnson_rad"),
    ):
        lines.append(
            "| {name} | {fraction:.2f} | {phase:.2e} |".format(
                name=name,
                fraction=100.0 * float(nominal[f"variance_fraction_{name}"]),
                phase=float(nominal[phase_key]),
            )
        )
    lines.extend(
        [
            "",
            "Result at this point:",
            "",
            "```text",
            "T_i = {ti:.3f} s".format(ti=float(nominal["interrogation_time_s"])),
            "T_cycle = {cycle:.3f} s".format(cycle=float(nominal["cycle_time_s"])),
            "dominant_noise = {dominant}".format(dominant=nominal["dominant_noise"]),
            "delta a = {noise:.2f} microGal/sqrtHz".format(
                noise=float(nominal["accel_noise_microgal_sqrt_hz"])
            ),
            "```",
            "",
            "## Benchmark sanity check",
            "",
            "| model case | published reference | T_i [s] | model [microGal/sqrtHz] | reference [microGal/sqrtHz] | ratio |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in benchmark_rows(rows):
        lines.append(
            "| {case} | {label} | {ti:.3f} | {model:.2f} | {target:.2f} | {ratio:.2f} |".format(
                case=row["case"],
                label=row["benchmark_label"],
                ti=float(row["interrogation_time_s"]),
                model=float(row["accel_noise_microgal_sqrt_hz"]),
                target=float(row["benchmark_microgal_sqrt_hz"]),
                ratio=float(row["model_to_benchmark_ratio"]),
            )
        )
    lines.extend(
        [
            "",
            "The benchmark cases are not fitted instruments. They are sanity checks:",
            "the model should land in the same order of magnitude only after choosing",
            "reasonable atom number, contrast, cycle time and isolation envelopes.",
            "",
            "Public anchors used here:",
            "",
            "- Muquans/Exail AQG: `50 microGal/sqrtHz` sensitivity at a quiet place;",
            "- NIM transportable atomic gravimeter: `20.5 microGal/sqrtHz` in the",
            "  laboratory and `10.8 microGal/sqrtHz` in a seismic station, with a",
            "  `105 ms` interrogation time and `1 s` measurement cycle reported.",
            "",
            "## Sample scan values",
            "",
            "| case | Ti [s] | cycle [s] | QPN [rad] | photon [rad] | laser [rad] | vib [rad] | thermal [rad] | JN [rad] | dominant | delta a [microGal/sqrtHz] |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|",
        ]
    )
    for row in sample_rows(rows):
        lines.append(
            "| {case} | {interrogation_time_s:.3f} | {cycle_time_s:.3f} | "
            "{sigma_phi_qpn_rad:.2e} | {sigma_phi_photon_rad:.2e} | "
            "{sigma_phi_laser_rad:.2e} | {sigma_phi_vibration_rad:.2e} | "
            "{sigma_phi_thermal_rad:.2e} | {sigma_phi_johnson_rad:.2e} | "
            "{dominant_noise} | {accel_noise_microgal_sqrt_hz:.2e} |".format(**row)
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- The constant `-40 dB` isolation case is an optimistic lower-bound",
            "  envelope, not a portable-system claim.",
            "- The `portable_active`, `cs_avi_like` and `feedforward_compensation`",
            "  cases use frequency-dependent isolation transfer functions, including",
            "  weak or no rejection at the lowest frequencies.",
            "- The photon-shot term is separated from QPN because imaging background,",
            "  camera readout and optical collection can make it much larger than the",
            "  ideal Poisson limit; this is represented by `photon_excess_noise_factor`.",
            "- The Johnson-Nyquist term is normally small in these nominal cases, but",
            "  it is now explicit and can dominate if shielding is poor or if the",
            "  chosen transition has a large `dnu/dB` sensitivity.",
            "- The duty cycle matters directly through `sqrt(T_cycle)`. Long source",
            "  preparation can erase part of the gain from increasing `T_i`.",
            "",
            "Data: `reports/data/sensor_noise_budget.csv`",
            "",
            "Figures:",
            "",
            "- `reports/figures/sensor_noise_budget.png`",
            "- `reports/figures/sensor_noise_dominance.png`",
        ]
    )
    (REPORTS / "sensor_noise_budget_report.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def plot_noise(rows: list[dict[str, float | str]]) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9.8, 5.8))
    for case in NOISE_CASES:
        subset = [row for row in rows if row["case"] == case.name]
        ti = [float(row["interrogation_time_s"]) for row in subset]
        noise = [float(row["accel_noise_microgal_sqrt_hz"]) for row in subset]
        ax.plot(ti, noise, linewidth=2.0, label=case.name.replace("_", " "))
    ax.axhline(10.0, color="black", linestyle="--", linewidth=1.0, label="10 microGal/sqrtHz")
    ax.axhline(50.0, color="gray", linestyle=":", linewidth=1.0, label="50 microGal/sqrtHz")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("interrogation time Ti [s]")
    ax.set_ylabel("acceleration noise [microGal/sqrtHz]")
    ax.set_title("Technical noise budget proxy for cold-atom gravimeters")
    ax.legend(fontsize=6)
    fig.tight_layout()
    fig.savefig(FIGURES / "sensor_noise_budget.png", dpi=180)
    plt.close(fig)


def plot_dominance(rows: list[dict[str, float | str]]) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    subset = [row for row in rows if row["case"] == "sr88_nominal_typical_lab_active"]
    ti = np.array([float(row["interrogation_time_s"]) for row in subset])
    fig, ax = plt.subplots(figsize=(9.8, 5.8))
    for name in ("qpn", "photon", "laser", "vibration", "thermal", "johnson"):
        frac = np.array([100.0 * float(row[f"variance_fraction_{name}"]) for row in subset])
        ax.plot(ti, frac, linewidth=2.0, label=name)
    ax.set_xscale("log")
    ax.set_ylim(0.0, 105.0)
    ax.set_xlabel("interrogation time Ti [s]")
    ax.set_ylabel("phase-variance contribution [%]")
    ax.set_title("Dominant-noise sensitivity scan: Sr88 nominal lab-active case")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "sensor_noise_dominance.png", dpi=180)
    plt.close(fig)


def main() -> None:
    rows = evaluate_grid()
    write_outputs(rows)
    plot_noise(rows)
    plot_dominance(rows)
    print(f"wrote sensor noise budget outputs to {REPORTS}")


if __name__ == "__main__":
    main()
