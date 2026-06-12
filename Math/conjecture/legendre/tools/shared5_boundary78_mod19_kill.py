#!/usr/bin/env python3
"""Kill the unique shared-5 lifted-root boundary family at energy 78.

The previous lifted-root certificate reduced the entire energy-78 boundary
modulo 2310 to one projected family:

    A = 882 mod 2310
    (e_5,e_17,e_25,e_49,e_65) = (42,18,10,2,6).

This script proves that the family has no lift modulo 19.  For each
offset/quotient pair it computes the set of alpha = A mod 19 for which

    r^2 + e r + c - e alpha = 0 mod 19

has a root satisfying the prime-label unit condition alpha-r != 0 mod 19.
The five allowed alpha sets have empty intersection.
"""

from __future__ import annotations


PRIME = 19
BOUNDARY_PATTERN = ((5, 42), (17, 18), (25, 10), (49, 2), (65, 6))


def lifted_roots_mod_prime(c: int, e: int, alpha: int) -> tuple[int, ...]:
    return tuple(
        r
        for r in range(PRIME)
        if (r * r + e * r + c - e * alpha) % PRIME == 0
        and (alpha - r) % PRIME != 0
    )


def allowed_alphas(c: int, e: int) -> tuple[int, ...]:
    return tuple(
        alpha
        for alpha in range(PRIME)
        if lifted_roots_mod_prime(c, e, alpha)
    )


def main() -> int:
    allowed_sets = []
    for c, e in BOUNDARY_PATTERN:
        alphas = allowed_alphas(c, e)
        allowed_sets.append(set(alphas))
        print(f"(c,e)=({c},{e}) allowed_A_mod_{PRIME}={alphas}")

    intersection = set(range(PRIME))
    for allowed in allowed_sets:
        intersection &= allowed

    print(f"intersection={tuple(sorted(intersection))}")

    if intersection:
        print("certificate failed: the boundary family still has a mod-19 lift")
        return 1

    print("certificate: the unique energy-78 boundary family has no mod-19 lift")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
