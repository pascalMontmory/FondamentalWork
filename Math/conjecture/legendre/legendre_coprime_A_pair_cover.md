# Coprime A-Block Pair Cover

This note turns the coprime complete A-block obstruction into an exact cover
by pairs of primes.

It builds on `legendre_A_block_gcd.md`, where the full gcd of the two
candidates in a complete A-block was computed.

Throughout,
\[
  n=3m.
\]

## 1. Oriented complete A-blocks

Let
\[
  a=3q+1,\qquad b=3q+2.
\]
In a complete A-block, one of \(a,b\) lies on A0 and the other lies on A1.
Define:
\[
  t_1(q)=
  \begin{cases}
  a,&a\equiv m\pmod2,\\
  b,&a\not\equiv m\pmod2,
  \end{cases}
\]
and
\[
  t_0(q)=
  \begin{cases}
  b,&a\equiv m\pmod2,\\
  a,&a\not\equiv m\pmod2.
  \end{cases}
\]
Thus \(t_1(q)\) is the A1 coordinate and \(t_0(q)\) is the A0 coordinate.

The two candidates are
\[
  U_q=9m^2+t_1(q)^2+1,
  \qquad
  G_q=9m^2+t_0(q)^2.
\]

The block is coprime exactly when
\[
  \gcd(t_1(q),9m^2+1)=1.
\]
For such a block,
\[
  \gcd(U_q,G_q)=1.
\]

## 2. Certificates on a coprime block

Assume a coprime complete A-block fails, so both \(U_q\) and \(G_q\) are
composite.

Then there exist primes
\[
  p_1,p_0\le3m
\]
such that
\[
  p_1\mid U_q,
  \qquad
  p_0\mid G_q.
\]
Because \(\gcd(U_q,G_q)=1\), one has
\[
  p_1\ne p_0.
\]

The A0 prime satisfies the Gaussian restriction:
\[
  p_0\equiv1\pmod4,\qquad p_0\nmid3m.
\]
Moreover
\[
  p_0\nmid t_0(q),
\]
because \(p_0\mid t_0(q)\) and \(p_0\mid G_q\) would imply
\[
  p_0\mid9m^2,
\]
contradicting \(p_0\nmid3m\).

The A1 prime satisfies
\[
  p_1\nmid t_1(q).
\]
Indeed, if \(p_1\mid t_1(q)\), then \(p_1\mid U_q\) gives
\[
  p_1\mid9m^2+1,
\]
contradicting
\[
  \gcd(t_1(q),9m^2+1)=1.
\]

Thus in a coprime failing block both coordinate variables are invertible
modulo their certificate primes.

## 3. Pair congruences

The certificate congruences are:
\[
  t_0(q)^2\equiv-9m^2\pmod{p_0},
\]
and
\[
  t_1(q)^2\equiv-9m^2-1\pmod{p_1}.
\]

Since
\[
  t_0(q),t_1(q)\in\{3q+1,3q+2\},
\]
and \(p_0,p_1\ge5\), the number \(3\) is invertible modulo both primes.
Therefore each root modulo \(p_i\) gives a linear congruence for \(q\).

For a fixed ordered pair
\[
  (p_0,p_1),
  \qquad
  p_0\ne p_1,
\]
the A0 congruence has at most two roots for \(t_0(q)\) modulo \(p_0\), and
the A1 congruence has at most two roots for \(t_1(q)\) modulo \(p_1\).

By the Chinese remainder theorem, the pair \((p_0,p_1)\) certifies at most
\[
  4
\]
residue classes of \(q\) modulo
\[
  p_0p_1.
\]

This is the pair-cover form of the coprime A-block obstruction.

## 4. Exact pair-cover obstruction

Let \(\mathcal Q_{\mathrm{cop}}(m)\) be the set of \(q\) for which
\[
  B_q=\{3q+1,3q+2\}
\]
is a complete coprime A-block.

If the combined A-channel fails on all coprime complete blocks, then
\[
  \mathcal Q_{\mathrm{cop}}(m)
\]
is covered by residue classes attached to ordered prime pairs
\[
  (p_0,p_1)
\]
with:

\[
\begin{array}{ll}
  p_0\le3m, & p_0\equiv1\pmod4,\quad p_0\nmid3m,\\
  p_1\le3m, & p_1\ge5,\quad p_1\ne p_0,
\end{array}
\]
and congruences
\[
  t_0(q)^2\equiv-9m^2\pmod{p_0},
  \qquad
  t_1(q)^2\equiv-9m^2-1\pmod{p_1}.
\]

Equivalently:

> A counterexample must cover every coprime complete A-block by a pair of
> distinct small primes, where each pair contributes at most four CRT classes
> modulo its product.

This is strictly stronger than the original small-prime cover, because the
two members of a coprime block cannot reuse the same prime.

## 5. Large-modulus consequence

Let
\[
  Q_{\max}(m)=\max \mathcal Q_{\mathrm{cop}}(m)
\]
when the set is nonempty.

If
\[
  p_0p_1>Q_{\max}(m)
\]
then each CRT class modulo \(p_0p_1\) contains at most one nonnegative
integer
\[
  q\le Q_{\max}(m).
\]
Thus large prime pairs cannot create dense coverage of the block interval.

Dense coverage, if it exists, must come from small ordered pairs
\[
  p_0p_1\le Q_{\max}(m),
\]
plus isolated hits from larger pairs.

Since complete A-blocks have
\[
  3q+2\le\sqrt{6m}+O(1),
\]
one has
\[
  Q_{\max}(m)\le \frac{\sqrt{6m}-1}{3}
\]
up to the endpoint convention.

Therefore any dense pair-cover must use prime pairs satisfying roughly
\[
  p_0p_1\lesssim \sqrt m.
\]
This is a severe restriction, because \(p_0\equiv1\pmod4\) and both primes
must satisfy the two quadratic residue conditions above.

## 6. Next exact target

The next proof target is:

Show that the small ordered pairs
\[
  p_0p_1\le Q_{\max}(m)
\]
cannot cover all coprime complete A-blocks, and that the remaining large
pairs give only isolated hits insufficient to fill the gaps.

This is still not a proof of Legendre.  It is the current exact bottleneck
after the A-block gcd reduction.
