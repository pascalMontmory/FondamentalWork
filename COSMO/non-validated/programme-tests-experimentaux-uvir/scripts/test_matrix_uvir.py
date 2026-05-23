#!/usr/bin/env python3
"""Experimental test matrix for the GUP--UV/IR programme."""

from __future__ import annotations

import math


def constants() -> dict[str, float]:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    kB = 1.380_649e-23
    eV = 1.602_176_634e-19
    mpc = 3.085_677_581_491_3673e22
    H0 = 67.4 * 1000.0 / mpc
    omega_l = 0.685
    omega_m = 1.0 - omega_l
    alpha_inv = 137.035_999_177
    alpha = 1.0 / alpha_inv
    lP = math.sqrt(hbar * G / c**3)
    tP = lP / c
    EP = math.sqrt(hbar * c**5 / G)
    mP = math.sqrt(hbar * c / G)
    me = 9.109_383_7139e-31
    return locals()


def beta0_dark_energy(cst: dict[str, float], g: float = 1.0) -> float:
    return math.sqrt(g / (6.0 * math.pi * cst["omega_l"])) / (
        cst["H0"] * cst["tP"]
    )


def alpha_lambda_test(cst: dict[str, float]) -> dict[str, float]:
    Lambda = 3.0 * cst["omega_l"] * cst["H0"] ** 2 / cst["c"] ** 2
    R = math.sqrt(3.0 / Lambda)
    pred = math.log(R / (10.0 * math.pi * cst["lP"]))
    alpha = cst["alpha"]
    Lambda_alpha = (
        3.0
        / (100.0 * math.pi**2 * cst["lP"] ** 2)
        * math.exp(-2.0 / alpha)
    )
    return {
        "Lambda_obs": Lambda,
        "R_Lambda": R,
        "alpha_inv_pred": pred,
        "delta": pred - cst["alpha_inv"],
        "Lambda_ratio": Lambda_alpha / Lambda,
    }


def hde_w(omega_de: float, c_hde: float) -> float:
    return -1.0 / 3.0 - 2.0 * math.sqrt(omega_de) / (3.0 * c_hde)


def alpha_dot_if_L_hubble(cst: dict[str, float]) -> float:
    # Flat LCDM: dot H/H^2 = -3 Omega_m/2 at z=0.
    dlnL_dt = 1.5 * cst["omega_m"] * cst["H0"]
    return -cst["alpha"] * dlnL_dt


def main() -> None:
    cst = constants()
    b0 = beta0_dark_energy(cst)

    print("GUP--UV/IR experimental test matrix")
    print("-----------------------------------")
    print(f"beta0_DE(g=1)                           = {b0:.6e}")
    print()

    print("1) Universal beta0 tests")
    beta0_firas_bound = 3.716510e58
    beta0_bbn_bound = 2.642965e41
    beta0_ns_bound = 1.656192e38
    chi_atom_per_beta0 = (cst["me"] / cst["mP"]) ** 2 * cst["alpha"] ** 2
    print(f"FIRAS beta0 bound                         ~= {beta0_firas_bound:.6e}")
    print(f"BBN beta0 bound                           ~= {beta0_bbn_bound:.6e}")
    print(f"neutron-star beta0 bound                  ~= {beta0_ns_bound:.6e}")
    print(f"atomic chi_e(beta0_DE)                    ~= {chi_atom_per_beta0*b0:.6e}")
    print("verdict                                   = beta0_DE excluded if universal")
    print()

    print("2) Holographic branch rho=3c^4/(8pi G L^2)")
    rho_c = 3.0 * cst["c"] ** 2 * cst["H0"] ** 2 / (8.0 * math.pi * cst["G"])
    L_H = cst["c"] / cst["H0"]
    rho_bh_LH = 3.0 * cst["c"] ** 4 / (8.0 * math.pi * cst["G"] * L_H**2)
    print(f"rho_c                                     = {rho_c:.6e} J/m^3")
    print(f"rho_BH(L_H)                               = {rho_bh_LH:.6e} J/m^3")
    print(f"rho_BH(L_H)/rho_c                         = {rho_bh_LH/rho_c:.12f}")
    print("verdict                                   = identity; dynamics still open")
    print()

    print("3) Choice of IR length and alpha variation")
    yr = 365.25 * 24.0 * 3600.0
    adot = alpha_dot_if_L_hubble(cst) * yr
    atomic_clock_limit = 1.0e-18
    print(f"predicted alpha_dot/alpha if L=c/H(t)     = {adot:.6e} /yr")
    print(f"representative atomic-clock limit         = {atomic_clock_limit:.6e} /yr")
    print(f"exclusion factor                          = {abs(adot)/atomic_clock_limit:.6e}")
    print("verdict                                   = L=c/H(t) strongly disfavored")
    print()

    print("4) Dynamic dark energy branch")
    w_c1 = hde_w(cst["omega_l"], 1.0)
    w_c08 = hde_w(cst["omega_l"], 0.8)
    print(f"HDE w(c_hde=1)                            = {w_c1:.6f}")
    print(f"HDE w(c_hde=0.8)                          = {w_c08:.6f}")
    print("verdict                                   = testable with BAO/SNe/CMB")
    print()

    print("5) alpha--Lambda relation")
    al = alpha_lambda_test(cst)
    print(f"alpha_inv observed                         = {cst['alpha_inv']:.12f}")
    print(f"alpha_inv predicted                        = {al['alpha_inv_pred']:.12f}")
    print(f"delta                                      = {al['delta']:.6e}")
    print(f"Lambda(alpha)/Lambda_obs                   = {al['Lambda_ratio']:.12f}")
    print("verdict                                    = strong numerical consistency, not proof")
    print()

    print("6) Maxwell edge mode")
    print("target                                     = g_edge^{U(1)} = 1/2")
    print("status                                     = theoretical calculation, not public-data test")


if __name__ == "__main__":
    main()
