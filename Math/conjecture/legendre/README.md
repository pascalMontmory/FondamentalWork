# Legendre Workbench

This directory contains the Legendre-conjecture thread.

Main notes:

- `PROGRESS.md`: chronological progress log.
- `legendre_residue_gaussian_note.md`: residue-cover and Gaussian-integer
  route.
- `legendre_exact_circle_cover_attack.md`: exact finite-field circle-cover
  reformulation of the \(t^2-1,t^2,t^2+1,t^2+2\) route.
- `legendre_circle_residue_calculus.md`: exact formulas for local bad
  residue sets \(B_p(n)\).
- `legendre_four_consecutive_certificate.md`: exact certificate layer for
  the four consecutive candidates \(A-1,A,A+1,A+2\).
- `legendre_primitive_channel_reduction.md`: primitive opposite-parity
  reduction to the Gaussian norm \(A\) and its twin shift \(A+2\).
- `legendre_primitive_double_cover.md`: reduction of counterexamples to a
  primitive Gaussian cover \(I_n\subseteq G(n)\) plus a twin-shift double cover.
- `legendre_multiple_of_three_channel.md`: exact \(n=3m\) split into the
  primitive \(3\nmid t\) Gaussian channel and the nonprimitive \(t=3u\)
  repair channel.

Current exact bottleneck: after the primitive double-cover reduction, the
remaining observed survivors are concentrated at \(3\mid n\), where the
primitive channel collapses to the pure Gaussian norm and a nonprimitive or
divisor-channel argument is needed.

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

Fourth checkpoint: all pure-square failures up to \(1000000\) are the same
33 cases already below \(10000\), and every one is repaired by
\(r\in\{-1,1,2\}\).  No \(r=-2\) witness is needed in this range.
