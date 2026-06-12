# Anchor Pair Nonrepetition

This note proves that the ordered pair of certificate primes covering the
fixed anchor block \(q=0\) cannot cover any of the next three complete blocks
\[
  q=1,\quad q=2,\quad q=3.
\]

This is an exact equation-level consequence of the collision equations.

## Setup

For each block \(q\), write
\[
  t_0(q)=3q+\alpha_q,\qquad t_1(q)=3q+\beta_q,
\]
with
\[
  \{\alpha_q,\beta_q\}=\{1,2\}.
\]

Let \((p_0,p_1)\) be the ordered pair covering the anchor block \(q=0\).
Thus
\[
  p_0\mid 9m^2+t_0(0)^2,
  \qquad
  p_1\mid 9m^2+t_1(0)^2+1,
\]
with
\[
  p_0,p_1\ge5,\qquad p_0\ne p_1.
\]

Assume, for contradiction, that the same ordered pair also covers a block
\[
  r\in\{1,2,3\}.
\]

Then the collision equations force
\[
  p_0\mid
  \bigl(3r+\alpha_r-\alpha_0\bigr)
  \bigl(3r+\alpha_r+\alpha_0\bigr),
\]
and
\[
  p_1\mid
  \bigl(3r+\beta_r-\beta_0\bigr)
  \bigl(3r+\beta_r+\beta_0\bigr).
\]
Signs are irrelevant because only divisibility is used.

## Odd \(m\)

If \(m\) is odd, then
\[
  \alpha_0=2,\qquad \beta_0=1.
\]

For even \(r\), the orientation is the same as \(q=0\), so
\[
  \alpha_r=2,\qquad \beta_r=1.
\]
Hence
\[
  p_0\mid (3r)(3r+4),
  \qquad
  p_1\mid (3r)(3r+2).
\]

For odd \(r\), the orientation is reversed, so
\[
  \alpha_r=1,\qquad \beta_r=2.
\]
Hence
\[
  p_0\mid (3r-1)(3r+3),
  \qquad
  p_1\mid (3r+1)(3r+3).
\]

Now check \(r=1,2,3\) by exact divisibility:

\[
\begin{array}{c|c|c}
 r & p_0\text{ divisor candidates} & p_1\text{ divisor candidates}\\
 \hline
 1 & 2,\ 6 & 4,\ 6\\
 2 & 6,\ 10 & 6,\ 8\\
 3 & 8,\ 12 & 10,\ 12
\end{array}
\]

Since \(p_0,p_1\ge5\), the only possible prime candidate in the table is
\[
  5.
\]
But no row contains \(5\) in both columns.  Therefore the same ordered pair
\((p_0,p_1)\) cannot cover \(q=0\) and any \(r=1,2,3\) when \(m\) is odd.

## Even \(m\)

If \(m\) is even, then
\[
  \alpha_0=1,\qquad \beta_0=2.
\]

For even \(r\), the orientation is the same as \(q=0\), so
\[
  \alpha_r=1,\qquad \beta_r=2.
\]
Hence
\[
  p_0\mid (3r)(3r+2),
  \qquad
  p_1\mid (3r)(3r+4).
\]

For odd \(r\), the orientation is reversed, so
\[
  \alpha_r=2,\qquad \beta_r=1.
\]
Hence
\[
  p_0\mid (3r+1)(3r+3),
  \qquad
  p_1\mid (3r-1)(3r+3).
\]

For \(r=1,2,3\), this gives
\[
\begin{array}{c|c|c}
 r & p_0\text{ divisor candidates} & p_1\text{ divisor candidates}\\
 \hline
 1 & 4,\ 6 & 2,\ 6\\
 2 & 6,\ 8 & 6,\ 10\\
 3 & 10,\ 12 & 8,\ 12
\end{array}
\]

Again, the only possible prime candidate \(\ge5\) is \(5\), and no row
contains \(5\) in both columns.  Therefore the same ordered pair
\((p_0,p_1)\) cannot cover \(q=0\) and any \(r=1,2,3\) when \(m\) is even.

## Conclusion

For every \(m\ge1\), the ordered pair of certificate primes covering the
anchor block \(q=0\) is a one-shot pair on the first four blocks:
\[
  (p_0(0),p_1(0))\ne(p_0(r),p_1(r))
  \qquad
  (r=1,2,3).
\]

This does not close the A-block non-cover lemma, but it gives a fixed
capacity cost: any counterexample that reaches the first four complete
coprime blocks must use a fresh ordered pair for the anchor relative to the
next three blocks.  The first block cannot be absorbed by an early repeated
pair.
