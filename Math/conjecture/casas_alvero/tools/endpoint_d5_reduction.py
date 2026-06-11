#!/usr/bin/env python3
"""Symbolic reduction for the endpoint multiplicity d-5 branch.

The branch has one endpoint of multiplicity n=d-5. The remaining four roots
have total multiplicity five, so exactly one of them is double. After choosing
the nonzero root a selected by Q2, the two remaining nonzero roots satisfy a
weighted quadratic. This script reconstructs that quadratic for the three
weight types, and records the reduced top-derivative equations Q3, Q4, Q5.
"""

import sympy as sp


def weighted_quadratic(
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    ma: int,
    my: int,
    mz: int,
) -> sp.Expr:
    d2 = (n + 5) * (n + 4)
    return sp.expand(
        my * (my + mz) * y**2
        + 2 * my * (ma * a - n) * y
        + n**2
        - 2 * ma * n * a
        + mz * n
        + ma * (ma + mz) * a**2
        - mz * d2 * a**2
    )


def main() -> None:
    n, a, y, x = sp.symbols("n a y x")
    d = n + 5
    d2 = d * (d - 1)
    d3 = d2 * (d - 2)
    d4 = d3 * (d - 3)
    d5 = d4 * (d - 4)

    weight_types = [
        ("double centroid", 2, 1, 1, 1),
        ("double Q2 root", 1, 2, 1, 1),
        ("double other root", 1, 1, 2, 1),
    ]

    for name, m0, ma, my, mz in weight_types:
        assert m0 + ma + my + mz == 5
        f = weighted_quadratic(n, a, y, ma, my, mz)
        z = sp.together((n - ma * a - my * y) / mz)

        moments = {}
        for k in range(2, 6):
            moments[k] = sp.expand(n * (-1) ** k + ma * a**k + my * y**k + mz * z**k)

        q3 = sp.expand(d3 * (x**3 - 3 * a**2 * x) - 2 * moments[3])
        q4 = sp.expand(
            d4 * (x**4 - 6 * a**2 * x**2)
            - 8 * moments[3] * x
            + 3 * moments[2] ** 2
            - 6 * moments[4]
        )
        q5 = sp.expand(
            d5 * (x**5 - 10 * a**2 * x**3)
            - 20 * moments[3] * (n + 2) * (n + 1) * x**2
            + (15 * moments[2] ** 2 - 30 * moments[4]) * (n + 1) * x
            + 20 * moments[2] * moments[3]
            - 24 * moments[5]
        )

        print(name)
        print(f"  weights (m0, ma, my, mz) = {(m0, ma, my, mz)}")
        print(f"  weighted quadratic degree in y: {sp.Poly(f, y).degree()}")
        for label, q in [("H3", q3), ("H4", q4), ("H5", q5)]:
            reduced = sp.Poly(q, y).rem(sp.Poly(f, y))
            print(
                f"  {label} reduced modulo F: "
                f"degree_y={sp.Poly(reduced, y).degree()}, "
                f"degree_a={sp.Poly(reduced, a).degree()}"
            )


if __name__ == "__main__":
    main()
