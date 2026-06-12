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
- `legendre_m3mod4_residual_elliptic_mwrank_certificate.md`: residual
  prefix-\(8\) reduction to the rank-\(3\) elliptic curve
  \(Y^2=X^3-128X^2-215865X\), including certified Mordell-Weil basis and the
  final IntegralPoints/Mordell-Weil sieve target.
- `legendre_m3mod4_residual_3adic_coset_closure.md`: exact \(3\)-adic
  closure of the final residual coset pair.  Since the curve has split
  multiplicative type \(I_8\) at \(3\), \(1320E(\mathbf Q)\subset
  E_1(\mathbf Q_3)\), and the cosets \(\pm P_0+1320E(\mathbf Q)\) are
  disjoint from \(x=1845s^2\) for \(s\in\mathbf Z\).
- `legendre_status_after_residual_closure.md`: current proof ledger after
  the residual elliptic endpoint closure; it records that this branch is
  closed, while full Legendre still requires closing the earlier coprime
  A-block pair-cover obstruction or replacing it by a stronger descent.
- `legendre_complete_proof_equation_gate.md`: exact equation-level gate for
  a complete proof in the current route: a counterexample must assign to
  every complete coprime A-block two distinct small certificate primes
  satisfying the A0/A1 conic congruences.
- `legendre_pair_collision_equations.md`: exact two-block collision lemma
  for repeated ordered pairs \((p_0,p_1)\).  A repeated pair must place
  \(p_0,p_1\) on explicit divisor hyperplanes in \(q-r\), \(q+r\), or
  \(q+r+1\).
- `legendre_Ablock_anchor_q0.md`: proves that \(q=0\) is always a complete
  coprime A-block and records the explicit odd/even boundary systems
  \(9m^2+4,9m^2+2\) or \(9m^2+1,9m^2+5\) that any counterexample must cover.
- `legendre_Ablock_anchor_pair_nonrepetition.md`: proves that the ordered
  pair covering the anchor block \(q=0\) cannot also cover any of
  \(q=1,2,3\); the first block has a forced one-shot pair cost among the
  first four blocks.
- `legendre_first_four_ordered_pair_distinct.md`: proves that no ordered
  pair \((p_0,p_1)\) can cover two distinct coprime blocks among
  \(B_0,\dots,B_3\).  The possible same-layer repetitions in \(E=(2,4,8,10)\)
  and \(O=(1,5,7,11)\) occur on disjoint block pairs.
- `legendre_first_five_ordered_pair_repetition.md`: extends the local
  capacity theorem to \(B_0,\dots,B_4\).  The only possible ordered-pair
  repetition is \((B_2,B_4)\) by \((p_0,p_1)=(5,11)\), with
  \(m\) even, \(m^2\equiv4\pmod5\), and \(m^2\equiv5\pmod{11}\).
- `legendre_first_six_ordered_pair_repetition.md`: extends the ordered-pair
  classification to \(B_0,\dots,B_5\).  Repetitions are possible only in
  two explicit gates: even \((B_2,B_4):(5,11)\), or odd
  \((B_3,B_5):(13,7)\), each with stated congruence conditions on \(m\).
  The tempting odd \((B_1,B_5):(5,11)\) gate dies because it would force
  \(m^2\equiv2\pmod{11}\), a nonsquare class.
- `legendre_global_mobius_dual_gate.md`: records the pivot away from
  increasing the number of initial blocks.  It defines exact Mobius
  detectors for the two small-prime kernels and reduces the remaining
  A-channel closure to the global positivity target \(Z(m)>0\).
- `legendre_mobius_root_count_formula.md`: expands \(Z(m)\) into exact CRT
  root counts over the complete block interval, with explicit bridge
  removal and a sharp remainder bound.  It shows why the full untruncated
  Mobius expansion still needs a parity-breaking weighted certificate.
- `legendre_cofactor_augmented_mobius_gate.md`: adds the missing cofactor
  rigidity to the Mobius gate.  A failed coprime block must satisfy the
  short bilinear equation \(p_1X_1-p_0X_0=\pm2t_1(q)\), or equivalently one
  of two explicit quartic bilinear equations after eliminating \(q\).  The
  same note derives the two-block cofactor descent for repeated ordered
  pairs.
- `legendre_centered_cofactor_pair_gate.md`: rewrites the cofactor gate with
  centered variables \(p_i=3m-r_i\).  Each failed block becomes two divisor
  equations \((A-r_i)e_i=r_i^2+c_i(q)\) plus one short same-block coupling
  equation, giving the next exact non-cover target.
- `legendre_global_high_label_oneshot.md`: proves a global repetition
  cutoff.  If \(Q^\ast_m=\lfloor(\sqrt{6m}-2)/3\rfloor\), then any ordered
  pair with \(\max(p_0,p_1)>6Q^\ast_m+4\) can cover at most one complete
  block.  Repeated ordered pairs are confined to the low-label box.
- `legendre_high_label_least_root_gate.md`: strengthens the high-label
  branch.  For \(p>2\lfloor\sqrt{6m}\rfloor\), a high certificate is exactly
  a least-root event \(t=\|3m\,i_p\|_p\) in A0 or
  \(t=\|s_p\|_p,\ s_p^2\equiv-(3m)^2-1\pmod p\) in A1.
- `legendre_capacity_dichotomy.md`: combines low labels, bounded middle
  labels, and high least-root labels into an exact three-zone decomposition
  for any remaining counterexample.
- `legendre_m3mod4_residual_global_integral_points_target.md`: exact final
  target after the local Mordell-Weil sieve: prove that the two cosets
  \(P\in\pm P_0+1320E(\mathbf Q)\) contain no integral point passing the
  \(x=1845s^2\), \(R4\), or \(R5\) square filters.
- `tools/m3mod4_residual_integral_points.sage`: Sage certificate script for
  the final residual R4/R5 fibers; it filters integral points on the
  certified elliptic curve by \(X=1845s^2\) and the separated square
  equations.
- `tools/m3mod4_residual_coset_integral_points.magma`: narrow Magma target
  for the final two cosets \(P\in\pm P_0+1320E(\mathbf Q)\), where
  \(P_0=(10045/9,-849520/27)\).
- `tools/m3mod4_residual_mw_sieve.py`: exact finite Mordell-Weil sieve; the
  option `--expect-prefix8-terminal-pair` asserts that both residual terminal
  fibers reduce to the two opposite coefficient classes modulo \(1320\).
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
- `legendre_initial_A0_spacing_envelope.md`: strengthened A0 lower-tail
  envelope using the fact that the four A0 distances are distinct and all
  congruent modulo \(4\), hence spaced by at least \(4\).
- `legendre_initial_A1_spacing_envelope.md`: A1 lower-tail envelope using
  odd-prime parity; the four A1 distances are congruent modulo \(2\), hence
  spaced by at least \(2\).
- `legendre_initial_two_layer_ladder_certificate.md`: global label-order
  certificate combining A0 and A1; all eight distances have the same parity,
  A0 adds modulo-\(4\) ladder edges, and any clean strong-gate counterexample
  must choose a layer word, offset-label matching, quotient-rank permutation,
  and compatible centered divisor equations.
- `legendre_initial_quotient_pell_pencil.md`: quotient-first reformulation
  using \(w=2r+e\), so each offset imposes
  \(w^2=4eA+e^2-4c\); since \(A=3m\), every quotient must pass the local
  congruence \(w^2\equiv e^2-4c\pmod{12e}\), and pairs of offsets satisfy a
  synchronized Pell-type equation independent of \(A\).
- `legendre_initial_even_quotient_lift.md`: exact \(2\)-adic lift showing
  all eight initial quotients are even; hence distinct quotient ranks satisfy
  \(e_{(k)}\ge2k\), strengthening the largest label barrier to roughly
  \(A-4\sqrt A\).
- `legendre_initial_mod6_quotient_lattice.md`: reduced quotient pencil
  modulo \(3\); A0 quotients satisfy \(e\equiv2,4\pmod6\), A1 quotients
  satisfy \(e\equiv0\pmod6\), giving global quotient lower bounds
  \(2,4,6,8,10,12,18,24\).
- `legendre_initial_A0_mod12_colored_ladder.md`: A0 quotient-label coupling;
  \(e\equiv2\pmod6\) forces the A0 label \(p\equiv1\pmod{12}\), while
  \(e\equiv4\pmod6\) forces \(p\equiv5\pmod{12}\).  Equal A0 quotient colors
  therefore create distance spacing \(12\), not just \(4\).
- `legendre_initial_A1_mod6_signed_ladder.md`: A1 root-sign coupling;
  since A1 has \(e=2f\) with \(3\mid f\), the reduced root satisfies
  \(r+f\equiv\pm1\pmod3\).  The sign determines the A1 label class modulo
  \(6\), and equal signs create distance spacing \(6\), not just \(2\).
- `legendre_initial_colored_quotient_rank_forcing.md`: quotient-rank
  refinement; \(q\) now determines A0 same-color quotient ranks and A1
  layer ranks, giving offset-specific lower bounds
  \(e_i\ge E_i(q,\chi)\), stronger than the global rank barrier alone.
- `legendre_initial_A0_cofactor_mirror.md`: A0 complementary-factor
  restriction; since \(A^2+x^2\equiv1\pmod4\) and both centered factors are
  \(1\bmod4\), one gets \(2r+e\equiv0\pmod4\), not \(e\equiv0\pmod4\).
  This splits A0 quotients by parity of \(m\): \(e\equiv2,10\pmod{12}\) for
  even \(m\), and \(e\equiv4,8\pmod{12}\) for odd \(m\).
- `legendre_initial_A1_cofactor_mirror.md`: A1 complementary-factor
  restriction; in both parity branches, A1 gives \(e\equiv2\pmod4\).
  Combined with \(e\equiv0\pmod6\), this forces all A1 quotients into the
  single class \(e\equiv6\pmod{12}\), with minima \(6,18,30,42\).
- `legendre_initial_odd_A1_mod24_lift.md`: odd-branch A1 lift; reducing the
  A1 half-quotient equation modulo \(8\) gives \(mf\equiv3\pmod4\).  Thus
  \(m\equiv1\pmod4\) forces A1 quotients \(e\equiv6\pmod{24}\), while
  \(m\equiv3\pmod4\) forces \(e\equiv18\pmod{24}\).
- `legendre_initial_even_mod8_quotient_lift.md`: even-branch modulo-\(16\)
  lift; the half-quotient equations split \(m\equiv0,2,4,6\pmod8\), with
  \(m\equiv2\pmod8\) forcing global quotient minima
  \(2,10,14,22,30,42,78,90\).
- `legendre_initial_odd_A0_mod16_lift.md`: odd-branch A0 modulo-\(16\)
  lift; in the branch \(m\equiv3\pmod4\), the A0 minima sharpen from
  \(4,8,16,20\) to \(4,8,16,28\), giving the final skeleton
  \(4,8,16,18,28,42,66,90\).
- `legendre_m3mod4_mod7_zero_filter.md`: structural modulo-\(7\) filter in
  the hard \(m\equiv3\pmod4\) Pell system; if \(7\mid f\), then
  \(u^2\equiv-c\pmod7\), so only offsets \(26,122\) can carry
  \(7\mid f\).  This raises the active skeleton from
  \(4,8,16,18,28,42,66,90\) to \(4,8,16,18,32,42,66,90\).
- `legendre_literature_strategy_reset.md`: proof-strategy reset after the
  quotient-skeleton phase; explains why known short-interval and pure sieve
  methods do not currently close Legendre, and identifies the two plausible
  next routes: Pell-synchronized finite-certificate elimination or an
  almost-prime-to-prime upgrade.
- `legendre_p3_terminal_descent.md`: exact bridge from a between-squares
  \(P_3\) theorem to terminal composite factor equations
  \(N=(n-a)(n+a+k)\), splitting the almost-prime obstruction into the T1,
  T2, and Tfar channels.
- `legendre_p3_weighted_terminal_gap.md`: correction of the geometry-only
  \(P_3\) descent attempt; shows that T1 contains \(n(n+1)\), so near-diagonal
  channels must be attacked through Campbell's actual sieve weights or by
  synchronization with quotient certificates.
- `legendre_campbell_weight_extraction.md`: exact extraction of Campbell's
  Richert weights, final parameters \(k=3,k_1=8,k_2=3.17,z=X^{1/8}\), and the
  \(0.0249\sqrt N/\log X\) margin; identifies the Richert-core terminal
  certificate lemma as the usable \(P_3\)-upgrade target.
- `legendre_richert_terminal_atom_types.md`: classification of Richert-core
  terminal \(P_3\) composites into exactly three atom types: prime-prime,
  lower-prime/upper-semiprime, and lower-semiprime/upper-prime.
- `legendre_p3_upgrade_boundary.md`: proof-level boundary showing that one
  terminal \(P_3\) survivor cannot force Legendre; the semiprime R2 shape
  \(n(n+2)\) is formally compatible, so any \(P_3\)-upgrade must be a
  collective packet/certificate-capacity argument.
- `legendre_m3mod4_pell_system.md`: explicit reduced Pell system for the
  hardest quotient skeleton \(m\equiv3\pmod4\), using \(e=2f,w=2u\),
  layer-specific \(f\)-residue classes, the lifted active sorted skeleton
  \((2,4,8,9,16,21,33,45)\), and the 28 pairwise synchronization equations.
- `legendre_m3mod4_minimal_component_mod7.md`: exact modulo-\(7\)
  certificate eliminating the naive minimal \(m\equiv3\pmod4\) component:
  the required \(f=14\) on \(c=16\) or \(c=64\) forces a nonsquare.
- `legendre_m3mod4_mod7_zero_filter.md`: structural upgrade of the previous
  certificate; \(7\mid f\) is possible only for offsets \(c=26,122\), raising
  the active hard-branch quotient skeleton to
  \(e=(4,8,16,18,32,42,66,90)\).
- `legendre_m3mod4_lifted_boundary_mod5_mod11.md`: exact certificate killing
  the lifted \(m\equiv3\pmod4\) boundary
  \(f=(2,4,8,9,16,21,33,45)\); modulo \(5\) forces a unique assignment, and
  that assignment has empty \(m\bmod11\) intersection.
- `legendre_m3mod4_next_boundary_layer_modular_closure.md`: exact closure of
  the complete next escape layer after the lifted boundary.  The three
  families \(4\leadsto10\), \(16\leadsto22\), and \(45\leadsto57\) are killed
  by small-prime congruence certificates, reducing the hard branch to a
  rank-cap problem.
- `legendre_m3mod4_rank_weight_2_4_closure.md`: rank-game closure of the next
  three layers.  With rank coordinates \((a,b,c)\), all families of weights
  \(a+b+c=2,3,4\) are killed by finite congruence certificates using
  \(5,7,11,13,17\).  Any remaining hard-branch counterexample must have
  \(a+b+c\ge5\), or else the branch closes.
- `legendre_m3mod4_rank_weight_0_30_certificate.md`: deeper finite
  certificate for the hard rank game.  The verifier
  `tools/m3mod4_rank_certificate.py` proves that all rank families with
  \(0\le a+b+c\le30\) are killed by the primes \(5,7,11,13,17\) or by the
  modulo-\(7\) zero filter.  Any remaining hard-branch counterexample must
  have \(a+b+c\ge31\).
- `legendre_m3mod4_periodic_automaton_obstruction.md`: exact obstruction to
  the first periodic closure attempt.  The primes \(5,7,11,13,17\) do not
  kill the full rank automaton: an explicit assignment pattern survives at
  \(m\equiv14325\pmod{85085}\).  The next target is to kill that survivor by
  Pell synchronization or by adding a genuinely necessary modulus.
- `legendre_m3mod4_periodic_boundary_automaton_closed.md`: closure of the
  periodic boundary-rank automaton.  Adding the prime \(83\) kills the unique
  five-prime survivor, and the verifier proves all 48 boundary assignment
  patterns are killed by \(\{5,7,11,13,17,83\}\).
- `legendre_m3mod4_arbitrary_prefix_rank_certificate.md`: stronger
  skipped-rank certificate.  The verifier mode `--prefix-ranks N` checks all
  arbitrary ordered assignments from the first \(N\) layer values; all
  assignments for \(N=7,8,9,10\) are killed by
  \(\{5,7,11,13,17,19,23,29,83\}\).  For \(N=9\), this is 15,676,416
  assignments; for \(N=10\), this is 40,824,000 assignments.
- `legendre_m3mod4_no_finite_local_modular_closure.md`: proof that no finite
  set of independent local square tests can close arbitrary skipped ranks.
  For any finite prime set, sufficiently skipped layer ranks can satisfy all
  local conditions by CRT with \(m\equiv0\).  The remaining closure must use
  Pell synchronization or rank descent.
- `legendre_m3mod4_self_residue_filter.md`: intrinsic quotient filter from
  reducing \(u^2=f^2+6mf-c\) modulo \(f\).  Every quotient must satisfy
  \(u^2\equiv-c\pmod f\), so each prime divisor \(q\mid f\), \(q\nmid c\),
  must have \(\left(\frac{-c}{q}\right)=1\).  This is the first non-finite
  prime mechanism for attacking arbitrary skipped ranks.
- `legendre_m3mod4_A0_square_quotient_theorem.md`: exact prime-power
  classification of the A0 square-offset quotient condition
  \(u^2+x^2\equiv0\pmod f\), with \(x\in\{2,4,8,10\}\).  It forces all odd
  prime divisors of \(f\) to be \(1\bmod4\) in these four cases, and gives
  offset-specific \(2\)-adic ceilings \(v_2(f)\le3,5,7,3\).
- `legendre_m3mod4_A1_quadratic_field_quotient_theorem.md`: exact
  prime-power classification of the A1 self-residue condition
  \(u^2\equiv-c\pmod f\).  A1 quotients must split in the offset-specific
  quadratic fields \(\mathbb Q(\sqrt{-c})\), with ramified caps
  \(v_{13}(f)\le1\), \(v_5(f)\le2\), and \(v_{61}(f)\le1\).
- `legendre_m3mod4_A0_zero_layer_collapse.md`: structural consequence of
  the A0 quotient theorem.  For \(c=16,64\), the old zero-layer classes
  \(f\equiv14,22\pmod{24}\) are impossible; the layer collapses to
  \(f\equiv8,16\pmod{24}\) with \(f=2^\nu s\) and all odd primes of \(s\)
  equal to \(1\bmod4\).
- `legendre_m3mod4_A0_four_layer_refinement.md`: companion structural
  refinement for \(c=4,100\).  The old layer
  \(f\equiv2,4,10,20\pmod{24}\) becomes
  \(f=2s\) or \(4s\), where \(s\) is odd, \(3\nmid s\), and all primes of
  \(s\) are \(1\bmod4\); residue-wise this excludes
  \(f\equiv28,44\pmod{48}\).
- `legendre_m3mod4_multiplicative_rank_model.md`: replacement of the old
  additive rank automaton by offset-specific multiplicative quotient
  semigroups.  A hard-branch counterexample must solve the pairwise Pell
  synchronization equations with \(f_c\) in the A0 sum-of-two-squares
  semigroups or the A1 quadratic-field splitting semigroups.
- `legendre_m3mod4_shared_prime_compatibility.md`: edge constraint for the
  multiplicative model.  Any prime dividing two quotients must lie in the
  intersection of the two relevant splitting laws; in particular A0--A1
  common divisors are coprime to \(6\), and nonramified shared primes split
  in \(\mathbb Q(\sqrt{-c},\sqrt{-d})\).
- `legendre_m3mod4_dual_factor_gap_model.md`: two-sided strengthening of
  the multiplicative model.  Each line factors as
  \(u_c^2+c=f_c(f_c+6m)\), so the upper factor \(F_c=f_c+6m\) satisfies the
  same offset-specific splitting law as the lower quotient \(f_c\).  The
  hard branch becomes eight same-gap factor pairs with
  \(F_c-f_c\equiv18\pmod{24}\).
- `legendre_m3mod4_A0_dual_four_layer_collapse.md`: dual-factor collapse of
  the A0 \(c=4,100\) lower layer.  The branch \(f=4s\) is impossible because
  the upper factor has odd part \(3\bmod4\); hence \(f\in2\mathcal S_4\),
  and the first two distinct lower quotients are \(2,10\), not \(2,4\).
- `legendre_m3mod4_A0_dual_valuation_collapse.md`: exact \(2\)-adic product
  valuation collapse for the A0 zero layer.  The equality \(u^2+x^2=fF\)
  forces \(c=16\) to use only \(8\mathcal S_4\cup16\mathcal S_4\), and
  \(c=64\) to use only \(8\mathcal S_4\cup32\mathcal S_4\cup64\mathcal S_4\);
  in particular \(f=16\) can only belong to the \(c=16\) row.
- `legendre_m3mod4_A1_dual_sign_parity.md`: two-sided A1 sign law.  Since
  \(f_c\equiv1\bmod4\) and \(F_c=f_c+6m\equiv3\bmod4\), the two factors
  split in the same quadratic field but have opposite parity for the number
  of prime divisors \(q\equiv3\bmod4\).
- `legendre_m3mod4_A0_dual_boundary_mod23.md`: exact modulo-\(23\)
  certificate killing the new A0 structural boundary after the dual
  collapses.  With \(c=16\mapsto16\), \(c=64\mapsto8\), both possible
  assignments \(c=4,100\mapsto2,10\) have empty \(m\bmod23\) intersection.
- `legendre_m3mod4_A0_dual_prefix2_certificate.md`: exact certificate
  killing all six pairwise-distinct assignments from the first two
  structural A0 lower quotients after the dual collapses.  Any remaining
  hard-branch point must use \(f\ge26\) on \(c=4,100\), or \(f\ge40\) on
  \(c=16\) or \(c=64\).
- `legendre_m3mod4_structural_prefix6_certificate.md`: exact closure of the
  first seven structural quotient values in every offset row.  The verifier
  kills 2,882,250 distinct assignments by finite local certificates except
  two ghost fibers, and both ghost fibers force \(m=-1\), hence no positive
  hard-branch point.
- `legendre_m3mod4_prefix8_exceptional_pell_fibers.md`: exact decomposition
  of the prefix-\(8\) frontier.  The 15 survivors split into two ghost
  fibers \(m=-1\), eight boundary fibers \(m=3\), three systems impossible
  modulo \(9\), and two residual coupled Pell systems.  The remaining closure
  target is to kill these two explicit systems, not to extend a CRT descent.
- `tools/m3mod4_structural_prefix_certificate.py`: reproduces the structural
  prefix certificate, the \(m=-1\) ghost-fiber closure, and the prefix-\(8\)
  exceptional-fiber decomposition.
- `tools/m3mod4_residual_pell_fibers.magma`: exact external closure target
  for the two remaining residual prefix-\(8\) systems.  It asks Magma to solve
  the genus-one quartic
  \(W^2=1845s^4-128s^2-117\) and then filters the separated square equations.
- `legendre_m3mod4_residual_elliptic_mwrank_certificate.md`: elliptic
  reformulation of the residual quartic as
  \(Y^2=X^3-128X^2-215865X\), together with the unconditional `mwrank`
  Mordell-Weil data: torsion \((\mathbf Z/2\mathbf Z)^2\), rank \(3\), and
  basis \((-363,3696),(-195,5460),(-117,4680)\).
- `tools/m3mod4_residual_elliptic_mwrank.sh`: reproduces the `mwrank`
  certificate when eclib is available.
- `tools/m3mod4_residual_mw_sieve.py`: first Mordell-Weil sieve scaffold for
  the residual rank-\(3\) curve.  It reduces the certified Mordell-Weil basis
  modulo good primes and supports the common core and the two terminal
  residual fibers \(R4,R5\).
- `literature/`: reading pack with an arXiv manifest, BibTeX file, and
  proof-use notes for short-interval primes, almost-primes between squares,
  prime gaps, Maier matrix methods, and computational verification.

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
\(Q_j\equiv1\pmod4\).  The corresponding A0 distances are all congruent to
\(A-1\pmod4\), so their ordered lower bounds strengthen to
\[
  \rho_j\ge
  \max_{j\le\ell\le4}
  \left(B_{5-\ell}(A)+4(\ell-j)\right).
\]
The A1 distances satisfy the analogous parity envelope with spacing \(2\).
Globally, all eight labels are odd primes, so all eight center-distances lie
in the same parity class.  For a fixed A0/A1 label-order word \(L\), this
gives a word-dependent ladder \(D_i\ge H_i^L(A)\); A0 positions add stronger
modulo-\(4\) edges.  A clean strong-gate counterexample is therefore a finite
two-layer ladder certificate: a layer word, a layer-respecting matching from
offsets to label positions, a quotient-rank permutation satisfying
\(\operatorname{Inv}(q)\subseteq\operatorname{Inv}(s)\), and the centered
divisor equations for all eight offsets.
The quotient-first variant writes \(w=2r+e\), turning each centered
factorization into
\[
  w^2=4eA+e^2-4c.
\]
Since \(A=3m\), every quotient must satisfy the local congruence
\[
  w^2\equiv e^2-4c\pmod{12e}.
\]
Thus odd primes dividing \(e\), away from \(c\), must split in
\(\mathbb Q(\sqrt{-c})\).  For A0 this forces quotient primes
\(\equiv1\pmod4\), except for coordinate primes.  Eliminating \(A\) between
two offsets gives a Pell-type synchronization equation independent of the
center.
The same parity analysis gives a stronger rank input: all eight initial
quotients are even.  For \(m\ge4881\), they are distinct, hence
\[
  e_{(k)}\ge2k.
\]
The quotient-rank barrier is therefore upgraded to
\[
  \widetilde B_k(A)=
  \left\lceil -k+\sqrt{k^2+2kA-122}\right\rceil,
\]
so the smallest label must already fall below
\[
  A-\widetilde B_8(A)
  =
  A-\left\lceil -8+\sqrt{16A-58}\right\rceil.
\]
Reducing the half-quotient pencil modulo \(3\) separates the layers:
A0 quotients are \(2\) or \(4\bmod6\), while A1 quotients are \(0\bmod6\).
Thus the global quotient ranks are bounded below by
\[
  2,4,6,8,10,12,18,24,
\]
and the largest-rank distance is forced beyond
\[
  \left\lceil -12+\sqrt{24A+22}\right\rceil.
\]
For A0, the quotient class modulo \(6\) also determines the label class
modulo \(12\):
\[
  e\equiv2\pmod6\Rightarrow p\equiv1\pmod{12},\qquad
  e\equiv4\pmod6\Rightarrow p\equiv5\pmod{12}.
\]
The A0 ladder is therefore colored: equal quotient colors force distance
spacing \(12\), while different A0 colors retain the basic spacing \(4\).
For A1, the quotient class is always \(0\bmod6\), but the reduced root sign
plays the same role:
\[
  r+f\equiv\varepsilon\pmod3,\qquad \varepsilon=\pm1.
\]
Then
\[
  \varepsilon=1\Rightarrow p\equiv5\pmod6,\qquad
  \varepsilon=-1\Rightarrow p\equiv1\pmod6.
\]
Equal A1 signs therefore force distance spacing \(6\).
The quotient permutation \(q\) is now colored: an A0 quotient of color
\(\chi\in\{2,4\}\) with same-color rank \(\kappa\) satisfies
\[
  e\ge \chi+6(\kappa-1),
\]
while an A1 quotient with A1-layer rank \(\lambda\) satisfies
\[
  e\ge6\lambda.
\]
Thus each offset gets an individual quotient lower bound
\[
  E_i(q,\chi),
\]
which replaces the rank-only barrier in the fully colored ladder.
A0 has an additional cofactor mirror: in
\[
  A^2+x^2=(A-r)(A+r+e),
\]
both factors are \(1\bmod4\), so
\[
  2r+e\equiv0\pmod4.
\]
This is parity-sensitive.  If \(m\) is even, A0 quotients are
\[
  2\text{ or }10\bmod12,
\]
and the quotient minima are
\[
  2,6,10,12,14,18,22,24.
\]
If \(m\) is odd, A0 quotients are
\[
  4\text{ or }8\bmod12,
\]
and the quotient minima are
\[
  4,6,8,12,16,18,20,24,
\]
with A0 same-color ranks advancing by \(12\) in both parity branches.
A1 also has a cofactor mirror.  It gives uniformly
\[
  e\equiv2\pmod4,
\]
and since A1 already has \(e\equiv0\pmod6\), every A1 quotient satisfies
\[
  e\equiv6\pmod{12}.
\]
Thus A1 minima become \(6,18,30,42\), and the cofactor quotient skeletons
are
\[
  M^{\mathrm{even},\mathrm{cof}}=(2,6,10,14,18,22,30,42),
\]
\[
  M^{\mathrm{odd},\mathrm{cof}}=(4,6,8,16,18,20,30,42).
\]
In the odd branch this sharpens further.  Writing \(e=2f\), the A1 equation
modulo \(8\) forces
\[
  mf\equiv3\pmod4.
\]
So if \(m\equiv1\pmod4\), A1 quotients are \(6\bmod24\), giving
\[
  (4,6,8,16,20,30,54,78),
\]
and if \(m\equiv3\pmod4\), A1 quotients are \(18\bmod24\), giving
\[
  (4,8,16,18,20,42,66,90).
\]
In the even branch, reducing the half-quotient equations modulo \(16\)
splits \(m\bmod8\).  The quotient skeletons become
\[
\begin{array}{c|c}
  m\bmod8 & \text{global quotient minima}\\
  \hline
  0 & 2,6,10,14,18,22,30,42\\
  2 & 2,10,14,22,30,42,78,90\\
  4 & 2,6,10,14,18,22,30,42\\
  6 & 2,6,10,14,18,22,54,66.
\end{array}
\]
The odd A0 modulo-\(16\) lift sharpens the \(m\equiv3\pmod4\) branch:
\[
  (4,8,16,18,20,42,66,90)
  \quad\leadsto\quad
  (4,8,16,18,28,42,66,90).
\]
The modulo-\(7\) zero-quotient filter then raises this hard branch once more:
\[
  (4,8,16,18,28,42,66,90)
  \quad\leadsto\quad
  (4,8,16,18,32,42,66,90).
\]
The lifted boundary is then killed exactly by the modulo \(5\)/\(11\)
certificate.  The next obstruction is the finite union in which at least one
layer boundary is raised:
\[
  4\leadsto10
  \quad\text{or}\quad
  16\leadsto22
  \quad\text{or}\quad
  45\leadsto57
\]
in \(f\)-variables.
That complete first escape layer is now also killed: \(16\leadsto22\) dies
modulo \(5\), while \(4\leadsto10\) and \(45\leadsto57\) die by
\((5,7,11)\) certificates.  The remaining closure mechanism must supply an
a priori rank cap for the hard quotient game; then the modular matching
certificates become a finite proof object.
The next three rank weights are also closed: all families with
\[
  a+b+c=2,3,4
\]
die by finite congruence certificates.  The sharp closure fork is now:
prove \(a+b+c\le4\) for any hard-branch counterexample, or prove that the
same modular automaton kills all rank triples periodically.
The finite certificate has since been pushed to weight \(30\).  Thus the
rank-cap route would now need only \(a+b+c\le30\), while the more natural
route is a periodicity or descent theorem for the modular automaton.
The first periodicity attempt with only \(5,7,11,13,17\) is false: one
periodic assignment pattern survives.  The closure target has therefore
shifted from more weight climbing to killing that survivor pattern by the
pairwise Pell synchronization equations.
That survivor is killed uniformly by \(83\), and all 48 periodic boundary
assignment patterns are now closed by
\[
  \{5,7,11,13,17,83\}.
\]
The remaining hard-branch gap is no longer this boundary automaton; it is
the descent/reduction from arbitrary skipped quotient ranks to the boundary
rank model.
The skipped-rank gap is now partially attacked directly: all arbitrary
ordered assignments using the first ten admissible values of each layer are
closed by
\[
  \{5,7,11,13,17,19,23,29,83\}.
\]
Any remaining hard-branch counterexample must escape beyond rank \(8\) in at
least one layer, and in fact beyond rank \(9\) after the \(N=10\)
certificate.
However, arbitrary skipped ranks cannot be closed by simply adding finitely
many independent local square tests: CRT lets sufficiently high ranks satisfy
any fixed finite prime set.  The next proof step must use global Pell
synchronization or a rank descent.
The new self-residue filter supplies the missing non-finite mechanism:
reducing each row modulo its own quotient \(f\) forces \(-c\) to be a square
modulo \(f\), so bad prime divisors of \(f\) kill skipped ranks intrinsically.
The strategy reset records the current status: the quotient skeletons are a
certificate language, not a proof.  Known short-interval prime technology
still lies above the \(x^{1/2}\) Legendre threshold, and pure sieve methods
run into the parity problem.  The next serious proof attempt should either
eliminate one quotient skeleton by Pell synchronization, or connect modern
almost-prime-in-square-interval results to a prime-producing descent.

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
