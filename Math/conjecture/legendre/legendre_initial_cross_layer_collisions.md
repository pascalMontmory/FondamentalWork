# Initial Cross-Layer Collisions

This note studies whether a single prime can appear once as an A0 label and
once as an A1 label among the first four complete coprime blocks.

It is a different question from same-layer repetition.  Same-layer repetition
has already been reduced to the mod \(70\) gate.  Here the layers are allowed
to differ.

Throughout this note, assume:
\[
  m\ge21,
\]
and assume the first four blocks are coprime, so
\[
  m\not\equiv\pm1\pmod5.
\]

## 1. Cross-layer collision equation

Let \(x\) be an A0 coordinate and \(y\) an A1 coordinate.  A cross-layer
collision by a prime \(p\ge5\) means
\[
  p\mid 9m^2+x^2,
\]
and
\[
  p\mid 9m^2+y^2+1.
\]

Subtracting gives the fixed congruence
\[
  y^2+1-x^2\equiv0\pmod p.
\]

Therefore every cross-layer collision prime must divide the integer
\[
  \Delta(x,y)=y^2+1-x^2.
\]

This removes \(m\) from the first pass.  The possible primes are divisors of
fixed small integers determined only by the initial coordinates.

We exclude the same block \(x,y\) pair, because in a coprime block the two
candidate values are coprime and therefore cannot share a label prime.

## 2. Even \(m\)

If \(m\) is even, then
\[
  \text{A0 coordinates}=(1,5,7,11),
\]
and
\[
  \text{A1 coordinates}=(2,4,8,10).
\]

After factoring
\[
  \Delta(x,y)=y^2+1-x^2
\]
and imposing the A0 congruence
\[
  9m^2+x^2\equiv0\pmod p,
\]
all valid cross-layer collisions outside the bridge classes are:
\[
\begin{array}{c|c|c|c}
  \text{A0 block} & \text{A1 block} & p & \text{condition on }m\\
  \hline
  B_2 & B_3 & 13 & m\equiv\pm3\pmod{13}\\
  B_3 & B_0 & 29 & m\equiv\pm14\pmod{29}\\
  B_3 & B_1 & 13 & m\equiv\pm1\pmod{13}.
\end{array}
\]

The discarded candidates are:

- \(p=5\), which either belongs to a bridge class or violates the A0
  condition \(p\nmid3m\);
- \(p=7,11,19\), where the required square class for \(m^2\) is not a
  quadratic residue.

Thus, for even \(m\) outside the bridge classes, a cross-layer label sharing
among the first four blocks can only use
\[
  p\in\{13,29\}
\]
and only in the three listed positions.

## 3. Odd \(m\)

If \(m\) is odd, then
\[
  \text{A0 coordinates}=(2,4,8,10),
\]
and
\[
  \text{A1 coordinates}=(1,5,7,11).
\]

The exact valid cross-layer collisions outside the bridge classes are:
\[
\begin{array}{c|c|c|c}
  \text{A0 block} & \text{A1 block} & p & \text{condition on }m\\
  \hline
  B_1 & B_2 & 17 & m\equiv\pm6\pmod{17}\\
  B_1 & B_3 & 53 & m\equiv\pm13\pmod{53}\\
  B_2 & B_3 & 29 & m\equiv\pm3\pmod{29}\\
  B_3 & B_1 & 37 & m\equiv\pm17\pmod{37}.
\end{array}
\]

The discarded candidates are:

- \(p=5\), which would force \(5\mid m\) in A0 and is therefore not an
  allowed A0 certificate;
- \(p=7,11,19,23,31,59\), where the required square class for \(m^2\) is not
  a quadratic residue.

Thus, for odd \(m\) outside the bridge classes, a cross-layer label sharing
among the first four blocks can only use
\[
  p\in\{17,29,37,53\}
\]
and only in the four listed positions.

## 4. Exact consequence

In the strong no-same-layer-repetition classes of the mod \(70\) gate, each
layer already needs four pairwise distinct labels among the first four
blocks.

This note shows that cross-layer identification is also rigid.  Outside the
bridge classes, it can occur only through the following fixed prime gates:
\[
  13,\ 17,\ 29,\ 37,\ 53,
\]
with the exact block positions and residue conditions listed above.

Equivalently, if \(m\) avoids those finitely many cross-layer congruence
classes in addition to the bridge classes, then the first four complete
blocks force eight distinct certificate labels:
\[
  p_0(0),p_0(1),p_0(2),p_0(3),
  p_1(0),p_1(1),p_1(2),p_1(3)
  \quad\text{all distinct}.
\]

This still does not close Legendre.  It sharpens the remaining proof target:
any counterexample in the strong gate must either use eight distinct small
prime labels immediately, or fall into one of the explicit cross-layer
collision congruences above.
