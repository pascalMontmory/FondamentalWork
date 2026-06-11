# Initial A0 Spacing Envelope

This note strengthens the A0 tail constraints by using the fact that all A0
distances lie in one residue class modulo \(4\).

The previous A0 tail bound gave four ordered lower bounds.  Since the four
A0 distances are also distinct and congruent modulo \(4\), they must be
separated by at least \(4\).  This creates a sharper envelope.

## 1. Ordered A0 distances

Let the four A0 labels be sorted increasingly:
\[
  Q_1<Q_2<Q_3<Q_4.
\]

Write
\[
  Q_j=A-\rho_j.
\]

Then
\[
  \rho_1>\rho_2>\rho_3>\rho_4,
\]
because smaller labels correspond to larger distances.

The A0 congruence condition is
\[
  Q_j\equiv1\pmod4.
\]
Therefore
\[
  \rho_j\equiv A-1\pmod4
\]
for every \(j\).

Since the \(\rho_j\) are distinct and lie in the same residue class modulo
\[
  4,
\]
one has
\[
\boxed{
  \rho_j\ge \rho_\ell+4(\ell-j)
  \qquad(1\le j<\ell\le4).
}
\]

## 2. Combining with the A0 tail bounds

The A0 tail constraints gave
\[
  \rho_\ell\ge B_{5-\ell}(A)
  \qquad(1\le\ell\le4).
\]

Using the spacing inequality, for each \(j\):
\[
  \rho_j
  \ge
  B_{5-\ell}(A)+4(\ell-j)
  \qquad(\ell\ge j).
\]

Thus:
\[
\boxed{
  \rho_j\ge
  E_j(A):=
  \max_{j\le\ell\le4}
  \left(B_{5-\ell}(A)+4(\ell-j)\right).
}
\]

Explicitly:
\[
\boxed{
  E_4(A)=B_1(A),
}
\]
\[
\boxed{
  E_3(A)=\max\{B_2(A),\,B_1(A)+4\},
}
\]
\[
\boxed{
  E_2(A)=\max\{B_3(A),\,B_2(A)+4,\,B_1(A)+8\},
}
\]
\[
\boxed{
  E_1(A)=\max\{B_4(A),\,B_3(A)+4,\,B_2(A)+8,\,B_1(A)+12\}.
}
\]

Therefore the A0 labels satisfy the sharpened bounds
\[
\boxed{
  Q_j\le A-E_j(A)
  \qquad(1\le j\le4).
}
\]

## 3. When spacing is inactive

For large \(A\), the sequence \(B_k(A)\) grows roughly as
\[
  \sqrt{kA}.
\]
Hence the gaps
\[
  B_{k+1}(A)-B_k(A)
\]
eventually exceed \(4\).  In that range the spacing correction is inactive
and
\[
  E_j(A)=B_{5-j}(A).
\]

For smaller \(A\), the spacing terms
\[
  B_{5-\ell}(A)+4(\ell-j)
\]
can dominate.  The formula above is exact in all cases and keeps these
finite boundary effects explicit.

## 4. A0 center-divisor envelope

A clean strong-gate counterexample must therefore supply four A0 coordinate
distances
\[
  \rho_1>\rho_2>\rho_3>\rho_4
\]
such that:
\[
\boxed{
  \rho_j\equiv A-1\pmod4,
}
\]
\[
\boxed{
  \rho_j\ge E_j(A),
}
\]
and for the associated A0 offsets \(x^2\),
\[
\boxed{
  A-\rho_j\mid \rho_j^2+x^2,
}
\]
with
\[
  A-\rho_j
\]
prime.

This is the exact A0 spacing envelope.

## 5. Clean strong-gate consequence

The A0 layer is now constrained by:

1. four labels \(Q_j\equiv1\pmod4\);
2. four distances in the same class \(A-1\pmod4\);
3. spacing at least \(4\) between ordered distances;
4. the sharpened lower envelope
   \[
     \rho_j\ge E_j(A);
   \]
5. the four Gaussian divisor equations
   \[
     A-\rho_j\mid \rho_j^2+x^2.
   \]

This still does not close the clean strong gate.  It isolates the next
possible proof target: show that the four initial A0 square offsets cannot
meet this spacing envelope together with the divisor equations and the A1
compatibility conditions.
