# Fixed-\(m\) Large-Sieve Target

This note turns the fixed-\(m\) decomposition into an explicit closure
criterion.

It also records a limitation: the classical large sieve is naturally suited
to sets avoiding residue classes, while the present obstruction is a covering
by residue classes.  The remaining proof needs a covering version that uses
the special quadratic origin of the classes.

## 1. Fixed-\(m\) block interval

Fix
\[
  m\ge1.
\]
Let
\[
  a=3q+1,\qquad b=3q+2.
\]
The complete A-block condition is that both surviving A-candidates are
admissible:
\[
  t_0(q)^2\le6m,\qquad t_1(q)^2+1\le6m,
\]
with \(t_0,t_1\in\{a,b\}\) determined by parity.

Thus the relevant \(q\)-set is a short interval, with bridge classes removed:
\[
  \mathcal Q_{\rm cop}(m)
  =
  \{q\in[0,Q_m]\cap\mathbb Z:\gcd(t_1(q),9m^2+1)=1\}.
\]
Here
\[
  Q_m\le \left\lfloor\frac{\sqrt{6m}-2}{3}\right\rfloor
\]
up to the endpoint convention.

## 2. Exact residue sets

The Gaussian layer uses primes
\[
  \mathcal P_0(m)=
  \{p\le3m:p\equiv1\pmod4,\ p\nmid3m\}.
\]
For each \(p\in\mathcal P_0(m)\),
\[
  \Omega_{0,p}(m)
  =
  \{q\bmod p:t_0(q)^2\equiv-9m^2\pmod p\}
\]
has exactly two classes.

The unit-lift layer uses primes
\[
  \mathcal P_1(m)=
  \left\{
  p\le3m:
  p\nmid9m^2+1,\quad
  \left(\frac{-9m^2-1}{p}\right)=1
  \right\}.
\]
For each \(p\in\mathcal P_1(m)\),
\[
  \Omega_{1,p}(m)
  =
  \{q\bmod p:t_1(q)^2\equiv-9m^2-1\pmod p\}
\]
has exactly two classes.  For primes outside \(\mathcal P_1(m)\), it has no
classes on coprime blocks.

The two sieve layers are
\[
  S_i(m)=
  \mathcal Q_{\rm cop}(m)
  \cap
  \bigcup_{p\in\mathcal P_i(m)}
  \{q:q\bmod p\in\Omega_{i,p}(m)\},
  \qquad i=0,1.
\]

The obstruction to closure is exactly
\[
  \mathcal Q_{\rm cop}(m)\subseteq S_0(m)\cap S_1(m).
\]

## 3. Closure criterion

The combined A-channel closes for \(n=3m\) if either of the following holds:

\[
  \mathcal Q_{\rm cop}(m)\not\subseteq S_0(m),
\]
or
\[
  \mathcal Q_{\rm cop}(m)\not\subseteq S_1(m).
\]

Indeed, if \(q\notin S_0(m)\), then no prime \(p\le3m\) divides \(G_q\).
Since
\[
  9m^2<G_q<(3m+1)^2,
\]
the number \(G_q\) is prime.

Similarly, if \(q\notin S_1(m)\), then no prime \(p\le3m\) divides \(U_q\).
Since
\[
  9m^2<U_q<(3m+1)^2,
\]
the number \(U_q\) is prime.

Thus a sufficient exact lemma is:

> Fixed-\(m\) double-sieve lemma.  For every \(m\ge1\),
> \[
>   \mathcal Q_{\rm cop}(m)\not\subseteq S_0(m)\cap S_1(m).
> \]

This lemma would close the whole combined \(3\nmid t\) A-channel.

## 4. Why the classical large sieve is not enough directly

The usual large sieve gives strong bounds for a set \(A\subset[0,Q]\) when
the image of \(A\) modulo many primes occupies few residue classes.

Here the bad sets \(S_i(m)\) are unions of few residue classes:
\[
  |\Omega_{i,p}(m)|=2.
\]
But to prove \(S_i(m)\ne\mathcal Q_{\rm cop}(m)\), one must show that these
few classes do not cover the whole interval.

Equivalently, the complement
\[
  \mathcal Q_{\rm cop}(m)\setminus S_i(m)
\]
avoids two classes modulo each available prime, and may occupy up to
\[
  p-2
\]
classes.  This is the wrong direction for a direct large-sieve upper bound.

Therefore the missing ingredient is not the standard large sieve alone.  It
is a covering obstruction for residue classes that are:

1. two square-root classes modulo each prime;
2. tied to the same fixed parameter \(m\);
3. further constrained by bridge removal
   \[
     \gcd(t_1(q),9m^2+1)=1;
   \]
4. split into two layers that must both cover the same \(q\)-set.

## 5. Exact next lemma

The right lemma to prove is a covering lemma, not a density lemma:

> Quadratic covering lemma.  Let \(m\ge1\).  The interval
> \(\mathcal Q_{\rm cop}(m)\) cannot be covered simultaneously by the two
> quadratic-root covering systems
> \[
>   \{\Omega_{0,p}(m):p\in\mathcal P_0(m)\}
> \]
> and
> \[
>   \{\Omega_{1,p}(m):p\in\mathcal P_1(m)\}.
> \]

More concretely, one must prove that there exists
\[
  q\in\mathcal Q_{\rm cop}(m)
\]
such that either
\[
  q\bmod p\notin\Omega_{0,p}(m)
  \qquad\text{for all }p\in\mathcal P_0(m),
\]
or
\[
  q\bmod p\notin\Omega_{1,p}(m)
  \qquad\text{for all }p\in\mathcal P_1(m).
\]

This is the current exact mathematical bottleneck.  It is the point where a
new argument is required.

## 6. Possible nonstandard route

The covering systems are not arbitrary.  They arise from the two quadratic
polynomials
\[
  9m^2+t_0(q)^2
  \qquad\text{and}\qquad
  9m^2+t_1(q)^2+1.
\]

A nonstandard route is to study the product
\[
  \Phi_m(q)=
  \left(9m^2+t_0(q)^2\right)
  \left(9m^2+t_1(q)^2+1\right)
\]
over the block interval, but with the exact coprime-block gcd condition
already imposed.

On coprime blocks the two factors are coprime.  A complete failure forces
\[
  \Phi_m(q)
\]
to have at least two distinct prime factors \(\le3m\), one from each layer,
for every \(q\in\mathcal Q_{\rm cop}(m)\).

Thus the next possible attack is a valuation or resultant argument for the
family \(\Phi_m(q)\), rather than another pointwise residue count.
