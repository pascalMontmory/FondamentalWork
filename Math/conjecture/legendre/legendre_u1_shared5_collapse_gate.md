# Shared-\(5\) Collapse in the \(u=1\) Cluster

This note isolates the cleanest exceptional fiber from the \(u=1\)-cluster
analysis: the even shared-\(5\) gate.

It is not a proof of Legendre.  It is an exact collapse of one residual
fiber to a single remaining colored divisor equation.

Throughout,
\[
  A=3m,
\]
with \(m\) even, and we are in the even no-\(u=1\)-repair cluster
\[
  \{1,5,11\}.
\]

## 1. The shared-\(5\) gate

The shared-\(5\) gate is
\[
  A\equiv\pm2\pmod5.
\]
Equivalently,
\[
  A^2\equiv -1\pmod5.
\]

Therefore
\[
  5\mid A^2+1,
  \qquad
  5\mid A^2+11.
\]

The two offsets \(1\) and \(11\) can be certified by the same prime label
\[
  p_1=p_{11}=5.
\]
Their common center-distance is
\[
  r_1=r_{11}=A-5.
\]

The quotients are
\[
  e_1=\frac{(A-5)^2+1}{5}
  =
  \frac{A^2-10A+26}{5},
\]
and
\[
  e_{11}=\frac{(A-5)^2+11}{5}
  =
  \frac{A^2-10A+36}{5}.
\]
Hence
\[
\boxed{
  e_{11}=e_1+2.
}
\]

This is a rigid two-offset atom, not a free collision.

## 2. The remaining offset \(c=5\)

The only remaining offset in the even cluster is
\[
  c=5.
\]
Since
\[
  A^2\equiv4\pmod5,
\]
we have
\[
  A^2+5\equiv4\pmod5.
\]
Thus \(5\) cannot certify the offset \(5\).  Any label for \(A^2+5\) must be
a prime
\[
  p_5\ge7.
\]

Write
\[
  p_5=A-r_5.
\]
Then the remaining condition is exactly
\[
\boxed{
  A-r_5\mid r_5^2+5,
  \qquad
  A-r_5\ge7.
}
\]

Outside the ramified label \(5\), the color condition is
\[
  \left(\frac{-5}{p_5}\right)=1.
\]
Equivalently,
\[
  p_5\equiv1,3,7,9\pmod {20}.
\]
So
\[
\boxed{
  r_5\equiv A-s\pmod {20},
  \qquad
  s\in\{1,3,7,9\}.
}
\]

Thus the shared-\(5\) gate reduces the three-offset cluster to one colored
divisor equation for \(A^2+5\).

## 3. Quotient order is fixed

The remaining quotient is
\[
  e_5=\frac{r_5^2+5}{A-r_5}.
\]
Since \(p_5=A-r_5\ge7\), write \(p=p_5\).  Then
\[
  e_5
  =
  \frac{(A-p)^2+5}{p}
  =
  \frac{A^2}{p}-2A+p+\frac5p.
\]
For \(p\ge7\),
\[
  e_5
  \le
  \frac{A^2}{7}-2A+7+\frac57.
\]

Compare this with
\[
  e_1=\frac{A^2}{5}-2A+\frac{26}{5}.
\]
Then
\[
  e_1-e_5
  \ge
  \frac{2A^2}{35}+\frac{26}{5}-7-\frac57
  =
  \frac{2A^2-88}{35}.
\]
This is positive for every \(A\ge7\).

Therefore:
\[
\boxed{
  e_5<e_1<e_{11}
  \qquad(A\ge7).
}
\]

So in the shared-\(5\) fiber, the quotient order is forced:
\[
  c=5
  \quad\text{has the lowest quotient rank,}
\]
and the shared labels \(c=1,11\) occupy the two top ranks.

## 4. Exact collapsed target

The shared-\(5\) no-\(u=1\)-repair fiber is equivalent to the following
single-offset obstruction:

There exists even \(A=3m\) such that
\[
  A\equiv\pm2\pmod5,
\]
and there exists a prime
\[
  p=A-r\ge7
\]
with
\[
  p\mid A^2+5,
\]
equivalently
\[
  A-r\mid r^2+5,
\]
and
\[
  p\equiv1,3,7,9\pmod {20}.
\]

The two other offsets are no longer variables:
\[
  A^2+1,\ A^2+11
\]
are both certified by the fixed label \(5\), with quotient gap \(2\).

In this fiber, a full A-block cover with no \(u=1\) repair must therefore
come from the interaction between:

1. the fixed shared-\(5\) atom at offsets \(1,11\);
2. the single colored divisor equation for \(A^2+5\);
3. the global A-block cover constraints beyond the anchor.

The next descent attempt should use this collapsed form: the first two
forced composites no longer supply independent covering resources.
