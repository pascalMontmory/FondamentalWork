# Legendre Workbench

This directory contains the Legendre-conjecture thread.

Main notes:

- `PROGRESS.md`: chronological progress log.
- `legendre_residue_gaussian_note.md`: residue-cover and Gaussian-integer
  route.

Computational scripts live in `tools/`.

Current first target: test the Gaussian Lemma G experimentally and record
whether small primitive square offsets
\[
  n^2+t^2,\qquad 1\le t\le\lfloor\sqrt{2n}\rfloor
\]
can always avoid all small prime divisors \(p\equiv1\pmod4\), \(p\le n+1\),
with the parity condition needed to avoid the divisor \(2\).

First checkpoint: Lemma G is false as a universal statement, with first
counterexample \(n=12\).  The square-offset route should now be treated as a
sparse-failure subcover, not a direct proof of Legendre.

Second checkpoint: the first primes in all strict failures observed up to
\(100000\) have offsets \(t^2+r\) with \(|r|\le5\).  The next candidate is a
bounded correction band around Gaussian square offsets.

Third checkpoint: the bounded band \(|r|\le2\) has no failures for
\(2\le n\le1000000\).  The band \(|r|\le1\) has one failure in the same range,
at \(n=23\).
