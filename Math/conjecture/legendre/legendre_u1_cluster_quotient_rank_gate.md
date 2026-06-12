# Quotient Rank Gate for the \(u=1\) Cluster

This note strengthens the \(u=1\) repair cluster gate.

The previous gate showed that a full coprime A-block cover with no \(u=1\)
repair forces a finite cluster of composites near
\[
  A^2,\qquad A=3m.
\]
Here we show that the corresponding quotient parameters are automatically
distinct except for a small finite range, or for the already isolated even
shared-\(5\) gate.

This gives ranked square-root barriers for the forced labels.

## 1. Equal quotient obstruction, specialized

For an offset \(c\), write the centered divisor equation as
\[
  A-r_c\mid r_c^2+c,
  \qquad
  e_c=\frac{r_c^2+c}{A-r_c}.
\]
Equivalently,
\[
  A=r_c+\frac{r_c^2+c}{e_c}.
\]

Suppose two distinct offsets \(c\ne d\) have distinct prime labels
\[
  A-r_c\ne A-r_d
\]
but equal quotient
\[
  e_c=e_d=e.
\]
In the large ranges used below, \(A\) is larger than every offset in the
cluster.  Therefore \(A-r_c=A\) cannot divide \(A^2+c\), and the forced
distances satisfy
\[
  r_c,r_d\ge1.
\]

The pair-compatibility equation becomes
\[
  c-d=(r_d-r_c)(r_c+r_d+e).
\]
Since \(r_d-r_c\ne0\), this implies
\[
  r_c+r_d+e\le |c-d|.
\]
In particular,
\[
  r_c\le |c-d|-2.
\]

Also, since \(e_c\ge1\),
\[
  A
  =
  r_c+\frac{r_c^2+c}{e_c}
  \le r_c+r_c^2+c.
\]

Thus equal quotients force a purely finite bound on \(A\).

## 2. Odd branch: four quotients are distinct for \(m\ge19\)

In the odd no-\(u=1\)-repair cluster,
\[
  \mathcal C_o=\{2,4,8,10\}.
\]
The maximum offset difference is
\[
  D_o=8,
\]
and the maximum offset is
\[
  C_o=10.
\]

If two distinct offsets in \(\mathcal C_o\) had the same quotient, then
\[
  r_c\le D_o-2=6.
\]
Therefore
\[
  A\le r_c+r_c^2+c\le6+36+10=52.
\]

Since
\[
  A=3m
\]
and \(m\) is odd, all odd-branch values with
\[
  m\ge19
\]
satisfy
\[
  A\ge57>52.
\]

Hence:
\[
\boxed{
  m\ge19,\ m\ \text{odd},\ \text{no }u=1\text{ repair}
  \quad\Longrightarrow\quad
  e_2,e_4,e_8,e_{10}\ \text{are distinct}.
}
\]

This is unconditional inside the odd forced cluster, because the four
cluster values are pairwise coprime, so their prime labels are distinct.

## 3. Odd ranked barriers

Order the four quotients as
\[
  e_{(1)}<e_{(2)}<e_{(3)}<e_{(4)}.
\]
For \(m\ge19\), quotient distinctness gives
\[
  e_{(k)}\ge k,\qquad 1\le k\le4.
\]

For any offset \(c\le10\),
\[
  r^2+er+c=eA
\]
implies
\[
  r\ge
  \left\lceil
    \frac{-e+\sqrt{e^2+4(eA-10)}}{2}
  \right\rceil.
\]

Therefore the distance attached to quotient rank \(k\) satisfies
\[
\boxed{
  r_{(k)}\ge
  \left\lceil
    \frac{-k+\sqrt{k^2+4(kA-10)}}{2}
  \right\rceil
  \qquad(1\le k\le4).
}
\]

In particular the largest quotient forces
\[
\boxed{
  r_{(4)}\ge
  \left\lceil
    -2+2\sqrt{A-9}
  \right\rceil.
}
\]

Thus at least one of the four forced labels satisfies
\[
\boxed{
  p=A-r\le
  A-\left\lceil -2+2\sqrt{A-9}\right\rceil.
}
\]

This is the first nontrivial rank cost of denying the \(u=1\) repair in the
odd branch.

## 4. Even branch outside the shared-\(5\) gate

In the even branch, the forced cluster is
\[
  \mathcal C_e=\{1,5,11\}.
\]
The only possible repeated prime label is the already isolated gate
\[
  A^2+1\equiv A^2+11\equiv0\pmod5,
  \qquad A\equiv\pm2\pmod5.
\]

Outside that gate, the three labels are distinct.

Here
\[
  D_e=10,\qquad C_e=11.
\]
If two distinct labels had the same quotient, then
\[
  r_c\le D_e-2=8.
\]
Therefore
\[
  A\le8+64+11=83.
\]
Thus for even \(m\) with
\[
  A=3m\ge84
  \qquad\text{equivalently}\qquad
  m\ge28,
\]
the quotients are distinct outside the shared-\(5\) gate.

Hence:
\[
\boxed{
  m\ge28,\ m\ \text{even},\ A\not\equiv\pm2\pmod5
  \quad\Longrightarrow\quad
  e_1,e_5,e_{11}\ \text{are distinct}.
}
\]

The corresponding rank barriers are
\[
\boxed{
  r_{(k)}\ge
  \left\lceil
    \frac{-k+\sqrt{k^2+4(kA-11)}}{2}
  \right\rceil
  \qquad(1\le k\le3).
}
\]

In particular,
\[
\boxed{
  r_{(3)}\ge
  \left\lceil
    \frac{-3+\sqrt{12A-123}}{2}
  \right\rceil.
}
\]

## 5. Residue colors of the forced labels

The forced labels also carry quadratic-residue colors.

In the odd branch:
\[
  p_2\mid A^2+2
  \quad\Longrightarrow\quad
  \left(\frac{-2}{p_2}\right)=1,
\]
\[
  p_4\mid A^2+4
  \quad\Longrightarrow\quad
  p_4\equiv1\pmod4,
\]
\[
  p_8\mid A^2+8
  \quad\Longrightarrow\quad
  \left(\frac{-2}{p_8}\right)=1,
\]
and
\[
  p_{10}\mid A^2+10
  \quad\Longrightarrow\quad
  \left(\frac{-10}{p_{10}}\right)=1.
\]

Since \(A\) is fixed, these are not independent color conditions on
abstract primes.  They impose congruence restrictions on the distances
\[
  r_c=A-p_c
\]
simultaneously with the quotient-rank barriers above.

## 6. New exact closure target

The previous \(u=1\) gate reduced a full cover with no \(u=1\) repair to a
finite cluster of centered divisor equations.

This note adds:

- odd branch, \(m\ge19\): four distinct quotient ranks;
- even branch, \(m\ge28\), outside \(A\equiv\pm2\pmod5\): three distinct
  quotient ranks;
- ranked lower bounds on the center distances \(r_c\);
- residue colors for the forced labels.

Thus the next exact theorem can be sharpened:

> The forced cluster cannot satisfy the quotient-rank barriers and the
> residue colors while also arising from a full A-block cover; the only
> remaining low branches are the finite small-\(m\) range and the even
> shared-\(5\) gate.

This is still not a closure of Legendre.  It is a stricter algebraic target:
the failure of \(u=1\) now has measurable rank cost before any further
blocks are used.
