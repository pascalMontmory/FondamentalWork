#!/usr/bin/env python3
"""Verify and display the shared-5 cofactor-center descent identities.

This is a symbolic/integer sanity tool for the descent pivot.  It does not
search for Legendre witnesses.  It checks the exact identities behind the
map

    e = 2u, p = A-r, W = r+u,
    W^2+c = u(2A+u),
    A-W = p-u.
"""

from __future__ import annotations

from math import isqrt


OFFSETS = (5, 17, 25, 49, 65)


def terminal_label_bound(A: int, c: int) -> int:
    """Largest integer p satisfying p <= -A + sqrt(2A^2+c)."""

    return isqrt(2 * A * A + c) - A


def verify_identity(A: int, c: int, p: int, u: int) -> bool:
    r = A - p
    if r * r + c != 2 * u * p:
        return False
    W = r + u
    return W * W + c == u * (2 * A + u) and A - W == p - u


def euclidean_terminal_data(A: int, c: int, p: int) -> tuple[int, int, int] | None:
    """Return k,s,v for A=kp+s and s^2+c=vp, if divisible."""

    k, s = divmod(A, p)
    value = s * s + c
    if value % p != 0:
        return None
    return k, s, value // p


def sample_terminal_bounds() -> None:
    for A in (3488, 10_000, 100_000):
        bounds = {c: terminal_label_bound(A, c) for c in OFFSETS}
        print(f"A={A} terminal_label_bounds={bounds}")


def sample_identities() -> None:
    examples = [
        # A, c, p, u chosen to satisfy (A-p)^2+c=2up.
        (20, 5, 3, 49),
        (22, 49, 13, 5),
    ]
    for A, c, p, u in examples:
        r = A - p
        W = r + u
        ok = verify_identity(A, c, p, u)
        print(
            f"A={A} c={c} p={p} u={u} r={r} W={W} "
            f"descending={u < p} identity={ok}"
        )
        if not ok:
            raise AssertionError((A, c, p, u))


def sample_euclidean_descent() -> None:
    examples = [
        # A,c,p with p | A^2+c.  The first is a prime-value atom for c=5.
        (88, 5, 41),
        # The second has v>1 and descends through a prime divisor of v.
        (17, 5, 7),
    ]
    for A, c, p in examples:
        data = euclidean_terminal_data(A, c, p)
        if data is None:
            raise AssertionError((A, c, p))
        k, s, v = data
        kind = "prime_atom" if v == 1 else "euclidean_descent"
        print(f"A={A} c={c} p={p} k={k} s={s} v={v} kind={kind}")


def main() -> int:
    sample_terminal_bounds()
    sample_identities()
    sample_euclidean_descent()
    print("certificate: cofactor-center identities verified on exact samples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
