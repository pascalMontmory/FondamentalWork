# \(m\equiv3\pmod4\) Pell System

This note writes the hardest quotient skeleton as an explicit reduced Pell
system.

The purpose is to stop speaking abstractly about "the six skeletons" and
produce the first exact algebraic object that Sage/Singular/Magma should
eliminate.

## 1. Branch and offsets

Work in the odd clean strong gate with
\[
  A=3m,
  \qquad
  m\equiv3\pmod4.
\]

The eight initial offsets are
\[
  \mathcal C_{\rm odd}
  =
  \{2,4,16,26,50,64,100,122\}.
\]

Split them into:
\[
  \mathrm{A0}=\{4,16,64,100\}
  =
  \{2^2,4^2,8^2,10^2\},
\]
and
\[
  \mathrm{A1}=\{2,26,50,122\}
  =
  \{1^2+1,5^2+1,7^2+1,11^2+1\}.
\]

## 2. Reduced variables

All quotients in this branch are even.  Write
\[
  e_i=2f_i,\qquad w_i=2u_i.
\]

The square-line equation
\[
  w_i^2=12me_i+e_i^2-4c_i
\]
becomes
\[
\boxed{
  u_i^2=f_i^2+6mf_i-c_i.
}
\]

The original distance and label are recovered by
\[
\boxed{
  r_i=u_i-f_i,
  \qquad
  p_i=3m-r_i=3m-u_i+f_i.
}
\]

Thus an actual clean-gate certificate additionally requires
\[
  u_i>f_i>0,
  \qquad
  p_i\text{ prime},
  \qquad
  p_i\mid (3m)^2+c_i.
\]

The divisibility is automatic from the quotient equation once
\[
  e_i=2f_i
\]
is integral and
\[
  p_i=\frac{r_i^2+c_i}{e_i}.
\]

## 3. Residue classes for \(f_i\)

The branch \(m\equiv3\pmod4\) splits into
\[
  m\equiv3\pmod8
  \quad\text{or}\quad
  m\equiv7\pmod8.
\]

For both subbranches, the A0 mod-\(16\) table gives:

### A0 offsets with \(x^2\equiv4\pmod{16}\)

These are
\[
  c=4,\ 100.
\]

Their quotient classes are
\[
  e\equiv4,8,20,40\pmod{48},
\]
so
\[
\boxed{
  f\equiv2,4,10,20\pmod{24}.
}
\]

### A0 offsets with \(x^2\equiv0\pmod{16}\)

These are
\[
  c=16,\ 64.
\]

Their quotient classes are
\[
  e\equiv16,28,32,44\pmod{48},
\]
so
\[
\boxed{
  f\equiv8,14,16,22\pmod{24}.
}
\]

### A1 offsets

For
\[
  c=2,\ 26,\ 50,\ 122,
\]
the odd A1 mod-\(24\) lift gives
\[
  e\equiv18\pmod{24},
\]
hence
\[
\boxed{
  f\equiv9\pmod{12}.
}
\]

## 4. Skeleton minima

The sorted global quotient skeleton is
\[
  (4,8,16,18,28,42,66,90).
\]

In \(f=e/2\) variables this is
\[
\boxed{
  (2,4,8,9,14,21,33,45).
}
\]

This sorted list is not a fixed assignment of offsets to quotients.  It is a
rank lower bound.  The exact system is a finite union over:

1. residue choices for the four A0 offsets;
2. a rank assignment of the eight distinct \(f_i\);
3. the two subbranches \(m\equiv3,7\pmod8\).

Any elimination must respect that union.  Fixing one rank assignment gives
one algebraic component of the skeleton.

## 5. Pairwise Pell synchronization

For two offsets \(c_i,c_j\), the reduced equations
\[
  u_i^2=f_i^2+6mf_i-c_i,
  \qquad
  u_j^2=f_j^2+6mf_j-c_j
\]
eliminate \(m\) to give
\[
\boxed{
  f_j u_i^2-f_i u_j^2
  =
  f_if_j(f_i-f_j)-f_jc_i+f_ic_j.
}
\]

There are \(28\) such pairwise equations.  They are redundant if one keeps a
common \(m\), but essential for quotient-first elimination because they
remove the center variable.

## 6. The finite exact target

For \(m\ge4881\), the equal-quotient obstruction already proves
\[
  f_i\ne f_j
  \qquad(i\ne j).
\]

Thus a counterexample in the \(m\equiv3\pmod4\) branch must produce integers
\[
  m,\quad (f_i,u_i)_{i=1}^8
\]
such that:

1. \(m\equiv3\pmod4\);
2. each \(f_i\) lies in its layer-specific residue class above;
3. the \(f_i\) are pairwise distinct;
4. the sorted lower-bound skeleton is
   \[
     f_{(1)},\dots,f_{(8)}
     \ge
     2,4,8,9,16,21,33,45;
   \]
5. each line equation holds:
   \[
     u_i^2=f_i^2+6mf_i-c_i;
   \]
6. equivalently, all \(28\) pairwise Pell equations hold;
7. each recovered label
   \[
     p_i=3m-u_i+f_i
   \]
   is a positive prime satisfying the previously recorded layer, color,
   ladder, and repetition constraints.

This is the first fully explicit algebraic target for closing a skeleton:

> Prove that this finite union of reduced Pell systems has no integral point
> satisfying the label and ladder constraints.

## 7. Why this is now the main closure path

The \(P_3\)-upgrade route cannot close from one almost-prime survivor.  It
would need a collective packet/capacity lemma that is not yet forced.

By contrast, the system above is exactly what a clean strong-gate
counterexample in the hardest odd branch must satisfy.  Eliminating it, even
for one quotient-rank component, is real progress toward closing the gate.

The next concrete step is to encode the next boundary families of this
system in Sage/Singular:

- choose \(m\equiv3\pmod8\) or \(m\equiv7\pmod8\);
- choose one of the boundary raises left after the modulo \(5\)/\(11\)
  certificate:
  \[
    4\leadsto10,
    \qquad
    16\leadsto22,
    \qquad
    45\leadsto57;
  \]
- saturate by
  \[
    f_i f_j(f_i-f_j),\quad u_i-f_i,\quad p_i;
  \]
- eliminate \(m,u_i\) modulo small primes and then over \(\mathbb Z\).

If the minimal component survives, extract the surviving parametric
obstruction.  If it dies, climb to the next rank component.

## 8. First boundary result

The naive minimal boundary component
\[
  f=(2,4,8,9,14,21,33,45)
\]
does not survive.

The reason is recorded in
\[
  \texttt{legendre\_m3mod4\_minimal\_component\_mod7.md}.
\]

The A0 offsets \(c=16,64\) must receive \(f=8,14\).  Pairing either of them
with \(f=14\) forces, modulo \(7\),
\[
  u^2\equiv-c\pmod7.
\]

But
\[
  -16\equiv5\pmod7,
  \qquad
  -64\equiv6\pmod7,
\]
and the square classes modulo \(7\) are
\[
  0,1,2,4.
\]

Thus the exact minimal component is killed modulo \(7\).  The next component
must raise the \(x^2\equiv0\pmod{16}\) A0 quotient beyond the naive
\(f=14\) boundary.

## 9. Modulo 7 zero-quotient filter

The previous component died for a structural reason.  If \(7\mid f\), then
the reduced line
\[
  u^2=f^2+6mf-c
\]
forces
\[
  u^2\equiv-c\pmod7.
\]

Thus \(7\mid f\) is allowed only when \(-c\) is a square modulo \(7\).
Among the eight offsets
\[
  2,4,16,26,50,64,100,122,
\]
this happens only for
\[
  c=26,\ 122.
\]

Therefore the A0 zero-square offsets \(c=16,64\) cannot carry any quotient
with \(7\mid f\).  Their first two admissible values are no longer
\[
  8,14,
\]
but
\[
  8,16.
\]

The active hard-branch lower bound is now
\[
\boxed{
  f_{(1)},\dots,f_{(8)}
  \ge
  2,4,8,9,16,21,33,45
}
\]
or, equivalently,
\[
\boxed{
  e_{(1)},\dots,e_{(8)}
  \ge
  4,8,16,18,32,42,66,90.
}
\]

Moreover, the A1 value \(f=21\) satisfies \(7\mid f\), so it must be attached
to
\[
  c=26
  \quad\text{or}\quad
  c=122.
\]

## 10. Lifted boundary killed modulo 5 and 11

The lifted boundary component
\[
  f=(2,4,8,9,16,21,33,45)
\]
also dies.

The proof is recorded in
\[
  \texttt{legendre\_m3mod4\_lifted\_boundary\_mod5\_mod11.md}.
\]

Modulo \(5\), the A0 and A1 lines force the unique assignment
\[
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 2 & 4 & 16 & 8 & 9 & 45 & 33 & 21
\end{array}
\]
with
\[
  m\equiv0\pmod5.
\]

For this assignment, reducing the eight lines modulo \(11\) gives an empty
intersection of admissible \(m\bmod11\) classes.  In fact, the first five
nontrivial constraints force
\[
  m\equiv9\pmod{11},
\]
but the row
\[
  c=26,\qquad f=45
\]
forbids
\[
  m\equiv9\pmod{11}.
\]

Therefore the first lifted boundary has no integral point.

The active exact target is now the next finite union, obtained by raising at
least one layer boundary:
\[
\boxed{
  4\leadsto10,
  \qquad
  16\leadsto22,
  \qquad
  45\leadsto57.
}
\]

## 11. Next boundary layer killed

The complete first escape layer after the lifted boundary also has no
integral point.  The proof is recorded in
\[
  \texttt{legendre\_m3mod4\_next\_boundary\_layer\_modular\_closure.md}.
\]

The three families are:
\[
\begin{array}{c|c|c|c}
  \text{family} & \mathrm{A0},\ x^2\equiv4 & \mathrm{A0},\ x^2\equiv0 & \mathrm{A1}\\
  \hline
  F_{04} & 2,10 & 8,16 & 9,21,33,45\\
  F_{00} & 2,4 & 8,22 & 9,21,33,45\\
  F_{1}  & 2,4 & 8,16 & 9,21,33,57.
\end{array}
\]

They are eliminated as follows:

- \(F_{00}\) is killed modulo \(5\);
- \(F_{04}\) is reduced modulo \(5\), then killed by modulo \(7\) and
  modulo \(11\);
- \(F_1\) is reduced modulo \(5\), survives modulo \(7\) in one class, and
  dies modulo \(11\) because \(M_{11}(26,33)=\varnothing\).

Thus a hard-branch counterexample must climb beyond the first escape layer:
at least two layer boundaries must rise, or one boundary must jump past its
first successor.

The local closure problem is therefore no longer just a component-killing
problem.  It is a rank problem:

\[
\boxed{
  \text{prove an a priori cap on the quotient ranks in the hard branch.}
}
\]

With such a cap, the remaining modular matching eliminations become a finite
certificate.  Without it, the method can still climb indefinitely without
closing Legendre.
