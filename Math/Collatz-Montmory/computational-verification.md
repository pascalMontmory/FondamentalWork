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

A baseline verifier has been added at:

```text
Math/Collatz-Montmory/scripts/verify_collatz_range.py
```

but it has not yet been executed in a local checkout of this PR branch. Therefore
no finite verification range is claimed here yet.

Run, from a checkout containing this file:

```bash
python3 Math/Collatz-Montmory/scripts/verify_collatz_range.py --limit 100000 --max-steps 10000
python3 Math/Collatz-Montmory/tests/test_verify_collatz_range.py
python3 -m py_compile \
  Math/Collatz-Montmory/scripts/verify_collatz_range.py \
  Math/Collatz-Montmory/tests/test_verify_collatz_range.py
```

Then paste the exact output and commit hash into this file.

## Non-claim

A finite range check is useful for debugging definitions and finding mistakes,
but it does not prove the Collatz conjecture.
