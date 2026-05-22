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
    isolation_factor: float
    laser_model: str
    contrast: float
    detected_atoms: float
    cycle_time_s: float
    atom: str
    laser_wavelength_m: float
    room_temperature_k: float
    room_temperature_noise_k: float
    thermal_mech_phase_rad_at_0p1s: float


NOISE_CASES = (
    NoiseCase(
        name="typical_lab_no_isolation",
        seismic_model="typical_lab",
        isolation_factor=1.0,
        laser_model="good_raman",
        contrast=0.55,
        detected_atoms=1.0e6,
        cycle_time_s=1.5,
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=1.0e-3,
    ),
    NoiseCase(
        name="typical_lab_40db_isolation",
        seismic_model="typical_lab",
        isolation_factor=0.01,
        laser_model="good_raman",
        contrast=0.55,
        detected_atoms=1.0e6,
        cycle_time_s=1.5,
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=1.0e-3,
    ),
    NoiseCase(
        name="quiet_site_40db_isolation",
        seismic_model="quiet_site",
        isolation_factor=0.01,
        laser_model="good_raman",
        contrast=0.65,
        detected_atoms=1.0e6,
        cycle_time_s=1.5,
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=5.0e-4,
    ),
    NoiseCase(
        name="urban_40db_isolation",
        seismic_model="urban",
        isolation_factor=0.01,
        laser_model="good_raman",
        contrast=0.50,
        detected_atoms=1.0e6,
        cycle_time_s=1.5,
        atom="Rb87",
        laser_wavelength_m=780.241e-9,
        room_temperature_k=300.0,
        room_temperature_noise_k=1.0e-3,
        thermal_mech_phase_rad_at_0p1s=2.0e-3,
    ),
)


def k_effective(laser_wavelength_m: float, pulse_order: int = 1) -> float:
    return pulse_order * 4.0 * math.pi / laser_wavelength_m


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


def integrate_log_grid(y: np.ndarray, x: np.ndarray) -> float:
    return float(np.trapz(y, x))


def sigma_phi_laser(interrogation_s: float, laser_model: str) -> float:
    f_hz = frequency_grid()
    integrand = laser_phase_transfer_squared(f_hz, interrogation_s) * laser_phase_psd(
        f_hz, laser_model
    )
    return math.sqrt(max(0.0, integrate_log_grid(integrand, f_hz)))


def sigma_phi_vibration(
    interrogation_s: float,
    k_eff_m_inv: float,
    seismic_model: str,
    isolation_factor: float,
) -> float:
    f_hz = frequency_grid()
    accel_asd = seismic_accel_asd(f_hz, seismic_model) * isolation_factor
    accel_psd = accel_asd**2
    displacement_variance = integrate_log_grid(
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
    phi_bbr = 2.0 * math.pi * abs(dnu_hz) * interrogation_s
    phi_mech = mechanical_phase_rad_at_0p1s * (interrogation_s / 0.1)
    return math.sqrt(phi_bbr**2 + phi_mech**2)


def total_phase_noise(
    detected_atoms: float,
    contrast: float,
    phi_laser: float,
    phi_vibration: float,
    phi_thermal: float,
) -> float:
    if detected_atoms <= 0.0 or contrast <= 0.0:
        return math.inf
    shot = 1.0 / math.sqrt(detected_atoms)
    return math.sqrt(
        shot**2
        + (phi_laser / contrast) ** 2
        + (phi_vibration / contrast) ** 2
        + (phi_thermal / contrast) ** 2
    )


def evaluate_noise_case(case: NoiseCase, interrogation_s: float) -> dict[str, float | str]:
    k_eff = k_effective(case.laser_wavelength_m)
    phi_laser = sigma_phi_laser(interrogation_s, case.laser_model)
    phi_vib = sigma_phi_vibration(
        interrogation_s, k_eff, case.seismic_model, case.isolation_factor
    )
    phi_therm = sigma_phi_thermal(
        interrogation_s,
        case.atom,
        case.room_temperature_k,
        case.room_temperature_noise_k,
        case.thermal_mech_phase_rad_at_0p1s,
    )
    phi_total = total_phase_noise(
        case.detected_atoms, case.contrast, phi_laser, phi_vib, phi_therm
    )
    accel_asd = phi_total * math.sqrt(case.cycle_time_s) / (
        k_eff * interrogation_s**2
    )
    species = SPECIES[case.atom]
    return {
        "case": case.name,
        "atom": case.atom,
        "mass_kg": species.mass_kg,
        "interrogation_time_s": interrogation_s,
        "cycle_time_s": case.cycle_time_s,
        "detected_atoms": case.detected_atoms,
        "contrast": case.contrast,
        "k_eff_m_inv": k_eff,
        "seismic_model": case.seismic_model,
        "isolation_factor": case.isolation_factor,
        "laser_model": case.laser_model,
        "sigma_phi_shot_rad": 1.0 / math.sqrt(case.detected_atoms),
        "sigma_phi_laser_rad": phi_laser,
        "sigma_phi_vibration_rad": phi_vib,
        "sigma_phi_thermal_rad": phi_therm,
        "sigma_phi_total_rad": phi_total,
        "accel_noise_m_s2_sqrt_hz": accel_asd,
        "accel_noise_microgal_sqrt_hz": accel_asd / MICROGAL,
    }


def evaluate_grid() -> list[dict[str, float | str]]:
    interrogation_times = np.logspace(math.log10(0.02), math.log10(1.0), 90)
    rows: list[dict[str, float | str]] = []
    for case in NOISE_CASES:
        for interrogation_s in interrogation_times:
            rows.append(evaluate_noise_case(case, float(interrogation_s)))
    return rows


def sample_rows(rows: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    samples = []
    targets = (0.05, 0.10, 0.25, 0.50, 1.00)
    for case in NOISE_CASES:
        subset = [row for row in rows if row["case"] == case.name]
        for target in targets:
            samples.append(
                min(
                    subset,
                    key=lambda row: abs(float(row["interrogation_time_s"]) - target),
                )
            )
    return samples


def write_outputs(rows: list[dict[str, float | str]]) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    with (DATA / "sensor_noise_budget.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "model_status": "engineering_noise_budget_proxy",
        "warning": (
            "This is not a calibrated instrument model. Laser PSD, seismic PSD, "
            "thermal phase and isolation factors are explicit envelope inputs."
        ),
        "formulae": [
            "sigma_phi_laser^2 = integral |H_phi(f)|^2 S_phi(f) df",
            "|H_phi(f)|^2 ~= 16 sin^4(pi f T_i)",
            "sigma_phi_vib^2 = k_eff^2 integral |H_a(f)|^2 S_a(f) df",
            "|H_a(f)|^2 ~= [4 sin^2(pi f T_i)/(2 pi f)^2]^2",
            "sigma_phi_total^2 = 1/N + (phi_laser/C)^2 + (phi_vib/C)^2 + (phi_thermal/C)^2",
            "delta a_sqrtHz = sigma_phi_total sqrt(T_cycle)/(k_eff T_i^2)",
        ],
        "cases": [asdict(case) for case in NOISE_CASES],
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
        "replaced by measured laser, seismometer and thermal data for a real design.",
        "",
        "## Equations",
        "",
        "```text",
        "sigma_phi_laser^2 = integral |H_phi(f)|^2 S_phi(f) df",
        "|H_phi(f)|^2 ~= 16 sin^4(pi f T_i)",
        "sigma_phi_vib^2 = k_eff^2 integral |H_a(f)|^2 S_a(f) df",
        "|H_a(f)|^2 ~= [4 sin^2(pi f T_i)/(2 pi f)^2]^2",
        "sigma_phi_total^2 = 1/N + (phi_laser/C)^2 + (phi_vib/C)^2 + (phi_thermal/C)^2",
        "delta a_sqrtHz = sigma_phi_total sqrt(T_cycle)/(k_eff T_i^2)",
        "```",
        "",
        "The vibration model uses acceleration PSD envelopes in `(m/s2)^2/Hz`.",
        "The isolation factor multiplies acceleration amplitude spectral density,",
        "so `0.01` corresponds to about `-40 dB` amplitude isolation.",
        "",
        "## Sample values",
        "",
        "| case | Ti [s] | laser [rad] | vib [rad] | thermal [rad] | total [rad] | delta a [microGal/sqrtHz] |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in sample_rows(rows):
        lines.append(
            "| {case} | {interrogation_time_s:.3f} | {sigma_phi_laser_rad:.2e} | "
            "{sigma_phi_vibration_rad:.2e} | {sigma_phi_thermal_rad:.2e} | "
            "{sigma_phi_total_rad:.2e} | {accel_noise_microgal_sqrt_hz:.2e} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Without isolation, vibration dominates quickly as `T_i` grows.",
            "- With `-40 dB` vibration isolation, the same source budget can move into",
            "  the `10-50 microGal/sqrtHz` transportable range for realistic",
            "  interrogation times, depending on contrast and cycle time.",
            "- The laser phase model is intentionally an envelope. A real Raman system",
            "  must replace it by the measured relative phase-noise PSD.",
            "- The thermal term combines BBR sensitivity and a mechanical thermal",
            "  phase proxy. It is usually not the dominant per-shot term here, but it",
            "  matters for drift, systematics and Allan deviation.",
            "",
            "Data: `reports/data/sensor_noise_budget.csv`",
            "",
            "Figure: `reports/figures/sensor_noise_budget.png`",
        ]
    )
    (REPORTS / "sensor_noise_budget_report.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def plot(rows: list[dict[str, float | str]]) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
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
    ax.set_title("Technical noise budget proxy for a cold-atom gravimeter")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURES / "sensor_noise_budget.png", dpi=180)
    plt.close(fig)


def main() -> None:
    rows = evaluate_grid()
    write_outputs(rows)
    plot(rows)
    print(f"wrote sensor noise budget outputs to {REPORTS}")


if __name__ == "__main__":
    main()
