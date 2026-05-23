# Definitions

This file defines only the classical baseline needed before the
Collatz-Montmory variant is written.

## Domain

Unless stated otherwise, the domain is

```text
N+ = {1, 2, 3, ...}
```

Zero and negative integers are excluded from the baseline audit.

## Classical Collatz map

For `n in N+`, define

```text
T(n) = n/2       if n is even
T(n) = 3n + 1   if n is odd.
```

The classical Collatz conjecture states that for every `n in N+`, some iterate
of `T` reaches `1`.

## Stopping time

For `n in N+`, define the stopping time

```text
tau(n) = min { k >= 0 : T^k(n) = 1 }
```

if such `k` exists. If no such `k` exists, `tau(n)` is undefined.

For finite computational verification up to a bound `N`, the statement is:

```text
for all 1 <= n <= N, tau(n) exists.
```

This is a finite theorem if checked exhaustively by a correct script. It is not
a proof of the infinite conjecture.

## Odd accelerated map

For odd `n in N+`, define

```text
v2(m) = max { a >= 0 : 2^a divides m }
A(n) = (3n + 1) / 2^v2(3n + 1).
```

Then `A(n)` is odd. The odd accelerated map skips all immediate divisions by
`2` after applying `3n+1`.

## Collatz-Montmory map

The Collatz-Montmory map is not defined yet in this repository.

Before any theorem or computational claim is attached to it, this section must
be completed with:

```text
M(n) = ...
domain(M) = ...
relationship to T or A = ...
claimed equivalence to classical Collatz = yes/no/partial
```

Until this is done, every Collatz-Montmory-specific statement is `open`.
