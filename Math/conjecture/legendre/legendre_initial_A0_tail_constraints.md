# Initial A0 Tail Constraints

This note projects the global label order-statistic barrier onto the A0
layer.

The global barrier controls all eight prime labels.  Since exactly four of
those labels come from A0, and every A0 label satisfies
\[
  p\equiv1\pmod4,
\]
one gets a forced lower tail of primes \(1\bmod4\).

This is a pigeonhole consequence, but it is exact.

## 1. Global sorted-label barrier

In the clean strong gate with
\[
  m\ge4881,
\]
let all eight prime labels be sorted increasingly:
\[
  P_1<P_2<\cdots<P_8.
\]

The order-statistic barrier gives
\[
\boxed{
  P_j\le A-B_{9-j}(A)
  \qquad(1\le j\le8),
}
\]
where
\[
  B_k(A)=
  \left\lceil
  \frac{-k+\sqrt{k^2+4(kA-122)}}{2}
  \right\rceil.
\]

## 2. Extracting the A0 labels

Let the four A0 labels be sorted increasingly:
\[
  Q_1<Q_2<Q_3<Q_4.
\]

Among the first
\[
  j+4
\]
global labels
\[
  P_1,\dots,P_{j+4},
\]
there must be at least \(j\) A0 labels, because there are only four A1
labels total.

Therefore
\[
\boxed{
  Q_j\le P_{j+4}
  \qquad(1\le j\le4).
}
\]

Combining with the global sorted-label barrier gives:
\[
\boxed{
  Q_j\le A-B_{5-j}(A)
  \qquad(1\le j\le4).
}
\]

Explicitly:
\[
\boxed{
  Q_1\le A-B_4(A),
}
\]
\[
\boxed{
  Q_2\le A-B_3(A),
}
\]
\[
\boxed{
  Q_3\le A-B_2(A),
}
\]
\[
\boxed{
  Q_4\le A-B_1(A).
}
\]

Thus the A0 layer cannot place all four \(1\bmod4\) labels near the top of
the allowed prime interval.  At least one A0 label lies below \(A-B_4(A)\),
at least two below \(A-B_3(A)\), at least three below \(A-B_2(A)\), and all
four below \(A-B_1(A)\).

## 3. A0 congruence in center-distance form

For an A0 label,
\[
  p=A-r
\]
and
\[
  p\equiv1\pmod4.
\]
Therefore every A0 distance satisfies
\[
\boxed{
  r\equiv A-1\pmod4.
}
\]

Consequently, the A0 tail constraints can be restated in terms of four
distances
\[
  \rho_1>\rho_2>\rho_3>\rho_4
\]
corresponding to
\[
  Q_1<Q_2<Q_3<Q_4,
\]
because smaller labels mean larger distances:
\[
  Q_j=A-\rho_j.
\]

The inequalities above become
\[
\boxed{
  \rho_j\ge B_{5-j}(A)
  \qquad(1\le j\le4),
}
\]
with
\[
  \rho_j\equiv A-1\pmod4.
\]

So the A0 layer must contain four distances in the same residue class modulo
\[
  4,
\]
with the ordered lower bounds
\[
  \rho_1\ge B_4(A),\quad
  \rho_2\ge B_3(A),\quad
  \rho_3\ge B_2(A),\quad
  \rho_4\ge B_1(A).
\]

## 4. Offset-specific A0 divisor form

The A0 offsets are squares:
\[
  c=x^2.
\]

For an A0 coordinate \(x\), the center-divisor condition is
\[
  A-r\mid r^2+x^2.
\]

Together with
\[
  A-r\equiv1\pmod4,
\]
this is the exact Gaussian condition in center-distance form.

Thus a clean strong-gate counterexample forces four distinct pairs
\[
  (x,r_x)
\]
from the A0 coordinates, satisfying:
\[
\boxed{
  A-r_x\mid r_x^2+x^2,
}
\]
\[
\boxed{
  A-r_x\equiv1\pmod4,
}
\]
and, after ordering their prime labels increasingly, the tail inequalities
above.

## 5. Clean strong-gate consequence

The A0 projection of the global label tail is:

> among the four A0 labels, the \(j\)-th smallest must satisfy
> \[
>   Q_j\le A-B_{5-j}(A),
> \]
> and each such label is \(1\bmod4\).

Equivalently, in distance form, the four A0 distances must lie in the single
residue class
\[
  A-1\pmod4
\]
and must satisfy the ordered lower bounds
\[
  B_4(A),\ B_3(A),\ B_2(A),\ B_1(A).
\]

This does not close the clean strong gate.  It isolates the next exact
target: prove that the four A0 square offsets cannot supply four distinct
Gaussian labels \(1\bmod4\) meeting this forced lower-tail profile while also
remaining compatible with the A1 labels.
