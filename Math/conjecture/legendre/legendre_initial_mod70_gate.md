# Initial Mod 70 Gate

This note compresses the first-four-block graph into one exact CRT gate.

The four blocks are
\[
  B_0,\ B_1,\ B_2,\ B_3.
\]
They are complete for
\[
  m\ge21.
\]

The relevant moduli are:

- \(10\), for parity and the \(p=5\) bridge/repetition conditions;
- \(14\), for the even \(p=7\) A1 repetition condition.

Thus the complete first-four-block gate is naturally modulo
\[
  \operatorname{lcm}(10,14)=70.
\]

## 1. Bridge classes

Among the first four blocks, a bridge occurs exactly when
\[
  m\equiv\pm1\pmod5.
\]

More precisely:
\[
  B_1\text{ is a bridge block}
  \quad\Longleftrightarrow\quad
  m\equiv1,9\pmod{10},
\]
and
\[
  B_3\text{ is a bridge block}
  \quad\Longleftrightarrow\quad
  m\equiv4,6\pmod{10}.
\]

Therefore the bridge classes modulo \(70\) are:
\[
\begin{gathered}
1,4,6,9,11,14,16,19,21,24,26,29,31,34,36,39,\\
41,44,46,49,51,54,56,59,61,64,66,69.
\end{gathered}
\]

These classes leave the coprime pair-cover graph and require bridge
elimination.

## 2. Coprime repetition edges

Outside the bridge classes, the first four blocks are complete and coprime.

The possible same-layer repetitions are exactly:
\[
\begin{array}{c|c|c|c}
  \text{edge} & \text{layer} & \text{prime} & \text{condition}\\
  \hline
  B_0/B_2 & \text{A1} & 5 & m\equiv0\pmod{10}\\
  B_0/B_2 & \text{A0} & 5 & m\equiv3,7\pmod{10}\\
  B_1/B_3 & \text{A1} & 7 & m\equiv4,10\pmod{14}.
\end{array}
\]

The last line is equivalent to
\[
  m\text{ even},\qquad m\equiv\pm3\pmod7.
\]

## 3. Exact residue classes modulo \(70\)

### No same-layer repetition

In the following coprime classes, there is no same-layer repetition among
\[
  B_0,\ B_1,\ B_2,\ B_3:
\]
\[
\boxed{
  2,5,8,12,15,22,25,28,35,42,45,48,55,58,62,65,68.
}
\]

For these \(17\) classes, each layer needs four pairwise distinct labels on
the first four blocks.

### A0 edge only

The A0 \(B_0/B_2\) edge by \(5\) occurs in exactly the classes
\[
\boxed{
  3,7,13,17,23,27,33,37,43,47,53,57,63,67.
}
\]

There are no A1 same-layer repetitions among the first four blocks in these
classes.

### A1 \(5\)-edge only

The A1 \(B_0/B_2\) edge by \(5\), with no \(7\)-edge, occurs in exactly
\[
\boxed{
  0,20,30,40,50.
}
\]

### A1 \(7\)-edge only

The A1 \(B_1/B_3\) edge by \(7\), with no \(5\)-edge, occurs in exactly
\[
\boxed{
  18,32,38,52.
}
\]

### Two A1 edges

Both A1 edges occur exactly when
\[
  m\equiv0\pmod{10}
  \quad\text{and}\quad
  m\equiv4,10\pmod{14}.
\]
Modulo \(70\), this gives
\[
\boxed{
  10,60.
}
\]

In these two classes, A1 may repeat \(5\) on \(B_0/B_2\) and \(7\) on
\(B_1/B_3\), while A0 has no same-layer repetition among the first four
blocks.

## 4. Exhaustion check

The \(70\) residue classes are partitioned as:
\[
  28\ \text{bridge classes}
  +17\ \text{no-repetition classes}
  +14\ \text{A0-edge classes}
  +5\ \text{A1-}5\text{-only classes}
  +4\ \text{A1-}7\text{-only classes}
  +2\ \text{double-A1 classes}
  =70.
\]

This is an exact CRT decomposition, not an experimental one.

## 5. Exact consequence

For \(m\ge21\), every hypothetical \(m\)-certificate enters exactly one of
the following gates:

1. a bridge gate \(m\equiv\pm1\pmod5\);
2. a strong coprime gate with no same-layer repetition among the first four
   blocks;
3. a coprime A0-\(5\) edge gate;
4. a coprime A1-\(5\) edge gate;
5. a coprime A1-\(7\) edge gate;
6. a coprime double-A1 gate with both \(5\) and \(7\).

Thus the first-four-block beginning of any counterexample is completely
localized modulo \(70\).  The next closure target is to eliminate these six
finite gate types, starting with the strong no-repetition gate and the bridge
gate.
