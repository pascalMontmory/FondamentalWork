# Residual 3-Adic Coset Closure

This note closes the final residual Mordell-Weil coset pair without using
`IntegralPoints`.

## Statement

Let
\[
  E:\quad y^2=x^3-128x^2-215865x
\]
and
\[
  P_0=2G_2+G_3+(0,0)
      =
      \left(\frac{10045}{9},-\frac{849520}{27}\right).
\]

There is no rational point
\[
  P\in \pm P_0+1320E(\mathbf Q)
\]
with
\[
  x(P)=1845s^2,\qquad s\in\mathbf Z.
\]

Consequently the two residual terminal fibers \(R4\) and \(R5\), which had
already been reduced to this opposite coset pair, are empty.

## Proof

Work over \(\mathbf Q_3\).  The curve has integral Weierstrass equation
\[
  y^2=x(x-533)(x+405).
\]

Its discriminant is
\[
  \Delta=16\,(533\cdot405\cdot938)^2,
\]
so
\[
  v_3(\Delta)=8.
\]
Also \(c_4\) is a \(3\)-adic unit, since
\[
  b_2=4(-128)=-512,\qquad c_4=b_2^2-24b_4
\]
and \(b_2\) is a unit at \(3\).  Thus the reduction at \(3\) is
multiplicative.

Modulo \(3\),
\[
  y^2=x^3-128x^2-215865x
      \equiv x^3+x^2=x^2(x+1).
\]
The singular point is \((0,0)\), and its tangent cone is
\[
  y^2-x^2=(y-x)(y+x),
\]
which splits over \(\mathbf F_3\).  Hence the reduction is split
multiplicative of type \(I_8\).

Let \(E_1(\mathbf Q_3)\) be the formal subgroup.  For split multiplicative
type \(I_8\),
\[
  E(\mathbf Q_3)/E_1(\mathbf Q_3)
\]
has exponent dividing
\[
  \operatorname{lcm}(8,\#\mathbf F_3^\times)=\operatorname{lcm}(8,2)=8.
\]
Since \(8\mid1320\), every rational point \(Q\in E(\mathbf Q)\) satisfies
\[
  1320Q\in E_1(\mathbf Q_3).
\]

Now
\[
  x(P_0)=\frac{10045}{9},\qquad
  y(P_0)=-\frac{849520}{27}.
\]
Thus
\[
  v_3(x(P_0))=-2,\qquad v_3(y(P_0))=-3.
\]
Equivalently, with the formal parameter \(t=-x/y\),
\[
  t(P_0)=\frac{6027}{169904}\in 3\mathbf Z_3.
\]
Therefore
\[
  P_0\in E_1(\mathbf Q_3),
  \qquad
  -P_0\in E_1(\mathbf Q_3).
\]

For any
\[
  P\in\pm P_0+1320E(\mathbf Q)
\]
we therefore have
\[
  P\in E_1(\mathbf Q_3).
\]

But every nonzero affine point in \(E_1(\mathbf Q_3)\) has negative
\(3\)-adic \(x\)-valuation.  Indeed, in the formal parameter \(t=-x/y\),
\[
  x=t^{-2}+O(t^{-1}),
\]
so \(t\in3\mathbf Z_3\setminus\{0\}\) gives
\[
  v_3(x)<0.
\]

On the other hand, if \(s\in\mathbf Z\), then
\[
  x=1845s^2
\]
has
\[
  v_3(x)\ge2
\]
when \(s\ne0\), while \(s=0\) gives \(x=0\), a finite point not reducing to
the identity and hence not lying in \(E_1(\mathbf Q_3)\).

Thus no point in the residual cosets can satisfy \(x(P)=1845s^2\).  This
proves the claim.

## Consequence

The finite Mordell-Weil sieve had reduced both residual terminal systems to
\[
  P\in\pm P_0+1320E(\mathbf Q).
\]
The \(3\)-adic argument above shows this whole pair of cosets is disjoint
from the quartic image \(x=1845s^2\) with \(s\in\mathbf Z\).  Therefore the
residual \(R4\) and \(R5\) fibers are closed before the separated square
filters are even needed.
