#!/usr/bin/env python3
"""Reference micro-uncertainty harness for PRNG experiments.

This script uses xorshift32 only as a compact, deterministic reference
generator. It is not a cryptographic validation and it does not certify
any production PRNG.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple


MASK32 = (1 << 32) - 1


@dataclass(frozen=True)
class XorShiftParams:
    left_a: int
    right_b: int
    left_c: int

    @property
    def label(self) -> str:
        return f"xorshift32({self.left_a},{self.right_b},{self.left_c})"


def xorshift32_step(state: int, params: XorShiftParams) -> int:
    state &= MASK32
    state ^= (state << params.left_a) & MASK32
    state ^= (state >> params.right_b) & MASK32
    state ^= (state << params.left_c) & MASK32
    return state & MASK32


def stream(seed: int, params: XorShiftParams, words: int) -> List[int]:
    state = seed & MASK32
    out: List[int] = []
    for _ in range(words):
        state = xorshift32_step(state, params)
        out.append(state)
    return out


def deterministic_seeds(count: int) -> List[int]:
    seeds: List[int] = []
    for idx in range(count):
        digest = hashlib.sha256(f"prng-micro-uncertainty:{idx}".encode()).digest()
        seed = int.from_bytes(digest[:4], "big")
        seeds.append(seed or 1)
    return seeds


def one_bit_neighbors(seed: int, bits: int) -> Iterable[int]:
    for bit in range(bits):
        neighbor = seed ^ (1 << bit)
        yield neighbor or 1


def hamming_words(left: Sequence[int], right: Sequence[int]) -> int:
    return sum((a ^ b).bit_count() for a, b in zip(left, right))


def bit_frequency(words: Sequence[int]) -> float:
    total_bits = 32 * len(words)
    if total_bits == 0:
        return 0.0
    ones = sum(word.bit_count() for word in words)
    return ones / total_bits


def analyze_params(
    params: XorShiftParams,
    seeds: Sequence[int],
    words: int,
    neighbor_bits: int,
) -> dict:
    paired_distances: List[float] = []
    base_frequencies: List[float] = []
    neighbor_frequencies: List[float] = []

    for seed in seeds:
        base = stream(seed, params, words)
        base_frequencies.append(bit_frequency(base))
        for neighbor in one_bit_neighbors(seed, neighbor_bits):
            perturbed = stream(neighbor, params, words)
            distance = hamming_words(base, perturbed) / (32 * words)
            paired_distances.append(distance)
            neighbor_frequencies.append(bit_frequency(perturbed))

    return {
        "parameter_label": params.label,
        "seed_count": len(seeds),
        "neighbor_count_per_seed": neighbor_bits,
        "output_words": words,
        "paired_hamming_distance": summarize(paired_distances),
        "base_bit_frequency": summarize(base_frequencies),
        "neighbor_bit_frequency": summarize(neighbor_frequencies),
    }


def summarize(values: Sequence[float]) -> dict:
    ordered = sorted(values)
    if not ordered:
        return {"count": 0}
    return {
        "count": len(ordered),
        "min": round(ordered[0], 8),
        "mean": round(sum(ordered) / len(ordered), 8),
        "max": round(ordered[-1], 8),
        "p05": round(percentile(ordered, 0.05), 8),
        "p50": round(percentile(ordered, 0.50), 8),
        "p95": round(percentile(ordered, 0.95), 8),
    }


def percentile(ordered: Sequence[float], q: float) -> float:
    if len(ordered) == 1:
        return ordered[0]
    pos = q * (len(ordered) - 1)
    low = int(pos)
    high = min(low + 1, len(ordered) - 1)
    weight = pos - low
    return ordered[low] * (1.0 - weight) + ordered[high] * weight


def parse_params(raw_values: Sequence[str]) -> List[XorShiftParams]:
    parsed: List[XorShiftParams] = []
    for raw in raw_values:
        parts = tuple(int(part) for part in raw.split(","))
        if len(parts) != 3:
            raise ValueError(f"invalid parameter triple: {raw!r}")
        parsed.append(XorShiftParams(*parts))
    return parsed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=32)
    parser.add_argument("--words", type=int, default=128)
    parser.add_argument("--neighbor-bits", type=int, default=16)
    parser.add_argument(
        "--params",
        action="append",
        default=["13,17,5", "7,9,13", "5,3,17"],
        help="xorshift32 parameter triple left,right,left; can be repeated",
    )
    args = parser.parse_args()

    if args.seeds <= 0:
        raise ValueError("--seeds must be positive")
    if args.words <= 0:
        raise ValueError("--words must be positive")
    if not 1 <= args.neighbor_bits <= 32:
        raise ValueError("--neighbor-bits must be in [1, 32]")

    seeds = deterministic_seeds(args.seeds)
    params_grid = parse_params(args.params)
    results = [analyze_params(params, seeds, args.words, args.neighbor_bits) for params in params_grid]

    print(
        json.dumps(
            {
                "status": "computational-evidence",
                "generator": "xorshift32-reference-not-cryptographic",
                "seed_model": "sha256-derived deterministic seeds",
                "perturbation_rule": "one-bit seed flips",
                "parameter_control": "finite parameter grid",
                "results": results,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
