# A centroid obstruction for Casas-Alvero polynomials

Date: 2026-06-10.

## 1. Conjecture

The Casas-Alvero conjecture says:

Let \(f\in\mathbb C[x]\) have degree \(d\ge2\). If
\[
  \gcd(f,f^{(k)})\ne 1
  \qquad (k=1,\ldots,d-1),
\]
then
\[
  f(x)=c(x-a)^d.
\]

Equivalently, the only complex polynomials sharing a root with every
nonzero derivative should be pure powers of a linear factor.

## 2. Result

Theorem. Let
\[
  f(x)=c\prod_{j=1}^r (x-a_j)^{m_j},
  \qquad
  a_i\ne a_j\ (i\ne j),\quad m_j\ge1,\quad \sum_{j=1}^r m_j=d.
\]
If \(f\) satisfies the Casas-Alvero condition, then either \(r=1\), or there is
an index \(j\) such that
\[
  a_j\in \operatorname{conv}\{a_i:i\ne j\}.
\]

Consequences.

1. Casas-Alvero holds for every polynomial whose distinct roots are all extreme
   points of their convex hull.
2. In particular, Casas-Alvero holds for every polynomial with at most two
   distinct roots.
3. In particular, Casas-Alvero holds whenever the distinct roots are the
   vertices of a convex polygon.

## 3. Proof

Write the roots of \(f\), counted with multiplicity, as
\[
  \alpha_1,\ldots,\alpha_d.
\]
The \((d-1)\)-st derivative of a degree \(d\) polynomial is linear. If
\[
  f(x)=c\prod_{\nu=1}^d (x-\alpha_\nu),
\]
then
\[
  f^{(d-1)}(x)=c\,d!\left(x-\frac1d\sum_{\nu=1}^d\alpha_\nu\right).
\]

Since \(f\) satisfies the Casas-Alvero condition, \(f\) and \(f^{(d-1)}\) have a
common root. Hence the centroid
\[
  \mu=\frac1d\sum_{\nu=1}^d\alpha_\nu
  =\frac1d\sum_{i=1}^r m_i a_i
\]
must be one of the distinct roots, say \(\mu=a_j\).

Therefore
\[
  d a_j=\sum_{i=1}^r m_i a_i,
\]
and so
\[
  (d-m_j)a_j=\sum_{i\ne j}m_i a_i.
\]

If \(r>1\), then \(d-m_j>0\), hence
\[
  a_j=\sum_{i\ne j}\frac{m_i}{d-m_j}a_i,
\]
where the coefficients are positive and sum to \(1\). Thus \(a_j\) lies in the
convex hull of the other distinct roots.

This proves the theorem.

## 4. Two-root corollary in coordinates

If
\[
  f(x)=c(x-a)^r(x-b)^s,\qquad a\ne b,\quad r,s\ge1,
\]
then
\[
  \mu=\frac{ra+sb}{r+s}.
\]
The Casas-Alvero condition for \(f^{(d-1)}\) forces \(\mu=a\) or \(\mu=b\).

If \(\mu=a\), then
\[
  ra+sb=(r+s)a,
\]
so \(s(b-a)=0\), contradiction.

If \(\mu=b\), then
\[
  r(a-b)=0,
\]
again a contradiction.

Thus no nontrivial two-root polynomial can be a Casas-Alvero counterexample.

## 5. Status

This does not prove the full Casas-Alvero conjecture. It gives a concise
structural obstruction: every nontrivial counterexample must have a root that
is a convex combination of the other distinct roots.

Any further attack must therefore focus on configurations with at least one
interior or non-extreme root.

## 6. Three distinct roots are impossible

Theorem. A Casas-Alvero polynomial over \(\mathbb C\) cannot have exactly three
distinct roots unless it is a pure power of one linear factor.

Proof.

Assume that \(f\) has exactly three distinct roots. By the centroid theorem
above, one of them is a convex combination of the two others. Hence the three
roots are collinear in \(\mathbb C\simeq\mathbb R^2\). After an affine change of
variable, we may write the roots as
\[
  -u,\quad 0,\quad v
\]
with \(u,v>0\). Let their multiplicities be
\[
  m,\quad n,\quad p
\]
respectively. The degree is
\[
  d=m+n+p.
\]

The \((d-1)\)-st derivative condition says that the weighted centroid is a
root of \(f\). Since the middle root is the only point lying in the convex hull
of the other two, that centroid must be \(0\). Thus
\[
  -mu+pv=0.
\]
Scaling the variable, we may therefore take
\[
  u=p,\qquad v=m.
\]
So every possible three-root counterexample is affinely equivalent to
\[
  f(x)=x^n(x+p)^m(x-m)^p.
\]

Now use the \((d-2)\)-nd derivative. If
\[
  f(x)=c\prod_{\nu=1}^d(x-\alpha_\nu)
\]
and the centroid is \(0\), then
\[
  \frac{f^{(d-2)}(x)}{c\,d!/2}
  =
  x^2-\frac{1}{d(d-1)}\sum_{\nu=1}^d\alpha_\nu^2.
\]

For our normalized roots,
\[
  \sum_{\nu=1}^d\alpha_\nu^2
  =
  m p^2+p m^2
  =
  mp(m+p).
\]
Therefore the two roots of \(f^{(d-2)}\) are
\[
  \pm\rho,
  \qquad
  \rho^2=\frac{mp(m+p)}{d(d-1)}.
\]

Since \(n\ge1\), we have
\[
  d=m+n+p\ge m+p+1,
  \qquad
  d-1\ge m+p.
\]
Consequently
\[
  \rho^2
  \le
  \frac{mp(m+p)}{(m+p+1)(m+p)}
  =
  \frac{mp}{m+p+1}
  <
  \min(m,p).
\]
Because \(m,p\ge1\), this implies
\[
  \rho^2<\min(m^2,p^2),
  \qquad\text{hence}\qquad
  0<\rho<\min(m,p).
\]

But the only roots of \(f\) are
\[
  -p,\quad 0,\quad m.
\]
The roots of \(f^{(d-2)}\) are \(\pm\rho\), neither of which is \(0\), and both
have modulus strictly smaller than \(\min(m,p)\). Hence neither can equal
\(-p\) or \(m\). Thus \(f\) and \(f^{(d-2)}\) have no common root, contradicting
the Casas-Alvero condition.

So no nontrivial Casas-Alvero polynomial has exactly three distinct roots.

Corollary. Every nontrivial Casas-Alvero counterexample must have at least four
distinct roots, and at least one of them must be non-extreme in the convex hull
of the roots.

Literature note. Laterveer and Ounaies proved a stronger statement: a
nontrivial Casas-Alvero counterexample must have at least five distinct roots.
Our three-root argument is therefore best viewed as a short self-contained
warm-up, not as a new frontier result.

## 7. Moment polynomials for the top derivatives

The previous arguments only used \(f^{(d-1)}\) and \(f^{(d-2)}\). The same
normalization gives a useful finite system for all top derivatives.

Let
\[
  f(x)=c\prod_{\nu=1}^d(x-\alpha_\nu)
  =
  c\sum_{j=0}^d(-1)^j e_jx^{d-j},
\]
where \(e_j\) is the \(j\)-th elementary symmetric function of the multiset of
roots \(\alpha_1,\ldots,\alpha_d\), and \(e_0=1\).

For \(1\le k\le d\), define the normalized top derivative
\[
  Q_k(x)=\frac{k!}{c\,d!}f^{(d-k)}(x).
\]
Then
\[
  Q_k(x)=
  \sum_{j=0}^k
  (-1)^j e_j
  \frac{\binom{k}{j}}{\binom{d}{j}}
  x^{k-j}.
\]

Thus the Casas-Alvero condition is equivalent to the following finite
incidence requirement:

For every \(k=1,\ldots,d-1\), at least one distinct root \(a_i\) of \(f\)
satisfies
\[
  Q_k(a_i)=0.
\]

After translating so that the centroid is \(0\), we have \(e_1=0\), and the
first two nontrivial top derivatives are
\[
  Q_1(x)=x,
\]
and
\[
  Q_2(x)=x^2-\frac{1}{d(d-1)}\sum_{\nu=1}^d\alpha_\nu^2.
\]

The cubic obstruction is
\[
  Q_3(x)=
  x^3+\frac{3e_2}{\binom d2}x-\frac{e_3}{\binom d3}.
\]

So a centered counterexample must contain:

* the centroid \(0\) as a root;
* a root at distance
  \[
    \rho^2=\frac{1}{d(d-1)}\sum_{\nu=1}^d\alpha_\nu^2;
  \]
* a root of the cubic \(Q_3\);
* and similarly a root of every \(Q_k\).

This gives a purely algebraic route: instead of searching among polynomials,
search among finite root configurations whose points repeatedly hit the
moment polynomials \(Q_k\).

## 8. The known five-root barrier

The next known obstruction is the following theorem of Laterveer and Ounaies.

Theorem. A nontrivial Casas-Alvero polynomial has at least five distinct roots.

The idea of the proof is geometric and is worth keeping as a guide.

First, Gauss-Lucas implies that if a root lies on the boundary of the convex
hull with multiplicity \(m\), then it cannot remain a root of \(f^{(k)}\) for
any \(k\ge m\). Thus a Casas-Alvero polynomial must have roots in the open
Gauss-Lucas hull. A sharper argument shows that it must have at least two
distinct roots in the open hull.

If there were only four distinct roots, two of them would have to lie in the
open hull. Four non-collinear points cannot have two of their own points in the
interior of their convex hull. Hence all four roots would lie on a line. After
an affine change of variable, the problem becomes real-rooted.

Rolle's theorem then constrains the roots of the successive derivatives so
tightly that the last few derivative conditions force an impossible pattern.
In the generic multiplicity case, one obtains
\[
  f^{(N-5)}(z)=\frac{N!}{5!}z(z^2-5)^2,
\]
which contradicts the fact that a root of multiplicity \(m\le i\) can be at
most simple as a root of \(f^{(i)}\). The remaining high-multiplicity cases are
eliminated by the first and third moment equations.

So any genuine counterexample must have at least five distinct roots, with at
least two of them strictly inside the Gauss-Lucas hull.

This is now the correct baseline for any new attack.
