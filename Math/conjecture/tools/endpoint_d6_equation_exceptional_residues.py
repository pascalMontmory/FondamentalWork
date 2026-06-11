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

from endpoint_d6_equation_modular_probe import DEFAULT_TYPES, specialized_gcd_degree


DEFAULT_PRIMES = [11, 13, 17]


def parse_args() -> tuple[list[tuple[int, int, int, int]], list[int]]:
    args = sys.argv[1:]
    primes = DEFAULT_PRIMES
    for arg in list(args):
        if arg.startswith("--primes="):
            primes = [int(part) for part in arg.removeprefix("--primes=").split(",")]
            args.remove(arg)
    if not args:
        return DEFAULT_TYPES, primes
    return [tuple(int(part) for part in arg.split(",")) for arg in args], primes


def live_degree(gcd_degree: int) -> bool:
    # -1 means all specialized eliminants vanished, so this residue cannot be
    # excluded by the gcd test.
    return gcd_degree != 0


def main() -> None:
    weights_list, primes = parse_args()
    for weights in weights_list:
        print(f"weights {weights}", flush=True)
        modulus = 1
        survivor_count = 1
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
            print(
                f"  p={prime}: bad={sorted(bad)}, live={live}, "
                f"gcd_degrees={gcd_degrees}, "
                f"saturated survivor classes={survivor_count} mod {modulus}",
                flush=True,
            )
            if not live:
                print("  saturated residues empty; type excluded modulo this prime", flush=True)
                break


if __name__ == "__main__":
    main()
