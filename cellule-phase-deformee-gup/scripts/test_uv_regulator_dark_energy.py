#!/usr/bin/env python3
"""Test the GUP UV-regulated vacuum energy against observed dark energy.

Data used:
- CODATA/NIST 2022 constants for c, h, G.
- Planck 2018 baseline LCDM values H0 = 67.4 km/s/Mpc and Omega_m = 0.315,
  with flatness Omega_Lambda = 1 - Omega_m.
"""

from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    mpc = 3.085_677_581_491_3673e22

    H0_km_s_mpc = 67.4
    omega_m = 0.315
    omega_lambda = 1.0 - omega_m

    H0 = H0_km_s_mpc * 1000.0 / mpc
    rho_crit_mass = 3.0 * H0**2 / (8.0 * math.pi * G)
    rho_de_energy = omega_lambda * rho_crit_mass * c**2

    planck_length = math.sqrt(hbar * G / c**3)
    rho_planck_energy = c**7 / (hbar * G**2)

    print("Input data")
    print(f"H0 = {H0_km_s_mpc:.3g} km/s/Mpc")
    print(f"Omega_Lambda = {omega_lambda:.3g}")
    print(f"rho_DE = {rho_de_energy:.6e} J/m^3")
    print(f"rho_P = {rho_planck_energy:.6e} J/m^3")
    print()

    print("Inverting rho_vac = g rho_P / (16 pi^2 beta0^2)")
    for g in (1, 2, 10, 100, 106.75):
        beta0 = math.sqrt(g * rho_planck_energy / (16.0 * math.pi**2 * rho_de_energy))
        ell_min = math.sqrt(beta0) * planck_length
        print(
            f"g={g:6.2f}  beta0={beta0:.6e}  "
            f"sqrt(beta0)*lP={ell_min:.6e} m"
        )

    print()
    print("Reference: beta0=1 prediction")
    for g in (1, 2, 100):
        rho_vac = g * rho_planck_energy / (16.0 * math.pi**2)
        ratio = rho_vac / rho_de_energy
        print(f"g={g:6.2f}  rho_vac={rho_vac:.6e} J/m^3  rho_vac/rho_DE={ratio:.6e}")


if __name__ == "__main__":
    main()
