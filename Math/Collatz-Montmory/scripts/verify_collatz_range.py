#!/usr/bin/env python3
"""Finite Collatz range verifier.

This script verifies only a finite range. It is not a proof of the Collatz
conjecture.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


def collatz_step(n: int) -> int:
    if n <= 0:
        raise ValueError("collatz_step is defined here only for positive integers")
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def stopping_time(n: int, max_steps: int) -> int | None:
    if n <= 0:
        raise ValueError("stopping_time is defined here only for positive integers")
    x = n
    for step in range(max_steps + 1):
        if x == 1:
            return step
        x = collatz_step(x)
    return None


@dataclass(frozen=True)
class VerificationResult:
    limit: int
    max_steps: int
    max_stopping_time: int
    argmax_stopping_time: int
    verified: bool
    first_failure: int | None


def verify_range(limit: int, max_steps: int) -> VerificationResult:
    if limit < 1:
        raise ValueError("limit must be >= 1")
    max_tau = 0
    argmax_tau = 1
    for n in range(1, limit + 1):
        tau = stopping_time(n, max_steps)
        if tau is None:
            return VerificationResult(
                limit=limit,
                max_steps=max_steps,
                max_stopping_time=max_tau,
                argmax_stopping_time=argmax_tau,
                verified=False,
                first_failure=n,
            )
        if tau > max_tau:
            max_tau = tau
            argmax_tau = n
    return VerificationResult(
        limit=limit,
        max_steps=max_steps,
        max_stopping_time=max_tau,
        argmax_stopping_time=argmax_tau,
        verified=True,
        first_failure=None,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--max-steps", type=int, default=10_000)
    args = parser.parse_args()

    result = verify_range(args.limit, args.max_steps)
    print(f"limit={result.limit}")
    print(f"max_steps={result.max_steps}")
    print(f"verified={result.verified}")
    print(f"first_failure={result.first_failure}")
    print(f"max_stopping_time={result.max_stopping_time}")
    print(f"argmax_stopping_time={result.argmax_stopping_time}")
    print("claim=finite verification only; not an infinite proof")


if __name__ == "__main__":
    main()
