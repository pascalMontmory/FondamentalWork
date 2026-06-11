# Refined Multiple-of-Three Channels

This note replaces the first \(M_3\) candidate by an exact channel
classification.

The previous \(M_3\) candidate kept the primitive Gaussian channel for
\(3\nmid t\) and the nonprimitive \(t=3u\) repair channel.  That is too narrow:
it misses the exact \(r=1\) lift inside \(3\nmid t\).

Throughout, write
\[
  n=3m
\]
and consider the four candidates
\[
  n^2+t^2+r,\qquad r\in\{-1,0,1,2\},
\]
with
\[
  1\le t^2+r\le 2n=6m.
\]

## 1. Exact split when \(3\nmid t\)

Assume
\[
  3\nmid t.
\]
Then
\[
  t^2\equiv1\pmod3,
  \qquad
  n^2=(3m)^2\equiv0\pmod3.
\]
Therefore
\[
  n^2+t^2+r\equiv1+r\pmod3.
\]
For the four offsets:
\[
\begin{array}{c|c}
  r & n^2+t^2+r \pmod3 \\
  \hline
  -1 & 0 \\
  0 & 1 \\
  1 & 2 \\
  2 & 0.
\end{array}
\]
Since \(n\ge3\), the offsets \(r=-1\) and \(r=2\) give numbers larger than
\(3\) and divisible by \(3\).  They are automatically composite.

Thus the entire \(3\nmid t\) channel has only two possible prime subchannels:
\[
  r=0,\qquad r=1.
\]

### 1.1 The \(r=0\) subchannel

The candidate is
\[
  n^2+t^2=9m^2+t^2.
\]
If this number is prime, then necessarily:

- \(n\) and \(t\) have opposite parity, because otherwise \(n^2+t^2\) is even
  and larger than \(2\);
- \(\gcd(n,t)=1\), because if \(d=\gcd(n,t)>1\), then
  \[
    d^2\mid n^2+t^2
  \]
  and \(n^2+t^2>d^2\).

So the \(r=0\) part is exactly the primitive opposite-parity Gaussian channel:
\[
  \gcd(3m,t)=1,\qquad 3m+t\equiv1\pmod2,\qquad
  9m^2+t^2\ \text{prime}.
\]

### 1.2 The missing \(r=1\) subchannel

The candidate is
\[
  n^2+t^2+1=9m^2+t^2+1.
\]
If \(n\) and \(t\) have opposite parity, then \(n^2+t^2\) is odd, so
\[
  n^2+t^2+1
\]
is even and larger than \(2\).  It is composite.

Therefore a prime in this subchannel requires
\[
  n\equiv t\pmod2.
\]
Since \(n=3m\), this is the same as
\[
  t\equiv m\pmod2.
\]

This is the channel missing from the first \(M_3\) candidate:
\[
  3\nmid t,\qquad t\equiv m\pmod2,\qquad
  9m^2+t^2+1\ \text{prime}.
\]
Unlike \(r=0\), there is no primitive gcd requirement forced by divisibility,
because the \(+1\) destroys the common divisor obstruction.

## 2. Exact split when \(t=3u\)

Assume
\[
  t=3u.
\]
Then
\[
  n^2+t^2=9(m^2+u^2).
\]
Let
\[
  B=m^2+u^2.
\]
The four candidates are
\[
  9B-1,\qquad 9B,\qquad 9B+1,\qquad 9B+2.
\]
The middle candidate \(9B\) is always composite.

Parity gives the remaining exact split:

- if \(B\) is even, then \(9B\) and \(9B+2\) are even, so the only possible
  prime candidates are
  \[
    9B-1,\qquad 9B+1;
  \]
- if \(B\) is odd, then \(9B-1\) and \(9B+1\) are even, so the only possible
  prime candidate is
  \[
    9B+2.
  \]

Since
\[
  B=m^2+u^2\equiv m+u\pmod2,
\]
this is exactly:
\[
\begin{array}{c|c}
  m\equiv u\pmod2 & 9(m^2+u^2)-1\ \text{or}\ 9(m^2+u^2)+1 \\
  m\not\equiv u\pmod2 & 9(m^2+u^2)+2.
\end{array}
\]

The admissibility conditions are:
\[
\begin{array}{c|c}
  \text{candidate} & \text{condition} \\
  \hline
  9(m^2+u^2)-1 & 9u^2-1\le6m \\
  9(m^2+u^2)+1 & 9u^2+1\le6m \\
  9(m^2+u^2)+2 & 9u^2+2\le6m.
\end{array}
\]

## 3. Why the first \(M_3\) candidate is false

The first \(M_3\) candidate omitted the \(3\nmid t,\ r=1\) unit-lift channel.
It is therefore false.

Take
\[
  m=4,\qquad n=12.
\]
The primitive \(3\nmid t,\ r=0\) channel has only
\[
  t=1
\]
inside the admissible primitive opposite-parity range, and
\[
  12^2+1^2=145=5\cdot29.
\]
The \(t=3u\) channel has \(u=1\) available in the opposite-parity case, giving
\[
  9(4^2+1^2)+2=155=5\cdot31.
\]
So the first \(M_3\) candidate fails at \(m=4\).

But the full four-offset family is repaired by the missing unit-lift channel:
\[
  t=2,\qquad r=1,
\]
because
\[
  12^2+2^2+1=149,
\]
which is prime.

Thus the correct lesson is not that the \(3\mid n\) route fails.  The correct
lesson is that \(3\nmid t\) has two exact prime subchannels:
\[
  r=0\quad\text{and}\quad r=1.
\]

## 4. Corrected \(M_3^\ast\) target

The corrected multiple-of-three target is:

For every \(m\ge1\), at least one of the following holds.

### A0. Primitive Gaussian channel

There exists \(t\) such that
\[
  1\le t^2\le6m,\qquad
  3\nmid t,\qquad
  \gcd(3m,t)=1,\qquad
  3m+t\equiv1\pmod2,
\]
and
\[
  9m^2+t^2
\]
is prime.

### A1. Nonmultiple unit-lift channel

There exists \(t\) such that
\[
  1\le t^2+1\le6m,\qquad
  3\nmid t,\qquad
  t\equiv m\pmod2,
\]
and
\[
  9m^2+t^2+1
\]
is prime.

### B. Multiple-of-three repair channel

There exists \(u\ge1\) satisfying the corresponding admissibility condition
such that:

- if \(m\equiv u\pmod2\), at least one of
  \[
    9(m^2+u^2)-1,\qquad 9(m^2+u^2)+1
  \]
  is prime;
- if \(m\not\equiv u\pmod2\),
  \[
    9(m^2+u^2)+2
  \]
  is prime.

This \(M_3^\ast\) statement is the exact corrected object for the
multiple-of-three channel.
