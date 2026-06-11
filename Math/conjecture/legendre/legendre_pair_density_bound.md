# Pair Incidence Density Bound

This note computes the exact density contributed by one ordered pair of
certificate primes in the coprime A-block incidence geometry.

It also records a failed route: the naive union bound is not strong enough by
itself to close Legendre.  The point of the computation is to identify the
extra structure still needed.

## 1. Setup

Let
\[
  (p_0,p_1)
\]
be an ordered pair of distinct primes with
\[
  p_0\equiv1\pmod4,\qquad p_0,p_1\ge5.
\]
The A0 prime is \(p_0\), and the A1 prime is \(p_1\).

The pair incidence lives modulo
\[
  p_0p_1
\]
in both variables \(m\) and \(q\).

For simplicity in this local count, ignore the global inequalities
\[
  p_i\le3m
\]
and the endpoint restrictions on complete blocks.  Those return later as
global constraints.

## 2. A0 local count

Modulo \(p_0\), A0 requires
\[
  t_0^2\equiv-9m^2\pmod{p_0}.
\]
Since
\[
  p_0\equiv1\pmod4,
\]
there are two square roots of \(-1\).  For every
\[
  m\not\equiv0\pmod{p_0},
\]
there are exactly two choices of \(t_0\bmod p_0\), hence exactly two choices
of \(q\bmod p_0\).

Thus the A0 side contributes
\[
  2(p_0-1)
\]
incidence pairs
\[
  (m,q)\bmod p_0.
\]

## 3. A1 local count

Modulo \(p_1\), A1 requires
\[
  t_1^2\equiv-9m^2-1\pmod{p_1},
\]
with nonzero right side.

From the A1 local filter, the number of \(m\bmod p_1\) for which this has
nonzero roots is
\[
R_{p_1}=
\begin{cases}
\dfrac{p_1-3}{2},&p_1\equiv1\pmod4,\\[2mm]
\dfrac{p_1+1}{2},&p_1\equiv3\pmod4.
\end{cases}
\]
For each such \(m\), there are exactly two roots for \(t_1\), hence two
classes of \(q\bmod p_1\).

Thus the A1 side contributes
\[
  2R_{p_1}
\]
incidence pairs
\[
  (m,q)\bmod p_1.
\]

## 4. Product count

By the Chinese remainder theorem, the ordered pair \((p_0,p_1)\) contributes
exactly
\[
  4(p_0-1)R_{p_1}
\]
incidence points
\[
  (m,q)\bmod p_0p_1.
\]

Since the ambient space has size
\[
  (p_0p_1)^2,
\]
the local density is
\[
  \boxed{
  \delta(p_0,p_1)
  =
  \frac{4(p_0-1)R_{p_1}}{p_0^2p_1^2}.
  }
\]

Equivalently:

If \(p_1\equiv1\pmod4\),
\[
  \delta(p_0,p_1)
  =
  \frac{2(p_0-1)(p_1-3)}{p_0^2p_1^2}.
\]
If \(p_1\equiv3\pmod4\),
\[
  \delta(p_0,p_1)
  =
  \frac{2(p_0-1)(p_1+1)}{p_0^2p_1^2}.
\]

In either case,
\[
  \delta(p_0,p_1)<\frac{2}{p_0p_1}
  \left(1+O\left(\frac1{p_1}\right)\right).
\]

## 5. Why the naive union bound does not close

For fixed \(m\), the block interval has length about
\[
  Q_{\max}(m)\asymp \sqrt m.
\]
Large products
\[
  p_0p_1>Q_{\max}(m)
\]
give only isolated \(q\)-hits per CRT class.  Dense coverage would therefore
have to come from smaller products.

However, summing the local upper density
\[
  \frac{2}{p_0p_1}
\]
over all admissible ordered pairs with
\[
  p_0p_1\le Q_{\max}(m)
\]
does not produce a uniform contradiction.  The harmonic sum over prime pairs
can grow like a square of a logarithm:
\[
  \sum_{p_0p_1\le Q}\frac1{p_0p_1}
\]
is not bounded away from \(1\) by a simple absolute argument.

Thus the naive density union bound is too weak.

This is a useful failed route: pair density alone does not close the
combined A-channel.

## 6. Structure still unused

The density bound ignores several exact constraints:

1. The same integer \(m\) is fixed across all pairs.
2. A1 availability depends on
   \[
     \left(\frac{-9m^2-1}{p_1}\right)=1.
   \]
3. Bridge blocks have already been removed:
   \[
     \gcd(t_1(q),9m^2+1)=1.
   \]
4. The \(q\)-classes from different pairs are not arbitrary; they come from
   two oriented conic systems.
5. Large products are isolated and cannot create intervals of coverage.

The next proof attempt must use at least one of these correlations.

## 7. Next exact target

The most promising next target is a fixed-\(m\) large-sieve style statement:

For the set of available A1 primes
\[
  \mathcal P_1(m)=
  \left\{
  p\le3m:
  \left(\frac{-9m^2-1}{p}\right)=1,\quad
  p\nmid9m^2+1
  \right\},
\]
show that the projected \(q\)-classes from pairs
\[
  (p_0,p_1),\qquad p_0\equiv1\pmod4,\quad p_1\in\mathcal P_1(m),
\]
cannot cover all coprime complete A-blocks.

This is still a proof target, not a completed proof.
