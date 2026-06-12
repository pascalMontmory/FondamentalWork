#!/usr/bin/env python3
"""Verify the shared-5 low-energy modular certificate.

This is a finite certificate, not a Legendre witness search.

In the shared-5 fiber, the five variable quotients are distinct and
congruent to 2 modulo 4.  This script checks every possible quotient set
with total energy at most 74 and proves that none can satisfy the five
centered equations modulo 2310.
"""

from __future__ import annotations

from itertools import combinations, permutations


OFFSETS = (5, 17, 25, 49, 65)
MODULUS = 2310
ENERGY_BOUND = 74


def candidate_quotient_sets() -> tuple[tuple[int, ...], ...]:
    """All five-element subsets of 2 mod 4 with energy <= 74."""

    values = tuple(2 + 4 * k for k in range(ENERGY_BOUND // 4 + 2))
    return tuple(
        quotients
        for quotients in combinations(values, 5)
        if sum(quotients) <= ENERGY_BOUND
    )


def has_root(e: int, c: int, a: int, modulus: int = MODULUS) -> bool:
    """Return whether r^2 + e r + c - e A has a root modulo modulus."""

    return any((r * r + e * r + c - e * a) % modulus == 0 for r in range(modulus))


def admissible_a_residues(modulus: int = MODULUS) -> tuple[int, ...]:
    """Shared-5 residues A mod modulus."""

    return tuple(a for a in range(modulus) if a % 30 in (12, 18))


def build_root_table(
    quotient_sets: tuple[tuple[int, ...], ...],
    residues: tuple[int, ...],
) -> dict[tuple[int, int, int], bool]:
    quotients = sorted({e for quotient_set in quotient_sets for e in quotient_set})
    return {
        (e, c, a): has_root(e, c, a)
        for e in quotients
        for c in OFFSETS
        for a in residues
    }


def surviving_assignment(
    quotient_set: tuple[int, ...],
    a: int,
    root_table: dict[tuple[int, int, int], bool],
) -> tuple[int, ...] | None:
    for perm in permutations(quotient_set):
        if all(root_table[(e, c, a)] for c, e in zip(OFFSETS, perm)):
            return perm
    return None


def main() -> int:
    quotient_sets = candidate_quotient_sets()
    residues = admissible_a_residues()
    root_table = build_root_table(quotient_sets, residues)

    survivors: list[tuple[int, tuple[int, ...], int, tuple[int, ...]]] = []
    for quotient_set in sorted(quotient_sets, key=lambda q: (sum(q), q)):
        survived = False
        for a in residues:
            assignment = surviving_assignment(quotient_set, a, root_table)
            if assignment is not None:
                survivors.append((sum(quotient_set), quotient_set, a, assignment))
                survived = True
                break

        status = "SURVIVES" if survived else "KILLED"
        print(f"E={sum(quotient_set):2d} Q={quotient_set} {status}")

    if survivors:
        print("survivors:")
        for energy, quotient_set, a, assignment in survivors:
            print(f"E={energy} Q={quotient_set} A={a} assignment={assignment}")
        return 1

    print(
        "certificate: no shared-5 quotient assignment with total energy "
        f"<= {ENERGY_BOUND} modulo {MODULUS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
