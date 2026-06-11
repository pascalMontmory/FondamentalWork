# Initial Factor-Gap System

This note converts the clean strong-gate cluster into exact factor-gap
equations.

The point is to remove the vague phrase "has a small prime divisor".  Since
all initial candidates lie strictly between two consecutive squares, every
composite candidate has a factorization that crosses the center \(3m\).  That
crossing factorization has an exact quadratic discriminant form.

## 1. Centered factorization between consecutive squares

Set
\[
  A=3m.
\]

Let
\[
  N=A^2+c
\]
with
\[
  0<c\le 2A.
\]
Then
\[
  A^2<N<(A+1)^2.
\]

If \(N\) is composite, then it has a factorization
\[
  N=pq
\]
with
\[
  p\le A<q.
\]
Choose \(p\) to be a prime divisor of \(N\) with \(p\le A\); then \(q=N/p\)
is the corresponding cofactor.

For the Legendre A-channel candidates considered here, \(N\) is odd and not
divisible by \(3\), so
\[
  p\ge5,\qquad q\ge5.
\]

Write
\[
  p=A-r,\qquad q=A+s,
\]
where
\[
  r\ge1,\qquad s\ge1.
\]
Then
\[
  A^2+c=(A-r)(A+s)
       =A^2+A(s-r)-rs.
\]
Hence
\[
  c=A(s-r)-rs.
\]
Since \(c>0\), necessarily
\[
  s>r.
\]
Put
\[
  e=s-r\ge1.
\]
Then the exact factor-gap equation is
\[
\boxed{
  c=Ae-r(r+e).
}
\]

Equivalently,
\[
  r^2+er+c-Ae=0.
\]
Therefore the discriminant must be a square:
\[
\boxed{
  w^2=e^2+4Ae-4c,
  \qquad
  w\equiv e\pmod2,
}
\]
with
\[
  r=\frac{w-e}{2},
  \qquad
  p=A-r,
  \qquad
  q=A+r+e.
\]

Thus a composite value \(A^2+c\) in the Legendre interval is equivalent to a
solution of this centered square-discriminant equation with
\[
  1\le r\le A-5,
  \qquad
  e\ge1.
\]

## 2. The two clean-gate offset sets

The first-four-block cluster has different offsets according to the parity
of \(m\).

### Even \(m\)

If \(m\) is even, the A0 coordinates are
\[
  1,5,7,11,
\]
and the A1 coordinates are
\[
  2,4,8,10.
\]
Therefore the eight offsets are
\[
\mathcal C_{\rm even}
=
\{1,25,49,121\}
\cup
\{5,17,65,101\}.
\]
Equivalently,
\[
\boxed{
  \mathcal C_{\rm even}
  =\{1,5,17,25,49,65,101,121\}.
}
\]

### Odd \(m\)

If \(m\) is odd, the A0 coordinates are
\[
  2,4,8,10,
\]
and the A1 coordinates are
\[
  1,5,7,11.
\]
Therefore the eight offsets are
\[
\mathcal C_{\rm odd}
=
\{4,16,64,100\}
\cup
\{2,26,50,122\}.
\]
Equivalently,
\[
\boxed{
  \mathcal C_{\rm odd}
  =\{2,4,16,26,50,64,100,122\}.
}
\]

For \(m\ge21\), every \(c\) in both sets satisfies
\[
  0<c\le122\le6m=2A,
\]
so all eight values lie in the interval
\[
  A^2<N<(A+1)^2.
\]

## 3. Necessary system for a clean strong-gate counterexample

Assume \(m\) lies in the clean strong gate:

1. \(m\ge21\);
2. \(m\not\equiv\pm1\pmod5\);
3. \(m\) is in a no-same-layer-repetition class modulo \(70\);
4. \(m\) avoids the listed cross-layer collision congruences.

If the A-channel fails on the first four blocks, then every
\[
  A^2+c,\qquad c\in\mathcal C_{\rm parity(m)},
\]
is composite.

By the pairwise-coprime cluster lemma, these eight integers are pairwise
coprime.  Thus a counterexample gives, for each
\[
  c\in\mathcal C_{\rm parity(m)},
\]
a distinct factorization
\[
  A^2+c=(A-r_c)(A+r_c+e_c),
\]
where
\[
  e_c\ge1,\qquad 1\le r_c\le A-5.
\]
Equivalently, for every \(c\) in the corresponding offset set,
\[
\boxed{
  c=Ae_c-r_c(r_c+e_c).
}
\]
Or in square-discriminant form:
\[
\boxed{
  w_c^2=e_c^2+4Ae_c-4c,
  \qquad
  w_c\equiv e_c\pmod2.
}
\]

The associated small prime labels are
\[
  p_c=A-r_c.
\]
They are distinct, and they satisfy the layer restrictions:

- for A0 offsets, \(p_c\equiv1\pmod4\) and \(p_c\nmid A\);
- for A1 offsets, \(p_c\nmid t_1^2\) and \(p_c\nmid 9m^2+1\) on coprime
  blocks.

## 4. Closure target

The clean strong-gate obstruction is now an exact Diophantine system:

> For a fixed \(A=3m\), the eight offsets in
> \(\mathcal C_{\rm parity(m)}\) cannot all admit centered factorizations
> \[
>   A^2+c=(A-r_c)(A+r_c+e_c)
> \]
> satisfying the layer restrictions and distinctness of the primes
> \(A-r_c\).

This is not yet a proof of Legendre.  It is a sharper proof target: the
remaining strong-gate counterexample must solve eight simultaneous
factor-gap equations with the same center \(A\), while respecting the
previous congruence gates.
