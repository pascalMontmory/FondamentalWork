# PRNG Definitions

This file fixes neutral notation for PRNG work. It does not claim that any concrete generator is secure, random, or statistically adequate.

## Generator Model

A deterministic PRNG instance is a tuple

```text
G = (S, P, T, O)
```

where:

- `S` is the state space;
- `P` is the parameter space;
- `T_p: S -> S` is the state transition for parameter value `p in P`;
- `O_p: S -> A` is the output map into an alphabet `A`.

Given an initial seed `s_0 in S` and a parameter value `p`, the generated stream is

```text
x_t = O_p(s_t),    s_{t+1} = T_p(s_t).
```

## Seed Model

A seed model is a probability law or finite test set over `S`.

Important seed classes:

- `uniform seed`: seed sampled uniformly from a declared finite subset of `S`;
- `structured seed`: seed constrained by an external rule, such as a counter, timestamp, hash digest, or domain-specific encoding;
- `neighbor seed`: seed obtained from a base seed by a declared perturbation operator.

The perturbation operator is written `N_delta(s)`. Examples include one-bit flips, Hamming-radius balls, additive offsets, prefix changes, or application-specific micro-changes in encoded seed fields.

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

## Micro-Uncertainty Observable

Let `Phi` be an observable of an output window, for example bit frequency, block count, autocorrelation, collision count, compression length, rank statistic, or test-suite score.

For a base seed `s`, perturbation scale `delta`, parameter `p`, and output horizon `n`, define the micro-uncertainty of `Phi` as the distribution of

```text
Delta_Phi(s, delta, p, n) = Phi(G(p, s, n)) - Phi(G(p, s', n)),
```

where `s'` ranges over `N_delta(s)`.

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
