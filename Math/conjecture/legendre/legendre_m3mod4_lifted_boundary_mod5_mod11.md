# Lifted \(m\equiv3\pmod4\) Boundary Killed Modulo 5 and 11

This note eliminates the lifted boundary component left after the modulo
\(7\) zero-quotient filter.

It is not a search over \(m\).  It is a finite congruence certificate for the
exact reduced Pell lines
\[
  u^2=f^2+6mf-c.
\]

## 1. Target component

After the modulo \(7\) zero-quotient filter, the first surviving sorted
boundary is
\[
\boxed{
  f=(2,4,8,9,16,21,33,45).
}
\]

The offsets are
\[
  \{2,4,16,26,50,64,100,122\}.
\]

The layer rules are:

\[
\begin{array}{c|c|c}
  \text{layer} & \text{offsets} & \text{boundary }f\text{-values}\\
  \hline
  \mathrm{A0},\ x^2\equiv4\pmod{16}
    & 4,100
    & 2,4\\
  \mathrm{A0},\ x^2\equiv0\pmod{16}
    & 16,64
    & 8,16\\
  \mathrm{A1}
    & 2,26,50,122
    & 9,21,33,45
\end{array}
\]

The modulo \(7\) zero-quotient filter also gives
\[
\boxed{
  f=21\quad\text{must be attached to }c=26\text{ or }c=122.
}
\]

We prove that this lifted boundary has no integral point.

## 2. Modulo 5 rigidity

The square classes modulo \(5\) are
\[
  \{0,1,4\}.
\]

For each possible pairing, write \(M_5(c,f)\) for the set of residues
\[
  m\bmod5
\]
for which
\[
  f^2+6mf-c
\]
is a square modulo \(5\).

### A0, \(x^2\equiv4\pmod{16}\)

\[
\begin{array}{c|c|c}
  c & f & M_5(c,f)\\
  \hline
  4   & 2 & \{0,2,3\}\\
  4   & 4 & \{1,2,3\}\\
  100 & 2 & \{0,1,3\}\\
  100 & 4 & \{0,1,2\}
\end{array}
\]

Thus the two possible assignments give:
\[
\begin{array}{c|c}
  \text{assignment} & m\bmod5\\
  \hline
  c=4\mapsto2,\ c=100\mapsto4 & \{0,2\}\\
  c=4\mapsto4,\ c=100\mapsto2 & \{1,3\}
\end{array}
\]

### A0, \(x^2\equiv0\pmod{16}\)

\[
\begin{array}{c|c|c}
  c & f & M_5(c,f)\\
  \hline
  16 & 8  & \{1,2,4\}\\
  16 & 16 & \{0,1,4\}\\
  64 & 8  & \{0,2,3\}\\
  64 & 16 & \{2,3,4\}
\end{array}
\]

Thus the two possible assignments give:
\[
\begin{array}{c|c}
  \text{assignment} & m\bmod5\\
  \hline
  c=16\mapsto8,\ c=64\mapsto16 & \{2,4\}\\
  c=16\mapsto16,\ c=64\mapsto8 & \{0\}
\end{array}
\]

Combining the two A0 sublayers, the assignment
\[
  c=4\mapsto4,\quad c=100\mapsto2
\]
is impossible modulo \(5\), because
\[
  \{1,3\}\cap\{2,4\}
  =
  \{1,3\}\cap\{0\}
  =
  \varnothing.
\]

Therefore any lifted-boundary point must have
\[
\boxed{
  c=4\mapsto2,\qquad c=100\mapsto4.
}
\]

There are then two A0 possibilities:

\[
\begin{array}{c|c}
  \text{A0 zero-square assignment} & m\bmod5\\
  \hline
  c=16\mapsto8,\ c=64\mapsto16 & 2\\
  c=16\mapsto16,\ c=64\mapsto8 & 0
\end{array}
\]

The first line, \(m\equiv2\pmod5\), is incompatible with the A1 offset
\[
  c=2.
\]

Indeed, at \(c=2\):

- \(f=9\) allows \(m\equiv0,3,4\pmod5\);
- \(f=33\) allows \(m\equiv1,3,4\pmod5\);
- \(f=45\) allows no residue modulo \(5\);
- \(f=21\) is forbidden on \(c=2\) by the modulo \(7\) zero-quotient filter.

So no admissible A1 value can sit on \(c=2\) when
\[
  m\equiv2\pmod5.
\]

Hence the lifted boundary forces
\[
\boxed{
  m\equiv0\pmod5,
  \qquad
  c=16\mapsto16,
  \qquad
  c=64\mapsto8.
}
\]

Now \(m\equiv0\pmod5\) also forces the A1 assignment.

At \(m\equiv0\pmod5\):

- \(c=2\) can only receive \(f=9\);
- \(f=33\) can only be placed on \(c=50\);
- \(f=45\) cannot be placed on \(c=122\) and \(c=50\) is already occupied,
  so it must be placed on \(c=26\);
- the remaining value \(f=21\) is placed on \(c=122\), which is allowed by
  the modulo \(7\) zero-quotient filter.

Thus modulo \(5\) and the zero-quotient filter leave exactly one assignment:
\[
\boxed{
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 2 & 4 & 16 & 8 & 9 & 45 & 33 & 21
\end{array}
}
\]
with
\[
\boxed{
  m\equiv0\pmod5.
}
\]

## 3. The remaining assignment dies modulo 11

For the unique remaining assignment, reduce the same lines modulo \(11\).

The square classes modulo \(11\) are
\[
  \{0,1,3,4,5,9\}.
\]

For each row of the forced assignment, the admissible classes of \(m\bmod11\)
are:

\[
\begin{array}{c|c|c}
  c & f & M_{11}(c,f)\\
  \hline
  4   & 2  & \{0,1,3,4,5,9\}\\
  100 & 4  & \{0,4,5,6,8,9\}\\
  16  & 16 & \{0,2,3,5,9,10\}\\
  64  & 8  & \{0,1,3,4,5,9\}\\
  2   & 9  & \{1,2,4,8,9,10\}\\
  26  & 45 & \{1,2,3,5,6,8\}\\
  50  & 33 & \{0,1,2,3,4,5,6,7,8,9,10\}\\
  122 & 21 & \{0,1,3,4,5,9\}
\end{array}
\]

Intersect the first five nontrivial constraints:
\[
\begin{aligned}
&\{0,1,3,4,5,9\}
\cap \{0,4,5,6,8,9\}
\cap \{0,2,3,5,9,10\}\\
&\qquad\cap \{0,1,3,4,5,9\}
\cap \{1,2,4,8,9,10\}
=\{9\}.
\end{aligned}
\]

But the \(c=26,\ f=45\) row requires
\[
  m\bmod11\in\{1,2,3,5,6,8\},
\]
which does not contain \(9\).

Therefore the intersection of all eight \(M_{11}(c,f)\) is empty.

## 4. Exact conclusion

The lifted boundary component
\[
  f=(2,4,8,9,16,21,33,45)
\]
has no integral point in the \(m\equiv3\pmod4\) Pell system.

Equivalently:
\[
\boxed{
  \text{the first boundary after the modulo }7\text{ lift is killed by }
  (5,11).
}
\]

The next target is not a residue-class search over \(m\).  It is the finite
union obtained by raising at least one of the three layer boundaries:

\[
\begin{array}{c|c}
  \text{layer raised} & \text{next local replacement}\\
  \hline
  \mathrm{A0},\ x^2\equiv4\pmod{16} & 4\leadsto10\\
  \mathrm{A0},\ x^2\equiv0\pmod{16} & 16\leadsto22\\
  \mathrm{A1} & 45\leadsto57
\end{array}
\]

Those are the next exact boundary families.
