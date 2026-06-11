# Richert-Core Terminal Atom Types

This note records the exact factor types available to a Richert-core
terminal \(P_3\) survivor in a prime-free Legendre interval.

It is a small but useful tightening: once small factors below
\[
  z=X^{1/8}
\]
have been removed, a composite \(P_3\) terminal survivor has only three
atomic shapes.

## 1. Setup

Let
\[
  N_0=n^2,
  \qquad
  \mathcal A(N_0)=\mathbb Z\cap(N_0,N_0+2\sqrt{N_0}),
\]
and let
\[
  X=\max\mathcal A(N_0),
  \qquad
  z=X^{1/8}.
\]

Assume \(I_n=(n^2,(n+1)^2)\) is prime-free and let
\[
  A\in\mathcal A(N_0)
\]
be a Richert-core \(P_3\) survivor:
\[
  \Omega(A)\le3,
  \qquad
  (A,P(z))=1.
\]

Since \(I_n\) is prime-free, \(A\) is composite.  Choose the terminal
factorization
\[
  A=dD,
  \qquad
  1<d\le\sqrt A<D.
\]

As before,
\[
  d\le n<D.
\]

Every prime divisor of \(A\) lies above the Richert cutoff:
\[
\boxed{
  p\ge z.
}
\]

There is no global upper bound \(p<n+1\) for every prime atom.  A large atom
can occur on the upper terminal side.  What is true is:

- every atom dividing the lower terminal factor \(d\) is \(\le d\le n\);
- if the upper terminal factor \(D\) is composite, at least one of its prime
  atoms is \(<\sqrt D<\sqrt A<n+1\).

For large \(n\),
\[
  z=X^{1/8}\asymp n^{1/4}.
\]

Thus the Richert core is not arbitrary: every atomic factor is at least
\[
  n^{1/4+o(1)}.
\]
The medium-prime certificate range
\[
  [z,n+1)
\]
is guaranteed for lower-side atoms and for at least one atom on any composite
upper side, but not for every upper-side atom.

## 2. Atomic classification

Since
\[
  \Omega(d)+\Omega(D)=\Omega(A)\le3
\]
and
\[
  d>1,\qquad D>1,
\]
there are only three possibilities.

### Type R2: prime times prime

\[
\boxed{
  d=p,\qquad D=q,
}
\]
where
\[
  z\le p\le n<q.
\]

This is a semiprime terminal survivor:
\[
  A=pq.
\]

### Type R3L: prime on the lower side, semiprime on the upper side

\[
\boxed{
  d=p,\qquad D=qr,
}
\]
where
\[
  z\le p\le n,
  \qquad
  z\le q\le r,
  \qquad
  \min(q,r)<n+1.
\]

The upper terminal factor \(D\) is larger than \(n\), but it is made from two
Richert-core prime atoms; at least one of them lies below \(n+1\).

### Type R3R: semiprime on the lower side, prime on the upper side

\[
\boxed{
  d=pq,\qquad D=r,
}
\]
where
\[
  z\le p,q\le n,
  \qquad
  z\le r,
  \qquad
  pq\le n<r.
\]

This is the only type in which the upper terminal factor is itself prime.

No other terminal type is possible: a triprime on either terminal side would
leave at least one further prime on the other side and force
\[
  \Omega(A)\ge4.
\]

## 3. Terminal equations by type

Write
\[
  d=n-a,
  \qquad
  D=n+a+k,
  \qquad
  k\ge1.
\]

The exact terminal inequality remains
\[
\boxed{
  1\le nk-a(a+k)\le2n.
}
\]

The atom types therefore become:

### R2

\[
\boxed{
  p=n-a,\qquad q=n+a+k.
}
\]

So
\[
  q-p=2a+k.
\]

This is a prime-pair straddling equation.

### R3L

\[
\boxed{
  p=n-a,\qquad qr=n+a+k.
}
\]

The upper terminal semiprime is constrained by
\[
  qr-p=2a+k.
\]

### R3R

\[
\boxed{
  pq=n-a,\qquad r=n+a+k.
}
\]

The lower terminal semiprime is constrained by
\[
  r-pq=2a+k.
\]

## 4. Link with prime-free certificates

If \(I_n\) is prime-free, every integer
\[
  m\in I_n
\]
has at least one prime divisor
\[
  \le \sqrt m<n+1.
\]

For a Richert-core terminal survivor, such certifying divisors have already
been restricted to
\[
  [z,n+1).
\]

Thus a prime-free interval must supply a medium-prime certificate for every
Richert-core survivor.  But a terminal \(P_3\) survivor has only two or three
prime atoms total, and all lower-side atoms are already locked into the
terminal factor \(d\).

The exact tension is:

> Can the quotient-certificate structure of a prime-free interval force more
> than three independent medium-prime certificates on every Richert-core
> survivor?

If yes, the \(P_3\)-upgrade route closes.  If no, one must return to the
Pell-synchronized quotient skeletons.

## 5. Next algebraic obstruction

For each atom type, synchronize the terminal equation with one quotient
certificate
\[
  m_0^2+t^2+\epsilon\equiv0\pmod p
\]
where the certificate prime \(p\) is one of the terminal atoms.

This creates three exact systems:

\[
  \mathrm{R2}\cap\mathrm{Cert},
  \qquad
  \mathrm{R3L}\cap\mathrm{Cert},
  \qquad
  \mathrm{R3R}\cap\mathrm{Cert}.
\]

The first target is to prove that one atom cannot certify too many structured
candidates in the same local block.  This is the atomic version of the
previous same-prime repetition obstruction, now tied to the Richert-core
\(P_3\) theorem.
