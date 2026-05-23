#!/usr/bin/env python3
"""Numerical checks for UV/IR, holographic and GUP relations."""

from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    kB = 1.380_649e-23
    mpc = 3.085_677_581_491_3673e22
    eV = 1.602_176_634e-19

    H0 = 67.4 * 1000.0 / mpc
    omega_lambda = 0.685
    g = 1.0
    beta0 = 1.0

    lP = math.sqrt(hbar * G / c**3)
    tP = lP / c
    EP = math.sqrt(hbar * c**5 / G)
    rhoP = c**7 / (hbar * G**2)
    LH = c / H0
    rho_c = 3.0 * c**2 * H0**2 / (8.0 * math.pi * G)
    rho_de = omega_lambda * rho_c
    rho_uv_ir = (3.0 * omega_lambda / (8.0 * math.pi)) * rhoP * (lP / LH) ** 2
    rho_bh = 3.0 * c**4 / (8.0 * math.pi * G * LH**2)

    EH = hbar * H0
    E_de = (rho_de * (hbar * c) ** 3) ** 0.25
    E_geom = (3.0 * omega_lambda / (8.0 * math.pi)) ** 0.25 * math.sqrt(EP * EH)

    beta0_lambda = math.sqrt(g / (6.0 * math.pi * omega_lambda)) / (H0 * tP)
    ell_lambda = math.sqrt(beta0_lambda) * lP
    E_gup_lambda = hbar * c / ell_lambda
    ratio_energy = E_gup_lambda / E_de

    L_cross = beta0 * math.sqrt(6.0 * math.pi / g) * lP
    weinberg_m = (hbar**2 * H0 / (G * c)) ** (1.0 / 3.0)
    weinberg_E = weinberg_m * c**2

    Lambda = 3.0 * omega_lambda * H0**2 / c**2
    aH = c * H0
    a_ds = c**2 * math.sqrt(Lambda / 3.0)
    a_lambda = c**2 * math.sqrt(Lambda)
    a_mond_like = a_ds / (2.0 * math.pi)

    entropy_hubble_over_kB = math.pi * (LH / lP) ** 2
    volume_cells = (LH / lP) ** 3

    print(f"H0 = {H0:.12e} s^-1")
    print(f"L_H = {LH:.6e} m")
    print(f"rho_c = {rho_c:.6e} J/m^3")
    print(f"rho_DE = {rho_de:.6e} J/m^3")
    print(f"rho_BH(L_H) = {rho_bh:.6e} J/m^3")
    print(f"rho_UVIR identity = {rho_uv_ir:.6e} J/m^3")
    print(f"relative identity error = {(rho_uv_ir/rho_de - 1.0):.3e}")
    print()
    print(f"E_DE = {E_de/eV*1000.0:.6e} meV")
    print(f"E_DE geometric formula = {E_geom/eV*1000.0:.6e} meV")
    print(f"E_GUP fitted to rho_DE = {E_gup_lambda/eV*1000.0:.6e} meV")
    print(f"E_GUP/E_DE = {ratio_energy:.6e}")
    print(f"2*sqrt(pi) = {2.0 * math.sqrt(math.pi):.6e}")
    print()
    print(f"L_cross(beta0=1,g=1) = {L_cross:.6e} m")
    print(f"L_cross/lP = {L_cross/lP:.6e}")
    print(f"beta0_Lambda = {beta0_lambda:.6e}")
    print(f"ell_Lambda = {ell_lambda:.6e} m")
    print()
    print(f"Weinberg mass energy = {weinberg_E/eV/1e6:.6e} MeV")
    print(f"a_H = {aH:.6e} m/s^2")
    print(f"a_dS = c^2 sqrt(Lambda/3) = {a_ds:.6e} m/s^2")
    print(f"a_Lambda = c^2 sqrt(Lambda) = {a_lambda:.6e} m/s^2")
    print(f"a_dS/(2pi) = {a_mond_like:.6e} m/s^2")
    print()
    print(f"S_H/kB = {entropy_hubble_over_kB:.6e}")
    print(f"(L_H/lP)^3 = {volume_cells:.6e}")
    print(f"(S_H/kB)/(volume cells)^(2/3) = {entropy_hubble_over_kB / volume_cells ** (2.0/3.0):.6e}")


if __name__ == "__main__":
    main()
