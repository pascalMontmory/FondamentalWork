#!/usr/bin/env python3
"""Measure the primitive Gaussian and twin-shift cover layers.

For each n, compute:

    |I_n|
    |G(n) cap I_n|
    |G(n) cap T(n) cap I_n^(*) cap I_n^+|

using the exact primality interpretation on the primitive channel.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt

from gaussian_band_probe import is_prime


@dataclass(frozen=True)
class LayerMeasure:
    n: int
    primitive_count: int
    gaussian_bad_count: int
    interior_nonmultiple_count: int
    double_bad_count: int
    first_gaussian_escape: int | None
    first_double_escape: int | None


def primitive_channel(n: int) -> list[int]:
    return [
        t
        for t in range(1, isqrt(2 * n) + 1)
        if gcd(n, t) == 1 and (n + t) % 2 == 1
    ]


def measure_n(n: int) -> LayerMeasure:
    primitive = primitive_channel(n)
    gaussian_bad = []
    double_domain = []
    double_bad = []
    first_gaussian_escape = None
    first_double_escape = None

    for t in primitive:
        gaussian_value = n * n + t * t
        is_gaussian_bad = not is_prime(gaussian_value)
        if is_gaussian_bad:
            gaussian_bad.append(t)
        elif first_gaussian_escape is None:
            first_gaussian_escape = t

        if n % 3 != 0 and t % 3 != 0 and t * t + 2 <= 2 * n:
            double_domain.append(t)
            twin_value = gaussian_value + 2
            is_double_bad = is_gaussian_bad and not is_prime(twin_value)
            if is_double_bad:
                double_bad.append(t)
            elif first_double_escape is None:
                first_double_escape = t

    return LayerMeasure(
        n=n,
        primitive_count=len(primitive),
        gaussian_bad_count=len(gaussian_bad),
        interior_nonmultiple_count=len(double_domain),
        double_bad_count=len(double_bad),
        first_gaussian_escape=first_gaussian_escape,
        first_double_escape=first_double_escape,
    )


def run(limit: int, show_records: bool, show_layer_survivors: int) -> int:
    gaussian_cover_holds = []
    double_cover_holds = []
    primitive_survivors = []
    killed_by_gaussian = 0
    killed_by_double = 0
    max_gaussian_bad = LayerMeasure(0, 0, 0, 0, 0, None, None)
    max_double_bad = LayerMeasure(0, 0, 0, 0, 0, None, None)
    max_primitive = LayerMeasure(0, 0, 0, 0, 0, None, None)

    for n in range(2, limit + 1):
        item = measure_n(n)
        if item.primitive_count > max_primitive.primitive_count:
            max_primitive = item
        if item.gaussian_bad_count > max_gaussian_bad.gaussian_bad_count:
            max_gaussian_bad = item
        if item.double_bad_count > max_double_bad.double_bad_count:
            max_double_bad = item
        if item.primitive_count and item.gaussian_bad_count == item.primitive_count:
            gaussian_cover_holds.append(item)
            if n % 3 == 0:
                primitive_survivors.append(item)
            elif item.double_bad_count == item.interior_nonmultiple_count:
                primitive_survivors.append(item)
            else:
                killed_by_double += 1
        else:
            killed_by_gaussian += 1
        if (
            item.interior_nonmultiple_count
            and item.double_bad_count == item.interior_nonmultiple_count
        ):
            double_cover_holds.append(item)

    print(f"checked n=2..{limit}")
    print(f"gaussian_full_cover_count={len(gaussian_cover_holds)}")
    print(f"double_full_cover_count={len(double_cover_holds)}")
    print(f"killed_by_gaussian_layer={killed_by_gaussian}")
    print(f"killed_by_double_layer_after_gaussian={killed_by_double}")
    print(f"primitive_double_cover_survivors={len(primitive_survivors)}")
    print(
        "max_primitive="
        f"n={max_primitive.n}, |I_n|={max_primitive.primitive_count}, "
        f"|G cap I|={max_primitive.gaussian_bad_count}"
    )
    print(
        "max_gaussian_bad="
        f"n={max_gaussian_bad.n}, |I_n|={max_gaussian_bad.primitive_count}, "
        f"|G cap I|={max_gaussian_bad.gaussian_bad_count}, "
        f"first_escape={max_gaussian_bad.first_gaussian_escape}"
    )
    print(
        "max_double_bad="
        f"n={max_double_bad.n}, domain={max_double_bad.interior_nonmultiple_count}, "
        f"double_bad={max_double_bad.double_bad_count}, "
        f"first_escape={max_double_bad.first_double_escape}"
    )

    if show_layer_survivors:
        print("gaussian_full_cover_examples:")
        for item in gaussian_cover_holds[:show_layer_survivors]:
            print(
                f"  n={item.n}, |I_n|={item.primitive_count}, "
                f"double_domain={item.interior_nonmultiple_count}, "
                f"double_bad={item.double_bad_count}, "
                f"first_double_escape={item.first_double_escape}"
            )
        print("double_full_cover_examples:")
        for item in double_cover_holds[:show_layer_survivors]:
            print(
                f"  n={item.n}, |I_n|={item.primitive_count}, "
                f"|G cap I|={item.gaussian_bad_count}, "
                f"domain={item.interior_nonmultiple_count}"
            )
        print("primitive_double_cover_survivors:")
        for item in primitive_survivors[:show_layer_survivors]:
            print(
                f"  n={item.n}, |I_n|={item.primitive_count}, "
                f"|G cap I|={item.gaussian_bad_count}, "
                f"domain={item.interior_nonmultiple_count}, "
                f"double_bad={item.double_bad_count}, "
                f"n_mod_3={item.n % 3}"
            )

    if show_records:
        print("records:")
        for item in [max_primitive, max_gaussian_bad, max_double_bad]:
            print(
                f"  n={item.n}, |I_n|={item.primitive_count}, "
                f"|G cap I|={item.gaussian_bad_count}, "
                f"domain={item.interior_nonmultiple_count}, "
                f"double_bad={item.double_bad_count}, "
                f"first_G_escape={item.first_gaussian_escape}, "
                f"first_double_escape={item.first_double_escape}"
            )

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--records", action="store_true")
    parser.add_argument("--show-layer-survivors", type=int, default=20)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raise SystemExit(run(args.limit, args.records, args.show_layer_survivors))


if __name__ == "__main__":
    main()
