# \(m\equiv3\pmod4\) Periodic Boundary Automaton Closed

This note closes the periodic boundary automaton that arose from the
hard \(m\equiv3\pmod4\) rank game.

It is stronger than the weight-\(0\) through weight-\(30\) certificate:
instead of checking rank weights, it checks the periodic assignment patterns
directly.

## 1. Boundary pattern model

The boundary rank families are encoded by three variable slots:

\[
\begin{array}{c|c}
  \text{slot} & \text{meaning}\\
  \hline
  a & L_{04}[1+a]\\
  b & L_{00}[1+b]\\
  c & L_1[3+c].
\end{array}
\]

The fixed slots are:

\[
  a0=2,\qquad b0=8,\qquad c0=9,\qquad c1=21,\qquad c2=33.
\]

Thus each periodic boundary assignment distributes
\[
  a0,a
\]
over the offsets
\[
  4,100,
\]
distributes
\[
  b0,b
\]
over
\[
  16,64,
\]
and distributes
\[
  c0,c1,c2,c
\]
over
\[
  2,26,50,122.
\]

The modulo \(7\) zero-quotient filter is imposed:
\[
  c1=21
  \quad\text{can only be placed on}\quad
  26\text{ or }122.
\]

This leaves exactly
\[
\boxed{
  48
}
\]
assignment patterns.

## 2. Periods used

For a prime \(\ell\), the variable slots are periodic modulo \(\ell\):

\[
\begin{array}{c|c}
  \text{slot} & \text{period modulo }\ell\\
  \hline
  a & 4\ell\\
  b & 24\ell\quad(\ell\ne7),\qquad 24\quad(\ell=7)\\
  c & \ell.
\end{array}
\]

For each pattern and prime \(\ell\), the verifier checks whether there is an
\[
  m\bmod\ell
\]
for which every fixed slot satisfies
\[
  f^2+6mf-c\in(\mathbb F_\ell)^2
\]
and every variable slot has at least one rank residue in its period
satisfying the same condition.

If no such \(m\bmod\ell\) exists, the prime \(\ell\) kills the pattern
uniformly, for all ranks.

## 3. The missing prime is 83

The previous note showed that
\[
  5,7,11,13,17
\]
do not kill the full periodic automaton.  One pattern survived:

\[
\begin{array}{c|cccccccc}
  \text{offset} & 4 & 100 & 16 & 64 & 2 & 26 & 50 & 122\\
  \hline
  \text{slot} & 2 & a & b & 8 & c & 21 & 33 & 9.
\end{array}
\]

For this pattern, the five-prime automaton allowed
\[
  m\equiv14325\pmod{85085}.
\]

But modulo \(83\), the same pattern has no surviving center residue.

Thus \(83\) is not cosmetic: it is the first extra modulus needed to close
the periodic boundary automaton found here.

## 4. Exact certificate

The verifier
\[
  \texttt{tools/m3mod4\_rank\_certificate.py}
\]
now supports:

\[
  \texttt{--periodic-patterns}.
\]

Running
\[
  \texttt{python3 Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py --periodic-patterns}
\]
returns:

\[
\begin{array}{c|c}
  \text{killer} & \#\text{patterns killed}\\
  \hline
  5  & 33\\
  7  & 3\\
  11 & 4\\
  13 & 5\\
  17 & 2\\
  83 & 1
\end{array}
\]

and ends with:

\[
  \texttt{certificate: all periodic boundary patterns closed}.
\]

Therefore:

\[
\boxed{
  \text{the periodic boundary automaton is closed by }
  \{5,7,11,13,17,83\}.
}
\]

## 5. What is closed, and what is not

This closes the boundary-rank automaton
\[
  F(a,b,c)
  =
  \{L_{04}[0],L_{04}[1+a]\},
  \{L_{00}[0],L_{00}[1+b]\},
  \{L_1[0],L_1[1],L_1[2],L_1[3+c]\}.
\]

It does **not** yet close all possible hard-branch quotient configurations.
The remaining gap is structural:

> show that any hard \(m\equiv3\pmod4\) clean-gate counterexample can be
> reduced to one of these boundary-rank configurations.

Equivalently, one must prove a descent from arbitrary skipped layer ranks to
the boundary model above, or enlarge the automaton to include all skipped
rank subsets.

The next closure target is therefore:

\[
\boxed{
  \text{boundary reduction/descent for the hard quotient rank game.}
}
\]

Once such a descent is proved, this note closes the hard
\(m\equiv3\pmod4\) branch.
