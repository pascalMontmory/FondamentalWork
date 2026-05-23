#!/usr/bin/env python3
"""Numerical check of the UV/IR fine-structure constant conjecture.

The test uses exact SI constants where available, CODATA 2022 for alpha^{-1}
and G, and Planck 2018 base-LambdaCDM central values for H0 and Omega_Lambda.
It is intentionally transparent: no fitting is performed except for reporting
the factor C that would exactly reproduce alpha^{-1}.
"""

from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    mpc = 3.085_677_581_491_3673e22

    # Public reference values.
    alpha_inv_codata_2022 = 137.035_999_177
    H0_km_s_Mpc = 67.4
    omega_lambda = 0.685

    H0 = H0_km_s_Mpc * 1000.0 / mpc
    ell_p = math.sqrt(hbar * G / c**3)
    lambda_obs = 3.0 * omega_lambda * H0**2 / c**2
    r_lambda = math.sqrt(3.0 / lambda_obs)

    alpha_inv_pred = math.log(r_lambda / (10.0 * math.pi * ell_p))
    delta_alpha_inv = alpha_inv_pred - alpha_inv_codata_2022
    rel_delta = delta_alpha_inv / alpha_inv_codata_2022

    alpha_codata = 1.0 / alpha_inv_codata_2022
    lambda_from_alpha = (
        3.0
        / (100.0 * math.pi**2 * ell_p**2)
        * math.exp(-2.0 / alpha_codata)
    )

    c_fit = r_lambda / (ell_p * math.exp(alpha_inv_codata_2022))
    g_eff_fit = c_fit / (4.0 * math.pi)
    s0_fit = math.pi * (r_lambda / ell_p) ** 2 * math.exp(
        -2.0 * alpha_inv_codata_2022
    )
    s0_candidate = 100.0 * math.pi**3

    # Linear propagated uncertainty from Planck H0 and Omega_Lambda only:
    # alpha^{-1}=const-ln(H0)-0.5 ln(Omega_Lambda).
    sigma_h0 = 0.5 / H0_km_s_Mpc
    sigma_omega = 0.0073 / omega_lambda
    sigma_pred_cosmo = math.sqrt(sigma_h0**2 + (0.5 * sigma_omega) ** 2)

    print("UV/IR alpha conjecture numerical check")
    print("--------------------------------------")
    print(f"ell_P                         = {ell_p:.12e} m")
    print(f"H0                            = {H0:.12e} s^-1")
    print(f"Omega_Lambda                  = {omega_lambda:.12f}")
    print(f"Lambda_obs                    = {lambda_obs:.12e} m^-2")
    print(f"R_Lambda                      = {r_lambda:.12e} m")
    print()
    print(f"alpha_inv_CODATA_2022         = {alpha_inv_codata_2022:.12f}")
    print(f"alpha_inv_pred_10pi           = {alpha_inv_pred:.12f}")
    print(f"delta                         = {delta_alpha_inv:.12e}")
    print(f"relative_delta                = {rel_delta:.12e}")
    print(f"cosmology_sigma_approx        = {sigma_pred_cosmo:.12e}")
    print(f"delta_over_cosmology_sigma    = {delta_alpha_inv/sigma_pred_cosmo:.12e}")
    print()
    print(f"Lambda_from_CODATA_alpha      = {lambda_from_alpha:.12e} m^-2")
    print(f"Lambda_from_alpha / Lambda_obs= {lambda_from_alpha/lambda_obs:.12f}")
    print()
    print(f"C_fit in alpha^-1=ln(R/C ellP)= {c_fit:.12f}")
    print(f"10*pi                         = {10.0*math.pi:.12f}")
    print(f"C_fit/(10*pi)                 = {c_fit/(10.0*math.pi):.12f}")
    print(f"g_eff_fit=C_fit/(4*pi)        = {g_eff_fit:.12f}")
    print(f"candidate g_eff               = {2.5:.12f}")
    print()
    print(f"S0_fit/kB                     = {s0_fit:.12f}")
    print(f"100*pi^3                      = {s0_candidate:.12f}")
    print(f"S0_fit/(100*pi^3)             = {s0_fit/s0_candidate:.12f}")


if __name__ == "__main__":
    main()
