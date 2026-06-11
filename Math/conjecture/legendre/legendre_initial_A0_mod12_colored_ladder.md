# Initial A0 Mod-12 Colored Ladder

This note extracts a coupling between the hidden A0 quotient class modulo
\(6\) and the visible A0 prime-label class modulo \(12\).

It strengthens the A0 part of the two-layer ladder: A0 distances are not
only congruent modulo \(4\); A0 labels whose quotients have the same
modulo-\(6\) color are congruent modulo \(12\), hence their distances are
spaced by at least \(12\).

## 1. A0 quotient-label coupling

For every initial quotient, write
\[
  e=2f.
\]

The reduced quotient pencil is
\[
\boxed{
  (r+f)^2=f^2+6mf-c.
}
\]

For an A0 offset,
\[
  c=x^2,
\]
where the initial A0 coordinate \(x\) is not divisible by \(3\).  Hence
\[
  x^2\equiv1\pmod3.
\]

Modulo \(3\), the reduced pencil becomes
\[
  (r+f)^2\equiv f^2-x^2\pmod3.
\]

The mod-\(6\) quotient lattice already showed that A0 quotients satisfy
\[
  3\nmid f.
\]
Thus
\[
  f^2\equiv x^2\equiv1\pmod3,
\]
so
\[
  (r+f)^2\equiv0\pmod3.
\]

Therefore
\[
\boxed{
  r\equiv -f\pmod3.
}
\]

The prime label is
\[
  p=A-r.
\]
Since
\[
  A=3m\equiv0\pmod3,
\]
we get
\[
\boxed{
  p\equiv f\pmod3.
}
\]

Because
\[
  e=2f,
\]
this gives the exact table
\[
\boxed{
  \begin{array}{c|c|c}
    e\bmod6 & f\bmod3 & p\bmod3\\
    \hline
    2 & 1 & 1\\
    4 & 2 & 2
  \end{array}
}
\]

## 2. Modulo \(12\) label classes

Every A0 label also satisfies the Gaussian restriction
\[
  p\equiv1\pmod4.
\]

Combining with the table above gives
\[
\boxed{
  e\equiv2\pmod6
  \quad\Longrightarrow\quad
  p\equiv1\pmod{12},
}
\]
and
\[
\boxed{
  e\equiv4\pmod6
  \quad\Longrightarrow\quad
  p\equiv5\pmod{12}.
}
\]

Thus the hidden quotient color determines the visible A0 label class.

In center-distance form,
\[
  p=A-D.
\]
So two A0 labels with the same quotient color have
\[
  D\equiv A-1\pmod{12}
  \quad\text{or}\quad
  D\equiv A-5\pmod{12}
\]
in common.

## 3. Colored spacing

Let the A0 labels appear in global label order at positions
\[
  a_1<a_2<a_3<a_4.
\]

Attach to each A0 position its quotient color
\[
  \chi_u\in\{2,4\},
  \qquad
  \chi_u\equiv e_{a_u}\pmod6.
\]

All A0 labels are \(1\bmod4\), so the usual A0 ladder gives
\[
\boxed{
  D_{a_u}\ge D_{a_{u+1}}+4
  \qquad(1\le u<4).
}
\]

But if two A0 positions have the same color, then their labels are congruent
modulo \(12\).  Therefore their distances are congruent modulo \(12\), and
distinctness gives a stronger spacing.

For consecutive occurrences of the same color in the A0 subsequence,
\[
  a_u<a_v,
  \qquad
  \chi_u=\chi_v,
\]
with no same-color A0 position between them, one has
\[
\boxed{
  D_{a_u}\ge D_{a_v}+12.
}
\]

This is a strict strengthening whenever equal A0 quotient colors recur.

## 4. Colored ladder graph

For a two-layer ladder certificate, the A0 part should now carry a color
word
\[
  \chi=(\chi_1,\chi_2,\chi_3,\chi_4)\in\{2,4\}^4.
\]

The ladder graph receives:

1. the global parity edges of weight \(2\);
2. the ordinary A0 consecutive edges of weight \(4\);
3. the same-color A0 edges of weight \(12\), between consecutive occurrences
   of each color in the A0 subsequence.

Let
\[
  W_{L,\chi}(i,j)
\]
be the maximum path weight in this colored ladder graph.

The word envelope becomes
\[
\boxed{
  H_i^{L,\chi}(A)
  =
  \max_{i\le j\le8}
  \left(\widehat B_{9-j}(A)+W_{L,\chi}(i,j)\right),
}
\]
where
\[
  \widehat B_k(A)
\]
is the mod-\(6\) quotient-rank barrier.

Thus every clean strong-gate certificate with \(m\ge4881\) satisfies
\[
\boxed{
  D_i\ge H_i^{L,\chi}(A).
}
\]

## 5. Exact closure target

The clean strong gate is now reduced to a smaller certificate language:

1. a layer word \(L\);
2. an A0 quotient-color word \(\chi\);
3. a layer-respecting matching from offsets to labels;
4. quotient ranks compatible with the layer-sensitive mod-\(6\) lattice;
5. distances satisfying the colored ladder envelope;
6. centered divisor equations and pairwise Pell synchronization.

The next exact target is:

> eliminate colored two-layer ladder certificates.

This is not a search over \(m\).  It is a finite structural obstruction:
same-color A0 quotients force mod-\(12\) label clustering, and that clustering
pushes the required labels farther below \(A\).
