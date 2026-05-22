#!/usr/bin/env python3
"""Public-data consistency tests for the GUP--UV/IR framework.

The script deliberately avoids a heavy cosmological MCMC. It tests direct
consequences against public observational constraints:

* COBE/FIRAS blackbody-shape precision.
* Planck+BAO+SNe constant-w dark-energy constraint.
* SPARC/MOND acceleration scale.
* BBN/CMB radiation-density tolerance.
* Neutron-star Fermi-momentum scale.
"""

from __future__ import annotations

import math


def planck_constants() -> dict[str, float]:
    c = 299_792_458.0
    h = 6.626_070_15e-34
    hbar = h / (2.0 * math.pi)
    G = 6.674_30e-11
    kB = 1.380_649e-23
    eV = 1.602_176_634e-19
    mpc = 3.085_677_581_491_3673e22
    H0 = 67.4 * 1000.0 / mpc
    omega_l = 0.685
    lP = math.sqrt(hbar * G / c**3)
    tP = lP / c
    EP = math.sqrt(hbar * c**5 / G)
    rhoP = c**7 / (hbar * G**2)
    rhoL = omega_l * 3.0 * H0**2 * c**2 / (8.0 * math.pi * G)
    return {
        "c": c,
        "h": h,
        "hbar": hbar,
        "G": G,
        "kB": kB,
        "eV": eV,
        "H0": H0,
        "omega_l": omega_l,
        "lP": lP,
        "tP": tP,
        "EP": EP,
        "rhoP": rhoP,
        "rhoL": rhoL,
    }


def beta0_lambda(constants: dict[str, float], g: float = 1.0) -> float:
    return math.sqrt(g / (6.0 * math.pi * constants["omega_l"])) / (
        constants["H0"] * constants["tP"]
    )


def blackbody_shape(x: float) -> float:
    return x**3 / math.expm1(x)


def gup_blackbody_shape(x: float, theta: float) -> float:
    """Dimensionless spectral shape with theta = beta0 (kT/EP)^2."""
    return blackbody_shape(x) / (1.0 + theta * x * x) ** 3


def rms_residual_for_theta(theta: float, x_min: float, x_max: float) -> float:
    """Fit the closest temperature-rescaled blackbody and return RMS/peak.

    A small temperature shift is allowed because FIRAS measures the blackbody
    temperature very precisely; this makes the exclusion conservative.
    """

    xs = [x_min + (x_max - x_min) * i / 399.0 for i in range(400)]
    target = [gup_blackbody_shape(x, theta) for x in xs]
    peak = max(target)

    def loss(alpha: float) -> float:
        # alpha = T_fit / T_true, and B(nu,T_fit) at fixed nu scales as
        # x_fit=nu/T_fit=x/alpha, with intensity proportional to alpha^3.
        model = [alpha**3 * blackbody_shape(x / alpha) for x in xs]
        amp = sum(t * m for t, m in zip(target, model)) / sum(m * m for m in model)
        return sum((t - amp * m) ** 2 for t, m in zip(target, model)) / len(xs)

    lo, hi = 0.8, 1.2
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c1 = hi - gr * (hi - lo)
    c2 = lo + gr * (hi - lo)
    f1 = loss(c1)
    f2 = loss(c2)
    for _ in range(90):
        if f1 > f2:
            lo = c1
            c1 = c2
            f1 = f2
            c2 = lo + gr * (hi - lo)
            f2 = loss(c2)
        else:
            hi = c2
            c2 = c1
            f2 = f1
            c1 = hi - gr * (hi - lo)
            f1 = loss(c1)
    return math.sqrt(min(f1, f2)) / peak


def firas_test(constants: dict[str, float], beta0_de: float) -> dict[str, float]:
    T0 = 2.7255
    kT = constants["kB"] * T0
    theta_de = beta0_de * (kT / constants["EP"]) ** 2
    x_min = constants["h"] * constants["c"] * 100.0 * 2.0 / kT
    x_max = constants["h"] * constants["c"] * 100.0 * 20.0 / kT
    rms_de = rms_residual_for_theta(theta_de, x_min, x_max)
    firas_limit = 5.0e-5

    lo, hi = 0.0, beta0_de
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        theta_mid = mid * (kT / constants["EP"]) ** 2
        if rms_residual_for_theta(theta_mid, x_min, x_max) < firas_limit:
            lo = mid
        else:
            hi = mid
    return {
        "theta_de": theta_de,
        "rms_de": rms_de,
        "firas_limit": firas_limit,
        "beta0_bound": lo,
        "exclusion_factor": beta0_de / lo if lo > 0 else math.inf,
    }


def hde_test(omega_de: float) -> dict[str, float]:
    w_obs = -1.03
    sigma = 0.03

    def w_hde(c_hde: float) -> float:
        return -1.0 / 3.0 - 2.0 * math.sqrt(omega_de) / (3.0 * c_hde)

    c_best = -2.0 * math.sqrt(omega_de) / (3.0 * (w_obs + 1.0 / 3.0))
    return {
        "w_c08": w_hde(0.8),
        "w_c10": w_hde(1.0),
        "w_c12": w_hde(1.2),
        "sigma_c10": abs(w_hde(1.0) - w_obs) / sigma,
        "c_best_for_wobs": c_best,
    }


def sparc_acceleration_test(constants: dict[str, float]) -> dict[str, float]:
    omega_l = constants["omega_l"]
    H0 = constants["H0"]
    c = constants["c"]
    Lambda = 3.0 * omega_l * H0**2 / c**2
    a_ds = c**2 * math.sqrt(Lambda / 3.0)
    a_lambda = c**2 * math.sqrt(Lambda)
    a0_sparc = 1.2e-10
    return {
        "a_ds": a_ds,
        "a_ds_over_2pi": a_ds / (2.0 * math.pi),
        "a_lambda_over_2pi": a_lambda / (2.0 * math.pi),
        "a0_sparc": a0_sparc,
        "ratio_ds": (a_ds / (2.0 * math.pi)) / a0_sparc,
        "ratio_lambda": (a_lambda / (2.0 * math.pi)) / a0_sparc,
    }


def bbn_neff_test(constants: dict[str, float], beta0_de: float) -> dict[str, float]:
    coeff = 40.0 * math.pi**2 / 7.0
    T_bbn_energy = 1.0e6 * constants["eV"]
    frac_de = coeff * beta0_de * (T_bbn_energy / constants["EP"]) ** 2
    bound = 0.1 / (coeff * (T_bbn_energy / constants["EP"]) ** 2)
    return {
        "frac_at_beta0_de": frac_de,
        "beta0_bound_10_percent": bound,
        "exclusion_factor": beta0_de / bound,
    }


def neutron_star_test(constants: dict[str, float], beta0_de: float) -> dict[str, float]:
    pfc = 300.0e6 * constants["eV"]
    chi_de = beta0_de * (pfc / constants["EP"]) ** 2
    bound_10_percent = 0.1 * (constants["EP"] / pfc) ** 2
    return {
        "pfc_MeV": 300.0,
        "chi_at_beta0_de": chi_de,
        "beta0_bound_10_percent": bound_10_percent,
        "exclusion_factor": beta0_de / bound_10_percent,
    }


def verdict(label: str, excluded: bool) -> str:
    return f"{label}: {'EXCLU si beta0 universel' if excluded else 'compatible comme ordre de grandeur'}"


def main() -> None:
    cst = planck_constants()
    b0 = beta0_lambda(cst, g=1.0)
    e_gup = cst["EP"] / math.sqrt(b0)

    print("=== Parametre ajuste directement a l'energie noire ===")
    print(f"beta0_DE(g=1) = {b0:.6e}")
    print(f"E_GUP = {e_gup/cst['eV']*1000.0:.6e} meV")
    print()

    print("=== Test 1: COBE/FIRAS, spectre CMB ===")
    firas = firas_test(cst, b0)
    print(f"theta_CMB(beta0_DE) = {firas['theta_de']:.6e}")
    print(f"RMS distortion / peak = {firas['rms_de']:.6e}")
    print(f"FIRAS public limit used = {firas['firas_limit']:.6e}")
    print(f"beta0 bound from FIRAS shape ~= {firas['beta0_bound']:.6e}")
    print(f"exclusion factor = {firas['exclusion_factor']:.6e}")
    print(verdict("FIRAS", firas["rms_de"] > firas["firas_limit"]))
    print()

    print("=== Test 2: equation d'etat holographique w ===")
    hde = hde_test(cst["omega_l"])
    print(f"w_HDE(c_hde=0.8) = {hde['w_c08']:.6f}")
    print(f"w_HDE(c_hde=1.0) = {hde['w_c10']:.6f}")
    print(f"w_HDE(c_hde=1.2) = {hde['w_c12']:.6f}")
    print(f"c_hde matching w=-1.03 ~= {hde['c_best_for_wobs']:.6f}")
    print(f"c_hde=1 tension vs w=-1.03+-0.03 ~= {hde['sigma_c10']:.2f} sigma")
    print("Conclusion: testable; c_hde=1 is disfavored by constant-w constraints.")
    print()

    print("=== Test 3: SPARC/RAR acceleration scale ===")
    sparc = sparc_acceleration_test(cst)
    print(f"a_dS/(2pi) = {sparc['a_ds_over_2pi']:.6e} m/s^2")
    print(f"c^2 sqrt(Lambda)/(2pi) = {sparc['a_lambda_over_2pi']:.6e} m/s^2")
    print(f"SPARC/MOND a0 reference = {sparc['a0_sparc']:.6e} m/s^2")
    print(f"ratio a_dS/(2pi)/a0 = {sparc['ratio_ds']:.6f}")
    print(f"ratio a_Lambda/(2pi)/a0 = {sparc['ratio_lambda']:.6f}")
    print(verdict("SPARC scale", False))
    print()

    print("=== Test 4: BBN / radiation density ===")
    bbn = bbn_neff_test(cst, b0)
    print(f"|delta rho/rho| at T~1 MeV for beta0_DE = {bbn['frac_at_beta0_de']:.6e}")
    print(f"beta0 bound for <10% radiation correction ~= {bbn['beta0_bound_10_percent']:.6e}")
    print(f"exclusion factor = {bbn['exclusion_factor']:.6e}")
    print(verdict("BBN", bbn["frac_at_beta0_de"] > 0.1))
    print()

    print("=== Test 5: neutron-star dense fermions ===")
    ns = neutron_star_test(cst, b0)
    print(f"representative p_F c = {ns['pfc_MeV']:.1f} MeV")
    print(f"chi=beta p_F^2 at beta0_DE = {ns['chi_at_beta0_de']:.6e}")
    print(f"beta0 bound for chi<0.1 ~= {ns['beta0_bound_10_percent']:.6e}")
    print(f"exclusion factor = {ns['exclusion_factor']:.6e}")
    print(verdict("Neutron stars", ns["chi_at_beta0_de"] > 0.1))
    print()

    print("=== Synthese ===")
    print("A universal beta0 adjusted to dark energy fails FIRAS, BBN and neutron-star tests.")
    print("The viable reading is sector-dependent or holographic: UV regularization plus IR projection.")


if __name__ == "__main__":
    main()
