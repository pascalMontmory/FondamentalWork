#!/usr/bin/env python3
"""Extract common a-roots on regular endpoint d-6 t-fibers.

After classifying local fibers in t, the regular-gcd fibers have no visible
degree drop and their specialized eliminants share a positive-degree gcd in
F_p[a].  For the representative fibers seen so far this gcd has degree one.
This script extracts the common root

    gcd(E_1,E_2,E_3,E_4) = a - A

and reports A together with simple degeneracy flags.
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_class_t_fiber_classify import (
    DEFAULT_CLASS,
    Fiber,
    classify_fibers,
    generic_degrees,
    scan_fibers,
)
from endpoint_d6_equation_modular_probe import (
    DEFAULT_TYPES,
    determinant_expr,
    line_quadratic_resultant_expr,
    reduced_cover_products_mod,
)


DEFAULT_PRIMES = [101, 103]


def parse_args() -> tuple[list[tuple[int, int, int, int]], tuple[int, int], list[int], int | None]:
    args = sys.argv[1:]
    cls = DEFAULT_CLASS
    primes = DEFAULT_PRIMES
    max_t = None
    for arg in list(args):
        if arg.startswith("--class="):
            residue, modulus = arg.removeprefix("--class=").split(",")
            cls = (int(residue), int(modulus))
            args.remove(arg)
        elif arg.startswith("--primes="):
            primes = [int(part) for part in arg.removeprefix("--primes=").split(",")]
            args.remove(arg)
        elif arg.startswith("--max-t="):
            max_t = int(arg.removeprefix("--max-t="))
            args.remove(arg)

    weights_list = DEFAULT_TYPES if not args else [
        tuple(int(part) for part in arg.split(",")) for arg in args
    ]
    return weights_list, cls, primes, max_t


def specialized_eliminants(
    weights: tuple[int, int, int, int],
    n_value: int,
    prime: int,
) -> list[sp.Poly]:
    a, y, x = sp.symbols("a y x")
    f, products = reduced_cover_products_mod(weights, n_value, a, y, x, prime)
    base = products[3]
    exprs = [
        line_quadratic_resultant_expr(f, base, y),
        determinant_expr(base, products[4], y),
        determinant_expr(base, products[5], y),
        determinant_expr(base, products[6], y),
    ]
    return [
        sp.Poly(sp.together(expr).as_numer_denom()[0], a, modulus=prime)
        for expr in exprs
    ]


def common_gcd(eliminants: list[sp.Poly]) -> sp.Poly:
    nonzero = [poly for poly in eliminants if not poly.is_zero]
    if not nonzero:
        raise ValueError("all eliminants vanished")

    gcd = nonzero[0]
    for eliminant in nonzero[1:]:
        gcd = sp.gcd(gcd, eliminant)
    return gcd.monic()


def linear_root(poly: sp.Poly, prime: int) -> int | None:
    if poly.degree() != 1:
        return None
    coeff_a, coeff_0 = [int(coeff) % prime for coeff in poly.all_coeffs()]
    return (-coeff_0 * pow(coeff_a, -1, prime)) % prime


def regular_fibers(
    weights: tuple[int, int, int, int],
    cls: int,
    modulus: int,
    prime: int,
    max_t: int | None,
) -> tuple[tuple[int, ...], list[Fiber]]:
    fibers, saturated_bad = scan_fibers(weights, cls, modulus, prime, max_t)
    categories = classify_fibers(fibers, saturated_bad)
    regular = [item for item in categories["regular_gcd"] if isinstance(item, Fiber)]
    return generic_degrees(fibers), regular


def report_prime(
    weights: tuple[int, int, int, int],
    cls: int,
    modulus: int,
    prime: int,
    max_t: int | None,
) -> None:
    expected, regular = regular_fibers(weights, cls, modulus, prime, max_t)
    print(
        f"  p={prime}: expected_degrees={expected}, regular_count={len(regular)}",
        flush=True,
    )
    roots = []
    saturated_a_bad = []
    for fiber in regular:
        eliminants = specialized_eliminants(weights, fiber.n_value, prime)
        gcd = common_gcd(eliminants)
        root = linear_root(gcd, prime)
        roots.append(root)
        if root == 0:
            saturated_a_bad.append(fiber.t_value)
        print(
            f"    t={fiber.t_value}, n={fiber.n_value}, "
            f"gcd_degree={gcd.degree()}, a_root={root}, "
            f"a_zero={root == 0}, gcd={gcd.as_expr()}",
            flush=True,
        )
    nonzero_roots = [root for root in roots if root is not None and root != 0]
    print(
        f"    root summary: linear={sum(root is not None for root in roots)}/"
        f"{len(roots)}, nonzero={len(nonzero_roots)}/{len(roots)}",
        flush=True,
    )
    if saturated_a_bad:
        print(f"    killed by a-saturation t={saturated_a_bad}", flush=True)


def main() -> None:
    weights_list, (cls, modulus), primes, max_t = parse_args()
    for weights in weights_list:
        print(f"weights {weights}, class n={cls}+{modulus}*t", flush=True)
        for prime in primes:
            report_prime(weights, cls, modulus, prime, max_t)


if __name__ == "__main__":
    main()
