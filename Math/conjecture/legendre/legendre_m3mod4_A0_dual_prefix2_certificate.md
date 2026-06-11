# A0 Dual Two-Value Prefix Certificate

This note strengthens the modulo-\(23\) A0 dual boundary certificate.

It closes the complete A0 structural prefix obtained by taking the first two
available lower quotients for each A0 offset after the dual collapses.

## 1. Prefix after the dual collapses

The surviving A0 semigroups are:
\[
\begin{array}{c|c}
  c & \text{surviving lower quotients}\\
  \hline
  4,100 & 2\mathcal S_4\\
  16 & 8\mathcal S_4\cup16\mathcal S_4\\
  64 & 8\mathcal S_4\cup32\mathcal S_4\cup64\mathcal S_4.
\end{array}
\]

The first two values in each row are:
\[
\begin{array}{c|c}
  c & \text{first two values}\\
  \hline
  4 & 2,\ 10\\
  100 & 2,\ 10\\
  16 & 8,\ 16\\
  64 & 8,\ 32.
\end{array}
\]

The four quotients must be pairwise distinct.  Therefore there are exactly
six possible A0 assignments in this two-value prefix.

## 2. Certificate language

For a prime \(p\), define
\[
  M_p(c,f)
  =
  \{m\bmod p:\ f^2+6mf-c\text{ is a square modulo }p\}.
\]

An assignment
\[
  (c_i,f_i)_{i=1}^4
\]
has no integral point if for some prime \(p\),
\[
\boxed{
  \bigcap_i M_p(c_i,f_i)=\varnothing.
}
\]

## 3. The six assignments

The complete two-value A0 prefix is killed as follows:

\[
\begin{array}{c|c|c|c|c}
  c=4 & c=100 & c=16 & c=64 & \text{killing prime}\\
  \hline
  2 & 10 & 8  & 32 & 7\\
  2 & 10 & 16 & 8  & 13\\
  2 & 10 & 16 & 32 & 13\\
  10 & 2 & 8  & 32 & 5\\
  10 & 2 & 16 & 8  & 23\\
  10 & 2 & 16 & 32 & 17.
\end{array}
\]

Each entry means that the intersection of the four corresponding local
sets \(M_p(c,f)\) is empty for the listed prime \(p\).

## 4. Consequence

The complete A0 dual two-value prefix has no integral point:
\[
\boxed{
  \text{first two structural A0 values in every row}
  \quad\Longrightarrow\quad
  \text{no hard-branch point.}
}
\]

Any remaining hard-branch counterexample must therefore use at least one A0
lower quotient beyond this prefix:
\[
\boxed{
  c=4,100:\ f\ge26
  \quad\text{or}\quad
  c=16:\ f\ge40
  \quad\text{or}\quad
  c=64:\ f\ge40,
}
\]
in the corresponding structural semigroup order.
