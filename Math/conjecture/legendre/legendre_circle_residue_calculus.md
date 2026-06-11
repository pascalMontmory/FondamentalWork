# Local Residue Calculus for the Four-Circle Legendre Attack

This note derives exact local formulas for the bad residue set
\[
  B_p(n)=
  \bigcup_{r\in\{-1,0,1,2\}}
  \{t\bmod p:n^2+t^2+r\equiv0\pmod p\}.
\]
These formulas are the first rigid algebraic input for the finite-field
circle-cover attack.

Throughout this note, \(\chi_p\) denotes the quadratic character modulo an
odd prime \(p\), extended by \(\chi_p(0)=0\).

## 1. Disjointness for \(p>3\)

Fix an odd prime \(p>3\).  For a fixed residue \(t\bmod p\), the congruence
\[
  n^2+t^2+r\equiv0\pmod p
\]
can hold for at most one value
\[
  r\in\{-1,0,1,2\}.
\]
Indeed, if it holds for \(r_1\) and \(r_2\), then
\[
  r_1-r_2\equiv0\pmod p.
\]
But the nonzero differences among \(-1,0,1,2\) have absolute value at most
\(3\), impossible modulo \(p>3\).

Thus for \(p>3\), the four bad-root sets are disjoint.

## 2. Exact Size Formula

For \(p>3\), each equation
\[
  t^2\equiv -n^2-r\pmod p
\]
has exactly
\[
  1+\chi_p(-n^2-r)
\]
solutions in \(t\bmod p\).  Therefore
\[
  |B_p(n)|
  =
  4+\chi_p(1-n^2)+\chi_p(-n^2)+\chi_p(-1-n^2)+\chi_p(-2-n^2).
\]
Equivalently,
\[
  |B_p(n)|
  =
  4+\sum_{r\in\{-1,0,1,2\}}\chi_p(-n^2-r).
\]

This formula is exact, including the cases where one of the right-hand sides
vanishes, because \(\chi_p(0)=0\) and \(1+\chi_p(0)=1\).

## 3. Gaussian Bias

The \(r=0\) term is
\[
  \chi_p(-n^2).
\]
If \(p\nmid n\), then
\[
  \chi_p(-n^2)=\chi_p(-1).
\]
Hence:

- if \(p\equiv1\pmod4\), the Gaussian channel \(r=0\) contributes two bad
  roots;
- if \(p\equiv3\pmod4\), it contributes no bad roots;
- if \(p\mid n\), it contributes the single root \(t\equiv0\pmod p\).

This is the exact local form of the Gaussian-norm observation.

## 4. Average Size Over \(n\bmod p\)

For \(a\ne0\), the standard quadratic character identity gives
\[
  \sum_{x\bmod p}\chi_p(x^2-a)=-1.
\]
For \(a=0\),
\[
  \sum_{x\bmod p}\chi_p(x^2)=p-1.
\]

Applying this to
\[
  \chi_p(-n^2-r)=\chi_p(-1)\chi_p(n^2+r)
\]
gives, for \(p>3\),
\[
  \sum_{n\bmod p}|B_p(n)|
  =
  4p+\chi_p(-1)(p-4).
\]
Therefore
\[
  \mathbb E_{n\bmod p}|B_p(n)|
  =
  \begin{cases}
    5-\dfrac4p, & p\equiv1\pmod4,\\[6pt]
    3+\dfrac4p, & p\equiv3\pmod4.
  \end{cases}
\]

This is a structural asymmetry, not a heuristic.  Primes \(1\pmod4\) are
locally stronger coverers for the four-offset family than primes
\(3\pmod4\), because only \(p\equiv1\pmod4\) can cover the primitive Gaussian
offset \(r=0\).

## 5. Immediate Consequences

For \(p>3\), the local bad density is
\[
  \frac{|B_p(n)|}{p}.
\]
The exact average densities are
\[
  \frac5p-\frac4{p^2}
  \qquad(p\equiv1\pmod4),
\]
and
\[
  \frac3p+\frac4{p^2}
  \qquad(p\equiv3\pmod4).
\]

Thus a hypothetical counterexample cannot be modeled as arbitrary residue
classes of density \(8/p\).  The four neighboring circles impose:

1. disjointness among offsets for \(p>3\);
2. a \(1\bmod4\) bias in the Gaussian channel;
3. divisor-prime exceptional behavior only when \(p\mid n\);
4. a total local cover size controlled by four quadratic characters.

## 6. Next Exact Target

A counterexample to the four-offset lemma must cover the segment
\[
  1\le t\le\lfloor\sqrt{2n}\rfloor+1
\]
by sets \(B_p(n)\) with \(p\le n\).

The next exact question is not whether the union of their sizes is large
enough.  The next question is whether the four-offset certificate requirement
forces incompatible assignments at some \(t\):

for each admissible \(t\), every one of
\[
  n^2+t^2-1,\quad n^2+t^2,\quad n^2+t^2+1,\quad n^2+t^2+2
\]
must receive a prime divisor certificate, and for \(p>3\) those certificates
cannot be shared across offsets.

This pushes the problem from a one-layer residue cover to a multi-layer
certificate-cover problem.
