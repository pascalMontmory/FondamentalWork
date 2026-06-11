# Initial Even Mod-8 Quotient Lift

This note sharpens the even branch by reducing the half-quotient equations
modulo \(16\).

This is not a search over \(m\).  It is a finite residue calculation for the
four even classes
\[
  m\equiv0,2,4,6\pmod8.
\]

The main gain is on A1: two even classes force the A1 quotients into much
sparser classes modulo \(48\).

## 1. Even-branch coordinates

Assume
\[
  m\text{ is even}.
\]

Then the initial A0 coordinates are
\[
  x=1,5,7,11,
\]
and the initial A1 coordinates are
\[
  y=2,4,8,10.
\]

Thus:

- A0 has two coordinates with \(x^2\equiv1\pmod{16}\) and two with
  \(x^2\equiv9\pmod{16}\);
- A1 has two coordinates with \(y^2\equiv4\pmod{16}\) and two with
  \(y^2\equiv0\pmod{16}\).

Write
\[
  e=2f.
\]

Since \(m\) is even, \(A\) is even.  All labels are odd, so \(r\) is odd.
In both layers \(f\) is odd, hence
\[
  u=r+f
\]
is even, and
\[
  u^2\equiv0\text{ or }4\pmod{16}.
\]

## 2. A1 modulo \(16\)

For A1,
\[
  u^2=f^2+6mf-(y^2+1).
\]

The A1 cofactor mirror gives
\[
  e\equiv6\pmod{12},
\]
so
\[
  f\equiv3\pmod6.
\]

Equivalently,
\[
  f\pmod{24}\in\{3,9,15,21\}.
\]

Requiring the right-hand side to be \(0\) or \(4\bmod16\) gives the exact
table:
\[
\boxed{
\begin{array}{c|c|c}
  m\bmod8 & y^2\bmod16 & e\bmod48\\
  \hline
  0 & 0 & 18,\ 30\\
  0 & 4 & 6,\ 42\\
  2 & 0 & 30,\ 42\\
  2 & 4 & 30,\ 42\\
  4 & 0 & 6,\ 42\\
  4 & 4 & 18,\ 30\\
  6 & 0 & 6,\ 18\\
  6 & 4 & 6,\ 18
\end{array}
}
\]

This table is just the congruence
\[
  f^2+6mf-(y^2+1)\in\{0,4\}\pmod{16}
\]
with \(f\equiv3\pmod6\).

## 3. A1 minima by even class

There are two A1 coordinates of each \(y^2\bmod16\) type.

From the table, the four A1 quotient minima are:
\[
\boxed{
\begin{array}{c|c}
  m\bmod8 & \text{A1 quotient minima}\\
  \hline
  0 & 6,\ 18,\ 30,\ 42\\
  2 & 30,\ 42,\ 78,\ 90\\
  4 & 6,\ 18,\ 30,\ 42\\
  6 & 6,\ 18,\ 54,\ 66
\end{array}
}
\]

The classes \(m\equiv2,6\pmod8\) are therefore much more rigid than the
coarse \(6\bmod12\) A1 mirror.

## 4. A0 modulo \(16\)

For A0,
\[
  u^2=f^2+6mf-x^2.
\]

In the even branch, the corrected A0 cofactor mirror gives
\[
  e\equiv2\text{ or }10\pmod{12}.
\]

Thus
\[
  f\pmod{24}\in\{1,5,7,11,13,17,19,23\}.
\]

The exact modulo-\(16\) table is:
\[
\boxed{
\begin{array}{c|c|c}
  m\bmod8 & x^2\bmod16 & e\bmod48\\
  \hline
  0 & 1 & 2,\ 14,\ 34,\ 46\\
  0 & 9 & 10,\ 22,\ 26,\ 38\\
  2 & 1 & 10,\ 14,\ 26,\ 46\\
  2 & 9 & 2,\ 22,\ 34,\ 38\\
  4 & 1 & 10,\ 22,\ 26,\ 38\\
  4 & 9 & 2,\ 14,\ 34,\ 46\\
  6 & 1 & 2,\ 22,\ 34,\ 38\\
  6 & 9 & 10,\ 14,\ 26,\ 46
\end{array}
}
\]

This table preserves the A0 quotient minima
\[
  2,\ 10,\ 14,\ 22
\]
in every even class, but it assigns the allowed classes to the individual
A0 coordinate types.

## 5. Even-branch quotient skeletons

Combining A0 and A1 gives the following exact quotient skeletons:
\[
\boxed{
\begin{array}{c|c}
  m\bmod8 & \text{global quotient minima}\\
  \hline
  0 & 2,\ 6,\ 10,\ 14,\ 18,\ 22,\ 30,\ 42\\
  2 & 2,\ 10,\ 14,\ 22,\ 30,\ 42,\ 78,\ 90\\
  4 & 2,\ 6,\ 10,\ 14,\ 18,\ 22,\ 30,\ 42\\
  6 & 2,\ 6,\ 10,\ 14,\ 18,\ 22,\ 54,\ 66
\end{array}
}
\]

Thus:
\[
\boxed{
  m\equiv2\pmod8
  \quad\Longrightarrow\quad
  e_{(8)}\ge90,
}
\]
and
\[
\boxed{
  m\equiv6\pmod8
  \quad\Longrightarrow\quad
  e_{(8)}\ge66.
}
\]

The even branch is no longer a single case.  It splits into four quotient
skeletons, two of which are substantially stronger than the coarse even
cofactor skeleton.

## 6. Closure significance

Together with the odd mod-\(24\) lift, the clean strong gate now splits into
six residue skeletons:

- \(m\equiv0\pmod8\);
- \(m\equiv2\pmod8\);
- \(m\equiv4\pmod8\);
- \(m\equiv6\pmod8\);
- \(m\equiv1\pmod4\);
- \(m\equiv3\pmod4\).

The strongest cases force
\[
  e_{(8)}\ge90.
\]

The next exact target is no longer to improve a global bound on \(e\).  It is
to eliminate these six quotient skeletons one by one using the fully colored
ladder and the Pell synchronization equations.
