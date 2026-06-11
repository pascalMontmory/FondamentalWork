#!/usr/bin/env python3
"""CRT refinement for endpoint d-6 exceptional n-specializations.

The residue sieve gives live residues modulo each coefficient prime.  This
script combines those residues into CRT classes and optionally refines a
single class, or all classes, by additional primes.

This is still a necessary-condition computation.  For a class n = c mod M and
an auxiliary prime q coprime to M, the parameter t in n = c + M t runs through
all residues modulo q.  Therefore a residue-only auxiliary prime usually
refines a class into sub-classes modulo Mq; it eliminates the class only when
no auxiliary live residue is compatible.
"""

from __future__ import annotations

import sys
from functools import cache

from sympy.ntheory.modular import crt

from endpoint_d6_equation_exceptional_residues import (
    combine_crt_classes,
    format_factor,
    live_degree,
    live_residue_factor,
)
from endpoint_d6_equation_modular_probe import DEFAULT_TYPES, specialized_gcd_degree


DEFAULT_BASE_PRIMES = [11, 13, 17]
DEFAULT_AUX_PRIMES = [19, 23]
DEFAULT_LIMIT = 40


def parse_args() -> tuple[
    list[tuple[int, int, int, int]],
    list[int],
    list[int],
    bool,
    bool,
    tuple[int, int] | None,
    int,
]:
    args = sys.argv[1:]
    base_primes = DEFAULT_BASE_PRIMES
    aux_primes = DEFAULT_AUX_PRIMES
    show_classes = "--classes" in args
    refine_all = "--refine-all" in args
    probe_class = None
    limit = DEFAULT_LIMIT
    args = [arg for arg in args if arg not in {"--classes", "--refine-all"}]

    for arg in list(args):
        if arg.startswith("--base-primes="):
            base_primes = [int(part) for part in arg.removeprefix("--base-primes=").split(",")]
            args.remove(arg)
        elif arg.startswith("--aux-primes="):
            aux_primes = [int(part) for part in arg.removeprefix("--aux-primes=").split(",")]
            args.remove(arg)
        elif arg.startswith("--probe-class="):
            raw_class = arg.removeprefix("--probe-class=")
            cls, modulus = raw_class.split(",")
            probe_class = (int(cls), int(modulus))
            args.remove(arg)
        elif arg.startswith("--limit="):
            limit = int(arg.removeprefix("--limit="))
            args.remove(arg)

    if not show_classes and not refine_all and probe_class is None:
        show_classes = True

    weights_list = DEFAULT_TYPES if not args else [
        tuple(int(part) for part in arg.split(",")) for arg in args
    ]
    return weights_list, base_primes, aux_primes, show_classes, refine_all, probe_class, limit


def bad_residues(prime: int) -> set[int]:
    return {(-offset) % prime for offset in range(1, 7)}


@cache
def live_residues(
    weights: tuple[int, int, int, int],
    prime: int,
) -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]:
    live = []
    gcd_degrees = {}
    for n_value in range(prime):
        if n_value in bad_residues(prime):
            continue
        gcd_degree, _ = specialized_gcd_degree(weights, n_value, prime)
        gcd_degrees[n_value] = gcd_degree
        if live_degree(gcd_degree):
            live.append(n_value)
    return tuple(live), tuple(sorted(gcd_degrees.items()))


def display_classes(classes: list[int], modulus: int, limit: int) -> str:
    if len(classes) <= limit:
        return str(classes)
    shown = ", ".join(str(item) for item in classes[:limit])
    return f"[{shown}, ...] ({len(classes) - limit} more)"


def live_factor_line(live: tuple[int, ...], prime: int) -> str:
    factor = live_residue_factor(list(live), prime)
    return f"degree={factor.degree()}, {format_factor(factor, prime)}"


def build_crt_classes(
    weights: tuple[int, int, int, int],
    primes: list[int],
) -> tuple[int, list[int]]:
    modulus = 1
    classes = [0]
    for prime in primes:
        live, _ = live_residues(weights, prime)
        classes = combine_crt_classes(classes, modulus, prime, list(live))
        modulus *= prime
        if not classes:
            break
    return modulus, classes


def refine_classes_by_prime(
    classes: list[int],
    modulus: int,
    live: tuple[int, ...],
    prime: int,
) -> tuple[int, list[int]]:
    refined = []
    for cls in classes:
        for residue in live:
            value, new_modulus = crt([modulus, prime], [cls, residue])
            assert int(new_modulus) == modulus * prime
            refined.append(int(value) % int(new_modulus))
    return modulus * prime, sorted(set(refined))


def compatible_t_residues(cls: int, modulus: int, live: tuple[int, ...], prime: int) -> list[int]:
    if modulus % prime == 0:
        return [0] if cls % prime in live else []
    inverse = pow(modulus % prime, -1, prime)
    return sorted({((residue - cls) * inverse) % prime for residue in live})


def print_prime_data(weights: tuple[int, int, int, int], prime: int) -> tuple[int, ...]:
    live, gcd_degrees = live_residues(weights, prime)
    print(
        f"  p={prime}: bad={sorted(bad_residues(prime))}, live={list(live)}, "
        f"gcd_degrees={dict(gcd_degrees)}",
        flush=True,
    )
    print(f"    live factor in F_{prime}[n]: {live_factor_line(live, prime)}", flush=True)
    return live


def run_classes(weights: tuple[int, int, int, int], base_primes: list[int], limit: int) -> tuple[int, list[int]]:
    print(f"weights {weights}", flush=True)
    modulus = 1
    classes = [0]
    for prime in base_primes:
        live = print_prime_data(weights, prime)
        classes = combine_crt_classes(classes, modulus, prime, list(live))
        modulus *= prime
        print(
            f"    CRT survivors: {len(classes)} classes mod {modulus}",
            flush=True,
        )
        if not classes:
            break
    print(f"  classes mod {modulus}: {display_classes(classes, modulus, limit)}", flush=True)
    return modulus, classes


def run_refine_all(
    weights: tuple[int, int, int, int],
    base_primes: list[int],
    aux_primes: list[int],
    limit: int,
) -> None:
    print(f"weights {weights}", flush=True)
    modulus, classes = build_crt_classes(weights, base_primes)
    print(f"  base: {len(classes)} classes mod {modulus}", flush=True)
    for prime in aux_primes:
        live = print_prime_data(weights, prime)
        if modulus % prime == 0:
            classes = [cls for cls in classes if cls % prime in live]
        else:
            modulus, classes = refine_classes_by_prime(classes, modulus, live, prime)
        print(f"    refined survivors: {len(classes)} classes mod {modulus}", flush=True)
        if not classes:
            print("    all CRT classes eliminated", flush=True)
            break
    print(f"  refined classes: {display_classes(classes, modulus, limit)}", flush=True)


def run_probe_class(
    weights: tuple[int, int, int, int],
    cls: int,
    modulus: int,
    aux_primes: list[int],
    limit: int,
) -> None:
    print(f"weights {weights}", flush=True)
    classes = [cls % modulus]
    print(f"  probing class n = {classes[0]} mod {modulus}", flush=True)
    for prime in aux_primes:
        live = print_prime_data(weights, prime)
        t_residues = compatible_t_residues(classes[0], modulus, live, prime)
        print(
            f"    compatible t residues mod {prime}: {t_residues}",
            flush=True,
        )
        if modulus % prime == 0:
            classes = [item for item in classes if item % prime in live]
        else:
            modulus, classes = refine_classes_by_prime(classes, modulus, live, prime)
        print(f"    refined to {len(classes)} classes mod {modulus}", flush=True)
        if not classes:
            print("    class eliminated", flush=True)
            return
    print(f"  refined class descendants: {display_classes(classes, modulus, limit)}", flush=True)


def main() -> None:
    weights_list, base_primes, aux_primes, show_classes, refine_all, probe_class, limit = parse_args()
    for index, weights in enumerate(weights_list):
        if index:
            print()
        if show_classes:
            run_classes(weights, base_primes, limit)
        if refine_all:
            run_refine_all(weights, base_primes, aux_primes, limit)
        if probe_class is not None:
            cls, modulus = probe_class
            run_probe_class(weights, cls, modulus, aux_primes, limit)


if __name__ == "__main__":
    main()
