# Resonance Bound Formulas

> Status: exploratory and testable framework.
>
> Verified here: definitions, algebraic normalizations, and the reported finite-range computation.
>
> Not verified here: existence of a limiting resonance law, uniqueness of any center, or special status of `89`.

## 1. Motivation

The previous bound definition

\[
\tau_B(n)=\inf\{t\ge 0:T^t(n)\le B\}
\]

is an entrance-below-bound definition. It does not fully capture the intuitive idea of an integer around which a Collatz trajectory passes or oscillates.

A closer object is a **resonance window** centered at `B`.

## 2. Multiplicative window around a center

Let

\[
T(n)=
\begin{cases}
n/2, & n\equiv 0\pmod 2,\\
(3n+1)/2, & n\equiv 1\pmod 2,
\end{cases}
\]

and let

\[
d=1-\frac{\log_2 3}{2}.
\]

For a center `B` and width `eta>0`, define the multiplicative window

\[
I_{B,\eta}=\{m\in\mathbb N:e^{-\eta}B\le m\le e^{\eta}B\}.
\]

The first passage time into the window is

\[
\tau_{B,\eta}(n)=\inf\{t\ge 0:T^t(n)\in I_{B,\eta}\}.
\]

The first passage value is

\[
P_{B,\eta}(n)=T^{\tau_{B,\eta}(n)}(n).
\]

If the trajectory never enters the window in the tested range, `tau_{B,eta}(n)` is undefined.

## 3. Centered passage time

The random-parity model predicts that reaching scale `B` from scale `n` should take approximately

\[
\frac{\log_2 n-\log_2 B}{d}
\]

accelerated Collatz steps. Therefore define

\[
U_{B,\eta}(n)=
\tau_{B,\eta}(n)-\frac{\log_2 n-\log_2 B}{d}.
\]

This is the window analogue of the Lambda_B centered stopping-time variable.

## 4. Hit rate and residence

For a population `P`, define the empirical hit rate

\[
H_{B,\eta}^{P}(x)=
\frac{\#\{n\le x:n\in P,\ \exists t\ge 0,\ T^t(n)\in I_{B,\eta}\}}
{\#\{n\le x:n\in P\}}.
\]

Define the total residence count

\[
R_{B,\eta}(n)=\#\{t\ge 0:T^t(n)\in I_{B,\eta}\}.
\]

A center is not interesting merely because `H` is large. Many windows are hit frequently by ordinary Collatz descent. The relevant question is whether a population, for example twin-prime starts, is overrepresented relative to controls.

## 5. Resonance ratios

For twin-prime starts and a control population `C`, define

\[
\Omega_{B,\eta}^{\rm twin/C}(x)=
\frac{H_{B,\eta}^{\rm twin}(x)}{H_{B,\eta}^{C}(x)}.
\]

A center-specific arithmetic resonance would require

\[
\Omega_{B,\eta}^{\rm twin/C}(x)\not\to 1
\]

with a stable sign and magnitude as `x` grows.

A log version is often cleaner:

\[
\omega_{B,\eta}^{\rm twin/C}(x)=
\log H_{B,\eta}^{\rm twin}(x)-\log H_{B,\eta}^{C}(x).
\]

Then `omega=0` means no detectable enrichment.

## 6. Resonance-law criterion

A center `B` is a candidate resonance bound for a population `P` if the following empirical laws stabilize:

\[
(P_{B,\eta}(n),U_{B,\eta}(n),R_{B,\eta}(n))
\Longrightarrow
\mathcal R_{B,\eta}^{P}.
\]

For a twin-specific resonance, one also requires separation from controls:

\[
\mathcal R_{B,\eta}^{\rm twin}\ne \mathcal R_{B,\eta}^{\rm control},
\]

or at least a stable nonzero resonance ratio.

This is stronger and more meaningful than saying that `B` is a bound. It asks whether `B` is a statistical center of passage.

## 7. First finite-range test

The script `scripts/evaluate_resonance_bounds.py` tests the formulas above.

Parameters used for this first diagnostic:

- accelerated Collatz map;
- multiplicative width `eta=0.08`;
- centers: `27,31,41,47,55,63,65,73,81,85,89,91,95,97,109,127,171,255`;
- populations: twin-prime starts, prime non-twins, odd sample;
- ranges: `x=10^6` and `x=3*10^6`.

Condensed ranking by closeness to controls at `x=3*10^6`:

| center | twin hit 1e6 | twin hit 3e6 | stability | twin/non-twin 3e6 | twin/odd 3e6 | signal distance |
|---:|---:|---:|---:|---:|---:|---:|
| 41 | 0.783327 | 0.784923 | 0.001595 | 0.999636 | 0.999256 | 0.001108 |
| 81 | 0.750765 | 0.751815 | 0.001050 | 0.998304 | 0.998268 | 0.003428 |
| 85 | 0.673767 | 0.670982 | 0.002784 | 0.996936 | 0.998842 | 0.004222 |
| 27 | 0.478149 | 0.477976 | 0.000173 | 1.005233 | 1.000062 | 0.005295 |
| 47 | 0.824336 | 0.823715 | 0.000621 | 0.997828 | 0.996156 | 0.006016 |
| 89 | 0.637042 | 0.634626 | 0.002416 | 0.996405 | 0.997464 | 0.006131 |
| 65 | 0.740237 | 0.737531 | 0.002706 | 0.995602 | 0.998192 | 0.006206 |
| 63 | 0.722610 | 0.719568 | 0.003042 | 0.994610 | 0.996025 | 0.009365 |
| 95 | 0.764353 | 0.761418 | 0.002935 | 0.995919 | 0.994659 | 0.009422 |
| 97 | 0.762517 | 0.760367 | 0.002150 | 0.995468 | 0.995036 | 0.009496 |
| 55 | 0.792753 | 0.791468 | 0.001285 | 0.993872 | 0.995908 | 0.010221 |
| 127 | 0.751132 | 0.751959 | 0.000826 | 0.994215 | 0.995286 | 0.010499 |
| 91 | 0.707186 | 0.702513 | 0.004673 | 0.994323 | 0.994779 | 0.010898 |
| 255 | 0.773044 | 0.771689 | 0.001355 | 0.993904 | 0.994975 | 0.011121 |
| 31 | 0.396989 | 0.395853 | 0.001135 | 1.007889 | 1.003854 | 0.011743 |
| 109 | 0.563104 | 0.567218 | 0.004113 | 0.996997 | 0.991154 | 0.011849 |
| 171 | 0.642796 | 0.641171 | 0.001625 | 0.995100 | 0.989992 | 0.014908 |
| 73 | 0.603256 | 0.596073 | 0.007183 | 0.990916 | 0.988119 | 0.020965 |

Here `signal distance` is

\[
|\Omega^{\rm twin/non-twin}-1|+|\Omega^{\rm twin/odd}-1|.
\]

## 8. Interpretation

This first passage-window test does **not** support a special twin-prime resonance at `89`.

For `B=89`:

\[
H_{89,0.08}^{\rm twin}(3\cdot 10^6)=0.634626,
\]

but

\[
\Omega_{89,0.08}^{\rm twin/non-twin}(3\cdot 10^6)=0.996405,
\qquad
\Omega_{89,0.08}^{\rm twin/odd}(3\cdot 10^6)=0.997464.
\]

These ratios are close to `1`, meaning that the window around `89` is hit by twin-prime starts at essentially the same rate as by the controls.

Thus `89` may still be a usable terminal-bound representative for the earlier `Lambda_B` framework, but this new **oscillation/passage-center** test does not make it stand out.

## 9. Next formula to test

The hit-rate criterion may be too coarse. The next sharper object is the full law

\[
(P_{B,\eta},U_{B,\eta},R_{B,\eta})
\]

and its distance between populations:

\[
D_{B,\eta}(x)=
\operatorname{TV}(P_{B,\eta}^{\rm twin},P_{B,\eta}^{\rm control})
+
\operatorname{KS}(U_{B,\eta}^{\rm twin},U_{B,\eta}^{\rm control})
+
\operatorname{KS}(R_{B,\eta}^{\rm twin},R_{B,\eta}^{\rm control}).
\]

A serious resonance claim would require `D_{B,eta}(x)` to remain separated from zero and stable across windows. If it tends to zero, the center is not arithmetically special for twin primes.
