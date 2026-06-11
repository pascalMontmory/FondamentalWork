# Initial A0 Cofactor Mirror

This note uses the complementary factor
\[
  A+r+e
\]
in the centered A0 factorization.  This is stronger than looking only at the
small prime label
\[
  A-r
\]
and the quotient residue \(e\bmod6\).

The result is an exact \(4\)-adic lift for A0 quotients:
\[
  \mathrm{A0}:\qquad e\equiv4\text{ or }8\pmod{12}.
\]

## 1. A0 complementary factor

For an A0 offset
\[
  c=x^2,
\]
the centered factorization is
\[
  A^2+x^2=(A-r)(A+r+e).
\]

The small factor
\[
  p=A-r
\]
is an A0 label, so the Gaussian restriction gives
\[
  p\equiv1\pmod4.
\]

In the initial cluster the value
\[
  A^2+x^2
\]
is odd and congruent to
\[
  1\pmod4.
\]

Therefore the complementary factor
\[
  Q=A+r+e
\]
also satisfies
\[
\boxed{
  Q\equiv1\pmod4.
}
\]

Since
\[
  e=Q-p,
\]
we get
\[
\boxed{
  e\equiv0\pmod4.
}
\]

This is a new A0 restriction: the hidden cofactor gap is divisible by \(4\).

## 2. Combining with the mod-\(6\) lattice

The mod-\(6\) quotient lattice already gave
\[
  \mathrm{A0}:\qquad e\equiv2\text{ or }4\pmod6.
\]

Together with
\[
  e\equiv0\pmod4,
\]
this sharpens to
\[
\boxed{
  \mathrm{A0}:\qquad e\equiv8\text{ or }4\pmod{12}.
}
\]

Equivalently:
\[
\boxed{
  \begin{array}{c|c|c}
    e\bmod12 & e\bmod6 & \text{A0 label class}\\
    \hline
    8 & 2 & p\equiv1\pmod{12}\\
    4 & 4 & p\equiv5\pmod{12}
  \end{array}
}
\]

The A0 color should therefore be upgraded from
\[
  \chi\in\{2,4\}\pmod6
\]
to the sharper cofactor color
\[
\boxed{
  \gamma\in\{4,8\}\pmod{12}.
}
\]

## 3. A0 color-rank forcing

For an A0 offset \(i\), let
\[
  \gamma_i\in\{4,8\}
\]
be its cofactor color.  Define the same-color A0 quotient rank
\[
\boxed{
  \kappa_i
  =
  1+
  \#\{j:\ j\text{ is A0},\ \gamma_j=\gamma_i,\ q_j<q_i\}.
}
\]

Positive integers in the class
\[
  \gamma_i\pmod{12}
\]
are
\[
  \gamma_i,\ \gamma_i+12,\ \gamma_i+24,\dots.
\]

Therefore
\[
\boxed{
  e_i\ge \gamma_i+12(\kappa_i-1).
}
\]

This replaces the weaker A0 color-rank bound
\[
  e_i\ge\chi_i+6(\kappa_i-1).
\]

## 4. Lifted global quotient lattice

The four A0 quotients are distinct and lie in
\[
  4,8\pmod{12}.
\]

The smallest possible four A0 quotients, allowing both cofactor colors, are
\[
\boxed{
  4,\ 8,\ 16,\ 20.
}
\]

The four A1 quotients remain distinct positive multiples of \(6\), with
smallest possible values
\[
\boxed{
  6,\ 12,\ 18,\ 24.
}
\]

Thus the globally sorted quotient tuple satisfies the componentwise bound
\[
\boxed{
  e_{(1)},\dots,e_{(8)}
  \ge
  4,\ 6,\ 8,\ 12,\ 16,\ 18,\ 20,\ 24.
}
\]

Define
\[
\boxed{
  M^\ast=(4,6,8,12,16,18,20,24).
}
\]

This removes the previously allowed small quotient classes
\[
  e=2,\qquad e=10
\]
from the clean strong-gate quotient skeleton.

## 5. Cofactor-mirrored quotient barrier

If an offset has global quotient rank
\[
  q_i=k,
\]
then the global lattice gives
\[
  e_i\ge M^\ast_k.
\]

For A0, the same-color cofactor rank gives the additional lower bound
\[
  e_i\ge \gamma_i+12(\kappa_i-1).
\]

For A1, the layer rank still gives
\[
  e_i\ge6\lambda_i.
\]

Define
\[
  E_i^\ast(q,\gamma)
  =
  \begin{cases}
    \max\{M^\ast_{q_i},\ \gamma_i+12(\kappa_i-1)\},
      & i\text{ in A0},\\
    \max\{M^\ast_{q_i},\ 6\lambda_i\},
      & i\text{ in A1}.
  \end{cases}
\]

Then
\[
\boxed{
  e_i\ge E_i^\ast(q,\gamma).
}
\]

The distance barrier becomes
\[
\boxed{
  r_i\ge
  \mathcal B_{E_i^\ast(q,\gamma)}(A),
}
\]
where
\[
  \mathcal B_E(A)
  =
  \left\lceil
    \frac{-E+\sqrt{E^2+4(EA-122)}}{2}
  \right\rceil.
\]

## 6. Why this is a closure path

The clean strong-gate certificate now has a cofactor mirror:

- A0 label class modulo \(4\) forces the complementary factor modulo \(4\);
- this forces \(e\equiv0\pmod4\);
- combined with the layer quotient lattice, A0 quotients live in
  \(4,8\bmod12\);
- the global quotient skeleton loses \(e=2\) and \(e=10\);
- A0 same-color ranks progress by \(12\), not by \(6\).

This is a genuine closure direction because it attacks both factors in
\[
  A^2+x^2=(A-r)(A+r+e),
\]
not just the small prime label.  The next exact target is to insert
\[
  E_i^\ast(q,\gamma)
\]
into the fully colored ladder and the Pell synchronization equations, then
eliminate the cofactor-mirrored certificates.
