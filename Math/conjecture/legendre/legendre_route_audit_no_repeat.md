# Route Audit: What Not To Repeat

This note audits the Legendre workbench to avoid repeating routes that have
already been explored.

It records a hard conclusion: local fibers, initial blocks, rank barriers,
and residue colors are useful certificate language, but they are not by
themselves a closure mechanism.

## 1. Gaussian and bounded-offset route

Files:

- `legendre_residue_gaussian_note.md`
- `legendre_exact_circle_cover_attack.md`
- `legendre_circle_residue_calculus.md`
- `legendre_four_consecutive_certificate.md`
- `legendre_primitive_channel_reduction.md`
- `legendre_primitive_double_cover.md`
- `tools/gaussian_*.py`

Outcome:

- The pure Gaussian square-offset lemma is false.
- The corrected four-offset family
  \[
    t^2-1,\quad t^2,\quad t^2+1,\quad t^2+2
  \]
  is the right experimental skeleton.
- It leads naturally to a residue-cover certificate, not a proof.

Do not repeat:

> Do not try to prove Legendre by the pure square norm channel
> \(n^2+t^2\).  It already fails.

Usable residue:

> Keep the four-offset family as the certificate surface.

## 2. Multiple-of-three split

Files:

- `legendre_multiple_of_three_channel.md`
- `legendre_multiple_of_three_refined_channels.md`
- `legendre_m3star_certificate.md`
- `tools/multiple_of_three_channel_measure.py`

Outcome:

- The first \(M_3\) candidate was false because it missed the
  \(3\nmid t,\ r=1\) channel.
- The corrected \(M_3^\ast\) split is exact:
  primitive \(r=0\), unit-lift \(r=1\), and nonprimitive \(t=3u\).

Do not repeat:

> Do not split \(3\mid n\) into only primitive and \(t=3u\).  The
> \(3\nmid t,\ r=1\) unit-lift channel is mandatory.

Usable residue:

> The \(t=3u\) channel is a repair mechanism, not a global proof by itself.

## 3. Initial block escalation

Files:

- `legendre_initial_block_obstruction.md`
- `legendre_initial_mod10_gate.md`
- `legendre_initial_four_block_graph.md`
- `legendre_initial_mod70_gate.md`
- `legendre_first_four_ordered_pair_distinct.md`
- `legendre_first_five_ordered_pair_repetition.md`
- `legendre_first_six_ordered_pair_repetition.md`

Outcome:

- The first blocks have strong exact repetition restrictions.
- Ordered pairs do not repeat among the first four coprime blocks.
- Extending to five and six blocks gives explicit exceptional gates.

Do not repeat:

> Do not keep adding initial blocks hoping the contradiction appears.  This
> route creates more finite gates but no global closure mechanism.

Usable residue:

> Initial blocks are good for calibration and for detecting bridge fibers.

## 4. Quotient, rank, ladder, and Pell skeleton route

Files:

- `legendre_initial_center_divisor_parametrization.md`
- `legendre_initial_pair_quotient_compatibility.md`
- `legendre_initial_quotient_rank_barrier.md`
- `legendre_initial_quotient_pell_pencil.md`
- `legendre_initial_*_ladder*.md`
- `legendre_m3mod4_*.md`

Outcome:

- The centered divisor form
  \[
    A-r\mid r^2+c
  \]
  is the best certificate language found.
- Quotient ranks force strong lower bounds on distances.
- Several \(m\equiv3\pmod4\) residual branches were closed, including a
  final elliptic endpoint via a \(3\)-adic Mordell-Weil coset argument.

Do not repeat:

> Do not expect rank lower bounds alone to close Legendre.  They push labels
> below \(A\), but do not contradict their existence.

Usable residue:

> The centered quotient language should be kept, but only as a compressed
> certificate language for a different proof mechanism.

## 5. Mobius-dual and cofactor route

Files:

- `legendre_global_mobius_dual_gate.md`
- `legendre_mobius_root_count_formula.md`
- `legendre_cofactor_augmented_mobius_gate.md`
- `legendre_centered_cofactor_pair_gate.md`

Outcome:

- There is an exact global positivity target
  \[
    Z(m)>0.
  \]
- The root counts can be written by CRT with explicit bridge removal.
- The untruncated Mobius identity still faces the parity problem.
- Cofactor equations add missing rigidity:
  \[
    p_1X_1-p_0X_0=\pm2t_1(q).
  \]

Do not repeat:

> Do not try to prove positivity by the raw Mobius expansion alone.  It
> needs a parity-breaking or cofactor-energy ingredient.

Usable residue:

> The cofactor pair equation is one of the few global-looking constraints
> available.  It should be combined with a compressed certificate, not used
> as another local gate.

## 6. High-label least-root route

Files:

- `legendre_global_high_label_oneshot.md`
- `legendre_high_label_least_root_gate.md`
- `legendre_capacity_dichotomy.md`
- `legendre_high_high_adjacency_gate.md`
- `legendre_layer_zone_cover_matrix.md`
- `legendre_mixed_high_low_neighbor_gate.md`
- `legendre_current_boundary_of_attack.md`
- `tools/least_root_zone_probe.py`

Outcome:

- High labels are one-shot.
- High labels become least-root events.
- The cover decomposes into low, middle, mixed, and high-high cells.

Do not repeat:

> Do not continue the least-root CRT descent as the main proof.  The
> \(m=391\) full cover shows that a pure open-A-block lemma is false.

Usable residue:

> The high-label theorem is useful to bound repetition.  It does not close
> the residual full-cover cases.

## 7. \(u=1\), ramified fibers, and shared-\(5\)

Files:

- `legendre_u1_repair_cluster_gate.md`
- `legendre_u1_cluster_quotient_rank_gate.md`
- `legendre_u1_cluster_colored_distance_gate.md`
- `legendre_u1_ramified_fiber_descent_gate.md`
- `legendre_u1_shared5_collapse_gate.md`
- `legendre_u1_odd5_u2_lift_gate.md`
- `legendre_shared5_bridge_coupling_gate.md`
- `legendre_shared5_fresh_block_color_gate.md`
- `legendre_shared5_variable_label_rank_gate.md`

Outcome:

- The \(u=1\) repair failure forces finite clusters.
- Ramified fibers become deterministic atoms.
- The shared-\(5\) fiber equals the even \(B_3\) bridge class.
- In shared-\(5\), five variable offsets
  \[
    \{5,17,25,49,65\}
  \]
  require five distinct labels, and for \(A\ge3488\), five distinct quotient
  ranks.

Do not repeat:

> Do not keep splitting fibers unless the split creates a contraction,
> a global identity, or an impossible Diophantine system.  Fibers alone will
> not prove Legendre.

Usable residue:

> Shared-\(5\) is now the best pilot for a compressed-certificate attack.

## 8. Literature lessons

Files:

- `literature/README.md`
- `literature/references.bib`
- `legendre_literature_strategy_reset.md`

Outcome:

- Direct short-interval prime technology remains above the square-root
  threshold.
- Almost-prime results reach close structural analogues but do not break
  parity.
- Recent proof patterns suggest compression of witnesses, not enumeration
  of local cases.

Do not repeat:

> Do not try to beat Baker-Harman-Pintz/Guth-Maynard exponents from inside
> this elementary certificate framework.

Usable residue:

> Borrow the modern pattern: compress a bad object, attach an invariant, and
> prove non-realization.

## 9. Actual pivot

The only direction that is not just a repetition is:

> Build a compressed certificate non-realization theorem.

For the pilot shared-\(5\) fiber:
\[
  \mathcal C=\{5,17,25,49,65\}.
\]

Known:

- five labels are pairwise distinct;
- for \(A\ge3488\), five quotients are pairwise distinct;
- all labels satisfy centered divisor equations and color restrictions;
- the same center \(A\) imposes pairwise compatibility equations.

New target:

> Prove that the five-offset shared-\(5\) certificate has no realization for
> \(A\ge3488\), after separating ramified gates \(7\mid A\), \(13\mid A\),
> and \(17\mid A\).

This is not a fiber split.  It is a non-realization theorem for a compressed
certificate.

## 10. Practical rule going forward

Before adding any new note, check whether it is one of:

1. another initial-block extension;
2. another isolated fiber split;
3. another rank lower bound without contradiction;
4. another local congruence color.

If yes, do not do it unless it feeds directly into the compressed
non-realization theorem.

The next acceptable outputs are:

- an exact elimination system for shared-\(5\);
- a modular certificate killing one quotient-rank permutation;
- a proof that all quotient-rank permutations reduce to finitely many
ramified gates;
- a genuine descent \(A\mapsto A'<A\).
