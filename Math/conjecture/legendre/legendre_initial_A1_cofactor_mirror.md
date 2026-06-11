# Initial A1 Cofactor Mirror

This note applies the complementary-factor mirror to A1.

Unlike the A0 mirror, the A1 result is uniform in the parity of \(m\):
\[
\boxed{
  \mathrm{A1}:\qquad e\equiv6\pmod{12}.
}
\]

This is a substantial strengthening of the previous A1 condition
\[
  e\equiv0\pmod6.
\]

## 1. A1 centered factorization

For an A1 offset
\[
  c=y^2+1,
\]
the centered factorization is
\[
  A^2+y^2+1=(A-r)(A+r+e).
\]

Let
\[
  p=A-r,\qquad Q=A+r+e.
\]

Then
\[
  Q-p=2r+e.
\]

All initial A1 values are odd, so both factors are odd.  Hence \(p,Q\) are
odd.

## 2. Parity of \(A1\) coordinates

In a complete A-block, the A1 coordinate has the same parity as \(A\).

Therefore:

- if \(m\) is even, then \(A\) and \(y\) are even;
- if \(m\) is odd, then \(A\) and \(y\) are odd.

Thus
\[
  A^2+y^2+1
  \equiv
  \begin{cases}
    1\pmod4, & m\text{ even},\\
    3\pmod4, & m\text{ odd}.
  \end{cases}
\]

## 3. Even \(m\)

If \(m\) is even, then \(A\) is even and the A1 coordinate \(y\) is even.
Thus
\[
  A^2+y^2+1\equiv1\pmod4.
\]

Since \(pQ\equiv1\pmod4\) and \(p,Q\) are odd, the two factors have the same
class modulo \(4\):
\[
  Q\equiv p\pmod4.
\]

Hence
\[
  Q-p=2r+e\equiv0\pmod4.
\]

Because \(A\) is even and \(p=A-r\) is odd, \(r\) is odd.  Therefore
\[
  2r\equiv2\pmod4.
\]

So
\[
\boxed{
  e\equiv2\pmod4.
}
\]

## 4. Odd \(m\)

If \(m\) is odd, then \(A\) and the A1 coordinate \(y\) are odd.  Thus
\[
  A^2+y^2+1\equiv3\pmod4.
\]

Since \(pQ\equiv3\pmod4\), the two odd factors have opposite classes modulo
\[
  4.
\]

Therefore
\[
  Q-p\equiv2\pmod4.
\]

Because \(A\) is odd and \(p=A-r\) is odd, \(r\) is even.  Hence
\[
  2r\equiv0\pmod4.
\]

So again
\[
\boxed{
  e\equiv2\pmod4.
}
\]

## 5. Uniform A1 quotient class

The mod-\(6\) quotient lattice gave
\[
  \mathrm{A1}:\qquad e\equiv0\pmod6.
\]

Together with
\[
  e\equiv2\pmod4,
\]
this gives the uniform class
\[
\boxed{
  \mathrm{A1}:\qquad e\equiv6\pmod{12}.
}
\]

Thus the four A1 quotients are distinct positive integers in one residue
class:
\[
  6,\ 18,\ 30,\ 42,\dots.
\]

Their ordered minima are therefore
\[
\boxed{
  6,\ 18,\ 30,\ 42.
}
\]

## 6. Combined cofactor quotient skeletons

Combining the A1 mirror with the corrected A0 mirror gives two parity
branches.

### Even \(m\)

A0 quotients lie in
\[
  2,\ 10\pmod{12},
\]
with four minima
\[
  2,\ 10,\ 14,\ 22.
\]

A1 quotients lie in
\[
  6\pmod{12},
\]
with four minima
\[
  6,\ 18,\ 30,\ 42.
\]

Therefore
\[
\boxed{
  M^{\mathrm{even},\mathrm{cof}}
  =
  (2,6,10,14,18,22,30,42).
}
\]

### Odd \(m\)

A0 quotients lie in
\[
  4,\ 8\pmod{12},
\]
with four minima
\[
  4,\ 8,\ 16,\ 20.
\]

A1 quotients again have minima
\[
  6,\ 18,\ 30,\ 42.
\]

Therefore
\[
\boxed{
  M^{\mathrm{odd},\mathrm{cof}}
  =
  (4,6,8,16,18,20,30,42).
}
\]

## 7. Closure significance

This is stronger than all previous quotient skeletons.  In particular, the
largest quotient-rank lower bound becomes
\[
  e_{(8)}\ge42,
\]
not \(24\).

The largest-rank distance barrier is now asymptotic to
\[
  \sqrt{42A}.
\]

This pushes at least one label below approximately
\[
  A-\sqrt{42A}.
\]

The next exact closure target is to eliminate parity-bifurcated,
cofactor-mirrored certificates with:

1. A0 quotient classes depending on the parity of \(m\);
2. A1 quotient class \(6\bmod12\);
3. fully colored A0/A1 label ladders;
4. colored quotient-rank forcing;
5. Pell synchronization equations.

This is the first quotient skeleton that appears rigid enough to plausibly
close the clean strong gate by finite certificate elimination.
