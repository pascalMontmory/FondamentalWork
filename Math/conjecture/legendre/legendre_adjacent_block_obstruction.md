# Adjacent Block Obstruction

This note strengthens the repetition constraints for neighboring coprime
A-blocks.

The previous repetition note showed that if a prime certifies two blocks in
one layer, then their indices satisfy either a progression relation or a
mirror relation.  For adjacent blocks \(q\) and \(q+1\), this collapses to a
very simple condition:

\[
  p\mid q+1.
\]

Thus a single prime can certify two adjacent blocks in the same layer only at
explicit divisor positions.

## 1. Orientation flips between adjacent blocks

Let
\[
  a_q=3q+1,\qquad b_q=3q+2.
\]
The parity of
\[
  a_q=3q+1
\]
changes when \(q\) is replaced by \(q+1\), because
\[
  a_{q+1}=3q+4.
\]
Therefore the orientation of the block flips between \(q\) and \(q+1\).

Recall:

- \(t_1(q)\) is the member of \(\{a_q,b_q\}\) with the same parity as \(m\);
- \(t_0(q)\) is the other member.

There are two cases.

### Case I

If
\[
  a_q\equiv m\pmod2,
\]
then
\[
  t_1(q)=3q+1,\qquad t_0(q)=3q+2.
\]
For \(q+1\), the orientation flips, so
\[
  t_1(q+1)=3q+5,\qquad t_0(q+1)=3q+4.
\]

### Case II

If
\[
  a_q\not\equiv m\pmod2,
\]
then
\[
  t_1(q)=3q+2,\qquad t_0(q)=3q+1.
\]
For \(q+1\), the orientation flips, so
\[
  t_1(q+1)=3q+4,\qquad t_0(q+1)=3q+5.
\]

In both cases, the sum of the same-layer adjacent coordinates is
\[
  t_i(q)+t_i(q+1)=6(q+1),
  \qquad i=0,1.
\]

## 2. Same-prime adjacent repetition

Suppose a prime
\[
  p\ge5
\]
certifies both adjacent blocks \(q\) and \(q+1\) in the same layer \(i\).
Then the same quadratic right-hand side is used in both congruences, so
\[
  t_i(q)^2\equiv t_i(q+1)^2\pmod p.
\]
Thus
\[
  \bigl(t_i(q+1)-t_i(q)\bigr)
  \bigl(t_i(q+1)+t_i(q)\bigr)
  \equiv0\pmod p.
\]

The adjacent difference is either \(2\) or \(4\), never divisible by
\[
  p\ge5.
\]
Therefore
\[
  p\mid t_i(q+1)+t_i(q).
\]
Using the identity above gives
\[
  p\mid 6(q+1).
\]
Since \(p\ge5\), this is equivalent to
\[
  \boxed{p\mid q+1.}
\]

This holds for both A0 and A1.

## 3. Consequence for adjacent double coverage

Let \(q,q+1\) be adjacent coprime complete A-blocks.

If a counterexample covers both blocks in the A0 layer with the same prime
\[
  p_0,
\]
then
\[
  p_0\mid q+1.
\]

If it covers both blocks in the A1 layer with the same prime
\[
  p_1,
\]
then
\[
  p_1\mid q+1.
\]

Therefore, except at divisor positions of \(q+1\), adjacent blocks must use
different certificate primes in each layer.

## 4. Local pressure on runs of adjacent blocks

Consider a run of consecutive coprime complete blocks
\[
  q,\ q+1,\ \dots,\ q+L.
\]
In one fixed layer, a prime \(p\ge5\) can certify two adjacent blocks in this
run only at an index \(j\) for which
\[
  p\mid j+1.
\]

Thus, for a prime \(p\), adjacent repetition can occur only at the sparse
positions
\[
  j\equiv-1\pmod p.
\]

Away from these positions, the certificate prime must change from one block
to the next.

This is a strong local constraint on a dense counterexample: long runs of
coprime complete blocks require frequent changes of certificate primes in
both A0 and A1 layers.

## 5. Exact next target

The next obstruction should combine:

1. adjacent repetition is possible only when the repeated prime divides
   \(q+1\);
2. A0 primes must satisfy
   \[
     p_0\equiv1\pmod4,\qquad p_0\nmid3m;
   \]
3. A1 primes must satisfy
   \[
     p_1\nmid9m^2+1,\qquad
     \left(\frac{-9m^2-1}{p_1}\right)=1;
   \]
4. on each coprime block, the two layer primes must be distinct.

This turns a hypothetical counterexample into a labeling problem on an
interval of \(q\)-indices, with strict rules for when labels can repeat on
adjacent vertices.

Closing the combined A-channel now amounts to proving that no such labeling
exists for all coprime complete blocks.
