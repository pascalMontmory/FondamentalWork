#!/usr/bin/env python3
"""Residue sieve for endpoint multiplicity d-6 diagnostics.

For each weight type and prime p, record the n-residues for which the
endpoint d-6 cover system has a nondegenerate F_p point.  An integer solution
must either land on one of those residues or on a bad denominator residue
n+1,...,n+6 == 0 mod p.

The script reports the local allowed residues and the resulting density of
surviving residue classes modulo the product of the tested primes.  It does
not materialize the CRT classes, which become numerous even when the density
shrinks.
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_modular_sieve import branch_conditions, eval_terms, poly_terms
from endpoint_d6_reduction import weight_types


PRIMES = [7, 11, 13, 17, 19, 23, 29, 31]


def parse_requested_weights() -> set[tuple[int, int, int, int]] | None:
    if len(sys.argv) == 1:
        return None
    return {tuple(int(part) for part in arg.split(",")) for arg in sys.argv[1:]}


def allowed_residues(
    f_terms: list[tuple[tuple[int, ...], int]],
    conditions: dict[int, list[list[tuple[tuple[int, ...], int]]]],
    prime: int,
) -> tuple[set[int], set[int], set[int]]:
    bad = {(-offset) % prime for offset in range(1, 7)}
    live: set[int] = set()
    for n_value in range(prime):
        for a_value in range(1, prime):
            for y_value in range(prime):
                values = (n_value, a_value, y_value)
                if n_value in bad:
                    continue
                if eval_terms(f_terms, values, prime) != 0:
                    continue
                if all(
                    any(eval_terms(condition, values, prime) == 0 for condition in choices)
                    for choices in conditions.values()
                ):
                    live.add(n_value)
                    break
            if n_value in live:
                break
    return bad | live, bad, live


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

        modulus = 1
        survivor_count = 1
        print(f"weights {weights}", flush=True)
        for prime in PRIMES:
            allowed, bad, live = allowed_residues(f_terms, conditions, prime)
            modulus *= prime
            survivor_count *= len(allowed)
            print(
                f"  p={prime}: bad={sorted(bad)}, live={sorted(live)}, "
                f"allowed={len(allowed)}/{prime}, "
                f"survivor classes={survivor_count} mod {modulus}",
                flush=True,
            )
        print(
            f"  density={survivor_count}/{modulus} "
            f"({survivor_count / modulus:.6f})",
            flush=True,
        )


if __name__ == "__main__":
    main()
