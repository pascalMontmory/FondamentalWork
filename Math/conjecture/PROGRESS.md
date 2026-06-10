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

### Top-order anchoring

Added an anchoring lemma for the two highest derivative orders. In centered
normal form, for a root \(r\) of multiplicity \(m\),
\[
  f(r+y)=C\,y^mG_r(y),\qquad D=\deg G_r=d-m.
\]
The coefficient of \(y^{D-1}\) in \(G_r\) equals \(dr\). Hence
\[
  f^{(d-1)}(r)=0\quad\Longleftrightarrow\quad r=0.
\]
So the top derivative condition is covered uniquely by the centroid root.

The next order cannot be covered by \(0\), because
\[
  Q_2(0)=-P_2/(d(d-1))\ne0
\]
for nontrivial real-rooted candidates. It also cannot be covered by an
endpoint root, since endpoint local products have all coefficients nonzero and
the order \(d-2\) is not automatic in the five-root frontier.

Conclusion: in the real five-root frontier, \(d-1\) is forced to the centroid
root, while \(d-2\) is forced to a nonzero interior root satisfying
\[
  |a|\le R/\sqrt{d-1}.
\]

### Three-top-order pattern

Extended the anchoring to \(d-3\). Since
\[
  Q_3(0)=-\frac{2P_3}{d(d-1)(d-2)},
\]
there are two top-order signatures:

- if \(P_3=0\), then \(d-3\) may be covered by the centroid root \(0\);
- if \(P_3\ne0\), then \(d-3\) must be covered by a nonzero interior root
  \(b\) satisfying the cubic fiber equation
  \[
    b^3-3a^2b=\frac{2P_3}{d(d-1)(d-2)},
  \]
  where \(a^2=P_2/(d(d-1))\).

Endpoint roots cannot cover any of \(d-1,d-2,d-3\) in the real five-root
frontier.

### Repeated-root compression

If the same absolute root covers both \(d-2\) and \(d-3\), i.e. \(Q_3(a)=0\)
or \(Q_3(-a)=0\) for the root \(a\) selected by \(Q_2\), then
\[
  |a|\le \frac{R}{d-2}.
\]
This improves the earlier \(R/\sqrt{d-1}\) localization to \(R/(d-2)\) in the
repeated-root branch. Therefore either the top-order cover creates a very
tight \(1/d\)-scale near-collision with the centroid, or it must use two
different nonzero interior roots.

### Four-top-order branching

Extended the finite top-order cover to \(d-4\). In the real five-root frontier,
the endpoint multiplicities are at most \(d-4\), and endpoints have no
recycled zeros. Hence endpoints cannot cover any of
\[
  d-1,\quad d-2,\quad d-3,\quad d-4.
\]
All four top orders must therefore be covered by the three interior roots.

The quartic top derivative gives
\[
  Q_4(0)=
  \frac{3P_2^2-6P_4}{d(d-1)(d-2)(d-3)}.
\]
Thus \(d-4\) is covered by the centroid root if and only if
\[
  P_4=\frac{P_2^2}{2}.
\]
Otherwise \(d-4\) must be covered by a nonzero interior root \(c\) satisfying
\[
  Q_4(c)=0.
\]

In the centroid branch, the identity \(P_4=P_2^2/2\) gives a sharper
localization. Since \(P_4\le R^2P_2\) for real roots bounded by \(R\), and
\[
  P_2=d(d-1)a^2
\]
for the root \(a\) selected by \(Q_2\), one obtains
\[
  |a|\le\frac{\sqrt2\,R}{\sqrt{d(d-1)}}.
\]

This is a new \(1/d\)-scale compression: if the top-order cover returns to the
centroid at \(d-4\), then the nonzero root forced by \(d-2\) must nearly collide
with the centroid.

### Non-Q2 double-cover clustering

Added the repeated-cover analysis for the case where a nonzero root \(b\)
covers both \(d-3\) and \(d-4\). If \(a\) is the root selected by \(Q_2\), then
eliminating \(P_3\) from
\[
  Q_3(b)=0,\qquad Q_4(b)=0
\]
gives the exact identity
\[
  \frac{3P_2^2-6P_4}{d(d-1)(d-2)(d-3)}
  =
  3b^2(b^2-2a^2).
\]
Equivalently,
\[
  P_4
  =
  \frac{P_2^2-d(d-1)(d-2)(d-3)b^2(b^2-2a^2)}{2}.
\]

Because \(P_4\ge0\) for real roots, this implies
\[
  \frac{b^2}{a^2}
  \left(\frac{b^2}{a^2}-2\right)
  \le
  \frac{d(d-1)}{(d-2)(d-3)}.
\]
Hence
\[
  |b|
  \le
  \left(
    1+\sqrt{1+\frac{d(d-1)}{(d-2)(d-3)}}
  \right)^{1/2}|a|.
\]

This gives a pigeonhole consequence for the noncentroid branch
\[
  P_3\ne0,\qquad P_4\ne P_2^2/2.
\]
The orders \(d-3\) and \(d-4\) are then both covered by nonzero interior roots.
Since the five-root frontier has only two nonzero interior roots, either the
cover repeats the \(Q_2\)-root, or the other nonzero interior root must cover
both \(d-3\) and \(d-4\) and is therefore clustered within a constant multiple
of \(|a|\).

### Fifth top derivative and endpoint gate

Computed the normalized fifth top derivative:
\[
  Q_5(x)
  =
  x^5
  -\frac{10P_2}{D_2}x^3
  -\frac{20P_3}{D_3}x^2
  +\frac{15P_2^2-30P_4}{D_4}x
  +\frac{20P_2P_3-24P_5}{D_5},
\]
where
\[
  D_j=d(d-1)\cdots(d-j+1).
\]
Thus
\[
  Q_5(0)=0
  \quad\Longleftrightarrow\quad
  5P_2P_3=6P_5.
\]

This gives the first clean condition for the centroid to cover \(d-5\).

Endpoint roots can re-enter at \(d-5\), but only through a narrow automatic
coverage gate. In the real five-root frontier, an endpoint can cover \(d-5\)
if and only if its multiplicity is exactly \(d-4\). Then the four other roots
are all simple.

Therefore outside this massive-endpoint branch, \(d-5\) is also forced to an
interior root. If it is not covered by the centroid identity
\[
  5P_2P_3=6P_5,
\]
then it must be covered by a nonzero interior root satisfying the quintic
moment equation
\[
  Q_5(z)=0.
\]

### Massive-endpoint reduction

Separated the endpoint-gate branch. If an endpoint \(e\) has multiplicity
\[
  m_e=d-4,
\]
then
\[
  f^{(k)}(e)=0\qquad(0\le k\le d-5).
\]
So all derivative orders \(1,\ldots,d-5\) are automatically covered by the
massive endpoint. The full Casas-Alvero condition in this branch is therefore
equivalent to the four top-order incidences. Since \(d-1\) is already anchored
at the centroid, the live finite system is
\[
  Q_2(a)=Q_3(b)=Q_4(c)=0
\]
on the three interior roots.

The centroid equation also forces the massive endpoint close to the centroid.
If the massive endpoint is \(-A\) and the opposite endpoint is \(B>0\), then
\[
  (d-4)A=x+y+B\le3B,
\]
where \(x,y\) are the two remaining nonzero simple roots. Hence
\[
  A\le\frac{3R}{d-4}.
\]
The right-endpoint case is symmetric.

Thus the massive-endpoint branch has two forced degeneracies: almost all
multiplicity sits at one endpoint, and that endpoint is itself \(O(R/d)\)-close
to the centroid. For \(d>5\), at most one endpoint can be massive.

### Massive-endpoint normal form

Reduced the massive-endpoint branch to a two-variable algebraic system. After
reflection and scaling, write the massive endpoint as \(-1\), with
multiplicity
\[
  n=d-4.
\]
The roots are
\[
  -1,\quad 0,\quad u,\quad v,\quad w,
\]
with the four non-endpoint roots simple. The centroid equation gives
\[
  w=n-u-v.
\]
Thus
\[
  P_k=n(-1)^k+u^k+v^k+(n-u-v)^k.
\]

The branch is now finite:

- \(Q_2\) must be covered by \(a\in\{u,v\}\), so
  \[
    D_2a^2=P_2.
  \]
- \(Q_3\) is covered either by the centroid, giving \(P_3=0\), or by
  \(t\in\{u,v\}\), giving
  \[
    t^3-3a^2t-\frac{2P_3}{D_3}=0.
  \]
- \(Q_4\) is covered either by the centroid, giving \(P_4=P_2^2/2\), or by
  \(s\in\{u,v\}\), giving
  \[
    s^4-6a^2s^2-\frac{8P_3}{D_3}s
    +\frac{3P_2^2-6P_4}{D_4}=0.
  \]

So the massive-endpoint branch has become finitely many explicit polynomial
systems in \(u,v\), indexed by
\[
  a\in\{u,v\},\qquad t,s\in\{0,u,v\}.
\]

### One-parameter collapse after \(Q_2\)

Refined the massive-endpoint branch further. Once the root \(a\) selected by
\(Q_2\) is fixed, the two remaining nonzero roots \(y,z\) have forced sum and
product:
\[
  S=y+z=n-a,
\]
\[
  p=yz
  =
  \frac{S^2+n+a^2-D_2a^2}{2}
  =
  \frac{n^2+n-2na-(n+5)(n+2)a^2}{2}.
\]
Thus \(y,z\) are roots of
\[
  F_a(X)=X^2-SX+p.
\]
The reality condition is
\[
  \Delta_a
  =
  (2n^2+14n+21)a^2+2na-n(n+2)\ge0.
\]

Using the recurrence
\[
  T_0=2,\qquad T_1=S,\qquad T_k=ST_{k-1}-pT_{k-2},
\]
all moments become one-variable polynomials:
\[
  M_k(a)=n(-1)^k+a^k+T_k.
\]

Therefore all \(Q_3\) and \(Q_4\) cover alternatives in the massive-endpoint
branch reduce to univariate equations in \(a\): direct equations if the cover
uses \(0\) or \(a\), and resultants with \(F_a\) if the cover uses one of the
two remaining roots. This removes the two-variable system from the massive
branch.

### First cubic gates in the massive branch

Expanded the two simplest \(Q_3\)-branches after the one-parameter reduction.
If the centroid covers \(d-3\), then \(a\) must solve the cubic
\[
  \begin{aligned}
  C_0(n,a)=&
  -3a^3n^2-21a^3n-30a^3
  +3a^2n^3+21a^2n^2+30a^2n  \\
  &+3an^2+3an
  -n^3-3n^2-2n=0.
  \end{aligned}
\]
If the same root \(a\) covers both \(d-2\) and \(d-3\), then \(a\) must solve
\[
  \begin{aligned}
  C_a(n,a)=&
  2a^3n^3+15a^3n^2+31a^3n+18a^3
  +3a^2n^3+21a^2n^2+30a^2n \\
  &+3an^2+3an
  -n^3-3n^2-2n=0.
  \end{aligned}
\]
Thus two massive-endpoint branches now start with explicit cubic gates in the
single variable \(a\), subject only to the real discriminant and ordering
conditions from the previous section.

### Interior selector for resultant branches

Refined the resultant branches in the massive-endpoint case. The two roots of
\[
  F_a(X)=X^2-SX+p
\]
are
\[
  X_-=\frac{S-\sqrt{\Delta_a}}2,\qquad
  X_+=\frac{S+\sqrt{\Delta_a}}2.
\]
Only \(X_-\) is admissible as a covering root; \(X_+\) is the right endpoint.

For any polynomial condition \(H(X)\), reduce modulo \(F_a\):
\[
  H(X)\equiv A_HX+B_H\pmod{F_a}.
\]
Then the admissible interior-root condition is
\[
  (A_HS+2B_H)^2=A_H^2\Delta_a,
  \qquad
  A_H(A_HS+2B_H)\ge0.
\]
The reverse inequality selects the endpoint root and must be rejected.

For the \(Q_3\)-resultant branch,
\[
  H_3(X)=D_3(X^3-3a^2X)-2M_3(a),
\]
and
\[
  H_3(X)\equiv A_3X+B_3\pmod{F_a},
\]
with
\[
  A_3=
  \frac{(n+2)(n+3)(n+4)}2
  \left((n+1)(n+6)a^2-2na+n(n-1)\right)>0
\]
for every \(n\ge2\). Therefore the admissible \(Q_3\)-resultant branch is
selected by
\[
  (A_3S+2B_3)^2=A_3^2\Delta_a,
  \qquad
  A_3S+2B_3\ge0.
\]
This removes endpoint contamination from the one-parameter elimination.

### Admissibility strip for the \(Q_2\)-root

Derived a simple interval for the \(Q_2\)-root \(a\) in the massive-endpoint
branch. Since both reconstructed roots of \(F_a\) must lie to the right of the
massive endpoint \(-1\), one needs
\[
  F_a(-1)>0.
\]
This gives
\[
  (n+5)(n+2)a^2+2(n+1)a-(n+1)(n+2)<0.
\]
Therefore
\[
  \alpha_n<a<\beta_n,
\]
where
\[
  \alpha_n=
  \frac{-n-1-\sqrt{n^4+10n^3+34n^2+46n+21}}
       {n^2+7n+10},
\]
\[
  \beta_n=
  \frac{-n-1+\sqrt{n^4+10n^3+34n^2+46n+21}}
       {n^2+7n+10}.
\]
The quadratic has positive values at \(-1\) and \(1\), and a negative value at
\(0\), so
\[
  -1<\alpha_n<0<\beta_n<1.
\]

Thus every cubic gate in the massive-endpoint branch only has to be tested on
the explicit interval \((\alpha_n,\beta_n)\), with the noncollision exclusions
\[
  F_a(0)\ne0,\qquad F_a(a)\ne0.
\]
