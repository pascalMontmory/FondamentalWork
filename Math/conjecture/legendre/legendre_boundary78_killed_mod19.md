# Boundary \(78\) Killed Modulo \(19\)

This note kills the unique lifted-root family that survived at the first
shared-\(5\) energy boundary.

The result is exact:
\[
\boxed{
  \mathcal E_A(\{5,17,25,49,65\})\ne78
}
\]
for every large shared-\(5\) obstruction.

Together with the low-energy theorem, this raises the shared-\(5\) energy
barrier to
\[
\boxed{
  \mathcal E_A(\{5,17,25,49,65\})\ge82.
}
\]

## 1. Remaining family before this note

The lifted-root complex modulo
\[
  2310=2\cdot3\cdot5\cdot7\cdot11
\]
reduced all energy-\(78\) top cells to one projected family:
\[
  A\equiv882\pmod {2310},
\]
with quotient assignment
\[
\begin{array}{c|ccccc}
c&5&17&25&49&65\\
\hline
e_c&42&18&10&2&6.
\end{array}
\]

Thus any integer obstruction at energy \(78\) must reduce to this family
modulo \(2310\).

## 2. Lift to modulo \(19\)

Now reduce the same projected family modulo
\[
  19.
\]

Write
\[
  \alpha\equiv A\pmod {19}.
\]

For each pair \((c,e)\), define
\[
  S_{c,e}
  =
  \left\{
    \alpha\in\mathbb F_{19}:
    \exists r\in\mathbb F_{19},\
    r^2+er+c-e\alpha=0,\
    \alpha-r\ne0
  \right\}.
\]

The condition
\[
  \alpha-r\ne0
\]
is the lifted prime-label unit condition
\[
  A-r\in(\mathbb Z/19\mathbb Z)^\times.
\]

It is legitimate in the large shared-\(5\) regime.  If \(A\ge3488\) and
\(\mathcal E=78\), then every quotient in this boundary satisfies
\[
  e_c\le42.
\]
If \(A-r_c=19\), then
\[
  19e_c=r_c^2+c=(A-19)^2+c,
\]
which is impossible because the right side is already larger than
\[
  (3488-19)^2>19\cdot42.
\]
Thus none of the five prime labels can be \(19\).

## 3. Exact residue table

For the five surviving pairs
\[
  (c,e)=(5,42),(17,18),(25,10),(49,2),(65,6),
\]
the allowed residues \(\alpha=A\bmod19\) are:

\[
\begin{array}{c|c|l}
c&e&S_{c,e}\\
\hline
5&42&\{2,3,5,6,9,10,11,12,14,16\}\\
17&18&\{0,1,2,3,6,7,9,10,15,17\}\\
25&10&\{0,2,3,8,10,12,13,14,15,18\}\\
49&2&\{0,1,4,5,7,8,13,15,17,18\}\\
65&6&\{0,1,3,4,7,8,9,10,12,14\}.
\end{array}
\]

Their intersection is empty:
\[
  S_{5,42}
  \cap S_{17,18}
  \cap S_{25,10}
  \cap S_{49,2}
  \cap S_{65,6}
  =
  \varnothing.
\]

Therefore the unique modulo-\(2310\) boundary family has no lift modulo
\[
  19.
\]

Equivalently, it has no lift modulo
\[
  2310\cdot19=43890.
\]

## 4. Conclusion

Every large shared-\(5\) obstruction with energy \(78\) would have to reduce
to the unique lifted-root family modulo \(2310\).  But that family has no
compatible residue for \(A\bmod19\).

Therefore
\[
  \mathcal E_A(\{5,17,25,49,65\})\ne78.
\]

Since the quotient energies are sums of five distinct numbers in
\[
  2\bmod4,
\]
the next possible energy after \(78\) is \(82\).  Hence:
\[
\boxed{
  \mathcal E_A(\{5,17,25,49,65\})\ge82
}
\]
in every large shared-\(5\) compressed obstruction.

This is the first closed boundary layer after the topological pivot.
