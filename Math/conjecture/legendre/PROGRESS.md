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
