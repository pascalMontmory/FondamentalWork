# A0 Square-Offset Quotient Theorem

This note sharpens the self-residue filter for the A0 offsets in the hard
\(m\equiv3\pmod4\) branch.

The A0 offsets are squares:

\[
  c=x^2,\qquad x\in\{2,4,8,10\}.
\]

For these rows, the self-residue condition
\[
  u^2\equiv-c\pmod f
\]
becomes
\[
\boxed{
  u^2+x^2\equiv0\pmod f.
}
\]

This has an exact prime-power classification.

## 1. Prime-power criterion

Let
\[
  q^\alpha\Vert f.
\]

Write
\[
  \beta=v_q(x).
\]

The congruence
\[
  u^2+x^2\equiv0\pmod{q^\alpha}
\]
is solvable if and only if:

### Odd \(q\)

Either
\[
  \alpha\le2\beta,
\]
or
\[
  q\equiv1\pmod4.
\]

Indeed, if \(\alpha\le2\beta\), choose \(u=0\).  If
\[
  \alpha>2\beta,
\]
write
\[
  x=q^\beta x',
  \qquad
  u=q^\beta v,
  \qquad
  q\nmid x'.
\]
Then the congruence reduces to
\[
  v^2\equiv-(x')^2\pmod{q^{\alpha-2\beta}},
\]
which is equivalent to
\[
  -1
  \text{ being a square modulo }q.
\]
For odd primes this is equivalent to
\[
  q\equiv1\pmod4.
\]

### \(q=2\)

The congruence is solvable if and only if
\[
\boxed{
  \alpha\le2\beta+1.
}
\]

If \(\alpha\le2\beta\), again \(u=0\) works.  If
\[
  \alpha=2\beta+1,
\]
then after dividing by \(2^{2\beta}\) the residual modulus is \(2\), and
\[
  -1\equiv1\pmod2
\]
is a square.  If
\[
  \alpha\ge2\beta+2,
\]
the residual condition requires
\[
  v^2\equiv-1\pmod4,
\]
impossible because squares modulo \(4\) are \(0,1\).

## 2. Consequence for the four A0 offsets

The four A0 square offsets give:

\[
\begin{array}{c|c|c}
  c & x & \text{necessary and sufficient condition on }f\\
  \hline
  4 & 2
    & v_2(f)\le3,\quad\text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  16 & 4
    & v_2(f)\le5,\quad\text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  64 & 8
    & v_2(f)\le7,\quad\text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4\\
  100 & 10
    & v_2(f)\le3,\quad\text{all odd }q\mid f\text{ satisfy }q\equiv1\pmod4.
\end{array}
\]

For \(c=100\), the prime \(5\mid x\), but \(5\equiv1\pmod4\), so the same
odd-prime condition remains.

Thus every A0 quotient is a "sum-of-two-squares" integer, with an
offset-specific \(2\)-adic ceiling.

## 3. Immediate rank consequences

The A0 \(x^2\equiv4\pmod{16}\) layer uses
\[
  f\equiv2,4,10,20\pmod{24}
\]
on offsets
\[
  c=4,\ 100.
\]

Since both \(c=4\) and \(c=100\) impose
\[
  v_2(f)\le3
\]
and no odd prime \(3\bmod4\), many nominal layer ranks disappear
intrinsically.

The A0 \(x^2\equiv0\pmod{16}\) layer uses
\[
  f\equiv8,14,16,22\pmod{24},
  \qquad 7\nmid f,
\]
on offsets
\[
  c=16,\ 64.
\]

The two offsets are no longer symmetric:

\[
\begin{array}{c|c}
  c=16 & v_2(f)\le5\\
  c=64 & v_2(f)\le7.
\end{array}
\]

For example,
\[
  f=64
\]
can pass the A0 square-quotient filter for
\[
  c=64
\]
but not for
\[
  c=16.
\]

This gives a new offset-specific obstruction inside the skipped-rank
problem, unavailable to finite external modular tests.

## 4. Closure use

Any hard \(m\equiv3\pmod4\) counterexample must now satisfy:

1. the prefix-rank certificate;
2. the periodic boundary automaton certificate;
3. the self-residue filter;
4. this A0 square-offset prime-power theorem;
5. the pairwise Pell synchronization equations.

The next descent target becomes sharper:

\[
\boxed{
  \text{a skipped A0 rank with a forbidden prime-power divisor cannot occur;}
}
\]

and if all skipped A0 ranks avoid forbidden divisors, their quotients lie in
a thin multiplicative semigroup of sums of two squares.  This is the first
structural arithmetic restriction strong enough to pair with Pell
synchronization.
