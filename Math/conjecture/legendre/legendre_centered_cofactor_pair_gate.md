# Centered Cofactor Pair Gate

This note rewrites the cofactor-augmented Mobius gate in centered divisor
variables.  It is the exact bridge between the global \(Z(m)>0\) target and
the earlier quotient-rank machinery.

The point is that a failed coprime A-block is not just two small prime
divisibilities.  It is a pair of centered divisor equations with adjacent
quadratic offsets.

## 1. One value between consecutive squares

Let
\[
  A=3m,\qquad 0<c\le2A,
\]
and let
\[
  N=A^2+c.
\]
Then
\[
  A^2<N<(A+1)^2.
\]

If \(N\) is composite, it has a prime divisor
\[
  p\le A.
\]
In the A-channel all certificate primes satisfy \(p\ge5\).  Write
\[
  p=A-r,\qquad 1\le r\le A-5.
\]
Then
\[
  p\mid N
  \quad\Longleftrightarrow\quad
  A-r\mid r^2+c.
\]

Define
\[
  e=\frac{r^2+c}{A-r}.
\]
Then the cofactor is
\[
  X=A+r+e,
\]
and the factorization is exactly
\[
  A^2+c=(A-r)(A+r+e).
\]

Thus a small-prime certificate is equivalent to the centered divisor
equation
\[
  \boxed{
  A-r\mid r^2+c.
  }
\]

## 2. The pair attached to a block

For a coprime complete A-block \(q\), put
\[
  c_0(q)=t_0(q)^2,\qquad c_1(q)=t_1(q)^2+1.
\]
The two failed values are
\[
  G_q=A^2+c_0(q),\qquad U_q=A^2+c_1(q).
\]

Failure on the block is equivalent to the existence of two distances
\[
  r_0(q),r_1(q)
\]
such that
\[
  p_0=A-r_0,\qquad p_1=A-r_1
\]
are eligible distinct primes and
\[
  A-r_0\mid r_0^2+c_0(q),
\]
\[
  A-r_1\mid r_1^2+c_1(q).
\]

Let
\[
  e_i(q)=\frac{r_i(q)^2+c_i(q)}{A-r_i(q)}\qquad(i=0,1).
\]
Then
\[
  X_i=A+r_i+e_i.
\]

The cofactor difference equation becomes, after cancelling \(A^2\),
\[
  c_1(q)-c_0(q)
  =
  (A-r_1)(A+r_1+e_1)
  -
  (A-r_0)(A+r_0+e_0).
\]
Equivalently,
\[
  \boxed{
  c_1(q)-c_0(q)
  =
  A(e_1-e_0)-r_1^2+r_0^2-r_1e_1+r_0e_0.
  }
\]

But the left side is tiny and explicit:
\[
  c_1(q)-c_0(q)=\eta_q\,2t_1(q),
\]
where
\[
  \eta_q=
  \begin{cases}
  +1,&q\equiv m\pmod2,\\
  -1,&q\not\equiv m\pmod2.
  \end{cases}
\]

Thus every failed coprime block gives the exact centered pair equation
\[
  \boxed{
  A(e_1-e_0)-r_1^2+r_0^2-r_1e_1+r_0e_0
  =
  \eta_q\,2t_1(q).
  }
\]

## 3. Immediate consequence: quotient closeness

Since
\[
  0<2t_1(q)\le2\sqrt{6m}=O(\sqrt A),
\]
the centered pair equation forces
\[
  A(e_1-e_0)
  =
  r_1^2-r_0^2+r_1e_1-r_0e_0+O(\sqrt A).
\]

The quotients \(e_i\) therefore cannot be chosen independently.  A block
failure requires the two centered quotients to be synchronized by a small
linear error.

This is stronger than the separate conditions
\[
  e_i=\frac{r_i^2+c_i}{A-r_i}.
\]
It couples the two layers inside the same block.

## 4. Two-block centered descent

Suppose the same ordered prime pair \((p_0,p_1)\) covers two blocks \(q\ne r\).
Then the centered distances \(r_0,r_1\) are the same for both blocks, while
the quotients \(e_i(q),e_i(r)\) vary.

Subtracting the centered pair equations gives
\[
\begin{aligned}
  &A\bigl((e_1(q)-e_1(r))-(e_0(q)-e_0(r))\bigr)\\
  &\quad
  -r_1\bigl(e_1(q)-e_1(r)\bigr)
  +r_0\bigl(e_0(q)-e_0(r)\bigr)\\
  &=
  \eta_q\,2t_1(q)-\eta_r\,2t_1(r).
\end{aligned}
\]

Because
\[
  p_i=A-r_i,
\]
this is exactly
\[
  \boxed{
  p_1\bigl(e_1(q)-e_1(r)\bigr)
  -
  p_0\bigl(e_0(q)-e_0(r)\bigr)
  =
  \eta_q\,2t_1(q)-\eta_r\,2t_1(r).
  }
\]

If \(q\equiv r\pmod2\), the right side is
\[
  \pm6(q-r).
\]
If \(q\not\equiv r\pmod2\), the right side is
\[
  \pm6(q+r+1).
\]

This is a descent equation for repeated ordered pairs: the repetition does
not merely force residue hyperplanes.  It forces quotient differences to
solve a short linear equation with coefficients \(p_0,p_1\).

## 5. New non-cover target

The next exact lemma should be stated in these variables:

> **Centered pair non-cover lemma.**  For every \(m\ge1\), not every coprime
> complete A-block \(q\) admits eligible prime distances \(r_0,r_1\) and
> positive quotients \(e_0,e_1\) satisfying
> \[
>   (A-r_i)e_i=r_i^2+c_i(q)\quad(i=0,1)
> \]
> and
> \[
>   A(e_1-e_0)-r_1^2+r_0^2-r_1e_1+r_0e_0
>   =
>   \eta_q\,2t_1(q).
> \]

This lemma is equivalent to the cofactor non-cover lemma, but it is better
suited to exact descent because all small factors are represented by
distances from the moving center \(A=3m\).

It is the next viable proof target after the raw Mobius expansion.
