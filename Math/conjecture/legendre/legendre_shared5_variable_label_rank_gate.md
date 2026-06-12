# Variable Label Rank Gate in the Shared-\(5\) Fiber

This note strengthens the shared-\(5\) bridge fiber.

The previous reduction produced one remaining anchor offset and four fresh
coprime-block offsets:
\[
  \mathcal C=\{5,17,25,49,65\}.
\]

Here we prove a concrete capacity result: in the shared-\(5\) fiber, the five
prime labels attached to these offsets are pairwise distinct.  Consequently,
for all sufficiently large \(A\), their five quotient parameters are also
pairwise distinct and obey rank barriers.

Throughout,
\[
  A=3m,\qquad m\ \text{even},\qquad A^2\equiv-1\pmod5.
\]

## 1. Pairwise label separation

Suppose the same prime label \(p\) certifies two offsets \(c\ne d\):
\[
  p\mid A^2+c,\qquad p\mid A^2+d.
\]
Then
\[
  p\mid d-c.
\]

For
\[
  \mathcal C=\{5,17,25,49,65\},
\]
the positive differences are
\[
\begin{array}{c|c}
  (c,d)&d-c\\
  \hline
  (5,17)&12\\
  (5,25)&20\\
  (5,49)&44\\
  (5,65)&60\\
  (17,25)&8\\
  (17,49)&32\\
  (17,65)&48\\
  (25,49)&24\\
  (25,65)&40\\
  (49,65)&16.
\end{array}
\]

Every possible common prime \(p\ge7\) is excluded immediately, except
possibly
\[
  p=11
\]
from the difference \(44\) in the pair
\[
  (5,49).
\]

For that pair, common certification by \(11\) would require
\[
  A^2+5\equiv0\pmod {11},
\]
or
\[
  A^2\equiv -5\equiv6\pmod {11}.
\]
But the square classes modulo \(11\) are
\[
  1,3,4,5,9,
\]
so \(6\) is not a square.  Therefore this exceptional possibility is also
impossible.

Hence:
\[
\boxed{
  c\ne d\in\{5,17,25,49,65\}
  \quad\Longrightarrow\quad
  p_c\ne p_d.
}
\]

The shared-\(5\) fiber therefore has five genuinely distinct variable
labels, in addition to the fixed bridge/anchor label \(5\).

## 2. Equal quotient obstruction for the five variables

For a centered divisor equation
\[
  A-r_c\mid r_c^2+c,
\]
write
\[
  e_c=\frac{r_c^2+c}{A-r_c}.
\]

If two distinct offsets \(c,d\in\mathcal C\) have equal quotient
\[
  e_c=e_d,
\]
then the equal-quotient obstruction gives
\[
  r_c\le |c-d|-2.
\]

The largest offset difference in \(\mathcal C\) is
\[
  65-5=60,
\]
so equal quotients force
\[
  r_c\le58.
\]
Since \(e_c\ge1\),
\[
  A
  =
  r_c+\frac{r_c^2+c}{e_c}
  \le
  r_c+r_c^2+c
  \le
  58+58^2+65
  =
  3487.
\]

Therefore:
\[
\boxed{
  A\ge3488
  \quad\Longrightarrow\quad
  e_c\ne e_d
  \text{ for all distinct }c,d\in\{5,17,25,49,65\}.
}
\]

Since \(A=3m\), this holds for
\[
  m\ge1163.
\]

## 3. Five quotient-rank barriers

For
\[
  A\ge3488,
\]
order the five quotients as
\[
  e_{(1)}<e_{(2)}<e_{(3)}<e_{(4)}<e_{(5)}.
\]
Then
\[
  e_{(k)}\ge k,\qquad1\le k\le5.
\]

Every offset in \(\mathcal C\) satisfies
\[
  c\le65.
\]
Thus each quotient rank gives
\[
\boxed{
  r_{(k)}
  \ge
  \left\lceil
    \frac{-k+\sqrt{k^2+4(kA-65)}}{2}
  \right\rceil
  \qquad(1\le k\le5).
}
\]

In particular, the top rank forces
\[
\boxed{
  r_{(5)}
  \ge
  \left\lceil
    \frac{-5+\sqrt{20A-235}}{2}
  \right\rceil.
}
\]

Equivalently, at least one of the five variable labels satisfies
\[
\boxed{
  p=A-r
  \le
  A-
  \left\lceil
    \frac{-5+\sqrt{20A-235}}{2}
  \right\rceil.
}
\]

## 4. Closure consequence for shared-\(5\)

The shared-\(5\) fiber now has the following exact structure:

1. fixed label \(5\) covers the anchor offsets \(1,11\);
2. fixed label \(5\) also bridges \(B_3\);
3. the five remaining offsets
   \[
     \{5,17,25,49,65\}
   \]
   require five pairwise distinct prime labels;
4. for \(A\ge3488\), those five labels also have five distinct quotient
   ranks with the barriers above.

Thus any large shared-\(5\) obstruction has a definite rank cost:
\[
  \text{one fixed }5\text{-atom}
  \quad+\quad
  \text{five distinct variable labels}
  \quad+\quad
  \text{five distinct quotient ranks}.
\]

This is a nonstandard certificate obstruction: the difficulty is no longer
to find a prime directly, but to realize a rigid multi-rank composite
certificate around the moving center \(A\).
