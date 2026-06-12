# Shared-\(5\) Low Energy Layers Closed

This note strengthens the first shared-\(5\) energy certificate.

The previous gate gave a necessary lower bound
\[
  \mathcal E_A(\{5,17,25,49,65\})\ge 50.
\]

The minimal layer \(50\) is not the true first obstruction.  A finite
CRT certificate kills every layer below \(78\).

## 1. Statement

In the shared-\(5\) fiber,
\[
  A=3m,\qquad m\text{ even},\qquad A^2\equiv-1\pmod5,
\]
so
\[
  A\equiv12\text{ or }18\pmod {30}.
\]

Let
\[
  \mathcal C=\{5,17,25,49,65\}.
\]

For every \(c\in\mathcal C\), a compressed obstruction has
\[
  (A-r_c)e_c=r_c^2+c.
\]

For \(A\ge3488\), the previous gates prove:

1. the five quotients \(e_c\) are pairwise distinct;
2. every quotient satisfies \(e_c\equiv2\pmod4\).

Define the shared-\(5\) energy
\[
  \mathcal E_A(\mathcal C)=\sum_{c\in\mathcal C}e_c.
\]

Then:
\[
\boxed{
  \mathcal E_A(\mathcal C)\ge 78
  \qquad(A\ge3488)
}
\]
for every shared-\(5\) compressed obstruction.

Equivalently, no obstruction can have energy \(50,54,58,62,66,70\), or
\(74\).

## 2. Finite quotient list

Since the five quotients are distinct and all lie in \(2\bmod4\), the
quotient set must be a five-element subset of
\[
  \{2,6,10,14,18,\ldots\}.
\]

The quotient sets with total energy at most \(74\) are exactly:

\[
\begin{array}{c|l}
\mathcal E&\{e_c\}\\
\hline
50&\{2,6,10,14,18\}\\
54&\{2,6,10,14,22\}\\
58&\{2,6,10,14,26\},\{2,6,10,18,22\}\\
62&\{2,6,10,14,30\},\{2,6,10,18,26\},\{2,6,14,18,22\}\\
66&\{2,6,10,14,34\},\{2,6,10,18,30\},\{2,6,10,22,26\},
   \{2,6,14,18,26\},\{2,10,14,18,22\}\\
70&\{2,6,10,14,38\},\{2,6,10,18,34\},\{2,6,10,22,30\},
   \{2,6,14,18,30\},\{2,6,14,22,26\},
   \{2,10,14,18,26\},\{6,10,14,18,22\}\\
74&\{2,6,10,14,42\},\{2,6,10,18,38\},\{2,6,10,22,34\},
   \{2,6,10,26,30\},\{2,6,14,18,34\},
   \{2,6,14,22,30\},\{2,6,18,22,26\},
   \{2,10,14,18,30\},\{2,10,14,22,26\},
   \{6,10,14,18,26\}.
\end{array}
\]

This is a finite list of 29 quotient sets.

## 3. CRT certificate modulo \(2310\)

Work modulo
\[
  2310=2\cdot3\cdot5\cdot7\cdot11.
\]

For a fixed quotient \(e\), offset \(c\), and residue \(A\bmod2310\), the
centered equation is the quadratic congruence
\[
  r^2+er+c-eA\equiv0\pmod {2310}.
\]

For each of the 29 quotient sets \(Q\), each admissible residue
\[
  A\bmod2310,\qquad A\equiv12\text{ or }18\pmod {30},
\]
and each bijection
\[
  \mathcal C\to Q,
\]
at least one of the five quadratic congruences has no root modulo \(2310\).

Thus there is no assignment satisfying all five centered equations modulo
\(2310\).

Any integer obstruction would reduce to such a modular assignment.  This is
impossible.  Therefore all energy layers \(\le74\) are excluded.

## 4. Boundary

The next layer is
\[
  \mathcal E_A(\mathcal C)=78.
\]

Modulo \(2310\), the first formal survivors occur at energy \(78\), for
example with quotient set
\[
  \{2,6,10,18,42\}.
\]

So the next exact target is not another global search.  It is the boundary
layer \(78\), starting from the surviving CRT assignments and adding either:

1. one more local prime to the CRT certificate, if it kills the layer; or
2. a genuine algebraic incompatibility among the lifted roots, if the
   local classes persist.

This is a sharper closure target than the previous minimal-layer note.
