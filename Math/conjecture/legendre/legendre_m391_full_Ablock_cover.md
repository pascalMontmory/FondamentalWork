# The \(m=391\) Full A-Block Cover

This note records an important failed lemma.

The tempting statement
\[
  \text{some coprime complete A-block always has an open A0 or A1 layer}
\]
is false for the current low/middle/high certificate decomposition.

The first full cover found by the least-root zone probe up to \(m=10000\)
is
\[
  m=391,\qquad n=3m=1173.
\]

This is not a counterexample to Legendre.  It is a counterexample to a
pure A-block closure lemma.

## 1. Zone data

For \(m=391\),
\[
  Q_m^\ast=15,\qquad T_m=48,\qquad B_m=94,\qquad C_m=96.
\]

The coprime complete A-block set has
\[
  13
\]
blocks, and the probe reports
\[
\begin{array}{c|c}
\text{quantity} & \text{value}\\
\hline
\text{covered in both layers} & 13\\
\text{A0-open} & 0\\
\text{A1-open} & 0\\
\text{low-low} & 9\\
\text{mixed} & 9\\
\text{high-high} & 2\\
\text{middle involved} & 0.
\end{array}
\]

The priority matrix is
\[
  LL:9,\qquad LH:2,\qquad HL:2.
\]

The full zone matrix is
\[
  LL:9,\qquad LH:4,\qquad HL:6,\qquad HH:2.
\]

Thus every coprime complete A-block has both A0 and A1 locally certified by
eligible labels.  There is no open A-layer.

## 2. Block table

The detailed certificate table is:
\[
\begin{array}{c|c|c|c|c}
q&t_0&t_1&\text{A0 labels}&\text{A1 labels}\\
\hline
0&2&1&L:13,53&H:211\\
2&8&7&L:37&L:11,67\\
3&10&11&L:89&L:71\\
4&14&13&L:5;\ H:101,109&L:17,61\\
5&16&17&L:5;\ H:449,613&L:13\\
6&20&19&L:41&L:7\\
7&22&23&H:277&L:7\\
9&28&29&L:13;\ H:137,773&L:11,47\\
10&32&31&L:61&L:29,79;\ H:601\\
12&38&37&H:433&L:7,11,31;\ H:577\\
13&40&41&L:29&H:683\\
14&44&43&L:5&L:13\\
15&46&47&L:5;\ H:521&L:7,17,37;\ H:313.
\end{array}
\]

## 3. Repair outside the A-block gate

The full four-offset channel is still repaired.  For
\[
  m=391,\qquad n=1173,
\]
one has a nonprimitive witness
\[
  t=3,\qquad r=-1,
\]
giving
\[
  n^2+t^2-1
  =
  1173^2+9-1
  =
  1375937.
\]

The existing measurement script reports this as a \(t=3u\) repair.

Thus \(m=391\) shows exactly why the pure coprime A-block gate cannot be the
whole proof: the A-block gate can close locally, while Legendre is repaired
by the nonprimitive channel.

## 4. Consequence

The next closure theorem must include one of the following:

1. a descent showing that a full A-block cover forces a smaller obstruction;
2. a theorem coupling full A-block covers to the nonprimitive \(t=3u\)
   channel;
3. a direct proof that every full A-block cover is repaired by a bridge or
   nonprimitive witness.

The \(m=391\) case is now the first calibration target for such a theorem.
