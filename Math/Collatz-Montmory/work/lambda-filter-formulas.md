# Lambda_B Filter Formulas

> Status: conditional mathematical framework.
>
> Verified here: algebraic identities, normalization formulas, and conditional implications.
>
> Not verified here: existence of the limiting laws, independence from primality, Hardy--Littlewood asymptotics for the filtered sequence, or the numerical value of `C_Montmory`.

## 1. Setup

Let

\[
T(n)=
\begin{cases}
n/2, & n\equiv 0 \pmod 2,\\
(3n+1)/2, & n\equiv 1 \pmod 2,
\end{cases}
\]

be the accelerated Collatz map. For a bound `B`, define the first entrance time and terminal entrance value

\[
\tau_B(n)=\inf\{t\ge 0:T^t(n)\le B\},
\qquad
E_B(n)=T^{\tau_B(n)}(n).
\]

All formulas below are conditional on `tau_B(n)<infty` on the population being studied.

The random-parity drift of `log_2 T(n)` is

\[
-d=\frac{1}{2}(\log_2 3-1)+\frac{1}{2}(-1),
\qquad
 d=1-\frac{\log_2 3}{2}\approx 0.20751874963942196.
\]

Thus the natural centered stopping-time variable is

\[
U_B(n)=\tau_B(n)-\frac{\log_2 n}{d}.
\]

The corresponding compression slope is

\[
\kappa_B(n)=\frac{\log_2 n}{\tau_B(n)}.
\]

For a pair `(p,p+2)`, define

\[
Z_B(p)=\left(\min\{\kappa_B(p),\kappa_B(p+2)\}-d\right)\log_2 p.
\]

This is the normalized pair score used for threshold filtering.

## 2. The moving limit law Lambda_B

For a population `P` (all integers, primes, twin-prime starts, or another explicitly defined population), the proposed limit object is

\[
(E_B(n),U_B(n))\ \Longrightarrow\ \Lambda_B^P
\]

as `n` tends to infinity inside `P`.

For twin-prime starts, the pair version is

\[
\big(E_B(p),E_B(p+2),U_B(p),U_B(p+2)\big)
\Longrightarrow \Lambda_B^{(2)}.
\]

This is the mathematically meaningful object. Fixed-depth inverse-tree cylinders alone have natural density zero; the depth must move with `log n`.

## 3. From Lambda_B to the normalized score

Let `L=log_2 n` and suppose

\[
\tau_B(n)=\frac{L}{d}+u.
\]

Then

\[
\kappa_B(n)=\frac{L}{L/d+u}
= d-\frac{d^2u}{L}+O\left(\frac{u^2}{L^2}\right).
\]

Therefore

\[
(\kappa_B(n)-d)L=-d^2u+O\left(\frac{u^2}{L}\right).
\]

For pairs, if `u_1,u_2` are the two centered stopping-time fluctuations, the limiting score is

\[
z_B(u_1,u_2)=\min\{-d^2u_1,-d^2u_2\}.
\]

Hence a limiting filtered density, if the pair law exists, is

\[
\rho_B(\alpha)
=\Lambda_B^{(2)}\left(\{(e_1,e_2,u_1,u_2):z_B(u_1,u_2)\ge \alpha\}\right).
\]

This gives the formula-first definition of the asymptotic density of the threshold filter `Z_B(p)>=alpha` among twin-prime starts.

## 4. Conditional Hardy--Littlewood coefficient

Let

\[
N_{B,\alpha}(x)=\#\{p\le x:p,p+2\text{ prime and }Z_B(p)\ge \alpha\}.
\]

The clean conditional statement is:

> If Hardy--Littlewood holds for twin primes and the score filter has limiting twin-prime density `rho_B(alpha)` without additional local bias, then
>
> \[
> N_{B,\alpha}(x)\sim 2C_2\rho_B(\alpha)\frac{x}{(\log x)^2}.
> \]

Thus a candidate constant of the form

\[
C_{B,\alpha}=2C_2\rho_B(\alpha)
\]

is not an independent replacement for Hardy--Littlewood. It is a filtered Hardy--Littlewood coefficient.

For the proposed value

\[
C_{\rm Montmory}=0.107983974916,
\]

the required relative density is

\[
\rho_*=rac{C_{\rm Montmory}}{2C_2}
\approx 0.08178598968002706.
\]

Therefore the formula-first threshold is

\[
\alpha_M(B)=\sup\{\alpha:\rho_B(\alpha)\ge \rho_*\}.
\]

This is a definition by a limiting law, not a proof that the law exists.

## 5. Product-law simplification

If the two centered fluctuations become independent and identically distributed with one-point law `Lambda_B^P`, define

\[
\Phi_B(\alpha)=\Lambda_B^P\left(\{(e,u):-d^2u\ge \alpha\}\right).
\]

Then

\[
\rho_B(\alpha)=\Phi_B(\alpha)^2.
\]

In that simplified model, the threshold matching `C_Montmory` solves

\[
\Phi_B(\alpha_M)=\sqrt{\frac{C_{\rm Montmory}}{2C_2}}
\approx 0.28598249856.
\]

This is a strong and testable formula: the single-orbit score tail must stabilize near `28.598%` at the selected threshold if the product-law explanation is correct.

## 6. Local-bias correction

The no-local-bias formula may be too optimistic. A more general filtered Hardy--Littlewood coefficient can be written through local correction factors.

For a prime modulus `q>=3`, define formally

\[
\beta_q(B,\alpha)=
\frac{
\Pr(n\not\equiv 0,-2\pmod q\mid Z_B(n)\ge \alpha)
}{1-2/q}.
\]

If the infinite product converges absolutely, i.e.

\[
\sum_q |\beta_q(B,\alpha)-1|<\infty,
\]

then the conditional coefficient becomes

\[
C_{B,\alpha}^{\rm loc}
=2C_2\rho_B(\alpha)\prod_{q\ge 3}\beta_q(B,\alpha).
\]

This formula separates three effects:

1. the classical twin-prime coefficient `2C_2`;
2. the global Collatz-score tail density `rho_B(alpha)`;
3. the residual modular bias of the filtered population.

If all `beta_q=1`, it reduces to the filtered Hardy--Littlewood coefficient of Section 4.

## 7. Bound-change formula

Let `B_1<B_2`. Once an orbit enters `<=B_2`, the additional time needed to enter `<=B_1` is exactly

\[
\Delta_{B_1,B_2}(n)=\tau_{B_1}(E_{B_2}(n)).
\]

Therefore

\[
\tau_{B_1}(n)=\tau_{B_2}(n)+\tau_{B_1}(E_{B_2}(n)).
\]

At the centered level,

\[
U_{B_1}(n)=U_{B_2}(n)+\tau_{B_1}(E_{B_2}(n)).
\]

So the limiting law, if it exists, transforms by push-forward:

\[
\Lambda_{B_1}^P=(\Psi_{B_1,B_2})_\#\Lambda_{B_2}^P,
\]

where

\[
\Psi_{B_1,B_2}(e,u)=\big(E_{B_1}(e),u+\tau_{B_1}(e)\big).
\]

For the normalized score, the asymptotic correction is

\[
Z_{B_1}(n)=Z_{B_2}(n)-d^2\tau_{B_1}(E_{B_2}(n))+O\left(\frac{(U_{B_2}(n)+\tau_{B_1}(E_{B_2}(n)))^2}{\log_2 n}\right).
\]

This gives a formula-first way to determine whether different bounds belong to the same effective class: their induced score-tail functions differ only by the finite terminal correction above.

## 8. Conditional theorem template

A publishable theorem should be stated in this shape.

**Theorem template.** Fix `B` and `alpha`. Assume:

1. the pair law `Lambda_B^(2)` exists for twin-prime starts;
2. the boundary error in the convergence of the score distribution is `epsilon_B(x,alpha)->0`;
3. the filtered sequence satisfies Hardy--Littlewood with local bias factors `beta_q(B,alpha)` and `sum_q |beta_q-1|<infty`.

Then

\[
N_{B,\alpha}(x)
= C_{B,\alpha}^{\rm loc}\frac{x}{(\log x)^2}
+O\left(\frac{x}{(\log x)^2}\epsilon_B(x,\alpha)\right)
+O\left(\frac{x}{(\log x)^3}\right),
\]

with

\[
C_{B,\alpha}^{\rm loc}
=2C_2\rho_B(\alpha)\prod_{q\ge 3}\beta_q(B,\alpha).
\]

This theorem would not prove the twin-prime conjecture. It would prove that the Collatz-Montmory filter selects a stable subfamily of twin primes with an explicit asymptotic coefficient, conditional on the same level of distribution assumptions required for such a filtered Hardy--Littlewood statement.

## 9. Novelty claim boundary

Do not claim novelty of:

- inverse Collatz trees;
- stopping times;
- terminal values below a fixed bound;
- random-walk drift heuristics for Collatz.

The defensible possible contribution is:

- the moving law `Lambda_B` for `(E_B,U_B)`;
- its bound-change push-forward formula;
- the score-tail coefficient `rho_B(alpha)`;
- the local-bias product `prod beta_q` connecting the Collatz filter to a Hardy--Littlewood coefficient.

## 10. References to secure before diffusion

Minimum bibliography:

- R. Terras, *A stopping time problem on the positive integers*, Acta Arithmetica 30, 1976, 241--252.
- J. C. Lagarias, *The 3x+1 problem: an annotated bibliography (1963--1999)*.
- J. C. Lagarias, *The 3x+1 problem: an annotated bibliography, II (2000--2009)*.
- M. Chamberland, *An update on the 3x+1 problem*.
- G. H. Hardy and J. E. Littlewood, *Some problems of Partitio Numerorum III*, Acta Mathematica, 1923.
- P. T. Bateman and R. A. Horn, *A heuristic asymptotic formula concerning the distribution of prime numbers*, Mathematics of Computation, 1962.
