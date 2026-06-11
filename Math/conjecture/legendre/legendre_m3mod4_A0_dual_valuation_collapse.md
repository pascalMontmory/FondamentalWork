# A0 Dual Valuation Collapse

This note uses the full equality
\[
  u^2+x^2=fF
\]
from the dual-factor model, not only the separate splitting laws for \(f\)
and \(F\).

The hard branch is
\[
  m\equiv3\pmod4,
  \qquad
  L=6m=2h,
  \qquad
  h\equiv1\pmod4.
\]

For A0 offsets \(c=x^2\), write
\[
  F=f+L.
\]

Then
\[
\boxed{
  u^2+x^2=fF.
}
\]

This gives an exact \(2\)-adic compatibility between the lower and upper
factors.

## 1. Valuations of \(u^2+2^{2a}\)

Let
\[
  x=2^a x_0,
  \qquad
  x_0\text{ odd}.
\]

For the A0 offsets relevant here, \(x_0=1\) or \(5\), so the \(2\)-adic
behavior is the same as for \(2^a\).

Write
\[
  u=2^r w,
  \qquad
  w\text{ odd}.
\]

Then the possible valuations of
\[
  u^2+x^2
\]
are:

- if \(r<a\), then
  \[
    v_2(u^2+x^2)=2r;
  \]
- if \(r>a\), then
  \[
    v_2(u^2+x^2)=2a;
  \]
- if \(r=a\), then
  \[
    v_2(u^2+x^2)=2a+v_2(w^2+x_0^2)=2a+1,
  \]
  since \(w^2+x_0^2\equiv2\pmod4\).

Thus the possible values are
\[
\boxed{
  0,2,\dots,2a-2,\quad 2a,\quad 2a+1.
}
\]

## 2. The zero-layer upper factor has \(v_2(F)=1\)

For the A0 zero-layer offsets
\[
  c=16,\ 64,
\]
the lower quotient has
\[
  f=2^\nu s,
  \qquad
  \nu\ge3,
  \qquad
  s\text{ odd}.
\]

The upper factor is
\[
  F=f+2h=2(2^{\nu-1}s+h).
\]

Since
\[
  \nu\ge3,
  \qquad
  h\equiv1\pmod4,
\]
the factor
\[
  2^{\nu-1}s+h
\]
is odd.  Hence
\[
\boxed{
  v_2(F)=1.
}
\]

Therefore
\[
\boxed{
  v_2(fF)=\nu+1.
}
\]

## 3. Consequence for \(c=16\)

For
\[
  c=16,
  \qquad
  x=4=2^2,
\]
one has \(a=2\).  The possible valuations of
\[
  u^2+16
\]
are
\[
\boxed{
  0,\ 2,\ 4,\ 5.
}
\]

The previous A0 zero-layer theorem allowed
\[
  3\le\nu\le5.
\]

But
\[
  v_2(fF)=\nu+1.
\]

Thus:
\[
\begin{array}{c|c|c}
  \nu & v_2(fF) & \text{status}\\
  \hline
  3 & 4 & \text{allowed}\\
  4 & 5 & \text{allowed}\\
  5 & 6 & \text{impossible}.
\end{array}
\]

Therefore:
\[
\boxed{
  c=16
  \quad\Longrightarrow\quad
  f\in 8\mathcal S_4\cup16\mathcal S_4.
}
\]

The old branch
\[
  f\in32\mathcal S_4
\]
is impossible.

## 4. Consequence for \(c=64\)

For
\[
  c=64,
  \qquad
  x=8=2^3,
\]
one has \(a=3\).  The possible valuations of
\[
  u^2+64
\]
are
\[
\boxed{
  0,\ 2,\ 4,\ 6,\ 7.
}
\]

The previous A0 zero-layer theorem allowed
\[
  3\le\nu\le7.
\]

Again
\[
  v_2(fF)=\nu+1.
\]

Thus:
\[
\begin{array}{c|c|c}
  \nu & v_2(fF) & \text{status}\\
  \hline
  3 & 4 & \text{allowed}\\
  4 & 5 & \text{impossible}\\
  5 & 6 & \text{allowed}\\
  6 & 7 & \text{allowed}\\
  7 & 8 & \text{impossible}.
\end{array}
\]

Therefore:
\[
\boxed{
  c=64
  \quad\Longrightarrow\quad
  f\in
  8\mathcal S_4\cup32\mathcal S_4\cup64\mathcal S_4.
}
\]

The old branches
\[
  f\in16\mathcal S_4
  \qquad\text{and}\qquad
  f\in128\mathcal S_4
\]
are impossible.

## 5. Consequence for the zero-layer pair

For the pair
\[
  c=16,\ 64,
\]
the lower quotient semigroups are now:
\[
\boxed{
  c=16:\quad 8\mathcal S_4\cup16\mathcal S_4,
}
\]
and
\[
\boxed{
  c=64:\quad 8\mathcal S_4\cup32\mathcal S_4\cup64\mathcal S_4.
}
\]

In particular, the lower quotient
\[
  f=16
\]
can occur only on the \(c=16\) row, not on the \(c=64\) row.

Thus the zero-layer assignment is no longer symmetric.  Any minimal
zero-layer use of the two quotients
\[
  8,\ 16
\]
must attach
\[
\boxed{
  f=16\text{ to }c=16.
}
\]

This is an intrinsic \(2\)-adic consequence of the same-gap factorization,
not a finite-prime certificate.
