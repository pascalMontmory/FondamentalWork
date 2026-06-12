#!/usr/bin/env python3
"""Lifted root-complex certificate at the shared-5 energy boundary 78.

The matching-complex certificate proves that energies <= 74 have no top
cell.  At energy 78, the graph-level matching complex is too coarse, so this
script builds the lifted root complex.

Vertices are triples (c,e,r) satisfying

    r^2 + e r + c - e A == 0 mod 2310

and the prime-label unit condition

    gcd(A-r, 2310) = 1.

A top cell is a choice of one lifted root for each offset, with distinct
quotients.  The script proves that modulo 2310 all energy-78 top cells lie
above one projected pattern.
"""

from __future__ import annotations

from itertools import combinations, permutations
from math import gcd, prod


OFFSETS = (5, 17, 25, 49, 65)
MODULUS = 2310
ENERGY = 78


def quotient_sets() -> tuple[tuple[int, ...], ...]:
    values = tuple(2 + 4 * k for k in range(ENERGY // 4 + 2))
    return tuple(q for q in combinations(values, 5) if sum(q) == ENERGY)


def admissible_a_residues() -> tuple[int, ...]:
    return tuple(a for a in range(MODULUS) if a % 30 in (12, 18))


def lifted_roots(e: int, c: int, a: int) -> tuple[int, ...]:
    return tuple(
        r
        for r in range(MODULUS)
        if (r * r + e * r + c - e * a) % MODULUS == 0
        and gcd(a - r, MODULUS) == 1
    )


def main() -> int:
    survivors: list[tuple[tuple[int, ...], int, tuple[int, ...], tuple[int, ...]]] = []

    for quotient_set in quotient_sets():
        for a in admissible_a_residues():
            root_table = {
                (c, e): lifted_roots(e, c, a)
                for c in OFFSETS
                for e in quotient_set
            }
            for assignment in permutations(quotient_set):
                root_counts = tuple(
                    len(root_table[(c, e)])
                    for c, e in zip(OFFSETS, assignment)
                )
                if all(root_counts):
                    survivors.append((quotient_set, a, assignment, root_counts))

    print(f"modulus={MODULUS}")
    print(f"energy={ENERGY}")
    print(f"quotient_sets={len(quotient_sets())}")
    print(f"projected_top_patterns={len(survivors)}")

    for quotient_set, a, assignment, root_counts in survivors:
        print(f"Q={quotient_set}")
        print(f"A={a}")
        print(f"assignment={dict(zip(OFFSETS, assignment))}")
        print(f"lifted_root_counts={dict(zip(OFFSETS, root_counts))}")
        print(f"lifted_top_cells={prod(root_counts)}")

    expected = [
        ((2, 6, 10, 18, 42), 882, (42, 18, 10, 2, 6), (8, 8, 2, 2, 4))
    ]
    if survivors != expected:
        print("certificate mismatch")
        return 1

    print("certificate: one projected lifted-root top pattern remains at energy 78")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
