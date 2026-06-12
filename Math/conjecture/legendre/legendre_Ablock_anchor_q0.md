# A-Block Anchor at q=0

This note proves that the first complete A-block is always present and gives
an exact boundary system that every remaining counterexample must satisfy.

It is a proof-level reduction: before any global covering of blocks is
possible, the block
\[
  q=0,\qquad \{3q+1,3q+2\}=\{1,2\}
\]
must already be covered in both A-layers.

## Lemma

For every \(m\ge1\), the block \(q=0\) is complete and coprime.

### Proof

Write
\[
  a_0=1,\qquad b_0=2.
\]

If \(m\) is odd, then \(a_0\equiv m\pmod2\), so
\[
  t_1(0)=1,\qquad t_0(0)=2.
\]
The completeness inequalities are
\[
  t_0(0)^2=4\le6m,
  \qquad
  t_1(0)^2+1=2\le6m.
\]
The coprime condition is
\[
  \gcd(t_1(0),9m^2+1)=\gcd(1,9m^2+1)=1.
\]

If \(m\) is even, then \(a_0\not\equiv m\pmod2\), so
\[
  t_1(0)=2,\qquad t_0(0)=1.
\]
The completeness inequalities are
\[
  t_0(0)^2=1\le6m,
  \qquad
  t_1(0)^2+1=5\le6m.
\]
The coprime condition is
\[
  \gcd(t_1(0),9m^2+1)=\gcd(2,9m^2+1)=1,
\]
because \(9m^2+1\) is odd.  Hence \(q=0\in\mathcal Q_{\rm cop}(m)\) for all
\(m\ge1\).  \(\square\)

## Boundary System Forced by a Counterexample

Since \(q=0\) is always a complete coprime block, any counterexample must
cover this block in both layers.

### Odd \(m\)

If \(m\) is odd, then
\[
  G_0=9m^2+4,\qquad U_0=9m^2+2.
\]
Thus a counterexample must have distinct primes
\[
  p_0,p_1\le3m
\]
such that
\[
  p_0\equiv1\pmod4,\qquad p_0\nmid3m,
\]
\[
  p_0\mid9m^2+4,
\]
and
\[
  p_1\ge5,\qquad p_1\ne p_0,\qquad p_1\mid9m^2+2.
\]

Equivalently,
\[
  (3m)^2\equiv-4\pmod {p_0},
  \qquad
  (3m)^2\equiv-2\pmod {p_1}.
\]
Thus
\[
  \left(\frac{-1}{p_0}\right)=1,
  \qquad
  \left(\frac{-2}{p_1}\right)=1.
\]

### Even \(m\)

If \(m\) is even, then
\[
  G_0=9m^2+1,\qquad U_0=9m^2+5.
\]
Thus a counterexample must have distinct primes
\[
  p_0,p_1\le3m
\]
such that
\[
  p_0\equiv1\pmod4,\qquad p_0\nmid3m,
\]
\[
  p_0\mid9m^2+1,
\]
and
\[
  p_1\ge5,\qquad p_1\ne p_0,\qquad p_1\mid9m^2+5.
\]

Equivalently,
\[
  (3m)^2\equiv-1\pmod {p_0},
  \qquad
  (3m)^2\equiv-5\pmod {p_1}.
\]
Thus
\[
  \left(\frac{-1}{p_0}\right)=1,
  \qquad
  \left(\frac{-5}{p_1}\right)=1.
\]

## Consequence

The global A-block non-cover lemma does not begin with an arbitrary block.
It has a fixed anchor:
\[
  q=0\in\mathcal Q_{\rm cop}(m)
  \qquad\text{for every }m\ge1.
\]

Therefore a complete counterexample must first pass one of the two explicit
boundary systems:
\[
  m\ \text{odd}:
  \quad
  9m^2+4\ \text{and}\ 9m^2+2
  \text{ have eligible small prime certificates},
\]
or
\[
  m\ \text{even}:
  \quad
  9m^2+1\ \text{and}\ 9m^2+5
  \text{ have eligible small prime certificates}.
\]

If either boundary system fails, the A-channel already produces a prime from
the first block.

The next equation-level attack is to combine this fixed anchor with the
collision equations for \(q=0\) and a second block \(r\).  In that case the
repetition hyperplanes become explicit divisibility conditions in \(r\):
\[
  r,\quad 3r\pm1,\quad 3r+2,\quad 3r+4,\quad r+1.
\]
