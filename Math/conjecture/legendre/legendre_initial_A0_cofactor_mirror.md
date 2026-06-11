# Initial A0 Cofactor Mirror

This note uses the complementary factor
\[
  A+r+e
\]
in the centered A0 factorization.

It corrects an important point: the difference between the complementary
factor and the small factor is not \(e\), but
\[
  2r+e.
\]

Therefore the cofactor mirror is parity-sensitive.  It splits the clean
strong gate into two exact quotient lattices according to the parity of
\[
  m.
\]

## 1. Complementary factor congruence

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
is an A0 label, so
\[
  p\equiv1\pmod4.
\]

In the initial cluster,
\[
  A^2+x^2\equiv1\pmod4.
\]

Thus the complementary factor
\[
  Q=A+r+e
\]
also satisfies
\[
\boxed{
  Q\equiv1\pmod4.
}
\]

Subtracting the two factors gives
\[
  Q-p=(A+r+e)-(A-r)=2r+e.
\]

Hence
\[
\boxed{
  2r+e\equiv0\pmod4.
}
\]

This is the correct cofactor-mirror congruence.

## 2. Dependence on the parity of \(m\)

Since
\[
  A=3m,
\]
the parity of \(A\) is the parity of \(m\).

The A0 label condition
\[
  A-r\equiv1\pmod4
\]
gives
\[
  r\equiv A-1\pmod4.
\]

### Even \(m\)

If \(m\) is even, then \(A\) is even.  Therefore
\[
  r\equiv A-1\pmod4
\]
is odd, so
\[
  2r\equiv2\pmod4.
\]

The cofactor mirror
\[
  2r+e\equiv0\pmod4
\]
then gives
\[
\boxed{
  e\equiv2\pmod4.
}
\]

Combining with the A0 mod-\(6\) quotient lattice
\[
  e\equiv2\text{ or }4\pmod6
\]
gives
\[
\boxed{
  m\text{ even},\ \mathrm{A0}:
  \qquad
  e\equiv2\text{ or }10\pmod{12}.
}
\]

### Odd \(m\)

If \(m\) is odd, then \(A\) is odd.  Therefore
\[
  r\equiv A-1\pmod4
\]
is even, so
\[
  2r\equiv0\pmod4.
\]

The cofactor mirror gives
\[
\boxed{
  e\equiv0\pmod4.
}
\]

Combining with the A0 mod-\(6\) quotient lattice gives
\[
\boxed{
  m\text{ odd},\ \mathrm{A0}:
  \qquad
  e\equiv4\text{ or }8\pmod{12}.
}
\]

## 3. Parity-sensitive quotient skeletons

A1 quotients remain positive multiples of \(6\).  Their four smallest
distinct values are
\[
  6,\ 12,\ 18,\ 24.
\]

For A0, the cofactor mirror gives different residue classes according to
the parity of \(m\).

### Even \(m\)

A0 quotients lie in
\[
  2,\ 10\pmod{12}.
\]

The four smallest possible A0 quotients are
\[
  2,\ 10,\ 14,\ 22.
\]

Together with the A1 minima, the globally sorted quotient tuple satisfies
\[
\boxed{
  e_{(1)},\dots,e_{(8)}
  \ge
  2,\ 6,\ 10,\ 12,\ 14,\ 18,\ 22,\ 24.
}
\]

Define
\[
\boxed{
  M^{\mathrm{even}}=(2,6,10,12,14,18,22,24).
}
\]

### Odd \(m\)

A0 quotients lie in
\[
  4,\ 8\pmod{12}.
\]

The four smallest possible A0 quotients are
\[
  4,\ 8,\ 16,\ 20.
\]

Together with the A1 minima, the globally sorted quotient tuple satisfies
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
  M^{\mathrm{odd}}=(4,6,8,12,16,18,20,24).
}
\]

## 4. Cofactor colors

The A0 cofactor color must now include the parity branch.

For even \(m\):
\[
\boxed{
  \gamma_i\in\{2,10\}\pmod{12}.
}
\]

For odd \(m\):
\[
\boxed{
  \gamma_i\in\{4,8\}\pmod{12}.
}
\]

If \(\kappa_i\) is the same-color A0 quotient rank, then in both branches
\[
\boxed{
  e_i\ge \gamma_i+12(\kappa_i-1).
}
\]

The A1 layer-rank bound remains
\[
\boxed{
  e_i\ge6\lambda_i.
}
\]

## 5. Corrected cofactor-mirrored barrier

Let
\[
  M^\parity
  =
  \begin{cases}
    M^{\mathrm{even}}, & m\text{ even},\\
    M^{\mathrm{odd}}, & m\text{ odd}.
  \end{cases}
\]

For an offset \(i\), define
\[
  E_i^\parity(q,\gamma)
  =
  \begin{cases}
    \max\{M^\parity_{q_i},\ \gamma_i+12(\kappa_i-1)\},
      & i\text{ in A0},\\
    \max\{M^\parity_{q_i},\ 6\lambda_i\},
      & i\text{ in A1}.
  \end{cases}
\]

Then
\[
\boxed{
  e_i\ge E_i^\parity(q,\gamma).
}
\]

The distance barrier is
\[
\boxed{
  r_i\ge
  \mathcal B_{E_i^\parity(q,\gamma)}(A),
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

## 6. Correct closure path

The cofactor mirror does not universally eliminate
\[
  e=2
\]
from the clean strong gate.  It eliminates it in the odd branch, but the even
branch keeps the A0 classes
\[
  2,\ 10\pmod{12}.
\]

This is still a useful closure path because it splits the certificate into
two different quotient skeletons:
\[
  M^{\mathrm{even}}=(2,6,10,12,14,18,22,24),
\]
\[
  M^{\mathrm{odd}}=(4,6,8,12,16,18,20,24).
\]

The next exact target is therefore parity-bifurcated:

> eliminate even and odd cofactor-mirrored certificates separately, with
> their own A0 cofactor colors, fully colored ladder envelopes, and Pell
> synchronization equations.

This corrected form is weaker than the overstrong universal \(e\equiv0\bmod4\)
claim, but it is mathematically exact and gives a genuine structural split.
