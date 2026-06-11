# A1 Dual Sign-Parity Law

This note records the first two-sided A1 consequence of the dual-factor gap
model.

Work in the hard branch
\[
  m\equiv3\pmod4,
  \qquad
  L=6m\equiv18\pmod{24}.
\]

For every A1 offset
\[
  c\in\{2,26,50,122\},
\]
the lower quotient satisfies
\[
  f_c\equiv9\pmod{12}.
\]

The upper factor is
\[
  F_c=f_c+L.
\]

Since
\[
  L\equiv18\pmod{24},
\]
one has
\[
\boxed{
  f_c\equiv1\pmod4,
  \qquad
  F_c\equiv3\pmod4.
}
\]

Both factors satisfy the same A1 splitting law:
\[
  u_c^2\equiv-c\pmod{f_c},
  \qquad
  u_c^2\equiv-c\pmod{F_c}.
\]

Thus the two factors live in the same quadratic-field splitting semigroup,
but with opposite signs modulo \(4\).

## 1. Prime-sign parity

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

This is independent of the offset.  The offset only determines which
primes \(q\equiv3\pmod4\) are allowed to appear.

## 2. Offset-specific allowed negative primes

For \(c=2\), the splitting law is
\[
  \left(\frac{-2}{q}\right)=1,
\]
so the allowed unramified primes are
\[
  q\equiv1,3\pmod8.
\]

The primes contributing to \(\Omega_3\) are therefore precisely the
unramified primes
\[
  q\equiv3\pmod8.
\]

For \(c=50=2\cdot5^2\), away from the ramified prime \(5\), the same
condition holds:
\[
  q\equiv1,3\pmod8.
\]

The ramified prime \(5\equiv1\pmod4\) does not contribute to
\(\Omega_3\).

For \(c=26\) and \(c=122\), the ramified primes \(13\) and \(61\) are also
\[
  1\pmod4,
\]
so again they do not contribute to \(\Omega_3\).  The contributing primes
are the unramified primes
\[
  q\equiv3\pmod4
\]
that split in
\[
  \mathbb Q(\sqrt{-26})
  \quad\text{or}\quad
  \mathbb Q(\sqrt{-122}).
\]

## 3. The forced prime \(3\)

Every A1 lower quotient satisfies
\[
  3\mid f_c,
\]
and every A1 upper factor satisfies
\[
  3\mid F_c.
\]

The prime \(3\) is allowed for all A1 offsets because
\[
  c\equiv2\pmod3,
  \qquad
  -c\equiv1\pmod3.
\]

Since
\[
  3\equiv3\pmod4,
\]
the sign-parity law may be written after removing the forced prime \(3\):
\[
\boxed{
  v_3(f_c)+\Omega_3^{(\ne3)}(f_c)\equiv0\pmod2,
}
\]
and
\[
\boxed{
  v_3(F_c)+\Omega_3^{(\ne3)}(F_c)\equiv1\pmod2.
}
\]

Thus the non-\(3\) negative split primes must compensate the \(3\)-adic
parity of each factor.

## 4. Descent use

The A1 part of a hard-branch counterexample is no longer just:
\[
  f_c,\ F_c\ \text{split in }\mathbb Q(\sqrt{-c}).
\]

It is:
\[
\boxed{
  f_c\text{ has even negative-prime parity,}
  \qquad
  F_c\text{ has odd negative-prime parity,}
}
\]
inside the same splitting field, with common gap
\[
  F_c-f_c=L.
\]

Therefore any A1 descent must track not only which primes split, but also
the parity of the split primes lying over rational primes
\[
  3\pmod4.
\]

This gives an exact obstruction target:
\[
\boxed{
  \text{same-field split pair}
  +\text{opposite sign parity}
  +\text{common gap }L
  \Longrightarrow
  \text{rank descent or forbidden label.}
}
\]
