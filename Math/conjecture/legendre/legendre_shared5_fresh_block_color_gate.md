# Fresh-Block Colors in the Shared-\(5\) Bridge Fiber

This note continues the shared-\(5\) bridge coupling.

The previous note proved that the shared-\(5\) fiber
\[
  A\equiv\pm2\pmod5
\]
is exactly the even \(B_3\) bridge fiber.  Hence the first usable coprime
pressure beyond the anchor comes from
\[
  B_1,\ B_2,
\]
with offsets
\[
  \{17,25,49,65\}.
\]

Here we record the exact quadratic-residue colors for these four fresh
offsets.

## 1. Setup

We are in the even shared-\(5\) fiber:
\[
  A=3m,\qquad m\ \text{even},\qquad A^2\equiv-1\pmod5.
\]

The anchor has collapsed to
\[
  p_1=p_{11}=5,
\]
and the remaining anchor offset is \(c=5\).

The first coprime pressure beyond the anchor and the bridge block \(B_3\) is
\[
  B_1:\quad c=25,\ 17,
\]
\[
  B_2:\quad c=49,\ 65.
\]

For each such offset, a failed prime witness gives a label
\[
  p_c=A-r_c
\]
with
\[
  p_c\mid A^2+c,
\]
or equivalently
\[
  A-r_c\mid r_c^2+c.
\]

Since \(A^2\equiv-1\pmod5\), none of these four offsets can be certified by
the bridge prime \(5\):
\[
  A^2+17\equiv1,\quad
  A^2+25\equiv4,\quad
  A^2+49\equiv3,\quad
  A^2+65\equiv4
  \pmod5.
\]

Thus every fresh label satisfies
\[
  p_c\ge7.
\]

## 2. Offset \(17\)

For \(c=17\), the ramified possibility is
\[
  p_{17}=17,\qquad17\mid A.
\]

Outside this gate,
\[
  \left(\frac{-17}{p_{17}}\right)=1.
\]
The classes are
\[
  p_{17}\equiv
  1,3,7,9,11,13,21,23,25,27,31,33,39,49,53,63
  \pmod {68}.
\]

Thus
\[
\boxed{
  r_{17}\equiv A-s\pmod {68}
}
\]
for one of those classes \(s\), unless \(p_{17}=17\) and \(17\mid A\).

## 3. Offset \(25\)

For \(c=25\), the only prime dividing the offset is \(5\), but \(5\) cannot
divide \(A^2+25\) in the shared-\(5\) fiber.  Therefore there is no ramified
label.

Since \(25\) is a square,
\[
  \left(\frac{-25}{p_{25}}\right)
  =
  \left(\frac{-1}{p_{25}}\right).
\]
Hence
\[
\boxed{
  p_{25}\equiv1\pmod4,
  \qquad
  r_{25}\equiv A-1\pmod4.
}
\]

## 4. Offset \(49\)

For \(c=49\), the ramified possibility is
\[
  p_{49}=7,\qquad7\mid A.
\]

Outside this gate,
\[
  \left(\frac{-49}{p_{49}}\right)
  =
  \left(\frac{-1}{p_{49}}\right).
\]
Thus
\[
\boxed{
  p_{49}\equiv1\pmod4,
  \qquad
  r_{49}\equiv A-1\pmod4,
}
\]
unless \(p_{49}=7\) and \(7\mid A\).

## 5. Offset \(65\)

For \(c=65=5\cdot13\), the label \(5\) is impossible in the shared-\(5\)
fiber, because
\[
  A^2+65\equiv4\pmod5.
\]

The only ramified possibility is therefore
\[
  p_{65}=13,\qquad13\mid A.
\]

Outside this gate,
\[
  \left(\frac{-65}{p_{65}}\right)=1.
\]
The allowed classes are
\[
\begin{gathered}
1,3,9,11,19,23,27,29,31,33,37,43,49,57,59,61,\\
69,71,73,81,87,93,97,99,101,103,107,111,119,121,\\
127,129,137,147,151,171,177,181,183,193,197,207,\\
209,213,219,239,243,253
\pmod {260}.
\end{gathered}
\]

Thus
\[
\boxed{
  r_{65}\equiv A-s\pmod {260}
}
\]
for one of those classes \(s\), unless \(p_{65}=13\) and \(13\mid A\).

## 6. Resulting shared-\(5\) obstruction

The shared-\(5\) bridge fiber now has the exact colored system:

Anchor:
\[
  p_1=p_{11}=5,\qquad e_{11}=e_1+2,
\]
and
\[
  A-r_5\mid r_5^2+5,\qquad
  p_5\equiv1,3,7,9\pmod {20}.
\]

Bridge:
\[
  5\mid A^2+101,\qquad5\mid A^2+121.
\]

Fresh coprime blocks:
\[
  A-r_c\mid r_c^2+c,
  \qquad
  c\in\{17,25,49,65\},
\]
with the color gates:
\[
  c=17:\quad (-17/p)=1\ \text{or }17\mid A,
\]
\[
  c=25:\quad p\equiv1\pmod4,
\]
\[
  c=49:\quad p\equiv1\pmod4\ \text{or }7\mid A,
\]
\[
  c=65:\quad (-65/p)=1\ \text{or }13\mid A.
\]

This is a concrete sharpened target for the shared-\(5\) fiber: it is now a
five-equation colored divisor system, plus the fixed \(B_3\) bridge atom.
