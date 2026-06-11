# Initial Label Order-Statistic Barrier

This note extracts the global order-statistic consequence of the quotient
rank barriers.

The previous rank barrier says that the distance attached to quotient rank
\(k\) satisfies
\[
  r_{(k)}\ge B_k(A).
\]
Since the quotient ranks are exactly \(1,\dots,8\), the eight distance values,
after sorting, must dominate the same barrier sequence.

This gives a clean statement about the sorted prime labels.

## 1. Sorted distances

In the clean strong gate with
\[
  m\ge4881,
\]
let the eight center distances be sorted increasingly:
\[
  R_1<R_2<\cdots<R_8.
\]

The quotient-rank barriers give a lower bound multiset
\[
  \{B_1(A),B_2(A),\dots,B_8(A)\},
\]
where
\[
  B_k(A)=
  \left\lceil
  \frac{-k+\sqrt{k^2+4(kA-122)}}{2}
  \right\rceil.
\]

The sequence \(B_k(A)\) is increasing in \(k\).

For each \(j\), at most \(j-1\) of the eight distances can be below
\[
  B_j(A),
\]
because only the quotient ranks
\[
  1,\dots,j-1
\]
have barriers below \(B_j(A)\).

Therefore:
\[
\boxed{
  R_j\ge B_j(A)
  \qquad(1\le j\le8).
}
\]

This is an order-statistic version of the quotient-rank barrier.  It does
not depend on knowing which offset carries which quotient rank.

## 2. Sorted prime labels

The prime label corresponding to a distance \(r\) is
\[
  p=A-r.
\]

Thus sorting distances increasingly sorts labels decreasingly.

Let the eight prime labels be sorted increasingly:
\[
  P_1<P_2<\cdots<P_8.
\]

Then
\[
  P_j=A-R_{9-j}.
\]

Using the distance order-statistic bound gives:
\[
\boxed{
  P_j\le A-B_{9-j}(A)
  \qquad(1\le j\le8).
}
\]

In particular:
\[
\boxed{
  P_1\le A-B_8(A)
}
\]
and
\[
\boxed{
  P_2\le A-B_7(A).
}
\]

So it is not merely true that one label is forced down to the
\(\sqrt{8A}\)-scale.  The whole lower tail of the label set is forced:
\[
\boxed{
  P_j\le
  A-
  \left\lceil
  \frac{-(9-j)+\sqrt{(9-j)^2+4((9-j)A-122)}}{2}
  \right\rceil.
}
\]

## 3. Counting form

Equivalently, for every
\[
  1\le k\le8,
\]
at least
\[
  9-k
\]
prime labels satisfy
\[
\boxed{
  p\le A-B_k(A).
}
\]

Thus:
\[
\begin{array}{c|c}
  \text{threshold} & \text{number of labels forced below it}\\
  \hline
  A-B_1(A) & 8\\
  A-B_2(A) & 7\\
  A-B_3(A) & 6\\
  A-B_4(A) & 5\\
  A-B_5(A) & 4\\
  A-B_6(A) & 3\\
  A-B_7(A) & 2\\
  A-B_8(A) & 1
\end{array}
\]

The last line is the previously noted strongest single-label drop:
\[
  A-B_8(A)
  =
  A-
  \left\lceil
  \frac{-8+\sqrt{32A-424}}{2}
  \right\rceil.
\]

## 4. Clean strong-gate consequence

A clean strong-gate counterexample with
\[
  m\ge4881
\]
must therefore contain eight distinct admissible prime labels whose sorted
values satisfy the full chain
\[
  P_1\le A-B_8(A),
\]
\[
  P_2\le A-B_7(A),
\]
\[
  \cdots
\]
\[
  P_8\le A-B_1(A).
\]

This is a stronger distributional statement than the existence of one low
label.  It says that the label set must have a prescribed lower tail.

The next exact target is to combine this lower-tail requirement with the
layer restrictions, especially:

- four A0 labels must satisfy \(p\equiv1\pmod4\);
- all eight labels must satisfy their offset-specific congruences;
- the rank-position coupling restricts which offset can carry each deep
  label.
