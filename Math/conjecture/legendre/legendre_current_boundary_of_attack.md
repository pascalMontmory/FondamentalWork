# Current Boundary of the Legendre Attack

This note records the exact point reached by the current route.

It is not a proof of Legendre.  It is the strongest exact decomposition
currently available in this repository.

## 1. Closed and reduced parts

The residual elliptic endpoint in the \(m\equiv3\pmod4\) branch was closed
by the \(3\)-adic Mordell-Weil coset argument.

The remaining global obstruction is the coprime complete A-block gate for
\[
  n=3m.
\]

For every complete coprime block, failure requires two distinct small-prime
certificates in A0 and A1.

## 2. Present global decomposition

Let
\[
  A=3m,\qquad T_m=\lfloor\sqrt{6m}\rfloor,
\]
\[
  Q_m^\ast=\left\lfloor\frac{\sqrt{6m}-2}{3}\right\rfloor,
\]
\[
  B_m=6Q_m^\ast+4,\qquad C_m=2T_m.
\]

The labels split into:

- low:
  \[
    p\le B_m;
  \]
- middle:
  \[
    B_m<p\le C_m,\qquad 0\le C_m-B_m\le4;
  \]
- high:
  \[
    C_m<p\le A.
  \]

All repeated ordered pairs lie in the low box
\[
  p_0,p_1\le B_m.
\]
All high labels are least-root events:
\[
  t=\|Ai_p\|_p
  \quad\text{or}\quad
  t=\|s_p\|_p,\ s_p^2\equiv-A^2-1\pmod p.
\]

The high-high cell is a shift-intersection of the high A0/A1 root images.
The mixed cells are neighbor images of one high root set into one low-or-
middle layer.

## 3. Exact final non-cover statement

The current route would close if one proves:

> For every \(m\ge1\), the complete coprime A-block set cannot be covered by
> the union of:
>
> 1. the low-low centered cofactor box \(p_0,p_1\le B_m\);
> 2. the bounded middle endpoint corrections \(B_m<p\le C_m\);
> 3. the high-high shift intersections
>    \[
>      R_0^{\rm hi}\cap(R_1^{\rm hi}-1),
>      \qquad
>      R_1^{\rm hi}\cap(R_0^{\rm hi}-1);
>    \]
> 4. the mixed neighbor sets
>    \[
>      \operatorname{nb}(R_0^{\rm hi})\cap S_1^{\le C},
>      \qquad
>      \operatorname{nb}(R_1^{\rm hi})\cap S_0^{\le C}.
>    \]

This is now a precise non-cover theorem.  It is substantially sharper than
the original pair-cover formulation, because large labels have been removed
as arbitrary covering resources.

## 4. Present limit

The remaining theorem is still hard.  It asks for a correlation/non-cover
result for least square-root images modulo primes, coupled with a finite
low-label cofactor system.

Without a new estimate or descent for those least-root image correlations,
the current route does not yet prove Legendre.

The productive next work is therefore not more initial blocks.  It is one of:

1. prove a correlation bound for the high least-root shift intersections;
2. prove a finite low-box cofactor non-cover theorem;
3. find a descent showing that any full cover at \(m\) produces a smaller
   full cover at \(m'<m\).

Any of these would be a genuine closure mechanism.
