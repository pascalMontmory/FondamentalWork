# Fixed-\(m\) Sieve Decomposition

This note rewrites the coprime A-block obstruction for a fixed integer \(m\)
as an intersection of two sifted sets.

The previous pair-cover formulation said that every coprime complete block
must be certified by an ordered pair \((p_0,p_1)\).  For a fixed \(m\), it is
more useful to separate the two requirements:

- the A0 member of the block is composite;
- the A1 member of the block is composite.

Thus a counterexample must put every coprime complete block in
\[
  S_0(m)\cap S_1(m).
\]

## 1. Oriented block coordinates

Let
\[
  a=3q+1,\qquad b=3q+2.
\]
Define the A1 coordinate
\[
  t_1(q)=
  \begin{cases}
  a,&a\equiv m\pmod2,\\
  b,&a\not\equiv m\pmod2,
  \end{cases}
\]
and the A0 coordinate
\[
  t_0(q)=
  \begin{cases}
  b,&a\equiv m\pmod2,\\
  a,&a\not\equiv m\pmod2.
  \end{cases}
\]

The two surviving A-candidates are
\[
  G_q=9m^2+t_0(q)^2,
\]
and
\[
  U_q=9m^2+t_1(q)^2+1.
\]

Let
\[
  \mathcal Q_{\rm cop}(m)
\]
be the set of \(q\) for which the block is complete and coprime:
\[
  \gcd(t_1(q),9m^2+1)=1.
\]

## 2. A0 sieve set

Define
\[
  S_0(m)=
  \left\{
  q\in\mathcal Q_{\rm cop}(m):
  G_q\ \text{is composite}
  \right\}.
\]
By the small-prime certificate principle,
\[
  q\in S_0(m)
\]
if and only if there exists a prime
\[
  p\le3m
\]
such that
\[
  p\mid G_q.
\]
Because A0 is primitive Gaussian, every such prime satisfies
\[
  p\equiv1\pmod4,\qquad p\nmid3m.
\]

Therefore
\[
  S_0(m)
  =
  \mathcal Q_{\rm cop}(m)
  \cap
  \bigcup_{\substack{p\le3m\\p\equiv1\pmod4\\p\nmid3m}}
  R_{0,p}(m),
\]
where
\[
  R_{0,p}(m)=
  \{q:t_0(q)^2\equiv-9m^2\pmod p\}.
\]

For every admissible \(p\), the set \(R_{0,p}(m)\) consists of exactly two
classes modulo \(p\).

## 3. A1 sieve set

Define
\[
  S_1(m)=
  \left\{
  q\in\mathcal Q_{\rm cop}(m):
  U_q\ \text{is composite}
  \right\}.
\]
Again by the small-prime certificate principle,
\[
  q\in S_1(m)
\]
if and only if there exists a prime
\[
  p\le3m
\]
such that
\[
  p\mid U_q.
\]
For coprime blocks, the degenerate A1 case is excluded:
\[
  p\nmid9m^2+1.
\]
Thus
\[
  S_1(m)
  =
  \mathcal Q_{\rm cop}(m)
  \cap
  \bigcup_{\substack{p\le3m\\p\nmid9m^2+1\\
  \left(\frac{-9m^2-1}{p}\right)=1}}
  R_{1,p}(m),
\]
where
\[
  R_{1,p}(m)=
  \{q:t_1(q)^2\equiv-9m^2-1\pmod p\}.
\]

For each available A1 prime \(p\), the set \(R_{1,p}(m)\) consists of exactly
two classes modulo \(p\).  If
\[
  \left(\frac{-9m^2-1}{p}\right)=-1
\]
or
\[
  p\mid9m^2+1,
\]
then \(R_{1,p}(m)\) is empty on coprime blocks.

## 4. Exact fixed-\(m\) obstruction

For a fixed \(m\), the combined A-channel fails on all coprime complete
blocks if and only if
\[
  \boxed{
  \mathcal Q_{\rm cop}(m)\subseteq S_0(m)\cap S_1(m).
  }
\]

Equivalently, a prime is produced in the combined A-channel if and only if
there exists
\[
  q\in\mathcal Q_{\rm cop}(m)
\]
such that
\[
  q\notin S_0(m)
  \quad\text{or}\quad
  q\notin S_1(m).
\]

This is stronger and cleaner than the pair-union formulation.  The pair cover
is recovered by expanding
\[
  S_0(m)\cap S_1(m)
\]
as intersections of one A0 residue class and one A1 residue class.

## 5. Why this is the right closure target

The naive pair-density route failed because it treated all ordered pairs as
independent cover pieces.  The fixed-\(m\) decomposition keeps the two sieve
layers separate:

\[
  S_0(m)=\text{Gaussian layer},
  \qquad
  S_1(m)=\text{unit-lift layer}.
\]

To close the combined A-channel it is enough to prove the fixed-\(m\) sieve
lemma:

> For every \(m\ge1\), the coprime complete block set
> \(\mathcal Q_{\rm cop}(m)\) is not contained in \(S_0(m)\cap S_1(m)\).

Equivalently:

> For every \(m\ge1\), there exists a complete coprime block for which either
> \(G_q\) is prime or \(U_q\) is prime.

This would close the entire \(3\nmid t\) combined A-channel.  If the lemma is
false, then the remaining obstruction is an explicit fixed-\(m\) double sieve:
\[
  \mathcal Q_{\rm cop}(m)\subseteq S_0(m)\cap S_1(m).
\]

## 6. Next exact target

The next proof step should attack the inclusion
\[
  \mathcal Q_{\rm cop}(m)\subseteq S_0(m)\cap S_1(m)
\]
directly.

The natural route is a two-layer large sieve on the same interval of \(q\):

1. estimate how many \(q\) can survive outside the Gaussian layer \(S_0(m)\);
2. prove that the A1 layer \(S_1(m)\) cannot cover all of those survivors,
   using the fixed-\(m\) condition
   \[
     \left(\frac{-9m^2-1}{p}\right)=1.
   \]

This is the current exact bottleneck toward closure.
