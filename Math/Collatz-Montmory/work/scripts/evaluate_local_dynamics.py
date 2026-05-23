#!/usr/bin/env python3
"""Evaluate empirical local Montmory dynamics modulo small primes.

This script implements the candidate-B dynamics from filter-dynamics-specification.md.
It estimates, for twin-prime seeds or control seeds, the empirical distribution of
accelerated Collatz trajectories modulo q, then computes

    Sigma_q = 1 - mu_q(0) - mu_q(-2)
    B_q = Sigma_q / (1 - 2/q)
    C_dyn(Q) = 2*C2*prod_{3<=q<=Q} B_q

The output is diagnostic only. It is not a proof of convergence.
"""
from __future__ import annotations

import argparse
import math
from typing import Iterable, List, Sequence

TWIN_PRIME_HL_COEFF = 1.3203236316937391478556242200291115568652467205695
C_MONTMORY = 0.107983974916
RHO_TARGET = C_MONTMORY / TWIN_PRIME_HL_COEFF


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


def primes_up_to(limit: int) -> List[int]:
    is_prime = sieve(limit)
    return [n for n in range(2, limit + 1) if is_prime[n]]


def twin_seeds(limit: int) -> List[int]:
    is_prime = sieve(limit + 2)
    return [p for p in range(3, limit + 1, 2) if is_prime[p] and is_prime[p + 2]]


def odd_control_seeds(limit: int) -> List[int]:
    return list(range(3, limit + 1, 2))


def accelerated_collatz_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trajectory_residue_counts(seeds: Sequence[int], q: int, steps: int) -> List[int]:
    counts = [0] * q
    for seed in seeds:
        n = seed
        for _ in range(steps + 1):
            counts[n % q] += 1
            n = accelerated_collatz_step(n)
    return counts


def estimate_for_q(seeds: Sequence[int], q: int, steps: int) -> tuple[float, float, float, float]:
    counts = trajectory_residue_counts(seeds, q, steps)
    total = sum(counts)
    mu0 = counts[0] / total
    mu_minus2 = counts[(-2) % q] / total
    sigma = 1.0 - mu0 - mu_minus2
    uniform_sigma = 1.0 - 2.0 / q
    bias = sigma / uniform_sigma if uniform_sigma else float("nan")
    return mu0, mu_minus2, sigma, bias


def parse_q_values(raw: str | None, q_max: int) -> List[int]:
    if raw:
        return [int(part.strip()) for part in raw.split(",") if part.strip()]
    return [p for p in primes_up_to(q_max) if p >= 3]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-limit", type=int, default=100_000)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--q-max", type=int, default=97)
    parser.add_argument("--q-values", default=None)
    parser.add_argument("--seed-mode", choices=["twins", "odd-control"], default="twins")
    args = parser.parse_args()

    if args.seed_mode == "twins":
        seeds = twin_seeds(args.seed_limit)
    else:
        seeds = odd_control_seeds(args.seed_limit)

    q_values = parse_q_values(args.q_values, args.q_max)
    product_bias = 1.0

    print(f"seed_mode={args.seed_mode}")
    print(f"seed_limit={args.seed_limit}")
    print(f"seed_count={len(seeds)}")
    print(f"steps={args.steps}")
    print(f"C_Montmory={C_MONTMORY:.12f}")
    print(f"rho_target={RHO_TARGET:.17f}")
    print("q,mu0,mu_minus2,sigma,bias,product_bias,c_dyn")

    for q in q_values:
        mu0, mu_minus2, sigma, bias = estimate_for_q(seeds, q, args.steps)
        product_bias *= bias
        c_dyn = TWIN_PRIME_HL_COEFF * product_bias
        print(
            f"{q},{mu0:.17g},{mu_minus2:.17g},{sigma:.17g},"
            f"{bias:.17g},{product_bias:.17g},{c_dyn:.17g}"
        )


if __name__ == "__main__":
    main()
