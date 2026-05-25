# CryptoVar API Map

Observed source: `https://api.eninca.com` and `https://api.eninca.com/landing/cookbook.html` on 2026-05-25.

This page maps the external CryptoVar surface to the local PRNG research structure. It is a provenance note, not a verification result.

## Public Claims to Reconcile

The external site presents CryptoVar as an auditable Monte Carlo and certified PRNG API with:

- deterministic replay from parameters plus seed;
- `/verify` proof for independent replay;
- API version `v0.4.5`;
- MCP adapter version `v0.2.0`;
- PRNG and VDF routes exposed through the same audited API layer.

## Seed and Replay

The cookbook states the common VaR parameters include `S0`, `sigma`, `T`, `N`, `alpha`, and `seed`.

Seed behavior to model locally:

- explicit nonzero `seed` gives reproducibility;
- absent or zero `seed` is derived with SHA-256 from inputs, reduced modulo `m-1`, then shifted by `+1`;
- the effective seed is exposed in audit metadata.

Local PRNG notes should therefore distinguish:

- caller seed;
- effective generator seed;
- derived seed rule;
- replay bundle;
- proof hash.

## Markov PRNG Track

The API exposes a Markov-style certified engine through `black_scholes_markov` and `/prng/markov`.

Declared or displayed parameters include:

- `a`: affine multiplier;
- `b`: affine increment;
- `m`: modulus;
- `q`: number of Markov/quantization classes;
- `lag`: transition lag;
- `diagnostic_n`: diagnostic sample size;
- `antithetic`: variate pairing control.

Displayed diagnostics include:

- `chi2`;
- `p_value`;
- `pslr`;
- `islr`;
- `spectral_gap`;
- `uniform_invariance_sup`;
- `tv_bound`;
- `bridge_gap`;
- `visited_classes`;
- `expected_classes`;
- `column_sums`;
- `transition`.

## PRNG Metrics Track

The cookbook exposes `/prng/metrics` for sequence-level diagnostics:

- chi-square statistic;
- p-value;
- PSLR/ISLR;
- optional periodogram.

This maps to local observables in `definitions.md` and should be tested independently on known sequences before being used as evidence for any generator.

## Gaming RNG Track

The cookbook exposes `/gaming/prng/certify` with:

- `seed`;
- `length`;
- `engine`, including `hash`;
- `hash_digest`, including `sha512`;
- `include_metrics`;
- `sequence_sample`;
- `audit_proof`.

This should be kept distinct from VaR Monte Carlo because public draw fairness has a different threat model from simulation reproducibility.

## Human Provenance

The user reports prior work with Nicolas Chopin and Lebrun on this subject. That note should be preserved as project provenance. It is not, by itself, a mathematical citation or verification artifact until linked to a paper, notebook, transcript, code version, or reproducible API output.

## Local Import Checklist

Before any CryptoVar result is promoted locally:

- capture the exact endpoint and payload;
- capture the full JSON response;
- record API version and date;
- record whether the result is from demo or professional key;
- reproduce with `/verify` when available;
- copy formulas into `definitions.md` only if they are independent of production code;
- keep empirical outcomes under `work/` or `tests/` until independently reproducible.
