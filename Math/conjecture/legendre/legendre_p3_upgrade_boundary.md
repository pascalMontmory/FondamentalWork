# Boundary of the P3 Upgrade Route

This note records a proof-level boundary for the attempted upgrade
\[
  P_3\text{ between squares}\quad\Longrightarrow\quad\text{prime between squares}.
\]

The route is still useful, but it cannot close Legendre from a single
terminal \(P_3\) survivor.  A proof would have to be collective: it must
combine the Richert-weighted family of survivors with the quotient
certificates forced by prime-freeness.

## 1. The single-survivor obstruction is compatible

In the Richert-core terminal language, the semiprime type R2 is
\[
  A=pq,
  \qquad
  p=n-a,\quad q=n+a+k,
\]
with
\[
  z\le p\le n<q,
\]
and terminal condition
\[
  1\le nk-a(a+k)\le2n.
\]

There is no algebraic contradiction here.

Indeed, the terminal condition is exactly
\[
  A-n^2=nk-a(a+k).
\]

For \(a=0\), this becomes
\[
  A=n(n+k),
  \qquad
  1\le nk\le2n,
\]
so
\[
  k\in\{1,2\}.
\]

The case \(k=2\) gives the formally admissible semiprime shape
\[
\boxed{
  A=n(n+2)=n^2+2n\in(n^2,(n+1)^2).
}
\]

This endpoint is not in Campbell's open analytic set
\[
  \mathcal A(n^2)=\mathbb Z\cap(n^2,n^2+2n),
\]
but it is in the full Legendre interval.  It shows that the Legendre
interval geometry itself does not object to a terminal semiprime at the upper
edge.

Inside Campbell's open set, R2 is also algebraically compatible.  For
example,
\[
  n=10,\qquad p=7,\qquad q=17
\]
gives
\[
  pq=119\in(100,120)=\mathcal A(100),
\]
with
\[
  p=10-3,\qquad q=10+3+4.
\]

The point is not that such examples occur in the large Richert range.  The
point is that the R2 equations themselves are not contradictory.  A proof
cannot close by saying "terminal semiprime" alone.

The conclusion is:

\[
\boxed{
  \text{A single terminal }P_3\text{ survivor cannot force a prime.}
}
\]

Any upgrade must use more than existence.

## 2. Why the terminal descent criterion needs a collective input

The previous descent criterion said:

> terminal composite \(P_3\) survivor \(\Rightarrow\) smaller prime-free
> interval.

The R2 boundary above shows that this implication is false as a statement
about one survivor.  A full-interval semiprime at
\[
  n^2+2n=(n+1)^2-1
\]
or an open-set R2 semiprime such as \(7\cdot17\) for \(n=10\) does not
naturally generate a smaller prime-free Legendre interval.

Therefore the correct descent target must be:

> the entire Richert-positive weighted set of terminal composites, together
> with the prime-free quotient certificates, forces a smaller counterexample
> or an impossible certificate cover.

This is a collective obstruction, not a pointwise obstruction.

## 3. Certificate pressure must exceed atom capacity

For a Richert-core terminal \(P_3\), there are at most three prime atoms.
Prime-freeness supplies at least one medium-prime certificate for the
survivor itself, but that is not enough: one atom can certify its own
compositeness.

To get a contradiction, the certificate structure must force the same
terminal survivor, or a tightly coupled local packet around it, to require
more independent certificate primes than its atom count allows.

The useful target is therefore:

> Atom-capacity lemma.  In a prime-free interval, every Richert-positive
> terminal packet coupled to a \(P_3\) survivor requires at least four
> independent medium-prime certificates.

If such a packet lemma is true, it contradicts
\[
  \Omega(A)\le3.
\]

The word "packet" is essential.  The survivor alone needs only one
certificate and is not contradictory.

## 4. Natural packets

The existing Legendre work already has packet structures:

- A-blocks:
  \[
    9m^2+t_0(q)^2,
    \qquad
    9m^2+t_1(q)^2+1;
  \]
- first-four block gates modulo \(70\);
- no-triple same-prime repetition;
- Pell-synchronized quotient skeletons.

The \(P_3\) upgrade should attach a Richert terminal survivor to one of these
packets.  The packet then asks:

1. which atom of the survivor certifies which packet member?
2. can one atom repeat across the packet without violating the repetition
   obstructions?
3. if repetition is impossible, does the packet require four certificates?

This is now a precise closure route:

\[
  \text{Richert survivor}
  +
  \text{local packet}
  +
  \text{no-repetition}
  \Longrightarrow
  \Omega(A)\ge4,
\]
contradicting \(P_3\).

## 5. Next exact task

The next task is to define the smallest packet around a Richert-core terminal
survivor that is forced by prime-freeness.

The likely candidate is a two-layer A-block packet, because it already
requires two transverse certificates in coprime blocks.  To close via
atom-capacity, one needs to prove that a Richert terminal survivor controls
or intersects two such blocks in a way that raises the certificate count from
two to four.

If no such forced packet exists, then the \(P_3\)-upgrade route should be
downgraded: Campbell's theorem is excellent context, but the closure path
returns to Pell-synchronized quotient skeleton elimination.
