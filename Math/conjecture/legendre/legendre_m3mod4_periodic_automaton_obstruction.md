# Obstruction to the First Periodic Automaton Closure

The certificate up to rank weight \(30\) suggested a possible closure of the
hard \(m\equiv3\pmod4\) branch by the five primes
\[
  5,\ 7,\ 11,\ 13,\ 17.
\]

This note records the exact obstruction: these five primes do **not** close
the full periodic rank automaton.

This is not a counterexample to Legendre.  It is a counterexample to the
too-optimistic closure lemma:

> Every rank triple \((a,b,c)\) is killed by the finite automaton using only
> \(5,7,11,13,17\).

That lemma is false.

## 1. The surviving assignment pattern

Use the rank-family notation
\[
  F(a,b,c)
  =
  \{L_{04}[0],L_{04}[1+a]\},
  \{L_{00}[0],L_{00}[1+b]\},
  \{L_1[0],L_1[1],L_1[2],L_1[3+c]\}.
\]

There is a surviving periodic assignment pattern:

\[
\begin{array}{c|cccccccc}
  \text{offset} & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  f\text{-slot} & L_{04}[0] & L_{04}[1+a] &
                  L_{00}[1+b] & L_{00}[0] &
                  L_1[3+c] & L_1[1] & L_1[2] & L_1[0].
\end{array}
\]

Equivalently:
\[
\begin{array}{c|cccccccc}
  \text{offset} & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  \text{fixed/variable} & 2 & a & b & 8 & c & 21 & 33 & 9.
\end{array}
\]

The fixed zero-quotient condition is respected because
\[
  f=21
\]
is attached to
\[
  c=26,
\]
which is one of the two offsets allowed to carry \(7\mid f\).

## 2. The surviving center residue

Modulo
\[
  5\cdot7\cdot11\cdot13\cdot17=85085,
\]
the center parameter \(m\) can lie in the class
\[
\boxed{
  m\equiv14325\pmod{85085}.
}
\]

Its prime residues are:
\[
\begin{array}{c|ccccc}
  \ell & 5 & 7 & 11 & 13 & 17\\
  \hline
  m\bmod\ell & 0 & 3 & 3 & 12 & 11.
\end{array}
\]

For this residue and the assignment pattern above, the finite local
conditions
\[
  f^2+6mf-c\in(\mathbb F_\ell)^2
\]
do not force an empty rank class for the variable slots \(a,b,c\).

Thus the five-prime automaton has at least one periodic survivor.

## 3. Exact consequence

The previous weight-\(0\) through weight-\(30\) certificate remains valid.
What fails is only the proposed extrapolation:

\[
\boxed{
  \{5,7,11,13,17\}
  \text{ alone does not prove periodic killing for all ranks.}
}
\]

Therefore the closure route must be refined.

There are now three exact options:

1. add further primes to kill the survivor pattern;
2. show that this periodic survivor cannot lift to an integral solution of
   the Pell synchronization equations;
3. build a descent from this survivor pattern to a lower rank family already
   killed.

Option 2 is the most mathematical: the survivor only satisfies local square
conditions.  It has not satisfied the pairwise Pell synchronization over
\(\mathbb Z\).

## 4. New target

The next closure target is:

\[
\boxed{
  \text{kill the survivor pattern above by synchronization, not by more}
  \text{ weight climbing.}
}
\]

Concretely, substitute the pattern into the pairwise Pell equations
\[
  f_j u_i^2-f_i u_j^2
  =
  f_if_j(f_i-f_j)-f_jc_i+f_ic_j
\]
and eliminate the three rank variables \(a,b,c\), or find a modulus
\(\ell>17\) that kills the pattern uniformly.

This is now the precise obstruction standing between the rank certificates
and a hard-branch closure.
