# Initial Quotient Pell Pencil

This note records a change of variables for the clean strong gate.

The previous centered form used distances
\[
  r_c
\]
and quotients
\[
  e_c=\frac{r_c^2+c}{A-r_c}.
\]

The nonstandard move is to make the quotients primary and replace each
centered factorization by a square-line equation in the common center
\[
  A=3m.
\]

## 1. From centered factors to a square line

The centered factor equation is
\[
  c=Ae-r(r+e).
\]

Equivalently,
\[
  e^2+4Ae-4c=(2r+e)^2.
\]

Define
\[
  w=2r+e.
\]

Then every certified offset gives
\[
\boxed{
  w^2=4eA+e^2-4c.
}
\]

Conversely, if
\[
  w^2=4eA+e^2-4c,
  \qquad
  w\equiv e\pmod2,
\]
and
\[
  r=\frac{w-e}{2}>0,
\]
then
\[
  c=Ae-r(r+e).
\]

Thus the clean strong-gate factorization is exactly a square on the affine
line
\[
  4eA+e^2-4c.
\]

## 2. The quotient-local congruence

Because
\[
  A=3m,
\]
the square-line equation implies the quotient-local condition
\[
\boxed{
  w^2\equiv e^2-4c\pmod{12e}.
}
\]

This condition depends only on the offset \(c\) and the quotient \(e\), not
on \(m\).

Therefore an offset \(c\) can use a quotient \(e\) only if
\[
\boxed{
  e^2-4c
  \text{ is a square modulo }12e.
}
\]

This is a quotient-side local sieve.  It is not a numerical search over
centers \(A\); it is a necessary local condition on the certificate itself.

## 3. Odd prime divisors of a quotient

Let \(\ell\) be an odd prime divisor of \(e\).

Reducing
\[
  w^2\equiv e^2-4c\pmod{\ell}
\]
gives
\[
  w^2\equiv -4c\pmod{\ell}.
\]

Hence, if
\[
  \ell\nmid c,
\]
then
\[
\boxed{
  \left(\frac{-c}{\ell}\right)=1.
}
\]

So every odd prime divisor of \(e\), away from the fixed offset \(c\), must
split the quadratic field
\[
  \mathbb Q(\sqrt{-c}).
\]

This is the quotient-side analogue of the Gaussian restriction on prime
labels.  The certificate now has two independent splitting requirements:

- the label prime \(A-r\) must certify \(A^2+c\);
- every non-degenerate odd prime divisor of the quotient \(e\) must split
  according to \(-c\).

## 4. A0 specialization

For A0 offsets,
\[
  c=x^2.
\]

If \(\ell\mid e\) is odd and
\[
  \ell\nmid x,
\]
then
\[
  \left(\frac{-x^2}{\ell}\right)
  =
  \left(\frac{-1}{\ell}\right)
  =
  1.
\]

Therefore
\[
\boxed{
  \ell\equiv1\pmod4
}
\]
for every odd quotient prime \(\ell\mid e\) not dividing the A0 coordinate
\(x\).

Thus an A0 offset forces the quotient \(e\) itself to be almost Gaussian:
outside the coordinate primes and the \(2\)-adic part, its odd prime support
lies in \(1\bmod4\).

This is stronger than using only the label condition
\[
  A-r\equiv1\pmod4.
\]
Both sides of the centered factorization carry Gaussian splitting.

## 5. A1 specialization

For A1 offsets,
\[
  c=y^2+1.
\]

If \(\ell\mid e\) is odd and \(\ell\nmid y^2+1\), then
\[
\boxed{
  \left(\frac{-(y^2+1)}{\ell}\right)=1.
}
\]

Equivalently,
\[
  -1-y^2
\]
must be a quadratic residue modulo every non-degenerate odd prime divisor of
the quotient.

This is not the same as the A1 label condition.  It is a new local
restriction on the hidden cofactor gap.

## 6. Pairwise Pell synchronization

For two offsets \(c_i,c_j\) with quotients \(e_i,e_j\) and square variables
\[
  w_i^2=4e_iA+e_i^2-4c_i,
\]
\[
  w_j^2=4e_jA+e_j^2-4c_j,
\]
eliminating \(A\) gives
\[
\boxed{
  e_jw_i^2-e_iw_j^2
  =
  e_ie_j(e_i-e_j)
  -4(e_jc_i-e_ic_j).
}
\]

This is a Pell-type compatibility equation independent of \(A\).

The clean strong gate therefore produces not eight unrelated square-line
conditions, but one synchronized pencil of \(28\) pairwise Pell equations.

## 7. Reformulated clean strong-gate target

For \(m\ge4881\), a clean strong-gate counterexample must now produce:

1. the eight offsets \(c_i\) from the parity of \(m\);
2. eight distinct positive quotients \(e_i\);
3. eight square variables \(w_i\);
4. the quotient-local congruences
   \[
     w_i^2\equiv e_i^2-4c_i\pmod{12e_i};
   \]
5. the splitting restrictions on every odd prime divisor of every \(e_i\);
6. the \(28\) Pell synchronization equations;
7. the label, layer, and ladder restrictions from the previous notes.

The new exact attack is:

> eliminate the quotient tuple \(e_1,\dots,e_8\) before eliminating the
> center \(A\).

This is a different direction from searching over \(m\).  It attacks the
hidden cofactor gaps.  If the quotient-local sieve and the Pell pencil are
incompatible with the two-layer ladder certificate, the clean strong gate
closes without a center-by-center argument.
