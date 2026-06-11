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

## 12. Rank weights 2--4 killed

The rank game can be organized by three nonnegative integers
\[
  (a,b,c)
\]
measuring the raises in:

1. A0 \(x^2\equiv4\pmod{16}\);
2. A0 \(x^2\equiv0\pmod{16}\);
3. A1.

The weight is
\[
  w=a+b+c.
\]

Weight \(0\) is the lifted boundary.  Weight \(1\) is the first escape
layer.  Both are dead by the previous notes.

The note
\[
  \texttt{legendre\_m3mod4\_rank\_weight\_2\_4\_closure.md}
\]
closes the next three layers:
\[
\boxed{
  w=2,3,4
  \quad\Longrightarrow\quad
  \text{no integral point.}
}
\]

Therefore any remaining \(m\equiv3\pmod4\) clean-gate counterexample must
have
\[
\boxed{
  a+b+c\ge5.
}
\]

The most promising closure route is now not an analytic estimate on one
quotient.  It is a periodic modular-killing theorem for the rank automaton:
prove that every triple \((a,b,c)\) is killed by a finite set of small
primes, or prove an independent rank cap \(a+b+c\le4\).

## 13. Rank weights 0--30 certified

The finite certificate has been extended substantially.

The note
\[
  \texttt{legendre\_m3mod4\_rank\_weight\_0\_30\_certificate.md}
\]
and verifier
\[
  \texttt{tools/m3mod4\_rank\_certificate.py}
\]
prove that every rank family with
\[
\boxed{
  0\le a+b+c\le30
}
\]
has no integral point in the reduced hard-branch Pell system.

Only the primes
\[
  5,\ 7,\ 11,\ 13,\ 17
\]
are needed, together with the modulo \(7\) zero-quotient filter.

Thus any remaining \(m\equiv3\pmod4\) clean-gate counterexample must satisfy
\[
\boxed{
  a+b+c\ge31.
}
\]

This makes the closure problem sharper:

- a rank cap \(a+b+c\le30\) would close this branch;
- a periodicity theorem for the modular automaton would close it without an
  analytic rank cap;
- a descent theorem from weight \(>30\) to a smaller surviving weight would
  also close it, since no smaller surviving weight exists.

## 14. Five-prime periodicity obstruction

The first natural periodicity theorem is false.

Using only
\[
  5,\ 7,\ 11,\ 13,\ 17,
\]
the full periodic rank automaton has a surviving pattern:
\[
\begin{array}{c|cccccccc}
  \text{offset} & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f\text{-slot} & 2 & a & b & 8 & c & 21 & 33 & 9.
\end{array}
\]

It survives in the center residue class
\[
  m\equiv14325\pmod{85085}.
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_periodic\_automaton\_obstruction.md}.
\]

Therefore the route "weights \(0..30\) die, so the five-prime automaton is
periodically closed" is invalid.

The next target is to kill this explicit survivor pattern by using the
pairwise Pell synchronization equations, or to identify the next modulus
that kills it uniformly.

## 15. Periodic boundary automaton closed

The survivor pattern is killed uniformly by
\[
  83.
\]

The verifier command
\[
  \texttt{python3 Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py --periodic-patterns}
\]
checks all \(48\) periodic boundary assignment patterns and returns:
\[
  \texttt{certificate: all periodic boundary patterns closed}.
\]

The killer distribution is:
\[
\begin{array}{c|cccccc}
  \ell & 5 & 7 & 11 & 13 & 17 & 83\\
  \hline
  \#\text{patterns killed} & 33 & 3 & 4 & 5 & 2 & 1.
\end{array}
\]

Therefore:
\[
\boxed{
  \text{the boundary-rank automaton is closed by }
  \{5,7,11,13,17,83\}.
}
\]

The remaining task is not more modular killing inside this boundary model.
It is the descent problem:
\[
\boxed{
  \text{reduce arbitrary skipped quotient ranks to the boundary model.}
}
\]

If that descent is proved, the hard \(m\equiv3\pmod4\) branch is closed.

## 16. Arbitrary prefix-rank certificate

The skipped-rank gap has been attacked directly.

The verifier mode
\[
  \texttt{--prefix-ranks N}
\]
checks all arbitrary ordered assignments using the first \(N\) admissible
values in each layer, not only the boundary-rank model.

The exact results are:
\[
\begin{array}{c|c|c}
  N & \#\text{ordered assignments} & \text{status}\\
  \hline
  7 & 1\,481\,760 & \text{closed}\\
  8 & 5\,268\,480 & \text{closed}\\
  9 & 15\,676\,416 & \text{closed}\\
  10 & 40\,824\,000 & \text{closed}.
\end{array}
\]

The prime set is
\[
  \{5,7,11,13,17,19,23,29,83\}.
\]

Therefore any remaining hard-branch counterexample must use at least one
rank
\[
\boxed{
  \ge10
}
\]
inside one of the three layers.

This does not yet close the hard branch, but it replaces the vague
"skipped-rank" gap by a concrete lower-rank exclusion theorem.

## 17. Why finite local tests cannot close arbitrary skipped ranks

There is a structural obstruction to continuing the prefix-rank method
indefinitely by adding more local primes.

For any finite set of odd primes \(\mathcal P\), choose
\[
  m\equiv0\pmod{\prod_{\ell\in\mathcal P}\ell}.
\]

Then the local line
\[
  u^2=f^2+6mf-c
\]
reduces modulo each \(\ell\in\mathcal P\) to
\[
  u^2\equiv f^2-c.
\]

Equivalently,
\[
  (f-u)(f+u)=c.
\]

This has local solutions modulo every odd prime.  By CRT, these local
choices can be combined with the layer lattices for \(f\), and by adding
multiples of the full CRT modulus the corresponding ranks can be made
arbitrarily large and distinct.

Thus:
\[
\boxed{
  \text{finite independent local-square tests cannot close arbitrary}
  \text{ skipped ranks.}
}
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_no\_finite\_local\_modular\_closure.md}.
\]

The remaining hard-branch closure must use either:

1. pairwise Pell synchronization; or
2. a rank descent into the closed prefix range.

## 18. Self-residue filter

There is an intrinsic quotient filter not captured by fixed finite local
prime tests.

Reduce
\[
  u^2=f^2+6mf-c
\]
modulo \(f\).  One obtains
\[
\boxed{
  u^2\equiv-c\pmod f.
}
\]

Hence every odd prime divisor
\[
  q\mid f,\qquad q\nmid c
\]
must satisfy
\[
\boxed{
  \left(\frac{-c}{q}\right)=1.
}
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_self\_residue\_filter.md}.
\]

The modulo \(7\) zero-filter was only one instance of this rule.  The
general form supplies a non-finite obstruction for skipped ranks: as
quotients climb, their own prime divisors create new necessary quadratic
residue tests.

The next theoretical closure target is now:
\[
\boxed{
  \text{self-residue filter}+\text{pairwise Pell synchronization}
  \Longrightarrow \text{rank descent.}
}
\]

## 19. A0 square-offset quotient theorem

The A0 offsets are squares:
\[
  c=x^2,\qquad x\in\{2,4,8,10\}.
\]

For these rows the self-residue filter becomes the sum-of-two-squares
quotient condition
\[
\boxed{
  u^2+x^2\equiv0\pmod f.
}
\]

Let
\[
  q^\alpha\Vert f,\qquad \beta=v_q(x).
\]

Then this congruence is solvable modulo \(q^\alpha\) if and only if:
\[
\begin{array}{c|c}
  q & \text{condition}\\
  \hline
  q\text{ odd} & \alpha\le2\beta\text{ or }q\equiv1\pmod4\\
  q=2 & \alpha\le2\beta+1.
\end{array}
\]

Indeed, if \(\alpha\le2\beta\), the choice \(u=0\) works.  Otherwise divide
by \(q^{2\beta}\).  For odd \(q\), the reduced condition is that \(-1\) is a
quadratic residue modulo \(q\), equivalently \(q\equiv1\pmod4\).  For
\(q=2\), the residual modulus can only be \(2\), since modulo \(4\) the
congruence \(v^2\equiv-1\) is impossible.

Thus:
\[
\begin{array}{c|c|c}
  c & x & \text{condition on }f\\
  \hline
  4 & 2
    & v_2(f)\le3,\ \text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  16 & 4
    & v_2(f)\le5,\ \text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  64 & 8
    & v_2(f)\le7,\ \text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  100 & 10
    & v_2(f)\le3,\ \text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4.
\end{array}
\]

The offsets \(c=16\) and \(c=64\) are therefore no longer symmetric in the
skipped-rank problem: for example \(f=64\) passes the A0 square quotient
filter for \(c=64\), but not for \(c=16\).

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A0\_square\_quotient\_theorem.md}.
\]

The closure target is correspondingly refined:
\[
\boxed{
  \text{A0 prime-power quotient theorem}
  +\text{A1 self-residue constraints}
  +\text{pairwise Pell synchronization}
  \Longrightarrow \text{rank descent.}
}
\]

## 20. A1 quadratic-field quotient theorem

For A1 rows,
\[
  c\in\{2,26,50,122\},
  \qquad
  f\equiv9\pmod{12}.
\]

Thus \(f\) is odd and divisible by \(3\), and the self-residue condition is
\[
\boxed{
  u^2\equiv-c\pmod f.
}
\]

Let
\[
  q^\alpha\Vert f,
  \qquad
  \gamma=v_q(c)
\]
for an odd prime \(q\).  The congruence modulo \(q^\alpha\) is governed by
the quadratic field \(\mathbb Q(\sqrt{-c})\):

- if \(q\nmid c\), then \(q\) must split:
  \[
    \left(\frac{-c}{q}\right)=1;
  \]
- if \(q\mid c\) and \(\alpha\le\gamma\), then \(u=0\) works;
- if \(q\mid c\), \(\alpha>\gamma\), and \(\gamma\) is even, then
  \[
    \left(\frac{-c/q^\gamma}{q}\right)=1;
  \]
- if \(q\mid c\), \(\alpha>\gamma\), and \(\gamma\) is odd, no solution
  exists.

Therefore:
\[
\begin{array}{c|c}
  c & \text{condition on }f\\
  \hline
  2
    & \left(\frac{-2}{q}\right)=1\text{ for every }q\mid f\\
  26
    & v_{13}(f)\le1,\quad
      \left(\frac{-26}{q}\right)=1\text{ for }q\mid f,\ q\ne13\\
  50
    & v_5(f)\le2,\quad
      \left(\frac{-50}{q}\right)=1\text{ for }q\mid f,\ q\ne5\\
  122
    & v_{61}(f)\le1,\quad
      \left(\frac{-122}{q}\right)=1\text{ for }q\mid f,\ q\ne61.
\end{array}
\]

The forced factor \(3\mid f\) is harmless for every A1 offset because
\[
  c\equiv2\pmod3,
  \qquad
  -c\equiv1\pmod3.
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A1\_quadratic\_field\_quotient\_theorem.md}.
\]

The hard branch is now reduced to a more rigid problem:
\[
\boxed{
  \text{A0 sum-of-two-squares quotient laws}
  +\text{A1 quadratic-field quotient laws}
  +\text{pairwise Pell synchronization}
  \Longrightarrow \text{rank descent.}
}
\]

## 21. A0 zero-layer collapse

The A0 zero offsets
\[
  c=16,\ 64
\]
originally had the layer
\[
  f\equiv8,14,16,22\pmod{24}.
\]

The A0 quotient theorem collapses this layer.

Indeed, for both \(c=16\) and \(c=64\),
\[
  f=2^\nu s,
  \qquad
  s\text{ odd},
  \qquad
  q\mid s\Rightarrow q\equiv1\pmod4.
\]

Thus
\[
  s\equiv1\pmod4.
\]

If \(f\equiv14\pmod{24}\), then \(v_2(f)=1\) and
\[
  s=f/2\equiv7\pmod{12}\equiv3\pmod4,
\]
impossible.  If \(f\equiv22\pmod{24}\), then
\[
  s=f/2\equiv11\pmod{12}\equiv3\pmod4,
\]
also impossible.

Therefore:
\[
\boxed{
  c=16,64
  \quad\Longrightarrow\quad
  f\equiv8,16\pmod{24}.
}
\]

The precise surviving forms are
\[
\begin{array}{c|c}
  c & \text{allowed form}\\
  \hline
  16
    & f=2^\nu s,\quad3\le\nu\le5,\quad
      q\mid s\Rightarrow q\equiv1\pmod4\\
  64
    & f=2^\nu s,\quad3\le\nu\le7,\quad
      q\mid s\Rightarrow q\equiv1\pmod4.
\end{array}
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A0\_zero\_layer\_collapse.md}.
\]

Consequently the previous first-escape family
\[
  16\leadsto22
\]
is not merely locally killed modulo \(5\); it is absent from the intrinsic
quotient lattice.  The hard rank game now has a thinner zero-layer lattice
before any pairwise Pell synchronization is applied.

## 22. A0 four-layer refinement

For the other A0 offsets
\[
  c=4,\ 100,
\]
the old layer was
\[
  f\equiv2,4,10,20\pmod{24}.
\]

The A0 quotient theorem forces
\[
  f=2s
  \quad\text{or}\quad
  f=4s,
\]
where
\[
  s\text{ is odd},
  \qquad
  3\nmid s,
  \qquad
  q\mid s\Rightarrow q\equiv1\pmod4.
\]

Therefore \(s\equiv1\pmod4\).

If \(f=2s\), this gives
\[
  f\equiv2,10\pmod{24}.
\]

If \(f=4s\), the residue is sharper:
\[
\boxed{
  f\equiv4,20\pmod{48}.
}
\]

Thus the old modulo-\(24\) classes
\[
  f\equiv4,20\pmod{24}
\]
contained two impossible modulo-\(48\) sub-classes:
\[
\boxed{
  f\equiv28,44\pmod{48}.
}
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A0\_four\_layer\_refinement.md}.
\]

After Sections 21 and 22, the A0 part of the hard branch is no longer an
additive rank lattice.  It is a pair of explicit multiplicative quotient
semigroups:
\[
  2\mathcal S\cup4\mathcal S
  \quad(c=4,100),
\]
and
\[
  \{2^\nu s:3\le\nu\le5\text{ or }3\le\nu\le7,\ q\mid s\Rightarrow q\equiv1\pmod4\}
  \quad(c=16,64),
\]
where
\[
  \mathcal S=\{s:\ s\text{ odd},\ 3\nmid s,\ q\mid s\Rightarrow q\equiv1\pmod4\}.
\]

The remaining exact target is to combine these A0 semigroups with the A1
quadratic-field semigroups through the pairwise Pell synchronization
equations.

## 23. Multiplicative rank model

The old rank automaton was additive: it listed allowed residue classes for
the three quotient layers.

The intrinsic quotient theorems replace it by a multiplicative model.

Define
\[
  \mathcal S_4
  =
  \{s\ge1:\ s\text{ odd},\ 3\nmid s,\ q\mid s\Rightarrow q\equiv1\pmod4\}.
\]

Then the A0 quotient sets are:
\[
\begin{array}{c|c}
  c & f_c\text{ belongs to}\\
  \hline
  4,100 & 2\mathcal S_4\cup4\mathcal S_4\\
  16 & \bigcup_{\nu=3}^{5}2^\nu\mathcal S_4\\
  64 & \bigcup_{\nu=3}^{7}2^\nu\mathcal S_4.
\end{array}
\]

The A1 quotient sets are the splitting semigroups
\[
  \mathcal T_2,\quad
  \mathcal T_{26},\quad
  \mathcal T_{50},\quad
  \mathcal T_{122},
\]
where always
\[
  f\equiv9\pmod{12},
\]
and away from ramified primes one has
\[
  \left(\frac{-c}{q}\right)=1.
\]

The ramified caps are
\[
  v_{13}(f)\le1,
  \qquad
  v_5(f)\le2,
  \qquad
  v_{61}(f)\le1.
\]

Thus a hard-branch clean-gate counterexample must solve
\[
  u_c^2=f_c^2+6mf_c-c
\]
with
\[
  f_c\in\mathcal M_c
\]
for the corresponding multiplicative semigroup \(\mathcal M_c\).

Equivalently, after eliminating \(m\), every pair of offsets satisfies
\[
\boxed{
  f_d u_c^2-f_c u_d^2
  =
  f_cf_d(f_c-f_d)-f_dc+f_cd.
}
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_multiplicative\_rank\_model.md}.
\]

The remaining closure target is now:
\[
\boxed{
  f_c\in\mathcal M_c
  \text{ for all }c
  +\text{pairwise Pell synchronization}
  \Longrightarrow
  \text{rank descent into the closed prefix range.}
}
\]

## 24. Shared-prime compatibility

The multiplicative model also has edge constraints.

If an odd prime \(q\) divides both \(f_c\) and \(f_d\), and
\[
  q\nmid cd,
\]
then the two self-residue congruences give
\[
\boxed{
  \left(\frac{-c}{q}\right)=
  \left(\frac{-d}{q}\right)=1.
}
\]

Thus \(q\) splits in both quadratic fields
\[
  \mathbb Q(\sqrt{-c}),
  \qquad
  \mathbb Q(\sqrt{-d}),
\]
or equivalently splits completely in
\[
  \mathbb Q(\sqrt{-c},\sqrt{-d}).
\]

In particular, for any A0 offset \(a\) and A1 offset \(b\),
\[
\boxed{
  \gcd(f_a,f_b)\text{ is coprime to }6.
}
\]

Every nonramified common prime on an A0--A1 edge must satisfy
\[
  q\equiv1\pmod4,
  \qquad
  \left(\frac{-b}{q}\right)=1.
\]

Since \(q\equiv1\pmod4\), this is the same as
\[
  \left(\frac{b}{q}\right)=1.
\]

For A1--A1 edges, the prime \(3\) is always allowed, since
\[
  -c\equiv1\pmod3
\]
for all A1 offsets.  Every other nonramified shared prime must split in the
corresponding biquadratic field.

This is recorded in
\[
  \texttt{legendre\_m3mod4\_shared\_prime\_compatibility.md}.
\]

The closure target is now graph-theoretic as well as Pell-theoretic:
\[
\boxed{
  \text{vertex semigroups}
  +\text{edge shared-prime compatibility}
  +\text{pairwise Pell synchronization}
  \Longrightarrow
  \text{rank descent.}
}
\]

## 25. Dual-factor gap model

Each reduced Pell line can be factored:
\[
  u_c^2=f_c^2+6mf_c-c
  \quad\Longleftrightarrow\quad
  u_c^2+c=f_c(f_c+6m).
\]

Set
\[
  L=6m,
  \qquad
  F_c=f_c+L.
\]

Since \(m\equiv3\pmod4\),
\[
\boxed{
  L\equiv18\pmod{24}.
}
\]

Then every row is a same-gap factorization:
\[
\boxed{
  u_c^2+c=f_cF_c,
  \qquad
  F_c-f_c=L.
}
\]

The upper factor obeys the same self-residue law:
\[
\boxed{
  u_c^2\equiv-c\pmod{F_c}.
}
\]

Hence all prime-power splitting laws already proved for \(f_c\) also apply
to \(F_c\).  In particular:

- for A0, every odd prime divisor of \(f_cF_c\) is \(1\bmod4\), with the
  offset-specific \(2\)-adic ceiling on both factors;
- for A1, both \(f_c\) and \(F_c\) obey the same quadratic-field splitting
  law and the same ramified caps.

For A1 rows,
\[
  f_c\equiv9\pmod{12},
  \qquad
  F_c=f_c+L\equiv3\pmod{12}.
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_dual\_factor\_gap\_model.md}.
\]

The hard branch is therefore an eight-row same-gap factorization problem:
\[
\boxed{
  u_c^2+c=f_cF_c,\quad
  F_c-f_c=L\equiv18\pmod{24},
}
\]
where both factors on every row satisfy the offset-specific splitting law.

The strengthened descent target is:
\[
\boxed{
  \text{two-sided splitting laws}
  +\text{common gap }L
  +\text{prime-label admissibility}
  \Longrightarrow
  \text{rank descent.}
}
\]

## 26. A0 dual four-layer collapse

The dual-factor model collapses the A0 \(c=4,100\) lower layer further.

For these two offsets the earlier A0 four-layer refinement gave
\[
  f=2s
  \quad\text{or}\quad
  f=4s,
\]
where
\[
  s\in\mathcal S_4.
\]

In particular,
\[
  s\equiv1\pmod4.
\]

Write
\[
  L=6m=2h.
\]

Since \(m\equiv3\pmod4\),
\[
  h=3m\equiv1\pmod4.
\]

If \(f=4s\), the upper factor is
\[
  F=f+L=4s+2h=2(2s+h).
\]

But
\[
  2s+h\equiv3\pmod4.
\]

This is impossible because the dual A0 splitting law requires every odd
prime divisor of \(F\) to be \(1\bmod4\), hence the odd part of \(F\) must be
\(1\bmod4\).

Therefore:
\[
\boxed{
  c=4,100
  \quad\Longrightarrow\quad
  f\in2\mathcal S_4.
}
\]

If \(f=2s\), then
\[
  F=2(s+h),
\]
and since \(s+h\equiv2\pmod4\), one has
\[
  F=4t.
\]

The upper splitting law then imposes
\[
  t\in\mathcal S_4.
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A0\_dual\_four\_layer\_collapse.md}.
\]

Thus the \(c=4,100\) pair has first two distinct lower quotients
\[
\boxed{
  2,\ 10
}
\]
instead of \(2,4\).  The old escape
\[
  4\leadsto10
\]
is now a structural consequence of the two-sided factorization.

## 27. A0 dual valuation collapse

The equality
\[
  u^2+x^2=fF
\]
also sharpens the A0 zero layer.

For \(c=16,64\), write
\[
  f=2^\nu s,
  \qquad
  \nu\ge3,
  \qquad
  s\text{ odd}.
\]

Since
\[
  F=f+6m=f+2h,
  \qquad
  h\equiv1\pmod4,
\]
one has
\[
\boxed{
  v_2(F)=1.
}
\]

Thus
\[
  v_2(fF)=\nu+1.
\]

For \(c=16\), \(x=4\), and the possible valuations of \(u^2+16\) are
\[
  0,\ 2,\ 4,\ 5.
\]

So \(\nu=5\) is impossible:
\[
\boxed{
  c=16:\quad f\in8\mathcal S_4\cup16\mathcal S_4.
}
\]

For \(c=64\), \(x=8\), and the possible valuations of \(u^2+64\) are
\[
  0,\ 2,\ 4,\ 6,\ 7.
\]

So \(\nu=4\) and \(\nu=7\) are impossible:
\[
\boxed{
  c=64:\quad f\in8\mathcal S_4\cup32\mathcal S_4\cup64\mathcal S_4.
}
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A0\_dual\_valuation\_collapse.md}.
\]

In particular, the lower quotient \(f=16\) is assignment-rigid:
\[
\boxed{
  f=16\quad\Longrightarrow\quad c=16.
}
\]

The bottom of the A0 zero layer is therefore no longer symmetric.

## 28. A1 dual sign-parity law

For every A1 row,
\[
  f_c\equiv9\pmod{12}.
\]

Since
\[
  L=6m\equiv18\pmod{24},
  \qquad
  F_c=f_c+L,
\]
one has
\[
\boxed{
  f_c\equiv1\pmod4,
  \qquad
  F_c\equiv3\pmod4.
}
\]

Both factors satisfy the same A1 splitting law, but they have opposite
prime-sign parity.

For odd \(N\), define
\[
  \Omega_3(N)
  =
  \sum_{\substack{q^\alpha\Vert N\\q\equiv3\pmod4}}\alpha.
\]

Then
\[
  N\equiv(-1)^{\Omega_3(N)}\pmod4.
\]

Therefore:
\[
\boxed{
  \Omega_3(f_c)\equiv0\pmod2,
  \qquad
  \Omega_3(F_c)\equiv1\pmod2.
}
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A1\_dual\_sign\_parity.md}.
\]

The A1 descent problem is now a same-field split-pair problem with opposite
sign parity across the common gap \(L\).

## 29. A0 dual boundary killed modulo 23

After the A0 dual collapses, the first A0 structural boundary is:
\[
  c=4,100:\quad f=2,10,
\]
and
\[
  c=16,64:\quad f=16,8,
\]
with \(f=16\) forced on \(c=16\).

There are only two assignments for \(c=4,100\):
\[
\begin{array}{c|cc}
  \text{case} & c=4 & c=100\\
  \hline
  I & 2 & 10\\
  II & 10 & 2.
\end{array}
\]

Both are killed modulo \(23\).

For
\[
  M_{23}(c,f)
  =
  \{m\bmod23:\ f^2+6mf-c\text{ is a square modulo }23\},
\]
case I satisfies
\[
  M_{23}(4,2)\cap M_{23}(100,10)=\{0\},
  \qquad
  0\notin M_{23}(16,16).
\]

Case II satisfies
\[
  M_{23}(4,10)
  \cap M_{23}(100,2)
  \cap M_{23}(16,16)
  =
  \{10,17\},
\]
and
\[
  \{10,17\}\cap M_{23}(64,8)=\varnothing.
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A0\_dual\_boundary\_mod23.md}.
\]

Therefore the new A0 dual boundary has no integral point.

## 30. A0 dual two-value prefix certificate

The complete A0 two-value structural prefix after the dual collapses is:
\[
\begin{array}{c|c}
  c & \text{first two values}\\
  \hline
  4 & 2,\ 10\\
  100 & 2,\ 10\\
  16 & 8,\ 16\\
  64 & 8,\ 32.
\end{array}
\]

Pairwise distinctness leaves exactly six assignments.  They are all killed
by finite congruence certificates:
\[
\begin{array}{c|c|c|c|c}
  c=4 & c=100 & c=16 & c=64 & \text{killing prime}\\
  \hline
  2 & 10 & 8  & 32 & 7\\
  2 & 10 & 16 & 8  & 13\\
  2 & 10 & 16 & 32 & 13\\
  10 & 2 & 8  & 32 & 5\\
  10 & 2 & 16 & 8  & 23\\
  10 & 2 & 16 & 32 & 17.
\end{array}
\]

This is recorded in
\[
  \texttt{legendre\_m3mod4\_A0\_dual\_prefix2\_certificate.md}.
\]

Thus any remaining hard-branch counterexample must use a higher A0 lower
quotient:
\[
\boxed{
  c=4,100:\ f\ge26
  \quad\text{or}\quad
  c=16:\ f\ge40
  \quad\text{or}\quad
  c=64:\ f\ge40.
}
\]

## 31. Structural prefix 7 closed

The structural quotient model now has a finite prefix certificate using the
first seven values in each offset row.

The verifier is
\[
  \texttt{tools/m3mod4\_structural\_prefix\_certificate.py}.
\]

For prefix \(7\), it checks
\[
  2882250
\]
pairwise-distinct assignments.  Finite local certificates kill all but two
assignments.  The two survivors are:
\[
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 10 & 58 & 8 & 40 & 9 & 21 & 33 & 69
\end{array}
\]
and
\[
\begin{array}{c|cccccccc}
  c & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f & 10 & 58 & 16 & 40 & 9 & 21 & 33 & 69.
\end{array}
\]

Both are ghost fibers with the universal local class
\[
  m\equiv-1.
\]

For the first survivor, the row \((c,f)=(16,8)\) gives
\[
  m=12n^2-1.
\]

The rows \((4,10)\) and \((64,40)\) then force
\[
  X^2=20n^2+1,
  \qquad
  Y^2=20n^2+9.
\]

Thus
\[
  Y^2-X^2=8,
\]
so \(X=1,Y=3\), hence \(n=0\) and \(m=-1\).

For the second survivor, the same two rows give
\[
  3X^2=5m+8,
  \qquad
  3Y^2=5m+32,
\]
again forcing
\[
  Y^2-X^2=8
  \quad\Longrightarrow\quad
  m=-1.
\]

Therefore neither survivor gives a positive hard-branch point, and
\[
\boxed{
  \text{structural prefix }7\text{ is closed.}
}
\]

For prefix \(8\), new local survivors appear beyond these two ghost fibers;
some pass through the small positive class \(m=3\).  They form the next
exceptional boundary target.

## 32. Prefix 8: exceptional fibers, not an infinite descent

The next structural prefix does not produce a new generic component.  It
produces a finite exceptional frontier whose exact algebraic content is
recorded in
\[
  \texttt{legendre\_m3mod4\_prefix8\_exceptional\_pell\_fibers.md}.
\]

For prefix \(8\), the verifier leaves \(15\) local survivors.  They split as:
\[
\begin{array}{c|c}
\text{fiber type} & \#\\
\hline
m=-1 & 2\\
m=3 & 8\\
\text{empty modulo }9 & 3\\
\text{residual Pell systems} & 2.
\end{array}
\]

The \(m=-1\) and \(m=3\) fibers are saturated boundary fibers.  The three
modulo-\(9\) systems have no integral point.  Hence only two residual
systems remain.

Both residual systems force
\[
  m=27k+3,\qquad 2k+1=s^2,
\]
and share the common core
\[
\begin{aligned}
  2X_4^2   &=153s^2-55,\\
  2X_{100}^2&=41s^2+9,\\
  2X_{16}^2&=45s^2-13,\\
  X_2^2    &=2673s^2-992,\\
  X_{50}^2 &=4617s^2-392.
\end{aligned}
\]

The first terminal pair is
\[
  X_{26}^2=1701s^2-908,\qquad
  X_{122}^2=7533s^2+2668.
\]

The second terminal pair is
\[
  X_{26}^2=3645s^2-836,\qquad
  X_{122}^2=1701s^2-1004.
\]

This replaces the former prefix-growth problem by a fixed Diophantine
problem: prove that these two coupled Pell systems have no positive integral
point after the \(m=-1\) and \(m=3\) saturations.
