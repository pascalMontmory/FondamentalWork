# Combined A-Cover Rigidity

This note studies the combined \(3\nmid t\) channel from the
\(M_3^\ast\) certificate.

The goal is to avoid treating the Gaussian channel \(A0\) and the unit-lift
channel \(A1\) as unrelated covers.  On the line \(3\nmid t\), they form one
parity-twisted quadratic family.

Throughout,
\[
  n=3m.
\]

## 1. The combined A-family

For \(3\nmid t\), the offsets \(r=-1\) and \(r=2\) are divisible by \(3\).
The only surviving offsets are
\[
  r=0,\qquad r=1.
\]
Parity selects exactly one of them:
\[
  \epsilon_m(t)=
  \begin{cases}
  0,&t\not\equiv m\pmod2,\\
  1,&t\equiv m\pmod2.
  \end{cases}
\]
Define
\[
  P_m(t)=9m^2+t^2+\epsilon_m(t).
\]

The combined A-domain is
\[
  \mathcal A(m)=
  \left\{
  t:
  3\nmid t,\quad
  1\le t^2+\epsilon_m(t)\le6m,\quad
  \epsilon_m(t)=1\ \text{or}\ \gcd(3m,t)=1
  \right\}.
\]
The final condition records that the \(r=0\) branch is still the primitive
Gaussian branch.  The \(r=1\) unit-lift branch has no such gcd restriction.

Failure of the combined A-channel means:
\[
  P_m(t)\ \text{is composite for every }t\in\mathcal A(m).
\]
By the small-prime certificate principle, this is equivalent to a cover of
\(\mathcal A(m)\) by primes \(p\le3m\) satisfying
\[
  P_m(t)\equiv0\pmod p.
\]

## 2. Local classes modulo \(6p\)

Let
\[
  p\ge5.
\]
The conditions \(3\nmid t\), parity, and one quadratic congruence naturally
live modulo
\[
  6p.
\]

### A0 classes

For the Gaussian side \(A0\),
\[
  t\not\equiv m\pmod2,
  \qquad
  t^2\equiv-9m^2\pmod p.
\]
If \(p\mid 3m\), this congruence would force \(p\mid t\), which is excluded
by the primitive condition \(\gcd(3m,t)=1\).  Hence A0 has no classes for
primes dividing \(3m\).

If \(p\nmid3m\), then A0 classes exist exactly when
\[
  -1
\]
is a quadratic residue modulo \(p\), i.e.
\[
  p\equiv1\pmod4.
\]
In that case there are two roots modulo \(p\).  Each root has one prescribed
parity and two allowed nonzero classes modulo \(3\), so A0 contributes at
most four residue classes modulo \(6p\).

### A1 classes

For the unit-lift side \(A1\),
\[
  t\equiv m\pmod2,
  \qquad
  t^2\equiv-9m^2-1\pmod p.
\]
The number of roots modulo \(p\) is
\[
  1+\left(\frac{-9m^2-1}{p}\right),
\]
with the convention that it is \(1\) when
\[
  p\mid 9m^2+1.
\]
Each root again has one prescribed parity and two allowed nonzero classes
modulo \(3\).  Thus A1 contributes at most four residue classes modulo
\(6p\).

If \(p\mid m\), the A1 congruence becomes
\[
  t^2\equiv-1\pmod p.
\]
Therefore primes
\[
  p\mid m,\qquad p\equiv3\pmod4
\]
are invisible to the entire combined A-cover: they cover neither A0 nor A1.

## 3. Block structure of \(3\nmid t\)

The allowed integers \(t\) with \(3\nmid t\) occur in adjacent pairs
\[
  a=3q+1,\qquad b=3q+2=a+1.
\]
Call
\[
  B_q=\{3q+1,3q+2\}
\]
a complete A-block when both elements are admissible:
\[
  3q+1,3q+2\in\mathcal A(m).
\]

The two elements of a complete A-block have opposite parity.  Consequently,
one member lies on A0 and the other lies on A1.  Completeness includes the
primitive condition on the A0 member.

Thus a combined A-cover must cover both members of every complete A-block.
This creates a two-point rigidity not visible when A0 and A1 are separated.

## 4. Adjacent-pair collision lemma

Let
\[
  a=3q+1,\qquad b=a+1=3q+2
\]
be a complete A-block.

Suppose an odd prime \(p\) divides both
\[
  P_m(a)
  \qquad\text{and}\qquad
  P_m(b).
\]
Then
\[
  p\mid 9m^2+1.
\]
Moreover:

- if \(a\equiv m\pmod2\), then
  \[
    p\mid a;
  \]
- if \(a\not\equiv m\pmod2\), then
  \[
    p\mid b.
  \]

Proof.

There are two parity cases.

If \(a\equiv m\pmod2\), then \(a\) is on A1 and \(b\) is on A0:
\[
  P_m(a)=9m^2+a^2+1,
  \qquad
  P_m(b)=9m^2+b^2.
\]
Subtracting gives
\[
  P_m(b)-P_m(a)=b^2-a^2-1=(2a+1)-1=2a.
\]
Since \(p\) is odd and divides both values, it follows that
\[
  p\mid a.
\]
Substituting \(a\equiv0\pmod p\) into \(P_m(a)\equiv0\pmod p\) gives
\[
  9m^2+1\equiv0\pmod p.
\]

If \(a\not\equiv m\pmod2\), then \(a\) is on A0 and \(b\) is on A1:
\[
  P_m(a)=9m^2+a^2,
  \qquad
  P_m(b)=9m^2+b^2+1.
\]
Subtracting gives
\[
  P_m(b)-P_m(a)=b^2-a^2+1=(2a+1)+1=2b.
\]
Thus
\[
  p\mid b.
\]
Substituting \(b\equiv0\pmod p\) into \(P_m(b)\equiv0\pmod p\) gives again
\[
  9m^2+1\equiv0\pmod p.
\]
This proves the lemma.

## 5. Bridge primes

Call a prime
\[
  p\le3m
\]
a bridge prime for \(m\) if
\[
  p\mid 9m^2+1.
\]
Every bridge prime satisfies
\[
  p\equiv1\pmod4,
\]
because
\[
  (3m)^2\equiv-1\pmod p.
\]

The adjacent-pair collision lemma says:

> A single odd prime can certify both members of a complete A-block only if it
> is a bridge prime.

Even then, it can bridge only blocks satisfying the extra linear condition
\[
\begin{array}{c|c}
  \text{parity of }a=3q+1 & \text{required bridge congruence} \\
  \hline
  a\equiv m\pmod2 & 3q+1\equiv0\pmod p \\
  a\not\equiv m\pmod2 & 3q+2\equiv0\pmod p.
\end{array}
\]

Thus bridge behavior is not generic.  It is confined to explicit arithmetic
progressions attached to prime divisors of \(9m^2+1\).

## 6. Exact obstruction for an A-cover

If the combined A-channel fails for a given \(m\), then every complete
A-block \(B_q=\{3q+1,3q+2\}\) must satisfy one of the following:

1. its two elements are certified by two distinct primes \(p_1,p_2\le3m\);
2. its two elements are certified by one bridge prime
   \[
     p\mid9m^2+1
   \]
   and the corresponding linear bridge congruence above holds.

This is a sharper obstruction than the previous A0/A1 separate covers.  It
forces a counterexample to provide either two independent small-prime
certificates per complete A-block, or an explicit bridge prime divisor of
\[
  9m^2+1.
\]

## 7. Next exact target

The next proof target is now:

Show that for every \(m\ge1\), some complete A-block fails to admit this
two-certificate-or-bridge alternative.

Equivalently, prove that the set of complete A-blocks cannot be covered by
the residue classes coming from:

- independent A0 and A1 roots modulo primes \(p\le3m\);
- bridge progressions coming from primes \(p\mid9m^2+1\).

This is a finite, exact covering obstruction.  It is stronger than the
original combined A-cover and does not use numerical extrapolation.
