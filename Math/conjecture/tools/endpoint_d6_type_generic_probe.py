#!/usr/bin/env python3
"""Generic gcd certificates for selected endpoint d-6 weight types.

For a fixed d-6 weight type, each cover pattern gives a finite list of
eliminants in a after eliminating Y.  This script checks whether those
eliminants have gcd 1 over Q(n)[a].  Such a pattern is impossible for generic
n; exceptional specializations still need exact integer certificates.  When
all 256 cover patterns have gcd 1, the given type is generically impossible.
"""

from __future__ import annotations

import itertools
import sys

import sympy as sp

from endpoint_d6_cover_degrees import h_polynomials, reduced_condition


COVERS = ["0", "a", "Y", "z"]
ORDERS = [3, 4, 5, 6]
GENERICALLY_CLOSED_TYPES = [
    (1, 1, 2, 2),
    (1, 3, 1, 1),
    (2, 2, 1, 1),
    (3, 1, 1, 1),
]


def parse_weights() -> list[tuple[int, int, int, int]]:
    if len(sys.argv) == 1:
        return GENERICALLY_CLOSED_TYPES
    return [tuple(int(part) for part in arg.split(",")) for arg in sys.argv[1:]]


def primitive_expr(expr: sp.Expr, *variables: sp.Symbol) -> sp.Expr:
    numerator = sp.together(expr).as_numer_denom()[0]
    _, primitive = sp.Poly(numerator, *variables).primitive()
    return primitive.as_expr()


def build_conditions(
    weights: tuple[int, int, int, int],
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
) -> tuple[sp.Poly, dict[tuple[int, str], sp.Poly]]:
    f, h_by_order, cover_exprs = h_polynomials(n, a, y, x, *weights)
    conditions = {}
    for order in ORDERS:
        for cover_name in COVERS:
            conditions[(order, cover_name)] = reduced_condition(
                h_by_order[order].subs(x, cover_exprs[cover_name]),
                f,
                y,
            )
    return f, conditions


def condition_shape(condition: sp.Poly, y: sp.Symbol) -> tuple[str, sp.Expr, sp.Expr]:
    if condition.is_zero:
        return ("zero", sp.Integer(0), sp.Integer(0))
    if condition.degree() == 0:
        return ("constant", condition.as_expr(), sp.Integer(0))
    assert condition.degree() == 1, condition
    return ("linear", condition.coeff_monomial(y), condition.coeff_monomial(1))


def certify_weights(weights: tuple[int, int, int, int]) -> None:
    n, a, y, x = sp.symbols("n a y x")
    f, conditions = build_conditions(weights, n, a, y, x)
    shapes = {key: condition_shape(condition, y) for key, condition in conditions.items()}
    field = sp.QQ.frac_field(n)
    f_y2 = f.coeff_monomial(y**2)
    f_y1 = f.coeff_monomial(y)
    f_y0 = f.coeff_monomial(1)

    constants: dict[tuple[int, str], sp.Poly] = {}
    line_resultants: dict[tuple[int, str], sp.Poly] = {}
    determinants: dict[tuple[tuple[int, str], tuple[int, str]], sp.Poly] = {}

    for key, (kind, coeff_y, coeff_0) in shapes.items():
        if kind == "constant":
            constants[key] = sp.Poly(primitive_expr(coeff_y, n, a), a, domain=field)
        elif kind == "linear":
            resultant_expr = f_y2 * coeff_0**2 - f_y1 * coeff_y * coeff_0 + f_y0 * coeff_y**2
            line_resultants[key] = sp.Poly(
                primitive_expr(resultant_expr, n, a),
                a,
                domain=field,
            )

    linear_keys = [key for key, shape in shapes.items() if shape[0] == "linear"]
    for left, right in itertools.combinations(linear_keys, 2):
        left_y, left_0 = shapes[left][1], shapes[left][2]
        right_y, right_0 = shapes[right][1], shapes[right][2]
        determinants[(left, right)] = sp.Poly(
            primitive_expr(left_y * right_0 - right_y * left_0, n, a),
            a,
            domain=field,
        )

    summary: dict[int, int] = {}
    examples: dict[int, tuple[str, str, str, str]] = {}
    for cover_tuple in itertools.product(COVERS, repeat=4):
        selected_keys = [
            (order, cover_name) for order, cover_name in zip(ORDERS, cover_tuple, strict=True)
        ]
        linears = [key for key in selected_keys if shapes[key][0] == "linear"]
        eliminants = [constants[key] for key in selected_keys if shapes[key][0] == "constant"]

        if linears:
            first = linears[0]
            eliminants.append(line_resultants[first])
            for key in linears[1:]:
                pair = tuple(sorted([first, key]))
                eliminants.append(determinants[pair])

        if not eliminants:
            degree = -1
        else:
            gcd = eliminants[0]
            for eliminant in eliminants[1:]:
                gcd = sp.gcd(gcd, eliminant)
                if gcd.degree() == 0:
                    break
            degree = gcd.degree()

        summary[degree] = summary.get(degree, 0) + 1
        examples.setdefault(degree, cover_tuple)

    print(f"weights {weights}", flush=True)
    for degree, count in sorted(summary.items()):
        label = "underdetermined" if degree < 0 else f"generic gcd degree {degree}"
        print(f"  {count}: {label}; example={examples[degree]}", flush=True)
    assert summary == {0: 256}, (weights, summary)


def main() -> None:
    for weights in parse_weights():
        certify_weights(weights)


if __name__ == "__main__":
    main()
