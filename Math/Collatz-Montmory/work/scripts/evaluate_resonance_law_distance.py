#!/usr/bin/env python3
"""Compare full resonance-window laws between twin starts and controls.

For a center B and width eta, this computes the law of

    (P_{B,eta}, U_{B,eta}, R_{B,eta})

where P is the first value in the window, U is the centered first-passage time,
and R is the residence count in the window.  It reports

    D = TV(P_twin, P_control) + KS(U_twin, U_control) + KS(R_twin, R_control).

The script is diagnostic only; it does not prove or refute an asymptotic law.
"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict

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
    raise ValueError(name)


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def window(center: int, eta: float) -> tuple[int, int]:
    return max(2, math.ceil(center * math.exp(-eta))), math.floor(center * math.exp(eta))


def records(items: list[int], center: int, eta: float, max_steps: int) -> tuple[dict[int, float], list[float], list[int], float]:
    lo, hi = window(center, eta)
    first_values: dict[int, int] = defaultdict(int)
    u_values: list[float] = []
    residence_values: list[int] = []
    hit_count = 0
    for n0 in items:
        n = n0
        first = None
        residence = 0
        t = 0
        while n != 1 and t <= max_steps:
            if lo <= n <= hi:
                residence += 1
                if first is None:
                    first = (t, n)
            n = step(n)
            t += 1
        if first is not None:
            hit_count += 1
            ft, fv = first
            first_values[fv] += 1
            u_values.append(ft - (math.log2(n0) - math.log2(center)) / D)
            residence_values.append(residence)
    hit_rate = hit_count / len(items) if items else float("nan")
    first_law = {k: v / hit_count for k, v in first_values.items()} if hit_count else {}
    return first_law, u_values, residence_values, hit_rate


def tv(a: dict[int, float], b: dict[int, float]) -> float:
    keys = set(a) | set(b)
    return 0.5 * sum(abs(a.get(k, 0.0) - b.get(k, 0.0)) for k in keys)


def ks(a: list[float] | list[int], b: list[float] | list[int]) -> float:
    if not a or not b:
        return float("nan")
    left = sorted(a)
    right = sorted(b)
    values = sorted(set(left + right))
    i = j = 0
    n = len(left)
    m = len(right)
    out = 0.0
    for value in values:
        while i < n and left[i] <= value:
            i += 1
        while j < m and right[j] <= value:
            j += 1
        out = max(out, abs(i / n - j / m))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=3_000_000)
    parser.add_argument("--centers", default="27,31,41,47,55,63,65,73,81,85,89,91,95,97,109,127,171,255")
    parser.add_argument("--eta", type=float, default=0.08)
    parser.add_argument("--odd-stride", type=int, default=20)
    parser.add_argument("--max-steps", type=int, default=10000)
    args = parser.parse_args()

    centers = [int(x) for x in args.centers.split(",")]
    items = {
        "twins": population(args.limit, "twins", args.odd_stride),
        "prime-non-twin": population(args.limit, "prime-non-twin", args.odd_stride),
        "odd-sample": population(args.limit, "odd-sample", args.odd_stride),
    }
    print("limit,center,control,twin_hit,control_hit,tv_first,ks_u,ks_residence,D")
    for center in centers:
        twin = records(items["twins"], center, args.eta, args.max_steps)
        for control in ["prime-non-twin", "odd-sample"]:
            ctrl = records(items[control], center, args.eta, args.max_steps)
            tv_first = tv(twin[0], ctrl[0])
            ks_u = ks(twin[1], ctrl[1])
            ks_res = ks(twin[2], ctrl[2])
            total = tv_first + ks_u + ks_res
            print(
                f"{args.limit},{center},{control},{twin[3]:.9f},{ctrl[3]:.9f},"
                f"{tv_first:.9f},{ks_u:.9f},{ks_res:.9f},{total:.9f}"
            )


if __name__ == "__main__":
    main()
