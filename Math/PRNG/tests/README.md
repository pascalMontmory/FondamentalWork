# PRNG Tests

This directory is reserved for deterministic PRNG checks.

## Reference Harness

`micro_uncertainty_reference.py` is a standalone reference harness for seed-impact and parameter-control measurements. It uses xorshift32 only as a compact deterministic example; it is not a cryptographic validation.

Run:

```bash
python3 Math/PRNG/tests/micro_uncertainty_reference.py
```

The output is JSON labelled `computational-evidence`.

## CryptoVar-Aligned Affine Harness

`affine_markov_micro_uncertainty.py` uses the affine/Markov parameter vocabulary exposed by CryptoVar-style diagnostics: `a`, `b`, `m`, `q`, `lag`, deterministic seed derivation, class counts, uniform-invariance deviation, and seed-perturbation sensitivity.

Run:

```bash
python3 Math/PRNG/tests/affine_markov_micro_uncertainty.py
```

This does not call `api.eninca.com`; it is a local scaffold for reproducing and isolating formulas before importing API transcripts.

## TestU01 Artifacts

Raw TestU01 logs are stored under `testu01/raw/`, with hashes and completeness notes in `testu01/MANIFEST.md`.

Current imported artifacts cover BigCrush seed 42 for CPU ARM, Apple Metal GPU, and CUDA GPU. SmallCrush raw logs and an x86 CPU raw log are not currently imported.

Future tests should avoid production services and external state. Each test should be runnable from a clean checkout and should print enough information to reproduce the seed model, perturbation rule, parameter values, observable, and expected output.
