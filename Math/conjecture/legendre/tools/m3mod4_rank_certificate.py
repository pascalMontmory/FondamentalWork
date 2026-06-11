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
    args = parser.parse_args()

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
