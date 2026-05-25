# Micro-Uncertainty Program for PRNGs

This note defines a work plan for analyzing seed impact and parameter controls. It is exploratory and should not be cited as a verified result.

## Objective

Build a reproducible framework for answering:

- how small seed changes affect early and long-run output windows;
- whether parameter choices create fragile or stable behavior;
- whether structured seeds behave differently from uniform seeds;
- which claims can be promoted from empirical evidence to exact finite verification or proof.

## Minimal Experiment Record

Every experiment should record:

```text
generator_id:
generator_version:
state_space:
parameter_values:
seed_model:
perturbation_rule:
output_horizon:
observable_list:
sample_size:
command:
expected_output:
status: computational-evidence | exact-enumeration | proof-backed
```

## Seed-Impact Protocol

1. Choose a base seed set `B`.
2. Choose a perturbation operator `N_delta`.
3. For each `s in B`, generate paired streams from `s` and from each `s' in N_delta(s)`.
4. Compute observable deltas `Delta_Phi`.
5. Compare against a control group of independently drawn seeds.
6. Report both central behavior and tail behavior.

Useful first observables:

- bit frequency by window;
- Hamming distance between paired output windows;
- block-frequency deviation;
- lagged autocorrelation;
- collision rate for fixed-size blocks;
- compression length or entropy proxy;
- standard battery score where available.

## Parameter-Control Protocol

1. Declare a finite parameter grid.
2. Hold seed model and perturbation rule constant.
3. Run the same observable set for every parameter value.
4. Add stress cases near degenerate or boundary parameters.
5. Mark any parameter-dependent failure as a first-class result.

## Status Labels

Use these labels consistently:

- `definition`: terminology or object definition only;
- `computational-evidence`: empirical result with reproducible command and expected output;
- `exact-enumeration`: finite exhaustive check with range and command;
- `conditional`: theorem or conclusion dependent on explicit assumptions;
- `conjecture`: plausible but unproven claim;
- `rejected`: negative result or failed candidate.

## Import Path from External API Work

If prior work exists in an API or cryptographic prototype, import it in this order:

1. copy only the generator definition and parameter list;
2. add seed model and perturbation rule;
3. add a minimal deterministic test that runs without production services;
4. document output and status under `tests/` or `work/`;
5. promote only definitions or exact results to visible root files.

## CryptoVar-Aligned Track

The immediate external target is the ENINCA CryptoVar API workstream:

- seed/replay Monte Carlo bundles;
- `black_scholes_markov` and related VaR engines;
- affine-generator diagnostics with `a`, `b`, `m`, `q`, `lag`, `diagnostic_n`, and `antithetic`;
- PRNG metrics such as chi-square, p-value, PSLR/ISLR, periodogram, spectral gap, uniform-invariance deviation, total-variation bound, bridge gap, visited classes, and transition matrix;
- hash-based RNG certification for public draws.

The user reports prior substantial work with Nicolas Chopin and Lebrun. That provenance should be recorded, but any mathematical claim still needs a local definition, proof, exact enumeration, or reproducible API/test transcript before promotion.

## Immediate Next Tests

Candidate first tests:

- one-bit seed flip sensitivity for a small reference generator;
- structured seed versus uniform seed comparison;
- fixed-parameter versus parameter-grid comparison;
- reduced-state exhaustive enumeration for toy versions of the generator.
- functional variance dispersion on identity, sinusoidal, quadratic, and rare-event integrands;
- representative-seed discovery across 100 seeds;
- cross-backend replay equality manifests for CPU, Metal, and CUDA.

These tests are not yet implemented in this repository.
