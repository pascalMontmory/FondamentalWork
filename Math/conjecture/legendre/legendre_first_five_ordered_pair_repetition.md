# First Five Ordered Pair Repetition

This note extends the first-four ordered-pair capacity theorem to the first
five A-blocks
\[
  B_0,\ B_1,\ B_2,\ B_3,\ B_4.
\]

The result is no longer total nonrepetition.  There is exactly one possible
ordered-pair repetition, and it is completely explicit.

## Coordinate Sequences

For the first five blocks, the two coordinate sequences are
\[
  E_5=(2,4,8,10,14),
\]
and
\[
  O_5=(1,5,7,11,13).
\]

If \(m\) is even, then A1 uses \(E_5\) and A0 uses \(O_5\).  If \(m\) is
odd, then A1 uses \(O_5\) and A0 uses \(E_5\).

For a same-layer repetition between two block indices \(i<j\), a prime
\(p\ge5\) must divide either the coordinate difference or the coordinate
sum.

## Repetitions Inside \(E_5\)

The possible same-layer repetitions inside \(E_5\) are:
\[
\begin{array}{c|c}
  \text{block pair} & \text{prime}\\
  \hline
  (B_0,B_2) & 5\\
  (B_1,B_3) & 7\\
  (B_1,B_4) & 5\\
  (B_2,B_4) & 11.
\end{array}
\]

Indeed, these come respectively from
\[
  2+8=10,\qquad 4+10=14,\qquad 14-4=10,\qquad 8+14=22.
\]
All other differences and sums have no prime divisor \(\ge5\) compatible
with a repetition.

## Repetitions Inside \(O_5\)

The possible same-layer repetitions inside \(O_5\) are:
\[
\begin{array}{c|c}
  \text{block pair} & \text{prime}\\
  \hline
  (B_0,B_3) & 5\\
  (B_0,B_4) & 7\\
  (B_2,B_4) & 5.
\end{array}
\]

These come from
\[
  11-1=10,\qquad 1+13=14,\qquad 7+13=20.
\]
All other differences and sums have no prime divisor \(\ge5\) compatible
with a repetition.

## Ordered-Pair Repetition Classification

An ordered pair \((p_0,p_1)\) can repeat only if the same block pair appears
in the A0 repetition list and in the A1 repetition list.

The only common block pair in the two lists above is
\[
  (B_2,B_4).
\]

If \(m\) is odd, then A0 uses \(E_5\), so the A0 repetition on
\((B_2,B_4)\) would use
\[
  p_0=11.
\]
This is impossible because A0 primes must satisfy
\[
  p_0\equiv1\pmod4.
\]

If \(m\) is even, then A0 uses \(O_5\) and A1 uses \(E_5\).  The only
possible ordered-pair repetition is therefore
\[
  (B_2,B_4)
  \quad\text{with}\quad
  (p_0,p_1)=(5,11).
\]

## Congruence Conditions for the Exceptional Repetition

Assume \(m\) is even.

On the A0 side, \(O_5\) gives the repeated coordinates
\[
  7,\ 13.
\]
The prime \(5\) certifies the A0 repetition exactly when
\[
  9m^2+7^2\equiv0\pmod5.
\]
Since \(9\equiv-1\pmod5\) and \(7^2\equiv4\pmod5\), this is
\[
  m^2\equiv4\pmod5.
\]

On the A1 side, \(E_5\) gives the repeated coordinates
\[
  8,\ 14.
\]
The prime \(11\) certifies the A1 repetition exactly when
\[
  9m^2+8^2+1\equiv0\pmod{11}.
\]
Since \(8^2+1=65\equiv-1\pmod{11}\), this is
\[
  9m^2\equiv1\pmod{11},
\]
or
\[
  m^2\equiv5\pmod{11}.
\]

Thus the only possible repeated ordered pair among the first five coprime
blocks is:
\[
  m\equiv0\pmod2,\qquad
  m^2\equiv4\pmod5,\qquad
  m^2\equiv5\pmod{11},
\]
with
\[
  (p_0,p_1)=(5,11)
\]
repeating on
\[
  (B_2,B_4).
\]

## Consequence

Outside this explicit exceptional gate, every ordered pair covering a
coprime block among
\[
  B_0,\dots,B_4
\]
is distinct.

Inside the exceptional gate, the only possible collision is the single
collision
\[
  (B_2,B_4)\quad\text{by}\quad(p_0,p_1)=(5,11).
\]

This is a sharper local capacity theorem: the first five coprime blocks
force either five distinct ordered pairs, or four distinct ordered pairs plus
one completely explicit \((5,11)\) collision.
