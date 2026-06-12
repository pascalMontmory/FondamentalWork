# The \(u=1\) Repair Cluster Gate

This note isolates the first exact coupling between a full coprime A-block
cover and the nonprimitive \(t=3u\) channel.

It is not a proof of Legendre.  It is a proof-level reduction: a full A-block
cover which is not repaired by \(u=1\) must satisfy a rigid cluster of
centered divisor equations at the fixed anchor \(q=0\).

Throughout,
\[
  n=3m,\qquad A=3m.
\]

## 1. The \(u=1\) channel

In the nonprimitive channel \(t=3u\), put \(u=1\).  Then
\[
  n^2+t^2+r=A^2+9+r.
\]

For \(m\ge2\), the admissibility inequalities
\[
  9u^2+r\le6m
\]
are automatic for the relevant \(u=1\) offsets.

If \(m\) is odd, then \(m\equiv u\pmod2\), so the two possible prime
candidates are
\[
  A^2+8,\qquad A^2+10.
\]

If \(m\) is even, then \(m\not\equiv u\pmod2\), so the only possible prime
candidate is
\[
  A^2+11.
\]

Each of these numbers lies strictly between \(A^2\) and \((A+1)^2\), because
\[
  8,10,11<2A+1
\]
for \(m\ge2\).  Therefore, if such a candidate is composite, it has a prime
divisor
\[
  p\le A.
\]

## 2. Coupling with the anchor block

The block \(q=0\) is always complete and coprime.  Hence any full A-block
cover must cover the anchor in both layers.

If \(m\) is odd, the anchor forces the two composites
\[
  A^2+4,\qquad A^2+2.
\]
If \(u=1\) does not repair the interval, it also forces the two composites
\[
  A^2+8,\qquad A^2+10.
\]
Thus a full A-block cover with no \(u=1\) repair forces the four-point
cluster
\[
  A^2+2,\quad A^2+4,\quad A^2+8,\quad A^2+10
\]
to be composite, each with a prime divisor at most \(A\).

If \(m\) is even, the anchor forces
\[
  A^2+1,\qquad A^2+5,
\]
and failure of \(u=1\) forces
\[
  A^2+11.
\]
Thus the even branch forces the three-point cluster
\[
  A^2+1,\quad A^2+5,\quad A^2+11.
\]

## 3. Coprimality inside the forced clusters

For any two offsets \(c\ne d\),
\[
  \gcd(A^2+c,A^2+d)\mid |c-d|.
\]

### Odd \(m\)

Here \(A\) is odd, so all four values
\[
  A^2+2,\ A^2+4,\ A^2+8,\ A^2+10
\]
are odd.  None is divisible by \(3\), since the offsets are congruent to
\(1\) or \(2\pmod3\).  The possible offset differences are
\[
  2,\ 4,\ 6,\ 8.
\]
Consequently all four values are pairwise coprime.

Therefore the odd no-\(u=1\)-repair branch forces four distinct primes
\[
  p_c\le A,\qquad c\in\{2,4,8,10\},
\]
such that
\[
  p_c\mid A^2+c.
\]

The anchor labels are not arbitrary:
\[
  p_4\equiv1\pmod4,
\]
and \(p_2\) is an A1 label, so \(p_2\ge5\) and \(p_2\ne p_4\).  The new
\(u=1\) labels \(p_8,p_{10}\) are only forced by compositeness, but they
still satisfy
\[
  A^2\equiv -8\pmod {p_8},\qquad
  A^2\equiv -10\pmod {p_{10}}.
\]

### Even \(m\)

Here \(A\) is even, so
\[
  A^2+1,\quad A^2+5,\quad A^2+11
\]
are odd.  The pairs \((1,5)\) and \((5,11)\) are coprime, because their
differences are \(4\) and \(6\), and no value is divisible by \(2\) or \(3\).

The only possible shared prime between \(A^2+1\) and \(A^2+11\) is \(5\):
\[
  \gcd(A^2+1,A^2+11)\mid10.
\]
Thus either the even branch forces three distinct prime labels, or it lies
in the explicit exceptional congruence
\[
  A^2\equiv -1\pmod5.
\]

Equivalently,
\[
  A\equiv\pm2\pmod5.
\]

## 4. Centered divisor form

Every forced composite \(A^2+c\) can be written with a prime label
\[
  p_c=A-r_c,\qquad 0\le r_c<A,
\]
and a positive integer quotient \(e_c\) defined by
\[
  A-r_c\mid r_c^2+c,\qquad
  e_c=\frac{r_c^2+c}{A-r_c}.
\]

Equivalently,
\[
  A
  =
  r_c+\frac{r_c^2+c}{e_c}.
\]

For two offsets \(c,d\), sharing the same center \(A\) gives the exact
compatibility equation
\[
  e_c e_d(r_c-r_d)
  +e_d(r_c^2+c)
  -e_c(r_d^2+d)
  =
  0.
\]

Hence the odd branch reduces to simultaneous solutions of this equation for
\[
  c,d\in\{2,4,8,10\},
\]
with four distinct labels \(A-r_c\).  The even branch reduces to
\[
  c,d\in\{1,5,11\},
\]
with the single exceptional shared-label gate \(A\equiv\pm2\pmod5\).

## 5. Exact closure target

The next theorem to prove is:

> A full coprime A-block cover cannot coexist with failure of the \(u=1\)
> repair cluster, except possibly in the explicit even shared-\(5\) gate;
> and that gate either descends or is repaired by another nonprimitive
> offset.

In contrapositive form:

> If the A-block gate is fully covered and no descent occurs, then one of
> the \(u=1\) candidates is prime.

This is strictly sharper than the previous target "full cover implies some
nonprimitive repair", because the first repair layer has been isolated as
the finite cluster
\[
  \{2,4,8,10\}
  \quad\text{or}\quad
  \{1,5,11\}.
\]

The calibration case
\[
  m=391,\qquad A=1173
\]
does not enter the forced odd cluster, because
\[
  A^2+8=1173^2+8
\]
is prime.  Thus it escapes exactly through the \(u=1,r=-1\) repair predicted
by this gate.
