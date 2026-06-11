# Primitive Double-Cover Reduction

This note turns the primitive Gaussian channel into an exact double-cover
condition.  It is the strongest current reformulation of the four-offset
Legendre route.

## 1. Primitive Channel Recap

Work with
\[
  A=n^2+t^2,
\]
where
\[
  1\le t\le\lfloor\sqrt{2n}\rfloor,
  \qquad \gcd(n,t)=1,
  \qquad n+t\equiv1\pmod2.
\]
On this channel, \(A\) is an odd primitive Gaussian norm.

The four-offset family
\[
  A-1,
  \quad A,
  \quad A+1,
  \quad A+2
\]
collapses after the deterministic \(2,3\)-layer to:

\[
\begin{array}{c|c|c}
  \text{condition mod }3 & A\bmod6 & \text{remaining condition} \\
  \hline
  \text{exactly one of } n,t \text{ divisible by }3 & 1 & A\text{ prime} \\
  \text{neither } n \text{ nor } t \text{ divisible by }3 & 5 & A\text{ prime or }A+2\text{ prime}.
\end{array}
\]

Thus a counterexample must force primality failure in one of two precise ways.
The \(A+2\) alternative is used only on the interior subrange
\[
  t^2+2\le2n.
\]

## 2. The Gaussian Bad Set

Define the primitive Gaussian bad set
\[
  G(n)=
  \bigcup_{\substack{p\le n\\ p\equiv1\pmod4}}
  \{t: t^2\equiv -n^2\pmod p\}.
\]

This definition is exact on primitive \(t\)'s.  If
\[
  A=n^2+t^2
\]
is composite and \(\gcd(n,t)=1\), then every odd prime divisor of \(A\) is
\(1\pmod4\).  Since \(A<(n+1)^2\), at least one such divisor satisfies
\[
  p\le n.
\]
Therefore
\[
  A\text{ composite}\quad\Longleftrightarrow\quad t\in G(n)
\]
for primitive opposite-parity \(t\) in the admissible interval.

## 3. The Twin-Shift Bad Set

Define the shifted bad set
\[
  T(n)=
  \bigcup_{\substack{q\le n\\ q>3}}
  \{t: t^2\equiv -n^2-2\pmod q\}.
\]

On the primitive Case II channel, the candidate
\[
  A+2=n^2+t^2+2
\]
is odd and not divisible by \(3\).  If it is composite, then it has a prime
divisor
\[
  q\le n,
\]
and this divisor must satisfy \(q>3\).  Hence, when \(t^2+2\le2n\),
\[
  A+2\text{ composite}\quad\Longleftrightarrow\quad t\in T(n)
\]
inside Case II.

No congruence class restriction like \(q\equiv1\pmod4\) is available for
\(A+2\).  This asymmetry is the point: the Gaussian candidate is covered only
by \(1\pmod4\) primes, while the twin-shift can use all primes \(q>3\).

## 4. Exact Counterexample Conditions

Let
\[
  I_n=\{1\le t\le\lfloor\sqrt{2n}\rfloor:
  \gcd(n,t)=1,\\ n+t\equiv1\pmod2\}.
\]
On this set the Gaussian candidate \(A=n^2+t^2\) is admissible.  Also define
the interior subset
\[
  I_n^+=\{t\in I_n:t^2+2\le2n\}.
\]
On \(I_n^+\), the twin-shift candidate \(A+2\) is also admissible.

A counterexample to the four-offset lemma must satisfy the following exact
conditions on \(I_n\).

### Case A: \(3\mid n\)

If \(3\mid n\), then primitivity forces \(3\nmid t\).  Thus exactly one of
\(n,t\) is divisible by \(3\) for every \(t\in I_n\).  The only residual
candidate is \(A\).

Therefore a counterexample with \(3\mid n\) must satisfy
\[
  I_n\subseteq G(n).
\]

This is a pure Gaussian cover by primes \(1\pmod4\).

### Case B: \(3\nmid n\)

If \(3\nmid n\), split
\[
  I_n=I_n^{(0)}\sqcup I_n^{(\ast)},
\]
where
\[
  I_n^{(0)}=\{t\in I_n:3\mid t\},
\]
and
\[
  I_n^{(\ast)}=\{t\in I_n:3\nmid t\}.
\]

For \(t\in I_n^{(0)}\), exactly one of \(n,t\) is divisible by \(3\), so only
\(A\) remains.  Hence a counterexample must satisfy
\[
  I_n^{(0)}\subseteq G(n).
\]

For \(t\in I_n^{(\ast)}\), neither \(n\) nor \(t\) is divisible by \(3\), so
the Gaussian candidate \(A\) must fail.  If \(t\in I_n^+\), then the
twin-shift candidate \(A+2\) is also admissible and must fail:
\[
  A\text{ composite},
  \qquad A+2\text{ composite}.
\]
Thus a counterexample must satisfy
\[
  I_n^{(\ast)}\subseteq G(n),
  \qquad
  I_n^{(\ast)}\cap I_n^+\subseteq G(n)\cap T(n).
\]

Combining the two subcases:
\[
  I_n^{(0)}\subseteq G(n),
  \qquad
  I_n^{(\ast)}\subseteq G(n),
  \qquad
  I_n^{(\ast)}\cap I_n^+\subseteq G(n)\cap T(n).
\]

## 5. The Main Rigidity

The reduction is now exact:

First, every counterexample must satisfy the universal primitive Gaussian
cover
\[
  I_n\subseteq G(n).
\]
This condition is independent of \(n\bmod3\).  It simply says that every
primitive opposite-parity Gaussian norm in the Legendre interval must be
composite.

Second, if \(3\nmid n\), the interior nonmultiples of \(3\) must satisfy the
additional double condition
\[
  I_n^{(\ast)}\cap I_n^+\subseteq G(n)\cap T(n).
\]

The interior double condition is extremely restrictive.  It says that for most
primitive \(t\)'s, a counterexample must simultaneously find:

1. a prime \(p\le n\), \(p\equiv1\pmod4\), with
   \[
     t^2\equiv -n^2\pmod p;
   \]
2. a distinct prime \(q\le n\), \(q>3\), with
   \[
     t^2\equiv -n^2-2\pmod q.
   \]

For a fixed \(t\), the primes \(p\) and \(q\) are distinct because a prime
\(>3\) cannot divide both \(A\) and \(A+2\).

## 6. Lemma P in Double-Cover Form

Lemma P is equivalent to the nonexistence of the following covers:

1. for every \(n\),
   \[
     I_n\subseteq G(n);
   \]
2. additionally, if \(3\nmid n\),
   \[
     I_n^{(\ast)}\cap I_n^+\subseteq G(n)\cap T(n).
   \]

This is the next proof target.  It removes all deterministic small-prime
noise and leaves only a Gaussian cover and a Gaussian/twin-shift double cover.
