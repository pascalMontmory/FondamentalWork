# PRNG

Workspace for mathematical foundations related to pseudo-random-number-generator work, with a current focus on micro-uncertainty: how small seed perturbations and controlled parameter changes propagate through a deterministic generator.

## Current Status

No PRNG quality result is marked as verified here. The material currently defines the vocabulary and research protocol for studying seed impact, parameter controls, and reproducible evidence.

## Visible Files

| File | Status |
| --- | --- |
| `definitions.md` | Neutral definitions for PRNG state, seed models, parameter controls, and micro-uncertainty observables. |
| `formules-diagnostiques.md` | Public diagnostic formulas for seed sensitivity, functional variance, Markov diagnostics, spectral proxies, and backend reproducibility. |
| `innovations-methodologiques.md` | Concise statement of the methodological contribution and reported dispersion results. |
| `verified-results.md` | Empty verified ledger except for definitional statements. |
| `conjectures.md` | Unverified research claims and open questions. |
| `structural-diagnostic-framework.md` | Technical-note draft on seed sensitivity, functional variance dispersion, and cross-architecture reproducibility. |
| `montmory-ctacm-public-spec.md` | Public non-confidential boundary for discussing the proprietary `Montmory_CTACM` test vehicle. |
| `testu01-results.md` | Reported SmallCrush and BigCrush outcomes for x86, Apple Metal, and CUDA pending raw-log import. |

## Work Area

Exploratory material is kept in `work/`:

- micro-uncertainty analysis plan;
- candidate metrics and control protocols;
- notes imported from external API or cryptographic experiments;
- TestU01 log summaries before raw log import;
- computational evidence before promotion.

Material in `work/` is not advertised as verified.

## Tests Area

Reproducible checks belong in `tests/`. Each check should declare:

- generator definition and version;
- seed set and seed perturbation rule;
- parameter set and controlled parameter grid;
- sample size and output window;
- expected output or acceptance interval;
- command required to reproduce the result.

## Verification Rule

Empirical randomness tests are evidence, not proof. Label them as computational evidence unless a mathematical theorem is provided. A claim about seed sensitivity or parameter robustness is not verified until the assumptions, observable, range, command, and expected output are documented locally.
