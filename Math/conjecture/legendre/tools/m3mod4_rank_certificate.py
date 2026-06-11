#!/usr/bin/env python3
"""Exact finite certificates for the hard m == 3 mod 4 rank game.

This is not a search over Legendre intervals.  For each rank family
F(a,b,c), it builds all layer-respecting assignments and checks the exact
local sets

    M_l(c,f) = {m mod l : f^2 + 6*m*f - c is a square mod l}.

If the common intersection is empty for some l, that prime is a certificate
that the family has no integral point in the reduced Pell system.
"""

from __future__ import annotations

import argparse
from itertools import permutations
from typing import Iterable


A04_OFFSETS = (4, 100)
A00_OFFSETS = (16, 64)
A1_OFFSETS = (2, 26, 50, 122)
PRIMES = (5, 7, 11, 13, 17)
PERIODIC_PRIMES = (5, 7, 11, 13, 17, 83)
PREFIX_PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 83)


def layer_values(limit: int) -> tuple[list[int], list[int], list[int]]:
    a04: list[int] = []
    for n in range(1, 100000):
        if n % 24 in (2, 4, 10, 20):
            a04.append(n)
            if len(a04) >= limit + 8:
                break

    a00: list[int] = []
    for n in range(1, 200000):
        if n % 24 in (8, 14, 16, 22) and n % 7 != 0:
            a00.append(n)
            if len(a00) >= limit + 8:
                break

    a1 = [9 + 12 * i for i in range(limit + 8)]
    return a04, a00, a1


def squares_mod(p: int) -> set[int]:
    return {x * x % p for x in range(p)}


def allowed_m(c: int, f: int, p: int) -> set[int]:
    sq = squares_mod(p)
    return {m for m in range(p) if (f * f + 6 * m * f - c) % p in sq}


def periodic_values(kind: str, p: int) -> list[int]:
    """Residues of the variable rank slot over one period modulo p."""
    if kind == "a":
        values = []
        n = 1
        while len(values) < 4 * p:
            if n % 24 in (2, 4, 10, 20):
                values.append(n % p)
            n += 1
        return values

    if kind == "b":
        values = []
        n = 1
        period = 24 if p == 7 else 24 * p
        while len(values) < period:
            if n % 24 in (8, 14, 16, 22) and n % 7 != 0:
                values.append(n % p)
            n += 1
        return values

    if kind == "c":
        return [(45 + 12 * i) % p for i in range(p)]

    raise ValueError(f"unknown variable kind: {kind}")


def pattern_surviving_m(
    pattern: tuple[tuple[int, str], ...], p: int, fixed: dict[str, int]
) -> list[int]:
    sq = squares_mod(p)
    variable_values = {kind: periodic_values(kind, p) for kind in ("a", "b", "c")}
    surviving = []
    for m in range(p):
        ok = True
        for offset, label in pattern:
            if label in fixed:
                f = fixed[label]
                if (f * f + 6 * m * f - offset) % p not in sq:
                    ok = False
                    break
            else:
                values = variable_values[label]
                if not any((f * f + 6 * m * f - offset) % p in sq for f in values):
                    ok = False
                    break
        if ok:
            surviving.append(m)
    return surviving


def periodic_patterns() -> list[tuple[tuple[int, str], ...]]:
    patterns = []
    for p04 in permutations(("a0", "a")):
        for p00 in permutations(("b0", "b")):
            for p1 in permutations(("c0", "c1", "c2", "c")):
                pattern = (
                    tuple(zip(A04_OFFSETS, p04))
                    + tuple(zip(A00_OFFSETS, p00))
                    + tuple(zip(A1_OFFSETS, p1))
                )
                if any(label == "c1" and offset not in (26, 122) for offset, label in pattern):
                    continue
                patterns.append(pattern)
    return patterns


def verify_periodic_patterns() -> int:
    fixed = {"a0": 2, "b0": 8, "c0": 9, "c1": 21, "c2": 33}
    killer_counts: dict[str, int] = {}
    open_patterns = []

    for index, pattern in enumerate(periodic_patterns()):
        killer = None
        for p in PERIODIC_PRIMES:
            if not pattern_surviving_m(pattern, p, fixed):
                killer = p
                break
        if killer is None:
            open_patterns.append((index, pattern))
        else:
            key = str(killer)
            killer_counts[key] = killer_counts.get(key, 0) + 1

    ordered = " ".join(f"{key}:{killer_counts[key]}" for key in sorted(killer_counts))
    print(f"periodic-patterns total={len(periodic_patterns())} {ordered}")
    if open_patterns:
        print("OPEN", open_patterns)
        return 1
    print("certificate: all periodic boundary patterns closed")
    return 0


def row_mask(c: int, f: int, p: int) -> int:
    mask = 0
    sq = squares_mod(p)
    for m in range(p):
        if (f * f + 6 * m * f - c) % p in sq:
            mask |= 1 << m
    return mask


def verify_prefix_ranks(prefix: int) -> int:
    """Verify all arbitrary ordered assignments from the first prefix values."""
    a04, a00, a1 = layer_values(prefix + 10)
    a04 = a04[:prefix]
    a00 = a00[:prefix]
    a1 = a1[:prefix]

    def layer_assignments(offsets: tuple[int, ...], values: list[int]):
        rows = []
        for fs in permutations(values, len(offsets)):
            if any(f % 7 == 0 and offset not in (26, 122) for offset, f in zip(offsets, fs)):
                rows.append(("zero", None))
                continue
            masks = []
            for p in PREFIX_PRIMES:
                common = (1 << p) - 1
                for offset, f in zip(offsets, fs):
                    common &= row_mask(offset, f, p)
                masks.append(common)
            rows.append(("ok", tuple(masks)))
        return rows

    layer04 = layer_assignments(A04_OFFSETS, a04)
    layer00 = layer_assignments(A00_OFFSETS, a00)
    layer1 = layer_assignments(A1_OFFSETS, a1)

    killer_counts: dict[str, int] = {str(p): 0 for p in PREFIX_PRIMES}
    killer_counts["zero"] = 0
    total = 0

    for state04, masks04 in layer04:
        for state00, masks00 in layer00:
            zero_prefix = state04 == "zero" or state00 == "zero"
            for state1, masks1 in layer1:
                total += 1
                if zero_prefix or state1 == "zero":
                    killer_counts["zero"] += 1
                    continue

                for idx, p in enumerate(PREFIX_PRIMES):
                    common = masks04[idx] & masks00[idx] & masks1[idx]
                    if common == 0:
                        killer_counts[str(p)] += 1
                        break
                else:
                    print("OPEN prefix-rank assignment")
                    return 1

    ordered = " ".join(
        f"{key}:{killer_counts[key]}"
        for key in [str(p) for p in PREFIX_PRIMES] + ["zero"]
        if killer_counts[key]
    )
    print(f"prefix-ranks={prefix} total={total} {ordered}")
    print(f"certificate: all arbitrary assignments from first {prefix} ranks closed")
    return 0


def family_values(
    a: int, b: int, c: int, a04: list[int], a00: list[int], a1: list[int]
) -> tuple[list[int], list[int], list[int]]:
    return [a04[0], a04[1 + a]], [a00[0], a00[1 + b]], a1[:3] + [a1[3 + c]]


def assignments(
    a: int, b: int, c: int, a04: list[int], a00: list[int], a1: list[int]
) -> Iterable[tuple[tuple[int, int], ...]]:
    v04, v00, v1 = family_values(a, b, c, a04, a00, a1)
    for p04 in permutations(v04):
        for p00 in permutations(v00):
            for p1 in permutations(v1):
                ass = (
                    tuple(zip(A04_OFFSETS, p04))
                    + tuple(zip(A00_OFFSETS, p00))
                    + tuple(zip(A1_OFFSETS, p1))
                )
                if any(f % 7 == 0 and offset not in (26, 122) for offset, f in ass):
                    continue
                yield ass


def killing_prime(
    a: int, b: int, c: int, a04: list[int], a00: list[int], a1: list[int]
) -> str | int | None:
    survivors = list(assignments(a, b, c, a04, a00, a1))
    if not survivors:
        return "zero"

    for p in PRIMES:
        next_survivors = []
        for ass in survivors:
            common = set(range(p))
            for offset, f in ass:
                common &= allowed_m(offset, f, p)
            if common:
                next_survivors.append(ass)
        survivors = next_survivors
        if not survivors:
            return p
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-weight", type=int, default=30)
    parser.add_argument("--min-weight", type=int, default=0)
    parser.add_argument(
        "--periodic-patterns",
        action="store_true",
        help="verify all periodic boundary assignment patterns using 5,7,11,13,17,83",
    )
    parser.add_argument(
        "--prefix-ranks",
        type=int,
        help="verify all arbitrary ordered assignments using the first N ranks of each layer",
    )
    args = parser.parse_args()

    if args.periodic_patterns:
        return verify_periodic_patterns()

    if args.prefix_ranks is not None:
        return verify_prefix_ranks(args.prefix_ranks)

    a04, a00, a1 = layer_values(args.max_weight + 10)
    open_families = []

    for weight in range(args.min_weight, args.max_weight + 1):
        counts: dict[str, int] = {}
        total = 0
        for a in range(weight + 1):
            for b in range(weight + 1 - a):
                c = weight - a - b
                total += 1
                killer = killing_prime(a, b, c, a04, a00, a1)
                key = str(killer)
                counts[key] = counts.get(key, 0) + 1
                if killer is None:
                    open_families.append((a, b, c))
        ordered = " ".join(f"{key}:{counts[key]}" for key in sorted(counts))
        print(f"weight={weight} total={total} {ordered}")

    if open_families:
        print("OPEN", open_families)
        return 1

    print(f"certificate: all weights {args.min_weight}..{args.max_weight} closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
