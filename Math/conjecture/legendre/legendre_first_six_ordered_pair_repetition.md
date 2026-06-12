# First Six Ordered Pair Repetition

This note extends the ordered-pair capacity classification to the first six
A-blocks
\[
  B_0,\dots,B_5.
\]

The result is still finite and exact: among the first six coprime complete
blocks, ordered-pair repetitions can occur only in two explicitly listed
ways.  A previously tempting odd \((B_1,B_5)\) gate dies because it would
force a nonsquare class modulo \(11\).

## Coordinate Sequences

For \(B_0,\dots,B_5\), the two coordinate sequences are
\[
  E_6=(2,4,8,10,14,16),
\]
and
\[
  O_6=(1,5,7,11,13,17).
\]

If \(m\) is even, A1 uses \(E_6\) and A0 uses \(O_6\).  If \(m\) is odd,
A1 uses \(O_6\) and A0 uses \(E_6\).

For same-layer repetition between two coordinates, a prime \(p\ge5\) must
divide their difference or their sum.

## Repetition Tables

Inside \(E_6\), the possible same-layer repetitions are:
\[
\begin{array}{c|c}
  \text{block pair} & \text{prime}\\
  \hline
  (B_0,B_2) & 5\\
  (B_0,B_5) & 7\\
  (B_1,B_3) & 7\\
  (B_1,B_4) & 5\\
  (B_1,B_5) & 5\\
  (B_2,B_4) & 11\\
  (B_3,B_5) & 13\\
  (B_4,B_5) & 5.
\end{array}
\]

Inside \(O_6\), the possible same-layer repetitions are:
\[
\begin{array}{c|c}
  \text{block pair} & \text{prime}\\
  \hline
  (B_0,B_3) & 5\\
  (B_0,B_4) & 7\\
  (B_1,B_5) & 11\\
  (B_2,B_4) & 5\\
  (B_2,B_5) & 5\\
  (B_3,B_5) & 7\\
  (B_4,B_5) & 5.
\end{array}
\]

Thus the common block pairs between the two same-layer repetition graphs are
\[
  (B_1,B_5),\quad (B_2,B_4),\quad (B_3,B_5),\quad (B_4,B_5).
\]

## Ordered-Pair Repetition Classification

### Even \(m\)

If \(m\) is even, then A0 uses \(O_6\) and A1 uses \(E_6\).

On the common pairs:

- \((B_1,B_5)\) would use \(p_0=11\) in A0, impossible since
  \(11\not\equiv1\pmod4\).
- \((B_2,B_4)\) uses
  \[
    (p_0,p_1)=(5,11),
  \]
  and remains possible.
- \((B_3,B_5)\) would use \(p_0=7\) in A0, impossible since
  \(7\not\equiv1\pmod4\).
- \((B_4,B_5)\) would use
  \[
    (p_0,p_1)=(5,5),
  \]
  impossible because the two primes in a coprime block must be distinct.

Therefore for even \(m\), the only possible ordered-pair repetition among
the first six coprime blocks is
\[
  (B_2,B_4)\quad\text{by}\quad(p_0,p_1)=(5,11).
\]
It requires
\[
  m^2\equiv4\pmod5,\qquad m^2\equiv5\pmod{11}.
\]

### Odd \(m\)

If \(m\) is odd, then A0 uses \(E_6\) and A1 uses \(O_6\).

On the common pairs:

- \((B_1,B_5)\) uses
  \[
    (p_0,p_1)=(5,11),
  \]
  but it is impossible after imposing the value congruences below.
- \((B_2,B_4)\) would use \(p_0=11\) in A0, impossible since
  \(11\not\equiv1\pmod4\).
- \((B_3,B_5)\) uses
  \[
    (p_0,p_1)=(13,7),
  \]
  and remains possible.
- \((B_4,B_5)\) would use
  \[
    (p_0,p_1)=(5,5),
  \]
  impossible because \(p_0\ne p_1\).

Therefore for odd \(m\), the only possible ordered-pair repetition among
the first six coprime blocks is
\[
  (B_3,B_5)\quad\text{by}\quad(p_0,p_1)=(13,7).
\]

Indeed, the tempting \((B_1,B_5)\) gate would require
\[
  9m^2+4^2\equiv0\pmod5,
  \qquad
  9m^2+5^2+1\equiv0\pmod{11},
\]
hence
\[
  m^2\equiv1\pmod5,
  \qquad
  m^2\equiv2\pmod{11}.
\]
But the square classes modulo \(11\) are
\[
  0,1,3,4,5,9,
\]
so \(2\) is not a square modulo \(11\).  Hence this gate has no integer
solution \(m\).

The surviving \((B_3,B_5)\) gate requires
\[
  9m^2+10^2\equiv0\pmod{13},
  \qquad
  9m^2+11^2+1\equiv0\pmod7,
\]
hence
\[
  m^2\equiv-1\pmod{13},
  \qquad
  m^2\equiv2\pmod7.
\]

## Consequence

Among the first six coprime complete blocks, ordered-pair repetitions are
confined to the following explicit gates:
\[
\begin{array}{c|c|c|c}
  \text{parity of }m & \text{block pair} & (p_0,p_1) & \text{conditions}\\
  \hline
  \text{even} & (B_2,B_4) & (5,11) &
  m^2\equiv4\pmod5,\ m^2\equiv5\pmod{11}\\
  \text{odd} & (B_3,B_5) & (13,7) &
  m^2\equiv-1\pmod{13},\ m^2\equiv2\pmod7.
\end{array}
\]

Outside these gates, the first six coprime complete blocks require six
distinct ordered pairs.

Inside the gates, repetitions are no longer free: every repeated ordered pair
is named, its block pair is named, and its congruence class in \(m\) is
explicit.
