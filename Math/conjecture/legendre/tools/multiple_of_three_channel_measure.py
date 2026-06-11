#!/usr/bin/env python3
"""Measure the two exact channels for n = 3m.

This script does not test Legendre directly in all intervals.  It measures the
four-offset route

    n^2 + t^2 + r,  r in {-1, 0, 1, 2}

after imposing n = 3m, and separates witnesses with 3 not dividing t from
witnesses with t = 3u.

It also records the stricter M_3 candidate channel:

    3 not dividing t: primitive opposite-parity pure Gaussian n^2 + t^2;
    t = 3u: the parity-collapsed nonprimitive repair candidates.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt

from gaussian_band_probe import is_prime


OFFSETS = (-1, 0, 1, 2)


@dataclass(frozen=True)
class Witness:
    m: int
    n: int
    channel: str
    t: int
    r: int
    value: int


@dataclass(frozen=True)
class M3Result:
    m: int
    witness: Witness | None
    m3_witness: Witness | None


def admissible(n: int, t: int, r: int) -> bool:
    return 1 <= t * t + r <= 2 * n


def full_channel_witness(m: int, want_multiple_of_three: bool) -> Witness | None:
    n = 3 * m
    for t in range(1, isqrt(2 * n) + 2):
        if (t % 3 == 0) != want_multiple_of_three:
            continue
        for r in OFFSETS:
            if not admissible(n, t, r):
                continue
            value = n * n + t * t + r
            if is_prime(value):
                channel = "t=3u" if want_multiple_of_three else "3nmid_t"
                return Witness(m=m, n=n, channel=channel, t=t, r=r, value=value)
    return None


def nonmultiple_offset_witness(m: int, r: int) -> Witness | None:
    n = 3 * m
    for t in range(1, isqrt(2 * n) + 2):
        if t % 3 == 0:
            continue
        if not admissible(n, t, r):
            continue
        value = n * n + t * t + r
        if is_prime(value):
            channel = "3nmid_t_r0" if r == 0 else "3nmid_t_r1"
            return Witness(m=m, n=n, channel=channel, t=t, r=r, value=value)
    return None


def m3_candidate_witness(m: int) -> Witness | None:
    n = 3 * m

    for t in range(1, isqrt(6 * m) + 1):
        if t % 3 == 0:
            continue
        if gcd(n, t) != 1 or (n + t) % 2 != 1:
            continue
        value = n * n + t * t
        if is_prime(value):
            return Witness(m=m, n=n, channel="M3_primitive_gaussian", t=t, r=0, value=value)

    for u in range(1, isqrt(6 * m) + 2):
        b = m * m + u * u
        t = 3 * u
        if (m - u) % 2 == 0:
            for r in (-1, 1):
                if 9 * u * u + r <= 6 * m:
                    value = 9 * b + r
                    if is_prime(value):
                        return Witness(m=m, n=n, channel="M3_nonprimitive", t=t, r=r, value=value)
        else:
            r = 2
            if 9 * u * u + r <= 6 * m:
                value = 9 * b + r
                if is_prime(value):
                    return Witness(m=m, n=n, channel="M3_nonprimitive", t=t, r=r, value=value)

    return None


def measure_m(m: int) -> M3Result:
    nonmultiple_gaussian = nonmultiple_offset_witness(m, 0)
    if nonmultiple_gaussian is not None:
        witness = nonmultiple_gaussian
    else:
        nonmultiple_unit_lift = nonmultiple_offset_witness(m, 1)
        if nonmultiple_unit_lift is not None:
            witness = nonmultiple_unit_lift
        else:
            witness = full_channel_witness(m, want_multiple_of_three=True)

    return M3Result(m=m, witness=witness, m3_witness=m3_candidate_witness(m))


def format_witness(witness: Witness | None) -> str:
    if witness is None:
        return "none"
    return (
        f"{witness.channel}: m={witness.m}, n={witness.n}, "
        f"t={witness.t}, r={witness.r}, value={witness.value}"
    )


def run(limit: int, show: int, show_m3_failures: int) -> int:
    repaired_by_nonmultiple_gaussian = 0
    repaired_by_nonmultiple_unit_lift = 0
    require_multiple = 0
    full_failures: list[M3Result] = []
    m3_failures: list[M3Result] = []
    m3_by_primitive = 0
    m3_by_nonprimitive = 0
    first_require_multiple: list[M3Result] = []
    first_m3_failures: list[M3Result] = []

    for m in range(1, limit + 1):
        result = measure_m(m)

        if result.witness is None:
            full_failures.append(result)
        elif result.witness.channel == "3nmid_t_r0":
            repaired_by_nonmultiple_gaussian += 1
        elif result.witness.channel == "3nmid_t_r1":
            repaired_by_nonmultiple_unit_lift += 1
        else:
            require_multiple += 1
            if len(first_require_multiple) < show:
                first_require_multiple.append(result)

        if result.m3_witness is None:
            m3_failures.append(result)
            if len(first_m3_failures) < show_m3_failures:
                first_m3_failures.append(result)
        elif result.m3_witness.channel == "M3_primitive_gaussian":
            m3_by_primitive += 1
        else:
            m3_by_nonprimitive += 1

    print(f"checked m=1..{limit} for n=3m")
    print("full four-offset channel:")
    print(f"  repaired_by_3nmid_t_r0_gaussian={repaired_by_nonmultiple_gaussian}")
    print(f"  repaired_by_3nmid_t_r1_unit_lift={repaired_by_nonmultiple_unit_lift}")
    print(f"  require_t_eq_3u={require_multiple}")
    print(f"  full_failures={len(full_failures)}")
    print("M3 candidate channel:")
    print(f"  M3_primitive_gaussian={m3_by_primitive}")
    print(f"  M3_nonprimitive={m3_by_nonprimitive}")
    print(f"  M3_failures={len(m3_failures)}")

    if first_require_multiple:
        print("first cases requiring t=3u in the full four-offset channel:")
        for result in first_require_multiple:
            print(f"  {format_witness(result.witness)}")

    if full_failures:
        print("full four-offset failures:")
        for result in full_failures[:show]:
            print(f"  m={result.m}, n={3 * result.m}")

    if first_m3_failures:
        print("first M3 candidate failures:")
        for result in first_m3_failures:
            nonmultiple = (
                nonmultiple_offset_witness(result.m, 0)
                or nonmultiple_offset_witness(result.m, 1)
            )
            multiple = full_channel_witness(result.m, want_multiple_of_three=True)
            print(
                f"  m={result.m}, n={3 * result.m}, "
                f"full_3nmid_t={format_witness(nonmultiple)}, "
                f"full_t_eq_3u={format_witness(multiple)}"
            )

    return 1 if full_failures else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--show", type=int, default=20)
    parser.add_argument("--show-m3-failures", type=int, default=20)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raise SystemExit(run(args.limit, args.show, args.show_m3_failures))


if __name__ == "__main__":
    main()
