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

### Same-root \(Q_3\) gate eliminated

Closed one massive-endpoint subbranch. The gate where the same root \(a\)
covers both \(d-2\) and \(d-3\) is
\[
  C_a(n,a)=0.
\]
Its cubic discriminant is
\[
  -108n^2(n+1)(n+2)(n+3)^2
  \left(3n^4+31n^3+102n^2+108n+18\right)<0,
\]
so it has exactly one real root for every \(n\ge2\).

Reducing \(C_a\) modulo the discriminant quadratic
\[
  \Delta_a=(2n^2+14n+21)a^2+2na-n(n+2)
\]
gives a linear remainder \(K_na+M_n\). Its zero \(a_n^*=-M_n/K_n\) satisfies
\[
  \Delta_{a_n^*}<0.
\]
Therefore \(C_a\) has opposite signs at the two roots of \(\Delta_a\), and its
unique real zero lies inside the forbidden interval \(\Delta_a<0\).

Conclusion: in the massive-endpoint branch, the same nonzero root cannot cover
both \(d-2\) and \(d-3\). After \(Q_2\), order \(d-3\) must be covered either
by the centroid or by the other interior nonzero root.

### Centroid \(Q_3\) gate reduced to \(n=2\)

Almost eliminated the other cubic gate in the massive-endpoint branch. The
centroid \(Q_3\)-gate is
\[
  C_0(n,a)=0.
\]
For \(n\ge3\), the cubic \(C_0(n,\cdot)\) has three distinct real roots. By
reducing \(C_0\) modulo
\[
  \Delta_a=(2n^2+14n+21)a^2+2na-n(n+2),
\]
one checks that
\[
  C_0(n,\delta_-)>0,\qquad C_0(n,\delta_+)>0,
\]
where \(\delta_-<0<\delta_+\) are the two roots of \(\Delta_a\). Since
\[
  C_0(n,0)=-n(n+1)(n+2)<0,
\]
two roots of \(C_0\) lie in the forbidden interval \(\Delta_a<0\). The third
root lies to the right of \(1\), because
\[
  C_0(n,1)=2(n-1)(n^2+10n+15)>0
\]
and the leading coefficient is negative.

Conclusion: for every \(n\ge3\), the centroid \(Q_3\)-gate has no admissible
massive-endpoint solution. The only remaining centroid-gate exception is
\[
  n=2\quad(d=6).
\]

### Finite centroid exception \(n=2\) closed

Checked the remaining centroid \(Q_3\)-exception in the massive-endpoint
branch. For \(n=2\),
\[
  C_0(2,a)=-6(14a^3-28a^2-3a+4).
\]
Let
\[
  R(a)=14a^3-28a^2-3a+4.
\]
The remaining \(Q_4\)-condition has three possible covers:

- the centroid, giving
  \[
    28a^3-11a^2-6a+3=0;
  \]
- the same root \(a\), giving
  \[
    61a^4+14a^2+2a-3=0;
  \]
- the other interior root, giving a degree-eight resultant with \(F_a\).

In all three cases, the relevant polynomial is coprime to \(R(a)\). Therefore
no root of the exceptional cubic can satisfy \(Q_4\).

Conclusion: the \(n=2\) centroid exception is impossible. In the massive
endpoint branch, \(d-3\) cannot be covered by the centroid; after \(Q_2\), it
must be covered by the other nonzero interior root.

### Reduced massive-endpoint branch

Recorded the current endpoint-massive normal form after the \(Q_3\) closures.
In the notation
\[
  -1,\quad 0,\quad a,\quad X_-,\quad X_+,
\]
where \(X_+\) is the right endpoint, the previous sections prove that
\[
  d-3
\]
cannot be covered by \(a\), by \(0\), or by an endpoint. Hence it must be
covered by the other interior root:
\[
  Q_3(X_-)=0.
\]

So the massive-endpoint branch is now reduced to one oriented
quadratic-cubic incidence \(H_3(X_-)=0\), plus the remaining \(Q_4\)-cover
condition.

### Two \(Q_4\)-covers eliminated by exact resultants

Closed two of the three remaining \(Q_4\)-possibilities in the reduced
massive-endpoint branch.

Let
\[
  E_3(n,a)=\operatorname{Res}_X(F_a,H_3).
\]
If \(Q_4\) is covered by the centroid, then a solution must satisfy
\[
  \operatorname{Res}_a(E_3,2M_4-M_2^2)=0.
\]
The exact resultant factors as
\[
  n^6(n+1)^4(n+2)^4(n+3)^6(n+5)P_{39}(n),
\]
where \(P_{39}\) has no root modulo \(17\). Thus this branch has no integer
\(n\ge2\).

If \(Q_4\) is covered by the \(Q_2\)-root \(a\), then the exact resultant
factors as
\[
  4096n^6(n+1)^4(n+2)^6(n+3)^8P_{48}(n),
\]
where \(P_{48}\) has no root modulo \(11\). This branch also has no integer
\(n\ge2\).

The exact verification script is
\[
  \texttt{Math/conjecture/tools/massive\_endpoint\_q4\_certificates.py}.
\]

Conclusion: in the massive-endpoint branch, \(d-4\) cannot be covered by
\(0\) or by \(a\). It must be covered by the same interior root \(X_-\) that
already covers \(d-3\).

### Massive-endpoint branch closed

Closed the final \(Q_4\)-possibility in the reduced massive-endpoint branch.
The last remaining pattern was
\[
  d-2\mapsto a,\qquad d-3\mapsto X_-,\qquad d-4\mapsto X_-.
\]
Let
\[
  H_4(X)
  =
  D_4(X^4-6a^2X^2)-8M_3(a)X+3M_2(a)^2-6M_4(a).
\]
Reducing \(H_3\) and \(H_4\) modulo \(F_a\) gives
\[
  H_3\equiv A_3X+B_3,\qquad H_4\equiv A_4X+B_4.
\]
Since \(A_3\ne0\) for \(n\ge2\), a common root must satisfy
\[
  C_{34}(n,a)=A_3B_4-A_4B_3=0.
\]
Together with
\[
  E_3(n,a)=\operatorname{Res}_X(F_a,H_3)=0,
\]
this gives the necessary resultant condition
\[
  \operatorname{Res}_a(E_3,C_{34})=0.
\]
The exact resultant factors as
\[
  2^{30}n^{10}(n+1)^8(n+2)^{12}(n+3)^{16}(n+4)^6(n+5)^2
  P_{13}(n)^2P_{46}(n),
\]
where \(P_{13}\) has no root modulo \(13\) and \(P_{46}\) has no root modulo
\(17\). Thus no integer \(n\ge2\) can satisfy the final branch.

Conclusion: the massive-endpoint branch is impossible. In the real five-root
frontier, any remaining counterexample must be non-massive, i.e. no endpoint
has multiplicity \(d-4\).

### Post-massive frontier

Recorded the immediate next branch point after closing the massive-endpoint
case.

Since endpoints can cover \(d-5\) only with multiplicity \(d-4\), and that
case is now impossible, derivative order \(d-5\) is universally forced to the
centroid condition
\[
  5P_2P_3=6P_5
\]
or to a non-endpoint root \(z\) with
\[
  Q_5(z)=0.
\]

The next endpoint gate is derivative order \(d-6\). An endpoint can cover it
automatically only if its multiplicity is at least \(d-5\); since \(d-4\) is
closed, the only remaining endpoint gate here is \(m_{\rm endpoint}=d-5\).

The exact sixth top derivative is
\[
\begin{aligned}
  Q_6(x)=&
  x^6
  -\frac{15P_2}{D_2}x^4
  -\frac{40P_3}{D_3}x^3
  +\frac{45P_2^2-90P_4}{D_4}x^2 \\
  &+\frac{120P_2P_3-144P_5}{D_5}x
  +\frac{-15P_2^3+90P_2P_4+40P_3^2-120P_6}{D_6}.
\end{aligned}
\]

So the next finite split is:

1. endpoint multiplicity \(d-5\);
2. centroid identity
   \[
     -15P_2^3+90P_2P_4+40P_3^2-120P_6=0;
   \]
3. non-endpoint incidence \(Q_6(t)=0\).

### Endpoint \(d-5\) gate reduced to three weight types

Reduced the endpoint multiplicity \(d-5\) branch to explicit weighted
quadratic systems.

Normalize the endpoint to \(-1\) with multiplicity
\[
  n=d-5.
\]
The remaining four distinct roots have total multiplicity \(5\), so exactly
one of them is double. After choosing the nonzero \(Q_2\)-root \(a\), write the
other two nonzero roots as \(y,z\), with multiplicities
\[
  m_0,\quad m_a,\quad m_y,\quad m_z,
  \qquad
  m_0+m_a+m_y+m_z=5.
\]
The centroid equation and \(Q_2(a)=0\) give
\[
  m_y y+m_z z=n-m_a a,
\]
\[
  m_y y^2+m_z z^2=(n+5)(n+4)a^2-n-m_a a^2.
\]
Eliminating \(z\) gives the weighted quadratic
\[
\begin{aligned}
  F_m(Y)=&
  m_y(m_y+m_z)Y^2+2m_y(m_a a-n)Y+n^2-2m_a n a+m_z n\\
  &+m_a(m_a+m_z)a^2-m_z(n+5)(n+4)a^2.
\end{aligned}
\]

Up to exchanging \(y,z\), only three weight types remain:
\[
  (2,1,1,1),\qquad(1,2,1,1),\qquad(1,1,2,1),
\]
corresponding to the double root being \(0\), \(a\), or another nonzero root.

The script
\[
  \texttt{Math/conjecture/tools/endpoint\_d5\_reduction.py}
\]
reconstructs these three cases and reduces \(Q_3,Q_4,Q_5\) modulo \(F_m\).
Thus the endpoint \(d-5\) branch is now a finite collection of explicit
two-variable systems indexed by three weight types and cover choices in
\(\{0,a,Y,z\}^3\).

### Symmetric endpoint \(d-5\) types closed

Checked the two endpoint-\(d-5\) weight types where the two remaining nonzero
roots have equal multiplicity:
\[
  (m_0,m_a,m_y,m_z)=(2,1,1,1)
\]
and
\[
  (m_0,m_a,m_y,m_z)=(1,2,1,1).
\]
For these two types, after \(Q_2(a)=0\), the moments \(M_3,M_4,M_5\) are
univariate in \(a\) over \(\mathbb Q(n)\). For each of the \(27\) cover triples
for \(Q_3,Q_4,Q_5\), using covers
\[
  0,\quad a,\quad r
\]
where \(r\) denotes either root of the symmetric quadratic, the gcd of the
three cover equations in \(\mathbb Q(n)[a]\) is \(1\).

The generic gcd verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d5\_symmetric\_gcds.py}.
\]

Then removed the remaining specialization caveat by taking the gcd in
\(\mathbb Z[n]\) of the pairwise resultants in \(a\) for each cover triple.
For the double-centroid type, all exceptional roots lie in
\[
  \{-6,-3,-2,-1\}.
\]
For the double-\(Q_2\)-root type, all exceptional roots lie in
\[
  \{-6,-4,-2,-1\}.
\]
Since \(n=d-5\ge1\), none is admissible.

The integer resultant verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d5\_symmetric\_resultants.py}.
\]

Conclusion: these two endpoint-\(d-5\) types are impossible. The only
remaining endpoint-\(d-5\) family is the genuinely two-variable asymmetric
weight type
\[
  (m_0,m_a,m_y,m_z)=(1,1,2,1).
\]

### Endpoint \(d-5\) branch closed

Closed the remaining asymmetric endpoint-\(d-5\) type
\[
  (m_0,m_a,m_y,m_z)=(1,1,2,1).
\]
In this type,
\[
  F(Y)
  =
  6Y^2+4(a-n)Y+n^2-2na+n-(n+3)(n+6)a^2
\]
and
\[
  z=n-a-2Y.
\]
For every cover \(c\in\{0,a,Y,z\}\), each \(Q_j(c)\)-condition
\((j=3,4,5)\) reduces modulo \(F\) to a linear form
\[
  A_{j,c}Y+B_{j,c}.
\]

For each of the \(64\) cover triples, the script eliminates \(Y\) using one
resultant and two linear-root compatibility determinants, then eliminates
\(a\) by pairwise resultants. Every necessary polynomial in \(n\) factors into
linear factors with roots in
\[
  \{-6,-4,-3,-2,-1,0\}
\]
and five nonlinear factors of degrees
\[
  5,\quad7,\quad7,\quad20,\quad22.
\]
The degree-\(5\) factor has no root modulo \(7\), the two degree-\(7\) factors
have no root modulo \(5\), the degree-\(20\) factor has no root modulo \(11\),
and the degree-\(22\) factor has no root modulo \(7\). Since \(n=d-5\ge1\),
no cover triple is possible.

The exact verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d5\_asymmetric\_resultants.py}.
\]

Conclusion: the endpoint \(d-5\) branch is impossible.

### Post-endpoint-\(d-5\) frontier and endpoint \(d-6\) reduction

Since endpoint multiplicities \(d-4\) and \(d-5\) are closed, derivative order
\(d-6\) cannot be covered by an endpoint. It is now forced to the centroid
identity
\[
  -15P_2^3+90P_2P_4+40P_3^2-120P_6=0
\]
or to a non-endpoint root satisfying \(Q_6=0\).

The next endpoint gate is derivative order \(d-7\), where the only remaining
endpoint multiplicity is \(d-6\). The seventh top derivative is
\[
\begin{aligned}
  Q_7(x)=&
  x^7
  -\frac{21P_2}{D_2}x^5
  -\frac{70P_3}{D_3}x^4
  +\frac{105(P_2^2-2P_4)}{D_4}x^3\\
  &+\frac{84(5P_2P_3-6P_5)}{D_5}x^2\\
  &-\frac{35(3P_2^3-18P_2P_4-8P_3^2+24P_6)}{D_6}x\\
  &-\frac{6(35P_2^2P_3-84P_2P_5-70P_3P_4+120P_7)}{D_7}.
\end{aligned}
\]
The centroid \(Q_7\)-condition is therefore
\[
  35P_2^2P_3-84P_2P_5-70P_3P_4+120P_7=0.
\]

For endpoint multiplicity \(d-6\), write \(n=d-6\). The four remaining roots
have total multiplicity \(6\). After choosing the nonzero \(Q_2\)-root \(a\),
the two remaining nonzero roots satisfy
\[
\begin{aligned}
  F_m(Y)=&
  m_y(m_y+m_z)Y^2+2m_y(m_a a-n)Y+n^2-2m_a n a+m_z n\\
  &+m_a(m_a+m_z)a^2-m_z(n+6)(n+5)a^2.
\end{aligned}
\]
Up to exchanging the two remaining roots, there are seven weight types:
\[
\begin{gathered}
  (1,1,2,2),\quad(1,1,3,1),\quad(1,2,2,1),\\
  (1,3,1,1),\quad(2,1,2,1),\quad(2,2,1,1),\quad(3,1,1,1).
\end{gathered}
\]

The reconstruction script
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_reduction.py}
\]
checks these seven types and reduces \(H_3,H_4,H_5,H_6\) modulo \(F_m\).
Four types become univariate in \(a\), and three remain linear in \(Y\).

### Endpoint \(d-6\) cover degrees and modular diagnostic

The explicit cover substitution has now been checked. For every \(d-6\)
weight type and every cover
\[
  X\in\{0,a,Y,z\},
\]
the reduced \(H_3,H_4,H_5,H_6\) cover condition has degree at most one in
\(Y\). The verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_cover\_degrees.py}.
\]

A finite-field diagnostic was also added:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_modular\_sieve.py}.
\]
It evaluates the system
\[
  F_m=0,\qquad
  \prod_{X\in\{0,a,Y,z\}} H_k(X)=0,\quad k=3,4,5,6.
\]
For all seven weight types there are no nondegenerate points modulo \(5\);
the remaining points all lie on \(a=0\) or on one of the bad denominator
residues \(n+1,\ldots,n+6\equiv0\pmod 5\).

This is currently a diagnostic, not the final characteristic-zero proof. The
next exact target is the saturation by
\[
  a(n+1)(n+2)(n+3)(n+4)(n+5)(n+6)
\]
followed by elimination of \(Y\) and \(a\) to recover univariate obstruction
factors in \(n\).

### Four endpoint \(d-6\) weight types closed generically

The first exact \(d-6\) elimination pass closes four of the seven weight types
over the generic parameter field \(\mathbb{Q}(n)\). For
\[
  (1,1,2,2),\quad(1,3,1,1),\quad(2,2,1,1),\quad(3,1,1,1),
\]
all \(4^4=256\) cover quadruples have gcd \(1\) in \(\mathbb{Q}(n)[a]\)
after eliminating \(Y\) with resultants and linear-root compatibility
determinants. These four types are therefore impossible away from finitely
many specializations of \(n\).

The verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_type\_generic\_probe.py}.
\]
The remaining non-generically-certified types are
\[
  (1,1,3,1),\quad(1,2,2,1),\quad(2,1,2,1).
\]
They require a specialization certificate rather than the naive generic sweep.
