#!/usr/bin/env python3
"""Find full A-block covers and their nonprimitive repairs.

This is exploratory.  It combines the least-root zone probe with the exact
multiple-of-three repair channel.  A full A-block cover is not a Legendre
counterexample; it means the coprime complete A-block gate has no open layer
in the current low/middle/high certificate model.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt

from gaussian_band_probe import is_prime
from least_root_zone_probe import MStats, analyze_m, primes_upto


@dataclass(frozen=True)
class Repair:
    m: int
    u: int
    t: int
    r: int
    value: int


def nonprimitive_repair(m: int) -> Repair | None:
    for u in range(1, isqrt(6 * m) + 2):
        b = m * m + u * u
        t = 3 * u
        if (m - u) % 2 == 0:
            for r in (-1, 1):
                if 9 * u * u + r <= 6 * m:
                    value = 9 * b + r
                    if is_prime(value):
                        return Repair(m=m, u=u, t=t, r=r, value=value)
        else:
            r = 2
            if 9 * u * u + r <= 6 * m:
                value = 9 * b + r
                if is_prime(value):
                    return Repair(m=m, u=u, t=t, r=r, value=value)
    return None


def is_full_cover(stats: MStats) -> bool:
    return (
        stats.complete_cop_blocks > 0
        and stats.both_layers_covered == stats.complete_cop_blocks
    )


def run(args: argparse.Namespace) -> int:
    primes = primes_upto(3 * args.end)
    full: list[tuple[MStats, Repair | None]] = []
    max_ratio: MStats | None = None

    for m in range(args.start, args.end + 1, args.step):
        stats = analyze_m(m, primes)
        if max_ratio is None:
            max_ratio = stats
        else:
            lhs = stats.both_layers_covered * max(1, max_ratio.complete_cop_blocks)
            rhs = max_ratio.both_layers_covered * max(1, stats.complete_cop_blocks)
            if lhs > rhs:
                max_ratio = stats

        if is_full_cover(stats):
            repair = nonprimitive_repair(m)
            full.append((stats, repair))
            if len(full) <= args.show:
                repair_text = (
                    "none"
                    if repair is None
                    else f"u={repair.u} t={repair.t} r={repair.r} value={repair.value}"
                )
                print(
                    f"full_cover m={m} cop={stats.complete_cop_blocks} "
                    f"lowlow={stats.low_low_possible} mixed={stats.mixed_high_low_or_mid} "
                    f"hihi={stats.high_high} repair={repair_text}"
                )

    print("summary:")
    print(f"  scanned={args.start}..{args.end} step={args.step}")
    print(f"  full_covers={len(full)}")
    if full:
        first_stats, first_repair = full[0]
        print(f"  first_full_cover_m={first_stats.m}")
        missing_repairs = [stats.m for stats, repair in full if repair is None]
        print(f"  full_covers_without_nonprimitive_repair={len(missing_repairs)}")
        if missing_repairs:
            print("  missing_repair_m=" + ",".join(map(str, missing_repairs[: args.show])))
        u_counts: dict[int, int] = {}
        r_counts: dict[int, int] = {}
        for _, repair in full:
            if repair is not None:
                u_counts[repair.u] = u_counts.get(repair.u, 0) + 1
                r_counts[repair.r] = r_counts.get(repair.r, 0) + 1
        print("  repair_u_counts=" + str(dict(sorted(u_counts.items()))))
        print("  repair_r_counts=" + str(dict(sorted(r_counts.items()))))
    if max_ratio is not None and max_ratio.complete_cop_blocks:
        ratio = max_ratio.both_layers_covered / max_ratio.complete_cop_blocks
        print(
            f"  max_ratio_m={max_ratio.m} ratio={ratio:.4f} "
            f"covered={max_ratio.both_layers_covered}/{max_ratio.complete_cop_blocks}"
        )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=10_000)
    parser.add_argument("--step", type=int, default=1)
    parser.add_argument("--show", type=int, default=30)
    return parser.parse_args()


def main() -> None:
    raise SystemExit(run(parse_args()))


if __name__ == "__main__":
    main()
