# Next \(m\equiv3\pmod4\) Boundary Layer Killed

This note closes the first escape layer after the lifted boundary
\[
  f=(2,4,8,9,16,21,33,45)
\]
was killed.

The result is still local to the hard \(m\equiv3\pmod4\) Pell system, but it
is no longer a single-component elimination.  It eliminates the full next
boundary layer.

## 1. The three next families

After the lifted boundary is dead, at least one layer boundary must rise.
The three minimal rises are:

\[
\boxed{
  4\leadsto10,
  \qquad
  16\leadsto22,
  \qquad
  45\leadsto57.
}
\]

Thus the next layer is the union of the following three families.

\[
\begin{array}{c|c|c|c}
  \text{family} & \mathrm{A0},\ x^2\equiv4 & \mathrm{A0},\ x^2\equiv0 & \mathrm{A1}\\
  \hline
  F_{04} & 2,10 & 8,16 & 9,21,33,45\\
  F_{00} & 2,4 & 8,22 & 9,21,33,45\\
  F_{1}  & 2,4 & 8,16 & 9,21,33,57
\end{array}
\]

The modulo \(7\) zero-quotient filter remains active:
\[
  7\mid f
  \quad\Longrightarrow\quad
  c\in\{26,122\}.
\]

We prove that all three families have no integral point.

For a prime \(\ell\), define
\[
  M_\ell(c,f)
  =
  \left\{
    m\bmod\ell:
    f^2+6mf-c\text{ is a square modulo }\ell
  \right\}.
\]

## 2. Family \(F_{00}\): killed modulo 5

Here
\[
  \mathrm{A0}_{4}=\{2,4\},
  \qquad
  \mathrm{A0}_{0}=\{8,22\}.
\]

The square classes modulo \(5\) are
\[
  \{0,1,4\}.
\]

The A0 assignment intersections are:

\[
\begin{array}{c|c}
  \text{A0}_{4}\text{ assignment} & m\bmod5\\
  \hline
  c=4\mapsto2,\ c=100\mapsto4 & \{0,2\}\\
  c=4\mapsto4,\ c=100\mapsto2 & \{1,3\}
\end{array}
\]

\[
\begin{array}{c|c}
  \text{A0}_{0}\text{ assignment} & m\bmod5\\
  \hline
  c=16\mapsto8,\ c=64\mapsto22 & \{2\}\\
  c=16\mapsto22,\ c=64\mapsto8 & \{3\}
\end{array}
\]

Therefore A0 can leave only two cases:
\[
  m\equiv2\pmod5
  \quad\text{or}\quad
  m\equiv3\pmod5.
\]

At \(m\equiv2\pmod5\), the A1 offset \(c=2\) has no admissible value among
\[
  9,21,33,45,
\]
because \(f=21\) is forbidden on \(c=2\) by the modulo \(7\) zero filter,
\(f=45\) is never admissible at \(c=2\) modulo \(5\), and \(f=9,33\) do not
allow \(m\equiv2\).

At \(m\equiv3\pmod5\), the A1 admissible sets are:
\[
\begin{array}{c|c}
  c & \text{admissible }f\\
  \hline
  2   & 9,33\\
  26  & 45\\
  50  & 45\\
  122 & 9,33
\end{array}
\]

The two offsets \(26\) and \(50\) both require the same value \(f=45\), but
the quotients in the boundary are distinct.  Hence no assignment exists.

Thus
\[
\boxed{
  F_{00}\text{ is killed modulo }5.
}
\]

## 3. Family \(F_{04}\): killed modulo 5, 7, and 11

Here
\[
  \mathrm{A0}_{4}=\{2,10\},
  \qquad
  \mathrm{A0}_{0}=\{8,16\},
  \qquad
  \mathrm{A1}=\{9,21,33,45\}.
\]

Modulo \(5\), all assignments are eliminated except the following two:

\[
\begin{array}{c|cccccccc|c}
  & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122 & m\bmod5\\
  \hline
  A & 2 & 10 & 16 & 8 & 9 & 45 & 33 & 21 & 0\\
  B & 10 & 2 & 16 & 8 & 9 & 45 & 33 & 21 & 0
\end{array}
\]

Modulo \(7\), assignment \(A\) dies.  Indeed its successive intersections
force
\[
  m\equiv0\pmod7
\]
from the first six rows, while the row
\[
  c=50,\qquad f=33
\]
does not allow \(m\equiv0\pmod7\).

Assignment \(B\) survives modulo \(7\), but only with
\[
  m\equiv6\pmod7.
\]

Now reduce assignment \(B\) modulo \(11\).  The relevant admissible sets are:

\[
\begin{array}{c|c|c}
  c & f & M_{11}(c,f)\\
  \hline
  4   & 10 & \{3,5,6,8,9,10\}\\
  100 & 2  & \{0,1,2,6,8,9\}\\
  16  & 16 & \{0,2,3,5,9,10\}\\
  64  & 8  & \{0,1,3,4,5,9\}\\
  2   & 9  & \{1,2,4,8,9,10\}\\
  26  & 45 & \{1,2,3,5,6,8\}\\
  50  & 33 & \mathbb Z/11\mathbb Z\\
  122 & 21 & \{0,1,3,4,5,9\}
\end{array}
\]

Intersecting the first five nontrivial rows gives
\[
  m\equiv9\pmod{11}.
\]

But the row
\[
  c=26,\qquad f=45
\]
allows
\[
  \{1,2,3,5,6,8\},
\]
which excludes \(9\).  Therefore assignment \(B\) also dies.

Hence
\[
\boxed{
  F_{04}\text{ is killed by }(5,7,11).
}
\]

## 4. Family \(F_1\): killed modulo 5, 7, and 11

Here
\[
  \mathrm{A0}_{4}=\{2,4\},
  \qquad
  \mathrm{A0}_{0}=\{8,16\},
  \qquad
  \mathrm{A1}=\{9,21,33,57\}.
\]

Modulo \(5\), all assignments are eliminated except one:

\[
\begin{array}{c|cccccccc|c}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122 & m\bmod5\\
  \hline
  f & 2 & 4 & 8 & 16 & 57 & 33 & 9 & 21 & 2
\end{array}
\]

Modulo \(7\), the same assignment survives only at
\[
  m\equiv5\pmod7.
\]

Modulo \(11\), it dies immediately because the row
\[
  c=26,\qquad f=33
\]
has no admissible residue at all:
\[
  M_{11}(26,33)=\varnothing.
\]

Thus
\[
\boxed{
  F_1\text{ is killed by }(5,7,11).
}
\]

## 5. Exact conclusion

The complete next boundary layer after the lifted component is impossible:
\[
\boxed{
  F_{04}\cup F_{00}\cup F_1=\varnothing
  \quad\text{inside the }m\equiv3\pmod4\text{ Pell system.}
}
\]

Equivalently, a surviving hard-branch counterexample must rise beyond the
first escape layer.  It cannot have only one of the minimal raises
\[
  4\leadsto10,
  \qquad
  16\leadsto22,
  \qquad
  45\leadsto57.
\]

Therefore at least two layer boundaries must rise, or one boundary must jump
past its first successor.

This is still not a proof of Legendre.  But it is the first multi-family
closure step in the hard branch: the local certificates now eliminate an
entire layer, not just a single tuple.

## 6. The actual closure mechanism now suggested

The pattern is no longer "kill tuples one by one".  The exact object is a
rank-raise game:

1. each layer has an ordered list of admissible \(f\)-values;
2. modulo \(7\) removes all \(7\mid f\) placements except on \(c=26,122\);
3. small primes force either an empty matching or a unique matching;
4. the unique matching then dies at the next modulus.

A closing proof would show that every rank-raise state has a local prime
\(\ell\) for which the matching graph has no perfect matching, or reduces to
a state already killed.  That is now a finite-state certificate problem only
if one proves an a priori bound on the relevant \(f\)-ranks.

The next mathematical target is therefore sharp:

\[
\boxed{
  \text{prove a rank cap for the hard }m\equiv3\pmod4\text{ quotient game.}
}
\]

Without a rank cap, modular elimination remains an infinite ladder.  With a
rank cap, the notes above become the beginning of a finite proof certificate.
