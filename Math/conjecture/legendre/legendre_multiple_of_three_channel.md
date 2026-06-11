# Multiple-of-Three Channel

This note isolates the remaining structural obstruction after the primitive
double-cover reduction.  The observed survivors are concentrated at
\[
  3\mid n.
\]
Write
\[
  n=3m.
\]
The four-offset family is
\[
  n^2+t^2+r,\qquad r\in\{-1,0,1,2\}.
\]

## 1. Split by \(t\bmod3\)

There are two channels.

### Channel A: \(3\nmid t\)

If \(3\nmid t\), then \(n\) and \(t\) are not both divisible by \(3\).  On the
primitive opposite-parity subchannel
\[
  \gcd(n,t)=1,\qquad n+t\equiv1\pmod2,
\]
the previous reduction applies with exactly one of \(n,t\) divisible by \(3\).
Thus
\[
  A=n^2+t^2
\]
satisfies
\[
  A\equiv1\pmod6,
\]
and the deterministic \(2,3\)-layer kills
\[
  A-1,\quad A+1,\quad A+2.
\]
Only
\[
  A=n^2+t^2
\]
remains.

Therefore this channel is a pure Gaussian channel.  If \(A\) is composite and
\(\gcd(n,t)=1\), its prime certificates must be \(1\pmod4\).

### Channel B: \(3\mid t\)

Write
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
The four candidates become
\[
  9B-1,\quad 9B,\quad 9B+1,\quad 9B+2.
\]
The middle candidate \(9B\) is automatically composite whenever it is
admissible.  Thus the nonprimitive channel is not Gaussian anymore; it is a
three-offset problem around a multiple of \(9\):
\[
  9B-1,\quad 9B+1,\quad 9B+2.
\]

## 2. Parity Collapse in the Nonprimitive Channel

Since \(9B\) has the same parity as \(B\), the parity layer gives:

- if \(B\) is even, then \(9B\) and \(9B+2\) are even, while
  \(9B-1\) and \(9B+1\) are odd;
- if \(B\) is odd, then \(9B-1\) and \(9B+1\) are even, while
  \(9B\) and \(9B+2\) are odd.

Because \(9B\) is already composite, the surviving prime conditions are:

\[
\begin{array}{c|c|c}
  B=m^2+u^2 \bmod2 & \text{surviving candidates} & \text{prime condition} \\
  \hline
  0 & 9B-1,\ 9B+1 & 9B-1\text{ prime or }9B+1\text{ prime} \\
  1 & 9B+2 & 9B+2\text{ prime}.
\end{array}
\]

Equivalently, since squares modulo \(2\) are themselves,
\[
  B\equiv m+u\pmod2.
\]
So:

- if \(m,u\) have the same parity, one needs a prime in
  \[
    9(m^2+u^2)-1,\qquad 9(m^2+u^2)+1;
  \]
- if \(m,u\) have opposite parity, one needs
  \[
    9(m^2+u^2)+2
  \]
  to be prime.

This is an exact reduction of the nonprimitive \(3\mid t\) channel.

## 3. Admissibility Bounds

The original Legendre interval requires
\[
  1\le t^2+r\le 2n.
\]
With \(n=3m\) and \(t=3u\), this becomes
\[
  1\le 9u^2+r\le6m.
\]
Thus the three nontrivial nonprimitive candidates are available under:

\[
\begin{array}{c|c}
  \text{candidate} & \text{admissibility} \\
  \hline
  9B-1 & 9u^2-1\le6m \\
  9B+1 & 9u^2+1\le6m \\
  9B+2 & 9u^2+2\le6m.
\end{array}
\]

For \(u\ge1\), the lower bound is automatic for \(9u^2-1\).  The upper bounds
force
\[
  u\lesssim \sqrt{\frac{2m}{3}}.
\]

## 4. Exact Remaining Target for \(3\mid n\)

The multiple-of-three obstruction is now split into:

1. a primitive pure Gaussian channel for \(3\nmid t\);
2. a nonprimitive channel \(t=3u\) with candidates around
   \[
     9(m^2+u^2).
   \]

A counterexample with \(n=3m\) must make both channels fail:

- for every primitive opposite-parity \(t\) with \(3\nmid t\), the Gaussian
  norm \(9m^2+t^2\) must be composite;
- for every admissible \(u\), the relevant nonprimitive candidate(s)
  determined by the parity of \(m^2+u^2\) must be composite.

Thus the next proof target is no longer a generic residue-cover statement.
It is a mixed primitive/nonprimitive dichotomy:

\[
\boxed{
\begin{array}{ll}
3\nmid t: & 9m^2+t^2,\\[2mm]
t=3u,\ m\equiv u\pmod2: &
  9(m^2+u^2)-1\ \text{or}\ 9(m^2+u^2)+1,\\[2mm]
t=3u,\ m\not\equiv u\pmod2: &
  9(m^2+u^2)+2.
\end{array}}
\]

If one can prove that at least one of these channels always produces a prime
inside the admissible range, then the remaining \(3\mid n\) obstruction is
removed.

## 5. Next Lemma

Lemma \(M_3\) candidate.  For every \(m\ge1\), at least one of the following
holds:

1. there exists \(t\) with
   \[
     1\le t\le\lfloor\sqrt{6m}\rfloor,\quad
     3\nmid t,\quad \gcd(3m,t)=1,\quad 3m+t\equiv1\pmod2,
   \]
   such that
   \[
     9m^2+t^2
   \]
   is prime;
2. there exists \(u\ge1\) satisfying the relevant admissibility inequality
   above such that, if \(m\equiv u\pmod2\), at least one of
   \[
     9(m^2+u^2)-1,\qquad 9(m^2+u^2)+1
   \]
   is prime;
3. there exists \(u\ge1\) with \(m\not\equiv u\pmod2\) and
   \[
     9u^2+2\le6m
   \]
   such that
   \[
     9(m^2+u^2)+2
   \]
   is prime.

Lemma \(M_3\) would close the currently isolated multiple-of-three channel.
