# Multiplicative Rank Model for the Hard Branch

This note replaces the old additive rank automaton by an intrinsic
multiplicative quotient model.

The branch is
\[
  A=3m,
  \qquad
  m\equiv3\pmod4.
\]

The eight offsets are
\[
  \{2,4,16,26,50,64,100,122\}.
\]

For every offset \(c\), a quotient \(f\) in a hard-branch counterexample must
satisfy
\[
  u^2=f^2+6mf-c,
\]
and hence the intrinsic self-residue condition
\[
\boxed{
  u^2\equiv-c\pmod f.
}
\]

The previous rank automaton used residue lattices for \(f\).  The A0 and A1
quotient theorems show that those lattices are too large.  The correct
object is a product of offset-dependent multiplicative semigroups.

## 1. Common A0 semigroup

Define
\[
  \mathcal S_4
  =
  \{s\ge1:\ s\text{ odd},\ 3\nmid s,\ q\mid s\Rightarrow q\equiv1\pmod4\}.
\]

Equivalently, \(\mathcal S_4\) is the odd, \(3\)-free part of the
sum-of-two-squares semigroup.

The A0 four-layer offsets satisfy
\[
\boxed{
  c=4,100
  \quad\Longrightarrow\quad
  f\in 2\mathcal S_4\cup4\mathcal S_4.
}
\]

Residue-wise this is
\[
  f\equiv2,10\pmod{24}
  \quad\text{or}\quad
  f\equiv4,20\pmod{48}.
\]

The A0 zero-layer offsets satisfy
\[
\boxed{
  c=16
  \quad\Longrightarrow\quad
  f\in
  \bigcup_{\nu=3}^{5}2^\nu\mathcal S_4,
}
\]
and
\[
\boxed{
  c=64
  \quad\Longrightarrow\quad
  f\in
  \bigcup_{\nu=3}^{7}2^\nu\mathcal S_4.
}
\]

In particular, for both \(c=16\) and \(c=64\),
\[
  f\equiv8,16\pmod{24},
\]
and the old classes \(14,22\pmod{24}\) are impossible.

## 2. A1 splitting semigroups

For an odd prime \(q\), write
\[
  \chi_c(q)=\left(\frac{-c}{q}\right)
\]
when \(q\nmid c\).

The A1 layer also imposes
\[
\boxed{
  f\equiv9\pmod{12}.
}
\]

Define the offset-specific A1 semigroups:

\[
\mathcal T_2
=
\{f\ge1:\ f\equiv9\pmod{12},\
q\mid f\Rightarrow \left(\frac{-2}{q}\right)=1\}.
\]

\[
\mathcal T_{26}
=
\{f\ge1:\ f\equiv9\pmod{12},\
v_{13}(f)\le1,\
q\mid f,\ q\ne13\Rightarrow \left(\frac{-26}{q}\right)=1\}.
\]

\[
\mathcal T_{50}
=
\{f\ge1:\ f\equiv9\pmod{12},\
v_5(f)\le2,\
q\mid f,\ q\ne5\Rightarrow \left(\frac{-50}{q}\right)=1\}.
\]

\[
\mathcal T_{122}
=
\{f\ge1:\ f\equiv9\pmod{12},\
v_{61}(f)\le1,\
q\mid f,\ q\ne61\Rightarrow \left(\frac{-122}{q}\right)=1\}.
\]

Then
\[
\boxed{
  c=2,26,50,122
  \quad\Longrightarrow\quad
  f\in\mathcal T_c.
}
\]

The forced factor \(3\mid f\) is compatible with all four A1 semigroups
because
\[
  c\equiv2\pmod3,
  \qquad
  -c\equiv1\pmod3.
\]

## 3. Multiplicative counterexample certificate

A hard-branch clean-gate counterexample must therefore give eight pairs
\[
  (f_c,u_c)
  \qquad
  c\in\{2,4,16,26,50,64,100,122\}
\]
and an integer \(m\equiv3\pmod4\) such that:

1. every line equation holds:
   \[
     u_c^2=f_c^2+6mf_c-c;
   \]
2. every quotient lies in its intrinsic semigroup:
   \[
   \begin{array}{c|c}
     c & f_c\text{ belongs to}\\
     \hline
     4,100 & 2\mathcal S_4\cup4\mathcal S_4\\
     16 & \bigcup_{\nu=3}^{5}2^\nu\mathcal S_4\\
     64 & \bigcup_{\nu=3}^{7}2^\nu\mathcal S_4\\
     2 & \mathcal T_2\\
     26 & \mathcal T_{26}\\
     50 & \mathcal T_{50}\\
     122 & \mathcal T_{122};
   \end{array}
   \]
3. the eight \(f_c\) are pairwise distinct;
4. the recovered prime labels
   \[
     p_c=3m-u_c+f_c
   \]
   are positive, distinct, and admissible labels for the clean gate.

Eliminating \(m\) between two offsets gives the synchronized equation
\[
\boxed{
  f_d u_c^2-f_c u_d^2
  =
  f_cf_d(f_c-f_d)-f_dc+f_cd.
}
\]

Thus the multiplicative rank model is the system of these pairwise
Pell-type equations with
\[
  f_c\in\mathcal M_c,
\]
where \(\mathcal M_c\) is the corresponding semigroup above.

## 4. Exact descent target

The previous finite certificates prove that all arbitrary assignments from
the first ten old layer values are closed.  The multiplicative model gives a
strictly smaller universe for all higher ranks.

The next exact theorem needed for closure is:
\[
\boxed{
  \text{Every integral point of the multiplicative Pell system}
  \text{ descends to the closed prefix range.}
}
\]

Equivalently, one must prove that a point with a quotient outside the closed
prefix range forces, through the pairwise synchronization equations, either:

- a forbidden prime divisor in one of the semigroups;
- a collision \(f_c=f_d\);
- an inadmissible label \(p_c\);
- or a smaller synchronized point.

This is now a descent problem in multiplicative semigroups, not a finite
local-modular sieve.
