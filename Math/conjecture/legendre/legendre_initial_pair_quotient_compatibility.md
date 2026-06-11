# Initial Pair-Quotient Compatibility

This note compares two offsets in the quotient form
\[
  A=r+\frac{r^2+c}{e}.
\]

The goal is to replace two independent centered factorizations by one exact
compatibility equation.  This is the next algebraic obstruction for the clean
strong gate.

## 1. Two offsets with the same center

Let two distinct offsets
\[
  c\ne d
\]
share the same center
\[
  A.
\]

Assume they are certified by distances and quotients
\[
  (r_c,e_c),
  \qquad
  (r_d,e_d),
\]
so that
\[
  A=r_c+\frac{r_c^2+c}{e_c}
   =r_d+\frac{r_d^2+d}{e_d}.
\]

Equivalently, their prime labels are
\[
  p_c=\frac{r_c^2+c}{e_c}=A-r_c,
\]
\[
  p_d=\frac{r_d^2+d}{e_d}=A-r_d.
\]

Set
\[
  h=r_d-r_c.
\]
Then the shared-center identity gives
\[
\boxed{
  p_c-p_d=h.
}
\]

In quotient form this is
\[
\boxed{
  \frac{r_c^2+c}{e_c}
  -
  \frac{r_d^2+d}{e_d}
  =
  r_d-r_c.
}
\]

Multiplying by \(e_ce_d\) gives the exact pair-compatibility equation
\[
\boxed{
  e_d(r_c^2+c)-e_c(r_d^2+d)=e_ce_d(r_d-r_c).
}
\]

Substituting
\[
  r_d=r_c+h
\]
gives the one-variable quadratic
\[
\boxed{
  (e_d-e_c)r_c^2
  -2e_chr_c
  +e_dc-e_c(h^2+d)-e_ce_dh
  =0.
}
\]

Thus, for fixed
\[
  c,d,e_c,e_d,h,
\]
the distance \(r_c\) is not free.  It must be an integral root of this
quadratic, and then
\[
  r_d=r_c+h.
\]

This is the binary compatibility equation requested by the shared-center
comparison.

## 2. Equal quotient obstruction

The special case
\[
  e_c=e_d=e
\]
is much sharper.

The compatibility equation becomes
\[
  c-d=h(2r_c+h+e).
\]
Since
\[
  r_d=r_c+h,
\]
this is
\[
\boxed{
  c-d=h(r_c+r_d+e).
}
\]

If the labels are distinct, then
\[
  p_c\ne p_d.
\]
Because
\[
  p_c-p_d=h,
\]
one has
\[
  h\ne0.
\]

Also
\[
  r_c\ge1,\qquad r_d\ge1,\qquad e\ge1.
\]
Therefore
\[
  r_c+r_d+e\ge r_c+2.
\]
Taking absolute values gives
\[
  |c-d|
  =
  |h|(r_c+r_d+e)
  \ge r_c+2.
\]

Hence:
\[
\boxed{
  e_c=e_d,\ c\ne d,\ p_c\ne p_d
  \quad\Longrightarrow\quad
  r_c\le |c-d|-2.
}
\]

In particular,
\[
  r_c<|c-d|.
\]

This is a purely algebraic obstruction: two different offsets can share the
same quotient only if the center-distance is bounded by their fixed offset
difference.

## 3. Consequence for the initial offset sets

For both initial offset sets,
\[
  \mathcal C_{\rm even}
  =
  \{1,5,17,25,49,65,101,121\},
\]
\[
  \mathcal C_{\rm odd}
  =
  \{2,4,16,26,50,64,100,122\},
\]
the largest possible offset difference is
\[
  D=120.
\]

Therefore, if two distinct offsets in either set share the same quotient
\[
  e_c=e_d,
\]
then the equal quotient obstruction forces
\[
  r_c<120.
\]

But the square-root barrier gives, for \(A>122\),
\[
  r_c\ge R(A)
  =
  \left\lceil
    \frac{-1+\sqrt{1+4(A-122)}}{2}
  \right\rceil.
\]

Thus if
\[
  R(A)>120,
\]
no two distinct initial offsets can have the same quotient.

The inequality
\[
  R(A)>120
\]
holds for
\[
  A\ge14643.
\]
Since
\[
  A=3m,
\]
this is
\[
  m\ge4881.
\]

Hence:
\[
\boxed{
  m\ge4881
  \quad\Longrightarrow\quad
  e_c\ne e_d
  \text{ for all distinct initial offsets }c,d
}
\]
inside the clean strong gate.

## 4. Unequal quotient compatibility

For
\[
  e_c\ne e_d,
\]
the pair equation remains a genuine quadratic:
\[
  (e_d-e_c)r_c^2
  -2e_chr_c
  +e_dc-e_c(h^2+d)-e_ce_dh
  =0.
\]

Therefore the discriminant
\[
\Delta_{c,d}
=
4e_c^2h^2
-4(e_d-e_c)
  \bigl(e_dc-e_c(h^2+d)-e_ce_dh\bigr)
\]
must be a square.

Equivalently,
\[
\boxed{
  e_c^2h^2
  -(e_d-e_c)
  \bigl(e_dc-e_c(h^2+d)-e_ce_dh\bigr)
  \text{ is a square.}
}
\]

This gives the next exact elimination target: for the eight offsets, one
must choose eight pairwise distinct quotients \(e_c\) and eight distances
\(r_c\), so that for every pair the nonzero difference
\[
  h_{c,d}=r_d-r_c
\]
satisfies this quadratic square condition while all centers remain equal to
the same
\[
  A=3m.
\]

## 5. Clean strong-gate consequence

A clean strong-gate counterexample with
\[
  m\ge4881
\]
must satisfy all of the following:

1. the eight prime labels \(p_c\) are distinct;
2. the eight quotients \(e_c\) are distinct;
3. every pair of offsets satisfies the quadratic compatibility equation;
4. every unequal-quotient pair satisfies the discriminant-square condition.

This does not yet close Legendre.  It is a stronger exact obstruction than
the previous factor-gap system: the eight offsets cannot merely have eight
prime quotient representations; those representations must be pairwise
compatible through a rigid quadratic relation.
