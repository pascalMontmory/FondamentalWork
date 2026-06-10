#!/usr/bin/env python3
"""Modular diagnostics for endpoint multiplicity d-6 weight types.

For a fixed weight type, the endpoint d-6 branch requires the weighted
quadratic F(a,Y)=0 and, for each k=3,4,5,6, at least one of the four roots
0,a,Y,z to cover Q_k. After clearing denominators this gives the polynomial
system

    F = 0,
    prod_root H_k(root) = 0  for k=3,4,5,6.

The test below counts points over small finite fields. This is a diagnostic
tool for finding promising eliminations before committing to exact resultants;
unlike the univariate-in-n certificates elsewhere in this directory, a
multivariate finite-field count is not by itself a complete characteristic-zero
certificate.
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_cover_degrees import h_polynomials, reduced_condition
from endpoint_d6_reduction import weight_types


PRIMES = [7, 11, 13, 17, 19, 23, 29, 31]


def poly_terms(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> list[tuple[tuple[int, ...], int]]:
    poly = sp.Poly(sp.together(expr).as_numer_denom()[0], *variables)
    return [(powers, int(coeff)) for powers, coeff in poly.terms()]


def eval_terms(
    terms: list[tuple[tuple[int, ...], int]],
    values: tuple[int, ...],
    prime: int,
) -> int:
    total = 0
    for powers, coeff in terms:
        term = coeff % prime
        for value, power in zip(values, powers, strict=True):
            if power:
                term = (term * pow(value, power, prime)) % prime
        total = (total + term) % prime
    return total


def branch_conditions(
    weights: tuple[int, int, int, int],
    n: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
) -> tuple[sp.Expr, dict[int, list[sp.Expr]]]:
    m0, ma, my, mz = weights
    f, h_by_order, covers = h_polynomials(n, a, y, x, m0, ma, my, mz)

    conditions: dict[int, list[sp.Expr]] = {}
    for order in [3, 4, 5, 6]:
        conditions[order] = []
        for cover in covers.values():
            conditions[order].append(
                reduced_condition(h_by_order[order].subs(x, cover), f, y).as_expr()
            )
    return f.as_expr(), conditions


def parse_requested_weights() -> set[tuple[int, int, int, int]] | None:
    if len(sys.argv) == 1:
        return None
    requested = set()
    for arg in sys.argv[1:]:
        requested.add(tuple(int(part) for part in arg.split(",")))
    return requested


def count_points(
    f_terms: list[tuple[tuple[int, ...], int]],
    conditions: dict[int, list[list[tuple[tuple[int, ...], int]]]],
    prime: int,
) -> tuple[int, int, dict[int, int]]:
    count = 0
    good_count = 0
    good_n_residues: dict[int, int] = {}
    bad_n = {(-offset) % prime for offset in range(1, 7)}
    for n_value in range(prime):
        for a_value in range(prime):
            for y_value in range(prime):
                values = (n_value, a_value, y_value)
                if eval_terms(f_terms, values, prime) != 0:
                    continue
                if not all(
                    any(eval_terms(condition, values, prime) == 0 for condition in choices)
                    for choices in conditions.values()
                ):
                    continue

                count += 1
                if a_value != 0 and n_value not in bad_n:
                    good_count += 1
                    good_n_residues[n_value] = good_n_residues.get(n_value, 0) + 1
    return count, good_count, good_n_residues


def main() -> None:
    n, a, y, x = sp.symbols("n a y x")
    variables = (n, a, y)
    requested = parse_requested_weights()

    for weights in weight_types():
        if requested is not None and weights not in requested:
            continue

        f_expr, condition_exprs = branch_conditions(weights, n, a, y, x)
        f_terms = poly_terms(f_expr, variables)
        conditions = {
            order: [poly_terms(condition, variables) for condition in choices]
            for order, choices in condition_exprs.items()
        }
        for prime in PRIMES:
            points, good_points, good_n_residues = count_points(f_terms, conditions, prime)
            if good_points == 0:
                print(
                    f"weights {weights}: no nondegenerate F_{prime}-points "
                    f"({points} total)",
                    flush=True,
                )
                break
            print(
                f"weights {weights}: {points} F_{prime}-points, "
                f"{good_points} nondegenerate, n-residues={sorted(good_n_residues)}",
                flush=True,
            )
        else:
            print(f"weights {weights}: no separating diagnostic prime in {PRIMES}", flush=True)


if __name__ == "__main__":
    main()
