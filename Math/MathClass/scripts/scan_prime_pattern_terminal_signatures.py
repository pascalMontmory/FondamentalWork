#!/usr/bin/env python3
"""Prime-pattern terminal signature scan.

Reports finite-N distances for prime patterns (twin, cousin, sexy) against
prime, non-pattern primes, odd integers, and admissible modulo controls.
The output is diagnostic, not an asymptotic proof.
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
    parser.add_argument("--patterns", default="twin,cousin,sexy")
    parser.add_argument("--controls", default="prime,prime_non_twin,odd,admissible_30,admissible_210,admissible_2310")
    parser.add_argument("--terminal-set", default="")
    parser.add_argument("--max-steps", type=int, default=10_000)
    args = parser.parse_args()

    limits = parse_ints(args.limits)
    bounds = parse_ints(args.bounds)
    patterns = [part for part in args.patterns.split(",") if part]
    controls = [part for part in args.controls.split(",") if part]
    terminal_set = {item.strip() for item in args.terminal_set.split(",") if item.strip()}

    print("kind,pattern,bound,N,value,control,verdict")
    previous: dict[tuple[str, int], dict[str, float]] = {}
    previous_limit: dict[tuple[str, int], int] = {}
    for limit in limits:
        samples = build_samples(limit)
        laws = {
            (name, bound): law(samples[name].values, bound, args.max_steps)
            for name in set(patterns + controls)
            for bound in bounds
        }
        for pattern in patterns:
            for bound in bounds:
                current = laws[(pattern, bound)]
                key = (pattern, bound)
                if key in previous:
                    value = tv(previous[key], current)
                    print(
                        f"stability,{pattern},{bound},{previous_limit[key]}->{limit},"
                        f"{value:.17g},,diagnostic"
                    )
                previous[key] = current
                previous_limit[key] = limit

                for control in controls:
                    if control == pattern:
                        continue
                    value = tv(current, laws[(control, bound)])
                    print(f"control_distance,{pattern},{bound},{limit},{value:.17g},{control},diagnostic")

                if terminal_set:
                    mass = sum(current.get(state, 0.0) for state in terminal_set)
                    print(f"terminal_filter_mass,{pattern},{bound},{limit},{mass:.17g},{args.terminal_set},diagnostic")

        for name in patterns + controls:
            print(f"sample_size,{name},,{limit},{len(samples[name].values)},,diagnostic")


if __name__ == "__main__":
    main()
