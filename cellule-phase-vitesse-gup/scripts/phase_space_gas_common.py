from __future__ import annotations

import math
from dataclasses import dataclass


H = 6.626_070_15e-34
KB = 1.380_649e-23
AMU = 1.660_539_066_60e-27
AVOGADRO = 6.022_140_76e23


@dataclass(frozen=True)
class Species:
    name: str
    mass_kg: float
    statistics: str = "boltzmann"


SPECIES = {
    "H2": Species("H2", 2.015_88 * AMU, "boson"),
    "He4": Species("He4", 4.002_602 * AMU, "boson"),
    "CH4": Species("CH4", 16.042_46 * AMU, "boltzmann"),
    "O2": Species("O2", 31.998_8 * AMU, "boson"),
    "H2O": Species("H2O", 18.015_28 * AMU, "boltzmann"),
    "N2": Species("N2", 28.013_4 * AMU, "boson"),
    "Xe": Species("Xe", 131.293 * AMU, "boson"),
    "Rb87": Species("Rb87", 86.909_180_5 * AMU, "boson"),
    "Cs133": Species("Cs133", 132.905_451_96 * AMU, "boson"),
    "Sr88": Species("Sr88", 87.905_612_5 * AMU, "boson"),
    "Yb174": Species("Yb174", 173.938_866_4 * AMU, "boson"),
}


def thermal_wavelength(mass_kg: float, temperature_k: float) -> float:
    return H / math.sqrt(2.0 * math.pi * mass_kg * KB * temperature_k)


def number_density_ideal(pressure_pa: float, temperature_k: float) -> float:
    return pressure_pa / (KB * temperature_k)


def number_density_from_mass_density(rho_kg_m3: float, mass_kg: float) -> float:
    return rho_kg_m3 / mass_kg


def degeneracy_parameter(n_m3: float, mass_kg: float, temperature_k: float) -> float:
    lam = thermal_wavelength(mass_kg, temperature_k)
    return n_m3 * lam**3


def mean_spacing(n_m3: float) -> float:
    return n_m3 ** (-1.0 / 3.0)


def phase_cell_ratio(n_m3: float, mass_kg: float, temperature_k: float) -> float:
    """Approximate D^3 p_th^3 / h^3 using p_th=sqrt(2*pi*m*kT)."""
    eta = degeneracy_parameter(n_m3, mass_kg, temperature_k)
    if eta <= 0.0:
        return math.inf
    return 1.0 / eta


def velocity_sigma_1d(mass_kg: float, temperature_k: float) -> float:
    """One-dimensional thermal velocity dispersion sqrt(kT/m)."""
    return math.sqrt(KB * temperature_k / mass_kg)


def cloud_radius_after_time(
    initial_radius_m: float, sigma_v_m_s: float, interrogation_s: float
) -> float:
    """Ballistic Gaussian radius proxy after free expansion."""
    return math.sqrt(initial_radius_m**2 + (sigma_v_m_s * interrogation_s) ** 2)


def gaussian_cubic_survival_fraction(radius_m: float, aperture_radius_m: float) -> float:
    """Conservative separable 3D acceptance proxy for a finite aperture."""
    if radius_m <= 0.0 or aperture_radius_m <= 0.0:
        return 0.0
    one_dim = math.erf(aperture_radius_m / (math.sqrt(2.0) * radius_m))
    return max(0.0, min(1.0, one_dim**3))


def atom_interferometer_acceleration_noise(
    k_eff_m_inv: float, interrogation_s: float, detected_atoms: float
) -> float:
    """Shot-noise acceleration floor proxy 1/(k_eff T^2 sqrt(N))."""
    if k_eff_m_inv <= 0.0 or interrogation_s <= 0.0 or detected_atoms <= 0.0:
        return math.inf
    return 1.0 / (k_eff_m_inv * interrogation_s**2 * math.sqrt(detected_atoms))


def atom_interferometer_rotation_noise(
    k_eff_m_inv: float,
    transverse_velocity_m_s: float,
    interrogation_s: float,
    detected_atoms: float,
) -> float:
    """Sagnac-like rotation floor proxy 1/(2 k_eff v T^2 sqrt(N))."""
    if (
        k_eff_m_inv <= 0.0
        or transverse_velocity_m_s <= 0.0
        or interrogation_s <= 0.0
        or detected_atoms <= 0.0
    ):
        return math.inf
    return 1.0 / (
        2.0
        * k_eff_m_inv
        * transverse_velocity_m_s
        * interrogation_s**2
        * math.sqrt(detected_atoms)
    )


def quantum_virial_correction_magnitude(eta: float) -> float:
    return eta / (2.0 ** 2.5)


def quantum_threshold_pressure(mass_kg: float, temperature_k: float, eta: float = 1.0) -> float:
    """Ideal-gas pressure where n lambda_th^3 reaches eta."""
    lam = thermal_wavelength(mass_kg, temperature_k)
    n = eta / lam**3
    return n * KB * temperature_k


def quantum_threshold_temperature(mass_kg: float, n_m3: float, eta: float = 1.0) -> float:
    """Temperature where n lambda_th^3 reaches eta at fixed number density."""
    factor = H**2 / (2.0 * math.pi * mass_kg * KB)
    return factor * (n_m3 / eta) ** (2.0 / 3.0)


def ideal_quantum_pressure_factor(eta: float, statistics: str) -> float:
    """Leading ideal quantum virial correction P/(n kT)."""
    if statistics == "boson":
        return 1.0 - quantum_virial_correction_magnitude(eta)
    if statistics == "fermion":
        return 1.0 + quantum_virial_correction_magnitude(eta)
    return 1.0


def gup_theta(beta0: float, mass_kg: float, temperature_k: float) -> float:
    """theta_T = beta m kT with beta=beta0*lP^2/hbar^2."""
    c = 299_792_458.0
    hbar = H / (2.0 * math.pi)
    G = 6.674_30e-11
    l_planck = math.sqrt(hbar * G / c**3)
    beta = beta0 * l_planck**2 / hbar**2
    return beta * mass_kg * KB * temperature_k


def gup_partition_factor_low_theta(theta_t: float) -> float:
    """Z1/Z10 = 1 - 9 theta + 90 theta^2 + O(theta^3)."""
    return 1.0 - 9.0 * theta_t + 90.0 * theta_t**2


def gup_energy_per_particle_factor_low_theta(theta_t: float) -> float:
    """(U/N)/(3 kT/2) from the audited expansion through theta^2."""
    return 1.0 - 6.0 * theta_t + 66.0 * theta_t**2


def isentropic_static_state(
    p0_pa: float, t0_k: float, mach: float, gamma: float
) -> tuple[float, float]:
    ratio = 1.0 + 0.5 * (gamma - 1.0) * mach**2
    t = t0_k / ratio
    p = p0_pa * (t / t0_k) ** (gamma / (gamma - 1.0))
    return p, t


def classify_eta(eta: float) -> str:
    if eta < 1.0e-6:
        return "classical_extreme"
    if eta < 1.0e-3:
        return "classical"
    if eta < 0.1:
        return "quantum_correction_watch"
    if eta < 1.0:
        return "partly_degenerate"
    return "degenerate_quantum"
