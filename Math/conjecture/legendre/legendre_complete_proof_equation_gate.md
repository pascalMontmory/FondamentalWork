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
