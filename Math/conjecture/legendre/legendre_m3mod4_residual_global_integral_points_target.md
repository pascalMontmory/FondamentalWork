# Residual Global Integral-Points Target

This note records the exact final obstruction left in the hard
\(m\equiv3\pmod4\) Legendre branch.

## Certified Reduction

The remaining residual prefix-\(8\) systems have been reduced to the elliptic
curve
\[
  E:\quad Y^2=X^3-128X^2-215865X.
\]

The certified Mordell-Weil data are
\[
  E(\mathbf Q)_{\rm tors}\simeq(\mathbf Z/2\mathbf Z)^2,\qquad
  {\rm rank}\,E(\mathbf Q)=3,
\]
with basis
\[
  G_1=(-363,3696),\qquad
  G_2=(-195,5460),\qquad
  G_3=(-117,4680).
\]

The finite Mordell-Weil sieve has already proved that both terminal residual
systems \(R4\) and \(R5\) can survive only in the opposite pair of cosets
\[
  P\in\pm P_0+1320E(\mathbf Q),
\]
where
\[
  P_0=2G_2+G_3+(0,0)
      =
      \left(\frac{10045}{9},-\frac{849520}{27}\right).
\]

Thus the residual problem is not a global search over \(n\), \(m\), or \(s\).
It is the following integral-points statement.

## Target Theorem

There is no point
\[
  P\in\pm P_0+1320E(\mathbf Q)
\]
such that
\[
  x(P)=1845s^2,\qquad s\in\mathbf Z,
\]
and such that the common square constraints
\[
\begin{aligned}
  &(153s^2-55)/2,\quad (41s^2+9)/2,\quad (45s^2-13)/2,\\
  &2673s^2-992,\quad 4617s^2-392
\end{aligned}
\]
are all integer squares together with either terminal pair
\[
  R4:\quad 1701s^2-908,\quad 7533s^2+2668
\]
or
\[
  R5:\quad 3645s^2-836,\quad 1701s^2-1004.
\]

Equivalently, after the already-certified Mordell-Weil sieve, the exact
closure condition is
\[
  R4_{\rm coset}=R5_{\rm coset}=\varnothing.
\]

## Boundary Check

The visible integral point
\[
  P=(1845,73800)=G_3+(0,0)
\]
comes from \(s=1\), but it is not in the residual terminal pair:
\[
  1701-908=793
\]
is not a square for \(R4\), and
\[
  1701-1004=697
\]
is not a square for \(R5\).

So a proof cannot stop at the boundary point.  It must prove that no other
integral point in the two residual cosets passes the square filters.

## Certificate File

The executable target is
\[
  \texttt{tools/m3mod4\_residual\_coset\_integral\_points.magma}.
\]

It verifies the curve, rank, torsion data, the coset representative \(P_0\),
the boundary point, then calls Magma's `IntegralPoints(E)` and filters the
complete integral-point set through the two cosets and the separated square
conditions.

The certificate succeeds only if it reaches
```text
CERTIFIED: the residual Mordell-Weil coset pair contains no R4/R5 integral point.
```

This is the next proof-level gate.  Another independent local CRT layer is
not the right object unless it is part of a genuine Mordell-Weil sieve with a
height bound.
