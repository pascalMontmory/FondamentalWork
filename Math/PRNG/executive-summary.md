# PRNG Structural Diagnostics - Executive Summary

## Purpose

This repository section documents a structural diagnostic framework for evaluating pseudo-random-number generators in Monte Carlo workloads.

The central point is simple: passing classical statistical batteries such as TestU01 BigCrush is necessary for a serious PRNG claim, but it is not sufficient to establish functional stability in practical simulations.

The framework therefore adds three complementary diagnostics:

- seed sensitivity of Monte Carlo variance;
- functional variance dispersion across representative integrands;
- null-calibrated `Z_s = F_0(V_s)` interpretation of raw variance ratios;
- cross-backend reproducibility across CPU and GPU execution targets.

The current HAL preprint is:

```text
hal-05633702v1
TACM / PRNG Structural Diagnostics
```

## Current Repository Evidence

The repository currently contains:

- formal PRNG definitions and diagnostic formulas;
- the submitted HAL manuscript and LaTeX source in `publication/hal/hal-05633702v1/`;
- a reproducible public NumPy CPU-only baseline in `WIP/prng-ztest/`;
- reported structural dispersion tables across several PRNG families;
- raw TestU01 BigCrush logs for `Montmory_CTACM` at seed `42`;
- SHA-256 hashes and backend labels for the imported logs;
- deterministic local diagnostic harnesses for reduced reference models.

Imported BigCrush artifacts currently cover:

| Backend | Suite | Seed | Result | Manifest |
| --- | --- | ---: | --- | --- |
| CPU ARM, Darwin | BigCrush | `42` | `160 / 160`, all passed | `tests/testu01/MANIFEST.md` |
| Apple Metal GPU, Darwin | BigCrush | `42` | `160 / 160`, all passed | `tests/testu01/MANIFEST.md` |
| CUDA GPU, Linux | BigCrush | `42` | `160 / 160`, all passed | `tests/testu01/MANIFEST.md` |

These artifacts are computational evidence. They are not mathematical proofs, and they are not yet a full independent reproducibility bundle.

## Public Review Readiness

| Expected public material | Current repository status | Gap |
| --- | --- | --- |
| High-level diagnostic framework | Present in `structural-diagnostic-framework.md`, `formules-diagnostiques.md`, and this summary. | Needs final publication polish. |
| Submitted manuscript | Present in `publication/hal/hal-05633702v1/`. | HAL public validation may still be pending. |
| Public CPU null-calibrated baseline | Present in `WIP/prng-ztest/` with scripts, summaries, and SVG figures. | Full seed-level CSV files are generated locally and may be archived separately. |
| Multi-seed structural sensitivity | Present through `rho_f`, representative seed selection, and reported dispersion tables. | Some earlier raw per-seed tables are not yet imported. |
| `GSQI` and `epsilon(T)` labels | Formalized in diagnostic notes and the consolidated manuscript. | Product/API mapping can still be refined. |
| Cross-architecture BigCrush logs | Imported for CPU ARM, Metal, and CUDA at seed `42`. | SmallCrush logs and x86 CPU raw logs are still missing. |
| Bit-exact reproducibility | Defined as a requirement. | Stream hashes or replay proofs are not yet imported. |
| Performance versus Philox4x32-10 | Philox appears in structural-dispersion comparisons. | Throughput benchmark tables and benchmark commands are not yet imported. |
| Non-proprietary technical documentation | Public boundary is documented without recurrence details. | A reproducibility bundle is still needed for external technical review. |

## Methodological Contribution

Classical batteries evaluate whether a stream exhibits statistical defects under a fixed test suite. The proposed structural framework asks a different question:

```text
Does Monte Carlo performance remain stable when the seed, integrand,
and backend are varied?
```

For an integrand `f`, seed `s`, sample count `N`, and replicate count `R`, the framework measures:

```text
I_{s,r}(f) = (1/N) sum_{t=1}^N f(u_{s,r,t})
```

and the seed-conditioned empirical variance:

```text
V_s(f) = (1/(R-1)) sum_{r=1}^R (I_{s,r}(f) - mean_r I_{s,r}(f))^2
```

The inter-seed dispersion ratio is:

```text
rho_f = max_s V_s(f) / min_s V_s(f)
```

Large `rho_f` values indicate that Monte Carlo variance depends materially on the seed, even when the generator passes distributional tests.

The consolidated manuscript refines this interpretation. Raw `rho_f` values are alerts, not final evidence. For a null model with

```text
T_s(f) = (R - 1) V_s(f) / (sigma_f^2 / N),
```

the calibrated diagnostic is:

```text
Z_s(f) = F_{chi^2_{R-1}}(T_s(f)).
```

Under the null model, `Z_s(f)` should be approximately uniform. The repository classifies outcomes as `compatible`, `calibration_drift`, or `tail_anomaly`.

## Reported Structural Findings

The reported protocol uses:

- `N = 10^6` samples per seed;
- `R = 8` replicates;
- 100 seeds per generator;
- representative structural seeds selected from the 100-seed profile;
- integrands including identity, sinusoidal, quadratic, and rare-event indicators.

Reported dispersion values show that common PRNGs can exhibit significant raw seed-dependent variance amplification, especially on rare events. The consolidated HAL manuscript adds the calibrated `Z_s` layer to avoid over-interpreting raw max/min ratios. The comparative table is maintained in `verified-results.md` and remains labelled as reported until raw per-seed tables are imported.

## What Is Still Missing

The current repository is strong enough to support a focused technical discussion, but not yet a complete reproducibility claim.

Missing items:

- raw SmallCrush logs for CPU ARM, Metal, and CUDA;
- raw x86 CPU logs if x86 remains part of the public backend claim;
- stream adapter source or source hash for TestU01;
- backend implementation hashes;
- compiler versions, flags, target hardware, and exact run commands;
- raw stream hashes proving bit-exact cross-backend equality;
- full per-seed structural variance tables;
- optional archive artifacts for the generated `prng-ztest` seed-level CSV files;
- a replay script that validates expected hashes and summaries from a clean checkout.

## Recommended Next Step

The next useful milestone is an open reproducibility bundle that excludes proprietary generator internals but includes:

- TestU01 adapter source or hash;
- fixed-seed stream hashes;
- raw SmallCrush and BigCrush artifacts;
- command lines and environment metadata;
- open-generator structural dispersion harness and expected outputs.

That bundle would make the methodology reviewable by external GPU, numerical-computing, and Monte Carlo engineering teams without requiring disclosure of the proprietary generator.
