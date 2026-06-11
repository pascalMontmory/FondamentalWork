#!/usr/bin/env python3
"""Probe one endpoint d-6 CRT class with a retained class parameter t.

The residue CRT sieve localizes possible exceptional integers to classes

    n = c mod M.

This script substitutes n = c + M t and works modulo a coefficient prime p
with p not dividing M.  It then rebuilds the four equation-level eliminants
and computes their gcd in F_p(t)[a].

If that gcd has degree 0 in a, the whole CRT class is generically eliminated.
The faster --scan-t mode looks for good t-specializations with gcd 0; these
are generic-elimination witnesses, leaving only the finite bad t-fibers where
denominators, leading coefficients, or specialization resultants degenerate.
If every scanned specialization stays live, the class needs stronger
extraction.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

import sympy as sp

from endpoint_d6_cover_degrees import h_polynomials
from endpoint_d6_exceptional_crt_classes import (
    bad_residues as saturated_bad_n_residues,
    build_crt_classes,
    display_classes,
    live_residues,
)
from endpoint_d6_equation_modular_probe import (
    COVERS,
    DEFAULT_TYPES,
    ORDERS,
    determinant_expr,
    line_quadratic_resultant_expr,
    specialized_gcd_degree,
)


DEFAULT_PRIME = 1009
DEFAULT_CLASS = (0, 2431)
DEFAULT_BASE_PRIMES = [11, 13, 17]
DEFAULT_T_PRIMES = [101, 103]
DEFAULT_LIMIT_CLASSES = 20


def parse_args() -> tuple[
    list[tuple[int, int, int, int]],
    int,
    tuple[int, int],
    list[int],
    bool,
    bool,
    bool,
    bool,
    list[int],
    int,
    int | None,
]:
    args = sys.argv[1:]
    prime = DEFAULT_PRIME
    cls = DEFAULT_CLASS
    base_primes = DEFAULT_BASE_PRIMES
    build_only = "--build-only" in args
    scan_t = "--scan-t" in args
    collect_t = "--collect-t" in args
    scan_base_classes = "--scan-base-classes" in args
    collect_base_t = "--collect-base-t" in args
    args = [arg for arg in args if arg != "--build-only"]
    args = [arg for arg in args if arg != "--scan-t"]
    args = [arg for arg in args if arg != "--collect-t"]
    args = [arg for arg in args if arg != "--scan-base-classes"]
    args = [arg for arg in args if arg != "--collect-base-t"]
    max_t = None
    t_primes = DEFAULT_T_PRIMES
    limit_classes = DEFAULT_LIMIT_CLASSES
    for arg in list(args):
        if arg.startswith("--prime="):
            prime = int(arg.removeprefix("--prime="))
            args.remove(arg)
        elif arg.startswith("--base-primes="):
            base_primes = [int(part) for part in arg.removeprefix("--base-primes=").split(",")]
            args.remove(arg)
        elif arg.startswith("--t-primes="):
            t_primes = [int(part) for part in arg.removeprefix("--t-primes=").split(",")]
            args.remove(arg)
        elif arg.startswith("--class="):
            raw_class = arg.removeprefix("--class=")
            residue, modulus = raw_class.split(",")
            cls = (int(residue), int(modulus))
            args.remove(arg)
        elif arg.startswith("--max-t="):
            max_t = int(arg.removeprefix("--max-t="))
            args.remove(arg)
        elif arg.startswith("--limit-classes="):
            limit_classes = int(arg.removeprefix("--limit-classes="))
            args.remove(arg)

    weights_list = DEFAULT_TYPES if not args else [
        tuple(int(part) for part in arg.split(",")) for arg in args
    ]
    return (
        weights_list,
        prime,
        cls,
        base_primes,
        build_only,
        scan_t,
        collect_t,
        scan_base_classes,
        collect_base_t,
        t_primes,
        limit_classes,
        max_t,
    )


@dataclass(frozen=True)
class TScan:
    witness: tuple[int, int] | None
    live_t: tuple[tuple[int, int, int], ...]
    bad_t: tuple[tuple[int, int], ...]


def reduce_mod_f(
    expr: sp.Expr,
    f: sp.Poly,
    y: sp.Symbol,
    domain: sp.Domain,
) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    reduced = sp.Poly(numerator, y, domain=domain).rem(f)
    reduced_numerator = sp.together(reduced.as_expr()).as_numer_denom()[0]
    return sp.Poly(reduced_numerator, y, domain=domain)


def reduced_cover_products_class(
    weights: tuple[int, int, int, int],
    n_expr: sp.Expr,
    t: sp.Symbol,
    a: sp.Symbol,
    y: sp.Symbol,
    x: sp.Symbol,
    prime: int,
) -> tuple[sp.Poly, dict[int, sp.Poly]]:
    domain = sp.GF(prime).frac_field(t, a)
    f_expr, h_by_order, cover_exprs = h_polynomials(n_expr, a, y, x, *weights)
    f = sp.Poly(f_expr.as_expr(), y, domain=domain)
    products = {}

    for order in ORDERS:
        print(f"    building R{order}", flush=True)
        product = sp.Poly(1, y, domain=domain)
        for cover_name in COVERS:
            condition = reduce_mod_f(
                h_by_order[order].subs(x, cover_exprs[cover_name]),
                f,
                y,
                domain,
            )
            product = reduce_mod_f(
                product.as_expr() * condition.as_expr(),
                f,
                y,
                domain,
            )
        products[order] = product
        print(f"    built R{order}: degree_y={product.degree()}", flush=True)

    return f, products


def poly_in_a_over_ft(expr: sp.Expr, t: sp.Symbol, a: sp.Symbol, prime: int) -> sp.Poly:
    numerator = sp.together(expr).as_numer_denom()[0]
    coeff_domain = sp.GF(prime).frac_field(t)
    return sp.Poly(numerator, a, domain=coeff_domain)


def build_eliminants(
    weights: tuple[int, int, int, int],
    cls: int,
    modulus: int,
    prime: int,
) -> tuple[list[sp.Poly], sp.Symbol]:
    if modulus % prime == 0:
        raise ValueError(f"prime {prime} divides class modulus {modulus}")

    t, a, y, x = sp.symbols("t a y x")
    n_expr = cls + modulus * t
    f, products = reduced_cover_products_class(weights, n_expr, t, a, y, x, prime)
    base = products[3]
    exprs = [
        line_quadratic_resultant_expr(f, base, y),
        determinant_expr(base, products[4], y),
        determinant_expr(base, products[5], y),
        determinant_expr(base, products[6], y),
    ]

    eliminants = []
    for index, expr in enumerate(exprs, start=1):
        print(f"  forming E{index}", flush=True)
        eliminant = poly_in_a_over_ft(expr, t, a, prime)
        eliminants.append(eliminant)
        print(
            f"  formed E{index}: degree_a={eliminant.degree()}",
            flush=True,
        )
    return eliminants, t


def gcd_in_a(eliminants: list[sp.Poly]) -> sp.Poly:
    nonzero = [poly for poly in eliminants if not poly.is_zero]
    if not nonzero:
        raise ValueError("all eliminants vanished over F_p(t)[a]")

    gcd = nonzero[0]
    for eliminant in nonzero[1:]:
        gcd = sp.gcd(gcd, eliminant)
        print(f"    running gcd degree_a={gcd.degree()}", flush=True)
        if gcd.degree() == 0:
            break
    return gcd


def bad_n_residues(prime: int) -> set[int]:
    return {(-offset) % prime for offset in range(1, 7)}


def residue_factor(residues: list[int], symbol: sp.Symbol, prime: int) -> sp.Poly:
    poly = sp.Poly(1, symbol, modulus=prime)
    for residue in residues:
        poly *= sp.Poly(symbol - residue, symbol, modulus=prime)
    return sp.Poly(poly.as_expr(), symbol, modulus=prime)


def format_residue_factor(poly: sp.Poly, prime: int) -> str:
    if poly.degree() == 0:
        return "1"
    return str(sp.factor(poly.as_expr(), modulus=prime))


def scan_t_specializations(
    weights: tuple[int, int, int, int],
    prime: int,
    cls: int,
    modulus: int,
    max_t: int | None,
    verbose: bool = True,
    stop_at_witness: bool = True,
) -> TScan:
    if modulus % prime == 0:
        raise ValueError(f"prime {prime} divides class modulus {modulus}")

    limit = prime if max_t is None else min(max_t, prime)
    bad_n = bad_n_residues(prime)
    witness = None
    live_t = []
    bad_t = []
    if verbose:
        print(
            f"weights {weights}, scanning n={cls}+{modulus}*t mod {prime}, "
            f"t=0..{limit - 1}",
            flush=True,
        )
    for t_value in range(limit):
        n_value = (cls + modulus * t_value) % prime
        if n_value in bad_n:
            bad_t.append((t_value, n_value))
            if verbose:
                print(f"  t={t_value}: n={n_value} is saturated-bad; skipped", flush=True)
            continue
        gcd_degree, eliminant_degrees = specialized_gcd_degree(weights, n_value, prime)
        if verbose:
            print(
                f"  t={t_value}: n={n_value}, gcd_degree={gcd_degree}, "
                f"eliminant_degrees={eliminant_degrees}",
                flush=True,
            )
        if gcd_degree == 0:
            if witness is None:
                witness = (t_value, n_value)
            if verbose and stop_at_witness:
                print(
                    "  specialization witness: generic gcd in F_p(t)[a] is 1 away from finite bad t-fibers",
                    flush=True,
                )
                print("  CRT class generically eliminated over this prime up to finite t-exceptions", flush=True)
            if stop_at_witness:
                return TScan(witness, tuple(live_t), tuple(bad_t))
        else:
            live_t.append((t_value, n_value, gcd_degree))

    if verbose and witness is None:
        print("  no gcd-1 t-specialization found in scanned range", flush=True)
    if verbose and not stop_at_witness:
        t_symbol = sp.symbols("t")
        live_factor = residue_factor([item[0] for item in live_t], t_symbol, prime)
        bad_factor = residue_factor([item[0] for item in bad_t], t_symbol, prime)
        print(f"  live t residues in scanned range: {live_t}", flush=True)
        print(f"  saturated-bad t residues in scanned range: {bad_t}", flush=True)
        print(
            f"  live t factor in F_{prime}[t]: "
            f"degree={live_factor.degree()}, {format_residue_factor(live_factor, prime)}",
            flush=True,
        )
        print(
            f"  saturated-bad t factor in F_{prime}[t]: "
            f"degree={bad_factor.degree()}, {format_residue_factor(bad_factor, prime)}",
            flush=True,
        )
    return TScan(witness, tuple(live_t), tuple(bad_t))


def scan_base_classes(
    weights: tuple[int, int, int, int],
    prime: int,
    base_primes: list[int],
    max_t: int | None,
) -> None:
    modulus, classes = build_crt_classes(weights, base_primes)
    print(
        f"weights {weights}, base primes={base_primes}, "
        f"{len(classes)} classes mod {modulus}, scan prime={prime}",
        flush=True,
    )
    failures = []
    witness_counts: dict[int, int] = {}
    for index, cls in enumerate(classes, start=1):
        scan = scan_t_specializations(weights, prime, cls, modulus, max_t, verbose=False)
        if scan.witness is None:
            print(f"  class {index}/{len(classes)}: n={cls} mod {modulus}: open", flush=True)
            failures.append(cls)
        else:
            t_value, n_value = scan.witness
            witness_counts[t_value] = witness_counts.get(t_value, 0) + 1
            print(
                f"  class {index}/{len(classes)}: n={cls} mod {modulus}: "
                f"witness t={t_value}, n={n_value} mod {prime}",
                flush=True,
            )

    if failures:
        print(
            f"  open classes: {display_classes(failures, modulus, 40)}",
            flush=True,
        )
    else:
        print("  all base CRT classes have generic-elimination witnesses", flush=True)
    print(f"  witness t distribution: {dict(sorted(witness_counts.items()))}", flush=True)


def t_residues_from_n_residues(
    cls: int,
    modulus: int,
    residues: tuple[int, ...] | set[int],
    prime: int,
) -> list[int]:
    if modulus % prime == 0:
        raise ValueError(f"prime {prime} divides class modulus {modulus}")
    inverse = pow(modulus % prime, -1, prime)
    return sorted({((residue - cls) * inverse) % prime for residue in residues})


def collect_base_t_fibers(
    weights: tuple[int, int, int, int],
    base_primes: list[int],
    t_primes: list[int],
    limit_classes: int,
) -> None:
    modulus, classes = build_crt_classes(weights, base_primes)
    print(
        f"weights {weights}, base primes={base_primes}, "
        f"{len(classes)} classes mod {modulus}",
        flush=True,
    )

    prime_data = {}
    for prime in t_primes:
        live_n, gcd_degrees = live_residues(weights, prime)
        bad_n = saturated_bad_n_residues(prime)
        live_factor = residue_factor(list(live_n), sp.symbols("n"), prime)
        print(
            f"  t-prime={prime}: live_n={list(live_n)}, bad_n={sorted(bad_n)}, "
            f"live_n_factor_degree={live_factor.degree()}",
            flush=True,
        )
        print(f"    gcd_degrees={dict(gcd_degrees)}", flush=True)
        prime_data[prime] = (live_n, bad_n)

    total_descendants = 0
    per_prime_totals = {prime: 0 for prime in t_primes}
    for index, cls in enumerate(classes, start=1):
        class_descendants = 1
        class_lines = []
        for prime in t_primes:
            live_n, bad_n = prime_data[prime]
            live_t = t_residues_from_n_residues(cls, modulus, live_n, prime)
            bad_t = t_residues_from_n_residues(cls, modulus, bad_n, prime)
            class_descendants *= len(live_t)
            per_prime_totals[prime] += len(live_t)
            if index <= limit_classes:
                t = sp.symbols("t")
                factor = residue_factor(live_t, t, prime)
                class_lines.append(
                    f"p={prime}: live_t={live_t}, bad_t={bad_t}, "
                    f"T_degree={factor.degree()}, T={format_residue_factor(factor, prime)}"
                )
        total_descendants += class_descendants
        if index <= limit_classes:
            print(
                f"  class {index}/{len(classes)}: n={cls} mod {modulus}; "
                f"descendants over {t_primes}={class_descendants}",
                flush=True,
            )
            for line in class_lines:
                print(f"    {line}", flush=True)

    if len(classes) > limit_classes:
        print(f"  ... {len(classes) - limit_classes} classes omitted from detailed output", flush=True)
    print(f"  per-prime total live t residues: {per_prime_totals}", flush=True)
    print(
        f"  total CRT descendants over t-primes {t_primes}: {total_descendants}",
        flush=True,
    )
    print(
        "  note: nonempty live t sets combine by CRT; this refines finite fibers but does not empty them by itself",
        flush=True,
    )


def probe_class(
    weights: tuple[int, int, int, int],
    prime: int,
    cls: int,
    modulus: int,
    build_only: bool,
) -> None:
    print(
        f"weights {weights}, class n={cls} mod {modulus}, prime={prime}",
        flush=True,
    )
    eliminants, t = build_eliminants(weights, cls, modulus, prime)
    print(
        "  eliminant degrees in a: "
        + ", ".join(str(poly.degree()) for poly in eliminants),
        flush=True,
    )
    if build_only:
        return

    gcd = gcd_in_a(eliminants)
    print(f"  gcd degree in a over F_{prime}(t): {gcd.degree()}", flush=True)
    if gcd.degree() == 0:
        print("  class generically eliminated over F_p(t)", flush=True)
    else:
        print(
            f"  class has a generic common factor; degree_t_hint={sp.Poly(gcd.as_expr(), t).degree()}",
            flush=True,
        )


def main() -> None:
    (
        weights_list,
        prime,
        (cls, modulus),
        base_primes,
        build_only,
        scan_t,
        collect_t,
        scan_base_classes_mode,
        collect_base_t_mode,
        t_primes,
        limit_classes,
        max_t,
    ) = parse_args()
    for weights in weights_list:
        if collect_base_t_mode:
            collect_base_t_fibers(weights, base_primes, t_primes, limit_classes)
        elif scan_base_classes_mode:
            scan_base_classes(weights, prime, base_primes, max_t)
        elif scan_t or collect_t:
            scan_t_specializations(
                weights,
                prime,
                cls,
                modulus,
                max_t,
                stop_at_witness=not collect_t,
            )
        else:
            probe_class(weights, prime, cls, modulus, build_only)


if __name__ == "__main__":
    main()
