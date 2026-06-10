# Progress Log

## 2026-06-10

### Repository setup

Created a local research repository for conjecture work.

### Short-list

Recorded a short-list of plausible conjecture targets:

- Casas-Alvero conjecture.
- Legendre's conjecture via residue covers and Gaussian integers.
- Erdős-Ulam rational distance problem.
- Seymour second-neighborhood conjecture.

Selected Casas-Alvero as the main algebraic thread because it has a concise
formal statement and derivative conditions that can be turned into exact
equations.

### Casas-Alvero centroid obstruction

Proved the centroid obstruction:

If \(f\) is a Casas-Alvero polynomial and
\[
  f(x)=c\prod_j(x-a_j)^{m_j},
\]
then the weighted centroid
\[
  \frac{1}{d}\sum_jm_ja_j
\]
is one of the roots of \(f\). Consequently, in any nontrivial counterexample,
some root lies in the convex hull of the other distinct roots.

### Three-root exclusion

Gave a self-contained proof that a nontrivial Casas-Alvero polynomial cannot
have exactly three distinct roots. Literature check later showed that this is
subsumed by the stronger Laterveer-Ounaies theorem requiring at least five
distinct roots.

### Literature correction

Checked Laterveer-Ounaies, *Constraints on hypothetical counterexamples to the
Casas-Alvero conjecture*, arXiv:1204.0450. Their result: any nontrivial
counterexample must have at least five distinct roots. Updated the notes so
the current frontier starts at five roots.

### Five-root frontier

Established the centered normal form for the first live case:

\[
  f(x)=x^{m_0}\prod_{i=1}^4(x-a_i)^{m_i},
  \qquad
  \sum_{i=1}^4m_ia_i=0.
\]

Introduced power sums
\[
  P_k=\sum_{i=1}^4m_ia_i^k
\]
and normalized top derivative polynomials \(Q_k\).

### Real-root gap obstruction

For a real-rooted centered candidate with outer radius \(R\), proved that a
nonzero root must satisfy
\[
  |a|\le \frac{R}{\sqrt{d-1}}.
\]

### Cubic obstruction

If \(a\) is selected by \(Q_2\), then a root \(b\) selected by \(Q_3\) satisfies
\[
  |b(b^2-3a^2)|\le \frac{2R^3}{(d-1)(d-2)}.
\]

### Quartic cascade

Computed \(Q_4\) explicitly and derived the next incidence equation. This
shows that the five-root frontier is overdetermined by repeated moment
incidences.

### Taylor-coefficient cover formulation

Reformulated Casas-Alvero as a finite cover problem for Taylor coefficients at
the roots. In the real-rooted five-root case, endpoint roots can only provide
automatic zeros from their multiplicities; only the three interior roots can
provide recycled derivative zeros.

## 2026-06-10, continuation

### Electrostatic obstruction

Added a local real-rooted obstruction for the first recycled Taylor
coefficients. For a root \(r_i\), write
\[
  f(r_i+y)=C\,y^{m_i}G_i(y),
  \qquad
  G_i(y)=\prod_{j\ne i}(r_i-r_j+y)^{m_j}.
\]
With
\[
  S_i^{(q)}=\sum_{j\ne i}\frac{m_j}{(r_i-r_j)^q},
\]
the first recycled coefficient is
\[
  [y]G_i(y)=G_i(0)S_i^{(1)}.
\]
Thus covering derivative order \(m_i+1\) at \(r_i\) requires the exact
electrostatic balance equation
\[
  S_i^{(1)}=0.
\]

The second recycled coefficient is
\[
  [y^2]G_i(y)=
  \frac{G_i(0)}{2}\left((S_i^{(1)})^2-S_i^{(2)}\right).
\]
Since \(S_i^{(2)}>0\) for real roots, the implication
\[
  [y]G_i(y)=0
  \quad\Longrightarrow\quad
  [y^2]G_i(y)\ne0
\]
holds.

Conclusion: no real root can simultaneously cover its first two recycled
derivative orders \(m_i+1\) and \(m_i+2\). In the five-root real frontier, the
three interior roots must therefore cover the remaining derivative orders with
forced local gaps.

### Separation-ratio exclusion

Converted the real-root gap obstruction into a scale-invariant exclusion.
For a centered real-rooted candidate, let
\[
  R=\max|\alpha_\nu|,
  \qquad
  \delta=\min\{|\alpha_\nu|:\alpha_\nu\ne0\}.
\]
Any nontrivial Casas-Alvero polynomial must satisfy
\[
  \delta\le \frac{R}{\sqrt{d-1}},
\]
or equivalently
\[
  d\le 1+\left(\frac{R}{\delta}\right)^2.
\]

This immediately eliminates centered real-rooted configurations whose roots
are too well separated from the centroid.

Concrete closed family: no real-rooted Casas-Alvero counterexample can have
distinct roots
\[
  -2h,\ -h,\ 0,\ h,\ 2h
\]
for \(h\ne0\), regardless of multiplicities. If the degree is \(>5\), the
separation-ratio bound excludes it; if the degree is \(5\), all roots are
simple, so \(f\) and \(f'\) have no common root.
