#!/usr/bin/env python3
"""Check geometric degeneracies on regular endpoint d-6 t-fibers.

For every regular local fiber, this script extracts the common a-root, then
tests every Y in the residue field against the full reduced system
F=R3=R4=R5=R6.  For every lift it computes z and tests collisions among
0,a,Y,z.  It also reports hidden denominator failures encountered while
evaluating the reduced equations.
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_equation_modular_probe import DEFAULT_TYPES, reduced_cover_products_mod
from endpoint_d6_regular_t_root_lift import (
    DEFAULT_CLASS,
    common_gcd,
    linear_root,
    regular_fibers,
    specialized_eliminants,
)


DEFAULT_PRIMES = [101, 103, 107]


def parse_args() -> tuple[list[tuple[int, int, int, int]], tuple[int, int], list[int], int | None]:
    args = sys.argv[1:]
    cls = DEFAULT_CLASS
    primes = DEFAULT_PRIMES
    max_t = None
    for arg in list(args):
        if arg.startswith("--class="):
            residue, modulus = arg.removeprefix("--class=").split(",")
            cls = (int(residue), int(modulus))
            args.remove(arg)
        elif arg.startswith("--primes="):
            primes = [int(part) for part in arg.removeprefix("--primes=").split(",")]
            args.remove(arg)
        elif arg.startswith("--max-t="):
            max_t = int(arg.removeprefix("--max-t="))
            args.remove(arg)

    weights_list = DEFAULT_TYPES if not args else [
        tuple(int(part) for part in arg.split(",")) for arg in args
    ]
    return weights_list, cls, primes, max_t


def eval_a_expr(expr: sp.Expr, a: sp.Symbol, a_value: int, prime: int) -> tuple[int | None, bool]:
    numerator, denominator = sp.together(expr).as_numer_denom()
    num_poly = sp.Poly(numerator, a, modulus=prime)
    den_poly = sp.Poly(denominator, a, modulus=prime)
    den_value = int(den_poly.eval(a_value)) % prime
    if den_value == 0:
        return None, True
    num_value = int(num_poly.eval(a_value)) % prime
    return (num_value * pow(den_value, -1, prime)) % prime, False


def eval_y_poly_at_a(
    poly: sp.Poly,
    a: sp.Symbol,
    y: sp.Symbol,
    a_value: int,
    y_value: int,
    prime: int,
) -> tuple[int | None, bool]:
    total = 0
    for (degree,), coeff in poly.terms():
        coeff_value, bad_denominator = eval_a_expr(coeff, a, a_value, prime)
        if bad_denominator:
            return None, True
        total = (total + coeff_value * pow(y_value, degree, prime)) % prime
    return total, False


def z_value(
    weights: tuple[int, int, int, int],
    n_value: int,
    a_value: int,
    y_value: int,
    prime: int,
) -> tuple[int | None, list[str]]:
    _, ma, my, mz = weights
    if mz % prime == 0:
        return None, ["z_denominator"]
    return ((n_value - ma * a_value - my * y_value) * pow(mz, -1, prime)) % prime, []


def equation_residuals_from_products(
    f: sp.Poly,
    products: dict[int, sp.Poly],
    weights: tuple[int, int, int, int],
    a: sp.Symbol,
    y: sp.Symbol,
    a_value: int,
    y_value: int,
    prime: int,
) -> tuple[dict[str, int | None], list[str]]:
    residuals = {}
    issues = []
    f_value, bad = eval_y_poly_at_a(f, a, y, a_value, y_value, prime)
    residuals["F"] = f_value
    if bad:
        issues.append("F_denominator")
    for order in [3, 4, 5, 6]:
        value, bad = eval_y_poly_at_a(products[order], a, y, a_value, y_value, prime)
        residuals[f"R{order}"] = value
        if bad:
            issues.append(f"R{order}_denominator")
    return residuals, issues


def y_candidates(
    weights: tuple[int, int, int, int],
    n_value: int,
    a_value: int,
    prime: int,
) -> tuple[list[tuple[int, dict[str, int | None]]], list[str]]:
    a, y, x = sp.symbols("a y x")
    f, products = reduced_cover_products_mod(weights, n_value, a, y, x, prime)
    candidates = []
    issues = []
    for y_value in range(prime):
        residuals, residual_issues = equation_residuals_from_products(
            f,
            products,
            weights,
            a,
            y,
            a_value,
            y_value,
            prime,
        )
        if residual_issues:
            issues.extend(residual_issues)
            continue
        if all(value == 0 for value in residuals.values()):
            candidates.append((y_value, residuals))
    return candidates, sorted(set(issues))


def geometry_for_fiber(
    weights: tuple[int, int, int, int],
    n_value: int,
    a_value: int,
    prime: int,
) -> list[tuple[int | None, int | None, dict[str, bool], dict[str, int | None], list[str]]]:
    candidates, issues = y_candidates(weights, n_value, a_value, prime)
    if not candidates:
        return [
            (
                None,
                None,
                {
                    "a_zero": a_value == 0,
                    "Y_zero": False,
                    "Y_eq_a": False,
                    "z_zero": False,
                    "z_eq_a": False,
                    "z_eq_Y": False,
                    "equations_ok": False,
                    "hidden_denominator_bad": bool(issues),
                    "no_Y_solution": True,
                },
                {},
                issues,
            )
        ]

    geometries = []
    for y_value, residuals in candidates:
        local_issues = []
        z, z_issues = z_value(weights, n_value, a_value, y_value, prime)
        local_issues.extend(z_issues)
        flags = {
            "a_zero": a_value == 0,
            "Y_zero": y_value == 0,
            "Y_eq_a": y_value == a_value,
            "z_zero": z == 0,
            "z_eq_a": z == a_value,
            "z_eq_Y": z == y_value,
            "equations_ok": all(value == 0 for value in residuals.values()),
            "hidden_denominator_bad": bool(local_issues),
            "no_Y_solution": False,
        }
        geometries.append((y_value, z, flags, residuals, local_issues))
    return geometries


def report_prime(
    weights: tuple[int, int, int, int],
    cls: int,
    modulus: int,
    prime: int,
    max_t: int | None,
) -> None:
    expected, regular = regular_fibers(weights, cls, modulus, prime, max_t)
    print(f"  p={prime}: expected_degrees={expected}, regular_count={len(regular)}", flush=True)
    killed = []
    survivors = []
    for fiber in regular:
        eliminants = specialized_eliminants(weights, fiber.n_value, prime)
        gcd = common_gcd(eliminants)
        a_root = linear_root(gcd, prime)
        if a_root is None:
            print(
                f"    t={fiber.t_value}, n={fiber.n_value}: gcd_degree={gcd.degree()}, "
                "nonlinear gcd; skipped",
                flush=True,
            )
            continue
        geometries = geometry_for_fiber(
            weights,
            fiber.n_value,
            a_root,
            prime,
        )
        live_geometries = []
        killed_geometries = []
        for y_root, z_root, flags, residuals, issues in geometries:
            collision_flags = {
                key: value
                for key, value in flags.items()
                if key not in {"equations_ok", "hidden_denominator_bad"} and value
            }
            killed_here = (
                bool(collision_flags)
                or flags.get("hidden_denominator_bad", False)
                or bool(issues)
            )
            if killed_here:
                killed_geometries.append((y_root, z_root, collision_flags, issues))
            else:
                live_geometries.append((y_root, z_root))
            print(
                f"    t={fiber.t_value}, n={fiber.n_value}, a={a_root}, "
                f"Y={y_root}, z={z_root}, flags={flags}, "
                f"collisions={collision_flags}, residuals={residuals}, issues={issues}",
                flush=True,
            )
        if live_geometries:
            survivors.append(fiber.t_value)
        else:
            killed.append(fiber.t_value)
    print(f"    geometry killed t={killed}", flush=True)
    print(f"    geometry survivors t={survivors}", flush=True)


def main() -> None:
    weights_list, (cls, modulus), primes, max_t = parse_args()
    for weights in weights_list:
        print(f"weights {weights}, class n={cls}+{modulus}*t", flush=True)
        for prime in primes:
            report_prime(weights, cls, modulus, prime, max_t)


if __name__ == "__main__":
    main()
