# High-High Adjacency Gate

This note pushes the high-label least-root reduction one step further.

When both layers of a coprime complete A-block are certified by high labels,
the block is equivalent to an adjacency between two least-root image sets.
This is stronger than saying that high labels are one-shot.

## 1. Coordinate image sets

Let
\[
  A=3m,\qquad T_m=\lfloor\sqrt{6m}\rfloor,\qquad C_m=2T_m.
\]

Define the high A0 coordinate image
\[
  R_0^{\rm hi}(m)\subseteq[1,T_m]\cap\mathbf Z
\]
by
\[
  t\in R_0^{\rm hi}(m)
\]
if and only if there exists a prime
\[
  C_m<p\le A,\qquad p\equiv1\pmod4,\qquad p\nmid A,
\]
and a square root \(i_p^2\equiv-1\pmod p\) such that
\[
  t=\|Ai_p\|_p.
\]

Define the high A1 coordinate image
\[
  R_1^{\rm hi}(m)\subseteq[1,T_m]\cap\mathbf Z
\]
by
\[
  t\in R_1^{\rm hi}(m)
\]
if and only if there exists a prime
\[
  C_m<p\le A,\qquad p\nmid A^2+1,
\]
and a square root
\[
  s_p^2\equiv-A^2-1\pmod p
\]
such that
\[
  t=\|s_p\|_p.
\]

These sets encode every high label in the two layers.

## 2. High-high block condition

Let
\[
  B_q=\{3q+1,3q+2\}
\]
be a complete coprime A-block.

If
\[
  q\equiv m\pmod2,
\]
then
\[
  t_0(q)=3q+1,\qquad t_1(q)=3q+2.
\]
Thus the block is high-high covered if and only if
\[
  3q+1\in R_0^{\rm hi}(m),
  \qquad
  3q+2\in R_1^{\rm hi}(m).
\]

If
\[
  q\not\equiv m\pmod2,
\]
then
\[
  t_0(q)=3q+2,\qquad t_1(q)=3q+1.
\]
Thus the block is high-high covered if and only if
\[
  3q+2\in R_0^{\rm hi}(m),
  \qquad
  3q+1\in R_1^{\rm hi}(m).
\]

Therefore high-high blocks are exactly adjacent pairs in the two image sets:
\[
  \boxed{
  \{3q+1,3q+2\}
  \subset
  R_0^{\rm hi}(m)\cup R_1^{\rm hi}(m)
  }
\]
with the layer assignment dictated by the parity of \(q-m\).

## 3. Shift-intersection form

Define
\[
  E_m=\{q: q\equiv m\pmod2\},
  \qquad
  O_m=\{q: q\not\equiv m\pmod2\}.
\]

The positive-parity high-high blocks are
\[
  \mathcal H_{++}(m)=
  \left\{
  q\in E_m:
  3q+1\in R_0^{\rm hi}(m),\
  3q+2\in R_1^{\rm hi}(m)
  \right\}.
\]
Equivalently,
\[
  3q+1\in
  R_0^{\rm hi}(m)\cap\bigl(R_1^{\rm hi}(m)-1\bigr).
\]

The negative-parity high-high blocks are
\[
  \mathcal H_{-+}(m)=
  \left\{
  q\in O_m:
  3q+2\in R_0^{\rm hi}(m),\
  3q+1\in R_1^{\rm hi}(m)
  \right\}.
\]
Equivalently,
\[
  3q+1\in
  R_1^{\rm hi}(m)\cap\bigl(R_0^{\rm hi}(m)-1\bigr).
\]

Thus all high-high coverage is controlled by the two shift intersections
\[
  R_0^{\rm hi}\cap(R_1^{\rm hi}-1),
  \qquad
  R_1^{\rm hi}\cap(R_0^{\rm hi}-1).
\]

## 4. Exact non-cover reformulation

Let \(\mathcal Q_{\rm cop}(m)\) be the coprime complete block set.  Split it
according to the label zones used in the two layers:
\[
  \mathcal Q_{\rm cop}(m)
  =
  \mathcal Q_{\rm low/mid}
  \cup
  \mathcal Q_{\rm mixed}
  \cup
  \mathcal Q_{\rm hi-hi}.
\]

Here:

- \(\mathcal Q_{\rm low/mid}\) contains blocks where both layers are covered
  by labels \(\le C_m\);
- \(\mathcal Q_{\rm mixed}\) contains blocks where exactly one layer uses a
  high label;
- \(\mathcal Q_{\rm hi-hi}\) is contained in the adjacency set above.

The high-high part therefore satisfies the exact inclusion
\[
  \mathcal Q_{\rm hi-hi}
  \subseteq
  \mathcal H_{++}(m)\cup\mathcal H_{-+}(m).
\]

This replaces high-high residue coverage by a shift-intersection problem for
least-root image sets.

## 5. Closure target

The remaining high-label obstacle can now be stated without primes:

> **High-root adjacency non-cover lemma.**  After removing blocks covered by
> low and middle labels, the two shift intersections
> \[
>   R_0^{\rm hi}\cap(R_1^{\rm hi}-1),
>   \qquad
>   R_1^{\rm hi}\cap(R_0^{\rm hi}-1)
> \]
> cannot contain all remaining complete coprime blocks.

This is a sharper target than bounding the number of high primes.  It asks
for a correlation estimate between two different least-root maps.
