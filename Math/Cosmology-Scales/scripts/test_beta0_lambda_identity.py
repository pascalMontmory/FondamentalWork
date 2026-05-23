#!/usr/bin/env python3
"""Check the beta_0^(Lambda) closed-form identity.

This script verifies that

    beta0 = sqrt(g / (6*pi*Omega_Lambda)) / (H0*tP)

equals the direct inversion

    beta0 = sqrt(g*rho_P / (16*pi^2*rho_Lambda))

under the definitions used in the COSMO notes.
"""
from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    hbar = 1.054_571_817e-34
    G = 6.674_30e-11
    mpc = 3.085_677_581_491_3673e22

    H0_km_s_mpc = 67.4
    H0 = H0_km_s_mpc * 1000.0 / mpc
    omega_lambda = 0.685
    g = 1.0

    t_planck = math.sqrt(hbar * G / c**5)
    ell_planck = math.sqrt(hbar * G / c**3)
    rho_planck = c**7 / (hbar * G**2)
    rho_lambda = omega_lambda * 3.0 * H0**2 * c**2 / (8.0 * math.pi * G)

    beta_direct = math.sqrt(g * rho_planck / (16.0 * math.pi**2 * rho_lambda))
    beta_closed = math.sqrt(g / (6.0 * math.pi * omega_lambda)) / (H0 * t_planck)
    ell_lambda = math.sqrt(beta_closed) * ell_planck
    ell_closed = (g / (6.0 * math.pi * omega_lambda)) ** 0.25 * math.sqrt(ell_planck * c / H0)

    rel = abs(beta_direct - beta_closed) / beta_direct
    ell_rel = abs(ell_lambda - ell_closed) / ell_lambda

    print(f"H0 = {H0:.17e} s^-1")
    print(f"t_P = {t_planck:.17e} s")
    print(f"rho_Lambda = {rho_lambda:.17e} J/m^3")
    print(f"rho_P = {rho_planck:.17e} J/m^3")
    print(f"beta0_direct = {beta_direct:.17e}")
    print(f"beta0_closed = {beta_closed:.17e}")
    print(f"relative_error = {rel:.17e}")
    print(f"ell_Lambda = {ell_lambda:.17e} m")
    print(f"ell_relative_error = {ell_rel:.17e}")

    assert rel < 1e-12
    assert ell_rel < 1e-12


if __name__ == "__main__":
    main()
