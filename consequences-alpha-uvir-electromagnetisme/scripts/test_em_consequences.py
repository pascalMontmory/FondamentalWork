#!/usr/bin/env python3
"""Numerical checks for the electromagnetic consequences of alpha=1/L.

The relations in the note are algebraic identities once L=alpha^{-1} is
assumed. This script evaluates the implied atomic and electromagnetic scales
using CODATA 2022 alpha^{-1} and standard SI constants.
"""

from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    e = 1.602_176_634e-19
    m_e = 9.109_383_7139e-31
    alpha_inv = 137.035_999_177
    alpha = 1.0 / alpha_inv

    eps0 = e**2 / (4.0 * math.pi * alpha * hbar * c)
    z0 = 1.0 / (eps0 * c)
    q_planck = math.sqrt(4.0 * math.pi * eps0 * hbar * c)
    m_planck = math.sqrt(hbar * c / G)
    lambda_bar_e = hbar / (m_e * c)

    L = alpha_inv
    e_from_L = q_planck / math.sqrt(L)
    v_e = c / L
    a0 = lambda_bar_e * L
    r_e = lambda_bar_e / L
    rydberg_energy = m_e * c**2 / (2.0 * L**2)
    sigma_thomson = (8.0 * math.pi / 3.0) * r_e**2
    rk = z0 * L / 2.0
    g0 = 4.0 / (z0 * L)
    phi0 = h / (2.0 * q_planck) * math.sqrt(L)
    force_ratio = (m_planck / m_e) ** 2 / L
    m_star = m_planck / math.sqrt(L)
    chi_e_per_beta0 = (m_e / m_planck) ** 2 / L**2
    es_ratio = 1.0 / L**3

    print("Electromagnetic consequences of alpha=1/L")
    print("------------------------------------------")
    print(f"L=alpha_inv                         = {L:.12f}")
    print(f"epsilon_0 from alpha                = {eps0:.12e} F/m")
    print(f"Planck charge q_P                   = {q_planck:.12e} C")
    print(f"e=q_P/sqrt(L)                       = {e_from_L:.12e} C")
    print(f"CODATA elementary charge            = {e:.12e} C")
    print(f"relative e difference               = {(e_from_L/e)-1.0:.12e}")
    print()
    print(f"Bohr velocity c/L                   = {v_e:.12e} m/s")
    print(f"reduced Compton length electron     = {lambda_bar_e:.12e} m")
    print(f"Bohr radius lambda_bar*L            = {a0:.12e} m")
    print(f"classical electron radius           = {r_e:.12e} m")
    print(f"a0*r_e/lambda_bar^2                 = {a0*r_e/lambda_bar_e**2:.12e}")
    print()
    print(f"Rydberg energy                      = {rydberg_energy/e:.12f} eV")
    print(f"Thomson cross section               = {sigma_thomson:.12e} m^2")
    print(f"Schwinger/Bohr field ratio 1/L^3    = {es_ratio:.12e}")
    print()
    print(f"von Klitzing resistance             = {rk:.12f} ohm")
    print(f"conductance quantum                 = {g0:.12e} S")
    print(f"superconducting flux quantum        = {phi0:.12e} Wb")
    print()
    print(f"F_e/F_G between electrons           = {force_ratio:.12e}")
    print(f"m_star=m_P/sqrt(L)                  = {m_star:.12e} kg")
    print(f"chi_e per beta0                     = {chi_e_per_beta0:.12e}")


if __name__ == "__main__":
    main()
