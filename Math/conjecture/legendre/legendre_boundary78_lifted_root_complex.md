# Boundary \(78\) Lifted Root Complex

The matching-complex pivot shows that the low-energy shared-\(5\) layers
\[
  \mathcal E\le74
\]
have no top cell.  The next boundary is
\[
  \mathcal E=78.
\]

At this boundary, the graph-level complex is too coarse.  We must remember
the actual roots.

## 1. Lifted complex

Fix
\[
  M=2310.
\]

For a residue \(A\bmod M\), quotient set \(Q\), and offset set
\[
  \mathcal C=\{5,17,25,49,65\},
\]
define the lifted vertices
\[
  (c,e,r)
\]
by
\[
  c\in\mathcal C,\qquad e\in Q,
\]
and
\[
  r^2+er+c-eA\equiv0\pmod M.
\]

Because the actual prime label is
\[
  p_c=A-r_c,
\]
and the labels are primes larger than \(11\) in the large shared-\(5\)
regime, we also impose the unit condition
\[
  A-r\in(\mathbb Z/M\mathbb Z)^\times.
\]

A top cell in the lifted complex is a choice of one vertex for every offset
with distinct quotients.

## 2. Energy \(78\) quotient sets

The quotient sets at energy \(78\) are the five-element subsets of
\[
  2,6,10,14,18,\ldots
\]
whose sum is \(78\).  There are \(13\) such sets.

The lifted-root certificate checks:

1. all \(13\) quotient sets;
2. all \(154\) residues
   \[
     A\bmod2310,\qquad A\equiv12\text{ or }18\pmod {30};
   \]
3. all assignments of the five quotients to the five offsets;
4. all lifted root existence conditions with
   \[
     \gcd(A-r,2310)=1.
   \]

## 3. Result

All projected top cells vanish except one.

The only surviving projected lifted-root pattern is:
\[
  A\equiv882\pmod {2310},
\]
\[
  Q=\{2,6,10,18,42\},
\]
with assignment
\[
\begin{array}{c|ccccc}
c&5&17&25&49&65\\
\hline
e_c&42&18&10&2&6.
\end{array}
\]

The lifted root multiplicities are
\[
\begin{array}{c|ccccc}
c&5&17&25&49&65\\
\hline
\#r_c&8&8&2&2&4.
\end{array}
\]

Thus there are
\[
  8\cdot8\cdot2\cdot2\cdot4=1024
\]
lifted top cells modulo \(2310\), but all lie above the same projected
pattern.

## 4. Exact residual system

The remaining boundary pattern is the system
\[
\begin{aligned}
r_5^2+42r_5+5&\equiv42A,\\
r_{17}^2+18r_{17}+17&\equiv18A,\\
r_{25}^2+10r_{25}+25&\equiv10A,\\
r_{49}^2+2r_{49}+49&\equiv2A,\\
r_{65}^2+6r_{65}+65&\equiv6A
\end{aligned}
\qquad(\bmod 2310),
\]
with
\[
  A\equiv882\pmod {2310}
\]
and
\[
  A-r_c\in(\mathbb Z/2310\mathbb Z)^\times
  \qquad(c\in\mathcal C).
\]

The next topological closure target is therefore sharply localized:

> Kill this one lifted-root family by adding compatibility among the five
> labels \(p_c=A-r_c\), or lift it to a higher modulus and find a new Hall
> defect in the root complex.

This is much closer to a proof skeleton than the raw CRT filtration: the
boundary layer has been compressed to one explicit topological residue
family.
