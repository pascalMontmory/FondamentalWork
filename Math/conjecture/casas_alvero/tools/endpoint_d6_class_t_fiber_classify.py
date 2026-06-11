#!/usr/bin/env python3
"""Classify local endpoint d-6 fibers in the class parameter t.

For a fixed CRT class

    n = c + M t,

this script scans t modulo one or more coefficient primes and separates the
fibers into:

- saturated_bad: one of n+1,...,n+6 vanishes modulo p;
- all_zero: all four specialized eliminants vanish;
- degree_drop: at least one eliminant drops below the observed generic degree;
- regular_gcd: no degree drop and the four eliminants have positive-degree gcd;
- excluded: no degree drop and gcd degree is zero.

The point is to separate true local gcd fibers from denominator and
specialization artifacts before attempting to reconstruct a class-level
factor in F_p[t].
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

import sympy as sp

from endpoint_d6_equation_modular_probe import DEFAULT_TYPES, specialized_gcd_degree


DEFAULT_CLASS = (0, 2431)
DEFAULT_PRIMES = [101, 103]
NEG_INF = -sp.oo


@dataclass(frozen=True)
class Fiber:
    t_value: int
    n_value: int
    gcd_degree: int
    eliminant_degrees: tuple[int | sp.Integer, ...]


def parse_args() -> tuple[list[tuple[int, int, int, int]], tuple[int, int], list[int], int | None]:
    args = sys.argv[1:]
    cls = DEFAULT_CLASS
    primes = DEFAULT_PRIMES
    max_t = None
    for arg in list(args):
        if arg.startswith("--class="):
            residue, modulus = arg.removeprefix("--class=").split(",")
            cls = (int(residue), int(modulus))
            args.remove(arg)
        elif arg.startswith("--primes="):
            primes = [int(part) for part in arg.removeprefix("--primes=").split(",")]
            args.remove(arg)
        elif arg.startswith("--max-t="):
            max_t = int(arg.removeprefix("--max-t="))
            args.remove(arg)

    weights_list = DEFAULT_TYPES if not args else [
        tuple(int(part) for part in arg.split(",")) for arg in args
    ]
    return weights_list, cls, primes, max_t


def bad_n_residues(prime: int) -> set[int]:
    return {(-offset) % prime for offset in range(1, 7)}


def residue_factor(residues: list[int], symbol: sp.Symbol, prime: int) -> sp.Poly:
    poly = sp.Poly(1, symbol, modulus=prime)
    for residue in residues:
        poly *= sp.Poly(symbol - residue, symbol, modulus=prime)
    return sp.Poly(poly.as_expr(), symbol, modulus=prime)


def format_factor(residues: list[int], prime: int) -> str:
    t = sp.symbols("t")
    factor = residue_factor(residues, t, prime)
    if factor.degree() == 0:
        return "1"
    return str(sp.factor(factor.as_expr(), modulus=prime))


def scan_fibers(
    weights: tuple[int, int, int, int],
    cls: int,
    modulus: int,
    prime: int,
    max_t: int | None,
) -> tuple[list[Fiber], list[tuple[int, int]]]:
    if modulus % prime == 0:
        raise ValueError(f"prime {prime} divides class modulus {modulus}")

    limit = prime if max_t is None else min(max_t, prime)
    bad_n = bad_n_residues(prime)
    fibers = []
    saturated_bad = []
    for t_value in range(limit):
        n_value = (cls + modulus * t_value) % prime
        if n_value in bad_n:
            saturated_bad.append((t_value, n_value))
            continue
        gcd_degree, eliminant_degrees = specialized_gcd_degree(weights, n_value, prime)
        fibers.append(
            Fiber(
                t_value=t_value,
                n_value=n_value,
                gcd_degree=gcd_degree,
                eliminant_degrees=tuple(eliminant_degrees),
            )
        )
    return fibers, saturated_bad


def generic_degrees(fibers: list[Fiber]) -> tuple[int, ...]:
    maxima = []
    for index in range(4):
        finite_degrees = [
            int(fiber.eliminant_degrees[index])
            for fiber in fibers
            if fiber.eliminant_degrees[index] != NEG_INF
        ]
        maxima.append(max(finite_degrees) if finite_degrees else -1)
    return tuple(maxima)


def has_degree_drop(fiber: Fiber, expected: tuple[int, ...]) -> bool:
    for degree, expected_degree in zip(fiber.eliminant_degrees, expected):
        if degree == NEG_INF or int(degree) < expected_degree:
            return True
    return False


def classify_fibers(
    fibers: list[Fiber],
    saturated_bad: list[tuple[int, int]],
) -> dict[str, list[Fiber | tuple[int, int]]]:
    expected = generic_degrees(fibers)
    categories: dict[str, list[Fiber | tuple[int, int]]] = {
        "saturated_bad": list(saturated_bad),
        "all_zero": [],
        "degree_drop": [],
        "regular_gcd": [],
        "excluded": [],
    }
    for fiber in fibers:
        if fiber.gcd_degree == -1:
            categories["all_zero"].append(fiber)
        elif has_degree_drop(fiber, expected):
            categories["degree_drop"].append(fiber)
        elif fiber.gcd_degree == 0:
            categories["excluded"].append(fiber)
        else:
            categories["regular_gcd"].append(fiber)
    return categories


def t_values(items: list[Fiber | tuple[int, int]]) -> list[int]:
    values = []
    for item in items:
        if isinstance(item, Fiber):
            values.append(item.t_value)
        else:
            values.append(item[0])
    return values


def detail_items(items: list[Fiber | tuple[int, int]]) -> list[tuple]:
    details = []
    for item in items:
        if isinstance(item, Fiber):
            details.append(
                (
                    item.t_value,
                    item.n_value,
                    item.gcd_degree,
                    item.eliminant_degrees,
                )
            )
        else:
            details.append((item[0], item[1]))
    return details


def report_prime(
    weights: tuple[int, int, int, int],
    cls: int,
    modulus: int,
    prime: int,
    max_t: int | None,
) -> None:
    fibers, saturated_bad = scan_fibers(weights, cls, modulus, prime, max_t)
    expected = generic_degrees(fibers)
    categories = classify_fibers(fibers, saturated_bad)
    print(
        f"  p={prime}: scanned={len(fibers) + len(saturated_bad)}, "
        f"expected_degrees={expected}",
        flush=True,
    )
    for name in ["saturated_bad", "all_zero", "degree_drop", "regular_gcd", "excluded"]:
        values = t_values(categories[name])
        print(
            f"    {name}: count={len(values)}, t={values}, "
            f"factor={format_factor(values, prime)}",
            flush=True,
        )
        if name != "excluded" and values:
            print(f"      details={detail_items(categories[name])}", flush=True)


def main() -> None:
    weights_list, (cls, modulus), primes, max_t = parse_args()
    for weights in weights_list:
        print(f"weights {weights}, class n={cls}+{modulus}*t", flush=True)
        for prime in primes:
            report_prime(weights, cls, modulus, prime, max_t)


if __name__ == "__main__":
    main()
