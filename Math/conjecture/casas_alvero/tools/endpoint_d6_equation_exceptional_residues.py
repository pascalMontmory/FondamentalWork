#!/usr/bin/env python3
"""Residue sieve for endpoint d-6 exceptional n-specializations.

The equation-level modular probe can certify generic gcd 1 from one good
specialization.  This companion script keeps every n-residue and records where
the specialized eliminants still have a positive-degree gcd in F_p[a].

For an integer solution with the saturation

    a(n+1)(n+2)(n+3)(n+4)(n+5)(n+6) != 0,

the residue of n modulo any tested prime must be one of the reported live
residues.  Bad denominator residues are displayed separately rather than
counted as saturated live residues.
"""

from __future__ import annotations

import sys

import sympy as sp
from sympy.ntheory.modular import crt

from endpoint_d6_equation_modular_probe import DEFAULT_TYPES, specialized_gcd_degree


DEFAULT_PRIMES = [11, 13, 17]


def parse_args() -> tuple[list[tuple[int, int, int, int]], list[int], bool, bool]:
    args = sys.argv[1:]
    primes = DEFAULT_PRIMES
    show_crt = "--crt" in args
    show_factors = "--factors" in args
    args = [arg for arg in args if arg != "--crt"]
    args = [arg for arg in args if arg != "--factors"]
    for arg in list(args):
        if arg.startswith("--primes="):
            primes = [int(part) for part in arg.removeprefix("--primes=").split(",")]
            args.remove(arg)
    if not args:
        return DEFAULT_TYPES, primes, show_crt, show_factors
    return [tuple(int(part) for part in arg.split(",")) for arg in args], primes, show_crt, show_factors


def live_degree(gcd_degree: int) -> bool:
    # -1 means all specialized eliminants vanished, so this residue cannot be
    # excluded by the gcd test.
    return gcd_degree != 0


def combine_crt_classes(classes: list[int], modulus: int, prime: int, residues: list[int]) -> list[int]:
    combined = []
    for cls in classes:
        for residue in residues:
            value, new_modulus = crt([modulus, prime], [cls, residue])
            assert int(new_modulus) == modulus * prime
            combined.append(int(value) % int(new_modulus))
    return sorted(set(combined))


def live_residue_factor(residues: list[int], prime: int) -> sp.Poly:
    n = sp.symbols("n")
    poly = sp.Poly(1, n, modulus=prime)
    for residue in residues:
        poly *= sp.Poly(n - residue, n, modulus=prime)
    return sp.Poly(poly.as_expr(), n, modulus=prime)


def format_factor(poly: sp.Poly, prime: int) -> str:
    if poly.degree() == 0:
        return "1"
    return str(sp.factor(poly.as_expr(), modulus=prime))


def main() -> None:
    weights_list, primes, show_crt, show_factors = parse_args()
    for weights in weights_list:
        print(f"weights {weights}", flush=True)
        modulus = 1
        survivor_count = 1
        crt_classes = [0]
        for prime in primes:
            bad = {(-offset) % prime for offset in range(1, 7)}
            live = []
            gcd_degrees = {}
            for n_value in range(prime):
                if n_value in bad:
                    continue
                gcd_degree, _ = specialized_gcd_degree(weights, n_value, prime)
                gcd_degrees[n_value] = gcd_degree
                if live_degree(gcd_degree):
                    live.append(n_value)

            modulus *= prime
            survivor_count *= len(live)
            crt_classes = combine_crt_classes(crt_classes, modulus // prime, prime, live)
            print(
                f"  p={prime}: bad={sorted(bad)}, live={live}, "
                f"gcd_degrees={gcd_degrees}, "
                f"saturated survivor classes={survivor_count} mod {modulus}",
                flush=True,
            )
            if show_factors:
                live_factor = live_residue_factor(live, prime)
                print(
                    f"    live factor in F_{prime}[n]: "
                    f"degree={live_factor.degree()}, {format_factor(live_factor, prime)}",
                    flush=True,
                )
            if not live:
                print("  saturated residues empty; type excluded modulo this prime", flush=True)
                break
        if show_crt:
            print(f"  CRT classes mod {modulus}: {crt_classes}", flush=True)


if __name__ == "__main__":
    main()
