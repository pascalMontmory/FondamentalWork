# Verified Lemmas

This file may contain only statements that are proved in this directory or
mechanically verified by reproducible scripts.

## Lemma 1 - Parity and integrality of the classical map

Label: `proved`

For every `n in N+`, the classical Collatz map

```text
T(n) = n/2       if n is even
T(n) = 3n + 1   if n is odd
```

maps `N+` into `N+`.

Proof:

- If `n` is even and positive, `n = 2k` for some `k in N+`, so `T(n)=k in N+`.
- If `n` is odd and positive, then `3n+1 >= 4`, so `T(n)=3n+1 in N+`.

## Lemma 2 - Integrality and oddness of the accelerated odd map

Label: `proved`

For odd `n in N+`, define

```text
A(n) = (3n + 1) / 2^v2(3n + 1).
```

Then `A(n)` is a positive odd integer.

Proof:

For odd positive `n`, `3n+1` is even and positive. By definition,
`2^v2(3n+1)` is the largest power of `2` dividing `3n+1`. The quotient is
therefore a positive integer not divisible by `2`, hence odd.

## Lemma 3 - Finite verification is not an infinite proof

Label: `proved`

For any finite `N`, the statement

```text
for all 1 <= n <= N, T^k(n)=1 for some k
```

does not imply the full Collatz conjecture over all `N+`.

Proof:

The full conjecture quantifies over infinitely many positive integers. A finite
verification covers only a finite initial segment. There are infinitely many
integers larger than `N`, so the finite statement is strictly weaker.

## Collatz-Montmory-specific lemmas

No Collatz-Montmory-specific lemma is verified yet because the map is not yet
defined in `definitions.md`.
