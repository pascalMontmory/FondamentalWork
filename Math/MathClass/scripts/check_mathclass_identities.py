#!/usr/bin/env python3
"""Finite checks for MathClass terminal-signature identities.

The script verifies identities that are true at finite N:

1. convex decomposition for disjoint class unions;
2. pure terminal classes;
3. total-variation pseudometric identities;
4. projection between bounds;
5. total-variation contraction under bound projection.

It uses Collatz terminal entry as the observation map, but the identities are
measure-theoretic.  Numerical errors should be zero up to floating point
roundoff.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from itertools import combinations, permutations
from math import gcd

INF = "inf"


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def terminal_entry(n: int, bound: int, max_steps: int) -> str:
    current = n
    for _ in range(max_steps + 1):
        if current <= bound:
            return str(current)
        current = step(current)
    return INF


def sieve(limit: int) -> bytearray:
    is_prime = bytearray(b"\x01") * (limit + 64)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int((limit + 63) ** 0.5) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 64 : p] = b"\x00" * (((limit + 63 - start) // p) + 1)
    return is_prime


def prime_pattern(limit: int, offsets: tuple[int, ...]) -> list[int]:
    primes = sieve(limit + max(offsets, default=0) + 2)
    return [
        n
        for n in range(2, limit + 1)
        if all(primes[n + offset] for offset in offsets)
    ]


@dataclass(frozen=True)
class Sample:
    name: str
    values: list[int]


def build_samples(limit: int) -> dict[str, Sample]:
    primes = prime_pattern(limit, (0,))
    odd_primes = [p for p in primes if p % 2 == 1]
    twin = prime_pattern(limit, (0, 2))
    cousin = prime_pattern(limit, (0, 4))
    sexy = prime_pattern(limit, (0, 6))
    twin_set = set(twin)
    prime_non_twin = [p for p in primes if p not in twin_set]
    odd = list(range(1, limit + 1, 2))
    even = list(range(2, limit + 1, 2))
    all_values = list(range(1, limit + 1))
    mod1_4 = [n for n in range(1, limit + 1) if n % 4 == 1]
    mod3_4 = [n for n in range(1, limit + 1) if n % 4 == 3]
    admissible_210 = [n for n in range(1, limit + 1) if gcd(n, 210) == 1]
    return {
        "all": Sample("all", all_values),
        "odd": Sample("odd", odd),
        "even": Sample("even", even),
        "mod1_4": Sample("mod1_4", mod1_4),
        "mod3_4": Sample("mod3_4", mod3_4),
        "admissible_210": Sample("admissible_210", admissible_210),
        "prime": Sample("prime", primes),
        "odd_prime": Sample("odd_prime", odd_primes),
        "twin": Sample("twin", twin),
        "cousin": Sample("cousin", cousin),
        "sexy": Sample("sexy", sexy),
        "prime_non_twin": Sample("prime_non_twin", prime_non_twin),
    }


def law(values: list[int], bound: int, max_steps: int) -> dict[str, float]:
    counts: Counter[str] = Counter(terminal_entry(n, bound, max_steps) for n in values)
    total = len(values)
    if total == 0:
        return {}
    return {state: count / total for state, count in counts.items()}


def tv(left: dict[str, float], right: dict[str, float]) -> float:
    states = set(left) | set(right)
    return 0.5 * sum(abs(left.get(state, 0.0) - right.get(state, 0.0)) for state in states)


def mix(
    left: dict[str, float],
    left_weight: float,
    right: dict[str, float],
    right_weight: float,
) -> dict[str, float]:
    out: Counter[str] = Counter()
    for state, mass in left.items():
        out[state] += left_weight * mass
    for state, mass in right.items():
        out[state] += right_weight * mass
    return dict(out)


def project_state(state: str, low_bound: int, max_steps: int) -> str:
    if state == INF:
        return INF
    return terminal_entry(int(state), low_bound, max_steps)


def project_law(high_law: dict[str, float], low_bound: int, max_steps: int) -> dict[str, float]:
    out: Counter[str] = Counter()
    for state, mass in high_law.items():
        out[project_state(state, low_bound, max_steps)] += mass
    return dict(out)


def pure_terminal_error(values: list[int], bound: int, max_steps: int) -> tuple[float, int]:
    fibers: dict[str, list[int]] = {}
    for n in values:
        fibers.setdefault(terminal_entry(n, bound, max_steps), []).append(n)

    worst = 0.0
    for state, fiber_values in fibers.items():
        fiber_law = law(fiber_values, bound, max_steps)
        expected = {state: 1.0}
        worst = max(worst, tv(fiber_law, expected))
    return worst, len(fibers)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20_000)
    parser.add_argument("--bounds", default="27,89,127")
    parser.add_argument("--max-steps", type=int, default=10_000)
    args = parser.parse_args()

    bounds = sorted({int(item) for item in args.bounds.split(",") if item.strip()})
    samples = build_samples(args.limit)
    laws = {
        (name, bound): law(sample.values, bound, args.max_steps)
        for name, sample in samples.items()
        for bound in bounds
    }

    print("check,scope,bound_or_pair,tv_error,verdict")

    decompositions = [
        ("all", "odd", "even"),
        ("odd", "mod1_4", "mod3_4"),
        ("prime", "twin", "prime_non_twin"),
    ]
    for whole, left, right in decompositions:
        whole_size = len(samples[whole].values)
        left_size = len(samples[left].values)
        right_size = len(samples[right].values)
        if whole_size != left_size + right_size:
            print(f"mixture,{whole}={left}+{right},all,inf,fail-size")
            continue
        for bound in bounds:
            mixed = mix(
                laws[(left, bound)],
                left_size / whole_size,
                laws[(right, bound)],
                right_size / whole_size,
            )
            error = tv(laws[(whole, bound)], mixed)
            verdict = "ok" if error <= 1e-14 else "fail"
            print(f"mixture,{whole}={left}+{right},{bound},{error:.17g},{verdict}")

    for bound in bounds:
        error, fiber_count = pure_terminal_error(samples["all"].values, bound, args.max_steps)
        verdict = "ok" if error <= 1e-14 else "fail"
        print(f"pure_terminal,all_fibers,{bound}:{fiber_count},{error:.17g},{verdict}")

    metric_classes = ["odd", "odd_prime", "admissible_210"]
    for bound in bounds:
        for left, right in permutations(metric_classes, 2):
            error = abs(tv(laws[(left, bound)], laws[(right, bound)]) - tv(laws[(right, bound)], laws[(left, bound)]))
            verdict = "ok" if error <= 1e-14 else "fail"
            print(f"pseudometric_symmetry,{left}<->{right},{bound},{error:.17g},{verdict}")
        for first, second, third in permutations(metric_classes, 3):
            lhs = tv(laws[(first, bound)], laws[(third, bound)])
            rhs = tv(laws[(first, bound)], laws[(second, bound)]) + tv(laws[(second, bound)], laws[(third, bound)])
            error = max(0.0, lhs - rhs)
            verdict = "ok" if error <= 1e-14 else "fail"
            print(f"pseudometric_triangle,{first}->{second}->{third},{bound},{error:.17g},{verdict}")

    for name in sorted(samples):
        for i, low in enumerate(bounds):
            for high in bounds[i + 1 :]:
                projected = project_law(laws[(name, high)], low, args.max_steps)
                error = tv(laws[(name, low)], projected)
                verdict = "ok" if error <= 1e-14 else "fail"
                print(f"projection,{name},{high}->{low},{error:.17g},{verdict}")

    contraction_pairs = list(combinations(["odd", "prime", "twin", "cousin", "sexy", "admissible_210"], 2))
    for left, right in contraction_pairs:
        for i, low in enumerate(bounds):
            for high in bounds[i + 1 :]:
                low_distance = tv(laws[(left, low)], laws[(right, low)])
                high_distance = tv(laws[(left, high)], laws[(right, high)])
                error = max(0.0, low_distance - high_distance)
                verdict = "ok" if error <= 1e-14 else "fail"
                print(f"tv_contraction,{left}|{right},{high}->{low},{error:.17g},{verdict}")

    for name in ["prime", "twin", "cousin", "sexy"]:
        print(f"sample_size,{name},N={args.limit},{len(samples[name].values)},diagnostic")


if __name__ == "__main__":
    main()
