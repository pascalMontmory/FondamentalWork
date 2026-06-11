# \(M_3^\ast\) Counterexample Certificate

This note rewrites failure of the corrected multiple-of-three target
\(M_3^\ast\) as an exact small-prime certificate.

No numerical evidence is used here.  The only input is the elementary fact
that if
\[
  n^2<N<(n+1)^2
\]
and \(N\) is composite, then \(N\) has a prime divisor \(\le n\).

Throughout,
\[
  n=3m.
\]
The four-offset values are
\[
  n^2+t^2+r=9m^2+t^2+r,
  \qquad r\in\{-1,0,1,2\},
\]
with
\[
  1\le t^2+r\le 6m.
\]

## 1. Small-prime certificate principle

Let
\[
  N=9m^2+t^2+r
\]
with
\[
  1\le t^2+r\le6m.
\]
Then
\[
  9m^2<N\le9m^2+6m<(3m+1)^2.
\]
If \(N\) is composite, then it has a prime divisor
\[
  p\le3m.
\]

Therefore a failure of \(M_3^\ast\) is not merely the assertion that many
numbers are composite.  It is equivalent to a finite covering by primes
\[
  p\le3m.
\]

Since all surviving channels have already passed the deterministic \(2\)- and
\(3\)-layers, every such certificate prime satisfies
\[
  p\ge5.
\]

## 2. Channel A0: primitive Gaussian certificate

The A0 domain is
\[
  \mathcal A_0(m)=
  \left\{
  t:
  \begin{array}{l}
  1\le t^2\le6m,\\
  3\nmid t,\\
  \gcd(3m,t)=1,\\
  t\not\equiv m\pmod2
  \end{array}
  \right\}.
\]
The candidate is
\[
  G_m(t)=9m^2+t^2.
\]

If \(G_m(t)\) is composite for every \(t\in\mathcal A_0(m)\), then for each
such \(t\) there exists a prime
\[
  p\le3m
\]
such that
\[
  t^2\equiv-9m^2\pmod p.
\]

Because \(\gcd(3m,t)=1\), no prime divisor \(p\) of \(3m\) can certify this
congruence.  Hence
\[
  p\nmid 3m.
\]
Dividing by \((3m)^2\) modulo \(p\) gives
\[
  \left(t(3m)^{-1}\right)^2\equiv-1\pmod p.
\]
Thus every A0 certificate prime satisfies
\[
  p\equiv1\pmod4.
\]

So A0 failure is exactly a Gaussian residue cover:
\[
  \mathcal A_0(m)
  \subseteq
  \bigcup_{\substack{p\le3m\\ p\equiv1\pmod4\\ p\nmid 3m}}
  \left\{t:t^2\equiv-9m^2\pmod p\right\}.
\]

This is the old primitive Gaussian obstruction, now localized to \(n=3m\).

## 3. Channel A1: unit-lift certificate

The A1 domain is
\[
  \mathcal A_1(m)=
  \left\{
  t:
  \begin{array}{l}
  1\le t^2+1\le6m,\\
  3\nmid t,\\
  t\equiv m\pmod2
  \end{array}
  \right\}.
\]
The candidate is
\[
  U_m(t)=9m^2+t^2+1.
\]

If A1 fails, then for every \(t\in\mathcal A_1(m)\) there is a prime
\[
  p\le3m
\]
such that
\[
  t^2\equiv-9m^2-1\pmod p.
\]

This is the new unit-lift cover:
\[
  \mathcal A_1(m)
  \subseteq
  \bigcup_{\substack{p\le3m\\ p\ge5}}
  \left\{t:t^2\equiv-9m^2-1\pmod p\right\}.
\]

It is not Gaussian.  In particular, there is no forced condition
\(p\equiv1\pmod4\) in general.

However, primes dividing \(m\) can only certify A1 in the Gaussian way.  If
\[
  p\mid m,
\]
then the A1 congruence becomes
\[
  t^2\equiv-1\pmod p,
\]
so any such certificate prime must satisfy
\[
  p\equiv1\pmod4.
\]
Thus primes
\[
  p\mid m,\qquad p\equiv3\pmod4
\]
are invisible to the A1 unit-lift cover.

This is the first structural difference between A0 and A1: A1 removes the
gcd obstruction, but primes already dividing \(m\) still obey a quadratic
restriction.

## 4. Channel B: nonprimitive repair certificate

Now write
\[
  t=3u.
\]
Let
\[
  B=m^2+u^2.
\]
The candidate values are
\[
  9B-1,\qquad 9B+1,\qquad 9B+2,
\]
with parity deciding which ones can be prime.

### B-even parity branch

If
\[
  m\equiv u\pmod2,
\]
then \(B\) is even and the only possible prime candidates are
\[
  9(m^2+u^2)-1,\qquad
  9(m^2+u^2)+1.
\]
The admissibility conditions are
\[
  9u^2-1\le6m,
  \qquad
  9u^2+1\le6m.
\]

Failure of this branch means: for every admissible \(u\) with
\(m\equiv u\pmod2\), both available candidates are composite.  Hence there
exist primes \(p_-(u),p_+(u)\le3m\) such that
\[
  9(m^2+u^2)-1\equiv0\pmod{p_-(u)}
\]
and, when \(9u^2+1\le6m\),
\[
  9(m^2+u^2)+1\equiv0\pmod{p_+(u)}.
\]
Equivalently,
\[
  (3u)^2\equiv1-9m^2\pmod{p_-(u)},
\]
and
\[
  (3u)^2\equiv-1-9m^2\pmod{p_+(u)}.
\]

### B-odd parity branch

If
\[
  m\not\equiv u\pmod2,
\]
then \(B\) is odd and the only possible prime candidate is
\[
  9(m^2+u^2)+2.
\]
For every admissible \(u\) with
\[
  9u^2+2\le6m,
\]
failure gives a prime \(p_2(u)\le3m\) such that
\[
  9(m^2+u^2)+2\equiv0\pmod{p_2(u)}.
\]
Equivalently,
\[
  (3u)^2\equiv-2-9m^2\pmod{p_2(u)}.
\]

Thus B failure is a residue cover of the short \(u\)-interval by three
quadratic families:
\[
  (3u)^2\equiv1-9m^2,\quad
  (3u)^2\equiv-1-9m^2,\quad
  (3u)^2\equiv-2-9m^2.
\]

## 5. Exact certificate for failure of \(M_3^\ast\)

A number \(m\) is a counterexample to \(M_3^\ast\) if and only if all three
of the following covers hold simultaneously.

### A0 cover

\[
  \mathcal A_0(m)
  \subseteq
  \bigcup_{\substack{p\le3m\\ p\equiv1\pmod4\\ p\nmid3m}}
  \left\{t:t^2\equiv-9m^2\pmod p\right\}.
\]

### A1 cover

\[
  \mathcal A_1(m)
  \subseteq
  \bigcup_{\substack{p\le3m\\ p\ge5}}
  \left\{t:t^2\equiv-9m^2-1\pmod p\right\}.
\]

### B cover

The parity-split \(u\)-domain is covered by the three families
\[
  (3u)^2\equiv1-9m^2,
  \qquad
  (3u)^2\equiv-1-9m^2,
  \qquad
  (3u)^2\equiv-2-9m^2,
\]
with the admissibility inequalities attached to the corresponding offsets.

This is the exact obstruction.  Proving \(M_3^\ast\) is equivalent to proving
that no \(m\ge1\) admits this simultaneous A0/A1/B small-prime cover.

## 6. Next non-computational target

The most promising proof target is the interaction between A0 and A1 on the
same \(3\nmid t\) line.

For \(3\nmid t\), the offsets \(r=-1\) and \(r=2\) are killed by \(3\), and
exactly one of the two remaining offsets has the correct parity:

- if \(t\not\equiv m\pmod2\), the candidate is
  \[
    9m^2+t^2;
  \]
- if \(t\equiv m\pmod2\), the candidate is
  \[
    9m^2+t^2+1.
  \]

So the \(3\nmid t\) channel is a single parity-twisted quadratic family:
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

The next exact lemma should therefore not separate A0 and A1.  It should
attack the combined cover:
\[
  3\nmid t,\qquad
  1\le t^2+\epsilon_m(t)\le6m,\qquad
  P_m(t)\ \text{composite}.
\]

If this combined A-cover cannot hold for all such \(t\), the rare
nonprimitive B channel is unnecessary.  If it can hold, the B channel is the
exact repair mechanism to study next.
