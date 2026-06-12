#!/usr/bin/env python3
"""Verify the shared-5 minimal energy modular certificate.

This is not a search for Legendre witnesses.  It is a finite modular
certificate: the quotient multiset {2,6,10,14,18} cannot satisfy the
shared-5 centered equations modulo 210.
"""

from __future__ import annotations

from itertools import permutations


OFFSETS = (5, 17, 25, 49, 65)
QUOTIENTS = (2, 6, 10, 14, 18)
MODULUS = 210


def has_root(e: int, c: int, a: int, modulus: int = MODULUS) -> bool:
    return any((r * r + e * r + c - e * a) % modulus == 0 for r in range(modulus))


def allowed_quotients(c: int, a: int) -> tuple[int, ...]:
    return tuple(e for e in QUOTIENTS if has_root(e, c, a))


def admissible_a_residues() -> tuple[int, ...]:
    return tuple(a for a in range(MODULUS) if a % 30 in (12, 18))


def permutation_survives(a: int, perm: tuple[int, ...]) -> bool:
    return all(has_root(e, c, a) for c, e in zip(OFFSETS, perm))


def main() -> int:
    survivors: list[tuple[int, tuple[int, ...]]] = []
    for a in admissible_a_residues():
        row = {c: allowed_quotients(c, a) for c in OFFSETS}
        print(f"A={a:3d} " + " ".join(f"E_{c}={row[c]}" for c in OFFSETS))
        for perm in permutations(QUOTIENTS):
            if permutation_survives(a, perm):
                survivors.append((a, perm))

    if survivors:
        print("survivors:")
        for a, perm in survivors:
            print(a, perm)
        return 1

    print("certificate: no minimal energy assignment modulo 210")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
