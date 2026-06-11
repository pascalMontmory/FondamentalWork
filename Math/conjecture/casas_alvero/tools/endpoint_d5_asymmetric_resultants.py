#!/usr/bin/env python3
"""Integer certificate for the asymmetric endpoint d-5 weight type.

This closes the remaining endpoint d-5 type

    (m0, ma, my, mz) = (1, 1, 2, 1).

After Q2, the weighted quadratic F(a,Y)=0 reconstructs the two remaining
nonzero roots. Every Q3/Q4/Q5 cover condition reduces modulo F to a linear
form in Y. For each cover triple, a solution must make:

* F and the Q3 linear form share a Y-root;
* the Q3, Q4, and Q5 linear forms share the same Y-root.

The script eliminates Y by one resultant and two 2x2 determinants, then
eliminates a by pairwise resultants. It verifies that every possible integer
parameter n=d-5 would have to vanish on one of five fixed nonlinear factors,
each of which has no root modulo a small prime.
"""

import itertools

import sympy as sp


def has_root_mod(poly: sp.Poly, prime: int) -> bool:
    for residue in range(prime):
        if poly.eval(residue) % prime == 0:
            return True
    return False


def primitive_poly(expr: sp.Expr, var: sp.Symbol) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    poly = sp.Poly(numerator, var)
    _, primitive = poly.primitive()
    return sp.Poly(primitive, var)


def build_linear_conditions() -> tuple[
    sp.Symbol,
    sp.Symbol,
    sp.Poly,
    dict[tuple[int, str], tuple[sp.Expr, sp.Expr]],
]:
    n, a, y, x = sp.symbols("n a y x")
    d = n + 5
    d2 = d * (d - 1)
    d3 = d2 * (d - 2)
    d4 = d3 * (d - 3)
    d5 = d4 * (d - 4)

    f = sp.Poly(
        6 * y**2
        + 4 * (a - n) * y
        + n**2
        - 2 * n * a
        + n
        - (n + 3) * (n + 6) * a**2,
        y,
    )
    z = n - a - 2 * y

    moments = {}
    for k in range(2, 6):
        moments[k] = sp.expand(n * (-1) ** k + a**k + 2 * y**k + z**k)

    h3 = sp.expand(d3 * (x**3 - 3 * a**2 * x) - 2 * moments[3])
    h4 = sp.expand(
        d4 * (x**4 - 6 * a**2 * x**2)
        - 8 * moments[3] * x
        + 3 * moments[2] ** 2
        - 6 * moments[4]
    )
    h5 = sp.expand(
        d5 * (x**5 - 10 * a**2 * x**3)
        - 20 * moments[3] * (n + 2) * (n + 1) * x**2
        + (15 * moments[2] ** 2 - 30 * moments[4]) * (n + 1) * x
        + 20 * moments[2] * moments[3]
        - 24 * moments[5]
    )

    cover_exprs = {"0": sp.Integer(0), "a": a, "Y": y, "z": z}
    conditions = {}
    for order, h in [(3, h3), (4, h4), (5, h5)]:
        for cover, expr in cover_exprs.items():
            reduced = sp.Poly(sp.together(h.subs(x, expr)).as_numer_denom()[0], y).rem(f)
            conditions[(order, cover)] = (
                reduced.coeff_monomial(y),
                reduced.coeff_monomial(1),
            )
    return n, a, f, conditions


def main() -> None:
    n, a, f, conditions = build_linear_conditions()
    y = f.gens[0]
    covers = ["0", "a", "Y", "z"]

    resultant_cache = {}

    def resultant_in_a(poly_a: sp.Poly, poly_b: sp.Poly) -> sp.Poly:
        key = (poly_a.as_expr(), poly_b.as_expr())
        if key not in resultant_cache:
            if poly_a.degree() == 0 or poly_b.degree() == 0:
                resultant_cache[key] = sp.Poly(1, n)
            else:
                resultant_cache[key] = sp.Poly(
                    sp.together(sp.resultant(poly_a.as_expr(), poly_b.as_expr(), a))
                    .as_numer_denom()[0],
                    n,
                )
        return resultant_cache[key]

    nonlinear_factors = {}
    linear_roots = set()

    for cover3, cover4, cover5 in itertools.product(covers, repeat=3):
        a3, b3 = conditions[(3, cover3)]
        a4, b4 = conditions[(4, cover4)]
        a5, b5 = conditions[(5, cover5)]

        q3_resultant = primitive_poly(sp.resultant(f.as_expr(), a3 * y + b3, y), a)
        q34_same_root = primitive_poly(a3 * b4 - a4 * b3, a)
        q35_same_root = primitive_poly(a3 * b5 - a5 * b3, a)

        candidate = sp.gcd(
            resultant_in_a(q3_resultant, q34_same_root),
            resultant_in_a(q3_resultant, q35_same_root),
        )
        candidate = sp.gcd(candidate, resultant_in_a(q34_same_root, q35_same_root))

        for factor, _ in sp.factor_list(candidate.as_expr())[1]:
            factor_poly = sp.Poly(factor, n)
            degree = factor_poly.degree()
            if degree == 0:
                continue
            if degree == 1:
                coeffs = factor_poly.all_coeffs()
                root = sp.Rational(-coeffs[1], coeffs[0])
                assert root.q == 1
                linear_roots.add(int(root))
            else:
                nonlinear_factors[sp.factor(factor_poly.as_expr())] = degree

    assert linear_roots <= {0, -1, -2, -3, -4, -6}, sorted(linear_roots)
    expected = {
        5: 7,
        7: 5,
        20: 11,
        22: 7,
    }
    degree_counts = {}
    for expr, degree in nonlinear_factors.items():
        degree_counts[degree] = degree_counts.get(degree, 0) + 1
        prime = expected[degree]
        poly = sp.Poly(expr, n)
        assert not has_root_mod(poly, prime), (degree, prime)

    assert degree_counts == {5: 1, 7: 2, 20: 1, 22: 1}, degree_counts
    print(f"asymmetric endpoint d-5: checked {len(covers) ** 3} cover triples")
    print(f"linear exceptional roots: {sorted(linear_roots)}")
    for degree in sorted(degree_counts):
        print(
            f"degree {degree}: {degree_counts[degree]} factor(s), "
            f"no roots modulo {expected[degree]}"
        )


if __name__ == "__main__":
    main()
