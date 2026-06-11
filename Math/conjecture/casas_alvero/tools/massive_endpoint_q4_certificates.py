#!/usr/bin/env python3
"""Exact certificates for the massive-endpoint Q4 branches.

This is not a numerical search. It reconstructs the symbolic resultants in
the one-parameter massive-endpoint branch and verifies that the integer
parameter n cannot satisfy any of the reduced Q4-cover branches.
"""

import sympy as sp


def has_root_mod(poly: sp.Poly, prime: int) -> bool:
    coeffs = [int(c % prime) for c in poly.all_coeffs()]
    for r in range(prime):
        value = 0
        for c in coeffs:
            value = (value * r + c) % prime
        if value == 0:
            return True
    return False


def largest_degree_factor(expr: sp.Expr, var: sp.Symbol) -> sp.Poly:
    factors = sp.factor_list(expr)[1]
    factor = max((factor for factor, _ in factors), key=lambda f: sp.Poly(f, var).degree())
    return sp.Poly(factor, var)


def main() -> None:
    n, a, x = sp.symbols("n a x")
    d = n + 4
    d2 = d * (d - 1)
    d3 = d2 * (d - 2)
    d4 = d3 * (d - 3)

    s = n - a
    p = (s**2 + n + a**2 - d2 * a**2) / 2
    f = sp.expand(x**2 - s * x + p)

    t0 = sp.Integer(2)
    t1 = s
    t2 = sp.expand(s * t1 - p * t0)
    t3 = sp.expand(s * t2 - p * t1)
    t4 = sp.expand(s * t3 - p * t2)

    m2 = sp.expand(n + a**2 + t2)
    m3 = sp.expand(-n + a**3 + t3)
    m4 = sp.expand(n + a**4 + t4)

    h3 = sp.expand(d3 * (x**3 - 3 * a**2 * x) - 2 * m3)
    e3 = sp.together(-8 * sp.resultant(f, h3, x)).as_numer_denom()[0]

    h4 = sp.expand(d4 * (x**4 - 6 * a**2 * x**2) - 8 * m3 * x + 3 * m2**2 - 6 * m4)
    q4_centroid = sp.together((2 * m4 - m2**2) / (-n)).as_numer_denom()[0]
    q4_same_root = sp.together(
        (d4 * (-5 * a**4) - 8 * m3 * a + 3 * m2**2 - 6 * m4) / (-n)
    ).as_numer_denom()[0]

    certificates = [
        ("Q4 centroid", q4_centroid, 17, 39),
        ("Q4 same root", q4_same_root, 11, 48),
    ]

    for name, condition, prime, expected_degree in certificates:
        resultant = sp.factor(sp.resultant(e3, condition, a))
        poly = largest_degree_factor(resultant, n)
        assert poly.degree() == expected_degree, (name, poly.degree())
        assert not has_root_mod(poly, prime), name
        print(f"{name}: degree {poly.degree()} factor has no roots modulo {prime}")

    f_poly = sp.Poly(f, x)
    h3_reduced = sp.Poly(h3, x).rem(f_poly)
    h4_reduced = sp.Poly(h4, x).rem(f_poly)
    a3 = h3_reduced.coeff_monomial(x)
    b3 = h3_reduced.coeff_monomial(1)
    a4 = h4_reduced.coeff_monomial(x)
    b4 = h4_reduced.coeff_monomial(1)

    common_root_condition = sp.together(a3 * b4 - a4 * b3).as_numer_denom()[0]
    final_resultant = sp.factor(sp.resultant(e3, common_root_condition, a))
    final_factors = [
        (sp.Poly(factor, n), exponent)
        for factor, exponent in sp.factor_list(final_resultant)[1]
        if sp.Poly(factor, n).degree() > 1
    ]
    final_factors.sort(key=lambda item: item[0].degree())

    expected_final = [
        (13, 2, 13),
        (46, 1, 17),
    ]
    assert len(final_factors) == len(expected_final), len(final_factors)
    for (poly, exponent), (expected_degree, expected_exponent, prime) in zip(
        final_factors, expected_final
    ):
        assert poly.degree() == expected_degree, poly.degree()
        assert exponent == expected_exponent, (poly.degree(), exponent)
        assert not has_root_mod(poly, prime), poly.degree()
        print(
            "Q4 interior common root: "
            f"degree {poly.degree()} factor has no roots modulo {prime}"
        )


if __name__ == "__main__":
    main()
