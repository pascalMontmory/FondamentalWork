# Transversality Repetition Constraints

This note records the first multi-block obstruction for the fixed-\(m\)
double sieve.

The key point is elementary but useful: if the same prime certifies two
different blocks in the same layer, then the two block indices are tied by a
linear congruence.  Thus the residue classes are not arbitrary; each prime
creates at most two mirror pairings on the \(q\)-line.

Throughout, fix \(m\), and let
\[
  a_q=3q+1,\qquad b_q=3q+2.
\]

## 1. Same-prime repetition for A0

For the A0 layer, the certified coordinate \(t_0(q)\) is either \(a_q\) or
\(b_q\), depending on the parity orientation.

Suppose a prime \(p\in\mathcal P_0(m)\) certifies two blocks \(q\) and \(r\)
in the A0 layer:
\[
  t_0(q)^2\equiv-9m^2\pmod p,
\]
\[
  t_0(r)^2\equiv-9m^2\pmod p.
\]
Then
\[
  t_0(q)^2\equiv t_0(r)^2\pmod p,
\]
so
\[
  t_0(q)\equiv\pm t_0(r)\pmod p.
\]

The plus sign gives
\[
  q\equiv r\pmod p,
\]
because both \(t_0(q)\) and \(t_0(r)\) have slope \(3\) in \(q\).

The minus sign gives a mirror relation.  If
\[
  t_0(q)=3q+\alpha,
  \qquad
  t_0(r)=3r+\beta,
  \qquad
  \alpha,\beta\in\{1,2\},
\]
then
\[
  3q+\alpha\equiv-(3r+\beta)\pmod p,
\]
or
\[
  q+r\equiv-\frac{\alpha+\beta}{3}\pmod p.
\]

Thus same-prime A0 repetition is constrained by either:
\[
  q\equiv r\pmod p,
\]
or by one of the mirror classes
\[
  q+r\equiv-\frac{2}{3},\quad -1,\quad -\frac{4}{3}\pmod p,
\]
depending on \((\alpha,\beta)\).

## 2. Same-prime repetition for A1

For the A1 layer, the same argument applies.  If
\[
  t_1(q)^2\equiv-9m^2-1\pmod p,
\]
and
\[
  t_1(r)^2\equiv-9m^2-1\pmod p,
\]
then
\[
  t_1(q)\equiv\pm t_1(r)\pmod p.
\]

Again, the plus sign gives
\[
  q\equiv r\pmod p,
\]
and the minus sign gives
\[
  q+r\equiv-\frac{\alpha+\beta}{3}\pmod p,
\]
where
\[
  t_1(q)=3q+\alpha,\qquad t_1(r)=3r+\beta,\qquad
  \alpha,\beta\in\{1,2\}.
\]

Thus A1 repetition has exactly the same mirror structure, but only for primes
in
\[
  \mathcal P_1(m).
\]

## 3. Consequence for dense covers

Let \(I\) be the interval of coprime complete block indices.

If a fixed prime \(p\) certifies many blocks in one layer, then those blocks
must lie in at most two root classes modulo \(p\).  Equivalently, the set of
indices certified by \(p\) has strong additive structure:

- all pairs within the same root class satisfy \(q\equiv r\pmod p\);
- pairs from opposite root classes satisfy a fixed mirror relation
  \[
    q+r\equiv c_p\pmod p.
  \]

Therefore a dense cover of \(I\) by many primes cannot be arbitrary.  It is a
union of small arithmetic progressions and mirrored progressions.

## 4. Transversality requirement

A full counterexample requires both layers to cover every
\[
  q\in\mathcal Q_{\rm cop}(m).
\]
Thus every \(q\) must lie simultaneously in:

1. an A0 progression or mirror class for some \(p_0\in\mathcal P_0(m)\);
2. an A1 progression or mirror class for some \(p_1\in\mathcal P_1(m)\).

Because A0 and A1 use different quadratic right-hand sides,
\[
  -9m^2
  \qquad\text{and}\qquad
  -9m^2-1,
\]
the same-prime mirror structures are transverse except on the bridge locus
already removed.

This motivates the following exact target.

## 5. Repetition transversality lemma

For fixed \(m\), the coprime block interval cannot be covered by two layers
of mirror-progressions arising from:
\[
  t_0(q)^2\equiv-9m^2\pmod p,
\]
and
\[
  t_1(q)^2\equiv-9m^2-1\pmod p,
\]
after bridge classes are removed.

Equivalently, if every coprime complete block is covered in both layers,
then the resulting mirror-progressions must satisfy an overdetermined system
of additive congruences in the block indices.

This is not yet a proof, but it is a sharper obstruction than the pair-density
or product formulation: it exposes rigid repetition patterns inside each
prime fiber.
