# Initial Rank-Position Coupling

This note combines:

- the quotient rank barriers;
- the order constraint
  \[
    \operatorname{Inv}_e\subseteq\operatorname{Inv}_r.
  \]

It gives an exact constraint on where a quotient rank can sit among the
ordered offsets.

## 1. Ordered offsets and ranks

Let the eight offsets in the clean strong gate be ordered as
\[
  c_1<c_2<\cdots<c_8.
\]

For each \(i\), let
\[
  q_i=\operatorname{rank}(e_{c_i})
\]
be the rank of the quotient \(e_{c_i}\) among the eight quotients, ordered
increasingly.

Let
\[
  s_i=\operatorname{rank}(r_{c_i})
\]
be the rank of the distance \(r_{c_i}\) among the eight distances, ordered
increasingly.

For
\[
  m\ge4881,
\]
the quotients are distinct.  The prime labels are also distinct, hence the
distances are distinct.  Thus both
\[
  (q_1,\dots,q_8)
\]
and
\[
  (s_1,\dots,s_8)
\]
are permutations of
\[
  \{1,\dots,8\}.
\]

The order-constraint lemma says:
\[
  i<j,\ q_i>q_j
  \quad\Longrightarrow\quad
  s_i>s_j.
\]

Equivalently,
\[
  \operatorname{Inv}(q)\subseteq\operatorname{Inv}(s).
\]

## 2. Lower bound for the distance rank

Fix an offset position \(i\), and suppose
\[
  q_i=k.
\]

Among the \(k-1\) quotient ranks smaller than \(k\), at most
\[
  i-1
\]
can occur before position \(i\).  Therefore at least
\[
  k-i
\]
of them occur after position \(i\), if \(k>i\).

For each later position \(j>i\) with
\[
  q_j<q_i,
\]
the pair \((i,j)\) is a quotient inversion.  Hence it must be a distance
inversion:
\[
  s_j<s_i.
\]

Thus at least
\[
  \max(0,k-i)
\]
distances are smaller than \(r_{c_i}\).  Therefore
\[
\boxed{
  s_i\ge 1+\max(0,k-i).
}
\]

Equivalently,
\[
\boxed{
  s_i\ge \max(1,k-i+1).
}
\]

## 3. Upper bound for the distance rank

Again fix \(i\) and \(q_i=k\).

Among the \(8-k\) quotient ranks larger than \(k\), at most
\[
  8-i
\]
can occur after position \(i\).  Therefore at least
\[
  i-k
\]
of them occur before position \(i\), if \(i>k\).

For each earlier position \(j<i\) with
\[
  q_j>q_i,
\]
the pair \((j,i)\) is a quotient inversion.  Hence
\[
  s_j>s_i.
\]

Thus at least
\[
  \max(0,i-k)
\]
distances are larger than \(r_{c_i}\).  Therefore
\[
\boxed{
  s_i\le 8-\max(0,i-k).
}
\]

Equivalently,
\[
\boxed{
  s_i\le \min(8,8+k-i).
}
\]

## 4. Rank-position band

Combining the two bounds gives:
\[
\boxed{
  \max(1,k-i+1)
  \le
  s_i
  \le
  \min(8,8+k-i).
}
\]

Thus, if offset position \(i\) carries quotient rank \(k\), its distance rank
cannot be arbitrary.

## 5. The last quotient rank

The strongest quotient-rank barrier is attached to
\[
  k=8.
\]

If the largest quotient occurs at offset position \(i\), then
\[
\boxed{
  s_i\ge9-i.
}
\]

So:
\[
\begin{array}{c|c}
  i & \text{forced lower bound on }s_i\\
  \hline
  1 & 8\\
  2 & 7\\
  3 & 6\\
  4 & 5\\
  5 & 4\\
  6 & 3\\
  7 & 2\\
  8 & 1
\end{array}
\]

At the same time, the quotient-rank barrier gives
\[
\boxed{
  r_{c_i}\ge B_8(A)
  =
  \left\lceil
  \frac{-8+\sqrt{32A-424}}{2}
  \right\rceil.
}
\]

Therefore, if the largest quotient sits early in the offset order, it must
also sit very late in the distance order and satisfy the strongest
square-root-rank barrier.

This is the precise form of the "impossible rank" lever: to rule out rank
\(8\) at a position \(i\), it is enough to prove that the corresponding
offset cannot have both
\[
  r_{c_i}\ge B_8(A)
\]
and
\[
  s_i\ge9-i.
\]

## 6. General quotient-rank obstruction

For a general quotient rank \(k\) at offset position \(i\), one has both:
\[
  r_{c_i}\ge B_k(A),
\]
and
\[
  \max(1,k-i+1)
  \le s_i
  \le
  \min(8,8+k-i).
\]

Thus every candidate placement
\[
  q_i=k
\]
has two independent exact requirements:

1. an analytic distance lower bound from quotient rank;
2. a combinatorial distance-rank band from the inversion constraint.

The remaining clean strong-gate target can now be phrased as a finite
rank-placement obstruction:

> no permutation \(q\) of the quotient ranks can be paired with a permutation
> \(s\) of the distance ranks satisfying
> \[
>   \operatorname{Inv}(q)\subseteq\operatorname{Inv}(s)
> \]
> and the individual barriers
> \[
>   r_{c_i}\ge B_{q_i}(A)
> \]
> together with the prime-label congruence restrictions.

This is still not a proof of Legendre.  It is the exact combinatorial form of
the next obstruction to attack.
