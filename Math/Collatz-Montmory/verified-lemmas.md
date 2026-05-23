# Collatz-Montmory Verified Lemmas

This file contains only elementary statements that follow directly from the definitions in `definitions.md`. It does not verify any asymptotic Montmory constant.

## Baseline Arithmetic Facts

1. If `n` is a positive even integer, then `n / 2` is a positive integer.
2. If `n` is a positive odd integer, then `3n + 1` is a positive even integer.
3. Therefore the accelerated map

```math
T(n)=
\begin{cases}
n/2, & n\equiv0\pmod2,\\
(3n+1)/2, & n\equiv1\pmod2
\end{cases}
```

sends positive integers to positive integers.

These are elementary properties of the map, not evidence for the full Collatz conjecture or for any Montmory constant.

## Lemma 1: Terminal Entrance Bound

Let `B >= 1`. If `\tau_B(n)` exists and

```math
E_B(n)=T^{\tau_B(n)}(n),
```

then

```math
1\le E_B(n)\le B.
```

### Proof

By definition, `\tau_B(n)` is the first `t >= 0` such that `T^t(n) <= B`. Since the accelerated map preserves positive integers, `T^t(n) >= 1`. Therefore `1 <= E_B(n) <= B`.

## Lemma 2: Exact Stopping-Time Decomposition

Let `B_1 < B_2`. Suppose `\tau_{B_2}(n)` exists and `\tau_{B_1}(E_{B_2}(n))` exists. Define

```math
\Delta_{B_1,B_2}(n)
=
\tau_{B_1}(E_{B_2}(n)).
```

Then

```math
\tau_{B_1}(n)
=
\tau_{B_2}(n)+\Delta_{B_1,B_2}(n).
```

### Proof

After `\tau_{B_2}(n)` steps, the orbit is at `E_{B_2}(n)`. By definition, it takes `\tau_{B_1}(E_{B_2}(n))` further steps to reach `<= B_1`. Concatenating the two orbit segments gives the displayed equality.

## Lemma 3: Terminal Correction As A Push-Forward

Let `\mathcal P` be a finite or asymptotic population for which the empirical entrance measure is defined:

```math
\nu_{B_2,x}^{\mathcal P}(y)
=
\frac{\#\{n\le x:n\in\mathcal P,E_{B_2}(n)=y\}}
{\#\{n\le x:n\in\mathcal P\}}.
```

For `B_1 < B_2`, define

```math
\delta_{B_1,B_2}(y)=\tau_{B_1}(y).
```

Then the empirical law of

```math
\Delta_{B_1,B_2}(n)=\delta_{B_1,B_2}(E_{B_2}(n))
```

is the push-forward measure

```math
(\delta_{B_1,B_2})_*\nu_{B_2,x}^{\mathcal P}.
```

If `\nu_{B_2,x}^{\mathcal P}` converges to a limit `\nu_{B_2}^{\mathcal P}`, then the limiting correction law, when it exists, is

```math
(\delta_{B_1,B_2})_*\nu_{B_2}^{\mathcal P}.
```

### Proof

This is the definition of a push-forward measure: the random variable `E_{B_2}(n)` has law `\nu_{B_2,x}^{\mathcal P}`, and `\Delta_{B_1,B_2}` is obtained by applying `\delta_{B_1,B_2}` to it.

## Lemma 4: Exact Effect On `K_B(n)`

Let

```math
K_B(n)=\frac{\log_2 n}{\tau_B(n)}.
```

Under the assumptions of Lemma 2, write

```math
L=\log_2 n,
\qquad
\tau=\tau_{B_2}(n),
\qquad
\Delta=\Delta_{B_1,B_2}(n).
```

Then

```math
K_{B_1}(n)
=
\frac{L}{\tau+\Delta}
=
K_{B_2}(n)\frac{\tau}{\tau+\Delta},
```

and

```math
K_{B_1}(n)-K_{B_2}(n)
=
-\frac{L\Delta}{\tau(\tau+\Delta)}.
```

### Proof

Substitute Lemma 2 into the definition of `K_{B_1}` and subtract `K_{B_2}=L/\tau`.

## Lemma 5: Pair-Score Bound Under Bound Change

For a pair `(p,p+2)`, set

```math
K_{B,i}=K_B(p+i),
\qquad i\in\{0,2\}.
```

For `B_1 < B_2`, define

```math
R_i=K_{B_2,i}-K_{B_1,i}\ge0.
```

Then

```math
S_{B_2}(p)-\max(R_0,R_2)
\le
S_{B_1}(p)
\le
S_{B_2}(p)-\min(R_0,R_2).
```

### Proof

Since `K_{B_1,i}=K_{B_2,i}-R_i`, one has

```math
S_{B_1}(p)=\min(K_{B_2,0}-R_0,K_{B_2,2}-R_2).
```

Subtracting at most `max(R_0,R_2)` and at least `min(R_0,R_2)` from the two entries gives the bounds.

## Not Verified Here

The following are not verified by these lemmas:

- existence of limiting entrance measures `\nu_B`;
- existence of a limiting law for `Z_B`;
- existence of a stable class of bounds containing `89`;
- independence or decorrelation from the event `p+2` prime;
- the value `C_Montmory = 0.107983974916`;
- the infinitude of twin primes.

These remain research assumptions or conjectural directions unless proven separately.