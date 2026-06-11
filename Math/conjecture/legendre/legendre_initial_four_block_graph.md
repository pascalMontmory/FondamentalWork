# Initial Four-Block Repetition Graph

This note extends the initial mod \(10\) gate from three blocks to four
blocks.

The four blocks are
\[
  B_0=\{1,2\},\quad
  B_1=\{4,5\},\quad
  B_2=\{7,8\},\quad
  B_3=\{10,11\}.
\]

They are complete once
\[
  11^2+1\le6m,
\]
so for
\[
  m\ge21.
\]

## 1. Coprimality of \(B_3\)

The block \(B_3\) introduces a new bridge case.

If \(m\) is even, then \(t_1(3)=10\).  Since \(9m^2+1\) is odd and is
congruent to
\[
  9m^2+1\equiv -m^2+1\pmod5,
\]
one has
\[
  5\mid 9m^2+1
  \quad\Longleftrightarrow\quad
  m^2\equiv1\pmod5.
\]
Thus \(B_3\) fails to be coprime exactly when
\[
  m\ \text{is even},\qquad m\equiv\pm1\pmod5,
\]
or equivalently
\[
  m\equiv4,6\pmod{10}.
\]

In this case \(5\) divides both candidates in \(B_3\), because
\[
  9m^2+11^2\equiv9m^2+1\equiv0\pmod5,
\]
\[
  9m^2+10^2+1\equiv9m^2+1\equiv0\pmod5.
\]

If \(m\) is odd, then \(t_1(3)=11\).  A common factor would require
\[
  9m^2+1\equiv0\pmod{11}.
\]
Equivalently,
\[
  m^2\equiv6\pmod{11},
\]
which is impossible because the square classes modulo \(11\) are
\[
  1,3,4,5,9.
\]

Therefore the bridge classes among the first four blocks are:
\[
  B_1\text{ bridge:}\quad m\equiv1,9\pmod{10},
\]
\[
  B_3\text{ bridge:}\quad m\equiv4,6\pmod{10}.
\]
Equivalently, a bridge occurs among the first four blocks exactly when
\[
  m\equiv\pm1\pmod5.
\]

## 2. Coordinate sequences

There are two coordinate sequences:
\[
  E=(2,4,8,10),
\]
\[
  O=(1,5,7,11).
\]

If \(m\) is even, then
\[
  (t_1(0),t_1(1),t_1(2),t_1(3))=E,
\]
\[
  (t_0(0),t_0(1),t_0(2),t_0(3))=O.
\]

If \(m\) is odd, the two sequences are interchanged:
\[
  (t_1(0),t_1(1),t_1(2),t_1(3))=O,
\]
\[
  (t_0(0),t_0(1),t_0(2),t_0(3))=E.
\]

Thus possible same-prime repetition inside the first four blocks can be
read from the differences and sums in \(E\) and \(O\).

## 3. Repetitions inside \(E=(2,4,8,10)\)

A same-layer repetition between two coordinates \(u,v\in E\) requires
\[
  p\mid u-v
  \quad\text{or}\quad
  p\mid u+v.
\]

For primes \(p\ge5\), the only possibilities are:
\[
  (2,8):\quad p=5,
\]
\[
  (4,10):\quad p=7.
\]

In block notation:
\[
  B_0/B_2\quad\text{may repeat by }5,
\]
\[
  B_1/B_3\quad\text{may repeat by }7.
\]

The \(p=5\) condition at \(t=2\) is:

- in A1, when \(m\) is even:
  \[
    9m^2+2^2+1\equiv0\pmod5
    \quad\Longleftrightarrow\quad
    m\equiv0\pmod5;
  \]
- in A0, when \(m\) is odd:
  \[
    9m^2+2^2\equiv0\pmod5
    \quad\Longleftrightarrow\quad
    m\equiv\pm2\pmod5.
  \]

The \(p=7\) condition at \(t=4\) is:

- in A1, when \(m\) is even:
  \[
    9m^2+4^2+1\equiv0\pmod7
    \quad\Longleftrightarrow\quad
    m^2\equiv2\pmod7;
  \]
  equivalently
  \[
    m\equiv\pm3\pmod7;
  \]
- in A0, when \(m\) is odd:
  \[
    9m^2+4^2\equiv0\pmod7
    \quad\Longleftrightarrow\quad
    m^2\equiv6\pmod7,
  \]
  which is impossible.

## 4. Repetitions inside \(O=(1,5,7,11)\)

For primes \(p\ge5\), the only possible repetition inside \(O\) is
\[
  (1,11):\quad p=5.
\]
In block notation, this is
\[
  B_0/B_3\quad\text{may repeat by }5.
\]

The \(p=5\) condition at \(t=1\) is:

- in A0, when \(m\) is even:
  \[
    9m^2+1^2\equiv0\pmod5
    \quad\Longleftrightarrow\quad
    m^2\equiv1\pmod5;
  \]
  equivalently
  \[
    m\equiv\pm1\pmod5;
  \]
- in A1, when \(m\) is odd:
  \[
    9m^2+1^2+1\equiv0\pmod5
    \quad\Longleftrightarrow\quad
    m^2\equiv2\pmod5,
  \]
  which is impossible.

Thus the only \(O\)-sequence repetition occurs exactly in the \(B_3\) bridge
classes.  It is not a coprime four-block edge.

## 5. Exact four-block graph

For \(m\ge21\), outside the first-four-block bridge classes
\[
  m\equiv\pm1\pmod5,
\]
the first four blocks are complete and coprime.

Any same-layer repetition among them must be one of the following:
\[
\begin{array}{c|c|c|c}
  \text{layer} & \text{blocks} & \text{prime} & \text{condition on }m\\
  \hline
  \text{A1} & B_0/B_2 & 5 & m\equiv0\pmod{10}\\
  \text{A1} & B_1/B_3 & 7 & m\text{ even},\ m\equiv\pm3\pmod7\\
  \text{A0} & B_0/B_2 & 5 & m\equiv3,7\pmod{10}\\
\end{array}
\]

There are no other same-layer repetitions among \(B_0,B_1,B_2,B_3\).

Thus the local certificate graph on the first four complete coprime blocks is
finite and explicit.  The remaining proof problem is no longer to understand
arbitrary early repetitions: every such repetition is one of the listed
\(5\)- or \(7\)-edges, while the omitted \(B_0/B_3\) repetition by \(5\)
belongs exactly to the \(B_3\) bridge case.
