# P3 Terminal Descent Target

This note records the exact obstruction produced by combining a
between-squares \(P_3\) theorem with the assumption that Legendre fails.

The point is not to use an almost-prime theorem as a proof of Legendre.
That would run into the sieve parity problem.  The point is to convert the
almost-prime survivor into a rigid terminal factor equation.

## 1. Terminal \(P_3\) setup

Let
\[
  I_n=(n^2,(n+1)^2).
\]

Assume:

1. \(I_n\) contains no prime;
2. \(I_n\) contains an integer \(N\) with at most three prime factors,
   counted with multiplicity.

Then \(N\) is composite and
\[
  \Omega(N)\le3.
\]

Choose a factorization
\[
  N=dD
\]
with
\[
  1<d\le \sqrt N<D.
\]

Since
\[
  N<(n+1)^2,
\]
one has
\[
  d<n+1,
\]
hence
\[
  d\le n.
\]

Since
\[
  N>n^2
\]
and \(d\le\sqrt N\), the complementary factor satisfies
\[
  D>\sqrt N>n.
\]

Therefore every composite \(P_3\) survivor gives a factor pair straddling
\(n\):
\[
\boxed{
  1<d\le n<D,\qquad dD\in I_n,\qquad \Omega(d)+\Omega(D)\le3.
}
\]

In particular, one side is prime and the other side is prime or semiprime.

## 2. Centered factor equation

Write
\[
  d=n-a,\qquad D=n+b,
\]
where
\[
  a\ge0,\qquad b\ge1.
\]

The condition
\[
  n^2<N<(n+1)^2=n^2+2n+1
\]
becomes
\[
  1\le n(b-a)-ab\le2n.
\]

Let
\[
  k=b-a.
\]

Since \(N>n^2\), necessarily
\[
  k\ge1.
\]

Then
\[
  b=a+k
\]
and the terminal equation is
\[
\boxed{
  N=(n-a)(n+a+k)
}
\]
with
\[
\boxed{
  1\le nk-a(a+k)\le2n.
}
\]

This equation is exact.  It is the factor-side analogue of the quotient
certificate equations.

## 3. Three terminal channels

The terminal inequality splits naturally by \(k\).

### Channel T1: \(k=1\)

Here
\[
  N=n^2+n-a(a+1),
\]
and the interval condition is equivalent to
\[
\boxed{
  0\le a(a+1)\le n-1.
}
\]

Thus the survivor lies below the midpoint \(n^2+n\), and the two factors are
separated by
\[
  D-d=2a+1.
\]

### Channel T2: \(k=2\)

Here
\[
  N=n^2+2n-a(a+2),
\]
and the interval condition is equivalent to
\[
\boxed{
  0\le a(a+2)\le2n-1.
}
\]

Thus the survivor lies near the upper endpoint, with factor separation
\[
  D-d=2a+2.
\]

### Channel Tfar: \(k\ge3\)

For \(k\ge3\), the upper endpoint condition forces a real drop of the lower
factor:
\[
  nk-a(a+k)\le2n
\]
is equivalent to
\[
\boxed{
  a(a+k)\ge n(k-2).
}
\]

Together with \(N>n^2\), one obtains the exact band
\[
\boxed{
  n(k-2)\le a(a+k)\le nk-1.
}
\]

Equivalently,
\[
\boxed{
  \frac{-k+\sqrt{k^2+4n(k-2)}}2
  \le a
  \le
  \frac{-k+\sqrt{k^2+4(nk-1)}}2.
}
\]

So every off-diagonal terminal \(P_3\) survivor has a lower factor
\[
  d=n-a
\]
which has moved down by a quantitatively forced amount.

## 4. Exact closure target

Campbell's \(P_3\) theorem supplies at least one \(P_3\) in every
between-squares interval.  Therefore, in a minimal counterexample to
Legendre, at least one terminal composite \(P_3\) must exist.

The useful closure criterion is a descent criterion, not the tautology that
some \(P_3\) must be prime:

> Terminal \(P_3\) descent criterion.  If every terminal composite
> \[
>   N=(n-a)(n+a+k)\in I_n,\qquad \Omega(N)\le3,
> \]
> occurring in a prime-free \(I_n\) forces a smaller prime-free interval
> \(I_{n'}\) with \(n'<n\), then Legendre is true.

Indeed, a least counterexample \(n\) would contain a \(P_3\) by the
between-squares \(P_3\) theorem.  Since \(I_n\) is prime-free, this \(P_3\)
is terminal composite.  The descent criterion would then produce a smaller
counterexample, contradiction.

This is the clean place where the parity problem has been isolated.  Instead
of trying to make a sieve distinguish primes from \(P_3\)'s globally, one
must show that a terminal composite
\[
  (n-a)(n+a+k)
\]
with
\[
  \Omega(n-a)+\Omega(n+a+k)\le3
\]
cannot be the unavoidable endpoint of the between-squares \(P_3\) theorem.

## 5. Link to the existing certificate language

The terminal channels should be compared with the existing quotient
certificates.

The quotient route studies composite candidates of the form
\[
  n^2+t^2+\epsilon
\]
through small prime labels
\[
  p=A-r.
\]

The terminal \(P_3\) route studies the same prime-free interval from the
opposite side: instead of asking which small prime certifies a candidate as
composite, it asks how an almost-prime candidate can factor across the center
\(n\).

The bridge is:

- T1 and T2 are near-diagonal factor channels;
- Tfar is the off-diagonal drop channel;
- in every channel one side is prime and the other side is prime or
  semiprime.

Thus the next proof attempt should not be another numerical search.  It
should be an exact synchronization between:

1. terminal factor equations
   \[
     N=(n-a)(n+a+k);
   \]
2. quotient certificates for the absence of primes in \(I_n\);
3. the \(P_3\) existence theorem.

If this synchronization forces a smaller prime-free between-squares interval,
one obtains the descent criterion above and Legendre closes.

## 6. Next exact lemma to attack

The most promising sharp sublemma is the following.

> Near-diagonal terminal lemma.  In a minimal counterexample to Legendre,
> no Campbell \(P_3\) survivor can lie in T1 or T2.

If this lemma is proved, then every terminal \(P_3\) survivor lies in Tfar,
where
\[
  a(a+k)\ge n(k-2).
\]

That inequality forces a substantial factor drop.  The remaining target
would then be a descent on the lower factor \(n-a\), rather than a global
short-interval prime-gap estimate.

This is a possible route around the direct \(x^{1/2}\) prime-gap barrier:
use \(P_3\) existence to create a terminal composite, then use terminal
factor geometry to force descent.
