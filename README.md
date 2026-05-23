# FondamentalWork

FondamentalWork is now organized as a research workspace with two explicit top-level namespaces.

```text
COSMO/  Fundamental physics, GUP, UV/IR, holography, cosmology, public-data tests, and sensor-oriented applications.
Math/   Reusable mathematical foundations shared with other repositories: VDF, PRNG, and Collatz-Montmory.
docs/   Repository-level structure and workflow notes.
```

## Research Status

The repository contains active research notes and verification material. A result should be treated as established only when the local document states its derivation, assumptions, numerical check, and reproducible script or test. Exploratory ideas should remain explicitly marked as conjectural.

## Start Here

- [COSMO/README.md](COSMO/README.md) for the cosmology and fundamental-physics corpus moved from the repository root.
- [Math/README.md](Math/README.md) for the mathematical workstreams.
- [docs/REPOSITORY_STRUCTURE.md](docs/REPOSITORY_STRUCTURE.md) for the intended layout and naming rules.

## Current Layout

| Path | Role |
| --- | --- |
| `COSMO/` | Existing non-mathematical research tracks formerly located at repository root. |
| `Math/VDF/` | Notes and verification plan for verifiable-delay-function mathematics. |
| `Math/PRNG/` | Notes and verification plan for pseudo-random-number-generator work. |
| `Math/Collatz-Montmory/` | Verified-only area for Collatz-Montmory definitions, lemmas, tests, and conjectures. |
| `docs/` | Cross-repository documentation. |

## Publication Rule

Do not publish a mathematical claim as confirmed unless it has a written proof or a reproducible computational check with stated limits. Conjectures belong in clearly named conjecture sections or files.