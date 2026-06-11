# Initial Square-Root Barrier

This note extracts the first inequality obstruction from the center-divisor
parametrization.

The clean strong-gate divisor condition is
\[
  A-r\mid r^2+c,
  \qquad A=3m.
\]
Since \(A-r\) is a positive prime divisor, it cannot exceed the positive
integer it divides.  This gives a square-root lower bound for the distance
\(r\) from the center.

## 1. The basic barrier

Let
\[
  0<c\le2A,
\]
and suppose
\[
  p=A-r
\]
is a prime divisor certifying the compositeness of
\[
  A^2+c.
\]
Then
\[
  p\mid r^2+c.
\]
Since \(r^2+c>0\), one has
\[
  A-r=p\le r^2+c.
\]
Equivalently,
\[
  r^2+r+c\ge A.
\]

Thus, whenever \(A>c\),
\[
\boxed{
  r\ge
  \left\lceil
    \frac{-1+\sqrt{1+4(A-c)}}{2}
  \right\rceil.
}
\]

In particular, for fixed \(c\),
\[
  r\ge \sqrt A+O(1).
\]

So a prime label
\[
  p=A-r
\]
cannot lie too close to \(A\).  It must satisfy
\[
\boxed{
  p\le
  A-
  \left\lceil
    \frac{-1+\sqrt{1+4(A-c)}}{2}
  \right\rceil.
}
\]

This is a deterministic exclusion interval at the top of the possible prime
labels.

## 2. Uniform barrier for the initial cluster

For the initial clean-gate cluster, the largest offset is
\[
  c_{\max}=122.
\]

Therefore, for
\[
  A>122,
\]
every one of the eight center distances satisfies the uniform lower bound
\[
\boxed{
  r_c\ge
  R(A):=
  \left\lceil
    \frac{-1+\sqrt{1+4(A-122)}}{2}
  \right\rceil.
}
\]

Equivalently, every prime label in the clean strong-gate cluster satisfies
\[
\boxed{
  p_c\le A-R(A).
}
\]

The top interval
\[
  A-R(A)<p\le A
\]
contains no possible label for any of the eight initial candidates.

For \(21\le m\le40\), i.e.
\[
  63\le A\le120,
\]
the uniform \(c_{\max}\) bound is not active for all offsets.  The exact
individual bound from Section 1 still applies whenever \(A>c\).  These are
finite boundary values for the square-root-barrier argument.

## 3. Quotient strata

The center-divisor parametrization gives
\[
  r^2+c=e(A-r),
\]
where
\[
  e=\frac{r^2+c}{A-r}
\]
is a positive integer.

Thus the admissible distances for a fixed offset \(c\) are partitioned by the
integer quotient \(e\):
\[
\boxed{
  r^2+er+c-Ae=0.
}
\]

Solving for \(A\) gives
\[
\boxed{
  A=r+\frac{r^2+c}{e}.
}
\]

Consequently, for each fixed offset \(c\) and quotient \(e\), the center
\(A\) is forced by the divisibility
\[
  e\mid r^2+c
\]
and the formula above.

This is a second exact parametrization:
\[
  (r,e)
  \longmapsto
  A=r+\frac{r^2+c}{e},
  \qquad
  p=A-r=\frac{r^2+c}{e}.
\]

In particular, the prime label is precisely
\[
\boxed{
  p=\frac{r^2+c}{e}.
}
\]

So admissible labels for a fixed \(c\) are not arbitrary primes below \(A\):
they are prime quotients of shifted squares \(r^2+c\).

## 4. Clean strong-gate consequence

In the clean strong gate, a counterexample must assign to each
\[
  c\in\mathcal C_{\rm parity(m)}
\]
a distance \(r_c\) and quotient \(e_c\) such that
\[
  A=r_c+\frac{r_c^2+c}{e_c},
\]
\[
  p_c=\frac{r_c^2+c}{e_c}
\]
is a distinct admissible prime.

For \(A>122\), all eight distances obey
\[
  r_c\ge R(A)\asymp\sqrt A.
\]

Thus the clean strong-gate obstruction has been sharpened:

> eight fixed offsets must represent the same center \(A\) as
> \[
>   A=r_c+\frac{r_c^2+c}{e_c}
> \]
> with eight distinct prime quotients
> \[
>   \frac{r_c^2+c}{e_c}.
> \]

This is still a necessary obstruction, not a completed proof.  The next
exact target is to compare two offsets \(c,d\) in this quotient form and
derive incompatibilities from equality of the shared center \(A\).
