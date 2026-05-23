#!/usr/bin/env python3
"""Evaluate candidate Collatz resonance centers.

This diagnostic tests the idea that a center B is an integer around which
Collatz trajectories pass or linger.  It uses multiplicative windows

    I_{B,eta} = [ceil(B exp(-eta)), floor(B exp(eta))]

and reports hit rates, residence counts, centered first-passage times, and the
first values observed in the window.

The script is diagnostic only; it does not prove that any center is canonical.
"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict
from statistics import fmean

D = 1.0 - 0.5 * math.log2(3.0)


def sieve(limit: int) -> bytearray:
    is_prime = bytearray(b"\x01") * (limit + 3)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int((limit + 2) ** 0.5) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 3 : p] = b"\x00" * (((limit + 2 - start) // p) + 1)
    return is_prime


def population(limit: int, name: str, odd_stride: int) -> list[int]:
    if name == "odd-sample":
        return list(range(3, limit + 1, 2 * odd_stride))
    primes = sieve(limit + 2)
    if name == "twins":
        return [p for p in range(3, limit + 1, 2) if primes[p] and primes[p + 2]]
    if name == "prime-non-twin":
        return [p for p in range(3, limit + 1, 2) if primes[p] and not primes[p + 2]]
    if name == "primes":
        return [p for p in range(3, limit + 1, 2) if primes[p]]
    raise ValueError(name)


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def make_windows(centers: list[int], eta: float) -> dict[int, tuple[int, int]]:
    out = {}
    for b in centers:
        lo = max(2, math.ceil(b * math.exp(-eta)))
        hi = max(lo, math.floor(b * math.exp(eta)))
        out[b] = (lo, hi)
    return out


def records(items: list[int], centers: list[int], eta: float, max_steps: int) -> dict[int, dict[str, object]]:
    windows = make_windows(centers, eta)
    stats = {
        b: {"hits": 0, "visits": [], "u": [], "first_values": defaultdict(int)}
        for b in centers
    }
    for n0 in items:
        n = n0
        first = {}
        visits = {b: 0 for b in centers}
        t = 0
        while n != 1 and t <= max_steps:
            for b, (lo, hi) in windows.items():
                if lo <= n <= hi:
                    visits[b] += 1
                    if b not in first:
                        first[b] = (t, n)
            n = step(n)
            t += 1
        for b in centers:
            if b in first:
                ft, fv = first[b]
                stats[b]["hits"] += 1
                stats[b]["visits"].append(visits[b])
                stats[b]["u"].append(ft - (math.log2(n0) - math.log2(b)) / D)
                stats[b]["first_values"][fv] += 1
    return stats


def summarize(limit: int, name: str, centers: list[int], eta: float, odd_stride: int, max_steps: int) -> list[dict[str, float | int | str]]:
    items = population(limit, name, odd_stride)
    stats = records(items, centers, eta, max_steps)
    rows = []
    for b in centers:
        hit_count = int(stats[b]["hits"])
        hit_rate = hit_count / len(items) if items else float("nan")
        visits = stats[b]["visits"]
        u = stats[b]["u"]
        first_values = stats[b]["first_values"]
        top = sorted(first_values.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
        window = make_windows([b], eta)[b]
        rows.append(
            {
                "population": name,
                "limit": limit,
                "center": b,
                "window": f"{window[0]}:{window[1]}",
                "items": len(items),
                "hits": hit_count,
                "hit_rate": hit_rate,
                "mean_visits": fmean(visits) if visits else 0.0,
                "u_mean": fmean(u) if u else float("nan"),
                "top_first": ";".join(f"{k}:{v / hit_count:.4f}" for k, v in top) if hit_count else "",
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limits", default="1000000,3000000")
    parser.add_argument("--populations", default="twins,prime-non-twin,odd-sample")
    parser.add_argument("--centers", default="27,31,41,47,55,63,65,73,81,85,89,91,95,97,109,127,171,255")
    parser.add_argument("--eta", type=float, default=0.08)
    parser.add_argument("--odd-stride", type=int, default=20)
    parser.add_argument("--max-steps", type=int, default=10000)
    args = parser.parse_args()

    limits = [int(x) for x in args.limits.split(",")]
    centers = [int(x) for x in args.centers.split(",")]
    populations = args.populations.split(",")

    print("population,limit,center,window,items,hits,hit_rate,mean_visits,u_mean,top_first")
    for limit in limits:
        for pop in populations:
            for row in summarize(limit, pop, centers, args.eta, args.odd_stride, args.max_steps):
                keys = ["population", "limit", "center", "window", "items", "hits", "hit_rate", "mean_visits", "u_mean", "top_first"]
                print(",".join(str(row[key]) for key in keys))


if __name__ == "__main__":
    main()
