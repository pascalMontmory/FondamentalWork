# Primitive Gaussian Channel Reduction

This note sharpens the four-consecutive certificate layer on the natural
Gaussian-safe values of \(t\): those with
\[
  \gcd(n,t)=1,
  \qquad n+t\equiv1\pmod2.
\]
For such \(t\), the Gaussian norm
\[
  A=n^2+t^2
\]
is odd and primitive.  Therefore any prime divisor of \(A\) is either
\(1\pmod4\) or divides \(\gcd(n,t)\).  Under primitivity, the latter case is
absent.

## 1. The Modulo \(6\) Split

Assume
\[
  \gcd(n,t)=1,
  \qquad n+t\equiv1\pmod2.
\]
Then \(A=n^2+t^2\) is odd.  Since \(\gcd(n,t)=1\), the pair \((n,t)\) is not
both divisible by \(3\).  Hence exactly one of the following cases holds.

### Case I: exactly one of \(n,t\) is divisible by \(3\)

Then
\[
  n^2+t^2\equiv1\pmod3.
\]
Since \(A\) is odd,
\[
  A\equiv1\pmod6.
\]
The four candidates are
\[
  A-1,
  \quad A,
  \quad A+1,
  \quad A+2.
\]
Here
\[
  A-1\equiv0\pmod2,
  \qquad A+1\equiv0\pmod2,
\]
and
\[
  A-1\equiv0\pmod3,
  \qquad A+2\equiv0\pmod3.
\]
Thus, away from the trivial small boundary values, the only candidate not
already certified composite by \(2\) or \(3\) is
\[
  A=n^2+t^2.
\]

Therefore, in Case I, the four-offset family succeeds at this \(t\) if and
only if \(A\) is prime.

If \(A\) is composite, then primitivity forces its prime certificates to be
\(1\pmod4\), and the correction offsets cannot rescue this particular \(t\):
\[
  A-1,
  A+1,
  A+2
\]
are already deterministically composite.

### Case II: neither \(n\) nor \(t\) is divisible by \(3\)

Then
\[
  n^2\equiv t^2\equiv1\pmod3,
\]
so
\[
  A=n^2+t^2\equiv2\pmod3.
\]
Since \(A\) is odd,
\[
  A\equiv5\pmod6.
\]
Now
\[
  A-1\equiv0\pmod2,
  \qquad A+1\equiv0\pmod2,
\]
and
\[
  A+1\equiv0\pmod3.
\]
The residual candidates are exactly
\[
  A,
  \qquad A+2.
\]

Therefore, in Case II, the four-offset family succeeds at this \(t\) if and
only if at least one of
\[
  A=n^2+t^2,
  \qquad A+2=n^2+t^2+2
\]
is prime.

If both are composite, then \(A\)'s primitive Gaussian certificate must use a
prime \(1\pmod4\), while \(A+2\) needs a distinct prime \(p>3\).

## 2. Exact Primitive-Channel Reformulation

For primitive opposite-parity \(t\), the four-offset test collapses to:

\[
\begin{array}{c|c|c}
  \text{condition mod }3 & A\bmod6 & \text{prime condition needed} \\
  \hline
  \text{exactly one of } n,t \text{ divisible by }3 & 1 & A\text{ prime} \\
  \text{neither } n \text{ nor } t \text{ divisible by }3 & 5 & A\text{ prime or }A+2\text{ prime}.
\end{array}
\]

This is an exact reduction, not a heuristic.

It shows that the corrected family does not provide four independent chances
on the natural Gaussian-safe channel.  After the deterministic \(2,3\)-layer,
there are only:

- one real chance in Case I;
- two real chances in Case II.

## 3. Consequence for a Counterexample

A counterexample to the four-offset lemma must satisfy the following for every
primitive opposite-parity \(t\) in the admissible range:

1. if exactly one of \(n,t\) is divisible by \(3\), then
   \[
     n^2+t^2
   \]
   is composite;
2. if neither \(n\) nor \(t\) is divisible by \(3\), then
   \[
     n^2+t^2
     \quad\text{and}\quad
     n^2+t^2+2
   \]
   are both composite.

This is much sharper than a generic residue-cover obstruction.  A hypothetical
counterexample must destroy all primitive Gaussian norms in Case I, and all
primitive Gaussian/twin-shift pairs in Case II.

## 4. Next Exact Target

The next lemma should attack the primitive channel directly.

Lemma P candidate.  For every \(n\ge2\), there exists
\[
  1\le t\le\lfloor\sqrt{2n}\rfloor,
  \qquad \gcd(n,t)=1,
  \qquad n+t\equiv1\pmod2,
\]
such that either:

1. exactly one of \(n,t\) is divisible by \(3\) and \(n^2+t^2\) is prime; or
2. neither \(n\) nor \(t\) is divisible by \(3\), and at least one of
   \[
     n^2+t^2,
     \qquad n^2+t^2+2
   \]
   is prime, with the second candidate used only when
   \[
     t^2+2\le2n.
   \]

Lemma P would imply the four-offset lemma, hence Legendre.

The point is that Lemma P is no longer a four-offset statement.  It is a
primitive Gaussian/twin-shift statement with an exact modulo \(6\) split.
