#!/usr/bin/env python3
"""Compute endpoint d-6 exceptional factors modulo coefficient primes.

This is the modular version of endpoint_d6_equation_exceptional_n.py.  It
keeps n symbolic, works over F_p, eliminates Y via the compact linear
equations, then eliminates a by pairwise resultants.  The output is the
saturated gcd in F_p[n].

If this gcd is 1 for a good coefficient prime, the pairwise-resultant
necessary exceptional factor has no nontrivial reduction modulo that prime.
If it is nonconstant, its degree and residue roots guide reconstruction or
direct treatment of the exceptional n-fibers.
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_cover_degrees import h_polynomials
from endpoint_d6_equation_modular_probe import (
    COVERS,
    DEFAULT_TYPES,
    ORDERS,
    determinant_expr,
    line_quadratic_resultant_expr,
)


DEFAULT_COEFF_PRIMES = [11, 13, 17]
TRIVIAL_OFFSETS = range(0, 7)


def parse_args() -> tuple[list[tuple[int, int, int, int]], list[int]]:
    args = sys.argv[1:]
    primes = DEFAULT_COEFF_PRIMES
    for arg in list(args):
        if arg.startswith("--coeff-primes="):
            primes = [int(part) for part in arg.removeprefix("--coeff-primes=").split(",")]
            args.remove(arg)
    if not args:
        return DEFAULT_TYPES, primes
    return [tuple(int(part) for part in arg.split(",")) for arg in args], primes


def reduce_mod_f(
    expr: sp.Expr,
    f: sp.Poly,
    y: sp.Symbol,
    domain: sp.Domain,
) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    reduced = sp.Poly(numerator, y, domain=domain).rem(f)
    reduced_numerator = sp.together(reduced.as_expr()).as_numer_denom()[0]
    return sp.Poly(reduced_numerator, y, domain=domain)


def reduced_cover_products(
    weights: tuple[int, int, int, int],
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
    prime: int,
) -> tuple[sp.Poly, dict[int, sp.Poly]]:
    domain = sp.GF(prime).frac_field(n, a)
    f_expr, h_by_order, cover_exprs = h_polynomials(n, a, y, x, *weights)
    f = sp.Poly(f_expr.as_expr(), y, domain=domain)
    products = {}

    for order in ORDERS:
        product = sp.Poly(1, y, domain=domain)
        for cover_name in COVERS:
            condition = reduce_mod_f(
                h_by_order[order].subs(x, cover_exprs[cover_name]),
                f,
                y,
                domain,
            )
            product = reduce_mod_f(
                product.as_expr() * condition.as_expr(),
                f,
                y,
                domain,
            )
        products[order] = product

    return f, products


def poly_in_a(expr: sp.Expr, n: sp.Symbol, a: sp.Symbol, prime: int) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    coeff_domain = sp.GF(prime).poly_ring(n)
    return sp.Poly(numerator, a, domain=coeff_domain)


def poly_in_n(expr: sp.Expr, n: sp.Symbol, prime: int) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    return sp.Poly(numerator, n, modulus=prime)


def saturated(poly: sp.Poly, n: sp.Symbol, prime: int) -> sp.Poly:
    result = poly
    for offset in TRIVIAL_OFFSETS:
        factor = sp.Poly(n + offset, n, modulus=prime)
        while result.degree() > 0 and result.rem(factor).is_zero:
            result = result.exquo(factor)
    return sp.Poly(result.as_expr(), n, modulus=prime)


def residue_roots(poly: sp.Poly, prime: int) -> list[int]:
    return [residue for residue in range(prime) if poly.eval(residue) % prime == 0]


def exceptional_factor_modp(
    weights: tuple[int, int, int, int],
    prime: int,
) -> tuple[sp.Poly, list[int], list[int]]:
    n, a, y, x = sp.symbols("n a y x")
    f, products = reduced_cover_products(weights, n, a, y, x, prime)
    base = products[3]
    eliminant_exprs = [
        line_quadratic_resultant_expr(f, base, y),
        determinant_expr(base, products[4], y),
        determinant_expr(base, products[5], y),
        determinant_expr(base, products[6], y),
    ]
    eliminants = [poly_in_a(expr, n, a, prime) for expr in eliminant_exprs]

    resultants = []
    for index, left in enumerate(eliminants):
        for right in eliminants[index + 1 :]:
            if left.is_zero or right.is_zero or left.degree() == 0 or right.degree() == 0:
                continue
            resultant = sp.resultant(left.as_expr(), right.as_expr(), a)
            resultants.append(saturated(poly_in_n(resultant, n, prime), n, prime))

    if not resultants:
        return sp.Poly(0, n, modulus=prime), [poly.degree() for poly in eliminants], []

    gcd = resultants[0]
    for resultant in resultants[1:]:
        gcd = sp.gcd(gcd, resultant)
        if gcd.degree() == 0:
            break
    gcd = saturated(gcd, n, prime)
    return gcd, [poly.degree() for poly in eliminants], [poly.degree() for poly in resultants]


def main() -> None:
    weights_list, primes = parse_args()
    for weights in weights_list:
        print(f"weights {weights}", flush=True)
        for prime in primes:
            gcd, eliminant_degrees, resultant_degrees = exceptional_factor_modp(weights, prime)
            print(
                f"  p={prime}: eliminant degrees in a={eliminant_degrees}; "
                f"pair resultant degrees in n={resultant_degrees}; "
                f"saturated gcd degree={gcd.degree()}; roots={residue_roots(gcd, prime)}",
                flush=True,
            )
            print(f"    factor mod {prime}: {sp.factor(gcd.as_expr(), modulus=prime)}", flush=True)


if __name__ == "__main__":
    main()
