# FondamentalWork

FondamentalWork is organized as a research workspace with explicit domains and explicit claim status.

```text
COSMO/  Fundamental physics, GUP, UV/IR, holography, cosmology, public-data tests, and sensor-oriented applications.
Math/   Reusable mathematical foundations shared with other repositories: VDF, PRNG, and Collatz-Montmory.
docs/   Repository-level structure, reading order, and workflow notes.
```

## Start Here

Read in this order:

1. [docs/RESEARCH_MAP.md](docs/RESEARCH_MAP.md) for the logic of the repository, reading path, and status levels.
2. [COSMO/README.md](COSMO/README.md) for the cosmology and fundamental-physics corpus.
3. [Math/README.md](Math/README.md) for the mathematical workstreams.
4. [docs/REPOSITORY_STRUCTURE.md](docs/REPOSITORY_STRUCTURE.md) for naming and placement rules.

## Status Legend

| Status | Meaning | Typical location |
|---|---|---|
| Verified | Proof, exact identity, or bounded reproducible computation. | Topic root |
| Conditional | Assumptions and conclusions are explicit. | Topic root or `non-validated/` |
| Non-validated | Hypothesis, draft article, candidate formula, negative diagnostic, or open program. | `non-validated/` |
| Script/work product | Reproducible diagnostic code or helper. | `work/scripts/` |
| Old/superseded | Preserved for history only. | `old/` |

## Current Layout

| Path | Role |
| --- | --- |
| `COSMO/` | Existing non-mathematical research tracks formerly located at repository root. |
| `Math/VDF/` | Notes and verification plan for verifiable-delay-function mathematics. |
| `Math/PRNG/` | Notes and verification plan for pseudo-random-number-generator work. |
| `Math/Collatz-Montmory/` | Verified-facing area for Collatz-Montmory definitions and exact/conditional results. |
| `Math/Collatz-Montmory/non-validated/` | Hypotheses, analyzed drafts, negative diagnostics, and non-verified Collatz-Montmory articles. |
| `Math/Collatz-Montmory/work/scripts/` | Reproducible exploratory scripts for Collatz-Montmory diagnostics. |
| `docs/` | Cross-repository documentation and reading guides. |

## Publication Rule

Do not publish a mathematical claim as confirmed unless it has a written proof or a reproducible computational check with stated limits. Conjectures, candidate articles, and weakened or negative diagnostics belong in clearly marked non-validated areas.
