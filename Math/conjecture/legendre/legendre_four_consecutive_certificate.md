# Four-Consecutive Certificate Layer

This note isolates the next exact layer in the four-offset Legendre attack.
For fixed \(n,t\), set
\[
  A=n^2+t^2.
\]
The four candidates are the consecutive integers
\[
  A-1,\quad A,\quad A+1,\quad A+2.
\]
Thus the obstruction is not only a circle-cover problem; it is also a
four-consecutive-integer certificate problem.

## 1. Pairwise GCD Skeleton

For \(r,s\in\{-1,0,1,2\}\),
\[
  \gcd(A+r,A+s)\mid |r-s|.
\]
Consequently:

- a prime \(p>3\) divides at most one of the four candidates;
- the prime \(3\) can divide both \(A-1\) and \(A+2\), and no other pair;
- the prime \(2\) divides exactly two of the four candidates.

So after removing the deterministic small-prime layer \(2,3\), every remaining
compositeness certificate must be assigned to a distinct prime \(p>3\).

## 2. Parity Layer

Exactly two of
\[
  A-1,\quad A,\quad A+1,\quad A+2
\]
are even.

If \(A\) is even, then
\[
  A,\quad A+2
\]
are even, and
\[
  A-1,\quad A+1
\]
are odd.

If \(A\) is odd, then
\[
  A-1,\quad A+1
\]
are even, and
\[
  A,\quad A+2
\]
are odd.

Since all candidates lie above \(1\) except for the boundary case
\[
  t=1,\quad r=-1,
\]
the parity layer can certify exactly two candidates as composite whenever
those even candidates exceed \(2\).  Boundary cases must be kept explicit.

## 3. Modulo \(3\) Layer

Among four consecutive integers, either one or two are divisible by \(3\).
More exactly:

- if \(A\equiv1\pmod3\), then \(A-1\) and \(A+2\) are divisible by \(3\);
- if \(A\equiv0\pmod3\), then only \(A\) is divisible by \(3\);
- if \(A\equiv2\pmod3\), then only \(A+1\) is divisible by \(3\).

The two-hit case is special because it is the only way one odd prime can
certify two offsets at the same \(t\).  It occurs precisely when
\[
  n^2+t^2\equiv1\pmod3.
\]
Since squares modulo \(3\) are \(0,1\), this happens exactly in the following
cases:
\[
\begin{array}{c|c}
  n^2\bmod3 & t^2\bmod3 \\
  \hline
  0 & 1 \\
  1 & 0.
\end{array}
\]
Equivalently, exactly one of \(n,t\) is divisible by \(3\).

## 4. Residual Certificate Demand

Let
\[
  C(A)=\{A-1,A,A+1,A+2\}
\]
with inadmissible boundary values removed.  Suppose all admissible elements of
\(C(A)\) are composite.

Define \(S_2(A)\) as the admissible elements divisible by \(2\), and
\(S_3(A)\) as the admissible elements divisible by \(3\).  The residual demand
is
\[
  D(A)=C(A)\setminus(S_2(A)\cup S_3(A)).
\]
Every element of \(D(A)\) must have a prime divisor
\[
  p>3.
\]
Moreover, by the pairwise gcd skeleton, these primes must be distinct across
the elements of \(D(A)\).

Thus a counterexample to the four-offset lemma must provide, for every
admissible \(t\), distinct \(p>3\) certificates for every residual element in
\[
  D(n^2+t^2).
\]

## 5. Size of the Residual Demand

For interior \(t\), all four offsets are admissible.  The size of
\[
  D(A)
\]
depends only on \(A\bmod6\):
\[
\begin{array}{c|c|c|c}
  A\bmod6 & \text{even offsets} & \text{offsets divisible by }3 & |D(A)| \\
  \hline
  0 & 0,2 & 0 & 2 \\
  1 & -1,1 & -1,2 & 1 \\
  2 & 0,2 & 1 & 1 \\
  3 & -1,1 & 0 & 1 \\
  4 & 0,2 & -1,2 & 1 \\
  5 & -1,1 & 1 & 2.
\end{array}
\]
Here an offset \(r\) denotes the candidate \(A+r\).

So the residual demand is never larger than \(2\) after removing \(2\) and
\(3\).  But those residual certificates must be supplied for every \(t\), and
the Gaussian residual at \(r=0\), when present and primitive, can only use
primes \(1\pmod4\).

## 6. Gaussian Residual Positions

The Gaussian candidate \(A\) has offset \(r=0\).  From the table above, \(r=0\)
lies in the residual demand exactly when
\[
  A\bmod6\in\{1,5\}.
\]
In these cases \(A\) is odd and not divisible by \(3\).

If also \(\gcd(n,t)=1\), then any residual certificate for \(A=n^2+t^2\) must
be a prime
\[
  p\equiv1\pmod4.
\]

Therefore the hardest \(t\)-positions are those where
\[
  n^2+t^2\equiv1 \text{ or }5\pmod6,
  \qquad \gcd(n,t)=1.
\]
At such positions, the certificate system must spend a \(1\bmod4\) prime on
the Gaussian channel.

## 7. Exact Next Lemma

The next target is now sharper than the earlier circle-cover statement.

Lemma E candidate.  For every \(n\ge2\), there exists an admissible \(t\) such
that at least one element of
\[
  \{n^2+t^2-1,\ n^2+t^2,\ n^2+t^2+1,\ n^2+t^2+2\}
\]
escapes the deterministic \(2,3\)-layer and all possible residual
certificates by primes \(p>3\).

Equivalently, no counterexample can provide the required residual certificate
assignment for every admissible \(t\), with the Gaussian residual restricted
to primes \(1\pmod4\) on primitive \(t\)'s.

This lemma is still open, but it is an exact certificate nonexistence
statement.  It replaces a prime-gap question by a constrained assignment
problem over the four consecutive candidates.
