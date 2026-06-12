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

## Refined multiple-of-three channels

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_multiple\_of\_three\_refined\_channels.md}
\]
and the auxiliary checker
\[
  \texttt{Math/conjecture/legendre/tools/multiple\_of\_three\_channel\_measure.py}.
\]

The first \(M_3\) candidate is false as stated.  It omitted an exact surviving
subchannel.

For \(n=3m\) and \(3\nmid t\),
\[
  n^2+t^2+r\equiv1+r\pmod3.
\]
Hence the offsets \(r=-1\) and \(r=2\) are automatically divisible by \(3\),
and the only possible prime subchannels are
\[
  r=0,\qquad r=1.
\]

The \(r=0\) subchannel is exactly the primitive opposite-parity Gaussian
channel:
\[
  \gcd(3m,t)=1,\qquad 3m+t\equiv1\pmod2,\qquad
  9m^2+t^2\ \text{prime}.
\]
The missing subchannel is the unit lift
\[
  3\nmid t,\qquad t\equiv m\pmod2,\qquad
  9m^2+t^2+1\ \text{prime}.
\]

This missing channel gives an exact counterexample to the first \(M_3\)
candidate:
\[
  m=4,\qquad n=12.
\]
The primitive Gaussian channel gives only
\[
  12^2+1^2=145=5\cdot29,
\]
and the \(t=3u\) channel gives
\[
  9(4^2+1^2)+2=155=5\cdot31.
\]
But the full four-offset family is repaired by
\[
  12^2+2^2+1=149,
\]
which is prime.

Therefore the corrected target is \(M_3^\ast\), with three exact channels:

1. \(A0\): \(3\nmid t\), primitive opposite-parity, \(9m^2+t^2\) prime;
2. \(A1\): \(3\nmid t\), same parity, \(9m^2+t^2+1\) prime;
3. \(B\): \(t=3u\), with the parity-collapsed candidates
   \[
     9(m^2+u^2)-1,\quad 9(m^2+u^2)+1,\quad 9(m^2+u^2)+2.
   \]

The auxiliary checker is not a proof, but it confirms that this corrected
classification is the right object to attack: up to \(m=1000000\), the full
four-offset \(n=3m\) channel had no failures; only two cases required
\(t=3u\), namely
\[
  m=10,\qquad m=391.
\]

## \(M_3^\ast\) counterexample certificate

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3star\_certificate.md}.
\]

This note removes the remaining ambiguity in what a failure of the corrected
\(M_3^\ast\) target would mean.

For every admissible candidate
\[
  N=9m^2+t^2+r,\qquad 1\le t^2+r\le6m,
\]
one has
\[
  9m^2<N<(3m+1)^2.
\]
Therefore, if \(N\) is composite, it has a prime divisor
\[
  p\le3m.
\]
Since the surviving channels have already passed the \(2\)- and \(3\)-layers,
every certificate prime satisfies \(p\ge5\).

Thus a counterexample to \(M_3^\ast\) is equivalent to three simultaneous
small-prime covers.

The A0 cover is Gaussian:
\[
  \mathcal A_0(m)
  \subseteq
  \bigcup_{\substack{p\le3m\\ p\equiv1\pmod4\\ p\nmid3m}}
  \{t:t^2\equiv-9m^2\pmod p\}.
\]

The A1 cover is the new unit-lift cover:
\[
  \mathcal A_1(m)
  \subseteq
  \bigcup_{\substack{p\le3m\\ p\ge5}}
  \{t:t^2\equiv-9m^2-1\pmod p\}.
\]
If \(p\mid m\), then A1 reduces to
\[
  t^2\equiv-1\pmod p,
\]
so primes \(p\mid m\), \(p\equiv3\pmod4\), are invisible to A1.

The B cover is the parity-split \(t=3u\) cover:
\[
  (3u)^2\equiv1-9m^2,\qquad
  (3u)^2\equiv-1-9m^2,\qquad
  (3u)^2\equiv-2-9m^2
  \pmod p,
\]
with the corresponding admissibility bounds.

The next exact target is therefore the combined A-cover, not another
simulation:
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
For \(3\nmid t\), this single parity-twisted family is exactly the surviving
\(3\nmid t\) channel.

## Combined A-cover rigidity

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_combined\_A\_cover.md}.
\]

This note attacks the combined \(3\nmid t\) channel directly instead of
treating A0 and A1 as independent covers.

For
\[
  3\nmid t,
\]
the surviving candidate is
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

The values \(3\nmid t\) occur in adjacent blocks
\[
  B_q=\{3q+1,\ 3q+2\}.
\]
In every complete admissible block, one member lies on A0 and the other lies
on A1.

The key exact lemma is the adjacent-pair collision lemma.  Let
\[
  a=3q+1,\qquad b=3q+2.
\]
If an odd prime \(p\) divides both
\[
  P_m(a)
  \qquad\text{and}\qquad
  P_m(b),
\]
then
\[
  p\mid9m^2+1.
\]
More precisely:

- if \(a\equiv m\pmod2\), then \(p\mid a\);
- if \(a\not\equiv m\pmod2\), then \(p\mid b\).

Thus a single prime can certify both members of a complete A-block only if it
is a bridge prime
\[
  p\mid9m^2+1.
\]
Every bridge prime satisfies
\[
  p\equiv1\pmod4.
\]

Therefore an A-cover counterexample must provide, for every complete
A-block, either two independent small-prime certificates or one bridge prime
with an explicit linear congruence:
\[
\begin{array}{c|c}
  a\equiv m\pmod2 & 3q+1\equiv0\pmod p \\
  a\not\equiv m\pmod2 & 3q+2\equiv0\pmod p.
\end{array}
\]

This is the new exact obstruction.  The next target is to prove that the
complete A-blocks cannot all satisfy this two-certificate-or-bridge
alternative.

## Exact gcd in complete A-blocks

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_A\_block\_gcd.md}.
\]

This sharpens the bridge-prime obstruction by computing the full gcd inside
each complete A-block.

Let
\[
  a=3q+1,\qquad b=3q+2.
\]
For the combined A-family
\[
  P_m(t)=9m^2+t^2+\epsilon_m(t),
\]
define the bridge coordinate
\[
  c_q=
  \begin{cases}
  a,&a\equiv m\pmod2,\\
  b,&a\not\equiv m\pmod2.
  \end{cases}
\]
Then for every complete A-block,
\[
  \boxed{
  \gcd(P_m(a),P_m(b))=\gcd(c_q,9m^2+1).
  }
\]

Proof outline:

- if \(a\equiv m\pmod2\), then
  \[
    P_m(a)=9m^2+a^2+1,\qquad P_m(b)=9m^2+b^2,
  \]
  and
  \[
    P_m(b)-P_m(a)=2a.
  \]
  Since both values are odd,
  \[
    \gcd(P_m(a),P_m(b))=\gcd(a,9m^2+1).
  \]
- if \(a\not\equiv m\pmod2\), then
  \[
    P_m(a)=9m^2+a^2,\qquad P_m(b)=9m^2+b^2+1,
  \]
  and
  \[
    P_m(b)-P_m(a)=2b.
  \]
  Hence
  \[
    \gcd(P_m(a),P_m(b))=\gcd(b,9m^2+1).
  \]

Therefore all common prime factors in a complete A-block are exactly bridge
prime factors.  There are no hidden common divisors.

Call a block coprime when
\[
  \gcd(c_q,9m^2+1)=1.
\]
On such a block, a counterexample must provide two genuinely distinct prime
certificates
\[
  p_a\mid P_m(3q+1),\qquad p_b\mid P_m(3q+2),\qquad p_a\ne p_b.
\]

The remaining proof target is now narrower: prove that for every \(m\), some
coprime complete A-block cannot carry two independent small-prime
certificates.  If this is achieved, the combined A-channel closes and the
nonprimitive B-channel becomes unnecessary.

## Coprime A-block pair cover

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_coprime\_A\_pair\_cover.md}.
\]

On a coprime complete A-block, write
\[
  t_1(q)=
  \begin{cases}
  3q+1,&3q+1\equiv m\pmod2,\\
  3q+2,&3q+1\not\equiv m\pmod2,
  \end{cases}
\]
for the A1 coordinate, and let \(t_0(q)\) be the other coordinate.

The two candidates are
\[
  U_q=9m^2+t_1(q)^2+1,
  \qquad
  G_q=9m^2+t_0(q)^2.
\]

For a coprime block,
\[
  \gcd(U_q,G_q)=1.
\]
Thus if both candidates are composite, their certificate primes
\[
  p_1\mid U_q,\qquad p_0\mid G_q
\]
must be distinct.

The exact congruences are
\[
  t_0(q)^2\equiv-9m^2\pmod{p_0},
  \qquad
  t_1(q)^2\equiv-9m^2-1\pmod{p_1},
\]
with
\[
  p_0\le3m,\quad p_0\equiv1\pmod4,\quad p_0\nmid3m,
\]
and
\[
  p_1\le3m,\quad p_1\ge5,\quad p_1\ne p_0.
\]

Because \(t_0(q)\) and \(t_1(q)\) are linear in \(q\), each ordered pair
\[
  (p_0,p_1)
\]
contributes at most four CRT residue classes modulo
\[
  p_0p_1.
\]

This is the pair-cover form of the coprime A-block obstruction.  It is
strictly stronger than the earlier prime-by-prime cover: the two members of a
coprime block cannot reuse a certificate prime.

The current exact bottleneck is now:

1. control the small ordered pairs
   \[
     p_0p_1\le Q_{\max}(m);
   \]
2. show that large ordered pairs
   \[
     p_0p_1>Q_{\max}(m)
   \]
   give only isolated hits and cannot fill all remaining coprime blocks.

## Pair incidence geometry

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_pair\_incidence\_geometry.md}.
\]

This rewrites the coprime A-block pair cover as an incidence problem in
\((m,q)\).

Let
\[
  a=3q+1,\qquad b=3q+2.
\]
There are two orientations.

If \(a\equiv m\pmod2\), then \(a\) is A1 and \(b\) is A0, so a pair
certificate satisfies
\[
  (3q+2)^2+9m^2\equiv0\pmod{p_0},
\]
\[
  (3q+1)^2+9m^2+1\equiv0\pmod{p_1}.
\]

If \(a\not\equiv m\pmod2\), then \(a\) is A0 and \(b\) is A1, so
\[
  (3q+1)^2+9m^2\equiv0\pmod{p_0},
\]
\[
  (3q+2)^2+9m^2+1\equiv0\pmod{p_1}.
\]

Thus the obstruction is a cover by two oriented products of conics over
\[
  \mathbb F_{p_0}\times\mathbb F_{p_1}.
\]

The coprime condition removes the degenerate A1 case.  On a coprime block,
an A1 certificate prime must satisfy
\[
  p_1\nmid9m^2+1.
\]
Therefore A1 exists only when
\[
  \left(\frac{-9m^2-1}{p_1}\right)=1,
\]
with a nonzero root.

The sharpened pair-certificate restrictions are:
\[
\begin{array}{ll}
  p_0\le3m, & p_0\equiv1\pmod4,\quad p_0\nmid3m,\\
  p_1\le3m, & p_1\ne p_0,\quad p_1\nmid9m^2+1,\\
             & \left(\frac{-9m^2-1}{p_1}\right)=1.
\end{array}
\]

The next exact target is to prove that these oriented conic-product
incidences cannot cover all coprime complete A-blocks after bridge blocks are
removed.

## A1 local filter

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_A1\_local\_filter.md}.
\]

This computes the exact local filter on \(m\bmod p\) imposed by the A1
certificate condition
\[
  \left(\frac{-9m^2-1}{p}\right)=1,
\]
with the nonzero condition
\[
  p\nmid9m^2+1.
\]

Let \(\chi\) be the quadratic character modulo \(p\ge5\).  For
\[
  f(m)=-9m^2-1,
\]
the discriminant is
\[
  -36\not\equiv0\pmod p.
\]
Hence the standard quadratic character sum gives
\[
  \sum_{m\bmod p}\chi(-9m^2-1)=-\chi(-9)=-\chi(-1).
\]

The zero classes satisfy
\[
  (3m)^2\equiv-1\pmod p,
\]
so there are
\[
  Z_p=1+\chi(-1)
\]
of them.

Therefore the number \(R_p\) of A1-admissible classes is
\[
  R_p=\frac{p-Z_p-\chi(-1)}{2},
\]
or explicitly
\[
\boxed{
R_p=
\begin{cases}
\dfrac{p-3}{2},&p\equiv1\pmod4,\\[2mm]
\dfrac{p+1}{2},&p\equiv3\pmod4.
\end{cases}}
\]

Thus an A1 prime \(p_1\) is unavailable for residue classes \(m\) outside this
set, and for each available class it contributes exactly two nonzero roots.

The next exact target is to combine this A1 \(m\)-filter with the
coprime-block \(q\)-interval and the A0 restriction \(p_0\equiv1\pmod4\).

## Pair incidence density bound

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_pair\_density\_bound.md}.
\]

This computes the exact local density contributed by one ordered certificate
pair
\[
  (p_0,p_1).
\]

For A0, since \(p_0\equiv1\pmod4\), every nonzero \(m\bmod p_0\) gives
exactly two \(q\)-classes.  Thus A0 contributes
\[
  2(p_0-1)
\]
incidence pairs modulo \(p_0\).

For A1, the local filter gives
\[
R_{p_1}=
\begin{cases}
\dfrac{p_1-3}{2},&p_1\equiv1\pmod4,\\[2mm]
\dfrac{p_1+1}{2},&p_1\equiv3\pmod4.
\end{cases}
\]
For each admissible \(m\bmod p_1\), A1 contributes exactly two
\(q\)-classes, hence
\[
  2R_{p_1}
\]
incidence pairs modulo \(p_1\).

By CRT, the ordered pair contributes exactly
\[
  4(p_0-1)R_{p_1}
\]
points \((m,q)\) modulo \(p_0p_1\).  The local density is
\[
\boxed{
  \delta(p_0,p_1)
  =
  \frac{4(p_0-1)R_{p_1}}{p_0^2p_1^2}.
}
\]

In particular,
\[
  \delta(p_0,p_1)\approx \frac{2}{p_0p_1}.
\]

This gives a useful failed route: the naive union bound over ordered pairs is
not strong enough to close the cover, because
\[
  \sum_{p_0p_1\le Q}\frac1{p_0p_1}
\]
does not give a uniform contradiction.

Therefore pair density alone does not close the combined A-channel.  The
next proof attempt must use fixed-\(m\) correlations, especially:

1. A1 availability depends on the fixed value
   \[
     \left(\frac{-9m^2-1}{p_1}\right);
   \]
2. bridge blocks have been removed by
   \[
     \gcd(t_1(q),9m^2+1)=1;
   \]
3. the \(q\)-classes come from two oriented conic systems, not arbitrary
   residue classes.

The next exact target is a fixed-\(m\) large-sieve style obstruction for the
available A1 primes.

## Fixed-\(m\) sieve decomposition

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_fixed\_m\_sieve\_decomposition.md}.
\]

This replaces the ordered pair union by a two-layer fixed-\(m\) sieve.

For a coprime complete block \(B_q=\{3q+1,3q+2\}\), let \(t_0(q)\) be the A0
coordinate and \(t_1(q)\) the A1 coordinate.  Define
\[
  G_q=9m^2+t_0(q)^2,
\]
\[
  U_q=9m^2+t_1(q)^2+1.
\]

Let \(\mathcal Q_{\rm cop}(m)\) be the set of complete coprime blocks.

The Gaussian sieve layer is
\[
  S_0(m)
  =
  \mathcal Q_{\rm cop}(m)
  \cap
  \bigcup_{\substack{p\le3m\\p\equiv1\pmod4\\p\nmid3m}}
  \{q:t_0(q)^2\equiv-9m^2\pmod p\}.
\]
Each prime in this union contributes exactly two classes modulo \(p\).

The unit-lift sieve layer is
\[
  S_1(m)
  =
  \mathcal Q_{\rm cop}(m)
  \cap
  \bigcup_{\substack{p\le3m\\p\nmid9m^2+1\\
  \left(\frac{-9m^2-1}{p}\right)=1}}
  \{q:t_1(q)^2\equiv-9m^2-1\pmod p\}.
\]
Each available prime again contributes exactly two classes modulo \(p\), while
unavailable A1 primes contribute none.

The exact fixed-\(m\) obstruction is now
\[
\boxed{
  \mathcal Q_{\rm cop}(m)\subseteq S_0(m)\cap S_1(m).
}
\]

Therefore the combined A-channel closes if one proves
\[
  \mathcal Q_{\rm cop}(m)\not\subseteq S_0(m)\cap S_1(m)
  \qquad\text{for every }m\ge1.
\]

This is the cleanest current proof target.  It avoids the weak naive
pair-density union bound and keeps the fixed-\(m\) correlations visible.

## Fixed-\(m\) large-sieve target

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_fixed\_m\_large\_sieve\_target.md}.
\]

This formulates the closure criterion as a covering obstruction.

For fixed \(m\), define
\[
  \Omega_{0,p}(m)=
  \{q:t_0(q)^2\equiv-9m^2\pmod p\},
\]
for
\[
  p\in\mathcal P_0(m)=
  \{p\le3m:p\equiv1\pmod4,\ p\nmid3m\},
\]
and
\[
  \Omega_{1,p}(m)=
  \{q:t_1(q)^2\equiv-9m^2-1\pmod p\},
\]
for
\[
  p\in\mathcal P_1(m)=
  \left\{
  p\le3m:p\nmid9m^2+1,\quad
  \left(\frac{-9m^2-1}{p}\right)=1
  \right\}.
\]

Each available prime contributes exactly two residue classes.

The fixed-\(m\) double-sieve lemma needed for closure is:
\[
  \mathcal Q_{\rm cop}(m)\not\subseteq S_0(m)\cap S_1(m)
  \qquad(m\ge1).
\]

Equivalently, one must show that the two quadratic-root covering systems
\[
  \{\Omega_{0,p}(m)\}_{p\in\mathcal P_0(m)}
  \quad\text{and}\quad
  \{\Omega_{1,p}(m)\}_{p\in\mathcal P_1(m)}
\]
cannot simultaneously cover every coprime complete block.

The note also records a limitation: the classical large sieve is not directly
enough, because it bounds sets occupying few residue classes, whereas here
the bad sets are unions of few residue classes and the desired conclusion is
that their union does not cover the interval.

The next possible nonstandard attack is to study the product family
\[
  \Phi_m(q)=
  \left(9m^2+t_0(q)^2\right)
  \left(9m^2+t_1(q)^2+1\right),
\]
using the exact fact that on coprime blocks the two factors are coprime.

## Product attack for coprime A-blocks

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_phi\_product\_attack.md}.
\]

This develops the product route
\[
  \Phi_m(q)=G_qU_q,
\]
where
\[
  G_q=9m^2+t_0(q)^2,
  \qquad
  U_q=9m^2+t_1(q)^2+1.
\]

There are two orientations:

- if \(a=3q+1\equiv m\pmod2\), then
  \[
    \Phi_m^{(I)}(q)
    =
    (9m^2+(3q+2)^2)(9m^2+(3q+1)^2+1);
  \]
- if \(a\not\equiv m\pmod2\), then
  \[
    \Phi_m^{(II)}(q)
    =
    (9m^2+(3q+1)^2)(9m^2+(3q+2)^2+1).
  \]

On coprime blocks,
\[
  \gcd(G_q,U_q)=1.
\]
The two factors also have the exact small difference
\[
  |G_q-U_q|=2t_1(q).
\]

The product route gives useful structure:

1. the two factors are coprime;
2. their difference is a small linear term;
3. their small prime divisors must come from different quadratic families.

However, the route does not close by a simple fixed-divisor argument.  The
product congruence
\[
  \Phi_m(q)\equiv0\pmod{p_0p_1}
\]
is exactly the pair-cover condition already isolated.

Thus this is a failed shortcut but a useful reformulation.  The remaining
target is a transversality lemma: not every coprime complete block can carry
two transverse small-prime certificates satisfying the Gaussian and A1
restrictions.

## Transversality repetition constraints

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_transversality\_repetition.md}.
\]

This extracts the first multi-block obstruction from the transversality
formulation.

If the same prime \(p\) certifies two blocks \(q\) and \(r\) in the same
layer, then the two relevant linear coordinates satisfy
\[
  t(q)^2\equiv t(r)^2\pmod p.
\]
Therefore
\[
  t(q)\equiv\pm t(r)\pmod p.
\]

Writing
\[
  t(q)=3q+\alpha,\qquad t(r)=3r+\beta,\qquad \alpha,\beta\in\{1,2\},
\]
the plus sign gives
\[
  q\equiv r\pmod p,
\]
and the minus sign gives the mirror relation
\[
  q+r\equiv-\frac{\alpha+\beta}{3}\pmod p.
\]

Thus a single certificate prime does not produce arbitrary coverage of block
indices.  Its fiber is a union of arithmetic progressions and mirror
progressions.  A full counterexample would require both A0 and A1 layers to
cover every coprime complete block by two transverse systems of such
progression/mirror fibers.

This is sharper than the pair-density bound and the product formulation.  It
turns the next target into an additive congruence obstruction on the
\(q\)-line.

## Adjacent block obstruction

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_adjacent\_block\_obstruction.md}.
\]

This strengthens the repetition constraint for neighboring blocks.

For adjacent indices \(q\) and \(q+1\), the block orientation flips.  In both
layers \(i=0,1\), one has
\[
  t_i(q)+t_i(q+1)=6(q+1).
\]

If a prime \(p\ge5\) certifies both adjacent blocks in the same layer, then
\[
  t_i(q)^2\equiv t_i(q+1)^2\pmod p.
\]
Since the adjacent difference is \(2\) or \(4\), it is nonzero modulo
\(p\ge5\).  Hence
\[
  p\mid t_i(q)+t_i(q+1)=6(q+1),
\]
and therefore
\[
\boxed{
  p\mid q+1.
}
\]

Thus same-prime repetition on adjacent blocks is possible only at explicit
divisor positions.  Away from indices \(q\) with \(p\mid q+1\), the
certificate prime must change from one block to the next in that layer.

The obstruction has now become a labeling problem on an interval of
coprime-block indices: every vertex needs an A0 label and an A1 label, labels
must satisfy their local quadratic restrictions, the two labels at a vertex
are distinct, and adjacent repeated labels are allowed only at divisor
positions.

## Triple-block labeling obstruction

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_triple\_block\_labeling.md}.
\]

This records a direct consequence of the adjacent-block obstruction.

In a fixed layer \(i\), suppose the same prime \(p\ge5\) certifies three
consecutive blocks
\[
  q,\qquad q+1,\qquad q+2.
\]
Applying the adjacent obstruction to \(q,q+1\) gives
\[
  p\mid q+1.
\]
Applying it to \(q+1,q+2\) gives
\[
  p\mid q+2.
\]
Hence \(p\mid1\), impossible.

Therefore
\[
\boxed{
\text{one prime cannot certify three consecutive blocks in one layer.}
}
\]

The remaining counterexample condition is now a two-layer labeling problem:
each coprime complete block needs an A0 label and an A1 label; the two labels
at a block are distinct; adjacent repeated labels are allowed only at divisor
positions; and triple repetition is impossible.

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

## Initial block obstruction

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_block\_obstruction.md}.
\]

This applies the two-layer labeling rules to the first three A-blocks
\[
  B_0=\{1,2\},\qquad B_1=\{4,5\},\qquad B_2=\{7,8\}.
\]
They are complete for \(m\ge11\), since the largest initial A1 offset
satisfies
\[
  8^2+1=65\le6m.
\]

The coprime-block condition
\[
  \gcd(t_1(q),9m^2+1)=1
\]
is automatic for \(B_0\) and \(B_2\).  For \(B_1\), the only loss is
\[
  m\ \text{odd},\qquad m\equiv\pm1\pmod5.
\]

Thus, for \(m\ge11\) outside those two residue classes, the first three
blocks are complete and coprime.  The adjacent-block obstruction then gives:
\[
  p_i(0)\ne p_i(1),\qquad p_i(1)\ne p_i(2)
\]
in each layer \(i=0,1\), because adjacent repetition would force \(p\mid1\)
or \(p\mid2\).

The only possible same-layer repetition inside this initial triple is between
\(B_0\) and \(B_2\).  Since the orientations agree and the coordinates differ
by \(6\), such a repetition forces
\[
  p\mid 2t_i(0)+6.
\]
With \(t_i(0)\in\{1,2\}\), the only possible certificate prime \(p\ge5\) is
\[
  p=5,
\]
and only for the coordinate \(t_i(0)=2\).

The exact residue split for this exceptional repetition is:
\[
\begin{array}{ll}
  \text{A0 repetition by }5: & m\ \text{odd},\ m\equiv\pm2\pmod5,\\
  \text{A1 repetition by }5: & m\ \text{even},\ 5\mid m.
\end{array}
\]

So the first universal triple now gives a finite exact local obstruction.
It does not close Legendre, but it sharply restricts the start of any
remaining \(m\)-certificate before the later interval is considered.

## Initial mod 10 gate

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_mod10\_gate.md}.
\]

This compresses the initial-block obstruction into an exact residue
classification modulo \(10\).

For \(m\ge11\), the first three blocks are complete.  Their behavior is:
\[
\begin{array}{c|c}
  m\bmod10 & \text{gate}\\
  \hline
  2,4,5,6,8 & \text{all three blocks coprime; no same-layer repetition}\\
  0 & \text{all three blocks coprime; only A1 can repeat }5\\
  3,7 & \text{all three blocks coprime; only A0 can repeat }5\\
  1,9 & B_1\text{ is a bridge block with bridge prime }5.
\end{array}
\]

The bridge classes are exactly
\[
  m\equiv1,9\pmod{10},
\]
because then \(m\) is odd, \(t_1(1)=5\), and
\[
  5\mid9m^2+1.
\]
Consequently \(5\) divides both middle-block candidates
\[
  9m^2+4^2,\qquad 9m^2+5^2+1.
\]

The A0 repetition classes are exactly
\[
  m\equiv3,7\pmod{10},
\]
coming from
\[
  9m^2+2^2\equiv0\pmod5.
\]
The A1 repetition class is exactly
\[
  m\equiv0\pmod{10}.
\]

Thus every remaining \(m\ge11\) certificate must enter one of four finite
gates: strong no-repetition, A0-\(5\), A1-\(5\), or bridge-\(5\).  The next
exact closure target is to show that none of these gates can be extended to a
full two-layer certificate over the complete block interval.

## Initial four-block repetition graph

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_four\_block\_graph.md}.
\]

This extends the exact initial obstruction to
\[
  B_0=\{1,2\},\quad B_1=\{4,5\},\quad B_2=\{7,8\},\quad B_3=\{10,11\}.
\]
The four blocks are complete for \(m\ge21\).

The new block \(B_3\) adds bridge classes.  If \(t_1(3)=10\), then
\[
  5\mid9m^2+1
  \quad\Longleftrightarrow\quad
  m^2\equiv1\pmod5.
\]
Thus \(B_3\) is a bridge block exactly for
\[
  m\equiv4,6\pmod{10}.
\]
If \(t_1(3)=11\), a common factor would require
\[
  m^2\equiv6\pmod{11},
\]
which is impossible.

The two coordinate sequences are
\[
  E=(2,4,8,10),\qquad O=(1,5,7,11).
\]
For primes \(p\ge5\), repetitions inside \(E\) are possible only for
\[
  (2,8)\text{ by }5,\qquad (4,10)\text{ by }7,
\]
and repetitions inside \(O\) are possible only for
\[
  (1,11)\text{ by }5.
\]

Consequently, for \(m\ge21\) outside the first-four bridge classes
\[
  m\equiv\pm1\pmod5,
\]
all same-layer repetitions among \(B_0,\dots,B_3\) are exactly:
\[
\begin{array}{c|c|c|c}
  \text{layer} & \text{blocks} & \text{prime} & \text{condition on }m\\
  \hline
  \text{A1} & B_0/B_2 & 5 & m\equiv0\pmod{10}\\
  \text{A1} & B_1/B_3 & 7 & m\text{ even},\ m\equiv\pm3\pmod7\\
  \text{A0} & B_0/B_2 & 5 & m\equiv3,7\pmod{10}\\
\end{array}
\]

There are no other early same-layer repetitions.  The beginning of any
remaining certificate is therefore a finite explicit graph, not an arbitrary
labeling pattern.  The apparent \(B_0/B_3\) repetition by \(5\) occurs
precisely in the \(B_3\) bridge classes \(m\equiv4,6\pmod{10}\), so it is not
a coprime-block edge.

## Initial mod 70 gate

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_mod70\_gate.md}.
\]

This compresses the first-four-block graph into a single CRT classification.
The relevant moduli are \(10\) and \(14\), so the gate is modulo
\[
  70.
\]

For \(m\ge21\), the bridge classes are exactly
\[
  m\equiv\pm1\pmod5.
\]
There are \(28\) such residue classes modulo \(70\).

Outside the bridge classes, the possible same-layer edges are:
\[
\begin{array}{c|c|c|c}
  \text{edge} & \text{layer} & \text{prime} & \text{condition}\\
  \hline
  B_0/B_2 & \text{A1} & 5 & m\equiv0\pmod{10}\\
  B_0/B_2 & \text{A0} & 5 & m\equiv3,7\pmod{10}\\
  B_1/B_3 & \text{A1} & 7 & m\equiv4,10\pmod{14}.
\end{array}
\]

The exact modulo \(70\) partition is:
\[
  28\ \text{bridge classes}
  +17\ \text{no-repetition classes}
  +14\ \text{A0-edge classes}
  +5\ \text{A1-}5\text{-only classes}
  +4\ \text{A1-}7\text{-only classes}
  +2\ \text{double-A1 classes}
  =70.
\]

The no-repetition classes are:
\[
  2,5,8,12,15,22,25,28,35,42,45,48,55,58,62,65,68.
\]
In these classes, each layer needs four pairwise distinct labels on the first
four blocks.

The double-A1 classes are:
\[
  10,60.
\]
There A1 may reuse \(5\) on \(B_0/B_2\) and \(7\) on \(B_1/B_3\), while A0
has no same-layer repetition among the first four blocks.

Thus the beginning of any remaining \(m\)-certificate is now completely
localized modulo \(70\).  The next exact target is to eliminate the six gate
types separately, starting with the strong no-repetition gate and the bridge
gate.

## Initial cross-layer collision lemma

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_cross\_layer\_collisions.md}.
\]

This studies when a single prime can appear once as an A0 label and once as
an A1 label among \(B_0,\dots,B_3\).

If \(x\) is an A0 coordinate and \(y\) is an A1 coordinate, a cross-layer
collision by \(p\ge5\) imposes
\[
  9m^2+x^2\equiv0\pmod p,
\]
\[
  9m^2+y^2+1\equiv0\pmod p.
\]
Subtracting eliminates \(m\):
\[
  y^2+1-x^2\equiv0\pmod p.
\]
Thus the collision prime must divide the fixed integer
\[
  \Delta(x,y)=y^2+1-x^2.
\]

Outside the first-four bridge classes \(m\not\equiv\pm1\pmod5\), the exact
valid cross-layer collisions are:
\[
\begin{array}{c|c|c|c|c}
  m\text{ parity} & \text{A0 block} & \text{A1 block} & p & \text{condition on }m\\
  \hline
  \text{even} & B_2 & B_3 & 13 & m\equiv\pm3\pmod{13}\\
  \text{even} & B_3 & B_0 & 29 & m\equiv\pm14\pmod{29}\\
  \text{even} & B_3 & B_1 & 13 & m\equiv\pm1\pmod{13}\\
  \text{odd} & B_1 & B_2 & 17 & m\equiv\pm6\pmod{17}\\
  \text{odd} & B_1 & B_3 & 53 & m\equiv\pm13\pmod{53}\\
  \text{odd} & B_2 & B_3 & 29 & m\equiv\pm3\pmod{29}\\
  \text{odd} & B_3 & B_1 & 37 & m\equiv\pm17\pmod{37}.
\end{array}
\]

All other finite candidates either lie in bridge classes, violate the A0
condition \(p\nmid3m\), or require a non-square class for \(m^2\).

Consequently, in strong no-same-layer-repetition classes, if \(m\) also
avoids these cross-layer collision congruences, the first four blocks force
eight distinct certificate labels:
\[
  p_0(0),p_0(1),p_0(2),p_0(3),
  p_1(0),p_1(1),p_1(2),p_1(3).
\]

The remaining strong-gate target is now sharper: either eight distinct small
labels appear immediately, or \(m\) is forced into one of the listed
cross-layer collision classes.

## Initial pairwise-coprime cluster

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_pairwise\_coprime\_cluster.md}.
\]

This records the clean strong-gate consequence of the same-layer and
cross-layer collision lemmas.

For \(j=0,1,2,3\), define
\[
  G_j=9m^2+t_0(j)^2,
  \qquad
  U_j=9m^2+t_1(j)^2+1.
\]

Assume \(m\ge21\), the first four blocks are coprime, \(m\) lies in a
no-same-layer-repetition class modulo \(70\), and \(m\) avoids the explicit
cross-layer collision congruences.  Then:
\[
\boxed{
  G_0,G_1,G_2,G_3,U_0,U_1,U_2,U_3
  \text{ are pairwise coprime.}
}
\]

The proof is exact:

- same-block coprimality is the A-block gcd formula;
- same-layer gcds would be same-layer repetitions, forbidden by the mod
  \(70\) gate;
- cross-layer gcds would satisfy
  \[
    p\mid t_1(j)^2+1-t_0(i)^2,
  \]
  hence are exactly the cross-layer collisions already listed.

Therefore, if the A-channel failed on the first four blocks in the clean
strong gate, the counterexample would force eight pairwise coprime composite
integers in a short interval near \(9m^2\).  Each would have a distinct prime
divisor \(p\le3m\).

The strong-gate closure target is now equivalent to excluding this
pairwise-coprime composite cluster.

## Initial factor-gap system

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_factor\_gap\_system.md}.
\]

This converts the clean strong-gate cluster into exact centered
factorizations.

Set
\[
  A=3m.
\]
For any candidate
\[
  N=A^2+c
\]
with \(0<c\le2A\), compositeness gives a factorization
\[
  N=(A-r)(A+s),
  \qquad r\ge1,\quad s\ge1.
\]
Since \(N>A^2\), one has \(s>r\).  Writing
\[
  e=s-r\ge1,
\]
gives the exact factor-gap equation
\[
  c=Ae-r(r+e).
\]
Equivalently,
\[
  w^2=e^2+4Ae-4c,
  \qquad w\equiv e\pmod2.
\]

For the first-four-block cluster, the offset sets are:
\[
  \mathcal C_{\rm even}=\{1,5,17,25,49,65,101,121\},
\]
\[
  \mathcal C_{\rm odd}=\{2,4,16,26,50,64,100,122\}.
\]
For \(m\ge21\), all these offsets satisfy \(c\le2A\).

Thus a clean strong-gate counterexample must solve, for every
\[
  c\in\mathcal C_{\rm parity(m)},
\]
the simultaneous equations
\[
  A^2+c=(A-r_c)(A+r_c+e_c),
\]
or
\[
  c=Ae_c-r_c(r_c+e_c),
\]
with the distinct small labels
\[
  p_c=A-r_c
\]
respecting the A0/A1 restrictions.

The remaining strong-gate obstruction is now a Diophantine system with one
shared center \(A=3m\) and eight fixed offsets.

## Initial center-divisor parametrization

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_center\_divisor\_parametrization.md}.
\]

This eliminates the cofactor gap \(e\) from the factor-gap system.

For
\[
  N=A^2+c,\qquad 0<c\le2A,
\]
and a divisor
\[
  d=A-r,
\]
one has
\[
  A\equiv r\pmod d.
\]
Therefore
\[
\boxed{
  A-r\mid A^2+c
  \quad\Longleftrightarrow\quad
  A-r\mid r^2+c.
}
\]

The old factor-gap equation
\[
  c=Ae-r(r+e)
\]
is equivalent to
\[
  r^2+c=e(A-r),
\]
so
\[
  e=\frac{r^2+c}{A-r}.
\]

Thus a clean strong-gate counterexample gives, for every offset
\[
  c\in\mathcal C_{\rm parity(m)},
\]
a distance
\[
  1\le r_c\le A-5
\]
such that
\[
  p_c=A-r_c
\]
is a distinct admissible prime and
\[
\boxed{
  p_c\mid r_c^2+c.
}
\]

The obstruction is now eight shifted-square divisibilities tied to the same
center \(A=3m\), rather than eight three-variable factorizations.

## Initial square-root barrier

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_sqrt\_barrier.md}.
\]

From the center-divisor condition
\[
  A-r\mid r^2+c,
\]
one gets
\[
  A-r\le r^2+c.
\]
Hence
\[
  r^2+r+c\ge A.
\]
Whenever \(A>c\),
\[
  r\ge
  \left\lceil
    \frac{-1+\sqrt{1+4(A-c)}}{2}
  \right\rceil.
\]

For the initial cluster, \(c_{\max}=122\).  Therefore, for \(A>122\), all
eight center distances satisfy the uniform barrier
\[
  r_c\ge
  \left\lceil
    \frac{-1+\sqrt{1+4(A-122)}}{2}
  \right\rceil.
\]
Equivalently, no prime label can lie in the top interval
\[
  A-R(A)<p\le A.
\]

The same note also records the quotient parametrization
\[
  r^2+c=e(A-r),
\]
or
\[
  A=r+\frac{r^2+c}{e},
  \qquad
  p=\frac{r^2+c}{e}.
\]

Thus a clean strong-gate counterexample must represent the same center \(A\)
eight times as
\[
  A=r_c+\frac{r_c^2+c}{e_c},
\]
with eight distinct admissible prime quotients.

## Initial pair-quotient compatibility

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_pair\_quotient\_compatibility.md}.
\]

For two offsets \(c\ne d\) sharing the same center \(A\), write
\[
  A=r_c+\frac{r_c^2+c}{e_c}
   =r_d+\frac{r_d^2+d}{e_d}.
\]
Let
\[
  h=r_d-r_c.
\]
Since
\[
  p_c=A-r_c,\qquad p_d=A-r_d,
\]
one has
\[
  p_c-p_d=h.
\]
Therefore
\[
  \frac{r_c^2+c}{e_c}
  -
  \frac{r_d^2+d}{e_d}
  =
  r_d-r_c.
\]
After clearing denominators:
\[
  e_d(r_c^2+c)-e_c(r_d^2+d)=e_ce_d(r_d-r_c).
\]
With \(r_d=r_c+h\), this becomes the binary quadratic compatibility equation
\[
  (e_d-e_c)r_c^2
  -2e_chr_c
  +e_dc-e_c(h^2+d)-e_ce_dh
  =0.
\]

If \(e_c=e_d=e\), this collapses to
\[
  c-d=h(r_c+r_d+e).
\]
Since distinct labels imply \(h\ne0\), this forces
\[
  r_c\le |c-d|-2.
\]

Both initial offset sets have maximum difference
\[
  D=120.
\]
Combining this with the square-root barrier gives:
\[
\boxed{
  m\ge4881
  \quad\Longrightarrow\quad
  e_c\ne e_d
  \text{ for all distinct initial offsets }c,d
}
\]
in the clean strong gate.

For \(e_c\ne e_d\), the compatibility equation gives a discriminant-square
condition:
\[
  e_c^2h^2
  -(e_d-e_c)
  \bigl(e_dc-e_c(h^2+d)-e_ce_dh\bigr)
  \text{ is a square.}
\]

The clean strong-gate obstruction is therefore stronger: for \(m\ge4881\),
the eight prime quotients and the eight quotient parameters \(e_c\) must both
be pairwise distinct, and every pair of offsets must satisfy this quadratic
compatibility.

## Initial order constraints

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_order\_constraints.md}.
\]

For fixed \(A\), define
\[
  F_c(r)=\frac{r^2+c}{A-r}.
\]
Then \(e_c=F_c(r_c)\).

The function \(F_c\) is strictly increasing in \(r\):
\[
  F_c(s)-F_c(r)
  =
  \frac{(s-r)\bigl(A(r+s)-rs+c\bigr)}
       {(A-r)(A-s)}
  >0
\]
for \(1\le r<s<A\).

It is also strictly increasing in \(c\):
\[
  F_d(r)-F_c(r)=\frac{d-c}{A-r}>0
\]
for \(c<d\).

Therefore, for two offsets \(c<d\),
\[
\boxed{
  r_c\le r_d
  \quad\Longrightarrow\quad
  e_c<e_d.
}
\]
Equivalently,
\[
\boxed{
  c<d,\ e_c>e_d
  \quad\Longrightarrow\quad
  r_c>r_d.
}
\]
Since \(p_c=A-r_c\), this also implies
\[
  c<d,\ e_c>e_d
  \quad\Longrightarrow\quad
  p_c<p_d.
\]

For \(m\ge4881\), the quotients are already known to be distinct, so they
define a permutation of the eight offsets.  The new order constraint is:
\[
  \operatorname{Inv}_e\subseteq\operatorname{Inv}_r.
\]

Thus the quotient permutation is not arbitrary.  Every quotient inversion
must be matched by a distance inversion and by the opposite prime-label
ordering.

## Initial quotient-rank barrier

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_quotient\_rank\_barrier.md}.
\]

For \(m\ge4881\), the clean strong gate has eight distinct positive quotients
\[
  e_c.
\]
Ordering them as
\[
  e_{(1)}<e_{(2)}<\cdots<e_{(8)},
\]
one has
\[
  e_{(k)}\ge k.
\]

For each quotient, the center equation is
\[
  r^2+er+c=eA.
\]
Since every initial offset satisfies \(c\le122\), this gives the uniform
ranked lower bound
\[
  r_{(k)}\ge
  B_k(A):=
  \left\lceil
  \frac{-k+\sqrt{k^2+4(kA-122)}}{2}
  \right\rceil.
\]

Thus the prime labels ordered by quotient rank satisfy
\[
  p_{(k)}=A-r_{(k)}\le A-B_k(A).
\]

In particular, the largest quotient forces
\[
  r_{(8)}\ge
  \left\lceil
  \frac{-8+\sqrt{32A-424}}{2}
  \right\rceil.
\]

So the eight labels do not merely avoid the top \(\sqrt A\)-window: the
quotient ranks impose progressively deeper exclusion windows below \(A\).

## Initial rank-position coupling

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_rank\_position\_coupling.md}.
\]

Let the offsets be ordered as
\[
  c_1<\cdots<c_8.
\]
Let
\[
  q_i=\operatorname{rank}(e_{c_i})
\]
be the quotient rank at offset position \(i\), and
\[
  s_i=\operatorname{rank}(r_{c_i})
\]
be the corresponding distance rank.

For \(m\ge4881\), both are permutations of \(\{1,\dots,8\}\).  The order
constraint gives
\[
  \operatorname{Inv}(q)\subseteq\operatorname{Inv}(s).
\]

If
\[
  q_i=k,
\]
then the inversion constraint forces the exact band
\[
\boxed{
  \max(1,k-i+1)
  \le
  s_i
  \le
  \min(8,8+k-i).
}
\]

In particular, for the largest quotient rank \(k=8\), if it occurs at offset
position \(i\), then
\[
\boxed{
  s_i\ge9-i.
}
\]
At the same time, the quotient-rank barrier gives
\[
  r_{c_i}\ge
  \left\lceil
  \frac{-8+\sqrt{32A-424}}{2}
  \right\rceil.
\]

Thus the "last-rank" label must be both far from \(A\) and sufficiently late
in the distance order.  The next obstruction is now finite and combinatorial:
rule out all rank placements compatible with the rank-position band, the
rank barriers, and the prime-label congruence restrictions.

## Initial label order-statistic barrier

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_label\_order\_statistic\_barrier.md}.
\]

Let the eight center distances be sorted increasingly:
\[
  R_1<\cdots<R_8.
\]
The quotient-rank barriers form the increasing sequence
\[
  B_k(A)=
  \left\lceil
  \frac{-k+\sqrt{k^2+4(kA-122)}}{2}
  \right\rceil.
\]

Since the quotient ranks are exactly \(1,\dots,8\), at most \(j-1\) distances
can lie below \(B_j(A)\).  Hence
\[
\boxed{
  R_j\ge B_j(A)
  \qquad(1\le j\le8).
}
\]

If the eight prime labels are sorted increasingly
\[
  P_1<\cdots<P_8,
\]
then \(P_j=A-R_{9-j}\), so
\[
\boxed{
  P_j\le A-B_{9-j}(A)
  \qquad(1\le j\le8).
}
\]

Equivalently, for every \(k\), at least \(9-k\) labels satisfy
\[
  p\le A-B_k(A).
\]

Thus the last-rank barrier is part of a full lower-tail constraint:
\[
  P_1\le A-B_8(A),\quad
  P_2\le A-B_7(A),\quad\dots,\quad
  P_8\le A-B_1(A).
\]

The next exact target is to combine this lower-tail requirement with the A0
condition \(p\equiv1\pmod4\) and the offset-specific congruence restrictions.

## Initial A0 tail constraints

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_A0\_tail\_constraints.md}.
\]

Let the four A0 labels be sorted increasingly:
\[
  Q_1<Q_2<Q_3<Q_4.
\]
Since there are only four A1 labels, among the first \(j+4\) global labels
there must be at least \(j\) A0 labels.  Therefore
\[
  Q_j\le P_{j+4}.
\]
Using the global label order-statistic barrier
\[
  P_\ell\le A-B_{9-\ell}(A)
\]
gives
\[
\boxed{
  Q_j\le A-B_{5-j}(A)
  \qquad(1\le j\le4).
}
\]

Explicitly:
\[
  Q_1\le A-B_4(A),\quad
  Q_2\le A-B_3(A),\quad
  Q_3\le A-B_2(A),\quad
  Q_4\le A-B_1(A).
\]

Each A0 label also satisfies
\[
  Q_j\equiv1\pmod4.
\]
In distance form, with \(Q_j=A-\rho_j\), this is
\[
  \rho_j\equiv A-1\pmod4.
\]

Thus the A0 layer must supply four distances in one fixed residue class
modulo \(4\), with the forced ordered lower-tail profile
\[
  B_4(A),B_3(A),B_2(A),B_1(A).
\]

## Initial A0 spacing envelope

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_A0\_spacing\_envelope.md}.
\]

Let the A0 labels be sorted increasingly:
\[
  Q_1<Q_2<Q_3<Q_4,
\]
and write
\[
  Q_j=A-\rho_j.
\]
Then
\[
  \rho_1>\rho_2>\rho_3>\rho_4.
\]
All A0 labels satisfy \(Q_j\equiv1\pmod4\), hence
\[
  \rho_j\equiv A-1\pmod4.
\]

Since the four distances are distinct and congruent modulo \(4\),
\[
  \rho_j\ge \rho_\ell+4(\ell-j)
  \qquad(1\le j<\ell\le4).
\]

Combining this with the A0 tail bounds
\[
  \rho_\ell\ge B_{5-\ell}(A)
\]
gives the exact strengthened envelope
\[
\boxed{
  \rho_j\ge
  E_j(A):=
  \max_{j\le\ell\le4}
  \left(B_{5-\ell}(A)+4(\ell-j)\right).
}
\]

Equivalently,
\[
  Q_j\le A-E_j(A).
\]

Thus the A0 layer must satisfy the Gaussian divisor equations inside one
fixed residue class modulo \(4\), with a spacing-refined lower-tail profile.

## Initial A1 spacing envelope

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_A1\_spacing\_envelope.md}.
\]

Let the A1 labels be sorted increasingly:
\[
  S_1<S_2<S_3<S_4.
\]
The same pigeonhole projection gives
\[
  S_j\le P_{j+4},
\]
and hence
\[
  S_j\le A-B_{5-j}(A).
\]

Writing
\[
  S_j=A-\sigma_j,
\]
the A1 labels are odd primes, so
\[
  \sigma_j\equiv A-1\pmod2.
\]
Since the four \(\sigma_j\) are distinct and congruent modulo \(2\),
\[
  \sigma_j\ge\sigma_\ell+2(\ell-j)
  \qquad(1\le j<\ell\le4).
\]

Combining with the tail bounds gives
\[
\boxed{
  \sigma_j\ge
  F_j(A):=
  \max_{j\le\ell\le4}
  \left(B_{5-\ell}(A)+2(\ell-j)\right).
}
\]

Thus the A1 layer must satisfy its own parity-spaced lower-tail envelope and
the four divisor equations
\[
  A-\sigma_j\mid \sigma_j^2+y^2+1.
\]

The next exact obstruction is to interleave the A0 spacing envelope and A1
spacing envelope under the cross-layer compatibility equations.

## Initial two-layer ladder certificate

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_two\_layer\_ladder\_certificate.md}.
\]

The separate A0/A1 envelopes can be fused.  In the clean strong gate, all
eight prime labels are odd, so if
\[
  P_j=A-D_j,\qquad P_1<\cdots<P_8,
\]
then
\[
  D_1>\cdots>D_8,
  \qquad
  D_j\equiv A-1\pmod2.
\]
Therefore
\[
\boxed{
  D_i\ge D_j+2(j-i)
  \qquad(1\le i<j\le8).
}
\]

For a fixed layer word
\[
  L\in\{0,1\}^8
\]
with four A0 and four A1 positions, consecutive A0 positions add stronger
edges of weight \(4\), because A0 labels are \(1\bmod4\).  Let \(W_L(i,j)\)
be the maximum path weight generated by the global parity edges of weight
\(2\) and the A0 edges of weight \(4\).  Then
\[
\boxed{
  D_i\ge
  H_i^L(A):=
  \max_{i\le j\le8}
  \left(B_{9-j}(A)+W_L(i,j)\right).
}
\]

The offset order is fixed by the parity of \(m\).  A counterexample must
choose a layer-respecting matching \(\pi\) from the eight offsets to the
eight label positions.  If \(r_i=D_{\pi(i)}\), then its distance rank is
\[
  s_i=9-\pi(i).
\]

For \(m\ge4881\), the quotient ranks \(q_i\) are distinct and must satisfy
\[
\boxed{
  \operatorname{Inv}(q)\subseteq\operatorname{Inv}(s).
}
\]
Each offset must also satisfy
\[
\boxed{
  D_{\pi(i)}
  \ge
  \max\{H_{\pi(i)}^L(A),\,B_{q_i}(A)\},
}
\]
and the exact centered divisor equation
\[
\boxed{
  A-D_{\pi(i)}\mid D_{\pi(i)}^2+c_i.
}
\]

For every pair of offsets, the shared center forces the pair-compatibility
equation
\[
\boxed{
  e_j(D_{\pi(i)}^2+c_i)
  -
  e_i(D_{\pi(j)}^2+c_j)
  =
  e_ie_j(D_{\pi(j)}-D_{\pi(i)}).
}
\]

Thus the clean strong gate is no longer an open search over \(m\).  It is a
finite family of exact two-layer ladder certificates: layer word, matching,
quotient-rank permutation, distances, quotients, and pairwise compatibility.
The next closure target is to eliminate these certificates structurally.

## Initial quotient Pell pencil

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_quotient\_pell\_pencil.md}.
\]

This is the next nonstandard attack: make the quotient \(e\), not the center
\(A\), the primary variable.

The centered equation
\[
  c=Ae-r(r+e)
\]
is equivalent, with
\[
  w=2r+e,
\]
to the square-line equation
\[
\boxed{
  w^2=4eA+e^2-4c.
}
\]

Since \(A=3m\), every quotient must satisfy the local congruence
\[
\boxed{
  w^2\equiv e^2-4c\pmod{12e}.
}
\]

Thus, before choosing any center \(A\), the pair \((c,e)\) must pass a local
square test modulo \(12e\).  In particular, if an odd prime \(\ell\mid e\)
does not divide \(c\), then
\[
\boxed{
  \left(\frac{-c}{\ell}\right)=1.
}
\]

For A0 offsets \(c=x^2\), this becomes
\[
\boxed{
  \ell\equiv1\pmod4
}
\]
for every odd quotient prime \(\ell\nmid x\).  Therefore the hidden quotient
side of an A0 factorization is also Gaussian, not just the visible prime
label side.

For A1 offsets \(c=y^2+1\), every non-degenerate odd quotient prime must
satisfy
\[
\boxed{
  \left(\frac{-(y^2+1)}{\ell}\right)=1.
}
\]

Finally, eliminating \(A\) between two offsets gives the Pell-type
synchronization equation
\[
\boxed{
  e_jw_i^2-e_iw_j^2
  =
  e_ie_j(e_i-e_j)
  -4(e_jc_i-e_ic_j).
}
\]

The clean strong gate now has a quotient-first closure target: eliminate
eight distinct quotients \(e_i\) satisfying the quotient-local splitting
conditions, the two-layer ladder restrictions, and the \(28\) pairwise Pell
synchronization equations.  This avoids a center-by-center search over
\(m\).

## Initial even quotient lift

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_even\_quotient\_lift.md}.
\]

This extracts the \(2\)-adic consequence of the initial offset parities.
If \(m\) is even, then \(A\) is even and all initial offsets are odd.  If
\(m\) is odd, then \(A\) is odd and all initial offsets are even.  In both
cases
\[
  A^2+c
\]
is odd for all eight initial offsets.

The centered factorization
\[
  A^2+c=(A-r)(A+r+e)
\]
therefore has two odd factors.  Hence
\[
\boxed{
  e\equiv0\pmod2.
}
\]

Thus every initial quotient is even.  For \(m\ge4881\), the eight quotients
are distinct, so their increasing order satisfies
\[
\boxed{
  e_{(k)}\ge2k
  \qquad(1\le k\le8).
}
\]

This doubles the quotient-rank barrier.  Define
\[
\boxed{
  \widetilde B_k(A)=
  \left\lceil
    -k+\sqrt{k^2+2kA-122}
  \right\rceil.
}
\]

Then an offset carrying quotient rank \(k\) satisfies
\[
\boxed{
  r\ge\widetilde B_k(A).
}
\]

The largest quotient rank gives
\[
\boxed{
  r\ge
  \widetilde B_8(A)
  =
  \left\lceil -8+\sqrt{16A-58}\right\rceil.
}
\]

Therefore the smallest prime label in a clean strong-gate counterexample
must satisfy
\[
\boxed{
  P_1\le
  A-\left\lceil -8+\sqrt{16A-58}\right\rceil.
}
\]

This is the first genuinely stronger tail barrier after the quotient Pell
pencil: the initial cluster must contain an admissible prime label around
\[
  A-4\sqrt A,
\]
not merely around \(A-\sqrt{8A}\).  The two-layer ladder certificate should
now use the lifted barriers \(\widetilde B_k(A)\) everywhere a quotient rank
barrier is invoked.

## Initial mod-6 quotient lattice

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_mod6\_quotient\_lattice.md}.
\]

This strengthens the even quotient lift by using the \(3\)-adic part of the
reduced quotient pencil.  Write
\[
  e=2f.
\]
Then
\[
\boxed{
  (r+f)^2=f^2+6mf-c.
}
\]

Modulo \(3\),
\[
\boxed{
  (r+f)^2\equiv f^2-c\pmod3.
}
\]

For A0 offsets, \(c=x^2\) and \(3\nmid x\), so
\[
  c\equiv1\pmod3.
\]
Thus \(3\mid f\) would force
\[
  f^2-c\equiv2\pmod3,
\]
impossible.  Therefore
\[
\boxed{
  \mathrm{A0}:\quad e\equiv2,4\pmod6.
}
\]

For A1 offsets, \(c=y^2+1\) and \(3\nmid y\), so
\[
  c\equiv2\pmod3.
\]
Thus \(3\nmid f\) would force
\[
  f^2-c\equiv2\pmod3,
\]
impossible.  Therefore
\[
\boxed{
  \mathrm{A1}:\quad e\equiv0\pmod6.
}
\]

The four A0 quotients have ordered minima
\[
  2,4,8,10,
\]
while the four A1 quotients have ordered minima
\[
  6,12,18,24.
\]
Hence the global quotient tuple satisfies the componentwise bound
\[
\boxed{
  e_{(1)},\dots,e_{(8)}
  \ge
  2,4,6,8,10,12,18,24.
}
\]

With
\[
  M=(2,4,6,8,10,12,18,24),
\]
define
\[
\boxed{
  \widehat B_k(A):=
  \left\lceil
    \frac{-M_k+\sqrt{M_k^2+4(M_kA-122)}}{2}
  \right\rceil.
}
\]

Then quotient rank \(k\) forces
\[
\boxed{
  r\ge\widehat B_k(A).
}
\]

In particular,
\[
\boxed{
  r\ge
  \widehat B_8(A)
  =
  \left\lceil -12+\sqrt{24A+22}\right\rceil.
}
\]

So the smallest prime label in the clean strong gate must now lie around
\[
  A-\sqrt{24A},
\]
which is sharper than the even-only \(A-4\sqrt A\) barrier.  This is an
exact layer-sensitive obstruction on the quotient lattice.

## Initial A0 mod-12 colored ladder

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_A0\_mod12\_colored\_ladder.md}.
\]

This continues the quotient-side attack without searching over \(m\).  For
A0 offsets, write
\[
  e=2f,\qquad c=x^2.
\]
The reduced quotient pencil gives
\[
\boxed{
  (r+f)^2=f^2+6mf-x^2.
}
\]

Modulo \(3\), since \(3\nmid f\) and \(3\nmid x\),
\[
  f^2\equiv x^2\equiv1\pmod3,
\]
so
\[
  r+f\equiv0\pmod3.
\]
Thus
\[
\boxed{
  p=A-r\equiv f\pmod3.
}
\]

Together with \(p\equiv1\pmod4\), this gives
\[
\boxed{
  e\equiv2\pmod6
  \Rightarrow
  p\equiv1\pmod{12},
}
\]
and
\[
\boxed{
  e\equiv4\pmod6
  \Rightarrow
  p\equiv5\pmod{12}.
}
\]

Therefore the hidden A0 quotient color controls the visible A0 label class.
If two A0 labels have the same quotient color, their distances are congruent
modulo \(12\), hence distinct ordered distances are spaced by at least
\[
  12.
\]

The two-layer ladder certificate should now carry an A0 color word
\[
  \chi\in\{2,4\}^4.
\]
Its graph has the global parity edges, the ordinary A0 modulo-\(4\) edges,
and additional same-color A0 edges of weight \(12\).  With
\[
  W_{L,\chi}(i,j)
\]
the maximum path weight, the colored envelope is
\[
\boxed{
  H_i^{L,\chi}(A)=
  \max_{i\le j\le8}
  \left(\widehat B_{9-j}(A)+W_{L,\chi}(i,j)\right).
}
\]

The next exact target is to eliminate these colored two-layer ladder
certificates, not by testing centers but by showing that their spacing,
quotient-rank, and Pell synchronization equations are incompatible.

## Initial A1 mod-6 signed ladder

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_A1\_mod6\_signed\_ladder.md}.
\]

This is the A1 analogue of the A0 colored ladder.  For A1, write
\[
  e=2f,\qquad c=y^2+1.
\]
The mod-\(6\) quotient lattice gives
\[
  3\mid f.
\]
Since the initial A1 coordinate satisfies \(3\nmid y\), one has
\[
  y^2+1\equiv2\pmod3.
\]
The reduced quotient pencil gives
\[
\boxed{
  (r+f)^2=f^2+6mf-(y^2+1).
}
\]
Modulo \(3\), this becomes
\[
\boxed{
  (r+f)^2\equiv1\pmod3.
}
\]

Therefore
\[
\boxed{
  r+f\equiv\varepsilon\pmod3,
  \qquad
  \varepsilon\in\{1,-1\}.
}
\]
Since \(f\equiv0\pmod3\),
\[
\boxed{
  r\equiv\varepsilon\pmod3.
}
\]

The prime label \(p=A-r\) satisfies
\[
\boxed{
  p\equiv-\varepsilon\pmod3.
}
\]
As \(p\) is odd, the sign determines the label class modulo \(6\):
\[
\boxed{
  \varepsilon=1\Rightarrow p\equiv5\pmod6,
}
\]
and
\[
\boxed{
  \varepsilon=-1\Rightarrow p\equiv1\pmod6.
}
\]

Thus equal A1 signs force equal distance classes modulo \(6\), so ordered
same-sign A1 distances are spaced by at least \(6\).  The fully colored
ladder now carries A0 quotient colors and A1 root signs.  Its envelope is
\[
\boxed{
  H_i^{L,\chi,\varepsilon}(A)
  =
  \max_{i\le j\le8}
  \left(\widehat B_{9-j}(A)+W_{L,\chi,\varepsilon}(i,j)\right).
}
\]

The next exact closure target is to eliminate fully colored ladder
certificates with A0 colors, A1 signs, quotient-rank constraints, centered
divisor equations, and pairwise Pell synchronization.

## Initial colored quotient-rank forcing

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_colored\_quotient\_rank\_forcing.md}.
\]

The quotient permutation \(q\) is no longer treated as an abstract global
permutation.  It must respect the mod-\(6\) quotient lattice inside each
layer and, for A0, inside each color.

For A0, with color
\[
  \chi_i\in\{2,4\},
\]
define the same-color quotient rank
\[
\boxed{
  \kappa_i
  =
  1+
  \#\{j:\ j\text{ is A0},\ \chi_j=\chi_i,\ q_j<q_i\}.
}
\]
Then
\[
\boxed{
  e_i\ge \chi_i+6(\kappa_i-1).
}
\]

For A1, define the A1-layer quotient rank
\[
\boxed{
  \lambda_i
  =
  1+
  \#\{j:\ j\text{ is A1},\ q_j<q_i\}.
}
\]
Since A1 quotients are positive multiples of \(6\),
\[
\boxed{
  e_i\ge6\lambda_i.
}
\]

Combining these with the global quotient lattice
\[
  M=(2,4,6,8,10,12,18,24)
\]
gives an offset-specific lower bound
\[
\boxed{
  e_i\ge E_i(q,\chi).
}
\]

Therefore
\[
\boxed{
  r_i\ge
  \mathcal B_{E_i(q,\chi)}(A),
}
\]
where
\[
\boxed{
  \mathcal B_E(A)
  =
  \left\lceil
    \frac{-E+\sqrt{E^2+4(EA-122)}}{2}
  \right\rceil.
}
\]

If \(\pi(i)\) is the label position of offset \(i\), then the fully colored
certificate must satisfy
\[
\boxed{
  D_{\pi(i)}
  \ge
  \max\left\{
    H_{\pi(i)}^{L,\chi,\varepsilon}(A),
    \mathcal B_{E_i(q,\chi)}(A)
  \right\}.
}
\]

The next exact target is now sharper: eliminate fully colored ladder
certificates with colored quotient-rank forcing, while preserving
\[
  \operatorname{Inv}(q)\subseteq\operatorname{Inv}(s)
\]
and the pairwise Pell synchronization equations.

## Initial A0 cofactor mirror

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_A0\_cofactor\_mirror.md}.
\]

This is a corrected closure-oriented use of the complementary factor.  For A0,
\[
  A^2+x^2=(A-r)(A+r+e).
\]
The small factor
\[
  A-r
\]
is an A0 label, hence
\[
  A-r\equiv1\pmod4.
\]
Also
\[
  A^2+x^2\equiv1\pmod4
\]
in the initial cluster.  Therefore the complementary factor satisfies
\[
\boxed{
  A+r+e\equiv1\pmod4.
}
\]
Subtracting the two factors gives
\[
\boxed{
  2r+e\equiv0\pmod4.
}
\]

This is the correct mirror congruence.  Since
\[
  A-r\equiv1\pmod4,
\]
one has
\[
  r\equiv A-1\pmod4.
\]
Therefore the consequence depends on the parity of \(m\).

If \(m\) is even, then \(A\) is even and \(r\) is odd.  Thus
\[
  e\equiv2\pmod4.
\]
Combined with the mod-\(6\) quotient lattice
\[
  \mathrm{A0}:\quad e\equiv2,4\pmod6,
\]
this gives
\[
\boxed{
  m\text{ even},\ \mathrm{A0}:\quad e\equiv2,10\pmod{12}.
}
\]

If \(m\) is odd, then \(A\) is odd and \(r\) is even.  Thus
\[
  e\equiv0\pmod4,
\]
and hence
\[
\boxed{
  m\text{ odd},\ \mathrm{A0}:\quad e\equiv4,8\pmod{12}.
}
\]

Thus the A0 color is parity-bifurcated from
\[
  \chi\in\{2,4\}\pmod6
\]
to
\[
\boxed{
  \gamma\in\{2,10\}\pmod{12}\quad(m\text{ even}),
  \qquad
  \gamma\in\{4,8\}\pmod{12}\quad(m\text{ odd}).
}
\]

For same-color A0 rank
\[
  \kappa_i
  =
  1+
  \#\{j:\ j\text{ A0},\ \gamma_j=\gamma_i,\ q_j<q_i\},
\]
one now has
\[
\boxed{
  e_i\ge \gamma_i+12(\kappa_i-1).
}
\]

For even \(m\), the four A0 quotient minima are
\[
  2,10,14,22,
\]
and the global quotient tuple satisfies
\[
\boxed{
  e_{(1)},\dots,e_{(8)}
  \ge
  2,6,10,12,14,18,22,24.
}
\]

For odd \(m\), the four A0 quotient minima are
\[
  4,8,16,20,
\]
and the global quotient tuple satisfies
\[
\boxed{
  e_{(1)},\dots,e_{(8)}
  \ge
  4,6,8,12,16,18,20,24.
}
\]

Thus the cofactor mirror does not universally remove \(e=2\).  It instead
splits the clean strong-gate quotient skeleton into even and odd branches.
The corrected cofactor-mirrored bound is
\[
\boxed{
  e_i\ge E_i^\parity(q,\gamma),
}
\]
and hence
\[
\boxed{
  r_i\ge \mathcal B_{E_i^\parity(q,\gamma)}(A).
}
\]

This is a genuine closure path: it attacks both centered factors, not just
the small prime label, but it must be handled in two parity branches with
their own fully colored ladder and Pell synchronization equations.

## Initial A1 cofactor mirror

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_A1\_cofactor\_mirror.md}.
\]

This is the strongest cofactor-mirror gain so far.  For A1,
\[
  A^2+y^2+1=(A-r)(A+r+e).
\]
Let
\[
  p=A-r,\qquad Q=A+r+e.
\]
Then
\[
  Q-p=2r+e.
\]

If \(m\) is even, then \(A\) and the A1 coordinate \(y\) are even, so
\[
  A^2+y^2+1\equiv1\pmod4.
\]
Thus \(Q\equiv p\pmod4\), hence \(2r+e\equiv0\pmod4\).  Since \(r\) is odd,
\[
  e\equiv2\pmod4.
\]

If \(m\) is odd, then \(A\) and \(y\) are odd, so
\[
  A^2+y^2+1\equiv3\pmod4.
\]
The two odd factors have opposite classes modulo \(4\), hence
\[
  2r+e\equiv2\pmod4.
\]
Since \(r\) is even, again
\[
  e\equiv2\pmod4.
\]

Therefore A1 has the uniform cofactor mirror
\[
\boxed{
  \mathrm{A1}:\quad e\equiv2\pmod4.
}
\]

Together with the mod-\(6\) quotient lattice
\[
  \mathrm{A1}:\quad e\equiv0\pmod6,
\]
this gives
\[
\boxed{
  \mathrm{A1}:\quad e\equiv6\pmod{12}.
}
\]

So the four A1 quotient minima are no longer
\[
  6,12,18,24,
\]
but
\[
\boxed{
  6,18,30,42.
}
\]

Combining with the corrected A0 cofactor mirror gives the parity-bifurcated
cofactor quotient skeletons
\[
\boxed{
  M^{\mathrm{even},\mathrm{cof}}
  =
  (2,6,10,14,18,22,30,42),
}
\]
and
\[
\boxed{
  M^{\mathrm{odd},\mathrm{cof}}
  =
  (4,6,8,16,18,20,30,42).
}
\]

Thus
\[
  e_{(8)}\ge42,
\]
so the largest-rank distance barrier is asymptotic to
\[
  \sqrt{42A}.
\]
At least one clean strong-gate label must lie below approximately
\[
  A-\sqrt{42A}.
\]

This is the first quotient skeleton rigid enough to be a plausible closure
mechanism: eliminate the even and odd cofactor-mirrored certificates with
A1 restricted to \(6\bmod12\), together with colored ladders and Pell
synchronization.

## Initial odd A1 mod-24 lift

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_odd\_A1\_mod24\_lift.md}.
\]

This sharpens the A1 cofactor mirror in the odd branch.  Write
\[
  e=2f.
\]
The reduced A1 equation is
\[
\boxed{
  u^2=f^2+6mf-(y^2+1),
  \qquad
  u=r+f.
}
\]

The A1 cofactor mirror gives
\[
  f\equiv3\pmod6.
\]

If \(m\) is odd, then the initial A1 coordinate \(y\) is odd, so
\[
  y^2\equiv1\pmod8.
\]
Also \(f\) is odd, so \(f^2\equiv1\pmod8\).  Reducing modulo \(8\) gives
\[
  u^2\equiv6mf-1\pmod8.
\]
Since an odd square is \(1\bmod8\), one must have
\[
\boxed{
  mf\equiv3\pmod4.
}
\]

Thus
\[
\boxed{
  f\equiv3m\pmod4.
}
\]

Combining with \(f\equiv3\pmod6\):
\[
\boxed{
  m\equiv1\pmod4
  \Rightarrow
  \mathrm{A1}:\ e\equiv6\pmod{24},
}
\]
and
\[
\boxed{
  m\equiv3\pmod4
  \Rightarrow
  \mathrm{A1}:\ e\equiv18\pmod{24}.
}
\]

For \(m\equiv1\pmod4\), the odd-branch quotient skeleton becomes
\[
\boxed{
  M^{1\bmod4}=(4,6,8,16,20,30,54,78).
}
\]

For \(m\equiv3\pmod4\), it becomes
\[
\boxed{
  M^{3\bmod4}=(4,8,16,18,20,42,66,90).
}
\]

So the largest quotient-rank lower bound in the odd branch is now
\[
  78
  \quad\text{or}\quad
  90,
\]
not \(42\).  This pushes the strongest label exclusion window to roughly
\[
  A-\sqrt{78A}
  \quad\text{or}\quad
  A-\sqrt{90A}.
\]

This is a genuine closure path for the odd clean strong gate: the A1
quotient lattice becomes sparse enough that the fully colored Pell
certificate may be impossible to realize.

## Initial even mod-8 quotient lift

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_even\_mod8\_quotient\_lift.md}.
\]

This is the even-branch analogue of the odd mod-\(24\) lift.  For even \(m\),
the initial A0 coordinates are
\[
  1,5,7,11,
\]
and the A1 coordinates are
\[
  2,4,8,10.
\]

Write
\[
  e=2f,\qquad u=r+f.
\]
Since \(A\) is even, all labels are odd and \(r\) is odd.  The quotient
classes make \(f\) odd, so \(u\) is even and
\[
  u^2\equiv0\text{ or }4\pmod{16}.
\]

For A1,
\[
  u^2=f^2+6mf-(y^2+1),
  \qquad
  f\equiv3\pmod6.
\]
The exact modulo-\(16\) table gives A1 quotient minima:
\[
\boxed{
\begin{array}{c|c}
  m\bmod8 & \text{A1 quotient minima}\\
  \hline
  0 & 6,\ 18,\ 30,\ 42\\
  2 & 30,\ 42,\ 78,\ 90\\
  4 & 6,\ 18,\ 30,\ 42\\
  6 & 6,\ 18,\ 54,\ 66
\end{array}
}
\]

For A0, the modulo-\(16\) table preserves the A0 minima
\[
  2,\ 10,\ 14,\ 22
\]
in every even class, while assigning allowed \(e\bmod48\) classes to the
individual coordinate types \(x^2\equiv1,9\pmod{16}\).

Combining A0 and A1 yields:
\[
\boxed{
\begin{array}{c|c}
  m\bmod8 & \text{global quotient minima}\\
  \hline
  0 & 2,\ 6,\ 10,\ 14,\ 18,\ 22,\ 30,\ 42\\
  2 & 2,\ 10,\ 14,\ 22,\ 30,\ 42,\ 78,\ 90\\
  4 & 2,\ 6,\ 10,\ 14,\ 18,\ 22,\ 30,\ 42\\
  6 & 2,\ 6,\ 10,\ 14,\ 18,\ 22,\ 54,\ 66
\end{array}
}
\]

Thus the clean strong gate now splits into six exact quotient skeletons:
four even classes modulo \(8\), plus the two odd classes modulo \(4\).  The
strongest cases force
\[
  e_{(8)}\ge90.
\]

The next exact target is to stop increasing \(e\)-barriers globally and
eliminate these six skeletons one by one with the colored ladder and Pell
synchronization equations.

## Initial odd A0 mod-16 lift

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_initial\_odd\_A0\_mod16\_lift.md}.
\]

This closes one remaining \(e\)-refinement in the odd branch.  For A0,
\[
  u^2=f^2+6mf-x^2,
  \qquad
  e=2f.
\]

In the odd branch, the A0 coordinates are
\[
  2,4,8,10,
\]
so \(x^2\equiv0\) or \(4\bmod16\).  The corrected A0 cofactor mirror gives
\[
  e\equiv4\text{ or }8\pmod{12}.
\]
Reducing the half-quotient equation modulo \(16\) gives the exact table
recorded in the note.

For \(m\equiv1\pmod4\), the A0 minima remain
\[
  4,8,16,20,
\]
and the global skeleton remains
\[
\boxed{
  M^{1\bmod4}=(4,6,8,16,20,30,54,78).
}
\]

For \(m\equiv3\pmod4\), the A0 minima sharpen to
\[
  4,8,16,28,
\]
and the global skeleton becomes
\[
\boxed{
  M^{3\bmod4}_{\mathrm{sharp}}
  =
  (4,8,16,18,28,42,66,90).
}
\]

Thus the quotient-refinement phase has a finite exact endpoint:
\[
\boxed{
\begin{array}{c|c}
  \text{residue branch} & \text{global quotient minima}\\
  \hline
  m\equiv0\pmod8 & 2,6,10,14,18,22,30,42\\
  m\equiv2\pmod8 & 2,10,14,22,30,42,78,90\\
  m\equiv4\pmod8 & 2,6,10,14,18,22,30,42\\
  m\equiv6\pmod8 & 2,6,10,14,18,22,54,66\\
  m\equiv1\pmod4 & 4,6,8,16,20,30,54,78\\
  m\equiv3\pmod4 & 4,8,16,18,28,42,66,90
\end{array}
}
\]

This does not close Legendre.  It marks the point where further progress
must come from eliminating the six skeletons by Pell synchronization and
colored ladder incompatibility, not by adding more isolated \(e\)-barriers.

## Literature strategy reset

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_literature\_strategy\_reset.md}.
\]

This is a deliberate pause after the quotient-skeleton phase.

The current route has produced a precise certificate language but not a
contradiction.  Known short-interval prime technology remains above the
Legendre threshold: the interval length is
\[
  (n+1)^2-n^2\asymp x^{1/2},
  \qquad x=n^2,
\]
while unconditional prime-gap technology still needs an exponent strictly
larger than \(1/2\).  Recent Guth-Maynard Dirichlet-polynomial methods are
major progress, but still do not directly give Legendre.

Modern almost-prime results are much closer structurally: there are now
explicit theorems placing a \(P_3\) in every interval between consecutive
squares.  But pure sieve methods hit the parity problem, so a direct
almost-prime proof does not become a prime proof without an additional
prime-detecting mechanism.

Therefore the current recommended pivot is:

1. treat the quotient skeletons as a finite certificate language;
2. stop refining isolated \(e\)-congruences;
3. try to eliminate one skeleton, beginning with
   \[
     m\equiv3\pmod4,\quad
     M=(4,8,16,18,28,42,66,90),
   \]
   using the pairwise Pell synchronization equations;
4. if this fails, pivot to an almost-prime-to-prime upgrade, using the
   quotient certificates as the obstruction language.

This note explicitly downgrades the previous route from "proof path" to
"certificate framework until a Pell contradiction is found."

## Literature pack

Added
\[
  \texttt{Math/conjecture/legendre/literature/}.
\]

The folder contains:

- `README.md`: reading map and proof-use notes;
- `arxiv_manifest.tsv`: arXiv IDs, abstracts links, PDF links, and roles;
- `references.bib`: BibTeX entries for the current Legendre bibliography.

PDFs are intentionally not committed at this stage.  The repository stores
metadata and source links first, because journal PDFs may be copyrighted and
arXiv papers have paper-specific licenses.

## P3 terminal descent target

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_p3\_terminal\_descent.md}.
\]

This is the first exact attempt to turn the modern \(P_3\)-between-squares
theorem into a possible Legendre closure route without pretending that a
sieve almost-prime theorem is already a prime theorem.

If \(I_n=(n^2,(n+1)^2)\) is prime-free but contains a \(P_3\) integer \(N\),
then \(N\) is composite.  Choosing \(N=dD\) with \(d\le\sqrt N<D\) gives
\[
  1<d\le n<D,
  \qquad
  \Omega(d)+\Omega(D)\le3.
\]

Writing
\[
  d=n-a,\qquad D=n+a+k
\]
gives the exact terminal equation
\[
  N=(n-a)(n+a+k),
  \qquad
  1\le nk-a(a+k)\le2n.
\]

The obstruction splits into:

- \(T1\): \(k=1\), with \(0\le a(a+1)\le n-1\);
- \(T2\): \(k=2\), with \(0\le a(a+2)\le2n-1\);
- \(Tfar\): \(k\ge3\), with
  \[
    n(k-2)\le a(a+k)\le nk-1.
  \]

The new closure target is a descent lemma: in a minimal Legendre
counterexample, eliminate T1 and T2 terminal \(P_3\) survivors, then use the
forced \(Tfar\) factor drop to descend from \(n\) to a smaller
between-squares obstruction.

## P3 weighted terminal correction

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_p3\_weighted\_terminal\_gap.md}.
\]

This corrects the first terminal-descent target.  The geometry-only
near-diagonal lemma is too strong: T1 contains the always-admissible formal
terminal value
\[
  N=n(n+1)
\]
from \(a=0,k=1\).  Thus T1/T2 elimination cannot follow from terminal factor
geometry alone.

The corrected closure target is weighted.  Under a prime-free assumption,
Campbell's \(P_3\) lower bound must be entirely accounted for by terminal
composites, so one needs a strict inequality of the form
\[
  W_{\mathrm{T1}}(n)+W_{\mathrm{T2}}(n)+W_{\mathrm{Tfar}}(n)
  <
  W_{P_3}(n),
\]
where the \(W_{\mathrm{T*}}\) use the same sieve weights as the \(P_3\)
theorem.

The next exact task is to extract Campbell's actual \(P_3\) weight and
rewrite its lower bound over terminal pairs \((a,k)\).  If T1 and T2 cannot
saturate that lower bound, the remaining Tfar channel becomes the genuine
descent target.

## Campbell weight extraction

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_campbell\_weight\_extraction.md}.
\]

The source TeX for Campbell's arXiv preprint was inspected locally in
\[
  \texttt{/tmp/2603.10356\_src}
\]
without committing the third-party source to Git.

The exact large-range parameters are:
\[
  k=3,\qquad k_1=8,\qquad k_2=3.17,
\]
\[
  z=X^{1/8},\qquad y=X^{1/3.17},\qquad \lambda=0.83.
\]

The Richert weight is
\[
  w(a)=
  \lambda
  -
  \sum_{\substack{z\le p<y\\p\mid a}}
  \left(1-\frac{\log p}{\log y}\right),
\]
summed over \((a,P(z))=1\).

Campbell's final margin is
\[
  r_3(\mathcal A)>0.0249\frac{\sqrt N}{\log X}>0
\]
for \(N\ge10^{31}\).

This exposes a real limitation: a naive upper bound for composite \(P_3\)'s
is unlikely to beat that small margin.  The usable target must instead focus
on Richert-core survivors, i.e. composite \(P_3\)'s with no prime factor
below
\[
  z=X^{1/8},
\]
and synchronize them with the small-prime certificates forced by
prime-freeness of the whole interval.

## Richert-core terminal atom types

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_richert\_terminal\_atom\_types.md}.
\]

For a prime-free interval, a Richert-core \(P_3\) survivor satisfies
\[
  \Omega(A)\le3,
  \qquad
  (A,P(z))=1,
  \qquad
  z=X^{1/8}.
\]

Its terminal factorization
\[
  A=dD,\qquad d\le n<D
\]
has only three atomic shapes:
\[
  \mathrm{R2}: d=p,\ D=q,
\]
\[
  \mathrm{R3L}: d=p,\ D=qr,
\]
\[
  \mathrm{R3R}: d=pq,\ D=r.
\]

All atomic primes lie above \(z\).  The lower-side atoms are \(\le n\), and
if the upper terminal side is composite then at least one of its atoms is
\(<n+1\).  Thus every prime-free Richert-core survivor has a medium-prime
certificate in \([z,n+1)\), but not every atom has to lie below \(n+1\).

The next algebraic obstruction is to synchronize these three atom types with
the existing quotient-certificate equations, and prove that two or three
medium-prime atoms cannot certify enough structured composites to support a
prime-free Legendre interval.

## Boundary of the P3 upgrade route

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_p3\_upgrade\_boundary.md}.
\]

This records a hard boundary for the attempted \(P_3\)-to-prime upgrade.
A single terminal \(P_3\) survivor cannot force a prime or a descent.

The semiprime atom type R2 is formally compatible with the interval:
\[
  A=pq,\qquad p=n-a,\quad q=n+a+k,
\]
and the full Legendre interval permits the upper-edge shape
\[
  a=0,\qquad k=2,
\]
namely
\[
  A=n(n+2)=n^2+2n=(n+1)^2-1.
\]

Campbell's open analytic set excludes that exact upper-edge point, but R2 is
also compatible inside the open set; for example
\[
  7\cdot17=119\in(10^2,10^2+2\cdot10).
\]
This does not threaten Legendre; it shows that existence of one composite
\(P_3\) is not contradictory.

The corrected closure target is collective:

\[
  \text{Richert survivor}
  +
  \text{local certificate packet}
  +
  \text{no-repetition constraints}
  \Longrightarrow
  \Omega(A)\ge4.
\]

This would contradict \(\Omega(A)\le3\).  The next exact task is therefore
to define a forced packet around a Richert-core terminal survivor.  If no
forced packet exists, the \(P_3\)-upgrade route should be downgraded and the
main closure path returns to Pell-synchronized quotient skeleton elimination.

## Explicit \(m\equiv3\pmod4\) Pell system

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_pell\_system.md}.
\]

This writes the hardest quotient skeleton as an exact reduced system.

Use
\[
  e_i=2f_i,\qquad w_i=2u_i.
\]
Then every offset satisfies
\[
  u_i^2=f_i^2+6mf_i-c_i.
\]

For \(m\equiv3\pmod4\), the offsets split as
\[
  \mathrm{A0}=\{4,16,64,100\},
  \qquad
  \mathrm{A1}=\{2,26,50,122\}.
\]

The residue classes are:

- for \(c=4,100\):
  \[
    f\equiv2,4,10,20\pmod{24};
  \]
- for \(c=16,64\):
  \[
    f\equiv8,14,16,22\pmod{24};
  \]
- for \(c=2,26,50,122\):
  \[
    f\equiv9\pmod{12}.
  \]

The sorted quotient skeleton
\[
  (4,8,16,18,28,42,66,90)
\]
becomes
\[
  (2,4,8,9,14,21,33,45)
\]
in \(f\)-variables.

Pairwise elimination of \(m\) gives the 28 reduced Pell equations
\[
  f_j u_i^2-f_i u_j^2
  =
  f_if_j(f_i-f_j)-f_jc_i+f_ic_j.
\]

This is now the main exact closure target: prove that the finite union over
rank assignments, residue choices, and \(m\bmod8\) has no integral point
satisfying the label and ladder constraints.  The first component to attack
is the minimal boundary component with
\[
  f=(2,4,8,9,14,21,33,45).
\]

## Minimal \(m\equiv3\pmod4\) component killed modulo 7

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_minimal\_component\_mod7.md}.
\]

The first boundary component of the hardest skeleton is eliminated exactly.

In the minimal \(f\)-skeleton
\[
  (2,4,8,9,14,21,33,45),
\]
the A0 offsets \(c=16,64\), i.e. the \(x^2\equiv0\pmod{16}\) offsets, must
receive \(f=8,14\).  Hence one of them must receive
\[
  f=14.
\]

The reduced Pell line
\[
  u^2=f^2+6mf-c
\]
then reduces modulo \(7\) to
\[
  u^2\equiv-c\pmod7.
\]

For \(c=16\),
\[
  -c\equiv5\pmod7,
\]
and for \(c=64\),
\[
  -c\equiv6\pmod7.
\]

But the square classes modulo \(7\) are
\[
  0,1,2,4.
\]

Therefore neither pairing is possible.  The exact minimal component is killed
modulo \(7\).

This is the first actual elimination inside the \(m\equiv3\pmod4\) Pell
skeleton.  The next components must raise the \(x^2\equiv0\pmod{16}\) A0
quotient beyond the naive \(f=14\) boundary.  The sharper zero-quotient
filter below identifies the true next boundary.

## \(m\equiv3\pmod4\) modulo 7 zero-quotient filter

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_mod7\_zero\_filter.md}.
\]

The modulo \(7\) obstruction is stronger than the single \(f=14\) boundary
kill.

For the reduced line
\[
  u^2=f^2+6mf-c,
\]
if
\[
  7\mid f,
\]
then the \(m\)-dependent term disappears modulo \(7\), giving the necessary
condition
\[
  u^2\equiv-c\pmod7.
\]

Since the square classes modulo \(7\) are
\[
  0,1,2,4,
\]
the only offsets among
\[
  2,4,16,26,50,64,100,122
\]
which can carry \(7\mid f\) are
\[
  c=26,\ 122.
\]

Consequences:

1. the A0 zero-square offsets \(c=16,64\) cannot carry \(f\equiv0\pmod7\);
2. their first two admissible values are \(8,16\), not \(8,14\);
3. the hard-branch sorted quotient lower bound sharpens from
   \[
     e=(4,8,16,18,28,42,66,90)
   \]
   to
   \[
   \boxed{
     e=(4,8,16,18,32,42,66,90);
   }
   \]
4. the A1 boundary value \(f=21\) must be attached to \(c=26\) or \(c=122\).

The active exact target is now the lifted boundary component
\[
\boxed{
  f=(2,4,8,9,16,21,33,45),
  \qquad
  f=21\text{ attached to }c=26\text{ or }122.
}
\]

## Lifted \(m\equiv3\pmod4\) boundary killed modulo 5 and 11

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_lifted\_boundary\_mod5\_mod11.md}.
\]

The lifted boundary component
\[
  f=(2,4,8,9,16,21,33,45)
\]
is also eliminated exactly.

The proof uses no search over \(m\).  It is a finite congruence certificate
for the reduced Pell lines
\[
  u^2=f^2+6mf-c.
\]

Modulo \(5\), the square classes are
\[
  0,1,4.
\]

The two A0 sublayers force:

1. \(c=4\) must receive \(f=2\), and \(c=100\) must receive \(f=4\);
2. the only surviving A0 zero-square assignment is
   \[
     c=16\mapsto16,\qquad c=64\mapsto8,
   \]
   with
   \[
     m\equiv0\pmod5.
   \]

At this same residue, the A1 layer is forced uniquely:
\[
\boxed{
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 2 & 4 & 16 & 8 & 9 & 45 & 33 & 21.
\end{array}
}
\]

For this unique assignment, modulo \(11\) gives an empty intersection of
allowed \(m\)-classes.  The first five constraints force
\[
  m\equiv9\pmod{11},
\]
but the row
\[
  c=26,\qquad f=45
\]
does not allow \(m\equiv9\pmod{11}\).

Therefore:
\[
\boxed{
  f=(2,4,8,9,16,21,33,45)
  \text{ has no integral point.}
}
\]

The next exact boundary is a finite union, not a single tuple.  At least one
of the following layer raises must occur:
\[
\boxed{
  4\leadsto10,
  \qquad
  16\leadsto22,
  \qquad
  45\leadsto57
}
\]
in \(f\)-variables.

## Complete next \(m\equiv3\pmod4\) boundary layer killed

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_next\_boundary\_layer\_modular\_closure.md}.
\]

The full first escape layer after the lifted component is eliminated.  The
three exact families are:

\[
\begin{array}{c|c|c|c}
  \text{family} & \mathrm{A0},\ x^2\equiv4 & \mathrm{A0},\ x^2\equiv0 & \mathrm{A1}\\
  \hline
  F_{04} & 2,10 & 8,16 & 9,21,33,45\\
  F_{00} & 2,4 & 8,22 & 9,21,33,45\\
  F_{1}  & 2,4 & 8,16 & 9,21,33,57.
\end{array}
\]

The certificates are:

- \(F_{00}\) dies modulo \(5\).  A0 leaves only \(m\equiv2,3\pmod5\).  At
  \(m\equiv2\), the offset \(c=2\) has no admissible A1 quotient; at
  \(m\equiv3\), the offsets \(c=26\) and \(c=50\) both require \(f=45\).
- \(F_{04}\) is reduced modulo \(5\) to two assignments.  Modulo \(7\) kills
  one and forces \(m\equiv6\pmod7\) for the other.  Modulo \(11\), the first
  five rows force \(m\equiv9\pmod{11}\), but the row \(c=26,f=45\) forbids
  that class.
- \(F_1\) is reduced modulo \(5\) to one assignment and modulo \(7\) to
  \(m\equiv5\pmod7\).  Modulo \(11\), the row \(c=26,f=33\) has no
  admissible class:
  \[
    M_{11}(26,33)=\varnothing.
  \]

Therefore the hard branch cannot escape by exactly one first boundary raise:
\[
\boxed{
  F_{04}\cup F_{00}\cup F_1=\varnothing.
}
\]

This is the first multi-family closure step in the \(m\equiv3\pmod4\)
quotient game.  It also exposes the real missing theorem:

\[
\boxed{
  \text{prove a rank cap for the hard quotient game.}
}
\]

Once such a cap exists, the remaining modular matching certificates become a
finite proof object.  Without such a cap, the modular eliminations may climb
forever and cannot by themselves close Legendre.

## \(m\equiv3\pmod4\) rank weights 2--4 closed

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_rank\_weight\_2\_4\_closure.md}.
\]

The first escape layer was weight \(1\).  The new note closes the next three
rank weights.

Use rank coordinates
\[
  (a,b,c)
\]
for the three layer raises:

- \(a\): A0 \(x^2\equiv4\pmod{16}\);
- \(b\): A0 \(x^2\equiv0\pmod{16}\);
- \(c\): A1.

The weight is
\[
  w=a+b+c.
\]

The exact result is:
\[
\boxed{
  w=2,3,4
  \quad\Longrightarrow\quad
  \text{no integral point in the hard }m\equiv3\pmod4\text{ Pell system.}
}
\]

The certificates use only the finite local sets
\[
  M_\ell(c,f)
  =
  \{m\bmod\ell:\ f^2+6mf-c\text{ is a square modulo }\ell\},
\]
with small primes
\[
  \ell\in\{5,7,11,13,17\}.
\]

Thus, combining the previous notes:
\[
\boxed{
  w=0,1,2,3,4
  \quad\Longrightarrow\quad
  \text{the rank family is impossible.}
}
\]

Any remaining hard-branch clean-gate counterexample must therefore satisfy
\[
\boxed{
  a+b+c\ge5.
}
\]

This sharpens the closure problem.  It is no longer enough to say "find a
rank cap".  The exact missing theorem is one of:

\[
\boxed{
  a+b+c\le4
  \quad\text{for every hard-branch clean-gate counterexample;}
}
\]

or

\[
\boxed{
  \text{the finite modular automaton kills every rank triple }(a,b,c).
}
\]

The second path is the more promising nonstandard route: prove periodic
modular killing in the rank variables, avoiding an analytic quotient bound.

## \(m\equiv3\pmod4\) rank weights 0--30 certified

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_rank\_weight\_0\_30\_certificate.md}
\]
and the verifier
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py}.
\]

The verifier checks the exact finite local sets
\[
  M_\ell(c,f)
  =
  \{m\bmod\ell:\ f^2+6mf-c\text{ is a square modulo }\ell\}
\]
for every rank family
\[
  F(a,b,c)
\]
with
\[
  0\le a+b+c\le30.
\]

It uses only
\[
  \ell\in\{5,7,11,13,17\}
\]
plus the modulo \(7\) zero-quotient filter.

The exact command
\[
  \texttt{python3 Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py --max-weight 30}
\]
ends with
\[
  \texttt{certificate: all weights 0..30 closed}.
\]

Therefore any remaining hard \(m\equiv3\pmod4\) clean-gate counterexample
must satisfy
\[
\boxed{
  a+b+c\ge31.
}
\]

This is the strongest current obstruction in the Legendre thread.  The
closure problem is now sharply reduced to one of:

1. prove a rank cap
   \[
     a+b+c\le30;
   \]
2. prove periodic modular killing for all rank triples;
3. prove a descent from any surviving weight \(>30\) to a smaller surviving
   weight.

## First periodic automaton closure attempt fails

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_periodic\_automaton\_obstruction.md}.
\]

The five-prime automaton
\[
  \{5,7,11,13,17\}
\]
does not close the full rank game by periodicity.

There is an explicit surviving assignment pattern:
\[
\begin{array}{c|cccccccc}
  \text{offset} & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  \text{slot} & 2 & a & b & 8 & c & 21 & 33 & 9.
\end{array}
\]

It survives the five-prime local-square automaton in the center class
\[
\boxed{
  m\equiv14325\pmod{85085}.
}
\]

This does not affect the finite certificate up to weight \(30\).  It only
rules out the naive extrapolation that the same five primes kill every rank
triple periodically.

The next closure target is now sharper:

\[
\boxed{
  \text{kill this survivor pattern by Pell synchronization,}
}
\]

or else add a new modulus that is genuinely forced by the survivor pattern.

## Periodic boundary automaton closed with 83

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_periodic\_boundary\_automaton\_closed.md}.
\]

The survivor pattern from the previous note is killed uniformly by the prime
\[
  83.
\]

The verifier
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py}
\]
now supports
\[
  \texttt{--periodic-patterns}.
\]

Running
\[
  \texttt{python3 Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py --periodic-patterns}
\]
returns:
\[
  \texttt{periodic-patterns total=48 11:4 13:5 17:2 5:33 7:3 83:1}
\]
and ends with
\[
  \texttt{certificate: all periodic boundary patterns closed}.
\]

Therefore the periodic boundary-rank automaton is closed by
\[
\boxed{
  \{5,7,11,13,17,83\}.
}
\]

This is a real closure of the boundary model
\[
  F(a,b,c)
  =
  \{L_{04}[0],L_{04}[1+a]\},
  \{L_{00}[0],L_{00}[1+b]\},
  \{L_1[0],L_1[1],L_1[2],L_1[3+c]\}.
\]

The remaining gap is now structural, not modular:

\[
\boxed{
  \text{prove a descent from arbitrary skipped ranks to this boundary model.}
}
\]

Once that descent is proved, the hard \(m\equiv3\pmod4\) branch closes.

## Arbitrary prefix ranks closed through \(N=9\)

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_arbitrary\_prefix\_rank\_certificate.md}.
\]

This attacks the skipped-rank gap directly.

The verifier
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py}
\]
now supports
\[
  \texttt{--prefix-ranks N}.
\]

For a given \(N\), it checks all arbitrary ordered assignments using the
first \(N\) admissible values of each layer:
\[
  N(N-1)\cdot N(N-1)\cdot N(N-1)(N-2)(N-3)
\]
assignments.

The exact certificates obtained:

\[
\begin{array}{c|c|c}
  N & \#\text{ordered assignments} & \text{status}\\
  \hline
  7 & 1\,481\,760 & \text{closed}\\
  8 & 5\,268\,480 & \text{closed}\\
  9 & 15\,676\,416 & \text{closed}\\
  10 & 40\,824\,000 & \text{closed}
\end{array}
\]

The prime set used is
\[
\boxed{
  \{5,7,11,13,17,19,23,29,83\}.
}
\]

For \(N=10\), the verifier returns:
\[
  \texttt{certificate: all arbitrary assignments from first 10 ranks closed}.
\]

Therefore any remaining hard \(m\equiv3\pmod4\) clean-gate counterexample
must use at least one layer rank
\[
\boxed{
  \ge10.
}
\]

This is stronger than the boundary automaton closure: skipped-rank
configurations are now directly eliminated through the first ten values.

## No finite local-modular closure for arbitrary skipped ranks

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_no\_finite\_local\_modular\_closure.md}.
\]

This note proves that the modular-certificate strategy cannot close the
fully arbitrary skipped-rank problem by merely adding finitely many local
square tests.

For any finite set of odd primes
\[
  \mathcal P,
\]
take
\[
  m\equiv0\pmod{\prod_{\ell\in\mathcal P}\ell}.
\]

Then each row reduces locally to
\[
  u^2\equiv f^2-c\pmod\ell.
\]

For each odd prime \(\ell\), the congruence
\[
  f^2-u^2=c
\]
has solutions because
\[
  (f-u)(f+u)=c
\]
can be solved by choosing \(t=f-u\) and setting
\[
  f=\frac{t+c/t}{2}.
\]

CRT then combines these local residues with the hard-branch layer lattices.
Ranks can be made arbitrarily large and distinct by adding multiples of the
CRT modulus.

Therefore:
\[
\boxed{
  \text{no finite independent local-square prime set closes arbitrary}
  \text{ skipped ranks.}
}
\]

The remaining closure must use:

1. the pairwise Pell synchronization equations; or
2. a genuine rank descent into the already closed prefix range.

## Self-residue filter for skipped ranks

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_self\_residue\_filter.md}.
\]

This is the first intrinsic obstruction on arbitrary skipped ranks.

Reducing the line
\[
  u^2=f^2+6mf-c
\]
modulo \(f\) gives
\[
\boxed{
  u^2\equiv-c\pmod f.
}
\]

Therefore, for every odd prime
\[
  q\mid f,\qquad q\nmid c,
\]
one must have
\[
\boxed{
  \left(\frac{-c}{q}\right)=1.
}
\]

This generalizes the earlier modulo \(7\) zero-filter: the obstruction is
not tied to a fixed external prime, but to whatever prime divisors appear in
the skipped quotient \(f\).

This is the first viable theoretical route beyond finite modular
certificates:

\[
\boxed{
  \text{self-residue filter}+\text{Pell synchronization}
  \Longrightarrow \text{rank descent target.}
}
\]

## A0 square-offset quotient theorem

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A0\_square\_quotient\_theorem.md}.
\]

For A0 rows the offsets are genuine squares:
\[
  c=x^2,\qquad x\in\{2,4,8,10\}.
\]

The intrinsic self-residue filter therefore becomes
\[
\boxed{
  u^2+x^2\equiv0\pmod f.
}
\]

This congruence has an exact prime-power classification.  If
\[
  q^\alpha\Vert f,\qquad \beta=v_q(x),
\]
then:

\[
\begin{array}{c|c}
  q & \text{condition}\\
  \hline
  q\text{ odd} & \alpha\le2\beta\text{ or }q\equiv1\pmod4\\
  q=2 & \alpha\le2\beta+1.
\end{array}
\]

Consequently the four A0 square offsets impose:
\[
\begin{array}{c|c|c}
  c & x & \text{condition on }f\\
  \hline
  4 & 2
    & v_2(f)\le3,\ \text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  16 & 4
    & v_2(f)\le5,\ \text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  64 & 8
    & v_2(f)\le7,\ \text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  100 & 10
    & v_2(f)\le3,\ \text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4.
\end{array}
\]

This is not a finite modular test.  It is an intrinsic arithmetic restriction
on every skipped A0 quotient: its odd prime divisors must lie in the
sum-of-two-squares class, and its power of \(2\) is capped by the offset.

The hard \(m\equiv3\pmod4\) closure target is now sharper:
\[
\boxed{
  \text{A0 square quotient theorem}
  +\text{A1 self-residue constraints}
  +\text{Pell synchronization}
  \Longrightarrow \text{rank descent.}
}
\]

## A1 quadratic-field quotient theorem

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A1\_quadratic\_field\_quotient\_theorem.md}.
\]

For the A1 offsets
\[
  c\in\{2,26,50,122\},
\]
one always has
\[
  f\equiv9\pmod{12}.
\]

Thus \(f\) is odd and divisible by \(3\), and the self-residue condition is
\[
\boxed{
  u^2\equiv-c\pmod f.
}
\]

For an odd prime power
\[
  q^\alpha\Vert f,\qquad \gamma=v_q(c),
\]
the exact criterion is:

- if \(q\nmid c\), then
  \[
    \left(\frac{-c}{q}\right)=1;
  \]
- if \(q\mid c\) and \(\alpha\le\gamma\), then \(u=0\) works;
- if \(q\mid c\), \(\alpha>\gamma\), and \(\gamma\) is even, then
  \[
    \left(\frac{-c/q^\gamma}{q}\right)=1;
  \]
- if \(q\mid c\), \(\alpha>\gamma\), and \(\gamma\) is odd, no solution
  exists.

For the four A1 rows this gives:
\[
\begin{array}{c|c}
  c & \text{condition on }f\\
  \hline
  2
    & \left(\frac{-2}{q}\right)=1\text{ for every }q\mid f\\
  26
    & v_{13}(f)\le1,\quad
      \left(\frac{-26}{q}\right)=1\text{ for }q\mid f,\ q\ne13\\
  50
    & v_5(f)\le2,\quad
      \left(\frac{-50}{q}\right)=1\text{ for }q\mid f,\ q\ne5\\
  122
    & v_{61}(f)\le1,\quad
      \left(\frac{-122}{q}\right)=1\text{ for }q\mid f,\ q\ne61.
\end{array}
\]

The forced divisor \(3\mid f\) is always compatible because
\[
  c\equiv2\pmod3,
  \qquad
  -c\equiv1\pmod3.
\]

Together with the A0 theorem, arbitrary skipped quotients are now controlled
by intrinsic splitting laws rather than by a fixed finite set of external
moduli.  The remaining proof problem is to combine these splitting laws with
the pairwise Pell synchronization equations to force rank descent into the
already closed prefix range.

## A0 zero-layer collapse

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A0\_zero\_layer\_collapse.md}.
\]

This is the first direct rank-game consequence of the A0 quotient theorem.

For the A0 zero offsets
\[
  c=16,\ 64,
\]
the old hard-branch layer was
\[
  f\equiv8,14,16,22\pmod{24}.
\]

But the A0 theorem forces
\[
  f=2^\nu s,
  \qquad
  s\text{ odd},
  \qquad
  q\mid s\Rightarrow q\equiv1\pmod4.
\]

Hence
\[
  s\equiv1\pmod4.
\]

If
\[
  f\equiv14\pmod{24},
\]
then \(v_2(f)=1\) and
\[
  s=f/2\equiv7\pmod{12},
\]
so \(s\equiv3\pmod4\), contradiction.  The same argument with
\[
  f\equiv22\pmod{24}
\]
gives
\[
  s=f/2\equiv11\pmod{12}\equiv3\pmod4,
\]
again impossible.

Therefore:
\[
\boxed{
  c=16,64
  \quad\Longrightarrow\quad
  f\equiv8,16\pmod{24}.
}
\]

More sharply:
\[
\begin{array}{c|c}
  c & \text{allowed form}\\
  \hline
  16
    & f=2^\nu s,\quad3\le\nu\le5,\quad
      q\mid s\Rightarrow q\equiv1\pmod4\\
  64
    & f=2^\nu s,\quad3\le\nu\le7,\quad
      q\mid s\Rightarrow q\equiv1\pmod4.
\end{array}
\]

This kills the old first-escape move
\[
  16\leadsto22
\]
structurally, not by a finite modulo-\(5\) certificate.  The rank automaton
for the hard branch must now be rebuilt over this thinner multiplicative
zero-layer semigroup.

## A0 four-layer refinement

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A0\_four\_layer\_refinement.md}.
\]

This is the companion consequence for the A0 offsets
\[
  c=4,\ 100.
\]

The old layer was
\[
  f\equiv2,4,10,20\pmod{24}.
\]

The A0 quotient theorem forces every admissible quotient in this layer to be
\[
\boxed{
  f=2s\quad\text{or}\quad f=4s,
}
\]
where
\[
\boxed{
  s\text{ is odd},\qquad
  3\nmid s,\qquad
  q\mid s\Rightarrow q\equiv1\pmod4.
}
\]

The \(v_2(f)=1\) part gives exactly
\[
  f\equiv2,10\pmod{24}.
\]

The \(v_2(f)=2\) part is sharper:
\[
\boxed{
  f\equiv4,20\pmod{48}.
}
\]

Thus the old residue classes
\[
  f\equiv4,20\pmod{24}
\]
were too large by a factor \(2\).  The sub-classes
\[
\boxed{
  f\equiv28,44\pmod{48}
}
\]
are impossible because after division by \(4\) their odd part is
\[
  s\equiv3\pmod4,
\]
contradicting the A0 quotient theorem.

Together with the zero-layer collapse, this replaces both A0 rank lattices
by multiplicative semigroups.  The next rank model should use these
semigroups directly, then impose the A1 splitting laws and the pairwise Pell
synchronization equations.

## Multiplicative rank model

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_multiplicative\_rank\_model.md}.
\]

This note replaces the old additive rank automaton by eight intrinsic
multiplicative quotient semigroups.

Let
\[
  \mathcal S_4
  =
  \{s\ge1:\ s\text{ odd},\ 3\nmid s,\ q\mid s\Rightarrow q\equiv1\pmod4\}.
\]

Then the A0 part becomes:
\[
\begin{array}{c|c}
  c & \text{quotient semigroup}\\
  \hline
  4,100 & 2\mathcal S_4\cup4\mathcal S_4\\
  16 & \bigcup_{\nu=3}^{5}2^\nu\mathcal S_4\\
  64 & \bigcup_{\nu=3}^{7}2^\nu\mathcal S_4.
\end{array}
\]

The A1 part becomes:
\[
\begin{array}{c|c}
  c & \text{quotient semigroup}\\
  \hline
  2 & \mathcal T_2\\
  26 & \mathcal T_{26}\\
  50 & \mathcal T_{50}\\
  122 & \mathcal T_{122},
\end{array}
\]
where each \(\mathcal T_c\) is defined by
\[
  f\equiv9\pmod{12}
\]
and the corresponding splitting law
\[
  \left(\frac{-c}{q}\right)=1
\]
away from the ramified primes, with the exact ramified caps
\[
  v_{13}(f)\le1,\qquad
  v_5(f)\le2,\qquad
  v_{61}(f)\le1.
\]

A hard-branch counterexample must now be an integral point of the pairwise
Pell synchronization system
\[
  f_d u_c^2-f_c u_d^2
  =
  f_cf_d(f_c-f_d)-f_dc+f_cd
\]
with every \(f_c\) in its offset-specific semigroup.

The closure target is no longer "add more local primes".  It is:
\[
\boxed{
  \text{multiplicative semigroup constraints}
  +\text{pairwise Pell synchronization}
  \Longrightarrow \text{rank descent into the closed prefix range.}
}
\]

## Shared-prime compatibility graph

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_shared\_prime\_compatibility.md}.
\]

This is the first edge constraint in the multiplicative model.

If an odd prime satisfies
\[
  q\mid f_c,
  \qquad
  q\mid f_d,
  \qquad
  q\nmid cd,
\]
then the two self-residue equations force
\[
\boxed{
  \left(\frac{-c}{q}\right)=
  \left(\frac{-d}{q}\right)=1.
}
\]

Thus \(q\) splits completely in
\[
\boxed{
  \mathbb Q(\sqrt{-c},\sqrt{-d}).
}
\]

For A0--A1 edges this gives a particularly useful restriction.  A0
quotients are even with \(3\)-free odd part, while A1 quotients are odd and
divisible by \(3\).  Therefore
\[
\boxed{
  \gcd(f_a,f_b)\text{ is coprime to }6
}
\]
for every A0 offset \(a\) and A1 offset \(b\).

Moreover, every nonramified prime \(q\mid\gcd(f_a,f_b)\) must satisfy
\[
  q\equiv1\pmod4
  \qquad\text{and}\qquad
  \left(\frac{-b}{q}\right)=1.
\]

Equivalently:
\[
\begin{array}{c|c}
  b & \text{condition on nonramified }q\mid\gcd(f_a,f_b)\\
  \hline
  2 & q\equiv1\pmod8\\
  26 & q\equiv1\pmod4,\ \left(\frac{26}{q}\right)=1\\
  50 & q\equiv1\pmod8\\
  122 & q\equiv1\pmod4,\ \left(\frac{122}{q}\right)=1.
\end{array}
\]

For A1--A1 edges, \(3\) is the universal shared prime, but every other
unramified shared prime must split in the corresponding biquadratic field.

The hard branch is now a labelled complete graph problem: each vertex label
\(f_c\) lies in its multiplicative semigroup, and every common prime divisor
of two labels must lie in the edge compatibility set.  The remaining
descent target is:
\[
\boxed{
  \text{vertex semigroups}
  +\text{shared-prime edge compatibility}
  +\text{Pell synchronization}
  \Longrightarrow \text{rank descent.}
}
\]

## Dual-factor common-gap model

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_dual\_factor\_gap\_model.md}.
\]

This is a two-sided strengthening of the multiplicative model.

The reduced Pell line
\[
  u_c^2=f_c^2+6mf_c-c
\]
is equivalent to
\[
\boxed{
  u_c^2+c=f_c(f_c+6m).
}
\]

Set
\[
  L=6m.
\]

Since \(m\equiv3\pmod4\),
\[
\boxed{
  L\equiv18\pmod{24}.
}
\]

For each offset define the upper factor
\[
  F_c=f_c+L.
\]

Then
\[
\boxed{
  u_c^2+c=f_cF_c,
  \qquad
  F_c-f_c=L.
}
\]

The key point is that both factors divide \(u_c^2+c\).  Hence both satisfy
the same self-residue law:
\[
\boxed{
  u_c^2\equiv-c\pmod{f_c},
  \qquad
  u_c^2\equiv-c\pmod{F_c}.
}
\]

Therefore every splitting restriction proved for \(f_c\) also applies to
the upper factor \(F_c\).  For A0, both factors have all odd prime divisors
\(1\bmod4\) and the same offset-specific \(2\)-adic ceiling.  For A1, both
factors obey the same quadratic-field splitting law and ramified caps.

In the A1 case,
\[
  f_c\equiv9\pmod{12},
  \qquad
  F_c=f_c+L\equiv3\pmod{12}.
\]

Thus the remaining hard branch is no longer one-sided:
\[
\boxed{
  f_c\text{ and }f_c+L
  \text{ must both satisfy the offset-specific splitting law}
}
\]
for the same gap
\[
  L\equiv18\pmod{24}
\]
across all eight offsets.

The next descent target is to show that a lower factor outside the closed
prefix range forces a forbidden prime divisor either in \(f_c\) or in its
upper partner \(f_c+L\).

## A0 dual four-layer collapse

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A0\_dual\_four\_layer\_collapse.md}.
\]

This is a genuine structural gain from the dual-factor model.

For \(c=4,100\), the previous A0 four-layer refinement gave
\[
  f=2s
  \quad\text{or}\quad
  f=4s,
\]
where
\[
  s\text{ is odd},\qquad
  3\nmid s,\qquad
  q\mid s\Rightarrow q\equiv1\pmod4.
\]

Thus
\[
  s\equiv1\pmod4.
\]

Write
\[
  L=6m=2h.
\]

Since \(m\equiv3\pmod4\),
\[
  h=3m\equiv1\pmod4.
\]

The upper factor is
\[
  F=f+L=f+2h.
\]

If \(f=4s\), then
\[
  F=2(2s+h).
\]

But
\[
  2s+h\equiv2\cdot1+1\equiv3\pmod4.
\]

This contradicts the dual A0 splitting law, because every odd prime divisor
of \(F\) must be \(1\bmod4\).  Therefore:
\[
\boxed{
  c=4,100
  \quad\Longrightarrow\quad
  f\notin4\mathcal S_4.
}
\]

Only the branch
\[
\boxed{
  f=2s,\qquad s\in\mathcal S_4
}
\]
survives.  Its upper partner automatically has
\[
  F=4t,
\]
and the dual splitting law imposes
\[
  t\in\mathcal S_4.
\]

Consequently the first two distinct lower quotients for \(c=4,100\) are
\[
\boxed{
  2,\ 10
}
\]
instead of
\[
  2,\ 4.
\]

The old first-escape move
\[
  4\leadsto10
\]
is now structural, just like the previous zero-layer collapse made
\[
  16\leadsto22
\]
structural.  Both A0 escape moves have therefore been absorbed into the
intrinsic quotient geometry.

## A0 dual valuation collapse

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A0\_dual\_valuation\_collapse.md}.
\]

This pushes the dual-factor model one step further by using the equality
\[
\boxed{
  u^2+x^2=fF,
  \qquad
  F=f+6m.
}
\]

For A0 zero-layer offsets \(c=16,64\), write
\[
  f=2^\nu s,
  \qquad
  \nu\ge3,
  \qquad
  s\text{ odd}.
\]

Since
\[
  6m=2h,
  \qquad
  h\equiv1\pmod4,
\]
the upper factor has
\[
\boxed{
  v_2(F)=1.
}
\]

Hence
\[
\boxed{
  v_2(fF)=\nu+1.
}
\]

For \(c=16\), one has \(x=4\), so the possible valuations of
\[
  u^2+16
\]
are only
\[
  0,\ 2,\ 4,\ 5.
\]

Thus \(\nu=5\) is impossible, and
\[
\boxed{
  c=16:\quad f\in8\mathcal S_4\cup16\mathcal S_4.
}
\]

For \(c=64\), one has \(x=8\), so the possible valuations of
\[
  u^2+64
\]
are only
\[
  0,\ 2,\ 4,\ 6,\ 7.
\]

Thus \(\nu=4\) and \(\nu=7\) are impossible, and
\[
\boxed{
  c=64:\quad f\in8\mathcal S_4\cup32\mathcal S_4\cup64\mathcal S_4.
}
\]

Consequently the lower quotient \(f=16\) can occur only on the \(c=16\)
row, not on \(c=64\).  The A0 zero layer is now assignment-rigid at the
bottom, again by intrinsic \(2\)-adic factorization rather than by finite
local testing.

## Multiplicative model updated after A0 dual collapses

Updated
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_multiplicative\_rank\_model.md}
\]
and
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_dual\_factor\_gap\_model.md}
\]
to use the surviving A0 lower semigroups:
\[
\begin{array}{c|c}
  c & \text{surviving lower semigroup}\\
  \hline
  4,100 & 2\mathcal S_4\\
  16 & 8\mathcal S_4\cup16\mathcal S_4\\
  64 & 8\mathcal S_4\cup32\mathcal S_4\cup64\mathcal S_4.
\end{array}
\]

This keeps the main hard-branch certificate aligned with the strongest
known intrinsic constraints.

## A1 dual sign-parity law

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A1\_dual\_sign\_parity.md}.
\]

For every A1 row,
\[
  f_c\equiv9\pmod{12}.
\]

With
\[
  L=6m\equiv18\pmod{24},
  \qquad
  F_c=f_c+L,
\]
one gets
\[
\boxed{
  f_c\equiv1\pmod4,
  \qquad
  F_c\equiv3\pmod4.
}
\]

Both factors satisfy the same quadratic-field splitting law, but their
signs modulo \(4\) are opposite.

For an odd integer \(N\), define
\[
  \Omega_3(N)
  =
  \sum_{\substack{q^\alpha\Vert N\\ q\equiv3\pmod4}}\alpha.
\]

Then
\[
  N\equiv(-1)^{\Omega_3(N)}\pmod4.
\]

Therefore every A1 row satisfies
\[
\boxed{
  \Omega_3(f_c)\equiv0\pmod2,
  \qquad
  \Omega_3(F_c)\equiv1\pmod2.
}
\]

Since \(3\mid f_c,F_c\) and \(3\equiv3\pmod4\), this can also be written as
\[
  v_3(f_c)+\Omega_3^{(\ne3)}(f_c)\equiv0\pmod2,
\]
and
\[
  v_3(F_c)+\Omega_3^{(\ne3)}(F_c)\equiv1\pmod2.
\]

Thus the non-\(3\) split primes \(3\bmod4\) must compensate the \(3\)-adic
parity of the lower and upper A1 factors.  This gives a new exact descent
target inside the A1 same-field pair.

## A0 dual boundary killed modulo 23

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A0\_dual\_boundary\_mod23.md}.
\]

After the A0 dual collapses, the first A0 structural boundary is:
\[
  c=4,100\quad\text{receive}\quad f=2,10,
\]
and
\[
  c=16,64\quad\text{receive}\quad f=16,8,
\]
with \(f=16\) forced onto \(c=16\).

Only two assignments remain:
\[
\begin{array}{c|cc}
  \text{case} & c=4 & c=100\\
  \hline
  I & 2 & 10\\
  II & 10 & 2.
\end{array}
\]

Modulo \(23\), define
\[
  M_{23}(c,f)
  =
  \{m\bmod23:\ f^2+6mf-c\text{ is a square modulo }23\}.
\]

Case I dies because
\[
  M_{23}(4,2)\cap M_{23}(100,10)=\{0\},
\]
but
\[
  0\notin M_{23}(16,16).
\]

Case II dies because
\[
  M_{23}(4,10)
  \cap M_{23}(100,2)
  \cap M_{23}(16,16)
  =
  \{10,17\},
\]
but
\[
  \{10,17\}\cap M_{23}(64,8)=\varnothing.
\]

Therefore the whole new A0 dual structural boundary has no integral point.
Any remaining hard-branch counterexample must leave this A0 boundary.

## A0 dual two-value prefix certificate

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_A0\_dual\_prefix2\_certificate.md}.
\]

This closes the complete A0 structural prefix obtained by taking the first
two available lower quotients for each A0 offset after the dual collapses:
\[
\begin{array}{c|c}
  c & \text{first two values}\\
  \hline
  4 & 2,\ 10\\
  100 & 2,\ 10\\
  16 & 8,\ 16\\
  64 & 8,\ 32.
\end{array}
\]

There are exactly six pairwise-distinct assignments.  They are killed by
finite congruence certificates:
\[
\begin{array}{c|c|c|c|c}
  c=4 & c=100 & c=16 & c=64 & \text{killing prime}\\
  \hline
  2 & 10 & 8  & 32 & 7\\
  2 & 10 & 16 & 8  & 13\\
  2 & 10 & 16 & 32 & 13\\
  10 & 2 & 8  & 32 & 5\\
  10 & 2 & 16 & 8  & 23\\
  10 & 2 & 16 & 32 & 17.
\end{array}
\]

Thus any remaining hard-branch counterexample must use at least one A0
lower quotient beyond this prefix:
\[
\boxed{
  c=4,100:\ f\ge26
  \quad\text{or}\quad
  c=16:\ f\ge40
  \quad\text{or}\quad
  c=64:\ f\ge40.
}
\]

## Structural prefix 7 closed

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_structural\_prefix6\_certificate.md}
\]
and verifier
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_structural\_prefix\_certificate.py}.
\]

The verifier checks the first seven structural quotient values in every
offset row, using the A0 dual semigroups and A1 splitting semigroups.

There are
\[
  2882250
\]
pairwise-distinct assignments.  Finite local certificates kill all but two,
with killer counts:
\[
\begin{array}{c|r}
  p & \#\\
  \hline
  5 & 2381772\\
  7 & 420640\\
  11 & 70472\\
  13 & 7556\\
  17 & 1321\\
  19 & 389\\
  23 & 69\\
  29 & 21\\
  31 & 5\\
  37 & 1\\
  41 & 1\\
  43 & 1.
\end{array}
\]

The two survivors are ghost fibers:
\[
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 10 & 58 & 8 & 40 & 9 & 21 & 33 & 69
\end{array}
\]
and
\[
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 10 & 58 & 16 & 40 & 9 & 21 & 33 & 69.
\end{array}
\]

Both contain the universal local class \(m\equiv-1\).  Over the integers,
the A0 rows force two squares whose difference is \(8\):
\[
  Y^2-X^2=8.
\]

Thus \(X=1,Y=3\), and in both cases
\[
  m=-1.
\]

## Prefix 8 exceptional fibers reduced to two Pell systems

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_prefix8\_exceptional\_pell\_fibers.md}.
\]

The prefix-\(8\) structural frontier has
\[
  9307368
\]
pairwise-distinct assignments.  Finite local certificates at odd primes
different from \(3\) kill all but \(15\).

Those \(15\) survivors split exactly as follows:
\[
\begin{array}{c|c}
\text{type} & \#\\
\hline
m=-1\text{ ghost fibers} & 2\\
m=3\text{ boundary fibers} & 8\\
\text{impossible modulo }9 & 3\\
\text{residual coupled Pell systems} & 2.
\end{array}
\]

The two residual systems share
\[
\begin{array}{c|cccccc}
c & 4 & 100 & 16 & 64 & 2 & 50\\
\hline
f_c & 34 & 82 & 40 & 64 & 33 & 57.
\end{array}
\]

Modulo \(81\) they force
\[
  m=27k+3.
\]
The row \((c,f)=(64,64)\) then gives
\[
  U_{64}^2=5184(2k+1),
\]
so for positive fibers
\[
  2k+1=s^2.
\]

The common core becomes
\[
\begin{aligned}
  2X_4^2   &=153s^2-55,\\
  2X_{100}^2&=41s^2+9,\\
  2X_{16}^2&=45s^2-13,\\
  X_2^2    &=2673s^2-992,\\
  X_{50}^2 &=4617s^2-392.
\end{aligned}
\]

The two terminal alternatives are
\[
\begin{aligned}
  X_{26}^2&=1701s^2-908,\\
  X_{122}^2&=7533s^2+2668,
\end{aligned}
\]
or
\[
\begin{aligned}
  X_{26}^2&=3645s^2-836,\\
  X_{122}^2&=1701s^2-1004.
\end{aligned}
\]

Therefore the next exact closure target is a genuine Diophantine one:
prove that these two coupled Pell systems have no positive integral point
after saturating the already identified fibers \(m=-1\) and \(m=3\).

The common equations
\[
  2X_{100}^2=41s^2+9,
  \qquad
  2X_{16}^2=45s^2-13
\]
give the genus-one quartic
\[
  W^2=1845s^4-128s^2-117,
  \qquad W=2X_{100}X_{16}.
\]

Added the external exact closure target
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_residual\_pell\_fibers.magma}.
\]

If its integral-point computation returns only \(s=\pm1\) after the separated
square-equation filter, then \(k=0\), hence \(m=3\), and the two residual
prefix-\(8\) fibers are closed by the existing \(m-3\) saturation.

## Residual elliptic curve Mordell-Weil data

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_residual\_elliptic\_mwrank\_certificate.md}
\]
and reproducibility wrapper
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_residual\_elliptic\_mwrank.sh}.
\]

The quartic
\[
  W^2=1845s^4-128s^2-117
\]
maps to
\[
  E:\quad Y^2=X^3-128X^2-215865X
\]
by
\[
  X=1845s^2,\qquad Y=1845sW.
\]

Using eclib `mwrank`, the Mordell-Weil group is certified
unconditionally:
\[
  E(\mathbf Q)_{\mathrm{tors}}\simeq(\mathbf Z/2\mathbf Z)^2,
  \qquad
  \operatorname{rank}E(\mathbf Q)=3.
\]

A basis is
\[
\begin{aligned}
  G_1&=(-363,3696),\\
  G_2&=(-195,5460),\\
  G_3&=(-117,4680).
\end{aligned}
\]

The boundary point
\[
  (s,W)=(1,40)
\]
maps to
\[
  P=(1845,73800)=G_3+(0,0).
\]

Thus the final residual closure is now a precise Mordell-Weil sieve:
show that the only points in the rank-\(3\) lattice with
\[
  X\in1845\mathbf Z^2
\]
come from \(P\) and \(-P\), then observe that the two terminal residual pairs
fail at \(s=1\).

## Residual Mordell-Weil sieve scaffold

Added
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_residual\_mw\_sieve.py}.
\]

This script reduces the certified Mordell-Weil basis modulo good primes and
filters the coefficient lattice by:

\[
  X\in1845\mathbf Z^2
\]
and, in modes \(\texttt{r4}\), \(\texttt{r5}\), the corresponding terminal
residual square conditions.

Current exact sieve status:
\[
\begin{array}{c|c|c}
\text{primes} & R4 & R5\\
\hline
23,43,47 & 16\pmod{24} & 32\pmod{24}\\
23,43,47,31 & 800\pmod{120} & 1600\pmod{120}\\
23,43,47,31,19,37 & 145200\pmod{1320} & 96800\pmod{1320}.
\end{array}
\]

The strengthened certificate option
\[
  \texttt{--expect-prefix8-terminal-pair}
\]
pushes both residual terminal fibers to the same exact pair of
Mordell-Weil residue classes modulo \(1320\):
\[
\begin{aligned}
  (n_1,n_2,n_3;T)&\equiv(0,2,1;(0,0))\pmod{1320},\\
  (n_1,n_2,n_3;T)&\equiv(0,-2,-1;(0,0))\pmod{1320}.
\end{aligned}
\]

The two commands
```bash
python3 Math/conjecture/legendre/tools/m3mod4_residual_mw_sieve.py \
  --mode r4 --prime-bound 0 --scan-bound 0 \
  --combine-primes 23,43,47,31,19,37,449,191,509,167,79,229,127,227,53,521 \
  --max-classes 1200000 --expect-prefix8-terminal-pair

python3 Math/conjecture/legendre/tools/m3mod4_residual_mw_sieve.py \
  --mode r5 --prime-bound 0 --scan-bound 0 \
  --combine-primes 23,43,47,31,19,37,229,191,449,509,227,127,521,53,167,79 \
  --max-classes 1200000 --expect-prefix8-terminal-pair
```
assert this result directly.  Thus the residual problem is no longer a broad
CRT sieve problem: it is the global task of excluding one opposite pair of
rank-\(3\) Mordell-Weil classes.

The corresponding rational representative is
\[
  P_0=2G_2+G_3+(0,0)
      =
      \left(\frac{10045}{9},-\frac{849520}{27}\right).
\]
So the final target can be written in the short coset form
\[
  P\in\pm P_0+1320E(\mathbf Q),
  \qquad
  x(P)=1845s^2,
\]
plus the separated \(R4\) or \(R5\) equations.

Added
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_residual\_coset\_integral\_points.magma}.
\]
This Magma target asks for integral points on \(E\), filters the two exact
cosets \(\pm P_0+1320E(\mathbf Q)\), and then applies the residual square
conditions.  It is narrower than the previous quartic and elliptic
IntegralPoints scripts because it uses the terminal Mordell-Weil pair
certificate directly.

At this stage, the local Mordell-Weil layer alone did not close the residual
fibers.  It left one exact opposite pair of cosets, later closed by the
\(3\)-adic argument recorded below.

Added the dedicated final-target note
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_residual\_global\_integral\_points\_target.md}.
\]
It records the exact theorem now needed:
\[
  P\in\pm P_0+1320E(\mathbf Q),\qquad x(P)=1845s^2,
\]
with the common square constraints and either the \(R4\) or \(R5\) terminal
pair, has no solution.  The visible boundary point
\[
  P=(1845,73800)=G_3+(0,0)
\]
comes from \(s=1\), but the terminal equations fail there because
\[
  1701-908=793,\qquad 1701-1004=697
\]
are nonsquares.

The Magma target now verifies the rank, torsion, coset representative, and
boundary point before calling `IntegralPoints(E)`.  This makes the remaining
gate explicitly global: success requires a complete integral-point
computation or a Mordell-Weil sieve with a height bound, not another
standalone residue search.

## Residual 3-adic coset closure

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_m3mod4\_residual\_3adic\_coset\_closure.md}.
\]

This closes the final residual Mordell-Weil coset pair without running
`IntegralPoints`.

At \(3\),
\[
  E:\quad y^2=x^3-128x^2-215865x=x(x-533)(x+405)
\]
has
\[
  \Delta=16(533\cdot405\cdot938)^2,\qquad v_3(\Delta)=8,
\]
and \(c_4\) is a \(3\)-adic unit.  Modulo \(3\),
\[
  y^2\equiv x^2(x+1),
\]
whose node has tangent cone
\[
  y^2-x^2=(y-x)(y+x).
\]
Thus \(E\) has split multiplicative reduction of type \(I_8\) at \(3\).
By the Tate uniformization, the quotient
\[
  E(\mathbf Q_3)/E_1(\mathbf Q_3)
\]
has exponent dividing
\[
  \operatorname{lcm}(8,\#\mathbf F_3^\times)=8.
\]
Since \(8\mid1320\),
\[
  1320E(\mathbf Q)\subset E_1(\mathbf Q_3).
\]

The residual coset representative satisfies
\[
  P_0=\left(\frac{10045}{9},-\frac{849520}{27}\right),
\]
so
\[
  v_3(x(P_0))=-2,\qquad v_3(y(P_0))=-3.
\]
Equivalently, the formal parameter
\[
  t(P_0)=-\frac{x(P_0)}{y(P_0)}
        =\frac{6027}{169904}
        \in3\mathbf Z_3,
\]
hence \(P_0\in E_1(\mathbf Q_3)\), and also \(-P_0\in E_1(\mathbf Q_3)\).
Therefore every point in
\[
  \pm P_0+1320E(\mathbf Q)
\]
lies in \(E_1(\mathbf Q_3)\).

But every nonzero affine point in \(E_1(\mathbf Q_3)\) has negative
\(3\)-adic \(x\)-valuation, while
\[
  x=1845s^2,\qquad s\in\mathbf Z,
\]
has \(v_3(x)\ge2\) for \(s\ne0\), and \(s=0\) gives the finite point
\((0,0)\), not the identity component \(E_1\).

Hence
\[
  \left(\pm P_0+1320E(\mathbf Q)\right)
  \cap
  \{P:x(P)=1845s^2,\ s\in\mathbf Z\}
  =
  \varnothing.
\]

The two residual terminal systems \(R4\) and \(R5\) had both already been
reduced to this opposite coset pair.  Therefore the residual \(R4/R5\)
endpoint fibers are closed before the separated terminal square filters are
needed.

Added the proof-status ledger
\[
  \texttt{Math/conjecture/legendre/legendre\_status\_after\_residual\_closure.md}.
\]
It records the precise consequence: the residual elliptic endpoint is closed,
but this is not yet a proof of Legendre.  Full closure still requires
eliminating the earlier primitive/multiple-of-three covering obstruction,
currently expressed as the coprime A-block pair-cover condition
\[
  \mathcal Q_{\rm cop}(m)\subseteq
  \bigcup_{(p_0,p_1)}C_{p_0,p_1}(m),
\]
with
\[
  t_0(q)^2\equiv-9m^2\pmod{p_0},
  \qquad
  t_1(q)^2\equiv-9m^2-1\pmod{p_1}.
\]
Each ordered pair contributes at most four classes modulo \(p_0p_1\), but a
global non-cover theorem, or a stronger descent replacing it, is still needed
for a complete Legendre proof.

Added the equation-level complete-proof gate
\[
  \texttt{Math/conjecture/legendre/legendre\_complete\_proof\_equation\_gate.md}.
\]
It records the remaining contradiction without simulation: a counterexample
must assign, for every complete coprime A-block \(q\), two distinct primes
\[
  p_0(q),p_1(q)\le3m
\]
with
\[
  p_0(q)\equiv1\pmod4,\qquad p_0(q)\nmid3m,
\]
\[
  p_1(q)\ge5,\qquad p_1(q)\ne p_0(q),
\]
satisfying
\[
  t_0(q)^2\equiv-9m^2\pmod{p_0(q)},
  \qquad
  t_1(q)^2\equiv-9m^2-1\pmod{p_1(q)}.
\]
Equivalently, for every such \(q\), one must have simultaneous
factorizations
\[
  9m^2+t_0(q)^2=\alpha_q\beta_q,\qquad
  9m^2+t_1(q)^2+1=\gamma_q\delta_q,
\]
with small certificate prime divisors in the two lower factors and
\[
  \gcd(9m^2+t_0(q)^2,\ 9m^2+t_1(q)^2+1)=1.
\]
The complete proof now requires proving that this oriented conic-product
cover cannot exist for any \(m\).

Added the exact repeated-pair collision lemma
\[
  \texttt{Math/conjecture/legendre/legendre\_pair\_collision\_equations.md}.
\]
If one ordered pair \((p_0,p_1)\) covers two distinct complete coprime
blocks \(q\ne r\), then, writing
\[
  t_0(s)=3s+\alpha_s,\qquad t_1(s)=3s+\beta_s,
\]
one must have
\[
  p_0\mid
  \bigl(3(q-r)+\alpha_q-\alpha_r\bigr)
  \bigl(3(q+r)+\alpha_q+\alpha_r\bigr),
\]
and
\[
  p_1\mid
  \bigl(3(q-r)+\beta_q-\beta_r\bigr)
  \bigl(3(q+r)+\beta_q+\beta_r\bigr).
\]
The proof is just subtraction and factorization of the two conic congruences.
After splitting by parity:

- if \(q\equiv r\pmod2\), each layer prime divides \(q-r\), or one of the
  mirror sums \(3(q+r)+2\), \(3(q+r)+4\);
- if \(q\not\equiv r\pmod2\), each layer prime divides
  \(3(q-r)+1\), \(3(q-r)-1\), or \(q+r+1\).

So repeated pair labels live only on explicit divisor hyperplanes.  This is
a genuine equation-level obstruction.  It still does not finish the proof by
itself, because a hypothetical cover might use many one-shot ordered pairs.
The exact remaining theorem is now a capacity statement: one-shot pairs plus
these collision hyperplanes cannot cover all of
\(\mathcal Q_{\rm cop}(m)\).

Added the fixed A-block anchor
\[
  \texttt{Math/conjecture/legendre/legendre\_Ablock\_anchor\_q0.md}.
\]
It proves that
\[
  q=0\in\mathcal Q_{\rm cop}(m)
  \qquad\text{for every }m\ge1.
\]
Indeed, if \(m\) is odd then
\[
  t_1(0)=1,\qquad t_0(0)=2,
\]
and if \(m\) is even then
\[
  t_1(0)=2,\qquad t_0(0)=1.
\]
The completeness inequalities are immediate, and the coprime condition is
\[
  \gcd(t_1(0),9m^2+1)=1.
\]

Therefore any counterexample must already cover the first block.  The
boundary systems are:
\[
  m\text{ odd}:\quad
  9m^2+4,\ 9m^2+2
  \text{ both have eligible small prime certificates},
\]
and
\[
  m\text{ even}:\quad
  9m^2+1,\ 9m^2+5
  \text{ both have eligible small prime certificates}.
\]
Combining this anchor with the two-block collision equations makes all
repetitions against \(q=0\) live on the explicit linear forms
\[
  r,\quad 3r\pm1,\quad 3r+2,\quad 3r+4,\quad r+1.
\]

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_Ablock\_anchor\_pair\_nonrepetition.md}.
\]
This proves that the ordered pair covering \(q=0\) cannot cover any of
\[
  q=1,\quad q=2,\quad q=3.
\]
For odd \(m\), the collision divisibility candidates are
\[
\begin{array}{c|c|c}
 r & p_0 & p_1\\
 \hline
 1 & 2,\ 6 & 4,\ 6\\
 2 & 6,\ 10 & 6,\ 8\\
 3 & 8,\ 12 & 10,\ 12,
\end{array}
\]
and for even \(m\),
\[
\begin{array}{c|c|c}
 r & p_0 & p_1\\
 \hline
 1 & 4,\ 6 & 2,\ 6\\
 2 & 6,\ 8 & 6,\ 10\\
 3 & 10,\ 12 & 8,\ 12.
\end{array}
\]
Since \(p_0,p_1\ge5\), the only possible prime candidate in these small
divisor lists is \(5\), and no row contains \(5\) in both layers.  Therefore
the anchor pair is necessarily one-shot relative to the next three blocks.

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_first\_four\_ordered\_pair\_distinct.md}.
\]
This strengthens the previous anchor result.  Among the first four blocks,
the two coordinate sequences are
\[
  E=(2,4,8,10),
  \qquad
  O=(1,5,7,11).
\]
For \(E\), same-layer repetition by primes \(p\ge5\) can occur only on
\[
  (B_0,B_2)\text{ by }5,
  \qquad
  (B_1,B_3)\text{ by }7.
\]
For \(O\), same-layer repetition by primes \(p\ge5\) can occur only on
\[
  (B_0,B_3)\text{ by }5.
\]
If \(m\) is even, A0 uses \(O\) and A1 uses \(E\); if \(m\) is odd, A0 uses
\(E\) and A1 uses \(O\).  The possible repetition block pairs are therefore
disjoint between the two layers.  Hence no ordered pair \((p_0,p_1)\) can
cover two distinct coprime blocks among
\[
  B_0,B_1,B_2,B_3.
\]
Thus, when these four blocks are complete and coprime, any counterexample
must use four distinct ordered prime pairs on them.

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_first\_five\_ordered\_pair\_repetition.md}.
\]
For the first five coordinate sequences
\[
  E_5=(2,4,8,10,14),
  \qquad
  O_5=(1,5,7,11,13),
\]
the same-layer repetitions are:
\[
\begin{array}{c|c}
E_5 & (B_0,B_2):5,\ (B_1,B_3):7,\ (B_1,B_4):5,\ (B_2,B_4):11\\
O_5 & (B_0,B_3):5,\ (B_0,B_4):7,\ (B_2,B_4):5.
\end{array}
\]
The only common block pair is \((B_2,B_4)\).  If \(m\) is odd, this would
put \(p_0=11\) in A0, impossible because A0 primes must be \(1\bmod4\).
If \(m\) is even, the only possible ordered-pair repetition is
\[
  (B_2,B_4)\quad\text{by}\quad(p_0,p_1)=(5,11),
\]
and it requires
\[
  m^2\equiv4\pmod5,\qquad m^2\equiv5\pmod{11}.
\]
Therefore the first five coprime blocks require either five distinct ordered
pairs, or four distinct ordered pairs plus this single explicit \((5,11)\)
collision.

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_first\_six\_ordered\_pair\_repetition.md}.
\]
For
\[
  E_6=(2,4,8,10,14,16),
  \qquad
  O_6=(1,5,7,11,13,17),
\]
the common block pairs in the two repetition graphs are
\[
  (B_1,B_5),\quad (B_2,B_4),\quad (B_3,B_5),\quad (B_4,B_5).
\]
After imposing the A0 condition \(p_0\equiv1\pmod4\), the coprime-block
condition \(p_0\ne p_1\), and the value congruences, only two ordered
repetition gates survive:
\[
\begin{array}{c|c|c|c}
  \text{parity of }m & \text{block pair} & (p_0,p_1) & \text{conditions}\\
  \hline
  \text{even} & (B_2,B_4) & (5,11) &
  m^2\equiv4\pmod5,\ m^2\equiv5\pmod{11}\\
  \text{odd} & (B_3,B_5) & (13,7) &
  m^2\equiv-1\pmod{13},\ m^2\equiv2\pmod7.
\end{array}
\]
The removed odd \((B_1,B_5):(5,11)\) candidate would force
\[
  m^2\equiv2\pmod{11},
\]
but \(2\) is not a square modulo \(11\).

Outside these gates, the first six coprime complete blocks require six
distinct ordered pairs.

## Global Mobius-dual gate

Added
\[
  \texttt{Math/conjecture/legendre/legendre\_global\_mobius\_dual\_gate.md}.
\]

This is the pivot away from increasing the number of initial blocks.
For fixed \(m\), define the eligible small-prime kernels
\[
  K_0(m)=
  \prod_{\substack{p\le3m\\p\equiv1\pmod4\\p\nmid3m}}p
\]
and
\[
  K_1(m)=
  \prod_{\substack{p\le3m\\p\nmid 9m^2+1\\
  \left(\frac{-9m^2-1}{p}\right)=1}}p.
\]
For complete coprime A-blocks, define exact Mobius detectors
\[
  \Delta_0(q)=
  \sum_{\substack{d\mid K_0(m)\\d\mid G_q}}\mu(d),
  \qquad
  \Delta_1(q)=
  \sum_{\substack{e\mid K_1(m)\\e\mid U_q}}\mu(e).
\]
Then \(\Delta_0(q)=1\) means \(G_q\) has no eligible small divisor, and
\(\Delta_1(q)=1\) means \(U_q\) has no eligible small divisor.  Since both
values lie between \(9m^2\) and \((3m+1)^2\), this is exactly primality in
the corresponding A-channel.

Thus the remaining A-channel closure is equivalent to proving
\[
  Z(m)>0\qquad(m\ge1),
\]
where
\[
  Z(m)=
  \sum_{q\in\mathcal Q_{\rm cop}(m)}
  \bigl(\Delta_0(q)+\Delta_1(q)-\Delta_0(q)\Delta_1(q)\bigr).
\]
Equivalently, a counterexample forces the exact identity \(Z(m)=0\).

Expanding by divisors gives the global finite identity
\[
\begin{aligned}
  Z(m)
  &=
  \sum_{d\mid K_0(m)}\mu(d)N_G(d;m)
  +
  \sum_{e\mid K_1(m)}\mu(e)N_U(e;m)\\
  &\quad
  -
  \sum_{\substack{d\mid K_0(m)\\e\mid K_1(m)}}
  \mu(d)\mu(e)N_{G,U}(d,e;m).
\end{aligned}
\]
The root counts are CRT counts for quadratic congruences.  This is now the
preferred non-local closure target: prove positivity of one global Mobius
quantity, rather than extending the local initial-block table indefinitely.

## Residual IntegralPoints certificate target, now superseded

Added
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_residual\_integral\_points.sage}.
\]

This was the direct exact closure script for the two remaining residual
prefix-\(8\) fibers before the \(3\)-adic coset closure was found.  It works
on the certified elliptic curve
\[
  E:\quad Y^2=X^3-128X^2-215865X
\]
with the mwrank basis
\[
  (-363,3696),\quad(-195,5460),\quad(-117,4680),
\]
asks Sage for all integral points on \(E\), and filters them by
\[
  X=1845s^2
\]
and by the separated common/R4/R5 square equations.

The exact certificate expected from Sage would be:
\[
  \texttt{R4 candidates}=\varnothing,
  \qquad
  \texttt{R5 candidates}=\varnothing
\]
after the saturated boundary \(s=\pm1\).  This external computation is no
longer needed for the residual \(R4/R5\) closure, because the two surviving
Mordell-Weil cosets are already disjoint from \(x=1845s^2\) over
\(\mathbf Z_3\).

I also checked the tempting shortcut: direct \(p\)-adic lifting in \(s\)
with the full separated terminal equations does not kill either fiber for
the small primes tested.  Both R4 and R5 survive modulo
\[
  3^8,5^6,7^6,11^6,13^5,17^5,19^5,23^5,
  29^4,31^4,37^4,41^4,43^4,47^4.
\]
This failed shortcut explains why the successful closure had to use the
Mordell-Weil coset position itself, not only the separated equations in the
parameter \(s\).

So neither survivor gives a positive hard-branch point.  Therefore:
\[
\boxed{
  \text{structural prefix }7\text{ is closed.}
}
\]

The next prefix is qualitatively different: prefix \(8\) has new local
survivors beyond the two \(m=-1\) ghost fibers, including fibers passing
through the small positive class \(m=3\).  Those are boundary exceptions to
analyze algebraically, not evidence for closure.
