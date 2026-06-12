# Mobius Root-Count Formula

This note is the first exact attempt to prove positivity of the global
Mobius-dual quantity
\[
  Z(m)>0.
\]

It does not prove the positivity theorem.  Its purpose is to turn the target
into explicit CRT counts and to isolate the precise obstruction that remains.

## 1. Exact block interval

Put
\[
  A=9m^2.
\]
For a complete A-block
\[
  B_q=\{3q+1,3q+2\},
\]
write
\[
  a_q=3q+1,\qquad b_q=3q+2.
\]

The orientation alternates with \(q\).  Since
\[
  a_q\equiv q+1\pmod2,\qquad b_q\equiv q\pmod2,
\]
we have
\[
  t_1(q)=
  \begin{cases}
  b_q,&q\equiv m\pmod2,\\
  a_q,&q\not\equiv m\pmod2,
  \end{cases}
  \qquad
  t_0(q)=\{a_q,b_q\}\setminus\{t_1(q)\}.
\]

Thus the complete block set is the union of two parity intervals:
\[
  I_m=I_{m,0}\cup I_{m,1},
\]
where
\[
  I_{m,\nu}=
  \{q\in\mathbf Z:0\le q\le Q_{m,\nu},\ q\equiv\nu\pmod2\}.
\]
If \(\nu\equiv m\pmod2\), then \(t_1=b_q\), so completeness requires
\[
  b_q^2+1\le6m,
\]
and
\[
  Q_{m,\nu}=
  \left\lfloor\frac{\sqrt{6m-1}-2}{3}\right\rfloor.
\]
If \(\nu\not\equiv m\pmod2\), then \(t_1=a_q\), so completeness is
equivalent to
\[
  b_q^2\le6m,
\]
and
\[
  Q_{m,\nu}=
  \left\lfloor\frac{\sqrt{6m}-2}{3}\right\rfloor.
\]

The coprime block set is
\[
  \mathcal Q_{\rm cop}(m)=
  \{q\in I_m:\gcd(t_1(q),A+1)=1\}.
\]

## 2. Bridge removal by Mobius

Let
\[
  H(m)=\operatorname{rad}(A+1).
\]
On each parity component, \(t_1(q)\) is linear in \(q\), so coprime-block
restriction has the exact Mobius form
\[
  {\bf 1}_{\gcd(t_1(q),A+1)=1}
  =
  \sum_{\substack{h\mid H(m)\\h\mid t_1(q)}}\mu(h).
\]

Therefore every count over \(\mathcal Q_{\rm cop}(m)\) can be written as a
count over the full interval \(I_m\) with one extra linear congruence.

This is important: the bridge removal does not need to be estimated
separately.  It is another squarefree divisor sum.

## 3. Linearized root sets

On the parity component \(I_{m,\nu}\), both \(G_q\) and \(U_q\) are quadratic
polynomials in one linear form:
\[
  G_q=A+(3q+c_0)^2,\qquad
  U_q=A+(3q+c_1)^2+1,
\]
where
\[
  (c_0,c_1)=
  \begin{cases}
  (1,2),&\nu\equiv m\pmod2,\\
  (2,1),&\nu\not\equiv m\pmod2.
  \end{cases}
\]

Let \(d,e,h\) be squarefree, with all prime factors of \(d\) in \(K_0(m)\),
all prime factors of \(e\) in \(K_1(m)\), and all prime factors of \(h\) in
\(H(m)\).  The mixed count is
\[
  N_\nu(d,e,h;m)=
  \#\{q\in I_{m,\nu}:
  G_q\equiv0\pmod d,
  U_q\equiv0\pmod e,
  t_1(q)\equiv0\pmod h\}.
\]

Let
\[
  L=\operatorname{lcm}(2,d,e,h).
\]
The factor \(2\) records the fixed parity \(q\equiv\nu\pmod2\).  The
admissible residue set modulo \(L\) is a CRT product of prime-level root
sets, with the \(2\)-part fixed by the parity condition.  Denote its
cardinality by
\[
  \rho_\nu(d,e,h;m).
\]
Then the exact interval count is
\[
  \boxed{
  N_\nu(d,e,h;m)=
  \rho_\nu(d,e,h;m)\left\lfloor\frac{Q_{m,\nu}+1}{L}\right\rfloor
  +R_\nu(d,e,h;m)
  }
\]
with the sharp deterministic bound
\[
  |R_\nu(d,e,h;m)|\le \rho_\nu(d,e,h;m).
\]

Equivalently,
\[
  N_\nu(d,e,h;m)=
  \frac{\rho_\nu(d,e,h;m)}{L}(Q_{m,\nu}+1)
  +O(\rho_\nu(d,e,h;m)),
\]
where the \(O\)-term is not asymptotic: it means the explicit inequality
above.

## 4. Prime-level factors

For a prime \(p\ge5\), the local factors are:

- if \(p\mid d\), the Gaussian condition contributes the two roots
  \[
    3q+c_0\equiv \pm 3mi_p\pmod p,
    \qquad i_p^2\equiv-1\pmod p;
  \]
- if \(p\mid e\), the A1 condition contributes the two roots
  \[
    3q+c_1\equiv \pm s_p\pmod p,
    \qquad s_p^2\equiv-A-1\pmod p;
  \]
- if \(p\mid h\), the bridge-removal condition contributes the single root
  \[
    3q+c_1\equiv0\pmod p.
  \]

If two or three conditions occur at the same prime, the local factor is the
intersection of the corresponding root sets.  In particular,
\[
  0\le \rho_{\nu,p}(d,e,h;m)\le4,
\]
and
\[
  \rho_\nu(d,e,h;m)=\prod_{p\mid L}\rho_{\nu,p}(d,e,h;m).
\]

This gives a completely explicit CRT formula for every term in \(Z(m)\).

## 5. Expanded form of \(Z(m)\)

The coprime-restricted detector can now be written over the full interval:
\[
\begin{aligned}
  Z(m)
  =
  \sum_{\nu=0}^1\sum_{q\in I_{m,\nu}}
  \sum_{\substack{h\mid H(m)\\h\mid t_1(q)}}\mu(h)
  \bigl(\Delta_0(q)+\Delta_1(q)-\Delta_0(q)\Delta_1(q)\bigr).
\end{aligned}
\]

After expanding \(\Delta_0,\Delta_1\), every term is a count
\(N_\nu(d,e,h;m)\).
Thus
\[
\begin{aligned}
  Z(m)
  &=
  \sum_{\nu=0}^1
  \sum_{h\mid H}\mu(h)
  \sum_{d\mid K_0}\mu(d)N_\nu(d,1,h;m)\\
  &\quad+
  \sum_{\nu=0}^1
  \sum_{h\mid H}\mu(h)
  \sum_{e\mid K_1}\mu(e)N_\nu(1,e,h;m)\\
  &\quad-
  \sum_{\nu=0}^1
  \sum_{h\mid H}\mu(h)
  \sum_{d\mid K_0}\sum_{e\mid K_1}
  \mu(d)\mu(e)N_\nu(d,e,h;m).
\end{aligned}
\]

Substituting the exact interval formula gives
\[
  Z(m)=
  \sum_{\nu=0}^1(Q_{m,\nu}+1)\mathfrak S_\nu(m)+\mathfrak R(m),
\]
where the formal singular coefficient is
\[
\begin{aligned}
  \mathfrak S_\nu(m)
  &=
  \sum_{h\mid H}\mu(h)
  \sum_{d\mid K_0}\mu(d)
  \frac{\rho_\nu(d,1,h;m)}{\operatorname{lcm}(2,d,h)}\\
  &\quad+
  \sum_{h\mid H}\mu(h)
  \sum_{e\mid K_1}\mu(e)
  \frac{\rho_\nu(1,e,h;m)}{\operatorname{lcm}(2,e,h)}\\
  &\quad-
  \sum_{h\mid H}\mu(h)
  \sum_{d\mid K_0}\sum_{e\mid K_1}
  \mu(d)\mu(e)
  \frac{\rho_\nu(d,e,h;m)}{\operatorname{lcm}(2,d,e,h)}.
\end{aligned}
\]

and the exact remainder satisfies
\[
\begin{aligned}
  |\mathfrak R(m)|
  &\le
  \sum_{\nu=0}^1
  \sum_{h\mid H}
  \sum_{d\mid K_0}\rho_\nu(d,1,h;m)\\
  &\quad+
  \sum_{\nu=0}^1
  \sum_{h\mid H}
  \sum_{e\mid K_1}\rho_\nu(1,e,h;m)\\
  &\quad+
  \sum_{\nu=0}^1
  \sum_{h\mid H}
  \sum_{d\mid K_0}\sum_{e\mid K_1}\rho_\nu(d,e,h;m).
\end{aligned}
\]

This is an exact theorem, not a heuristic.

## 6. The obstruction

The formula shows why the untruncated full Mobius expansion does not
immediately prove positivity.

The interval length is only
\[
  Q_m+1\asymp\sqrt m,
\]
whereas the kernels \(K_0(m)\) and \(K_1(m)\) contain primes up to \(3m\).
For divisors
\[
  L=\operatorname{lcm}(d,e,h)>Q_m+1,
\]
the count \(N(d,e,h;m)\) is either \(0\) or a small boundary number, and the
main term
\[
  \frac{\rho(d,e,h;m)}{L}(Q_m+1)
\]
is too small to control the exact remainder.

Therefore positivity of \(Z(m)\) cannot follow from the full CRT main term
alone.  One needs a parity-breaking certificate:

> find a truncation and weights for which the positive part of the Mobius
> identity dominates the boundary remainders, while still detecting
> primality rather than only almost-primality.

This is the precise global obstruction.  It is the same structural wall as
the sieve parity problem, now expressed in the exact A-block coordinates.

## 7. Next exact target

The next useful theorem is not another expansion.  It is a weighted
positivity certificate:

Find finitely supported coefficients
\[
  \lambda_{d,e,h}(m)
\]
such that the identity
\[
  W(m)=
  \sum_{q\in I_m}
  \sum_{d,e,h}\lambda_{d,e,h}(m)
  {\bf 1}_{d\mid G_q}{\bf 1}_{e\mid U_q}{\bf 1}_{h\mid t_1(q)}
\]
satisfies both:

1. \(W(m)>0\) by exact CRT root-count estimates;
2. \(W(m)>0\) implies
   \[
     Z(m)>0.
   \]

Such a certificate would be a genuine parity-breaking proof for the current
Legendre route.  Without it, the Mobius identity is exact but not yet a
proof.
