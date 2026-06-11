# Legendre's conjecture: residue-cover and Gaussian-integer route

Date: 2026-06-10.

## 1. Target

Legendre's conjecture asserts that for every integer \(n\ge 1\), the interval
\[
  (n^2,(n+1)^2)
\]
contains a prime.

Equivalently, at least one of
\[
  n^2+1,\ n^2+2,\ \ldots,\ n^2+2n
\]
is prime.

The problem is currently open; it is one of Landau's classical prime-number
problems.

## 2. Exact residue-cover reformulation

Let
\[
  P_{n+1}=\prod_{p\le n+1}p
\]
be the primorial up to \(n+1\).

For \(1\le m\le 2n\), the integer \(n^2+m\) is prime if and only if
\[
  \gcd(n^2+m,P_{n+1})=1.
\]

Indeed, if \(n^2+m\) is composite, then it has a prime divisor
\[
  q\le \sqrt{n^2+m}<n+1,
\]
except for the endpoint possibility \(q=n+1\), which is also covered by
\(P_{n+1}\). Conversely, if it is coprime to all primes \(\le n+1\), it has no
prime divisor at most its square root, hence is prime.

Therefore Legendre's conjecture is equivalent to:
\[
  \exists m\in\{1,\ldots,2n\}\quad
  \gcd(n^2+m,P_{n+1})=1.
\]

Equivalently, the interval \(\{1,\ldots,2n\}\) is not covered by the residue
classes
\[
  m\equiv -n^2\pmod p,\qquad p\le n+1.
\]

This is the clean combinatorial form:
\[
  \{1,\ldots,2n\}\not\subseteq
  \bigcup_{p\le n+1}\{m:m\equiv -n^2\pmod p\}.
\]

## 3. Non-standard observation: the forbidden residue is quadratic

For primes \(p\nmid n\),
\[
  -n^2\pmod p
\]
has Legendre symbol
\[
  \left(\frac{-n^2}{p}\right)=\left(\frac{-1}{p}\right).
\]

Thus, for \(p\equiv 3\pmod 4\), the forbidden residue is a quadratic
non-residue; for \(p\equiv 1\pmod 4\), it is a quadratic residue.

This suggests not treating the forbidden classes as arbitrary sieve classes.
They have character structure.

## 4. Gaussian-integer test family

Restrict to square offsets:
\[
  m=t^2,\qquad 1\le t\le \lfloor\sqrt{2n}\rfloor.
\]

Then
\[
  n^2+t^2=N(n+it)
\]
is a Gaussian norm and still lies in the Legendre interval.

If \(\gcd(n,t)=1\), no prime \(p\equiv 3\pmod 4\) divides \(n^2+t^2\). Indeed,
if \(p\equiv3\pmod4\) and \(p\mid n^2+t^2\), then
\[
  (nt^{-1})^2\equiv -1\pmod p,
\]
impossible unless \(p\mid t\), hence also \(p\mid n\).

So for primitive offsets \(t\), every odd prime divisor of \(n^2+t^2\) is
\(1\pmod4\).

This removes half of the small-prime obstruction in one stroke.

## 5. A sufficient lemma

The following lemma would prove Legendre.

Lemma G. For every \(n\ge 2\), there exists an integer
\[
  1\le t\le \sqrt{2n},\qquad \gcd(t,n)=1,
\]
such that no prime \(p\equiv 1\pmod4\), \(p\le n+1\), divides \(n^2+t^2\).

Proof that Lemma G implies Legendre:

By the observation above, no prime \(p\equiv3\pmod4\), \(p\le n+1\), divides
\(n^2+t^2\). Lemma G excludes the primes \(p\equiv1\pmod4\). The prime \(2\) is
also excluded when \(n,t\) have opposite parity; if needed this can be added to
the lemma. Hence
\[
  \gcd(n^2+t^2,P_{n+1})=1.
\]
Since
\[
  n^2<n^2+t^2\le n^2+2n<(n+1)^2,
\]
the integer \(n^2+t^2\) is prime.

## 6. Where the obstruction remains

Lemma G is still strong. Written modulo primes \(p\equiv1\pmod4\), it asks for
a small \(t\) avoiding at most two residues:
\[
  t\equiv \pm i_p n\pmod p,
\]
where \(i_p^2\equiv -1\pmod p\).

So the square-offset route converts Legendre into a much thinner covering
problem:
\[
  [1,\sqrt{2n}]
  \not\subseteq
  \bigcup_{\substack{p\le n+1\\p\equiv1\!\!\!\pmod4}}
  \{t:t\equiv \pm i_p n\pmod p\},
\]
plus a parity condition.

This is not a proof yet. The attractive point is that the original cover had
one residue class for every prime \(p\le n+1\) over an interval of length
\(2n\), whereas this reduced cover has two residue classes only for primes
\(1\pmod4\) over an interval of length \(\sqrt{2n}\), with residues constrained
by square roots of \(-1\).

The remaining task is to prove that this structured cover cannot be complete.

## 7. Computational checkpoint: Lemma G is false as stated

The first probe of Lemma G was implemented in
\[
  \texttt{Math/conjecture/legendre/tools/gaussian\_lemma\_g\_probe.py}.
\]
It tests the strict sufficient version: \(1\le t\le\lfloor\sqrt{2n}\rfloor\),
\(\gcd(n,t)=1\), \(n,t\) of opposite parity, and no prime
\[
  p\equiv1\pmod4,\qquad p\le n+1
\]
dividing \(n^2+t^2\).

The lemma fails already at \(n=12\).  Since
\[
  \lfloor\sqrt{24}\rfloor=4,
\]
the square offsets are \(t=1,2,3,4\).  The only primitive opposite-parity
candidate is \(t=1\), and
\[
  12^2+1^2=145=5\cdot29.
\]
The remaining square offsets give
\[
  148,\quad153,\quad160,
\]
all composite.  Thus the Gaussian square-offset subfamily does not contain a
prime in every Legendre interval.

The route is still informative.  Up to \(100000\), the probe finds only \(33\)
failures of the strict square-offset lemma, all already below \(4000\) in the
current run.  This suggests replacing Lemma G by a weaker target:

1. prove that square offsets work outside a finite or structured exceptional
   set; then
2. handle that exceptional set by a second offset family or by the full
   residue-cover formulation.

The first failure analysis supports a bounded-correction variant.  For every
strict failure observed up to \(100000\), the first actual prime in the
Legendre interval has offset
\[
  m=t^2+r
\]
with
\[
  |r|\le5.
\]
The exact histogram over the \(33\) observed failures is
\[
  |r|=1:14,\quad |r|=2:10,\quad |r|=3:7,\quad |r|=4:1,\quad |r|=5:1.
\]
So the next experimental target is a bounded band around Gaussian square
offsets, rather than pure square offsets.
