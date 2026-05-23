#!/usr/bin/env python3
"""Evaluate the moving-depth Lambda_B entrance-law candidate.

This script computes empirical window laws for

    (E_B(n), u_B(n), Z_B(n))

where

    E_B(n) = T^{tau_B(n)}(n)
    u_B(n) = tau_B(n) - log2(n)/d
    Z_B(n) = -d^2 u_B(n)
    d = 1 - 1/2 log2(3)

It compares consecutive windows using total variation on E_B and a KS distance
on u_B and Z_B. The output is diagnostic only; it is not a proof of convergence.
"""
from __future__ import annotations

import argparse
import bisect
import math
from dataclasses import dataclass
from statistics import fmean
from typing import Dict, List, Sequence, Tuple

COLLATZ_RANDOM_WALK_DRIFT = 1.0 - 0.5 * math.log2(3.0)
POPULATIONS = ["twins", "prime-non-twin", "odd-sample"]


def sieve(limit: int) -> bytearray:
    if limit < 2:
        return bytearray(limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    r = int(limit**0.5)
    for p in range(2, r + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return is_prime


def population_up_to(limit: int, population: str, odd_stride: int, bound: int) -> List[int]:
    if population == "odd-sample":
        return [n for n in range(3, limit + 1, 2 * odd_stride) if n > bound]

    is_prime = sieve(limit + 2)
    if population == "twins":
        return [p for p in range(3, limit + 1, 2) if p > bound and is_prime[p] and is_prime[p + 2]]
    if population == "prime-non-twin":
        return [p for p in range(3, limit + 1, 2) if p > bound and is_prime[p] and not is_prime[p + 2]]
    raise ValueError(f"unknown population: {population}")


def accelerated_collatz_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def tau_entry(n: int, bound: int, max_steps: int) -> tuple[int, int]:
    t = 0
    while n > bound:
        n = accelerated_collatz_step(n)
        t += 1
        if t > max_steps:
            raise RuntimeError("tau exceeded max_steps")
    return t, n


@dataclass(frozen=True)
class Record:
    n: int
    entry: int
    u: float
    z: float


def build_records(items: Sequence[int], bound: int, max_steps: int) -> List[Record]:
    out: List[Record] = []
    d = COLLATZ_RANDOM_WALK_DRIFT
    for n in items:
        tau, entry = tau_entry(n, bound, max_steps)
        u = tau - math.log2(n) / d
        z = -(d * d) * u
        out.append(Record(n=n, entry=entry, u=u, z=z))
    return out


def parse_windows(raw: str) -> List[tuple[int, int]]:
    windows = []
    for part in raw.split(","):
        if not part.strip():
            continue
        lo, hi = part.split(":")
        windows.append((int(lo), int(hi)))
    return windows


def quantiles(values: Sequence[float], qs: Sequence[float]) -> List[float]:
    if not values:
        return [float("nan")] * len(qs)
    ordered = sorted(values)
    n = len(ordered)
    return [ordered[min(n - 1, max(0, round(q * (n - 1))))] for q in qs]


def tv_distance(a: Dict[int, float], b: Dict[int, float]) -> float:
    keys = set(a) | set(b)
    return 0.5 * sum(abs(a.get(k, 0.0) - b.get(k, 0.0)) for k in keys)


def ks_distance(a: Sequence[float], b: Sequence[float]) -> float:
    if not a or not b:
        return float("nan")
    left = sorted(a)
    right = sorted(b)
    i = j = 0
    n = len(left)
    m = len(right)
    best = 0.0
    for value in sorted(set(left + right)):
        while i < n and left[i] <= value:
            i += 1
        while j < m and right[j] <= value:
            j += 1
        best = max(best, abs(i / n - j / m))
    return best


def summarize_window(records: Sequence[Record], lo: int, hi: int) -> tuple[dict[int, float], list[float], list[float]]:
    subset = [r for r in records if lo < r.n <= hi]
    count = len(subset)
    entries: Dict[int, float] = {}
    u_values: List[float] = []
    z_values: List[float] = []
    for record in subset:
        entries[record.entry] = entries.get(record.entry, 0.0) + 1.0
        u_values.append(record.u)
        z_values.append(record.z)
    if count:
        entries = {key: value / count for key, value in entries.items()}
    return entries, u_values, z_values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--bound", type=int, default=89)
    parser.add_argument("--population", choices=POPULATIONS, default="twins")
    parser.add_argument("--odd-stride", type=int, default=20)
    parser.add_argument("--windows", default="100000:1000000,1000000:3000000,3000000:10000000")
    parser.add_argument("--max-steps", type=int, default=100000)
    args = parser.parse_args()

    windows = parse_windows(args.windows)
    limit = max(args.limit, max(hi for _, hi in windows))
    items = population_up_to(limit, args.population, args.odd_stride, args.bound)
    records = build_records(items, args.bound, args.max_steps)

    print(f"bound={args.bound}")
    print(f"population={args.population}")
    print(f"item_count={len(items)}")
    print(f"d={COLLATZ_RANDOM_WALK_DRIFT:.17f}")
    print("window,item_count,entry_support,entry_top,u_mean,u_q10,u_q25,u_q50,u_q75,u_q90,z_mean,z_q10,z_q25,z_q50,z_q75,z_q90,z_q918,tv_entry_vs_prev,ks_u_vs_prev,ks_z_vs_prev")

    previous = None
    for lo, hi in windows:
        entries, u_values, z_values = summarize_window(records, lo, hi)
        top = ";".join(f"{key}:{value:.6g}" for key, value in sorted(entries.items(), key=lambda item: -item[1])[:8])
        u_q = quantiles(u_values, [0.10, 0.25, 0.50, 0.75, 0.90])
        z_q = quantiles(z_values, [0.10, 0.25, 0.50, 0.75, 0.90, 0.9182140103199729])
        if previous is None:
            tv = ks_u = ks_z = float("nan")
        else:
            tv = tv_distance(previous[0], entries)
            ks_u = ks_distance(previous[1], u_values)
            ks_z = ks_distance(previous[2], z_values)
        print(
            f"({lo},{hi}],{len(u_values)},{len(entries)},{top},"
            f"{fmean(u_values):.17g},{','.join(f'{value:.17g}' for value in u_q)},"
            f"{fmean(z_values):.17g},{','.join(f'{value:.17g}' for value in z_q)},"
            f"{tv:.17g},{ks_u:.17g},{ks_z:.17g}"
        )
        previous = (entries, u_values, z_values)


if __name__ == "__main__":
    main()
