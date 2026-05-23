#!/usr/bin/env python3
"""Compute Collatz terminal entrance measures and projection checks.

This is a finite diagnostic script.  It verifies the exact projectivity identity
on computed samples:

    nu_{B_low,F,N} = (delta_{B_low,B_high})_# nu_{B_high,F,N}.

It does not prove convergence as N -> infinity and it does not assume global
Collatz convergence.  Values that do not enter within max_steps are recorded
as "inf".
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
from typing import Iterable

INF = "inf"


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def terminal_entry(n: int, bound: int, max_steps: int) -> int | None:
    current = n
    for _ in range(max_steps + 1):
        if current <= bound:
            return current
        current = step(current)
    return None


def sieve(limit: int) -> bytearray:
    is_prime = bytearray(b"\x01") * (limit + 3)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int((limit + 2) ** 0.5) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 3 : p] = b"\x00" * (((limit + 2 - start) // p) + 1)
    return is_prime


def population(limit: int, family: str, mod_q: int, mod_a: int) -> list[int]:
    if family == "all":
        return list(range(1, limit + 1))
    if family == "odd":
        return list(range(1, limit + 1, 2))
    if family == "mod-class":
        if mod_q <= 0:
            raise ValueError("--mod-q must be positive for mod-class")
        return [n for n in range(1, limit + 1) if n % mod_q == mod_a % mod_q]

    primes = sieve(limit + 2)
    if family == "prime":
        return [n for n in range(2, limit + 1) if primes[n]]
    if family == "twin-prime-start":
        return [n for n in range(2, limit + 1) if primes[n] and primes[n + 2]]
    if family == "prime-non-twin":
        return [n for n in range(2, limit + 1) if primes[n] and not primes[n + 2]]
    raise ValueError(f"unknown family: {family}")


def terminal_counts(items: Iterable[int], bound: int, max_steps: int) -> Counter[str]:
    counts: Counter[str] = Counter()
    for n in items:
        entry = terminal_entry(n, bound, max_steps)
        counts[str(entry) if entry is not None else INF] += 1
    return counts


def law(counts: Counter[str], total: int) -> dict[str, float]:
    if total == 0:
        return {}
    return {state: count / total for state, count in counts.items()}


def tv_distance(left: dict[str, float], right: dict[str, float]) -> float:
    keys = set(left) | set(right)
    return 0.5 * sum(abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in keys)


def project_state(state: str, low_bound: int, max_steps: int) -> str:
    if state == INF:
        return INF
    entry = terminal_entry(int(state), low_bound, max_steps)
    return str(entry) if entry is not None else INF


def project_law(high_law: dict[str, float], low_bound: int, max_steps: int) -> dict[str, float]:
    out: Counter[str] = Counter()
    for state, probability in high_law.items():
        out[project_state(state, low_bound, max_steps)] += probability
    return dict(out)


def parse_bounds(raw: str) -> list[int]:
    bounds = sorted({int(part) for part in raw.split(",") if part.strip()})
    if not bounds:
        raise ValueError("at least one bound is required")
    return bounds


def parse_families(raw: str) -> list[str]:
    families = [part.strip() for part in raw.split(",") if part.strip()]
    if not families:
        raise ValueError("at least one family is required")
    return families


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--bounds", default="27,89")
    parser.add_argument("--families", default="all,odd,prime,twin-prime-start,prime-non-twin")
    parser.add_argument("--mod-q", type=int, default=3)
    parser.add_argument("--mod-a", type=int, default=1)
    parser.add_argument("--max-steps", type=int, default=10_000)
    parser.add_argument("--projection-check", action="store_true")
    parser.add_argument("--pairwise-tv", action="store_true")
    args = parser.parse_args()

    bounds = parse_bounds(args.bounds)
    families = parse_families(args.families)
    laws_by_family: dict[tuple[str, int], dict[str, float]] = {}

    print("kind,family,B,N,state,count,probability,B_high,B_low,tv_error,verdict")
    for family in families:
        items = population(args.limit, family, args.mod_q, args.mod_a)
        laws: dict[int, dict[str, float]] = {}
        for bound in bounds:
            counts = terminal_counts(items, bound, args.max_steps)
            laws[bound] = law(counts, len(items))
            laws_by_family[(family, bound)] = laws[bound]
            for state in sorted(counts, key=lambda value: (value == INF, int(value) if value != INF else 10**18)):
                probability = counts[state] / len(items) if items else float("nan")
                print(
                    f"law,{family},{bound},{len(items)},{state},{counts[state]},"
                    f"{probability:.17g},,,,"
                )

        if args.projection_check and len(bounds) > 1:
            for i, low in enumerate(bounds):
                for high in bounds[i + 1 :]:
                    projected = project_law(laws[high], low, args.max_steps)
                    error = tv_distance(laws[low], projected)
                    verdict = "ok" if error <= 1e-15 else "fail"
                    print(
                        f"projection,{family},,{len(items)},,,,{high},{low},"
                        f"{error:.17g},{verdict}"
                    )

    if args.pairwise_tv and len(families) > 1:
        for bound in bounds:
            for left, right in combinations(families, 2):
                error = tv_distance(laws_by_family[(left, bound)], laws_by_family[(right, bound)])
                print(
                    f"tv,{left}|{right},{bound},,,,,,,"
                    f"{error:.17g},diagnostic"
                )


if __name__ == "__main__":
    main()
