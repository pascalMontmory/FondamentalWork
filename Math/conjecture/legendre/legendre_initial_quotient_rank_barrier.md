# Initial Quotient-Rank Barrier

This note combines two previous facts:

1. for \(m\ge4881\), the eight quotient parameters \(e_c\) are distinct in
   the clean strong gate;
2. every quotient satisfies
   \[
     r_c^2+e_cr_c+c=e_cA.
   \]

Distinct positive quotients force rank lower bounds
\[
  e_{(k)}\ge k.
\]
Each rank then gives a stronger square-root barrier for the corresponding
center-distance.

## 1. Rank lower bounds for quotients

In the clean strong gate with
\[
  m\ge4881,
\]
the initial pair-quotient compatibility lemma gives
\[
  e_c\ne e_d
  \qquad(c\ne d).
\]

Since all quotients are positive integers, if they are ordered as
\[
  e_{(1)}<e_{(2)}<\cdots<e_{(8)},
\]
then necessarily
\[
\boxed{
  e_{(k)}\ge k
  \qquad(1\le k\le8).
}
\]

This is elementary, but it has a useful consequence after substitution into
the center equation.

## 2. Barrier for a fixed quotient

For an offset \(c\), the quotient equation is
\[
  r^2+er+c=eA.
\]

Equivalently,
\[
  r^2+er=eA-c.
\]

Thus, whenever \(eA>c\),
\[
\boxed{
  r=
  \frac{-e+\sqrt{e^2+4(eA-c)}}{2}.
}
\]

Since \(r\) is an integer, this gives
\[
\boxed{
  r\ge
  \left\lceil
  \frac{-e+\sqrt{e^2+4(eA-c)}}{2}
  \right\rceil.
}
\]

For the initial cluster, every offset satisfies
\[
  c\le122.
\]
Therefore
\[
  eA-c\ge eA-122,
\]
and so every quotient \(e\) gives the uniform lower bound
\[
\boxed{
  r\ge
  B_e(A):=
  \left\lceil
  \frac{-e+\sqrt{e^2+4(eA-122)}}{2}
  \right\rceil.
}
\]

This is sharper than the previous \(e\)-free square-root barrier when
\[
  e>1.
\]

## 3. Monotonicity of the quotient barrier

The real root
\[
  \rho_e(A,c)=
  \frac{-e+\sqrt{e^2+4(eA-c)}}{2}
\]
is increasing in \(e\) as long as
\[
  \rho_e(A,c)<A.
\]

Indeed, differentiating the identity
\[
  \rho^2+e\rho+c=eA
\]
with respect to \(e\) gives
\[
  (2\rho+e)\frac{\partial\rho}{\partial e}+\rho=A,
\]
so
\[
  \frac{\partial\rho}{\partial e}
  =
  \frac{A-\rho}{2\rho+e}>0.
\]

Thus the bound \(B_e(A)\) increases with the quotient rank.

## 4. Eight ranked distance barriers

Let the eight quotients be ordered as
\[
  e_{(1)}<e_{(2)}<\cdots<e_{(8)}.
\]

Let \(r_{(k)}\) be the center-distance attached to \(e_{(k)}\).  Since
\[
  e_{(k)}\ge k,
\]
and the barrier is increasing in \(e\), one obtains:
\[
\boxed{
  r_{(k)}\ge B_k(A)
  \qquad(1\le k\le8).
}
\]

Explicitly,
\[
\boxed{
  r_{(k)}\ge
  \left\lceil
  \frac{-k+\sqrt{k^2+4(kA-122)}}{2}
  \right\rceil.
}
\]

Therefore the corresponding prime labels satisfy
\[
\boxed{
  p_{(k)}=A-r_{(k)}\le A-B_k(A).
}
\]

In particular, the largest quotient forces
\[
\boxed{
  r_{(8)}\ge
  \left\lceil
  \frac{-8+\sqrt{64+32A-488}}{2}
  \right\rceil
  =
  \left\lceil
  \frac{-8+\sqrt{32A-424}}{2}
  \right\rceil.
}
\]

So at least one initial label prime satisfies
\[
\boxed{
  p\le
  A-
  \left\lceil
  \frac{-8+\sqrt{32A-424}}{2}
  \right\rceil.
}
\]

This is the first ranked exclusion: the top prime interval is larger for at
least one of the eight labels.

## 5. Clean strong-gate consequence

For
\[
  m\ge4881,
\]
a clean strong-gate counterexample must assign eight distinct quotients and
therefore eight ranked distances obeying
\[
  r_{(1)}\ge B_1(A),\quad
  r_{(2)}\ge B_2(A),\quad
  \dots,\quad
  r_{(8)}\ge B_8(A).
\]

This does not close the gate.  It gives a stronger distributional
constraint: the eight prime labels cannot merely avoid the top
\(\sqrt A\)-window; their quotient ranks force progressively deeper
exclusion windows below \(A\).

The next exact target is to combine these ranked windows with the order
constraint
\[
  \operatorname{Inv}_e\subseteq\operatorname{Inv}_r
\]
and the A0 congruence condition
\[
  p\equiv1\pmod4.
\]
