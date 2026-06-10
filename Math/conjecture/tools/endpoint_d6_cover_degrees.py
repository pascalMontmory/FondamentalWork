#!/usr/bin/env python3
"""Cover-condition degrees for the endpoint multiplicity d-6 branch.

The first d-6 reduction records the shape of H3,H4,H5,H6 modulo the weighted
quadratic before choosing which root covers each derivative. This script makes
the next obstruction explicit: it substitutes each possible covering root
0,a,Y,z and records the remaining Y-degree of every condition.
"""

from __future__ import annotations

import sympy as sp

from endpoint_d6_reduction import weight_types, weighted_quadratic


def h_polynomials(
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
    m0: int,
    ma: int,
    my: int,
    mz: int,
) -> tuple[sp.Poly, dict[int, sp.Expr], dict[str, sp.Expr]]:
    d = n + 6
    d2 = d * (d - 1)
    d3 = d2 * (d - 2)
    d4 = d3 * (d - 3)
    d5 = d4 * (d - 4)
    d6 = d5 * (d - 5)

    f = sp.Poly(weighted_quadratic(n, a, y, ma, my, mz), y)
    z = sp.together((n - ma * a - my * y) / mz)

    moments = {}
    for k in range(2, 7):
        moments[k] = sp.expand(
            n * (-1) ** k + m0 * 0**k + ma * a**k + my * y**k + mz * z**k
        )

    h3 = sp.expand(d3 * (x**3 - 3 * a**2 * x) - 2 * moments[3])
    h4 = sp.expand(
        d4 * (x**4 - 6 * a**2 * x**2)
        - 8 * moments[3] * x
        + 3 * moments[2] ** 2
        - 6 * moments[4]
    )
    h5 = sp.expand(
        d5 * (x**5 - 10 * a**2 * x**3)
        - 20 * moments[3] * (n + 3) * (n + 2) * x**2
        + (15 * moments[2] ** 2 - 30 * moments[4]) * (n + 2) * x
        + 20 * moments[2] * moments[3]
        - 24 * moments[5]
    )
    h6 = sp.expand(
        d6 * x**6
        - 15 * moments[2] * (n + 4) * (n + 3) * (n + 2) * (n + 1) * x**4
        - 40 * moments[3] * (n + 3) * (n + 2) * (n + 1) * x**3
        + (45 * moments[2] ** 2 - 90 * moments[4]) * (n + 2) * (n + 1) * x**2
        + (120 * moments[2] * moments[3] - 144 * moments[5]) * (n + 1) * x
        - 15 * moments[2] ** 3
        + 90 * moments[2] * moments[4]
        + 40 * moments[3] ** 2
        - 120 * moments[6]
    )
    return f, {3: h3, 4: h4, 5: h5, 6: h6}, {"0": sp.Integer(0), "a": a, "Y": y, "z": z}


def reduced_condition(expr: sp.Expr, f: sp.Poly, y: sp.Symbol) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    reduced = sp.Poly(numerator, y).rem(f)
    _, primitive = reduced.primitive()
    return sp.Poly(primitive, y)


def main() -> None:
    n, a, y, x = sp.symbols("n a y x")

    for weights in weight_types():
        m0, ma, my, mz = weights
        f, h_by_order, covers = h_polynomials(n, a, y, x, m0, ma, my, mz)

        print(f"weights (m0, ma, my, mz) = {weights}")
        for order in [3, 4, 5, 6]:
            degrees = []
            for name, cover in covers.items():
                condition = reduced_condition(h_by_order[order].subs(x, cover), f, y)
                degrees.append(f"{name}:{condition.degree()}")
            print(f"  H{order} cover degrees in Y: {', '.join(degrees)}")


if __name__ == "__main__":
    main()
