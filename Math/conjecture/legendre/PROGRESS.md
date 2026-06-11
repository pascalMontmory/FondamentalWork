# Legendre Progress Log

## Gaussian Lemma G probe

Added
\[
  \texttt{Math/conjecture/legendre/tools/gaussian\_lemma\_g\_probe.py}.
\]

The tested sufficient lemma was:
\[
  \exists\,1\le t\le\lfloor\sqrt{2n}\rfloor,\qquad \gcd(n,t)=1,
\]
with \(n,t\) of opposite parity, such that no prime
\[
  p\equiv1\pmod4,\qquad p\le n+1
\]
divides \(n^2+t^2\).

This lemma is false as a universal statement.  The first counterexample is
\[
  n=12.
\]
Here \(\lfloor\sqrt{24}\rfloor=4\), and the only primitive opposite-parity
candidate is \(t=1\).  But
\[
  12^2+1^2=145=5\cdot29.
\]
The other square offsets in the Legendre interval also fail:
\[
  12^2+2^2=148,\quad
  12^2+3^2=153,\quad
  12^2+4^2=160.
\]
Thus the square-offset Gaussian subfamily cannot by itself prove Legendre.

The probe nevertheless shows that the obstruction is sparse in the tested
range.  Up to \(100000\), it reports:

\[
\begin{array}{c|c}
  \text{range} & 2\le n\le100000 \\
  \hline
  \text{failures} & 33 \\
  \text{prime witnesses} & 99966/99999 \\
  \max t & 208 \\
  \max \left(t/\lfloor\sqrt{2n}\rfloor\right) & 1 \\
  \max \text{ candidates tried before witness} & 75.
\end{array}
\]

The failure list up to \(10000\) is:
\[
\begin{gathered}
12,23,30,39,48,60,63,83,105,113,114,141,152,174,186,196,\\
408,459,592,651,678,811,921,1173,1284,2046,2058,2163,\\
2181,2376,2658,2697,3954.
\end{gathered}
\]
Since the run up to \(100000\) also reports \(33\) failures, these are all
the failures observed in that range.

The next viable target is not Lemma G as stated.  It is either:

1. prove a finite-exception version of the square-offset lemma and handle the
   exceptional classes by another offset family; or
2. use the square-offset data as a structured subcover inside the full
   residue-cover formulation.

## Gaussian failure offset analysis

Added
\[
  \texttt{Math/conjecture/legendre/tools/gaussian\_failure\_analyzer.py}.
\]
For each failure of the strict square-offset lemma, it finds the first actual
prime in the Legendre interval and writes its offset as
\[
  m=t^2+r,
\]
choosing the nearest square.

For the \(33\) strict failures observed up to \(100000\), the first prime
offset is always very close to a square:
\[
\begin{array}{c|c}
  |r| & \text{number of failures} \\
  \hline
  1 & 14 \\
  2 & 10 \\
  3 & 7 \\
  4 & 1 \\
  5 & 1.
\end{array}
\]
Thus every observed strict failure is repaired by the broadened offset family
\[
  n^2+t^2+r,\qquad |r|\le5.
\]
The smaller band \(|r|\le4\) covers \(32/33\) failures; the unique \(|r|=5\)
case in this run is
\[
  n=1284,\qquad n^2+41=1648697,\qquad 41=6^2+5.
\]

This suggests the next experimental lemma:

Lemma \(G_5\) candidate. For every \(n\ge2\), there exist integers
\[
  1\le t\le\lfloor\sqrt{2n}\rfloor+1,\qquad |r|\le5,
\]
such that
\[
  1\le t^2+r\le 2n
\]
and \(n^2+t^2+r\) is prime.

This no longer has the clean Gaussian-norm divisor exclusion when \(r\ne0\),
but it may be the correct empirical bridge: square norms provide the main
skeleton, and a bounded correction handles the sparse failures.

## Gaussian bounded-band probe

Added
\[
  \texttt{Math/conjecture/legendre/tools/gaussian\_band\_probe.py}.
\]
For a fixed radius \(R\), it tests whether every interval has a prime of the
form
\[
  n^2+t^2+r,\qquad |r|\le R,\qquad 1\le t^2+r\le2n.
\]
The script uses deterministic Miller-Rabin for fast primality testing and
orders candidates by increasing \(|r|\), then by \(t\).

The initial \(G_5\) candidate was stronger than needed in the tested range.
For \(2\le n\le100000\), the probe found no failures with \(R=5\), and no
witness used \(|r|>2\):
\[
\begin{array}{c|c}
  r & \text{witness count} \\
  \hline
  -1 & 11 \\
  0 & 99966 \\
  1 & 21 \\
  2 & 1.
\end{array}
\]

Testing the smaller bands gives:
\[
\begin{array}{c|c|c}
  R & \text{range} & \text{failures} \\
  \hline
  1 & 2\le n\le1000000 & 1\quad(n=23) \\
  2 & 2\le n\le1000000 & 0.
\end{array}
\]
Thus the sharpened experimental target is now:

Lemma \(G_2\) candidate. For every \(n\ge2\), there exist integers \(t,r\)
with
\[
  |r|\le2,\qquad 1\le t^2+r\le2n,
\]
such that
\[
  n^2+t^2+r
\]
is prime.

Up to \(1000000\), the only non-square corrections needed are \(r=-1,1,2\),
and \(r=2\) occurs only for \(n=23\) in the tested range.

## Gaussian correction case analysis

Added
\[
  \texttt{Math/conjecture/legendre/tools/gaussian\_correction\_case\_analyzer.py}.
\]
It isolates the pure-square failures and compares two quantities:

1. the first actual prime in the Legendre interval;
2. the first prime found by the \(R=2\) correction-band search.

Up to \(1000000\), the pure-square failures are exactly the same \(33\) cases
already observed below \(10000\):
\[
\begin{gathered}
12,23,30,39,48,60,63,83,105,113,114,141,152,174,186,196,\\
408,459,592,651,678,811,921,1173,1284,2046,2058,2163,\\
2181,2376,2658,2697,3954.
\end{gathered}
\]
No new pure-square failure appears for
\[
  3955\le n\le1000000.
\]

Every one of the \(33\) failures is repaired by \(R=2\).  The actual repair
histogram is sharper than the symmetric band:
\[
\begin{array}{c|c}
  r & \text{repair count} \\
  \hline
  -1 & 11 \\
  1 & 21 \\
  2 & 1.
\end{array}
\]
Thus \(r=-2\) is not used in the tested range.  The current minimal empirical
candidate is therefore the four-family offset set
\[
  m\in\{t^2-1,\ t^2,\ t^2+1,\ t^2+2\},
\]
rather than the full symmetric band \(|r|\le2\).

The first-prime offsets themselves can be farther from the nearest square:
\[
\begin{array}{c|c}
  r_{\rm nearest} & \text{count} \\
  \hline
  -3 & 3 \\
  -2 & 10 \\
  -1 & 4 \\
  1 & 10 \\
  3 & 4 \\
  4 & 1 \\
  5 & 1.
\end{array}
\]
So the \(R=2\) family is not always capturing the first prime; it is capturing
a nearby prime later in the same interval.

## Exact circle-cover reformulation

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_exact\_circle\_cover\_attack.md}.
\]
This is the non-computational reformulation of the current route.

The four-offset target is:
\[
  n^2+t^2+r,\qquad r\in\{-1,0,1,2\}.
\]
If this family failed for some \(n\), then for every admissible \((t,r)\)
there would be a prime \(p\le n\) such that
\[
  n^2+t^2+r\equiv0\pmod p.
\]
Equivalently,
\[
  n^2+t^2\equiv c\pmod p,\qquad c\in\{1,0,-1,-2\}.
\]
Thus a counterexample is exactly a finite-field circle cover of a short
vertical segment by the four neighboring conics
\[
  X^2+Y^2=1,\quad X^2+Y^2=0,\quad X^2+Y^2=-1,\quad X^2+Y^2=-2.
\]

The key rigidity is that, for fixed \(t\), an odd prime \(p\ne3\) can certify
at most one of the four offsets.  The Gaussian offset \(r=0\) is even more
rigid: on primitive \(t\), it can only be certified by primes
\[
  p\equiv1\pmod4.
\]
This gives an exact target for proof: rule out the existence of such a
multi-offset certificate system, rather than estimating prime gaps directly.

## Local residue calculus

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_circle\_residue\_calculus.md}.
\]
For \(p>3\), the four offset root sets are disjoint.  Therefore
\[
  |B_p(n)|
  =
  4+\sum_{r\in\{-1,0,1,2\}}\chi_p(-n^2-r).
\]
Averaging over \(n\bmod p\) gives the exact local bias
\[
  \mathbb E |B_p(n)|
  =
  \begin{cases}
    5-\dfrac4p, & p\equiv1\pmod4,\\[6pt]
    3+\dfrac4p, & p\equiv3\pmod4.
  \end{cases}
\]
This proves that the circle cover is structurally asymmetric: primes
\(1\pmod4\) cover more local \(t\)-classes on average because they can cover
the primitive Gaussian channel \(r=0\), while primes \(3\pmod4\) cannot.

## Four-consecutive certificate layer

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_four\_consecutive\_certificate.md}.
\]
For fixed \(n,t\), write
\[
  A=n^2+t^2.
\]
The four candidates
\[
  A-1,\quad A,\quad A+1,\quad A+2
\]
are consecutive.  Hence
\[
  \gcd(A+r,A+s)\mid |r-s|.
\]
Consequently, any prime \(p>3\) can certify at most one offset at a fixed
\(t\).  The only shared-prime layers are deterministic:

1. \(2\) certifies exactly two parity-selected candidates;
2. \(3\) certifies one candidate, except when \(A\equiv1\pmod3\), where it
   certifies both \(A-1\) and \(A+2\).

After removing the \(2,3\)-layer, the residual demand has size at most \(2\),
depending only on \(A\bmod6\).  The Gaussian residual \(A=n^2+t^2\) remains
only when
\[
  A\equiv1\text{ or }5\pmod6,
\]
and on primitive \(t\)'s it can only be certified by primes \(1\pmod4\).

This converts the next proof target into a constrained certificate-assignment
problem for residual primes \(p>3\), not a raw prime-gap estimate.

## Primitive Gaussian channel reduction

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_primitive\_channel\_reduction.md}.
\]
On the natural Gaussian-safe channel
\[
  \gcd(n,t)=1,\qquad n+t\equiv1\pmod2,
\]
write
\[
  A=n^2+t^2.
\]
Then \(A\) is odd, and the deterministic \(2,3\)-layer collapses the
four-offset family as follows:
\[
\begin{array}{c|c|c}
  \text{condition mod }3 & A\bmod6 & \text{remaining prime condition} \\
  \hline
  \text{exactly one of } n,t \text{ divisible by }3 & 1 & A\text{ prime} \\
  \text{neither } n \text{ nor } t \text{ divisible by }3 & 5 &
  A\text{ prime or }A+2\text{ prime}.
\end{array}
\]
Thus the four-offset statement becomes, on primitive opposite-parity \(t\)'s,
a Gaussian norm/twin-shift statement:
\[
  n^2+t^2
  \quad\text{or}\quad
  n^2+t^2+2.
\]
This is a sharper exact target than the full four-circle cover.

## Primitive double-cover reduction

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_primitive\_double\_cover.md}.
\]
Let
\[
  I_n=\{1\le t\le\lfloor\sqrt{2n}\rfloor:
  \gcd(n,t)=1,\ n+t\equiv1\pmod2\}.
\]
Define the Gaussian bad set
\[
  G(n)=
  \bigcup_{\substack{p\le n\\ p\equiv1\pmod4}}
  \{t:t^2\equiv -n^2\pmod p\}.
\]
Then every counterexample must satisfy the universal primitive Gaussian cover
\[
  I_n\subseteq G(n).
\]
If \(3\nmid n\), there is also a double-cover condition on the interior
nonmultiples of \(3\).  With
\[
  T(n)=
  \bigcup_{\substack{q\le n\\ q>3}}
  \{t:t^2\equiv -n^2-2\pmod q\},
\]
and
\[
  I_n^+=\{t\in I_n:t^2+2\le2n\},
\]
one needs
\[
  I_n^{(\ast)}\cap I_n^+\subseteq G(n)\cap T(n),
\]
where \(I_n^{(\ast)}=\{t\in I_n:3\nmid t\}\).

This is the strongest current exact reduction: any counterexample must first
destroy every primitive opposite-parity Gaussian norm, and then, for most
remaining primitive positions when \(3\nmid n\), also destroy the twin-shift
\(n^2+t^2+2\).

## Multiple-of-three channel

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_multiple\_of\_three\_channel.md}.
\]
For the remaining obstruction, write
\[
  n=3m.
\]
There are two channels.

If \(3\nmid t\), then on the primitive opposite-parity channel the previous
modulo-\(6\) reduction leaves only the pure Gaussian candidate
\[
  9m^2+t^2.
\]

If \(3\mid t\), write \(t=3u\).  Then
\[
  n^2+t^2=9(m^2+u^2).
\]
The offset \(r=0\) is automatically composite, and the repair channel becomes
\[
  9(m^2+u^2)-1,\qquad
  9(m^2+u^2)+1,\qquad
  9(m^2+u^2)+2.
\]
Parity collapses this further.  If \(m\equiv u\pmod2\), the possible primes are
\[
  9(m^2+u^2)-1
  \quad\text{or}\quad
  9(m^2+u^2)+1.
\]
If \(m\not\equiv u\pmod2\), the only possible prime is
\[
  9(m^2+u^2)+2.
\]

Thus the \(3\mid n\) obstruction has been reduced to a mixed
primitive/nonprimitive dichotomy, not a global residue cover.

## Primitive double-cover measurements

Added
\[
  \texttt{Math/conjecture/legendre/tools/primitive\_double\_cover\_measure.py}.
\]
For each \(n\), it measures the exact primitive-channel quantities
\[
  |I_n|,
  \qquad
  |G(n)\cap I_n|,
  \qquad
  |G(n)\cap T(n)\cap I_n^{(\ast)}\cap I_n^+|.
\]
The implementation uses the exact primality interpretation on the primitive
channel: \(t\in G(n)\) iff \(n^2+t^2\) is composite, and on the interior
Case-II channel \(t\in T(n)\) iff \(n^2+t^2+2\) is composite.

For \(2\le n\le100000\), the result is:
\[
\begin{array}{c|c}
  \text{quantity} & \text{value} \\
  \hline
  \text{Gaussian full covers } I_n\subseteq G(n) & 33 \\
  \text{killed by Gaussian layer} & 99966 \\
  \text{killed by double layer after Gaussian cover} & 7 \\
  \text{primitive double-cover survivors} & 26.
\end{array}
\]
The \(33\) Gaussian full covers are exactly the previously known pure-square
failures.  The \(7\) cases killed by the double layer are
\[
  23,83,113,152,196,592,811.
\]
The remaining \(26\) primitive double-cover survivors all satisfy
\[
  3\mid n.
\]
For these values, the primitive channel has no Case-II twin-shift domain:
primitivity forces \(3\nmid t\), so exactly one of \(n,t\) is divisible by
\(3\), and only the Gaussian candidate \(n^2+t^2\) survives the deterministic
\(2,3\)-layer.

Thus the current exact picture is:

1. if \(3\nmid n\), the primitive Gaussian plus twin-shift channel already
   kills all observed Gaussian full covers up to \(100000\);
2. the remaining obstruction is concentrated at \(3\mid n\), where one must
   use a nonprimitive/divisor channel or another offset to escape the pure
   Gaussian cover.
