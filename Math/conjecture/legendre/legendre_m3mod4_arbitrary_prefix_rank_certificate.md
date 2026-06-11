# \(m\equiv3\pmod4\) Arbitrary Prefix-Rank Certificate Through \(N=10\)

The periodic boundary automaton is closed, but a hard-branch counterexample
could still skip ranks in a way that is not represented by the boundary
model.

This note attacks that gap directly.

Instead of using the boundary shape
\[
  \{L_{04}[0],L_{04}[1+a]\},
  \{L_{00}[0],L_{00}[1+b]\},
  \{L_1[0],L_1[1],L_1[2],L_1[3+c]\},
\]
we allow arbitrary rank choices from the first \(N\) values of each layer:

\[
  \binom{L_{04}[0:N]}{2},
  \qquad
  \binom{L_{00}[0:N]}{2},
  \qquad
  \binom{L_1[0:N]}{4},
\]
with all ordered assignments to the offsets.

## 1. Exact verifier mode

The verifier
\[
  \texttt{tools/m3mod4\_rank\_certificate.py}
\]
now supports:

\[
  \texttt{--prefix-ranks N}.
\]

For a given \(N\), it checks every ordered assignment:

\[
  N(N-1)\cdot N(N-1)\cdot N(N-1)(N-2)(N-3)
\]
possibilities.

For each assignment it uses the exact local sets
\[
  M_\ell(c,f)
  =
  \{m\bmod\ell:\ f^2+6mf-c\text{ is a square modulo }\ell\}.
\]

The prime set is
\[
\boxed{
  5,\ 7,\ 11,\ 13,\ 17,\ 19,\ 23,\ 29,\ 83.
}
\]

The modulo \(7\) zero-quotient filter is also imposed:
\[
  7\mid f
  \quad\Longrightarrow\quad
  c\in\{26,122\}.
\]

## 2. Results

The verifier was optimized by precomputing layer masks.  This allows the
\(N=10\) certificate below without changing the mathematical certificate
language.

### Prefix \(N=7\)

\[
  1\,481\,760
\]
ordered assignments are checked.

The verifier returns:

\[
\begin{array}{c|c}
  \text{killer} & \#\\
  \hline
  5 & 695656\\
  7 & 53187\\
  11 & 6719\\
  13 & 347\\
  17 & 84\\
  19 & 3\\
  23 & 3\\
  29 & 1\\
  \mathrm{zero} & 725760
\end{array}
\]

and:
\[
  \texttt{certificate: all arbitrary assignments from first 7 ranks closed}.
\]

### Prefix \(N=8\)

\[
  5\,268\,480
\]
ordered assignments are checked.

The verifier returns:

\[
\begin{array}{c|c}
  \text{killer} & \#\\
  \hline
  5 & 2778191\\
  7 & 167371\\
  11 & 17043\\
  13 & 752\\
  17 & 141\\
  19 & 18\\
  23 & 3\\
  29 & 1\\
  \mathrm{zero} & 2304960
\end{array}
\]

and:
\[
  \texttt{certificate: all arbitrary assignments from first 8 ranks closed}.
\]

### Prefix \(N=9\)

\[
  15\,676\,416
\]
ordered assignments are checked.

The verifier returns:

\[
\begin{array}{c|c}
  \text{killer} & \#\\
  \hline
  5 & 6552671\\
  7 & 495261\\
  11 & 59530\\
  13 & 4041\\
  17 & 835\\
  19 & 92\\
  23 & 13\\
  29 & 4\\
  83 & 1\\
  \mathrm{zero} & 8563968
\end{array}
\]

and:
\[
  \texttt{certificate: all arbitrary assignments from first 9 ranks closed}.
\]

### Prefix \(N=10\)

\[
  40\,824\,000
\]
ordered assignments are checked.

The verifier returns:

\[
\begin{array}{c|c}
  \text{killer} & \#\\
  \hline
  5 & 18371658\\
  7 & 1759247\\
  11 & 177621\\
  13 & 11317\\
  17 & 1259\\
  19 & 143\\
  23 & 20\\
  29 & 8\\
  83 & 7\\
  \mathrm{zero} & 20502720
\end{array}
\]

and:
\[
  \texttt{certificate: all arbitrary assignments from first 10 ranks closed}.
\]

## 3. Consequence

This is stronger than the boundary automaton closure.

The boundary result says that all patterns of the form
\[
  \{0,1+a\},\quad \{0,1+b\},\quad \{0,1,2,3+c\}
\]
are killed.

The prefix-rank certificate says that every arbitrary skipped configuration
inside the first nine values of each layer is killed.

Thus any remaining hard \(m\equiv3\pmod4\) clean-gate counterexample must
use at least one layer rank
\[
\boxed{
  \ge10.
}
\]

Equivalently, after sorting within layers, it must escape beyond the first
ten admissible values in at least one layer.

## 4. New closure target

The remaining descent problem is now sharper:

\[
\boxed{
  \text{prove that any hard-branch counterexample can be reduced into the}
  \text{ first nine ranks of each layer.}
}
\]

or prove a periodic arbitrary-rank automaton that replaces the finite
prefix \(N=9\).

This is no longer a boundary-only statement.  It is a genuine finite
certificate for skipped-rank configurations.
