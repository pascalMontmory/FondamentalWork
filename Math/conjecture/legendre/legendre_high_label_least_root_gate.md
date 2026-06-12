# High-Label Least-Root Gate

This note strengthens the high-label one-shot theorem.

The one-shot theorem says that large certificate primes cannot repeat across
complete A-blocks.  Here we record the sharper fact: sufficiently large
labels are not merely one-shot; they are exactly small least-root events.

## 1. Threshold

Let
\[
  A=3m,
\]
and let
\[
  T_m=\lfloor\sqrt{6m}\rfloor.
\]
Every A-coordinate \(t\) in a complete block satisfies
\[
  1\le t\le T_m.
\]

Define the least-root threshold
\[
  C_m=2T_m.
\]

If
\[
  p>C_m,
\]
then every admissible \(t\) satisfies
\[
  0<t<\frac p2.
\]
Thus a congruence modulo \(p\) determines \(t\) as the least positive
absolute residue of a root.

## 2. Gaussian layer

For the A0 layer,
\[
  G=A^2+t^2.
\]
Let \(p>C_m\) be an eligible A0 prime:
\[
  p\le A,\qquad p\equiv1\pmod4,\qquad p\nmid A.
\]

Choose \(i_p\) with
\[
  i_p^2\equiv-1\pmod p.
\]
Then
\[
  p\mid A^2+t^2
\]
if and only if
\[
  t\equiv \pm Ai_p\pmod p.
\]
Since \(0<t<p/2\), this is equivalent to
\[
  t=\|Ai_p\|_p,
\]
where \(\|x\|_p\) denotes the least positive absolute residue:
\[
  \|x\|_p=\min_{k\in\mathbf Z}|x-kp|.
\]

Therefore a high A0 label exists only when
\[
  \boxed{
  \|Ai_p\|_p\le T_m.
  }
\]

The corresponding block is then forced by \(t\) and by the A0 parity rule.
It is not a free residue class.

## 3. Unit-lift layer

For the A1 layer,
\[
  U=A^2+t^2+1.
\]
Let \(p>C_m\) be an eligible A1 prime:
\[
  p\le A,\qquad p\nmid A^2+1,
\]
and suppose
\[
  -A^2-1
\]
is a quadratic residue modulo \(p\).

Let \(s_p\) be any square root:
\[
  s_p^2\equiv-A^2-1\pmod p.
\]
Then
\[
  p\mid A^2+t^2+1
\]
with \(0<t<p/2\) is equivalent to
\[
  t=\|s_p\|_p.
\]

Thus a high A1 label exists only when
\[
  \boxed{
  \|s_p\|_p\le T_m.
  }
\]

Again the block is forced by this least root and the A1 parity rule.

## 4. Exact high-label encoding

Define the high-root sets
\[
  \mathcal H_0(m)=
  \left\{
  p:
  C_m<p\le A,\ p\equiv1\pmod4,\ p\nmid A,\
  \|Ai_p\|_p\le T_m
  \right\},
\]
and
\[
  \mathcal H_1(m)=
  \left\{
  p:
  C_m<p\le A,\ p\nmid A^2+1,\
  \exists s_p^2\equiv-A^2-1\pmod p,\
  \|s_p\|_p\le T_m
  \right\}.
\]

Each prime in \(\mathcal H_i(m)\) determines at most one A-coordinate
\[
  t\in[1,T_m].
\]
After imposing \(3\nmid t\), parity, completeness, and the coprime-block
condition, it determines at most one complete coprime A-block in that layer.

Thus high-label coverage is exactly the image of the two least-root maps
\[
  p\mapsto \|Ai_p\|_p,
  \qquad
  p\mapsto \|s_p\|_p.
\]

## 5. Consequence for a counterexample

A counterexample must cover every coprime complete block in both layers.
For any block using a high A0 label, that label must lie in
\(\mathcal H_0(m)\).  For any block using a high A1 label, that label must
lie in \(\mathcal H_1(m)\).

Therefore the high one-shot branch is not an arbitrary supply of fresh
labels.  It requires enough primes \(p\le A\) for which a specified modular
square root has least absolute residue at most
\[
  T_m\asymp\sqrt A.
\]

The remaining closure target can be stated as:

> **Least-root non-cover lemma.**  The union of the low-label repeated
> cover and the high-label least-root images cannot cover all complete
> coprime A-blocks in both A0 and A1 layers.

This is a different analytic object from the original residue cover.  It is
closer to a problem on the distribution of least square roots modulo primes,
with the moving parameter \(A=3m\).
