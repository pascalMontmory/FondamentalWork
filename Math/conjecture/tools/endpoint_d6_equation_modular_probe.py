#!/usr/bin/env python3
"""Specialized modular probe for endpoint d-6 equation-level elimination.

The direct equation-level script builds four large eliminants in Q(n)[a] and
then asks SymPy for their gcd.  This probe fixes n modulo a prime before
building the products.  A single non-bad specialization with gcd 1 in F_p[a]
rules out a positive-degree generic gcd over Q(n)[a].
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_cover_degrees import h_polynomials


ORDERS = [3, 4, 5, 6]
COVERS = ["0", "a", "Y", "z"]
DEFAULT_TYPES = [(1, 1, 3, 1), (1, 2, 2, 1), (2, 1, 2, 1)]
PRIMES = [11, 13, 17, 19, 23, 29, 31]


def parse_weights() -> list[tuple[int, int, int, int]]:
    if len(sys.argv) == 1:
        return DEFAULT_TYPES
    return [tuple(int(part) for part in arg.split(",")) for arg in sys.argv[1:]]


def format_degrees(degrees: list[sp.Integer | int]) -> str:
    return (
        "["
        + ", ".join("zero" if degree == -sp.oo else str(degree) for degree in degrees)
        + "]"
    )


def reduce_mod_f_mod(
    expr: sp.Expr,
    f: sp.Poly,
    y: sp.Symbol,
    domain: sp.Domain,
) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    reduced = sp.Poly(numerator, y, domain=domain).rem(f)
    reduced_numerator = sp.together(reduced.as_expr()).as_numer_denom()[0]
    return sp.Poly(reduced_numerator, y, domain=domain)


def reduced_cover_products_mod(
    weights: tuple[int, int, int, int],
    n_value: int,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
    prime: int,
) -> tuple[sp.Poly, dict[int, sp.Poly]]:
    domain = sp.GF(prime).frac_field(a)
    f_expr, h_by_order, cover_exprs = h_polynomials(n_value, a, y, x, *weights)
    f = sp.Poly(f_expr.as_expr(), y, domain=domain)
    products = {}

    for order in ORDERS:
        product = sp.Poly(1, y, domain=domain)
        for cover_name in COVERS:
            condition = reduce_mod_f_mod(
                h_by_order[order].subs(x, cover_exprs[cover_name]),
                f,
                y,
                domain,
            )
            product = reduce_mod_f_mod(
                product.as_expr() * condition.as_expr(),
                f,
                y,
                domain,
            )
        products[order] = product

    return f, products


def line_quadratic_resultant_expr(f: sp.Poly, linear: sp.Poly, y: sp.Symbol) -> sp.Expr:
    f_y2 = f.coeff_monomial(y**2)
    f_y1 = f.coeff_monomial(y)
    f_y0 = f.coeff_monomial(1)
    coeff_y = linear.coeff_monomial(y)
    coeff_0 = linear.coeff_monomial(1)
    return f_y2 * coeff_0**2 - f_y1 * coeff_y * coeff_0 + f_y0 * coeff_y**2


def determinant_expr(left: sp.Poly, right: sp.Poly, y: sp.Symbol) -> sp.Expr:
    return (
        left.coeff_monomial(y) * right.coeff_monomial(1)
        - right.coeff_monomial(y) * left.coeff_monomial(1)
    )


def specialized_gcd_degree(
    weights: tuple[int, int, int, int],
    n_value: int,
    prime: int,
) -> tuple[int, list[int]]:
    a, y, x = sp.symbols("a y x")
    f, products = reduced_cover_products_mod(weights, n_value, a, y, x, prime)
    base = products[3]
    eliminant_exprs = [
        line_quadratic_resultant_expr(f, base, y),
        determinant_expr(base, products[4], y),
        determinant_expr(base, products[5], y),
        determinant_expr(base, products[6], y),
    ]
    eliminants = [
        sp.Poly(sp.together(expr).as_numer_denom()[0], a, modulus=prime)
        for expr in eliminant_exprs
    ]
    nonzero_eliminants = [poly for poly in eliminants if not poly.is_zero]
    if not nonzero_eliminants:
        return -1, [poly.degree() for poly in eliminants]

    gcd = nonzero_eliminants[0]
    for eliminant in nonzero_eliminants[1:]:
        gcd = sp.gcd(gcd, eliminant)
        if gcd.degree() == 0:
            break
    return gcd.degree(), [poly.degree() for poly in eliminants]


def main() -> None:
    for weights in parse_weights():
        print(f"weights {weights}", flush=True)
        certified = False
        for prime in PRIMES:
            bad_n = {(-offset) % prime for offset in range(1, 7)}
            degrees_by_n = []
            for n_value in range(prime):
                if n_value in bad_n:
                    continue
                gcd_degree, eliminant_degrees = specialized_gcd_degree(weights, n_value, prime)
                degrees_by_n.append((n_value, gcd_degree))
                if gcd_degree == 0:
                    print(
                        f"  generic gcd 1 certified by p={prime}, n={n_value}; "
                        f"eliminant degrees={format_degrees(eliminant_degrees)}",
                        flush=True,
                    )
                    certified = True
                    break
            if certified:
                break
            print(f"  p={prime}: gcd degrees by good n {degrees_by_n}", flush=True)
        if not certified:
            print("  no generic gcd-1 specialization found", flush=True)


if __name__ == "__main__":
    main()
