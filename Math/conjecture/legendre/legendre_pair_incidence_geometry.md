# Pair Incidence Geometry for Coprime A-Blocks

This note rewrites the coprime A-block pair cover as an incidence problem in
\((m,q)\) modulo the certificate primes.

It refines `legendre_coprime_A_pair_cover.md` by separating the two parity
orientations and by recording the nonzero restrictions forced by coprimality.

Throughout,
\[
  n=3m,\qquad a=3q+1,\qquad b=3q+2.
\]

## 1. Two orientations

The parity of \(a\) decides which member of the block is A1.

### Orientation I

If
\[
  a\equiv m\pmod2,
\]
then
\[
  t_1=a,\qquad t_0=b.
\]
The pair-certificate equations are
\[
  b^2+9m^2\equiv0\pmod{p_0},
\]
and
\[
  a^2+9m^2+1\equiv0\pmod{p_1}.
\]
In terms of \(q\):
\[
  (3q+2)^2+9m^2\equiv0\pmod{p_0},
\]
\[
  (3q+1)^2+9m^2+1\equiv0\pmod{p_1}.
\]

### Orientation II

If
\[
  a\not\equiv m\pmod2,
\]
then
\[
  t_1=b,\qquad t_0=a.
\]
The pair-certificate equations are
\[
  a^2+9m^2\equiv0\pmod{p_0},
\]
and
\[
  b^2+9m^2+1\equiv0\pmod{p_1}.
\]
In terms of \(q\):
\[
  (3q+1)^2+9m^2\equiv0\pmod{p_0},
\]
\[
  (3q+2)^2+9m^2+1\equiv0\pmod{p_1}.
\]

Thus every coprime failing block gives an incidence point on one of two
products of conics over
\[
  \mathbb F_{p_0}\times\mathbb F_{p_1}.
\]

## 2. Nonzero restrictions

On a coprime block,
\[
  \gcd(t_1(q),9m^2+1)=1.
\]
If
\[
  p_1\mid 9m^2+1,
\]
then the A1 equation
\[
  t_1(q)^2+9m^2+1\equiv0\pmod{p_1}
\]
forces
\[
  t_1(q)\equiv0\pmod{p_1},
\]
contradicting the coprime condition.

Therefore every A1 certificate on a coprime block satisfies
\[
  \boxed{p_1\nmid 9m^2+1.}
\]
Consequently the A1 congruence has no zero root, and it exists only when
\[
  \left(\frac{-9m^2-1}{p_1}\right)=1.
\]

Similarly, the A0 certificate satisfies
\[
  p_0\nmid3m,\qquad p_0\equiv1\pmod4,
\]
and the A0 coordinate is nonzero modulo \(p_0\).

Thus a coprime pair certificate has the exact restrictions
\[
\begin{array}{ll}
  p_0\le3m, & p_0\equiv1\pmod4,\quad p_0\nmid3m,\\
  p_1\le3m, & p_1\ge5,\quad p_1\ne p_0,\quad p_1\nmid9m^2+1,\\
             & \left(\frac{-9m^2-1}{p_1}\right)=1.
\end{array}
\]

This removes the degenerate A1 case from the coprime pair-cover problem.

## 3. Linearized root form

For A0, choose a square root
\[
  i_0^2\equiv-1\pmod{p_0}.
\]
Then
\[
  t_0\equiv \pm 3m i_0\pmod{p_0}.
\]
Since \(t_0\) is either \(3q+1\) or \(3q+2\), this gives two explicit linear
classes of \(q\) modulo \(p_0\).

For A1, choose a square root
\[
  s_1^2\equiv-9m^2-1\pmod{p_1}.
\]
The nonzero restriction above gives
\[
  s_1\not\equiv0\pmod{p_1}.
\]
Then
\[
  t_1\equiv\pm s_1\pmod{p_1},
\]
which gives two explicit linear classes of \(q\) modulo \(p_1\).

Hence each ordered pair \((p_0,p_1)\) gives at most four classes modulo
\[
  p_0p_1,
\]
but now all four classes are produced by nonzero roots.

## 4. Projection to \(m\)-classes

The A0 condition only requires
\[
  p_0\equiv1\pmod4
\]
and
\[
  p_0\nmid m.
\]
For every nonzero \(m\bmod p_0\), A0 has exactly two roots.

The A1 condition is restrictive in \(m\).  It requires
\[
  -9m^2-1
\]
to be a nonzero square modulo \(p_1\).
Equivalently,
\[
  9m^2+1
\]
must be a nonzero negative square modulo \(p_1\).

Thus, for fixed \(p_1\), only the residue classes
\[
  m\bmod p_1
\]
lying in
\[
  \mathcal M_{p_1}
  =
  \left\{
  m:
  \left(\frac{-9m^2-1}{p_1}\right)=1
  \right\}
\]
can participate in a coprime A1 certificate.

This is the first place where the pair-cover becomes an incidence problem in
both variables \(m\) and \(q\), rather than a cover of \(q\) for a fixed \(m\).

## 5. Exact obstruction

A counterexample surviving all coprime complete A-blocks must satisfy:

For every
\[
  q\in\mathcal Q_{\mathrm{cop}}(m),
\]
there exists an ordered prime pair \((p_0,p_1)\) such that one of the two
orientation systems holds:

\[
\begin{cases}
(3q+2)^2+9m^2\equiv0\pmod{p_0},\\
(3q+1)^2+9m^2+1\equiv0\pmod{p_1},
\end{cases}
\]
or
\[
\begin{cases}
(3q+1)^2+9m^2\equiv0\pmod{p_0},\\
(3q+2)^2+9m^2+1\equiv0\pmod{p_1},
\end{cases}
\]
with
\[
\begin{array}{ll}
  p_0\le3m, & p_0\equiv1\pmod4,\quad p_0\nmid3m,\\
  p_1\le3m, & p_1\ne p_0,\quad p_1\nmid9m^2+1,\\
             & \left(\frac{-9m^2-1}{p_1}\right)=1.
\end{array}
\]

This is the sharpened incidence obstruction.

## 6. Next exact target

The next proof target is to eliminate dense incidence covers:

Show that for each fixed \(m\), the admissible \(q\)-interval cannot be
covered by the above conic-product incidences once bridge blocks have been
removed.

Equivalently, prove that the projections of these incidences to the
\(q\)-line leave at least one coprime complete A-block uncovered.
