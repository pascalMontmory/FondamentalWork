# Cofactor-Augmented Mobius Gate

The root-count formula for \(Z(m)\) exposes a limitation: a pure divisor
Mobius expansion sees only the residue facts
\[
  p_0\mid G_q,\qquad p_1\mid U_q.
\]
That is not yet enough to break the sieve parity barrier.

This note adds the missing exact information: if both values are composite,
then their small prime divisors come with large cofactors that must satisfy a
very short bilinear difference equation.

## 1. Setup

Let
\[
  A=9m^2.
\]
On a complete coprime A-block,
\[
  G_q=A+t_0(q)^2,\qquad
  U_q=A+t_1(q)^2+1,
\]
and
\[
  \gcd(G_q,U_q)=1.
\]

The two values have a small signed difference:
\[
  U_q-G_q=\eta_q\,2t_1(q),
\]
where
\[
  \eta_q=
  \begin{cases}
  +1,&q\equiv m\pmod2,\\
  -1,&q\not\equiv m\pmod2.
  \end{cases}
\]

Indeed, if \(q\equiv m\pmod2\), then \(t_0=3q+1\) and \(t_1=3q+2\), so
\[
  U_q-G_q=(3q+2)^2+1-(3q+1)^2=2(3q+2).
\]
If \(q\not\equiv m\pmod2\), then \(t_0=3q+2\) and \(t_1=3q+1\), so
\[
  U_q-G_q=(3q+1)^2+1-(3q+2)^2=-2(3q+1).
\]

## 2. Cofactor equation

Assume the A-channel fails on a coprime block \(q\).  Then there are
eligible distinct primes
\[
  p_0,p_1\le3m
\]
and cofactors
\[
  X_0,X_1>3m
\]
such that
\[
  G_q=p_0X_0,\qquad U_q=p_1X_1.
\]
Therefore
\[
  \boxed{
  p_1X_1-p_0X_0=\eta_q\,2t_1(q).
  }
\]

This equation is exact.  It is stronger than the two congruences
\[
  p_0\mid G_q,\qquad p_1\mid U_q,
\]
because it remembers that the two divisible values are adjacent on the
scale \(O(\sqrt m)\) while both factors are on the scale \(m\) or larger.

The cofactor ranges are also exact:
\[
  3m<X_i<\frac{(3m+1)^2}{p_i}\qquad(i=0,1).
\]

## 3. Reduced bilinear form

Write
\[
  X_i=3m+s_i,\qquad s_i\ge1.
\]
Then the cofactor equation becomes
\[
  3m(p_1-p_0)+p_1s_1-p_0s_0=\eta_q\,2t_1(q).
\]

Since
\[
  0<2t_1(q)\le2\sqrt{6m},
\]
the large term \(3m(p_1-p_0)\) must be almost cancelled by
\[
  p_0s_0-p_1s_1.
\]
Thus every failed coprime block produces a short bilinear approximation:
\[
  \boxed{
  \left|
  3m(p_1-p_0)+p_1s_1-p_0s_0
  \right|
  \le2\sqrt{6m}.
  }
\]

This is not visible in the residue-cover formulation.

## 4. Elimination of \(q\)

The identities
\[
  p_0X_0=A+t_0(q)^2,
  \qquad
  p_1X_1=A+t_1(q)^2+1
\]
allow \(q\) to be eliminated from the cofactor equation.

In the positive branch \(q\equiv m\pmod2\),
\[
  t_0=3q+1,\qquad t_1=3q+2.
\]
Thus
\[
  t_1=t_0+1,
\]
and the two factorization equations imply
\[
  p_1X_1-p_0X_0=2t_0+2.
\]
Equivalently,
\[
  t_0=\frac{p_1X_1-p_0X_0-2}{2}.
\]
Substitution into \(p_0X_0=A+t_0^2\) gives the single quartic bilinear
constraint
\[
  \boxed{
  (p_1X_1-p_0X_0-2)^2
  =
  4(p_0X_0-A).
  }
\]

In the negative branch \(q\not\equiv m\pmod2\),
\[
  t_0=3q+2,\qquad t_1=3q+1,
\]
and
\[
  U_q-G_q=-2t_1.
\]
Therefore
\[
  t_1=\frac{p_0X_0-p_1X_1}{2},
\]
and substitution into \(p_1X_1=A+t_1^2+1\) gives
\[
  \boxed{
  (p_0X_0-p_1X_1)^2
  =
  4(p_1X_1-A-1).
  }
\]

So a failed block is not merely a pair of residue hits.  It is an integral
point on one of two explicit quartic bilinear surfaces with the inequalities
\[
  p_i\le3m<X_i.
\]

## 5. New positivity strategy

The Mobius root-count formula proves that a purely local divisor expansion
needs a parity-breaking ingredient.  The cofactor equation supplies one.

The next certificate should not weight only
\[
  {\bf 1}_{p_0\mid G_q}{\bf 1}_{p_1\mid U_q}.
\]
It should weight the full integral solutions of
\[
  p_1X_1-p_0X_0=\eta_q\,2t_1(q),
\]
or equivalently the quartic bilinear equations above.

A proof of the current Legendre route would follow from:

> **Cofactor non-cover lemma.**  For every \(m\ge1\), the complete coprime
> block interval contains a \(q\) for which no eligible
> \((p_0,p_1,X_0,X_1)\) satisfies the cofactor equation and the two
> factorization identities.

This lemma is equivalent to \(Z(m)>0\), but it is structurally stronger than
the residue statement.  It is the first form of the global gate that exposes
the small-difference rigidity needed to beat parity.

## 6. Two-block cofactor descent

Suppose the same ordered pair \((p_0,p_1)\) covers two coprime complete
blocks \(q\ne r\), and suppose first that they lie in the same parity branch:
\[
  q\equiv r\pmod2.
\]
Then
\[
  \eta_q=\eta_r=:\eta,
\]
and
\[
  t_1(q)-t_1(r)=3(q-r).
\]

Writing
\[
  G_q=p_0X_0(q),\quad U_q=p_1X_1(q),
\]
and similarly for \(r\), subtracting the two cofactor equations gives
\[
  \boxed{
  p_1\bigl(X_1(q)-X_1(r)\bigr)
  -
  p_0\bigl(X_0(q)-X_0(r)\bigr)
  =
  6\eta(q-r).
  }
\]

The individual cofactor differences are not arbitrary.  In the positive
branch \(q\equiv m\pmod2\),
\[
  t_0(s)=3s+1,\qquad t_1(s)=3s+2,
\]
so
\[
  X_0(q)-X_0(r)
  =
  \frac{3(q-r)(3(q+r)+2)}{p_0},
\]
and
\[
  X_1(q)-X_1(r)
  =
  \frac{3(q-r)(3(q+r)+4)}{p_1}.
\]
Substitution gives the identity
\[
  3(q-r)(3(q+r)+4)
  -
  3(q-r)(3(q+r)+2)
  =
  6(q-r),
\]
but the point is divisibility:
\[
  p_0\mid3(q-r)(3(q+r)+2),
\]
\[
  p_1\mid3(q-r)(3(q+r)+4).
\]

In the negative branch \(q\not\equiv m\pmod2\),
\[
  t_0(s)=3s+2,\qquad t_1(s)=3s+1,
\]
and therefore
\[
  p_0\mid3(q-r)(3(q+r)+4),
\]
\[
  p_1\mid3(q-r)(3(q+r)+2).
\]

Thus same-branch repetition is forced onto the divisor hyperplanes
\[
  q-r,\qquad 3(q+r)+2,\qquad 3(q+r)+4.
\]

For opposite parity branches, \(q\not\equiv r\pmod2\), the signs satisfy
\[
  \eta_q=-\eta_r.
\]
The subtracted cofactor equation becomes a sum condition:
\[
  p_1\bigl(X_1(q)-X_1(r)\bigr)
  -
  p_0\bigl(X_0(q)-X_0(r)\bigr)
  =
  2\eta_q\bigl(t_1(q)+t_1(r)\bigr).
\]
Since in opposite branches the two \(t_1\)-coordinates are \(3s+1\) and
\(3s+2\), this right side is
\[
  \pm2(3(q+r)+3)=\pm6(q+r+1).
\]
Consequently opposite-branch repetition is forced onto the divisor
hyperplanes
\[
  3(q-r)\pm1,\qquad q+r+1.
\]

This recovers the earlier collision hyperplanes, but now with cofactor
differences attached.  The strengthened descent target is:

> a repeated ordered pair must not only lie on a collision hyperplane; its
> two large cofactor differences must solve the short linear equation above.

That is the extra structure unavailable to a pure residue cover.
