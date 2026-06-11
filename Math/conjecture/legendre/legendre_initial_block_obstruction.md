# Initial Block Obstruction

This note applies the labeling constraints to the first three A-blocks
\[
  q=0,\qquad q=1,\qquad q=2.
\]

The point is to extract a finite, exact obstruction near the start of the
interval, before any asymptotic argument is used.

## 1. Admissibility of the first three blocks

The blocks are:
\[
  B_0=\{1,2\},\qquad B_1=\{4,5\},\qquad B_2=\{7,8\}.
\]

They are complete A-blocks once the larger A1 coordinate satisfies
\[
  t_1^2+1\le6m.
\]
For \(B_2\), this is at worst
\[
  8^2+1=65\le6m.
\]
Thus all three blocks are complete for
\[
  m\ge11.
\]

The remaining cases
\[
  m\le10
\]
are finite boundary cases for this initial-block argument.

## 2. Coprimality of the first blocks

Recall that a block is coprime when
\[
  \gcd(t_1(q),9m^2+1)=1.
\]

### Block \(q=0\)

Here \(t_1(0)\in\{1,2\}\).
Since
\[
  9m^2+1
\]
is always odd when \(t_1(0)=2\), one has
\[
  \gcd(t_1(0),9m^2+1)=1.
\]
Thus \(B_0\) is always coprime.

### Block \(q=2\)

Here \(t_1(2)\in\{7,8\}\).
If \(t_1(2)=8\), coprimality is automatic because \(9m^2+1\) is odd.

If \(t_1(2)=7\), then
\[
  9m^2+1\equiv2m^2+1\pmod7.
\]
The nonzero square classes modulo \(7\) are
\[
  1,2,4.
\]
The congruence
\[
  2m^2+1\equiv0\pmod7
\]
would require
\[
  m^2\equiv3\pmod7,
\]
which is impossible.

Thus \(B_2\) is always coprime.

### Block \(q=1\)

Here \(t_1(1)\in\{4,5\}\).
If \(t_1(1)=4\), coprimality is automatic because \(9m^2+1\) is odd.

If \(t_1(1)=5\), then
\[
  9m^2+1\equiv -m^2+1\pmod5.
\]
So \(B_1\) fails to be coprime exactly when
\[
  m^2\equiv1\pmod5.
\]

Since \(t_1(1)=5\) occurs when \(m\) is odd, the only initial coprime-block
loss is:
\[
  m\ \text{odd},\qquad m\equiv\pm1\pmod5.
\]

## 3. Initial triple of coprime blocks

For
\[
  m\ge11
\]
and not in the exceptional classes
\[
  m\ \text{odd},\qquad m\equiv\pm1\pmod5,
\]
the three blocks
\[
  B_0,\ B_1,\ B_2
\]
are complete and coprime.

In this situation, the no-triple rule applies in each layer.  Moreover,
adjacent repetition is impossible between:

- \(B_0\) and \(B_1\), because repeated adjacent labels would require
  \[
    p\mid1;
  \]
- \(B_1\) and \(B_2\), because repeated adjacent labels would require
  \[
    p\mid2.
  \]

For all certificate primes \(p\ge5\), both are impossible.

Thus in each layer, the labels on \(B_0,B_1,B_2\) must satisfy
\[
  p_i(0)\ne p_i(1),
  \qquad
  p_i(1)\ne p_i(2).
\]

## 4. Possible repetition between \(B_0\) and \(B_2\)

The only possible same-layer repetition among the initial triple is between
\[
  B_0
  \quad\text{and}\quad
  B_2.
\]

Since the orientation is the same for \(q=0\) and \(q=2\), the same-layer
coordinates differ by \(6\).  If a prime \(p\ge5\) certifies both, then
\[
  t_i(0)^2\equiv t_i(2)^2\pmod p.
\]
The difference factor is
\[
  t_i(2)-t_i(0)=6,
\]
so \(p\) must divide the sum
\[
  t_i(2)+t_i(0)=2t_i(0)+6.
\]

Since \(t_i(0)\in\{1,2\}\), this sum is either
\[
  8
  \quad\text{or}\quad
  10.
\]
Therefore the only possible prime \(p\ge5\) allowing a same-layer repetition
between \(B_0\) and \(B_2\) is
\[
  p=5,
\]
and this can occur only for the coordinate
\[
  t_i(0)=2.
\]

## 5. Layer restrictions for the exceptional repetition \(p=5\)

The coordinate \(t_i(0)=2\) lies:

- in A1 when \(m\) is even;
- in A0 when \(m\) is odd.

### A0 case

If \(p=5\) is used in A0, it satisfies
\[
  p\equiv1\pmod4.
\]
It is allowed only if
\[
  5\nmid m.
\]
But certification of the repeated coordinate \(t=2\) imposes the stronger
congruence
\[
  9m^2+2^2\equiv0\pmod5.
\]
Since \(9\equiv4\pmod5\), this is
\[
  4m^2+4\equiv0\pmod5,
\]
or equivalently
\[
  m^2\equiv -1\equiv4\pmod5.
\]

Thus A0 can repeat \(p=5\) from \(B_0\) to \(B_2\) only when
\[
  m\ \text{is odd},\qquad m\equiv\pm2\pmod5.
\]

### A1 case

If \(p=5\) is used in A1, then A1 availability requires
\[
  -9m^2-1
\]
to be a nonzero square modulo \(5\).  Since
\[
  -9m^2-1\equiv m^2-1\pmod5,
\]
this happens exactly when
\[
  m\equiv0\pmod5.
\]

Thus A1 can repeat \(p=5\) from \(B_0\) to \(B_2\) only when
\[
  m\ \text{is even},\qquad 5\mid m.
\]

## 6. Exact initial obstruction

For
\[
  m\ge11
\]
outside the coprime-loss classes
\[
  m\ \text{odd},\qquad m\equiv\pm1\pmod5,
\]
the initial three blocks force the following:

1. In each layer, adjacent labels among \(B_0,B_1,B_2\) are all distinct.
2. A same-layer repetition between \(B_0\) and \(B_2\) is possible only with
   the prime \(5\).
3. That \(p=5\) repetition is restricted to:
   \[
   \begin{array}{ll}
   \text{A0:} & m\ \text{odd},\ m\equiv\pm2\pmod5,\\
   \text{A1:} & m\ \text{even},\ 5\mid m.
   \end{array}
   \]

This does not close the conjecture, but it gives a finite exact split of the
first universal triple.  Any complete counterexample must respect these
initial labeling constraints before the later interval is considered.
