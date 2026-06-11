# Initial Pairwise-Coprime Cluster

This note records the strongest consequence so far of the initial gate
analysis.

In the clean strong gate, the eight candidate values attached to the first
four complete A-blocks are pairwise coprime.  Therefore a counterexample must
begin with a short cluster of eight pairwise coprime composite integers, each
having a small prime divisor.

No computation is used here.  The proof is only gcd algebra and the previous
same-layer and cross-layer collision lemmas.

## 1. The eight initial candidates

For \(j=0,1,2,3\), write
\[
  G_j=9m^2+t_0(j)^2,
\]
and
\[
  U_j=9m^2+t_1(j)^2+1.
\]

These are the A0 and A1 candidates on the first four blocks
\[
  B_0,\ B_1,\ B_2,\ B_3.
\]

Assume:

1. \(m\ge21\), so the four blocks are complete;
2. \(m\not\equiv\pm1\pmod5\), so the four blocks are coprime;
3. \(m\) lies in a no-same-layer-repetition class of the mod \(70\) gate;
4. \(m\) avoids the cross-layer collision congruences listed in
   `legendre_initial_cross_layer_collisions.md`.

Call this the clean strong gate.

## 2. Same-block coprimality

For each block \(B_j\), the exact A-block gcd formula gives
\[
  \gcd(G_j,U_j)=1
\]
because the block is coprime.

Thus no prime can divide both candidates in the same block.

## 3. Same-layer coprimality

Suppose a prime \(p\) divides two distinct A0 candidates:
\[
  p\mid G_i,\qquad p\mid G_j,\qquad i\ne j.
\]
Then
\[
  t_0(i)^2\equiv t_0(j)^2\pmod p.
\]

The candidates \(G_i,G_j\) are odd and not divisible by \(3\):
\[
  G_j\equiv1\pmod3.
\]
So any common prime satisfies \(p\ge5\).

But a common prime \(p\ge5\) is exactly a same-layer repetition in the A0
layer.  The clean strong gate excludes all such repetitions among the first
four blocks.  Hence
\[
  \gcd(G_i,G_j)=1
  \qquad(i\ne j).
\]

The same argument applies to the A1 layer.  If
\[
  p\mid U_i,\qquad p\mid U_j,\qquad i\ne j,
\]
then
\[
  t_1(i)^2\equiv t_1(j)^2\pmod p.
\]
The values \(U_j\) are odd and satisfy
\[
  U_j\equiv2\pmod3.
\]
Thus any common prime again has \(p\ge5\), and would be a forbidden A1
same-layer repetition.  Therefore
\[
  \gcd(U_i,U_j)=1
  \qquad(i\ne j).
\]

## 4. Cross-layer coprimality

Suppose a prime \(p\) divides an A0 value and an A1 value in different
blocks:
\[
  p\mid G_i,
  \qquad
  p\mid U_j,
  \qquad i\ne j.
\]
Then
\[
  p\mid 9m^2+t_0(i)^2,
\]
and
\[
  p\mid 9m^2+t_1(j)^2+1.
\]
Subtracting gives
\[
  p\mid t_1(j)^2+1-t_0(i)^2.
\]

The values are again odd and not divisible by \(3\), so any common prime has
\[
  p\ge5.
\]

This is exactly a cross-layer collision.  By the clean strong gate
hypothesis, all cross-layer collision congruences among the first four blocks
are excluded.  Hence
\[
  \gcd(G_i,U_j)=1
  \qquad(i\ne j).
\]

Together with same-block coprimality, this proves:
\[
\boxed{
  \text{The eight integers }G_0,\dots,G_3,U_0,\dots,U_3
  \text{ are pairwise coprime.}
}
\]

## 5. Consequence for a counterexample

If the combined A-channel fails on these four blocks, then every one of the
eight values
\[
  G_0,G_1,G_2,G_3,U_0,U_1,U_2,U_3
\]
is composite.

Since the eight values are pairwise coprime, each must contribute a distinct
prime divisor.  Moreover, because all eight values lie below \((3m+1)^2\) in
the Legendre interval, each composite value has a prime divisor
\[
  p\le3m.
\]

Thus a counterexample in the clean strong gate forces eight distinct small
prime labels.  Equivalently, if
\[
  \Omega_m=
  \prod_{j=0}^{3}G_jU_j,
\]
then the squarefree kernel of \(\Omega_m\), restricted to primes
\[
  5\le p\le3m,
\]
contains at least eight primes satisfying the corresponding A0/A1
congruences.

## 6. Closure target

The strong-gate closure target can now be stated without label language:

> For every \(m\) in the clean strong gate, the eight initial candidates
> cannot all be composite and pairwise coprime with small prime divisors
> \(p\le3m\).

Equivalently, one must prove that the short cluster
\[
  9m^2+\{t_0(0)^2,t_0(1)^2,t_0(2)^2,t_0(3)^2\},
\]
\[
  9m^2+\{t_1(0)^2+1,t_1(1)^2+1,t_1(2)^2+1,t_1(3)^2+1\}
\]
cannot be a cluster of eight pairwise coprime composites in the clean strong
gate.

This is still a remaining obstruction, not a completed proof of Legendre.
But it is a strictly sharper proof target than the original residue cover:
the first four blocks already force a rigid pairwise-coprime composite
cluster.
