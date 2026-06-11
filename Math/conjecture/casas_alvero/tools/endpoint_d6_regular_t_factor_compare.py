#!/usr/bin/env python3
"""Compare regular endpoint d-6 local t-factors across primes.

This script uses the local t-fiber classifier and keeps only the regular-gcd
fibers: no saturated denominator, no all-zero eliminant fiber, and no
eliminant degree drop.  The goal is to avoid reconstructing the raw live
factor, which mixes true local gcd fibers with specialization artifacts.
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_class_t_fiber_classify import (
    DEFAULT_CLASS,
    Fiber,
    classify_fibers,
    format_factor,
    generic_degrees,
    scan_fibers,
    t_values,
)
from endpoint_d6_equation_modular_probe import DEFAULT_TYPES


DEFAULT_PRIMES = [101, 103, 107]


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


def gcd_degree_profile(items: list[Fiber]) -> dict[int, int]:
    profile: dict[int, int] = {}
    for item in items:
        profile[item.gcd_degree] = profile.get(item.gcd_degree, 0) + 1
    return dict(sorted(profile.items()))


def regular_factor_report(
    weights: tuple[int, int, int, int],
    cls: int,
    modulus: int,
    prime: int,
    max_t: int | None,
) -> tuple[int, int]:
    fibers, saturated_bad = scan_fibers(weights, cls, modulus, prime, max_t)
    categories = classify_fibers(fibers, saturated_bad)
    regular = [item for item in categories["regular_gcd"] if isinstance(item, Fiber)]
    regular_t = t_values(categories["regular_gcd"])
    expected = generic_degrees(fibers)
    print(
        f"  p={prime}: expected_degrees={expected}; "
        f"saturated_bad={len(categories['saturated_bad'])}, "
        f"all_zero={len(categories['all_zero'])}, "
        f"degree_drop={len(categories['degree_drop'])}, "
        f"regular_degree={len(regular_t)}, excluded={len(categories['excluded'])}",
        flush=True,
    )
    print(f"    regular gcd profile={gcd_degree_profile(regular)}", flush=True)
    print(f"    regular roots={regular_t}", flush=True)
    print(f"    regular factor={format_factor(regular_t, prime)}", flush=True)
    return prime, len(regular_t)


def compare_degrees(degrees: list[tuple[int, int]]) -> None:
    if not degrees:
        return
    if len(degrees) == 1:
        print(f"  regular degree observed: {degrees[0][1]}", flush=True)
        return
    degree_values = [degree for _, degree in degrees]
    if len(set(degree_values)) == 1:
        print(f"  regular degree stable: {degree_values[0]}", flush=True)
        return

    print(f"  regular degree varies by prime: {degrees}", flush=True)
    print(
        "  interpretation: the regular positive-gcd fibers are not yet a stable "
        "single lifted factor over these primes, or some primes are still bad "
        "for the local model.",
        flush=True,
    )


def main() -> None:
    weights_list, (cls, modulus), primes, max_t = parse_args()
    for weights in weights_list:
        print(f"weights {weights}, class n={cls}+{modulus}*t", flush=True)
        degrees = [
            regular_factor_report(weights, cls, modulus, prime, max_t)
            for prime in primes
        ]
        compare_degrees(degrees)


if __name__ == "__main__":
    main()
