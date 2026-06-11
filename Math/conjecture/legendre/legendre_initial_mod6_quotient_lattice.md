# Initial Mod-6 Quotient Lattice

This note strengthens the even quotient lift by using the \(3\)-adic part
of the reduced quotient pencil.

The result is layer-sensitive: A0 quotients and A1 quotients occupy disjoint
classes modulo \(6\).

## 1. Reduced quotient pencil modulo \(3\)

From the even quotient lift, every initial quotient is even.  Write
\[
  e=2f.
\]

The centered equation becomes
\[
\boxed{
  (r+f)^2=f^2+6mf-c.
}
\]

Reducing modulo \(3\) gives
\[
\boxed{
  (r+f)^2\equiv f^2-c\pmod3.
}
\]

Since the only square classes modulo \(3\) are
\[
  0,1,
\]
the class \(f^2-c\) cannot be \(2\bmod3\).

## 2. A0 quotients

For an A0 offset,
\[
  c=x^2.
\]

In the initial four complete A-blocks, the coordinate \(x\) is never
divisible by \(3\).  Hence
\[
  c=x^2\equiv1\pmod3.
\]

The congruence
\[
  f^2-c
\]
is a square modulo \(3\).  If \(3\mid f\), then
\[
  f^2-c\equiv -1\equiv2\pmod3,
\]
impossible.

Therefore
\[
\boxed{
  3\nmid f
}
\]
for every A0 quotient.

Equivalently,
\[
\boxed{
  e=2f\equiv2\text{ or }4\pmod6.
}
\]

## 3. A1 quotients

For an A1 offset,
\[
  c=y^2+1.
\]

Again \(3\nmid y\), so
\[
  y^2\equiv1\pmod3,
  \qquad
  c=y^2+1\equiv2\pmod3.
\]

If \(3\nmid f\), then
\[
  f^2-c\equiv 1-2\equiv2\pmod3,
\]
impossible.

Therefore
\[
\boxed{
  3\mid f
}
\]
for every A1 quotient.

Equivalently,
\[
\boxed{
  e=2f\equiv0\pmod6.
}
\]

## 4. Layer-sensitive quotient support

Thus the clean strong-gate quotient support is split exactly as follows:
\[
\boxed{
  \begin{array}{c|c}
    \text{layer} & \text{quotient class}\\
    \hline
    \mathrm{A0} & e\equiv2,4\pmod6\\
    \mathrm{A1} & e\equiv0\pmod6
  \end{array}
}
\]

This is stronger than mere evenness.

The four A0 quotients are distinct positive integers in
\[
  \{2,4,8,10,14,16,\dots\},
\]
so their ordered lower bounds are
\[
\boxed{
  2,\ 4,\ 8,\ 10.
}
\]

The four A1 quotients are distinct positive multiples of \(6\), so their
ordered lower bounds are
\[
\boxed{
  6,\ 12,\ 18,\ 24.
}
\]

Consequently the globally ordered quotient tuple satisfies
\[
\boxed{
  e_{(1)},\dots,e_{(8)}
  \ge
  2,\ 4,\ 6,\ 8,\ 10,\ 12,\ 18,\ 24
}
\]
componentwise.

## 5. Mod-6 rank barrier

Define
\[
  M=(M_1,\dots,M_8)=(2,4,6,8,10,12,18,24).
\]

If an offset carries global quotient rank \(k\), then
\[
  e\ge M_k.
\]

As before, from
\[
  e=\frac{r^2+c}{A-r},
  \qquad
  c\le122,
\]
the condition \(e\ge M_k\) gives
\[
  r^2+M_kr\ge M_kA-122.
\]

Define
\[
\boxed{
  \widehat B_k(A):=
  \left\lceil
    \frac{-M_k+\sqrt{M_k^2+4(M_kA-122)}}{2}
  \right\rceil.
}
\]

Then every offset carrying quotient rank \(k\) satisfies
\[
\boxed{
  r\ge\widehat B_k(A).
}
\]

The largest quotient rank now forces
\[
\boxed{
  r\ge
  \widehat B_8(A)
  =
  \left\lceil
    \frac{-24+\sqrt{576+96A-488}}{2}
  \right\rceil
  =
  \left\lceil
    -12+\sqrt{24A+22}
  \right\rceil.
}
\]

This is asymptotic to
\[
  \sqrt{24A},
\]
stronger than the even-only asymptotic
\[
  4\sqrt A=\sqrt{16A}.
\]

## 6. Clean strong-gate consequence

The two-layer ladder certificate should now use
\[
  \widehat B_k(A)
\]
instead of both previous barriers
\[
  B_k(A)
  \quad\text{and}\quad
  \widetilde B_k(A).
\]

For a layer word \(L\), the lifted word envelope is
\[
\boxed{
  \widehat H_i^L(A):=
  \max_{i\le j\le8}
  \left(\widehat B_{9-j}(A)+W_L(i,j)\right).
}
\]

Every clean strong-gate certificate with \(m\ge4881\) satisfies
\[
\boxed{
  D_i\ge\widehat H_i^L(A).
}
\]

This is an exact mod-\(6\) obstruction on the hidden cofactor gaps.  It comes
from the identity \(A=3m\) and the A0/A1 layer geometry, not from numerical
experimentation.
