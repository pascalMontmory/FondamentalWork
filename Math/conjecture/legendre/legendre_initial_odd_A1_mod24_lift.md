# Initial Odd A1 Mod-24 Lift

This note sharpens the A1 cofactor mirror in the odd branch.

For odd \(m\), the A1 quotient class is not merely
\[
  e\equiv6\pmod{12}.
\]
It is forced into one residue class modulo \(24\), determined by
\[
  m\bmod4.
\]

This gives a much stronger quotient skeleton for the odd clean strong gate.

## 1. Reduced A1 equation

Write
\[
  e=2f.
\]

For A1,
\[
  c=y^2+1,
\]
and the reduced quotient pencil is
\[
\boxed{
  u^2=f^2+6mf-(y^2+1),
  \qquad
  u=r+f.
}
\]

The A1 cofactor mirror gives
\[
  e\equiv6\pmod{12},
\]
so
\[
\boxed{
  f\equiv3\pmod6.
}
\]

## 2. Odd branch modulo \(8\)

Assume
\[
  m\text{ is odd}.
\]

Then the initial A1 coordinate \(y\) is odd, so
\[
  y^2\equiv1\pmod8.
\]

Also \(f\) is odd, hence
\[
  f^2\equiv1\pmod8.
\]

Reducing the reduced A1 equation modulo \(8\) gives
\[
  u^2
  \equiv
  1+6mf-(1+1)
  \equiv
  6mf-1
  \pmod8.
\]

The odd square classes modulo \(8\) are only
\[
  1.
\]

Therefore
\[
  6mf-1\equiv1\pmod8,
\]
which is equivalent to
\[
\boxed{
  mf\equiv3\pmod4.
}
\]

Since \(m\) is odd, \(m^{-1}\equiv m\pmod4\).  Hence
\[
\boxed{
  f\equiv3m\pmod4.
}
\]

## 3. A1 quotient class modulo \(24\)

Combine
\[
  f\equiv3\pmod6
\]
with
\[
  f\equiv3m\pmod4.
\]

If
\[
  m\equiv1\pmod4,
\]
then
\[
  f\equiv3\pmod4.
\]
Together with \(f\equiv3\pmod6\), this gives
\[
  f\equiv3\pmod{12}.
\]
Therefore
\[
\boxed{
  m\equiv1\pmod4,\ \mathrm{A1}:
  \qquad
  e=2f\equiv6\pmod{24}.
}
\]

If
\[
  m\equiv3\pmod4,
\]
then
\[
  f\equiv1\pmod4.
\]
Together with \(f\equiv3\pmod6\), this gives
\[
  f\equiv9\pmod{12}.
\]
Therefore
\[
\boxed{
  m\equiv3\pmod4,\ \mathrm{A1}:
  \qquad
  e=2f\equiv18\pmod{24}.
}
\]

## 4. Odd-branch quotient skeletons

For odd \(m\), the corrected A0 cofactor mirror gives
\[
  \mathrm{A0}:\qquad e\equiv4\text{ or }8\pmod{12}.
\]

The four smallest possible A0 quotients are
\[
  4,\ 8,\ 16,\ 20.
\]

### The branch \(m\equiv1\pmod4\)

A1 quotients are distinct positive integers in the class
\[
  6\pmod{24}.
\]

Their four minima are
\[
  6,\ 30,\ 54,\ 78.
\]

Combining with A0 gives
\[
\boxed{
  M^{1\bmod4}
  =
  (4,6,8,16,20,30,54,78).
}
\]

### The branch \(m\equiv3\pmod4\)

A1 quotients are distinct positive integers in the class
\[
  18\pmod{24}.
\]

Their four minima are
\[
  18,\ 42,\ 66,\ 90.
\]

Combining with A0 gives
\[
\boxed{
  M^{3\bmod4}
  =
  (4,8,16,18,20,42,66,90).
}
\]

## 5. Closure significance

The previous A1 cofactor mirror only gave
\[
  e_{(8)}\ge42.
\]

In the odd branch, the mod-\(24\) lift gives:
\[
\boxed{
  m\equiv1\pmod4
  \quad\Longrightarrow\quad
  e_{(8)}\ge78,
}
\]
and
\[
\boxed{
  m\equiv3\pmod4
  \quad\Longrightarrow\quad
  e_{(8)}\ge90.
}
\]

Thus the strongest quotient-rank distance barrier is asymptotic to
\[
  \sqrt{78A}
  \quad\text{or}\quad
  \sqrt{90A}
\]
in the odd clean strong gate.

This is a genuine closure path for the odd branch: the A1 quotients become
so sparse that the first-four-block certificate must contain a prime label
far below \(A\), while still satisfying the fully colored ladder and Pell
synchronization equations.

The next exact target is:

> eliminate the odd clean strong gate separately for
> \(m\equiv1\pmod4\) and \(m\equiv3\pmod4\), using the mod-\(24\) A1
> quotient skeletons.
