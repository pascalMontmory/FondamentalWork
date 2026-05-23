# Verified Bound-Correction Identities

Status: verified elementary identities only  
Date: 2026-05-23

This note records what is mathematically verified about Collatz-Montmory bounds. It does not validate `B=89` as a unique fundamental bound, and it does not validate `C_Montmory`.

## 1. Setup

Use the accelerated Collatz map:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2.
\end{cases}
```

For a bound `B >= 1`, when the minimum exists:

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\}.
```

The terminal entrance point is:

```math
E_B(n)=T^{\tau_B(n)}(n).
```

Then:

```math
1\le E_B(n)\le B.
```

## 2. Exact Bound-Correction Identity

Let:

```math
B_1<B_2.
```

Define:

```math
\Delta_{B_1,B_2}(n)
=
\tau_{B_1}(E_{B_2}(n))
=
\tau_{B_1}(T^{\tau_{B_2}(n)}(n)).
```

Whenever the stopping times exist, one has the exact identity:

```math
\boxed{
\tau_{B_1}(n)=\tau_{B_2}(n)+\Delta_{B_1,B_2}(n)
}
```

This is verified directly from the definitions.

## 3. Correction Law As Push-Forward

For a population `\mathcal P`, define the empirical entrance measure:

```math
\nu_{B,x}^{\mathcal P}(y)
=
\frac{\#\{n\le x:n\in\mathcal P,E_B(n)=y\}}
{\#\{n\le x:n\in\mathcal P\}}.
```

For `B_1<B_2`, define the finite correction function:

```math
\delta_{B_1,B_2}(y)=\tau_{B_1}(y),
\qquad 1\le y\le B_2.
```

Then the empirical law of `\Delta_{B_1,B_2}` is exactly:

```math
\boxed{
\mathcal L_x(\Delta_{B_1,B_2})
=
(\delta_{B_1,B_2})_*\nu_{B_2,x}^{\mathcal P}
}
```

If the entrance measures converge, then the limiting correction law is conditionally:

```math
\mathcal L(\Delta_{B_1,B_2})
=
(\delta_{B_1,B_2})_*\nu_{B_2}^{\mathcal P}.
```

The push-forward identity is verified. The existence of the limiting measure `\nu_{B_2}^{\mathcal P}` is not verified here.

## 4. Exact Effect On The Score `K_B`

Define:

```math
K_B(n)=\frac{\log_2 n}{\tau_B(n)}.
```

Let:

```math
L=\log_2 n,
\qquad
\tau=\tau_{B_2}(n),
\qquad
\Delta=\Delta_{B_1,B_2}(n).
```

Then:

```math
\boxed{
K_{B_1}(n)
=K_{B_2}(n)\frac{\tau}{\tau+\Delta}
}
```

and:

```math
\boxed{
K_{B_1}(n)-K_{B_2}(n)
=-\frac{L\Delta}{\tau(\tau+\Delta)}
}
```

This is exact.

## 5. Conditional First-Order Approximation

Let:

```math
d=1-\frac12\log_2 3.
```

The work notes use the normalized score:

```math
Z_B(n)=(K_B(n)-d)\log_2 n.
```

If one assumes the heuristic stopping-time scale:

```math
\tau_{B_2}(n)=\frac{\log_2 n}{d}+r(n),
```

with an error term small enough relative to `\log_2 n`, then:

```math
Z_{B_1}(n)-Z_{B_2}(n)
=
-d^2\Delta_{B_1,B_2}(n)
+O\left(
\frac{|r(n)|\Delta_{B_1,B_2}(n)+\Delta_{B_1,B_2}(n)^2}{\log_2 n}
\right).
```

This approximation is conditional on the stopping-time scale. It is not an unconditional theorem here.

## 6. Meaning For The Bound `89`

The verified identities support only this cautious statement:

```text
Changing the bound changes the stopping time through an explicit terminal correction.
A bound such as 89 can be studied as a possible representative of a class of bounds
whose terminal corrections preserve the normalized-score tail.
```

They do not prove:

```text
89 is the unique fundamental bound.
```

## 7. Not Verified By This Note

This note does not verify:

- global Collatz convergence;
- existence of limiting entrance measures;
- stability of a bound class containing `89`;
- a limiting law for `Z_B`;
- decorrelation with primality or twin primality;
- `C_Montmory = 0.107983974916`.

Those statements remain conditional or exploratory.