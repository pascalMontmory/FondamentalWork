# Initial A1 Mod-6 Signed Ladder

This note extracts the A1 analogue of the A0 colored ladder.

For A0, the quotient class \(e\bmod6\) determines the label class modulo
\(12\).  For A1, every quotient satisfies
\[
  e\equiv0\pmod6,
\]
so the quotient class alone no longer separates the labels.  The missing
color is instead the sign of the reduced square root modulo \(3\).

## 1. A1 reduced pencil modulo \(3\)

Write
\[
  e=2f.
\]

For an A1 offset,
\[
  c=y^2+1,
\]
where the initial A1 coordinate \(y\) is not divisible by \(3\).  Hence
\[
  y^2\equiv1\pmod3,
  \qquad
  c\equiv2\pmod3.
\]

The reduced quotient pencil is
\[
\boxed{
  (r+f)^2=f^2+6mf-(y^2+1).
}
\]

The mod-\(6\) quotient lattice gives
\[
  3\mid f
\]
for A1.  Reducing modulo \(3\), we get
\[
  (r+f)^2\equiv -(y^2+1)\equiv -2\equiv1\pmod3.
\]

Thus
\[
\boxed{
  r+f\equiv\varepsilon\pmod3,
  \qquad
  \varepsilon\in\{1,-1\}.
}
\]

Since
\[
  f\equiv0\pmod3,
\]
this is
\[
\boxed{
  r\equiv\varepsilon\pmod3.
}
\]

The sign
\[
  \varepsilon\in\{1,-1\}
\]
is the A1 signed color.

## 2. A1 label class

The prime label is
\[
  p=A-r.
\]

Since
\[
  A=3m\equiv0\pmod3,
\]
we have
\[
\boxed{
  p\equiv-\varepsilon\pmod3.
}
\]

All A1 labels are odd primes.  Therefore the sign determines the label class
modulo \(6\):
\[
\boxed{
  \varepsilon=1
  \quad\Longrightarrow\quad
  p\equiv5\pmod6,
}
\]
and
\[
\boxed{
  \varepsilon=-1
  \quad\Longrightarrow\quad
  p\equiv1\pmod6.
}
\]

Thus the hidden root sign in the A1 quotient pencil determines the visible
A1 label class modulo \(6\).

In center-distance form,
\[
  p=A-D,
\]
so equal A1 signs force equal distance classes modulo \(6\).

## 3. Signed spacing

Let the A1 labels appear in global label order at positions
\[
  b_1<b_2<b_3<b_4.
\]

Attach to each A1 position its sign
\[
  \varepsilon_u\in\{1,-1\}.
\]

All A1 labels are odd, so the basic A1 ladder gives only
\[
\boxed{
  D_{b_u}\ge D_{b_{u+1}}+2
  \qquad(1\le u<4).
}
\]

But if two A1 positions have the same sign, then their labels are congruent
modulo \(6\).  Therefore their distances are congruent modulo \(6\), and
distinctness gives
\[
\boxed{
  D_{b_u}\ge D_{b_v}+6
}
\]
whenever
\[
  b_u<b_v,\qquad \varepsilon_u=\varepsilon_v,
\]
and no same-sign A1 position lies between them.

This is the A1 signed analogue of the A0 same-color spacing \(12\).

## 4. Fully colored ladder graph

A clean strong-gate ladder certificate should now carry:

- a layer word
  \[
    L\in\{0,1\}^8;
  \]
- an A0 quotient-color word
  \[
    \chi\in\{2,4\}^4;
  \]
- an A1 sign word
  \[
    \varepsilon\in\{1,-1\}^4.
  \]

The directed ladder graph receives:

1. global parity edges of weight \(2\);
2. ordinary A0 consecutive edges of weight \(4\);
3. same-color A0 edges of weight \(12\);
4. same-sign A1 edges of weight \(6\).

Let
\[
  W_{L,\chi,\varepsilon}(i,j)
\]
be the maximum path weight from \(i\) to \(j\) in this graph.

The fully colored envelope is
\[
\boxed{
  H_i^{L,\chi,\varepsilon}(A)
  =
  \max_{i\le j\le8}
  \left(\widehat B_{9-j}(A)+W_{L,\chi,\varepsilon}(i,j)\right).
}
\]

Every clean strong-gate certificate with \(m\ge4881\) satisfies
\[
\boxed{
  D_i\ge H_i^{L,\chi,\varepsilon}(A).
}
\]

## 5. Exact closure target

The clean strong gate has now been converted into a fully colored finite
certificate:

1. A0 colors from quotient classes \(e\equiv2,4\pmod6\);
2. A1 signs from roots \(r+f\equiv\pm1\pmod3\);
3. a global two-layer label order;
4. a matching from offsets to labels;
5. quotient ranks satisfying the mod-\(6\) quotient lattice;
6. the fully colored ladder envelope;
7. centered divisor equations and Pell synchronization.

The next exact target is:

> eliminate fully colored ladder certificates.

This is still not a search over \(m\).  The finite certificate now remembers
the visible residue class of every A0 and A1 prime label.
