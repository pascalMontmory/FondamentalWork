#!/usr/bin/env python3
"""Analytic and numerical GUP dark-energy constraint."""

from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    mpc = 3.085_677_581_491_3673e22
    eV = 1.602_176_634e-19

    H0 = 67.4 * 1000.0 / mpc
    omega_lambda = 0.685

    lP = math.sqrt(hbar * G / c**3)
    tP = lP / c
    EP = math.sqrt(hbar * c**5 / G)
    rhoP = c**7 / (hbar * G**2)
    rhoL = omega_lambda * 3.0 * H0**2 * c**2 / (8.0 * math.pi * G)

    print(f"H0 tP = {H0 * tP:.6e}")
    print(f"rho_Lambda = {rhoL:.6e} J/m^3")
    print(f"rho_P = {rhoP:.6e} J/m^3")
    print(f"sqrt(lP c/H0) = {math.sqrt(lP * c / H0):.6e} m")
    print()

    for g in (1.0, 2.0, 100.0, 106.75):
        beta0 = math.sqrt(g / (6.0 * math.pi * omega_lambda)) / (H0 * tP)
        ell = math.sqrt(beta0) * lP
        e_cut = hbar * c / ell
        nmax = g / (32.0 * math.pi * beta0**1.5 * lP**3)
        spacing = nmax ** (-1.0 / 3.0)
        print(f"g = {g:g}")
        print(f"  beta0_Lambda = {beta0:.6e}")
        print(f"  ell_Lambda = {ell:.6e} m")
        print(f"  E_GUP = {e_cut/eV*1000:.6e} meV")
        print(f"  m_* = E_GUP/c^2 = {e_cut/eV:.6e} eV/c^2")
        print(f"  nmax = {nmax:.6e} m^-3")
        print(f"  nmax^(-1/3) = {spacing:.6e} m")
        print()


if __name__ == "__main__":
    main()
