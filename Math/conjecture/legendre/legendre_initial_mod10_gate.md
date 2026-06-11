# Initial Mod 10 Gate

This note compresses the first-three-block obstruction into an exact
classification by the residue of \(m\) modulo \(10\).

The setting is the initial triple
\[
  B_0=\{1,2\},\qquad B_1=\{4,5\},\qquad B_2=\{7,8\}.
\]
For \(m\ge11\), all three blocks are complete.

## 1. Three local mechanisms

From the initial-block obstruction, only three exceptional mechanisms can
occur.

### Coprime loss at \(B_1\)

The block \(B_1\) fails to be coprime exactly when
\[
  m\ \text{is odd},\qquad m\equiv\pm1\pmod5.
\]
Equivalently,
\[
  m\equiv1,9\pmod{10}.
\]

In this case \(t_1(1)=5\), and
\[
  5\mid 9m^2+1.
\]
Thus the bridge prime \(5\) divides both candidates in \(B_1\):
\[
  9m^2+4^2\equiv0\pmod5,
\]
\[
  9m^2+5^2+1\equiv0\pmod5.
\]
This is not a coprime pair-cover block.  It must be treated as a bridge
block.

### A0 nonadjacent repetition

The only possible same-layer repetition between \(B_0\) and \(B_2\) is
\[
  p=5
\]
at the coordinate \(t=2\).

The coordinate \(2\) belongs to A0 when \(m\) is odd.  Certification by \(5\)
then requires
\[
  9m^2+2^2\equiv0\pmod5,
\]
so
\[
  m^2\equiv-1\pmod5.
\]
Therefore A0 repetition occurs only in the residue classes
\[
  m\equiv3,7\pmod{10}.
\]

### A1 nonadjacent repetition

The same coordinate \(2\) belongs to A1 when \(m\) is even.

For A1, the repeated \(p=5\) condition is
\[
  -9m^2-1\equiv m^2-1\pmod5
\]
being a nonzero square and compatible with \(t=2\).  This forces
\[
  m\equiv0\pmod5.
\]
Together with even parity, this gives
\[
  m\equiv0\pmod{10}.
\]

## 2. Exact mod \(10\) table

For \(m\ge11\), the initial triple falls into the following exact cases:
\[
\begin{array}{c|c|c}
  m\bmod10 & \text{initial triple status} & \text{allowed }B_0/B_2\text{ repetition}\\
  \hline
  0 & \text{all three blocks coprime} & \text{A1 only, by }5\\
  1 & B_1\text{ is a bridge block} & \text{none in coprime layers}\\
  2 & \text{all three blocks coprime} & \text{none}\\
  3 & \text{all three blocks coprime} & \text{A0 only, by }5\\
  4 & \text{all three blocks coprime} & \text{none}\\
  5 & \text{all three blocks coprime} & \text{none}\\
  6 & \text{all three blocks coprime} & \text{none}\\
  7 & \text{all three blocks coprime} & \text{A0 only, by }5\\
  8 & \text{all three blocks coprime} & \text{none}\\
  9 & B_1\text{ is a bridge block} & \text{none in coprime layers}
\end{array}
\]

Thus the strong classes are
\[
  m\equiv2,4,5,6,8\pmod{10}.
\]
In those classes, the first three blocks are complete and coprime, and in
each layer the three labels are pairwise distinct:
\[
  p_i(0),\ p_i(1),\ p_i(2)
  \quad\text{are pairwise distinct for }i=0,1.
\]

The remaining classes are forced into one of three exact exceptional gates:
\[
\begin{array}{c|c}
  m\bmod10 & \text{exceptional gate}\\
  \hline
  0 & \text{A1 may repeat }5\text{ between }B_0\text{ and }B_2\\
  3,7 & \text{A0 may repeat }5\text{ between }B_0\text{ and }B_2\\
  1,9 & B_1\text{ is a bridge block with bridge prime }5.
\end{array}
\]

## 3. Exact consequence

Any \(m\ge11\) counterexample certificate must pass this mod \(10\) gate.

In particular, there is no longer an undifferentiated initial triple:

1. in five residue classes, the first three coprime blocks require six
   locally valid labels with no same-layer repetition;
2. in class \(0\), only the A1 layer can reuse \(5\) between the two outer
   blocks;
3. in classes \(3,7\), only the A0 layer can reuse \(5\) between the two
   outer blocks;
4. in classes \(1,9\), the middle block is a noncoprime bridge block and must
   be eliminated by a separate bridge argument.

This is a finite exact splitting of the remaining \(m\)-channel.  The next
closure target is to prove that none of the four gates can extend to a full
two-layer certificate on the complete block interval.
