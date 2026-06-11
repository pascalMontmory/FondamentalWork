#!/usr/bin/env python3
"""Analyze failures of the strict Gaussian square-offset lemma.

For every n where the strict square-offset probe fails, find the first prime
in (n^2, (n+1)^2), then measure how far its offset is from a square.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt

from gaussian_lemma_g_probe import Failure, Witness, is_prime, primes_upto, probe_n


@dataclass(frozen=True)
class FailureAnalysis:
    n: int
    first_prime: int
    offset: int
    lower_square_t: int
    lower_square: int
    lower_r: int
    nearest_square_t: int
    nearest_square: int
    nearest_r: int
    strict_candidates: int


def first_prime_offset(n: int, primes: list[int]) -> tuple[int, int]:
    start = n * n + 1
    stop = (n + 1) * (n + 1)
    for value in range(start, stop):
        if is_prime(value, primes):
            return value, value - n * n
    raise RuntimeError(f"Legendre interval has no prime for n={n}")


def square_decomposition(offset: int) -> tuple[int, int, int, int, int, int]:
    lower_t = isqrt(offset)
    lower_square = lower_t * lower_t
    lower_r = offset - lower_square

    upper_t = lower_t + 1
    upper_square = upper_t * upper_t
    upper_r = offset - upper_square

    if abs(upper_r) < abs(lower_r):
        return lower_t, lower_square, lower_r, upper_t, upper_square, upper_r
    return lower_t, lower_square, lower_r, lower_t, lower_square, lower_r


def analyze_failure(n: int, primes: list[int], strict_candidates: int) -> FailureAnalysis:
    prime, offset = first_prime_offset(n, primes)
    lower_t, lower_square, lower_r, nearest_t, nearest_square, nearest_r = square_decomposition(
        offset
    )
    return FailureAnalysis(
        n=n,
        first_prime=prime,
        offset=offset,
        lower_square_t=lower_t,
        lower_square=lower_square,
        lower_r=lower_r,
        nearest_square_t=nearest_t,
        nearest_square=nearest_square,
        nearest_r=nearest_r,
        strict_candidates=strict_candidates,
    )


def collect(limit: int) -> list[FailureAnalysis]:
    primes = primes_upto(limit + 1)
    analyses = []
    for n in range(2, limit + 1):
        result = probe_n(n, primes)
        if isinstance(result, Witness):
            continue
        if not isinstance(result, Failure):
            raise TypeError(result)
        analyses.append(analyze_failure(n, primes, result.primitive_candidates))
    return analyses


def print_table(analyses: list[FailureAnalysis]) -> None:
    print(
        "n,first_prime,offset,lower_square_t,lower_square,lower_r,"
        "nearest_square_t,nearest_square,nearest_r,strict_candidates"
    )
    for item in analyses:
        print(
            f"{item.n},{item.first_prime},{item.offset},"
            f"{item.lower_square_t},{item.lower_square},{item.lower_r},"
            f"{item.nearest_square_t},{item.nearest_square},{item.nearest_r},"
            f"{item.strict_candidates}"
        )


def print_summary(analyses: list[FailureAnalysis], limit: int) -> None:
    if not analyses:
        print(f"no strict Gaussian failures up to {limit}")
        return

    max_abs_nearest_r = max(abs(item.nearest_r) for item in analyses)
    max_lower_r = max(item.lower_r for item in analyses)
    exact_square_count = sum(1 for item in analyses if item.nearest_r == 0)
    by_abs_r: dict[int, int] = {}
    for item in analyses:
        by_abs_r[abs(item.nearest_r)] = by_abs_r.get(abs(item.nearest_r), 0) + 1

    print(f"analyzed_failures={len(analyses)}")
    print(f"first_failure_n={analyses[0].n}")
    print(f"last_failure_n={analyses[-1].n}")
    print(f"max_abs_nearest_r={max_abs_nearest_r}")
    print(f"max_lower_r={max_lower_r}")
    print(f"exact_square_offsets={exact_square_count}")
    print("abs_nearest_r_histogram:")
    for radius in sorted(by_abs_r):
        print(f"  {radius}: {by_abs_r[radius]}")

    for radius in [1, 2, 4, 8, 16, 32, 64]:
        covered = sum(1 for item in analyses if abs(item.nearest_r) <= radius)
        print(f"covered_by_nearest_square_band_{radius}={covered}/{len(analyses)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--table", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    analyses = collect(args.limit)
    print_summary(analyses, args.limit)
    if args.table:
        print_table(analyses)


if __name__ == "__main__":
    main()
