#!/usr/bin/env python3
"""Checks for the master UV/IR holographic GUP framework."""

from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    mpc = 3.085_677_581_491_3673e22
    H0 = 67.4 * 1000.0 / mpc
    omega_l = 0.685
    alpha_inv = 137.035_999_177
    alpha = 1.0 / alpha_inv

    lP = math.sqrt(hbar * G / c**3)
    tP = lP / c
    rhoP = c**7 / (hbar * G**2)
    rho_c = 3.0 * c**2 * H0**2 / (8.0 * math.pi * G)
    rho_de = omega_l * rho_c
    L_H = c / H0
    Lambda = 3.0 * omega_l * H0**2 / c**2
    R_L = math.sqrt(3.0 / Lambda)

    beta0_de = math.sqrt(1.0 / (6.0 * math.pi * omega_l)) / (H0 * tP)
    ell_eff = math.sqrt(beta0_de) * lP
    rho_ratio_identity = (3.0 * omega_l / (8.0 * math.pi)) * (lP / L_H) ** 2
    rho_bh_LH = 3.0 * c**4 / (8.0 * math.pi * G * L_H**2)
    alpha_inv_pred = math.log(R_L / (10.0 * math.pi * lP))
    Lambda_from_alpha = 3.0 / (100.0 * math.pi**2 * lP**2) * math.exp(
        -2.0 / alpha
    )

    # The "bits of horizon" argument is order-of-magnitude unless the energy
    # per bit is normalized. We report the exact factor for epsilon=hbar*c/L.
    rho_bits = (math.pi * L_H**2 / lP**2) * (hbar * c / L_H) / (
        4.0 * math.pi * L_H**3 / 3.0
    )
    bit_factor = rho_bits / rho_bh_LH

    print("Master equations check")
    print("----------------------")
    print(f"lP                                = {lP:.12e} m")
    print(f"rhoP                              = {rhoP:.12e} J/m^3")
    print(f"rho_c                             = {rho_c:.12e} J/m^3")
    print(f"rho_DE                            = {rho_de:.12e} J/m^3")
    print(f"rho_DE/rhoP                       = {rho_de/rhoP:.12e}")
    print(f"UV/IR identity ratio              = {rho_ratio_identity:.12e}")
    print()
    print(f"beta0_DE(g=1)                     = {beta0_de:.12e}")
    print(f"sqrt(beta0_DE)*lP                 = {ell_eff:.12e} m")
    print()
    print(f"rho_BH(L_H)                       = {rho_bh_LH:.12e} J/m^3")
    print(f"rho_BH(L_H)/rho_c                 = {rho_bh_LH/rho_c:.12f}")
    print(f"bits estimate / BH density        = {bit_factor:.12f}")
    print()
    print(f"R_Lambda                          = {R_L:.12e} m")
    print(f"alpha_inv observed                = {alpha_inv:.12f}")
    print(f"alpha_inv predicted               = {alpha_inv_pred:.12f}")
    print(f"delta alpha_inv                   = {alpha_inv_pred-alpha_inv:.12e}")
    print(f"Lambda(alpha)/Lambda_obs          = {Lambda_from_alpha/Lambda:.12f}")


if __name__ == "__main__":
    main()
