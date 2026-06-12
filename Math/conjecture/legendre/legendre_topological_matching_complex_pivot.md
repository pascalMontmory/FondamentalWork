# Topological Matching-Complex Pivot

This note gives the first genuinely topological formulation of the
compressed Legendre attack.

It does not prove Legendre.  It changes the shape of the remaining problem:
a bad compressed certificate is no longer just a residue assignment.  It is a
top-dimensional cell in an arithmetic matching complex.

## 1. Incidence tensor

Keep the shared-\(5\) pilot fiber
\[
  \mathcal C=\{5,17,25,49,65\}.
\]

For a quotient set
\[
  Q=\{e_1,\ldots,e_5\}
\]
and a residue \(A\bmod M\), define the incidence tensor
\[
  T_{A,Q}(c,e)
  =
  \begin{cases}
  1,&\exists r\pmod M:\ r^2+er+c-eA\equiv0\pmod M,\\
  0,&\text{otherwise.}
  \end{cases}
\]

Here
\[
  c\in\mathcal C,\qquad e\in Q.
\]

An integer obstruction in the quotient layer \(Q\) gives, after reduction
modulo \(M\), a bijection
\[
  \sigma:\mathcal C\to Q
\]
such that
\[
  T_{A,Q}(c,\sigma(c))=1
  \qquad(c\in\mathcal C).
\]

Equivalently,
\[
\boxed{
  \operatorname{per}(T_{A,Q})>0.
}
\]

Thus the arithmetic obstruction is a permanent problem for a \(5\times5\)
zero-one tensor.

## 2. Matching complex

Let \(G_{A,Q}\) be the bipartite graph with left vertices \(\mathcal C\),
right vertices \(Q\), and edge
\[
  c\sim e
  \quad\Longleftrightarrow\quad
  T_{A,Q}(c,e)=1.
\]

Define the matching complex
\[
  \mathfrak M(A,Q)
  =
  \{\text{matchings in }G_{A,Q}\}.
\]

A \(k\)-edge matching is a \((k-1)\)-simplex.  Therefore a full compressed
certificate is exactly a \(4\)-simplex in \(\mathfrak M(A,Q)\).

So the low-energy shared-\(5\) theorem can be written topologically as:
\[
\boxed{
  \dim \mathfrak M(A,Q)\le3
}
\]
for every low-energy \(Q\) and every admissible residue \(A\).

This is the clean topological reduction: prove that the arithmetic matching
complex has no top cell.

## 3. Hall defect as a collapse certificate

For \(S\subseteq\mathcal C\), write
\[
  N_{A,Q}(S)=\{e\in Q:\exists c\in S,\ T_{A,Q}(c,e)=1\}.
\]

If
\[
  |N_{A,Q}(S)|<|S|,
\]
then every matching misses at least
\[
  \delta(S)=|S|-|N_{A,Q}(S)|
\]
vertices of \(S\).  Consequently no \(4\)-simplex can exist.

This is Hall's theorem, but here it has a topological interpretation:
the subcomplex of potential certificates collapses away from the top
dimension because \(S\) cannot be fully matched into its neighborhood.

In tensor language, the same condition forces
\[
  \operatorname{per}(T_{A,Q})=0.
\]

## 4. Exact low-energy theorem

For the shared-\(5\) fiber, previous gates prove that for \(A\ge3488\)
the five quotient labels are distinct and satisfy
\[
  e_c\equiv2\pmod4.
\]

Hence every low-energy obstruction with
\[
  \mathcal E_A(\mathcal C)\le74
\]
must use one of the 29 quotient sets listed in
`legendre_shared5_low_energy_layers_closed.md`.

The topological certificate checks all
\[
  29\cdot154
\]
complexes
\[
  \mathfrak M(A,Q),
\]
where
\[
  A\bmod2310,\qquad A\equiv12\text{ or }18\pmod {30}.
\]

For every one of these complexes,
\[
  \operatorname{per}(T_{A,Q})=0.
\]

Equivalently, every complex has a Hall-defect subset \(S\subseteq\mathcal C\)
and therefore no \(4\)-simplex.

The verifier gives the exact distribution of maximal matching size:
\[
\begin{array}{c|ccccc}
\max |M|&0&1&2&3&4\\
\hline
\#\text{ complexes}&663&1745&1428&558&72.
\end{array}
\]

So the certificate is not merely detecting empty graphs.  There are \(72\)
low-energy complexes with \(3\)-dimensional top cells, but none with a
\(4\)-simplex.  Every one of the \(4466\) complexes has a Hall defect of
defect \(1\).

Thus:
\[
\boxed{
  \mathcal E_A(\mathcal C)\ge78
}
\]
is now not only a CRT statement.  It is a topological non-existence theorem
for top cells in arithmetic matching complexes.

## 5. Why this is a better proof skeleton

The previous local certificates were rows of congruences.  The new object is
structural:

\[
  \text{Legendre obstruction}
  \Rightarrow
  \text{top cell in } \mathfrak M(A,Q).
\]

A closure strategy can now aim for a global theorem of the form:
\[
  \mathfrak M_n
  \text{ is collapsible below the certificate dimension for every }n.
\]

This is the right place for topology:

1. vertices are local divisibility events;
2. simplices are mutually compatible partial certificates;
3. full bad certificates are top-dimensional cells;
4. Hall defects, discrete Morse matchings, or homology vanishing can kill
   the top cells.

## 6. Next exact topological target

The first surviving boundary is the energy layer
\[
  \mathcal E_A(\mathcal C)=78,
\]
with a surviving tensor pattern beginning at
\[
  Q=\{2,6,10,18,42\}.
\]

The next non-enumerative goal is:

> Construct an acyclic discrete Morse matching on
> \(\mathfrak M(A,Q)\) for every surviving \(A\bmod2310\), or find a lifted
> Hall defect after adding the prime-unity condition \(A-r\in(\mathbb Z/M)^\times\).

If this succeeds uniformly at the boundary, the shared-\(5\) route becomes a
genuine topological descent rather than a residue-level filtration.

The conceptual upgrade needed at \(\mathcal E=78\) is to replace the graph
complex by a lifted root complex.  Its vertices should be triples
\[
  (c,e,r)
  \quad\text{with}\quad
  r^2+er+c-eA\equiv0\pmod M,
\]
and its simplices should enforce both:

1. distinct offsets and distinct quotients;
2. compatibility of the lifted labels
   \[
     p_c=A-r_c
   \]
   as prime labels, especially the unit condition
   \[
     p_c\in(\mathbb Z/M\mathbb Z)^\times.
   \]

This is the next topological object.  It is finer than the current matching
complex because it remembers the actual roots, not only the existence of a
root.
