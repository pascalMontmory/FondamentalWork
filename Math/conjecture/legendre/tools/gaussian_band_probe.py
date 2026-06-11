#!/usr/bin/env python3
"""Probe bounded bands around Gaussian square offsets.

For a fixed radius R, search for a prime in each Legendre interval of the form

    n^2 + t^2 + r,    |r| <= R.

This tests the empirical G_R candidate suggested by the failures of the strict
square-offset lemma.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class BandWitness:
    n: int
    t: int
    r: int
    offset: int
    value: int
    tried: int


@dataclass(frozen=True)
class BandFailure:
    n: int
    tried: int


def is_prime(value: int) -> bool:
    """Deterministic Miller-Rabin for values below 2^64."""
    if value < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if value % p == 0:
            return value == p

    d = value - 1
    shift = 0
    while d % 2 == 0:
        d //= 2
        shift += 1

    for base in small_primes:
        if base >= value:
            continue
        x = pow(base, d, value)
        if x in {1, value - 1}:
            continue
        for _ in range(shift - 1):
            x = (x * x) % value
            if x == value - 1:
                break
        else:
            return False
    return True


def candidate_offsets(n: int, radius: int):
    max_t = isqrt(2 * n) + 1
    for delta in range(radius + 1):
        offsets = [0] if delta == 0 else [-delta, delta]
        for t in range(1, max_t + 1):
            square = t * t
            for r in offsets:
                offset = square + r
                if 1 <= offset <= 2 * n:
                    yield t, r, offset


def probe_n(n: int, radius: int) -> BandWitness | BandFailure:
    tried = 0
    seen_offsets: set[int] = set()
    for t, r, offset in candidate_offsets(n, radius):
        if offset in seen_offsets:
            continue
        seen_offsets.add(offset)
        tried += 1
        value = n * n + offset
        if is_prime(value):
            return BandWitness(n=n, t=t, r=r, offset=offset, value=value, tried=tried)
    return BandFailure(n=n, tried=tried)


def run(limit: int, radius: int, show_failures: int, show_records: bool) -> int:
    failures: list[BandFailure] = []
    records: list[BandWitness] = []
    max_abs_r = 0
    max_t = 0
    max_tried = 0
    exact_square_count = 0
    r_histogram: dict[int, int] = {}

    for n in range(2, limit + 1):
        result = probe_n(n, radius)
        if isinstance(result, BandFailure):
            failures.append(result)
            if len(failures) <= show_failures:
                print(f"failure n={result.n}, tried={result.tried}")
            continue

        exact_square_count += int(result.r == 0)
        r_histogram[result.r] = r_histogram.get(result.r, 0) + 1
        if abs(result.r) > max_abs_r or result.t > max_t or result.tried > max_tried:
            records.append(result)
            max_abs_r = max(max_abs_r, abs(result.r))
            max_t = max(max_t, result.t)
            max_tried = max(max_tried, result.tried)

    print(f"checked n=2..{limit}")
    print(f"radius={radius}")
    print(f"failures={len(failures)}")
    print(f"exact_square_witnesses={exact_square_count}/{max(0, limit - 1)}")
    print(f"max_abs_r_used={max_abs_r}")
    print(f"max_t_used={max_t}")
    print(f"max_candidates_tried_before_witness={max_tried}")
    print("r_histogram:")
    for r in sorted(r_histogram):
        print(f"  {r}: {r_histogram[r]}")

    if show_records:
        print("records:")
        for item in records:
            bound = isqrt(2 * item.n) + 1
            print(
                f"  n={item.n}, t={item.t}, r={item.r}, offset={item.offset}, "
                f"bound={bound}, tried={item.tried}, value={item.value}"
            )

    return 1 if failures else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--radius", type=int, default=5)
    parser.add_argument("--show-failures", type=int, default=20)
    parser.add_argument("--records", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raise SystemExit(run(args.limit, args.radius, args.show_failures, args.records))


if __name__ == "__main__":
    main()
