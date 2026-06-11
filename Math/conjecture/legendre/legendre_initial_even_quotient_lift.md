# Initial Even Quotient Lift

This note extracts the \(2\)-adic consequence hidden in the centered
factorization.  It strengthens the quotient-rank barrier in the clean strong
gate.

## 1. All initial values are odd

Recall
\[
  A=3m.
\]

If \(m\) is even, then \(A\) is even and the initial offset set is
\[
  \mathcal C_{\rm even}
  =
  \{1,5,17,25,49,65,101,121\},
\]
so every offset is odd.  Hence every value
\[
  A^2+c
\]
is odd.

If \(m\) is odd, then \(A\) is odd and the initial offset set is
\[
  \mathcal C_{\rm odd}
  =
  \{2,4,16,26,50,64,100,122\},
\]
so every offset is even.  Again every value
\[
  A^2+c
\]
is odd.

Thus, in both parity cases,
\[
\boxed{
  A^2+c\equiv1\pmod2
}
\]
for all eight initial offsets.

## 2. The centered quotient is even

The centered factorization is
\[
  A^2+c=(A-r)(A+r+e),
\]
where
\[
  A-r
\]
is a prime label.

Since \(A^2+c\) is odd, both factors are odd.  Therefore
\[
  A-r\equiv1\pmod2,
\]
and
\[
  A+r+e\equiv1\pmod2.
\]

Subtracting gives
\[
  (A+r+e)-(A-r)=2r+e.
\]
The left side is even, so
\[
\boxed{
  e\equiv0\pmod2.
}
\]

Thus every quotient in the initial clean strong-gate cluster is even.

Equivalently, writing
\[
  e=2f,
\]
the Pell pencil becomes
\[
  w=2(r+f)
\]
and
\[
\boxed{
  (r+f)^2=f^2+2Af-c=f^2+6mf-c.
}
\]

The quotient-local congruence can therefore be divided by the forced
\(2\)-adic factor:
\[
\boxed{
  (r+f)^2\equiv f^2-c\pmod{6f}.
}
\]

This is the reduced quotient pencil.

## 3. Even quotient rank barrier

For
\[
  m\ge4881,
\]
the eight quotients are already known to be distinct.  Since they are also
positive even integers, their increasing order satisfies
\[
\boxed{
  e_{(k)}\ge2k
  \qquad(1\le k\le8).
}
\]

The previous quotient-rank barrier used only
\[
  e_{(k)}\ge k.
\]
The clean strong gate therefore has a doubled quotient-rank barrier.

For an offset \(c\le122\) with quotient rank \(k\), the equation
\[
  e=\frac{r^2+c}{A-r}
\]
and
\[
  e\ge2k
\]
give
\[
  r^2+c\ge2k(A-r).
\]

Since
\[
  c\le122,
\]
this implies
\[
  r^2+2kr\ge2kA-122.
\]

Define
\[
\boxed{
  \widetilde B_k(A):=
  \left\lceil
    \frac{-2k+\sqrt{4k^2+4(2kA-122)}}{2}
  \right\rceil.
}
\]

Equivalently,
\[
\boxed{
  \widetilde B_k(A)=
  \left\lceil
    -k+\sqrt{k^2+2kA-122}
  \right\rceil.
}
\]

Then every offset carrying quotient rank \(k\) satisfies
\[
\boxed{
  r\ge\widetilde B_k(A).
}
\]

In particular, the largest quotient rank gives
\[
\boxed{
  r\ge
  \widetilde B_8(A)
  =
  \left\lceil
    -8+\sqrt{16A-58}
  \right\rceil.
}
\]

This is asymptotic to
\[
  4\sqrt A,
\]
where the previous largest-rank barrier was asymptotic to
\[
  \sqrt{8A}.
\]

## 4. Strengthened label order statistic

Let the eight distances be sorted increasingly:
\[
  R_1<R_2<\cdots<R_8.
\]

The multiset of quotient ranks forces the multiset of lower bounds
\[
  \{\widetilde B_1(A),\dots,\widetilde B_8(A)\}.
\]

Therefore
\[
\boxed{
  R_j\ge\widetilde B_j(A)
  \qquad(1\le j\le8).
}
\]

Equivalently, if the prime labels are sorted increasingly,
\[
  P_1<P_2<\cdots<P_8,
\]
then
\[
\boxed{
  P_j\le A-\widetilde B_{9-j}(A)
  \qquad(1\le j\le8).
}
\]

Thus the first label must satisfy
\[
\boxed{
  P_1\le
  A-\left\lceil -8+\sqrt{16A-58}\right\rceil.
}
\]

So a clean strong-gate counterexample needs at least one admissible label
roughly below
\[
  A-4\sqrt A.
\]

## 5. Consequence for the two-layer ladder

The two-layer ladder certificate can now replace every occurrence of
\[
  B_k(A)
\]
coming from quotient ranks by
\[
  \widetilde B_k(A).
\]

For a layer word \(L\), the word-dependent lower envelope becomes
\[
\boxed{
  \widetilde H_i^L(A):=
  \max_{i\le j\le8}
  \left(\widetilde B_{9-j}(A)+W_L(i,j)\right).
}
\]

Every clean strong-gate certificate with \(m\ge4881\) satisfies
\[
\boxed{
  D_i\ge\widetilde H_i^L(A)
  \qquad(1\le i\le8).
}
\]

The remaining closure target is correspondingly sharper:

> eliminate two-layer ladder certificates using the doubled quotient ranks
> \(e_{(k)}\ge2k\), not the weaker ranks \(e_{(k)}\ge k\).

This is a purely exact \(2\)-adic gain.  It does not depend on computation
over centers \(m\).
