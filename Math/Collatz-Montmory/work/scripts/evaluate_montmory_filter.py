#!/usr/bin/env python3
"""Evaluate candidate Montmory filters on twin primes and controls.

This script is intentionally simple and deterministic. It is not a proof of an
asymptotic constant; it is a reproducible diagnostic for the filter-lock problem.

Default filter:
    T(n) = n/2 if n even, (3n+1)/2 if n odd
    tau_B(n) = first t with T^t(n) <= B
    kappa_B(n) = log2(n) / tau_B(n)
    pair_score(p) = min(kappa_B(p), kappa_B(p+2))
    M_alpha(p,p+2) = 1 iff pair_score(p) >= alpha
"""
from __future__ import annotations

import argparse
import bisect
import math
from dataclasses import dataclass
from typing import List, Sequence

TWIN_PRIME_HL_COEFF = 1.3203236316937391478556242200291115568652467205695
C_MONTMORY = 0.107983974916
RHO_TARGET = C_MONTMORY / TWIN_PRIME_HL_COEFF
COLLATZ_RANDOM_WALK_DRIFT = 1.0 - 0.5 * math.log2(3.0)
SCORE_MODES = [
    "min",
    "geo",
    "harm",
    "min-log-centered",
    "geo-log-centered",
    "harm-log-centered",
]
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
            step = p
            is_prime[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)
    return is_prime


def population_up_to(limit: int, population: str, odd_stride: int) -> List[int]:
    if population == "odd-sample":
        return list(range(3, limit + 1, 2 * odd_stride))

    is_prime = sieve(limit + 2)
    if population == "twins":
        return [p for p in range(3, limit + 1, 2) if is_prime[p] and is_prime[p + 2]]
    if population == "prime-non-twin":
        return [p for p in range(3, limit + 1, 2) if is_prime[p] and not is_prime[p + 2]]
    raise ValueError(f"unknown population: {population}")


def accelerated_collatz_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def tau_to_bound(n: int, bound: int = 89, max_steps: int = 100000) -> int:
    t = 0
    while n > bound:
        n = accelerated_collatz_step(n)
        t += 1
        if t > max_steps:
            raise RuntimeError(f"tau exceeded max_steps for n={n}")
    return t


def kappa(n: int, bound: int = 89, max_steps: int = 100000) -> float:
    tau = tau_to_bound(n, bound=bound, max_steps=max_steps)
    if tau == 0:
        return math.inf
    return math.log2(n) / tau


def combine_pair_scores(a: float, b: float, mode: str) -> float:
    if mode == "min":
        return min(a, b)
    if mode == "geo":
        return math.sqrt(a * b)
    if mode == "harm":
        return 2.0 / (1.0 / a + 1.0 / b)
    raise ValueError(f"unknown base score mode: {mode}")


def pair_score(p: int, bound: int = 89, max_steps: int = 100000, mode: str = "min") -> float:
    centered = mode.endswith("-log-centered")
    base_mode = mode.removesuffix("-log-centered") if centered else mode
    a = kappa(p, bound=bound, max_steps=max_steps)
    b = kappa(p + 2, bound=bound, max_steps=max_steps)
    score = combine_pair_scores(a, b, base_mode)
    if centered:
        return (score - COLLATZ_RANDOM_WALK_DRIFT) * math.log2(p)
    return score


@dataclass(frozen=True)
class Evaluation:
    x: int
    item_count: int
    selected_count: int
    ratio: float
    coefficient_estimate: float


def evaluate_at_x(items: Sequence[int], scores: Sequence[float], x: int, alpha: float) -> Evaluation:
    n = bisect.bisect_right(items, x)
    selected = sum(1 for s in scores[:n] if s >= alpha)
    ratio = selected / n if n else float("nan")
    coefficient = selected / (x / (math.log(x) ** 2)) if x > 1 else float("nan")
    return Evaluation(x=x, item_count=n, selected_count=selected, ratio=ratio, coefficient_estimate=coefficient)


def calibrate_alpha(scores: Sequence[float], target_ratio: float) -> float:
    if not scores:
        raise ValueError("cannot calibrate alpha without scores")
    ordered = sorted(scores, reverse=True)
    # Keep approximately target_ratio of scores with score >= alpha.
    idx = min(len(ordered) - 1, max(0, int(math.ceil(target_ratio * len(ordered))) - 1))
    return ordered[idx]


def parse_x_values(raw: str) -> List[int]:
    return [int(part.strip()) for part in raw.split(",") if part.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--x-values", default="10000,100000,1000000")
    parser.add_argument("--bound", type=int, default=89)
    parser.add_argument("--mode", choices=SCORE_MODES, default="min")
    parser.add_argument("--population", choices=POPULATIONS, default="twins")
    parser.add_argument("--odd-stride", type=int, default=20)
    parser.add_argument("--alpha", type=float, default=None)
    parser.add_argument("--calibrate-x", type=int, default=None)
    parser.add_argument("--max-steps", type=int, default=100000)
    args = parser.parse_args()

    x_values = parse_x_values(args.x_values)
    limit = max(args.limit, max(x_values) if x_values else args.limit)
    items = population_up_to(limit, args.population, args.odd_stride)
    scores = [pair_score(p, bound=args.bound, max_steps=args.max_steps, mode=args.mode) for p in items]

    if args.alpha is None:
        if args.calibrate_x is None:
            calibration_n = len(scores)
        else:
            calibration_n = bisect.bisect_right(items, args.calibrate_x)
        alpha = calibrate_alpha(scores[:calibration_n], RHO_TARGET)
    else:
        alpha = args.alpha

    print(f"C_Montmory={C_MONTMORY:.12f}")
    print(f"HL_twin_coefficient_2C2={TWIN_PRIME_HL_COEFF:.16f}")
    print(f"rho_target={RHO_TARGET:.17f}")
    print(f"collatz_random_walk_drift={COLLATZ_RANDOM_WALK_DRIFT:.17f}")
    print(f"bound={args.bound}")
    print(f"mode={args.mode}")
    print(f"population={args.population}")
    if args.population == "odd-sample":
        print(f"odd_stride={args.odd_stride}")
    print(f"alpha={alpha:.17g}")
    print("x,item_count,selected_count,selected_ratio,coefficient_estimate")
    for x in x_values:
        result = evaluate_at_x(items, scores, x, alpha)
        print(
            f"{result.x},{result.item_count},{result.selected_count},"
            f"{result.ratio:.17g},{result.coefficient_estimate:.17g}"
        )


if __name__ == "__main__":
    main()
