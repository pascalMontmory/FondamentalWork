"""Shared helpers for MathClass terminal-signature scripts."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
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
    is_prime = bytearray(b"\x01") * (limit + 4096)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int((limit + 4095) ** 0.5) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 4096 : p] = b"\x00" * (((limit + 4095 - start) // p) + 1)
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
    twin = prime_pattern(limit, (0, 2))
    cousin = prime_pattern(limit, (0, 4))
    sexy = prime_pattern(limit, (0, 6))
    twin_set = set(twin)
    cousin_set = set(cousin)
    sexy_set = set(sexy)
    out = {
        "all": list(range(1, limit + 1)),
        "odd": list(range(1, limit + 1, 2)),
        "even": list(range(2, limit + 1, 2)),
        "mod1_4": [n for n in range(1, limit + 1) if n % 4 == 1],
        "mod3_4": [n for n in range(1, limit + 1) if n % 4 == 3],
        "admissible_30": [n for n in range(1, limit + 1) if gcd(n, 30) == 1],
        "admissible_210": [n for n in range(1, limit + 1) if gcd(n, 210) == 1],
        "admissible_2310": [n for n in range(1, limit + 1) if gcd(n, 2310) == 1],
        "prime": primes,
        "odd_prime": [p for p in primes if p % 2 == 1],
        "twin": twin,
        "cousin": cousin,
        "sexy": sexy,
        "prime_non_twin": [p for p in primes if p not in twin_set],
        "prime_non_cousin": [p for p in primes if p not in cousin_set],
        "prime_non_sexy": [p for p in primes if p not in sexy_set],
    }
    return {name: Sample(name, values) for name, values in out.items()}


def law(values: list[int], bound: int, max_steps: int) -> dict[str, float]:
    counts: Counter[str] = Counter(terminal_entry(n, bound, max_steps) for n in values)
    total = len(values)
    if total == 0:
        return {}
    return {state: count / total for state, count in counts.items()}


def tv(left: dict[str, float], right: dict[str, float]) -> float:
    states = set(left) | set(right)
    return 0.5 * sum(abs(left.get(state, 0.0) - right.get(state, 0.0)) for state in states)
