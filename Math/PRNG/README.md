# PRNG

Workspace for mathematical foundations related to pseudo-random-number-generator work, with a current focus on micro-uncertainty: how small seed perturbations and controlled parameter changes propagate through a deterministic generator.

## HAL Submission

Current submitted preprint:

```text
hal-05633702v1
TACM / PRNG Structural Diagnostics
Pré-publication, Document de travail
Submitted: 2026-05-26
```

Repository copy:

```text
publication/hal/hal-05633702v1/
```

The companion reproducibility bundle for the public CPU-only baseline is:

```text
WIP/prng-ztest/
```

## Current Status

No PRNG quality, security, period, distribution, or independence theorem is marked as verified here. The material currently defines the vocabulary and research protocol for studying seed impact, parameter controls, and reproducible evidence.

Imported repository evidence currently includes raw TestU01 BigCrush logs for `Montmory_CTACM` at seed `42` on CPU ARM, Apple Metal GPU, and CUDA GPU. These logs are computational evidence artifacts, not mathematical proofs, and they are not yet a complete reproducibility package because stream adapter source, implementation hashes, build commands, SmallCrush logs, and an x86 CPU raw log are still missing.

The public NumPy CPU-only TACM baseline used in `hal-05633702v1` is reproducible from the committed scripts and summaries in `WIP/prng-ztest/`. The large seed-level CSV files are generated locally and may be archived as release artifacts rather than committed directly.

## Visible Files

| File | Status |
| --- | --- |
| `definitions.md` | Neutral definitions for PRNG state, seed models, parameter controls, and micro-uncertainty observables. |
| `formules-diagnostiques.md` | Public diagnostic formulas for seed sensitivity, functional variance, Markov diagnostics, spectral proxies, and backend reproducibility. |
| `innovations-methodologiques.md` | Concise statement of the methodological contribution and reported dispersion results. |
| `verified-results.md` | Registry separating verified definitions, imported computational artifacts, reported results, and promotion requirements. |
| `conjectures.md` | Unverified research claims and open questions. |
| `structural-diagnostic-framework.md` | Technical-note draft on seed sensitivity, functional variance dispersion, and cross-architecture reproducibility. |
| `executive-summary.md` | Short neutral summary of the framework, current evidence, and missing reproducibility artifacts. |
| `montmory-ctacm-public-spec.md` | Public non-confidential boundary for discussing the proprietary `Montmory_CTACM` test vehicle. |
| `testu01-results.md` | Imported BigCrush logs and remaining TestU01 gaps for CPU ARM, Apple Metal, CUDA, and x86. |
| `tests/testu01/MANIFEST.md` | Hashes, backend labels, summaries, and completeness assessment for imported raw TestU01 logs. |
| `publication/hal/hal-05633702v1/` | Submitted HAL manuscript, LaTeX source, and included figure renderings. |
| `WIP/prng-ztest/` | Reproducible CPU-only public-generator baseline for calibrated `Z_s` diagnostics. |

## Work Area

Exploratory material is kept in `work/`:

- micro-uncertainty analysis plan;
- candidate metrics and control protocols;
- notes imported from external API or cryptographic experiments;
- TestU01 log summaries and import checklists;
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
