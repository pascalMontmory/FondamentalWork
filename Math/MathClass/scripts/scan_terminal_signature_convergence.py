#!/usr/bin/env python3
"""Experimental convergence scan for MathClass terminal signatures.

This script does not prove the existence of a terminal law.  It reports
finite-N stability:

    TV(nu_{B,F,N_i}, nu_{B,F,N_{i+1}})

and distances to controls such as odd integers and admissible modulo 210.
"""
from __future__ import annotations

import argparse
from mathclass_common import build_samples, law, tv


def parse_ints(raw: str) -> list[int]:
    return [int(part) for part in raw.split(",") if part.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limits", default="10000,30000,100000")
    parser.add_argument("--bounds", default="27,89,127")
    parser.add_argument("--families", default="odd,admissible_210,prime,twin,cousin,sexy")
    parser.add_argument("--controls", default="odd,admissible_210")
    parser.add_argument("--max-steps", type=int, default=10_000)
    args = parser.parse_args()

    limits = parse_ints(args.limits)
    bounds = parse_ints(args.bounds)
    families = [part for part in args.families.split(",") if part]
    controls = [part for part in args.controls.split(",") if part]

    rows: dict[tuple[str, int, int], dict[str, float]] = {}
    sizes: dict[tuple[str, int], int] = {}
    for limit in limits:
        samples = build_samples(limit)
        for family in set(families + controls):
            sizes[(family, limit)] = len(samples[family].values)
            for bound in bounds:
                rows[(family, bound, limit)] = law(samples[family].values, bound, args.max_steps)

    print("kind,family,bound,N_left,N_right,value,control,verdict")
    for family in families:
        for bound in bounds:
            for left, right in zip(limits, limits[1:]):
                value = tv(rows[(family, bound, left)], rows[(family, bound, right)])
                verdict = "diagnostic"
                print(f"stability,{family},{bound},{left},{right},{value:.17g},,{verdict}")
            for limit in limits:
                for control in controls:
                    if control == family:
                        continue
                    value = tv(rows[(family, bound, limit)], rows[(control, bound, limit)])
                    print(f"control_distance,{family},{bound},{limit},,{value:.17g},{control},diagnostic")
    for family in families:
        for limit in limits:
            print(f"sample_size,{family},,{limit},,{sizes[(family, limit)]},,diagnostic")


if __name__ == "__main__":
    main()
