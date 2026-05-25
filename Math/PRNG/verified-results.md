# PRNG Verified Results

No PRNG quality, security, period, distribution, independence, seed-impact, or parameter-robustness theorem is currently verified in this directory.

This file intentionally separates:

- verified definitions;
- reported empirical results pending raw artifact import;
- requirements for promotion to reproducible computational evidence.

## Verified Definitional Statements

The following content is verified at the level of definitions and notation:

- the abstract PRNG model `G = (S, P, A, T, O, U)`;
- the finite-window notation `X_n(p,s)` and `U_n(p,s)`;
- the distinction between caller seed, effective seed, and internal state;
- the formal perturbation map `N_delta : Seed -> P(Seed)`;
- the observable convention `Phi : A^n -> R^d` or `Phi : [0,1)^n -> R^d`;
- the distinction between parameter control, seed perturbation rule, observable, horizon, and acceptance criterion.

These are definitions, not claims that any concrete PRNG is good or secure.

## Reported Computational Results

The following results are empirical. They are not mathematical verification results. Some raw BigCrush logs are now imported, while commands, implementation hashes, stream adapter source, and complete rerun instructions remain incomplete.

### TestU01 Summary for Montmory_CTACM

| Backend | SmallCrush | BigCrush | Repository Status |
| --- | ---: | ---: | --- |
| CPU ARM, Darwin | reported pass | `160 / 160` | BigCrush raw log imported for seed 42; SmallCrush raw log pending. |
| Apple Metal GPU, Darwin | reported pass | `160 / 160` | BigCrush raw log imported for seed 42; SmallCrush raw log pending. |
| CUDA GPU, Linux | reported pass | `160 / 160` | BigCrush raw log imported for seed 42; SmallCrush raw log pending. |
| x86 CPU | reported pass | reported `160 / 160` | No raw x86 log imported. |

Imported BigCrush log manifest: `tests/testu01/MANIFEST.md`.

### Reported Inter-Seed Dispersion

Protocol summary:

- `N = 10^6` samples per seed;
- `R = 8` replicates;
- 100 tested seeds per PRNG;
- table reports representative structural seeds selected from the 100-seed profile;
- `rho_f = max_s V_s(f) / min_s V_s(f)` on the selected seed set.

| PRNG | Backend | `rho_{u^2}` | `rho_{1{u>0.99}}` | Repository Status |
| --- | --- | ---: | ---: | --- |
| Montmory_CTACM | CPU | `~10` | `~3.4` | Reported; raw table pending. |
| Montmory_CTACM | GPU lane 1 | `~10` | `~3.4` | Reported; raw table pending. |
| MT19937 | CPU | `~10` | `~14` | Reported; raw table pending. |
| MT19937-64 | CPU | `~1.9` | `~25` | Reported; raw table pending. |
| PCG32 | CPU | `~15` | `~3.2` | Reported; raw table pending. |
| xoshiro256** | CPU | `~5.9` | `~10.5` | Reported; raw table pending. |
| Philox4x32-10 | CPU | `~4.6` | `~11` | Reported; raw table pending. |
| MRG32k3a | CPU | `~7.7` | `~3.9` | Reported; raw table pending. |

### Cross-Backend Reproducibility

Reported condition for `Montmory_CTACM` in single-lane mode:

```text
stream_x86(seed) = stream_Metal(seed) = stream_CUDA(seed)
```

Repository status: reported only. Stream hashes and backend implementation hashes are pending import.

## Promotion Requirements

A result can be promoted beyond reported status only if it includes at least one of:

- a complete proof with explicit hypotheses;
- an exact finite enumeration with command, range, code version, and expected output;
- a reproducible empirical check with command, raw artifacts, implementation hash, and expected output.

For TestU01 results, promotion requires:

- full SmallCrush and BigCrush logs;
- TestU01 version;
- stream adapter source or hash;
- backend implementation hash;
- compiler and target details;
- seed and output horizon;
- SHA-256 of raw logs.

For structural dispersion results, promotion requires:

- full seed list;
- complete per-seed variance table;
- integrand definitions;
- replicate count and sample size;
- command and implementation hash;
- expected output file hash.

Statements about cryptographic security require a separate threat model. Statistical evidence alone must not be promoted to a security theorem.
