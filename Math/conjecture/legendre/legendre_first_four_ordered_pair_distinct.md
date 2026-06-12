# First Four Ordered Pairs Are Distinct

This note proves a stronger first-four-block capacity fact.

Among the first four A-blocks
\[
  B_0=\{1,2\},\quad B_1=\{4,5\},\quad
  B_2=\{7,8\},\quad B_3=\{10,11\},
\]
no ordered pair of certificate primes \((p_0,p_1)\) can cover two distinct
coprime blocks.

This is stronger than saying that one layer has few repetitions.  Some
same-layer repetitions are possible, but they occur in different block pairs
in A0 and A1, so a full ordered pair never repeats.

## Coordinate Sequences

The two possible coordinate sequences are
\[
  E=(2,4,8,10)
\]
and
\[
  O=(1,5,7,11).
\]

If \(m\) is even, then
\[
  (t_1(0),t_1(1),t_1(2),t_1(3))=E,
  \qquad
  (t_0(0),t_0(1),t_0(2),t_0(3))=O.
\]
If \(m\) is odd, the two sequences are interchanged:
\[
  (t_1(0),t_1(1),t_1(2),t_1(3))=O,
  \qquad
  (t_0(0),t_0(1),t_0(2),t_0(3))=E.
\]

For a prime \(p\ge5\) to certify the same layer at two block indices \(i<j\),
it must divide either the coordinate difference or the coordinate sum.

## Repetitions Inside E

For
\[
  E=(2,4,8,10),
\]
the unordered pairs give:
\[
\begin{array}{c|c|c|c}
  (i,j) & |E_j-E_i| & E_i+E_j & \text{prime candidates }p\ge5\\
  \hline
  (0,1) & 2 & 6 & \varnothing\\
  (0,2) & 6 & 10 & \{5\}\\
  (0,3) & 8 & 12 & \varnothing\\
  (1,2) & 4 & 12 & \varnothing\\
  (1,3) & 6 & 14 & \{7\}\\
  (2,3) & 2 & 18 & \varnothing.
\end{array}
\]

Thus same-layer repetition inside \(E\) can only occur on block pairs
\[
  (B_0,B_2)\quad\text{by }5,
  \qquad
  (B_1,B_3)\quad\text{by }7.
\]

## Repetitions Inside O

For
\[
  O=(1,5,7,11),
\]
the unordered pairs give:
\[
\begin{array}{c|c|c|c}
  (i,j) & |O_j-O_i| & O_i+O_j & \text{prime candidates }p\ge5\\
  \hline
  (0,1) & 4 & 6 & \varnothing\\
  (0,2) & 6 & 8 & \varnothing\\
  (0,3) & 10 & 12 & \{5\}\\
  (1,2) & 2 & 12 & \varnothing\\
  (1,3) & 6 & 16 & \varnothing\\
  (2,3) & 4 & 18 & \varnothing.
\end{array}
\]

Thus same-layer repetition inside \(O\) can only occur on
\[
  (B_0,B_3)\quad\text{by }5.
\]

## Ordered Pair Nonrepetition

Suppose an ordered pair \((p_0,p_1)\) covers two distinct coprime blocks among
\[
  B_0,B_1,B_2,B_3.
\]
Then \(p_0\) must be a same-layer repetition prime in the A0 coordinate
sequence, and \(p_1\) must be a same-layer repetition prime in the A1
coordinate sequence for the same block pair.

If \(m\) is even, A0 uses \(O\) and A1 uses \(E\).  The only possible A0
repetition pair is \((B_0,B_3)\), while the possible A1 repetition pairs are
\[
  (B_0,B_2),\quad (B_1,B_3).
\]
There is no common block pair.

If \(m\) is odd, A0 uses \(E\) and A1 uses \(O\).  The possible A0 repetition
pairs are
\[
  (B_0,B_2),\quad (B_1,B_3),
\]
while the only possible A1 repetition pair is \((B_0,B_3)\).  Again, there
is no common block pair.

Therefore no ordered pair \((p_0,p_1)\) can cover two distinct coprime blocks
among the first four blocks.

## Consequence

Whenever the first four blocks are complete and coprime, a counterexample
must use four distinct ordered pairs:
\[
  (p_0(0),p_1(0)),\quad
  (p_0(1),p_1(1)),\quad
  (p_0(2),p_1(2)),\quad
  (p_0(3),p_1(3)).
\]

When one of the first four blocks is a bridge block, this statement applies
to the coprime subcollection.  The bridge block must be handled by the
separate bridge equations.

This is a local capacity theorem: the first four coprime blocks cannot share
ordered pair labels at all.
