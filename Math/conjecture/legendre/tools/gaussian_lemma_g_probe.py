#!/usr/bin/env python3
"""Probe the Gaussian offset version of Legendre's conjecture.

For each n, search for a primitive offset

    1 <= t <= floor(sqrt(2*n))

such that n and t have opposite parity and no prime p == 1 mod 4, p <= n+1,
divides n^2 + t^2.  Under these conditions, no p == 3 mod 4 can divide the
Gaussian norm either, so n^2 + t^2 is prime if it lies in the Legendre
interval.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True)
class Witness:
    n: int
    t: int
    value: int
    prime: bool
    tried: int
    primitive_candidates: int


@dataclass(frozen=True)
class Failure:
    n: int
    primitive_candidates: int
    blocked: list[tuple[int, int]]


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def is_prime(value: int, primes: list[int]) -> bool:
    if value < 2:
        return False
    root = isqrt(value)
    for p in primes:
        if p > root:
            break
        if value % p == 0:
            return value == p
    return True


def first_blocker(value: int, primes_1mod4: list[int]) -> int | None:
    for p in primes_1mod4:
        if value % p == 0:
            return p
    return None


def probe_n(n: int, primes: list[int]) -> Witness | Failure:
    bound = isqrt(2 * n)
    small_1mod4 = [p for p in primes if p <= n + 1 and p % 4 == 1]
    blocked: list[tuple[int, int]] = []
    primitive_candidates = 0
    tried = 0
    for t in range(1, bound + 1):
        if gcd(n, t) != 1:
            continue
        if (n + t) % 2 == 0:
            continue
        primitive_candidates += 1
        value = n * n + t * t
        blocker = first_blocker(value, small_1mod4)
        tried += 1
        if blocker is None:
            return Witness(
                n=n,
                t=t,
                value=value,
                prime=is_prime(value, primes),
                tried=tried,
                primitive_candidates=primitive_candidates,
            )
        blocked.append((t, blocker))
    return Failure(n=n, primitive_candidates=primitive_candidates, blocked=blocked)


def run(limit: int, show_failures: int, show_records: bool) -> int:
    primes = primes_upto(limit + 1)
    failures: list[Failure] = []
    max_t = 0
    max_ratio = 0.0
    max_tried = 0
    records: list[Witness] = []
    prime_witnesses = 0

    for n in range(2, limit + 1):
        result = probe_n(n, primes)
        if isinstance(result, Failure):
            failures.append(result)
            if len(failures) <= show_failures:
                blocked = ", ".join(f"t={t}:p={p}" for t, p in result.blocked[:12])
                suffix = "" if len(result.blocked) <= 12 else ", ..."
                print(
                    f"failure n={n}, primitive_candidates={result.primitive_candidates}, "
                    f"blocked=[{blocked}{suffix}]"
                )
            continue

        if result.prime:
            prime_witnesses += 1
        ratio = result.t / max(1, isqrt(2 * n))
        if result.t > max_t or ratio > max_ratio or result.tried > max_tried:
            records.append(result)
            max_t = max(max_t, result.t)
            max_ratio = max(max_ratio, ratio)
            max_tried = max(max_tried, result.tried)

    print(f"checked n=2..{limit}")
    print(f"failures={len(failures)}")
    print(f"prime_witnesses={prime_witnesses}/{max(0, limit - 1)}")
    print(f"max_t={max_t}")
    print(f"max_t_over_floor_sqrt_2n={max_ratio:.6f}")
    print(f"max_tried_candidates_before_witness={max_tried}")

    if show_records:
        print("records:")
        for witness in records:
            bound = isqrt(2 * witness.n)
            print(
                f"  n={witness.n}, t={witness.t}, bound={bound}, "
                f"tried={witness.tried}, value={witness.value}, prime={witness.prime}"
            )

    return 1 if failures else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10_000)
    parser.add_argument("--show-failures", type=int, default=20)
    parser.add_argument("--records", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raise SystemExit(run(args.limit, args.show_failures, args.records))


if __name__ == "__main__":
    main()
