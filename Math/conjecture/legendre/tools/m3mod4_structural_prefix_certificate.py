#!/usr/bin/env python3
"""Exact structural-prefix certificates for the hard m == 3 mod 4 branch.

This verifier uses the offset-specific multiplicative quotient sets obtained
after the A0/A1 self-residue and dual-factor collapses.  It is not a search
over Legendre intervals.  It checks finite congruence certificates for fixed
structural quotient prefixes.
"""

from __future__ import annotations

import argparse
from itertools import product


OFFSETS = (4, 100, 16, 64, 2, 26, 50, 122)
PRIMES = (
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
)


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def legendre_symbol(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def in_s4(n: int) -> bool:
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(q % 4 == 1 for q in factor(n))


def a0_values(c: int, count: int) -> list[int]:
    values: list[int] = []
    n = 1
    while len(values) < count:
        if c in (4, 100):
            ok = n % 2 == 0 and in_s4(n // 2)
        elif c == 16:
            ok = (n % 8 == 0 and in_s4(n // 8)) or (
                n % 16 == 0 and in_s4(n // 16)
            )
        elif c == 64:
            ok = (
                (n % 8 == 0 and in_s4(n // 8))
                or (n % 32 == 0 and in_s4(n // 32))
                or (n % 64 == 0 and in_s4(n // 64))
            )
        else:
            raise ValueError(c)
        if ok:
            values.append(n)
        n += 1
    return values


def a1_allowed(c: int, f: int) -> bool:
    if f % 12 != 9:
        return False
    for q, alpha in factor(f).items():
        gamma = 0
        reduced_c = c
        while reduced_c % q == 0:
            gamma += 1
            reduced_c //= q
        if gamma == 0:
            if legendre_symbol(-c, q) != 1:
                return False
        elif alpha > gamma:
            if gamma % 2:
                return False
            if legendre_symbol(-reduced_c, q) != 1:
                return False
    return True


def a1_values(c: int, count: int) -> list[int]:
    values: list[int] = []
    n = 9
    while len(values) < count:
        if a1_allowed(c, n):
            values.append(n)
        n += 12
    return values


def squares_mod(p: int) -> set[int]:
    return {x * x % p for x in range(p)}


def row_mask(c: int, f: int, p: int) -> int:
    mask = 0
    sq = squares_mod(p)
    for m in range(p):
        if (f * f + 6 * m * f - c) % p in sq:
            mask |= 1 << m
    return mask


def structural_values(prefix: int) -> dict[int, list[int]]:
    return {
        c: (a0_values(c, prefix) if c in (4, 100, 16, 64) else a1_values(c, prefix))
        for c in OFFSETS
    }


def verify_prefix(prefix: int) -> tuple[int, list[tuple[tuple[int, int], ...]]]:
    values = structural_values(prefix)
    masks = {
        (c, f, p): row_mask(c, f, p)
        for c in OFFSETS
        for f in values[c]
        for p in PRIMES
    }
    total = 0
    non_distinct = 0
    open_assignments: list[tuple[tuple[int, int], ...]] = []
    killer_counts: dict[int, int] = {p: 0 for p in PRIMES}

    for fs in product(*(values[c] for c in OFFSETS)):
        if len(set(fs)) < len(fs):
            non_distinct += 1
            continue
        total += 1
        assignment = tuple(zip(OFFSETS, fs))
        for p in PRIMES:
            common = (1 << p) - 1
            for c, f in assignment:
                common &= masks[(c, f, p)]
            if common == 0:
                killer_counts[p] += 1
                break
        else:
            open_assignments.append(assignment)

    print(f"prefix={prefix}")
    print("values=" + repr(values))
    print(f"total_distinct={total} non_distinct={non_distinct}")
    print(
        "killers="
        + " ".join(f"{p}:{killer_counts[p]}" for p in PRIMES if killer_counts[p])
    )
    if open_assignments:
        print(f"open={len(open_assignments)}")
        for assignment in open_assignments:
            print("OPEN " + repr(assignment))
    else:
        print("certificate: structural prefix closed by finite local sets")
    return total, open_assignments


def verify_ghost_closure(open_assignments: list[tuple[tuple[int, int], ...]]) -> bool:
    ghost_assignments = {
        (
            (4, 10),
            (100, 58),
            (16, 8),
            (64, 40),
            (2, 9),
            (26, 21),
            (50, 33),
            (122, 69),
        ),
        (
            (4, 10),
            (100, 58),
            (16, 16),
            (64, 40),
            (2, 9),
            (26, 21),
            (50, 33),
            (122, 69),
        ),
    }
    if set(open_assignments) != ghost_assignments:
        return False

    print("ghost-fibers: exactly the two m=-1 assignments")
    print("closure: positive integral points are impossible")
    print("case c=16,f=8: m=12n^2-1, then X^2=20n^2+1 and Y^2=20n^2+9")
    print("case c=16,f=16: 3X^2=5m+8 and 3Y^2=5m+32")
    print("both cases force Y^2-X^2=8, hence X=1,Y=3 and m=-1")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", type=int, default=6)
    parser.add_argument("--close-ghosts", action="store_true")
    args = parser.parse_args()

    _, open_assignments = verify_prefix(args.prefix)
    if not open_assignments:
        return 0
    if args.close_ghosts and verify_ghost_closure(open_assignments):
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
