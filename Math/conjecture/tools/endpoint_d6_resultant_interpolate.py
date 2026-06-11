#!/usr/bin/env python3
"""Interpolate endpoint d-6 pairwise resultants modulo a coefficient prime.

Direct symbolic resultants in a are too large for SymPy on the d-6
equation-level eliminants.  This script evaluates one pairwise resultant at
many n-values over F_p and interpolates the univariate polynomial in n.
"""

from __future__ import annotations

import sys

import sympy as sp

from endpoint_d6_equation_modular_probe import (
    determinant_expr,
    line_quadratic_resultant_expr,
    reduced_cover_products_mod,
)


DEFAULT_PRIME = 1009
DEFAULT_SAMPLES = 40


def parse_args() -> tuple[tuple[int, int, int, int], int, int, tuple[int, int]]:
    args = sys.argv[1:]
    prime = DEFAULT_PRIME
    samples = DEFAULT_SAMPLES
    pair = (0, 1)
    for arg in list(args):
        if arg.startswith("--prime="):
            prime = int(arg.removeprefix("--prime="))
            args.remove(arg)
        elif arg.startswith("--samples="):
            samples = int(arg.removeprefix("--samples="))
            args.remove(arg)
        elif arg.startswith("--pair="):
            left, right = arg.removeprefix("--pair=").split(",")
            pair = (int(left) - 1, int(right) - 1)
            args.remove(arg)
    if len(args) != 1:
        raise SystemExit("usage: endpoint_d6_resultant_interpolate.py [opts] m0,ma,my,mz")
    return tuple(int(part) for part in args[0].split(",")), prime, samples, pair


def poly_add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    result = [0] * size
    for index in range(size):
        result[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_mul_linear(poly: list[int], root: int, prime: int) -> list[int]:
    result = [0] * (len(poly) + 1)
    for index, coeff in enumerate(poly):
        result[index] = (result[index] - coeff * root) % prime
        result[index + 1] = (result[index + 1] + coeff) % prime
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def interpolate(xs: list[int], ys: list[int], prime: int) -> list[int]:
    coeffs = [value % prime for value in ys]
    for order in range(1, len(xs)):
        for index in range(len(xs) - 1, order - 1, -1):
            denominator = (xs[index] - xs[index - order]) % prime
            coeffs[index] = (
                (coeffs[index] - coeffs[index - 1]) * pow(denominator, -1, prime)
            ) % prime

    result = [0]
    basis = [1]
    for index, coeff in enumerate(coeffs):
        result = poly_add(result, [(coeff * item) % prime for item in basis], prime)
        basis = poly_mul_linear(basis, xs[index], prime)
    return result


def eval_poly(coeffs: list[int], value: int, prime: int) -> int:
    total = 0
    for coeff in reversed(coeffs):
        total = (total * value + coeff) % prime
    return total


def resultant_value(
    weights: tuple[int, int, int, int],
    n_value: int,
    prime: int,
    pair: tuple[int, int],
) -> int:
    a, y, x = sp.symbols("a y x")
    f, products = reduced_cover_products_mod(weights, n_value, a, y, x, prime)
    base = products[3]
    exprs = [
        line_quadratic_resultant_expr(f, base, y),
        determinant_expr(base, products[4], y),
        determinant_expr(base, products[5], y),
        determinant_expr(base, products[6], y),
    ]
    polys = [
        sp.Poly(sp.together(expr).as_numer_denom()[0], a, modulus=prime)
        for expr in exprs
    ]
    left, right = pair
    if polys[left].is_zero or polys[right].is_zero:
        return 0
    return int(sp.resultant(polys[left].as_expr(), polys[right].as_expr(), a) % prime)


def main() -> None:
    weights, prime, samples, pair = parse_args()
    xs = []
    ys = []
    n_value = 0
    print(f"weights {weights}, prime={prime}, pair=E{pair[0]+1},E{pair[1]+1}", flush=True)
    while len(xs) < samples:
        if (n_value + 1) % prime not in {0}:
            value = resultant_value(weights, n_value, prime, pair)
            xs.append(n_value)
            ys.append(value)
            print(f"  sample {len(xs)}: n={n_value}, value={value}", flush=True)
        n_value += 1

    coeffs = interpolate(xs, ys, prime)
    print(f"  interpolated degree <= {len(coeffs) - 1}", flush=True)
    checks = []
    for check_n in range(n_value, n_value + 5):
        actual = resultant_value(weights, check_n, prime, pair)
        predicted = eval_poly(coeffs, check_n, prime)
        checks.append((check_n, actual, predicted, actual == predicted))
    print(f"  checks: {checks}", flush=True)
    print(f"  leading coeffs: {list(reversed(coeffs[-10:]))}", flush=True)


if __name__ == "__main__":
    main()
