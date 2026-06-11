# Initial A1 Spacing Envelope

This note projects the global label order-statistic barrier onto the A1
layer and strengthens it by parity spacing.

The A1 layer does not impose
\[
  p\equiv1\pmod4
\]
as A0 does.  However, all A1 labels are odd primes.  Therefore all A1
center-distances lie in one residue class modulo \(2\), so distinct A1
distances are spaced by at least \(2\).

## 1. Ordered A1 labels

Let the four A1 labels be sorted increasingly:
\[
  S_1<S_2<S_3<S_4.
\]

Among the first
\[
  j+4
\]
global labels, there must be at least \(j\) A1 labels, because there are only
four A0 labels total.  Hence
\[
\boxed{
  S_j\le P_{j+4}
  \qquad(1\le j\le4).
}
\]

Using the global label order-statistic barrier gives
\[
\boxed{
  S_j\le A-B_{5-j}(A)
  \qquad(1\le j\le4).
}
\]

## 2. A1 parity in center-distance form

Write
\[
  S_j=A-\sigma_j.
\]

Since every A1 label \(S_j\) is an odd prime,
\[
  S_j\equiv1\pmod2.
\]
Therefore
\[
\boxed{
  \sigma_j\equiv A-1\pmod2.
}
\]

The labels are sorted increasingly, so the distances are sorted decreasingly:
\[
  \sigma_1>\sigma_2>\sigma_3>\sigma_4.
\]

Because the \(\sigma_j\) are distinct and congruent modulo \(2\), one has
\[
\boxed{
  \sigma_j\ge\sigma_\ell+2(\ell-j)
  \qquad(1\le j<\ell\le4).
}
\]

## 3. A1 spacing envelope

The A1 tail constraints gave
\[
  \sigma_\ell\ge B_{5-\ell}(A)
  \qquad(1\le\ell\le4).
\]

Combining this with the parity spacing gives
\[
\boxed{
  \sigma_j\ge
  F_j(A):=
  \max_{j\le\ell\le4}
  \left(B_{5-\ell}(A)+2(\ell-j)\right).
}
\]

Explicitly:
\[
\boxed{
  F_4(A)=B_1(A),
}
\]
\[
\boxed{
  F_3(A)=\max\{B_2(A),\,B_1(A)+2\},
}
\]
\[
\boxed{
  F_2(A)=\max\{B_3(A),\,B_2(A)+2,\,B_1(A)+4\},
}
\]
\[
\boxed{
  F_1(A)=\max\{B_4(A),\,B_3(A)+2,\,B_2(A)+4,\,B_1(A)+6\}.
}
\]

Therefore the A1 labels satisfy
\[
\boxed{
  S_j\le A-F_j(A)
  \qquad(1\le j\le4).
}
\]

## 4. Offset-specific A1 divisor form

The A1 offsets have the form
\[
  c=y^2+1.
\]

For an A1 coordinate \(y\), the center-divisor condition is
\[
  A-\sigma\mid \sigma^2+y^2+1.
\]

The coprime-block condition excludes the hidden common-divisor case inside a
block, so the A1 label is genuinely separate from the A0 label in that same
block.

Thus a clean strong-gate counterexample forces four distinct A1 pairs
\[
  (y,\sigma_y)
\]
satisfying
\[
\boxed{
  A-\sigma_y\mid \sigma_y^2+y^2+1,
}
\]
\[
\boxed{
  \sigma_y\equiv A-1\pmod2,
}
\]
and the A1 spacing envelope above.

## 5. Clean strong-gate consequence

The A1 layer is constrained by:

1. four odd prime labels;
2. four distances in the single residue class \(A-1\pmod2\);
3. spacing at least \(2\) between ordered distances;
4. the lower envelope
   \[
     \sigma_j\ge F_j(A);
   \]
5. the four A1 divisor equations
   \[
     A-\sigma_j\mid \sigma_j^2+y^2+1.
   \]

Together with the A0 spacing envelope, this gives both layers their own
forced lower-tail profiles.  The next obstruction is to show that the two
profiles cannot be interleaved while preserving the cross-layer
compatibility equations.
