# Montmory_CTACM Public Specification Boundary

## Status

This document defines the public, non-confidential boundary of `Montmory_CTACM` for repository discussion, review, and reproducibility planning.

It is not a full generator disclosure. The internal transition rule, extraction map, proprietary seed-discovery score, and implementation-level constants are intentionally not published here.

## Purpose in This Repository

`Montmory_CTACM` is used as a controlled test vehicle for the structural diagnostic framework described in `structural-diagnostic-framework.md`.

The repository contribution is therefore:

- the diagnostic method;
- the seed-sensitivity and functional-variance protocol;
- cross-backend reproducibility requirements;
- reproducibility scaffolding for open generators;
- reported comparison against standard PRNG families.

The proprietary generator itself is not presented as an open mathematical object.

## Public Interface

For the purposes of the diagnostic framework, `Montmory_CTACM` is treated as a deterministic PRNG with:

- fixed-width integer state;
- caller-provided seed or derived effective seed;
- deterministic transition;
- deterministic output map to unsigned integer words;
- deterministic mapping to floating-point uniforms for Monte Carlo tests;
- single-lane CPU/GPU replay mode;
- backend targets including x86 CPU, Apple Metal GPU, and CUDA GPU.

The exact public test interface should expose:

```text
init(seed) -> state_0
next_u64(state_t) -> (state_{t+1}, word_t)
uniform01(word_t) -> u_t in [0, 1)
```

Any future publication or external review should specify the bit width, output convention, and floating-point mapping used for the reported logs.

## Seed Model

The structural diagnostic framework distinguishes:

- caller seed: the seed provided by a user or test harness;
- effective seed: the seed actually used after validation or derivation;
- representative structural seeds: seeds selected by an auto-discovery procedure over a fixed seed set.

The proprietary representative-seed score is not disclosed here. The non-proprietary requirement is that a third-party implementation can reproduce a comparable 100-seed profile using the published integrands and variance measures.

## Backend Reproducibility Requirement

The public reproducibility target is bit-exact agreement in single-lane mode:

```text
x86 CPU stream = Apple Metal stream = CUDA stream
```

For a backend claim to be independently checkable, the repository should eventually include:

- backend source or implementation hash;
- compiler version;
- flags and target architecture;
- seed list;
- first output words for reference seeds;
- SHA-256 hash of generated streams;
- TestU01 command and raw logs.

## Non-Claims

This document does not claim:

- disclosure of the full generator;
- proof of period;
- proof of equidistribution;
- proof of cryptographic security;
- proof that TestU01 success implies functional stability.

The current verified public claim is limited to the existence of a documented diagnostic framework and reported empirical outcomes pending raw-log import.

## Publication Gap

For a serious external review, especially by GPU or numerical-computing teams, the open part should be extended with at least:

- reference stream hashes for fixed seeds;
- exact floating-point conversion rule;
- exact TestU01 stream adapter;
- full SmallCrush and BigCrush logs;
- non-proprietary version of the seed-sensitivity harness for open PRNGs.
