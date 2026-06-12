# Global High-Label One-Shot Theorem

This note extracts a global consequence from the cofactor/collision
equations.  It is independent of any fixed number of initial blocks.

The theorem says that repeated ordered pairs can only use small labels on
the \(q\)-scale.  All larger labels are one-shot.

## 1. Block range

Let
\[
  A=3m.
\]
Let
\[
  Q^\ast_m=
  \left\lfloor\frac{\sqrt{6m}-2}{3}\right\rfloor.
\]
Every complete A-block satisfies
\[
  0\le q\le Q^\ast_m.
\]

Define the global repetition cutoff
\[
  B_m=6Q^\ast_m+4.
\]

Since
\[
  Q^\ast_m=O(\sqrt m),
\]
the cutoff \(B_m\) is \(O(\sqrt m)\), while certificate primes are allowed
up to
\[
  3m.
\]

## 2. Same-layer repetition bound

Let a prime \(p\ge5\) divide the same quadratic layer at two distinct blocks
\[
  q\ne r.
\]
If the two blocks have the same parity, the collision equations give one of
the following divisibilities:
\[
  p\mid q-r,
\]
or
\[
  p\mid 3(q+r)+2,
\]
or
\[
  p\mid 3(q+r)+4,
\]
up to the harmless factor \(3\), which \(p\ge5\) cannot divide.

Because
\[
  |q-r|\le Q^\ast_m,
\]
and
\[
  3(q+r)+4\le6Q^\ast_m+4=B_m,
\]
any such repeated prime must satisfy
\[
  p\le B_m.
\]

If the two blocks have opposite parity, the collision equations instead
force one of
\[
  p\mid 3(q-r)+1,
\]
\[
  p\mid 3(q-r)-1,
\]
or
\[
  p\mid q+r+1.
\]
These factors are bounded by
\[
  |3(q-r)\pm1|\le3Q^\ast_m+1<B_m,
  \qquad
  q+r+1\le2Q^\ast_m+1<B_m.
\]
Hence the same conclusion holds in the opposite-parity case.

Therefore:

\[
  \boxed{
  p>B_m
  \quad\Longrightarrow\quad
  p\text{ covers at most one complete block in a fixed layer.}
  }
\]

## 3. Ordered-pair repetition bound

Suppose an ordered pair
\[
  (p_0,p_1)
\]
covers two distinct coprime complete blocks.

Then \(p_0\) repeats in the A0 layer and \(p_1\) repeats in the A1 layer.
By the same-layer repetition bound, both labels must satisfy
\[
  p_0\le B_m,\qquad p_1\le B_m.
\]

Thus:
\[
  \boxed{
  \max(p_0,p_1)>B_m
  \quad\Longrightarrow\quad
  (p_0,p_1)\text{ is one-shot.}
  }
\]

Equivalently, all repeated ordered pairs lie inside the finite low-label
box
\[
  p_0,p_1\le6Q^\ast_m+4.
\]

## 4. Consequence for the global cover

A counterexample to the A-channel must cover every coprime complete block by
an ordered pair.

The theorem splits the cover into two disjoint mechanisms:

1. high-label pairs with
   \[
     \max(p_0,p_1)>B_m,
   \]
   each of which can cover only one block;
2. low-label pairs with
   \[
     p_0,p_1\le B_m,
   \]
   which are the only pairs capable of repetition.

This is a genuine global capacity reduction.  It does not close Legendre,
because one-shot high-label pairs might still cover many blocks.  But it
removes the possibility that large labels create hidden high-multiplicity
coverage.

The remaining exact non-cover problem is therefore:

> show that the low-label box cannot supply enough repeated structure, and
> that the one-shot high-label pairs cannot align with every remaining
> block.

This is the natural next target for a weighted cofactor/Mobius certificate.
