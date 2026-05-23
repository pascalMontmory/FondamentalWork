#!/usr/bin/env python3
"""Numerical checks for cosmological GUP--UV/IR conclusions."""

from __future__ import annotations

import math


def main() -> None:
    c_light = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    mpc = 3.085_677_581_491_3673e22
    eV = 1.602_176_634e-19

    H0 = 67.4 * 1000.0 / mpc
    omega_l = 0.685
    L_H = c_light / H0
    ell_p = math.sqrt(hbar * G / c_light**3)
    rho_p = c_light**7 / (hbar * G**2)
    rho_c = 3.0 * c_light**2 * H0**2 / (8.0 * math.pi * G)
    rho_de = omega_l * rho_c
    rho_bh = 3.0 * c_light**4 / (8.0 * math.pi * G * L_H**2)
    rho_reg = rho_p / (16.0 * math.pi**2)

    projection = rho_de / rho_reg
    area_factor = (ell_p / L_H) ** 2
    L_star = math.sqrt(6.0 * math.pi) * ell_p

    E_P = math.sqrt(hbar * c_light**5 / G)
    E_H = hbar * H0
    E_DE = (rho_de * (hbar * c_light) ** 3) ** 0.25

    # Standard flat holographic dark-energy relation for future event horizon.
    # Here c_hde is the dimensionless HDE parameter, not the speed of light.
    for c_hde in (0.8, 1.0, 1.2):
        w0 = -1.0 / 3.0 - 2.0 * math.sqrt(omega_l) / (3.0 * c_hde)
        print(f"HDE w0(c_hde={c_hde:.1f}) = {w0:.6f}")

    print()
    print(f"L_H = {L_H:.6e} m")
    print(f"ell_P/L_H = {ell_p/L_H:.6e}")
    print(f"(ell_P/L_H)^2 = {area_factor:.6e}")
    print(f"rho_P = {rho_p:.6e} J/m^3")
    print(f"rho_reg(beta0=1,g=1) = {rho_reg:.6e} J/m^3")
    print(f"rho_c = {rho_c:.6e} J/m^3")
    print(f"rho_BH(L_H) = {rho_bh:.6e} J/m^3")
    print(f"rho_DE = {rho_de:.6e} J/m^3")
    print(f"rho_DE/rho_reg = {projection:.6e}")
    print(f"projection / area_factor = {projection/area_factor:.6e}")
    print(f"L_star(beta0=1,g=1) = {L_star:.6e} m")
    print(f"L_star/ell_P = {L_star/ell_p:.6e}")
    print(f"E_DE = {E_DE/eV*1000.0:.6e} meV")
    print(f"sqrt(E_P E_H) = {math.sqrt(E_P*E_H)/eV*1000.0:.6e} meV")


if __name__ == "__main__":
    main()
