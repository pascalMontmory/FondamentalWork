#!/usr/bin/env python3
"""Mordell-Weil sieve scaffolding for the residual Legendre elliptic curve.

Curve:
    E: y^2 = x^3 - 128*x^2 - 215865*x.

The residual prefix-8 fibers can only survive at rational points whose
x-coordinate lies in 1845 * Z^2.  This script performs exact reductions of the
certified Mordell-Weil basis modulo good primes and provides two reproducible
checks:

* local-prime statistics for the square-x condition;
* a bounded lattice scan in the certified Mordell-Weil coordinates.

The bounded scan is not a proof by itself.  The proof target remains the full
Mordell-Weil sieve with a height bound.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import gcd, isqrt, lcm
from typing import Iterable


A2 = -128
A4 = -215865
SQUARE_FACTOR = 1845

Point = tuple[int, int] | None

GENERATORS: tuple[tuple[int, int], ...] = (
    (-363, 3696),
    (-195, 5460),
    (-117, 4680),
)

TORSION: tuple[Point, ...] = (
    None,
    (0, 0),
    (533, 0),
    (-405, 0),
)

BAD_PRIMES = {2, 3, 5, 7, 13, 41, 67}
COMMON_TWICE = ((153, -55), (41, 9), (45, -13))
COMMON_SQUARE = ((2673, -992), (4617, -392))
TERMINAL_R4 = ((1701, -908), (7533, 2668))
TERMINAL_R5 = ((3645, -836), (1701, -1004))


def inv_mod(a: int, p: int) -> int:
    return pow(a % p, -1, p)


def add_mod(p1: Point, p2: Point, p: int) -> Point:
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1 = p1[0] % p, p1[1] % p
    x2, y2 = p2[0] % p, p2[1] % p
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if x1 == x2 and y1 == y2:
        lam = (3 * x1 * x1 + 2 * A2 * x1 + A4) * inv_mod(2 * y1, p)
    else:
        lam = (y2 - y1) * inv_mod(x2 - x1, p)
    lam %= p
    x3 = (lam * lam - A2 - x1 - x2) % p
    y3 = (-(y1 + lam * (x3 - x1))) % p
    return (x3, y3)


def neg_mod(point: Point, p: int) -> Point:
    if point is None:
        return None
    return (point[0] % p, (-point[1]) % p)


def mul_mod(point: Point, n: int, p: int) -> Point:
    if n < 0:
        return mul_mod(neg_mod(point, p), -n, p)
    out: Point = None
    acc = point
    while n:
        if n & 1:
            out = add_mod(out, acc, p)
        acc = add_mod(acc, acc, p)
        n >>= 1
    return out


def add_q(p1: Point, p2: Point) -> Point:
    from fractions import Fraction

    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1 = Fraction(p1[0]), Fraction(p1[1])
    x2, y2 = Fraction(p2[0]), Fraction(p2[1])
    if x1 == x2 and y1 == -y2:
        return None
    if x1 == x2 and y1 == y2:
        lam = (3 * x1 * x1 + 2 * A2 * x1 + A4) / (2 * y1)
    else:
        lam = (y2 - y1) / (x2 - x1)
    x3 = lam * lam - A2 - x1 - x2
    y3 = -(y1 + lam * (x3 - x1))
    if x3.denominator == 1 and y3.denominator == 1:
        return (int(x3), int(y3))
    return (x3, y3)  # type: ignore[return-value]


def neg_q(point: Point) -> Point:
    if point is None:
        return None
    return (point[0], -point[1])


def mul_q(point: Point, n: int) -> Point:
    if n < 0:
        return mul_q(neg_q(point), -n)
    out: Point = None
    acc = point
    while n:
        if n & 1:
            out = add_q(out, acc)
        acc = add_q(acc, acc)
        n >>= 1
    return out


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def square_x_point(point: Point) -> tuple[bool, int | None]:
    if point is None:
        return (False, None)
    x = point[0]
    if not isinstance(x, int):
        return (False, None)
    if x % SQUARE_FACTOR:
        return (False, None)
    s2 = x // SQUARE_FACTOR
    if is_square(s2):
        return (True, isqrt(s2))
    return (False, None)


def allowed_z_residues(p: int, mode: str) -> set[int]:
    squares = {x * x % p for x in range(p)}
    two_squares = {2 * x * x % p for x in range(p)}
    if mode == "common":
        terminal: tuple[tuple[int, int], ...] = ()
    elif mode == "r4":
        terminal = TERMINAL_R4
    elif mode == "r5":
        terminal = TERMINAL_R5
    else:
        raise ValueError(mode)

    out: set[int] = set()
    for s in range(p):
        z = s * s % p
        if not all((a * z + b) % p in two_squares for a, b in COMMON_TWICE):
            continue
        if not all((a * z + b) % p in squares for a, b in COMMON_SQUARE):
            continue
        if not all((a * z + b) % p in squares for a, b in terminal):
            continue
        out.add(z)
    return out


def allowed_mod(point: Point, p: int, mode: str, allowed_z: set[int] | None = None) -> bool:
    if point is None or p in BAD_PRIMES:
        return False
    if allowed_z is None:
        allowed_z = allowed_z_residues(p, mode)
    x = point[0] % p
    scaled = x * inv_mod(SQUARE_FACTOR, p) % p
    return scaled in allowed_z


def point_order_mod(point: Point, p: int) -> int:
    acc: Point = None
    # Hasse gives #E(F_p) <= p + 1 + 2 sqrt(p); this loose bound is enough.
    for n in range(1, p + 2 + 2 * isqrt(p) + 10):
        acc = add_mod(acc, point, p)
        if acc is None:
            return n
    raise RuntimeError(f"order not found modulo {p}")


def primes_upto(n: int) -> list[int]:
    out: list[int] = []
    for x in range(2, n + 1):
        if all(x % d for d in range(2, isqrt(x) + 1)):
            out.append(x)
    return out


@dataclass(frozen=True)
class PrimeStat:
    p: int
    orders: tuple[int, int, int]
    group_points: int
    allowed_points: int


def subgroup_points_mod(p: int) -> set[Point]:
    gens = tuple((x % p, y % p) for x, y in GENERATORS)
    seen: set[Point] = {None}
    frontier: list[Point] = [None]
    while frontier:
        current = frontier.pop()
        for gen in gens:
            for step in (gen, neg_mod(gen, p)):
                nxt = add_mod(current, step, p)
                if nxt not in seen:
                    seen.add(nxt)
                    frontier.append(nxt)
    return seen


def prime_stat(p: int, mode: str) -> PrimeStat:
    gens = tuple((x % p, y % p) for x, y in GENERATORS)
    orders = tuple(point_order_mod(gen, p) for gen in gens)
    subgroup = subgroup_points_mod(p)
    allowed = 0
    torsion = tuple(None if t is None else (t[0] % p, t[1] % p) for t in TORSION)
    allowed_z = allowed_z_residues(p, mode)
    for point in subgroup:
        if any(allowed_mod(add_mod(point, t, p), p, mode, allowed_z) for t in torsion):
            allowed += 1
    return PrimeStat(p, orders, len(subgroup), allowed)


def bounded_scan(bound: int) -> list[tuple[tuple[int, int, int], int, Point, int]]:
    hits: list[tuple[tuple[int, int, int], int, Point, int]] = []
    for n1 in range(-bound, bound + 1):
        p1 = mul_q(GENERATORS[0], n1)
        for n2 in range(-bound, bound + 1):
            p12 = add_q(p1, mul_q(GENERATORS[1], n2))
            for n3 in range(-bound, bound + 1):
                free = add_q(p12, mul_q(GENERATORS[2], n3))
                for ti, torsion in enumerate(TORSION):
                    point = add_q(free, torsion)
                    ok, s = square_x_point(point)
                    if ok and s is not None:
                        hits.append(((n1, n2, n3), ti, point, s))
    return hits


def combined_sieve(
    primes: Iterable[int], max_classes: int, mode: str
) -> tuple[int, list[tuple[int, int, int, int]]]:
    prime_list = list(primes)
    modulus = 1
    survivors: list[tuple[int, int, int, int]] = [(0, 0, 0, ti) for ti in range(4)]

    print(f"combined sieve mode={mode} primes={prime_list}")
    for p in prime_list:
        if p in BAD_PRIMES:
            raise ValueError(f"bad reduction or square-factor prime: {p}")
        gens = tuple((x % p, y % p) for x, y in GENERATORS)
        orders = tuple(point_order_mod(gen, p) for gen in gens)
        new_modulus = modulus
        for order in orders:
            new_modulus = lcm(new_modulus, order)
        torsion = tuple(None if t is None else (t[0] % p, t[1] % p) for t in TORSION)
        allowed_z = allowed_z_residues(p, mode)
        multiples = tuple(
            [mul_mod(gen, n, p) for n in range(new_modulus)] for gen in gens
        )

        lift = new_modulus // modulus
        candidate_count = len(survivors) * lift**3
        if candidate_count > max_classes:
            raise RuntimeError(
                f"lift to modulus {new_modulus} has {candidate_count} candidates; "
                "raise --max-classes"
            )
        next_survivors: list[tuple[int, int, int, int]] = []
        for n1, n2, n3, ti in survivors:
            for a in range(lift):
                nn1 = n1 + a * modulus
                for b in range(lift):
                    nn2 = n2 + b * modulus
                    for c in range(lift):
                        nn3 = n3 + c * modulus
                        point = add_mod(
                            add_mod(multiples[0][nn1], multiples[1][nn2], p),
                            multiples[2][nn3],
                            p,
                        )
                        point = add_mod(point, torsion[ti], p)
                        if allowed_mod(point, p, mode, allowed_z):
                            next_survivors.append((nn1, nn2, nn3, ti))
        modulus = new_modulus
        survivors = next_survivors
        print(
            f" after p={p}: modulus={modulus} survivors={len(survivors)} "
            f"orders={orders}"
        )
        if not survivors:
            break

    print(f"combined final_modulus={modulus} survivors={len(survivors)}")
    for item in survivors[:100]:
        print(f"survivor {((item[0], item[1], item[2]), item[3])}")
    if len(survivors) > 100:
        print("...")
    return modulus, survivors


def assert_prefix8_terminal_pair(
    mode: str, modulus: int, survivors: list[tuple[int, int, int, int]]
) -> None:
    if modulus != 1320:
        raise AssertionError(f"expected modulus 1320, got {modulus}")
    expected = {
        (0, 2, 1, 1),
        (0, 1318, 1319, 1),
    }
    actual = set(survivors)
    if actual != expected:
        raise AssertionError(f"unexpected {mode} survivors: {sorted(actual)}")
    print(f"CERTIFIED {mode}: only +/-((0,2,1), torsion_index=1) modulo 1320")


def terminal_status(s: int) -> tuple[bool, bool]:
    r4 = is_square(1701 * s * s - 908) and is_square(7533 * s * s + 2668)
    r5 = is_square(3645 * s * s - 836) and is_square(1701 * s * s - 1004)
    return r4, r5


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-bound", type=int, default=200)
    parser.add_argument("--scan-bound", type=int, default=3)
    parser.add_argument("--mode", choices=("common", "r4", "r5"), default="common")
    parser.add_argument(
        "--combine-primes",
        default="",
        help="Comma-separated good primes for a direct combined coefficient sieve.",
    )
    parser.add_argument(
        "--expect-prefix8-terminal-pair",
        action="store_true",
        help="Assert the known residual prefix-8 terminal pair modulo 1320.",
    )
    parser.add_argument("--max-classes", type=int, default=2_000_000)
    args = parser.parse_args()

    print("local Mordell-Weil sieve statistics")
    for p in primes_upto(args.prime_bound):
        if p in BAD_PRIMES:
            continue
        stat = prime_stat(p, args.mode)
        ratio = stat.allowed_points / stat.group_points if stat.group_points else 0
        print(
            f"p={stat.p} orders={stat.orders} subgroup={stat.group_points} "
            f"allowed={stat.allowed_points} ratio={ratio:.4f}"
        )

    if args.combine_primes:
        primes = [int(part) for part in args.combine_primes.split(",") if part]
        modulus, survivors = combined_sieve(primes, args.max_classes, args.mode)
        if args.expect_prefix8_terminal_pair:
            if args.mode not in {"r4", "r5"}:
                raise ValueError("--expect-prefix8-terminal-pair requires r4 or r5 mode")
            assert_prefix8_terminal_pair(args.mode, modulus, survivors)

    print(f"bounded coordinate scan: |n_i| <= {args.scan_bound}")
    hits = bounded_scan(args.scan_bound)
    for coeffs, torsion_index, point, s in hits:
        r4, r5 = terminal_status(s)
        print(
            f"hit coeffs={coeffs} torsion_index={torsion_index} "
            f"point={point} s={s} terminal_R4={r4} terminal_R5={r5}"
        )
    print(f"hits={len(hits)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
