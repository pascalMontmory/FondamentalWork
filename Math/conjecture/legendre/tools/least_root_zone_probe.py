#!/usr/bin/env python3
"""Probe the least-root zone decomposition for the Legendre A-block gate.

This is exploratory.  It measures the exact objects defined in the notes:

* low labels p <= B_m;
* middle labels B_m < p <= C_m;
* high labels C_m < p <= A, encoded by least square roots;
* high-high shift adjacencies and mixed high/low-neighbor cells.

It does not prove Legendre.  Its purpose is to expose the size and overlap
of the remaining exact non-cover components.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from math import gcd, isqrt


ZoneSet = frozenset[str]


@dataclass(frozen=True)
class BlockData:
    q: int
    t0: int
    t1: int
    z0: ZoneSet
    z1: ZoneSet


@dataclass(frozen=True)
class MStats:
    m: int
    complete_cop_blocks: int
    both_layers_covered: int
    a0_uncovered: int
    a1_uncovered: int
    high_high: int
    mixed_high_low_or_mid: int
    low_low_possible: int
    middle_involved: int
    priority_cells: Counter[tuple[str, str]]
    all_cells: Counter[tuple[str, str]]
    high_a0_roots: int
    high_a1_roots: int
    high_a0_primes: int
    high_a1_primes: int
    b_cutoff: int
    c_cutoff: int
    q_star: int
    t_bound: int


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def legendre_symbol(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def sqrt_mod_prime(a: int, p: int) -> int | None:
    """Return one square root of a modulo odd prime p, or None."""
    a %= p
    if a == 0:
        return 0
    if p == 2:
        return a
    if legendre_symbol(a, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q //= 2

    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    while t != 1:
        i = 1
        t2i = (t * t) % p
        while t2i != 1:
            t2i = (t2i * t2i) % p
            i += 1
            if i >= m:
                return None
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p
    return r


def least_abs_residue(x: int, p: int) -> int:
    r = x % p
    return min(r, p - r)


def q_star(m: int) -> int:
    return max(-1, (isqrt(6 * m) - 2) // 3)


def block_coordinates(m: int, q: int) -> tuple[int, int]:
    a = 3 * q + 1
    b = 3 * q + 2
    if q % 2 == m % 2:
        return a, b  # t0, t1
    return b, a


def complete_coprime_blocks(m: int) -> list[tuple[int, int, int]]:
    a_center = 3 * m
    out: list[tuple[int, int, int]] = []
    for q in range(q_star(m) + 1):
        t0, t1 = block_coordinates(m, q)
        if t0 * t0 <= 6 * m and t1 * t1 + 1 <= 6 * m:
            if gcd(t1, a_center * a_center + 1) == 1:
                out.append((q, t0, t1))
    return out


def high_root_sets(m: int, primes: list[int]) -> tuple[set[int], set[int], int, int]:
    a_center = 3 * m
    t_bound = isqrt(6 * m)
    c_cutoff = 2 * t_bound
    r0: set[int] = set()
    r1: set[int] = set()
    p0_count = 0
    p1_count = 0

    for p in primes:
        if p <= c_cutoff:
            continue
        if p > a_center:
            break

        if p % 4 == 1 and a_center % p != 0:
            root_i = sqrt_mod_prime(-1, p)
            if root_i is not None:
                t = least_abs_residue(a_center * root_i, p)
                if 1 <= t <= t_bound:
                    r0.add(t)
                    p0_count += 1

        if (a_center * a_center + 1) % p != 0:
            root_s = sqrt_mod_prime(-(a_center * a_center + 1), p)
            if root_s is not None:
                t = least_abs_residue(root_s, p)
                if 1 <= t <= t_bound:
                    r1.add(t)
                    p1_count += 1

    return r0, r1, p0_count, p1_count


def low_middle_zones(m: int, t: int, layer: int, primes: list[int]) -> set[str]:
    a_center = 3 * m
    t_bound = isqrt(6 * m)
    b_cutoff = 6 * q_star(m) + 4
    c_cutoff = 2 * t_bound
    value = a_center * a_center + t * t + (1 if layer == 1 else 0)
    zones: set[str] = set()

    for p in primes:
        if p < 5:
            continue
        if p > c_cutoff:
            break
        if layer == 0:
            if p % 4 != 1 or a_center % p == 0:
                continue
        else:
            if (a_center * a_center + 1) % p == 0:
                continue
        if value % p == 0:
            zones.add("L" if p <= b_cutoff else "M")
    return zones


def priority(zones: ZoneSet) -> str:
    for z in ("L", "M", "H"):
        if z in zones:
            return z
    return "-"


def analyze_m(m: int, primes: list[int]) -> MStats:
    t_bound = isqrt(6 * m)
    b_cutoff = 6 * q_star(m) + 4
    c_cutoff = 2 * t_bound
    r0_hi, r1_hi, p0_hi, p1_hi = high_root_sets(m, primes)
    priority_cells: Counter[tuple[str, str]] = Counter()
    all_cells: Counter[tuple[str, str]] = Counter()
    high_high = 0
    mixed = 0
    low_low = 0
    middle_involved = 0
    both = 0
    a0_uncovered = 0
    a1_uncovered = 0

    for q, t0, t1 in complete_coprime_blocks(m):
        z0 = set(low_middle_zones(m, t0, 0, primes))
        z1 = set(low_middle_zones(m, t1, 1, primes))
        if t0 in r0_hi:
            z0.add("H")
        if t1 in r1_hi:
            z1.add("H")
        fz0 = frozenset(z0)
        fz1 = frozenset(z1)
        if not fz0:
            a0_uncovered += 1
        if not fz1:
            a1_uncovered += 1
        if fz0 and fz1:
            both += 1
        if "H" in fz0 and "H" in fz1:
            high_high += 1
        if ("H" in fz0 and (("L" in fz1) or ("M" in fz1))) or (
            "H" in fz1 and (("L" in fz0) or ("M" in fz0))
        ):
            mixed += 1
        if "L" in fz0 and "L" in fz1:
            low_low += 1
        if "M" in fz0 or "M" in fz1:
            middle_involved += 1

        priority_cells[(priority(fz0), priority(fz1))] += 1
        for x in fz0 or frozenset({"-"}):
            for y in fz1 or frozenset({"-"}):
                all_cells[(x, y)] += 1

    return MStats(
        m=m,
        complete_cop_blocks=len(complete_coprime_blocks(m)),
        both_layers_covered=both,
        a0_uncovered=a0_uncovered,
        a1_uncovered=a1_uncovered,
        high_high=high_high,
        mixed_high_low_or_mid=mixed,
        low_low_possible=low_low,
        middle_involved=middle_involved,
        priority_cells=priority_cells,
        all_cells=all_cells,
        high_a0_roots=len(r0_hi),
        high_a1_roots=len(r1_hi),
        high_a0_primes=p0_hi,
        high_a1_primes=p1_hi,
        b_cutoff=b_cutoff,
        c_cutoff=c_cutoff,
        q_star=q_star(m),
        t_bound=t_bound,
    )


def fmt_counter(counter: Counter[tuple[str, str]]) -> str:
    keys = [
        ("L", "L"),
        ("L", "M"),
        ("L", "H"),
        ("M", "L"),
        ("M", "M"),
        ("M", "H"),
        ("H", "L"),
        ("H", "M"),
        ("H", "H"),
        ("-", "L"),
        ("L", "-"),
        ("-", "-"),
    ]
    parts = [f"{a}{b}:{counter[(a, b)]}" for a, b in keys if counter[(a, b)]]
    return " ".join(parts) if parts else "none"


def print_stats(stats: MStats, verbose: bool) -> None:
    print(
        f"m={stats.m} Q*={stats.q_star} T={stats.t_bound} "
        f"B={stats.b_cutoff} C={stats.c_cutoff} cop={stats.complete_cop_blocks} "
        f"covered={stats.both_layers_covered} a0_open={stats.a0_uncovered} "
        f"a1_open={stats.a1_uncovered} lowlow={stats.low_low_possible} "
        f"mixed={stats.mixed_high_low_or_mid} hihi={stats.high_high} "
        f"mid={stats.middle_involved} R0hi={stats.high_a0_roots}/{stats.high_a0_primes} "
        f"R1hi={stats.high_a1_roots}/{stats.high_a1_primes}"
    )
    if verbose:
        print(f"  priority_cells {fmt_counter(stats.priority_cells)}")
        print(f"  all_cells      {fmt_counter(stats.all_cells)}")


def run(args: argparse.Namespace) -> int:
    todo: list[int] = []
    if args.m:
        todo.extend(args.m)
    if args.start is not None and args.end is not None:
        todo.extend(range(args.start, args.end + 1, args.step))
    if not todo:
        todo = [100, 1_000, 10_000]

    primes = primes_upto(3 * max(todo))

    worst_high_high: MStats | None = None
    worst_open: MStats | None = None
    for m in todo:
        stats = analyze_m(m, primes)
        print_stats(stats, args.verbose)
        if worst_high_high is None or stats.high_high > worst_high_high.high_high:
            worst_high_high = stats
        open_layers = stats.a0_uncovered + stats.a1_uncovered
        if worst_open is None or open_layers > worst_open.a0_uncovered + worst_open.a1_uncovered:
            worst_open = stats

    if len(todo) > 1:
        print("summary:")
        if worst_high_high is not None:
            print(
                f"  max_high_high m={worst_high_high.m} "
                f"hihi={worst_high_high.high_high}"
            )
        if worst_open is not None:
            print(
                f"  max_layer_open m={worst_open.m} "
                f"a0_open={worst_open.a0_uncovered} a1_open={worst_open.a1_uncovered}"
            )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, action="append", help="Specific m to inspect.")
    parser.add_argument("--start", type=int, help="Range start for m.")
    parser.add_argument("--end", type=int, help="Range end for m.")
    parser.add_argument("--step", type=int, default=1)
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def main() -> None:
    raise SystemExit(run(parse_args()))


if __name__ == "__main__":
    main()
