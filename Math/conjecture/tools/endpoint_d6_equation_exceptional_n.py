#!/usr/bin/env python3
"""Exceptional-n extraction for endpoint d-6 equation-level eliminants.

The modular equation probe proves that the three remaining endpoint d-6
weight types have no generic component over Q(n).  This script performs the
next step: eliminate a from the equation-level eliminants and collect the
finite set of n-specializations where a common a-root can survive.

For a weight type, the compact equations are

    F(a,Y) = 0,
    R_k(a,Y) = prod_{X in {0,a,Y,z}} H_k(X) = 0,  k=3,4,5,6,

with each R_k reduced modulo F.  In the three remaining types these reduced
products are linear in Y.  Using R_3 as the base, a solution must satisfy one
quadratic-linear resultant and three 2x2 common-root determinants in a.  A
common a-root then forces every pairwise resultant in a to vanish.  The gcd of
those pairwise resultants gives a univariate necessary obstruction in n.

This is an extraction tool: any positive integer n not vanishing on the
reported factor set is excluded.  The final proof still has to certify that
the reported factors have no admissible positive integer roots, or handle those
roots directly if any occur.
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_equation_elimination import (
    determinant_expr,
    reduced_cover_products,
    resultant_linear_with_quadratic_expr,
)


DEFAULT_TYPES = [(1, 1, 3, 1), (1, 2, 2, 1), (2, 1, 2, 1)]
TRIVIAL_N_FACTORS = {0, -1, -2, -3, -4, -5, -6}


def parse_weights() -> list[tuple[int, int, int, int]]:
    if len(sys.argv) == 1:
        return DEFAULT_TYPES
    return [tuple(int(part) for part in arg.split(",")) for arg in sys.argv[1:]]


def primitive_poly(expr: sp.Expr, var: sp.Symbol) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    poly = sp.Poly(numerator, var)
    _, primitive = poly.primitive()
    return sp.Poly(primitive, var)


def saturated_n_poly(poly: sp.Poly, n: sp.Symbol) -> sp.Poly:
    expr = poly.as_expr()
    for root in TRIVIAL_N_FACTORS:
        factor = n - root
        while sp.rem(sp.Poly(expr, n), sp.Poly(factor, n)).is_zero:
            expr = sp.cancel(expr / factor)
    return primitive_poly(expr, n)


def has_root_mod(poly: sp.Poly, prime: int) -> bool:
    coeffs = [int(c % prime) for c in poly.all_coeffs()]
    for residue in range(prime):
        value = 0
        for coeff in coeffs:
            value = (value * residue + coeff) % prime
        if value == 0:
            return True
    return False


def small_prime_certificate(poly: sp.Poly) -> int | None:
    for prime in [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        if not has_root_mod(poly, prime):
            return prime
    return None


def build_eliminants(
    weights: tuple[int, int, int, int],
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
) -> list[sp.Poly]:
    f, products = reduced_cover_products(weights, n, a, y, x)
    base = products[3]
    exprs = [
        resultant_linear_with_quadratic_expr(f, base, y),
        determinant_expr(base, products[4], y),
        determinant_expr(base, products[5], y),
        determinant_expr(base, products[6], y),
    ]
    return [primitive_poly(expr, a) for expr in exprs]


def pairwise_resultant(poly_a: sp.Poly, poly_b: sp.Poly, n: sp.Symbol, a: sp.Symbol) -> sp.Poly:
    if poly_a.degree() == 0 or poly_b.degree() == 0:
        return sp.Poly(1, n)
    resultant = sp.resultant(poly_a.as_expr(), poly_b.as_expr(), a)
    return saturated_n_poly(primitive_poly(resultant, n), n)


def factor_summary(poly: sp.Poly, n: sp.Symbol) -> list[str]:
    if poly.degree() == 0:
        return ["1"]

    summary = []
    for factor, exponent in sp.factor_list(poly.as_expr())[1]:
        factor_poly = sp.Poly(factor, n)
        degree = factor_poly.degree()
        if degree == 1:
            coeffs = factor_poly.all_coeffs()
            root = sp.Rational(-coeffs[1], coeffs[0])
            label = f"linear root {root}"
        else:
            prime = small_prime_certificate(factor_poly)
            if prime is None:
                label = f"degree {degree}, no small-prime certificate"
            else:
                label = f"degree {degree}, no roots mod {prime}"
        if exponent != 1:
            label += f"^{exponent}"
        summary.append(label)
    return summary


def certify_weights(weights: tuple[int, int, int, int]) -> None:
    n, a, y, x = sp.symbols("n a y x")
    print(f"weights {weights}", flush=True)
    eliminants = build_eliminants(weights, n, a, y, x)
    print(
        "  eliminant degrees in a: "
        + ", ".join(str(poly.degree()) for poly in eliminants),
        flush=True,
    )

    resultants = []
    for i, left in enumerate(eliminants):
        for right in eliminants[i + 1 :]:
            resultant = pairwise_resultant(left, right, n, a)
            resultants.append(resultant)
            print(f"  pair resultant degree in n: {resultant.degree()}", flush=True)

    gcd = resultants[0]
    for resultant in resultants[1:]:
        gcd = sp.gcd(gcd, resultant)
    gcd = saturated_n_poly(gcd, n)

    print(f"  saturated exceptional gcd degree in n: {gcd.degree()}", flush=True)
    for line in factor_summary(gcd, n):
        print(f"    {line}", flush=True)


def main() -> None:
    for weights in parse_weights():
        certify_weights(weights)


if __name__ == "__main__":
    main()
