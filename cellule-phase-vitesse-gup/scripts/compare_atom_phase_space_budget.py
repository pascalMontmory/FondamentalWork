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
    cloud_radius_after_time,
    gaussian_cubic_survival_fraction,
    gup_beta_p2_from_velocity,
    recoil_temperature,
    thermal_wavelength,
    velocity_sigma_1d,
)


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
DATA = REPORTS / "data"
FIGURES = REPORTS / "figures"


@dataclass(frozen=True)
class AtomOption:
    species: str
    cooling_wavelength_m: float
    cooling_access: str
    practical_temperature_floor_k: float
    notes: str


ATOM_OPTIONS = (
    AtomOption("Rb87", 780.241e-9, "excellent", 1.0e-7, "mature alkali platform"),
    AtomOption("Cs133", 852.347e-9, "excellent", 1.0e-7, "clock and inertial heritage"),
    AtomOption("Sr88", 689.449e-9, "good", 1.0e-8, "narrow-line cooling, clocks"),
    AtomOption("Yb174", 556.000e-9, "good", 1.0e-8, "narrow-line cooling, clocks"),
    AtomOption("Li6", 670.977e-9, "specialized", 3.0e-7, "light fermion, larger recoil"),
    AtomOption("Li7", 670.977e-9, "specialized", 3.0e-7, "light boson, larger recoil"),
)


def effective_volume(radius_m: float, aperture_radius_m: float) -> float:
    return 4.0 * math.pi * min(radius_m, aperture_radius_m) ** 3 / 3.0


def phase_space_atom_cap(eta_max: float, volume_m3: float, lambda_th_m: float) -> float:
    if lambda_th_m <= 0.0:
        return math.inf
    return eta_max * volume_m3 / lambda_th_m**3


def k_effective(wavelength_m: float, pulse_order: int = 1) -> float:
    return pulse_order * 4.0 * math.pi / wavelength_m


def evaluate_atom_budget(
    atom: AtomOption,
    temperature_k: float,
    interrogation_s: float,
    eta_max: float,
    initial_atoms_cap: float,
    initial_radius_m: float,
    aperture_radius_m: float,
    beta0_for_gup_bound: float,
) -> dict[str, float | str]:
    species = SPECIES[atom.species]
    sigma_v = velocity_sigma_1d(species.mass_kg, temperature_k)
    radius = cloud_radius_after_time(initial_radius_m, sigma_v, interrogation_s)
    survival = gaussian_cubic_survival_fraction(radius, aperture_radius_m)
    lambda_th = thermal_wavelength(species.mass_kg, temperature_k)
    volume = effective_volume(radius, aperture_radius_m)
    n_phase_cap = phase_space_atom_cap(eta_max, volume, lambda_th)
    n_detected = min(initial_atoms_cap * survival, n_phase_cap)
    fom = math.sqrt(max(n_detected, 0.0)) * interrogation_s**2
    k_eff = k_effective(atom.cooling_wavelength_m)
    recoil_k = recoil_temperature(species.mass_kg, atom.cooling_wavelength_m)
    accel_noise = atom_interferometer_acceleration_noise(k_eff, interrogation_s, n_detected)
    gup_planck = gup_beta_p2_from_velocity(1.0, species.mass_kg, sigma_v)
    gup_bound = gup_beta_p2_from_velocity(beta0_for_gup_bound, species.mass_kg, sigma_v)
    return {
        "species": atom.species,
        "statistics": species.statistics,
        "cooling_wavelength_m": atom.cooling_wavelength_m,
        "cooling_access": atom.cooling_access,
        "notes": atom.notes,
        "temperature_K": temperature_k,
        "practical_temperature_floor_K": atom.practical_temperature_floor_k,
        "interrogation_time_s": interrogation_s,
        "recoil_temperature_K": recoil_k,
        "thermal_wavelength_m": lambda_th,
        "velocity_sigma_m_s": sigma_v,
        "cloud_radius_m": radius,
        "aperture_radius_m": aperture_radius_m,
        "survival_fraction_proxy": survival,
        "effective_volume_m3": volume,
        "eta_max": eta_max,
        "phase_space_atom_cap": n_phase_cap,
        "technical_atom_cap": initial_atoms_cap,
        "detected_atoms_budget": n_detected,
        "sensitivity_fom_s2_sqrt_atoms": fom,
        "accel_noise_m_s2_proxy": accel_noise,
        "gup_beta_p2_beta0_1": gup_planck,
        "gup_beta_p2_beta0_bound": gup_bound,
        "beta0_bound_used": beta0_for_gup_bound,
    }


def evaluate_grid() -> list[dict[str, float | str]]:
    interrogation_times = (0.05, 0.10, 0.25, 0.50, 1.00)
    rows: list[dict[str, float | str]] = []
    for atom in ATOM_OPTIONS:
        temperatures = np.logspace(
            math.log10(atom.practical_temperature_floor_k), -5, 61
        )
        for temp in temperatures:
            for ti in interrogation_times:
                rows.append(
                    evaluate_atom_budget(
                        atom=atom,
                        temperature_k=float(temp),
                        interrogation_s=ti,
                        eta_max=0.3,
                        initial_atoms_cap=1.0e7,
                        initial_radius_m=1.0e-3,
                        aperture_radius_m=12.0e-3,
                        beta0_for_gup_bound=1.0e26,
                    )
                )
    return rows


def best_rows(rows: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    best = []
    for atom in ATOM_OPTIONS:
        subset = [row for row in rows if row["species"] == atom.species]
        best.append(max(subset, key=lambda row: float(row["sensitivity_fom_s2_sqrt_atoms"])))
    return sorted(best, key=lambda row: float(row["sensitivity_fom_s2_sqrt_atoms"]), reverse=True)


def write_outputs(rows: list[dict[str, float | str]]) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    with (DATA / "atom_phase_space_budget.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "model_status": "first_order_budget_constraint",
        "assumptions": {
            "eta_max": 0.3,
            "technical_atom_cap": 1.0e7,
            "initial_radius_m": 1.0e-3,
            "aperture_radius_m": 12.0e-3,
            "fom": "sqrt(N_detected_budget) * T_i^2",
            "phase_space_atom_cap": "eta_max * V_eff / lambda_th^3",
            "gup_bound_beta0": 1.0e26,
        },
        "atoms": [asdict(atom) for atom in ATOM_OPTIONS],
        "best_rows": best_rows(rows),
    }
    (REPORTS / "atom_phase_space_budget_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    report_lines = [
        "# Atom comparison: phase-space budget",
        "",
        "This report adds an explicit sensitivity figure of merit with a",
        "phase-space atom-number cap:",
        "",
        "```text",
        "N_phase_cap = eta_max V_eff / lambda_th^3",
        "N_detected = min(N_technical survival, N_phase_cap)",
        "FOM = sqrt(N_detected) T_i^2",
        "delta a ~= 1 / (k_eff FOM)",
        "```",
        "",
        "The GUP correction is also quantified through",
        "`epsilon_GUP = beta0 (m sigma_v / p_Pl)^2`.",
        "",
        "| atom | access | T [K] | Ti [s] | recoil T [K] | sigma_v [m/s] | N budget | FOM | delta a [m/s2] | beta p2 beta0=1 | beta p2 beta0=1e26 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in best_rows(rows):
        report_lines.append(
            "| {species} | {cooling_access} | {temperature_K:.2e} | {interrogation_time_s:.2g} | "
            "{recoil_temperature_K:.2e} | {velocity_sigma_m_s:.2e} | "
            "{detected_atoms_budget:.2e} | {sensitivity_fom_s2_sqrt_atoms:.2e} | "
            "{accel_noise_m_s2_proxy:.2e} | {gup_beta_p2_beta0_1:.2e} | "
            "{gup_beta_p2_beta0_bound:.2e} |".format(**row)
        )
    report_lines.extend(
        [
            "",
            "Interpretation:",
            "",
            "- heavier atoms have smaller velocity dispersion at fixed temperature;",
            "- Sr/Yb benefit from narrow-line cooling but require more complex optics;",
            "- Li has larger recoil and larger velocity spread, so it is less natural",
            "  for compact inertial sensors despite specialized advantages;",
            "- even the deliberately loose `beta0=1e26` GUP column is far below",
            "  direct relevance for cold-atom sensor design.",
            "",
            "Data: `reports/data/atom_phase_space_budget.csv`",
            "",
            "Figure: `reports/figures/atom_phase_space_budget.png`",
        ]
    )
    (REPORTS / "atom_phase_space_budget_report.md").write_text(
        "\n".join(report_lines), encoding="utf-8"
    )


def plot(rows: list[dict[str, float | str]]) -> None:
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    for atom in ATOM_OPTIONS:
        subset = [
            row
            for row in rows
            if row["species"] == atom.species and float(row["interrogation_time_s"]) == 0.5
        ]
        temps = [float(row["temperature_K"]) for row in subset]
        fom = [float(row["sensitivity_fom_s2_sqrt_atoms"]) for row in subset]
        ax.plot(temps, fom, label=atom.species)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("atom temperature [K]")
    ax.set_ylabel(r"$\sqrt{N_{\rm budget}}T_i^2$ at $T_i=0.5$ s")
    ax.set_title("Phase-space constrained sensitivity figure of merit")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "atom_phase_space_budget.png", dpi=180)
    plt.close(fig)


def main() -> None:
    rows = evaluate_grid()
    write_outputs(rows)
    plot(rows)
    print(f"wrote atom phase-space budget outputs to {REPORTS}")


if __name__ == "__main__":
    main()
