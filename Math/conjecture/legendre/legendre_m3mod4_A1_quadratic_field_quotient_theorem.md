# A1 Quadratic-Field Quotient Theorem

This note sharpens the self-residue filter for the A1 offsets in the hard
\(m\equiv3\pmod4\) branch.

The A1 offsets are
\[
  c\in\{2,26,50,122\}.
\]

For every A1 row the quotient satisfies
\[
  f\equiv9\pmod{12},
\]
so \(f\) is odd and divisible by \(3\).  The self-residue condition is
\[
\boxed{
  u^2\equiv-c\pmod f.
}
\]

Thus every prime power in \(f\) is governed by the quadratic field
\[
  \mathbb Q(\sqrt{-c}).
\]

## 1. Prime-power criterion

Let \(q\) be an odd prime and write
\[
  q^\alpha\Vert f,
  \qquad
  \gamma=v_q(c).
\]

The congruence
\[
  u^2\equiv-c\pmod{q^\alpha}
\]
is solvable if and only if one of the following alternatives holds.

### Unramified case: \(q\nmid c\)

One must have
\[
\boxed{
  \left(\frac{-c}{q}\right)=1.
}
\]

Equivalently, \(q\) splits in
\[
  \mathbb Q(\sqrt{-c}).
\]

Once this holds modulo \(q\), Hensel lifting gives solutions modulo every
\(q^\alpha\).

### Ramified case: \(q\mid c\)

If
\[
  \alpha\le\gamma,
\]
then \(u=0\) works.

Assume now
\[
  \alpha>\gamma.
\]

Then a solution can exist only if \(\gamma\) is even.  Writing
\[
  c=q^\gamma c',
  \qquad
  q\nmid c',
\]
the remaining condition is
\[
\boxed{
  \left(\frac{-c'}{q}\right)=1.
}
\]

If \(\gamma\) is odd, no solution exists for \(\alpha>\gamma\), because the
valuation of a square is even.

## 2. Consequence for the four A1 offsets

The offset factorizations are
\[
\begin{array}{c|c}
  c & \text{factorization}\\
  \hline
  2 & 2\\
  26 & 2\cdot13\\
  50 & 2\cdot5^2\\
  122 & 2\cdot61.
\end{array}
\]

Since \(f\) is odd, the prime \(2\) never occurs in \(f\).  Therefore:

\[
\begin{array}{c|c}
  c & \text{condition on odd prime powers }q^\alpha\Vert f\\
  \hline
  2
    & \left(\frac{-2}{q}\right)=1
      \text{ for every }q\mid f\\
  26
    & v_{13}(f)\le1,\quad
      \left(\frac{-26}{q}\right)=1
      \text{ for every }q\mid f,\ q\ne13\\
  50
    & v_5(f)\le2,\quad
      \left(\frac{-50}{q}\right)=1
      \text{ for every }q\mid f,\ q\ne5\\
  122
    & v_{61}(f)\le1,\quad
      \left(\frac{-122}{q}\right)=1
      \text{ for every }q\mid f,\ q\ne61.
\end{array}
\]

For \(c=2\), this is the elementary congruence condition
\[
  q\equiv1,3\pmod8
  \qquad(q\mid f).
\]

For \(c=50\), away from \(5\) the square factor \(5^2\) disappears, so the
same unramified condition is again
\[
  q\equiv1,3\pmod8
  \qquad(q\mid f,\ q\ne5),
\]
with the ramified cap
\[
  v_5(f)\le2.
\]

For \(c=26\) and \(c=122\), the ramified primes have odd valuation in \(c\),
so they may divide \(f\) at most once.

## 3. Compatibility with the forced factor \(3\)

All A1 quotients satisfy
\[
  3\mid f.
\]

This is compatible with every A1 offset because
\[
  c\equiv2\pmod3,
  \qquad
  -c\equiv1\pmod3.
\]

Thus the unavoidable prime \(3\) is always locally allowed, to any exponent.
The restrictions begin with the other prime divisors of \(f\).

## 4. Closure use

Together with the A0 theorem, every skipped quotient in the hard
\(m\equiv3\pmod4\) branch is now constrained by its own prime divisors:

- A0 quotients lie in the sum-of-two-squares semigroup, with an
  offset-specific \(2\)-adic ceiling.
- A1 quotients lie in offset-specific splitting semigroups for
  \(\mathbb Q(\sqrt{-2})\), \(\mathbb Q(\sqrt{-26})\),
  \(\mathbb Q(\sqrt{-50})\), or \(\mathbb Q(\sqrt{-122})\), with ramified
  caps at \(13\), \(5\), and \(61\).

This turns arbitrary skipped ranks into a multiplicative compatibility
problem rather than an external finite-prime sieve.

The next exact descent target is:
\[
\boxed{
  \text{A0/A1 quotient splitting laws}
  +\text{pairwise Pell synchronization}
  \Longrightarrow \text{rank descent into the closed prefix range.}
}
\]
