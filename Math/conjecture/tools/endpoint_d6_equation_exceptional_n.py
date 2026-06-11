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
    resultant_linear_with_quadratic_expr,
)
from endpoint_d6_cover_degrees import h_polynomials


DEFAULT_TYPES = [(1, 1, 3, 1), (1, 2, 2, 1), (2, 1, 2, 1)]
TRIVIAL_N_FACTORS = {0, -1, -2, -3, -4, -5, -6}
ORDERS = [3, 4, 5, 6]
COVERS = ["0", "a", "Y", "z"]


def parse_args() -> tuple[list[tuple[int, int, int, int]], bool, bool, int | None]:
    args = sys.argv[1:]
    build_only = "--build-only" in args
    raw_eliminants = "--raw-eliminants" in args
    args = [arg for arg in args if arg != "--build-only"]
    args = [arg for arg in args if arg != "--raw-eliminants"]
    max_resultants = None
    for arg in list(args):
        if arg.startswith("--max-resultants="):
            max_resultants = int(arg.removeprefix("--max-resultants="))
            args.remove(arg)
    if not args:
        return DEFAULT_TYPES, build_only, raw_eliminants, max_resultants
    return (
        [tuple(int(part) for part in arg.split(",")) for arg in args],
        build_only,
        raw_eliminants,
        max_resultants,
    )


def primitive_poly(expr: sp.Expr, var: sp.Symbol) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    poly = sp.Poly(numerator, var)
    _, primitive = poly.primitive()
    return sp.Poly(primitive, var)


def primitive_linear(expr: sp.Expr, y: sp.Symbol) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    poly = sp.Poly(numerator, y)
    _, primitive = poly.primitive()
    return sp.Poly(primitive, y)


LinearPair = tuple[sp.Expr, sp.Expr]


def reduce_quadratic_fast(expr: sp.Expr, f: sp.Poly, y: sp.Symbol) -> LinearPair:
    """Reduce expr modulo a quadratic f in y using a linear recurrence."""

    numerator = sp.together(expr).as_numer_denom()[0]
    poly = sp.Poly(numerator, y)
    a2 = f.coeff_monomial(y**2)
    a1 = f.coeff_monomial(y)
    a0 = f.coeff_monomial(1)

    powers: list[tuple[sp.Expr, sp.Expr]] = [(sp.Integer(0), sp.Integer(1))]
    if poly.degree() >= 1:
        powers.append((sp.Integer(1), sp.Integer(0)))
    for _ in range(2, max(poly.degree(), 1) + 1):
        prev_y, prev_0 = powers[-1]
        # y*(prev_y*y + prev_0), with y^2 = -(a1*y+a0)/a2.
        powers.append((prev_0 - prev_y * a1 / a2, -prev_y * a0 / a2))

    coeff_y = sp.Integer(0)
    coeff_0 = sp.Integer(0)
    for (power,), coeff in poly.terms():
        rem_y, rem_0 = powers[power]
        coeff_y += coeff * rem_y
        coeff_0 += coeff * rem_0

    return coeff_y, coeff_0


def multiply_linear_mod(left: LinearPair, right: LinearPair, f: sp.Poly, y: sp.Symbol) -> LinearPair:
    a2 = f.coeff_monomial(y**2)
    a1 = f.coeff_monomial(y)
    a0 = f.coeff_monomial(1)
    left_y, left_0 = left
    right_y, right_0 = right

    quadratic_coeff = left_y * right_y
    coeff_y = left_y * right_0 + left_0 * right_y - quadratic_coeff * a1 / a2
    coeff_0 = left_0 * right_0 - quadratic_coeff * a0 / a2
    return coeff_y, coeff_0


def reduced_cover_products_fast(
    weights: tuple[int, int, int, int],
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
) -> tuple[sp.Poly, dict[int, sp.Poly]]:
    f, h_by_order, cover_exprs = h_polynomials(n, a, y, x, *weights)
    products = {}
    for order in ORDERS:
        print(f"    building R{order}", flush=True)
        product = (sp.Integer(0), sp.Integer(1))
        for cover_name in COVERS:
            condition = reduce_quadratic_fast(
                h_by_order[order].subs(x, cover_exprs[cover_name]),
                f,
                y,
            )
            product = multiply_linear_mod(product, condition, f, y)
        products[order] = primitive_linear(product[0] * y + product[1], y)
        print(f"    built R{order}: degree_a={sp.Poly(products[order].as_expr(), a).degree()}", flush=True)
    return f, products


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
    normalize: bool,
) -> list[sp.Poly]:
    f, products = reduced_cover_products_fast(weights, n, a, y, x)
    base = products[3]
    exprs = [
        resultant_linear_with_quadratic_expr(f, base, y),
        determinant_expr(base, products[4], y),
        determinant_expr(base, products[5], y),
        determinant_expr(base, products[6], y),
    ]
    eliminants = []
    for index, expr in enumerate(exprs, start=1):
        print(f"  forming E{index}", flush=True)
        if normalize:
            eliminant = primitive_poly(expr, a)
        else:
            eliminant = sp.Poly(sp.together(expr).as_numer_denom()[0], a)
        print(f"  formed E{index}: degree_a={eliminant.degree()}", flush=True)
        eliminants.append(eliminant)
    return eliminants


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


def certify_weights(
    weights: tuple[int, int, int, int],
    build_only: bool,
    raw_eliminants: bool,
    max_resultants: int | None,
) -> None:
    n, a, y, x = sp.symbols("n a y x")
    print(f"weights {weights}", flush=True)
    eliminants = build_eliminants(
        weights,
        n,
        a,
        y,
        x,
        normalize=not build_only and not raw_eliminants,
    )
    print(
        "  eliminant degrees in a: "
        + ", ".join(str(poly.degree()) for poly in eliminants),
        flush=True,
    )
    if build_only:
        return

    resultants = []
    for i, left in enumerate(eliminants):
        for j, right in enumerate(eliminants[i + 1 :], start=i + 1):
            if max_resultants is not None and len(resultants) >= max_resultants:
                return
            print(f"  computing resultant E{i + 1},E{j + 1}", flush=True)
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
    weights_list, build_only, raw_eliminants, max_resultants = parse_args()
    for weights in weights_list:
        certify_weights(weights, build_only, raw_eliminants, max_resultants)


if __name__ == "__main__":
    main()
