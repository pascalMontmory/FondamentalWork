# \(m\equiv3\pmod4\) Rank Weights 0--30 Certificate

This note records a deeper finite certificate for the hard
\(m\equiv3\pmod4\) rank game.

It does not prove Legendre.  It proves a precise obstruction:

\[
\boxed{
  \text{no hard-branch rank family of weight }0\le w\le30
  \text{ has an integral point.}
}
\]

Thus any remaining clean-gate counterexample in this branch must lie at
rank weight
\[
\boxed{
  w=a+b+c\ge31.
}
\]

## 1. Exact verifier

Added the deterministic verifier
\[
  \texttt{Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py}.
\]

For each rank family \(F(a,b,c)\), it builds the finite assignment set and
checks the exact local conditions
\[
  M_\ell(c,f)
  =
  \{m\bmod\ell:\ f^2+6mf-c\text{ is a square modulo }\ell\}.
\]

The primes used are only
\[
\boxed{
  5,\ 7,\ 11,\ 13,\ 17.
}
\]

The word `zero` in the output means that the modulo \(7\) zero-quotient
filter already kills the family before any additional prime is needed:
\[
  7\mid f
  \quad\Longrightarrow\quad
  c\in\{26,122\}.
\]

## 2. Certificate summary

Running
\[
  \texttt{python3 Math/conjecture/legendre/tools/m3mod4\_rank\_certificate.py --max-weight 30}
\]
returns:

\[
\begin{array}{c|c|c}
w & \#\text{families} & \text{killing certificate counts}\\
\hline
0 & 1 & 11:1\\
1 & 3 & 11:2,\ 5:1\\
2 & 6 & 11:1,\ 17:1,\ 5:2,\ 7:2\\
3 & 10 & 11:3,\ 13:1,\ 17:1,\ 5:4,\ 7:1\\
4 & 15 & 11:5,\ 5:7,\ 7:2,\ \mathrm{zero}:1\\
5 & 21 & 11:6,\ 13:1,\ 17:1,\ 5:8,\ 7:3,\ \mathrm{zero}:2\\
6 & 28 & 11:8,\ 13:3,\ 5:11,\ 7:3,\ \mathrm{zero}:3\\
7 & 36 & 11:6,\ 13:3,\ 17:1,\ 5:13,\ 7:9,\ \mathrm{zero}:4\\
8 & 45 & 11:14,\ 13:4,\ 5:16,\ 7:6,\ \mathrm{zero}:5\\
9 & 55 & 11:13,\ 13:5,\ 17:1,\ 5:21,\ 7:9,\ \mathrm{zero}:6\\
10 & 66 & 11:19,\ 13:4,\ 17:2,\ 5:23,\ 7:11,\ \mathrm{zero}:7\\
11 & 78 & 11:20,\ 13:4,\ 17:2,\ 5:28,\ 7:16,\ \mathrm{zero}:8\\
12 & 91 & 11:14,\ 13:10,\ 17:2,\ 5:32,\ 7:24,\ \mathrm{zero}:9\\
13 & 105 & 11:27,\ 13:8,\ 5:36,\ 7:24,\ \mathrm{zero}:10\\
14 & 120 & 11:22,\ 13:10,\ 17:2,\ 5:44,\ 7:31,\ \mathrm{zero}:11\\
15 & 136 & 11:27,\ 13:15,\ 5:49,\ 7:32,\ \mathrm{zero}:13\\
16 & 153 & 11:29,\ 13:15,\ 17:1,\ 5:55,\ 7:38,\ \mathrm{zero}:15\\
17 & 171 & 11:29,\ 13:19,\ 17:1,\ 5:61,\ 7:44,\ \mathrm{zero}:17\\
18 & 190 & 11:41,\ 13:17,\ 17:1,\ 5:67,\ 7:45,\ \mathrm{zero}:19\\
19 & 210 & 11:36,\ 13:20,\ 17:1,\ 5:78,\ 7:54,\ \mathrm{zero}:21\\
20 & 231 & 11:38,\ 13:21,\ 17:2,\ 5:88,\ 7:59,\ \mathrm{zero}:23\\
21 & 253 & 11:45,\ 13:19,\ 5:97,\ 7:67,\ \mathrm{zero}:25\\
22 & 276 & 11:45,\ 13:18,\ 17:1,\ 5:103,\ 7:81,\ \mathrm{zero}:28\\
23 & 300 & 11:56,\ 13:22,\ 17:3,\ 5:111,\ 7:77,\ \mathrm{zero}:31\\
24 & 325 & 11:54,\ 13:25,\ 17:1,\ 5:124,\ 7:87,\ \mathrm{zero}:34\\
25 & 351 & 11:63,\ 13:28,\ 17:3,\ 5:135,\ 7:84,\ \mathrm{zero}:38\\
26 & 378 & 11:68,\ 13:30,\ 17:2,\ 5:145,\ 7:91,\ \mathrm{zero}:42\\
27 & 406 & 11:60,\ 13:37,\ 17:2,\ 5:151,\ 7:110,\ \mathrm{zero}:46\\
28 & 435 & 11:74,\ 13:34,\ 17:2,\ 5:161,\ 7:114,\ \mathrm{zero}:50\\
29 & 465 & 11:74,\ 13:35,\ 17:2,\ 5:178,\ 7:122,\ \mathrm{zero}:54\\
30 & 496 & 11:81,\ 13:36,\ 17:4,\ 5:189,\ 7:128,\ \mathrm{zero}:58
\end{array}
\]

The final line of the verifier is:
\[
  \texttt{certificate: all weights 0..30 closed}.
\]

## 3. Mathematical meaning

The hard branch has moved from:

\[
  \text{kill one component}
\]

to:

\[
  \text{kill every rank family up to weight }30.
\]

Equivalently, any remaining hard-branch clean-gate counterexample must push
the rank coordinates at least \(31\) steps beyond the lifted boundary.

This is not likely to be a natural analytic state.  It suggests that the
modular obstruction is periodic and should close the entire rank game.

## 4. New closure target

The target is now precise:

\[
\boxed{
  \text{prove that the finite modular automaton kills all rank triples }
  (a,b,c).
}
\]

The verifier already proves this for
\[
  a+b+c\le30.
\]

To turn this into a proof of the hard \(m\equiv3\pmod4\) branch, one must
prove that the automaton is periodic in the rank variables and then check
one full period, or find a monotone descent showing that any survivor of
weight \(>30\) descends to a smaller surviving weight.

The computational evidence here is not used as probability.  It identifies
the exact finite proof object that remains:

\[
\boxed{
  \text{periodicity or descent for the rank-certificate automaton.}
}
\]
