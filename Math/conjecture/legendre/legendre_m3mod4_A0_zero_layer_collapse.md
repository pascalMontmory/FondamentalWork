# A0 Zero-Layer Collapse

This note records the first immediate rank-descent consequence of the A0
square-offset quotient theorem.

It applies to the hard \(m\equiv3\pmod4\) branch and to the A0 offsets
\[
  c=16,\ 64.
\]

These are the A0 offsets with
\[
  x^2\equiv0\pmod{16}.
\]

Before applying the intrinsic quotient theorem, their quotient layer was
\[
\boxed{
  f\equiv8,14,16,22\pmod{24}.
}
\]

The A0 square-offset theorem collapses this to two classes.

## 1. Intrinsic form of A0 quotients

For \(c=x^2\), the self-residue condition is
\[
  u^2+x^2\equiv0\pmod f.
\]

For \(c=16\), \(x=4\), hence
\[
  v_2(f)\le5,
\]
and every odd prime divisor of \(f\) is \(1\bmod4\).

For \(c=64\), \(x=8\), hence
\[
  v_2(f)\le7,
\]
and again every odd prime divisor of \(f\) is \(1\bmod4\).

Thus in both cases
\[
\boxed{
  f=2^\nu s,
  \qquad
  s\ \text{odd},
  \qquad
  q\mid s\Rightarrow q\equiv1\pmod4.
}
\]

In particular,
\[
  s\equiv1\pmod4.
\]

## 2. Collapse of the old residue layer

Assume first
\[
  f\equiv14\pmod{24}.
\]

Then
\[
  v_2(f)=1,
  \qquad
  s=f/2\equiv7\pmod{12}.
\]

But
\[
  7\equiv3\pmod4,
\]
contradicting
\[
  s\equiv1\pmod4.
\]

Assume next
\[
  f\equiv22\pmod{24}.
\]

Then
\[
  v_2(f)=1,
  \qquad
  s=f/2\equiv11\pmod{12},
\]
so again
\[
  s\equiv3\pmod4,
\]
contradicting the A0 quotient theorem.

Therefore:
\[
\boxed{
  c=16,64
  \quad\Longrightarrow\quad
  f\not\equiv14,22\pmod{24}.
}
\]

Inside the old zero-layer lattice one is left with only
\[
\boxed{
  f\equiv8,16\pmod{24}.
}
\]

## 3. Exact allowed forms

The collapse can be written more sharply as:

\[
\begin{array}{c|c}
  c & \text{allowed form of }f\\
  \hline
  16
    & f=2^\nu s,\quad 3\le\nu\le5,\quad
      s\text{ odd},\ q\mid s\Rightarrow q\equiv1\pmod4\\
  64
    & f=2^\nu s,\quad 3\le\nu\le7,\quad
      s\text{ odd},\ q\mid s\Rightarrow q\equiv1\pmod4.
\end{array}
\]

The lower bound \(\nu\ge3\) is not an extra assumption.  It is forced by the
surviving residue classes
\[
  f\equiv8,16\pmod{24}.
\]

## 4. Consequence for the rank game

The previous rank automaton treated the A0 zero layer as a four-class
lattice:
\[
  8,\ 14,\ 16,\ 22
  \pmod{24}.
\]

The intrinsic quotient theorem proves that this was too large.  The classes
\[
  14,\ 22\pmod{24}
\]
are not exceptional fibers to eliminate by finite congruence certificates;
they are impossible for every skipped rank in the A0 zero layer.

In particular, the old first-escape move
\[
  16\leadsto22
\]
is now killed structurally, not just by the finite modulo-\(5\) certificate.

The hard branch should therefore be reparametrized with the zero-layer
semigroups above.  Any remaining counterexample must place the \(c=16\) and
\(c=64\) quotients inside those semigroups and still satisfy the pairwise
Pell synchronization equations.
