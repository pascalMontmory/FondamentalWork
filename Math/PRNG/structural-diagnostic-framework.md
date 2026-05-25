# Structural Diagnostic Framework for PRNG Stability

Cross-Architecture Empirical Analysis on ARM CPU, Apple Metal and CUDA

Pascal Montmory  
ENINCA Consulting  
hello@eninca.com  
December 2025

## Status

This is a technical-note draft. It documents a diagnostic framework and reported empirical observations. Raw BigCrush logs for seed `42` are now imported for CPU ARM, Apple Metal GPU, and CUDA GPU under `tests/testu01/raw/`, with hashes in `tests/testu01/MANIFEST.md`.

The repository still does not contain the full dataset, stream adapter source, backend implementation hashes, exact build commands, SmallCrush raw logs, x86 CPU raw logs, or complete proprietary sensitivity metrics.

The proprietary generator `Montmory_CTACM` is used here only as a controlled test vehicle. The contribution claimed by this note is the structural diagnostic framework, not disclosure or validation of the proprietary generator itself.

## Abstract

This technical note introduces a structural diagnostic framework designed to evaluate seed sensitivity, functional variance dispersion, and cross-architecture reproducibility of pseudo-random number generators (PRNGs) in Monte Carlo workloads. These dimensions are largely orthogonal to classical statistical batteries such as TestU01 and PractRand. The public formulas used by the framework are collected in `formules-diagnostiques.md`.

A lightweight proprietary 64-bit PRNG, `Montmory_CTACM`, is used solely as a controlled test vehicle for the methodology. The generator itself is not the contribution of this note. Instead, the focus is the diagnostic framework and empirical comparisons across widely used PRNGs:

- MT19937;
- MT19937-64;
- PCG32;
- xoshiro256**;
- Philox4x32-10;
- MRG32k3a.

Experiments were conducted on ARM64 CPU, Apple Metal GPU, and CUDA GPU.

The proprietary nature of `Montmory_CTACM` is explicitly acknowledged. The contribution of this note lies in the diagnostic framework and the observed gaps in existing open-source generators, not the undisclosed generator itself.

Under a single-lane configuration, the prototype generator is reported to produce bit-exact outputs across CPU, Metal, and CUDA backends. Imported repository artifacts currently support the narrower statement that BigCrush seed `42` logs report `160 / 160` passed statistics on CPU ARM, Apple Metal GPU, and CUDA GPU.

Structural diagnostics reveal that popular PRNGs can exhibit one to two orders of magnitude amplification of Monte Carlo variance depending on the seed, despite all passing BigCrush. In contrast, the prototype displays significantly lower inter-seed dispersion across integrands.

These findings suggest that BigCrush sufficiency does not guarantee functional stability, and that seed sensitivity should be considered a first-class property in PRNG evaluation.

## 1. Introduction

Monte Carlo simulations rely critically on the quality and robustness of pseudo-random number generators. Classical PRNG evaluation relies on distributional statistical batteries such as TestU01 and PractRand. These tools detect statistical defects on a single infinite stream.

However, practitioners routinely observe phenomena that these batteries do not measure:

- large differences in Monte Carlo variance depending on the seed;
- backend-dependent behaviour, for example CPU versus Metal versus CUDA;
- unexplained variance amplification on practical integrands.

In this note, the term `structural stability` refers to:

- low sensitivity of Monte Carlo functional variance to the seed;
- robustness of this variance across computational backends.

This notion is unrelated to the dynamical-systems meaning of structural stability.

## 2. Diagnostic Methodology

The framework distinguishes three classes of diagnostics.

### 2.1 Distributional and Spectral Tests

Classical diagnostics include:

- chi-square uniformity;
- transition-matrix spectral-gap proxy;
- autocorrelation;
- asymptotic variance proxy.

These diagnostics remain useful, but they do not exhaust the practical stability questions encountered in Monte Carlo workloads.

### 2.2 Structural Seed-Dependent Tests

Monte Carlo variance is measured on the following integrands:

- identity;
- sinusoidal;
- quadratic;
- rare event indicator `1{u > 0.99}`.

For each PRNG:

- 100 seeds are tested;
- `N = 10^6` samples per seed;
- 8 independent replicates are used.

For exposition, this note reports minimum and maximum variances and simple dispersion ratios, `max / min`, based on five representative structural seeds per generator. The complete proprietary sensitivity metrics, including quantile-based indices and structural score functions, are intentionally not disclosed.

### 2.3 Representative Seed Selection

The five reported seeds per PRNG are not arbitrary. They are obtained through an automatic structural auto-discovery procedure over the 100 tested seeds, including seed `0` when meaningful.

For each generator, the procedure identifies:

- a default seed, usually `1`;
- a best seed, corresponding to minimum structural variance;
- a worst seed, corresponding to maximum structural variance;
- a mean seed, closest to the structural median;
- a std seed, closest to one structural standard deviation;
- and, systematically, seed `0` when applicable.

The internal scoring functions mix quadratic and rare-event variances with structural indices. They remain proprietary, but a third party should be able to reproduce similar patterns by evaluating the 100-seed variance profiles.

### 2.4 Cross-Architecture Reproducibility

Bit-exact equality of sequences is tested across:

```text
ARM64 CPU = Apple Metal GPU = CUDA GPU
```

Only the prototype generator satisfied this condition in the reported experiments.

## 3. Experimental Protocol

- `N = 10^6` samples per seed;
- 8 replicates;
- 100 seeds per PRNG, including seed `0` when meaningful;
- backends in the imported raw BigCrush logs: CPU ARM on Darwin, Apple Metal GPU on Darwin, CUDA GPU on Linux;
- x86 CPU remains a reported target, but its raw log is not yet imported;
- TestU01 SmallCrush and BigCrush are reported for the prototype; imported raw artifacts currently cover BigCrush seed `42`.

## 4. Results

### 4.1 TestU01 Cross-Architecture Logs

`Montmory_CTACM` has imported raw BigCrush logs for three execution targets:

| Backend | SmallCrush | BigCrush | Notes |
| --- | ---: | ---: | --- |
| CPU ARM, Darwin | reported pass | `160 / 160` | Raw BigCrush log imported for seed `42`. |
| Apple Metal GPU, Darwin | reported pass | `160 / 160` | Raw BigCrush log imported for seed `42`. |
| CUDA GPU, Linux | reported pass | `160 / 160` | Raw BigCrush log imported for seed `42`. |
| x86 CPU | reported pass | reported `160 / 160` | No raw x86 log imported. |

The imported logs end with `All tests were passed`. The manifest also records SHA-256 hashes, host labels, generator labels, total CPU time, and parsed p-value ranges.

These logs are repository computational evidence, but not yet a complete independent reproducibility package.

### 4.2 Mean Functional Variances

Mean functional variances are omitted in this draft and should be restored from the full measurement archive.

### 4.3 Inter-Seed Dispersion

Even with only five representative structural seeds per PRNG, the differences in dispersion are already visible. This is a deliberately conservative presentation to avoid disclosing the full proprietary sensitivity metrics.

The table below records the reported minimum and maximum empirical variances on the quadratic and rare-event integrands, along with the ratio `max / min`.

| PRNG | Backend | minVar quad | maxVar quad | ratio quad | minVar rare | maxVar rare | ratio rare |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Montmory_CTACM | CPU | `2.0e-7` | `2.1e-6` | `~10` | `1.1e-6` | `3.8e-6` | `~3.4` |
| Montmory_CTACM | GPU lane 1 | `2.0e-7` | `2.1e-6` | `~10` | `1.1e-6` | `3.8e-6` | `~3.4` |
| MT19937 | CPU | `1.3e-7` | `1.3e-6` | `~10` | `2.5e-7` | `3.5e-6` | `~14` |
| MT19937-64 | CPU | `3.4e-7` | `6.6e-7` | `~1.9` | `2.0e-7` | `4.9e-6` | `~25` |
| PCG32 | CPU | `1.4e-7` | `2.1e-6` | `~15` | `4.7e-7` | `1.5e-6` | `~3.2` |
| xoshiro256** | CPU | `2.4e-7` | `1.4e-6` | `~5.9` | `3.3e-7` | `3.5e-6` | `~10.5` |
| Philox4x32-10 | CPU | `2.4e-7` | `1.1e-6` | `~4.6` | `3.1e-7` | `3.5e-6` | `~11` |
| MRG32k3a | CPU | `1.9e-7` | `1.5e-6` | `~7.7` | `4.2e-7` | `1.6e-6` | `~3.9` |

### 4.4 Interpretation

Key observations:

- MT19937-64 and Philox show dispersion up to roughly `25x` on rare events;
- xoshiro256** shows moderate dispersion except on rare events;
- MRG32k3a exhibits high rare-event amplification despite low-variance behaviour elsewhere;
- `Montmory_CTACM` shows the lowest and most homogeneous dispersion in the reported comparison;
- CPU/GPU behaviour is identical for `Montmory_CTACM` in single-lane mode.

## 5. Conclusion

This note introduces a structural diagnostic framework that complements classical statistical test suites.

The reported experiments suggest that:

- BigCrush is necessary but not sufficient for functional stability;
- seed sensitivity can exceed two orders of magnitude depending on the functional being estimated;
- cross-architecture reproducibility is achievable but requires careful generator and backend design.

An open-source reference implementation of the diagnostic protocol, excluding the proprietary generator, is planned.

## Repository Integration Plan

To promote this note from draft to reproducible evidence, the repository should add:

- the exact seed list used for each PRNG;
- the auto-discovery rule for representative structural seeds, or a non-proprietary approximation;
- CPU, Metal, and CUDA implementation hashes;
- raw SmallCrush logs for CPU ARM, Metal, and CUDA;
- raw x86 CPU SmallCrush and BigCrush logs if x86 remains part of the public backend claim;
- stream adapter source or source hash for TestU01;
- exact build commands, compiler versions, flags, and target details;
- raw variance tables for all 100 seeds;
- a reproducible script for the four integrands;
- a verification manifest with commands and expected outputs.

## References

1. P. L'Ecuyer and R. Simard, "TestU01: A C library for empirical testing of random number generators", ACM TOMS, 33(4), 2007.
2. C. Blackman and M. Vigna, "PractRand", technical report, 2021.
3. M. Matsumoto and T. Nishimura, "Mersenne Twister", ACM TOMACS, 1998.
4. M. E. O'Neill, "PCG: A family of simple fast space-efficient statistically good RNGs", technical report, 2014.
5. M. Vigna, "Further scramblings of Marsaglia's xorshift generators", Journal of Computational and Applied Mathematics, 315, 2017.
6. J. K. Salmon, M. A. Moraes, R. O. Dror, and D. E. Shaw, "Parallel random numbers: As easy as 1,2,3", Proceedings of SC11, 2011.
7. P. L'Ecuyer, "Good parameter sets for combined multiple recursive generators", Operations Research, 47(1), 1999.
