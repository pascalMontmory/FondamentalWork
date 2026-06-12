# Global Mobius-Dual Gate

This note records the pivot away from extending the finite initial
A-block classification.

The first-block, four-block, five-block, and six-block notes are exact local
capacity theorems, but increasing the number of initial blocks is not a
closure strategy.  A counterexample could keep paying with new one-shot
prime labels.  The next object must therefore see all complete coprime
blocks at once.

The replacement target is a global Mobius identity.  It is not a simulation:
it is an exact prime-detection equality for the two surviving quadratic
families.

## 1. The two kernels

Fix \(m\ge1\).  Let \(\mathcal Q_{\rm cop}(m)\) be the complete coprime
A-block set, and write
\[
  G_q=9m^2+t_0(q)^2,\qquad
  U_q=9m^2+t_1(q)^2+1.
\]
On \(\mathcal Q_{\rm cop}(m)\),
\[
  \gcd(G_q,U_q)=1.
\]

The eligible A0 small-prime kernel is
\[
  K_0(m)=
  \prod_{\substack{p\le3m\\p\equiv1\pmod4\\p\nmid3m}}p.
\]
The eligible A1 small-prime kernel is
\[
  K_1(m)=
  \prod_{\substack{p\le3m\\p\nmid 9m^2+1\\
  \left(\frac{-9m^2-1}{p}\right)=1}}p.
\]

Because
\[
  9m^2<G_q,U_q<(3m+1)^2,
\]
absence of an eligible small prime divisor is exactly primality in the
corresponding A-channel.

Thus Legendre follows from the existence of \(q\in\mathcal Q_{\rm cop}(m)\)
for which
\[
  \gcd(G_q,K_0(m))=1
  \quad\text{or}\quad
  \gcd(U_q,K_1(m))=1.
\]

## 2. Exact Mobius detectors

For any squarefree kernel \(K\),
\[
  {\bf 1}_{\gcd(F,K)=1}
  =
  \sum_{\substack{d\mid K\\d\mid F}}\mu(d).
\]
Therefore define
\[
  \Delta_0(q)=
  \sum_{\substack{d\mid K_0(m)\\d\mid G_q}}\mu(d),
  \qquad
  \Delta_1(q)=
  \sum_{\substack{e\mid K_1(m)\\e\mid U_q}}\mu(e).
\]
Then
\[
  \Delta_0(q)=1
  \iff
  G_q\text{ has no eligible small divisor},
\]
and
\[
  \Delta_1(q)=1
  \iff
  U_q\text{ has no eligible small divisor}.
\]

On a complete coprime block, the A-channel succeeds precisely when
\[
  \Delta_0(q)+\Delta_1(q)-\Delta_0(q)\Delta_1(q)=1.
\]

Hence a counterexample forces the exact identity
\[
  Z(m)=0,
\]
where
\[
  Z(m)=
  \sum_{q\in\mathcal Q_{\rm cop}(m)}
  \bigl(\Delta_0(q)+\Delta_1(q)-\Delta_0(q)\Delta_1(q)\bigr).
\]

Conversely, if
\[
  Z(m)>0
\]
for every \(m\ge1\), then the combined A-channel produces a prime in every
remaining \(n=3m\) interval governed by this reduction.  Together with the
already closed residual branches, this is the global gate for the current
Legendre route.

Thus the new closure lemma is:
\[
  \boxed{Z(m)>0\quad\text{for every }m\ge1.}
\]

## 3. Divisor-sum form

Introduce the exact root counts
\[
  N_G(d;m)=
  \#\{q\in\mathcal Q_{\rm cop}(m):G_q\equiv0\pmod d\},
\]
\[
  N_U(e;m)=
  \#\{q\in\mathcal Q_{\rm cop}(m):U_q\equiv0\pmod e\},
\]
and
\[
  N_{G,U}(d,e;m)=
  \#\{q\in\mathcal Q_{\rm cop}(m):
  G_q\equiv0\pmod d,\ U_q\equiv0\pmod e\}.
\]
Then
\[
\begin{aligned}
  Z(m)
  &=
  \sum_{d\mid K_0(m)}\mu(d)N_G(d;m)
  +
  \sum_{e\mid K_1(m)}\mu(e)N_U(e;m)\\
  &\quad
  -
  \sum_{\substack{d\mid K_0(m)\\e\mid K_1(m)}}
  \mu(d)\mu(e)N_{G,U}(d,e;m).
\end{aligned}
\]

This is the exact global replacement for finite block escalation.

The local pieces are completely algebraic.  For squarefree \(d\), the roots
of \(G_q\equiv0\pmod d\) are obtained by CRT from the two roots modulo each
prime \(p\mid d\).  The same holds for \(U_q\).  For the mixed term, each
prime contributes either the A0 root set, the A1 root set, both root sets,
or the empty set, depending on whether it divides \(d\), \(e\), or both.

No numerical extrapolation is involved: proving positivity of this single
Mobius expression would close the current Legendre route.

## 4. Why this is a different attack

The initial-block method asks how many distinct labels are forced at the
start.  That can never be the final mechanism by itself, because a
hypothetical counterexample may spend fresh labels on later blocks.

The Mobius-dual gate instead asks whether all labels, across all blocks, can
make the exact inclusion
\[
  \mathcal Q_{\rm cop}(m)\subseteq S_0(m)\cap S_1(m)
\]
hold.  It turns the problem into cancellation and positivity in a single
finite divisor identity.

The next proof task is not to enumerate more \(B_j\).  It is to prove a
rigorous lower bound
\[
  Z(m)>0
\]
by combining:

- exact CRT root counts for \(N_G,N_U,N_{G,U}\);
- the coprime-block condition
  \[
    \gcd(t_1(q),9m^2+1)=1;
  \]
- cancellation in the Mobius sums;
- a controlled remainder after truncating to divisors below a proof
  threshold.

This is the new non-local closure route.
