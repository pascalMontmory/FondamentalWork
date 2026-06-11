# Initial Order Constraints

This note extracts an order obstruction from the quotient form
\[
  A=r+\frac{r^2+c}{e}.
\]

Equivalently,
\[
  e=\frac{r^2+c}{A-r}.
\]

For fixed center \(A\), the quotient is strictly increasing in both the
offset \(c\) and the center-distance \(r\).  Therefore the eight quotients in
the clean strong gate cannot be assigned in an arbitrary order.

## 1. Monotonicity in the distance

Fix
\[
  A,
\]
and an offset
\[
  c>0.
\]
Define
\[
  F_c(r)=\frac{r^2+c}{A-r},
\]
for
\[
  1\le r<A.
\]

If
\[
  1\le r<s<A,
\]
then
\[
  F_c(s)-F_c(r)
  =
  \frac{(s-r)\bigl(A(r+s)-rs+c\bigr)}
       {(A-r)(A-s)}.
\]

The denominator is positive.  The numerator is positive because
\[
  s-r>0
\]
and
\[
  A(r+s)-rs+c>0.
\]

Therefore
\[
\boxed{
  r<s
  \quad\Longrightarrow\quad
  F_c(r)<F_c(s).
}
\]

So, for a fixed offset, larger center-distance means larger quotient.

## 2. Monotonicity in the offset

For fixed
\[
  A
\]
and fixed
\[
  r<A,
\]
if
\[
  c<d,
\]
then
\[
  F_d(r)-F_c(r)=\frac{d-c}{A-r}>0.
\]

Thus
\[
\boxed{
  c<d
  \quad\Longrightarrow\quad
  F_c(r)<F_d(r)
}
\]
for the same distance \(r\).

## 3. Product-order constraint

Let two distinct offsets
\[
  c<d
\]
share the same center \(A\), with distances
\[
  r_c,\qquad r_d,
\]
and quotients
\[
  e_c=F_c(r_c),
  \qquad
  e_d=F_d(r_d).
\]

If
\[
  r_c\le r_d,
\]
then monotonicity gives
\[
  F_c(r_c)\le F_c(r_d)<F_d(r_d).
\]
Therefore
\[
\boxed{
  c<d,\ r_c\le r_d
  \quad\Longrightarrow\quad
  e_c<e_d.
}
\]

Equivalently:
\[
\boxed{
  c<d,\ e_c>e_d
  \quad\Longrightarrow\quad
  r_c>r_d.
}
\]

Since
\[
  p_c=A-r_c,
  \qquad
  p_d=A-r_d,
\]
this also gives
\[
\boxed{
  c<d,\ e_c>e_d
  \quad\Longrightarrow\quad
  p_c<p_d.
}
\]

Thus every quotient inversion relative to the offset order must be mirrored
by a distance inversion and by the opposite prime-label order.

## 4. Clean strong-gate permutation constraint

In the clean strong gate with
\[
  m\ge4881,
\]
the pair-quotient compatibility lemma shows that the eight quotients
\[
  e_c,\qquad c\in\mathcal C_{\rm parity(m)},
\]
are pairwise distinct.

Hence the quotients define a permutation of the eight offsets.

The product-order constraint says this permutation is not arbitrary:

> if \(c<d\) but \(e_c>e_d\), then necessarily
> \[
>   r_c>r_d
> \]
> and
> \[
>   p_c<p_d.
> \]

Equivalently, every inversion of the quotient order must be paid for by an
inversion of the distance order.

Let
\[
  \operatorname{Inv}_e
  =
  \{(c,d):c<d,\ e_c>e_d\},
\]
and
\[
  \operatorname{Inv}_r
  =
  \{(c,d):c<d,\ r_c>r_d\}.
\]
Then
\[
\boxed{
  \operatorname{Inv}_e\subseteq\operatorname{Inv}_r.
}
\]

Since prime order is opposite distance order,
\[
  r_c>r_d
  \quad\Longleftrightarrow\quad
  p_c<p_d,
\]
one also has
\[
\boxed{
  \operatorname{Inv}_e
  \subseteq
  \{(c,d):c<d,\ p_c<p_d\}.
}
\]

## 5. Closure target

The clean strong-gate counterexample for
\[
  m\ge4881
\]
must now satisfy all of the following:

1. eight distinct admissible prime labels \(p_c\);
2. eight distinct quotients \(e_c\);
3. pairwise quadratic compatibility for every pair of offsets;
4. the order constraint
   \[
     \operatorname{Inv}_e\subseteq\operatorname{Inv}_r.
   \]

This does not close the clean strong gate.  It gives the next exact route:
prove that the pairwise quadratic compatibility forces a quotient inversion
that is not matched by a distance inversion, or conversely that the required
distance inversions contradict the prime-label congruence restrictions.
