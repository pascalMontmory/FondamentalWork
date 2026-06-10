# Casas-Alvero: the five-root frontier

Date: 2026-06-10.

This file records the first genuinely live configuration after the known
Laterveer-Ounaies obstruction: any nontrivial counterexample must have at least
five distinct roots.

## 1. Normal form

Let \(f\) be a hypothetical nontrivial Casas-Alvero polynomial of degree \(d\).
After translation, the centroid root is \(0\). Thus we may write the distinct
roots as
\[
  0,\ a_1,\ldots,a_s,
\]
with multiplicities
\[
  m_0,m_1,\ldots,m_s,
\]
where \(s\ge4\), and
\[
  d=m_0+m_1+\cdots+m_s.
\]

The centroid condition is
\[
  \sum_{i=1}^s m_i a_i=0.
\]

The known five-root theorem says that the first possible case is
\[
  s=4.
\]

So the frontier normal form is
\[
  f(x)=x^{m_0}\prod_{i=1}^4(x-a_i)^{m_i},
  \qquad
  \sum_{i=1}^4m_i a_i=0.
\]

## 2. Power sums

Define
\[
  P_k=\sum_{i=1}^4m_i a_i^k.
\]
Then \(P_1=0\). The top derivative polynomials are:
\[
  Q_1(x)=x,
\]
\[
  Q_2(x)=x^2-\frac{P_2}{d(d-1)},
\]
\[
  Q_3(x)=x^3-\frac{3P_2}{d(d-1)}x
  -\frac{2P_3}{d(d-1)(d-2)}.
\]

For \(f\) to be Casas-Alvero, the finite set
\[
  A=\{0,a_1,a_2,a_3,a_4\}
\]
must hit each equation
\[
  Q_k(x)=0,\qquad k=1,\ldots,d-1.
\]

Already the second derivative condition gives the sharp dichotomy:

Either
\[
  P_2=0,
\]
or there exists \(i\in\{1,2,3,4\}\) such that
\[
  a_i^2=\frac{P_2}{d(d-1)}.
\]

## 3. First obstruction: no asymmetric second moment hit

Suppose \(P_2\ne0\) and \(Q_2\) hits the root \(a_1\). Then
\[
  P_2=d(d-1)a_1^2.
\]
Substituting into \(Q_3(a_j)=0\) for some \(j\) gives
\[
  a_j^3-3a_1^2a_j
  =
  \frac{2P_3}{d(d-1)(d-2)}.
\]

The right-hand side is independent of \(j\). Therefore any two roots hit by
\(Q_3\) must have the same value under the cubic map
\[
  \Phi_{a_1}(z)=z^3-3a_1^2z.
\]

This is useful because \(\Phi_{a_1}(z)\) has the Chebyshev symmetry
\[
  \Phi_{a_1}(2a_1\cos\theta)=2a_1^3\cos(3\theta).
\]

So a five-root counterexample with \(P_2\ne0\) must arrange its roots on fibers
of a cubic Chebyshev-type map determined by whichever root is selected by
\(Q_2\).

This is a rigid, non-generic condition.

## 4. Isotropic case

The alternative is
\[
  P_2=0.
\]
Then \(Q_2(x)=x^2\), so the second derivative condition is absorbed by the
centroid root \(0\).

The third derivative becomes
\[
  Q_3(x)=x^3-\frac{2P_3}{d(d-1)(d-2)}.
\]
Thus one of the nonzero roots must satisfy
\[
  a_i^3=\frac{2P_3}{d(d-1)(d-2)}.
\]

So the first live five-root case splits into:

1. **anisotropic moment case** \(P_2\ne0\), controlled by the cubic
   Chebyshev fiber condition;
2. **isotropic moment case** \(P_2=0\), controlled first by a cubic moment
   equation.

## 5. Current status

This is not yet a solution of Casas-Alvero.

It is the first compact formal system where a new proof could plausibly enter.
The non-standard route suggested here is to treat the top derivative
conditions as a finite dynamical incidence problem:

\[
  A\cap Z(Q_k)\ne\varnothing
  \qquad(k=1,\ldots,d-1),
\]

where \(A\) is a fixed five-point root set and \(Q_k\) is determined by the
moments of \(A\) with multiplicities.

## 6. A real-root gap obstruction

The second top derivative already gives a useful exclusion for real-rooted
configurations.

Proposition. Let \(f\) be a nontrivial Casas-Alvero polynomial all of whose
roots are real. Translate so that the centroid root is \(0\), and write the
roots, with multiplicity, as
\[
  \alpha_1,\ldots,\alpha_d\in\mathbb R,
  \qquad
  \sum_{\nu=1}^d\alpha_\nu=0.
\]
Let
\[
  R=\max_\nu |\alpha_\nu|.
\]
Then \(f\) has a nonzero root \(a\) satisfying
\[
  0<|a|\le \frac{R}{\sqrt{d-1}}.
\]

Proof.

Since \(f\) is nontrivial and real-rooted,
\[
  P_2=\sum_{\nu=1}^d\alpha_\nu^2>0.
\]
The normalized \((d-2)\)-nd derivative is
\[
  Q_2(x)=x^2-\frac{P_2}{d(d-1)}.
\]
The Casas-Alvero condition forces \(Q_2\) to vanish at some root \(a\) of
\(f\). Because \(P_2>0\), this root is nonzero and satisfies
\[
  a^2=\frac{P_2}{d(d-1)}.
\]
But
\[
  P_2=\sum_{\nu=1}^d\alpha_\nu^2\le dR^2.
\]
Therefore
\[
  a^2\le \frac{R^2}{d-1},
\]
which proves the claim.

Corollary. A real-rooted centered polynomial cannot be Casas-Alvero if its
only root in the interval
\[
  \left[-\frac{R}{\sqrt{d-1}},\frac{R}{\sqrt{d-1}}\right]
\]
is the centroid root \(0\).

This is a genuine gap obstruction: a real counterexample must place a distinct
root extremely close to its barycenter, within a factor \(1/\sqrt{d-1}\) of the
outer radius.

## 7. Consequence for the five-root frontier over the real line

In the five-root normal form
\[
  f(x)=x^{m_0}\prod_{i=1}^4(x-a_i)^{m_i},
  \qquad
  a_i\in\mathbb R,
  \qquad
  \sum_{i=1}^4m_i a_i=0,
\]
put
\[
  R=\max_i |a_i|.
\]
If this is a Casas-Alvero polynomial, then one of the four nonzero roots
satisfies
\[
  |a_i|\le \frac{R}{\sqrt{d-1}}.
\]

Thus every real five-root counterexample must be highly unbalanced: at least
one nonzero root must lie very close to the centroid compared with the
diameter of the root set.

For example, after scaling so that \(R=1\), the root set must contain a
nonzero point in
\[
  \left[-\frac1{\sqrt{d-1}},\frac1{\sqrt{d-1}}\right].
\]

So for large degree, the five-root real frontier is forced into a singular
configuration with one nonzero root converging to the centroid.

## 8. Cubic gap obstruction

The next top derivative makes the localization sharper.

Proposition. Keep the hypotheses of the real-rooted proposition. Suppose the
root \(a\) is selected by \(Q_2\), so that
\[
  a^2=\frac{P_2}{d(d-1)}.
\]
Let \(b\) be a root of \(f\) selected by \(Q_3\), i.e. \(Q_3(b)=0\). Then
\[
  \left|b(b^2-3a^2)\right|
  \le
  \frac{2R^3}{(d-1)(d-2)}.
\]

Proof.

Since \(P_2=d(d-1)a^2\), the cubic top derivative is
\[
  Q_3(x)
  =
  x^3-3a^2x-\frac{2P_3}{d(d-1)(d-2)}.
\]
If \(Q_3(b)=0\), then
\[
  b(b^2-3a^2)
  =
  \frac{2P_3}{d(d-1)(d-2)}.
\]
But for real roots,
\[
  |P_3|
  =
  \left|\sum_{\nu=1}^d\alpha_\nu^3\right|
  \le
  \sum_{\nu=1}^d|\alpha_\nu|^3
  \le
  dR^3.
\]
The claimed inequality follows.

Corollary. After scaling \(R=1\), a real-rooted Casas-Alvero polynomial must
have roots \(a,b\) such that
\[
  0<|a|\le\frac1{\sqrt{d-1}}
\]
and
\[
  |b(b^2-3a^2)|
  \le
  \frac{2}{(d-1)(d-2)}.
\]

Thus \(b\) must lie close to one of the three points
\[
  0,\quad \sqrt3\,a,\quad -\sqrt3\,a.
\]

This is the beginning of a local cascade: top derivative conditions force
actual roots to accumulate near the centroid at scales controlled by
\(d^{-1/2}\), then \(d^{-1}\), and so on. A five-root real counterexample can
therefore not be a generic five-point configuration; it must satisfy a nested
near-resonance pattern.

## 9. Quartic cascade

The fourth top derivative gives the next explicit incidence equation. With
the same centered notation,
\[
  P_k=\sum_{\nu=1}^d\alpha_\nu^k,
  \qquad P_1=0,
\]
Newton's identities give
\[
  e_2=-\frac{P_2}{2},\qquad
  e_3=\frac{P_3}{3},\qquad
  e_4=\frac{P_2^2/2-P_4}{4}.
\]
Hence
\[
  Q_4(x)
  =
  x^4-\frac{6P_2}{d(d-1)}x^2
  -\frac{8P_3}{d(d-1)(d-2)}x
  +
  \frac{3P_2^2-6P_4}{d(d-1)(d-2)(d-3)}.
\]

If \(a\) is selected by \(Q_2\), so that
\[
  P_2=d(d-1)a^2,
\]
and \(b\) is selected by \(Q_3\), so that
\[
  P_3=\frac{d(d-1)(d-2)}{2}\,b(b^2-3a^2),
\]
then any root \(c\) selected by \(Q_4\) must satisfy
\[
  c^4-6a^2c^2-4b(b^2-3a^2)c
  +
  \frac{3d(d-1)a^4-6P_4/(d(d-1))}
       {(d-2)(d-3)}
  =0.
\]

In the real normalized case \(R=1\), the unknown constant term obeys the crude
bound
\[
  \left|
  \frac{3P_2^2-6P_4}{d(d-1)(d-2)(d-3)}
  \right|
  \le
  \frac{3d^2+6d}{d(d-1)(d-2)(d-3)}
  =
  \frac{3d+6}{(d-1)(d-2)(d-3)}.
\]

Thus \(c\) must be a root of the quartic skeleton
\[
  x^4-6a^2x^2-4b(b^2-3a^2)x
\]
up to an error of size \(O(d^{-2})\).

Combined with
\[
  |a|=O(d^{-1/2}),\qquad
  |b(b^2-3a^2)|=O(d^{-2}),
\]
this forces the next selected root \(c\) into a still narrower algebraic
neighborhood of the centroid and the Chebyshev fibers already created by
\(a\) and \(b\).

This quartic formula is the first point where the five-root frontier becomes
overdetermined: the same four nonzero roots must repeatedly serve as exact
zeros of increasingly rigid moment polynomials.

## 10. Taylor-coefficient cover formulation

There is a second formal way to view the same obstruction, useful for future
work because it avoids recomputing derivatives.

Let the distinct roots be
\[
  A=\{a_0,\ldots,a_s\},
\]
with multiplicities \(m_i\), and write
\[
  f(x)=C\prod_{i=0}^s(x-a_i)^{m_i}.
\]

For a fixed root \(a_i\), expand \(f\) at \(a_i\):
\[
  f(a_i+y)=
  C\,y^{m_i}
  \prod_{j\ne i}(a_i-a_j+y)^{m_j}
  =
  \sum_{\ell=0}^d c_{i,\ell}y^\ell.
\]

Then
\[
  f^{(\ell)}(a_i)=\ell!\,c_{i,\ell}.
\]

So \(f\) is Casas-Alvero if and only if, for every
\[
  \ell=1,\ldots,d-1,
\]
there exists a root \(a_i\in A\) such that
\[
  c_{i,\ell}=0.
\]

The automatic zeros are exactly
\[
  c_{i,\ell}=0\qquad(0\le \ell<m_i).
\]
All other zeros are recycled zeros of the local polynomial
\[
  G_i(y)=\prod_{j\ne i}(a_i-a_j+y)^{m_j}.
\]

Equivalently, the high derivative part of Casas-Alvero asks the finite family
of local products \(G_i\) to have missing coefficients whose index sets cover
all non-automatic derivative orders.

For an extreme real root \(a_i\), all numbers \(a_i-a_j\) have the same sign.
Hence all coefficients of \(G_i\) are nonzero. Therefore an extreme real root
can never provide a recycled zero; it only covers the automatic range
\[
  0\le\ell<m_i.
\]

Thus in a real-rooted counterexample, every derivative order
\[
  \ell\ge \max(m_{\min},m_{\max})
\]
must be covered by an interior root.

In the five-root real frontier, after ordering
\[
  r_1<r_2<r_3<r_4<r_5,
\]
only \(r_2,r_3,r_4\) can provide recycled zeros. The endpoint roots \(r_1,r_5\)
are purely automatic. This reduces the live covering problem to three local
generating polynomials:
\[
  G_2,\quad G_3,\quad G_4.
\]

This is a precise finite target: prove that three such mixed-sign products
cannot cover all remaining coefficient indices.

## 11. Electrostatic obstruction for the first recycled coefficients

The Taylor-coefficient cover has a useful local obstruction over the real
line.

Keep the real-rooted notation
\[
  r_1<r_2<\cdots<r_s,
  \qquad
  f(x)=C\prod_{j=1}^s(x-r_j)^{m_j}.
\]
Fix a root \(r_i\), and write
\[
  f(r_i+y)=C\,y^{m_i}G_i(y),
  \qquad
  G_i(y)=\prod_{j\ne i}(r_i-r_j+y)^{m_j}.
\]
Put
\[
  B_i=G_i(0)=\prod_{j\ne i}(r_i-r_j)^{m_j}\ne0
\]
and define the reciprocal power sums
\[
  S_i^{(q)}=\sum_{j\ne i}\frac{m_j}{(r_i-r_j)^q}.
\]

Then the first recycled coefficient is
\[
  [y]G_i(y)=B_iS_i^{(1)}.
\]
Thus \(r_i\) can cover the derivative order \(m_i+1\) if and only if
\[
  S_i^{(1)}=0.
\]

This is an exact equilibrium equation:
\[
  \sum_{j<i}\frac{m_j}{r_i-r_j}
  =
  \sum_{j>i}\frac{m_j}{r_j-r_i}.
\]
The weighted repulsion from the left and from the right must balance.

Now consider the second recycled coefficient. Since
\[
  \frac{G_i'(y)}{G_i(y)}
  =
  \sum_{j\ne i}\frac{m_j}{r_i-r_j+y},
\]
we have
\[
  G_i''(0)
  =
  B_i\left((S_i^{(1)})^2-S_i^{(2)}\right).
\]
Therefore
\[
  [y^2]G_i(y)
  =
  \frac{B_i}{2}\left((S_i^{(1)})^2-S_i^{(2)}\right).
\]

If the first recycled coefficient vanishes, then
\[
  [y^2]G_i(y)
  =
  -\frac{B_i}{2}S_i^{(2)}.
\]
But
\[
  S_i^{(2)}=\sum_{j\ne i}\frac{m_j}{(r_i-r_j)^2}>0.
\]
Hence
\[
  [y]G_i(y)=0
  \quad\Longrightarrow\quad
  [y^2]G_i(y)\ne0.
\]

Proposition. For a real-rooted polynomial, no root can simultaneously cover
its first two recycled derivative orders
\[
  m_i+1
  \quad\text{and}\quad
  m_i+2.
\]

Equivalently,
\[
  f^{(m_i+1)}(r_i)=0
  \quad\Longrightarrow\quad
  f^{(m_i+2)}(r_i)\ne0.
\]

This is independent of the Casas-Alvero condition; it is a structural fact
about real-rooted polynomials.

## 12. Consequence for the five-root real frontier

For a hypothetical five-root real counterexample
\[
  r_1<r_2<r_3<r_4<r_5,
\]
the endpoint roots \(r_1,r_5\) provide no recycled zeros at all. The interior
roots \(r_2,r_3,r_4\) may provide recycled zeros, but each of them has a forced
gap:
\[
  m_i+1\text{ covered at }r_i
  \quad\Longrightarrow\quad
  m_i+2\text{ not covered at }r_i.
\]

Thus the cover of derivative orders cannot contain a two-step local block
coming from a single interior root immediately after its multiplicity. Any
attempt to cover all derivative orders above the endpoint multiplicities must
alternate between different interior roots, subject to their three independent
electrostatic balance equations
\[
  S_2^{(1)}=0,\qquad S_3^{(1)}=0,\qquad S_4^{(1)}=0
\]
whenever the corresponding first recycled order is used.

This gives a new finite obstruction:

1. endpoint roots only cover automatic ranges;
2. each interior root can start recycling only at an exact equilibrium point;
3. after such a start, the immediately following recycled order at the same
   root is forbidden.

The remaining real five-root task is therefore a constrained covering problem
with three interior roots and forced local gaps.

## 13. Separation-ratio exclusion

The gap obstruction can be stated as a clean geometric exclusion.

Let \(f\) be real-rooted and centered at the centroid root \(0\). Define
\[
  R=\max_\nu|\alpha_\nu|,
  \qquad
  \delta=\min\{|\alpha_\nu|:\alpha_\nu\ne0\}.
\]

If \(f\) is a nontrivial Casas-Alvero polynomial, then
\[
  \delta\le \frac{R}{\sqrt{d-1}}.
\]

Equivalently,
\[
  d\le 1+\left(\frac{R}{\delta}\right)^2.
\]

Therefore:

Proposition. A centered real-rooted polynomial of degree
\[
  d>1+\left(\frac{R}{\delta}\right)^2
\]
cannot be Casas-Alvero.

This is a scale-invariant obstruction: it depends only on the ratio between
the outer radius and the closest nonzero root to the centroid.

### Arithmetic-progression corollary

Suppose the distinct roots are contained in a centered arithmetic progression
\[
  -Mh,\ldots,-h,0,h,\ldots,Mh,
\]
and include at least one endpoint \(\pm Mh\). Then
\[
  R=Mh,\qquad \delta=h,
\]
so every real-rooted Casas-Alvero candidate of this type must satisfy
\[
  d\le M^2+1.
\]

For the first five-root symmetric progression
\[
  -2h,\ -h,\ 0,\ h,\ 2h,
\]
this gives
\[
  d\le5.
\]

But a nontrivial Casas-Alvero counterexample is known to require at least five
distinct roots, and degree \(5\) would force all five roots to be simple. A
simple-root polynomial cannot be Casas-Alvero because \(f\) and \(f'\) have no
common root. Hence:

Corollary. No real-rooted Casas-Alvero counterexample has distinct roots
\[
  -2h,\ -h,\ 0,\ h,\ 2h
\]
for any \(h\ne0\), regardless of multiplicities.

More generally, the separation-ratio exclusion eliminates every centered
real-rooted configuration whose nearest nonzero root is too far from the
centroid relative to the outer radius.
