# \(m\equiv3\pmod4\) Modulo 7 Zero-Quotient Filter

This note strengthens the previous modulo \(7\) elimination of the first
minimal component.

The earlier certificate killed the single boundary value \(f=14\) in the
\(x^2\equiv0\pmod{16}\) A0 layer.  The actual mechanism is more structural:
for most offsets, any quotient with \(7\mid f\) is impossible.

## 1. The reduced line

In the hard odd branch
\[
  A=3m,\qquad m\equiv3\pmod4,
\]
the quotient pencil is
\[
\boxed{
  u^2=f^2+6mf-c.
}
\]

Reduce this equation modulo \(7\).  If
\[
  f\equiv0\pmod7,
\]
then both \(f^2\) and \(6mf\) vanish modulo \(7\).  Hence any solution must
satisfy
\[
\boxed{
  u^2\equiv -c\pmod7.
}
\]

The square classes modulo \(7\) are
\[
  \{0,1,2,4\}.
\]

Therefore:
\[
\boxed{
  7\mid f
  \quad\Longrightarrow\quad
  -c\in\{0,1,2,4\}\pmod7.
}
\]

Equivalently, since the eight offsets are
\[
  \mathcal C=
  \{2,4,16,26,50,64,100,122\},
\]
we have the following table.

\[
\begin{array}{c|c|c|c}
  c & c\bmod7 & -c\bmod7 & 7\mid f\text{ allowed?}\\
  \hline
  2   & 2 & 5 & \text{no}\\
  4   & 4 & 3 & \text{no}\\
  16  & 2 & 5 & \text{no}\\
  26  & 5 & 2 & \text{yes}\\
  50  & 1 & 6 & \text{no}\\
  64  & 1 & 6 & \text{no}\\
  100 & 2 & 5 & \text{no}\\
  122 & 3 & 4 & \text{yes}
\end{array}
\]

Thus only the two A1 offsets
\[
\boxed{
  c=26,\ 122
}
\]
can carry a quotient with \(7\mid f\).

## 2. Consequence for the A0 zero-square sublayer

The A0 offsets with
\[
  x^2\equiv0\pmod{16}
\]
are
\[
  c=16,\ 64.
\]

For both of them, the table gives
\[
  7\nmid f.
\]

Their permitted \(m\equiv3\pmod4\) residue classes before the modulo \(7\)
filter were
\[
  f\equiv8,14,16,22\pmod{24}.
\]

Inside these classes, the previously minimal value
\[
  f=14
\]
is forbidden because
\[
  14\equiv0\pmod7.
\]

The two smallest admissible distinct values in this sublayer are therefore
\[
\boxed{
  8,\ 16.
}
\]

So the A0 zero-square sublayer cannot contribute
\[
  8,\ 14.
\]
It must already climb to at least
\[
  8,\ 16.
\]

## 3. New minimal sorted skeleton

Recall the layer minima before the modulo \(7\) zero filter:

\[
\begin{array}{c|c|c}
  \text{layer} & \text{offsets} & \text{first values of }f\\
  \hline
  \mathrm{A0},\ x^2\equiv4\pmod{16}
    & 4,100
    & 2,4\\
  \mathrm{A0},\ x^2\equiv0\pmod{16}
    & 16,64
    & 8,14\\
  \mathrm{A1}
    & 2,26,50,122
    & 9,21,33,45
\end{array}
\]

The modulo \(7\) zero filter changes only the second row at the first
boundary:
\[
  8,14
  \quad\leadsto\quad
  8,16.
\]

Hence every surviving point of the hard branch must satisfy the sharper
sorted lower bound
\[
\boxed{
  f_{(1)},\dots,f_{(8)}
  \ge
  2,4,8,9,16,21,33,45.
}
\]

Equivalently, in the original quotient variable \(e=2f\),
\[
\boxed{
  e_{(1)},\dots,e_{(8)}
  \ge
  4,8,16,18,32,42,66,90.
}
\]

This is a genuine lift of the quotient skeleton, not a numerical
observation.

## 4. Additional assignment restriction inside A1

The same table also constrains the A1 value
\[
  f=21.
\]

Since
\[
  21\equiv0\pmod7,
\]
this quotient can only be paired with offsets for which \(7\mid f\) is
allowed, namely
\[
\boxed{
  c=26\quad\text{or}\quad c=122.
}
\]

Therefore any boundary assignment using the four smallest A1 values
\[
  9,\ 21,\ 33,\ 45
\]
must place \(21\) on one of the two offsets
\[
  26,\ 122.
\]

This does not raise the sorted skeleton, but it cuts the rank-assignment
union by a factor of two and gives the next exact target: eliminate the
lifted boundary
\[
  f=(2,4,8,9,16,21,33,45)
\]
under the forced placement
\[
  f=21\longleftrightarrow c\in\{26,122\}.
\]

## 5. Status

The hard branch has moved from the naive minimal skeleton
\[
  (4,8,16,18,28,42,66,90)
\]
to the sharper skeleton
\[
\boxed{
  (4,8,16,18,32,42,66,90).
}
\]

The next proof target is no longer the old \(f=14\) component.  It is the
lifted boundary component:
\[
\boxed{
  f=(2,4,8,9,16,21,33,45),
  \qquad
  f=21\text{ attached to }c=26\text{ or }122.
}
\]

Any further local certificate should attack this lifted component directly.
