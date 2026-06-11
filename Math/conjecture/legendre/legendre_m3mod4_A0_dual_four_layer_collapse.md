# A0 Dual Four-Layer Collapse

This note strengthens the A0 four-layer refinement by using the upper factor
in the dual-factor gap model.

It applies in the hard branch
\[
  m\equiv3\pmod4,
  \qquad
  L=6m.
\]

Write
\[
  L=2h,
  \qquad
  h=3m.
\]

Since \(m\equiv3\pmod4\),
\[
\boxed{
  h\equiv1\pmod4.
}
\]

For the A0 offsets
\[
  c=4,\ 100,
\]
the previous four-layer refinement gave
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

In particular,
\[
\boxed{
  s\equiv1\pmod4.
}
\]

The dual-factor model introduces
\[
  F=f+L=f+2h.
\]

Both \(f\) and \(F\) divide \(u^2+x^2\), with \(x=2\) or \(10\).  Therefore
every odd prime divisor of \(F\) must also be \(1\bmod4\).

## 1. The \(f=4s\) branch is impossible

Assume
\[
  f=4s.
\]

Then
\[
  F=f+2h=4s+2h=2(2s+h).
\]

Because
\[
  s\equiv1\pmod4,
  \qquad
  h\equiv1\pmod4,
\]
the odd part of \(F\) satisfies
\[
  2s+h\equiv2\cdot1+1\equiv3\pmod4.
\]

But every odd prime divisor of \(F\) is \(1\bmod4\).  Hence the odd part of
\(F\) must be \(1\bmod4\), contradiction.

Therefore:
\[
\boxed{
  c=4,100
  \quad\Longrightarrow\quad
  f\ne4s.
}
\]

Equivalently, the entire lower-factor branch
\[
  f\equiv4,20\pmod{48}
\]
is impossible.

## 2. The surviving branch

If
\[
  f=2s,
\]
then
\[
  F=f+2h=2(s+h).
\]

Since
\[
  s\equiv h\equiv1\pmod4,
\]
one has
\[
  s+h\equiv2\pmod4.
\]

Thus
\[
  v_2(F)=2.
\]

Write
\[
  F=4t,
  \qquad
  t=\frac{s+h}{2}.
\]

The dual-factor splitting law requires
\[
  t\text{ odd},
  \qquad
  3\nmid t,
  \qquad
  q\mid t\Rightarrow q\equiv1\pmod4.
\]

So the surviving same-gap condition is:
\[
\boxed{
  f=2s,\quad
  F=4t,\quad
  F-f=L,\quad
  s,t\in\mathcal S_4.
}
\]

Equivalently,
\[
\boxed{
  c=4,100
  \quad\Longrightarrow\quad
  f\in2\mathcal S_4
}
\]
and the upper partner lies in
\[
\boxed{
  F\in4\mathcal S_4.
}
\]

## 3. Consequence for the rank skeleton

The old A0 \(x^2\equiv4\pmod{16}\) lower layer was
\[
  f\equiv2,4,10,20\pmod{24}.
\]

The first refinement reduced it to
\[
  2\mathcal S_4\cup4\mathcal S_4.
\]

The dual-factor argument collapses it further:
\[
\boxed{
  2\mathcal S_4\cup4\mathcal S_4
  \quad\longrightarrow\quad
  2\mathcal S_4.
}
\]

Therefore the first two available distinct lower quotients for the pair
\[
  c=4,\ 100
\]
are no longer
\[
  2,\ 4,
\]
but
\[
\boxed{
  2,\ 10.
}
\]

Thus the old first-escape move
\[
  4\leadsto10
\]
is now structural.  It is not a finite-prime certificate phenomenon.

Combined with the A0 zero-layer collapse, both old A0 escape moves
\[
  4\leadsto10,
  \qquad
  16\leadsto22
\]
have been absorbed into the intrinsic quotient geometry.

The remaining hard-branch rank problem starts after this stronger A0
structural skeleton.
