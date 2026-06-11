# Exact GCD in Complete A-Blocks

This note sharpens the adjacent-pair collision lemma from
`legendre_combined_A_cover.md`.

The previous lemma showed that if one prime certifies both elements of a
complete A-block, then it must divide
\[
  9m^2+1.
\]
Here we compute the full gcd of the two block candidates.

Throughout,
\[
  n=3m,
\]
and the combined A-candidate is
\[
  P_m(t)=9m^2+t^2+\epsilon_m(t),
\]
where
\[
  \epsilon_m(t)=
  \begin{cases}
  0,&t\not\equiv m\pmod2,\\
  1,&t\equiv m\pmod2.
  \end{cases}
\]

Let
\[
  a=3q+1,\qquad b=3q+2=a+1
\]
be a complete A-block.

## 1. Exact block gcd

There are two parity cases.

### Case I: \(a\equiv m\pmod2\)

Then \(a\) lies on A1 and \(b\) lies on A0:
\[
  P_m(a)=9m^2+a^2+1,
  \qquad
  P_m(b)=9m^2+b^2.
\]
Both numbers are odd.  Their difference is
\[
  P_m(b)-P_m(a)=b^2-a^2-1=2a.
\]
Therefore
\[
  \gcd(P_m(a),P_m(b))=\gcd(P_m(a),2a)=\gcd(P_m(a),a).
\]
Reducing \(P_m(a)\) modulo \(a\) gives
\[
  P_m(a)\equiv9m^2+1\pmod a.
\]
Hence
\[
  \boxed{
  \gcd(P_m(a),P_m(b))=\gcd(a,9m^2+1).
  }
\]

### Case II: \(a\not\equiv m\pmod2\)

Then \(a\) lies on A0 and \(b\) lies on A1:
\[
  P_m(a)=9m^2+a^2,
  \qquad
  P_m(b)=9m^2+b^2+1.
\]
Again both numbers are odd, and
\[
  P_m(b)-P_m(a)=b^2-a^2+1=2b.
\]
Therefore
\[
  \gcd(P_m(a),P_m(b))=\gcd(P_m(b),2b)=\gcd(P_m(b),b).
\]
Reducing \(P_m(b)\) modulo \(b\) gives
\[
  P_m(b)\equiv9m^2+1\pmod b.
\]
Hence
\[
  \boxed{
  \gcd(P_m(a),P_m(b))=\gcd(b,9m^2+1).
  }
\]

## 2. Bridge divisor of a block

Define the bridge coordinate
\[
  c_q=
  \begin{cases}
  a,&a\equiv m\pmod2,\\
  b,&a\not\equiv m\pmod2.
  \end{cases}
\]
Then the two cases combine into the exact formula
\[
  \boxed{
  \gcd(P_m(3q+1),P_m(3q+2))=\gcd(c_q,9m^2+1).
  }
\]

Thus all common prime factors in a complete A-block are precisely bridge
prime factors:
\[
  p\mid c_q,\qquad p\mid9m^2+1.
\]
There is no hidden common divisor.

## 3. Coprime blocks

Call a complete A-block coprime if
\[
  \gcd(c_q,9m^2+1)=1.
\]
For such a block,
\[
  \gcd(P_m(3q+1),P_m(3q+2))=1.
\]

Therefore, if the combined A-channel fails on a coprime block, the two
certificates must be genuinely distinct prime divisors:
\[
  p_a\mid P_m(3q+1),\qquad
  p_b\mid P_m(3q+2),\qquad p_a\ne p_b.
\]

This is stronger than the previous bridge-prime statement: for coprime
blocks, bridge behavior is impossible altogether.

## 4. Sparse bridge blocks

A non-coprime complete block requires
\[
  \gcd(c_q,9m^2+1)>1.
\]
Equivalently, for some prime divisor \(p\) of \(9m^2+1\),
\[
  c_q\equiv0\pmod p.
\]

Since \(c_q\) is either \(3q+1\) or \(3q+2\), each bridge prime \(p\mid9m^2+1\)
selects at most one residue class of \(q\) modulo \(p\) in each parity
orientation.

Thus bridge blocks form an explicit union of arithmetic progressions indexed
by prime divisors of
\[
  9m^2+1.
\]

The proof target can now be stated without ambiguity:

> To close the combined A-channel, it is enough to show that among the
> complete A-blocks there exists a coprime block for which the two required
> independent certificates cannot both occur.

If such a block exists for every \(m\), then the combined A-channel always
produces a prime and the nonprimitive B-channel is unnecessary.

If not, the remaining obstruction is concentrated on the explicit bridge
progressions
\[
  c_q\equiv0\pmod p,\qquad p\mid9m^2+1.
\]

## 5. Exact next target

The next exact step is to study the coprime block obstruction:
\[
  \gcd(c_q,9m^2+1)=1,
\]
with both
\[
  P_m(3q+1)
  \quad\text{and}\quad
  P_m(3q+2)
\]
composite.

For such a block, a counterexample must assign two distinct primes
\[
  p_a,p_b\le3m
\]
satisfying two unrelated quadratic congruences.  The remaining task is to
turn this two-prime requirement into an incompatibility over the interval of
complete blocks.
