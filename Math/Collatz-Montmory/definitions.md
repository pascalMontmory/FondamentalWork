# Collatz-Montmory Definitions

This file contains the exact objects currently allowed in verified-facing Collatz-Montmory notes. It does not assert the Collatz conjecture, convergence for all integers, or the value of any Montmory constant.

## Classical Collatz Map

For reference, the classical Collatz map on positive integers is

```text
C(n) = n / 2        if n is even
C(n) = 3n + 1      if n is odd
```

## Accelerated Collatz Map

The current Collatz-Montmory stopping-time notes use the accelerated map on positive integers:

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod 2,\\
(3n+1)/2, & n\equiv1\pmod 2.
\end{cases}
```

This map is well-defined from positive integers to positive integers.

## Stopping Time To A Bound

For a bound `B >= 1`, define

```math
\tau_B(n)=\min\{t\ge0:T^t(n)\le B\},
```

when this minimum exists.

For statements involving `\tau_B(n)`, existence of the stopping time is an explicit hypothesis unless `n <= B`, in which case:

```math
\tau_B(n)=0.
```

No global Collatz convergence claim is implied by this definition.

## Terminal Entrance Point

When `\tau_B(n)` exists, define the terminal entrance point:

```math
E_B(n)=T^{\tau_B(n)}(n).
```

Then, by definition:

```math
1\le E_B(n)\le B.
```

## Bound-Correction Function

For two bounds `B_1 < B_2`, define the finite terminal correction function:

```math
\delta_{B_1,B_2}(y)=\tau_{B_1}(y),
\qquad 1\le y\le B_2,
```

whenever the right-hand side exists.

For a trajectory with existing stopping times, define:

```math
\Delta_{B_1,B_2}(n)
=
\delta_{B_1,B_2}(E_{B_2}(n))
=
\tau_{B_1}(T^{\tau_{B_2}(n)}(n)).
```

## Score Objects

For `n` with `\tau_B(n)>0`, define:

```math
K_B(n)=\frac{\log_2 n}{\tau_B(n)}.
```

For a twin-prime candidate pair `(p,p+2)` with both stopping times positive, define:

```math
S_B(p)=\min(K_B(p),K_B(p+2)).
```

The centered score used in work notes is:

```math
Z_B(p)=(S_B(p)-d)\log_2 p,
\qquad
 d=1-\frac12\log_2 3.
```

The definition of `Z_B` is exact. Any claim about its limiting distribution is not verified at this level.

## Required For Any Stronger Montmory Claim

A stronger Montmory claim must state:

- the domain or population being counted;
- the transition map;
- the bound `B` or bound class;
- whether stopping-time existence is assumed or proven in the claimed range;
- the exact limiting statement;
- whether the statement is unconditional, conditional on Hardy-Littlewood, or conditional on a decorrelation hypothesis.

Until those hypotheses are fixed, no asymptotic Collatz-Montmory theorem should be marked as verified.