#!/usr/bin/env python3
"""Symbolic reduction for the endpoint multiplicity d-6 branch.

After the endpoint d-5 branch is closed, the next endpoint gate occurs at
derivative order d-7. In that gate one endpoint has multiplicity n=d-6 and
the four remaining roots have total multiplicity six.

After choosing the nonzero root a selected by Q2, the two remaining nonzero
roots again satisfy a weighted quadratic. This script enumerates the seven
weight types, up to exchanging the two remaining roots, and records the
reduced Q3, Q4, Q5, Q6 equations modulo that quadratic.
"""

import itertools

import sympy as sp


def weighted_quadratic(
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    ma: int,
    my: int,
    mz: int,
) -> sp.Expr:
    d2 = (n + 6) * (n + 5)
    return sp.expand(
        my * (my + mz) * y**2
        + 2 * my * (ma * a - n) * y
        + n**2
        - 2 * ma * n * a
        + mz * n
        + ma * (ma + mz) * a**2
        - mz * d2 * a**2
    )


def weight_types() -> list[tuple[int, int, int, int]]:
    types = []
    for m0, ma, my, mz in itertools.product(range(1, 7), repeat=4):
        if m0 + ma + my + mz == 6 and my >= mz:
            types.append((m0, ma, my, mz))
    return types


def main() -> None:
    n, a, y, x = sp.symbols("n a y x")
    d = n + 6
    d2 = d * (d - 1)
    d3 = d2 * (d - 2)
    d4 = d3 * (d - 3)
    d5 = d4 * (d - 4)
    d6 = d5 * (d - 5)

    for m0, ma, my, mz in weight_types():
        f = sp.Poly(weighted_quadratic(n, a, y, ma, my, mz), y)
        z = sp.together((n - ma * a - my * y) / mz)

        moments = {}
        for k in range(2, 7):
            moments[k] = sp.expand(n * (-1) ** k + ma * a**k + my * y**k + mz * z**k)

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

        print(f"weights (m0, ma, my, mz) = {(m0, ma, my, mz)}")
        print(f"  weighted quadratic degree in y: {f.degree()}")
        for label, h in [("H3", h3), ("H4", h4), ("H5", h5), ("H6", h6)]:
            reduced = sp.Poly(sp.together(h).as_numer_denom()[0], y).rem(f)
            print(
                f"  {label} reduced modulo F: "
                f"degree_y={sp.Poly(reduced, y).degree()}, "
                f"degree_a={sp.Poly(reduced, a).degree()}"
            )


if __name__ == "__main__":
    main()
