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
- `legendre_phi_product_attack.md`: product-family formulation
  \(\Phi_m(q)=G_qU_q\), exposing coprime factors, small difference, and the
  failed fixed-divisor shortcut.
- `legendre_transversality_repetition.md`: multi-block repetition constraints
  showing that repeated certificates by one prime impose arithmetic
  progression or mirror congruences on block indices.
- `legendre_adjacent_block_obstruction.md`: adjacent-block rule showing that
  same-prime repetition on neighboring blocks forces \(p\mid q+1\).
- `legendre_triple_block_labeling.md`: no-triple repetition rule and
  two-layer labeling formulation for the remaining obstruction.
- `legendre_initial_block_obstruction.md`: exact first-three-block
  constraints; for \(m\ge11\), the initial triple has no adjacent same-layer
  repetition, and the only possible nonadjacent repetition is the prime \(5\)
  in explicit residue classes.
- `legendre_initial_mod10_gate.md`: exact reduction of the initial triple to
  four residue gates modulo \(10\): strong no-repetition classes, A0 reuse of
  \(5\), A1 reuse of \(5\), and bridge classes.
- `legendre_initial_four_block_graph.md`: exact repetition graph for the
  first four blocks; all same-layer repetitions are reduced to listed
  \(5\)- and \(7\)-edges or to explicit bridge classes.
- `legendre_initial_mod70_gate.md`: exact CRT classification modulo \(70\)
  of the first-four-block gates: bridge, no-repetition, A0-\(5\), A1-\(5\),
  A1-\(7\), and double-A1.
- `legendre_initial_cross_layer_collisions.md`: exact cross-layer collision
  lemma for the first four blocks; outside bridge classes, shared A0/A1 labels
  are confined to fixed primes \(13,17,29,37,53\) with explicit congruences.
- `legendre_initial_pairwise_coprime_cluster.md`: clean strong-gate
  consequence showing that the eight first-four-block A0/A1 candidates are
  pairwise coprime; a counterexample must begin with eight distinct small
  prime labels.
- `legendre_initial_factor_gap_system.md`: exact centered factorization
  equations for the clean strong-gate cluster, replacing small prime labels
  by eight simultaneous factor-gap equations around \(A=3m\).
- `legendre_initial_center_divisor_parametrization.md`: equivalent
  center-divisor form \(A-r\mid r^2+c\), eliminating the cofactor gap
  variable and restating the clean strong-gate obstruction as eight shifted
  square divisibilities.
- `legendre_initial_sqrt_barrier.md`: square-root lower bound on center
  distances \(r_c\) and quotient parametrization
  \(A=r_c+(r_c^2+c)/e_c\) for the clean strong-gate cluster.
- `legendre_initial_pair_quotient_compatibility.md`: exact pairwise
  compatibility equation for two offsets sharing the same center; for
  \(m\ge4881\), all eight initial quotients \(e_c\) must be distinct in the
  clean strong gate.
- `legendre_initial_order_constraints.md`: monotonicity constraints for
  \(e=(r^2+c)/(A-r)\); quotient-order inversions must be mirrored by
  distance-order inversions and opposite prime-label order.
- `legendre_initial_quotient_rank_barrier.md`: ranked square-root barriers
  from the distinct quotients \(e_{(k)}\ge k\); higher quotient rank forces
  deeper exclusion windows for prime labels below \(A\).
- `legendre_initial_rank_position_coupling.md`: exact band for the distance
  rank forced by placing quotient rank \(k\) at offset position \(i\), with
  the strongest case \(k=8\) forcing \(s_i\ge9-i\).
- `legendre_initial_label_order_statistic_barrier.md`: global sorted-label
  consequence of the quotient ranks; the \(j\)-th smallest prime label
  satisfies \(P_j\le A-B_{9-j}(A)\).
- `legendre_initial_A0_tail_constraints.md`: pigeonhole projection of the
  global label tail onto A0; the \(j\)-th smallest A0 label satisfies
  \(Q_j\le A-B_{5-j}(A)\) and all A0 distances satisfy
  \(r\equiv A-1\pmod4\).

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
for the product family \(\Phi_m(q)\); the product route reduces the target to
a transversality lemma rather than a fixed-divisor contradiction.  Repetition
by the same certificate prime now has explicit progression/mirror structure
on the \(q\)-line, and adjacent same-prime repetition can occur only at
divisor positions \(p\mid q+1\).  In particular, one prime cannot label three
consecutive blocks in the same layer.  The first universal triple
\(q=0,1,2\) has now been isolated exactly: once complete and coprime, adjacent
same-layer repetition is impossible, and the only possible nonadjacent
repetition is \(p=5\), with A0 restricted to odd \(m\equiv\pm2\pmod5\) and
A1 restricted to even \(5\mid m\).  This has been compressed into an exact
mod \(10\) gate: classes \(2,4,5,6,8\) force full same-layer distinctness,
class \(0\) permits only A1 reuse of \(5\), classes \(3,7\) permit only A0
reuse of \(5\), and classes \(1,9\) are bridge-block cases.  Extending to
the first four blocks adds bridge classes \(4,6\) through \(B_3\); outside
the bridge classes \(m\equiv\pm1\pmod5\), every same-layer repetition among
\(B_0,\dots,B_3\) is now one of finitely many explicit \(5\)- or \(7\)-edges.
The first-four gate has been compressed modulo \(70\), giving six disjoint
types: bridge, no-repetition, A0-\(5\), A1-\(5\), A1-\(7\), and double-A1.
Cross-layer label sharing among the first four blocks has also been
localized exactly: outside bridge classes, it can only occur through the
fixed primes \(13,17,29,37,53\) in explicitly listed block positions.  In
the clean strong gate, excluding those cross-layer congruences, the eight
initial A0/A1 candidate values are pairwise coprime.  A counterexample there
must therefore start with eight pairwise coprime composites, each carrying a
distinct small prime label.  This cluster has now been rewritten as eight
centered factor-gap equations
\[
  A^2+c=(A-r_c)(A+r_c+e_c),
  \qquad A=3m,
\]
with \(c\) running through an explicit parity-dependent offset set.  The
cofactor gap can be eliminated: each composite candidate is equivalently
certified by a distance \(r_c\) such that
\[
  A-r_c\mid r_c^2+c.
\]
This gives the square-root barrier \(r_c^2+r_c+c\ge A\), so for \(A>122\)
all eight initial distances satisfy \(r_c\gg\sqrt A\).  Comparing two offsets
in the quotient form yields a binary quadratic compatibility equation; in
particular, for \(m\ge4881\), equal quotients are impossible among distinct
initial offsets in the clean strong gate.  The quotient order is also
constrained: if \(c<d\) but \(e_c>e_d\), then \(r_c>r_d\) and \(p_c<p_d\).
The quotient ranks give stronger distance barriers:
\[
  r_{(k)}\ge
  \left\lceil
  \frac{-k+\sqrt{k^2+4(kA-122)}}{2}
  \right\rceil.
\]
Combining quotient rank with order gives the rank-position band
\[
  \max(1,k-i+1)\le s_i\le\min(8,8+k-i).
\]
Globally, if the prime labels are sorted
\[
  P_1<\cdots<P_8,
\]
then
\[
  P_j\le A-B_{9-j}(A).
\]
Projecting onto A0 gives \(Q_j\le A-B_{5-j}(A)\) for the four labels
\(Q_j\equiv1\pmod4\).

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
