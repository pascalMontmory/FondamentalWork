#!/usr/bin/env python3
"""Analyze cases repaired by bounded corrections to square offsets."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from gaussian_band_probe import BandFailure, BandWitness, probe_n
from gaussian_failure_analyzer import first_prime_offset, square_decomposition
from gaussian_lemma_g_probe import primes_upto


@dataclass(frozen=True)
class CorrectionCase:
    n: int
    witness_t: int
    witness_r: int
    witness_offset: int
    witness_value: int
    first_prime: int
    first_prime_offset: int
    first_prime_nearest_t: int
    first_prime_nearest_r: int


def collect(limit: int, radius: int) -> list[CorrectionCase]:
    primes = primes_upto(limit + 1)
    cases = []
    for n in range(2, limit + 1):
        square_result = probe_n(n, 0)
        if isinstance(square_result, BandWitness):
            continue
        if not isinstance(square_result, BandFailure):
            raise TypeError(square_result)

        band_result = probe_n(n, radius)
        if isinstance(band_result, BandFailure):
            raise RuntimeError(f"radius {radius} does not repair n={n}")

        prime, offset = first_prime_offset(n, primes)
        _, _, _, nearest_t, _, nearest_r = square_decomposition(offset)
        cases.append(
            CorrectionCase(
                n=n,
                witness_t=band_result.t,
                witness_r=band_result.r,
                witness_offset=band_result.offset,
                witness_value=band_result.value,
                first_prime=prime,
                first_prime_offset=offset,
                first_prime_nearest_t=nearest_t,
                first_prime_nearest_r=nearest_r,
            )
        )
    return cases


def print_summary(cases: list[CorrectionCase], limit: int, radius: int) -> None:
    print(f"limit={limit}")
    print(f"radius={radius}")
    print(f"square_failures={len(cases)}")
    if not cases:
        return
    print(f"first_square_failure={cases[0].n}")
    print(f"last_square_failure={cases[-1].n}")
    print(f"max_abs_witness_r={max(abs(item.witness_r) for item in cases)}")
    print(f"max_abs_first_prime_nearest_r={max(abs(item.first_prime_nearest_r) for item in cases)}")

    witness_histogram: dict[int, int] = {}
    first_prime_histogram: dict[int, int] = {}
    for item in cases:
        witness_histogram[item.witness_r] = witness_histogram.get(item.witness_r, 0) + 1
        first_prime_histogram[item.first_prime_nearest_r] = (
            first_prime_histogram.get(item.first_prime_nearest_r, 0) + 1
        )

    print("witness_r_histogram:")
    for r in sorted(witness_histogram):
        print(f"  {r}: {witness_histogram[r]}")
    print("first_prime_nearest_r_histogram:")
    for r in sorted(first_prime_histogram):
        print(f"  {r}: {first_prime_histogram[r]}")


def print_table(cases: list[CorrectionCase]) -> None:
    print(
        "n,witness_t,witness_r,witness_offset,witness_value,"
        "first_prime,first_prime_offset,first_prime_nearest_t,first_prime_nearest_r"
    )
    for item in cases:
        print(
            f"{item.n},{item.witness_t},{item.witness_r},{item.witness_offset},"
            f"{item.witness_value},{item.first_prime},{item.first_prime_offset},"
            f"{item.first_prime_nearest_t},{item.first_prime_nearest_r}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--radius", type=int, default=2)
    parser.add_argument("--table", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases = collect(args.limit, args.radius)
    print_summary(cases, args.limit, args.radius)
    if args.table:
        print_table(cases)


if __name__ == "__main__":
    main()
