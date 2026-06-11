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
The corrected diagnostic starts at primes \(p>6\), since for \(p=5\) the bad
denominator residues \(n+1,\ldots,n+6\equiv0\pmod p\) cover the whole field.
Five types have no nondegenerate points modulo \(7\):
\[
  (1,1,2,2),\quad(1,2,2,1),\quad(1,3,1,1),\quad
  (2,1,2,1),\quad(2,2,1,1).
\]
The remaining two diagnostic cases,
\[
  (1,1,3,1),\quad(3,1,1,1),
\]
have nondegenerate points modulo \(7\), but none modulo \(11\).

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

### Residue sieve for the three remaining endpoint \(d-6\) types

Added a residue-level modular sieve for the three remaining types:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_residue\_sieve.py}.
\]
It records the allowed \(n\)-residues for each tested prime, including both
bad denominator residues and residues with actual nondegenerate finite-field
points. For primes
\[
  7,11,13,17,19,23,29,31
\]
the combined surviving densities are
\[
\begin{array}{c|c}
  \text{type} & \text{surviving density}\\
  \hline
  (1,1,3,1) & 4064256/6685349671\\
  (1,2,2,1) & 2667168/6685349671\\
  (2,1,2,1) & 3111696/6685349671.
\end{array}
\]

This is still diagnostic rather than a closure. It narrows the exact target:
the specialization certificates should be built on the surviving residue
families after saturation by
\[
  a(n+1)(n+2)(n+3)(n+4)(n+5)(n+6).
\]

### Checkpoint: equation-level endpoint \(d-6\) elimination

Started the equation-level approach suggested after the residue sieve. Instead
of enumerating the \(4^4\) cover quadruples, define
\[
  R_k=\prod_{X\in\{0,a,Y,z\}}H_k(X),\qquad k=3,4,5,6,
\]
and reduce each \(R_k\) modulo the weighted quadratic \(F_m\). The draft
script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_equation\_elimination.py}.
\]

For the remaining type \((1,1,3,1)\), the reduced products are all linear in
\(Y\), with degrees in \(a\)
\[
  12,\quad16,\quad20,\quad22.
\]
The resulting equation-level eliminants have degrees in \(a\)
\[
  24,\quad27,\quad31,\quad33.
\]
This confirms that the construction of the four compact equations is feasible;
the next blocker is the gcd of these larger eliminants over \(\mathbb{Q}(n)[a]\)
or a faster modular substitute.

### Equation-level modular specialization closes the remaining generic types

Added the modular-specialization substitute:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_equation\_modular\_probe.py}.
\]
It fixes \(n\) modulo a prime before constructing the four equation-level
products. If a good specialization gives gcd \(1\) in \(\mathbb F_p[a]\), then
the generic gcd over \(\mathbb Q(n)[a]\) is also \(1\).

For the three previously remaining endpoint-\(d-6\) types, the probe finds:
\[
\begin{array}{c|c|c}
  \text{type} & p & n\pmod p \\
  \hline
  (1,1,3,1) & 11 & 4 \\
  (1,2,2,1) & 11 & 1 \\
  (2,1,2,1) & 11 & 1
\end{array}
\]
Each row gives equation-level gcd \(1\) after specialization. Together with
the earlier four cover-enumeration generic closures, all seven endpoint
\(d-6\) weight types are now impossible over the generic parameter field.

The remaining work in this endpoint branch is no longer generic gcd
construction. It is the finite specialization problem: identify and eliminate
the exceptional integer values of \(n\) where denominators, leading
coefficients, or specialization resultants can degenerate.

### Endpoint \(d-6\): exceptional specialization extraction started

Clarified the final \(d-6\) lock. The modular-specialization probe does not
close all integer \(n\ge1\). It proves that the three remaining types have no
generic component. Therefore any remaining solution must lie over finitely
many exceptional specializations of \(n\).

Added the exact extraction skeleton:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_equation\_exceptional\_n.py}.
\]
It forms the four equation-level eliminants, takes pairwise resultants in
\(a\), and saturates the resulting univariate obstruction by
\[
  a(n+1)(n+2)(n+3)(n+4)(n+5)(n+6).
\]
The direct global symbolic path is currently too heavy, so it should be used
as the target specification for a modular/reconstructed computation rather
than as the final engine.

Added the lighter residue extractor:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_equation\_exceptional\_residues.py}.
\]
For each residue \(n\bmod p\), it computes the gcd of the four specialized
eliminants in \(\mathbb F_p[a]\). A residue with gcd \(0\) is excluded over
the algebraic closure; a positive-degree gcd, or total vanishing of the
specialized eliminants, is kept as live.

With primes \(11,13,17\), the saturated live classes are:
\[
\begin{array}{c|c}
  \text{type} & \text{saturated live classes mod }2431 \\
  \hline
  (1,1,3,1) & 64 \\
  (1,2,2,1) & 144 \\
  (2,1,2,1) & 54
\end{array}
\]
These are not yet a closure, but they are the right finite targets for the
next exact reconstruction of exceptional factors in \(n\).

### Endpoint \(d-6\): resultant reconstruction path

Tested the direct symbolic resultant path after optimizing the quadratic
reduction. The construction of the four compact products is now traceable and
reaches the expected degrees for \((1,1,3,1)\):
\[
  \deg_a(R_3,R_4,R_5,R_6)=(12,16,20,22),
\]
and the corresponding eliminants have
\[
  \deg_a(E_3,E_{34},E_{35},E_{36})=(24,27,31,33).
\]
However, the first pairwise resultant \(\operatorname{Res}_a(E_3,E_{34})\)
is still too large for a direct SymPy computation.

Added the interpolation prototype:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_resultant\_interpolate.py}.
\]
For \((1,1,3,1)\), modulo \(1009\), the first pairwise resultant has degree
greater than \(39\) in \(n\). This confirms the next implementation target:
compute exceptional factors by modular evaluation/interpolation and gcd
reconstruction, rather than by direct global resultants.

### Endpoint \(d-6\): modular exceptional factors

Extended the residue extractor with a `--factors` mode. For each coefficient
prime \(p\), it now records the live residues as the polynomial
\[
  P_p(n)=\prod_{r\ \mathrm{live}}(n-r)\in\mathbb F_p[n].
\]
This is a cleaner modular form of the exceptional-specialization data: an
admissible integer \(n\) must satisfy \(P_p(n)\equiv0\pmod p\) for every
tested prime, after excluding the saturated denominator residues.

For the baseline primes \(11,13,17\), the live factors are:
\[
\begin{array}{c|c|c}
  \text{type} & p & P_p(n) \\
  \hline
  (1,1,3,1) & 11 & n(n-1)(n-2)(n-3) \\
  (1,1,3,1) & 13 & n(n-1)(n-2)(n-5) \\
  (1,1,3,1) & 17 & n(n-1)(n-2)(n-6) \\
  (1,2,2,1) & 11 & n(n-2)(n-3) \\
  (1,2,2,1) & 13 & n(n-1)(n-2)(n-3)(n-4)(n-5) \\
  (1,2,2,1) & 17 & n(n-1)(n-2)(n-3)(n-5)(n-6)(n-8)(n+8) \\
  (2,1,2,1) & 11 & n(n-2)(n-3) \\
  (2,1,2,1) & 13 & n(n-1)(n-5) \\
  (2,1,2,1) & 17 & n(n-1)(n-4)(n-6)(n-7)(n+8).
\end{array}
\]

An additional check through primes \(11,13,17,19,23\) did not empty the live
sets, so the next useful computation is not just a larger residue sieve. It
is either a reconstructed exceptional gcd in \(\mathbb F_p[n]\), or direct
treatment of the CRT classes selected by these modular factors.

### Endpoint \(d-6\): CRT class refinement

Added the CRT refinement driver:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_exceptional\_crt\_classes.py}.
\]
It has three uses:

- `--classes` builds the CRT classes selected by the live residue factors;
- `--probe-class=c,M` refines one class \(n\equiv c\pmod M\) by auxiliary
  primes and reports the compatible \(t\)-residues in \(n=c+Mt\);
- `--refine-all` refines all current classes by auxiliary primes.

The key structural point is now explicit in the tool: if \(q\nmid M\), then
\(n=c+Mt\) runs through every residue modulo \(q\) as \(t\) varies. Therefore
a residue-only auxiliary prime usually refines a class into sub-classes
modulo \(Mq\); it does not eliminate the class unless the live set modulo
\(q\) is empty or incompatible.

For the baseline classes from \(11,13,17\), followed by refinement through
\(19,23\), the counts are:
\[
\begin{array}{c|c|c}
  \text{type} & \text{base classes mod }2431
              & \text{refined classes mod }1062347 \\
  \hline
  (1,1,3,1) & 64 & 2688 \\
  (1,2,2,1) & 144 & 4320 \\
  (2,1,2,1) & 54 & 2700.
\end{array}
\]

Thus the CRT sieve is a localization map, not a final lock. The next proof
step must use stronger algebra on the classes: either reconstruct the
exceptional gcd in \(\mathbb F_p[n]\), or specialize \(n=c+Mt\) and eliminate
with \(t\) retained, instead of relying only on residue membership.

### Endpoint \(d-6\): class-parameter \(t\) probes

Added the class-parameter probe:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_exceptional\_class\_t\_probe.py}.
\]
For a CRT class \(n\equiv c\pmod M\), it substitutes
\[
  n=c+Mt
\]
and can build the four equation-level eliminants over \(\mathbb F_p(t)[a]\).
The direct symbolic gcd over \(\mathbb F_p(t)[a]\) builds the eliminants for
the test class but is still too slow at the gcd step, so the script also has
a faster `--scan-t` mode.

The scan mode searches for good \(t\)-specializations whose specialized gcd
in \(\mathbb F_p[a]\) is \(1\). Such a point is a generic-elimination witness
for the class: any remaining obstruction must be confined to the finite set
of bad \(t\)-fibers where denominators, leading coefficients, or
specialization resultants degenerate.

With \(p=1009\), base classes from \(11,13,17\), and \(t=0,\ldots,5\), every
baseline CRT class in all three remaining types has such a witness:
\[
\begin{array}{c|c|c}
  \text{type} & \text{classes mod }2431 & \text{witnessed classes} \\
  \hline
  (1,1,3,1) & 64 & 64 \\
  (1,2,2,1) & 144 & 144 \\
  (2,1,2,1) & 54 & 54.
\end{array}
\]
For example, for \((2,1,2,1)\) and \(n\equiv0\pmod{2431}\), the first live
witness is \(t=1\), giving \(n\equiv413\pmod{1009}\) and gcd degree \(0\) in
\(\mathbb F_{1009}[a]\).

This is the right next reduction: the endpoint-\(d-6\) problem has moved from
generic components in \(n\), to generic components along CRT classes, and now
to finite bad \(t\)-fibers on those classes.

### Endpoint \(d-6\): first finite \(t\)-fiber factors

Extended the class-parameter probe with two refinements:

- `--scan-base-classes` now records the first witness \(t\) and the
  corresponding \(n\bmod p\) for each CRT class;
- `--collect-t` scans a bounded or full residue range in \(t\) and prints the
  live \(t\)-factor
  \[
    T_p(t)=\prod_{r\ \mathrm{live}}(t-r)\in\mathbb F_p[t],
  \]
  with saturated-bad \(t\)-residues separated.

For the representative class
\[
  (2,1,2,1),\qquad n=2431t,
\]
modulo \(p=101\), the full scan \(t=0,\ldots,100\) leaves only the live
residues
\[
  t\in\{0,10,22,25,26,30,38,89\}\pmod{101}.
\]
The saturated-bad residues are
\[
  t\in\{14,28,43,57,72,86\}\pmod{101}.
\]
Thus the first explicit finite \(t\)-fiber factor is
\[
  T_{101}(t)=
  t(t-10)(t-22)(t-25)(t-26)(t-30)(t-38)(t-89).
\]

This is the next usable object: instead of a CRT class carrying an infinite
parameter \(t\), the representative class now has a finite modular
exceptional set in \(t\). The next step is to repeat this extraction across
classes or reconstruct the corresponding exceptional \(t\)-factor directly.

### Endpoint \(d-6\): base-class \(t\)-fiber collector

Added a `--collect-base-t` mode to the class-parameter probe. For every base
CRT class \(n\equiv c\pmod{2431}\), and for each chosen \(t\)-prime \(p\), it
computes the live \(t\)-fibers by transporting the live \(n\)-residues:
\[
  t\equiv (r-c)2431^{-1}\pmod p.
\]
This avoids redoing the specialized gcd calculation for every class.

With base primes \(11,13,17\) and \(t\)-primes \(101,103\), the collector
gives:
\[
\begin{array}{c|c|c|c|c}
  \text{type} & \text{classes} & |L_{101}| & |L_{103}|
              & \text{descendants mod }101\cdot103 \\
  \hline
  (1,1,3,1) & 64 & 9 & 17 & 9792 \\
  (1,2,2,1) & 144 & 16 & 12 & 27648 \\
  (2,1,2,1) & 54 & 8 & 13 & 5616.
\end{array}
\]

Here \(|L_p|\) is the number of live \(n\)-residues modulo \(p\), hence also
the number of live \(t\)-residues for each class because \(p\nmid2431\). The
second \(t\)-prime therefore refines the finite fibers but cannot empty them
by itself when both live sets are nonempty: CRT combines every pair of live
residues.

For the representative class \(n=2431t\) in type \((2,1,2,1)\), the first two
finite factors are:
\[
  T_{101}(t)=
  t(t-10)(t-22)(t-25)(t-26)(t-30)(t-38)(t-89),
\]
and
\[
  T_{103}(t)=
  t(t-4)(t-9)(t-12)(t-17)(t-20)(t-24)(t-25)
  (t-32)(t-50)(t-51)(t-58)(t-89).
\]

The next required step is no longer adding more independent \(t\)-primes
blindly. It is to extract a true class-level exceptional factor in
\(\mathbb F_p[t]\), or to add algebraic constraints that distinguish the CRT
descendants rather than merely intersecting nonempty residue sets.

### Endpoint \(d-6\): local \(t\)-fiber classification

Added the local fiber classifier:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_class\_t\_fiber\_classify.py}.
\]
For a fixed class \(n=c+Mt\), it separates each \(t\bmod p\) into:

- saturated-bad: one of \(n+1,\ldots,n+6\) vanishes;
- all-zero: all four eliminants vanish;
- degree-drop: at least one eliminant drops below the observed generic
  degree;
- regular-gcd: no degree drop and the gcd in \(\mathbb F_p[a]\) has positive
  degree;
- excluded: no degree drop and gcd degree \(0\).

For the representative class
\[
  (2,1,2,1),\qquad n=2431t,
\]
the observed generic eliminant degrees are
\[
  (24,27,30,33)
\]
for both \(p=101\) and \(p=103\).

Modulo \(101\), the raw live factor
\[
  t(t-10)(t-22)(t-25)(t-26)(t-30)(t-38)(t-89)
\]
splits as:
\[
\begin{array}{c|c}
  \text{category} & t\text{-residues mod }101 \\
  \hline
  \text{saturated-bad} & \{14,28,43,57,72,86\} \\
  \text{all-zero} & \varnothing \\
  \text{degree-drop} & \{0,24,29,54,60,61,66,74,87,100\} \\
  \text{regular-gcd} & \{10,22,25,26,30,38,89\}.
\end{array}
\]
Thus the regular part has degree \(7\), not \(8\); the missing raw live fiber
is \(t=0\), which is a degree-drop artifact.

Modulo \(103\), the regular-gcd residues are
\[
  \{4,9,12,17,20,24,25,32,50,51,58,89\},
\]
while the degree-drop residues are
\[
  \{0,3,5,11,18,35,45,55,57,59,61,66,68,75\}.
\]
There are no all-zero fibers in either test.

This is the desired local separation. The next reconstruction should target
the regular-gcd factor, not the raw live factor.

### Endpoint \(d-6\): regular \(t\)-factor comparison

Added the regular-factor comparator:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_regular\_t\_factor\_compare.py}.
\]
It uses the local classifier and keeps only the `regular_gcd` fibers, removing
saturated, all-zero, and degree-drop artifacts before comparing primes.

For the representative class
\[
  (2,1,2,1),\qquad n=2431t,
\]
the first regular factors have:
\[
\begin{array}{c|c|c}
  p & \deg T^{\mathrm{regular}}_p & \text{regular }t\text{-roots} \\
  \hline
  101 & 7 & \{10,22,25,26,30,38,89\} \\
  103 & 12 & \{4,9,12,17,20,24,25,32,50,51,58,89\} \\
  107 & 6 & \{4,39,47,57,59,95\}.
\end{array}
\]
In all three cases, every regular gcd has degree \(1\) in \(a\).

The regular degree is not stable across these primes. Therefore the current
data does not support a naive lift of a single stable regular factor in
\(\mathbb Z[t]\). The local obstruction is sharper, but the next step must
identify which primes are bad for the local model or add further algebraic
constraints on the regular fibers.

### Endpoint \(d-6\): regular \(a\)-root extraction

Added the regular root extractor:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_regular\_t\_root\_lift.py}.
\]
For each regular \(t\)-fiber it recomputes the four specialized eliminants
and extracts the gcd in \(\mathbb F_p[a]\). In the representative class
\[
  (2,1,2,1),\qquad n=2431t,
\]
all regular fibers over \(p=101,103,107\) have linear gcds in \(a\).

Modulo \(101\), the regular pairs \((t,a)\) are:
\[
  (10,55),(22,38),(25,49),(26,53),(30,41),(38,55),(89,70).
\]
Modulo \(103\), they are:
\[
\begin{aligned}
  &(4,96),(9,71),(12,36),(17,18),(20,59),(24,28),\\
  &(25,59),(32,20),(50,77),(51,7),(58,100),(89,18).
\end{aligned}
\]
Modulo \(107\), they are:
\[
  (4,0),(39,83),(47,65),(57,41),(59,7),(95,101).
\]

The first new geometric filter appears at \(p=107\): the fiber \(t=4\) has
common root \(a=0\), so it is killed by the saturation in \(a\). The remaining
regular fibers have nonzero \(a\)-roots. The next filter should evaluate the
corresponding \(Y\)-root and \(z\)-root degeneracy conditions.

### Endpoint \(d-6\): local geometric lift check on regular fibers

Added the geometric lift checker:
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_regular\_t\_geometry\_check.py}.
\]
For each regular local \(t\)-fiber it extracts the common \(a\)-root from the
four \(a\)-eliminants, then tests every \(Y\in\mathbb F_p\) against the full
reduced system
\[
  F=R_3=R_4=R_5=R_6=0.
\]
Every actual lift is then checked for the geometric degeneracies
\[
  a=0,\quad Y=0,\quad Y=a,\quad z=0,\quad z=a,\quad z=Y
\]
and for hidden denominator failures.

For the representative class
\[
  (2,1,2,1),\qquad n=2431t,
\]
the regular fibers over \(p=101,103,107\) do not lift to any \(Y\)-root of the
full system:
\[
\begin{array}{c|c|c}
  p & \text{regular }t\text{-roots} & \text{geometric survivors} \\
  \hline
  101 & \{10,22,25,26,30,38,89\} & \varnothing \\
  103 & \{4,9,12,17,20,24,25,32,50,51,58,89\} & \varnothing \\
  107 & \{4,39,47,57,59,95\} & \varnothing.
\end{array}
\]
The \(p=107\), \(t=4\) fiber is also killed by \(a=0\). No hidden denominator
failure is needed in these tests: the obstruction is already `no_Y_solution`.

This is the first local certificate that the regular \(a\)-gcd fibers are
projection artifacts: they survive in the \(a\)-eliminants but do not lift to
solutions of the full \((a,Y)\)-system. The result currently covers this
representative CRT class only; the same lift check should now be run across
the remaining finite regular classes.
