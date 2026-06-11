# No Finite Local-Modular Closure for Arbitrary Skipped Ranks

This note records a necessary strategic correction.

The boundary-rank automaton is closed.  Arbitrary skipped ranks are closed
through the first ten values of each layer.  But the fully arbitrary
skipped-rank problem cannot be closed by merely adding finitely many local
square tests.

The reason is structural: once ranks may be chosen freely far enough out in
their residue classes, finite local square constraints can always be
satisfied independently.

## 1. Local square condition

The reduced hard-branch line is
\[
  u^2=f^2+6mf-c.
\]

Fix any finite set of odd primes
\[
  \mathcal P
\]
and impose local square conditions modulo every
\[
  \ell\in\mathcal P.
\]

Set
\[
  m\equiv0\pmod{\ell}
  \qquad(\ell\in\mathcal P).
\]

Then the local condition becomes
\[
\boxed{
  u^2\equiv f^2-c\pmod{\ell}.
}
\]

Thus each row asks only that
\[
  f^2-c
\]
be a square modulo \(\ell\).

## 2. Nonemptiness modulo one prime

For an odd prime \(\ell\), the congruence
\[
  f^2-c\in(\mathbb F_\ell)^2
\]
is equivalent to the existence of \(u\) with
\[
  f^2-u^2=c.
\]

Equivalently,
\[
  (f-u)(f+u)=c.
\]

If
\[
  c\not\equiv0\pmod\ell,
\]
choose any
\[
  t\in\mathbb F_\ell^\times
\]
and set
\[
  f-u=t,\qquad f+u=c/t.
\]

Since \(\ell\) is odd,
\[
  2
\]
is invertible, so
\[
  f=\frac{t+c/t}{2},
  \qquad
  u=\frac{c/t-t}{2}
\]
gives a solution.

If
\[
  c\equiv0\pmod\ell,
\]
then any
\[
  f
\]
works with
\[
  u=\pm f.
\]

Therefore, for every offset \(c\) and every odd prime \(\ell\), the local
admissible set
\[
  \{f\bmod\ell:\ f^2-c\text{ is a square modulo }\ell\}
\]
is nonempty.

## 3. Compatibility with layer lattices

The hard \(m\equiv3\pmod4\) layer lattices are:

\[
\begin{array}{c|c}
  \text{layer} & f\text{-classes}\\
  \hline
  \mathrm{A0},\ x^2\equiv4\pmod{16}
    & f\equiv2,4,10,20\pmod{24}\\
  \mathrm{A0},\ x^2\equiv0\pmod{16}
    & f\equiv8,14,16,22\pmod{24},\quad 7\nmid f\\
  \mathrm{A1}
    & f\equiv9\pmod{12}.
\end{array}
\]

For primes
\[
  \ell\nmid24,
\]
the Chinese remainder theorem allows one to combine:

1. any chosen admissible residue modulo \(\ell\);
2. any chosen layer residue modulo \(24\) or \(12\).

For a finite set \(\mathcal P\), repeat this prime by prime.  CRT gives an
integer \(f\) in the required layer lattice such that
\[
  f^2-c
\]
is a square modulo every
\[
  \ell\in\mathcal P.
\]

The modulo \(7\) zero-filter is also avoidable in the arbitrary skipped-rank
setting: for offsets not equal to \(26,122\), choose a nonzero admissible
residue modulo \(7\).  Such residues exist in the relevant layer lattices.

Finally, the actual ranks can be made distinct by adding multiples of the
full CRT modulus.  Each layer lattice is infinite.

## 4. Consequence

For every finite set of local primes
\[
  \mathcal P,
\]
there exist arbitrarily large skipped ranks such that every row of the hard
\(m\equiv3\pmod4\) system satisfies the local square condition modulo all
\[
  \ell\in\mathcal P
\]
with
\[
  m\equiv0\pmod{\prod_{\ell\in\mathcal P}\ell}.
\]

Therefore:

\[
\boxed{
  \text{no finite collection of independent local square tests can close}
  \text{ the arbitrary skipped-rank problem.}
}
\]

This explains why the prefix-rank certificates can keep climbing without
becoming a proof of the full branch.

## 5. What remains possible

The closure must use information not present in independent local square
tests.  There are only two viable exact routes left:

1. **Pell synchronization.**  Use the pairwise equations
   \[
     f_j u_i^2-f_i u_j^2
     =
     f_if_j(f_i-f_j)-f_jc_i+f_ic_j
   \]
   to link the rows globally.

2. **Rank descent.**  Prove that any skipped-rank solution produces another
   solution in lower ranks, eventually entering the already closed prefix
   range.

The next proof target is therefore not "add more primes".  It is:

\[
\boxed{
  \text{derive a global Pell-synchronization obstruction or descent.}
}
\]

This is the exact remaining obstruction to closing the hard
\(m\equiv3\pmod4\) branch.
