# \(m\equiv3\pmod4\) Minimal Component Killed Modulo 7

This note eliminates the first boundary component of the hardest odd
quotient skeleton.

It is a genuine exact certificate: no search over \(m\), no heuristic
evidence.  The minimal quotient assignment is incompatible with the reduced
Pell line modulo \(7\).

## 1. Minimal boundary component

In the \(m\equiv3\pmod4\) branch, the sorted quotient skeleton is
\[
  e=(4,8,16,18,28,42,66,90).
\]

Equivalently, with
\[
  e=2f,
\]
the sorted \(f\)-skeleton is
\[
\boxed{
  f=(2,4,8,9,14,21,33,45).
}
\]

The A0 offsets are
\[
  c=4,16,64,100.
\]

The A0 offsets with
\[
  x^2\equiv0\pmod{16}
\]
are exactly
\[
  c=16,\ 64.
\]

In the minimal boundary assignment, these two offsets must receive the two
smallest admissible \(x^2\equiv0\pmod{16}\) \(f\)-values:
\[
\boxed{
  f=8,\ 14.
}
\]

Therefore one of
\[
  c=16,\ 64
\]
must be paired with
\[
\boxed{
  f=14.
}
\]

## 2. Reduced Pell line modulo 7

The reduced Pell line is
\[
  u^2=f^2+6mf-c.
\]

For
\[
  f=14,
\]
reduce modulo \(7\):
\[
  f\equiv0\pmod7.
\]

Hence
\[
  f^2+6mf-c\equiv -c\pmod7,
\]
so the line requires
\[
\boxed{
  u^2\equiv -c\pmod7.
}
\]

The square classes modulo \(7\) are
\[
\boxed{
  0,1,2,4.
}
\]

For the two possible offsets:
\[
  c=16\equiv2\pmod7,
  \qquad
  -c\equiv5\pmod7,
\]
and
\[
  c=64\equiv1\pmod7,
  \qquad
  -c\equiv6\pmod7.
\]

But
\[
  5,6\notin\{0,1,2,4\}.
\]

Thus neither \(c=16\) nor \(c=64\) can be paired with \(f=14\).

## 3. Exact conclusion

The minimal boundary component
\[
  f=(2,4,8,9,14,21,33,45)
\]
has no integral point in the \(m\equiv3\pmod4\) branch.

Equivalently:
\[
\boxed{
  \text{the exact minimal quotient skeleton is killed modulo }7.
}
\]

This does not eliminate the whole \(m\equiv3\pmod4\) skeleton.  It eliminates
the first boundary component and gives the next refinement rule:

> In the \(x^2\equiv0\pmod{16}\) A0 sublayer, any admissible \(f\) paired
> with \(c=16\) or \(c=64\) must avoid the class \(f\equiv0\pmod7\).

For the class
\[
  f\equiv14\pmod{24},
\]
this means
\[
  f=14+24t
\]
requires
\[
  t\not\equiv0\pmod7.
\]

The next component is therefore not the naive minimal one.  The quotient
rank must climb at least once in the \(x^2\equiv0\pmod{16}\) A0 sublayer, or
move to a nonzero \(t\) in the \(14\bmod24\) class.
