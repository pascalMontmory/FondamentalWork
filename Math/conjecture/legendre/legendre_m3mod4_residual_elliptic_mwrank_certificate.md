# Residual Elliptic Curve Mordell-Weil Certificate

This note records the exact elliptic-curve data for the two residual
prefix-\(8\) Pell fibers.

The common residual quartic is
\[
  W^2=1845s^4-128s^2-117.
\]

Set
\[
  X=1845s^2,\qquad Y=1845sW.
\]
Then
\[
  Y^2=X^3-128X^2-215865X.
\]

Thus every integral point on the residual quartic maps to a rational point on
\[
  E:\quad Y^2=X^3-128X^2-215865X
\]
with
\[
  X\in1845\mathbf Z^2.
\]

## mwrank certificate

Running
\[
  \texttt{mwrank [0,-128,0,-215865,0]}
\]
gives an unconditional Mordell-Weil computation.

The torsion points are
\[
  (0,0),\qquad (533,0),\qquad (-405,0),
\]
so
\[
  E(\mathbf Q)_{\mathrm{tors}}\simeq(\mathbf Z/2\mathbf Z)^2.
\]

The rank is
\[
  \operatorname{rank}E(\mathbf Q)=3,
\]
with Mordell-Weil basis
\[
\begin{aligned}
  G_1&=(-363,3696),\\
  G_2&=(-195,5460),\\
  G_3&=(-117,4680).
\end{aligned}
\]

Therefore every rational point on \(E\) has the form
\[
  n_1G_1+n_2G_2+n_3G_3+T,
\]
where
\[
  n_i\in\mathbf Z,\qquad
  T\in\{O,(0,0),(533,0),(-405,0)\}.
\]

The boundary quartic point
\[
  s=1,\qquad W=40
\]
maps to
\[
  P=(1845,73800).
\]

In the Mordell-Weil basis,
\[
  P=G_3+(0,0).
\]

## Remaining exact sieve

The residual fibers are closed once one proves:
\[
  x(n_1G_1+n_2G_2+n_3G_3+T)\in1845\mathbf Z^2
  \quad\Longrightarrow\quad
  (n_1,n_2,n_3,T)=(0,0,1,(0,0))
\]
up to sign, and then checks the two terminal residual pairs.  At \(s=1\),
neither terminal pair is satisfied:
\[
  1701s^2-908=793\quad\text{is not a square}
\]
for the first residual fiber, and
\[
  1701s^2-1004=697\quad\text{is not a square}
\]
for the second.

So the remaining proof is a Mordell-Weil sieve/integral-point computation on
the explicit rank-\(3\) curve above.  No further CRT descent or prefix growth
is mathematically appropriate.

## Sage integral-points target

The direct global certificate is now recorded in
\[
  \texttt{tools/m3mod4\_residual\_integral\_points.sage}.
\]

It asks Sage for the integral points on
\[
  E:\quad Y^2=X^3-128X^2-215865X
\]
using the certified Mordell-Weil basis
\[
  G_1=(-363,3696),\quad
  G_2=(-195,5460),\quad
  G_3=(-117,4680).
\]

It then applies the exact filters
\[
  X=1845s^2
\]
and the separated square equations for the common core and for the two
terminal fibers \(R4,R5\).

The certificate condition is:
\[
  \texttt{R4 candidates}=\varnothing,\qquad
  \texttt{R5 candidates}=\varnothing,
\]
after the already saturated boundary \(s=\pm1\).  This is the correct
rank-\(3\) IntegralPoints closure target.

Sage/Magma is not optional at this point: elementary finite local tests on
\(s\) do not kill the fibers.  Direct \(p\)-adic lifting of the full separated
R4/R5 square systems survives for the small primes tested, e.g. both fibers
survive through \(3^8,5^6,7^6,11^6,13^5,17^5,19^5,23^5\) and through
\(29^4,31^4,37^4,41^4,43^4,47^4\).  This negative result is not a proof of
existence; it only rules out the easy local-congruence closure.

## Implemented sieve scaffold

The script
\[
  \texttt{tools/m3mod4\_residual\_mw\_sieve.py}
\]
implements the first Mordell-Weil sieve layer using the certified basis
\[
  G_1,G_2,G_3
\]
and reductions modulo good primes.  It supports three modes:

\[
  \texttt{common},\qquad \texttt{r4},\qquad \texttt{r5}.
\]

The modes \(\texttt{r4}\) and \(\texttt{r5}\) impose not only
\[
  X\in1845\mathbf Z^2,
\]
but also the separated square conditions for the corresponding terminal
residual pair.

The implemented certificate option
\[
  \texttt{--expect-prefix8-terminal-pair}
\]
now verifies the strongest local Mordell-Weil reduction reached so far.  For
both terminal fibers \(R4\) and \(R5\), the surviving coefficient classes
modulo \(1320\) are exactly
\[
\begin{aligned}
  (n_1,n_2,n_3;T)&\equiv(0,2,1;(0,0))\pmod{1320},\\
  (n_1,n_2,n_3;T)&\equiv(0,-2,-1;(0,0))\pmod{1320}.
\end{aligned}
\]

Equivalently, the two residual terminal systems share the same opposite pair
of Mordell-Weil classes:
\[
  \boxed{(0,\pm2,\pm1)+(0,0)\pmod{1320}.}
\]

The positive representative is
\[
  P_0=2G_2+G_3+(0,0)
      =
      \left(\frac{10045}{9},-\frac{849520}{27}\right).
\]

Thus every remaining residual point must satisfy the exact coset condition
\[
  P\in P_0+1320E(\mathbf Q)
  \quad\text{or}\quad
  P\in -P_0+1320E(\mathbf Q),
\]
in addition to
\[
  x(P)=1845s^2
\]
and the separated \(R4\) or \(R5\) square equations.

This is an exact finite-group certificate, not an interval computation.  It
does not close the residual fibers, because a global rational point may still
lie in one of these two congruence classes.  It does however reduce the final
obstruction to one pair of rank-\(3\) Mordell-Weil residue classes.

The coset-specific Magma target is recorded in
\[
  \texttt{tools/m3mod4\_residual\_coset\_integral\_points.magma}.
\]
It computes \(E(\mathbf Q)\), tests membership in the two cosets above, and
then applies the \(x=1845s^2\), \(R4\), and \(R5\) filters.  The desired final
certificate is
\[
  \texttt{R4 candidates}=\varnothing,\qquad
  \texttt{R5 candidates}=\varnothing.
\]

The final proof still needs either:

1. a height bound plus a full Mordell-Weil sieve, or
2. an external integral-points computation on the rank-\(3\) curve.
