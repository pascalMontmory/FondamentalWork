# Shared-\(5\) Fiber Equals the \(B_3\) Bridge Gate

This note couples the collapsed shared-\(5\) \(u=1\)-fiber to the first
A-blocks.

It gives a concrete result: the shared-\(5\) fiber is not an ordinary
coprime-block fiber.  It is exactly the even \(B_3\) bridge class among the
first four blocks.

Throughout,
\[
  A=3m,
\]
and \(m\) is even.

## 1. Shared-\(5\) rewritten in \(m\)

The shared-\(5\) fiber is
\[
  A\equiv\pm2\pmod5.
\]
Since
\[
  A=3m
\]
and \(3^{-1}\equiv2\pmod5\), this is equivalent to
\[
  m\equiv2(\pm2)\pmod5,
\]
that is
\[
\boxed{
  m\equiv\pm1\pmod5.
}
\]

Thus the shared-\(5\) fiber is precisely
\[
  m\ \text{even},\qquad m\equiv\pm1\pmod5.
\]

## 2. This is exactly the \(B_3\) bridge class

For even \(m\), the first four block coordinates are
\[
  \text{A0}:\quad O=(1,5,7,11),
\]
\[
  \text{A1}:\quad E=(2,4,8,10).
\]

The fourth block is
\[
  B_3=\{10,11\}.
\]
For even \(m\), its candidates are
\[
  A^2+11^2=A^2+121
\]
in A0 and
\[
  A^2+10^2+1=A^2+101
\]
in A1.

If \(A^2\equiv-1\pmod5\), then
\[
  A^2+121\equiv -1+1\equiv0\pmod5,
\]
and
\[
  A^2+101\equiv -1+1\equiv0\pmod5.
\]

Therefore:
\[
\boxed{
  A\equiv\pm2\pmod5
  \quad\Longrightarrow\quad
  B_3\text{ is a bridge block with bridge prime }5.
}
\]

Conversely, the even \(B_3\) bridge condition is
\[
  m\equiv\pm1\pmod5,
\]
which is the same as
\[
  A\equiv\pm2\pmod5.
\]

Hence:
\[
\boxed{
  \text{shared-}5\text{ fiber}
  =
  \text{even }B_3\text{ bridge fiber}.
}
\]

## 3. Consequence for the next coprime blocks

The shared-\(5\) collapse already fixed the anchor offsets
\[
  A^2+1,\qquad A^2+11
\]
by the label \(5\), and left only the colored divisor equation for
\[
  A^2+5.
\]

The equality with the \(B_3\) bridge gate says that the next block \(B_3\)
does not provide a coprime A-block pair.  Its two candidates are both killed
by the same bridge prime \(5\).

Therefore the first genuinely coprime blocks beyond the anchor in this
fiber are
\[
  B_1=\{4,5\},\qquad B_2=\{7,8\}.
\]

Their even-\(m\) offsets are:
\[
  B_1:\quad A^2+25\ \text{in A0},\qquad A^2+17\ \text{in A1},
\]
and
\[
  B_2:\quad A^2+49\ \text{in A0},\qquad A^2+65\ \text{in A1}.
\]

Since \(A^2\equiv-1\pmod5\), these are congruent modulo \(5\) to
\[
  4,\quad1,\quad3,\quad4.
\]
Thus the bridge prime \(5\) cannot certify any of the four \(B_1,B_2\)
coprime candidates.

## 4. Fresh-label consequence

For \(m\ge11\), the blocks \(B_1\) and \(B_2\) are complete and coprime in
this fiber.

Adjacent same-layer repetition between \(B_1\) and \(B_2\) is impossible for
prime labels \(p\ge5\), because the coordinate differences and sums give no
eligible prime divisor in either sequence.

Therefore a full cover in the shared-\(5\) fiber must supply four non-\(5\)
labels for the two coprime blocks:
\[
  A^2+25,\quad A^2+17,\quad A^2+49,\quad A^2+65.
\]

In centered form, there must exist prime labels
\[
  p_c=A-r_c\ge7,
  \qquad c\in\{17,25,49,65\},
\]
with
\[
\boxed{
  A-r_c\mid r_c^2+c
  \qquad(c\in\{17,25,49,65\}).
}
\]

The labels in each of the two layers are distinct between \(B_1\) and
\(B_2\); and within each block, the A0 and A1 labels must be distinct because
the block is coprime.

Thus the shared-\(5\) fiber has the following exact structure:

1. fixed anchor atom:
   \[
     p_1=p_{11}=5,\qquad e_{11}=e_1+2;
   \]
2. one remaining anchor equation:
   \[
     A-r_5\mid r_5^2+5,\qquad p_5\ge7;
   \]
3. \(B_3\) is a bridge, not a coprime resource:
   \[
     5\mid A^2+101,\qquad5\mid A^2+121;
   \]
4. the next coprime pressure is the four-offset system
   \[
     \{17,25,49,65\}.
   \]

## 5. New closure target for this fiber

The shared-\(5\) fiber should no longer be attacked as a three-offset anchor
cluster.  It has collapsed to:
\[
  \{5\}
  \quad\text{plus}\quad
  \{17,25,49,65\}
\]
with a bridge block in between.

The exact closure target is:

> In the even bridge fiber \(A\equiv\pm2\pmod5\), the single colored anchor
> equation for \(A^2+5\), together with the four non-\(5\) labels
> required by \(B_1,B_2\), cannot coexist with the full A-block cover
> constraints unless a nonprimitive repair occurs.

This is a concrete refinement: the next-block coupling does not use \(B_3\);
it proves that \(B_3\) is exactly the bridge already encoded by shared-\(5\),
so the first usable coprime pressure is \(B_1,B_2\).
