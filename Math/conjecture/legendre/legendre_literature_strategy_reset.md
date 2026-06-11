# Legendre Literature Strategy Reset

This note is a deliberate pause.

The quotient-skeleton route produced a precise certificate language, but it
has not produced a contradiction.  Continuing to refine isolated local
congruences is unlikely to close Legendre by itself.

The goal here is to identify which modern mathematical tools could plausibly
move the problem, and which routes should be downgraded to partial
obstructions.

## 1. What a proof must beat

Legendre asks for a prime in
\[
  (n^2,(n+1)^2).
\]

Putting
\[
  x=n^2,
\]
the interval length is
\[
  (n+1)^2-n^2=2n+1\asymp x^{1/2}.
\]

Thus any global prime-gap proof needs, in effect,
\[
  p_{k+1}-p_k < 2\sqrt{p_k}
\]
at the relevant scale.

Current unconditional prime-gap technology is still above this threshold.
The classical Baker-Harman-Pintz exponent gives primes in intervals of
length roughly
\[
  x^{0.525},
\]
which is close but still strictly larger than
\[
  x^{1/2}.
\]

Recent Guth-Maynard technology gives major new estimates for Dirichlet
polynomials and short-interval asymptotics, but the exponent in the known
short-interval consequence is still above the Legendre threshold.

So an analytic proof by known short-interval machinery would require a real
breakthrough at the square-root barrier.

## 2. Why pure sieve cannot close it

Recent almost-prime results are very close structurally.  In particular,
there are now explicit theorems proving that every interval between
consecutive squares contains an integer with at most three prime factors.

This is strong evidence that the right interval is sieve-accessible.
However, it is not a proof of Legendre because of the parity problem of
sieve theory: a sieve can often force an almost-prime but cannot usually
separate a prime from a product of two or three primes.

Therefore a route based only on Richert weights, linear sieve, or
Bombieri-Vinogradov style distribution will probably stop at almost-primes
unless it imports a genuinely new prime-detecting ingredient.

## 3. Status of our quotient-certificate route

The quotient route reduced the clean strong gate to six exact residue
skeletons for the hidden quotients \(e_i\):
\[
\begin{array}{c|c}
  \text{residue branch} & \text{global quotient minima}\\
  \hline
  m\equiv0\pmod8 & 2,6,10,14,18,22,30,42\\
  m\equiv2\pmod8 & 2,10,14,22,30,42,78,90\\
  m\equiv4\pmod8 & 2,6,10,14,18,22,30,42\\
  m\equiv6\pmod8 & 2,6,10,14,18,22,54,66\\
  m\equiv1\pmod4 & 4,6,8,16,20,30,54,78\\
  m\equiv3\pmod4 & 4,8,16,18,28,42,66,90
\end{array}
\]

This is useful but not enough.

The reason is simple: lower bounds such as
\[
  r\gtrsim \sqrt{90A}
\]
are not contradictory.  They force a label far below \(A\), but such labels
can exist.

The route only becomes a proof if the six skeletons are shown incompatible
with the shared-center Pell equations:
\[
  e_jw_i^2-e_iw_j^2
  =
  e_ie_j(e_i-e_j)-4(e_jc_i-e_ic_j).
\]

Thus the exact remaining target is not another congruence for \(e\).  It is:

> eliminate the six quotient skeletons as Pell-synchronized systems.

## 4. Plausible modern routes

### Route A: Pell-synchronized finite-certificate elimination

This is the continuation of the current work, but it must change character.
No more isolated barriers.  One should attack one skeleton, for example
\[
  m\equiv3\pmod4,\qquad
  (4,8,16,18,28,42,66,90),
\]
and try to prove that no assignment of quotients, colors, signs, distances,
and square variables satisfies all pairwise Pell equations.

The right tools are:

- Sage/Singular/Magma elimination over residue rings;
- resultants and discriminants for the pairwise Pell pencil;
- modular obstruction certificates;
- saturation away from repeated labels, zero denominators, bridge classes,
  and same-layer collisions.

This route is exact and local.  It might close the clean strong gate, but it
will not automatically close every gate unless the bridge and repetition
classes are handled too.

### Route B: Almost-prime-to-prime upgrade

The modern almost-prime theorem says the interval always contains a
\(P_3\), an integer with at most three prime factors.

A genuinely new idea would be to prove that, in the Legendre interval, any
unavoidable \(P_3\) survivor can be locally deformed to a prime unless it
creates one of the finite certificates already isolated.

This would combine:

- Richert-weighted sieve existence of a \(P_3\);
- local algebra of the six quotient skeletons;
- a descent showing that composite \(P_3\) survivors cannot be terminal.

This is speculative, but it is more promising than trying to beat the sieve
parity problem head-on.

### Route C: Maier-matrix inversion

Maier's matrix method shows that short intervals can behave irregularly.
For Legendre, one could try to reverse the method:

Assume a row interval
\[
  (n^2,(n+1)^2)
\]
has no primes.  Place it inside a matrix whose columns are arithmetic
progressions modulo a primorial.  The empty row would force a deficit of
primes across many columns.  If the column estimates are strong enough in
the square-root-length geometry, contradiction follows.

Known matrix methods do not reach this strength, but this is a coherent
modern analytic target.

### Route D: Conditional theorem as a calibration target

Before attempting the unconditional theorem, prove a conditional version
under a strong but standard hypothesis:

- Cramér-type prime gaps;
- Hardy-Littlewood prime \(k\)-tuples with uniformity;
- Elliott-Halberstam plus a local transference principle.

This would not solve Legendre unconditionally, but it would test whether our
certificate language is aligned with the expected distribution of primes.

## 5. Recommended pivot

The current quotient route should be kept, but only as a certificate
language.

The next serious step should be:

1. pick the hardest-looking skeleton
   \[
     m\equiv3\pmod4,\quad
     M=(4,8,16,18,28,42,66,90);
   \]
2. build the exact Pell-synchronized algebraic system;
3. eliminate modulo small primes first, not by testing \(m\), but by proving
   no residue assignment can satisfy the system after saturation;
4. if one residue model survives, extract it as an explicit obstruction and
   stop claiming the route is closing.

This is the best proof-oriented use of the current work.

The broader analytic literature suggests that a direct prime-gap proof is
out of reach with current exponents, and a pure sieve proof is blocked by
the parity problem.  So the two realistic paths are:

- exact finite-certificate elimination;
- or an almost-prime-to-prime upgrade using the certificate language as the
  obstruction mechanism.
