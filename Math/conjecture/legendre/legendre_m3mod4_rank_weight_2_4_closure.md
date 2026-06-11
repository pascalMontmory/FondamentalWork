# \(m\equiv3\pmod4\) Rank Weights 2--4 Closed

This note records the first real layer-closure pattern in the hard
\(m\equiv3\pmod4\) quotient game.

The previous notes killed:

1. the lifted boundary
   \[
     f=(2,4,8,9,16,21,33,45);
   \]
2. the complete first escape layer.

Here we close the next three rank weights.

This is not a search over \(n\).  Each entry below is a finite congruence
certificate for the exact Pell lines
\[
  u^2=f^2+6mf-c.
\]

## 1. Rank coordinates

In the hard branch the three ordered layer lists are:

\[
\begin{aligned}
L_{04}&=2,4,10,20,26,28,34,44,50,\dots,\\
L_{00}&=8,16,22,32,38,40,46,62,\dots,\\
L_{1}&=9,21,33,45,57,69,81,93,\dots.
\end{aligned}
\]

Here:

- \(L_{04}\) is the A0 \(x^2\equiv4\pmod{16}\) list for offsets \(4,100\);
- \(L_{00}\) is the A0 \(x^2\equiv0\pmod{16}\) list for offsets \(16,64\),
  after deleting the forbidden \(7\mid f\) values;
- \(L_1\) is the A1 list for offsets \(2,26,50,122\).

The base boundary is
\[
  L_{04}[0],L_{04}[1];
  \qquad
  L_{00}[0],L_{00}[1];
  \qquad
  L_1[0],L_1[1],L_1[2],L_1[3].
\]

For nonnegative integers
\[
  a,b,c,
\]
write \(F(a,b,c)\) for the family
\[
\boxed{
  \{L_{04}[0],L_{04}[1+a]\},
  \quad
  \{L_{00}[0],L_{00}[1+b]\},
  \quad
  \{L_1[0],L_1[1],L_1[2],L_1[3+c]\}.
}
\]

The weight is
\[
  w=a+b+c.
\]

Weight \(0\) is the lifted boundary.  Weight \(1\) is the first escape
layer.  Both are already dead.

## 2. Certificate language

For a prime \(\ell\), define
\[
  M_\ell(c,f)
  =
  \{m\bmod\ell:\ f^2+6mf-c\text{ is a square modulo }\ell\}.
\]

For a fixed rank family \(F(a,b,c)\), one considers all offset-to-\(f\)
matchings respecting:

1. the two A0 sublayers;
2. the A1 layer;
3. the zero-quotient filter
   \[
     7\mid f\Longrightarrow c\in\{26,122\}.
   \]

There are \(48\) matchings after this filter in every listed family except
\((4,0,0)\), which is killed immediately because \(f=28\) is divisible by
\(7\) but belongs to the A0 offsets \(4,100\).

A row
\[
  5:48\to2,\quad 7:2\to0
\]
means:

- modulo \(5\), only \(2\) of the \(48\) matchings have nonempty common
  \(m\bmod5\) intersection;
- modulo \(7\), neither of those \(2\) matchings has nonempty common
  \(m\bmod7\) intersection.

This is a finite proof certificate: each arrow is the intersection of eight
explicit sets \(M_\ell(c,f)\).

## 3. Weight 2 closed

The six weight-\(2\) families are all impossible:

\[
\begin{array}{c|c|c}
  (a,b,c) & F(a,b,c) & \text{certificate}\\
  \hline
  (2,0,0) & 2,20;\ 8,16;\ 9,21,33,45
    & 5:48\to2,\ 7:2\to0\\
  (0,2,0) & 2,4;\ 8,32;\ 9,21,33,45
    & 5:48\to0\\
  (0,0,2) & 2,4;\ 8,16;\ 9,21,33,69
    & 5:48\to4,\ 7:4\to2,\ 11:2\to1,\ 13:1\to1,\ 17:1\to0\\
  (1,1,0) & 2,10;\ 8,22;\ 9,21,33,45
    & 5:48\to0\\
  (1,0,1) & 2,10;\ 8,16;\ 9,21,33,57
    & 5:48\to1,\ 7:1\to0\\
  (0,1,1) & 2,4;\ 8,22;\ 9,21,33,57
    & 5:48\to1,\ 7:1\to1,\ 11:1\to0
\end{array}
\]

Therefore:
\[
\boxed{
  \text{all rank-weight }2\text{ families are impossible.}
}
\]

## 4. Weight 3 closed

The ten weight-\(3\) families are all impossible:

\[
\begin{array}{c|c}
  (a,b,c) & \text{certificate}\\
  \hline
  (0,0,3) & 5:48\to5,\ 7:5\to3,\ 11:3\to1,\ 13:1\to0\\
  (0,1,2) & 5:48\to0\\
  (0,2,1) & 5:48\to1,\ 7:1\to1,\ 11:1\to0\\
  (0,3,0) & 5:48\to0\\
  (1,0,2) & 5:48\to8,\ 7:8\to2,\ 11:2\to1,\ 13:1\to1,\ 17:1\to0\\
  (1,1,1) & 5:48\to1,\ 7:1\to0\\
  (1,2,0) & 5:48\to0\\
  (2,0,1) & 5:48\to1,\ 7:1\to1,\ 11:1\to0\\
  (2,1,0) & 5:48\to0\\
  (3,0,0) & 5:48\to1,\ 7:1\to1,\ 11:1\to0
\end{array}
\]

Therefore:
\[
\boxed{
  \text{all rank-weight }3\text{ families are impossible.}
}
\]

## 5. Weight 4 closed

The fifteen weight-\(4\) families are all impossible:

\[
\begin{array}{c|c}
  (a,b,c) & \text{certificate}\\
  \hline
  (0,0,4) & 5:48\to0\\
  (0,1,3) & 5:48\to1,\ 7:1\to1,\ 11:1\to0\\
  (0,2,2) & 5:48\to0\\
  (0,3,1) & 5:48\to2,\ 7:2\to1,\ 11:1\to0\\
  (0,4,0) & 5:48\to3,\ 7:3\to2,\ 11:2\to0\\
  (1,0,3) & 5:48\to9,\ 7:9\to2,\ 11:2\to0\\
  (1,1,2) & 5:48\to0\\
  (1,2,1) & 5:48\to1,\ 7:1\to0\\
  (1,3,0) & 5:48\to0\\
  (2,0,2) & 5:48\to8,\ 7:8\to0\\
  (2,1,1) & 5:48\to1,\ 7:1\to1,\ 11:1\to0\\
  (2,2,0) & 5:48\to0\\
  (3,0,1) & 5:48\to0\\
  (3,1,0) & 5:48\to0\\
  (4,0,0) & \text{zero-filter: }f=28\text{ on A0 is impossible}
\end{array}
\]

Therefore:
\[
\boxed{
  \text{all rank-weight }4\text{ families are impossible.}
}
\]

## 6. Consequence

Combining the previous notes with this one:

\[
\boxed{
  w=0,1,2,3,4
  \quad\Longrightarrow\quad
  F(a,b,c)\text{ has no integral point.}
}
\]

Thus any remaining \(m\equiv3\pmod4\) clean-gate counterexample must satisfy
\[
\boxed{
  a+b+c\ge5.
}
\]

Equivalently, it must climb at least five rank steps beyond the lifted
boundary.

## 7. What this means for closure

This is the point where the proof route becomes clear.

The modular certificates are not random.  They repeatedly do the same thing:

1. modulo \(5\) destroys most matchings;
2. modulo \(7\) applies the zero-quotient rigidity and often leaves one
   class;
3. modulo \(11,13,17\) kills the remaining class.

The remaining missing theorem is now sharper than a vague "rank cap".

One must prove either:

\[
\boxed{
  a+b+c\le4
  \quad\text{for every hard-branch clean-gate counterexample,}
}
\]

which would close the \(m\equiv3\pmod4\) branch immediately, or a stronger
periodicity theorem:

\[
\boxed{
  \text{every }F(a,b,c)\text{ is killed by the same finite prime set}
  \{5,7,11,13,17,19,23\}.
}
\]

The second route would avoid an analytic rank cap.  It would turn the hard
branch into a finite automaton over the rank residues of
\[
  L_{04},\quad L_{00},\quad L_1.
\]

This is now the best closure candidate: prove periodic modular killing for
all \((a,b,c)\), rather than trying to estimate the quotients analytically.
