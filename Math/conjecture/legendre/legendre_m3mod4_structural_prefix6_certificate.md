# Structural Prefix-6 Certificate

This note closes the first six structural quotient values in every offset
row of the hard \(m\equiv3\pmod4\) branch.

It uses the offset-specific multiplicative quotient sets obtained after the
A0 dual collapses and the A1 splitting laws.  The verification is exact:
each killed assignment has an empty intersection of local sets
\[
  M_p(c,f)
  =
  \{m\bmod p:\ f^2+6mf-c\text{ is a square modulo }p\}.
\]

The verifier is
\[
  \texttt{tools/m3mod4\_structural\_prefix\_certificate.py}.
\]

## 1. Structural prefix values

The first six values in each offset row are:
\[
\begin{array}{c|l}
  c & \text{first six structural values}\\
  \hline
  4
    & 2,\ 10,\ 26,\ 34,\ 50,\ 58\\
  100
    & 2,\ 10,\ 26,\ 34,\ 50,\ 58\\
  16
    & 8,\ 16,\ 40,\ 80,\ 104,\ 136\\
  64
    & 8,\ 32,\ 40,\ 64,\ 104,\ 136\\
  2
    & 9,\ 33,\ 57,\ 81,\ 129,\ 153\\
  26
    & 9,\ 21,\ 45,\ 81,\ 93,\ 105\\
  50
    & 9,\ 33,\ 45,\ 57,\ 81,\ 129\\
  122
    & 9,\ 21,\ 57,\ 69,\ 81,\ 93.
\end{array}
\]

The values are not arbitrary rank values.  They are the first six values in
the intrinsic structural semigroups:

- A0 sum-of-two-squares lower semigroups after the dual collapses;
- A1 quadratic-field splitting semigroups.

## 2. Finite local certificate

The verifier checks all assignments from the table above with the eight
quotients pairwise distinct.

The exact count is:
\[
\boxed{
  678720
}
\]
distinct assignments.

The local certificates kill all but two assignments:
\[
\begin{array}{c|r}
  p & \#\text{assignments killed}\\
  \hline
  5 & 562842\\
  7 & 99585\\
  11 & 14308\\
  13 & 1589\\
  17 & 308\\
  19 & 65\\
  23 & 13\\
  29 & 5\\
  37 & 1\\
  41 & 1\\
  43 & 1.
\end{array}
\]

The two locally surviving assignments are:
\[
\boxed{
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 10 & 58 & 8 & 40 & 9 & 21 & 33 & 69
\end{array}
}
\]
and
\[
\boxed{
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 10 & 58 & 16 & 40 & 9 & 21 & 33 & 69.
\end{array}
}
\]

They survive finite local tests because they contain the universal residue
class
\[
  m\equiv-1\pmod p
\]
for every prime \(p\).  They are ghost fibers, not positive hard-branch
points.

## 3. Ghost fiber with \(c=16,\ f=8\)

Consider the first survivor.  The row
\[
  (c,f)=(16,8)
\]
gives
\[
  u^2=48m+48.
\]

Thus
\[
  m=12n^2-1
\]
for some integer \(n\).

The rows
\[
  (c,f)=(4,10)
  \quad\text{and}\quad
  (c,f)=(64,40)
\]
then become
\[
  X^2=20n^2+1,
  \qquad
  Y^2=20n^2+9.
\]

Subtracting gives
\[
\boxed{
  Y^2-X^2=8.
}
\]

Hence
\[
  (Y-X)(Y+X)=8.
\]

The only positive solution is
\[
  X=1,\qquad Y=3.
\]

Therefore
\[
  n=0,
  \qquad
  m=-1.
\]

So the first survivor has no positive integral point.

## 4. Ghost fiber with \(c=16,\ f=16\)

For the second survivor, use the two rows
\[
  (c,f)=(4,10)
  \quad\text{and}\quad
  (c,f)=(64,40).
\]

They give
\[
  U^2=60m+96=12(5m+8),
\]
and
\[
  V^2=240m+1536=48(5m+32).
\]

Thus
\[
  U=6X,
  \qquad
  V=12Y,
\]
and therefore
\[
  3X^2=5m+8,
  \qquad
  3Y^2=5m+32.
\]

Subtracting gives again
\[
\boxed{
  Y^2-X^2=8.
}
\]

Thus
\[
  X=1,\qquad Y=3,
\]
and hence
\[
  m=-1.
\]

So the second survivor also has no positive integral point.

## 5. Consequence

The complete structural prefix of length \(6\) has no positive hard-branch
point:
\[
\boxed{
  \text{structural prefix }6
  \quad\Longrightarrow\quad
  \text{closed.}
}
\]

Therefore any remaining hard-branch counterexample must use at least one
offset beyond the six listed structural values.

This is a stronger statement than the old additive prefix certificates:
the prefix is now built from intrinsic quotient semigroups and the only
local survivors are eliminated by an exact integer ghost-fiber argument.
