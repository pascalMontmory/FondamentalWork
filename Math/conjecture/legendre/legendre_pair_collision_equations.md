# Pair Collision Equations

This note proves the exact two-block collision equations for the remaining
A-block pair-cover gate.

It is a proof-level reduction, not a numerical test.

## Setup

Fix \(m\ge1\).  For a block index \(q\), write
\[
  a_q=3q+1,\qquad b_q=3q+2.
\]

The A1 coordinate \(t_1(q)\) is the member of \(\{a_q,b_q\}\) with the same
parity as \(m\), and \(t_0(q)\) is the other member.  Thus
\[
  t_0(q)=3q+\alpha_q,\qquad t_1(q)=3q+\beta_q,
\]
where
\[
  \{\alpha_q,\beta_q\}=\{1,2\}.
\]
Moreover the orientation flips when \(q\) is replaced by \(q+1\).

Assume one ordered pair of certificate primes \((p_0,p_1)\) covers two
complete coprime blocks \(q\ne r\):
\[
  t_0(q)^2\equiv-9m^2\pmod {p_0},
  \qquad
  t_0(r)^2\equiv-9m^2\pmod {p_0},
\]
and
\[
  t_1(q)^2\equiv-9m^2-1\pmod {p_1},
  \qquad
  t_1(r)^2\equiv-9m^2-1\pmod {p_1}.
\]

Here
\[
  p_0\ge5,\quad p_0\equiv1\pmod4,\quad p_0\nmid3m,
\]
\[
  p_1\ge5,\quad p_1\ne p_0.
\]

## Collision Lemma

The repeated pair \((p_0,p_1)\) must satisfy
\[
  p_0\mid
  \bigl(t_0(q)-t_0(r)\bigr)
  \bigl(t_0(q)+t_0(r)\bigr)
\]
and
\[
  p_1\mid
  \bigl(t_1(q)-t_1(r)\bigr)
  \bigl(t_1(q)+t_1(r)\bigr).
\]

Equivalently,
\[
  p_0\mid
  \bigl(3(q-r)+\alpha_q-\alpha_r\bigr)
  \bigl(3(q+r)+\alpha_q+\alpha_r\bigr),
\]
and
\[
  p_1\mid
  \bigl(3(q-r)+\beta_q-\beta_r\bigr)
  \bigl(3(q+r)+\beta_q+\beta_r\bigr).
\]

### Proof

Subtract the two A0 congruences:
\[
  t_0(q)^2-t_0(r)^2\equiv0\pmod {p_0}.
\]
Factoring gives
\[
  \bigl(t_0(q)-t_0(r)\bigr)
  \bigl(t_0(q)+t_0(r)\bigr)\equiv0\pmod {p_0}.
\]
The A1 identity is identical:
\[
  t_1(q)^2-t_1(r)^2\equiv0\pmod {p_1}.
\]
Substituting \(t_i(s)=3s+\alpha_i(s)\) gives the displayed linear factors.
\(\square\)

## Parity-Split Form

If \(q\equiv r\pmod2\), then the orientation is the same for \(q\) and \(r\).
Hence
\[
  \alpha_q=\alpha_r,\qquad \beta_q=\beta_r,
\]
and the collision equations become
\[
  p_0\mid 3(q-r)\quad\text{or}\quad
  p_0\mid 3(q+r)+2\alpha_q,
\]
\[
  p_1\mid 3(q-r)\quad\text{or}\quad
  p_1\mid 3(q+r)+2\beta_q.
\]
Since \(p_0,p_1\ge5\), the difference branch is
\[
  p_i\mid q-r.
\]

If \(q\not\equiv r\pmod2\), then the orientation is reversed.  Writing
\[
  \alpha_q-\alpha_r=\varepsilon,\qquad
  \beta_q-\beta_r=-\varepsilon,\qquad \varepsilon\in\{\pm1\},
\]
the collision equations become
\[
  p_0\mid 3(q-r)+\varepsilon
  \quad\text{or}\quad
  p_0\mid 3(q+r+1),
\]
\[
  p_1\mid 3(q-r)-\varepsilon
  \quad\text{or}\quad
  p_1\mid 3(q+r+1).
\]
Since \(p_0,p_1\ge5\), the mirror branch is
\[
  p_i\mid q+r+1.
\]

## Consequences

1. Same-parity repeated coverage forces each layer prime either to divide the
   separation \(q-r\), or to divide one of two layer-specific mirror sums
   \(3(q+r)+2\) or \(3(q+r)+4\).

2. Opposite-parity repeated coverage forces each layer prime either to divide
   one of the two adjacent-difference forms
   \[
     3(q-r)+1,\qquad 3(q-r)-1,
   \]
   or to divide the common mirror sum
   \[
     q+r+1.
   \]

3. For adjacent blocks \(r=q+1\), the mirror branch recovers the earlier
   adjacent obstruction:
   \[
     p_i\mid q+1.
   \]

Thus any dense counterexample must either use many one-shot prime pairs, or
must place repeated pairs on the explicit divisor hyperplanes above.

## Why This Does Not Yet Close Legendre

The lemma gives necessary equations for repeated pair labels, but it does
not rule out a cover by mostly one-shot pairs.  To finish the proof, one
must combine these collision equations with a capacity bound showing that
one-shot pairs and divisor-hyperplane repetitions cannot cover all complete
coprime A-blocks.

So the next exact theorem is a capacity theorem, not another local congruence:
\[
  \text{one-shot pairs}+\text{collision hyperplanes}
  \quad\text{cannot cover}\quad
  \mathcal Q_{\rm cop}(m).
\]
