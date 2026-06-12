# Mixed High-Low Neighbor Gate

This note handles the mixed cells of the layer-zone matrix:
\[
  (H_0,L_1),\quad (L_0,H_1),
\]
and their finite middle-label variants.

The point is simple but useful: once one layer is high, its coordinate is a
least-root image.  The opposite layer is forced to be the adjacent coordinate
in the same A-block.

## 1. Neighbor maps

Let
\[
  R_0^{\rm hi}(m),\qquad R_1^{\rm hi}(m)
\]
be the high coordinate image sets from the high-high adjacency gate.

For a coordinate \(t\), define its A-block neighbor
\[
  \operatorname{nb}(t)=
  \begin{cases}
  t+1,&t\equiv1\pmod3,\\
  t-1,&t\equiv2\pmod3.
  \end{cases}
\]
This is defined on \(3\nmid t\).  The pair
\[
  \{t,\operatorname{nb}(t)\}
\]
is exactly the complete A-block containing \(t\), provided the neighbor is
admissible.

## 2. Mixed cell \((H_0,L_1)\)

Suppose a block lies in \((H_0,L_1)\).  Then its A0 coordinate belongs to
\[
  R_0^{\rm hi}(m).
\]
Call it \(t_0\).  The A1 coordinate is forced:
\[
  t_1=\operatorname{nb}(t_0).
\]

Therefore the block can lie in \((H_0,L_1)\) only if
\[
  t_0\in R_0^{\rm hi}(m),
\]
the neighbor \(t_1\) is admissible in A1, and
\[
  A^2+t_1^2+1
\]
has a low label
\[
  p_1\le B_m.
\]

Equivalently,
\[
  \boxed{
  t_0\in R_0^{\rm hi}(m)
  \quad\text{and}\quad
  \operatorname{nb}(t_0)\in S_1^{\rm low}(m).
  }
\]

Here
\[
  S_1^{\rm low}(m)=
  \{t: A^2+t^2+1\equiv0\pmod p
  \text{ for some eligible }p\le B_m\}.
\]

## 3. Mixed cell \((L_0,H_1)\)

Similarly, a block lies in \((L_0,H_1)\) only if its A1 coordinate
\[
  t_1\in R_1^{\rm hi}(m)
\]
and the A0 neighbor
\[
  t_0=\operatorname{nb}(t_1)
\]
has a low A0 label:
\[
  A^2+t_0^2\equiv0\pmod p
  \qquad
  \text{for some eligible }p\le B_m.
\]

Equivalently,
\[
  \boxed{
  t_1\in R_1^{\rm hi}(m)
  \quad\text{and}\quad
  \operatorname{nb}(t_1)\in S_0^{\rm low}(m).
  }
\]

## 4. Middle-label variants

The same statements hold with low replaced by low-or-middle:
\[
  p\le C_m.
\]
Since
\[
  0\le C_m-B_m\le4,
\]
the middle contribution adds only a bounded endpoint correction to the low
sets:
\[
  S_i^{\le C}(m)=S_i^{\rm low}(m)\cup S_i^{\rm mid}(m).
\]

Thus all mixed cells are controlled by neighbor images:
\[
  R_0^{\rm hi}\xrightarrow{\operatorname{nb}}S_1^{\le C},
  \qquad
  R_1^{\rm hi}\xrightarrow{\operatorname{nb}}S_0^{\le C}.
\]

## 5. Exact mixed-cell non-cover target

The mixed cells cannot be studied as independent high and low covers.  They
must satisfy adjacency:

> **Mixed neighbor non-cover lemma.**  The neighbor images
> \[
>   \operatorname{nb}(R_0^{\rm hi})\cap S_1^{\le C},
>   \qquad
>   \operatorname{nb}(R_1^{\rm hi})\cap S_0^{\le C}
> \]
> together with the high-high adjacency set and the low-low cofactor box do
> not cover all complete coprime A-blocks.

This is the exact mixed-cell form needed for a final global non-cover proof.
