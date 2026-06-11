# A0 Dual Boundary Killed Modulo 23

This note eliminates the new A0 structural boundary produced by the
dual-factor collapses.

It is an exact finite congruence certificate, not a search over Legendre
intervals.

## 1. Structural A0 boundary after the dual collapses

In the hard branch \(m\equiv3\pmod4\), the A0 dual collapses give:

\[
\begin{array}{c|c}
  c & \text{surviving lower quotient semigroup}\\
  \hline
  4,100 & 2\mathcal S_4\\
  16 & 8\mathcal S_4\cup16\mathcal S_4\\
  64 & 8\mathcal S_4\cup32\mathcal S_4\cup64\mathcal S_4.
\end{array}
\]

Thus the first possible A0 boundary lower quotients are:
\[
  2,\ 10
  \quad\text{for}\quad
  c=4,100,
\]
and
\[
  8,\ 16
  \quad\text{for}\quad
  c=16,64.
\]

The A0 dual valuation collapse also proves
\[
  f=16\quad\Longrightarrow\quad c=16.
\]

Therefore the A0 zero-layer assignment is forced:
\[
\boxed{
  c=16\mapsto16,
  \qquad
  c=64\mapsto8.
}
\]

Only two A0 four-layer assignments remain:
\[
\begin{array}{c|cc}
  \text{case} & c=4 & c=100\\
  \hline
  I & 2 & 10\\
  II & 10 & 2.
\end{array}
\]

## 2. Local sets modulo 23

For a row \((c,f)\), define
\[
  M_{23}(c,f)
  =
  \{m\bmod23:\ f^2+6mf-c\text{ is a square modulo }23\}.
\]

The square classes modulo \(23\) are used in the usual reduced Pell line
\[
  u^2=f^2+6mf-c.
\]

The relevant local sets are:

\[
\begin{array}{c|c|l}
  c & f & M_{23}(c,f)\\
  \hline
  4 & 2
    & \{0,1,2,3,4,6,8,9,12,13,16,18\}\\
  4 & 10
    & \{0,1,2,3,8,10,13,14,17,18,20,22\}\\
  100 & 2
    & \{1,3,8,9,10,11,12,14,16,17,20,21\}\\
  100 & 10
    & \{0,5,7,10,11,14,15,17,19,20,21,22\}\\
  16 & 16
    & \{2,4,9,10,11,12,13,15,17,18,21,22\}\\
  64 & 8
    & \{0,1,2,3,4,6,8,9,12,13,16,18\}.
\end{array}
\]

## 3. Case I dies

Case I is
\[
  (c,f)=(4,2),(100,10),(16,16),(64,8).
\]

The first two rows give
\[
  M_{23}(4,2)\cap M_{23}(100,10)=\{0\}.
\]

But
\[
  0\notin M_{23}(16,16).
\]

Hence
\[
\boxed{
  M_{23}(4,2)
  \cap M_{23}(100,10)
  \cap M_{23}(16,16)
  =
  \varnothing.
}
\]

Thus case I has no integral point.

## 4. Case II dies

Case II is
\[
  (c,f)=(4,10),(100,2),(16,16),(64,8).
\]

The first three rows give
\[
  M_{23}(4,10)
  \cap M_{23}(100,2)
  \cap M_{23}(16,16)
  =
  \{10,17\}.
\]

But
\[
  \{10,17\}\cap M_{23}(64,8)=\varnothing.
\]

Therefore
\[
\boxed{
  M_{23}(4,10)
  \cap M_{23}(100,2)
  \cap M_{23}(16,16)
  \cap M_{23}(64,8)
  =
  \varnothing.
}
\]

Thus case II also has no integral point.

## 5. Consequence

The entire A0 dual structural boundary is killed modulo \(23\):
\[
\boxed{
  \{2,10\}_{c=4,100}
  \quad\text{and}\quad
  \{16,8\}_{c=16,64}
  \quad\Longrightarrow\quad
  \text{no }m.
}
\]

Consequently any remaining hard-branch counterexample must leave this A0
boundary.  Since A0 already absorbed the old structural moves
\[
  4\leadsto10,
  \qquad
  16\leadsto22,
\]
the next obstruction is now a genuinely higher A0 escape or an A1
same-gap obstruction, not the old boundary component.
