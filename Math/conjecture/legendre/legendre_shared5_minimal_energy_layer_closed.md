# Shared-\(5\) Minimal Energy Layer Closed

This note closes the first energy layer of the compressed shared-\(5\)
certificate.

It is a limited result, not a proof of Legendre.  But it is the first
non-realization theorem in the compressed-certificate direction:

\[
  \boxed{\mathcal E_A(\{5,17,25,49,65\})=50
  \text{ is impossible in the shared-}5\text{ fiber}.}
\]

## 1. Setup

In the shared-\(5\) fiber,
\[
  A=3m,\qquad m\text{ even},\qquad A^2\equiv-1\pmod5.
\]

Equivalently,
\[
  A\equiv12\text{ or }18\pmod {30}.
\]

The compressed variable offsets are
\[
  \mathcal C=\{5,17,25,49,65\}.
\]

For every \(c\in\mathcal C\), a composite certificate gives
\[
  (A-r_c)e_c=r_c^2+c.
\]

The mod-\(4\) energy gate proved
\[
  e_c\equiv2\pmod4
  \qquad(c\in\mathcal C).
\]

For \(A\ge3488\), the five quotients are distinct.  Therefore the minimal
possible energy layer is
\[
  \{e_c:c\in\mathcal C\}=\{2,6,10,14,18\}.
\]

We now prove that this layer is impossible.

## 2. Modular certificate modulo \(210\)

Work modulo
\[
  210=2\cdot3\cdot5\cdot7.
\]

An integer solution in the minimal layer would reduce modulo \(210\) to a
solution of
\[
  r_c^2+e_cr_c+c-e_cA\equiv0\pmod {210}
  \qquad(c\in\mathcal C),
\]
where
\[
  A\equiv12\text{ or }18\pmod {30}
\]
and
\[
  \{e_c:c\in\mathcal C\}=\{2,6,10,14,18\}.
\]

For each admissible residue \(A\bmod210\), define
\[
  E_c(A)
  =
  \{e\in\{2,6,10,14,18\}:
  \exists r\pmod {210},\
  r^2+er+c-eA\equiv0\pmod {210}\}.
\]

The exact computation gives:

\[
\begin{array}{c|ccccc}
A\bmod210&E_5&E_{17}&E_{25}&E_{49}&E_{65}\\
\hline
12&\varnothing&\{6,18\}&\{2,10\}&\{2\}&\{6\}\\
18&\{18\}&\{6\}&\varnothing&\{10\}&\{18\}\\
42&\{6\}&\{18\}&\{2,10\}&\{2,10\}&\{6\}\\
48&\{18\}&\{6\}&\{10\}&\{10\}&\varnothing\\
72&\{6\}&\{6,18\}&\{2\}&\varnothing&\varnothing\\
78&\varnothing&\varnothing&\varnothing&\{10\}&\varnothing\\
102&\{6\}&\{6\}&\varnothing&\{2,10\}&\varnothing\\
108&\{18\}&\varnothing&\{10\}&\varnothing&\{18\}\\
132&\varnothing&\{6,18\}&\{2,10\}&\{10\}&\{6\}\\
138&\varnothing&\{6\}&\{10\}&\varnothing&\{18\}\\
162&\varnothing&\varnothing&\varnothing&\{10\}&\varnothing\\
168&\varnothing&\varnothing&\{10\}&\{10\}&\{18\}\\
192&\{6\}&\varnothing&\{10\}&\{2\}&\{6\}\\
198&\{18\}&\{6\}&\varnothing&\varnothing&\varnothing
\end{array}
\]

In every row, the five sets \(E_c(A)\) cannot support a bijective assignment
of the five distinct quotients
\[
  2,6,10,14,18.
\]

Indeed, many rows already contain an empty set.  The remaining row
\[
  A\equiv42\pmod {210}
\]
still fails because the possible quotient \(14\) appears nowhere.

Thus no minimal-layer residue assignment exists modulo \(210\).

## 3. Conclusion

If a shared-\(5\) compressed certificate exists for \(A\ge3488\), then its
energy cannot be minimal:
\[
  \mathcal E_A(\mathcal C)>50.
\]

Since every quotient is \(2\pmod4\), the next possible energy is at least
\[
  54.
\]

Therefore:
\[
\boxed{
  \mathcal E_A(\{5,17,25,49,65\})\ge54
  \quad
  \text{in every large shared-}5\text{ obstruction}.
}
\]

This is the first closed energy stratum in the compressed certificate
approach.

## 4. Next stratum

The next exact target after this note was the energy layer
\[
  \{2,6,10,14,22\}
\]
and its permutations.

Because the quotients are distinct and all lie in the same arithmetic
progression \(2\bmod4\), this is the only sorted quotient set of energy
\(54\).

This target has now been absorbed into the stronger low-energy certificate:
all energy layers \(\le74\) are impossible modulo \(2310\).

The route is now stratified:

1. quotient congruence \(e_c\equiv2\pmod4\);
2. distinct quotient ranks;
3. energy layers;
4. modular non-realization certificates for each layer.

This is not fiber enumeration.  It is an energy filtration of a compressed
incidence variety.
