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

## 14. Top-order anchoring

The two highest derivative orders are anchored in a particularly rigid way.

Let \(f\) be centered, so that
\[
  \sum_{\nu=1}^d\alpha_\nu=0,
\]
and let \(r\) be a distinct root of multiplicity \(m\). Write
\[
  f(r+y)=C\,y^mG_r(y),
  \qquad
  D=\deg G_r=d-m.
\]
The coefficient of \(y^{D-1}\) in \(G_r\) is
\[
  \sum_{\alpha_\nu\ne r}(r-\alpha_\nu).
\]
Counting multiplicities, this equals
\[
  (d-m)r-\sum_{\alpha_\nu\ne r}\alpha_\nu.
\]
Since the total sum of all roots is \(0\), we have
\[
  \sum_{\alpha_\nu\ne r}\alpha_\nu=-mr.
\]
Therefore
\[
  [y^{D-1}]G_r(y)=dr.
\]

But derivative order \(d-1\) at \(r\) corresponds exactly to this coefficient:
\[
  f^{(d-1)}(r)=0
  \quad\Longleftrightarrow\quad
  [y^{D-1}]G_r(y)=0.
\]
Hence
\[
  f^{(d-1)}(r)=0
  \quad\Longleftrightarrow\quad
  r=0.
\]

So in centered normal form, the top derivative condition is covered uniquely
by the centroid root.

Now consider the next order. The normalized top derivative is
\[
  Q_2(x)=x^2-\frac{P_2}{d(d-1)}.
\]
For a nontrivial real-rooted polynomial,
\[
  P_2>0,
\]
so
\[
  Q_2(0)\ne0.
\]
Thus the centroid root cannot cover derivative order \(d-2\). Any
Casas-Alvero candidate must use a nonzero root \(a\) satisfying
\[
  a^2=\frac{P_2}{d(d-1)}.
\]
In the real-rooted case this root cannot be the centroid and is small:
\[
  |a|\le\frac{R}{\sqrt{d-1}}<R
  \qquad(d\ge3).
\]
Moreover it cannot be an endpoint root. Indeed, for an endpoint root \(r\),
all shifts \(r-\alpha_\nu\) appearing in \(G_r\) have the same sign, so every
coefficient of \(G_r\) is nonzero. Hence an endpoint root provides no recycled
zeros at all; it only provides the automatic zeros below its multiplicity. In
a five-root candidate, every endpoint multiplicity is at most \(d-4\), so the
order \(d-2\) is not automatic at an endpoint either.

Proposition. In any centered, nontrivial, real-rooted Casas-Alvero candidate:

1. \(f^{(d-1)}\) is covered uniquely at the centroid root \(0\);
2. \(f^{(d-2)}\) is covered at a nonzero interior root \(a\);
3. the covering root \(a\) satisfies
   \[
     |a|\le R/\sqrt{d-1}.
   \]

For the real five-root frontier \(r_1<r_2<r_3<r_4<r_5\), this means the top
two derivative orders are forced into the pattern
\[
  d-1\mapsto 0,
  \qquad
  d-2\mapsto r_i\in\{r_2,r_3,r_4\}\setminus\{0\},
\]
where \(0\) is whichever one of \(r_2,r_3,r_4\) is the centroid root.

Thus the \(d-2\) covering root is an interior nonzero root, never an endpoint.

## 15. Three-top-order pattern in the real five-root frontier

The previous anchoring extends one more step with a clean dichotomy.

In centered notation,
\[
  Q_3(x)=x^3-\frac{3P_2}{d(d-1)}x
  -\frac{2P_3}{d(d-1)(d-2)}.
\]
Thus
\[
  Q_3(0)=
  -\frac{2P_3}{d(d-1)(d-2)}.
\]

Therefore:

* if \(P_3=0\), the centroid root \(0\) covers derivative order \(d-3\);
* if \(P_3\ne0\), the centroid root cannot cover \(d-3\), so the order must be
  covered by a nonzero root \(b\) satisfying
  \[
    b^3-\frac{3P_2}{d(d-1)}b
    =
    \frac{2P_3}{d(d-1)(d-2)}.
  \]

In the real five-root frontier, endpoint roots cannot cover any of the three
orders
\[
  d-1,\quad d-2,\quad d-3.
\]
Indeed, endpoint roots have no recycled zeros, and their multiplicities are at
most \(d-4\), so none of these orders is automatic there.

Hence all three top orders must be covered by the three interior roots.

Proposition. Let a real-rooted five-root Casas-Alvero candidate be ordered as
\[
  r_1<r_2<r_3<r_4<r_5.
\]
Then:

1. \(d-1\) is covered by the centroid root \(0\), which is one of
   \(r_2,r_3,r_4\);
2. \(d-2\) is covered by an interior nonzero root
   \[
     a\in\{r_2,r_3,r_4\}\setminus\{0\};
   \]
3. if \(P_3\ne0\), then \(d-3\) is also covered by an interior nonzero root
   \[
     b\in\{r_2,r_3,r_4\}\setminus\{0\}
   \]
   lying on the cubic fiber
   \[
     b^3-3a^2b
     =
     \frac{2P_3}{d(d-1)(d-2)},
   \]
   where \(a^2=P_2/(d(d-1))\);
4. if \(P_3=0\), then \(d-3\) may be covered by the centroid root \(0\), and
   the cubic top derivative factors as
   \[
     Q_3(x)=x(x^2-3a^2).
   \]

Thus the top three derivative orders leave only two possible signatures:

* **even-moment signature:** \(P_3=0\), with
  \[
    d-1\mapsto0,\quad d-2\mapsto a,\quad d-3\mapsto0;
  \]
* **asymmetric signature:** \(P_3\ne0\), with
  \[
    d-1\mapsto0,\quad d-2\mapsto a,\quad d-3\mapsto b,
  \]
  where \(a,b\) are nonzero interior roots.

This gives a small finite branching at the top of the covering problem. The
remaining derivative orders must extend one of these two signatures without
using endpoints for recycled zeros.

## 16. Repeated-root compression

There is a sharper estimate when the same absolute root participates in the
top-order cover more than once.

Assume again that \(a\) is selected by \(Q_2\), so that
\[
  a^2=\frac{P_2}{d(d-1)}.
\]
Suppose that \(Q_3\) is covered by either \(a\) or \(-a\). Then
\[
  |a|\le \frac{R}{d-2}.
\]

Proof.

If \(Q_3(a)=0\), then
\[
  a^3-3a^3-\frac{2P_3}{d(d-1)(d-2)}=0,
\]
so
\[
  P_3=-d(d-1)(d-2)a^3.
\]
If \(Q_3(-a)=0\), the same computation gives
\[
  P_3=d(d-1)(d-2)a^3.
\]
In either case,
\[
  |P_3|=d(d-1)(d-2)|a|^3.
\]

But for real roots bounded by \(R\),
\[
  |P_3|
  =
  \left|\sum_{\nu=1}^d\alpha_\nu^3\right|
  \le
  R\sum_{\nu=1}^d\alpha_\nu^2
  =
  RP_2
  =
  Rd(d-1)a^2.
\]
Since \(a\ne0\), division gives
\[
  |a|\le \frac{R}{d-2}.
\]

Corollary. In the real five-root frontier, if no nonzero interior root lies in
\[
  \left[-\frac{R}{d-2},\frac{R}{d-2}\right],
\]
then the roots covering \(d-2\) and \(d-3\) cannot be opposites or identical in
absolute value. In the asymmetric signature, \(d-3\) must then be covered by
the other nonzero interior root.

This sharpens the top-order branching: either the cover repeats the same
absolute root and forces a \(1/d\)-scale near-collision with the centroid, or
the cover must use two genuinely different nonzero interior roots.

## 17. Four-top-order branching

The next step is to make the quartic incidence from Section 9 part of the
finite top-order cover.

In the real five-root frontier
\[
  r_1<r_2<r_3<r_4<r_5,
\]
the endpoint multiplicities satisfy
\[
  m_1,m_5\le d-4,
\]
because the other four distinct roots have multiplicity at least \(1\). Since
endpoint roots have no recycled zeros, neither endpoint can cover any of the
four derivative orders
\[
  d-1,\quad d-2,\quad d-3,\quad d-4.
\]
Thus all four top orders must be covered by the three interior roots.

The order \(d-4\) is governed by
\[
  Q_4(x)
  =
  x^4-\frac{6P_2}{d(d-1)}x^2
  -\frac{8P_3}{d(d-1)(d-2)}x
  +
  \frac{3P_2^2-6P_4}{d(d-1)(d-2)(d-3)}.
\]
At the centroid root,
\[
  Q_4(0)=
  \frac{3P_2^2-6P_4}{d(d-1)(d-2)(d-3)}.
\]
Therefore \(d-4\) can be covered by the centroid if and only if
\[
  P_4=\frac{P_2^2}{2}.
\]
If this identity fails, then \(d-4\) must be covered by a nonzero interior root
\[
  c\in\{r_2,r_3,r_4\}\setminus\{0\}
\]
satisfying the exact quartic equation \(Q_4(c)=0\).

This gives the four-top-order branch:

* \(d-1\mapsto0\);
* \(d-2\mapsto a\ne0\), with
  \[
    a^2=\frac{P_2}{d(d-1)};
  \]
* \(d-3\mapsto0\) if \(P_3=0\), otherwise \(d-3\mapsto b\ne0\) with
  \[
    b^3-3a^2b=\frac{2P_3}{d(d-1)(d-2)};
  \]
* \(d-4\mapsto0\) if \(P_4=P_2^2/2\), otherwise \(d-4\mapsto c\ne0\) with
  \[
    Q_4(c)=0.
  \]

There is an immediate compression in the centroid branch. Suppose
\[
  P_4=\frac{P_2^2}{2}.
\]
For real roots bounded by \(R\),
\[
  P_4=\sum_{\nu=1}^d\alpha_\nu^4
  \le
  R^2\sum_{\nu=1}^d\alpha_\nu^2
  =
  R^2P_2.
\]
Since the candidate is nontrivial and real-rooted, \(P_2>0\). Hence
\[
  \frac{P_2}{2}\le R^2.
\]
Using \(P_2=d(d-1)a^2\), we obtain
\[
  |a|\le\frac{\sqrt2\,R}{\sqrt{d(d-1)}}.
\]

Proposition. In the real five-root frontier, if the centroid root covers both
\[
  d-1
  \quad\text{and}\quad
  d-4,
\]
then the nonzero root forced by \(d-2\) lies at distance at most
\[
  \frac{\sqrt2\,R}{\sqrt{d(d-1)}}
\]
from the centroid.

This is a stronger \(1/d\)-scale localization than the universal
\(R/\sqrt{d-1}\) bound. Consequently the top four orders leave only two
possibilities:

1. the cover returns to the centroid at \(d-4\), forcing the near-collision
   \(|a|=O(R/d)\);
2. the order \(d-4\) must be absorbed by one of the two nonzero interior roots,
   subject to the exact quartic equation \(Q_4(c)=0\).

Either way, the four highest derivatives already force repeated use of the
three interior roots and exclude the endpoints completely.

## 18. Non-Q2 double-cover clustering

The four-top-order branch forces repetition. The cleanest repeated case is
when one nonzero root, not necessarily the root selected by \(Q_2\), covers
both \(d-3\) and \(d-4\).

Assume \(a\) is selected by \(Q_2\), so that
\[
  a^2=\frac{P_2}{d(d-1)}.
\]
Suppose a nonzero root \(b\) satisfies
\[
  Q_3(b)=0
  \qquad\text{and}\qquad
  Q_4(b)=0.
\]
Then
\[
  P_3=\frac{d(d-1)(d-2)}{2}\,b(b^2-3a^2).
\]
Substitute this into \(Q_4(b)=0\). The quartic equation becomes
\[
  b^4-6a^2b^2-4b^2(b^2-3a^2)
  +
  \frac{3P_2^2-6P_4}{d(d-1)(d-2)(d-3)}
  =
  0.
\]
Hence
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

This identity gives an immediate localization. Since \(P_4\ge0\) for real
roots,
\[
  d(d-1)(d-2)(d-3)b^2(b^2-2a^2)\le P_2^2.
\]
Put
\[
  t=\frac{b^2}{a^2}.
\]
Using \(P_2=d(d-1)a^2\), we obtain
\[
  t(t-2)\le
  \frac{d(d-1)}{(d-2)(d-3)}.
\]
Therefore
\[
  t\le
  1+
  \sqrt{
    1+\frac{d(d-1)}{(d-2)(d-3)}
  }.
\]

Proposition. If the same nonzero root \(b\) covers \(d-3\) and \(d-4\), then
\[
  |b|
  \le
  \Lambda_d |a|,
  \qquad
  \Lambda_d=
  \left(
    1+
    \sqrt{
      1+\frac{d(d-1)}{(d-2)(d-3)}
    }
  \right)^{1/2}.
\]
In particular, since \(d\ge5\) on the five-root frontier,
\[
  |b|\le \Lambda_d\frac{R}{\sqrt{d-1}},
\]
and \(\Lambda_d\to\sqrt{1+\sqrt2}\) as \(d\to\infty\).

Thus the non-Q2 double-cover branch also clusters near the centroid. It cannot
send the \(d-3\) and \(d-4\) conditions to a root at macroscopic distance while
\(a\) is forced near \(0\).

Pigeonhole corollary. Work in the real five-root frontier and assume the
noncentroid branch
\[
  P_3\ne0,
  \qquad
  P_4\ne \frac{P_2^2}{2}.
\]
Then \(d-3\) and \(d-4\) are both covered by nonzero interior roots. Since
there are only two nonzero interior roots, one of the following must happen:

1. \(d-3\) is covered by a root with square \(a^2\), giving the previous
   repeated-root compression
   \[
     |a|\le \frac{R}{d-2};
   \]
2. \(d-4\) is covered by a root with square \(a^2\), so the quartic equation
   repeats the \(Q_2\)-root;
3. the other nonzero interior root covers both \(d-3\) and \(d-4\), and hence
   satisfies the clustering bound above.

So every noncentroid four-top-order branch either repeats the \(Q_2\) root or
forces the remaining nonzero interior root into the same \(O(R/\sqrt d)\)
centroid cluster.

## 19. The fifth top derivative and the endpoint gate

The next derivative is the first one where endpoint roots can re-enter, but
only through a very narrow multiplicity gate.

Let
\[
  D_j=d(d-1)\cdots(d-j+1).
\]
Using Newton's identities with \(P_1=0\), we have
\[
  e_2=-\frac{P_2}{2},
  \qquad
  e_3=\frac{P_3}{3},
  \qquad
  e_4=\frac{P_2^2/2-P_4}{4},
\]
and
\[
  e_5=\frac{P_5}{5}-\frac{P_2P_3}{6}.
\]
Therefore the normalized fifth top derivative is
\[
  Q_5(x)
  =
  x^5
  -\frac{10P_2}{D_2}x^3
  -\frac{20P_3}{D_3}x^2
  +\frac{15P_2^2-30P_4}{D_4}x
  +\frac{20P_2P_3-24P_5}{D_5}.
\]

In particular,
\[
  Q_5(0)=\frac{20P_2P_3-24P_5}{D_5}.
\]
Thus the centroid root covers derivative order \(d-5\) if and only if
\[
  5P_2P_3=6P_5.
\]

Now consider endpoints in the real five-root frontier. An endpoint root has no
recycled zeros, so it can cover \(d-5\) only automatically. For an endpoint of
multiplicity \(m\), automatic coverage of \(d-5\) requires
\[
  d-5<m,
\]
hence
\[
  m\ge d-4.
\]
But an endpoint multiplicity is always at most \(d-4\), because the other four
distinct roots have multiplicity at least \(1\). Therefore:

Proposition. In the real five-root frontier, an endpoint can cover \(d-5\) if
and only if it has multiplicity exactly \(d-4\). In that case the four other
distinct roots are all simple.

Consequently, outside the massive-endpoint branch
\[
  m_{\rm endpoint}=d-4,
\]
the fifth top order is also forced to an interior root. It then gives the
branch:

* \(d-5\mapsto0\) if
  \[
    5P_2P_3=6P_5;
  \]
* otherwise \(d-5\mapsto z\), where \(z\) is a nonzero interior root satisfying
  \[
    Q_5(z)=0.
  \]

This separates the next obstruction into two explicit cases:

1. a degenerate multiplicity branch with one endpoint of multiplicity \(d-4\)
   and all other roots simple;
2. an interior fifth-order branch governed by the quintic moment equation
   \(Q_5(z)=0\).

The first branch is combinatorially small. The second branch continues the
top-order incidence cascade entirely inside the three interior roots.

## 20. Massive-endpoint reduction

The massive-endpoint branch is not just a special way to cover \(d-5\). It
collapses the whole lower part of the Casas-Alvero cover.

Assume a real five-root candidate has an endpoint root \(e\) of multiplicity
\[
  m_e=d-4.
\]
Then the other four distinct roots are simple. Since
\[
  f(x)=(x-e)^{d-4}H(x),
  \qquad
  H(e)\ne0,
\]
we have
\[
  f^{(k)}(e)=0
  \qquad(0\le k\le d-5).
\]
Thus every derivative order
\[
  1,\ldots,d-5
\]
is automatically covered by the massive endpoint.

The endpoint still cannot cover any recycled order, and in particular cannot
cover
\[
  d-4,\quad d-3,\quad d-2,\quad d-1.
\]
Therefore, in this branch, the full Casas-Alvero condition is equivalent to
the four top-order incidences:
\[
  Q_1(0)=0,
  \qquad
  Q_2(a)=0,
  \qquad
  Q_3(b)=0,
  \qquad
  Q_4(c)=0,
\]
where \(a,b,c\) are interior roots, with \(a\ne0\). The centroid condition
already supplies \(Q_1(0)=0\), so the live content is exactly the finite system
\[
  Q_2(a)=Q_3(b)=Q_4(c)=0
\]
on the three interior roots.

There is also a geometric cost. Suppose the massive endpoint is the left
endpoint
\[
  e=-A<0,
\]
and let \(B>0\) be the right endpoint. The centroid equation has the form
\[
  -(d-4)A+x+y+B=0,
\]
where \(x,y\) are the two remaining nonzero simple roots. Since
\[
  x,y\le B,
\]
we get
\[
  (d-4)A=x+y+B\le3B.
\]
Hence
\[
  A\le\frac{3B}{d-4}\le\frac{3R}{d-4}.
\]
The right-endpoint massive case is symmetric.

Proposition. In the massive-endpoint branch, the massive endpoint itself lies
within
\[
  \frac{3R}{d-4}
\]
of the centroid.

Thus the branch has two simultaneous degeneracies:

1. one endpoint carries almost all multiplicity and automatically covers the
   low derivative orders;
2. that same endpoint must be \(O(R/d)\)-close to the centroid, while the four
   top orders are still forced onto the three interior roots.

For \(d>5\), at most one endpoint can be massive. Indeed, two endpoint
multiplicities \(d-4\) would leave at least three more simple roots, so
\[
  2(d-4)+3\le d,
\]
which implies \(d\le5\).

Therefore the five-root real frontier splits cleanly into:

* the massive-endpoint finite system, where all lower orders are automatic and
  only \(Q_2,Q_3,Q_4\) remain live;
* the non-massive branch, where \(d-5\) is also forced to the interior or to
  the centroid identity \(5P_2P_3=6P_5\).

## 21. Massive-endpoint normal form

The massive-endpoint branch can be written as a two-variable algebraic system.
After reflection if needed, assume the massive endpoint is the left endpoint.
Scale so that it is
\[
  -1.
\]
Put
\[
  n=d-4.
\]
The roots are then
\[
  -1,\quad 0,\quad u,\quad v,\quad w,
\]
where \(-1\) has multiplicity \(n\), the other four roots are simple, and the
centroid equation gives
\[
  -n+u+v+w=0.
\]
Hence
\[
  w=n-u-v.
\]

The power sums become explicit polynomials in \(u,v\):
\[
  P_k=n(-1)^k+u^k+v^k+(n-u-v)^k.
\]
Since \(d=n+4\), write
\[
  D_j=(n+4)(n+3)\cdots(n+5-j).
\]

The \(Q_2\)-condition must be covered by one of the two nonzero interior roots.
Thus for some
\[
  a\in\{u,v\},
\]
we have
\[
  D_2a^2=P_2.
\]

The \(Q_3\)-condition has the finite alternatives
\[
  P_3=0
\]
if it is covered by the centroid, or
\[
  t^3-3a^2t-\frac{2P_3}{D_3}=0
\]
for some
\[
  t\in\{u,v\}.
\]

The \(Q_4\)-condition similarly has the finite alternatives
\[
  P_4=\frac{P_2^2}{2}
\]
if it is covered by the centroid, or
\[
  s^4-6a^2s^2-\frac{8P_3}{D_3}s
  +\frac{3P_2^2-6P_4}{D_4}=0
\]
for some
\[
  s\in\{u,v\}.
\]

Therefore the massive-endpoint branch is reduced to finitely many explicit
systems in the two real variables \(u,v\), indexed by the choices
\[
  a\in\{u,v\},
  \qquad
  t\in\{0,u,v\},
  \qquad
  s\in\{0,u,v\}.
\]

The order restrictions are also explicit:
\[
  -1<u,v<n-u-v,
\]
with \(0\) lying strictly between the two endpoints. Any solution of one of
these finite systems satisfying the order restrictions gives the full
top-order cover for the massive-endpoint branch; conversely, every
massive-endpoint real five-root Casas-Alvero candidate appears in this normal
form.

This is a concrete elimination target: for each integer \(n=d-4\ge2\), rule
out finitely many two-variable systems. The original infinitely many
derivative conditions no longer appear in this branch.

## 22. One-parameter collapse after \(Q_2\)

The massive-endpoint normal form collapses further after the \(Q_2\)-root is
chosen.

Keep the normalization
\[
  -1,\quad 0,\quad u,\quad v,\quad w,
  \qquad
  w=n-u-v,
\]
with \(-1\) of multiplicity \(n=d-4\). Suppose \(Q_2\) is covered by the root
\[
  a=u.
\]
The case \(a=v\) is identical after renaming \(u,v\).

Let \(y,z\) denote the two remaining nonzero roots. Their sum is forced by the
centroid equation:
\[
  S=y+z=n-a.
\]
The \(Q_2\)-condition says
\[
  D_2a^2=P_2=n+a^2+y^2+z^2.
\]
Since
\[
  y^2+z^2=S^2-2yz,
\]
their product is forced:
\[
  p=yz
  =
  \frac{S^2+n+a^2-D_2a^2}{2}.
\]
Equivalently,
\[
  p=
  \frac{n^2+n-2na-(n+5)(n+2)a^2}{2}.
\]

Thus \(y,z\) are the two roots of the explicit quadratic
\[
  F_a(X)=X^2-SX+p.
\]
The reality condition is just
\[
  \Delta_a=S^2-4p\ge0,
\]
that is
\[
  \Delta_a
  =
  (2n^2+14n+21)a^2+2na-n(n+2)\ge0.
\]

Now define
\[
  T_0=2,\qquad T_1=S,\qquad T_k=ST_{k-1}-pT_{k-2}\quad(k\ge2).
\]
Then
\[
  T_k=y^k+z^k.
\]
Consequently every moment is a polynomial in the single variable \(a\):
\[
  M_k(a)=n(-1)^k+a^k+T_k,
  \qquad
  P_k=M_k(a).
\]

This gives a one-parameter elimination form for the whole massive-endpoint
branch.

For \(Q_3\), the finite alternatives become:
\[
  M_3(a)=0
\]
if the centroid covers \(d-3\);
\[
  M_3(a)=-D_3a^3
\]
if the same root \(a\) covers \(d-3\); or
\[
  \operatorname{Res}_X
  \left(
    F_a(X),
    X^3-3a^2X-\frac{2M_3(a)}{D_3}
  \right)=0
\]
if one of the two remaining nonzero roots covers \(d-3\).

For \(Q_4\), the finite alternatives are:
\[
  M_4(a)=\frac{M_2(a)^2}{2}
\]
if the centroid covers \(d-4\);
\[
  -5a^4-\frac{8M_3(a)}{D_3}a
  +\frac{3M_2(a)^2-6M_4(a)}{D_4}=0
\]
if the same root \(a\) covers \(d-4\); or
\[
  \operatorname{Res}_X
  \left(
    F_a(X),
    X^4-6a^2X^2-\frac{8M_3(a)}{D_3}X
    +\frac{3M_2(a)^2-6M_4(a)}{D_4}
  \right)=0
\]
if one of the two remaining nonzero roots covers \(d-4\).

Therefore, after \(Q_2\), every massive-endpoint branch is governed by
univariate equations in \(a\), plus the real-order restrictions for the roots
of \(F_a\). The two-variable system has disappeared.

This is a sharper elimination target: for each integer \(n\ge2\), one must
exclude finitely many real roots \(a\) of explicit univariate polynomial
equations satisfying
\[
  -1<a,\qquad \Delta_a\ge0,
\]
and the ordering requirement that exactly one of the two roots of \(F_a\) is
the right endpoint.

## 23. The first cubic gates in the massive branch

The one-parameter collapse makes the first two \(Q_3\)-branches completely
explicit.

Let
\[
  C_0(n,a)=2M_3(a).
\]
Then the branch where the centroid covers \(d-3\) is exactly
\[
  C_0(n,a)=0,
\]
where
\[
  \begin{aligned}
  C_0(n,a)=&
  -3a^3n^2-21a^3n-30a^3
  +3a^2n^3+21a^2n^2+30a^2n  \\
  &+3an^2+3an
  -n^3-3n^2-2n .
  \end{aligned}
\]

Similarly, let
\[
  C_a(n,a)=2\left(M_3(a)+D_3a^3\right).
\]
Then the branch where the same root \(a\) covers both \(d-2\) and \(d-3\) is
exactly
\[
  C_a(n,a)=0,
\]
where
\[
  \begin{aligned}
  C_a(n,a)=&
  2a^3n^3+15a^3n^2+31a^3n+18a^3
  +3a^2n^3+21a^2n^2+30a^2n \\
  &+3an^2+3an
  -n^3-3n^2-2n .
  \end{aligned}
\]

These are genuine cubic gates: for each fixed \(n\ge2\), the two simplest
massive-endpoint branches can have only the finitely many \(a\)-values solving
\[
  C_0(n,a)=0
  \qquad\text{or}\qquad
  C_a(n,a)=0,
\]
subject to the discriminant and ordering restrictions
\[
  \Delta_a\ge0,
  \qquad
  -1<a.
\]

The remaining \(Q_3\)-branch, where one of the two roots of \(F_a\) covers
\(d-3\), is the resultant branch already described in Section 22. Thus the
massive endpoint case now begins with two explicit cubics plus one explicit
quadratic-cubic resultant.

## 24. Interior selector for the resultant branches

The resultant branches need one further refinement. The two roots of
\[
  F_a(X)=X^2-SX+p
\]
are not symmetric for the covering problem: one is the remaining interior root
and the other is the right endpoint. The endpoint is not allowed to cover
\[
  d-3
  \quad\text{or}\quad
  d-4.
\]

Write
\[
  \Delta_a=S^2-4p,
  \qquad
  X_-=\frac{S-\sqrt{\Delta_a}}2,
  \qquad
  X_+=\frac{S+\sqrt{\Delta_a}}2.
\]
The admissible root is \(X_-\), while \(X_+\) is the right endpoint.

Let \(H(X)\) be any polynomial condition to be tested on a root of \(F_a\).
Reduce \(H\) modulo \(F_a\):
\[
  H(X)\equiv A_HX+B_H\pmod{F_a}.
\]
Then
\[
  H(X_-)=0
\]
if and only if
\[
  A_HS+2B_H=A_H\sqrt{\Delta_a}.
\]
Equivalently, this is the pair of algebraic conditions
\[
  (A_HS+2B_H)^2=A_H^2\Delta_a
\]
and
\[
  A_H(A_HS+2B_H)\ge0.
\]
The same squared equation with the opposite sign selects the endpoint root
\[
  X_+.
\]

This removes the endpoint contamination from the resultants. The condition
\[
  \operatorname{Res}(F_a,H)=0
\]
is now replaced by the sharper interior-root test
\[
  (A_HS+2B_H)^2=A_H^2\Delta_a,
  \qquad
  A_H(A_HS+2B_H)\ge0.
\]

For the \(Q_3\)-resultant branch, take
\[
  H_3(X)=D_3(X^3-3a^2X)-2M_3(a).
\]
Modulo \(F_a\),
\[
  H_3(X)\equiv A_3X+B_3.
\]
The coefficient of \(X\) is
\[
  A_3=
  \frac{(n+2)(n+3)(n+4)}2
  \left((n+1)(n+6)a^2-2na+n(n-1)\right).
\]
For every \(n\ge2\), the quadratic factor in parentheses is strictly
positive. Indeed its minimum is
\[
  n(n-1)-\frac{n^2}{(n+1)(n+6)}>0.
\]
Thus
\[
  A_3>0.
\]

Consequently the admissible \(Q_3\)-resultant branch is selected by
\[
  (A_3S+2B_3)^2=A_3^2\Delta_a,
  \qquad
  A_3S+2B_3\ge0.
\]
The endpoint branch has the same squared equation but the reverse inequality.

This is useful because the sign condition is not numerical; it is a formal
orientation of the two quadratic roots. It identifies which resultant zeros
are geometrically admissible in the massive-endpoint branch.

## 25. Admissibility strip for the \(Q_2\)-root

The one-parameter reduction also gives a simple interval for the root \(a\).
The two reconstructed roots \(X_-,X_+\) of \(F_a\) must both lie strictly to
the right of the massive endpoint \(-1\). Equivalently,
\[
  X_-+1>0,
  \qquad
  X_++1>0.
\]
In terms of \(F_a\), this implies
\[
  F_a(-1)>0.
\]
Since
\[
  F_a(-1)
  =
  \frac{(n+1)(n+2)-2(n+1)a-(n+5)(n+2)a^2}{2},
\]
every admissible \(a\) must satisfy
\[
  (n+5)(n+2)a^2+2(n+1)a-(n+1)(n+2)<0.
\]

Thus
\[
  \alpha_n<a<\beta_n,
\]
where
\[
  \alpha_n=
  \frac{-n-1-\sqrt{n^4+10n^3+34n^2+46n+21}}
       {n^2+7n+10},
\]
and
\[
  \beta_n=
  \frac{-n-1+\sqrt{n^4+10n^3+34n^2+46n+21}}
       {n^2+7n+10}.
\]

Moreover,
\[
  -1<\alpha_n<0<\beta_n<1.
\]
Indeed the quadratic
\[
  L_n(a)=(n+5)(n+2)a^2+2(n+1)a-(n+1)(n+2)
\]
satisfies
\[
  L_n(-1)=2n+6>0,
  \qquad
  L_n(0)=-(n+1)(n+2)<0,
\]
and
\[
  L_n(1)=6n+10>0.
\]

Proposition. In the massive-endpoint branch, the \(Q_2\)-root \(a\) must lie
in the explicit strip
\[
  \alpha_n<a<\beta_n\subset(-1,1).
\]

There are also two noncollision filters:
\[
  F_a(0)=p\ne0,
  \qquad
  F_a(a)\ne0.
\]
The first excludes a second copy of the centroid root, and the second excludes
a repeated nonzero root. Explicitly,
\[
  p=
  \frac{n^2+n-2na-(n+5)(n+2)a^2}{2},
\]
and
\[
  F_a(a)=
  \frac{n^2+n-4na-(n+1)(n+6)a^2}{2}.
\]

So each massive-endpoint cubic gate must be tested only on the finite interval
\[
  \alpha_n<a<\beta_n,
\]
with the two noncollision exclusions above. This is the correct domain for a
Sturm or sign argument.

## 26. Elimination of the same-root \(Q_3\) gate

One of the massive-endpoint cubic gates can already be closed.

Consider the branch where the same root \(a\) covers both
\[
  d-2
  \quad\text{and}\quad
  d-3.
\]
This is the gate
\[
  C_a(n,a)=0.
\]
The cubic discriminant is
\[
  \operatorname{disc}_a C_a
  =
  -108n^2(n+1)(n+2)(n+3)^2
  \left(3n^4+31n^3+102n^2+108n+18\right).
\]
Hence, for every \(n\ge2\), the polynomial \(C_a(n,\cdot)\) has exactly one
real root.

Now compare this root with the reality interval for \(F_a\). Let
\[
  \Delta_a=(2n^2+14n+21)a^2+2na-n(n+2).
\]
The roots reconstructed from \(F_a\) are real only when
\[
  \Delta_a\ge0.
\]

Reduce \(C_a\) modulo \(\Delta_a\). One obtains
\[
  C_a(n,a)\equiv
  \frac{n(n+3)}{(2n^2+14n+21)^2}(K_na+M_n)
  \pmod{\Delta_a},
\]
where
\[
  K_n=
  4n^5+54n^4+288n^3+783n^2+1130n+693
  >0,
\]
and
\[
  M_n=
  2n^5+18n^4+37n^3-78n^2-339n-294.
\]
Put
\[
  a_n^*=-\frac{M_n}{K_n}.
\]
A direct calculation gives
\[
  \Delta_{a_n^*}
  =
  -\frac{
    2(n+2)(2n^2+14n+21)^2
    \left(n^7+19n^6+149n^5+597n^4+1183n^3+725n^2-859n-1029\right)
  }{K_n^2}.
\]
The final polynomial in parentheses is positive for every \(n\ge2\): its
possibly negative tail satisfies
\[
  725n^2-859n-1029>0
  \qquad(n\ge2),
\]
and all higher terms are positive. Hence
\[
  \Delta_{a_n^*}<0.
\]

Therefore \(a_n^*\) lies strictly between the two real roots of \(\Delta_a\).
Since the remainder \(K_na+M_n\) has positive leading coefficient, \(C_a\)
has opposite signs at the two roots of \(\Delta_a\). The unique real root of
\[
  C_a(n,a)=0
\]
must consequently lie in the interval where
\[
  \Delta_a<0.
\]

Proposition. In the massive-endpoint branch, the same nonzero root cannot
cover both \(d-2\) and \(d-3\). Equivalently, the gate
\[
  C_a(n,a)=0
\]
has no admissible real solution.

Thus the massive-endpoint branch loses one of its three \(Q_3\)-possibilities:
after \(Q_2\), derivative order \(d-3\) must be covered either by the centroid
root or by the other interior nonzero root.

## 27. The centroid \(Q_3\) gate is finite-exceptional

The centroid gate
\[
  C_0(n,a)=0
\]
can also be almost eliminated.

Its discriminant is
\[
  \operatorname{disc}_a C_0
  =
  108n^2(n+1)(n+2)(n+3)^2(n+5)
  \left(n^5+10n^4+31n^3+26n^2-10n-10\right),
\]
which is positive for \(n\ge2\). Thus \(C_0(n,\cdot)\) has three distinct real
roots.

Let \(\delta_-<0<\delta_+\) be the two roots of
\[
  \Delta_a=(2n^2+14n+21)a^2+2na-n(n+2).
\]
The admissible real reconstruction requires
\[
  \Delta_a\ge0.
\]

Reducing \(C_0\) modulo \(\Delta_a\) gives
\[
  C_0(n,a)\equiv
  -\frac{n(n+3)}{(2n^2+14n+21)^2}(K_n^{(0)}a+M_n^{(0)})
  \pmod{\Delta_a},
\]
where
\[
  K_n^{(0)}
  =
  6n^4+66n^3+225n^2+222n-21,
\]
and
\[
  M_n^{(0)}
  =
  -2n^5-22n^4-69n^3-2n^2+275n+294.
\]
For \(n\ge3\), \(K_n^{(0)}>0\) and \(M_n^{(0)}<0\). Put
\[
  b_n^*=-\frac{M_n^{(0)}}{K_n^{(0)}}.
\]
Then \(b_n^*>0\), and
\[
  \Delta_{b_n^*}
  =
  \frac{
    2(n+2)(2n^2+14n+21)^2
    \left(n^7+13n^6+47n^5-33n^4-455n^3-469n^2+731n+1029\right)
  }{(K_n^{(0)})^2}.
\]
The polynomial in parentheses is positive for \(n\ge3\). It is positive at
\(n=3\), and its derivative
\[
  7n^6+78n^5+235n^4-132n^3-1365n^2-938n+731
\]
is positive for \(n\ge3\), by grouping the positive differences
\[
  78n^5-132n^3,\qquad
  235n^4-1365n^2,\qquad
  7n^6-938n+731.
\]
Hence
\[
  \Delta_{b_n^*}>0.
\]
Since \(b_n^*>0\), this implies
\[
  b_n^*>\delta_+.
\]
Therefore
\[
  K_n^{(0)}\delta_-+M_n^{(0)}<0,
  \qquad
  K_n^{(0)}\delta_++M_n^{(0)}<0,
\]
and the negative prefactor in the remainder gives
\[
  C_0(n,\delta_-)>0,
  \qquad
  C_0(n,\delta_+)>0.
\]

But
\[
  C_0(n,0)=-n(n+1)(n+2)<0.
\]
Thus two of the three real roots of \(C_0(n,\cdot)\) lie in the forbidden
interval
\[
  \delta_-<a<\delta_+,
  \qquad
  \Delta_a<0.
\]
The third root lies to the right of \(1\), because
\[
  C_0(n,1)=2(n-1)(n^2+10n+15)>0
\]
while the leading coefficient of \(C_0\) is negative.

Proposition. For every \(n\ge3\), the centroid \(Q_3\)-gate
\[
  C_0(n,a)=0
\]
has no admissible massive-endpoint solution.

The only remaining centroid-gate exception is \(n=2\), equivalently degree
\[
  d=n+4=6.
\]
Thus, in the massive-endpoint branch, the \(Q_3\)-stage is reduced to:

1. the other-interior-root resultant branch for all \(n\ge2\);
2. the finite exceptional centroid case \(n=2\).

## 28. The finite centroid exception \(n=2\) is closed

It remains to check the exceptional centroid gate
\[
  n=2.
\]
Then \(d=6\), and the \(Q_3\)-centroid condition is
\[
  C_0(2,a)=0.
\]
Explicitly,
\[
  C_0(2,a)=-6(14a^3-28a^2-3a+4).
\]
Let
\[
  R(a)=14a^3-28a^2-3a+4.
\]
The quadratic reconstructing the other interior root and the right endpoint is
\[
  F_a(X)=X^2+(a-2)X-14a^2-2a+3.
\]

Now impose the remaining top condition \(Q_4\). There are three possibilities.

If the centroid covers \(d-4\), then
\[
  P_4=\frac{P_2^2}{2},
\]
which reduces, after substituting \(n=2\) and \(C_0(2,a)=0\), to the condition
\[
  28a^3-11a^2-6a+3=0.
\]
But
\[
  \gcd(14a^3-28a^2-3a+4,\,
       28a^3-11a^2-6a+3)=1.
\]

If the same root \(a\) covers \(d-4\), the condition reduces to
\[
  61a^4+14a^2+2a-3=0,
\]
and
\[
  \gcd(14a^3-28a^2-3a+4,\,
       61a^4+14a^2+2a-3)=1.
\]

Finally, if the remaining interior root covers \(d-4\), then \(Q_4\) must have
a common root with \(F_a\). The resultant is, up to a nonzero constant,
\[
  \begin{aligned}
  &2663836a^8+2912392a^7-3145793a^6-2239544a^5\\
  &\quad+1292520a^4+545096a^3-234903a^2-42308a+15876.
  \end{aligned}
\]
This polynomial is also coprime to \(R(a)\):
\[
  \gcd(R(a),\operatorname{Res}_X(F_a,Q_4(X)))=1.
\]

Therefore no root of the exceptional cubic \(R(a)=0\) can satisfy the
remaining \(Q_4\)-condition.

Proposition. The exceptional massive-endpoint centroid case \(n=2\) is
impossible.

Consequently, in the massive-endpoint branch, derivative order \(d-3\) cannot
be covered by the centroid root at all. Combined with Sections 26 and 27, the
only remaining \(Q_3\)-possibility in the massive-endpoint branch is:
\[
  d-3
  \quad\text{is covered by the other nonzero interior root.}
\]

## 29. Current reduced massive-endpoint branch

The massive-endpoint branch has now reached a single forced \(Q_3\)-pattern.

In the normalization
\[
  -1,\quad 0,\quad a,\quad X_-,\quad X_+,
\]
where \(-1\) has multiplicity \(n=d-4\), the \(Q_2\)-root is \(a\), and
\[
  X_\pm=\frac{S\pm\sqrt{\Delta_a}}2,
\]
the right endpoint is \(X_+\) and the remaining interior root is \(X_-\).

The closed gates prove:

1. \(d-3\) cannot be covered by \(a\);
2. \(d-3\) cannot be covered by \(0\);
3. endpoints cannot cover \(d-3\).

Therefore the only possible cover is
\[
  Q_3(X_-)=0.
\]
Equivalently, with
\[
  H_3(X)=D_3(X^3-3a^2X)-2M_3(a),
\]
the remaining massive-endpoint branch is exactly the oriented algebraic system
\[
  H_3(X_-)=0,
  \qquad
  \Delta_a\ge0,
  \qquad
  \alpha_n<a<\beta_n,
\]
together with the \(Q_4\)-cover condition.

This is the next target. The whole massive-endpoint branch has been reduced
from a cover of all derivative orders to one oriented quadratic-cubic
incidence plus the final \(Q_4\)-incidence.

## 30. Two \(Q_4\)-covers are eliminated by exact resultants

In the reduced massive-endpoint branch, the \(Q_3\)-condition is already
forced to
\[
  H_3(X_-)=0.
\]
The remaining \(Q_4\)-condition has three possible covers:
\[
  0,\qquad a,\qquad X_-.
\]
The first two can be eliminated by exact resultants.

Let
\[
  E_3(n,a)=\operatorname{Res}_X(F_a(X),H_3(X)).
\]
This is the unoriented resultant attached to the forced \(Q_3\)-incidence.
Any solution of the oriented branch must in particular satisfy
\[
  E_3(n,a)=0.
\]

If \(Q_4\) is covered by the centroid, then
\[
  G_0(n,a)=2M_4(a)-M_2(a)^2=0.
\]
Thus a solution would force
\[
  \operatorname{Res}_a(E_3,G_0)=0.
\]
A direct symbolic calculation gives
\[
  \operatorname{Res}_a(E_3,G_0)
  =
  n^6(n+1)^4(n+2)^4(n+3)^6(n+5)\,P_{39}(n),
\]
where \(P_{39}\in\mathbb Z[n]\) has degree \(39\). For integer \(n\ge2\), the
prefactor is nonzero. The remaining factor has no root modulo \(17\):
\[
  P_{39}(r)\not\equiv0\pmod{17}
  \qquad(r=0,1,\ldots,16).
\]
Hence \(P_{39}(n)\ne0\) for every integer \(n\), and the centroid \(Q_4\)-cover
is impossible in the reduced massive-endpoint branch.

If \(Q_4\) is covered by the same root \(a\), then
\[
  G_a(n,a)=D_4Q_4(a)=0.
\]
Again any solution would force
\[
  \operatorname{Res}_a(E_3,G_a)=0.
\]
The exact resultant has the form
\[
  \operatorname{Res}_a(E_3,G_a)
  =
  4096n^6(n+1)^4(n+2)^6(n+3)^8\,P_{48}(n),
\]
where \(P_{48}\in\mathbb Z[n]\) has degree \(48\). The prefactor is nonzero
for \(n\ge2\), and the remaining factor has no root modulo \(11\):
\[
  P_{48}(r)\not\equiv0\pmod{11}
  \qquad(r=0,1,\ldots,10).
\]
Therefore \(P_{48}(n)\ne0\) for every integer \(n\), and the same-root
\(Q_4\)-cover is impossible.

These modular checks are finite exact arithmetic, not numerical sampling. The
verification script is
\[
  \texttt{Math/conjecture/tools/massive\_endpoint\_q4\_certificates.py}.
\]

Proposition. In the reduced massive-endpoint branch, \(d-4\) cannot be covered
by the centroid root \(0\) or by the \(Q_2\)-root \(a\).

Thus the massive-endpoint branch is forced into the single pattern
\[
  d-2\mapsto a,
  \qquad
  d-3\mapsto X_-,
  \qquad
  d-4\mapsto X_-.
\]
The only remaining \(Q_4\)-possibility is that the same interior root \(X_-\)
covers both \(d-3\) and \(d-4\).

## 31. The last \(Q_4\)-cover is eliminated

It remains to exclude the possibility
\[
  H_3(X_-)=0,
  \qquad
  H_4(X_-)=0,
\]
where
\[
  H_4(X)
  =
  D_4(X^4-6a^2X^2)-8M_3(a)X+3M_2(a)^2-6M_4(a).
\]

Reduce both equations modulo the quadratic \(F_a\):
\[
  H_3(X)\equiv A_3X+B_3,
  \qquad
  H_4(X)\equiv A_4X+B_4
  \pmod {F_a}.
\]
For \(n\ge2\), \(A_3\ne0\). Thus if a common root of \(F_a\) is to annul
both \(H_3\) and \(H_4\), the two linear remainders must have the same zero.
Hence any solution must satisfy
\[
  C_{34}(n,a):=A_3B_4-A_4B_3=0.
\]
Together with the already forced condition
\[
  E_3(n,a)=\operatorname{Res}_X(F_a,H_3)=0,
\]
this gives the necessary elimination condition
\[
  \operatorname{Res}_a(E_3,C_{34})=0.
\]

The exact resultant factors as
\[
\begin{aligned}
  \operatorname{Res}_a(E_3,C_{34})
  =&\;2^{30}n^{10}(n+1)^8(n+2)^{12}(n+3)^{16}  \\
   &\cdot (n+4)^6(n+5)^2P_{13}(n)^2P_{46}(n),
\end{aligned}
\]
where \(P_{13}\in\mathbb Z[n]\) has degree \(13\) and \(P_{46}\in\mathbb Z[n]\)
has degree \(46\). The prefactor is nonzero for every integer \(n\ge2\).
Moreover
\[
  P_{13}(r)\not\equiv0\pmod {13}
  \qquad(r=0,\ldots,12),
\]
and
\[
  P_{46}(r)\not\equiv0\pmod {17}
  \qquad(r=0,\ldots,16).
\]
Therefore neither \(P_{13}\) nor \(P_{46}\) can vanish at an integer \(n\).

So the final \(Q_4\)-possibility is impossible. Combined with the two previous
\(Q_4\)-eliminations, this proves:

Proposition. The massive-endpoint branch contains no real five-root
Casas-Alvero counterexample.

Equivalently, in the real five-root frontier, the degenerate branch where an
endpoint has multiplicity \(d-4\) is closed. Any remaining real five-root
counterexample must lie in the non-massive branch.

## 32. Post-massive frontier and the sixth top derivative

The closure of the massive-endpoint branch upgrades the fifth top derivative
from a conditional obstruction to a universal constraint in the real five-root
frontier.

Indeed, an endpoint root can cover \(d-5\) only if it has multiplicity
\(d-4\). Since this case is now impossible, derivative order \(d-5\) must be
covered either by the centroid identity
\[
  5P_2P_3=6P_5
\]
or by a non-endpoint root \(z\) satisfying
\[
  Q_5(z)=0.
\]

The next point where endpoints can re-enter is derivative order \(d-6\). An
endpoint of multiplicity \(m\) can cover \(d-6\) automatically only when
\[
  d-6<m,
\]
that is,
\[
  m\ge d-5.
\]
Since the \(m=d-4\) endpoint case is already closed, the only remaining
endpoint gate at this level is
\[
  m_{\rm endpoint}=d-5.
\]

The sixth normalized top derivative is explicit. Newton's identities with
\(P_1=0\) give
\[
  e_6
  =
  -\frac{3P_2^3-18P_2P_4-8P_3^2+24P_6}{144}.
\]
Therefore
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

Thus, after the massive-endpoint closure, the next frontier splits into:

1. an endpoint gate with one endpoint of multiplicity exactly \(d-5\);
2. a purely non-endpoint sixth-order incidence \(Q_6(t)=0\);
3. the centroid sixth-order identity
\[
  -15P_2^3+90P_2P_4+40P_3^2-120P_6=0.
\]

This is the next finite branch point for the real five-root attack.

## 33. Endpoint multiplicity \(d-5\): weighted quadratic reduction

Consider the first endpoint gate left after the massive-endpoint closure.
After reflection and scaling, let the left endpoint be \(-1\) with
multiplicity
\[
  n=d-5.
\]
The four remaining roots have total multiplicity \(5\). Since they are
distinct and all have positive multiplicity, exactly one of them is double.

Write the roots as
\[
  -1,\quad 0,\quad a,\quad y,\quad z,
\]
with multiplicities
\[
  n,\quad m_0,\quad m_a,\quad m_y,\quad m_z,
\]
where
\[
  m_0+m_a+m_y+m_z=5.
\]
Choose \(a\) to be the nonzero root selected by \(Q_2\). Then
\[
  D_2a^2=P_2.
\]
The centroid equation and the \(Q_2\)-condition give
\[
  m_y y+m_z z=n-m_a a
\]
and
\[
  m_y y^2+m_z z^2=D_2a^2-n-m_a a^2.
\]
Eliminating \(z\) gives a single weighted quadratic in \(Y\):
\[
\begin{aligned}
  F_{m}(Y)=&
  m_y(m_y+m_z)Y^2
  +2m_y(m_a a-n)Y+n^2-2m_a n a+m_z n \\
  &+m_a(m_a+m_z)a^2-m_z(n+5)(n+4)a^2.
\end{aligned}
\]
Then
\[
  z=\frac{n-m_a a-m_yY}{m_z}.
\]

Up to exchanging the two remaining nonzero roots, there are only three weight
types:
\[
  (m_0,m_a,m_y,m_z)
  =
  (2,1,1,1),\quad(1,2,1,1),\quad(1,1,2,1).
\]
They correspond respectively to the double root being the centroid, the
\(Q_2\)-root, or one of the two remaining nonzero roots.

For each of these three types, define
\[
  M_k=n(-1)^k+m_a a^k+m_yY^k+m_z z^k.
\]
The live endpoint-\(d-5\) branch is now finite: \(Q_3,Q_4,Q_5\) must each be
covered by one of
\[
  0,\quad a,\quad Y,\quad z.
\]
Equivalently, for each weight type and each cover choice in
\[
  \{0,a,Y,z\}^3,
\]
one obtains an explicit two-variable algebraic system in \(a,Y\), together
with the real ordering constraints.

The reconstruction script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d5\_reduction.py}.
\]
It verifies the three weight types and reduces the \(Q_3,Q_4,Q_5\) equations
modulo the weighted quadratic \(F_m\). Thus the endpoint \(d-5\) gate has been
reduced from an arbitrary five-root multiplicity problem to three finite
families of explicit polynomial systems.

## 34. The two symmetric endpoint-\(d-5\) types are closed

Two of the three endpoint-\(d-5\) weight types are symmetric in the remaining
roots \(y,z\):
\[
  (m_0,m_a,m_y,m_z)=(2,1,1,1)
\]
and
\[
  (m_0,m_a,m_y,m_z)=(1,2,1,1).
\]
In these cases, after imposing \(Q_2(a)=0\), the moments \(M_3,M_4,M_5\)
reduce to polynomials in \(n,a\) alone.

For each \(j=3,4,5\), the possible covers are
\[
  0,\qquad a,\qquad r,
\]
where \(r\) denotes either root of the symmetric quadratic \(F_m\). The
\(r\)-cover condition is represented by
\[
  \operatorname{Res}_Y(F_m(Y),H_j(Y))=0.
\]

There are therefore \(3^3=27\) cover triples for each symmetric weight type.
For each triple, compute the three corresponding equations in \(a\). Their
greatest common divisor in the polynomial ring
\[
  \mathbb Q(n)[a]
\]
is \(1\). Hence both symmetric endpoint-\(d-5\) types are generically
inconsistent over the rational function field in \(n\).

The generic gcd verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d5\_symmetric\_gcds.py}.
\]

A full integer certificate also has to exclude special parameter values. For
each cover triple, compute the three pairwise resultants in \(a\), then take
their gcd in \(\mathbb Z[n]\). A common root would force this gcd to vanish.

For the double-centroid type \((2,1,1,1)\), all such exceptional factors have
roots only in
\[
  \{-6,-3,-2,-1\}.
\]
For the double-\(Q_2\)-root type \((1,2,1,1)\), all such exceptional factors
have roots only in
\[
  \{-6,-4,-2,-1\}.
\]
But in the endpoint-\(d-5\) branch
\[
  n=d-5\ge1.
\]
Therefore no exceptional integer specialization is admissible.

The resultant verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d5\_symmetric\_resultants.py}.
\]

Proposition. The endpoint-\(d-5\) branch cannot occur when the double
non-endpoint root is either the centroid or the \(Q_2\)-root.

The only endpoint-\(d-5\) weight type still open is the asymmetric type
\[
  (m_0,m_a,m_y,m_z)=(1,1,2,1)
\]
which remains genuinely two-variable after reduction.

## 35. The asymmetric endpoint-\(d-5\) type is closed

It remains to treat
\[
  (m_0,m_a,m_y,m_z)=(1,1,2,1).
\]
For this type the weighted quadratic becomes
\[
  F(Y)
  =
  6Y^2+4(a-n)Y+n^2-2na+n-(n+3)(n+6)a^2.
\]
The remaining simple nonzero root is
\[
  z=n-a-2Y.
\]

For every cover \(c\in\{0,a,Y,z\}\) and each \(j=3,4,5\), reduce the
condition \(H_j(c)=0\) modulo \(F\):
\[
  H_j(c)\equiv A_{j,c}Y+B_{j,c}\pmod F.
\]
Thus each cover condition is linear in \(Y\).

Fix a cover triple
\[
  (c_3,c_4,c_5)\in\{0,a,Y,z\}^3.
\]
A solution must satisfy
\[
  F(Y)=0,\qquad
  A_{3,c_3}Y+B_{3,c_3}=0,
\]
and the three linear cover equations must have the same \(Y\)-root. Hence it
must satisfy the necessary equations
\[
  R_3(n,a):=\operatorname{Res}_Y(F,A_{3,c_3}Y+B_{3,c_3})=0,
\]
\[
  C_{34}(n,a):=A_{3,c_3}B_{4,c_4}-A_{4,c_4}B_{3,c_3}=0,
\]
\[
  C_{35}(n,a):=A_{3,c_3}B_{5,c_5}-A_{5,c_5}B_{3,c_3}=0.
\]
Eliminating \(a\) by pairwise resultants gives a necessary polynomial
condition in \(n\).

The exact verification over all \(4^3=64\) cover triples shows that every
such necessary polynomial factors into linear factors with roots contained in
\[
  \{-6,-4,-3,-2,-1,0\}
\]
and five nonlinear factors. These nonlinear factors have degrees
\[
  5,\quad7,\quad7,\quad20,\quad22.
\]
The degree-\(5\) factor has no root modulo \(7\); the two degree-\(7\) factors
have no root modulo \(5\); the degree-\(20\) factor has no root modulo \(11\);
and the degree-\(22\) factor has no root modulo \(7\).

Therefore no integer
\[
  n=d-5\ge1
\]
can satisfy any asymmetric endpoint-\(d-5\) cover triple.

The verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d5\_asymmetric\_resultants.py}.
\]

Proposition. The asymmetric endpoint-\(d-5\) type is impossible.

Together with the two symmetric closures, this proves that the whole endpoint
\(d-5\) branch is impossible.

## 36. Post-endpoint-\(d-5\) frontier and \(Q_7\)

Since the endpoint \(d-5\) branch is impossible, an endpoint cannot cover
derivative order \(d-6\). Indeed, automatic endpoint coverage of \(d-6\)
would require endpoint multiplicity at least \(d-5\), and the cases
\(d-4\) and \(d-5\) are both closed.

Thus \(d-6\) is now forced to be covered by the centroid identity
\[
  -15P_2^3+90P_2P_4+40P_3^2-120P_6=0
\]
or by a non-endpoint root satisfying \(Q_6=0\).

The next endpoint gate is derivative order \(d-7\). An endpoint can cover it
automatically only if its multiplicity is at least \(d-6\). Since the higher
endpoint multiplicities are closed, the only new gate here is
\[
  m_{\rm endpoint}=d-6.
\]

The seventh normalized top derivative is
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
Consequently the centroid covers \(d-7\) exactly when
\[
  35P_2^2P_3-84P_2P_5-70P_3P_4+120P_7=0.
\]

## 37. Endpoint multiplicity \(d-6\): weighted quadratic reduction

In the new endpoint gate, normalize the endpoint to \(-1\) with multiplicity
\[
  n=d-6.
\]
The four remaining roots have total multiplicity \(6\). Write
\[
  -1,\quad 0,\quad a,\quad y,\quad z
\]
with multiplicities
\[
  n,\quad m_0,\quad m_a,\quad m_y,\quad m_z,
  \qquad
  m_0+m_a+m_y+m_z=6,
\]
and choose \(a\) as the nonzero \(Q_2\)-root.

The centroid equation and \(Q_2(a)=0\) again give
\[
  m_y y+m_z z=n-m_a a,
\]
\[
  m_y y^2+m_z z^2=(n+6)(n+5)a^2-n-m_a a^2.
\]
Eliminating \(z\) gives the weighted quadratic
\[
\begin{aligned}
  F_m(Y)=&
  m_y(m_y+m_z)Y^2+2m_y(m_a a-n)Y+n^2-2m_a n a+m_z n\\
  &+m_a(m_a+m_z)a^2-m_z(n+6)(n+5)a^2.
\end{aligned}
\]

Up to exchanging \(y,z\), there are seven weight types:
\[
\begin{gathered}
  (1,1,2,2),\quad(1,1,3,1),\quad(1,2,2,1),\\
  (1,3,1,1),\quad(2,1,2,1),\quad(2,2,1,1),\quad(3,1,1,1).
\end{gathered}
\]

For each type, the live endpoint-\(d-6\) branch is the finite system where
\[
  Q_3,\quad Q_4,\quad Q_5,\quad Q_6
\]
are covered by roots among
\[
  0,\quad a,\quad Y,\quad z.
\]
The reconstruction script
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_reduction.py}
\]
verifies these seven types and reduces \(H_3,H_4,H_5,H_6\) modulo \(F_m\).
Four of the seven types become univariate in \(a\) after \(Q_2\); the other
three remain linear in \(Y\). This is the next finite elimination target.

## 38. Endpoint multiplicity \(d-6\): modular diagnostic

After substituting each possible cover
\[
  X\in\{0,a,Y,z\}
\]
and reducing modulo \(F_m\), every \(Q_3,Q_4,Q_5,Q_6\) cover condition has
degree at most one in \(Y\). The degree-check script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_cover\_degrees.py}.
\]

As an orientation check, the modular diagnostic script
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_modular\_sieve.py}
\]
tests the finite-field system
\[
  F_m=0,\qquad
  \prod_{X\in\{0,a,Y,z\}} H_k(X)=0,\quad k=3,4,5,6.
\]
The corrected diagnostic starts at primes \(p>6\), so that the bad denominator
residues
\[
  n+1,\ldots,n+6\equiv0\pmod p
\]
do not cover the whole field. Five types have no nondegenerate points modulo
\(7\):
\[
  (1,1,2,2),\quad(1,2,2,1),\quad(1,3,1,1),\quad
  (2,1,2,1),\quad(2,2,1,1).
\]
The remaining two diagnostic cases,
\[
  (1,1,3,1),\quad(3,1,1,1),
\]
have nondegenerate points modulo \(7\), but none modulo \(11\).

This is not yet a characteristic-zero closure: unlike the earlier univariate
certificates in \(n\), this is a multivariate diagnostic. Its value is that it
points to the right exact target: saturate by
\[
  a(n+1)(n+2)(n+3)(n+4)(n+5)(n+6)
\]
and then eliminate \(Y\) and \(a\) to produce univariate factors in \(n\).

## 39. Endpoint multiplicity \(d-6\): four generic type closures

For the four weight types
\[
  (1,1,2,2),\quad(1,3,1,1),\quad(2,2,1,1),\quad(3,1,1,1),
\]
every one of the \(4^4=256\) cover quadruples has gcd \(1\) after eliminating
\(Y\), over the field \(\mathbb{Q}(n)\) in the variable \(a\). Thus these
four types are impossible for generic \(n\).

The verification script is
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_type\_generic\_probe.py}.
\]

The three remaining types are
\[
  (1,1,3,1),\quad(1,2,2,1),\quad(2,1,2,1).
\]
They are exactly the types where all covers stay linear in \(Y\), and they
need a more targeted specialization certificate.

## 40. Endpoint multiplicity \(d-6\): residue sieve for remaining types

For the three remaining types, the script
\[
  \texttt{Math/conjecture/tools/endpoint\_d6\_residue\_sieve.py}
\]
records, prime by prime, the \(n\)-residues that can still support a
nondegenerate finite-field point. The tested primes are
\[
  7,11,13,17,19,23,29,31.
\]

The residue densities after combining these local constraints are:
\[
\begin{array}{c|c}
  \text{type} & \text{surviving density}\\
  \hline
  (1,1,3,1) & 4064256/6685349671\\
  (1,2,2,1) & 2667168/6685349671\\
  (2,1,2,1) & 3111696/6685349671.
\end{array}
\]
This does not close the three types, but it shows that the remaining
specialization set is arithmetically thin. The next step is to turn these
residue constraints into exact saturated resultants for the surviving residue
families.
