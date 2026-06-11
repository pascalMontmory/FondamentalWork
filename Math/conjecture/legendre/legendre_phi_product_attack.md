# Product Attack for Coprime A-Blocks

This note develops the product route suggested by the fixed-\(m\) large-sieve
target.

The aim is to replace pointwise residue covering by an arithmetic constraint
on
\[
  \Phi_m(q)=G_qU_q,
\]
where
\[
  G_q=9m^2+t_0(q)^2,
  \qquad
  U_q=9m^2+t_1(q)^2+1.
\]

On coprime complete A-blocks,
\[
  \gcd(G_q,U_q)=1.
\]
Thus a complete failure forces \(\Phi_m(q)\) to have at least two distinct
prime factors \(\le3m\), one from the Gaussian layer and one from the
unit-lift layer.

## 1. Two explicit orientations

Let
\[
  a=3q+1,\qquad b=3q+2.
\]

### Orientation I: \(a\equiv m\pmod2\)

Then
\[
  t_1=a,\qquad t_0=b.
\]
So
\[
  G_q=9m^2+b^2,
\]
\[
  U_q=9m^2+a^2+1.
\]
The product is
\[
  \Phi_m^{(I)}(q)
  =
  (9m^2+(3q+2)^2)(9m^2+(3q+1)^2+1).
\]

### Orientation II: \(a\not\equiv m\pmod2\)

Then
\[
  t_1=b,\qquad t_0=a.
\]
So
\[
  G_q=9m^2+a^2,
\]
\[
  U_q=9m^2+b^2+1.
\]
The product is
\[
  \Phi_m^{(II)}(q)
  =
  (9m^2+(3q+1)^2)(9m^2+(3q+2)^2+1).
\]

The two products differ only by the placement of the \(+1\).

## 2. Coprime-block gcd

From the A-block gcd formula,
\[
  \gcd(G_q,U_q)=\gcd(t_1(q),9m^2+1).
\]
Therefore on coprime blocks,
\[
  \gcd(G_q,U_q)=1.
\]

This means that any common small-prime explanation has already been removed.
Every complete failure must supply two genuinely independent certificates:
\[
  p_0\mid G_q,\qquad p_1\mid U_q,\qquad p_0\ne p_1.
\]

## 3. Exact size bounds

For every admissible complete block,
\[
  t_0(q)^2\le6m,
  \qquad
  t_1(q)^2+1\le6m.
\]
Hence
\[
  9m^2<G_q<(3m+1)^2,
\]
and
\[
  9m^2<U_q<(3m+1)^2.
\]

If \(G_q\) is composite, it has a prime divisor \(\le3m\).  If \(U_q\) is
composite, it has a prime divisor \(\le3m\).  Conversely, because of the same
size bounds, absence of such divisors forces primality.

Thus the product obstruction is exact:
\[
  q\in S_0(m)\cap S_1(m)
\]
if and only if
\[
  \Phi_m(q)
\]
has at least one Gaussian-eligible prime divisor of \(G_q\) and at least one
A1-eligible prime divisor of \(U_q\).

## 4. Difference invariant inside a block

The two factors have a very small difference.

In Orientation I:
\[
  G_q-U_q
  =
  (9m^2+b^2)-(9m^2+a^2+1)
  =
  b^2-a^2-1
  =
  2a.
\]

In Orientation II:
\[
  U_q-G_q
  =
  (9m^2+b^2+1)-(9m^2+a^2)
  =
  b^2-a^2+1
  =
  2b.
\]

Thus on a coprime block the two factors are coprime even though their
difference is a small linear term.  The exact identity is
\[
  |G_q-U_q|=2t_1(q).
\]

This is the key nonstandard structure:

> two coprime odd integers, both lying in the same short interval near
> \(9m^2\), differ by \(2t_1(q)\), and each is forced to have a small prime
> divisor from a different quadratic family.

## 5. Resultant viewpoint

For fixed \(m\), the two factors are quadratic polynomials in \(q\).  Let
\[
  G_m(q)=9m^2+t_0(q)^2,
  \qquad
  U_m(q)=9m^2+t_1(q)^2+1.
\]
Their resultant with respect to \(q\) is controlled by the same bridge
quantity.

Indeed, a prime \(p\ge5\) can divide both values for some \(q\) only if
\[
  p\mid9m^2+1.
\]
Equivalently, all common roots modulo \(p\) occur on the bridge locus.

After restricting to coprime blocks, the product family has no local common
root modulo any certificate prime.  The two divisibility conditions are
therefore genuinely transverse.

## 6. Failed simplification

One might hope that the product
\[
  \Phi_m(q)
\]
has a fixed divisor or a simple congruence obstruction forcing one factor to
be prime.

This is false as a general mechanism:

- the factors are coprime on coprime blocks, so no shared divisor can force a
  contradiction;
- each factor individually can have small prime divisors in its own quadratic
  family;
- the product congruence
  \[
    \Phi_m(q)\equiv0\pmod{p_0p_1}
  \]
  is exactly the pair-cover condition already isolated.

Thus the product route does not close by a simple fixed-divisor argument.

## 7. What remains usable

The product formulation is still useful because it exposes three simultaneous
constraints:

1. \(G_q\) and \(U_q\) are coprime.
2. Their difference is the small linear term \(2t_1(q)\).
3. Their small prime divisors must come from different quadratic families.

The next exact target is therefore not a fixed divisor of \(\Phi_m(q)\).  It
is a transversality lemma:

> For every \(m\), not every coprime complete block can have two transverse
> small-prime certificates \(p_0,p_1\le3m\) satisfying the Gaussian and A1
> local restrictions.

This is equivalent to the fixed-\(m\) double-sieve lemma, but expressed in a
form that may be more amenable to valuation, resultant, or determinant
methods.
