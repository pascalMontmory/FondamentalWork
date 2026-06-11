# Triple-Block Labeling Obstruction

This note derives a direct consequence of the adjacent-block obstruction.

In one fixed layer, the same certificate prime cannot label three consecutive
coprime complete A-blocks.

This turns the remaining covering problem into a constrained labeling problem
on an interval.

## 1. No triple repetition in one layer

Fix a layer \(i\in\{0,1\}\).

Suppose a prime
\[
  p\ge5
\]
certifies three consecutive blocks
\[
  q,\qquad q+1,\qquad q+2
\]
in the same layer.

By the adjacent-block obstruction applied to the adjacent pair \(q,q+1\),
\[
  p\mid q+1.
\]
By the same obstruction applied to the adjacent pair \(q+1,q+2\),
\[
  p\mid q+2.
\]
Therefore
\[
  p\mid(q+2)-(q+1)=1,
\]
impossible.

Hence:
\[
\boxed{
\text{No prime }p\ge5\text{ can certify three consecutive blocks in one layer.}
}
\]

This holds separately for A0 and A1.

## 2. Consequence for a full counterexample

A full counterexample on a run of coprime complete blocks
\[
  q,\ q+1,\ \dots,\ q+L
\]
must assign two labels to every vertex:

- an A0 label \(p_0(j)\in\mathcal P_0(m)\);
- an A1 label \(p_1(j)\in\mathcal P_1(m)\).

The labels must satisfy:

1. vertex-wise distinctness:
   \[
     p_0(j)\ne p_1(j);
   \]
2. A0 local restrictions:
   \[
     p_0(j)\equiv1\pmod4,\qquad p_0(j)\nmid3m;
   \]
3. A1 local restrictions:
   \[
     p_1(j)\nmid9m^2+1,\qquad
     \left(\frac{-9m^2-1}{p_1(j)}\right)=1;
   \]
4. adjacent repetition rule:
   if
   \[
     p_i(j)=p_i(j+1),
   \]
   then
   \[
     p_i(j)\mid j+1;
   \]
5. no-triple rule:
   \[
     p_i(j),p_i(j+1),p_i(j+2)
   \]
   cannot all be equal.

Thus the remaining obstruction is not merely a residue cover.  It is a
two-layer labeling problem with local congruence and adjacency constraints.

## 3. Why this still does not close immediately

The no-triple rule alone is not enough.

A label can still reappear on non-adjacent vertices.  For example, the same
prime can in principle certify \(q\) and \(q+2\), because the adjacent
obstruction only controls immediate repetition.

The general repetition formula remains:
\[
  q\equiv r\pmod p
  \quad\text{or}\quad
  q+r\equiv-\frac{\alpha+\beta}{3}\pmod p,
\]
where
\[
  t(q)=3q+\alpha,\qquad t(r)=3r+\beta.
\]

Therefore a proof cannot rely only on a graph-coloring lower bound.  It must
use the exact arithmetic of the labels:

- the A0 labels are restricted to \(1\bmod4\);
- the A1 labels depend on the fixed character condition
  \[
    \left(\frac{-9m^2-1}{p}\right)=1;
  \]
- bridge positions have been removed;
- the two layer labels at each vertex are distinct.

## 4. Current exact target

The next plausible closure lemma is:

> There is no labeling of the full coprime complete block interval satisfying
> the five rules above and the layer congruences
> \[
>   t_0(q)^2\equiv-9m^2\pmod{p_0(q)},
> \]
> \[
>   t_1(q)^2\equiv-9m^2-1\pmod{p_1(q)}.
> \]

This labeling lemma is equivalent to the fixed-\(m\) double-sieve obstruction,
but it exposes the local adjacency pressure needed for a possible proof.
