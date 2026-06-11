# Prefix-8 Exceptional Pell Fibers

This note records the exact meaning of the next structural frontier in the
hard branch
\[
  m\equiv 3\pmod 4.
\]

It is not a numerical search statement.  The structural quotient certificate
for prefix \(8\) leaves finitely many local survivors.  These survivors split
into exact algebraic fibers.

## 1. Row equations

For every selected offset \(c\) and lower quotient \(f_c\), an integral
counterexample must satisfy
\[
  U_c^2=f_c^2+6mf_c-c.
\]

Thus each prefix assignment is a system of eight linear-square equations in
\(m\).

The prefix-\(8\) verifier checks the structural rows
\[
\begin{array}{c|l}
c & f_c\text{ values}\\
\hline
4   & 2,10,26,34,50,58,74,82\\
100 & 2,10,26,34,50,58,74,82\\
16  & 8,16,40,80,104,136,200,208\\
64  & 8,32,40,64,104,136,160,200\\
2   & 9,33,57,81,129,153,177,201\\
26  & 9,21,45,81,93,105,117,129\\
50  & 9,33,45,57,81,129,153,165\\
122 & 9,21,57,69,81,93,189,213.
\end{array}
\]

There are
\[
  9307368
\]
pairwise-distinct prefix assignments.  Local certificates at odd primes
different from \(3\) kill all but \(15\).

## 2. Exact split of the 15 survivors

The \(15\) survivors are not one generic component.

Two are the already known ghost fibers:
\[
  m=-1.
\]
They are impossible for positive hard-branch points.

Eight are boundary fibers:
\[
  m=3.
\]
In the original Legendre interval this corresponds to the tiny center
\[
  A=3m=9,
\]
and the interval
\[
  9^2<p<10^2
\]
contains the prime \(83\).  Hence these fibers are not counterexamples to
Legendre; in the structural certificate language they must be saturated away
by the factor \(m-3\).

Three further survivors are impossible modulo \(9\).  Equivalently, their
local square system has
\[
  \{m\bmod 9:\ U_c^2\equiv f_c^2+6mf_c-c\pmod 9\text{ for all }c\}=\varnothing.
\]

Thus after saturating the ghost and boundary fibers, the prefix-\(8\)
frontier has exactly two residual algebraic systems.

## 3. The two residual systems

Both residual systems share the six rows
\[
\begin{array}{c|cccccc}
c & 4 & 100 & 16 & 64 & 2 & 50\\
\hline
f_c & 34 & 82 & 40 & 64 & 33 & 57.
\end{array}
\]

The exact congruence system modulo \(81\) forces
\[
  m\equiv 3\pmod{27},
\]
so write
\[
  m=27k+3.
\]

The common row \((c,f)=(64,64)\) gives
\[
  U_{64}^2=64^2+6m\cdot64-64=5184(2k+1).
\]
For positive fibers,
\[
  2k+1=s^2.
\]

Substitution gives the following common Pell-type core:
\[
\begin{aligned}
  2X_4^2   &=153s^2-55,\\
  2X_{100}^2&=41s^2+9,\\
  2X_{16}^2&=45s^2-13,\\
  X_2^2    &=2673s^2-992,\\
  X_{50}^2 &=4617s^2-392.
\end{aligned}
\]

The first residual fiber appends
\[
\begin{aligned}
  X_{26}^2&=1701s^2-908,\\
  X_{122}^2&=7533s^2+2668.
\end{aligned}
\]

The second residual fiber appends
\[
\begin{aligned}
  X_{26}^2&=3645s^2-836,\\
  X_{122}^2&=1701s^2-1004.
\end{aligned}
\]

## 4. Exact closure target

The next closure lemma is therefore not a deeper finite prefix statement.
It is the following Diophantine assertion.

**Residual Pell-fiber lemma.**  There is no positive integer \(s\) satisfying
the common five equations above together with either residual terminal pair,
except the already saturated boundary \(m=3\).

Equivalently, in ideal language, for each residual terminal pair one must
show that the saturated ideal
\[
  I_{\mathrm{res}}:
  \bigl(s(s^2-1)(m+1)(m-3)\prod_c U_c\bigr)^\infty
\]
has no positive integral point after adjoining
\[
  m=27k+3,\qquad 2k+1=s^2,
\]
and the corresponding eight row equations.

This is the correct non-asymptotic target: close the two explicit coupled
Pell systems, not a degree sequence or an infinite CRT descent.

## 5. Elliptic quartic form of the common core

Already the two common equations
\[
  2X_{100}^2=41s^2+9,
  \qquad
  2X_{16}^2=45s^2-13
\]
force
\[
  W^2=(41s^2+9)(45s^2-13),
  \qquad W=2X_{100}X_{16}.
\]

Equivalently,
\[
  \boxed{W^2=1845s^4-128s^2-117.}
\]

The boundary solution is
\[
  s=\pm1,\qquad W=\pm40.
\]

Therefore a sufficient exact closure of both residual fibers is:

**Quartic integral-point lemma.**  The only integral points on
\[
  W^2=1845s^4-128s^2-117
\]
whose \(s\)-coordinate also satisfies the separated common-core square
conditions
\[
\begin{aligned}
  2X_4^2   &=153s^2-55,\\
  2X_{100}^2&=41s^2+9,\\
  2X_{16}^2&=45s^2-13,\\
  X_2^2    &=2673s^2-992,\\
  X_{50}^2 &=4617s^2-392
\end{aligned}
\]
have
\[
  s=\pm1.
\]

The Magma closure target is recorded in
\[
  \texttt{tools/m3mod4\_residual\_pell\_fibers.magma}.
\]

If that script returns only \(s=\pm1\), then \(k=0\), \(m=3\), and the two
residual prefix-\(8\) fibers disappear after the \(m-3\) saturation.
