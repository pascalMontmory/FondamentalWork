# A0 Four-Layer Refinement

This note records the companion consequence of the A0 square-offset quotient
theorem for the A0 offsets
\[
  c=4,\ 100.
\]

These are the A0 offsets with
\[
  x^2\equiv4\pmod{16}.
\]

Before using the intrinsic quotient theorem, their hard-branch layer was
\[
\boxed{
  f\equiv2,4,10,20\pmod{24}.
}
\]

Unlike the zero layer \(c=16,64\), no whole class modulo \(24\) disappears.
However, the classes with \(4\mid f\) refine from modulo \(24\) to modulo
\(48\).

## 1. Intrinsic form

For \(c=4\), \(x=2\).  For \(c=100\), \(x=10\).  In both cases the A0
quotient theorem gives
\[
  v_2(f)\le3,
\]
and every odd prime divisor of \(f\) is \(1\bmod4\).

Inside the old layer
\[
  f\equiv2,4,10,20\pmod{24},
\]
one has
\[
  v_2(f)=1
  \quad\text{for}\quad
  f\equiv2,10\pmod{24},
\]
and
\[
  v_2(f)=2
  \quad\text{for}\quad
  f\equiv4,20\pmod{24}.
\]

Thus every admissible quotient is of one of the two forms
\[
\boxed{
  f=2s
  \quad\text{or}\quad
  f=4s,
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

In particular,
\[
  s\equiv1\pmod4.
\]

## 2. Refinement of the old classes

If
\[
  f=2s,
\]
then
\[
  s\equiv1\pmod4,
  \qquad
  3\nmid s,
\]
so
\[
  s\equiv1,5\pmod{12}.
\]
Therefore
\[
  f\equiv2,10\pmod{24}.
\]

This reproduces the old \(v_2(f)=1\) part exactly.

If
\[
  f=4s,
\]
then the same alternatives
\[
  s\equiv1,5\pmod{12}
\]
give
\[
\boxed{
  f\equiv4,20\pmod{48}.
}
\]

Hence the old classes
\[
  f\equiv4,20\pmod{24}
\]
were twice too large.  More explicitly:
\[
\boxed{
  f\equiv28,44\pmod{48}
  \quad\text{are impossible for }c=4,100.
}
\]

Indeed, these two classes correspond to
\[
  f=4s,
  \qquad
  s\equiv7,11\pmod{12},
\]
so
\[
  s\equiv3\pmod4,
\]
contradicting the A0 quotient theorem.

## 3. Refined layer

The exact A0 four-layer condition is therefore:
\[
\boxed{
  c=4,100
  \quad\Longrightarrow\quad
  f=2s\text{ or }4s,
  \quad
  s\text{ odd},\ 3\nmid s,\ q\mid s\Rightarrow q\equiv1\pmod4.
}
\]

Equivalently, at the residue level:
\[
\boxed{
  f\equiv2,10\pmod{24}
  \quad\text{or}\quad
  f\equiv4,20\pmod{48},
}
\]
with the remaining multiplicative restriction on the odd part.

## 4. Consequence for the rank game

The old A0 \(x^2\equiv4\pmod{16}\) layer was an additive lattice modulo
\(24\).  The intrinsic quotient theorem replaces it by two multiplicative
semigroups:
\[
  2\mathcal S
  \quad\text{and}\quad
  4\mathcal S,
\]
where
\[
  \mathcal S
  =
  \{s\ge1:\ s\text{ odd},\ 3\nmid s,\ q\mid s\Rightarrow q\equiv1\pmod4\}.
\]

The hard branch should therefore no longer be modeled by the three old
layer lattices.  It should be modeled by:

- \(2\mathcal S\cup4\mathcal S\) for \(c=4,100\);
- the zero-layer semigroups from the A0 zero-layer collapse for \(c=16,64\);
- the A1 quadratic-field splitting semigroups for \(c=2,26,50,122\).

This is the first full multiplicative replacement of the rank automaton.
