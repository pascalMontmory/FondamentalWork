#!/usr/bin/env python3
"""Topological matching-complex certificate for the shared-5 low layers.

This tool does not search for primes.  It builds the finite arithmetic
incidence tensor

    T_A,Q(c,e) = 1  iff  exists r mod 2310:
        r^2 + e r + c - e A == 0 mod 2310.

For a fixed residue A and quotient set Q, a compressed obstruction in that
layer would be a perfect matching in this bipartite incidence graph.  Equivalently,
it would be a top-dimensional simplex in the matching complex M(T_A,Q), or a
nonzero permanent of T_A,Q.

The script verifies that, for all shared-5 quotient sets with energy <= 74,
every matching complex has no top cell.  It also records a Hall-defect witness,
which is the finite topological collapse certificate for the missing top cell.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations


OFFSETS = (5, 17, 25, 49, 65)
MODULUS = 2310
ENERGY_BOUND = 74


Edge = tuple[int, int]
HallDefect = tuple[tuple[int, ...], tuple[int, ...], int]


def candidate_quotient_sets() -> tuple[tuple[int, ...], ...]:
    values = tuple(2 + 4 * k for k in range(ENERGY_BOUND // 4 + 2))
    return tuple(q for q in combinations(values, 5) if sum(q) <= ENERGY_BOUND)


def admissible_a_residues() -> tuple[int, ...]:
    return tuple(a for a in range(MODULUS) if a % 30 in (12, 18))


def has_root(e: int, c: int, a: int) -> bool:
    return any((r * r + e * r + c - e * a) % MODULUS == 0 for r in range(MODULUS))


def root_table(
    quotient_sets: tuple[tuple[int, ...], ...],
    residues: tuple[int, ...],
) -> dict[tuple[int, int, int], bool]:
    quotients = sorted({e for q in quotient_sets for e in q})
    return {
        (c, e, a): has_root(e, c, a)
        for c in OFFSETS
        for e in quotients
        for a in residues
    }


def incidence_edges(
    quotient_set: tuple[int, ...],
    a: int,
    table: dict[tuple[int, int, int], bool],
) -> frozenset[Edge]:
    return frozenset(
        (c, e)
        for c in OFFSETS
        for e in quotient_set
        if table[(c, e, a)]
    )


def matching_count(edges: frozenset[Edge], quotient_set: tuple[int, ...], size: int) -> int:
    count = 0
    for left_subset in combinations(OFFSETS, size):
        for right_subset in combinations(quotient_set, size):
            for perm in permutations(right_subset):
                if all((c, e) in edges for c, e in zip(left_subset, perm)):
                    count += 1
    return count


def f_vector(edges: frozenset[Edge], quotient_set: tuple[int, ...]) -> tuple[int, ...]:
    """Return f_k = number of k-edge matchings for k=0..5."""

    return tuple(matching_count(edges, quotient_set, size) for size in range(6))


def permanent(edges: frozenset[Edge], quotient_set: tuple[int, ...]) -> int:
    """Permanent of the 5x5 incidence tensor."""

    return matching_count(edges, quotient_set, 5)


def hall_defect(edges: frozenset[Edge], quotient_set: tuple[int, ...]) -> HallDefect | None:
    """Return a Hall defect S, N(S), |S|-|N(S)| if one exists."""

    for size in range(1, len(OFFSETS) + 1):
        for subset in combinations(OFFSETS, size):
            neighbors = tuple(
                e for e in quotient_set if any((c, e) in edges for c in subset)
            )
            defect = len(subset) - len(neighbors)
            if defect > 0:
                return subset, neighbors, defect
    return None


def main() -> int:
    quotient_sets = candidate_quotient_sets()
    residues = admissible_a_residues()
    table = root_table(quotient_sets, residues)

    checked = 0
    nonzero_permanents: list[tuple[tuple[int, ...], int, int]] = []
    max_matching_hist = Counter()
    defect_hist = Counter()
    sample_defects: dict[int, tuple[tuple[int, ...], int, HallDefect, tuple[int, ...]]] = {}

    for quotient_set in sorted(quotient_sets, key=lambda q: (sum(q), q)):
        for a in residues:
            checked += 1
            edges = incidence_edges(quotient_set, a, table)
            f_vec = f_vector(edges, quotient_set)
            top_cells = f_vec[5]
            if top_cells:
                nonzero_permanents.append((quotient_set, a, top_cells))

            max_matching_size = max(i for i, count in enumerate(f_vec) if count)
            max_matching_hist[max_matching_size] += 1

            defect = hall_defect(edges, quotient_set)
            if defect is None:
                defect_hist[0] += 1
            else:
                defect_hist[defect[2]] += 1
                sample_defects.setdefault(
                    defect[2], (quotient_set, a, defect, f_vec)
                )

    print(f"modulus={MODULUS}")
    print(f"energy_bound={ENERGY_BOUND}")
    print(f"quotient_sets={len(quotient_sets)}")
    print(f"admissible_A_residues={len(residues)}")
    print(f"matching_complexes_checked={checked}")
    print(f"max_matching_size_hist={dict(sorted(max_matching_hist.items()))}")
    print(f"hall_defect_hist={dict(sorted(defect_hist.items()))}")

    for defect, (quotient_set, a, witness, f_vec) in sorted(sample_defects.items()):
        subset, neighbors, amount = witness
        print(
            "sample_defect "
            f"delta={defect} Q={quotient_set} A={a} "
            f"S={subset} N(S)={neighbors} f={f_vec}"
        )
        assert defect == amount

    if nonzero_permanents:
        print("nonzero permanents:")
        for quotient_set, a, top_cells in nonzero_permanents[:20]:
            print(f"Q={quotient_set} A={a} permanent={top_cells}")
        return 1

    print("certificate: every low-energy matching complex has no top cell")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
