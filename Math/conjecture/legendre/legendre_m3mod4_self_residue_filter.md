# Self-Residue Filter for Arbitrary Skipped Ranks

This note gives the first non-finite-prime obstruction for arbitrary skipped
ranks in the hard \(m\equiv3\pmod4\) branch.

It comes from reducing each Pell line modulo its own quotient \(f\).

## 1. The self-residue congruence

The reduced line is
\[
  u^2=f^2+6mf-c.
\]

Reduce modulo \(f\).  The terms \(f^2\) and \(6mf\) vanish, giving
\[
\boxed{
  u^2\equiv -c\pmod f.
}
\]

Therefore:

\[
\boxed{
  -c\text{ must be a square modulo }f.
}
\]

Equivalently, for every odd prime
\[
  q\mid f,\qquad q\nmid c,
\]
one must have
\[
\boxed{
  \left(\frac{-c}{q}\right)=1.
}
\]

This is an intrinsic condition on the skipped rank itself.  It is not a
finite external local test.

The modulo \(7\) zero-filter used earlier is only the first special case of
this rule.

## 2. Consequence for the offsets

For the hard branch offsets
\[
  \mathcal C=
  \{2,4,16,26,50,64,100,122\},
\]
each row has its own allowed set of prime divisors of \(f\):

\[
\boxed{
  q\mid f,\ q\nmid c
  \quad\Longrightarrow\quad
  -c\in(\mathbb F_q^\times)^2.
}
\]

Thus arbitrary skipped ranks are not free.  They must lie in multiplicative
semigroups determined by quadratic characters.

For example:

- for \(c=16\), every odd prime \(q\mid f\), \(q\ne2\), must satisfy
  \[
    \left(\frac{-1}{q}\right)=1,
  \]
  hence
  \[
    q\equiv1\pmod4;
  \]
- for \(c=64\), the same condition holds;
- for \(c=4\) and \(c=100\), again the non-\(2,5\) odd prime divisors of
  \(f\) must satisfy the corresponding \(-c\)-quadratic-residue condition.

This explains why isolated bad prime divisors of \(f\) immediately kill
rank candidates.

## 3. Stronger than finite modular climbing

The previous note showed that no fixed finite set of independent external
prime tests can close arbitrary skipped ranks.

The self-residue filter avoids that obstruction because the tested primes
are the prime divisors of \(f\) itself.  As \(f\) climbs, new internal tests
appear automatically.

Thus the correct skipped-rank closure route is:

1. factor the candidate quotient \(f\);
2. reject it if any prime divisor violates
   \[
     \left(\frac{-c}{q}\right)=1;
   \]
3. combine the surviving self-residue-restricted quotients with pairwise
   Pell synchronization.

## 4. Descent target

A rank descent would follow from a theorem of the following form.

> If every row in the hard \(m\equiv3\pmod4\) system satisfies the
> self-residue filter and the pairwise Pell synchronization equations, then
> one can replace at least one quotient by a lower admissible quotient in the
> same layer, preserving all necessary local conditions.

Such a descent would eventually enter the already closed prefix range.

The exact next target is therefore:

\[
\boxed{
  \text{combine the self-residue filter with pairwise Pell synchronization}
  \text{ to force rank descent.}
}
\]

This is the first viable theoretical route beyond finite modular
certificates.
