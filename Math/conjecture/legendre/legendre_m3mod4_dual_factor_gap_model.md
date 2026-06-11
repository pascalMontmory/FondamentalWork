# Dual-Factor Gap Model

This note strengthens the multiplicative rank model by using both factors
of each Pell line.

The hard branch is
\[
  A=3m,
  \qquad
  m\equiv3\pmod4.
\]

For each offset
\[
  c\in\{2,4,16,26,50,64,100,122\},
\]
the reduced line is
\[
  u_c^2=f_c^2+6mf_c-c.
\]

Rearrange it as
\[
\boxed{
  u_c^2+c=f_c(f_c+6m).
}
\]

Thus the quotient \(f_c\) is only the lower factor of a factor pair.  The
upper factor
\[
\boxed{
  F_c=f_c+6m
}
\]
is just as constrained.

## 1. Common-gap factorization

Set
\[
  L=6m.
\]

Since
\[
  m\equiv3\pmod4,
\]
one has
\[
\boxed{
  L\equiv18\pmod{24}.
}
\]

Each row becomes
\[
\boxed{
  u_c^2+c=f_cF_c,
  \qquad
  F_c-f_c=L.
}
\]

Therefore a hard-branch counterexample is a system of eight factor pairs
with the same gap \(L\).

This is equivalent to the original reduced Pell system, but it exposes a
new necessary condition: both factors divide the same number
\[
  u_c^2+c.
\]

## 2. The upper factor obeys the same splitting law

Because
\[
  F_c\mid u_c^2+c,
\]
one has
\[
\boxed{
  u_c^2\equiv-c\pmod{F_c}.
}
\]

Thus every prime-power restriction previously proved for \(f_c\) also
applies to \(F_c\).

This is stronger than the one-sided multiplicative model:
\[
\boxed{
  f_c\in\mathcal M_c
  \quad\text{and}\quad
  F_c=f_c+L\in\mathcal M_c^{\rm split},
}
\]
where \(\mathcal M_c^{\rm split}\) denotes the same quadratic splitting
semigroup, without necessarily imposing the original lower-factor residue
class if that class came from quotient placement rather than divisibility.

## 3. A0 dual restrictions

For A0 offsets
\[
  c=x^2,
  \qquad
  x\in\{2,4,8,10\},
\]
both factors satisfy
\[
\boxed{
  u_c^2+x^2\equiv0\pmod{f_c}
  \quad\text{and}\quad
  u_c^2+x^2\equiv0\pmod{F_c}.
}
\]

Hence for every odd prime divisor \(q\) of either factor,
\[
\boxed{
  q\equiv1\pmod4.
}
\]

The \(2\)-adic ceilings also apply to both factors:
\[
\begin{array}{c|c|c}
  c & x & \text{ceiling for }v_2(f_c)\text{ and }v_2(F_c)\\
  \hline
  4 & 2 & \le3\\
  16 & 4 & \le5\\
  64 & 8 & \le7\\
  100 & 10 & \le3.
\end{array}
\]

Thus the gap equation
\[
  F_c-f_c=L
\]
must connect two integers whose odd prime factors are all \(1\bmod4\), with
the same offset-specific \(2\)-adic ceiling.

## 4. A1 dual restrictions

For A1 offsets
\[
  c\in\{2,26,50,122\},
\]
both factors satisfy
\[
  u_c^2\equiv-c\pmod{f_c},
  \qquad
  u_c^2\equiv-c\pmod{F_c}.
\]

Therefore both factors obey the same quadratic-field splitting law:
\[
\begin{array}{c|c}
  c & \text{condition on odd prime powers of }f_c\text{ and }F_c\\
  \hline
  2
    & \left(\frac{-2}{q}\right)=1\text{ for all }q\\
  26
    & v_{13}\le1,\quad
      \left(\frac{-26}{q}\right)=1\text{ away from }13\\
  50
    & v_5\le2,\quad
      \left(\frac{-50}{q}\right)=1\text{ away from }5\\
  122
    & v_{61}\le1,\quad
      \left(\frac{-122}{q}\right)=1\text{ away from }61.
\end{array}
\]

The lower A1 quotient has
\[
  f_c\equiv9\pmod{12}.
\]

Since
\[
  L\equiv18\pmod{24},
\]
the upper factor satisfies
\[
\boxed{
  F_c=f_c+L\equiv3\pmod{12}.
}
\]

Thus A1 gives a forced same-field pair
\[
  f_c\equiv9\pmod{12},
  \qquad
  F_c\equiv3\pmod{12},
  \qquad
  F_c-f_c=L.
\]

## 5. Reformulated certificate

A hard-branch clean-gate counterexample must now give:

1. a common gap
   \[
     L\equiv18\pmod{24};
   \]
2. eight lower factors \(f_c\);
3. eight upper factors
   \[
     F_c=f_c+L;
   \]
4. eight integers \(u_c\) such that
   \[
     u_c^2+c=f_cF_c;
   \]
5. both \(f_c\) and \(F_c\) satisfy the offset-specific splitting laws;
6. the recovered labels
   \[
     p_c=3m-u_c+f_c
     =
     \frac{L}{2}-u_c+f_c
   \]
   are admissible prime labels.

The pairwise Pell synchronization is now the statement that all eight
factor pairs have the same gap \(L\).

## 6. Descent target

The previous one-sided target was:
\[
  f_c\in\mathcal M_c
  \quad\text{for all }c.
\]

The strengthened target is:
\[
\boxed{
  f_c,\ f_c+L
  \text{ both satisfy the offset-specific splitting law}
}
\]
for the same gap
\[
  L\equiv18\pmod{24}
\]
across all eight offsets.

This creates a two-sided multiplicative obstruction.  A rank-descent proof
can now try to show that if one lower factor is outside the closed prefix
range, then the common gap \(L\) forces a forbidden prime divisor in either
the lower factor or its upper partner.
