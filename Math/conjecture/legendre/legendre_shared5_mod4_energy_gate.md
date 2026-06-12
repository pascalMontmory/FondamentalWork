# Mod-\(4\) Energy Gate in the Shared-\(5\) Certificate

This note gives the first compressed-certificate strengthening after the
route audit.

It is not a new fiber split.  It is a rank/energy obstruction inside the
already compressed shared-\(5\) certificate
\[
  \mathcal C=\{5,17,25,49,65\}.
\]

## 1. Setup

We are in the shared-\(5\) fiber:
\[
  A=3m,\qquad m\ \text{even},\qquad A^2\equiv-1\pmod5.
\]

The variable offsets are
\[
  \mathcal C=\{5,17,25,49,65\}.
\]
For every \(c\in\mathcal C\), a composite certificate has
\[
  p_c=A-r_c
\]
and
\[
  (A-r_c)e_c=r_c^2+c.
\]

The previous shared-\(5\) rank gate proved:

- the five labels \(p_c\) are pairwise distinct;
- for \(A\ge3488\), the five quotients \(e_c\) are pairwise distinct.

## 2. All variable quotients are \(2\pmod4\)

Since \(m\) is even,
\[
  A=3m
\]
is even.

Each certificate label \(p_c=A-r_c\) is an odd prime.  Therefore
\[
  r_c=A-p_c
\]
is odd.

Every offset in
\[
  \mathcal C=\{5,17,25,49,65\}
\]
satisfies
\[
  c\equiv1\pmod4.
\]
Thus
\[
  r_c^2+c\equiv1+1\equiv2\pmod4.
\]

But
\[
  r_c^2+c=p_ce_c,
\]
and \(p_c\) is odd.  Multiplying by the inverse of \(p_c\) modulo \(4\),
one gets
\[
\boxed{
  e_c\equiv2\pmod4
  \qquad(c\in\{5,17,25,49,65\}).
}
\]

This includes all ramified gates \(p=7,13,17\), because those labels are
also odd.

## 3. Five distinct quotients in one residue class

For \(A\ge3488\), the five quotients are pairwise distinct and all lie in
the same residue class
\[
  2\pmod4.
\]

Order them as
\[
  e_{(1)}<e_{(2)}<e_{(3)}<e_{(4)}<e_{(5)}.
\]
Then
\[
\boxed{
  e_{(k)}\ge4k-2
  \qquad(1\le k\le5).
}
\]

Explicitly,
\[
  e_{(1)}\ge2,\quad
  e_{(2)}\ge6,\quad
  e_{(3)}\ge10,\quad
  e_{(4)}\ge14,\quad
  e_{(5)}\ge18.
\]

Therefore the certificate energy satisfies
\[
\boxed{
  \mathcal E_A(\mathcal C)
  =
  \sum_{c\in\mathcal C}e_c
  \ge
  2+6+10+14+18
  =
  50.
}
\]

This replaces the weaker rank energy lower bound
\[
  1+2+3+4+5=15.
\]

## 4. Improved distance barriers

For a fixed quotient lower bound \(E\), the centered equation
\[
  r^2+Er+c=EA
\]
gives
\[
  r\ge
  \left\lceil
    \frac{-E+\sqrt{E^2+4(EA-c)}}{2}
  \right\rceil.
\]

Since all offsets in \(\mathcal C\) satisfy \(c\le65\), and the \(k\)-th
quotient rank satisfies
\[
  E_k=4k-2,
\]
we get
\[
\boxed{
  r_{(k)}
  \ge
  \left\lceil
    \frac{-E_k+\sqrt{E_k^2+4(E_kA-65)}}{2}
  \right\rceil,
  \qquad E_k=4k-2.
}
\]

In particular, the top quotient rank gives
\[
  E_5=18,
\]
and hence
\[
\boxed{
  r_{(5)}
  \ge
  \left\lceil
    -9+\sqrt{18A+16}
  \right\rceil.
}
\]

Thus at least one variable label satisfies
\[
\boxed{
  p=A-r
  \le
  A-
  \left\lceil
    -9+\sqrt{18A+16}
  \right\rceil.
}
\]

This is substantially stronger than the previous five-rank barrier
\[
  r_{(5)}
  \ge
  \left\lceil
    \frac{-5+\sqrt{20A-235}}{2}
  \right\rceil.
\]

## 5. Why this matters

The shared-\(5\) compressed certificate now has:

1. five distinct variable labels;
2. five distinct quotients for \(A\ge3488\);
3. all five quotients constrained to the same residue class \(2\pmod4\);
4. certificate energy at least \(50\);
5. a top distance at least
   \[
     \left\lceil -9+\sqrt{18A+16}\right\rceil.
   \]

This is the first genuine energy gate for the compressed-certificate route.
It does not close the fiber, but it gives a sharper invariant that any
geometric, topological, or Nullstellensatz non-realization attempt must use.

## 6. Next exact target

The next non-repetitive step is:

> Build the shared-\(5\) incidence ideal with the quotient congruences
> \[
>   e_c\equiv2\pmod4
> \]
> and the strict rank lower bounds
> \[
>   e_{(k)}\ge4k-2.
> \]

Equivalently, every quotient-rank permutation should now be tested only
inside the arithmetic progression
\[
  2,6,10,14,18,\dots
\]
not inside all positive integers.
