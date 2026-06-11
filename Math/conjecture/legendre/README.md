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
- `legendre_multiple_of_three_refined_channels.md`: corrected exact
  classification of the \(n=3m\) channels; the first \(M_3\) candidate is
  false because it misses the \(3\nmid t,\ r=1\) unit-lift channel.
- `legendre_m3star_certificate.md`: exact small-prime certificate for failure
  of the corrected \(M_3^\ast\) target.
- `legendre_combined_A_cover.md`: exact rigidity of the combined \(3\nmid t\)
  channel, including the adjacent-block bridge-prime obstruction.
- `legendre_A_block_gcd.md`: exact gcd formula for both candidates in a
  complete A-block, isolating bridge blocks from coprime blocks.
- `legendre_coprime_A_pair_cover.md`: pair-cover reformulation for coprime
  complete A-blocks, where each ordered prime pair contributes at most four
  CRT classes.
- `legendre_pair_incidence_geometry.md`: conic-product incidence formulation
  for the coprime A-block pair cover, including nonzero A1 restrictions.
- `legendre_A1_local_filter.md`: exact count of the \(m\bmod p\) classes
  for which the A1 congruence has nonzero roots.
- `legendre_pair_density_bound.md`: exact local density of one ordered
  pair incidence and failed naive union-bound route.
- `legendre_fixed_m_sieve_decomposition.md`: fixed-\(m\) reformulation of
  coprime A-block failure as \(\mathcal Q_{\rm cop}(m)\subseteq S_0(m)\cap
  S_1(m)\).
- `legendre_fixed_m_large_sieve_target.md`: exact large-sieve/covering
  target for the fixed-\(m\) double sieve, including why the classical large
  sieve is not directly enough.

Current exact bottleneck: after the primitive double-cover reduction, the
remaining \(3\mid n\) channel has been refined into three exact subchannels:
the primitive Gaussian channel \(r=0\), the nonmultiple unit-lift channel
\(r=1\), and the \(t=3u\) repair channel.  The corrected target is
\(M_3^\ast\), and a counterexample is now equivalent to a simultaneous
A0/A1/B small-prime cover.  The combined A-cover now has a sharper block
rigidity: a single prime can cover both members of a complete
\((3q+1,3q+2)\) block only if it divides \(9m^2+1\).  The full block gcd is
exactly \(\gcd(c_q,9m^2+1)\), so coprime blocks require two genuinely
distinct prime certificates.  On coprime blocks this becomes a pair-cover
problem by ordered primes \((p_0,p_1)\), each contributing at most four
classes modulo \(p_0p_1\).  The pair-cover has now been rewritten as an
incidence problem in \((m,q)\) on two oriented products of conics.  The A1
side has an exact local filter: \((p-3)/2\) admissible \(m\)-classes for
\(p\equiv1\pmod4\), and \((p+1)/2\) for \(p\equiv3\pmod4\).  The local
density of one ordered pair is known exactly, but the naive union bound is
too weak; the target has been sharpened to a fixed-\(m\) double-sieve
inclusion \(\mathcal Q_{\rm cop}(m)\subseteq S_0(m)\cap S_1(m)\).  The
remaining bottleneck is a quadratic covering lemma or a valuation argument
for the product family \(\Phi_m(q)\).

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
