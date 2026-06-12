# Complete Proof Equation Gate

This note records the equation-level gate that would close the current
Legendre route.

It is not a simulation and not an asymptotic prime-gap estimate.  It is the
exact contradiction that remains to be proved.

## Counterexample Certificate

Assume Legendre fails for some \(n\ge2\).  Then every integer
\[
  n^2+1,\ n^2+2,\ \ldots,\ n^2+2n
\]
is composite.  Hence every such integer has a prime divisor at most \(n\).

The four-offset route restricts to candidates
\[
  n^2+t^2+r,\qquad r\in\{-1,0,1,2\},
\]
with
\[
  1\le t^2+r\le2n.
\]

The existing reductions split the only stubborn channel into \(n=3m\) and
complete A-blocks
\[
  \{3q+1,3q+2\}.
\]
For a complete coprime A-block, define the oriented coordinates
\[
  t_1(q),t_0(q)\in\{3q+1,3q+2\},
\]
where \(t_1\) is the A1 coordinate and \(t_0\) is the A0 coordinate.  The two
surviving candidates are
\[
  U_q=9m^2+t_1(q)^2+1,
  \qquad
  G_q=9m^2+t_0(q)^2.
\]

The block is coprime exactly when
\[
  \gcd(t_1(q),9m^2+1)=1.
\]
In that case
\[
  \gcd(U_q,G_q)=1.
\]

Therefore a counterexample must assign to every complete coprime A-block two
distinct certificate primes
\[
  p_0(q),p_1(q)\le3m,
\]
with
\[
  p_0(q)\equiv1\pmod4,\qquad p_0(q)\nmid3m,
\]
\[
  p_1(q)\ge5,\qquad p_1(q)\ne p_0(q),
\]
such that
\[
  p_0(q)\mid G_q,
  \qquad
  p_1(q)\mid U_q.
\]

Equivalently,
\[
  t_0(q)^2\equiv-9m^2\pmod{p_0(q)}
\]
and
\[
  t_1(q)^2\equiv-9m^2-1\pmod{p_1(q)}.
\]

This is the complete equation gate for the remaining cover problem:
\[
  \boxed{
  \forall q\in\mathcal Q_{\rm cop}(m),\quad
  \exists(p_0,p_1)\ \text{satisfying the two conic congruences above}.
  }
\]

## Closure Lemma Needed

The full Legendre proof follows from the following finite-cover
nonexistence theorem.

**A-block non-cover lemma.**  For every \(m\ge1\), there exists a complete
coprime A-block \(q\in\mathcal Q_{\rm cop}(m)\) such that no ordered pair of
primes \((p_0,p_1)\) with
\[
  p_0\le3m,\quad p_0\equiv1\pmod4,\quad p_0\nmid3m,
\]
\[
  p_1\le3m,\quad p_1\ge5,\quad p_1\ne p_0
\]
satisfies
\[
  t_0(q)^2\equiv-9m^2\pmod{p_0},
  \qquad
  t_1(q)^2\equiv-9m^2-1\pmod{p_1}.
\]

This lemma is exactly the point where a complete proof must now strike.

## Equivalent Product Equation

The same gate can be written without congruence language.  A counterexample
requires, for every \(q\in\mathcal Q_{\rm cop}(m)\), factorizations
\[
  9m^2+t_0(q)^2=\alpha_q\beta_q,
  \qquad
  9m^2+t_1(q)^2+1=\gamma_q\delta_q,
\]
with
\[
  1<\alpha_q,\gamma_q\le3m,
\]
and with prime divisors
\[
  p_0\mid\alpha_q,\qquad p_1\mid\gamma_q
\]
obeying the restrictions above.

Thus the desired contradiction may also be sought from the simultaneous
system
\[
\begin{aligned}
  9m^2+t_0(q)^2&=\alpha_q\beta_q,\\
  9m^2+t_1(q)^2+1&=\gamma_q\delta_q,\\
  \gcd(9m^2+t_0(q)^2,\ 9m^2+t_1(q)^2+1)&=1,\\
  \gcd(t_1(q),9m^2+1)&=1,
\end{aligned}
\]
for every complete coprime block \(q\).

The residual elliptic endpoint is already closed.  The equations above are
the remaining complete-proof gate.

## Two-Block Collision Subgate

The first exact multi-block consequence is recorded in
\[
  \texttt{legendre\_pair\_collision\_equations.md}.
\]

If the same ordered pair \((p_0,p_1)\) covers two distinct complete coprime
blocks \(q\ne r\), then
\[
  p_0\mid
  \bigl(3(q-r)+\alpha_q-\alpha_r\bigr)
  \bigl(3(q+r)+\alpha_q+\alpha_r\bigr),
\]
and
\[
  p_1\mid
  \bigl(3(q-r)+\beta_q-\beta_r\bigr)
  \bigl(3(q+r)+\beta_q+\beta_r\bigr),
\]
where
\[
  t_0(s)=3s+\alpha_s,\qquad t_1(s)=3s+\beta_s.
\]

Thus repeated pair labels are not arbitrary.  They can only occur on explicit
divisor hyperplanes:

- for \(q\equiv r\pmod2\), the primes divide \(q-r\) or layer-specific
  mirror sums \(3(q+r)+2\), \(3(q+r)+4\);
- for \(q\not\equiv r\pmod2\), the primes divide
  \(3(q-r)+1\), \(3(q-r)-1\), or the common mirror sum \(q+r+1\).

Therefore a complete proof may now be phrased as a capacity theorem:
\[
  \text{one-shot ordered pairs plus these collision hyperplanes cannot cover}
  \quad
  \mathcal Q_{\rm cop}(m).
\]

## Fixed Anchor Block

The set \(\mathcal Q_{\rm cop}(m)\) is never empty.  The note
\[
  \texttt{legendre\_Ablock\_anchor\_q0.md}
\]
proves that
\[
  q=0\in\mathcal Q_{\rm cop}(m)
  \qquad\text{for every }m\ge1.
\]

Thus a counterexample must first cover the fixed block \(\{1,2\}\).  This
gives an explicit boundary system:

- if \(m\) is odd, the two values are
  \[
    G_0=9m^2+4,\qquad U_0=9m^2+2;
  \]
- if \(m\) is even, the two values are
  \[
    G_0=9m^2+1,\qquad U_0=9m^2+5.
  \]

In particular, failure of the A-channel already forces eligible small prime
certificates for one of these two pairs.  The collision equations with
\(q=0\) and a second block \(r\) specialize to divisibility by the explicit
linear forms
\[
  r,\quad 3r\pm1,\quad 3r+2,\quad 3r+4,\quad r+1.
\]

The note
\[
  \texttt{legendre\_Ablock\_anchor\_pair\_nonrepetition.md}
\]
uses these specialized equations to prove that the ordered pair covering
\(q=0\) cannot also cover any of
\[
  q=1,\quad q=2,\quad q=3.
\]
Indeed, the collision divisibility tables for \(r=1,2,3\) only offer the
prime \(5\) as a possible divisor \(\ge5\), and never in both layers of the
same row.  Therefore the anchor pair is forced to be one-shot among the
first four blocks.

This is strengthened in
\[
  \texttt{legendre\_first\_four\_ordered\_pair\_distinct.md}.
\]
There are two coordinate sequences
\[
  E=(2,4,8,10),\qquad O=(1,5,7,11).
\]
Inside \(E\), same-layer repetition can occur only on
\[
  (B_0,B_2)\text{ by }5,\qquad (B_1,B_3)\text{ by }7.
\]
Inside \(O\), same-layer repetition can occur only on
\[
  (B_0,B_3)\text{ by }5.
\]
Since A0 and A1 use opposite sequences according to the parity of \(m\), no
block pair admits repetition in both layers.  Thus no ordered pair
\((p_0,p_1)\) can cover two distinct coprime blocks among \(B_0,\dots,B_3\).
