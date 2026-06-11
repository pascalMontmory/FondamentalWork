# A1 Local Filter

This note computes the exact local filter imposed by the A1 part of the
coprime pair incidence.

The A1 certificate prime \(p\) must satisfy
\[
  \left(\frac{-9m^2-1}{p}\right)=1
\]
and
\[
  p\nmid9m^2+1.
\]
Equivalently, \(-9m^2-1\) must be a nonzero square modulo \(p\).

We count exactly how many residue classes \(m\bmod p\) satisfy this.

## 1. Character sum

Let
\[
  p\ge5
\]
be prime, and let \(\chi\) be the quadratic character modulo \(p\).
Consider
\[
  f(m)=-9m^2-1.
\]
Its discriminant is
\[
  \Delta=-4(-9)(-1)=-36,
\]
which is nonzero modulo \(p\).

For a nondegenerate quadratic polynomial
\[
  Am^2+Bm+C
\]
over \(\mathbb F_p\), one has
\[
  \sum_{m\bmod p}\chi(Am^2+Bm+C)=-\chi(A).
\]
Here
\[
  A=-9,
\]
so
\[
  \chi(A)=\chi(-9)=\chi(-1).
\]
Therefore
\[
  \boxed{
  \sum_{m\bmod p}\chi(-9m^2-1)=-\chi(-1).
  }
\]

## 2. Zero classes

The zero condition is
\[
  -9m^2-1\equiv0\pmod p,
\]
or
\[
  (3m)^2\equiv-1\pmod p.
\]
Hence the number of zero classes is
\[
  Z_p=
  \begin{cases}
  2,&p\equiv1\pmod4,\\
  0,&p\equiv3\pmod4.
  \end{cases}
\]
Equivalently,
\[
  Z_p=1+\chi(-1).
\]

These zero classes are excluded from coprime A1 certificates, because they
are exactly the classes with
\[
  p\mid9m^2+1.
\]

## 3. Number of admissible A1 classes

Let
\[
  R_p=
  \#\left\{m\bmod p:
  \chi(-9m^2-1)=1
  \right\}.
\]
Since zero classes contribute neither to residues nor nonresidues,
\[
  R_p=\frac{p-Z_p-\chi(-1)}{2}.
\]
Thus:

\[
\boxed{
R_p=
\begin{cases}
\dfrac{p-3}{2},&p\equiv1\pmod4,\\[2mm]
\dfrac{p+1}{2},&p\equiv3\pmod4.
\end{cases}}
\]

So the A1 filter is slightly stricter for primes \(p\equiv1\pmod4\), because
two bridge classes are removed.

## 4. Consequence for pair incidences

In the coprime pair cover, an ordered pair
\[
  (p_0,p_1)
\]
can participate only if
\[
  p_0\equiv1\pmod4,\qquad p_0\nmid3m,
\]
and
\[
  m\bmod p_1
\]
belongs to the A1-admissible set of size \(R_{p_1}\) above.

For each admissible \(m\bmod p_1\), the A1 equation has exactly two nonzero
roots:
\[
  t_1\equiv\pm s_1\pmod{p_1},
  \qquad
  s_1^2\equiv-9m^2-1.
\]

Therefore the pair incidence has the exact local size:

- A0 contributes two roots for every nonzero \(m\bmod p_0\), but only for
  primes \(p_0\equiv1\pmod4\);
- A1 contributes two roots only for \(R_{p_1}\) classes of \(m\bmod p_1\).

This is a necessary local filter on any dense coprime A-block cover.

## 5. Current exact bottleneck

The remaining problem is to combine this \(m\)-filter with the \(q\)-interval.

For a fixed \(m\), primes \(p_1\) with
\[
  \chi(-9m^2-1)=-1
\]
are entirely unavailable as A1 certificate primes on coprime blocks.

Thus a dense pair-cover would need many primes \(p_1\le3m\) for which
\[
  -9m^2-1
\]
is a nonzero quadratic residue.

The exact target is now:

> Prove that the available A1 primes, after the local filter above and after
> bridge classes are removed, cannot pair with A0 primes to cover every
> coprime complete A-block.

This is still a precise obstruction, not yet a proof of Legendre.
