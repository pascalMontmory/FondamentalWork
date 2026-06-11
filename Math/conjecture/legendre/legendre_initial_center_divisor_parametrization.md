# Initial Center-Divisor Parametrization

This note rewrites the factor-gap system in a more rigid form.

The centered equation
\[
  A^2+c=(A-r)(A+r+e)
\]
can be reduced to a divisor condition involving only the distance \(r\) from
the center:
\[
  A-r\mid r^2+c.
\]

This is an exact equivalence.  It turns each initial composite candidate into
a divisor of a much smaller shifted square.

## 1. Divisor form of a composite between squares

Let
\[
  A=3m,
\]
and let
\[
  N=A^2+c,\qquad 0<c\le2A.
\]
Then
\[
  A^2<N<(A+1)^2.
\]

Suppose \(N\) has a proper divisor
\[
  2\le d\le A.
\]
Write
\[
  d=A-r,
  \qquad
  1\le r\le A-2.
\]
Then, modulo \(d\),
\[
  A\equiv r.
\]
Therefore
\[
  d\mid A^2+c
  \quad\Longleftrightarrow\quad
  d\mid r^2+c.
\]

Thus:
\[
\boxed{
  A-r\mid A^2+c
  \quad\Longleftrightarrow\quad
  A-r\mid r^2+c.
}
\]

If \(d=A-r\) is a proper divisor with \(2\le d\le A\), then \(A^2+c\) is
composite.  Conversely, if \(A^2+c\) is composite, it has a prime divisor
\[
  p\le A,
\]
and with
\[
  r=A-p
\]
one gets
\[
  p=A-r\mid r^2+c.
\]

For the Legendre A-channel candidates, the values are odd and not divisible
by \(3\), so any prime certificate satisfies
\[
  p\ge5,
\]
or equivalently
\[
  1\le r\le A-5.
\]

## 2. Relation with the factor-gap equation

The factor-gap equation was
\[
  c=Ae-r(r+e).
\]
Since
\[
  p=A-r,
\]
this becomes
\[
  c=ep-r^2,
\]
or
\[
  r^2+c=ep.
\]
Therefore
\[
\boxed{
  e=\frac{r^2+c}{A-r}.
}
\]

The cofactor is
\[
  q=A+r+e.
\]
So a prime-label factorization is equivalently:
\[
\boxed{
  p=A-r\text{ prime},\qquad p\mid r^2+c,\qquad
  e=\frac{r^2+c}{p}.
}
\]

This removes the extra variable \(e\).  The factor gap is determined by
\[
  A,\ c,\ r.
\]

## 3. Clean strong-gate certificate in divisor form

In the clean strong gate, the offset set is
\[
  \mathcal C_{\rm even}
  =\{1,5,17,25,49,65,101,121\}
\]
if \(m\) is even, and
\[
  \mathcal C_{\rm odd}
  =\{2,4,16,26,50,64,100,122\}
\]
if \(m\) is odd.

A clean strong-gate counterexample gives, for every
\[
  c\in\mathcal C_{\rm parity(m)},
\]
an integer \(r_c\) and a prime
\[
  p_c=A-r_c
\]
such that
\[
\boxed{
  p_c\mid r_c^2+c.
}
\]

The eight primes
\[
  p_c
\]
are distinct, because the eight initial candidates are pairwise coprime.

The bounds are:
\[
  1\le r_c\le A-5,
  \qquad
  p_c=A-r_c\le A.
\]

The layer restrictions remain:

- if \(c\) comes from an A0 coordinate, then
  \[
    p_c\equiv1\pmod4,
    \qquad
    p_c\nmid A;
  \]
- if \(c\) comes from an A1 coordinate, then \(p_c\) is an odd prime
  admissible for that A1 value, and coprime-block conditions exclude the
  hidden common-divisor case.

## 4. Difference between two offsets

Let two offsets \(c,d\) have prime labels
\[
  p_c=A-r_c,\qquad p_d=A-r_d.
\]
The divisor conditions are:
\[
  A-r_c\mid r_c^2+c,
\]
\[
  A-r_d\mid r_d^2+d.
\]

If two offsets used the same label prime, then
\[
  A-r_c=A-r_d,
\]
so
\[
  r_c=r_d.
\]
The common prime would divide both
\[
  r_c^2+c
  \quad\text{and}\quad
  r_c^2+d,
\]
and hence would divide
\[
  c-d.
\]

This recovers the same-layer and cross-layer collision philosophy in the
center-divisor language: repeated labels force divisibility of fixed
differences of offsets.

In the clean strong gate, those repeated labels have already been excluded.
Therefore the eight distances \(r_c\) give eight distinct primes
\[
  A-r_c.
\]

## 5. Closure target

The clean strong-gate obstruction can now be stated without cofactors:

> For \(A=3m\) in the clean strong gate, it is impossible to assign to every
> \(c\in\mathcal C_{\rm parity(m)}\) a distance
> \[
>   1\le r_c\le A-5
> \]
> such that
> \[
>   A-r_c\text{ is a distinct admissible prime}
> \]
> and
> \[
>   A-r_c\mid r_c^2+c.
> \]

This is still not a proof of Legendre.  It is a smaller exact Diophantine
target than the factor-gap system: eight divisors of eight shifted squares,
all tied to the same center \(A\).
