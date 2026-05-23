#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from phase_space_gas_common import (
    SPECIES,
    atom_interferometer_acceleration_noise,
    atom_interferometer_rotation_noise,
    cloud_radius_after_time,
    degeneracy_parameter,
    gaussian_cubic_survival_fraction,
    thermal_wavelength,
    velocity_sigma_1d,
)


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"
DATA = REPORTS / "data"


@dataclass(frozen=True)
class Scenario:
    name: str
    species: str
    laser_wavelength_m: float
    central_density_m3: float
    initial_atoms: float
    initial_radius_m: float
    aperture_radius_m: float
    interrogation_times_s: tuple[float, ...]
    target_accel_noise_m_s2: float | None
    target_rotation_noise_rad_s: float | None
    transverse_velocity_m_s: float
    pulse_order: int
    practical_temperature_floor_k: float
    mission: str


SCENARIOS = (
    Scenario(
        name="gps_denied_inertial_accelerometer",
        species="Rb87",
        laser_wavelength_m=780.241e-9,
        central_density_m3=1.0e18,
        initial_atoms=1.0e6,
        initial_radius_m=0.8e-3,
        aperture_radius_m=12.0e-3,
        interrogation_times_s=(0.05, 0.10, 0.25, 0.50, 1.00),
        target_accel_noise_m_s2=1.0e-7,
        target_rotation_noise_rad_s=None,
        transverse_velocity_m_s=0.0,
        pulse_order=1,
        practical_temperature_floor_k=1.0e-7,
        mission="navigation inertielle sans GPS",
    ),
    Scenario(
        name="field_gravimeter",
        species="Rb87",
        laser_wavelength_m=780.241e-9,
        central_density_m3=5.0e17,
        initial_atoms=2.0e6,
        initial_radius_m=1.2e-3,
        aperture_radius_m=18.0e-3,
        interrogation_times_s=(0.10, 0.25, 0.50, 0.75, 1.00),
        target_accel_noise_m_s2=3.0e-9,
        target_rotation_noise_rad_s=None,
        transverse_velocity_m_s=0.0,
        pulse_order=1,
        practical_temperature_floor_k=5.0e-8,
        mission="gravimetrie portable et cartographie souterraine",
    ),
    Scenario(
        name="compact_atomic_gyroscope",
        species="Cs133",
        laser_wavelength_m=852.347e-9,
        central_density_m3=8.0e17,
        initial_atoms=8.0e5,
        initial_radius_m=0.7e-3,
        aperture_radius_m=8.0e-3,
        interrogation_times_s=(0.05, 0.10, 0.20, 0.35, 0.50),
        target_accel_noise_m_s2=None,
        target_rotation_noise_rad_s=1.0e-8,
        transverse_velocity_m_s=1.0,
        pulse_order=1,
        practical_temperature_floor_k=1.0e-7,
        mission="gyroscope atomique compact",
    ),
    Scenario(
        name="space_gravity_gradiometer_source",
        species="Sr88",
        laser_wavelength_m=689.449e-9,
        central_density_m3=2.0e17,
        initial_atoms=1.0e6,
        initial_radius_m=1.5e-3,
        aperture_radius_m=30.0e-3,
        interrogation_times_s=(0.25, 0.50, 1.00, 1.50, 2.00),
        target_accel_noise_m_s2=1.0e-10,
        target_rotation_noise_rad_s=None,
        transverse_velocity_m_s=0.0,
        pulse_order=2,
        practical_temperature_floor_k=1.0e-8,
        mission="source pour gradiometrie gravitationnelle spatiale",
    ),
)


def k_effective(scenario: Scenario) -> float:
    return scenario.pulse_order * 4.0 * math.pi / scenario.laser_wavelength_m


def saturating_ratio(target: float | None, achieved: float) -> float:
    if target is None:
        return 0.0
    if achieved <= 0.0:
        return 1.0
    return max(0.0, min(1.0, target / achieved))


def phase_density_score(eta: float) -> float:
    # eta much below 1e-4 is too dilute for a strong atom source; eta near 1 is excellent.
    if eta <= 0.0:
        return 0.0
    return max(0.0, min(1.0, (math.log10(eta) + 4.0) / 4.0))


def compactness_score(aperture_radius_m: float) -> float:
    # 10 mm radius is excellent, 30 mm is still acceptable for a field package.
    return max(0.0, min(1.0, 0.03 / max(aperture_radius_m, 1.0e-9)))


def cooling_practicality_score(temperature_k: float, practical_floor_k: float) -> float:
    """Penalize unnecessarily extreme cooling below a mission-specific floor."""
    if temperature_k <= 0.0:
        return 0.0
    if temperature_k >= practical_floor_k:
        return 1.0
    return max(0.0, min(1.0, math.sqrt(temperature_k / practical_floor_k)))


def evaluate_row(scenario: Scenario, temperature_k: float, interrogation_s: float) -> dict[str, float | str]:
    species = SPECIES[scenario.species]
    sigma_v = velocity_sigma_1d(species.mass_kg, temperature_k)
    radius = cloud_radius_after_time(
        scenario.initial_radius_m, sigma_v, interrogation_s
    )
    survival = gaussian_cubic_survival_fraction(radius, scenario.aperture_radius_m)
    detected_atoms = scenario.initial_atoms * survival
    eta = degeneracy_parameter(
        scenario.central_density_m3, species.mass_kg, temperature_k
    )
    lam = thermal_wavelength(species.mass_kg, temperature_k)
    k_eff = k_effective(scenario)
    accel_noise = atom_interferometer_acceleration_noise(
        k_eff, interrogation_s, detected_atoms
    )
    rotation_noise = atom_interferometer_rotation_noise(
        k_eff,
        scenario.transverse_velocity_m_s,
        interrogation_s,
        detected_atoms,
    )
    sensitivity_score = max(
        saturating_ratio(scenario.target_accel_noise_m_s2, accel_noise),
        saturating_ratio(scenario.target_rotation_noise_rad_s, rotation_noise),
    )
    utility_score = (
        0.25 * survival
        + 0.30 * sensitivity_score
        + 0.15 * phase_density_score(eta)
        + 0.10 * compactness_score(scenario.aperture_radius_m)
        + 0.20
        * cooling_practicality_score(
            temperature_k, scenario.practical_temperature_floor_k
        )
    )
    return {
        "scenario": scenario.name,
        "mission": scenario.mission,
        "species": scenario.species,
        "temperature_K": temperature_k,
        "interrogation_time_s": interrogation_s,
        "central_density_m3": scenario.central_density_m3,
        "eta_n_lambda3": eta,
        "thermal_wavelength_m": lam,
        "velocity_sigma_m_s": sigma_v,
        "initial_radius_m": scenario.initial_radius_m,
        "cloud_radius_m": radius,
        "aperture_radius_m": scenario.aperture_radius_m,
        "survival_fraction_proxy": survival,
        "initial_atoms": scenario.initial_atoms,
        "detected_atoms_proxy": detected_atoms,
        "k_eff_m_inv": k_eff,
        "accel_noise_m_s2_proxy": accel_noise,
        "rotation_noise_rad_s_proxy": rotation_noise,
        "phase_density_score": phase_density_score(eta),
        "sensitivity_score": sensitivity_score,
        "cooling_practicality_score": cooling_practicality_score(
            temperature_k, scenario.practical_temperature_floor_k
        ),
        "utility_score": utility_score,
    }


def evaluate_design_space() -> list[dict[str, float | str]]:
    temperatures = np.logspace(-9, -5, 81)
    rows: list[dict[str, float | str]] = []
    for scenario in SCENARIOS:
        for interrogation_s in scenario.interrogation_times_s:
            for temperature_k in temperatures:
                rows.append(evaluate_row(scenario, float(temperature_k), interrogation_s))
    return rows


def best_rows(rows: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    output = []
    for scenario in SCENARIOS:
        subset = [row for row in rows if row["scenario"] == scenario.name]
        output.append(max(subset, key=lambda row: float(row["utility_score"])))
    return output


def write_csv(rows: list[dict[str, float | str]]) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    with (DATA / "phase_space_sensor_cad.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(rows: list[dict[str, float | str]]) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    payload = {
        "model_status": "first_order_design_space_proxy",
        "warning": (
            "Not a full sensor simulator: no laser phase noise, vibration rejection, "
            "wavefront aberrations, collisions, dead time, or full Allan variance model."
        ),
        "formulae": [
            "eta = n lambda_th^3",
            "lambda_th = h/sqrt(2*pi*m*kB*T)",
            "sigma_v = sqrt(kB*T/m)",
            "R(t) = sqrt(R0^2 + sigma_v^2 t^2)",
            "delta a = 1/(k_eff*T_i^2*sqrt(N_detected))",
            "delta Omega = 1/(2*k_eff*v*T_i^2*sqrt(N_detected))",
        ],
        "scenarios": [asdict(scenario) for scenario in SCENARIOS],
        "best_rows": best_rows(rows),
    }
    (REPORTS / "phase_space_sensor_cad_summary.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )


def write_report(rows: list[dict[str, float | str]]) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase-space CAD pour capteurs quantiques",
        "",
        "Ce rapport transforme la cellule de phase `D^3 v^3 ~ h^3/m^3` en outil",
        "de conception. L'objectif n'est pas de remplacer un simulateur complet",
        "d'instrument, mais de fournir un budget physique minimal: temperature,",
        "densite, expansion balistique, nombre d'atomes detectes et bruit de tir.",
        "",
        "## Formules utilisees",
        "",
        "```text",
        "eta = n lambda_th^3",
        "lambda_th = h / sqrt(2 pi m k_B T)",
        "sigma_v = sqrt(k_B T / m)",
        "R(t) = sqrt(R0^2 + sigma_v^2 t^2)",
        "delta a ~= 1 / (k_eff T_i^2 sqrt(N_detected))",
        "delta Omega ~= 1 / (2 k_eff v T_i^2 sqrt(N_detected))",
        "```",
        "",
        "## Meilleurs points trouves par scenario",
        "",
        "| scenario | espece | T [K] | Ti [s] | eta | rayon [mm] | survie | N det. | bruit a [m/s2] | bruit Omega [rad/s] | score |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in best_rows(rows):
        lines.append(
            "| {scenario} | {species} | {temperature_K:.2e} | {interrogation_time_s:.2g} | "
            "{eta_n_lambda3:.2e} | {radius_mm:.2f} | {survival_fraction_proxy:.2f} | "
            "{detected_atoms_proxy:.2e} | {accel_noise_m_s2_proxy:.2e} | "
            "{rotation_noise_rad_s_proxy:.2e} | {utility_score:.3f} |".format(
                radius_mm=1.0e3 * float(row["cloud_radius_m"]), **row
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- La variable vraiment industrielle est `sigma_v`: elle fixe la taille de",
            "  l'instrument apres expansion libre.",
            "- `eta` n'est pas seulement un indicateur de degenerate quantique; c'est un",
            "  indicateur de qualite de source atomique a densite et temperature donnees.",
            "- Le meilleur produit n'est pas une propulsion nouvelle. C'est un logiciel",
            "  de pre-dimensionnement pour capteurs inertiels, gravimetres, gyroscopes",
            "  et gradiometres atomiques.",
            "- Un score eleve ne prouve pas qu'un instrument est realisable: il signifie",
            "  seulement que le budget d'espace des phases ne l'interdit pas deja.",
            "",
            "## Limites a ajouter dans une version industrielle",
            "",
            "- bruit laser et bruit de phase optique;",
            "- vibrations et strategie de rejet classique/quantique;",
            "- aberrations de front d'onde;",
            "- collisions froides, pertes et densite maximale exploitable;",
            "- temps mort, cadence, Allan deviation;",
            "- modele complet de detection et bruit technique.",
            "",
            "Donnees: `reports/data/phase_space_sensor_cad.csv`",
            "",
            "Figure: `reports/figures/phase_space_sensor_cad.png`",
        ]
    )
    (REPORTS / "phase_space_sensor_cad_report.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def plot(rows: list[dict[str, float | str]]) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(12.0, 9.0))
    axes_flat = axes.ravel()
    for ax, scenario in zip(axes_flat, SCENARIOS):
        subset = [row for row in rows if row["scenario"] == scenario.name]
        for interrogation_s in scenario.interrogation_times_s:
            sub = [row for row in subset if float(row["interrogation_time_s"]) == interrogation_s]
            temps = [float(row["temperature_K"]) for row in sub]
            scores = [float(row["utility_score"]) for row in sub]
            ax.plot(temps, scores, label=f"{interrogation_s:g} s")
        ax.set_xscale("log")
        ax.set_ylim(0.0, 1.05)
        ax.set_title(scenario.name.replace("_", " "))
        ax.set_xlabel("temperature atomique [K]")
        ax.set_ylabel("score proxy")
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURES / "phase_space_sensor_cad.png", dpi=180)
    plt.close(fig)


def main() -> None:
    rows = evaluate_design_space()
    write_csv(rows)
    write_json(rows)
    write_report(rows)
    plot(rows)
    print(f"wrote phase-space sensor CAD outputs to {REPORTS}")


if __name__ == "__main__":
    main()
