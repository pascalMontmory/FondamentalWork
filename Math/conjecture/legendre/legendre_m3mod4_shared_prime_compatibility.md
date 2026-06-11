# Shared-Prime Compatibility in the Multiplicative Model

This note extracts the first edge constraint from the multiplicative rank
model.

The quotient theorems constrain each individual quotient \(f_c\).  Pairwise
Pell synchronization forces the eight quotients to coexist.  A necessary
compatibility condition is obtained by looking at primes that divide two
quotients at once.

Throughout, the hard branch is
\[
  A=3m,
  \qquad
  m\equiv3\pmod4,
\]
with offsets
\[
  c\in\{2,4,16,26,50,64,100,122\}.
\]

For each row,
\[
  u_c^2=f_c^2+6mf_c-c
\]
implies
\[
\boxed{
  u_c^2\equiv-c\pmod{f_c}.
}
\]

## 1. General shared-prime rule

Let \(q\) be an odd prime and suppose
\[
  q\mid f_c,\qquad q\mid f_d.
\]

If
\[
  q\nmid cd,
\]
then
\[
  \left(\frac{-c}{q}\right)=1,
  \qquad
  \left(\frac{-d}{q}\right)=1.
\]

Equivalently, \(q\) splits in both quadratic fields
\[
  \mathbb Q(\sqrt{-c}),
  \qquad
  \mathbb Q(\sqrt{-d}).
\]

Thus \(q\) splits completely in the biquadratic compositum
\[
\boxed{
  \mathbb Q(\sqrt{-c},\sqrt{-d}).
}
\]

In particular,
\[
\boxed{
  \left(\frac{cd}{q}\right)=1.
}
\]

This is only a necessary condition, but it is attached to an edge
\((c,d)\), not merely to a single vertex \(c\).

## 2. A0--A1 shared primes

Every A0 quotient is even and has odd part in
\[
  \mathcal S_4
  =
  \{s:\ s\text{ odd},\ 3\nmid s,\ q\mid s\Rightarrow q\equiv1\pmod4\}.
\]

Every A1 quotient is odd and divisible by \(3\).

Therefore, for any A0 offset
\[
  a\in\{4,16,64,100\}
\]
and any A1 offset
\[
  b\in\{2,26,50,122\},
\]
one has
\[
\boxed{
  \gcd(f_a,f_b)\ \text{is coprime to }6.
}
\]

Moreover every prime
\[
  q\mid\gcd(f_a,f_b)
\]
satisfies
\[
\boxed{
  q\equiv1\pmod4
}
\]
and, away from the ramified primes of \(b\),
\[
\boxed{
  \left(\frac{-b}{q}\right)=1.
}
\]

Since \(q\equiv1\pmod4\), this is equivalently
\[
  \left(\frac{b}{q}\right)=1.
\]

Thus:

\[
\begin{array}{c|c}
  b & \text{condition on }q\mid\gcd(f_a,f_b),\ q\nmid b\\
  \hline
  2 & q\equiv1\pmod8\\
  26 & q\equiv1\pmod4,\ \left(\frac{26}{q}\right)=1\\
  50 & q\equiv1\pmod8\\
  122 & q\equiv1\pmod4,\ \left(\frac{122}{q}\right)=1.
\end{array}
\]

The ramified A1 primes are compatible with A0 precisely because
\[
  13\equiv5\equiv61\equiv1\pmod4.
\]
Their exponents are still capped by the A1 theorem:
\[
  v_{13}(f_{26})\le1,
  \qquad
  v_5(f_{50})\le2,
  \qquad
  v_{61}(f_{122})\le1.
\]

## 3. A1--A1 shared primes

All A1 quotients are divisible by \(3\), and \(3\) is always allowed because
\[
  c\equiv2\pmod3,
  \qquad
  -c\equiv1\pmod3.
\]

Hence \(3\) is the universal A1 common prime and carries no obstruction by
itself.

For any odd prime
\[
  q\ne3
\]
that divides two A1 quotients \(f_c,f_d\), and is unramified for both
offsets, one must have
\[
\boxed{
  \left(\frac{-c}{q}\right)=
  \left(\frac{-d}{q}\right)=1.
}
\]

Equivalently, \(q\) splits completely in
\[
  \mathbb Q(\sqrt{-c},\sqrt{-d}).
\]

If \(q\) is ramified for one of the two offsets, the corresponding ramified
cap from the A1 quotient theorem still applies.

## 4. A0--A0 shared primes

For two A0 offsets, every shared odd prime is simply constrained by
\[
\boxed{
  q\equiv1\pmod4.
}
\]

The power of \(2\) in a common divisor is controlled by the offset-specific
ceilings:
\[
\begin{array}{c|c}
  c & v_2(f_c)\text{ ceiling}\\
  \hline
  4 & 3\\
  16 & 5\\
  64 & 7\\
  100 & 3.
\end{array}
\]

The zero-layer collapse and four-layer refinement give the sharper lower
and residue constraints recorded in the multiplicative model.

## 5. Edge formulation for descent

Attach to every offset \(c\) its multiplicative quotient semigroup
\[
  \mathcal M_c.
\]

For every edge \((c,d)\), define the shared-prime compatibility set
\[
  \mathcal E_{c,d}
  =
  \{q\text{ prime}:\ q\text{ may divide both }f_c\text{ and }f_d\}.
\]

The rules above give:

- A0--A1 edges have
  \[
    2,3\notin\mathcal E_{a,b};
  \]
- nonramified A0--A1 edge primes must satisfy both \(q\equiv1\pmod4\) and
  the A1 splitting condition;
- A1--A1 edge primes, except \(3\) and ramified primes, must split in a
  biquadratic field;
- A0--A0 edge primes are sums-of-two-squares primes, with \(2\)-adic
  ceilings.

Thus a hard-branch counterexample is not only a choice
\[
  f_c\in\mathcal M_c
\]
at each vertex.  It is a labelled complete graph in which every common
prime divisor of two vertex labels must lie in the edge set
\[
  \mathcal E_{c,d}.
\]

The next exact closure target becomes:
\[
\boxed{
  \text{multiplicative vertex semigroups}
  +\text{shared-prime edge compatibility}
  +\text{Pell synchronization}
  \Longrightarrow \text{rank descent.}
}
\]
