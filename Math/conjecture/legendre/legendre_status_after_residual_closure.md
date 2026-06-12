# Status After Residual Coset Closure

This note separates what is now closed from what is still required for a full
proof of Legendre's conjecture in this workbench.

## Closed

The hard \(m\equiv3\pmod4\) structural prefix-\(8\) endpoint has no remaining
residual elliptic fiber.

The last two terminal fibers \(R4\) and \(R5\) were reduced to
\[
  P\in\pm P_0+1320E(\mathbf Q),
  \qquad
  E:\ y^2=x^3-128x^2-215865x,
\]
with
\[
  P_0=\left(\frac{10045}{9},-\frac{849520}{27}\right).
\]

At \(3\), the curve has split multiplicative type \(I_8\), so
\[
  1320E(\mathbf Q)\subset E_1(\mathbf Q_3).
\]
Since \(P_0\in E_1(\mathbf Q_3)\), both residual cosets lie inside
\[
  E_1(\mathbf Q_3).
\]
But every nonzero affine point in this formal subgroup has negative
\(3\)-adic \(x\)-valuation, while the quartic image requires
\[
  x=1845s^2,\qquad s\in\mathbf Z,
\]
which has \(v_3(x)\ge2\) for \(s\ne0\).  The case \(s=0\) gives the finite
point \((0,0)\), not a point of the formal subgroup.  Hence
\[
  \left(\pm P_0+1320E(\mathbf Q)\right)
  \cap
  \{x=1845s^2:s\in\mathbf Z\}
  =
  \varnothing.
\]

So the residual elliptic endpoint is closed.

## Not Yet A Full Legendre Proof

This does not by itself prove Legendre's conjecture.  The global route still
requires a proof that a counterexample must enter one of the closed structural
prefix endpoints, or else a direct closure of the earlier cover problem.

The current exact non-closed target is the primitive/multiple-of-three
covering obstruction.  In the \(n=3m\) channel, complete coprime A-blocks
lead to the pair-cover condition
\[
  \mathcal Q_{\rm cop}(m)
  \subseteq
  \bigcup_{(p_0,p_1)} C_{p_0,p_1}(m),
\]
where
\[
  p_0\le3m,\quad p_0\equiv1\pmod4,\quad p_0\nmid3m,
\]
\[
  p_1\le3m,\quad p_1\ge5,\quad p_1\ne p_0,
\]
and the two certificate congruences are
\[
  t_0(q)^2\equiv-9m^2\pmod{p_0},
  \qquad
  t_1(q)^2\equiv-9m^2-1\pmod{p_1}.
\]

For each ordered pair \((p_0,p_1)\), this contributes at most four residue
classes of \(q\bmod p_0p_1\).  A full proof must still show that these
oriented conic-product classes cannot cover all coprime complete A-blocks,
or must replace that cover target by a stronger global descent.

Thus the honest status is:
\[
  \text{residual elliptic endpoint closed, full Legendre closure not yet proven.}
\]
