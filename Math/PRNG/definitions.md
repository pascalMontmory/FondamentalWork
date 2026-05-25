# PRNG Definitions

This file fixes neutral notation for PRNG work. It does not claim that any concrete generator is secure, random, or statistically adequate.

## Generator Model

A deterministic PRNG instance is a tuple

```text
G = (S, P, A, T, O, U)
```

where:

- `S` is the state space;
- `P` is the parameter space;
- `A` is the output alphabet, usually fixed-width machine words;
- `T_p: S -> S` is the state transition for parameter value `p in P`;
- `O_p: S -> A` is the output map;
- `U: A -> [0,1)` maps output words to Monte Carlo uniforms.

Given an initial seed `s_0 in S` and a parameter value `p`, the generated stream is

```text
s_{t+1} = T_p(s_t)
x_t = O_p(s_t)
u_t = U(x_t)
```

For a finite horizon `n`, write:

```text
X_n(p,s) = (x_0, ..., x_{n-1})
U_n(p,s) = (u_0, ..., u_{n-1})
```

All empirical claims in this repository are claims about finite windows unless a theorem explicitly states otherwise.

## Seed Model

A seed model is a probability law or finite test set over a declared seed domain `Seed`, together with an initialization map:

```text
Init_p : Seed -> S
```

The caller seed and the effective internal state do not have to be identical.

Important seed classes:

- `uniform seed`: seed sampled uniformly from a declared finite subset of `S`;
- `structured seed`: seed constrained by an external rule, such as a counter, timestamp, hash digest, or domain-specific encoding;
- `neighbor seed`: seed obtained from a base seed by a declared perturbation operator.

The perturbation operator is written:

```text
N_delta : Seed -> P(Seed)
```

where `P(Seed)` is the power set of `Seed`. Thus `N_delta(s)` is a finite set of seed neighbors.

Standard perturbation rules include:

```text
N_1bit(s) = { s xor 2^j : 0 <= j < w }
N_ham,h(s) = { s xor e : HammingWeight(e) <= h }
N_add,k(s) = { (s + r) mod 2^w : -k <= r <= k }
```

For structured seeds, `N_delta(s)` must state which field is perturbed and how the effective seed is recomputed.

## Parameter Control

A parameter control is a declared subset `C subset P` plus a rule for comparing generator behavior across parameter values.

Typical controls:

- `fixed control`: compare seed perturbations while holding `p` constant;
- `grid control`: compare a finite grid of parameter values;
- `matched control`: compare parameter values chosen to keep one observable fixed while testing another;
- `stress control`: test boundary or degenerate parameter values explicitly.

No parameter is considered validated merely because it passes a single empirical test.

## Affine Markov Diagnostic Model

The CryptoVar API currently exposes a Markov diagnostic vocabulary for an affine generator. In abstract form, this is a recurrence

```text
y_{t+1} = a y_t + b mod m,
u_t = y_t / m,
c_t = floor(q u_t),
```

where:

- `a` is the multiplier;
- `b` is the increment;
- `m` is the modulus;
- `q` is the number of quantization classes;
- `lag` is the transition lag used to build empirical class transitions;
- `antithetic` optionally pairs `u` with `1-u` or an equivalent mirrored variate in downstream Monte Carlo use.

The class process `c_t` can be used to build empirical transition counts, class-frequency diagnostics, and Markov-style mixing observables. These diagnostics are evidence about the declared finite sample and parameter values; they are not automatically cryptographic security claims.

## Observable

An observable is a declared function applied to a finite output window:

```text
Phi : A^n -> R^d
```

or to a finite uniform window:

```text
Phi : [0,1)^n -> R^d.
```

Examples:

- bit frequency;
- block count;
- autocorrelation;
- collision count;
- compression-length proxy;
- rank statistic;
- TestU01 score;
- Monte Carlo estimator for an integrand `f`.

`Phi(G(p,s,n))` is shorthand for applying `Phi` to `X_n(p,s)` or `U_n(p,s)`, depending on the observable. A reproducible claim must specify which one.

## Micro-Uncertainty Observable

For a base seed `s`, perturbation scale `delta`, parameter `p`, output horizon `n`, and observable `Phi`, define the paired response:

```text
Delta_Phi(s, s', p, n) = Phi(G(p, s, n)) - Phi(G(p, s', n))
```

where `s' in N_delta(s)`.

The local median response is:

```text
D_Phi(s, delta, p, n) =
  median_{s' in N_delta(s)} ||Delta_Phi(s, s', p, n)||
```

The local worst-case response is:

```text
W_Phi(s, delta, p, n) =
  max_{s' in N_delta(s)} ||Delta_Phi(s, s', p, n)||
```

This is a sensitivity object. It is not itself a proof of unpredictability or cryptographic security.

## Seed Impact

Seed impact is the measured or proven dependence of an observable on the seed under a fixed generator definition.

A seed-impact claim must state:

- generator and parameter values;
- seed model;
- perturbation rule;
- output horizon;
- observable;
- proof, exact enumeration range, or reproducible empirical protocol.

## Robustness

A parameter setting is called robust for an observable only relative to a declared seed model, perturbation rule, horizon, and acceptance criterion.

Robustness is therefore a conditional statement:

```text
robust(G, p, seed_model, perturbation, observable, horizon, criterion).
```

Changing any component creates a new claim.

## Audit Proof

An audit proof is a hash commitment to a canonicalized bundle of inputs, outputs, and audit metadata. It supports replay and tamper detection, but the proof only certifies consistency with the declared implementation and parameters. It does not by itself prove that the generator is statistically or cryptographically adequate.
