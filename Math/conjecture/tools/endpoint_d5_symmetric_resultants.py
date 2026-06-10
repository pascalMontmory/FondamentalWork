#!/usr/bin/env python3
"""Integer certificates for the symmetric endpoint d-5 weight types.

The generic gcd script shows that the two symmetric endpoint d-5 types have
gcd 1 over Q(n)[a]. This script removes the remaining specialization caveat.

For each cover triple of Q3,Q4,Q5, it computes the three pairwise resultants
in a and takes their gcd in Z[n]. A common root in characteristic zero forces
this gcd to vanish. The only possible integer roots are negative, while the
endpoint d-5 parameter satisfies n=d-5 >= 1.
"""

import itertools

import sympy as sp

from endpoint_d5_symmetric_gcds import build_conditions


def primitive_poly(expr: sp.Expr, var: sp.Symbol) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    poly = sp.Poly(numerator, var)
    _, primitive = poly.primitive()
    return sp.Poly(primitive, var)


def nonconstant_linear_roots(poly: sp.Poly, var: sp.Symbol) -> set[int]:
    roots = set()
    for factor, _ in sp.factor_list(poly.as_expr())[1]:
        factor_poly = sp.Poly(factor, var)
        if factor_poly.degree() == 0:
            continue
        assert factor_poly.degree() == 1, factor
        coeffs = factor_poly.all_coeffs()
        root = sp.Rational(-coeffs[1], coeffs[0])
        assert root.q == 1, factor
        roots.add(int(root))
    return roots


def certify_case(name: str, double_q2_root: bool, allowed_roots: set[int]) -> None:
    n, a = sp.symbols("n a")
    conditions = build_conditions(double_q2_root)
    covers = ["0", "a", "r"]

    polys = {
        (order, cover): primitive_poly(conditions[(order, cover)], a)
        for order in [3, 4, 5]
        for cover in covers
    }

    pair_resultants = {}
    for order_a, order_b in [(3, 4), (3, 5), (4, 5)]:
        for cover_a, cover_b in itertools.product(covers, repeat=2):
            p = polys[(order_a, cover_a)]
            q = polys[(order_b, cover_b)]
            if p.degree() == 0 or q.degree() == 0:
                resultant = sp.Poly(1, n)
            else:
                resultant = sp.Poly(
                    sp.together(sp.resultant(p.as_expr(), q.as_expr(), a)).as_numer_denom()[0],
                    n,
                )
            pair_resultants[(order_a, cover_a, order_b, cover_b)] = resultant

    triples = 0
    for cover3, cover4, cover5 in itertools.product(covers, repeat=3):
        resultants = [
            pair_resultants[(3, cover3, 4, cover4)],
            pair_resultants[(3, cover3, 5, cover5)],
            pair_resultants[(4, cover4, 5, cover5)],
        ]
        gcd = resultants[0]
        for resultant in resultants[1:]:
            gcd = sp.gcd(gcd, resultant)
        roots = nonconstant_linear_roots(gcd, n)
        assert roots <= allowed_roots, (name, (cover3, cover4, cover5), roots)
        triples += 1

    print(
        f"{name}: all {triples} triples have exceptional roots "
        f"inside {sorted(allowed_roots)}"
    )


def main() -> None:
    certify_case("double centroid", False, {-1, -2, -3, -6})
    certify_case("double Q2 root", True, {-1, -2, -4, -6})


if __name__ == "__main__":
    main()
