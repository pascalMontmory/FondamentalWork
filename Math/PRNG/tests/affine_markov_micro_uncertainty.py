#!/usr/bin/env python3
"""CryptoVar-aligned affine Markov micro-uncertainty harness.

This is a local diagnostic scaffold inspired by the public CryptoVar API
parameter vocabulary. It does not call the API and does not verify the
production implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple


@dataclass(frozen=True)
class AffineParams:
    a: int
    b: int
    m: int
    q: int
    lag: int

    @property
    def label(self) -> str:
        return f"affine(a={self.a},b={self.b},m={self.m},q={self.q},lag={self.lag})"


def derive_seed(label: str, m: int) -> int:
    digest = hashlib.sha256(label.encode()).digest()
    return int.from_bytes(digest[:8], "big") % (m - 1) + 1


def deterministic_seeds(count: int, m: int) -> List[int]:
    return [derive_seed(f"cryptovar-affine-seed:{idx}", m) for idx in range(count)]


def one_bit_neighbors(seed: int, bits: int, m: int) -> Iterable[int]:
    for bit in range(bits):
        candidate = seed ^ (1 << bit)
        yield candidate % (m - 1) + 1


def affine_classes(seed: int, params: AffineParams, n: int) -> List[int]:
    state = seed % params.m
    classes: List[int] = []
    for _ in range(n):
        state = (params.a * state + params.b) % params.m
        classes.append(min(params.q - 1, (params.q * state) // params.m))
    return classes


def transition_counts(classes: Sequence[int], q: int, lag: int) -> List[List[int]]:
    counts = [[0 for _ in range(q)] for _ in range(q)]
    for idx in range(max(0, len(classes) - lag)):
        counts[classes[idx]][classes[idx + lag]] += 1
    return counts


def class_counts(classes: Sequence[int], q: int) -> List[int]:
    counts = [0 for _ in range(q)]
    for cls in classes:
        counts[cls] += 1
    return counts


def normalized_l1(left: Sequence[int], right: Sequence[int]) -> float:
    denom = sum(left) + sum(right)
    if denom == 0:
        return 0.0
    return sum(abs(a - b) for a, b in zip(left, right)) / denom


def chi_square_uniform(counts: Sequence[int]) -> float:
    total = sum(counts)
    if total == 0:
        return 0.0
    expected = total / len(counts)
    return sum(((count - expected) ** 2) / expected for count in counts)


def uniform_invariance_sup(counts: Sequence[int]) -> float:
    total = sum(counts)
    if total == 0:
        return 0.0
    expected = 1.0 / len(counts)
    return max(abs((count / total) - expected) for count in counts)


def analyze_params(params: AffineParams, seeds: Sequence[int], n: int, neighbor_bits: int) -> Dict[str, object]:
    chi2_values: List[float] = []
    uniform_sup_values: List[float] = []
    seed_l1_values: List[float] = []
    visited_values: List[int] = []

    for seed in seeds:
        base_classes = affine_classes(seed, params, n)
        base_counts = class_counts(base_classes, params.q)
        chi2_values.append(chi_square_uniform(base_counts))
        uniform_sup_values.append(uniform_invariance_sup(base_counts))
        visited_values.append(sum(1 for count in base_counts if count > 0))

        for neighbor in one_bit_neighbors(seed, neighbor_bits, params.m):
            neighbor_classes = affine_classes(neighbor, params, n)
            neighbor_counts = class_counts(neighbor_classes, params.q)
            seed_l1_values.append(normalized_l1(base_counts, neighbor_counts))

    return {
        "parameter_label": params.label,
        "seed_count": len(seeds),
        "neighbor_count_per_seed": neighbor_bits,
        "diagnostic_n": n,
        "class_chi2": summarize(chi2_values),
        "uniform_invariance_sup": summarize(uniform_sup_values),
        "seed_perturbation_l1": summarize(seed_l1_values),
        "visited_classes": summarize_int(visited_values),
    }


def summarize(values: Sequence[float]) -> Dict[str, float | int]:
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


def summarize_int(values: Sequence[int]) -> Dict[str, float | int]:
    summary = summarize([float(value) for value in values])
    for key in ("min", "max"):
        if key in summary:
            summary[key] = int(summary[key])
    return summary


def percentile(ordered: Sequence[float], q: float) -> float:
    if len(ordered) == 1:
        return ordered[0]
    pos = q * (len(ordered) - 1)
    low = int(pos)
    high = min(low + 1, len(ordered) - 1)
    weight = pos - low
    return ordered[low] * (1.0 - weight) + ordered[high] * weight


def parse_params(raw_values: Sequence[str]) -> List[AffineParams]:
    parsed: List[AffineParams] = []
    for raw in raw_values:
        parts = tuple(int(part) for part in raw.split(","))
        if len(parts) != 5:
            raise ValueError(f"invalid parameter tuple: {raw!r}")
        parsed.append(AffineParams(*parts))
    return parsed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=32)
    parser.add_argument("--diagnostic-n", type=int, default=2048)
    parser.add_argument("--neighbor-bits", type=int, default=16)
    parser.add_argument(
        "--params",
        action="append",
        default=["16807,0,2147483647,64,1", "5,3,2147483647,64,1"],
        help="affine tuple a,b,m,q,lag; can be repeated",
    )
    args = parser.parse_args()

    if args.seeds <= 0:
        raise ValueError("--seeds must be positive")
    if args.diagnostic_n <= 1:
        raise ValueError("--diagnostic-n must be greater than 1")
    if not 1 <= args.neighbor_bits <= 32:
        raise ValueError("--neighbor-bits must be in [1, 32]")

    params_grid = parse_params(args.params)
    modulus_values = {params.m for params in params_grid}
    if len(modulus_values) != 1:
        raise ValueError("all parameter tuples must use the same modulus for this harness")

    modulus = next(iter(modulus_values))
    seeds = deterministic_seeds(args.seeds, modulus)
    results = [
        analyze_params(params, seeds, args.diagnostic_n, args.neighbor_bits)
        for params in params_grid
    ]

    print(
        json.dumps(
            {
                "status": "computational-evidence",
                "generator_family": "affine-modular-markov-reference",
                "seed_model": "sha256-derived deterministic seeds reduced modulo m-1 plus 1",
                "perturbation_rule": "one-bit caller-seed flips then reduction modulo m-1 plus 1",
                "parameter_control": "finite affine parameter grid",
                "results": results,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
