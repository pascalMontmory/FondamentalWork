# Computational Verification

This file documents finite verification only. It must never be confused with a
proof of the infinite Collatz conjecture.

## Baseline finite statement

For a bound `N`, the finite statement is:

```text
for every integer n with 1 <= n <= N, the orbit of n under T reaches 1.
```

This can be exhaustively checked by script for a specified `N` and stopping-step
limit.

## Required metadata

Every computational claim must record:

```text
map used
range checked
maximum steps allowed
maximum observed stopping time
input code path
code hash or commit hash
machine/integer model
whether arbitrary-precision integers were used
```

## Current verified range

No range is recorded yet in this document.

The next step is to run `scripts/verify_collatz_range.py` and paste the exact
result here, including the commit hash.

## Non-claim

A finite range check is useful for debugging definitions and finding mistakes,
but it does not prove the Collatz conjecture.
