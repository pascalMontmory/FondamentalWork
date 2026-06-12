# Colored Distance Gate for the \(u=1\) Cluster

This note adds residue colors to the \(u=1\) cluster and quotient-rank
gates.

It does not close Legendre.  It makes the failure of the first nonprimitive
repair layer more rigid: every forced center distance \(r_c\) lies in an
explicit congruence class family, unless the chosen label is a ramified prime
dividing the offset and hence also dividing the center \(A=3m\).

## 1. General color principle

Let
\[
  p_c=A-r_c
\]
be a prime label forced by
\[
  p_c\mid A^2+c.
\]

If
\[
  p_c\nmid c,
\]
then
\[
  A^2\equiv -c\pmod {p_c}
\]
forces
\[
  \left(\frac{-c}{p_c}\right)=1.
\]

Equivalently, \(p_c\) lies in the corresponding quadratic-residue color
classes.  Since
\[
  r_c=A-p_c,
\]
this becomes an explicit congruence restriction on \(r_c\):
\[
  r_c\equiv A-s\pmod M
\]
for one of the allowed prime residue classes \(s\pmod M\).

If instead
\[
  p_c\mid c,
\]
then the same divisibility gives
\[
  p_c\mid A.
\]
This is the ramified alternative.  In the \(u=1\) cluster it can only happen
for the small labels \(5\) or \(11\).

## 2. Odd branch colors

In the odd no-\(u=1\)-repair branch,
\[
  \mathcal C_o=\{2,4,8,10\}.
\]

### Offsets \(2\) and \(8\)

For \(c=2\) and \(c=8\), no odd prime label divides \(c\).  Since
\[
  \left(\frac{-2}{p}\right)=1
  \quad\Longleftrightarrow\quad
  p\equiv1,3\pmod8,
\]
we have
\[
  p_2,p_8\equiv1,3\pmod8.
\]
Thus
\[
\boxed{
  r_2,r_8\equiv A-1,\ A-3\pmod8.
}
\]

### Offset \(4\)

For \(c=4\), the A0 anchor already imposes
\[
  p_4\equiv1\pmod4.
\]
Therefore
\[
\boxed{
  r_4\equiv A-1\pmod4.
}
\]

### Offset \(10\)

For \(c=10\), there is one ramified possibility:
\[
  p_{10}=5,\qquad 5\mid A.
\]

Outside this ramified gate, the color is
\[
  \left(\frac{-10}{p_{10}}\right)=1.
\]
The corresponding classes are
\[
  p_{10}\equiv
  1,7,9,11,13,19,23,37
  \pmod {40}.
\]
Hence the nonramified distance restriction is
\[
\boxed{
  r_{10}\equiv
  A-s\pmod {40},
  \quad
  s\in\{1,7,9,11,13,19,23,37\}.
}
\]

So the odd branch has only one ramified color gate:
\[
\boxed{
  5\mid A\quad\text{through the label }p_{10}=5.
}
\]

## 3. Even branch colors

In the even no-\(u=1\)-repair branch,
\[
  \mathcal C_e=\{1,5,11\}.
\]

### Offset \(1\)

For \(c=1\),
\[
  \left(\frac{-1}{p_1}\right)=1
  \quad\Longleftrightarrow\quad
  p_1\equiv1\pmod4.
\]
Thus
\[
\boxed{
  r_1\equiv A-1\pmod4.
}
\]

### Offset \(5\)

There is a ramified possibility
\[
  p_5=5,\qquad 5\mid A.
\]

Outside it,
\[
  \left(\frac{-5}{p_5}\right)=1
  \quad\Longleftrightarrow\quad
  p_5\equiv1,3,7,9\pmod {20}.
\]
Therefore
\[
\boxed{
  r_5\equiv A-s\pmod {20},
  \quad
  s\in\{1,3,7,9\}.
}
\]

### Offset \(11\)

There is a ramified possibility
\[
  p_{11}=11,\qquad 11\mid A.
\]

Outside it,
\[
  \left(\frac{-11}{p_{11}}\right)=1,
\]
which gives
\[
  p_{11}\equiv
  1,3,5,9,15,23,25,27,31,37
  \pmod {44}.
\]
Thus
\[
\boxed{
  r_{11}\equiv
  A-s\pmod {44},
  \quad
  s\in\{1,3,5,9,15,23,25,27,31,37\}.
}
\]

The even branch therefore has two ramified color gates:
\[
\boxed{
  5\mid A\quad\text{through }p_5=5,
  \qquad
  11\mid A\quad\text{through }p_{11}=11.
}
\]

The previously isolated shared-\(5\) gate
\[
  A\equiv\pm2\pmod5
\]
is different: it is not a ramified \(5\mid A\) gate.  It is the possible
common-label gate where
\[
  5\mid A^2+1
  \quad\text{and}\quad
  5\mid A^2+11.
\]

## 4. Colored rank target

Combine this note with the quotient-rank gate.

In the odd branch, for \(m\ge19\), the four quotients are distinct and hence
have ranks
\[
  e_{(k)}\ge k,\qquad1\le k\le4.
\]
The attached distances must also satisfy:
\[
  r_2,r_8\in A-\{1,3\}\pmod8,
\]
\[
  r_4\equiv A-1\pmod4,
\]
and either
\[
  p_{10}=5,\ 5\mid A,
\]
or
\[
  r_{10}\in
  A-\{1,7,9,11,13,19,23,37\}\pmod {40}.
\]

In the even branch, for \(m\ge28\), outside the shared-\(5\) gate, the three
quotients are distinct and their distances must satisfy:
\[
  r_1\equiv A-1\pmod4,
\]
and either the ramified gates
\[
  p_5=5,\ 5\mid A,
  \qquad
  p_{11}=11,\ 11\mid A,
\]
or the nonramified color restrictions modulo \(20\) and \(44\) above.

Thus the next exact closure statement is:

> A full A-block cover with no \(u=1\) repair must realize a ranked colored
> distance assignment.  The only escapes from the color classes are explicit
> ramified divisibility gates \(5\mid A\) or \(11\mid A\), plus the even
> shared-\(5\) gate \(A\equiv\pm2\pmod5\).

This is the right form for the next descent attempt: every exceptional color
gate is now a small-prime divisibility condition on the center \(A=3m\).
