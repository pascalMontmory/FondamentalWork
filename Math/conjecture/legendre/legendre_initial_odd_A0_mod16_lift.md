# Initial Odd A0 Mod-16 Lift

This note sharpens the odd branch on the A0 side.

The previous odd A1 mod-\(24\) lift made the A1 quotient classes very sparse.
There is one remaining A0 refinement in the branch
\[
  m\equiv3\pmod4.
\]

Reducing the A0 half-quotient equation modulo \(16\) raises the third A0
minimum in that branch from \(20\) to \(28\).

## 1. Odd A0 half-quotient equation

Write
\[
  e=2f.
\]

For A0,
\[
  c=x^2,
\]
and the reduced equation is
\[
\boxed{
  u^2=f^2+6mf-x^2,
  \qquad
  u=r+f.
}
\]

In the odd branch, the A0 coordinates are
\[
  x=2,4,8,10.
\]

Thus there are two coordinates with
\[
  x^2\equiv0\pmod{16},
\]
and two with
\[
  x^2\equiv4\pmod{16}.
\]

The corrected A0 cofactor mirror gives
\[
  e\equiv4\text{ or }8\pmod{12},
\]
so
\[
  f\pmod{24}\in\{2,4,8,10,14,16,20,22\}.
\]

Since \(m\) is odd, \(A\) is odd.  The A0 label is odd, hence \(r\) is even.
Also \(f\) is even, so \(u\) is even and
\[
  u^2\equiv0\text{ or }4\pmod{16}.
\]

## 2. The modulo-\(16\) table

The exact congruence
\[
  f^2+6mf-x^2\in\{0,4\}\pmod{16}
\]
gives:
\[
\boxed{
\begin{array}{c|c|c}
  m\bmod8 & x^2\bmod16 & e\bmod48\\
  \hline
  1 & 0 & 4,\ 16,\ 20,\ 32\\
  1 & 4 & 8,\ 28,\ 40,\ 44\\
  3 & 0 & 16,\ 28,\ 32,\ 44\\
  3 & 4 & 4,\ 8,\ 20,\ 40\\
  5 & 0 & 4,\ 16,\ 20,\ 32\\
  5 & 4 & 8,\ 28,\ 40,\ 44\\
  7 & 0 & 16,\ 28,\ 32,\ 44\\
  7 & 4 & 4,\ 8,\ 20,\ 40
\end{array}
}
\]

## 3. Consequences by odd branch

### The branch \(m\equiv1\pmod4\)

This means
\[
  m\equiv1\text{ or }5\pmod8.
\]

The A0 minima remain
\[
\boxed{
  4,\ 8,\ 16,\ 20.
}
\]

Combined with the A1 mod-\(24\) minima
\[
  6,\ 30,\ 54,\ 78,
\]
the global quotient skeleton remains
\[
\boxed{
  M^{1\bmod4}=(4,6,8,16,20,30,54,78).
}
\]

### The branch \(m\equiv3\pmod4\)

This means
\[
  m\equiv3\text{ or }7\pmod8.
\]

The A0 minima become
\[
\boxed{
  4,\ 8,\ 16,\ 28.
}
\]

Combined with the A1 mod-\(24\) minima
\[
  18,\ 42,\ 66,\ 90,
\]
the global quotient skeleton is sharpened to
\[
\boxed{
  M^{3\bmod4}_{\mathrm{sharp}}
  =
  (4,8,16,18,28,42,66,90).
}
\]

This replaces the previous weaker skeleton
\[
  (4,8,16,18,20,42,66,90).
\]

## 4. Status of the \(e\)-phase

After this lift, the \(e\)-phase has reached a finite exact residue
decomposition:

\[
\boxed{
\begin{array}{c|c}
  \text{residue branch} & \text{global quotient minima}\\
  \hline
  m\equiv0\pmod8 & 2,6,10,14,18,22,30,42\\
  m\equiv2\pmod8 & 2,10,14,22,30,42,78,90\\
  m\equiv4\pmod8 & 2,6,10,14,18,22,30,42\\
  m\equiv6\pmod8 & 2,6,10,14,18,22,54,66\\
  m\equiv1\pmod4 & 4,6,8,16,20,30,54,78\\
  m\equiv3\pmod4 & 4,8,16,18,28,42,66,90
\end{array}
}
\]

This does not prove Legendre.  It closes the quotient-refinement phase:
remaining progress must come from eliminating these six skeletons with the
fully colored ladder and the Pell synchronization equations, not from adding
more isolated \(e\)-congruences.
