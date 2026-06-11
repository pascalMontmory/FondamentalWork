# Campbell Weight Extraction

This note extracts the exact sieve objects from Campbell's \(P_3\)
between-squares theorem and states what would actually be needed to upgrade
it toward Legendre.

The conclusion is important: the theorem gives a \(P_3\) survivor, but the
positive margin is small and the proof is designed to count almost-primes,
not to distinguish primes from terminal composites.  Therefore a direct
"subtract all composites" argument is not realistic without additional
certificate structure.

## 1. The interval used in the analytic range

Campbell writes
\[
  N=n^2,
  \qquad
  \mathcal A(N)=\mathbb Z\cap(N,N+2\sqrt N).
\]

Since
\[
  N+2\sqrt N=(n+1)^2-1,
\]
one has
\[
  \mathcal A(n^2)\subset(n^2,(n+1)^2).
\]

Thus proving the existence of \(a\in\mathcal A(n^2)\) with
\[
  \Omega(a)\le3
\]
is enough for the \(P_3\) analogue of Legendre.

## 2. Richert parameters

For a finite set \(\mathcal A\), Campbell defines
\[
  r_k(\mathcal A)=|\{a\in\mathcal A:\Omega(a)\le k\}|.
\]

The Richert setup uses
\[
  X=\max(\mathcal A),
  \qquad
  z=X^{1/k_1},
  \qquad
  y=X^{1/k_2},
\]
and, for \(a\in\mathcal A\) with \((a,P(z))=1\),
\[
\boxed{
  w(a)=
  \lambda
  -
  \sum_{\substack{z\le p<y\\p\mid a}}
  \left(1-\frac{\log p}{\log y}\right),
  \qquad
  \lambda=k+1-k_2.
}
\]

The weighted sifting function is
\[
\boxed{
  W(\mathcal A,\mathcal P,z)
  =
  \sum_{\substack{a\in\mathcal A\\(a,P(z))=1}}w(a).
}
\]

Campbell uses the standard implication
\[
\boxed{
  r_k(\mathcal A)\ge \frac1k W(\mathcal A',\mathcal P,z),
}
\]
where \(\mathcal A'\) removes square divisors \(p^2\) in the intermediate
range
\[
  z\le p<y.
\]

## 3. The final \(P_3\) parameters

In the large range
\[
  N\ge10^{31},
\]
the final proof takes
\[
\boxed{
  k=3,\qquad k_1=8,\qquad k_2=3.17,
}
\]
so
\[
\boxed{
  z=X^{1/8},
  \qquad
  y=X^{1/3.17},
  \qquad
  \lambda=3+1-3.17=0.83.
}
\]

The lower-bound inequality used in the proof is
\[
\boxed{
\begin{aligned}
  r_3(\mathcal A)
  \ge&
  \frac{0.83}{3}S(\mathcal A,\mathcal P,z)
  \\
  &-\frac13
  \sum_{z\le p<y}
  \left(1-\frac{\log p}{\log y}\right)
  S(\mathcal A_p,\mathcal P,z)
  \\
  &-\frac{0.83\cdot0.297}{3}|\mathcal A|^{3/4}.
\end{aligned}
}
\]

After the explicit estimates and the choice \(s=3.33\), Campbell obtains:
\[
  \frac{0.83}{3}S(\mathcal A,\mathcal P,z)
  >
  2.095\frac{\sqrt N}{\log X},
\]
\[
  \frac13
  \sum_{z\le p<y}
  \left(1-\frac{\log p}{\log y}\right)
  S(\mathcal A_p,\mathcal P,z)
  \le
  2.0687\frac{\sqrt N}{\log X},
\]
and
\[
  \frac{0.83\cdot0.297}{3}|\mathcal A|^{3/4}
  \le
  0.0014\frac{\sqrt N}{\log X}.
\]

Therefore
\[
\boxed{
  r_3(\mathcal A)>0.0249\frac{\sqrt N}{\log X}>0.
}
\]

This is the exact analytic margin available from the \(P_3\) theorem.

## 4. Why a naive composite subtraction will not close Legendre

If \(I_n\) is prime-free, then every element counted by \(r_3(\mathcal A)\)
is a composite \(P_3\).  The Campbell theorem alone only says that at least
one such object exists.

To turn this into a prime theorem by subtraction, one would need an upper
bound of the form
\[
\boxed{
  \#\{a\in\mathcal A(n^2):\Omega(a)\le3,\ a\text{ composite}\}
  <
  0.0249\frac{\sqrt N}{\log X}
}
\]
under the prime-free assumption.

There is no reason to expect such a bound from ordinary almost-prime
technology.  Composite almost-primes in a short interval can be plentiful,
and the positive margin in Campbell's proof is intentionally only large
enough to prove non-emptiness of \(P_3\)'s.

Thus the route

\[
  P_3\text{ exists}
  \quad\Longrightarrow\quad
  \text{one of them is prime}
\]
is blocked unless the prime-free assumption supplies extra algebraic
structure.

## 5. The usable survivor structure

The useful information is not merely \(\Omega(a)\le3\).  The weighted proof
is built around survivors with
\[
  (a,P(z))=1,
  \qquad
  z=X^{1/8}.
\]

Thus a relevant prime-free \(P_3\) survivor in the weighted core has no prime
factor below \(X^{1/8}\).  Since \(a\asymp X\), a composite survivor has one
of the following shapes:

1. semiprime:
   \[
     a=pq,\qquad p,q\ge X^{1/8};
   \]
2. triprime:
   \[
     a=pqr,\qquad p,q,r\ge X^{1/8}.
   \]

The terminal factorization
\[
  a=(n-a_0)(n+a_0+k)
\]
therefore has to be synchronized with the absence of small prime factors
below \(X^{1/8}\), not just with \(\Omega(a)\le3\).

This gives a sharper obstruction language:

> In a prime-free interval, the Richert-positive survivors must be terminal
> composites whose terminal factors split into two or three prime blocks, all
> above \(X^{1/8}\), while every actual candidate in the interval still has a
> small-prime certificate below \(n+1\).

The contradiction, if it exists, must come from this tension:

- the Richert core removes all primes below \(X^{1/8}\);
- prime-freeness of \(I_n\) forces every candidate to have some prime divisor
  below \(\sqrt a<n+1\);
- terminal \(P_3\) structure allows only two or three such divisors total.

## 6. Correct next exact target

The next lemma should be formulated as follows.

> Richert-terminal certificate lemma.  Let \(N=n^2\), \(X=\max\mathcal A(N)\),
> and \(z=X^{1/8}\).  Suppose \(I_n\) is prime-free.  Then every
> Richert-core \(P_3\) survivor \(a\in\mathcal A(N)\), with
> \((a,P(z))=1\), admits a terminal factorization
> \[
>   a=(n-a_0)(n+a_0+k)
> \]
> whose prime factors all lie in \([z,n+1)\).  Show that such terminal
> factorizations cannot supply the positive Richert weight
> \[
>   0.0249\frac{\sqrt N}{\log X}
> \]
> while also satisfying the quotient-certificate constraints imposed by
> prime-freeness.

This is the precise bridge between Campbell's theorem and the existing
certificate work.

It is still an open target, but it is now mathematically aligned with the
actual theorem rather than with an over-strong geometry-only descent claim.
