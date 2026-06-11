#!/usr/bin/env python3
"""Equation-level elimination for endpoint multiplicity d-6.

Instead of enumerating the 4^4 choices of covers for Q3,Q4,Q5,Q6, this script
uses the compact equations

    prod_{X in {0,a,Y,z}} H_k(X) = 0,  k=3,4,5,6.

Each product is reduced modulo the weighted quadratic F_m immediately, so it
has degree at most one in Y.  A common solution must make one reduced product
share a Y-root with F_m and make the four reduced products share the same
Y-root.  This gives one quadratic-linear resultant and three 2x2 determinants
in a over Q(n).
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_cover_degrees import h_polynomials, reduced_condition


ORDERS = [3, 4, 5, 6]
COVERS = ["0", "a", "Y", "z"]
DEFAULT_TYPES = [(1, 1, 3, 1), (1, 2, 2, 1), (2, 1, 2, 1)]
GENERIC_PRIMES = [1000003, 1000033, 1000037]


def parse_args() -> tuple[list[tuple[int, int, int, int]], bool]:
    args = sys.argv[1:]
    exact = "--exact" in args
    args = [arg for arg in args if arg != "--exact"]
    if not args:
        return DEFAULT_TYPES, exact
    return [tuple(int(part) for part in arg.split(",")) for arg in args], exact


def primitive_expr(expr: sp.Expr, *variables: sp.Symbol) -> sp.Expr:
    numerator = sp.together(expr).as_numer_denom()[0]
    _, primitive = sp.Poly(numerator, *variables).primitive()
    return primitive.as_expr()


def reduce_mod_f(expr: sp.Expr, f: sp.Poly, y: sp.Symbol) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    reduced = sp.Poly(numerator, y).rem(f)
    _, primitive = reduced.primitive()
    return sp.Poly(primitive, y)


def reduced_cover_products(
    weights: tuple[int, int, int, int],
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
) -> tuple[sp.Poly, dict[int, sp.Poly]]:
    f, h_by_order, cover_exprs = h_polynomials(n, a, y, x, *weights)
    products = {}

    for order in ORDERS:
        product = sp.Poly(1, y)
        for cover_name in COVERS:
            condition = reduced_condition(
                h_by_order[order].subs(x, cover_exprs[cover_name]),
                f,
                y,
            )
            product = reduce_mod_f(product.as_expr() * condition.as_expr(), f, y)
        products[order] = product

    return f, products


def resultant_linear_with_quadratic(
    f: sp.Poly,
    linear: sp.Poly,
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    field: sp.Domain,
) -> sp.Poly:
    f_y2 = f.coeff_monomial(y**2)
    f_y1 = f.coeff_monomial(y)
    f_y0 = f.coeff_monomial(1)
    coeff_y = linear.coeff_monomial(y)
    coeff_0 = linear.coeff_monomial(1)
    resultant = f_y2 * coeff_0**2 - f_y1 * coeff_y * coeff_0 + f_y0 * coeff_y**2
    return sp.Poly(primitive_expr(resultant, n, a), a, domain=field)


def resultant_linear_with_quadratic_expr(
    f: sp.Poly,
    linear: sp.Poly,
    y: sp.Symbol,
) -> sp.Expr:
    f_y2 = f.coeff_monomial(y**2)
    f_y1 = f.coeff_monomial(y)
    f_y0 = f.coeff_monomial(1)
    coeff_y = linear.coeff_monomial(y)
    coeff_0 = linear.coeff_monomial(1)
    return f_y2 * coeff_0**2 - f_y1 * coeff_y * coeff_0 + f_y0 * coeff_y**2


def determinant(
    left: sp.Poly,
    right: sp.Poly,
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    field: sp.Domain,
) -> sp.Poly:
    expr = left.coeff_monomial(y) * right.coeff_monomial(1)
    expr -= right.coeff_monomial(y) * left.coeff_monomial(1)
    return sp.Poly(primitive_expr(expr, n, a), a, domain=field)


def determinant_expr(left: sp.Poly, right: sp.Poly, y: sp.Symbol) -> sp.Expr:
    expr = left.coeff_monomial(y) * right.coeff_monomial(1)
    expr -= right.coeff_monomial(y) * left.coeff_monomial(1)
    return expr


def has_root_mod(poly: sp.Poly, prime: int) -> bool:
    for residue in range(prime):
        if poly.eval(residue) % prime == 0:
            return True
    return False


def classify_gcd(gcd: sp.Poly, n: sp.Symbol) -> str:
    if gcd.degree() == 0:
        return "gcd 1"

    pieces = []
    for factor, _ in sp.factor_list(gcd.as_expr())[1]:
        factor_poly = sp.Poly(factor, n)
        if factor_poly.degree() == 1:
            coeffs = factor_poly.all_coeffs()
            pieces.append(f"linear root {sp.Rational(-coeffs[1], coeffs[0])}")
            continue
        for prime in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
            if not has_root_mod(factor_poly, prime):
                pieces.append(f"degree {factor_poly.degree()} no roots mod {prime}")
                break
        else:
            pieces.append(f"degree {factor_poly.degree()} no small-prime certificate")
    return "; ".join(pieces)


def modular_gcd_degrees(
    eliminants: list[sp.Expr],
    n: sp.Symbol,
    a: sp.Symbol,
) -> list[tuple[int, int]]:
    degrees = []
    for prime in GENERIC_PRIMES:
        field = sp.GF(prime).frac_field(n)
        gcd = sp.Poly(eliminants[0], a, domain=field)
        for eliminant in eliminants[1:]:
            poly = sp.Poly(eliminant, a, domain=field)
            gcd = sp.gcd(gcd, poly)
            if gcd.degree() == 0:
                break
        degrees.append((prime, gcd.degree()))
    return degrees


def main() -> None:
    n, a, y, x = sp.symbols("n a y x")
    field = sp.QQ.frac_field(n)
    weights_list, exact = parse_args()

    for weights in weights_list:
        f, products = reduced_cover_products(weights, n, a, y, x)
        print(f"weights {weights}", flush=True)
        for order in ORDERS:
            poly = products[order]
            print(
                f"  R{order}: degree_y={poly.degree()}, degree_a={sp.Poly(poly.as_expr(), a).degree()}",
                flush=True,
            )

        base = products[3]
        eliminant_exprs = [
            resultant_linear_with_quadratic_expr(f, base, y),
            determinant_expr(base, products[4], y),
            determinant_expr(base, products[5], y),
            determinant_expr(base, products[6], y),
        ]
        print(
            "  eliminant degrees in a: "
            + ", ".join(str(sp.Poly(expr, a).degree()) for expr in eliminant_exprs),
            flush=True,
        )
        print(
            f"  modular gcd degrees: {modular_gcd_degrees(eliminant_exprs, n, a)}",
            flush=True,
        )
        if not exact:
            continue

        eliminants = [
            resultant_linear_with_quadratic(f, base, n, a, y, field),
            determinant(base, products[4], n, a, y, field),
            determinant(base, products[5], n, a, y, field),
            determinant(base, products[6], n, a, y, field),
        ]
        gcd = eliminants[0]
        for eliminant in eliminants[1:]:
            gcd = sp.gcd(gcd, eliminant)
            if gcd.degree() == 0:
                break
        print(f"  equation-level gcd degree in a: {gcd.degree()}", flush=True)
        print(f"  {classify_gcd(gcd, n)}", flush=True)


if __name__ == "__main__":
    main()
