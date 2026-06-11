# Legendre via Finite-Field Circle Covers

This note is the non-computational reformulation of the Gaussian-band
experiments.  The aim is not to extrapolate from data, but to isolate an exact
obstruction whose impossibility would imply Legendre.

## 1. The Four-Offset Target

The experiments suggest the following strengthening of Legendre.

Conjectural Lemma \(G_2^\ast\).  For every \(n\ge2\), there exist integers
\[
  t\ge1,\qquad r\in\{-1,0,1,2\},
\]
such that
\[
  1\le t^2+r\le2n
\]
and
\[
  n^2+t^2+r
\]
is prime.

This immediately implies Legendre, since
\[
  n^2<n^2+t^2+r\le n^2+2n<(n+1)^2.
\]

The strict Gaussian case is \(r=0\).  The corrected family is
\[
  t^2-1,\quad t^2,\quad t^2+1,\quad t^2+2.
\]
The point of this note is to rewrite the failure of this four-offset lemma as
a rigid finite-field circle-covering problem.

## 2. Exact Composite Criterion

Let
\[
  M_{t,r}=n^2+t^2+r.
\]
If \(M_{t,r}\) is composite and \(1\le t^2+r\le2n\), then
\[
  M_{t,r}<(n+1)^2,
\]
so \(M_{t,r}\) has a prime divisor
\[
  p\le n.
\]
Thus \(M_{t,r}\) is prime if and only if no prime \(p\le n\) divides it.

Therefore a counterexample to \(G_2^\ast\) is exactly a covering statement:
for every admissible pair \((t,r)\), there exists a prime \(p\le n\) such that
\[
  n^2+t^2+r\equiv0\pmod p.
\]

Equivalently,
\[
  n^2+t^2\equiv -r\pmod p,
\]
where
\[
  -r\in\{1,0,-1,-2\}.
\]

So the obstruction is not an arbitrary residue cover.  It is a cover of a
short vertical segment by four finite-field circles:
\[
  X^2+Y^2=c,\qquad c\in\{1,0,-1,-2\}.
\]

For a fixed integer \(n\), each prime \(p\le n\) sees the vertical line
\[
  X\equiv n\pmod p.
\]
The bad \(t\)-values modulo \(p\) are exactly the solutions of
\[
  Y^2\equiv c-n^2\pmod p,\qquad c\in\{1,0,-1,-2\}.
\]

Thus each odd prime \(p\) forbids at most eight residue classes of \(t\)
modulo \(p\), but these residue classes are tied together by the four
consecutive circle radii \(1,0,-1,-2\).

## 3. Rigidity at a Fixed \(t\)

Fix \(n,t\), and set
\[
  A=n^2+t^2.
\]
The four candidates are
\[
  A-1,\quad A,\quad A+1,\quad A+2.
\]

For any odd prime \(p\), the congruence
\[
  p\mid A+r
\]
can hold for at most one value of
\[
  r\in\{-1,0,1,2\}.
\]
Indeed, if \(p\mid A+r_1\) and \(p\mid A+r_2\), then
\[
  p\mid r_1-r_2,
\]
but
\[
  |r_1-r_2|\le3.
\]
Thus only \(p=3\) can collide between \(r=-1\) and \(r=2\), and otherwise an
odd prime covers only one of the four offsets.

The prime \(2\) is completely deterministic:
\[
  A+r\equiv0\pmod2
\]
covers exactly two of the four offsets.  Hence, after parity is removed, a
counterexample must assign distinct odd prime obstructions to the remaining
offsets for every \(t\).

This is the first rigidity principle: a counterexample is not merely a cover
of \(t\)-values.  For most \(t\), it must provide several independent small
prime certificates at once.

## 4. The Gaussian Channel

The offset \(r=0\) is special:
\[
  A=n^2+t^2=N(n+it).
\]
If \(\gcd(n,t)=1\), then no prime
\[
  p\equiv3\pmod4
\]
can divide \(A\).  Therefore the \(r=0\) circle can only be covered by primes
\[
  p\equiv1\pmod4
\]
or by primes dividing \(\gcd(n,t)\).

This creates an asymmetry among the four offsets.  The corrected offsets
\[
  r=-1,\quad r=1,\quad r=2
\]
must compensate exactly where the Gaussian norm channel is blocked.

The experiments found that the compensation set is tiny:
\[
  r=-1,\quad r=1,\quad r=2,
\]
with no observed need for \(r=-2\).  The exact question is therefore:

Can the finite-field circles
\[
  X^2+Y^2=1,\quad X^2+Y^2=0,\quad X^2+Y^2=-1,\quad X^2+Y^2=-2
\]
cover every admissible \(Y=t\) on a vertical segment without leaving a prime
candidate?

## 5. Minimal-Counterexample Obstruction

Assume \(n\) is the least counterexample to \(G_2^\ast\).

For every \(t\) with at least one admissible offset, define a certificate
\[
  \pi_t:\{-1,0,1,2\}\supseteq R_t\to\{p:p\le n\}
\]
such that
\[
  \pi_t(r)\mid n^2+t^2+r.
\]
Here
\[
  R_t=\{r\in\{-1,0,1,2\}:1\le t^2+r\le2n\}.
\]

The certificate must satisfy:

1. For odd \(p\ne3\), one prime cannot certify two different \(r\)'s at the
   same \(t\).
2. The \(r=0\) certificate is either \(p\equiv1\pmod4\) or \(p\mid\gcd(n,t)\).
3. If \(p\mid n\), then
   \[
     t^2+r\equiv0\pmod p,
   \]
   so primes dividing \(n\) cover \(t\)-values independently of \(n\)'s
   residue class.
4. If \(p\nmid n\), after scaling by \(n^{-1}\), the obstruction is
   \[
     (tn^{-1})^2\equiv -1-rn^{-2}\pmod p.
   \]
   Thus all non-divisor primes cover values of \(t/n\) by square-root
   constraints.

This certificate language is exact.  A proof of \(G_2^\ast\) is equivalent to
proving that such certificates cannot exist for any \(n\ge2\).

## 6. Proposed Exact Attack

The attack should not try to estimate primes in short intervals directly.
Instead, it should prove that the above certificate system cannot cover the
short segment
\[
  1\le t\le\lfloor\sqrt{2n}\rfloor+1.
\]

The first target lemma is a local-to-global obstruction.

Lemma C candidate.  Let \(n\ge2\).  Suppose every admissible
\[
  n^2+t^2+r,\qquad r\in\{-1,0,1,2\},
\]
is composite.  Then there exists a prime \(p\le n\) and a block of consecutive
\(t\)-values on which the four-circle cover forces two incompatible square
classes modulo \(p\).

This is deliberately not a standard prime-gap lemma.  It is a finite-field
incidence statement about four neighboring conics.

The second target lemma is a divisor-channel separation.

Lemma D candidate.  The primes dividing \(n\) cannot cover enough of the
admissible \(t\)-segment to compensate for the restriction that the Gaussian
channel \(r=0\) only accepts primes \(1\pmod4\) on primitive \(t\)'s.

Together, Lemma C and Lemma D would prove \(G_2^\ast\), hence Legendre.

## 7. Immediate Next Work

The next step is to derive exact formulas for the residue sets
\[
  B_p(n)=
  \bigcup_{r\in\{-1,0,1,2\}}
  \{t\bmod p:t^2\equiv -n^2-r\pmod p\}
\]
and study their overlaps as \(p\) varies.

The critical object is not the size of \(B_p(n)\), but the forced
four-offset certification at the same \(t\).  The computational scripts should
therefore be used only to guess exact overlap lemmas, not as evidence for the
conjecture.
