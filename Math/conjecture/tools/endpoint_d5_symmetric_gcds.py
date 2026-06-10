#!/usr/bin/env python3
"""Generic gcd checks for two endpoint d-5 weight types.

This verifies the generic part of the endpoint multiplicity d-5 branch when
the double non-endpoint root is either the centroid or the Q2 root. In both
cases the two remaining nonzero roots have equal weights, so after Q2 the
moments are univariate in a over Q(n).

The check is intentionally generic: gcd 1 in Q(n)[a] rules out common
solutions away from finitely many special n. Those specializations still need
separate certificates.
"""

import itertools

import sympy as sp


def condition_remainder(expr: sp.Expr, f_poly: sp.Poly, y: sp.Symbol) -> sp.Expr:
    numerator = sp.together(expr).as_numer_denom()[0]
    return sp.Poly(numerator, y).rem(f_poly).as_expr()


def build_conditions(double_q2_root: bool) -> dict[tuple[int, str], sp.Expr]:
    n, a, y, x = sp.symbols("n a y x")
    ma = 2 if double_q2_root else 1
    d = n + 5
    d2 = d * (d - 1)
    d3 = d2 * (d - 2)
    d4 = d3 * (d - 3)
    d5 = d4 * (d - 4)

    f = sp.Poly(
        2 * y**2
        + 2 * (ma * a - n) * y
        + n**2
        - 2 * ma * n * a
        + n
        + ma * (ma + 1) * a**2
        - d2 * a**2,
        y,
    )
    z = n - ma * a - y

    moments = {}
    for k in range(2, 6):
        moments[k] = sp.expand(n * (-1) ** k + ma * a**k + y**k + z**k)

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

    conditions = {}
    for order, h in [(3, h3), (4, h4), (5, h5)]:
        conditions[(order, "0")] = condition_remainder(h.subs(x, 0), f, y)
        conditions[(order, "a")] = condition_remainder(h.subs(x, a), f, y)
        conditions[(order, "r")] = sp.resultant(f.as_expr(), h.subs(x, y), y)
    return conditions


def count_trivial_gcds(conditions: dict[tuple[int, str], sp.Expr]) -> int:
    n, a = sp.symbols("n a")
    field = sp.QQ.frac_field(n)
    count = 0
    covers = ["0", "a", "r"]
    for cover3, cover4, cover5 in itertools.product(covers, repeat=3):
        polys = [
            sp.Poly(conditions[(3, cover3)], a, domain=field),
            sp.Poly(conditions[(4, cover4)], a, domain=field),
            sp.Poly(conditions[(5, cover5)], a, domain=field),
        ]
        gcd = polys[0]
        for poly in polys[1:]:
            gcd = sp.gcd(gcd, poly)
        if gcd.degree() == 0:
            count += 1
    return count


def main() -> None:
    cases = [
        ("double centroid", False),
        ("double Q2 root", True),
    ]
    for name, double_q2_root in cases:
        count = count_trivial_gcds(build_conditions(double_q2_root))
        assert count == 27, (name, count)
        print(f"{name}: all {count} cover triples have gcd 1 in Q(n)[a]")


if __name__ == "__main__":
    main()
