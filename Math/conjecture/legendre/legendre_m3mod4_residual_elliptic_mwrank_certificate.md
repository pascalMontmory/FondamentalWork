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
