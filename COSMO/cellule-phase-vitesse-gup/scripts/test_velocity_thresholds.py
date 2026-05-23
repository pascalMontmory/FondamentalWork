#!/usr/bin/env python3
"""Numerical checks for mass-velocity GUP thresholds."""

from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11

    m_planck = math.sqrt(hbar * c / G)
    l_planck = math.sqrt(hbar * G / c**3)

    masses = {
        "electron": 9.109_383_7139e-31,
        "proton": 1.672_621_92595e-27,
        "1 amu": 1.660_539_06892e-27,
        "1 kg": 1.0,
    }

    beta0_values = {
        "Planck beta0=1": 1.0,
        "dark-energy-fit beta0": 2.363_228e60,
    }

    for label, beta0 in beta0_values.items():
        root = math.sqrt(beta0)
        print(label)
        print(f"  sqrt(beta0) lP = {root * l_planck:.6e} m")
        for name, mass in masses.items():
            v_gup = c * m_planck / (mass * root)
            print(f"  {name:8s} v_GUP/c = {v_gup/c:.6e}  v_GUP = {v_gup:.6e} m/s")
        print()


if __name__ == "__main__":
    main()
